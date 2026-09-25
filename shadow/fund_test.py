"""The fund test's start and its three bars, worked out from the day calibration ends.

The fund test starts on the first trading day after calibration ends, and
reads its three looks on the race's look days with O'Brien-Fleming bars from
its own share of its data at each (the owner's decision of 24 Sep 2026). The
registered start and bars in ``shadow.schedule`` were worked out from the
planned end, 2026-10-16.

Under the fail rule a fix can move calibration's end: it ends at day 15 or
at the last fix + 5 days, whichever is later. A later end is a later start,
fewer sessions to each look, and so different bars. The owner's rule is
that they are then recomputed by the same function and the change logged in
the Amendments table before the fund test starts; this is that computation,
so the 4 Funds page can say whether the registered numbers still hold.

Arithmetic on dates only: nothing is read, fetched or written.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import Optional, Sequence

from analysis.decision_gate import obrien_fleming_bars
from config.market_calendar import is_trading_day
from shadow import schedule
from shadow.schedule import FUND_TEST_LOOK_ESTIMATES


def next_trading_day(day: date) -> date:
    """The first trading day after ``day``."""
    day += timedelta(days=1)
    while not is_trading_day(day):
        day += timedelta(days=1)
    return day


def sessions_through(first: date, last: date) -> int:
    """Trading days from ``first`` to ``last``, both included; 0 when ``last`` is earlier."""
    count, day = 0, first
    while day <= last:
        if is_trading_day(day):
            count += 1
        day += timedelta(days=1)
    return count


def fund_test_plan(calibration_end: date, look_dates: Sequence[date] = FUND_TEST_LOOK_ESTIMATES) -> dict:
    """The fund test's start, sessions to each look, and bars, if calibration ends on ``calibration_end``.

    ``bars`` are rounded to 2 decimals as the race's are, ``exact`` to 3;
    ``matches_registered`` is whether the start and the rounded bars are
    still the ones in ``shadow.schedule``. A look on or before the start
    cannot be read by the fund test at all: it gets 0 sessions and no bar,
    the bars are those of the looks that remain, and the plan cannot match.
    That would be a new design for the owner to decide, not a detail. A
    look on the start day itself is one of those: read after the funds'
    first session alone, its bar would be about 22, which nothing reaches.
    """
    start = next_trading_day(calibration_end)
    sessions = [sessions_through(start, look) if look > start else 0 for look in look_dates]
    readable = [n for n in sessions if n > 0]
    computed = iter(obrien_fleming_bars(readable) if readable else [])
    exact: list[Optional[float]] = [next(computed) if n > 0 else None for n in sessions]
    bars = [None if b is None else round(b, 2) for b in exact]
    registered = list(schedule.FUND_TEST_BARS)
    return {
        "start": start.isoformat(),
        "sessions": sessions,
        "bars": bars,
        "exact": [None if b is None else round(b, 3) for b in exact],
        "registered": registered,
        "registered_start": schedule.FUND_TEST_PLANNED_START.isoformat(),
        "matches_registered": start == schedule.FUND_TEST_PLANNED_START and bars == registered,
    }


__all__ = ["fund_test_plan", "next_trading_day", "sessions_through"]
