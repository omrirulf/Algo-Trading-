"""The weather every fund is trading in.

The fund prompt tells the model to answer NEUTRAL unless something specific
has changed -- "a policy or rate surprise, a data release well outside
expectations". Then it hands over a day of headlines and nothing else, and
asks it to judge whether a rate surprise happened. It has no rates.

This is the missing half of that instruction. Six numbers, all of them free
and unauthenticated, all of them the actual price of the thing rather than
somebody's summary of it:

* **The Treasury curve**, at three months, five years, ten and thirty. A bond
  fund *is* a bet on this. An equity fund is one at a remove.
* **The slope**, ten-year minus three-month. The single most watched number
  in macro, and the one a level cannot give you: an inverted curve is a
  regime, not a reading.
* **The dollar**, because a non-US fund held in dollars earns the currency
  move whether it wants to or not.
* **Volatility**, because the same signal means different things at a VIX of
  12 and a VIX of 34.

Those six are prices, which say what traders think. What actually *happened*
-- an inflation print, a jobs number, a claims figure -- is published by the
statistical agencies and reaches this block through ``orchestrator.fred``,
when a key for it is configured. With no key the block is four lines instead
of six and nothing else changes: a key is a way to see more, never a thing
the system depends on.

Funds only, for now. The company prompt is the input every replay and sanity
baseline was measured against, and changing it would invalidate all of them
for a block that matters far less to a single name than to an index.

Pure parsing, like its sibling modules: ``orchestrator.context`` does the
fetching and hands the histories in.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from orchestrator import formatting as fmt, fred

#: Yahoo symbols, in the order they are read out. The yields are quoted in
#: percent already (``^TNX`` of 4.12 means 4.12%), which is why nothing here
#: scales them.
YIELD_SYMBOLS = (
    ("^IRX", "3-month"),
    ("^FVX", "5-year"),
    ("^TNX", "10-year"),
    ("^TYX", "30-year"),
)
DOLLAR_SYMBOL = "DX-Y.NYB"
VOLATILITY_SYMBOL = "^VIX"

SYMBOLS = tuple(symbol for symbol, _ in YIELD_SYMBOLS) + (DOLLAR_SYMBOL, VOLATILITY_SYMBOL)

#: Trading days in the change window. A week of sessions, not a week of days.
WEEK = 5

#: The slope, in percentage points, below which the curve is called inverted
#: rather than flat. Exactly zero is a knife edge that nothing trades on.
INVERSION_EDGE = -0.05
FLAT_EDGE = 0.25

#: VIX bands, named rather than left as a bare number. The same bullish
#: signal is a different trade at 12 and at 34.
VIX_CALM = 15.0
VIX_ELEVATED = 25.0


def _move(value: Optional[float], digits: int = 2) -> str:
    """A signed change with no unit attached.

    Not ``fmt.points``: these are moves *in* percentage points, and rendering
    a two-basis-point shift as "0.0%" both loses the size and reads as a
    percentage change in the yield, which it is not.
    """
    if fmt.is_missing(value):
        return fmt.NA
    return f"{float(value):+.{digits}f}"


def _last_and_change(frame: Any, lookback: int = WEEK) -> tuple[Optional[float], Optional[float]]:
    """``(latest close, change over the lookback)`` from a history frame."""
    if frame is None:
        return None, None
    try:
        closes = frame["Close"].dropna()
    except Exception:  # noqa: BLE001 - an odd shape is a missing reading
        return None, None
    try:
        values = [float(v) for v in closes.tolist()]
    except (TypeError, ValueError):
        return None, None
    if not values:
        return None, None
    latest = values[-1]
    if len(values) <= lookback:
        return latest, None
    return latest, latest - values[-1 - lookback]


def _curve_shape(slope: Optional[float]) -> str:
    if slope is None:
        return "unknown"
    if slope < INVERSION_EDGE:
        return "inverted -- short rates above long, which markets read as a slowdown ahead"
    if slope < FLAT_EDGE:
        return "flat"
    return "upward sloping (normal)"


def _vix_band(level: Optional[float]) -> str:
    if level is None:
        return "unknown"
    if level < VIX_CALM:
        return "calm"
    if level < VIX_ELEVATED:
        return "elevated"
    return "stressed"


@dataclass(frozen=True)
class MacroSnapshot:
    """Rates, the curve, the dollar and volatility."""

    yields: dict[str, float] = field(default_factory=dict)
    yield_changes: dict[str, float] = field(default_factory=dict)
    slope: Optional[float] = None
    dollar: Optional[float] = None
    dollar_change: Optional[float] = None
    volatility: Optional[float] = None
    volatility_change: Optional[float] = None
    #: Official releases, already rendered. Stored as the lines the model was
    #: shown rather than as numbers: this is the record of what it read.
    release_lines: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        parts = []
        for _, label in YIELD_SYMBOLS:
            level = self.yields.get(label)
            if level is None:
                # No trailing per-cent sign on a blank: "5-year n/a%" reads
                # like a number that happens to be missing its digits.
                parts.append(f"{label} {fmt.NA}")
                continue
            change = self.yield_changes.get(label)
            parts.append(
                f"{label} {fmt.num(level)}% ({_move(change)} on the week)"
                if change is not None
                else f"{label} {fmt.num(level)}%"
            )
        lines = ["US Treasury yields: " + " | ".join(parts)]
        lines.append(
            f"Yield curve, 10-year minus 3-month: {_move(self.slope)} "
            f"points -- {_curve_shape(self.slope)}"
        )
        lines.append(
            f"US dollar index: {fmt.num(self.dollar)} "
            f"({_move(self.dollar_change)} on the week)"
        )
        lines.append(
            f"Volatility (VIX): {fmt.num(self.volatility)} "
            f"({_move(self.volatility_change, digits=1)} on the week) -- "
            f"{_vix_band(self.volatility)}"
        )
        lines.extend(self.release_lines)
        return lines


def build_snapshot(
    histories: Optional[dict[str, Any]] = None,
    releases: Optional[dict] = None,
) -> Optional[MacroSnapshot]:
    """The macro block, or ``None`` when not one number arrived.

    ``None`` rather than four lines of ``n/a``: a block that says nothing four
    different ways is the thing every module here was written to avoid.
    """
    histories = histories or {}
    yields: dict[str, float] = {}
    changes: dict[str, float] = {}
    for symbol, label in YIELD_SYMBOLS:
        level, change = _last_and_change(histories.get(symbol))
        if level is not None:
            yields[label] = level
        if change is not None:
            changes[label] = change

    dollar, dollar_change = _last_and_change(histories.get(DOLLAR_SYMBOL))
    volatility, volatility_change = _last_and_change(histories.get(VOLATILITY_SYMBOL))

    slope = None
    if "10-year" in yields and "3-month" in yields:
        slope = yields["10-year"] - yields["3-month"]

    release_lines = fred.as_lines(releases)

    if not yields and dollar is None and volatility is None and not release_lines:
        return None

    return MacroSnapshot(
        yields=yields,
        yield_changes=changes,
        slope=slope,
        dollar=dollar,
        dollar_change=dollar_change,
        volatility=volatility,
        volatility_change=volatility_change,
        release_lines=release_lines,
    )


__all__ = [
    "MacroSnapshot",
    "build_snapshot",
    "SYMBOLS",
    "YIELD_SYMBOLS",
    "DOLLAR_SYMBOL",
    "VOLATILITY_SYMBOL",
    "WEEK",
]
