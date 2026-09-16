"""Whether this company beats its own guidance, and by how much.

The company block already carries what analysts *expect*. It says nothing
about the one thing that predicts whether an expectation will be met: the
company's own record of meeting them. A business that has beaten four
quarters running and one that has missed four are priced by the same
consensus and are not the same bet.

Finnhub publishes the surprise history free -- actual against estimate, by
quarter -- and covers the non-US lines on this watchlist, which is what
decided it over the alternatives. ASML and TEVA both return full histories;
that was checked against the live API rather than assumed.

Single names only, and only where the section can be added without moving
the company prompt... which it cannot, so see ``orchestrator.context``: this
rides in the existing ``FUNDAMENTALS`` block as extra lines rather than as a
new section of its own. The prompt every replay and sanity baseline was
measured against keeps its five headings.

Absent is not failed. With no key nothing is fetched and the section is
simply not there.

Pure parsing, like its siblings. ``orchestrator.sources`` does the fetching,
because it is the one module on this side permitted to read a credential.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from orchestrator import formatting as fmt

#: Quarters read out. Four is a year, which is the span over which a habit of
#: beating or missing is a habit rather than a run.
MAX_QUARTERS = 4

#: A surprise smaller than this is a rounding difference, not a beat. Consensus
#: is an average of estimates that were never meant to be exact.
FLAT_SURPRISE_PCT = 2.0

#: Past this, the number is more likely a broken estimate than a real result:
#: a company earning a cent against a forecast of nothing prints thousands of
#: per cent and tells the model nothing it can use.
MAX_SANE_SURPRISE_PCT = 500.0


def _number(value: Any) -> Optional[float]:
    if fmt.is_missing(value):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


@dataclass(frozen=True)
class Quarter:
    """One quarter: what was expected, what arrived."""

    period: str = ""
    actual: Optional[float] = None
    estimate: Optional[float] = None
    surprise_pct: Optional[float] = None

    @property
    def verdict(self) -> str:
        """Beat, missed or in line -- by percentage where that is usable.

        Where it is not, the direction still is: a penny against a forecast of
        nothing prints thousands of per cent, and "beat" is true even when
        "beat by 9,900%" is not worth saying.
        """
        if self.surprise_pct is not None:
            if self.surprise_pct > FLAT_SURPRISE_PCT:
                return "beat"
            if self.surprise_pct < -FLAT_SURPRISE_PCT:
                return "missed"
            return "in line"
        if self.actual is None or self.estimate is None:
            return "unknown"
        if self.actual > self.estimate:
            return "beat"
        if self.actual < self.estimate:
            return "missed"
        return "in line"

    def as_text(self) -> str:
        verdict = self.verdict
        if verdict == "in line" or self.surprise_pct is None:
            return f"{self.period} {verdict}"
        return f"{self.period} {verdict} by {abs(self.surprise_pct):.0f}%"


@dataclass(frozen=True)
class EarningsSnapshot:
    """A company's record against its own consensus."""

    ticker: str = ""
    beats: int = 0
    misses: int = 0
    in_line: int = 0
    quarters: list[Quarter] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    @property
    def record(self) -> str:
        parts = []
        if self.beats:
            parts.append(f"{self.beats} beat" + ("s" if self.beats > 1 else ""))
        if self.in_line:
            parts.append(f"{self.in_line} in line")
        if self.misses:
            parts.append(f"{self.misses} missed")
        return ", ".join(parts) or fmt.NA

    def as_lines(self) -> list[str]:
        if not self.quarters:
            return []
        span = ("last quarter" if len(self.quarters) == 1
                else f"last {len(self.quarters)} quarters")
        return [
            f"Earnings record, {span}: {self.record}",
            "  " + " | ".join(q.as_text() for q in self.quarters),
        ]


def build_snapshot(ticker: str, rows: Any = None) -> Optional[EarningsSnapshot]:
    """A company's surprise history, or ``None`` when there is none to read."""
    if not isinstance(rows, list) or not rows:
        return None

    quarters: list[Quarter] = []
    for row in rows[:MAX_QUARTERS]:
        if not isinstance(row, dict):
            continue
        surprise = _number(row.get("surprisePercent"))
        if surprise is not None and abs(surprise) > MAX_SANE_SURPRISE_PCT:
            # A cent against a forecast of nothing prints thousands of per
            # cent. The quarter is kept, the unusable number is not.
            surprise = None
        quarters.append(Quarter(
            period=str(row.get("period") or ""),
            actual=_number(row.get("actual")),
            estimate=_number(row.get("estimate")),
            surprise_pct=surprise,
        ))
    if not quarters:
        return None

    return EarningsSnapshot(
        ticker=ticker.strip().upper(),
        beats=sum(1 for q in quarters if q.verdict == "beat"),
        misses=sum(1 for q in quarters if q.verdict == "missed"),
        in_line=sum(1 for q in quarters if q.verdict == "in line"),
        quarters=quarters,
    )


__all__ = [
    "EarningsSnapshot",
    "Quarter",
    "build_snapshot",
    "MAX_QUARTERS",
]
