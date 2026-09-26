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

What it sends (26 Sep 2026: the rule is to keep what cannot be got back
later, and what a result would need to be checked again):

* ``signals`` and ``executions`` -- the journal and the audit log, as ever;
  the audit log's ``position_managed`` lines (the ladder, the stops) now
  included (``store/loader.py:execution_row``);
* ``account_snapshots`` and ``account_fills`` -- ``logs/account.jsonl``,
  the paper account after each run and every fill it read;
* ``model_calls`` and ``model_io_files``, and the bodies themselves to the
  private Storage bucket ``model-io`` -- every model call a cycle made
  (``--model-io``, ``store/model_calls.py``); a record that looks like it
  holds a credential is withheld whole and counted in ``--status``;
* ``scoring_prices`` and ``scoring_runs`` -- only with ``--prices``: the
  daily prices a race or funds run scored with, from the artifact
  ``scoring-prices.yml`` downloads (``store/scoring_prices.py``).

The git journal stays the official record; this is a backup and a place to
search. Nothing in the race, the funds or the pre-registration reads it.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# Allow ``python store/push_remote.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import journal_files  # noqa: E402
from config import settings as cfg  # noqa: E402
from store import loader, model_calls, remote, scoring_prices  # noqa: E402
from store.remote import (  # noqa: E402
    ACCOUNT_FILLS, ACCOUNT_SNAPSHOTS, EXECUTIONS, MODEL_CALLS, MODEL_IO_BUCKET, MODEL_IO_FILES,
    NOT_CONFIGURED, SCORING_PRICES, SCORING_RUNS, SIGNALS, RemoteArchive, RemoteArchiveError,
    describe_failure,
)

SCHEMA_PATH = Path(__file__).resolve().parent / "remote_schema.sql"

#: The parts a push can send, in the order it sends them. The two logs go
#: first: they are the archive's reason to exist, and a part added later (a
#: table the SQL has not created yet) must not stand in their way.
PARTS = ("signals", "executions", "account", "model-io", "prices")

#: What the failure record says when a price hand-over was refused before
#: anything was sent: it did not hash to its own prices_sha256, or it was not
#: shaped like prices.
PRICES_REFUSED = "price table refused"


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
        "--account", type=Path, default=cfg.LOG_DIR / "account.jsonl",
        help="account snapshots to push (default: %(default)s)",
    )
    parser.add_argument(
        "--model-io", type=Path, default=cfg.MODEL_IO_DIR,
        help=(
            "directory of model-call capture files to push, rows and Storage "
            "objects (default: %(default)s)"
        ),
    )
    parser.add_argument(
        "--prices", type=Path, action="append", default=[],
        help="a scoring-prices table (analysis/price_tape.py) to push; repeatable",
    )
    parser.add_argument(
        "--run-id", default=None,
        help="the GitHub run the --prices tables came from, recorded beside them",
    )
    parser.add_argument(
        "--only", default=None,
        help=(
            f"comma-separated parts to send, of {', '.join(PARTS)} (default: all of "
            "them; prices only when --prices is given)"
        ),
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
            "success, ok, a short reason, records withheld). Not with "
            "--dry-run or --print-schema"
        ),
    )
    return parser


@dataclass
class Outcome:
    """How a push went: the exit code, the first thing that failed (in a few words), and
    how many model-call records were withheld as credential-shaped."""

    code: int = 0
    failure: Optional[str] = None
    withheld: int = 0

    def fail(self, words: str) -> None:
        self.code = 1
        self.failure = self.failure or words


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.print_schema:
        print(SCHEMA_PATH.read_text(encoding="utf-8"))
        return 0

    record = args.status is not None and not args.dry_run
    try:
        outcome = push(args)
    except Exception as exc:
        # Written down before the crash goes on up, so the phone alert and
        # the brief can say the push broke rather than show yesterday's
        # record. The exception still fails the step, loudly, as before.
        if record:
            record_status(args.status, f"push crashed ({type(exc).__name__})")
        raise
    if record:
        record_status(args.status, outcome.failure, withheld=outcome.withheld)
    return outcome.code


def parts_of(args: argparse.Namespace) -> tuple[str, ...]:
    """The parts this push sends, in ``PARTS`` order."""
    if args.only:
        asked = {p.strip() for p in args.only.split(",") if p.strip()}
        unknown = asked - set(PARTS)
        if unknown:
            raise SystemExit(f"--only: unknown part(s) {', '.join(sorted(unknown))}; choose from {', '.join(PARTS)}")
        return tuple(p for p in PARTS if p in asked)
    return tuple(p for p in PARTS if p != "prices" or args.prices)


def push(args: argparse.Namespace) -> Outcome:
    """Do the push; how it went.

    The failure words are ``not configured``, ``project paused or
    unreachable`` or ``HTTP <code>`` (``store.remote.describe_failure``):
    never the remote's own text, which is still printed to the log as it
    always was. One part failing does not stop the others -- a table the
    SQL has not created yet must not keep the journal out -- but the push
    as a whole fails, and says why with the first failure.
    """
    outcome = Outcome()
    if not RemoteArchive.is_configured():
        print(
            "No remote archive configured (SUPABASE_URL / SUPABASE_SERVICE_KEY "
            "are unset); nothing to push. The local logs are unaffected."
        )
        outcome.failure = NOT_CONFIGURED
        return outcome

    try:
        archive = RemoteArchive.from_settings()
    except RemoteArchiveError as exc:
        print(exc, file=sys.stderr)
        outcome.fail(NOT_CONFIGURED)
        return outcome

    parts = parts_of(args)
    steps = {
        "signals": lambda: push_log(archive, args, SIGNALS, args.journal, loader.signal_row),
        "executions": lambda: push_log(archive, args, EXECUTIONS, args.audit, loader.execution_row),
        "account": lambda: push_account(archive, args),
        "model-io": lambda: push_model_io(archive, args, outcome),
        "prices": lambda: push_prices(archive, args, outcome),
    }
    for part in parts:
        try:
            steps[part]()
        except RemoteArchiveError as exc:
            print(f"Remote archive push failed ({part}): {exc}", file=sys.stderr)
            outcome.fail(describe_failure(exc))
    return outcome


def push_log(archive: RemoteArchive, args: argparse.Namespace, table: str, path: Path, build_row) -> None:
    """One log file into its table, from the remote's high-water mark on."""
    rows = rows_from(path, build_row)
    if not rows:
        print(f"{table}: nothing at {path}")
        return

    watermark = None if args.all else archive.latest_timestamp(table)
    pending = remote.select_new(rows, watermark)
    since = f" since {watermark}" if watermark else " (everything)"

    if args.dry_run:
        print(f"{table}: would send {len(pending)} of {len(rows)} rows{since}")
        return

    result = archive.push(table, pending)
    print(f"{result.describe()}{since}")


def push_account(archive: RemoteArchive, args: argparse.Namespace) -> None:
    """The account snapshots from the watermark on, and every fill in them.

    Fills are keyed on the broker's fill id, so a fill that two overlapping
    snapshots both read is stored once.
    """
    pairs = pairs_from(args.account, loader.account_row)
    if not pairs:
        print(f"{ACCOUNT_SNAPSHOTS}: nothing at {args.account}")
        return
    rows = [row for row, _ in pairs]
    watermark = None if args.all else archive.latest_timestamp(ACCOUNT_SNAPSHOTS)
    pending = remote.select_new(rows, watermark)
    picked = {row["line_hash"] for row in pending}
    fills: dict[str, dict[str, Any]] = {}
    for row, raw in pairs:
        if row["line_hash"] in picked:
            for fill in loader.fill_rows(raw):
                fills.setdefault(fill["fill_id"], fill)
    since = f" since {watermark}" if watermark else " (everything)"
    if args.dry_run:
        print(f"{ACCOUNT_SNAPSHOTS}: would send {len(pending)} of {len(rows)} rows{since}, "
              f"{len(fills)} fill(s)")
        return
    print(f"{archive.push(ACCOUNT_SNAPSHOTS, pending).describe()}{since}")
    print(archive.push(ACCOUNT_FILLS, list(fills.values()), key="fill_id").describe())


def push_model_io(archive: RemoteArchive, args: argparse.Namespace, outcome: Outcome) -> None:
    """Every capture file under ``--model-io``: its rows, its Storage object, its file row.

    Idempotent end to end: rows are keyed on the call id, the object is
    never overwritten (a re-send is "already there"), and the file row is
    keyed on the object's path. A file whose upload fails still sends its
    rows, and the push fails, so the phone hears about it the same day; the
    file is also the run's workflow artifact, which archive-push.yml can
    send again.
    """
    files = model_calls.capture_files(args.model_io)
    if not files:
        print(f"{MODEL_CALLS}: nothing at {args.model_io}")
        return
    first_error: Optional[RemoteArchiveError] = None
    for path in files:
        package = model_calls.package(path, args.model_io)
        withheld = package.withheld + package.withheld_before
        outcome.withheld += withheld
        note = f", {withheld} withheld as credential-shaped" if withheld else ""
        if args.dry_run:
            print(f"{package.object_path}: would send {len(package.rows)} call(s), "
                  f"{len(package.data)} bytes{note}")
            continue
        try:
            print(f"{archive.push(MODEL_CALLS, package.rows, key='call_id').describe()}{note}")
            stored = archive.upload_object(MODEL_IO_BUCKET, package.object_path, package.data,
                                           "application/gzip")
            print(f"{MODEL_IO_BUCKET}/{package.object_path}: "
                  f"{'stored' if stored else 'already there'} ({len(package.data)} bytes)")
            archive.push(MODEL_IO_FILES, [package.file_row(model_calls.run_of(package.rows))],
                         key="object_path")
        except RemoteArchiveError as exc:
            print(f"model-io push failed for {package.object_path}: {exc}", file=sys.stderr)
            first_error = first_error or exc
    if first_error is not None:
        raise first_error


def push_prices(archive: RemoteArchive, args: argparse.Namespace, outcome: Outcome) -> None:
    """Each ``--prices`` table: its distinct bars, and its run row. Refused whole if it does not check."""
    for path in args.prices:
        try:
            tape = scoring_prices.load(Path(path).read_text(encoding="utf-8"))
        except (OSError, scoring_prices.TapeError) as exc:
            print(f"{path}: not pushed: {exc}", file=sys.stderr)
            outcome.fail(PRICES_REFUSED)
            continue
        prices = scoring_prices.price_rows(tape, args.run_id)
        run = scoring_prices.run_row(tape, args.run_id)
        if args.dry_run:
            print(f"{path}: would send {len(prices)} distinct bar(s) of {len(tape['rows'])}, "
                  f"run {run['run_key']}")
            continue
        print(archive.push(SCORING_PRICES, prices, key="price_key").describe())
        print(archive.push(SCORING_RUNS, [run], key="run_key").describe())


def read_status(path: Path) -> dict[str, Any]:
    """The previous push's record, or an empty one if there is none to read."""
    try:
        previous = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return previous if isinstance(previous, dict) else {}


def status_after(previous: dict[str, Any], failure: Optional[str], now: datetime,
                 withheld: int = 0) -> dict[str, Any]:
    """This push's record: when it was tried, when one last worked, and why not.

    ``last_success`` is carried over from ``previous`` when this push did not
    work, so a week of failures still says when the archive last had
    everything -- the date the brief shows. A value there that is not a
    string is dropped rather than copied: this file is committed and read
    by the brief, and it only ever holds what this function wrote.

    ``withheld`` is how many model-call records this push withheld because
    they looked like they held a credential -- a number, never what matched.
    """
    stamp = now.astimezone(timezone.utc).isoformat(timespec="seconds")
    kept = previous.get("last_success")
    return {
        "last_attempt": stamp,
        "last_success": stamp if failure is None else (kept if isinstance(kept, str) else None),
        "ok": failure is None,
        "error": failure,
        "withheld": int(withheld),
    }


def render_status(status: dict[str, Any]) -> str:
    return json.dumps(status, indent=2) + "\n"


def record_status(path: Path, failure: Optional[str], now: Optional[datetime] = None,
                  withheld: int = 0) -> None:
    """Write this push's record to ``path``. Never raises: a record is not a reason to fail.

    The one file ``store/`` writes outside SQLite (the CI guardrail names
    this exact line). It is not a log this package reads as a source: it is
    this script's own note about itself, rewritten whole every time.
    """
    status = status_after(read_status(path), failure, now or datetime.now(timezone.utc), withheld)
    try:
        path.write_text(render_status(status), encoding="utf-8")
    except OSError as exc:
        print(f"could not write the push record to {path}: {type(exc).__name__}", file=sys.stderr)


def pairs_from(path: Path, build_row) -> list[tuple[dict[str, Any], str]]:
    """Every readable line of a log file, as (row, line). A missing file is empty."""
    if not journal_files.exists(path):
        return []
    pairs: list[tuple[dict[str, Any], str]] = []
    seen: set[str] = set()
    # The journal's monthly files joined in order, or one plain file.
    for line in journal_files.iter_lines(path):
        if not line.strip():
            continue
        row = build_row(line)
        if row is None or row["line_hash"] in seen:
            continue
        seen.add(row["line_hash"])
        pairs.append((row, line))
    return pairs


def rows_from(path: Path, build_row) -> list[dict[str, Any]]:
    """Every readable line of a log file, as rows. A missing file is empty.

    Unreadable lines are skipped silently here rather than counted: the local
    loader already reports them, and this tool's job is to move what parses,
    not to re-audit the file.
    """
    return [row for row, _ in pairs_from(path, build_row)]


if __name__ == "__main__":
    raise SystemExit(main())
