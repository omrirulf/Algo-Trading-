"""Which days the market trades on, without asking anyone.

Not authoritative. The broker's own clock, checked downstream, is what
actually decides whether an order can be placed -- this is only the free
thing to check before that, on the days that check is skipped or before it is
worth paying for eighty tickers of context to find out. See ``heartbeat.py``:
the pre-market cycle gives up the broker's market-hours gate to run before the
open, and this is what stands in its place.
"""

from __future__ import annotations

import logging
from datetime import date
from typing import Final

log = logging.getLogger(__name__)

#: Full-day NYSE closures, by year. A half day -- the Friday after
#: Thanksgiving, Christmas Eve some years -- is deliberately absent: the
#: market is genuinely open then, just for fewer hours, and treating it as
#: closed would cost a real session rather than a wasted one.
#:
#: Good Friday has no calendar rule of its own -- it moves with Easter -- so
#: it is entered by hand each year rather than derived. Juneteenth has been a
#: NYSE holiday since 2022, which is why it is present from 2025 on and would
#: need removing, not adding, for an equivalent list before that.
#:
#: Extend this a year at a time as each one approaches. A year missing
#: entirely does not stop the cycle -- see ``is_trading_day``.
NYSE_HOLIDAYS: Final[frozenset[date]] = frozenset({
    # 2025
    date(2025, 1, 1), date(2025, 1, 20), date(2025, 2, 17), date(2025, 4, 18),
    date(2025, 5, 26), date(2025, 6, 19), date(2025, 7, 4), date(2025, 9, 1),
    date(2025, 11, 27), date(2025, 12, 25),
    # 2026
    date(2026, 1, 1), date(2026, 1, 19), date(2026, 2, 16), date(2026, 4, 3),
    date(2026, 5, 25), date(2026, 6, 19), date(2026, 7, 3), date(2026, 9, 7),
    date(2026, 11, 26), date(2026, 12, 25),
    # 2027
    date(2027, 1, 1), date(2027, 1, 18), date(2027, 2, 15), date(2027, 3, 26),
    date(2027, 5, 31), date(2027, 6, 18), date(2027, 7, 5), date(2027, 9, 6),
    date(2027, 11, 25), date(2027, 12, 24),
})

#: The last year this list actually has entries for. Read by
#: ``is_trading_day`` so a call past it can say so, rather than silently
#: answering from a list that has quietly run out.
LAST_COVERED_YEAR: Final[int] = max(d.year for d in NYSE_HOLIDAYS)


def is_trading_day(day: date) -> bool:
    """Whether the NYSE trades at all on ``day`` -- a weekday, not a holiday.

    Says nothing about *hours*: a half day passes this check, because the
    market is genuinely open, just for less of it. This is the cheap gate
    before the broker's own clock, not a replacement for it.

    Past ``LAST_COVERED_YEAR`` the answer can only ever mean "not a
    known holiday" rather than "definitely trading" -- logged once so the gap
    stays visible without failing the cycle over it. Defaulting to "trading"
    here is deliberate: it degrades to exactly the behaviour before this
    check existed, a wasted pre-market cycle on the rare day it is wrong,
    rather than a real session silently skipped because a list nobody updated
    misread a trading day as a holiday.
    """
    if day.year > LAST_COVERED_YEAR:
        log.warning(
            "NYSE_HOLIDAYS has no entries for %d (covers through %d); "
            "assuming %s is a trading day",
            day.year, LAST_COVERED_YEAR, day,
        )
    return day.weekday() < 5 and day not in NYSE_HOLIDAYS


__all__ = ["NYSE_HOLIDAYS", "LAST_COVERED_YEAR", "is_trading_day"]
