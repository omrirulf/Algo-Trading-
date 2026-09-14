"""Price one model-and-effort configuration against another, on the same inputs.

The question "is a cheaper model good enough here" has no answer in the
abstract, and the honest version of it is awkward: there is no ground truth
for a trading signal until the market has moved, which takes weeks. So this
measures the thing that *is* available now -- **agreement with the incumbent
on identical recorded context** -- and reports it next to measured cost.

Agreement is a proxy, and a weak one in a specific direction: a cheaper model
that agrees with Opus 100% of the time is interchangeable *with Opus*, which
is only good news if Opus was right. Whether any configuration produces
signals worth trading is a question for ``analysis/score_journal.py`` against
realised returns. This tool answers "what would switching cost me, and how
differently would it behave" -- nothing more.

Two rules borrowed from the cost guide, because both are easy to get wrong:

**Walk a staircase, not a grid.** The cheapest acceptable configuration is
often a *stronger* model at *lower* effort -- it spends fewer tokens reaching
the same answer. Fixing the model and tuning effort never finds that cell, and
a full grid pays for every expensive corner to find it.

**Effort is part of the cache key, and the cache is per model.** Every cell
starts cold, so a cell's first call pays a cache write that steady-state
running would not. Cost here is therefore an upper bound.
"""

from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from typing import Optional, Sequence

from app.schemas import Bias, LLMSignal
from config import settings as cfg
from orchestrator.pricing import Usage, monthly_usd
from replay.compare import SignalDiff
from replay.runner import ReplayEntry

#: Effort notches, cheapest first. The walk steps rightward through these.
EFFORT_NOTCHES: tuple[str, ...] = ("low", "medium", "high")

#: Model tiers, most capable first -- the axis the walk steps *down*.
MODEL_TIERS: tuple[str, ...] = ("claude-opus-5", "claude-sonnet-5", "claude-haiku-4-5")


@dataclass(frozen=True)
class Cell:
    """One (model, effort) configuration, measured on N recorded contexts."""

    model: str
    effort: str
    usages: list[Usage] = field(default_factory=list)
    diffs: list[SignalDiff] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def label(self) -> str:
        return f"{self.model.replace('claude-', '')} / {self.effort}"

    @property
    def n(self) -> int:
        return len(self.diffs)

    @property
    def cost_per_call(self) -> Optional[float]:
        costs = [u.cost_usd for u in self.usages if u.cost_usd is not None]
        return statistics.fmean(costs) if costs else None

    @property
    def mean_output_tokens(self) -> Optional[float]:
        return statistics.fmean(u.output_tokens for u in self.usages) if self.usages else None

    @property
    def cache_reads(self) -> int:
        return sum(u.cache_read_input_tokens for u in self.usages)

    def monthly_usd(self, tickers: int, cycles_per_day: Optional[int] = None) -> Optional[float]:
        per_call = self.cost_per_call
        return None if per_call is None else monthly_usd(per_call, tickers, cycles_per_day)

    # --- agreement with the incumbent ------------------------------------

    @property
    def bias_agreement(self) -> Optional[float]:
        """Share of contexts where the bias matched. The headline number."""
        comparable = [d for d in self.diffs if d.before is not None and d.after is not None]
        if not comparable:
            return None
        return sum(1 for d in comparable if not d.bias_flipped) / len(comparable)

    @property
    def tradeable_agreement(self) -> Optional[float]:
        """Share where both agreed on whether to trade at all.

        Stricter than bias agreement and closer to what matters: a signal that
        matches on direction but lands the other side of MIN_CONVICTION
        produces a different portfolio.
        """
        comparable = [d for d in self.diffs if d.before is not None and d.after is not None]
        if not comparable:
            return None
        return sum(1 for d in comparable if not (d.bias_flipped or d.crossed_floor)) / len(comparable)

    @property
    def mean_conviction_delta(self) -> Optional[float]:
        deltas = [d.conviction_delta for d in self.diffs if d.conviction_delta is not None]
        return statistics.fmean(deltas) if deltas else None

    @property
    def failure_rate(self) -> float:
        total = self.n + len(self.errors)
        return len(self.errors) / total if total else 0.0


def clears_floor(cell: Cell, floor: float) -> Optional[bool]:
    """Whether this cell meets the pre-registered agreement floor.

    ``None`` when there is nothing to judge on -- reported as unknown rather
    than silently treated as a pass, since a false pass prunes the walk and
    the error is only caught after the pruned cells are gone.
    """
    agreement = cell.tradeable_agreement
    return None if agreement is None else agreement >= floor


def staircase_order(
    models: Sequence[str] = MODEL_TIERS, efforts: Sequence[str] = EFFORT_NOTCHES
) -> list[tuple[str, str]]:
    """The cells to probe, in walk order: enter top-left, step down or right.

    Returns the full ordering rather than driving the walk, so a caller can
    stop early once an incumbent prunes the rest. Entry is the most capable
    tier at the cheapest effort -- the cell that is both budget-bounded and
    unambiguous to step away from.
    """
    return [(model, effort) for model in models for effort in efforts]


__all__ = [
    "EFFORT_NOTCHES",
    "MODEL_TIERS",
    "Cell",
    "clears_floor",
    "staircase_order",
]
