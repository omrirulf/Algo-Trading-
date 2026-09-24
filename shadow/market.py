"""Daily bars, and a feed that only ever shows the engine what it could have seen.

``Bars`` holds one final OHLC frame per ticker, fetched once through the
race's own ``OhlcFetcher`` (the same yfinance call, ``auto_adjust=False``,
cut to final closes by ``last_final_session``), so the funds and the race
price everything from the same source.

``SimFeed`` IS ``app.market_data.YFinanceMarketData`` -- the class the live
engine uses -- with only ``_history`` replaced: instead of asking yfinance
for "the last 90 days", it hands back the same 90 calendar days as of the
simulated moment. So ``get_latest_price`` and ``get_atr`` are the
production methods, running the production ``calculate_atr``.

The simulated moment is the open of session T (see ``shadow.fund``). Live,
the cycle runs during the session, and yfinance's last row is today's
partial bar; here the last row is a partial bar for T made of the only
thing known at the open: O = H = L = C = Open[T]. Bars after T never
exist in the slice. Results are cached per (ticker, T): a thousand funds
read the same numbers.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import Iterable, Optional, Sequence

import pandas as pd

from app.market_data import MarketDataError, YFinanceMarketData
from config import settings as cfg

#: Enough history before the first session for a 90-day ATR window.
LEAD_DAYS = 150


def _day(value: object) -> date:
    if hasattr(value, "date") and callable(value.date):
        return value.date()
    return pd.Timestamp(value).date()


class Bars:
    """Final daily bars per ticker, indexed by exchange date."""

    def __init__(self, frames: dict[str, pd.DataFrame]) -> None:
        self._frames: dict[str, pd.DataFrame] = {}
        self._rows: dict[str, dict[date, tuple[float, float, float, float, float]]] = {}
        for ticker, frame in frames.items():
            self.add(ticker, frame)

    def add(self, ticker: str, frame: pd.DataFrame) -> None:
        ticker = ticker.strip().upper()
        if frame is None or frame.empty:
            self._frames[ticker] = pd.DataFrame(columns=["Open", "High", "Low", "Close"])
            self._rows[ticker] = {}
            return
        frame = frame.dropna(subset=["Open", "High", "Low", "Close"]).copy()
        frame.index = pd.DatetimeIndex([pd.Timestamp(_day(ts)) for ts in frame.index])
        frame = frame[~frame.index.duplicated(keep="last")].sort_index()
        dividends = frame["Dividends"] if "Dividends" in frame.columns else pd.Series(0.0, index=frame.index)
        self._frames[ticker] = frame
        self._rows[ticker] = {
            ts.date(): (float(r.Open), float(r.High), float(r.Low), float(r.Close),
                        float(d) if d == d else 0.0)
            for ts, r, d in zip(frame.index, frame.itertuples(), dividends)
        }

    @classmethod
    def fetch(cls, tickers: Iterable[str], start: date, end: date, fetcher) -> "Bars":
        """Through an ``OhlcFetcher`` (the race's), widest window first."""
        return cls({t: fetcher.ohlc(t, start - timedelta(days=LEAD_DAYS), end) for t in sorted(set(tickers))})

    def tickers(self) -> list[str]:
        return sorted(self._frames)

    def bar(self, ticker: str, day: date) -> Optional[tuple[float, float, float, float, float]]:
        """``(open, high, low, close, dividend)`` on ``day``, or None."""
        return self._rows.get(ticker.strip().upper(), {}).get(day)

    def sessions(self, calendar_ticker: str, first: date, last: date) -> list[date]:
        """Every session in [first, last] that ``calendar_ticker`` has a final bar for."""
        rows = self._rows.get(calendar_ticker.strip().upper(), {})
        return sorted(d for d in rows if first <= d <= last)

    def history(self, ticker: str, through: date) -> pd.DataFrame:
        """Bars dated on or before ``through``."""
        frame = self._frames.get(ticker.strip().upper())
        if frame is None or frame.empty:
            return pd.DataFrame(columns=["Open", "High", "Low", "Close"])
        return frame.loc[: pd.Timestamp(through)]

    def last_close_before(self, ticker: str, day: date) -> Optional[float]:
        frame = self.history(ticker, day - timedelta(days=1))
        return float(frame["Close"].iloc[-1]) if not frame.empty else None


class SimFeed(YFinanceMarketData):
    """The live market-data class, answering as of the open of one session."""

    def __init__(self, bars: Bars) -> None:
        super().__init__(lookback_days=cfg.OHLC_LOOKBACK_DAYS, atr_period=cfg.ATR_PERIOD)
        self._bars = bars
        self._session: Optional[date] = None
        self._slices: dict[str, pd.DataFrame] = {}
        self._atr: dict[str, float] = {}
        self._price: dict[str, float] = {}

    def at_open(self, session: date) -> None:
        """Move the clock to the open of ``session``; drop what was cached."""
        if session != self._session:
            self._session = session
            self._slices.clear()
            self._atr.clear()
            self._price.clear()

    @property
    def session(self) -> Optional[date]:
        return self._session

    def _history(self, ticker: str) -> pd.DataFrame:
        """What yfinance's "90d" would have returned at the open of the session."""
        if self._session is None:
            raise MarketDataError("the simulated clock is not set")
        ticker = ticker.strip().upper()
        cached = self._slices.get(ticker)
        if cached is not None:
            return cached
        session = self._session
        today = self._bars.bar(ticker, session)
        if today is None:
            raise MarketDataError(f"no bar for {ticker} on {session}")
        start = session - timedelta(days=self._lookback_days)
        past = self._bars.history(ticker, session - timedelta(days=1))
        past = past.loc[past.index > pd.Timestamp(start), ["Open", "High", "Low", "Close"]]
        opened = today[0]
        partial = pd.DataFrame(
            {"Open": [opened], "High": [opened], "Low": [opened], "Close": [opened]},
            index=pd.DatetimeIndex([pd.Timestamp(session)]),
        )
        frame = pd.concat([past, partial])
        self._slices[ticker] = frame
        return frame

    # The production methods, memoised per session: the same answer for
    # every fund that asks, computed once.
    def get_latest_price(self, ticker: str) -> float:
        ticker = ticker.strip().upper()
        if ticker not in self._price:
            self._price[ticker] = super().get_latest_price(ticker)
        return self._price[ticker]

    def get_atr(self, ticker: str) -> float:
        ticker = ticker.strip().upper()
        if ticker not in self._atr:
            self._atr[ticker] = super().get_atr(ticker)
        return self._atr[ticker]


def calendar(bars: Bars, tickers: Sequence[str], first: date, last: date) -> list[date]:
    """Sessions: the dates the first of ``tickers`` with any bars has final bars for."""
    for ticker in tickers:
        days = bars.sessions(ticker, first, last)
        if days:
            return days
    return []


__all__ = ["Bars", "LEAD_DAYS", "SimFeed", "calendar"]
