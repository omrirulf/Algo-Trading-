"""The sessions of the past: the days SPY traded.

``config.market_calendar`` lists NYSE holidays for 2025 to 2027 only, and
answers "a trading day" for any other weekday -- right for the live system,
which only ever asks about this year, and wrong for 2000 to 2024, where it
would take every Good Friday, Thanksgiving and Christmas for a session, and
the days the exchange was shut (11-14 Sep 2001, 29-30 Oct 2012, the national
days of mourning) with them.

Two pieces of the registered code count sessions with it: C's "valid for the
3 sessions after the signal's day" (``shadow.exploratory.sessions_after``) and
B's "the month's last trading day" (``shadow.exploratory.last_trading_day``),
and the funds' calendar filters with it (``shadow.market.calendar``). A
holiday counted as a session would shorten C's window and move B's month-end.
So, for a screen only, those two modules are handed a calendar read from the
prices themselves: a day is a session if SPY has a final bar for it. After
the last bar the production calendar answers, as it always does.

Nothing else changes: the rule code is the registered code, and outside
``historical_calendar`` both modules read ``config.market_calendar`` again.
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import date
from typing import Callable, Iterable, Iterator

from config import market_calendar

#: The modules whose ``is_trading_day`` a screen replaces, by import path.
PATCHED: tuple[str, ...] = ("shadow.market", "shadow.exploratory")


def trading_day(sessions: Iterable[date]) -> Callable[[date], bool]:
    """``is_trading_day`` for the past: a day SPY traded; after the last one, production's answer."""
    known = frozenset(sessions)
    if not known:
        return market_calendar.is_trading_day
    first, last = min(known), max(known)

    def is_trading_day(day: date) -> bool:
        if first <= day <= last:
            return day in known
        if day > last:
            return market_calendar.is_trading_day(day)
        return day.weekday() < 5          # before the data: nothing asks, but answer like production would

    return is_trading_day


@contextmanager
def historical_calendar(sessions: Iterable[date]) -> Iterator[Callable[[date], bool]]:
    """Inside the block, the patched modules count sessions on ``sessions``; after it, as before."""
    import importlib

    calendar = trading_day(sessions)
    modules = [importlib.import_module(name) for name in PATCHED]
    saved = [module.is_trading_day for module in modules]
    try:
        for module in modules:
            module.is_trading_day = calendar
        yield calendar
    finally:
        for module, original in zip(modules, saved):
            module.is_trading_day = original


def production_differences(sessions: Iterable[date], first: date, last: date) -> dict[str, list[str]]:
    """Where the price calendar and ``config.market_calendar`` disagree, from ``first`` to ``last``.

    For the report: in the years the production list covers, every
    disagreement should be a day the exchange closed for something the list
    does not carry (a day of mourning), never a holiday.
    """
    from datetime import timedelta

    known = frozenset(sessions)
    extra, missing = [], []
    day = first
    while day <= last:
        prod = market_calendar.is_trading_day(day)
        ours = day in known
        if ours and not prod:
            extra.append(day.isoformat())
        elif prod and not ours:
            missing.append(day.isoformat())
        day += timedelta(days=1)
    return {"traded_but_production_says_closed": extra, "no_bar_but_production_says_open": missing}


__all__ = ["PATCHED", "historical_calendar", "production_differences", "trading_day"]
