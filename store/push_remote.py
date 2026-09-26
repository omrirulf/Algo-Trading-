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

    python store/push_remote.py --status logs/archive_status.json

With ``--status`` it also writes down how the push went, for the owner: the
heartbeat commits that file and sends a phone alert the same day when the
push failed, and the daily brief shows the date of the last push that
worked. That record exists because the archive went quiet once already: the
Supabase project "algo-trading-archive" was paused by Supabase for
inactivity, because every push had printed "No remote archive configured"
(the two secrets were never set) and nothing read that line. A free project
nothing writes to is paused after about a week, so "not configured" is
written down too, and the brief warns about it every day.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional, Sequence

# Allow ``python store/push_remote.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import journal_files  # noqa: E402
from config import settings as cfg  # noqa: E402
from store import loader, remote  # noqa: E402
from store.remote import (  # noqa: E402
    EXECUTIONS, NOT_CONFIGURED, SIGNALS, RemoteArchive, RemoteArchiveError, describe_failure,
)

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
    parser.add_argument(
        "--status", type=Path, default=None,
        help=(
            "write how this push went to this JSON file (last attempt, last "
            "success, ok, a short reason). Not with --dry-run or --print-schema"
        ),
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.print_schema:
        print(SCHEMA_PATH.read_text(encoding="utf-8"))
        return 0

    record = args.status is not None and not args.dry_run
    try:
        code, failure = push(args)
    except Exception as exc:
        # Written down before the crash goes on up, so the phone alert and
        # the brief can say the push broke rather than show yesterday's
        # record. The exception still fails the step, loudly, as before.
        if record:
            record_status(args.status, f"push crashed ({type(exc).__name__})")
        raise
    if record:
        record_status(args.status, failure)
    return code


def push(args: argparse.Namespace) -> tuple[int, Optional[str]]:
    """Do the push; the exit code, and what went wrong in a few words (None when nothing did).

    The words are ``not configured``, ``project paused or unreachable`` or
    ``HTTP <code>`` (``store.remote.describe_failure``): never the remote's
    own text, which is still printed to the log as it always was.
    """
    if not RemoteArchive.is_configured():
        print(
            "No remote archive configured (SUPABASE_URL / SUPABASE_SERVICE_KEY "
            "are unset); nothing to push. The local logs are unaffected."
        )
        return 0, NOT_CONFIGURED

    try:
        archive = RemoteArchive.from_settings()
    except RemoteArchiveError as exc:
        print(exc, file=sys.stderr)
        return 1, NOT_CONFIGURED

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
        return 1, describe_failure(exc)

    return 0, None


def read_status(path: Path) -> dict[str, Any]:
    """The previous push's record, or an empty one if there is none to read."""
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return previous if isinstance(previous, dict) else {}


def status_after(previous: dict[str, Any], failure: Optional[str], now: datetime) -> dict[str, Any]:
    """This push's record: when it was tried, when one last worked, and why not.

    ``last_success`` is carried over from ``previous`` when this push did not
    work, so a week of failures still says when the archive last had
    everything -- the date the brief shows. A value there that is not a
    string is dropped rather than copied: this file is committed and read
    by the brief, and it only ever holds what this function wrote.
    """
    stamp = now.astimezone(timezone.utc).isoformat(timespec="seconds")
    kept = previous.get("last_success")
    return {
        "last_attempt": stamp,
        "last_success": stamp if failure is None else (kept if isinstance(kept, str) else None),
        "ok": failure is None,
        "error": failure,
    }


def render_status(status: dict[str, Any]) -> str:
    return json.dumps(status, indent=2) + "\n"


def record_status(path: Path, failure: Optional[str], now: Optional[datetime] = None) -> None:
    """Write this push's record to ``path``. Never raises: a record is not a reason to fail.

    The one file ``store/`` writes outside SQLite (the CI guardrail names
    this exact line). It is not a log this package reads as a source: it is
    this script's own note about itself, rewritten whole every time.
    """
    status = status_after(read_status(path), failure, now or datetime.now(timezone.utc))
    try:
        path.write_text(render_status(status), encoding="utf-8")
    except OSError as exc:
        print(f"could not write the push record to {path}: {type(exc).__name__}", file=sys.stderr)


def rows_from(path: Path, build_row) -> list[dict[str, Any]]:
    """Every readable line of a log file, as rows. A missing file is empty.

    Unreadable lines are skipped silently here rather than counted: the local
    loader already reports them, and this tool's job is to move what parses,
    not to re-audit the file.
    """
    if not journal_files.exists(path):
        return []
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    # The journal's monthly files joined in order, or one plain file.
    for line in journal_files.iter_lines(path):
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
