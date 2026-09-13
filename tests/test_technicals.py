"""Indicator math against independent reference implementations.

The reference functions here are written from the textbook definitions rather
than by copying the module, so a change of behaviour in ``technicals`` shows up
as a failure instead of being mirrored on both sides.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from orchestrator import technicals


def make_frame(closes: list[float], volumes: list[float] | None = None) -> pd.DataFrame:
    """Daily OHLCV frame in yfinance's column convention."""
    index = pd.date_range("2024-01-01", periods=len(closes), freq="B")
    close = pd.Series(closes, dtype=float, index=index)
    return pd.DataFrame(
        {
            "Open": close.shift(1).bfill(),
            "High": close * 1.01,
            "Low": close * 0.99,
            "Close": close,
            "Volume": pd.Series(
                volumes if volumes is not None else [1_000.0] * len(closes),
                dtype=float,
                index=index,
            ),
        }
    )


def reference_rsi(closes: list[float], period: int = 14) -> float:
    deltas = np.diff(np.asarray(closes, dtype=float))
    gains, losses = np.clip(deltas, 0, None), np.clip(-deltas, 0, None)

    def smooth(values):
        average = values[:period].mean()
        for value in values[period:]:
            average = (average * (period - 1) + value) / period
        return average

    average_gain, average_loss = smooth(gains), smooth(losses)
    if average_loss == 0:
        return 100.0
    return 100.0 - 100.0 / (1.0 + average_gain / average_loss)


# --------------------------------------------------------------------------- #
# Individual indicators
# --------------------------------------------------------------------------- #


def test_sma_is_the_mean_of_the_last_n_bars():
    close = pd.Series([float(i) for i in range(1, 21)])
    assert technicals.simple_moving_average(close, 5) == pytest.approx(18.0)
    assert technicals.simple_moving_average(close, 20) == pytest.approx(10.5)


def test_sma_reports_none_rather_than_a_short_window():
    assert technicals.simple_moving_average(pd.Series([1.0, 2.0]), 50) is None


def test_rsi_matches_the_wilder_reference():
    rng = np.random.default_rng(7)
    closes = list(100 + np.cumsum(rng.normal(0, 1.5, 60)))
    assert technicals.relative_strength_index(pd.Series(closes)) == pytest.approx(
        reference_rsi(closes), rel=1e-9
    )


def test_rsi_is_100_when_nothing_falls():
    closes = pd.Series([float(i) for i in range(1, 40)])
    assert technicals.relative_strength_index(closes) == pytest.approx(100.0)


def test_rsi_of_a_flat_series_is_neutral_not_infinite():
    # Zero average loss would otherwise divide through to an infinity.
    assert technicals.relative_strength_index(pd.Series([50.0] * 40)) == 50.0


def test_macd_histogram_is_the_gap_to_the_signal_line():
    closes = pd.Series([100 + i * 0.5 for i in range(80)])
    line, signal, histogram = technicals.macd(closes)
    assert histogram == pytest.approx(line - signal)
    assert line > 0  # a steadily rising series


def test_macd_reports_none_on_thin_history():
    assert technicals.macd(pd.Series([1.0] * 10)) == (None, None, None)


def test_trailing_return_is_a_fraction():
    closes = pd.Series([100.0, 101.0, 110.0])
    assert technicals.trailing_return(closes, 2) == pytest.approx(0.10)
    assert technicals.trailing_return(closes, 99) is None


def test_relative_volume_compares_with_the_trailing_average():
    volume = pd.Series([100.0] * 19 + [200.0])
    assert technicals.relative_volume(volume, period=20) == pytest.approx(200.0 / 105.0)


def test_annualised_volatility_scales_by_root_252():
    rng = np.random.default_rng(3)
    closes = pd.Series(100 + np.cumsum(rng.normal(0, 1.0, 60)))
    expected = closes.pct_change().dropna().iloc[-20:].std(ddof=1) * np.sqrt(252)
    assert technicals.annualised_volatility(closes) == pytest.approx(expected)


# --------------------------------------------------------------------------- #
# Snapshot assembly
# --------------------------------------------------------------------------- #


def test_snapshot_over_full_history_populates_every_field():
    rng = np.random.default_rng(11)
    frame = make_frame(list(100 + np.cumsum(rng.normal(0.05, 1.0, 300))))
    snapshot = technicals.build_snapshot(frame)

    assert snapshot.bars == 300
    assert snapshot.as_of == "2025-02-21"
    for field, value in snapshot.as_dict().items():
        assert value is not None, f"{field} should be populated by 300 bars"


def test_snapshot_on_thin_history_degrades_field_by_field():
    """30 bars is enough for RSI, not for a 200-day average."""
    frame = make_frame([100.0 + i for i in range(30)])
    snapshot = technicals.build_snapshot(frame)

    assert snapshot.sma20 is not None
    assert snapshot.rsi14 is not None
    assert snapshot.sma200 is None
    assert snapshot.distance_sma200 is None
    assert snapshot.return_63d is None


def test_snapshot_position_in_52w_range():
    frame = make_frame([100.0] * 10 + [200.0] + [150.0])
    snapshot = technicals.build_snapshot(frame)
    assert snapshot.low_52w == pytest.approx(100.0)
    assert snapshot.high_52w == pytest.approx(200.0)
    assert snapshot.position_in_52w_range == pytest.approx(0.5)


def test_snapshot_reuses_the_engines_atr():
    from app.market_data import calculate_atr

    frame = make_frame([100.0 + (i % 7) for i in range(60)])
    snapshot = technicals.build_snapshot(frame)
    assert snapshot.atr14 == pytest.approx(calculate_atr(frame))
    assert snapshot.atr_pct_of_price == pytest.approx(snapshot.atr14 / snapshot.last_close)


def test_snapshot_rejects_an_unusable_frame():
    with pytest.raises(ValueError, match="missing columns"):
        technicals.build_snapshot(pd.DataFrame({"Close": [1.0, 2.0]}))
    with pytest.raises(ValueError, match="no usable rows"):
        technicals.build_snapshot(make_frame([100.0, 101.0]).assign(Close=float("nan")))


def test_snapshot_lines_render_gaps_as_na():
    lines = "\n".join(technicals.build_snapshot(make_frame([100.0, 101.0])).as_lines())
    assert "n/a" in lines
    assert "Last close 101.00" in lines
