"""How much oil and gas is actually sitting in tanks.

Every Wednesday the Energy Information Administration publishes what the
United States is holding: crude, petrol, diesel, and gas in underground
storage. For an oil or gas fund this is not background -- it is *the*
scheduled event of the week, the one release that reliably moves the price,
and until now the model was being asked to judge USO with a chart and a day
of headlines.

Four series, and the reason each is here:

``crude``
    Commercial crude stocks, excluding the Strategic Petroleum Reserve. The
    headline number. A build is bearish for crude, a draw bullish -- as a
    rule of thumb rather than a law, which is why the prompt says so.
``gasoline`` and ``distillate``
    What the refineries made of it. These move the refiners and the broad
    energy sector even when crude itself does not.
``natural_gas``
    Working gas in underground storage in the Lower 48. In summer the weekly
    figure is an injection, in winter a withdrawal, and the *sign flip* is
    the seasonal story.

Three numbers per series, for the same reason as the CFTC block: the level
alone is not a signal. What is held, what changed on the week, and where that
level sits against its own past year -- because "424 million barrels" means
nothing to anyone who does not already know the range.

Absent is not failed. With no key nothing is fetched and the section is
omitted, exactly as it is for a ticker that has no energy exposure.

Pure parsing, like its siblings. ``orchestrator.sources`` does the fetching,
because it is the one module on this side permitted to read a credential.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from orchestrator import formatting as fmt

#: A year of weekly readings, which is what makes a level interpretable.
HISTORY_WEEKS = 52
MIN_WEEKS_FOR_PERCENTILE = 26

#: ``label -> (route, series id, unit, plain-English name)``. The series ids
#: are EIA's own and were read off the live route metadata rather than
#: guessed: the facet is ``series`` and these are its values.
SERIES = {
    "crude": ("petroleum/stoc/wstk", "WCESTUS1", "million barrels", "Crude oil"),
    "gasoline": ("petroleum/stoc/wstk", "WGTSTUS1", "million barrels", "Petrol"),
    "distillate": ("petroleum/stoc/wstk", "WDISTUS1", "million barrels", "Diesel"),
    "natural_gas": ("natural-gas/stor/wkly", "NW2_EPG0_SWO_R48_BCF",
                    "billion cubic feet", "Natural gas"),
}

#: Which tickers get this section, and which series each one is asked about.
#: A broad energy fund cares about all of it; a gas fund cares about gas.
#:
#: Funds only, and XOM is deliberately absent despite being the most
#: oil-exposed line on the watchlist. The company prompt is the input every
#: replay and sanity baseline was measured against, and a new section in it
#: would invalidate all of them -- for a name that already has fundamentals,
#: analysts and insider filings of its own.
#:
#: DBC is a broad commodity basket that is mostly energy by weight, which is
#: why it is here at all; it gets the crude series and not the refined ones,
#: since the basket does not hold petrol or diesel.
COVERAGE = {
    "USO": ("crude", "gasoline", "distillate"),
    "UNG": ("natural_gas",),
    "XLE": ("crude", "gasoline", "distillate", "natural_gas"),
    "DBC": ("crude", "natural_gas"),
}

#: Stocks are reported in thousands of barrels. Shown in millions, because
#: "424,069" is a number nobody holds in their head and "424.1 million" is.
_THOUSANDS_TO_MILLIONS = 1000.0


def series_for(ticker: str) -> tuple[str, ...]:
    """Which series this ticker is asked about, empty when none apply."""
    return COVERAGE.get(ticker.strip().upper(), ())


def percentile(value: Optional[float], history: list[float]) -> Optional[float]:
    """Where ``value`` sits in its own past year, as a fraction."""
    usable = [v for v in history if v is not None]
    if value is None or len(usable) < MIN_WEEKS_FOR_PERCENTILE:
        return None
    return sum(1 for v in usable if v <= value) / len(usable)


def _band(share: Optional[float]) -> str:
    if share is None:
        return ""
    if share >= 0.85:
        return " -- high for the time of year"
    if share <= 0.15:
        return " -- low for the time of year"
    return ""


@dataclass(frozen=True)
class Stock:
    """One series: what is held, what changed, and how unusual that is."""

    label: str = ""
    name: str = ""
    unit: str = ""
    level: Optional[float] = None
    change: Optional[float] = None
    percentile: Optional[float] = None
    period: str = ""
    weeks: int = 0

    def as_text(self) -> str:
        direction = ""
        if self.change is not None:
            direction = " (a build)" if self.change > 0 else " (a draw)" if self.change < 0 else ""
        rank = ""
        if self.percentile is not None:
            rank = (f", {self.percentile * 100:.0f}% percentile over {self.weeks} weeks"
                    f"{_band(self.percentile)}")
        return (f"{self.name}: {fmt.num(self.level, 1)} {self.unit}, "
                f"{'+' if (self.change or 0) > 0 else ''}{fmt.num(self.change, 1)} "
                f"on the week{direction}{rank}")


@dataclass(frozen=True)
class EnergySnapshot:
    """What the United States is holding, as of last Wednesday."""

    ticker: str = ""
    period: str = ""
    stocks: list[Stock] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        lines = [f"US inventories, week ending {self.period or fmt.NA} "
                 f"(published the following Wednesday)"]
        lines.extend(f"  {stock.as_text()}" for stock in self.stocks)
        lines.append(
            "A build is more supply than demand and a draw is the reverse, so a "
            "build reads bearish and a draw bullish -- as a rule of thumb, not a "
            "law. Weigh the change and how unusual the level is above the level "
            "itself, and remember the market has already seen this number."
        )
        return lines


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


def build_stock(label: str, payload: Any) -> Optional[Stock]:
    """One series' snapshot from its raw EIA rows, newest first."""
    spec = SERIES.get(label)
    if spec is None:
        return None
    _, _, unit, name = spec

    values: list[float] = []
    period = ""
    for row in _rows(payload):
        value = _value(row)
        if value is None:
            continue
        if not values:
            period = str(row.get("period") or "")
        values.append(value)
    if not values:
        return None

    scale = _THOUSANDS_TO_MILLIONS if unit == "million barrels" else 1.0
    scaled = [v / scale for v in values]
    change = scaled[0] - scaled[1] if len(scaled) > 1 else None

    return Stock(
        label=label,
        name=name,
        unit=unit,
        level=scaled[0],
        change=change,
        percentile=percentile(scaled[0], scaled[:HISTORY_WEEKS]),
        period=period,
        weeks=min(len(scaled), HISTORY_WEEKS),
    )


def build_snapshot(ticker: str, payloads: Optional[dict] = None) -> Optional[EnergySnapshot]:
    """The energy block for one ticker, or ``None`` when there is nothing to say."""
    wanted = series_for(ticker)
    if not wanted or not payloads:
        return None
    stocks = [s for s in (build_stock(label, payloads.get(label)) for label in wanted) if s]
    if not stocks:
        return None
    return EnergySnapshot(
        ticker=ticker.strip().upper(),
        period=stocks[0].period,
        stocks=stocks,
    )


__all__ = [
    "EnergySnapshot",
    "Stock",
    "build_snapshot",
    "build_stock",
    "percentile",
    "series_for",
    "COVERAGE",
    "SERIES",
    "HISTORY_WEEKS",
]
