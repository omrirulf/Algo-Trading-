#!/usr/bin/env python3
"""Build the dashboard pages from their templates and the snapshots.

    python dashboard/build.py                      # writes dashboard/desk.html
    python dashboard/build.py --out /tmp/desk.html
    python dashboard/build.py --site _site         # the whole installable site

The desk embeds ``logs/book.json`` at build time, so it opens correctly
before the first network read; online it reads the live file straight from
the public repository. ``--site`` writes the desk as ``index.html`` and the
four-fund page as ``funds.html`` beside the manifest, the service worker and
the icons, which is what the ``pages`` workflow deploys to GitHub Pages after
every cycle so the owner's phone has it as an app.

The four-fund page embeds ``logs/funds.json`` and ``logs/race_gate.json`` the
same way. Either may be missing -- neither exists until the nightly
simulation has run once -- and the page then embeds ``{}`` and opens on its
empty states, because the desk must keep publishing whatever the experiment's
files say.

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
FUNDS_TEMPLATE = Path(__file__).resolve().parent / "funds.html"
FUNDS_PLACEHOLDER = "/*__FUNDS__*/{}"
RACE_PLACEHOLDER = "/*__RACE__*/{}"
#: Everything the installed app needs beside the page itself.
STATIC = ("manifest.webmanifest", "sw.js", "icon.svg", "icon-192.png", "icon-512.png")


def build(template: Path, book: Path) -> str:
    text = template.read_text(encoding="utf-8")
    if PLACEHOLDER not in text:
        raise SystemExit(f"{template} carries no {PLACEHOLDER} placeholder")
    snapshot = json.loads(book.read_text(encoding="utf-8"))
    return text.replace(PLACEHOLDER, "/*__SEED__*/" + _embed(snapshot), 1)


def _embed(data: object) -> str:
    # Every "<" is written as the JSON escape "\u003c", so nothing a string
    # holds can act as markup inside the seed's script block: not "</script>",
    # which would end it early, and not "<!--" followed by "<script>", which
    # sends the HTML parser into the script-escape states where the block's
    # own closing tag no longer ends it and the page's main script is
    # swallowed. JSON.parse reads "\u003c" back as "<".
    return json.dumps(data, separators=(",", ":")).replace("<", "\\u003c")


def _no_constant(name: str) -> object:
    # Python's json module reads NaN, Infinity and -Infinity, which are not
    # JSON: the browser's JSON.parse rejects them, so a file holding one
    # would embed a seed the page cannot read. Refusing them here sends such
    # a file down the same path as any other unparseable one.
    raise ValueError(f"{name} is not valid JSON")


def _seed(path: Path) -> object:
    """The file's JSON, or ``{}`` when there is none yet or it does not parse.

    A missing file is the normal state before the first nightly run. A file
    that does not parse (NaN or Infinity included) is not, so it is said on
    stderr -- but the page is still built, on its empty states, rather than
    stopping the desk's deploy.
    """
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"), parse_constant=_no_constant)
    except (OSError, ValueError) as exc:
        print(f"warning: {path} could not be read ({exc}); the page embeds {{}} instead", file=sys.stderr)
        return {}


def build_funds(template: Path, funds_json_path: Path, race_json_path: Path) -> str:
    """The four-fund page with both snapshots embedded."""
    text = template.read_text(encoding="utf-8")
    for placeholder in (FUNDS_PLACEHOLDER, RACE_PLACEHOLDER):
        if placeholder not in text:
            raise SystemExit(f"{template} carries no {placeholder} placeholder")
    text = text.replace(FUNDS_PLACEHOLDER, "/*__FUNDS__*/" + _embed(_seed(funds_json_path)), 1)
    return text.replace(RACE_PLACEHOLDER, "/*__RACE__*/" + _embed(_seed(race_json_path)), 1)


def build_site(
    template: Path,
    book: Path,
    site: Path,
    funds: Path = ROOT / "logs" / "funds.json",
    race: Path = ROOT / "logs" / "race_gate.json",
) -> list[Path]:
    """Write index.html and funds.html and copy the static files next to them.

    The four-fund page's template sits beside the desk's, like the static
    files, so a copied dashboard directory builds the same site.
    """
    site.mkdir(parents=True, exist_ok=True)
    written = [site / "index.html", site / "funds.html"]
    written[0].write_text(build(template, book), encoding="utf-8")
    written[1].write_text(build_funds(template.parent / FUNDS_TEMPLATE.name, funds, race), encoding="utf-8")
    for name in STATIC:
        target = site / name
        target.write_bytes((template.parent / name).read_bytes())
        written.append(target)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the dashboard page.")
    parser.add_argument("--template", type=Path, default=TEMPLATE)
    parser.add_argument("--book", type=Path, default=ROOT / "logs" / "book.json")
    parser.add_argument("--funds", type=Path, default=ROOT / "logs" / "funds.json",
                        help="the simulation's nightly record for the four-fund page (missing: empty states)")
    parser.add_argument("--race", type=Path, default=ROOT / "logs" / "race_gate.json",
                        help="the decision gate's nightly record for the four-fund page (missing: empty states)")
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent / "desk.html")
    parser.add_argument("--site", type=Path, default=None, help="write the installable site into this directory")
    args = parser.parse_args(argv)
    if args.site:
        for path in build_site(args.template, args.book, args.site, args.funds, args.race):
            print(f"wrote {path} ({path.stat().st_size} bytes)")
        return 0
    args.out.write_text(build(args.template, args.book), encoding="utf-8")
    print(f"wrote {args.out} ({args.out.stat().st_size} bytes) from {args.book}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
