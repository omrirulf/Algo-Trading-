"""The correlation measurement, proven on series whose answer is known.

Every test builds its own returns from a seeded generator, so the suite needs
no network and the expected correlation is a property of the construction
rather than of whatever the market did last quarter.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from analysis import correlations as corr


def days(n: int = 400) -> pd.DatetimeIndex:
    return pd.bdate_range("2024-01-01", periods=n)


def frame(**columns) -> pd.DataFrame:
    index = days(len(next(iter(columns.values()))))
    return pd.DataFrame(columns, index=index)


def noise(n: int, seed: int, scale: float = 0.01) -> np.ndarray:
    return np.random.default_rng(seed).normal(0.0, scale, n)


# --------------------------------------------------------------------------- #
# Returns and baskets
# --------------------------------------------------------------------------- #


def test_returns_are_day_over_day_and_drop_the_first_row():
    closes = frame(AAA=[100.0, 110.0, 99.0])
    out = corr.daily_returns(closes)
    assert len(out) == 2
    assert out["AAA"].iloc[0] == pytest.approx(0.10)
    assert out["AAA"].iloc[1] == pytest.approx(-0.10)


def test_a_basket_is_the_equal_weighted_mean_of_what_is_present():
    returns = frame(AAA=[0.02, 0.04], BBB=[0.04, 0.08])
    out = corr.basket(returns, ["AAA", "BBB", "NOPE"])
    assert list(out) == pytest.approx([0.03, 0.06])


def test_a_basket_of_nothing_present_is_none_not_an_empty_series():
    """A delisted ETN should cost one row of the report, not a whole pair."""
    returns = frame(AAA=[0.01, 0.02])
    assert corr.basket(returns, ["GONE", "ALSO_GONE"]) is None


# --------------------------------------------------------------------------- #
# Correlation, and refusing to report one from too little data
# --------------------------------------------------------------------------- #


def test_a_pair_moving_together_measures_near_one():
    n = 300
    shared = noise(n, seed=1)
    returns = frame(AAA=shared, BBB=shared * 1.5)
    r, count = corr.correlation(returns["AAA"], returns["BBB"])
    assert r == pytest.approx(1.0, abs=1e-9) and count == n


def test_an_inverse_pair_measures_near_minus_one():
    n = 300
    shared = noise(n, seed=2)
    returns = frame(AAA=shared, BBB=-shared)
    r, _ = corr.correlation(returns["AAA"], returns["BBB"])
    assert r == pytest.approx(-1.0, abs=1e-9)


def test_too_few_overlapping_days_is_unmeasured_not_a_number():
    """A correlation from eight days is noise with a decimal point."""
    n = corr.MIN_OBSERVATIONS - 1
    returns = frame(AAA=noise(n, 3), BBB=noise(n, 4))
    r, count = corr.correlation(returns["AAA"], returns["BBB"])
    assert r is None and count == n


def test_a_flat_series_has_no_correlation_rather_than_a_nan():
    n = 100
    returns = frame(AAA=noise(n, 5), BBB=np.zeros(n))
    r, _ = corr.correlation(returns["AAA"], returns["BBB"])
    assert r is None


# --------------------------------------------------------------------------- #
# Removing the market factor -- what makes the cross-group section readable
# --------------------------------------------------------------------------- #


def test_two_pure_market_plays_have_no_excess_correlation():
    """The wall of 0.8s this exists to prevent.

    Two baskets that are nothing but the market plus their own noise are
    strongly correlated raw, and not at all once the market is removed --
    which is the honest answer, because the gross cap already bounds the
    risk they share.
    """
    n = 400
    rng = np.random.default_rng(31)
    mkt = rng.normal(0.0, 0.01, n)
    returns = frame(
        RSP=mkt,
        AAA=mkt + rng.normal(0.0, 0.004, n),
        BBB=mkt + rng.normal(0.0, 0.004, n),
    )
    raw, _ = corr.correlation(returns["AAA"], returns["BBB"])
    ra = corr.market_residual(returns["AAA"], returns["RSP"])
    rb = corr.market_residual(returns["BBB"], returns["RSP"])
    excess, _ = corr.correlation(ra, rb)
    assert raw > corr.STRONG
    assert abs(excess) < 0.2


def test_a_shared_second_factor_survives_removing_the_market():
    """A rates factor two groups share is exactly what should still show."""
    n = 400
    rng = np.random.default_rng(32)
    mkt, rates = rng.normal(0.0, 0.01, n), rng.normal(0.0, 0.01, n)
    returns = frame(
        RSP=mkt,
        AAA=mkt + rates + rng.normal(0.0, 0.002, n),
        BBB=mkt + rates + rng.normal(0.0, 0.002, n),
    )
    ra = corr.market_residual(returns["AAA"], returns["RSP"])
    rb = corr.market_residual(returns["BBB"], returns["RSP"])
    excess, _ = corr.correlation(ra, rb)
    assert excess > corr.STRONG


def test_the_factor_is_the_watchlist_average_not_one_noisy_etf():
    """Regression: subtracting a single noisy proxy fakes a link everywhere.

    Twenty baskets that are pure market plus their own noise have zero true
    excess correlation. Regress them against one ETF that has its *own*
    idiosyncratic noise and every residual inherits the same -beta x noise
    term, so they all correlate -- an artefact that measured ~0.9 when this
    module first used RSP for the job. Averaging the whole watchlist into
    the factor is what makes the number mean what it says.
    """
    n = 400
    rng = np.random.default_rng(36)
    mkt = rng.normal(0.0, 0.01, n)
    columns = {f"T{i:02d}": mkt + rng.normal(0.0, 0.004, n) for i in range(20)}
    columns["RSP"] = mkt + rng.normal(0.0, 0.004, n)   # as noisy as any member
    returns = frame(**columns)

    def excess_between(factor):
        ra = corr.market_residual(returns["T00"], factor)
        rb = corr.market_residual(returns["T01"], factor)
        return corr.correlation(ra, rb)[0]

    single_proxy = excess_between(returns["RSP"])
    averaged = excess_between(corr.book_factor(returns))
    assert abs(averaged) < abs(single_proxy)
    assert abs(averaged) < 0.2


def test_the_book_factor_needs_enough_days():
    assert corr.book_factor(frame(AAA=noise(5, 37))) is None
    assert corr.book_factor(pd.DataFrame()) is None


def test_a_residual_needs_enough_days_and_a_moving_market():
    short = frame(AAA=noise(5, 33), RSP=noise(5, 34))
    assert corr.market_residual(short["AAA"], short["RSP"]) is None
    flat = frame(AAA=noise(100, 35), RSP=np.zeros(100))
    assert corr.market_residual(flat["AAA"], flat["RSP"]) is None


def test_pairs_rank_by_the_tail_excess_before_the_raw_number():
    """Ranking by raw would put 'two equity groups' at the top of every run."""
    raw_only = corr.PairResult("raw", ("A",), ("B",), 0.9, 0.9, 0.9,
                               0.05, 0.05, 10, 250, corr.STABLE, corr.WEAK)
    excess = corr.PairResult("excess", ("C",), ("D",), 0.4, 0.4, 0.4,
                             0.5, 0.8, 10, 250, corr.WEAK, corr.STRESS_ONLY)
    assert excess.rank_by > raw_only.rank_by


def test_a_pair_carries_a_verdict_on_the_excess_as_well_as_the_raw():
    """Two groups whose whole co-movement is the market are 'stable' raw.

    Reading only that column would promote a pair the gross cap already
    bounds, so the excess gets its own verdict and the cross-group table
    prints that one.
    """
    n = 400
    rng = np.random.default_rng(38)
    mkt = rng.normal(0.0, 0.01, n)
    columns = {f"T{i:02d}": mkt + rng.normal(0.0, 0.004, n) for i in range(12)}
    returns = frame(RSP=mkt + rng.normal(0.0, 0.004, n), **columns)
    result = corr.measure_pair(
        returns, "pure market", ["T00"], ["T01"],
        corr.stress_index(returns), corr.book_factor(returns),
    )
    assert result.verdict == corr.STABLE
    assert result.excess_verdict == corr.WEAK


# --------------------------------------------------------------------------- #
# The stress window
# --------------------------------------------------------------------------- #


def test_the_stress_window_is_the_benchmarks_worst_days():
    n = 100
    rsp = np.linspace(-0.05, 0.05, n)          # worst days are the first ones
    returns = frame(RSP=rsp, AAA=noise(n, 6))
    stress = corr.stress_index(returns, quantile=0.10)
    assert len(stress) == 10
    assert set(stress) == set(returns.index[:10])


def test_a_missing_benchmark_gives_an_empty_window_not_the_whole_sample():
    """A stress number quietly computed over every day looks like one."""
    returns = frame(AAA=noise(50, 7))
    assert len(corr.stress_index(returns, benchmark="RSP")) == 0


# --------------------------------------------------------------------------- #
# The verdicts -- the point of measuring three windows
# --------------------------------------------------------------------------- #


def test_strong_everywhere_is_stable():
    assert corr.verdict(0.9, 0.85, 0.8) == corr.STABLE


def test_strong_only_when_the_market_falls_is_flagged_as_such():
    """The dangerous case: looks like diversification until the day it isn't."""
    assert corr.verdict(0.1, 0.2, 0.9) == corr.STRESS_ONLY


def test_a_link_that_fades_in_the_tail_is_diversification_working():
    assert corr.verdict(0.8, 0.8, 0.1) == corr.FADES


def test_a_quiet_quarter_does_not_downgrade_a_link_the_tail_agrees_on():
    """Regression: `recent` is context, not a vote.

    A pair the long window and the sell-off both call strong is stable even
    if the last quarter was quiet. An earlier cut of this logic required all
    three windows and silently reported such a pair as weak.
    """
    assert corr.verdict(0.39, 0.64, 1.0) == corr.STABLE


def test_a_link_only_the_last_quarter_sees_is_emerging():
    assert corr.verdict(0.9, 0.2, 0.1) == corr.EMERGING


def test_a_strong_link_with_no_tail_data_still_counts():
    """Missing stress days are not evidence of diversification."""
    assert corr.verdict(0.8, 0.8, None) == corr.STABLE


def test_weak_is_a_finding_too():
    assert corr.verdict(0.1, 0.2, 0.15) == corr.WEAK


def test_no_data_at_all_is_unmeasured():
    assert corr.verdict(None, None, None) == corr.UNMEASURED


def test_the_sign_does_not_change_the_verdict():
    """An inverse pair is as correlated as a direct one, for a cap's purposes."""
    assert corr.verdict(-0.9, -0.85, -0.8) == corr.STABLE


# --------------------------------------------------------------------------- #
# A pair, end to end
# --------------------------------------------------------------------------- #


def test_a_stress_only_pair_is_caught_end_to_end():
    """Two series that are independent day to day and identical in a sell-off.

    Built deliberately: on the benchmark's worst days both legs take the same
    shock, and on every other day they are unrelated. A full-sample number
    would call this diversification.

    The shock is the same size as an ordinary day's move, so those twenty
    days cannot dominate the long window's variance -- otherwise the test
    would be measuring a link the long window can see too, which is a
    different verdict.
    """
    n = 400
    rng = np.random.default_rng(11)
    rsp = rng.normal(0.0, 0.01, n)
    left, right = rng.normal(0.0, 0.01, n), rng.normal(0.0, 0.01, n)
    worst = np.argsort(rsp)[: int(n * corr.STRESS_QUANTILE)]
    shock = rng.normal(0.0, 0.01, len(worst))
    left[worst], right[worst] = shock, shock

    returns = frame(RSP=rsp, AAA=left, BBB=right)
    result = corr.measure_pair(
        returns, "AAA vs BBB", ["AAA"], ["BBB"], corr.stress_index(returns)
    )
    assert result.verdict == corr.STRESS_ONLY
    assert abs(result.stress) > corr.STRONG
    assert abs(result.long) < corr.STRONG
    assert result.stress_days == len(worst)


def test_a_pair_with_a_missing_leg_is_unmeasured():
    returns = frame(AAA=noise(100, 12))
    result = corr.measure_pair(returns, "x", ["AAA"], ["GONE"], pd.Index([]))
    assert result.verdict == corr.UNMEASURED and result.long is None


# --------------------------------------------------------------------------- #
# Group cohesion and cross-group links
# --------------------------------------------------------------------------- #


def test_cohesion_finds_the_member_that_does_not_belong():
    """The check nobody had run on EXPOSURE_GROUPS: is the group one bet?"""
    n = 300
    shared = noise(n, 13)
    returns = frame(AAA=shared, BBB=shared * 1.1, ODD=noise(n, 14))
    [row] = corr.cohesion(returns, {"Made up": ("AAA", "BBB", "ODD")})
    assert row["members"] == 3
    assert row["loosest_member"] == "ODD"
    assert row["mean_pairwise"] < 0.9        # dragged down by the odd one
    assert row["min_pairwise"] < 0.3


def test_a_group_of_one_is_not_reported_on():
    returns = frame(AAA=noise(50, 15))
    assert corr.cohesion(returns, {"Alone": ("AAA",)}) == []


def test_cohesion_lists_the_least_coherent_group_first():
    n = 300
    tight = noise(n, 16)
    returns = frame(
        AAA=tight, BBB=tight * 1.02,           # a real group
        CCC=noise(n, 17), DDD=noise(n, 18),    # a label, not a bet
    )
    rows = corr.cohesion(returns, {"Tight": ("AAA", "BBB"), "Loose": ("CCC", "DDD")})
    assert [r["group"] for r in rows] == ["Loose", "Tight"]


def test_cross_group_measures_every_pair_of_groups():
    n = 300
    shared = noise(n, 19)
    returns = frame(RSP=noise(n, 20), AAA=shared, BBB=shared, CCC=noise(n, 21))
    groups = {"One": ("AAA",), "Two": ("BBB",), "Three": ("CCC",)}
    results = corr.cross_group(returns, corr.stress_index(returns), groups)
    assert len(results) == 3                   # 3 groups -> 3 pairs
    top = results[0]
    assert set(top.left) | set(top.right) == {"AAA", "BBB"}


# --------------------------------------------------------------------------- #
# The report and its rendering
# --------------------------------------------------------------------------- #


def test_the_report_names_every_hypothesis_even_the_ones_that_fail():
    """A story that is wrong must be recorded as wrong, not quietly dropped."""
    n = 300
    returns = frame(RSP=noise(n, 22), UUP=noise(n, 23), TLT=noise(n, 24))
    data = corr.report(returns)
    labels = [h["label"] for h in data["hypotheses"]]
    assert labels == [label for label, _, _ in corr.HYPOTHESES]
    dollar_duration = next(h for h in data["hypotheses"] if h["label"] == "Dollar vs duration")
    assert dollar_duration["verdict"] in (corr.WEAK, corr.UNMEASURED)


def test_the_report_carries_its_own_sample_size():
    n = 300
    returns = frame(RSP=noise(n, 25), UUP=noise(n, 26))
    data = corr.report(returns)
    assert data["observations"] == n
    assert data["stress_days"] == int(n * corr.STRESS_QUANTILE)
    assert data["windows"]["strong_threshold"] == corr.STRONG


def test_render_reads_as_a_report_and_says_it_changes_nothing():
    n = 300
    returns = frame(RSP=noise(n, 27), UUP=noise(n, 28), TLT=noise(n, 29))
    text = corr.render(corr.report(returns))
    assert "The stories, adjudicated" in text
    assert "Dollar vs duration" in text
    assert "Nothing here changes a cap." in text


def test_the_module_cannot_reach_a_broker_or_write_anything():
    """The structural guarantee, asserted rather than assumed.

    CI greps analysis/ for order paths and file writes; this is the same
    check close to the code it protects, so a future edit fails here first.
    """
    source = (corr.__file__ or "")
    assert source.endswith("correlations.py")
    with open(source, encoding="utf-8") as fh:
        text = fh.read()
    for forbidden in ("submit_order", "ExecutionEngine", "broker", ".write_text("):
        assert forbidden not in text, forbidden
