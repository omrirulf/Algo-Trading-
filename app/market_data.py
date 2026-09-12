"""Market data access: OHLC history, latest price, and Wilder ATR.

``calculate_atr`` is a pure function of a DataFrame so the stop-loss math can
be unit-tested without network access. Only ``YFinanceMarketData`` touches
the network.
"""

from __future__ import annotations

from typing import Protocol

import numpy as np
import pandas as pd

from config import settings as cfg


class MarketDataError(RuntimeError):
    """Raised when price/volatility data cannot be obtained or is unusable."""


def calculate_atr(ohlc: pd.DataFrame, period: int = cfg.ATR_PERIOD) -> float:
    """Wilder's Average True Range over the last ``period`` bars.

    Expects columns ``High``, ``Low``, ``Close`` (yfinance convention). Uses
    Wilder smoothing (an EMA with alpha = 1/period, seeded with the simple
    mean of the first ``period`` true ranges), which is the textbook ATR.
    """
    required = {"High", "Low", "Close"}
    if not required.issubset(ohlc.columns):
        raise MarketDataError(f"OHLC frame missing columns: {required - set(ohlc.columns)}")
    if period < 1:
        raise MarketDataError(f"ATR period must be >= 1, got {period}")

    df = ohlc[["High", "Low", "Close"]].dropna()
    if len(df) < period + 1:
        raise MarketDataError(
            f"need at least {period + 1} bars for a {period}-period ATR, got {len(df)}"
        )

    high = df["High"].to_numpy(dtype=float)
    low = df["Low"].to_numpy(dtype=float)
    close = df["Close"].to_numpy(dtype=float)
    prev_close = np.roll(close, 1)

    tr = np.maximum.reduce(
        [high - low, np.abs(high - prev_close), np.abs(low - prev_close)]
    )
    tr = tr[1:]  # first bar has no previous close

    atr = tr[:period].mean()
    for value in tr[period:]:
        atr = (atr * (period - 1) + value) / period

    atr = float(atr)
    if not np.isfinite(atr) or atr <= 0:
        raise MarketDataError(f"computed ATR is not a positive finite number: {atr}")
    return atr


class MarketDataProvider(Protocol):
    """What the execution engine needs from a market-data source."""

    def get_latest_price(self, ticker: str) -> float: ...

    def get_atr(self, ticker: str) -> float: ...


class YFinanceMarketData:
    """Live implementation backed by yfinance daily bars."""

    def __init__(
        self,
        lookback_days: int = cfg.OHLC_LOOKBACK_DAYS,
        atr_period: int = cfg.ATR_PERIOD,
    ) -> None:
        self._lookback_days = lookback_days
        self._atr_period = atr_period

    def _history(self, ticker: str) -> pd.DataFrame:
        import yfinance as yf  # imported lazily so tests never need it

        try:
            df = yf.Ticker(ticker).history(
                period=f"{self._lookback_days}d", interval="1d", auto_adjust=False
            )
        except Exception as exc:  # noqa: BLE001 - surface as a domain error
            raise MarketDataError(f"yfinance fetch failed for {ticker}: {exc}") from exc
        if df is None or df.empty:
            raise MarketDataError(f"no OHLC data returned for {ticker}")
        return df

    def get_latest_price(self, ticker: str) -> float:
        df = self._history(ticker)
        price = float(df["Close"].dropna().iloc[-1])
        if not np.isfinite(price) or price <= 0:
            raise MarketDataError(f"latest close for {ticker} is not a positive number: {price}")
        return price

    def get_atr(self, ticker: str) -> float:
        return calculate_atr(self._history(ticker), self._atr_period)
