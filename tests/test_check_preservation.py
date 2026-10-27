#!/usr/bin/env python3
"""Offline tests for academic-writing/scripts/check_preservation.py using synthetic text."""

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.dont_write_bytecode = True  # keep skill directories free of __pycache__
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills" / "academic-writing" / "scripts"))
import check_preservation as cp  # noqa: E402

LATEX = r"""Samples were annealed from 90 \si{\celsius} to 20 \si{\celsius} over 16 h in buffer with 12.5 mM MgCl$_2$ \cite{alder2021,brook2022}.
The yield was 82\% of 200 particles (Fig.~\ref{fig:yield}); see Eq.~\eqref{eq:fit} and \SI{10}{\milli\molar}.
\begin{equation} y = a e^{-k t} \label{eq:fit} \end{equation}
% internal note: 5 mM in an older draft
"""


class CheckPreservation(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)

    def run_check(self, original, revised, suffix=".tex"):
        paths = []
        for name, text in (("original", original), ("revised", revised)):
            path = Path(self.workspace.name) / f"{name}{suffix}"
            path.write_text(text, encoding="utf-8")
            paths.append(str(path))
        out = io.StringIO()
        with redirect_stdout(out), redirect_stderr(io.StringIO()):
            code = cp.main(["check_preservation.py", *paths])
        return code, out.getvalue()

    def test_identical_text_passes(self):
        code, out = self.run_check(LATEX, LATEX)
        self.assertEqual(code, 0)
        self.assertIn("No numbers, units, citation keys, labels/refs, or math differ.", out)

    def test_wording_only_edit_passes(self):
        revised = LATEX.replace("Samples were annealed", "We annealed the samples").replace("The yield was", "Yield was")
        code, _ = self.run_check(LATEX, revised)
        self.assertEqual(code, 0)

    def test_changed_value_and_unit_are_reported(self):
        revised = LATEX.replace("16 h", "18 h").replace("12.5 mM", "12.5 µM")
        code, out = self.run_check(LATEX, revised)
        self.assertEqual(code, 1)
        for token in ("16h", "18h", "12.5mM", "12.5µM"):
            self.assertIn(token, out)

    def test_siunitx_value_change_is_reported(self):
        code, out = self.run_check(LATEX, LATEX.replace(r"\SI{10}{\milli\molar}", r"\SI{100}{\milli\molar}"))
        self.assertEqual(code, 1)
        self.assertIn("100", out)

    def test_dropped_citation_key_is_reported(self):
        code, out = self.run_check(LATEX, LATEX.replace(r"\cite{alder2021,brook2022}", r"\cite{alder2021}"))
        self.assertEqual(code, 1)
        self.assertIn("[citations]", out)
        self.assertIn("brook2022", out)

    def test_changed_label_and_math_are_reported(self):
        revised = LATEX.replace(r"\ref{fig:yield}", r"\ref{fig:yields}").replace("e^{-k t}", "e^{-2k t}")
        code, out = self.run_check(LATEX, revised)
        self.assertEqual(code, 1)
        self.assertIn("[labels/refs]", out)
        self.assertIn("[math]", out)

    def test_latex_comments_are_ignored(self):
        code, _ = self.run_check(LATEX, LATEX.replace("5 mM in an older draft", "8 mM in an older draft"))
        self.assertEqual(code, 0)

    def test_plain_text_references_and_percent(self):
        original = "The structure were imaged at 10 mM MgCl2; yield was 82 %. See Fig. 2b and [12].\n"
        typographic = "The structure was imaged at 10 mM MgCl₂; yield was 82%. See Fig. 2b and [12].\n"
        code, _ = self.run_check(original, typographic, suffix=".txt")
        self.assertEqual(code, 0)
        code, out = self.run_check(original, typographic.replace("Fig. 2b", "Fig. 2c"), suffix=".txt")
        self.assertEqual(code, 1)
        self.assertIn("Fig.2c", out)

    def test_placeholders_are_listed_but_not_counted_as_claims(self):
        revised = LATEX.replace("particles (", r"particles \textbf{[DATA: number of preparations, e.g. 3]} (")
        code, out = self.run_check(LATEX, revised)
        self.assertEqual(code, 0)
        self.assertIn("[placeholders in revised] DATA 1", out)

    def test_word_count_convention(self):
        # Inline math and a reference each count as one word; punctuation alone does not.
        self.assertEqual(cp.word_count(r"We measured $k$ in \cite{a} Fig.~\ref{f} ."), 6)

    def test_unreadable_input_is_usage_error(self):
        with redirect_stderr(io.StringIO()):
            self.assertEqual(cp.main(["check_preservation.py", "missing-a.tex", "missing-b.tex"]), 2)
            self.assertEqual(cp.main(["check_preservation.py"]), 2)


if __name__ == "__main__":
    unittest.main()
