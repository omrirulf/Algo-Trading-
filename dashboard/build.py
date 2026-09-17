#!/usr/bin/env python3
"""Build the dashboard page from the template and the book snapshot.

    python dashboard/build.py                      # writes dashboard/desk.html
    python dashboard/build.py --out /tmp/desk.html
    python dashboard/build.py --site _site         # the whole installable site

The page embeds ``logs/book.json`` at build time, so it opens correctly
before the first network read; online it reads the live file straight from
the public repository. ``--site`` writes the page as ``index.html`` beside
the manifest, the service worker and the icons, which is what the ``pages``
workflow deploys to GitHub Pages after every cycle so the owner's phone has
it as an app.

Reads a handful of files, writes a handful. Nothing here touches a broker, a
model or the network.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = Path(__file__).resolve().parent / "template.html"
PLACEHOLDER = "/*__SEED__*/{}"
#: Everything the installed app needs beside the page itself.
STATIC = ("manifest.webmanifest", "sw.js", "icon.svg", "icon-192.png", "icon-512.png")


def build(template: Path, book: Path) -> str:
    text = template.read_text(encoding="utf-8")
    if PLACEHOLDER not in text:
        raise SystemExit(f"{template} carries no {PLACEHOLDER} placeholder")
    snapshot = json.loads(book.read_text(encoding="utf-8"))
    seed = json.dumps(snapshot, separators=(",", ":")).replace("</", "<\\/")
    return text.replace(PLACEHOLDER, "/*__SEED__*/" + seed, 1)


def build_site(template: Path, book: Path, site: Path) -> list[Path]:
    """Write index.html and copy the static files next to it."""
    site.mkdir(parents=True, exist_ok=True)
    written = [site / "index.html"]
    written[0].write_text(build(template, book), encoding="utf-8")
    for name in STATIC:
        target = site / name
        target.write_bytes((template.parent / name).read_bytes())
        written.append(target)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the dashboard page.")
    parser.add_argument("--template", type=Path, default=TEMPLATE)
    parser.add_argument("--book", type=Path, default=ROOT / "logs" / "book.json")
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent / "desk.html")
    parser.add_argument("--site", type=Path, default=None, help="write the installable site into this directory")
    args = parser.parse_args(argv)
    if args.site:
        for path in build_site(args.template, args.book, args.site):
            print(f"wrote {path} ({path.stat().st_size} bytes)")
        return 0
    args.out.write_text(build(args.template, args.book), encoding="utf-8")
    print(f"wrote {args.out} ({args.out.stat().st_size} bytes) from {args.book}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
