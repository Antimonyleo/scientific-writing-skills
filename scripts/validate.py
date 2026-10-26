#!/usr/bin/env python3
"""Check this package's metadata and local Markdown links; standard library only."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


def validate(root):
    errors = []
    expected = {"academic-writing", "literature-review", "research-ideation"}
    found = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if found != expected:
        errors.append(f"Expected {sorted(expected)}, found {sorted(found)}")
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        # Entry points deliberately use simple scalar identity fields. This is
        # not a general YAML parser or a complete Agent Skills specification check.
        values = dict(re.findall(r"^(name|description|license): (.+)$", match[1], re.M))
        name = values.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"{path.relative_to(root)}: invalid name")
        if name != path.parent.name:
            errors.append(f"{path.relative_to(root)}: name differs from directory")
        if not 1 <= len(values.get("description", "")) <= 1024:
            errors.append(f"{path.relative_to(root)}: invalid description")
    for path in root.rglob("*.md"):
        if ".git" in path.relative_to(root).parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", text):
            url = urlsplit(target.strip("<>"))
            if url.scheme or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(f"{path.relative_to(root)}: invalid local link {target}")
            elif "skills" in path.relative_to(root).parts:
                skill_root = root / "skills" / path.relative_to(root).parts[1]
                if not resolved.is_relative_to(skill_root.resolve()):
                    errors.append(f"{path.relative_to(root)}: non-self-contained link {target}")
    for path in root.rglob("*.json"):
        if ".git" not in path.relative_to(root).parts:
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (ValueError, UnicodeError) as error:
                errors.append(f"{path.relative_to(root)}: {error}")
    for path in sorted((root / "skills").glob("*/scripts/*.py")):
        # Bundled helper scripts must at least parse; behavior is tested in tests/.
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except (SyntaxError, UnicodeError) as error:
            errors.append(f"{path.relative_to(root)}: {error}")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    issues = validate(root)
    for issue in issues:
        print(issue, file=sys.stderr)
    if issues:
        raise SystemExit(1)
    print("Validated three skill entrypoints, local Markdown links, JSON records, and bundled scripts.")
