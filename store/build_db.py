#!/usr/bin/env python3
"""Build or refresh the queryable index over the logs.

    python store/build_db.py                 # load both logs, print a summary
    python store/build_db.py --rebuild       # discard and reload from scratch
    python store/build_db.py --db /tmp/x.db  # somewhere other than logs/

Safe to run after every cycle. Loading is keyed on a content hash of each
source line, so a journal that has grown by one line costs one insert.

This writes exactly one file -- the database named by ``--db`` -- and reads
everything else. It holds no broker keys, has no order path, and never touches
the logs it reads.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow ``python store/build_db.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import settings as cfg  # noqa: E402
from store import database, loader  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="build_db",
        description="Load the signal journal and execution audit into SQLite.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--db", type=Path, default=cfg.DATABASE_PATH,
        help="database to write (default: %(default)s)",
    )
    parser.add_argument(
        "--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH,
        help="signal journal to load (default: %(default)s)",
    )
    parser.add_argument(
        "--audit", type=Path, default=cfg.AUDIT_LOG_PATH,
        help="execution audit log to load (default: %(default)s)",
    )
    parser.add_argument(
        "--rebuild", action="store_true",
        help=(
            "delete the database first and reload from the logs. Cheap and "
            "always available, because the logs are the record and this file "
            "is only an index over them"
        ),
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="exit code only")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.rebuild and args.db.exists():
        args.db.unlink()
        # WAL leaves two siblings behind; an orphaned -wal would be reapplied
        # to the next database created at this path.
        for suffix in ("-wal", "-shm"):
            sidecar = args.db.with_name(args.db.name + suffix)
            if sidecar.exists():
                sidecar.unlink()

    missing = [p for p in (args.journal, args.audit) if not p.exists()]
    if len(missing) == 2:
        print(
            f"Neither {args.journal} nor {args.audit} exists.\n"
            "The orchestrator writes them; run a cycle first "
            "(python -m orchestrator.heartbeat --once).",
            file=sys.stderr,
        )
        return 1

    connection = database.connect_rw(args.db)
    try:
        signals = loader.load_file(connection, args.journal, "signals")
        executions = loader.load_file(connection, args.audit, "executions")
        counts = summarise(connection)
    finally:
        connection.close()

    if not args.quiet:
        print(signals.describe("signals"))
        print(executions.describe("executions"))
        for path in missing:
            print(f"  (no file at {path} -- nothing to load from it)")
        print()
        print(f"{args.db}: {counts['signals']} signals, {counts['executions']} executions")
        if counts["span"]:
            print(f"covering {counts['span'][0]} to {counts['span'][1]}")
    return 0


def summarise(connection) -> dict:
    """Row counts and the date span, for the one line worth printing."""
    signals = connection.execute("SELECT COUNT(*) FROM signals").fetchone()[0]
    executions = connection.execute("SELECT COUNT(*) FROM executions").fetchone()[0]
    span = connection.execute(
        "SELECT MIN(trade_date), MAX(trade_date) FROM signals WHERE trade_date IS NOT NULL"
    ).fetchone()
    return {
        "signals": signals,
        "executions": executions,
        "span": tuple(span) if span and span[0] else None,
    }


if __name__ == "__main__":
    raise SystemExit(main())
