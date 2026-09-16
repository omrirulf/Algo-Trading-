"""Statistics, and the refusal to produce one when the data can't support it."""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

import pytest

from analysis import metrics
from analysis.metrics import ScoredSignal
from analysis.reader import JournalEntry
from analysis.returns import ForwardReturn


def entry(conviction=0.7, bias="BULLISH", scores=None, ts=None, gaps=(), **kw) -> JournalEntry:
    return JournalEntry(
        ticker=kw.pop("ticker", "AAPL"),
        timestamp=ts or datetime(2026, 3, 2, 14, tzinfo=timezone.utc),
        timestamp_is_exact=True,
        bias=bias,
        conviction=conviction,
        scores=scores if scores is not None else {},
        gaps=list(gaps),
        **kw,
    )


def signal(pct, conviction=0.7, bias="BULLISH", scores=None) -> ScoredSignal:
    return ScoredSignal(
        entry=entry(conviction=conviction, bias=bias, scores=scores),
        forward=ForwardReturn(date(2026, 3, 2), date(2026, 3, 5), 100.0, 100 * (1 + pct), pct),
    )


# --------------------------------------------------------------------------- #
# Correlation
# --------------------------------------------------------------------------- #


def test_spearman_is_one_for_a_monotonic_pair():
    assert metrics.spearman([1, 2, 3, 4], [10, 20, 30, 40]).rho == pytest.approx(1.0)


def test_spearman_is_minus_one_when_reversed():
    assert metrics.spearman([1, 2, 3, 4], [40, 30, 20, 10]).rho == pytest.approx(-1.0)


def test_spearman_matches_a_hand_computed_value_with_ties():
    # y = [5, 6, 7, 8, 7] -> average ranks [1, 2, 3.5, 5, 3.5]; rho = 8/sqrt(95).
    result = metrics.spearman([1, 2, 3, 4, 5], [5, 6, 7, 8, 7])
    assert result.rho == pytest.approx(8 / (95**0.5), rel=1e-9)


def test_spearman_ignores_outlier_magnitude():
    """The reason rank correlation is used: one earnings day must not decide."""
    ranked = metrics.spearman([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]).rho
    exploded = metrics.spearman([1, 2, 3, 4, 5], [1, 2, 3, 4, 10_000]).rho
    assert ranked == exploded == pytest.approx(1.0)


def test_a_constant_series_has_no_correlation_rather_than_zero():
    assert metrics.spearman([1, 2, 3, 4], [7, 7, 7, 7]).rho is None


def test_too_few_points_yields_no_number_but_keeps_the_count():
    result = metrics.spearman([1, 2], [3, 4])
    assert result.rho is None and result.n == 2


def test_mismatched_series_is_a_programming_error():
    with pytest.raises(ValueError):
        metrics.spearman([1, 2, 3], [1, 2])


# --------------------------------------------------------------------------- #
# Signed returns
# --------------------------------------------------------------------------- #


def test_a_bearish_call_on_a_falling_stock_is_a_hit():
    bearish = signal(-0.05, bias="BEARISH")
    assert bearish.signed_return == pytest.approx(0.05)
    assert bearish.hit


def test_a_bullish_call_on_a_falling_stock_is_a_miss():
    assert not signal(-0.05, bias="BULLISH").hit


def test_raw_return_keeps_the_market_direction():
    assert signal(-0.05, bias="BEARISH").raw_return == pytest.approx(-0.05)


# --------------------------------------------------------------------------- #
# Conviction
# --------------------------------------------------------------------------- #


def test_buckets_split_on_the_floor_and_count_members():
    signals = [signal(0.01, conviction=c) for c in (0.10, 0.50, 0.65, 0.80, 0.95)]
    buckets = {b.label: b for b in metrics.conviction_buckets(signals)}
    assert buckets["0.00-0.30"].n == 1
    assert buckets["0.45-0.60"].n == 1
    assert buckets["0.60-0.75"].n == 1
    assert buckets["0.75-1.00"].n == 2


def test_conviction_of_one_lands_in_the_top_bucket():
    # An open interval ending at 1.00 would silently drop a perfect-confidence call.
    buckets = {b.label: b for b in metrics.conviction_buckets([signal(0.01, conviction=1.0)])}
    assert buckets["0.75-1.00"].n == 1


def test_floor_check_reports_the_edge_the_floor_is_buying():
    signals = [
        signal(0.04, conviction=0.9), signal(0.02, conviction=0.7),
        signal(-0.03, conviction=0.3), signal(-0.01, conviction=0.5),
    ]
    check = metrics.floor_check(signals, floor=0.6)
    assert check.above_n == 2 and check.below_n == 2
    assert check.above_mean == pytest.approx(0.03)
    assert check.below_mean == pytest.approx(-0.02)
    assert check.edge == pytest.approx(0.05)


def test_floor_check_edge_is_none_when_one_side_is_empty():
    check = metrics.floor_check([signal(0.01, conviction=0.9)], floor=0.6)
    assert check.below_n == 0 and check.edge is None


# --------------------------------------------------------------------------- #
# Dimensions and agreement
# --------------------------------------------------------------------------- #


def test_dimension_correlation_uses_only_entries_that_reported_that_score():
    signals = [
        signal(0.05, scores={"news_score": 0.9, "technical_score": None}),
        signal(-0.05, scores={"news_score": -0.9, "technical_score": None}),
        signal(0.02, scores={"news_score": 0.3, "technical_score": None}),
    ]
    correlations = metrics.dimension_correlations(signals)
    assert correlations["news_score"].n == 3
    assert correlations["news_score"].rho == pytest.approx(1.0)
    assert correlations["technical_score"].n == 0


def test_conflicting_dimensions_are_separated_from_aligned_ones():
    aligned = entry(conviction=0.9, scores={"news_score": 0.8, "technical_score": 0.6})
    conflicted = entry(conviction=0.4, scores={"news_score": 0.8, "technical_score": -0.6})
    check = metrics.agreement_check([aligned, conflicted])

    assert check.aligned_n == 1 and check.conflicted_n == 1
    assert check.gap == pytest.approx(0.5)  # conviction fell when they disagreed


def test_a_zero_score_is_unknown_not_a_disagreement():
    # 0.0 means "this dimension had no data", so it must not create a conflict.
    both = entry(scores={"news_score": 0.8, "technical_score": 0.0})
    check = metrics.agreement_check([both])
    assert check.aligned_n == 1 and check.conflicted_n == 0


def test_agreement_needs_at_least_two_scores_to_say_anything():
    check = metrics.agreement_check([entry(scores={"news_score": 0.8})])
    assert check.aligned_n == 0 and check.conflicted_n == 0


def test_agreement_check_needs_no_price_data():
    """It compares the model against its own instructions, so it works on day one."""
    check = metrics.agreement_check([
        entry(conviction=0.8, scores={"news_score": 0.5, "analyst_score": 0.5}),
    ])
    assert check.aligned_mean_conviction == pytest.approx(0.8)


# --------------------------------------------------------------------------- #
# Drift and health
# --------------------------------------------------------------------------- #


def test_drift_compares_the_halves_in_time_order():
    base = datetime(2026, 3, 2, 14, tzinfo=timezone.utc)
    entries = [
        entry(conviction=c, ts=base + timedelta(days=i))
        for i, c in enumerate([0.3, 0.3, 0.9, 0.9])
    ]
    drift = metrics.conviction_drift(entries, floor=0.6)
    assert drift.first_mean == pytest.approx(0.3)
    assert drift.second_mean == pytest.approx(0.9)
    assert drift.change == pytest.approx(0.6)
    assert drift.first_above_floor == 0.0 and drift.second_above_floor == 1.0


def test_drift_groups_by_day():
    base = datetime(2026, 3, 2, 9, tzinfo=timezone.utc)
    entries = [entry(conviction=0.5, ts=base), entry(conviction=0.7, ts=base + timedelta(hours=3))]
    drift = metrics.conviction_drift(entries, floor=0.6)
    assert drift.daily == [(date(2026, 3, 2), 2, pytest.approx(0.6))]


def test_drift_on_an_empty_journal_is_empty_not_an_error():
    assert metrics.conviction_drift([], floor=0.6).daily == []


def test_gap_summary_counts_cycles_and_groups_by_kind():
    entries = [
        entry(gaps=["fundamentals unavailable: HTTP 429"]),
        entry(gaps=["fundamentals unavailable: timeout", "analyst view unavailable: x"]),
        entry(),
    ]
    with_gaps, kinds = metrics.gap_summary(entries)
    assert with_gaps == 2
    assert kinds["fundamentals unavailable"] == 2
    assert kinds["analyst view unavailable"] == 1


def test_bias_distribution_counts_each_call():
    counts = metrics.bias_distribution(
        [entry(bias="BULLISH"), entry(bias="BULLISH"), entry(bias="NEUTRAL")]
    )
    assert counts["BULLISH"] == 2 and counts["NEUTRAL"] == 1



# --------------------------------------------------------------------------- #
# The learned blend beside what it has to beat
# --------------------------------------------------------------------------- #


def _scored_line(bias, conviction, ret, scores=None, blend=None):
    from datetime import date as _date
    from analysis import reader as _reader
    from analysis.returns import ForwardReturn as _Forward
    payload = {
        "ts_utc": "2026-03-02T14:00:00+00:00", "ticker": "NVDA", "context": {"gaps": []},
        "signal": {"ticker": "NVDA", "bias": bias, "conviction": conviction, "rationale": "r", **(scores or {})},
        "blend": blend,
    }
    entry = _reader.entry_from(payload)
    forward = _Forward(entry_date=_date(2026, 3, 2), exit_date=_date(2026, 3, 5),
                       entry_price=100.0, exit_price=100.0 * (1 + ret), pct=ret)
    return metrics.ScoredSignal(entry, forward)


def test_the_blend_comparison_counts_neutral_lines_for_the_blend_but_not_the_model():
    signals = [
        _scored_line("BULLISH", 0.8, +0.02, {"news_score": 0.5}, {"composite": 0.1, "level": "equal"}),
        _scored_line("NEUTRAL", 0.2, -0.01, {"news_score": -0.5}, {"composite": -0.1, "level": "ticker:NVDA"}),
        # The model and the blend disagree here; the blend is right.
        _scored_line("BEARISH", 0.6, +0.01, {"news_score": 0.5}, {"composite": 0.1, "level": "kind:equity"}),
        # A line from before the blend existed: counts for the model and equal weights only.
        _scored_line("BULLISH", 0.5, +0.01, {"news_score": 0.5}),
    ]
    c = metrics.blend_comparison(signals)
    assert (c.model.n, c.model.called) == (4, 3)
    assert c.model.hit_rate == pytest.approx(2 / 3)
    assert (c.equal.n, c.equal.called) == (4, 4)
    assert (c.learned.n, c.learned.called, c.learned_fitted) == (3, 3, 2)
    assert c.learned.hit_rate == 1.0
    assert c.disagreements == 1
    assert c.model_hit_rate_when_disagreeing == 0.0
    assert c.blend_hit_rate_when_disagreeing == 1.0


def test_a_policy_with_nothing_to_judge_is_empty_not_an_error():
    check = metrics.policy_check("x", [])
    assert (check.n, check.called, check.hit_rate, check.rank_corr.n) == (0, 0, None, 0)
    empty = metrics.blend_comparison([])
    assert empty.learned.n == 0 and empty.disagreements == 0
    assert empty.model_hit_rate_when_disagreeing is None



# --------------------------------------------------------------------------- #
# The rule for leaving shadow
# --------------------------------------------------------------------------- #


def _policy(label, n, rho, hit_rate):
    return metrics.PolicyCheck(label=label, n=n, called=n, rank_corr=metrics.Correlation(n, rho), hit_rate=hit_rate)


def _comparison(learned_n=40, learned_rho=0.30, model_rho=0.10, equal_rho=0.20, hit_rate=0.6):
    return metrics.BlendComparison(
        model=_policy("model conviction", 60, model_rho, 0.55),
        equal=_policy("equal weights", 60, equal_rho, 0.52),
        learned=_policy("learned blend", learned_n, learned_rho, hit_rate),
        learned_fitted=learned_n, disagreements=0,
        model_hit_rate_when_disagreeing=None, blend_hit_rate_when_disagreeing=None,
    )


def test_the_blend_is_ready_only_when_it_beats_both_baselines_with_enough_data():
    verdict = metrics.promotion_verdict(_comparison(), min_sample=20)
    assert verdict.ready and "more often than not" in verdict.reason


@pytest.mark.parametrize("kwargs, phrase", [
    ({"learned_n": 0}, "no line carries a learned composite yet"),
    ({"learned_n": 19}, "too few learned composites to judge (n=19, want 20+)"),
    ({"learned_rho": None}, "undefined"),
    ({"model_rho": 0.35}, "model's conviction still carries more information"),
    ({"equal_rho": 0.35}, "not equal weights"),
    ({"hit_rate": 0.5}, "was right only 50% of the time"),
    ({"hit_rate": None}, "was right only n/a of the time"),
])
def test_every_way_of_not_being_ready_says_which(kwargs, phrase):
    verdict = metrics.promotion_verdict(_comparison(**kwargs), min_sample=20)
    assert not verdict.ready
    assert phrase in verdict.reason


def test_an_undefined_equal_weight_correlation_does_not_block_promotion():
    assert metrics.promotion_verdict(_comparison(equal_rho=None), min_sample=20).ready
