"""Did a cycle actually run today?

The 16 Sep schedule never fired. Not late, not failed -- GitHub simply never
created the run, and nothing noticed. A trading day would have been lost in
silence if an unrelated reminder had not happened to look.

A second scheduled run later in the day fixes that, but only if it can tell
whether the first one happened. This answers that question from the one
artifact that proves it: the journal, which the cycle commits to the
repository at the end of every run. One entry dated today means a cycle ran
today.

Two things make this the right evidence rather than merely the easiest:

* It is committed, so a fresh checkout can read it. A workflow run's status
  would need an API call, a token and a permission; the journal needs none.
* It is what the rest of the system is scored from. A cycle whose journal
  never landed is, to every later measurement, a cycle that did not happen --
  so re-running is the repair, not a duplicate.

That last point is only safe because the broker refuses a second order for
the same ticker and side inside the same UTC day (see
``broker_client.build_client_order_id``). A catch-up run therefore cannot
double a position the lost run already opened; at worst it pays for one more
cycle's model calls and writes the record that went missing.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from analysis.reader import JournalEntry, read_journal  # noqa: E402


def cycle_ran_on(entries: Iterable[JournalEntry], day: date) -> bool:
    """Whether any journal entry was written on ``day``, in UTC.

    Entries with no readable timestamp do not count. A line that cannot say
    when it happened cannot prove that today is covered, and treating it as
    proof would skip the catch-up on exactly the days the journal is damaged.
    """
    for entry in entries:
        stamp = entry.timestamp
        if stamp is None:
            continue
        if stamp.astimezone(timezone.utc).date() == day:
            return True
    return False


def _today(value: Optional[str]) -> date:
    return date.fromisoformat(value) if value else datetime.now(timezone.utc).date()


def main(argv: Optional[list[str]] = None) -> int:
    """Print ``yes`` or ``no`` and exit 0 either way.

    A non-zero exit would be indistinguishable from the script itself
    breaking, and the caller must be able to tell "no cycle today" from "the
    check failed" -- those call for opposite actions.
    """
    parser = argparse.ArgumentParser(description="Has a cycle run today?")
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--day", default=None, help="ISO date, default today in UTC")
    args = parser.parse_args(argv)

    day = _today(args.day)
    try:
        entries = read_journal(args.journal).entries
    except FileNotFoundError:
        # No journal at all is the strongest possible "no cycle today".
        print("no")
        print(f"no journal at {args.journal}", file=sys.stderr)
        return 0

    ran = cycle_ran_on(entries, day)
    print("yes" if ran else "no")
    print(f"{'found' if ran else 'no'} journal entries for {day.isoformat()}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
