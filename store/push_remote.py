#!/usr/bin/env python3
"""Push the log files to the remote archive.

    python store/push_remote.py                # send what the remote is missing
    python store/push_remote.py --all          # backfill everything
    python store/push_remote.py --dry-run      # count what would go, send nothing
    python store/push_remote.py --print-schema # the SQL to run once, first

Runs *after* a cycle, never inside one. The heartbeat writes its JSON-lines and
commits them exactly as before; this then copies them up. A failure here cannot
cost a signal, because the signal is already on disk and already in git -- and
the next push catches up on its own, since inserts are keyed on a content hash
and conflicts are ignored.

With no Supabase credential configured this exits 0 and does nothing. Not
having a remote is a state, not a failure.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Optional, Sequence

# Allow ``python store/push_remote.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from store import loader, remote  # noqa: E402
from store.remote import EXECUTIONS, SIGNALS, RemoteArchive, RemoteArchiveError  # noqa: E402

SCHEMA_PATH = Path(__file__).resolve().parent / "remote_schema.sql"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="push_remote",
        description="Copy the signal journal and execution audit to Supabase.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
        help="signal journal to push (default: %(default)s)",
    )
    parser.add_argument(
        "--audit", type=Path, default=cfg.AUDIT_LOG_PATH,
        help="execution audit log to push (default: %(default)s)",
    )
    parser.add_argument(
        "--all", action="store_true",
        help=(
            "send every line rather than only those at or after the remote's "
            "newest timestamp. Use for the first backfill; safe any time, "
            "because duplicates are ignored on arrival"
        ),
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="report what would be sent without sending it",
    )
    parser.add_argument(
        "--print-schema", action="store_true",
        help="print the SQL to create the remote tables, then exit",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.print_schema:
        print(SCHEMA_PATH.read_text(encoding="utf-8"))
        return 0

    if not RemoteArchive.is_configured():
        print(
            "No remote archive configured (SUPABASE_URL / SUPABASE_SERVICE_KEY "
            "are unset); nothing to push. The local logs are unaffected."
        )
        return 0

    try:
        archive = RemoteArchive.from_settings()
    except RemoteArchiveError as exc:
        print(exc, file=sys.stderr)
        return 1

    plan = [(SIGNALS, args.journal, loader.signal_row),
            (EXECUTIONS, args.audit, loader.execution_row)]

    try:
        for table, path, build_row in plan:
            rows = rows_from(path, build_row)
            if not rows:
                print(f"{table}: nothing at {path}")
                continue

            watermark = None if args.all else archive.latest_timestamp(table)
            pending = remote.select_new(rows, watermark)
            since = f" since {watermark}" if watermark else " (everything)"

            if args.dry_run:
                print(f"{table}: would send {len(pending)} of {len(rows)} rows{since}")
                continue

            result = archive.push(table, pending)
            print(f"{result.describe()}{since}")
    except RemoteArchiveError as exc:
        print(f"Remote archive push failed: {exc}", file=sys.stderr)
        return 1

    return 0


def rows_from(path: Path, build_row) -> list[dict[str, Any]]:
    """Every readable line of a log file, as rows. A missing file is empty.

    Unreadable lines are skipped silently here rather than counted: the local
    loader already reports them, and this tool's job is to move what parses,
    not to re-audit the file.
    """
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = build_row(line)
            if row is None or row["line_hash"] in seen:
                continue
            seen.add(row["line_hash"])
            rows.append(row)
    return rows


if __name__ == "__main__":
    raise SystemExit(main())
