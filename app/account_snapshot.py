"""Record the real paper account as one JSON line on stdout. Reads only.

    python -m app.account_snapshot --log logs/account.jsonl --mode cycle >> logs/account.jsonl

The shadow funds run the production engine and position manager against a
simulated broker, and a simulation is only worth reading once it has been
shown to track the account it imitates. That comparison needs the account's
own numbers -- cash, equity at each close, what actually filled and at what
price, which stops are resting -- and until this existed the repository kept
none of them: the audit log records what was asked for, not what the broker
did. The heartbeat already holds the Alpaca keys, so it runs this once a run
and commits the line; everything that measures the funds then reads the
committed file and never needs a key of its own.

It never writes the file. It reads ``--log`` for one thing -- where the last
fills window ended -- and prints; the workflow appends. The whole line is
built before anything is printed, so a run killed mid-read leaves no half
line in the log.

It never fails the run that called it. Any exception becomes a one-line
``{"at", "sha", "mode", "error"}`` record and exit status 0: a recorder that
could turn a trading run red would be a recorder somebody eventually turns
off.

Line format (readers must tolerate fields they do not know):

    {"at": "2026-09-25T15:40:12Z", "sha": "<GITHUB_SHA>" | null, "mode": "cycle" | "protect",
     "account": {...} | null, "positions": [...] | null, "stops": [...] | null,
     "fills": [...] | null, "history": {"days": [...], "equity": [...]} | null,
     "fills_after": "<UTC ISO>", "reads": {"<part>": {"from": "<UTC ISO>", "to": "<UTC ISO>"}, ...},
     "errors": [{"part", "error"}, ...]}

Each part is described in ``AlpacaPaperBroker.account_snapshot``.
"""

from __future__ import annotations

import argparse
import contextlib
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Sequence

from app.broker_client import AlpacaPaperBroker

MODES = ("cycle", "protect")
#: Each fills window starts this long before the last snapshot that read its
#: fills. An activity is stamped with the moment it filled, and a fill made
#: just before one snapshot can reach the activity list just after that
#: snapshot read it; a window starting at the snapshot would never read it
#: again. The overlap costs a few fills recorded twice, with the same id,
#: which every reader deduplicates.
FILLS_OVERLAP = timedelta(hours=1)
#: A failure's text is kept to one line of this many characters.
ERROR_CHARS = 300


def utc_stamp(moment: datetime) -> str:
    """``2026-09-25T15:40:12Z``: UTC, to the second."""
    return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_at(value: object) -> Optional[datetime]:
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip()
    if text.endswith(("Z", "z")):
        text = text[:-1] + "+00:00"
    try:
        moment = datetime.fromisoformat(text)
    except ValueError:
        return None
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc)


def previous_at(log: Path) -> Optional[datetime]:
    """The latest earlier snapshot that actually read its fills; this
    snapshot's fills window starts ``FILLS_OVERLAP`` before it.

    Not simply the last line's ``at``. A run whose fills read failed -- its
    ``fills`` is null, or it is an error line with no ``fills`` at all -- read
    nothing for that window, and starting the next window after it would
    drop those fills from the record for good. Such lines are skipped, so the
    next snapshot reads the gap again.

    And the latest ``at`` rather than the last line, because the log merges
    as a union (.gitattributes): two runs that land at once keep both their
    lines, in either order. A line that does not parse is skipped. A missing
    or empty log means there is no window yet, and the broker falls back to
    its own lookback.
    """
    try:
        text = log.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return None
    latest: Optional[datetime] = None
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except ValueError:
            continue
        if not isinstance(record, dict) or not isinstance(record.get("fills"), list):
            continue
        at = _parse_at(record.get("at"))
        if at is not None and (latest is None or at > latest):
            latest = at
    return latest


def _failure_text(exc: BaseException) -> str:
    return " ".join(f"{type(exc).__name__}: {exc}".split())[:ERROR_CHARS]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Print one JSON line describing the paper account. Reads only; never writes --log."
    )
    parser.add_argument("--log", type=Path, required=True,
                        help="the account log, read only for where the last fills window ended")
    parser.add_argument("--mode", choices=MODES, required=True,
                        help="which heartbeat run recorded this line")
    args = parser.parse_args(argv)

    # Stamped before the broker is read: every part of the line was read
    # after this moment (``reads`` says exactly when). The next window starts
    # FILLS_OVERLAP before it, so a fill is recorded twice, with the same id,
    # rather than never.
    at = utc_stamp(datetime.now(timezone.utc))
    sha = os.environ.get("GITHUB_SHA") or None
    out = sys.stdout
    try:
        # Anything else that prints -- a library, a stray debug line -- goes
        # to stderr, so the workflow's `>>` appends exactly one line.
        with contextlib.redirect_stdout(sys.stderr):
            since = previous_at(args.log)
            if since is not None:
                since -= FILLS_OVERLAP
            body = AlpacaPaperBroker().account_snapshot(since)
        record = {"at": at, "sha": sha, "mode": args.mode, **body}
        line = json.dumps(record, separators=(",", ":"), allow_nan=False)
    except Exception as exc:  # noqa: BLE001 -- a recorder must never fail the run
        line = json.dumps(
            {"at": at, "sha": sha, "mode": args.mode, "error": _failure_text(exc)},
            separators=(",", ":"),
        )
    out.write(line + "\n")
    out.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
