"""Statistics over scored signals. Pure functions, no I/O, no presentation.

Every function here returns the sample size alongside the number, and returns
``None`` rather than a number it cannot honestly compute -- a correlation over
four points, or over a constant series, is not a small result, it is not a
result. Deciding what is worth showing belongs to ``report.py``; deciding what
is *true* belongs here.

Rank correlation is used throughout rather than Pearson. Forward returns have
fat tails, and with a few weeks of signals one earnings-day move would
otherwise set the sign of the whole answer.
"""

from __future__ import annotations

import math
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from statistics import median
from typing import Optional, Sequence

from analysis.reader import SCORE_FIELDS, JournalEntry
from analysis.returns import ForwardReturn

#: Conviction bucket edges. Deliberately straddles MIN_CONVICTION (0.60) so the
#: question "did the floor filter the right signals" is visible in the table.
DEFAULT_BUCKET_EDGES = (0.0, 0.30, 0.45, 0.60, 0.75, 1.01)


@dataclass(frozen=True)
class ScoredSignal:
    """A journalled signal joined to what actually happened next."""

    entry: JournalEntry
    forward: ForwardReturn

    @property
    def raw_return(self) -> float:
        """The ticker's move, sign unchanged."""
        return self.forward.pct

    @property
    def signed_return(self) -> float:
        """The move in the direction the model called: positive means right."""
        return self.entry.direction * self.forward.pct

    @property
    def hit(self) -> bool:
        return self.signed_return > 0

    @property
    def conviction(self) -> float:
        return self.entry.conviction or 0.0


@dataclass(frozen=True)
class Correlation:
    n: int
    rho: Optional[float]


@dataclass(frozen=True)
class Bucket:
    label: str
    n: int
    hit_rate: Optional[float]
    mean_return: Optional[float]
    median_return: Optional[float]


@dataclass(frozen=True)
class FloorCheck:
    """Did MIN_CONVICTION filter out the signals that deserved filtering?"""

    floor: float
    above_n: int
    above_mean: Optional[float]
    above_hit_rate: Optional[float]
    below_n: int
    below_mean: Optional[float]
    below_hit_rate: Optional[float]

    @property
    def edge(self) -> Optional[float]:
        if self.above_mean is None or self.below_mean is None:
            return None
        return self.above_mean - self.below_mean


@dataclass(frozen=True)
class AgreementCheck:
    """The prompt demands conviction *fall* when dimensions disagree."""

    aligned_n: int
    aligned_mean_conviction: Optional[float]
    conflicted_n: int
    conflicted_mean_conviction: Optional[float]
    dispersion_vs_conviction: Correlation

    @property
    def gap(self) -> Optional[float]:
        if self.aligned_mean_conviction is None or self.conflicted_mean_conviction is None:
            return None
        return self.aligned_mean_conviction - self.conflicted_mean_conviction


@dataclass(frozen=True)
class Drift:
    first_n: int
    first_mean: Optional[float]
    second_n: int
    second_mean: Optional[float]
    first_above_floor: Optional[float]
    second_above_floor: Optional[float]
    daily: list[tuple[date, int, float]] = field(default_factory=list)

    @property
    def change(self) -> Optional[float]:
        if self.first_mean is None or self.second_mean is None:
            return None
        return self.second_mean - self.first_mean


# --------------------------------------------------------------------------- #
# Correlation primitives
# --------------------------------------------------------------------------- #


def _ranks(values: Sequence[float]) -> list[float]:
    """Average ranks, so ties do not invent an ordering that isn't there."""
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    start = 0
    while start < len(order):
        stop = start
        while stop + 1 < len(order) and values[order[stop + 1]] == values[order[start]]:
            stop += 1
        shared = (start + stop) / 2.0 + 1.0
        for position in range(start, stop + 1):
            ranks[order[position]] = shared
        start = stop + 1
    return ranks


def pearson(xs: Sequence[float], ys: Sequence[float]) -> Optional[float]:
    n = len(xs)
    if n != len(ys) or n < 3:
        return None
    mean_x, mean_y = sum(xs) / n, sum(ys) / n
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    spread_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    spread_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    if spread_x == 0 or spread_y == 0:
        # One series never varies; correlation is undefined, not zero.
        return None
    return covariance / (spread_x * spread_y)


def spearman(xs: Sequence[float], ys: Sequence[float]) -> Correlation:
    """Rank correlation, robust to the outlier days that dominate small samples."""
    if len(xs) != len(ys):
        raise ValueError("spearman needs two series of equal length")
    if len(xs) < 3:
        return Correlation(len(xs), None)
    return Correlation(len(xs), pearson(_ranks(xs), _ranks(ys)))


# --------------------------------------------------------------------------- #
# The questions the journal was built to answer
# --------------------------------------------------------------------------- #


def conviction_vs_outcome(signals: Sequence[ScoredSignal]) -> Correlation:
    """Does a higher conviction actually mean a better call?"""
    return spearman(
        [s.conviction for s in signals], [s.signed_return for s in signals]
    )


def conviction_buckets(
    signals: Sequence[ScoredSignal], edges: Sequence[float] = DEFAULT_BUCKET_EDGES
) -> list[Bucket]:
    buckets: list[Bucket] = []
    for low, high in zip(edges, edges[1:]):
        members = [s for s in signals if low <= s.conviction < high]
        returns = [s.signed_return for s in members]
        buckets.append(
            Bucket(
                label=f"{low:.2f}-{min(high, 1.0):.2f}",
                n=len(members),
                hit_rate=(sum(s.hit for s in members) / len(members)) if members else None,
                mean_return=(sum(returns) / len(returns)) if returns else None,
                median_return=median(returns) if returns else None,
            )
        )
    return buckets


def floor_check(signals: Sequence[ScoredSignal], floor: float) -> FloorCheck:
    above = [s for s in signals if s.conviction >= floor]
    below = [s for s in signals if s.conviction < floor]

    def summarise(group: Sequence[ScoredSignal]) -> tuple[Optional[float], Optional[float]]:
        if not group:
            return None, None
        returns = [s.signed_return for s in group]
        return sum(returns) / len(returns), sum(s.hit for s in group) / len(group)

    above_mean, above_hit = summarise(above)
    below_mean, below_hit = summarise(below)
    return FloorCheck(
        floor=floor,
        above_n=len(above),
        above_mean=above_mean,
        above_hit_rate=above_hit,
        below_n=len(below),
        below_mean=below_mean,
        below_hit_rate=below_hit,
    )


def dimension_correlations(signals: Sequence[ScoredSignal]) -> dict[str, Correlation]:
    """Which per-dimension score, if any, predicts the move.

    Correlated against the *raw* return rather than the signed one: a score is
    itself directional, so a bullish read on a ticker that rose is a hit no
    matter which way the headline bias went.
    """
    results: dict[str, Correlation] = {}
    for name in SCORE_FIELDS:
        pairs = [
            (s.entry.scores.get(name), s.raw_return)
            for s in signals
            if s.entry.scores.get(name) is not None
        ]
        results[name] = spearman([p[0] for p in pairs], [p[1] for p in pairs])
    return results


def agreement_check(entries: Sequence[JournalEntry]) -> AgreementCheck:
    """Test the prompt's central instruction against what the model actually did.

    Needs no price data: it compares the model's own dimension scores with the
    conviction it attached, so it can be run from day one.
    """
    aligned: list[float] = []
    conflicted: list[float] = []
    dispersions: list[float] = []
    convictions: list[float] = []

    for entry in entries:
        if entry.conviction is None:
            continue
        scores = list(entry.available_scores().values())
        if len(scores) < 2:
            continue

        dispersions.append(max(scores) - min(scores))
        convictions.append(entry.conviction)

        signs = {_sign(v) for v in scores if _sign(v) != 0}
        (conflicted if len(signs) > 1 else aligned).append(entry.conviction)

    return AgreementCheck(
        aligned_n=len(aligned),
        aligned_mean_conviction=(sum(aligned) / len(aligned)) if aligned else None,
        conflicted_n=len(conflicted),
        conflicted_mean_conviction=(sum(conflicted) / len(conflicted)) if conflicted else None,
        dispersion_vs_conviction=spearman(dispersions, convictions),
    )


@dataclass(frozen=True)
class PolicyCheck:
    """One way of turning a line into a directional number, against what followed."""

    label: str
    #: Lines the policy could be evaluated on.
    n: int
    #: Of which it took a side (a non-zero value).
    called: int
    #: The policy's value against the ticker's raw forward return, over ``n``.
    rank_corr: Correlation
    #: Share of the lines it called whose direction was right.
    hit_rate: Optional[float]


@dataclass(frozen=True)
class BlendComparison:
    """The learned blend beside the two things it has to beat."""

    model: PolicyCheck
    equal: PolicyCheck
    learned: PolicyCheck
    #: Learned composites that came from a fitted level rather than the
    #: equal-weight fallback a cycle uses while nothing has been learned.
    learned_fitted: int
    #: Lines where the model and the learned blend called opposite directions.
    disagreements: int
    model_hit_rate_when_disagreeing: Optional[float]
    blend_hit_rate_when_disagreeing: Optional[float]


def policy_check(label: str, pairs: Sequence[tuple[float, float]]) -> PolicyCheck:
    """``pairs`` are (policy value, raw forward return)."""
    called = [(value, ret) for value, ret in pairs if _sign(value) != 0]
    hits = [_sign(value) * ret > 0 for value, ret in called]
    return PolicyCheck(
        label=label,
        n=len(pairs),
        called=len(called),
        rank_corr=spearman([p[0] for p in pairs], [p[1] for p in pairs]),
        hit_rate=(sum(hits) / len(hits)) if hits else None,
    )


def blend_comparison(signals: Sequence[ScoredSignal]) -> BlendComparison:
    """Does the blend carry information, and more of it than the model's own conviction?

    Three policies over the same lines. The model's is its conviction signed
    by its bias, zero on NEUTRAL. Equal weights is the plain average of the
    scores, recomputed here so lines from before the blend existed count.
    The learned blend is the composite as journalled: whatever weights that
    cycle had, applied at the time -- the honest walk-forward record, never
    a refit that has seen the return it is judged on.
    """
    from analysis import blend as blending  # local: keeps analysis.blend importable on its own

    model_pairs: list[tuple[float, float]] = []
    equal_pairs: list[tuple[float, float]] = []
    learned_pairs: list[tuple[float, float]] = []
    fitted = 0
    disagreements: list[tuple[bool, bool]] = []

    for signal in signals:
        entry = signal.entry
        ret = signal.raw_return
        model_value = entry.direction * (entry.conviction or 0.0)
        model_pairs.append((model_value, ret))
        equal = blending.composite(entry.scores, blending.EQUAL_WEIGHTS)
        if equal is not None:
            equal_pairs.append((equal.value, ret))
        learned = entry.composite
        if learned is None:
            continue
        learned_pairs.append((learned, ret))
        if entry.blend.get("level") not in (None, blending.EQUAL_KEY):
            fitted += 1
        if _sign(model_value) != 0 and _sign(learned) != 0 and _sign(model_value) != _sign(learned):
            disagreements.append((_sign(model_value) * ret > 0, _sign(learned) * ret > 0))

    def rate(index: int) -> Optional[float]:
        if not disagreements:
            return None
        return sum(pair[index] for pair in disagreements) / len(disagreements)

    return BlendComparison(
        model=policy_check("model conviction", model_pairs),
        equal=policy_check("equal weights", equal_pairs),
        learned=policy_check("learned blend", learned_pairs),
        learned_fitted=fitted,
        disagreements=len(disagreements),
        model_hit_rate_when_disagreeing=rate(0),
        blend_hit_rate_when_disagreeing=rate(1),
    )


@dataclass(frozen=True)
class PromotionVerdict:
    """Whether the blend has earned its way out of shadow, and why or why not."""

    ready: bool
    reason: str


def promotion_verdict(comparison: BlendComparison, min_sample: int) -> PromotionVerdict:
    """The rule for leaving shadow, written once so the report and the daily job cannot disagree.

    Ready when at least ``min_sample`` learned composites have a realised
    return behind them, the blend's rank correlation with what followed is
    above the model's conviction's and above equal weights', and the blend
    was right more often than not. Anything less is a reason to keep
    watching, and the reason says which.
    """
    learned = comparison.learned
    if learned.n == 0:
        return PromotionVerdict(
            False,
            "no line carries a learned composite yet; the equal-weight row is the floor "
            "the fitted weights have to clear",
        )
    if learned.n < min_sample:
        return PromotionVerdict(
            False, f"too few learned composites to judge (n={learned.n}, want {min_sample}+)"
        )
    model_rho = comparison.model.rank_corr.rho
    equal_rho = comparison.equal.rank_corr.rho
    learned_rho = learned.rank_corr.rho
    if learned_rho is None or model_rho is None:
        return PromotionVerdict(False, "a rank correlation is undefined for one policy; no verdict")
    if learned_rho <= model_rho:
        return PromotionVerdict(
            False,
            "the model's conviction still carries more information than the learned blend; "
            "keep it in shadow",
        )
    if equal_rho is not None and learned_rho <= equal_rho:
        return PromotionVerdict(
            False,
            "the learned blend beats the model's conviction but not equal weights; the fitted "
            "weights are not yet earning their keep",
        )
    if learned.hit_rate is None or learned.hit_rate <= 0.5:
        rate = f"{learned.hit_rate:.0%}" if learned.hit_rate is not None else "n/a"
        return PromotionVerdict(
            False,
            f"the learned blend ranks outcomes better than the model but was right only {rate} "
            "of the time; not a direction to trade on",
        )
    return PromotionVerdict(
        True,
        "the learned blend carries more information than the model's conviction and than "
        "equal weights, and was right more often than not",
    )


def conviction_drift(entries: Sequence[JournalEntry], floor: float) -> Drift:
    """Is conviction creeping up until the floor stops filtering anything?"""
    dated = sorted(
        (e for e in entries if e.conviction is not None and e.timestamp is not None),
        key=lambda e: e.timestamp,
    )
    if not dated:
        return Drift(0, None, 0, None, None, None, [])

    by_day: dict[date, list[float]] = {}
    for entry in dated:
        by_day.setdefault(entry.timestamp.date(), []).append(entry.conviction)
    daily = [(day, len(vs), sum(vs) / len(vs)) for day, vs in sorted(by_day.items())]

    midpoint = len(dated) // 2
    first, second = dated[:midpoint], dated[midpoint:]

    def mean_conviction(group: Sequence[JournalEntry]) -> Optional[float]:
        return sum(e.conviction for e in group) / len(group) if group else None

    def above(group: Sequence[JournalEntry]) -> Optional[float]:
        return sum(e.conviction >= floor for e in group) / len(group) if group else None

    return Drift(
        first_n=len(first),
        first_mean=mean_conviction(first),
        second_n=len(second),
        second_mean=mean_conviction(second),
        first_above_floor=above(first),
        second_above_floor=above(second),
        daily=daily,
    )


def bias_distribution(entries: Sequence[JournalEntry]) -> Counter:
    return Counter(e.bias for e in entries if e.bias)


def gap_summary(entries: Sequence[JournalEntry]) -> tuple[int, Counter]:
    """How often the enrichment was actually there.

    If most cycles ran with a missing section, every other number on this page
    is describing a different system than the one that was designed.
    """
    with_gaps = sum(1 for e in entries if e.gaps)
    kinds: Counter = Counter()
    for entry in entries:
        for gap in entry.gaps:
            kinds[gap.split(":", 1)[0].strip()] += 1
    return with_gaps, kinds


def _sign(value: float) -> int:
    if value > 0:
        return 1
    return -1 if value < 0 else 0
