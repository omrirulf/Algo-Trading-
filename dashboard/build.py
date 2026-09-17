#!/usr/bin/env python3
"""Build the dashboard page from the template and the book snapshot.

    python dashboard/build.py                      # writes dashboard/desk.html
    python dashboard/build.py --out /tmp/desk.html

The page embeds ``logs/book.json`` at build time, so it reads correctly with
no connector at all; where the viewer can run one it also reads the live file
from GitHub. Rebuilt and republished after every cycle by a Routine in the
owner's Claude account, because publishing an artifact needs a Claude
session and the workflow runner has none.

Reads two files, writes one. Nothing here touches a broker, a model or the
network.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "template.html"
PLACEHOLDER = "/*__SEED__*/{}"


def build(template: Path, book: Path) -> str:
    text = template.read_text(encoding="utf-8")
    if PLACEHOLDER not in text:
        raise SystemExit(f"{template} carries no {PLACEHOLDER} placeholder")
    snapshot = json.loads(book.read_text(encoding="utf-8"))
    seed = json.dumps(snapshot, separators=(",", ":")).replace("</", "<\\/")
    return text.replace(PLACEHOLDER, "/*__SEED__*/" + seed, 1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the dashboard page.")
    parser.add_argument("--template", type=Path, default=TEMPLATE)
    parser.add_argument("--book", type=Path, default=ROOT / "logs" / "book.json")
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent / "desk.html")
    args = parser.parse_args(argv)
    args.out.write_text(build(args.template, args.book), encoding="utf-8")
    print(f"wrote {args.out} ({args.out.stat().st_size} bytes) from {args.book}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
