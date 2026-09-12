"""ATR math on synthetic OHLC frames; no yfinance calls."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from app.market_data import MarketDataError, calculate_atr


def _frame(highs, lows, closes):
    return pd.DataFrame({"High": highs, "Low": lows, "Close": closes})


def test_constant_range_gives_that_range():
    # every bar: high = close + 1, low = close - 1, close flat -> TR = 2 always
    n = 40
    closes = [100.0] * n
    df = _frame([c + 1 for c in closes], [c - 1 for c in closes], closes)
    assert calculate_atr(df, period=14) == pytest.approx(2.0)


def test_gap_is_included_in_true_range():
    # Day 2 gaps up: prev close 100, low 110, high 111. TR = max(1, 11, 10) = 11
    df = _frame([101, 111, 112], [99, 110, 111], [100, 110.5, 111.5])
    # period=2: TR series (skipping the first bar) = [11, max(1, 1.5, 0.5)=1.5]; seed = mean = 6.25
    assert calculate_atr(df, period=2) == pytest.approx(6.25)


def test_wilder_smoothing_matches_reference():
    rng = np.random.default_rng(0)
    n = 60
    close = 100 + np.cumsum(rng.normal(0, 1, n))
    high = close + rng.uniform(0.5, 2.0, n)
    low = close - rng.uniform(0.5, 2.0, n)
    df = _frame(high, low, close)

    # Independent reference implementation with pandas ewm (Wilder alpha=1/p, seed with SMA)
    p = 14
    prev_close = pd.Series(close).shift(1)
    tr = pd.concat(
        [pd.Series(high) - pd.Series(low), (pd.Series(high) - prev_close).abs(), (pd.Series(low) - prev_close).abs()],
        axis=1,
    ).max(axis=1).iloc[1:].reset_index(drop=True)
    ref = tr.iloc[:p].mean()
    for v in tr.iloc[p:]:
        ref = (ref * (p - 1) + v) / p

    assert calculate_atr(df, period=p) == pytest.approx(ref)


def test_too_few_bars_rejected():
    df = _frame([1] * 10, [0] * 10, [0.5] * 10)
    with pytest.raises(MarketDataError):
        calculate_atr(df, period=14)


def test_missing_columns_rejected():
    with pytest.raises(MarketDataError):
        calculate_atr(pd.DataFrame({"Close": [1, 2, 3]}), period=1)


def test_nan_rows_are_dropped_not_propagated():
    n = 30
    closes = [100.0] * n
    df = _frame([c + 1 for c in closes], [c - 1 for c in closes], closes)
    df.loc[5, "High"] = np.nan
    assert calculate_atr(df, period=14) == pytest.approx(2.0)
