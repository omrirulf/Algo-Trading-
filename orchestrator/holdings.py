"""What analysts say about a fund, by asking about what the fund holds.

A fund has no analyst coverage of its own -- nobody publishes a price target
on XLE. But XLE *is* twenty-three companies, and every one of them is
covered. Roll the coverage of the holdings up by the fund's own weights and
you have the analyst view of the fund, built entirely from data this project
already knows how to fetch.

The number that makes it honest is **coverage**: the share of the fund's
weight that could actually be analysed. Five names at 62% of the fund is a
statement about most of the fund; five names at 11% of a 500-stock index is
not, and the prompt says which it is so the model can discount accordingly.

Two deliberate limits:

* **Top holdings only.** yfinance returns a handful, and fetching every
  constituent of a broad index would cost hundreds of calls per cycle for a
  progressively weaker signal.
* **Weights are the fund's, ratings are the holdings'.** No attempt is made
  to model the fund's own tracking, fees or structure here; that belongs in
  ``funds.py``.

Pure parsing: the caller fetches each holding's analyst snapshot -- reusing
``orchestrator.analysts`` unchanged -- and hands the pairs in.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Iterable, Optional, Sequence

from orchestrator import formatting as fmt
from orchestrator.analysts import AnalystSnapshot

#: Holdings rolled up. yfinance returns about ten; five is where the weight
#: concentrates and the call budget stays sane across forty funds.
MAX_HOLDINGS = 5

#: Below this share of fund weight the roll-up is reported but flagged as
#: thin, because a roll-up over 4% of an index is a fact about four percent.
THIN_COVERAGE = 0.25

#: yfinance's 1.0 (strong buy) to 5.0 (strong sell) mean, bucketed.
_BUY_MAX = 2.5
_SELL_MIN = 3.5


def _weighted(pairs: Sequence[tuple[float, float]]) -> Optional[float]:
    """Weighted mean of ``(value, weight)``, or ``None`` when nothing weighs in."""
    usable = [(v, w) for v, w in pairs if v is not None and w]
    total = sum(w for _, w in usable)
    if not usable or not total:
        return None
    return sum(v * w for v, w in usable) / total


@dataclass(frozen=True)
class HoldingsSnapshot:
    """The analyst view of a fund, assembled from the analyst view of its holdings."""

    ticker: str = ""
    covered: int = 0
    coverage_weight: Optional[float] = None
    buy_weight: Optional[float] = None
    hold_weight: Optional[float] = None
    sell_weight: Optional[float] = None
    mean_rating: Optional[float] = None
    target_upside: Optional[float] = None
    recent_actions: list[str] = field(default_factory=list)
    names: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        coverage = fmt.pct(self.coverage_weight, signed=False)
        thin = (
            "  -- thin, so read this as a fact about that slice rather than the fund"
            if self.coverage_weight is not None and self.coverage_weight < THIN_COVERAGE
            else ""
        )
        lines = [
            f"Rolled up from the {self.covered} largest holdings, "
            f"{coverage} of the fund by weight{thin}",
            f"Ratings by weight: buy {fmt.pct(self.buy_weight, signed=False)} | "
            f"hold {fmt.pct(self.hold_weight, signed=False)} | "
            f"sell {fmt.pct(self.sell_weight, signed=False)} "
            f"(mean {fmt.num(self.mean_rating)} on a 1=strong buy to 5=strong sell scale)",
            f"Weighted price target: {fmt.pct(self.target_upside)} above the current prices",
        ]
        if self.names:
            lines.append(f"Holdings read: {', '.join(self.names)}")
        if self.recent_actions:
            lines.append("Recent rating changes among them:")
            lines.extend(f"  - {action}" for action in self.recent_actions)
        else:
            lines.append("Recent rating changes among them: none reported")
        return lines


def build_snapshot(
    ticker: str, holdings: Sequence[tuple[str, Optional[float], Optional[AnalystSnapshot]]]
) -> Optional[HoldingsSnapshot]:
    """Roll ``(symbol, weight, analyst snapshot)`` up into one fund-level view.

    ``None`` when nothing could be analysed, so the caller omits the section
    rather than printing a roll-up over zero holdings.
    """
    usable = [(sym, w or 0.0, snap) for sym, w, snap in holdings if snap is not None]
    if not usable:
        return None

    total_weight = sum(w for _, w, _ in usable) or None
    buckets = {"buy": 0.0, "hold": 0.0, "sell": 0.0}
    for _, weight, snap in usable:
        mean = snap.recommendation_mean
        if mean is None or not weight:
            continue
        if mean <= _BUY_MAX:
            buckets["buy"] += weight
        elif mean >= _SELL_MIN:
            buckets["sell"] += weight
        else:
            buckets["hold"] += weight
    rated = sum(buckets.values()) or None

    actions: list[str] = []
    for symbol, _, snap in usable:
        for action in (snap.recent_actions or [])[:1]:
            actions.append(f"{symbol}: {action}")

    return HoldingsSnapshot(
        ticker=ticker.strip().upper(),
        covered=len(usable),
        coverage_weight=total_weight,
        buy_weight=(buckets["buy"] / rated) if rated else None,
        hold_weight=(buckets["hold"] / rated) if rated else None,
        sell_weight=(buckets["sell"] / rated) if rated else None,
        mean_rating=_weighted([(s.recommendation_mean, w) for _, w, s in usable]),
        target_upside=_weighted([(s.target_upside, w) for _, w, s in usable]),
        recent_actions=actions[:MAX_HOLDINGS],
        names=[symbol for symbol, _, _ in usable],
    )


def holdings_from_payload(payload: Any, limit: int = MAX_HOLDINGS) -> list[tuple[str, Optional[float]]]:
    """``(symbol, weight)`` pairs out of yfinance's top-holdings payload.

    The symbol is what matters here -- it is what gets looked up -- so a row
    whose index is not a ticker is skipped rather than guessed at.
    """
    out: list[tuple[str, Optional[float]]] = []
    if payload is None:
        return out
    try:
        if isinstance(payload, dict):
            items = list(payload.items())
        elif hasattr(payload, "iterrows"):
            columns = [str(c) for c in getattr(payload, "columns", [])]
            weight_col = next(
                (c for c in columns if "percent" in c.lower() or "weight" in c.lower()), None
            )
            items = [
                (index, row[weight_col] if weight_col else None)
                for index, row in payload.iterrows()
            ]
        elif hasattr(payload, "items"):
            items = list(payload.items())
        else:
            return out
    except Exception:  # noqa: BLE001 - an odd shape is no holdings
        return out

    for symbol, weight in items[:limit]:
        text = str(symbol).strip().upper()
        if not text or not text.replace(".", "").replace("-", "").isalnum():
            continue
        try:
            value = float(weight) if weight is not None and weight == weight else None
        except (TypeError, ValueError):
            value = None
        out.append((text, value))
    return out


__all__ = [
    "HoldingsSnapshot",
    "build_snapshot",
    "holdings_from_payload",
    "MAX_HOLDINGS",
    "THIN_COVERAGE",
]
