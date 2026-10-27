#!/usr/bin/env python3
"""Compare an original and a revised text for silently changed scientific tokens.

Reports numbers (with an attached unit or %), citation keys, cross-reference
labels, and inline/display math that appear in one version but not the other,
plus a simple word count for each version. Works on LaTeX, Markdown, or plain
text. Standard library only.

Usage:
    python3 check_preservation.py ORIGINAL REVISED

Exit status: 0 if nothing differs, 1 if anything differs, 2 on usage error.
A difference is not necessarily an error; it is a prompt to confirm that each
change was intentional (for example, a number deliberately cut from an
abstract) and to restore anything that was not. The script also lists any
[CITE: ...], [DATA: ...] or [CHECK: ...] placeholders left in the revision.
The checks are pattern-based: they catch common silent changes, not every
change of meaning, and they do not judge whether a revision is correct.
"""

import re
import sys
from collections import Counter
from pathlib import Path

UNIT = (
    r"(?:%|°C|K|mM|µM|uM|μM|nM|pM|fM|M|mg|µg|μg|ng|g|kg|mL|µL|μL|uL|nL|L|"
    r"nm|µm|μm|um|mm|cm|m|Å|s|ms|µs|μs|ns|ps|min|h|hr|d|kDa|Da|bp|nt|kb|"
    r"kcal/mol|kJ/mol|pN|nN|Hz|kHz|MHz|eV|V|mV|W|mW|rpm|x|×|fold|equiv)"
)
NUMBER = re.compile(
    r"(?<![\w.])[-−+±]?\d+(?:[.,]\d+)*(?:\s?(?:×|x|\\times)\s?10\^?\{?[-−]?\d+\}?|[eE][-−+]?\d+)?"
    r"(?:\s?(?:\\,|~)?\s?" + UNIT + r"(?![A-Za-z]))?"
)
CITE = re.compile(r"\\(?:[A-Za-z]*cite[A-Za-z]*|footcite|autocite)\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
REF = re.compile(r"\\(label|ref|eqref|cref|Cref|autoref|pageref|nameref)\*?\{([^}]*)\}")
SIUNITX = re.compile(r"\\(?:SI|qty|num|si|unit|SIrange|qtyrange|numrange)\{([^}]*)\}(?:\{([^}]*)\})?(?:\{([^}]*)\})?")
INLINE_MATH = re.compile(r"(?<!\\)\$(?!\$)(.+?)(?<!\\)\$|\\\((.+?)\\\)", re.S)
DISPLAY_MATH = re.compile(
    r"\$\$(.+?)\$\$|\\\[(.+?)\\\]|\\begin\{(equation|align|gather|multline)\*?\}(.+?)\\end\{\3\*?\}",
    re.S,
)
COMMENT = re.compile(r"(?<!\\)%.*$", re.M)
PLACEHOLDER = re.compile(r"\[(CITE|DATA|CHECK):[^\]]*\]")
# Plain-text cross-references such as "Fig. 2b", "Supplementary Table S3", "Eq. 4", "ref. 12", "[12, 14]".
TEXT_XREF = re.compile(
    r"\b(?:Supplementary\s+)?(?:Figs?\.|Figures?|Tables?|Eqs?\.|Equations?|Refs?\.|Sections?|Notes?)"
    r"(?:~|\s)*(S?\d+[A-Za-z]?(?:\s*[-–,]\s*S?\d+[A-Za-z]?)*)"
    r"|\[(\d+(?:\s*[-–,]\s*\d+)*)\]"
)


def norm(s: str) -> str:
    return re.sub(r"\s+", "", s.replace("−", "-").replace("μ", "µ").replace("\\,", "").replace("~", ""))


def looks_like_latex(path: Path, text: str) -> bool:
    return path.suffix.lower() in {".tex", ".ltx", ".sty", ".cls"} or bool(
        re.search(r"\\(begin|cite[a-z]*|ref|eqref|cref|label|section|emph|textit|SI|qty)\b", text)
    )


def strip_comments(text: str, latex: bool) -> str:
    # In LaTeX an unescaped % starts a comment; in plain text it is a percent sign.
    return COMMENT.sub("", text) if latex else text


def extract(text: str) -> dict:
    found = {"numbers": Counter(), "citations": Counter(), "labels/refs": Counter(), "math": Counter()}
    for m in DISPLAY_MATH.finditer(text):
        body = next(g for g in (m.group(1), m.group(2), m.group(4)) if g is not None)
        found["math"][norm(body)] += 1
    text_wo_display = DISPLAY_MATH.sub(" ", text)
    for m in INLINE_MATH.finditer(text_wo_display):
        found["math"][norm(m.group(1) or m.group(2))] += 1
    for m in CITE.finditer(text):
        for key in m.group(1).split(","):
            if key.strip():
                found["citations"][key.strip()] += 1
    for m in REF.finditer(text):
        for key in m.group(2).split(","):
            found["labels/refs"][f"\\{m.group(1)}{{{key.strip()}}}"] += 1
    for m in TEXT_XREF.finditer(re.sub(r"\\[A-Za-z]*ref\*?\{[^}]*\}", " ", text)):
        found["labels/refs"][norm(m.group(0))] += 1
    for m in SIUNITX.finditer(text):
        found["numbers"][norm(" ".join(g for g in m.groups() if g))] += 1
    # Numbers in prose: drop commands, keys, and math so their digits are not double counted.
    prose = SIUNITX.sub(" ", text_wo_display)
    prose = INLINE_MATH.sub(" ", prose)
    prose = CITE.sub(" ", prose)
    prose = REF.sub(" ", prose)
    prose = TEXT_XREF.sub(" ", prose)
    prose = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", prose)
    for m in NUMBER.finditer(prose):
        found["numbers"][norm(m.group(0))] += 1
    return found


def word_count(text: str) -> int:
    text = DISPLAY_MATH.sub(" ", text)
    text = INLINE_MATH.sub(" MATH ", text)
    text = CITE.sub(" ", text)
    text = REF.sub(" REF ", text)
    text = re.sub(r"\\[A-Za-z]+\*?(\[[^\]]*\])?", " ", text)
    text = re.sub(r"[{}]", " ", text)
    return sum(1 for token in text.split() if re.search(r"\w", token))


def main(argv: list) -> int:
    if len(argv) != 3:
        print("usage: check_preservation.py ORIGINAL REVISED", file=sys.stderr)
        return 2
    paths = [Path(argv[1]), Path(argv[2])]
    try:
        raw = [p.read_text(encoding="utf-8") for p in paths]
    except (OSError, UnicodeDecodeError) as error:
        print(f"cannot read input: {error}", file=sys.stderr)
        return 2
    latex = any(looks_like_latex(p, t) for p, t in zip(paths, raw))
    orig_text, rev_text = (strip_comments(t, latex) for t in raw)
    # Placeholders are reported separately; their contents are notes, not claims.
    bare = [PLACEHOLDER.sub(" ", t) for t in (orig_text, rev_text)]
    orig, rev = (extract(t) for t in bare)
    differs = False
    for kind in orig:
        removed = orig[kind] - rev[kind]
        added = rev[kind] - orig[kind]
        if removed or added:
            differs = True
            print(f"[{kind}]")
            for item, n in sorted(removed.items()):
                print(f"  only in original ({n}x): {item}")
            for item, n in sorted(added.items()):
                print(f"  only in revised  ({n}x): {item}")
    print(
        f"[words] original {word_count(bare[0])}, revised {word_count(bare[1])} "
        "(whitespace tokens containing a letter or digit, after stripping LaTeX commands, citations, display math, and placeholders; "
        "inline math and refs count as one word; venues may count differently)"
    )
    placeholders = Counter(m.group(1) for m in PLACEHOLDER.finditer(rev_text))
    if placeholders:
        listed = ", ".join(f"{kind} {n}" for kind, n in sorted(placeholders.items()))
        print(f"[placeholders in revised] {listed}")
    if not differs:
        print("No numbers, units, citation keys, labels/refs, or math differ.")
    return 1 if differs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
