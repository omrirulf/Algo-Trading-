"""The fund test's looks and their bars, from its fixed start.

The fund test's start is fixed (the owner's decision of 26 Sep 2026): the
funds act on the cycle journalled on 2026-09-28, so the first fund session
is 2026-09-29 (``shadow.schedule.FUND_START``), whenever calibration ends.
It reads its three looks on the race's look days, with bars from an
O'Brien-Fleming-type alpha-spending rule on its own share of its data at
each (``analysis.decision_gate.spending_bars``): the share is the look's
fund sessions over the planned final sessions (180), and the final look
counts as 1.

What calibration's end still changes is which looks can be read. The fund
test counts only after calibration passes, and a look that comes before
calibration has passed is skipped: it is not read, spends none of the 5%,
and uses no bar; the next look's bar comes from the same rule with the bars
actually used before it. This works that out from calibration's estimated
end, so the 4 Funds page can say whether the planned bars still hold.

Arithmetic on dates only: nothing is read, fetched or written.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import Optional, Sequence

from analysis.decision_gate import rounded_bar, spending_bars
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


def skipped_look(look: date, calibration_end: Optional[date]) -> bool:
    """Whether a look comes before calibration has passed, and so is skipped.

    Calibration can pass only on its last day's close, judged that night,
    so a look on or before that day is skipped: the fund test has no
    counted result to read there. With no end known (``None``) nothing is
    skipped here; the caller says so.
    """
    return calibration_end is not None and look <= calibration_end


def fund_test_plan(calibration_end: Optional[date] = None,
                   look_dates: Sequence[date] = FUND_TEST_LOOK_ESTIMATES,
                   planned_final: Optional[int] = None) -> dict:
    """Fund sessions to each look from the fixed start, which looks are skipped, and the bars.

    ``calibration_end`` is the day calibration ends if nothing more fails
    (``shadow.calibration.estimated_end``); a look on or before it is
    skipped (``skipped_look``). Each look read gets the spending rule's bar
    at share = its fund sessions / ``planned_final`` (the planned final
    sessions, 180), the last look read counting as 1, given the bars of the
    looks read before it; a skipped look gets no bar. ``bars`` are printed
    as the pre-registration prints them (``rounded_bar``), ``exact`` to 3
    decimals. ``matches_registered`` is whether no look is skipped and the
    sessions and bars are the planned ones in ``shadow.schedule``.
    """
    start = schedule.FUND_START
    final = planned_final if planned_final is not None else schedule.FUND_TEST_PLANNED_SESSIONS[-1]
    sessions = [sessions_through(start, look) for look in look_dates]
    skipped = [skipped_look(look, calibration_end) or n == 0 for look, n in zip(look_dates, sessions)]
    read = [k for k, skip in enumerate(skipped) if not skip]
    shares = [min(1.0, sessions[k] / final) for k in read]
    if shares:
        shares[-1] = 1.0 if read[-1] == len(look_dates) - 1 else shares[-1]
    computed = spending_bars(shares) if shares else []
    exact: list[Optional[float]] = [None] * len(look_dates)
    for k, bar in zip(read, computed):
        exact[k] = bar
    bars = [None if b is None else rounded_bar(b) for b in exact]
    registered = list(schedule.FUND_TEST_BARS)
    return {
        "start": start.isoformat(),
        "first_cycle": schedule.FUND_FIRST_CYCLE.isoformat(),
        "sessions": sessions,
        "skipped": skipped,
        "bars": bars,
        "exact": [None if b is None else round(b, 3) for b in exact],
        "registered": registered,
        "registered_sessions": list(schedule.FUND_TEST_PLANNED_SESSIONS),
        "registered_start": schedule.FUND_TEST_PLANNED_START.isoformat(),
        "matches_registered": (not any(skipped) and sessions == list(schedule.FUND_TEST_PLANNED_SESSIONS)
                               and bars == registered),
    }


__all__ = ["fund_test_plan", "next_trading_day", "sessions_through", "skipped_look"]
