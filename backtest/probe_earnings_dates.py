#!/usr/bin/env python3
"""Could past earnings surprises be backfilled onto the journal without look-ahead?

    python backtest/probe_earnings_dates.py

An earnings-surprise arm needs, for every journal line, only the surprises
*announced before that line's timestamp*. The Finnhub endpoint the cycle
reads (``/stock/earnings``) reports each surprise by fiscal quarter, not by
the date it was announced -- so a row from it cannot be placed in time on
its own, and a backfill built from it alone would leak. Yahoo's earnings
calendar carries the announcement timestamp beside the estimate, the
reported figure and the surprise, which is what a safe backfill would join
on.

This asks both sources what they actually return for every company on the
watchlist, and prints only shape and coverage: how many announcements, the
earliest and latest, whether the timestamp carries a time of day (a report
before the open is known to that day's line; one after the close is not),
how many fall inside the journal's span, and which keys a Finnhub row has.
It builds nothing. Whether an arm is worth building is a later question,
and a separate registration.

Needs the open internet (and the Finnhub key for that half), so it runs on
a runner. No key value is ever printed. Read-only: no orders, no model.
"""

from __future__ import annotations

import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config.instruments import SINGLE_NAMES  # noqa: E402
from orchestrator import sources  # noqa: E402

#: The first journal line. Announcements before it could only ever be
#: history in a prompt; the ones after it are what an arm would trade on.
JOURNAL_START = date(2026, 9, 15)


def _as_utc(value: Any) -> Optional[datetime]:
    try:
        import pandas as pd

        stamp = pd.Timestamp(value)
    except (TypeError, ValueError):
        return None
    if stamp.tzinfo is None:
        return stamp.to_pydatetime().replace(tzinfo=timezone.utc)
    return stamp.tz_convert("UTC").to_pydatetime()


def probe_yahoo(ticker: str) -> str:
    try:
        import yfinance as yf

        frame = yf.Ticker(ticker).earnings_dates
    except Exception as exc:  # noqa: BLE001 - a dead source is the finding
        return f"{ticker:<6} yahoo: FAILED {type(exc).__name__}: {exc}"
    if frame is None or getattr(frame, "empty", True):
        return f"{ticker:<6} yahoo: no earnings-date rows"

    stamps = [s for s in (_as_utc(ix) for ix in frame.index) if s is not None]
    reported = frame.get("Reported EPS")
    with_actual = int(reported.notna().sum()) if reported is not None else 0
    surprise = frame.get("Surprise(%)")
    with_surprise = int(surprise.notna().sum()) if surprise is not None else 0
    today = datetime.now(timezone.utc)
    past = [s for s in stamps if s <= today]
    in_span = [s for s in past if s.date() >= JOURNAL_START]
    timed = sum(1 for s in stamps if (s.hour, s.minute) != (0, 0))
    span = f"{min(stamps).date()} .. {max(stamps).date()}" if stamps else "n/a"
    return (
        f"{ticker:<6} yahoo: {len(frame)} rows ({span}); reported EPS on {with_actual}, "
        f"surprise% on {with_surprise}; {len(past)} already announced, {len(in_span)} since "
        f"{JOURNAL_START}; time-of-day present on {timed}/{len(stamps)}"
    )


def probe_finnhub(ticker: str) -> str:
    if not sources.api_key("finnhub"):
        return f"{ticker:<6} finnhub: no key in this environment"
    try:
        rows = sources.fetch_earnings_rows(ticker)
    except Exception as exc:  # noqa: BLE001
        return f"{ticker:<6} finnhub: FAILED {type(exc).__name__}"
    if not rows:
        return f"{ticker:<6} finnhub: no rows"
    keys = sorted({str(k) for row in rows if isinstance(row, dict) for k in row})
    periods = [str(r.get("period")) for r in rows if isinstance(r, dict)]
    return (
        f"{ticker:<6} finnhub: {len(rows)} rows, keys {keys}; periods "
        f"{min(periods)} .. {max(periods)}"
    )


def main() -> int:
    print("EARNINGS SURPRISES: COULD THEY BE BACKFILLED WITHOUT LOOK-AHEAD?")
    print("=" * 78)
    print(f"journal starts {JOURNAL_START}; a safe backfill uses only announcements before each line")
    print()
    print("Yahoo earnings calendar (announcement timestamp + estimate + reported + surprise)")
    print("-" * 78)
    for ticker in SINGLE_NAMES:
        print(probe_yahoo(ticker))
    print()
    print("Finnhub /stock/earnings (what the cycle reads today)")
    print("-" * 78)
    for ticker in SINGLE_NAMES:
        print(probe_finnhub(ticker))
    print()
    print("HOW TO READ THIS")
    print("-" * 78)
    print("A Finnhub row without an announcement date cannot be placed in time on")
    print("its own. If Yahoo's rows carry a timestamp with a time of day, they can")
    print("be joined to a journal line by 'announced before this line', which is")
    print("the only honest backfill. Nothing here builds an arm.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
