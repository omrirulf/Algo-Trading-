"""What it costs to hold a commodity through a fund rather than in a vault.

Gold, silver and copper had four sections and no numbers at all. This is the
number that belongs there, and for a commodity fund it is arguably the most
important fact about the instrument -- more important than any forecast.

A commodity fund does not hold the commodity. It holds futures, and every
month it must sell the contract that is expiring and buy the next one. When
the next month costs *more* than the expiring one (contango) that roll loses
money, every month, for ever. USO is the famous case: crude oil traded at the
same price at both ends of a stretch in which USO lost most of its value, and
the difference went into rolling contracts.

So the measure here is not the shape of the futures curve, which would have
to be assembled from dated contract symbols that differ by commodity and roll
under your feet. It is the thing the holder actually experiences:

    the fund's return, minus the commodity's own return, over the same window

That gap *is* the cost of holding -- roll losses and fees together, measured
rather than modelled. It needs no key, only two price histories this project
already knows how to fetch, and it works for a basket like DBC where no
single pair of contracts would.

The reference has a limit of its own, and it is the reason for the band
below. Yahoo's ``CL=F`` and friends are *continuous front-month* series: at
each contract change the quoted price becomes the next contract's, and where
the two differ the series steps without anyone having gained or lost. Gold
suggests this is small -- GLD measured against ``GC=F`` came back at -0.1% a
year, which is about its fee and could not happen if the steps were large.
Crude did not: USO against ``CL=F`` measured **+55.9% a year**, a roll yield
at the very edge of what deep backwardation can produce and equally
consistent with the reference stepping down at every roll.

Faced with a number that could be either, this module does what the rest of
the project does with a number it cannot corroborate: it does not show it.
Past ``MAX_CREDIBLE_DRAG_PCT`` the section is omitted and the prompt is
shorter. A drag of 15% a year on a grain fund is ordinary and survives; a
claimed 56% gain does not, because being wrong about that one would be worse
than saying nothing about it.

Three honest limits, all stated in the prompt:

* **It is backward-looking.** A fund that bled 8% a year to contango will
  keep doing so while the curve stays in contango, and stops the day it
  flips. The gap says what the structure has been costing, not what it will.
* **It is not a direction.** A heavy carry cost is a reason to want a *bigger*
  move to justify the trade, and a reason to prefer a short. It is not by
  itself bearish, and the prompt says so.
* **A physically backed fund has almost none of it.** GLD holds bullion, so
  its gap is roughly its fee. That is a real and useful difference from USO,
  which is exactly why both are measured the same way.

Pure parsing, like its siblings: ``orchestrator.context`` does the fetching.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from orchestrator import formatting as fmt

#: ``ticker -> (Yahoo symbol for the commodity itself, plain-English name)``.
#:
#: The reference is the front-month future, which is the closest free thing to
#: the spot price. DBC and DBA are absent: a basket spanning a dozen contracts
#: has no single commodity to be measured against, and inventing one would be
#: worse than leaving the section out.
REFERENCES = {
    "GLD": ("GC=F", "gold"),
    "SLV": ("SI=F", "silver"),
    "CPER": ("HG=F", "copper"),
    "USO": ("CL=F", "crude oil"),
    "UNG": ("NG=F", "natural gas"),
    "CORN": ("ZC=F", "corn"),
    "WEAT": ("ZW=F", "wheat"),
    "SOYB": ("ZS=F", "soybeans"),
    "CANE": ("SB=F", "sugar"),
}

#: Windows measured, in trading days, with the names used in the prompt.
WINDOWS = (("3 months", 63), ("6 months", 126), ("12 months", 252))

#: Below this the drag is a rounding difference rather than a structure. A
#: physically backed fund's fee lands here, which is the point: "costs you
#: essentially nothing" is a finding about GLD, not a missing number.
FLAT_DRAG_PCT = 1.0

#: Past this a yearly drag is severe enough to name. USO has spent whole years
#: beyond it.
HEAVY_DRAG_PCT = 5.0

#: Past this, annualised, the figure is not credible as a roll yield and is
#: at least as likely to be an artefact of the reference series stepping at
#: contract changes. The section is omitted rather than shown: see the module
#: docstring for the USO reading that set this.
#:
#: Wide on purpose. Real carry on a grain or gas fund reaches the high teens
#: and should survive; the band is here to catch the impossible, not to
#: flatten the merely dramatic.
MAX_CREDIBLE_DRAG_PCT = 25.0

#: Both histories must overlap by at least this many days for the shortest
#: window to mean anything.
MIN_OVERLAP = 30


def reference_for(ticker: str) -> Optional[tuple[str, str]]:
    """``(Yahoo symbol, plain name)`` for the commodity behind a fund."""
    return REFERENCES.get(ticker.strip().upper())


def _closes(frame: Any) -> list[float]:
    """Daily closes, oldest first, from a history frame."""
    if frame is None:
        return []
    try:
        series = frame["Close"].dropna()
        values = [float(v) for v in series.tolist()]
    except Exception:  # noqa: BLE001 - an odd shape is no history
        return []
    return [v for v in values if v > 0]


def _return_over(closes: list[float], days: int) -> Optional[float]:
    if len(closes) <= days:
        return None
    start = closes[-1 - days]
    return (closes[-1] / start - 1.0) if start else None


def _verdict(annual_pct: Optional[float]) -> str:
    if annual_pct is None:
        return "unknown"
    if annual_pct <= -HEAVY_DRAG_PCT:
        return "heavy: rolling contracts costs this fund real money"
    if annual_pct < -FLAT_DRAG_PCT:
        return "a steady drag"
    if annual_pct > FLAT_DRAG_PCT:
        return "the roll has been paying this fund"
    return "close to nothing, as a physically backed fund should be"


@dataclass(frozen=True)
class Window:
    """One window: what the fund did, what the commodity did, and the gap."""

    label: str = ""
    days: int = 0
    fund: Optional[float] = None
    commodity: Optional[float] = None
    gap: Optional[float] = None

    @property
    def annualised_pct(self) -> Optional[float]:
        """The gap scaled to a year, in percentage points."""
        if self.gap is None or not self.days:
            return None
        return self.gap * (252.0 / self.days) * 100.0

    def as_text(self) -> str:
        return (f"{self.label}: fund {fmt.pct(self.fund)}, "
                f"commodity {fmt.pct(self.commodity)}, "
                f"gap {fmt.pct(self.gap)}")


@dataclass(frozen=True)
class CarrySnapshot:
    """What the structure of the fund has cost its holders."""

    ticker: str = ""
    commodity: str = ""
    windows: list[Window] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    @property
    def headline(self) -> Optional[Window]:
        """The longest window there is: a year of rolls beats a quarter."""
        return self.windows[-1] if self.windows else None

    def as_lines(self) -> list[str]:
        headline = self.headline
        annual = headline.annualised_pct if headline else None
        lines = [
            f"Cost of holding this fund instead of {self.commodity} itself: "
            f"{fmt.num(annual, 1) if annual is not None else fmt.NA}% a year "
            f"-- {_verdict(annual)}"
        ]
        lines.append("Measured: " + " | ".join(w.as_text() for w in self.windows))
        lines.append(
            f"A commodity fund holds futures, not {self.commodity}, and must sell each "
            "expiring contract to buy the next one. Where the next month costs more, "
            "that roll loses money every month. This gap is what the structure has "
            "actually cost, fees included -- it is history rather than a forecast, and "
            "it is not a direction: heavy carry is a reason to want a larger move to "
            "justify a long, and a tailwind for a short."
        )
        return lines


def build_snapshot(
    ticker: str,
    fund_history: Any = None,
    commodity_history: Any = None,
) -> Optional[CarrySnapshot]:
    """The holding-cost block, or ``None`` when it cannot be measured.

    ``None`` rather than a gap of zero: "no difference" and "we could not
    compare" are opposite findings, and only one of them is good news.
    """
    mapping = reference_for(ticker)
    if mapping is None:
        return None
    _, name = mapping

    fund = _closes(fund_history)
    commodity = _closes(commodity_history)
    if len(fund) < MIN_OVERLAP or len(commodity) < MIN_OVERLAP:
        return None

    windows: list[Window] = []
    for label, days in WINDOWS:
        fund_return = _return_over(fund, days)
        commodity_return = _return_over(commodity, days)
        if fund_return is None or commodity_return is None:
            continue
        windows.append(Window(
            label=label,
            days=days,
            fund=fund_return,
            commodity=commodity_return,
            gap=fund_return - commodity_return,
        ))
    if not windows:
        return None

    # The headline is what the model reads first and what it would carry into
    # a decision. If that cannot be believed, none of it can.
    headline = windows[-1].annualised_pct
    if headline is None or abs(headline) > MAX_CREDIBLE_DRAG_PCT:
        return None

    return CarrySnapshot(ticker=ticker.strip().upper(), commodity=name, windows=windows)


__all__ = [
    "CarrySnapshot",
    "Window",
    "build_snapshot",
    "reference_for",
    "REFERENCES",
    "WINDOWS",
    "FLAT_DRAG_PCT",
    "HEAVY_DRAG_PCT",
    "MAX_CREDIBLE_DRAG_PCT",
]
