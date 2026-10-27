#!/usr/bin/env python3
"""Verify scholarly references against registries before they are cited.

Checks, per reference:
  - the DOI resolves (Crossref, then doi.org content negotiation for DataCite
    DOIs such as arXiv/Zenodo);
  - the registry title / first author / year match what the citation claims
    (catches real-DOI-wrong-paper mis-attribution);
  - retractions, withdrawals, expressions of concern and corrections
    (Crossref `updated-by`, which includes Retraction Watch data);
  - whether a cited DOI is itself a notice rather than the article;
  - preprints that now have a published version (bioRxiv/medRxiv API,
    Crossref `is-preprint-of`, arXiv `arxiv:doi`);
  - for entries without a DOI, the best Crossref title match (a candidate to
    confirm, never an automatic fix).
With a .bib file it also runs offline hygiene checks (duplicate keys/DOIs,
malformed DOIs, missing required fields).

Usage:
  verify_refs.py refs.bib                 # check every entry
  verify_refs.py refs.bib --offline       # hygiene checks only, no network
  verify_refs.py --doi 10.1038/nature04586 --doi 10.1101/2020.03.22.002386
  verify_refs.py --title "Folding DNA to create nanoscale shapes and patterns"
  add --json for machine-readable output.

Exit status: 0 no blocking problems; 1 at least one entry is NOT_FOUND,
MISMATCH, RETRACTED or ERROR (registry unreachable, so unverified), or the
.bib has a blocking hygiene error; 2 usage error.

Standard library only; no API key or account is needed. Network mode sends
DOIs, arXiv ids, titles and first-author family names to public registries
(api.crossref.org, doi.org, api.biorxiv.org, export.arxiv.org). Nothing is
written to disk. Optionally set the CROSSREF_MAILTO environment variable to
an address you choose to join Crossref's polite pool; no address is sent
otherwise.
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

# Registry calls are small JSON lookups; 20 s tolerates slow responses without
# hanging a run for long.
TIMEOUT_S = 20
# Two retries on 429/5xx: most transient registry failures clear by then.
MAX_RETRIES = 2
# Pause between registry calls; keeps sequential runs well under Crossref's
# public-pool rate limit.
PAUSE_S = 0.25
# Title similarity (0-1, after normalisation). >= MATCH is the same title;
# between CLOSE and MATCH usually means subtitle/punctuation drift worth a look;
# below CLOSE the DOI almost certainly points at a different work.
TITLE_MATCH = 0.90
TITLE_CLOSE = 0.75
# Online-first vs issue year commonly differ by one.
YEAR_TOLERANCE = 1

# bioRxiv/medRxiv DOI prefixes: legacy CSHL 10.1101 and openRxiv 10.64898.
RXIV_PREFIXES = ("10.1101/", "10.64898/")
RETRACTION_TYPES = {"retraction", "partial_retraction", "withdrawal", "removal"}
CONCERN_TYPES = {"expression_of_concern"}
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})(v\d+)?", re.I)
REQUIRED_FIELDS = {
    "article": ["author", "title", "journal", "year"],
    "inproceedings": ["author", "title", "booktitle", "year"],
    "incollection": ["author", "title", "booktitle", "year"],
    "book": ["title", "publisher", "year"],
    "phdthesis": ["author", "title", "school", "year"],
}
PREPRINT_VENUES = ("biorxiv", "medrxiv", "arxiv", "chemrxiv", "research square", "ssrn", "preprints.org")


# ----------------------------------------------------------------------------
# HTTP


def _user_agent() -> str:
    mailto = os.environ.get("CROSSREF_MAILTO", "").strip()
    base = ("scientific-writing-skills verify_refs.py "
            "(+https://github.com/Antimonyleo/scientific-writing-skills)")
    return f"{base} (mailto:{mailto})" if mailto else base


def http_get(url: str, accept: str = "application/json") -> tuple[int | None, str]:
    """Return (status, body). status None means a network failure."""
    req = urllib.request.Request(url, headers={"User-Agent": _user_agent(), "Accept": accept})
    for attempt in range(MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
                body = resp.read().decode("utf-8", errors="replace")
            time.sleep(PAUSE_S)
            return resp.status, body
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt < MAX_RETRIES:
                time.sleep(2 ** (attempt + 1))
                continue
            return exc.code, ""
        except Exception:  # DNS, timeout, TLS
            if attempt < MAX_RETRIES:
                time.sleep(2 ** (attempt + 1))
                continue
            return None, ""
    return None, ""


def get_json(url: str, accept: str = "application/json") -> tuple[int | None, dict | None]:
    status, body = http_get(url, accept)
    if status == 200 and body:
        try:
            return status, json.loads(body)
        except json.JSONDecodeError:
            return status, None
    return status, None


# ----------------------------------------------------------------------------
# Normalisation helpers

_LATEX_ACCENT = re.compile(r"\\[`'^\"~=.uvHtcdbk]\s*\{?([A-Za-z])\}?")
_LATEX_CMD = re.compile(r"\\[A-Za-z]+\s*")


def delatex(text: str) -> str:
    text = _LATEX_ACCENT.sub(r"\1", text)
    text = _LATEX_CMD.sub(" ", text)
    return text.replace("{", "").replace("}", "").replace("~", " ")


def fold(text: str) -> str:
    text = unicodedata.normalize("NFKD", delatex(text or ""))
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"<[^>]+>", " ", text)  # JATS/MathML tags in Crossref titles
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def title_similarity(a: str, b: str) -> float:
    fa, fb = fold(a), fold(b)
    if not fa or not fb:
        return 0.0
    # A citation that drops or adds a subtitle is still the same work.
    if fa.startswith(fb) or fb.startswith(fa):
        if min(len(fa), len(fb)) >= 20:
            return max(0.95, difflib.SequenceMatcher(None, fa, fb).ratio())
    return difflib.SequenceMatcher(None, fa, fb).ratio()


def clean_doi(raw: str) -> str:
    doi = (raw or "").strip()
    doi = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I)
    return doi.strip().rstrip(".")


def first_author_family(author_field: str) -> str:
    """First author's family name from a BibTeX author string."""
    if not author_field:
        return ""
    first = re.split(r"\s+and\s+", delatex(author_field).strip(), maxsplit=1)[0].strip()
    if "," in first:
        return first.split(",")[0].strip()
    parts = first.split()
    return parts[-1] if parts else ""


def same_family(a: str, b: str) -> bool:
    """Family names match, tolerating compound names ('Kumar' vs 'Sudheesh Kumar')."""
    ta, tb = fold(a).split(), fold(b).split()
    if not ta or not tb:
        return True
    return ta == tb or set(ta) <= set(tb) or set(tb) <= set(ta)


def year_of(date_obj: dict | None) -> int | None:
    try:
        return int(date_obj["date-parts"][0][0])  # type: ignore[index]
    except Exception:
        return None


# ----------------------------------------------------------------------------
# BibTeX parsing (sufficient for verification; not a full BibTeX implementation)


def parse_bibtex(text: str) -> list[dict]:
    entries: list[dict] = []
    i = 0
    while True:
        at = text.find("@", i)
        if at < 0:
            break
        m = re.match(r"@\s*([A-Za-z]+)\s*([({])", text[at:])
        if not m:
            i = at + 1
            continue
        etype = m.group(1).lower()
        open_ch = m.group(2)
        close_ch = "}" if open_ch == "{" else ")"
        start = at + m.end()
        depth, j = 1, start
        while j < len(text) and depth:
            if text[j] == open_ch:
                depth += 1
            elif text[j] == close_ch:
                depth -= 1
            j += 1
        body = text[start : j - 1]
        i = j
        if etype in ("comment", "string", "preamble"):
            continue
        line = text.count("\n", 0, at) + 1
        if depth:
            entries.append({"_type": etype, "_key": "", "_line": line, "_error": "unbalanced braces"})
            continue
        key, _, rest = body.partition(",")
        entry = {"_type": etype, "_key": key.strip(), "_line": line}
        entry.update(_parse_fields(rest))
        entries.append(entry)
    return entries


def _parse_fields(body: str) -> dict:
    fields: dict[str, str] = {}
    pos = 0
    while pos < len(body):
        m = re.compile(r"\s*([A-Za-z][\w\-:.]*)\s*=\s*").match(body, pos)
        if not m:
            nxt = body.find(",", pos)
            if nxt < 0:
                break
            pos = nxt + 1
            continue
        name = m.group(1).lower()
        pos = m.end()
        parts: list[str] = []
        while pos < len(body):
            ch = body[pos]
            if ch == "{":
                depth, k = 1, pos + 1
                while k < len(body) and depth:
                    depth += {"{": 1, "}": -1}.get(body[k], 0)
                    k += 1
                parts.append(body[pos + 1 : k - 1])
                pos = k
            elif ch == '"':
                k = pos + 1
                depth = 0
                while k < len(body) and not (body[k] == '"' and depth == 0):
                    depth += {"{": 1, "}": -1}.get(body[k], 0)
                    k += 1
                parts.append(body[pos + 1 : k])
                pos = k + 1
            else:
                mm = re.compile(r"[^,#}\s]+").match(body, pos)
                if mm:
                    parts.append(mm.group(0))
                    pos = mm.end()
            ws = re.compile(r"\s*#\s*").match(body, pos)
            if ws:
                pos = ws.end()
                continue
            break
        fields[name] = re.sub(r"\s+", " ", "".join(parts)).strip()
        comma = body.find(",", pos)
        pos = len(body) if comma < 0 else comma + 1
    return fields


def hygiene(entries: list[dict]) -> list[dict]:
    """Offline checks. Returns issues with severity error|warn."""
    issues: list[dict] = []
    seen_keys: dict[str, int] = {}
    seen_dois: dict[str, str] = {}
    for e in entries:
        key = e.get("_key") or f"<line {e['_line']}>"
        if e.get("_error"):
            issues.append({"key": key, "severity": "error", "issue": e["_error"]})
            continue
        if key in seen_keys:
            issues.append({"key": key, "severity": "error", "issue": f"duplicate citation key (first at line {seen_keys[key]})"})
        seen_keys.setdefault(key, e["_line"])
        raw_doi = e.get("doi", "")
        if raw_doi:
            doi = clean_doi(raw_doi)
            if doi != raw_doi.strip():
                issues.append({"key": key, "severity": "warn", "issue": f"doi field should be bare DOI: use '{doi}'"})
            if not DOI_RE.match(doi):
                issues.append({"key": key, "severity": "error", "issue": f"malformed DOI '{raw_doi}'"})
            low = doi.lower()
            if low in seen_dois:
                issues.append({"key": key, "severity": "warn", "issue": f"same DOI as '{seen_dois[low]}' (duplicate entry?)"})
            seen_dois.setdefault(low, key)
        for field in REQUIRED_FIELDS.get(e["_type"], []):
            if not e.get(field):
                issues.append({"key": key, "severity": "warn", "issue": f"@{e['_type']} missing '{field}'"})
        venue = (e.get("journal", "") + " " + e.get("publisher", "") + " " + e.get("howpublished", "")).lower()
        if e.get("eprint") or e.get("archiveprefix") or any(v in venue for v in PREPRINT_VENUES):
            issues.append({"key": key, "severity": "info", "issue": "preprint: check for a published version"})
    return issues


# ----------------------------------------------------------------------------
# Registry lookups


def crossref_work(doi: str) -> tuple[str, dict | None]:
    status, data = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/:;()"))
    if status == 200 and data:
        return "crossref", data.get("message")
    if status is None:
        return "network_error", None
    # Not a Crossref DOI (DataCite: arXiv, Zenodo, figshare...) or nonexistent.
    status, csl = get_json("https://doi.org/" + urllib.parse.quote(doi, safe="/:;()"),
                           accept="application/vnd.citationstyles.csl+json")
    if status == 200 and csl:
        return "doi.org", csl
    if status is None:
        return "network_error", None
    return "not_found", None


def normalise_record(msg: dict) -> dict:
    title = msg.get("title")
    if isinstance(title, list):
        title = title[0] if title else ""
    container = msg.get("container-title")
    if isinstance(container, list):
        container = container[0] if container else ""
    authors = msg.get("author") or []
    family = ""
    if authors:
        family = authors[0].get("family") or authors[0].get("literal") or authors[0].get("name") or ""
    year = None
    for k in ("issued", "published", "published-print", "published-online", "posted", "created"):
        year = year_of(msg.get(k))
        if year:
            break
    institution = msg.get("institution")
    if not container and isinstance(institution, list) and institution:
        container = institution[0].get("name", "")  # e.g. bioRxiv posted-content
    return {
        "title": re.sub(r"\s+", " ", title or "").strip(),
        "first_author": family,
        "year": year,
        "venue": container or msg.get("publisher", ""),
        "type": msg.get("type", ""),
        "doi": msg.get("DOI") or msg.get("doi") or "",
    }


def published_version(doi: str, msg: dict) -> str | None:
    for rel in (msg.get("relation") or {}).get("is-preprint-of", []) or []:
        if rel.get("id-type") == "doi":
            return rel.get("id")
    inst = " ".join(i.get("name", "") for i in msg.get("institution") or []).lower()
    is_rxiv = doi.lower().startswith(RXIV_PREFIXES) or "openrxiv" in (msg.get("publisher") or "").lower()
    if is_rxiv and msg.get("type") == "posted-content":
        servers = ("medrxiv", "biorxiv") if "medrxiv" in inst else ("biorxiv", "medrxiv")
        for server in servers:
            status, data = get_json(f"https://api.biorxiv.org/details/{server}/{doi}")
            coll = (data or {}).get("collection") or []
            if coll:
                pub = coll[-1].get("published")
                return pub if pub and pub != "NA" else None
    m = re.match(r"10\.48550/arxiv\.(.+)$", doi, re.I)
    if m:
        return arxiv_published_doi(m.group(1))
    return None


def arxiv_lookup(arxiv_id: str) -> dict | None:
    status, body = http_get("https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(arxiv_id),
                            accept="application/atom+xml")
    if status != 200 or not body:
        return None
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    try:
        entry = ET.fromstring(body).find("a:entry", ns)
    except ET.ParseError:
        return None
    if entry is None or entry.find("a:title", ns) is None:
        return None
    title = re.sub(r"\s+", " ", entry.findtext("a:title", "", ns)).strip()
    if not title or title.lower() == "error":
        return None
    author = entry.findtext("a:author/a:name", "", ns).split()
    return {
        "title": title,
        "first_author": author[-1] if author else "",
        "year": int(entry.findtext("a:published", "0000", ns)[:4] or 0) or None,
        "venue": "arXiv",
        "type": "preprint",
        "doi": f"10.48550/arXiv.{arxiv_id}",
        "published_doi": entry.findtext("x:doi", "", ns) or None,
    }


def arxiv_published_doi(arxiv_id: str) -> str | None:
    rec = arxiv_lookup(arxiv_id)
    return rec.get("published_doi") if rec else None


SEARCH_TYPES = ("journal-article", "proceedings-article", "posted-content", "book-chapter",
                "book", "monograph", "edited-book", "report", "dissertation", "reference-entry")


def crossref_search(title: str, author: str = "") -> list[dict]:
    q = [("query.bibliographic", title), ("rows", "10"),
         # Same-name filters are OR'ed by Crossref. Restricting to citable work
         # types keeps PDB/dataset/supplement records that reuse an article's
         # title from crowding out the article itself.
         ("filter", ",".join("type:" + t for t in SEARCH_TYPES))]
    if author:
        q.append(("query.author", author))
    status, data = get_json("https://api.crossref.org/works?" + urllib.parse.urlencode(q))
    items = ((data or {}).get("message") or {}).get("items") or []
    return [dict(normalise_record(it), _msg=it) for it in items]


# ----------------------------------------------------------------------------
# Verification


def find_published_by_title(preprint: dict) -> dict | None:
    """Best-effort: a journal/proceedings record with the preprint's title and first author."""
    if not preprint.get("title"):
        return None
    for hit in crossref_search(preprint["title"], preprint.get("first_author", "")):
        if hit.get("type") not in ("journal-article", "proceedings-article"):
            continue
        if title_similarity(preprint["title"], hit["title"]) >= TITLE_MATCH and same_family(
                preprint.get("first_author", ""), hit.get("first_author", "")):
            return hit
    return None


NON_ARTICLE_TYPES = {"dataset", "component", "peer-review", "grant", "standard", "other"}


def rank_hit(claimed: dict, hit: dict) -> float:
    """Title similarity, nudged toward the right year/author and away from
    datasets or PDB/supplement records that reuse the article title."""
    score = title_similarity(claimed["title"], hit["title"])
    if claimed.get("year") and hit.get("year"):
        try:
            if abs(int(claimed["year"]) - int(hit["year"])) <= YEAR_TOLERANCE:
                score += 0.05
        except ValueError:
            pass
    if claimed.get("first_author") and hit.get("first_author") and same_family(claimed["first_author"], hit["first_author"]):
        score += 0.03
    if hit.get("type") in NON_ARTICLE_TYPES:
        score -= 0.10
    return score


def compare(claimed: dict, found: dict, result: dict) -> None:
    if claimed.get("title"):
        sim = title_similarity(claimed["title"], found["title"])
        result["title_similarity"] = round(sim, 2)
        if sim < TITLE_CLOSE:
            result["problems"].append(f"title mismatch: registry has '{found['title']}'")
        elif sim < TITLE_MATCH:
            result["notes"].append(f"title differs slightly: registry has '{found['title']}'")
    if claimed.get("first_author") and found.get("first_author"):
        if not same_family(claimed["first_author"], found["first_author"]):
            result["problems"].append(
                f"first author mismatch: cited '{claimed['first_author']}', registry '{found['first_author']}'")
    if claimed.get("year") and found.get("year"):
        try:
            diff = abs(int(claimed["year"]) - int(found["year"]))
        except ValueError:
            diff = 0
        if diff > YEAR_TOLERANCE:
            result["problems"].append(f"year mismatch: cited {claimed['year']}, registry {found['year']}")
        elif diff:
            result["notes"].append(f"year off by one (online vs print?): registry {found['year']}")


def check_updates(msg: dict, result: dict) -> None:
    title = (msg.get("title") or [""])[0] if isinstance(msg.get("title"), list) else msg.get("title") or ""
    for upd in msg.get("updated-by") or []:
        utype = (upd.get("type") or "").lower()
        label = f"{utype} ({upd.get('source', '?')}, notice {upd.get('DOI', '?')})"
        if utype in RETRACTION_TYPES:
            result["flags"].append("RETRACTED")
            result["problems"].append("retracted/withdrawn: " + label)
        elif utype in CONCERN_TYPES:
            result["flags"].append("CONCERN")
            result["notes"].append("expression of concern: " + label)
        elif utype:
            result["notes"].append("has update: " + label)
    if re.match(r"^\s*(retracted|withdrawn)\b", title, re.I):
        if "RETRACTED" not in result["flags"]:
            result["flags"].append("RETRACTED")
            result["problems"].append("title marked as retracted/withdrawn")
    if msg.get("update-to"):
        kinds = sorted({(u.get("type") or "?") for u in msg["update-to"]})
        result["problems"].append(f"this DOI is a notice ({', '.join(kinds)}), not the original article")


def verify(claimed: dict) -> dict:
    result = {
        "key": claimed.get("key", ""),
        "claimed": {k: claimed.get(k) for k in ("title", "first_author", "year", "doi", "arxiv") if claimed.get(k)},
        "status": "OK",
        "flags": [],
        "problems": [],
        "notes": [],
    }
    doi = clean_doi(claimed.get("doi", ""))
    arxiv_id = claimed.get("arxiv", "")
    found = None
    msg: dict = {}

    if doi:
        if not DOI_RE.match(doi):
            result.update(status="NOT_FOUND")
            result["problems"].append(f"malformed DOI '{doi}'")
            return result
        source, msg = crossref_work(doi)
        if source == "network_error":
            result.update(status="ERROR")
            result["problems"].append("registry unreachable; not verified")
            return result
        if source == "not_found":
            result.update(status="NOT_FOUND")
            result["problems"].append(f"DOI {doi} does not resolve in Crossref or doi.org")
            return result
        found = normalise_record(msg or {})
        result["source"] = source
    elif arxiv_id:
        found = arxiv_lookup(arxiv_id)
        if not found:
            result.update(status="NOT_FOUND")
            result["problems"].append(f"arXiv:{arxiv_id} not found")
            return result
        result["source"] = "arxiv"
        result["flags"].append("PREPRINT")
        if not found.get("published_doi"):
            guess = find_published_by_title(found)
            if guess:
                result["notes"].append(
                    f"arXiv lists no journal DOI; possible published version doi:{guess['doi']} "
                    f"({guess['venue']}, {guess['year']}) - confirm before citing")
            else:
                result["notes"].append("arXiv preprint; no published version found (arXiv DOI field empty, no Crossref title match)")
        if found.get("published_doi"):
            result["published_version"] = found["published_doi"]
    elif claimed.get("title"):
        hits = crossref_search(claimed["title"], claimed.get("first_author", ""))
        best = max(hits, key=lambda h: rank_hit(claimed, h), default=None)
        if not best or title_similarity(claimed["title"], best["title"]) < TITLE_MATCH:
            result.update(status="NOT_FOUND")
            result["problems"].append(
                "no confident Crossref match (books, theses, some proceedings and arXiv-only papers are "
                "not in Crossref; verify another way before treating as fabricated)")
            if best:
                result["notes"].append(f"nearest: '{best['title']}' doi:{best['doi']}")
            return result
        found, msg = {k: v for k, v in best.items() if k != "_msg"}, best["_msg"]
        result["source"] = "crossref-search"
        result["flags"].append("CANDIDATE")
        result["notes"].append(f"no DOI given; best match doi:{found['doi']} (confirm before adding)")
    else:
        result.update(status="ERROR")
        result["problems"].append("nothing to verify (no DOI, arXiv id or title)")
        return result

    result["found"] = {k: found.get(k) for k in ("title", "first_author", "year", "venue", "type", "doi")}
    compare(claimed, found, result)
    if msg:
        check_updates(msg, result)
        if found.get("type") in ("posted-content",) or (found.get("doi") or "").lower().startswith("10.48550/"):
            result["flags"].append("PREPRINT")
            pub = published_version(found.get("doi") or doi, msg)
            if pub:
                result["published_version"] = pub
            else:
                result["notes"].append("preprint; no published version found by the registry")
    if result.get("published_version"):
        if "PREPRINT" not in result["flags"]:
            result["flags"].append("PREPRINT")
        result["notes"].append(f"published version: doi:{result['published_version']}")

    if "RETRACTED" in result["flags"]:
        result["status"] = "RETRACTED"
    elif any(p.startswith(("title mismatch", "first author", "year mismatch", "this DOI is a notice")) for p in result["problems"]):
        result["status"] = "MISMATCH"
    elif "CANDIDATE" in result["flags"]:
        result["status"] = "CANDIDATE"
    elif result["flags"] or result["notes"]:
        result["status"] = "CHECK"
    return result


def claimed_from_bib(e: dict) -> dict:
    arxiv = ""
    if (e.get("archiveprefix", "").lower() == "arxiv" or "arxiv" in e.get("journal", "").lower()) and e.get("eprint"):
        arxiv = e["eprint"]
    elif not e.get("doi"):
        m = re.search(r"arxiv\.org/abs/" + ARXIV_RE.pattern, e.get("url", ""), re.I)
        if m:
            arxiv = m.group(1)
    if arxiv:
        arxiv = re.sub(r"v\d+$", "", arxiv.strip())
    return {
        "key": e.get("_key", ""),
        "title": delatex(e.get("title", "")).strip(),
        "first_author": first_author_family(e.get("author", "")),
        "year": re.sub(r"\D", "", e.get("year", ""))[:4],
        "doi": e.get("doi", ""),
        "arxiv": arxiv,
    }


# ----------------------------------------------------------------------------
# Output


def render_markdown(results: list[dict], issues: list[dict]) -> str:
    out: list[str] = []
    if issues:
        out.append("## BibTeX hygiene\n")
        out.append("| key | severity | issue |\n|---|---|---|")
        for i in issues:
            out.append(f"| {i['key']} | {i['severity']} | {i['issue']} |")
        out.append("")
    if results:
        counts: dict[str, int] = {}
        for r in results:
            counts[r["status"]] = counts.get(r["status"], 0) + 1
        out.append("## Registry verification\n")
        out.append("Summary: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())) + "\n")
        out.append("| key / input | status | flags | details |\n|---|---|---|---|")
        for r in results:
            label = r["key"] or r["claimed"].get("doi") or r["claimed"].get("arxiv") or (r["claimed"].get("title", "")[:50])
            details = "; ".join(r["problems"] + r["notes"]).replace("|", "/") or "matches registry"
            out.append(f"| {label} | {r['status']} | {' '.join(sorted(set(r['flags'])))} | {details} |")
    return "\n".join(out) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("bib", nargs="?", help="BibTeX file to check")
    p.add_argument("--doi", action="append", default=[], help="DOI to check (repeatable)")
    p.add_argument("--arxiv", action="append", default=[], help="arXiv id to check (repeatable)")
    p.add_argument("--title", action="append", default=[], help="title to look up when no DOI is known (repeatable)")
    p.add_argument("--pair", nargs=2, action="append", default=[], metavar=("DOI", "TITLE"),
                   help="check that DOI belongs to the paper with TITLE (repeatable)")
    p.add_argument("--keys", help="comma-separated citation keys: only check these entries of the .bib")
    p.add_argument("--offline", action="store_true", help="BibTeX hygiene only; no network")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args(argv)

    if not (args.bib or args.doi or args.arxiv or args.title or args.pair):
        p.error("give a .bib file or at least one --doi/--arxiv/--title/--pair")

    claims: list[dict] = []
    issues: list[dict] = []
    if args.bib:
        try:
            with open(args.bib, encoding="utf-8", errors="replace") as fh:
                entries = parse_bibtex(fh.read())
        except OSError as exc:
            p.error(f"cannot read {args.bib}: {exc}")
        if args.keys:
            wanted = {k.strip() for k in args.keys.split(",") if k.strip()}
            entries = [e for e in entries if e.get("_key") in wanted]
            missing = wanted - {e.get("_key") for e in entries}
            for k in sorted(missing):
                issues.append({"key": k, "severity": "error", "issue": "key not found in .bib"})
        issues += hygiene(entries)
        claims += [claimed_from_bib(e) for e in entries if not e.get("_error")]
    claims += [{"doi": d} for d in args.doi]
    claims += [{"arxiv": a} for a in args.arxiv]
    claims += [{"title": t} for t in args.title]
    claims += [{"doi": d, "title": t} for d, t in args.pair]

    results = [] if args.offline else [verify(c) for c in claims]

    if args.json:
        print(json.dumps({"hygiene": issues, "results": results}, indent=2, ensure_ascii=False))
    else:
        sys.stdout.write(render_markdown(results, issues))
        if args.offline:
            print(f"Offline mode: {len(claims)} entries parsed; registry checks skipped.")

    blocking = any(r["status"] in ("NOT_FOUND", "MISMATCH", "RETRACTED", "ERROR") for r in results)
    blocking |= any(i["severity"] == "error" for i in issues)
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
