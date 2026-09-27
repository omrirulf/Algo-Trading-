"""The slices a screen is read over, and the few sums every slice needs.

Every result is shown over the whole history and split at 2010 (the owner's
request), and -- the process of 27 Sep 2026 -- over the years after the
rule's source was published, when those are not already the whole history.
A trade belongs to the slice of its entry day; a fund's session to the slice
of its date.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass
from datetime import date
from typing import Final, Optional, Sequence

from analysis.horse_race import newey_west_t
from analysis.multiple_tests import p_two_sided


@dataclass(frozen=True)
class Period:
    name: str
    first: Optional[date] = None
    last: Optional[date] = None

    def contains(self, day: date) -> bool:
        return (self.first is None or day >= self.first) and (self.last is None or day <= self.last)


SPLIT: Final[date] = date(2010, 1, 1)
ALL: Final[Period] = Period("all years")
BEFORE_2010: Final[Period] = Period("before 2010", None, date(2009, 12, 31))
FROM_2010: Final[Period] = Period("2010 on", SPLIT, None)

#: Each rule's published source, and the year it was published (None: no source).
SOURCES: Final[dict[str, tuple[str, Optional[int]]]] = {
    "momentum": ("Moskowitz, Ooi and Pedersen (2012), Time Series Momentum", 2012),
    "momentum_200": ("Brock, Lakonishok and LeBaron (1992)", 1992),
    "vt_timing": ("Faber (2007)", 2007),
    "momentum_pullback": ("none: the owner's fixed choice", None),
}


def periods_for(rule: str, first_day: Optional[date] = None) -> list[Period]:
    """The slices a rule is read over: all, before 2010, 2010 on, and after its source when that is shorter."""
    out = [ALL, BEFORE_2010, FROM_2010]
    year = SOURCES.get(rule, ("", None))[1]
    if year is not None:
        after = date(year + 1, 1, 1)
        if first_day is None or after > first_day:
            out.append(Period(f"after the source ({year + 1} on)", after, None))
    return out


def test_of(diffs: Sequence[float], lag: int) -> dict:
    """Mean difference, Newey-West t at ``lag`` (the race's own), two-sided p, and the number of days."""
    t = newey_west_t(list(diffs), lag) if len(diffs) >= 2 else None
    return {"days": len(diffs), "mean": statistics.fmean(diffs) if diffs else None, "t": t, "p": p_two_sided(t)}


def annualised(total: Optional[float], sessions: int) -> Optional[float]:
    """A total return over ``sessions`` trading days, as a yearly rate (252 sessions a year)."""
    if total is None or sessions <= 0 or total <= -1.0:
        return None
    return (1.0 + total) ** (252.0 / sessions) - 1.0


def max_drawdown(values: Sequence[float]) -> Optional[float]:
    """The deepest fall from a high, as a share of that high (``shadow.run.max_drawdown``'s rule)."""
    if not values:
        return None
    peak, worst = -math.inf, 0.0
    for value in values:
        peak = max(peak, value)
        if peak > 0:
            worst = max(worst, 1.0 - value / peak)
    return worst


def welch(a: Sequence[float], b: Sequence[float]) -> Optional[float]:
    """Welch's t of mean(a) - mean(b); for reading only."""
    if len(a) < 2 or len(b) < 2:
        return None
    se = math.sqrt(statistics.variance(a) / len(a) + statistics.variance(b) / len(b))
    return (statistics.fmean(a) - statistics.fmean(b)) / se if se > 0 else None


__all__ = ["ALL", "BEFORE_2010", "FROM_2010", "Period", "SOURCES", "SPLIT", "annualised", "max_drawdown",
           "periods_for", "test_of", "welch"]
