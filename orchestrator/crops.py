"""How the crop is actually doing, from the people who walk the fields.

A grain fund tracks one number: how much of the thing there will be. The
United States Department of Agriculture publishes exactly that -- weekly
condition ratings through the growing season, county by county, aggregated
nationally -- and it is free.

The measure here is the share of the crop rated **good or excellent**. It is
the number the grain trade quotes, it is directly comparable week to week,
and its *direction* is the signal: a crop deteriorating three weeks running
is a supply story whatever the level.

Two honest limits, both stated in the prompt rather than left implied:

* **It is seasonal.** Condition is reported while the crop is in the ground
  and not at all outside that window. Out of season the section is absent
  rather than showing a stale summer reading as though it were news.

  This is not theoretical, and the shape it takes is nastier than a simple
  gap. USDA labels winter wheat by its *harvest* year, so in September a
  request for 2026 returns ``WEEK #47`` -- a week that has not happened yet
  in 2026, because the reading is from November of the year before. Printed
  as "week 47 of 2026" it reads as the freshest number in the block while
  being ten months old. Every reading is therefore aged against the calendar,
  wrapping the year, and anything older than ``MAX_READING_AGE_WEEKS`` is
  dropped -- which correctly leaves wheat with no section between seasons.
* **The market has already seen it.** These are published on a schedule that
  everyone trades. The edge, if any, is in the trend and the comparison to
  the same week last year, not in the number itself.

Absent is not failed. With no key nothing is fetched, exactly as for a ticker
that has no crop exposure.

Pure parsing, like its siblings. ``orchestrator.sources`` does the fetching,
because it is the one module on this side permitted to read a credential.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any, Optional

from orchestrator import formatting as fmt

#: ``ticker -> (USDA commodity, plain-English name)``. CANE tracks sugar,
#: which the USDA reports for sugarcane rather than for "sugar".
COMMODITIES = {
    "CORN": ("CORN", "corn"),
    "WEAT": ("WHEAT", "wheat"),
    "SOYB": ("SOYBEANS", "soybeans"),
    "CANE": ("SUGARCANE", "sugarcane"),
}

#: The two buckets that make up the quoted figure.
GOOD_ENOUGH = ("PCT GOOD", "PCT EXCELLENT")

#: Weeks of readings kept. A season, so the trend has somewhere to run.
MAX_WEEKS = 30

#: Fewer readings than this and there is no trend to speak of, only a number.
MIN_WEEKS_FOR_TREND = 3

#: How old the latest reading may be and still be called current. USDA
#: publishes weekly in season, so a fortnight covers an ordinary gap; past
#: this the crop is between seasons and there is nothing to report.
MAX_READING_AGE_WEEKS = 5

#: Change over the trend window past which the crop is called improving or
#: deteriorating rather than steady. Condition ratings are noisy by a point
#: or two from rain alone.
TREND_EDGE = 3.0


def commodity_for(ticker: str) -> Optional[tuple[str, str]]:
    """``(USDA commodity, plain name)`` for a ticker, or ``None``."""
    return COMMODITIES.get(ticker.strip().upper())


def _week_number(text: Any) -> Optional[int]:
    """``"WEEK #22"`` -> ``22``. Anything else is not a weekly reading."""
    raw = str(text or "").strip().upper()
    if not raw.startswith("WEEK #"):
        return None
    try:
        return int(raw[len("WEEK #"):].strip())
    except ValueError:
        return None


def weeks_old(week: int, today: Optional[date] = None) -> int:
    """How many weeks back a reading labelled ``week`` actually is.

    Wraps the year, because a reading whose week number is *ahead* of today's
    belongs to the previous calendar year -- which is exactly what a winter
    crop labelled by its harvest year produces.
    """
    current = (today or date.today()).isocalendar()[1]
    age = current - week
    return age if age >= 0 else age + 52


def _percent(text: Any) -> Optional[float]:
    raw = str(text or "").strip().replace(",", "")
    if not raw or raw.startswith("("):  # USDA writes withheld values as "(D)"
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def good_or_excellent(rows: Any) -> dict[int, float]:
    """``{week number: percent good or excellent}`` from raw USDA rows."""
    totals: dict[int, float] = {}
    if not isinstance(rows, list):
        return {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        if str(row.get("unit_desc", "")).strip().upper() not in GOOD_ENOUGH:
            continue
        week = _week_number(row.get("reference_period_desc"))
        value = _percent(row.get("Value"))
        if week is None or value is None:
            continue
        totals[week] = totals.get(week, 0.0) + value
    return dict(sorted(totals.items()))


def _direction(change: Optional[float]) -> str:
    if change is None:
        return "not enough readings to say"
    if change > TREND_EDGE:
        return "improving"
    if change < -TREND_EDGE:
        return "deteriorating"
    return "steady"


@dataclass(frozen=True)
class CropSnapshot:
    """The condition of one crop, and which way it is going."""

    ticker: str = ""
    crop: str = ""
    year: int = 0
    week: Optional[int] = None
    condition: Optional[float] = None
    change: Optional[float] = None
    weeks: int = 0
    last_year: Optional[float] = None
    history: list[float] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        week = f"week {self.week}" if self.week else "the latest week"
        lines = [
            f"{self.crop.capitalize()} rated good or excellent: "
            f"{fmt.num(self.condition, 0)}% of the US crop ({week} of {self.year})"
        ]
        lines.append(
            f"Direction over {self.weeks} weeks: {_direction(self.change)}"
            + (f", {'+' if (self.change or 0) > 0 else ''}{fmt.num(self.change, 0)} points"
               if self.change is not None else "")
        )
        if self.last_year is not None:
            gap = (self.condition or 0.0) - self.last_year
            lines.append(
                f"Same week last year: {fmt.num(self.last_year, 0)}% "
                f"({'+' if gap > 0 else ''}{fmt.num(gap, 0)} points)"
            )
        lines.append(
            "A better crop means more supply, which reads bearish for the price, "
            "and a worse one bullish. The trend matters more than the level, and "
            "the market has already seen this: it is published on a schedule "
            "everyone trades."
        )
        return lines


def build_snapshot(
    ticker: str,
    rows: Any = None,
    prior_rows: Any = None,
    year: Optional[int] = None,
    today: Optional[date] = None,
) -> Optional[CropSnapshot]:
    """The crop block for one ticker, or ``None`` out of season.

    ``None`` rather than a stale summer reading in January: condition is
    reported while the crop is in the ground and not otherwise, and a figure
    presented as current when it is four months old is the kind of
    usable-looking wrong number this project keeps having to remove.
    """
    mapping = commodity_for(ticker)
    if mapping is None:
        return None
    _, name = mapping

    weekly = good_or_excellent(rows)
    if not weekly:
        return None

    # Age first, and against the calendar rather than against the other
    # readings: a set of rows can be internally consistent and still be from
    # last November. See the module docstring for the case that taught us.
    fresh = {w: v for w, v in weekly.items() if weeks_old(w, today) <= MAX_READING_AGE_WEEKS}
    if not fresh:
        return None

    weeks = sorted(fresh)[-MAX_WEEKS:]
    values = [fresh[w] for w in weeks]
    latest_week = weeks[-1]

    change = None
    if len(values) >= MIN_WEEKS_FOR_TREND:
        change = values[-1] - values[-MIN_WEEKS_FOR_TREND]

    prior = good_or_excellent(prior_rows)
    last_year = prior.get(latest_week)

    return CropSnapshot(
        ticker=ticker.strip().upper(),
        crop=name,
        year=year or date.today().year,
        week=latest_week,
        condition=values[-1],
        change=change,
        weeks=min(len(values), MIN_WEEKS_FOR_TREND),
        last_year=last_year,
        history=values,
    )


__all__ = [
    "CropSnapshot",
    "build_snapshot",
    "commodity_for",
    "good_or_excellent",
    "weeks_old",
    "COMMODITIES",
    "MAX_READING_AGE_WEEKS",
]
