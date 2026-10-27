#!/usr/bin/env python3
"""Offline tests for literature-review/scripts/verify_refs.py.

All bibliography data are synthetic and every registry response is mocked, so
these tests never contact a network service.
"""

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

sys.dont_write_bytecode = True  # keep skill directories free of __pycache__
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "literature-review" / "scripts"))
import verify_refs as v  # noqa: E402

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "synthetic.bib"


def work(doi, title, family, year, **extra):
    """A minimal synthetic Crossref work record."""
    record = {
        "DOI": doi,
        "title": [title],
        "author": [{"family": family, "given": "A."}],
        "issued": {"date-parts": [[year]]},
        "type": "journal-article",
        "container-title": ["Journal of Synthetic Assemblies"],
    }
    record.update(extra)
    return record


REGISTRY = {
    "10.5555/syn.0001": work("10.5555/syn.0001", "Programmable folding of synthetic lattice tiles", "Alder", 2021),
    "10.5555/syn.0002": work("10.5555/syn.0002", "Cation-dependent stacking of synthetic lattice tiles", "Brook", 2022),
    "10.5555/syn.0003": work(
        "10.5555/syn.0003", "Synthetic tile stability in low-salt buffer", "Fern", 2018,
        **{"updated-by": [{"type": "retraction", "source": "retraction-watch", "DOI": "10.5555/syn.0004"}]}),
    "10.5555/syn.0004": work(
        "10.5555/syn.0004", "Retraction notice for a synthetic article", "Fern", 2020,
        **{"update-to": [{"type": "retraction", "DOI": "10.5555/syn.0003"}]}),
    "10.5555/syn.0005": work(
        "10.5555/syn.0005", "Mock posted preprint on tile assembly", "Gale", 2019,
        type="posted-content", relation={"is-preprint-of": [{"id-type": "doi", "id": "10.5555/syn.0006"}]}),
    "10.5555/syn.0007": work(
        "10.5555/syn.0007", "Synthetic article with a correction", "Hale", 2017,
        **{"updated-by": [{"type": "correction", "source": "publisher", "DOI": "10.5555/syn.0008"}]}),
}


def fake_get_json(url, accept="application/json"):
    if url.startswith("https://api.crossref.org/works/"):
        doi = url.rsplit("/works/", 1)[1]
        doi = v.urllib.parse.unquote(doi)
        if doi in REGISTRY:
            return 200, {"message": REGISTRY[doi]}
        return 404, None
    if url.startswith("https://doi.org/"):
        return 404, None
    if url.startswith("https://api.crossref.org/works?"):
        items = [REGISTRY["10.5555/syn.0001"], REGISTRY["10.5555/syn.0002"]]
        return 200, {"message": {"items": items}}
    raise AssertionError(f"unexpected request: {url}")


def fake_get_json_offline(url, accept="application/json"):
    return None, None


class ParsingAndHygiene(unittest.TestCase):
    def setUp(self):
        self.entries = v.parse_bibtex(FIXTURE.read_text(encoding="utf-8"))

    def test_parses_entries_and_skips_string_macros(self):
        self.assertEqual(len(self.entries), 7)
        self.assertEqual(self.entries[0]["_key"], "alder2021")
        self.assertEqual(self.entries[0]["doi"], "10.5555/syn.0001")

    def test_hygiene_flags(self):
        issues = {(i["key"], i["severity"], i["issue"].split(":")[0].split(" (")[0]) for i in v.hygiene(self.entries)}
        self.assertIn(("alder2021", "error", "duplicate citation key"), issues)
        self.assertIn(("brook2022", "warn", "doi field should be bare DOI"), issues)
        self.assertIn(("cedar2023_samedoi", "warn", "same DOI as 'alder2021'"), issues)
        self.assertIn(("dune2020", "info", "preprint"), issues)
        self.assertIn(("elm2019", "warn", "@article missing 'journal'"), issues)
        self.assertTrue(any(sev == "error" and "unbalanced" in text for _, sev, text in issues))

    def test_claim_extraction(self):
        claims = {e["_key"]: v.claimed_from_bib(e) for e in self.entries if not e.get("_error")}
        self.assertEqual(claims["brook2022"]["first_author"], "Brook")
        self.assertEqual(claims["dune2020"]["arxiv"], "2001.00001")
        self.assertEqual(claims["brook2022"]["year"], "2022")

    def test_helpers(self):
        self.assertEqual(v.clean_doi("https://doi.org/10.5555/ABC."), "10.5555/ABC")
        self.assertEqual(v.clean_doi("doi: 10.5555/xyz"), "10.5555/xyz")
        self.assertEqual(v.first_author_family('H{\\"o}lm, Ida and Y, Z'), "Holm")
        self.assertEqual(v.first_author_family("Ida Holm and Z Y"), "Holm")
        self.assertTrue(v.same_family("Kumar", "Vale Kumar"))
        self.assertFalse(v.same_family("Alder", "Brook"))
        self.assertGreaterEqual(v.title_similarity(
            "Programmable folding of synthetic lattice tiles",
            "Programmable folding of synthetic lattice tiles: a mock study"), 0.95)
        self.assertLess(v.title_similarity(
            "Programmable folding of synthetic lattice tiles",
            "Cation-dependent stacking of a different system"), v.TITLE_CLOSE)


class MockedRegistry(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(v, "get_json", side_effect=fake_get_json)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_matching_doi_is_ok(self):
        r = v.verify({"doi": "10.5555/syn.0001", "title": "Programmable folding of synthetic lattice tiles",
                      "first_author": "Alder", "year": "2021"})
        self.assertEqual(r["status"], "OK", r)

    def test_real_doi_wrong_paper_is_mismatch(self):
        r = v.verify({"doi": "10.5555/syn.0001", "title": "A different paper reusing an existing identifier",
                      "first_author": "Cedar", "year": "2023"})
        self.assertEqual(r["status"], "MISMATCH")
        self.assertTrue(any(p.startswith("title mismatch") for p in r["problems"]))
        self.assertTrue(any(p.startswith("first author mismatch") for p in r["problems"]))

    def test_unknown_doi_is_not_found(self):
        r = v.verify({"doi": "10.5555/syn.9999"})
        self.assertEqual(r["status"], "NOT_FOUND")

    def test_malformed_doi_is_not_found_without_lookup(self):
        r = v.verify({"doi": "not-a-doi"})
        self.assertEqual(r["status"], "NOT_FOUND")

    def test_retraction_is_flagged(self):
        r = v.verify({"doi": "10.5555/syn.0003"})
        self.assertEqual(r["status"], "RETRACTED")

    def test_citing_the_notice_is_mismatch(self):
        r = v.verify({"doi": "10.5555/syn.0004"})
        self.assertEqual(r["status"], "MISMATCH")
        self.assertTrue(any("is a notice" in p for p in r["problems"]))

    def test_preprint_reports_published_version(self):
        r = v.verify({"doi": "10.5555/syn.0005"})
        self.assertEqual(r["status"], "CHECK")
        self.assertEqual(r["published_version"], "10.5555/syn.0006")
        self.assertIn("PREPRINT", r["flags"])

    def test_correction_needs_check(self):
        r = v.verify({"doi": "10.5555/syn.0007"})
        self.assertEqual(r["status"], "CHECK")

    def test_one_year_offset_is_note_not_mismatch(self):
        r = v.verify({"doi": "10.5555/syn.0002", "title": "Cation-dependent stacking of synthetic lattice tiles",
                      "first_author": "Brook", "year": "2023"})
        self.assertEqual(r["status"], "CHECK")

    def test_title_only_returns_candidate_not_fix(self):
        r = v.verify({"title": "Cation-dependent stacking of synthetic lattice tiles", "first_author": "Brook"})
        self.assertEqual(r["status"], "CANDIDATE")
        self.assertEqual(r["found"]["doi"], "10.5555/syn.0002")

    def test_unmatched_title_is_not_found(self):
        r = v.verify({"title": "An invented study of an unrelated topic entirely"})
        self.assertEqual(r["status"], "NOT_FOUND")

    def test_main_exit_codes_and_report(self):
        out = io.StringIO()
        with redirect_stdout(out):
            code = v.main(["--doi", "10.5555/syn.0001"])
        self.assertEqual(code, 0)
        self.assertIn("OK 1", out.getvalue())
        with redirect_stdout(io.StringIO()):
            self.assertEqual(v.main(["--doi", "10.5555/syn.0003"]), 1)


class NetworkFailure(unittest.TestCase):
    def test_unreachable_registry_is_error_and_fails_run(self):
        with mock.patch.object(v, "get_json", side_effect=fake_get_json_offline):
            r = v.verify({"doi": "10.5555/syn.0001"})
            self.assertEqual(r["status"], "ERROR")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(v.main(["--doi", "10.5555/syn.0001"]), 1)

    def test_offline_mode_runs_hygiene_only(self):
        with mock.patch.object(v, "get_json", side_effect=AssertionError("network used")):
            out = io.StringIO()
            with redirect_stdout(out):
                code = v.main([str(FIXTURE), "--offline"])
        self.assertEqual(code, 1)  # duplicate key and unbalanced braces are blocking
        self.assertIn("registry checks skipped", out.getvalue())


if __name__ == "__main__":
    unittest.main()
