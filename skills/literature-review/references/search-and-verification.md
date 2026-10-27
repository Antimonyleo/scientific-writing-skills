# Searching and reference verification

Use for a substantial search, a search log, or checking references before delivery. A single citation check needs only the verification section.

## Plan and test the search

- Build concept blocks: synonyms joined by OR within a block, blocks joined by AND. Avoid NOT, which silently drops relevant records; each added block lowers recall.
- Cover variants: abbreviations, hyphenation (cryo-EM, cryoEM), older terminology, spelling variants, plurals or truncation, and controlled vocabulary such as MeSH where the index has it. Missing spellings are a common cause of low recall.
- Define "recent" as an explicit date window and record it.
- Seed check: name a few papers a correct search must return, from the user, their library, or a recent review. If the search misses one, inspect its title, abstract, and keywords for the missing vocabulary and revise. If no seeds exist, say so; after screening, check whether each search alone recovers the included papers.
- For substantial work, query at least two complementary indexes. Use general web search for discovery, then resolve each candidate at a DOI record, index, or publisher page.
- Chase citations backward (reference lists) and forward (citing works) from key included papers spread across groups and years. Stop when a round adds no new includes, and report the start set and rounds.
- De-duplicate by DOI, then by normalized title and year. A preprint and its journal version are one study; cite the published version and note the preprint.

## Search log

Deliver the log with the results when the search is substantial:

| Source | Exact query or seed | Filters and date window | Date run | Hits | New after de-duplication | Included | Notes (failed or revised queries) |
| --- | --- | --- | --- | --- | --- | --- | --- |

Record reasons for full-text exclusions. Report counts only from actual results; leave a cell blank rather than estimating it.

## Optional free services

These help when the host has shell and network access; none is required. Do not register accounts, request API keys, or send the user's email address to any service unless the user asks, even when an API response invites it. Keys the user has already set in the environment may be used. Respect published rate limits. Endpoints change; if a call fails or behaves unexpectedly, check the service's current documentation. Conventions below were checked on October 26, 2026.

| Service | Use | Pattern |
| --- | --- | --- |
| Crossref | DOI metadata, title lookup, retraction and correction notices | `https://api.crossref.org/works/{doi}`; `https://api.crossref.org/works?query.bibliographic=...&rows=10`. Confirm title-search hits; the top result can be a related record |
| doi.org | DataCite DOIs, including arXiv | Request `https://doi.org/{doi}` with `Accept: application/vnd.citationstyles.csl+json` |
| OpenAlex | Topic search; forward and backward citations | `https://api.openalex.org/works?search.title_and_abstract=...`; `filter=cites:{OpenAlex ID}` for citing works; the `referenced_works` field for references. Keyless use draws on a small shared daily budget |
| Europe PMC | Open-access full text | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&format=json` returns a `pmcid` when available; then `.../rest/{PMCID}/fullTextXML`. Only part of the literature is covered, and requests can fail |
| PubMed E-utilities | Biomedical search and abstracts | `esearch.fcgi` then `efetch.fcgi`; no more than three requests per second without a key |
| arXiv | Preprint metadata and search | `https://export.arxiv.org/api/query?id_list=...`; one request every three seconds |
| bioRxiv/medRxiv | Preprint metadata and published-version DOI | `https://api.biorxiv.org/details/{server}/{doi}`, field `published` |

## Verify references before delivering

When Python 3 and network access are available, run the bundled verifier on the references you are about to deliver; it uses only the standard library and sends DOIs, titles, and first-author names to the public registries above:

```bash
python3 <skill-dir>/scripts/verify_refs.py refs.bib            # --keys k1,k2 checks a subset
python3 <skill-dir>/scripts/verify_refs.py --pair DOI "Title as cited"
python3 <skill-dir>/scripts/verify_refs.py --doi DOI --arxiv ID --title "Title"
python3 <skill-dir>/scripts/verify_refs.py refs.bib --offline  # BibTeX hygiene only
```

It checks that each DOI resolves, that the registry title, first author, and year match the citation, whether Crossref records a retraction, withdrawal, correction, or expression of concern, whether the cited DOI is itself a notice, and whether a bioRxiv, medRxiv, or arXiv preprint has a recorded published version. A title-only lookup returns a candidate, never an automatic fix. The script never edits files. Setting `CROSSREF_MAILTO` is optional.

Act on each status, then rerun until every remaining flag is explained:

- `NOT_FOUND`: find the real source or drop the claim. Books, theses, and some proceedings are not in Crossref; confirm them another way before calling them fabricated.
- `MISMATCH`: the DOI belongs to another work, or to a notice. Correct the identifier or the citation.
- `RETRACTED`: do not use the work as support; mention it only as retracted and tell the user.
- `CHECK`: read the note (published version, correction, expression of concern, one-year offset) and act on it.
- `CANDIDATE`: confirm the suggested DOI is the intended work before adding it.
- `ERROR`: the registry was unreachable; the reference is unverified, not confirmed.

Without a runnable script or network access, open each DOI record and publisher page, compare title, first author, and year, look for retraction, correction, or concern notices, and search for a journal version of each preprint. Either way, report what was checked, when, and what remains unverified. A resolving DOI establishes identity, not that the source supports the claim; reopen the cited passage for each key claim.
