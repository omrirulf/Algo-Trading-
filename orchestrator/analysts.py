"""What professional money says about the ticker: sell-side and ownership.

This is the market's existing prior, and it is deliberately kept separate from
the other context because it should be weighed differently. A consensus is
already in the price; what carries information is a *change* to it (a fresh
upgrade or downgrade) or a wide gap between the price and where the people
paid to model the company think it belongs.

Pure parsing, like its sibling modules: ``orchestrator.context`` does the
fetching and hands the frames in.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Optional

from orchestrator import formatting as fmt

#: How many recent rating changes and top holders to put in the prompt.
MAX_RATING_ACTIONS = 6
MAX_TOP_HOLDERS = 5

_RATING_BUCKETS = ("strongBuy", "buy", "hold", "sell", "strongSell")
_BUCKET_LABELS = {
    "strongBuy": "strong buy",
    "buy": "buy",
    "hold": "hold",
    "sell": "sell",
    "strongSell": "strong sell",
}


@dataclass(frozen=True)
class AnalystSnapshot:
    recommendation: Optional[str] = None
    #: yfinance's 1.0 (strong buy) to 5.0 (strong sell) scale.
    recommendation_mean: Optional[float] = None
    analyst_count: Optional[int] = None
    target_mean: Optional[float] = None
    target_high: Optional[float] = None
    target_low: Optional[float] = None
    target_upside: Optional[float] = None
    rating_counts: dict[str, int] = field(default_factory=dict)
    recent_actions: list[str] = field(default_factory=list)
    institutional_ownership: Optional[float] = None
    top_holders: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return asdict(self)

    def as_lines(self) -> list[str]:
        lines = [
            f"Consensus: {self.recommendation or fmt.NA} "
            f"(mean {fmt.num(self.recommendation_mean)} on a 1=strong buy to "
            f"5=strong sell scale, {self.analyst_count if self.analyst_count is not None else fmt.NA} analysts)",
            f"Ratings: {self._rating_breakdown()}",
            f"Price target: mean {fmt.num(self.target_mean)} "
            f"({fmt.pct(self.target_upside)} vs last close), "
            f"range {fmt.num(self.target_low)} - {fmt.num(self.target_high)}",
        ]

        if self.recent_actions:
            lines.append("Recent rating changes:")
            lines.extend(f"  - {action}" for action in self.recent_actions)
        else:
            lines.append("Recent rating changes: none reported")

        lines.append(
            f"Institutional ownership: {fmt.pct(self.institutional_ownership, signed=False)}"
        )
        if self.top_holders:
            lines.append(f"Largest holders: {', '.join(self.top_holders)}")
        return lines

    def _rating_breakdown(self) -> str:
        if not self.rating_counts:
            return fmt.NA
        return ", ".join(
            f"{self.rating_counts[bucket]} {_BUCKET_LABELS[bucket]}"
            for bucket in _RATING_BUCKETS
            if bucket in self.rating_counts
        )


def build_snapshot(
    info: dict[str, Any],
    recommendations: Any = None,
    upgrades_downgrades: Any = None,
    institutional_holders: Any = None,
    last_close: Optional[float] = None,
) -> AnalystSnapshot:
    info = info or {}
    target_mean = fmt.clean(info.get("targetMeanPrice"))
    upside = None
    if target_mean is not None and last_close:
        upside = target_mean / last_close - 1.0

    count = fmt.clean(info.get("numberOfAnalystOpinions"))

    return AnalystSnapshot(
        recommendation=_text(info.get("recommendationKey")),
        recommendation_mean=fmt.clean(info.get("recommendationMean")),
        analyst_count=int(count) if count is not None else None,
        target_mean=target_mean,
        target_high=fmt.clean(info.get("targetHighPrice")),
        target_low=fmt.clean(info.get("targetLowPrice")),
        target_upside=upside,
        rating_counts=parse_rating_counts(recommendations),
        recent_actions=parse_rating_actions(upgrades_downgrades),
        institutional_ownership=fmt.clean(info.get("heldPercentInstitutions")),
        top_holders=parse_top_holders(institutional_holders),
    )


def parse_rating_counts(recommendations: Any) -> dict[str, int]:
    """Analyst rating buckets for the most recent period in the frame."""
    row = _first_row(recommendations)
    if row is None:
        return {}
    counts: dict[str, int] = {}
    for bucket in _RATING_BUCKETS:
        value = fmt.clean(row.get(bucket))
        if value is not None:
            counts[bucket] = int(value)
    return counts


def parse_rating_actions(upgrades_downgrades: Any, limit: int = MAX_RATING_ACTIONS) -> list[str]:
    """Most recent upgrades / downgrades as ``"date Firm: action, From -> To"``."""
    frame = upgrades_downgrades
    if frame is None or not hasattr(frame, "empty") or frame.empty:
        return []

    try:
        ordered = frame.sort_index(ascending=False).head(limit)
    except (TypeError, ValueError):
        ordered = frame.head(limit)

    actions: list[str] = []
    for when, row in ordered.iterrows():
        firm = _text(row.get("Firm")) or "unknown firm"
        action = _text(row.get("Action")) or "change"
        to_grade = _text(row.get("ToGrade"))
        from_grade = _text(row.get("FromGrade"))

        line = f"{_date_text(when)} {firm}: {action}"
        if to_grade:
            line += f", {from_grade or '?'} -> {to_grade}"
        actions.append(line)
    return actions


def parse_top_holders(institutional_holders: Any, limit: int = MAX_TOP_HOLDERS) -> list[str]:
    """Largest institutional holders as ``"Name (4.1%)"``."""
    frame = institutional_holders
    if frame is None or not hasattr(frame, "empty") or frame.empty:
        return []

    holders: list[str] = []
    for _, row in frame.head(limit).iterrows():
        name = _text(row.get("Holder"))
        if not name:
            continue
        share = fmt.clean(row.get("pctHeld"))
        if share is None:
            share = fmt.clean(row.get("% Out"))
        holders.append(f"{name} ({fmt.pct(share, signed=False)})" if share is not None else name)
    return holders


def _first_row(frame: Any) -> Optional[dict]:
    if frame is None or not hasattr(frame, "empty") or frame.empty:
        return None
    try:
        return frame.iloc[0].to_dict()
    except (AttributeError, IndexError, TypeError):
        return None


def _date_text(value: Any) -> str:
    try:
        import pandas as pd

        return pd.Timestamp(value).date().isoformat()
    except (TypeError, ValueError):
        return str(value)[:10]


def _text(value: Any) -> Optional[str]:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None
