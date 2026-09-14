"""What changed when the prompt changed.

A replay is only useful if the diff is legible. Two signals differ in ways
that matter very differently: a bias flip changes whether a trade happens at
all, a conviction move across 0.60 changes it almost as much, and a shift from
0.90 to 0.85 changes nothing the engine will ever act on.

So the comparison is graded by *consequence*, not by how many fields differ.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from app.schemas import Bias, LLMSignal
from config import settings as cfg

#: Dimension scores are recorded for evaluation and never read by the engine,
#: so a change in one is informative but never, on its own, consequential.
SCORE_FIELDS = (
    "news_score",
    "technical_score",
    "fundamental_score",
    "analyst_score",
    "insider_score",
)


@dataclass(frozen=True)
class SignalDiff:
    ticker: str
    before: Optional[LLMSignal]
    after: Optional[LLMSignal]

    @property
    def bias_flipped(self) -> bool:
        if self.before is None or self.after is None:
            return False
        return self.before.bias is not self.after.bias

    @property
    def conviction_delta(self) -> Optional[float]:
        if self.before is None or self.after is None:
            return None
        return round(self.after.conviction - self.before.conviction, 4)

    @property
    def crossed_floor(self) -> bool:
        """Whether this change alters whether the engine would act at all.

        The floor is the only threshold in the system the model's number is
        measured against, so crossing it is the difference between a trade and
        silence -- the single most consequential thing a prompt change can do.
        """
        if self.before is None or self.after is None:
            return False
        return self._tradeable(self.before) is not self._tradeable(self.after)

    @property
    def appeared(self) -> bool:
        """The new prompt produced a signal where the old one failed."""
        return self.before is None and self.after is not None

    @property
    def vanished(self) -> bool:
        return self.before is not None and self.after is None

    @property
    def consequential(self) -> bool:
        """Would this change what the engine does?"""
        return self.bias_flipped or self.crossed_floor or self.appeared or self.vanished

    @property
    def score_changes(self) -> dict[str, tuple[Optional[float], Optional[float]]]:
        if self.before is None or self.after is None:
            return {}
        changed = {}
        for name in SCORE_FIELDS:
            was, now = getattr(self.before, name, None), getattr(self.after, name, None)
            if was != now:
                changed[name] = (was, now)
        return changed

    @staticmethod
    def _tradeable(signal: LLMSignal) -> bool:
        return signal.bias is not Bias.NEUTRAL and signal.conviction >= cfg.MIN_CONVICTION

    def summary(self) -> str:
        if self.appeared:
            return f"{self.ticker}: no signal -> {self._describe(self.after)}"
        if self.vanished:
            return f"{self.ticker}: {self._describe(self.before)} -> no signal"
        if self.before is None and self.after is None:
            return f"{self.ticker}: no signal either way"

        parts = [f"{self.ticker}: {self._describe(self.before)} -> {self._describe(self.after)}"]
        if self.bias_flipped:
            parts.append("BIAS FLIP")
        if self.crossed_floor:
            was = "tradeable" if self._tradeable(self.before) else "below floor"
            now = "tradeable" if self._tradeable(self.after) else "below floor"
            parts.append(f"CROSSED FLOOR ({was} -> {now})")
        return "  ".join(parts)

    @staticmethod
    def _describe(signal: Optional[LLMSignal]) -> str:
        if signal is None:
            return "no signal"
        return f"{signal.bias.value} {signal.conviction:.2f}"


@dataclass(frozen=True)
class ReplaySummary:
    diffs: list[SignalDiff]

    @property
    def n(self) -> int:
        return len(self.diffs)

    @property
    def consequential(self) -> list[SignalDiff]:
        return [d for d in self.diffs if d.consequential]

    @property
    def bias_flips(self) -> int:
        return sum(1 for d in self.diffs if d.bias_flipped)

    @property
    def floor_crossings(self) -> int:
        return sum(1 for d in self.diffs if d.crossed_floor)

    @property
    def mean_conviction_delta(self) -> Optional[float]:
        deltas = [d.conviction_delta for d in self.diffs if d.conviction_delta is not None]
        if not deltas:
            return None
        return round(sum(deltas) / len(deltas), 4)

    @property
    def conviction_drift_direction(self) -> Optional[str]:
        """Whether the new prompt is systematically bolder or more cautious.

        Worth naming separately from the mean: a prompt that lifts every
        conviction by 0.05 has not become better calibrated, it has just moved
        more signals over the floor.
        """
        mean = self.mean_conviction_delta
        if mean is None or abs(mean) < 0.01:
            return None
        return "bolder" if mean > 0 else "more cautious"


__all__ = ["SCORE_FIELDS", "SignalDiff", "ReplaySummary"]
