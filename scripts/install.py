#!/usr/bin/env python3
"""Copy the three skills to an explicit host directory, preserving replaced copies."""

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

from validate import validate


def content_map(path):
    return {str(p.relative_to(path)): p.read_bytes() for p in path.rglob("*") if p.is_file()}


def install(root, target):
    issues = validate(root)
    if issues:
        raise ValueError("Package validation failed: " + "; ".join(issues))
    target = target.expanduser().absolute()
    source = root / "skills"
    if target.resolve().is_relative_to(root.resolve()) or root.resolve().is_relative_to(target.resolve()):
        raise ValueError("Install target must be separate from this repository")
    plans = []
    for item in sorted(source.iterdir()):
        if not item.is_dir():
            continue
        destination = target / item.name
        if destination.is_symlink() or (destination.exists() and not destination.is_dir()):
            raise ValueError(f"Refusing to replace symlink or non-directory: {destination}")
        if destination.exists() and any(p.is_symlink() for p in destination.rglob("*")):
            raise ValueError(f"Refusing to replace directory containing symlinks: {destination}")
        if destination.exists() and content_map(destination) == content_map(item):
            continue
        plans.append((item, destination))
    if not plans:
        print("Already current; no files changed.")
        return
    target.mkdir(parents=True, exist_ok=True)
    # Stage every copy before changing any existing installation.
    with tempfile.TemporaryDirectory(prefix=".scientific-writing-stage-", dir=target) as stage_name:
        stage = Path(stage_name)
        for item, _ in plans:
            shutil.copytree(item, stage / item.name)
        backup = None
        for item, destination in plans:
            old = None
            if destination.exists():
                if backup is None:
                    backup = Path(tempfile.mkdtemp(prefix=".scientific-writing-backup-", dir=target))
                old = backup / item.name
                destination.rename(old)
            try:
                (stage / item.name).rename(destination)
            except OSError:
                if old is not None:
                    old.rename(destination)
                raise
            print(f"Installed {destination}")
        if backup:
            print(f"Previous copies preserved at {backup}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="Host skill directory")
    args = parser.parse_args()
    try:
        install(Path(__file__).resolve().parents[1], args.target)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
