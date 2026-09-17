"""Where the official forecaster says the price is going.

Every month the Energy Information Administration publishes its Short-Term
Energy Outlook: a month-by-month forecast of the spot prices that the energy
funds on the watchlist actually track -- WTI and Brent crude, and Henry Hub
natural gas -- running about a year and a half ahead. It is free, it is the
number the trade quotes when it says "EIA sees oil at sixty next year", and
until now the model was asked to judge an oil fund with a chart, a day of
headlines and last week's inventories, but no view of where anyone official
thinks the price is headed.

What the block says, per series: the outlook's figure for this month, the
figures three and six months out, next calendar year's average, and the
direction those imply in one phrase. Three horizons rather than one because
a forecast that dips and recovers and one that falls all the way are
different stories at the same six-month point.

Two honest limits, stated in the prompt rather than left implied:

* **It is one agency's view.** The EIA has been wrong, sometimes by a lot,
  and the market has read the same document. The edge, if any, is in the
  direction and in the gap between the forecast and today's price, not in
  the level.
* **It is monthly.** An outlook published on the tenth is the same document
  on the thirtieth. The block does not pretend otherwise: it carries no
  "on the week" figures, because there are none.

Absent is not failed. With no EIA key nothing is fetched and the section is
omitted, exactly as it is for a ticker with no energy exposure. A payload
that arrives without this month, or without any month ahead of it, is also
nothing: a forecast that cannot say "from here" is not one.

Pure parsing, like its siblings. ``orchestrator.sources`` does the fetching,
because it is the one module on this side permitted to read a credential.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any, Optional

from orchestrator import formatting as fmt

#: The STEO route under EIA's v2 API. Its facet is ``seriesId``.
ROUTE = "steo"

#: ``label -> (STEO series id, unit, plain-English name)``. Table 2 of the
#: outlook, "Energy Prices": the spot averages, not the refiner acquisition
#: costs or the retail prices.
SERIES = {
    "wti": ("WTIPUUS", "$/barrel", "WTI crude"),
    "brent": ("BREPUUS", "$/barrel", "Brent crude"),
    "henry_hub": ("NGHHUUS", "$/million BTU", "Henry Hub natural gas"),
}

#: Which tickers get this section, and which series each is asked about.
#: The same funds as the inventory block and for the same reason: an energy
#: fund is a bet on these prices; a company with energy exposure already has
#: fundamentals, analysts and filings of its own, and the company prompt is
#: the input every baseline was measured against.
COVERAGE = {
    "USO": ("wti", "brent"),
    "UNG": ("henry_hub",),
    "XLE": ("wti", "henry_hub"),
    "DBC": ("wti", "henry_hub"),
}

#: Months ahead of this month that are read out, in order.
HORIZONS_MONTHS = (3, 6)

#: How many of next year's twelve months must be present before their mean
#: is called "next year's average". Half: the outlook's last edition of a
#: year still runs past the following December.
MIN_MONTHS_FOR_YEAR_AVERAGE = 6

#: Rows to ask for. The outlook runs about eighteen months ahead and the
#: route returns newest first, so this covers the whole forecast and a few
#: months of history for the "this month" row whatever the edition date.
ROW_LIMIT = 36

#: A six-month change smaller than this is "roughly flat".
FLAT_EDGE_PCT = 2.0

MONTH_NAMES = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")


def series_for(ticker: str) -> tuple[str, ...]:
    """The series labels a ticker is asked about, or nothing."""
    return COVERAGE.get(ticker.strip().upper(), ())


def _rows(payload: Any) -> list[dict]:
    if not isinstance(payload, dict):
        return []
    response = payload.get("response")
    if not isinstance(response, dict):
        return []
    data = response.get("data")
    return [row for row in data if isinstance(row, dict)] if isinstance(data, list) else []


def _value(row: dict) -> Optional[float]:
    raw = row.get("value")
    if fmt.is_missing(raw):
        return None
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def _month(text: Any) -> Optional[tuple[int, int]]:
    """``"2026-09"`` -> ``(2026, 9)``. Anything else is not a monthly period."""
    raw = str(text or "").strip()
    if len(raw) < 7 or raw[4] != "-":
        return None
    try:
        year, month = int(raw[:4]), int(raw[5:7])
    except ValueError:
        return None
    if not 1 <= month <= 12:
        return None
    return year, month


def _add_months(month: tuple[int, int], count: int) -> tuple[int, int]:
    year, mon = month
    index = (year * 12 + (mon - 1)) + count
    return index // 12, index % 12 + 1


def month_label(month: tuple[int, int]) -> str:
    return f"{MONTH_NAMES[month[1] - 1]} {month[0]}"


def by_month(payload: Any) -> dict[tuple[int, int], float]:
    """``{(year, month): value}`` from a raw STEO payload."""
    out: dict[tuple[int, int], float] = {}
    for row in _rows(payload):
        month = _month(row.get("period"))
        value = _value(row)
        if month is not None and value is not None:
            out[month] = value
    return out


@dataclass(frozen=True)
class Point:
    """One month of the outlook."""

    months_ahead: int
    period: str
    value: float


@dataclass(frozen=True)
class Forecast:
    """The outlook for one price."""

    label: str = ""
    name: str = ""
    unit: str = ""
    #: This month's figure, and the month it is for.
    now: Optional[Point] = None
    #: The horizons that arrived, in order.
    ahead: list[Point] = field(default_factory=list)
    #: ``(year, mean)`` of next calendar year's months, when enough arrived.
    next_year: Optional[tuple[int, float]] = None

    @property
    def six_month_change_pct(self) -> Optional[float]:
        if self.now is None or self.now.value == 0:
            return None
        last = next((p for p in reversed(self.ahead) if p.months_ahead == HORIZONS_MONTHS[-1]), None)
        if last is None:
            return None
        return (last.value - self.now.value) / self.now.value * 100.0

    def direction(self) -> str:
        change = self.six_month_change_pct
        if change is None:
            return "no six-month figure"
        if abs(change) < FLAT_EDGE_PCT:
            return "seen roughly flat over six months"
        verb = "rise" if change > 0 else "fall"
        return f"seen to {verb} about {abs(change):.0f}% over six months"

    def as_text(self) -> str:
        money = "$" if self.unit.startswith("$") else ""
        parts = []
        if self.now is not None:
            parts.append(f"{money}{fmt.num(self.now.value)} this month ({self.now.period})")
        for point in self.ahead:
            parts.append(f"{money}{fmt.num(point.value)} in {point.months_ahead} months ({point.period})")
        text = f"{self.name} ({self.unit}): " + " -> ".join(parts)
        if self.next_year is not None:
            year, mean = self.next_year
            text += f"; {year} average {money}{fmt.num(mean)}"
        return f"{text} -- {self.direction()}"


def build_forecast(label: str, payload: Any, today: Optional[date] = None) -> Optional[Forecast]:
    """The forecast for one series, or ``None`` when it cannot say "from here"."""
    if label not in SERIES:
        return None
    _, unit, name = SERIES[label]
    months = by_month(payload)
    if not months:
        return None
    today = today or date.today()
    this_month = (today.year, today.month)
    if this_month not in months:
        return None
    now = Point(0, month_label(this_month), months[this_month])
    ahead = []
    for count in HORIZONS_MONTHS:
        target = _add_months(this_month, count)
        if target in months:
            ahead.append(Point(count, month_label(target), months[target]))
    if not ahead:
        return None
    next_year = None
    year = this_month[0] + 1
    values = [months[(year, m)] for m in range(1, 13) if (year, m) in months]
    if len(values) >= MIN_MONTHS_FOR_YEAR_AVERAGE:
        next_year = (year, sum(values) / len(values))
    return Forecast(label=label, name=name, unit=unit, now=now, ahead=ahead, next_year=next_year)


@dataclass(frozen=True)
class OutlookSnapshot:
    """The official forecast for the prices a fund tracks."""

    ticker: str = ""
    forecasts: list[Forecast] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        lines = ["EIA Short-Term Energy Outlook, the official monthly price forecast:"]
        lines.extend(f"  {forecast.as_text()}" for forecast in self.forecasts)
        lines.append(
            "One agency's view, published monthly, and the market has read it. "
            "Weigh the direction and the gap between the forecast and today's "
            "price over the level itself; the EIA has been wrong before."
        )
        return lines


def build_snapshot(
    ticker: str, payloads: Optional[dict] = None, today: Optional[date] = None
) -> Optional[OutlookSnapshot]:
    """The outlook block for one ticker, or ``None`` when there is nothing to say."""
    wanted = series_for(ticker)
    if not wanted or not payloads:
        return None
    forecasts = [
        f for f in (build_forecast(label, payloads.get(label), today) for label in wanted) if f
    ]
    if not forecasts:
        return None
    return OutlookSnapshot(ticker=ticker.strip().upper(), forecasts=forecasts)


__all__ = [
    "COVERAGE",
    "Forecast",
    "OutlookSnapshot",
    "Point",
    "ROUTE",
    "ROW_LIMIT",
    "SERIES",
    "build_forecast",
    "build_snapshot",
    "by_month",
    "month_label",
    "series_for",
]
