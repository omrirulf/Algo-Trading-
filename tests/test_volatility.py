"""The VIX-regime measurement, proven on series whose answer is known.

Every test builds its own prices, so the suite needs no network and the
expected answer is a property of the construction rather than of whatever
the market did last quarter.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from analysis import volatility as vol
from config import settings as cfg


def days(n: int = 400) -> pd.DatetimeIndex:
    return pd.bdate_range("2020-01-01", periods=n)


def flat_vix(n: int, level: float) -> pd.Series:
    return pd.Series(float(level), index=days(n))


# --------------------------------------------------------------------------- #
# Forward returns
# --------------------------------------------------------------------------- #


def test_forward_return_looks_ahead_by_exactly_the_horizon():
    """Day t carries what a position opened at t would have made by t+h."""
    closes = pd.Series([100.0, 110.0, 121.0, 133.1], index=days(4))
    out = vol.forward_return(closes, 1)
    assert out.iloc[0] == pytest.approx(0.10)
    assert out.iloc[2] == pytest.approx(0.10)


def test_the_last_days_have_no_future_and_are_left_empty():
    """Filling them would invent the one thing this measures."""
    closes = pd.Series([100.0, 101.0, 102.0, 103.0, 104.0], index=days(5))
    out = vol.forward_return(closes, 3)
    assert out.iloc[-3:].isna().all()
    assert out.iloc[:2].notna().all()


def test_a_horizon_below_one_is_refused():
    with pytest.raises(ValueError):
        vol.forward_return(pd.Series([1.0, 2.0], index=days(2)), 0)


# --------------------------------------------------------------------------- #
# The trend split -- rising vs falling volatility
# --------------------------------------------------------------------------- #


def test_vix_trend_is_positive_while_fear_is_climbing():
    vix = pd.Series(np.linspace(12.0, 40.0, 60), index=days(60))
    trend = vol.vix_trend(vix, window=5)
    assert (trend.iloc[5:] > 0).all()


def test_vix_trend_is_negative_while_fear_is_receding():
    vix = pd.Series(np.linspace(40.0, 12.0, 60), index=days(60))
    trend = vol.vix_trend(vix, window=5)
    assert (trend.iloc[5:] < 0).all()


def test_the_first_days_have_no_history_and_count_as_neither():
    vix = pd.Series(np.linspace(12.0, 40.0, 30), index=days(30))
    assert (vol.vix_trend(vix, window=5).iloc[:5] == 0).all()


# --------------------------------------------------------------------------- #
# Banding
# --------------------------------------------------------------------------- #


def test_each_day_lands_in_exactly_one_band():
    """Bands are half-open, so 20.0 is 'uneasy' and not also 'normal'."""
    for level, expected in ((10.0, "calm (<15)"), (15.0, "normal (15-20)"),
                            (20.0, "uneasy (20-30)"), (30.0, "afraid (30-40)"),
                            (55.0, "panic (40+)")):
        hits = [label for label, low, high in vol.VIX_BANDS if low <= level < high]
        assert hits == [expected], f"{level} landed in {hits}"


def test_a_thin_band_reports_its_count_and_no_average():
    """A mean over eleven days is an anecdote, and must not read as evidence."""
    n = 300
    vix = pd.Series(12.0, index=days(n))
    vix.iloc[:10] = 45.0                       # only ten panic days
    market = pd.Series(np.linspace(100.0, 200.0, n), index=days(n))
    rows = {(r.band, r.horizon): r for r in vol.by_regime(vix, market)}
    panic = rows[("panic (40+)", "1m")]
    assert panic.days < vol.MIN_DAYS
    assert panic.mean_pct is None and panic.worst_pct is None


def test_a_band_that_always_rose_reports_a_positive_mean_and_a_full_win_rate():
    n = 300
    vix = flat_vix(n, 35.0)
    market = pd.Series(np.linspace(100.0, 200.0, n), index=days(n))
    rows = {(r.band, r.horizon): r for r in vol.by_regime(vix, market)}
    afraid = rows[("afraid (30-40)", "1m")]
    assert afraid.days >= vol.MIN_DAYS
    assert afraid.mean_pct > 0
    assert afraid.share_positive == 100.0


def test_the_worst_case_is_reported_beside_the_average():
    """The whole point: an average that hides a ruinous tail is a trap."""
    n = 300
    index = days(n)
    vix = flat_vix(n, 35.0)
    # Mostly drifting up, with one severe decline in the middle.
    market = pd.Series(np.linspace(100.0, 160.0, n), index=index)
    market.iloc[100:130] = np.linspace(130.0, 60.0, 30)
    rows = {(r.band, r.horizon): r for r in vol.by_regime(vix, market)}
    afraid = rows[("afraid (30-40)", "1m")]
    assert afraid.worst_pct < -20, "a severe drawdown must show in the worst column"
    assert afraid.mean_pct > afraid.worst_pct


def test_rising_and_falling_are_measured_separately():
    """Same VIX level, opposite outcomes -- the split must keep them apart."""
    n = 400
    index = days(n)
    # Fear climbs for the first half and recedes for the second.
    vix = pd.Series(np.concatenate([np.linspace(30.0, 39.0, n // 2),
                                    np.linspace(39.0, 30.0, n // 2)]), index=index)
    # The market falls while fear climbs and rallies while it recedes.
    market = pd.Series(np.concatenate([np.linspace(100.0, 60.0, n // 2),
                                       np.linspace(60.0, 120.0, n // 2)]), index=index)
    out = vol.by_regime_and_trend(vix, market, min_days=10)
    rising = {(r["band"], r["horizon"]): r for r in out["rising"]}
    falling = {(r["band"], r["horizon"]): r for r in out["falling"]}
    key = ("afraid (30-40)", "1m")
    assert rising[key]["mean_pct"] < 0, "buying into climbing fear should show as a loss"
    assert falling[key]["mean_pct"] > 0, "buying receding fear should show as a gain"


# --------------------------------------------------------------------------- #
# What the book already risks
# --------------------------------------------------------------------------- #


def test_true_range_is_relative_to_price_so_eras_compare():
    ohlc = pd.DataFrame(
        {"High": [102.0, 204.0], "Low": [98.0, 196.0], "Close": [100.0, 200.0]},
        index=days(2),
    )
    # Second bar's true range spans the gap from the previous close.
    out = vol.true_range(ohlc)
    assert len(out) == 1
    assert out.iloc[0] == pytest.approx((204.0 - 100.0) / 200.0)


def test_risk_per_trade_rises_with_volatility_at_the_same_position_size():
    """The finding this module exists to make visible.

    Size is a fixed share of equity and the stop is a multiple of ATR, so a
    band with twice the daily range carries twice the loss per trade -- with
    nobody having decided that.
    """
    n = 400
    index = days(n)
    vix = pd.Series(np.where(np.arange(n) < n // 2, 12.0, 35.0), index=index)
    close = pd.Series(100.0, index=index)
    # Calm half: 1% daily range. Fearful half: 4%.
    span = pd.Series(np.where(np.arange(n) < n // 2, 1.0, 4.0), index=index)
    ohlc = pd.DataFrame({"High": close + span / 2, "Low": close - span / 2, "Close": close})
    rows = {r["band"]: r for r in vol.risk_per_trade_by_regime(vix, ohlc)}
    calm, afraid = rows["calm (<15)"], rows["afraid (30-40)"]
    assert calm["median_tr_pct"] == pytest.approx(1.0, abs=0.01)
    assert afraid["median_tr_pct"] == pytest.approx(4.0, abs=0.01)
    assert afraid["risk_per_trade_pct"] == pytest.approx(4 * calm["risk_per_trade_pct"], rel=0.01)


def test_risk_per_trade_uses_the_caps_the_engine_actually_applies():
    n = 200
    index = days(n)
    close = pd.Series(100.0, index=index)
    ohlc = pd.DataFrame({"High": close + 0.5, "Low": close - 0.5, "Close": close})
    [row] = [r for r in vol.risk_per_trade_by_regime(flat_vix(n, 12.0), ohlc)
             if r["band"] == "calm (<15)"]
    expected = cfg.MAX_BROAD_FUND_PCT * cfg.ATR_STOP_MULTIPLIER * 0.01 * 100
    assert row["risk_per_trade_pct"] == pytest.approx(expected, rel=0.01)


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


def test_the_report_renders_without_ohlc():
    n = 200
    vix = flat_vix(n, 18.0)
    market = pd.Series(np.linspace(100.0, 120.0, n), index=days(n))
    data = vol.report(vix, market)
    assert data["risk_per_trade"] is None
    text = vol.render(data)
    assert "Does buying fear pay?" in text
    assert "What one trade already risks" not in text


def test_the_report_carries_every_section_when_given_bars():
    n = 400
    index = days(n)
    vix = pd.Series(np.linspace(10.0, 45.0, n), index=index)
    close = pd.Series(np.linspace(100.0, 140.0, n), index=index)
    ohlc = pd.DataFrame({"High": close * 1.01, "Low": close * 0.99, "Close": close})
    data = vol.report(vix, close, ohlc)
    text = vol.render(data)
    for heading in ("Does buying fear pay?", "rising or falling",
                    "What one trade already risks"):
        assert heading in text
    assert data["observations"] == n
