"""Daily bars, and a feed that only ever shows the engine what it could have seen.

``Bars`` holds one final OHLC frame per ticker, fetched once through the
race's own ``OhlcFetcher`` (the same yfinance call, ``auto_adjust=False``,
cut to final closes by ``last_final_session``), so the funds and the race
price everything from the same source.

**The traded scale** (calibration fix of 25 Nov 2026, Amendment 2026-11-25).
Yahoo's bars are split-adjusted: after a 3-for-1 split every earlier bar is
divided by three, so the series is continuous but no longer the price
anyone traded at. The books here hold shares bought at real prices (the
calibration copy at the account's recorded fills), so a split-adjusted bar
would mark a position bought at 209 at 70: on 2026-11-05 ITA split 3-for-1
and the copy's ITA, bought on 16 Oct at the recorded 209.07, was marked at
~69.7 for a week, a gap of ~4,590 that was the whole of calibration's
condition-1 fail. So ``Bars`` keeps the ``Stock Splits`` column yfinance
hands over and puts every bar back on the scale it traded at: each bar's
open, high, low, close and dividend are multiplied by the ratio of every
split dated after it, and ``split`` says which day a split falls on and by
how much, so a book can apply it to its shares that day
(``SimBroker.apply_split``). ``history`` -- what the engine's ATR and the
rules' moving averages read -- shows the bars as Yahoo showed them at the
moment asked about (``as_of``): the splits up to then taken out, the ones
after it not yet, so a series read across a split has no step in it, as the
live engine's did not. The race's own scoring reads the fetcher's frames
directly and is untouched: it enters and exits on one series, where the
adjustment cancels out.

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

from datetime import date, datetime, timedelta, timezone
from typing import Iterable, Optional, Sequence
from zoneinfo import ZoneInfo

import pandas as pd

from analysis.cycle_day import MARKET_OPEN_NY, closes_at
from app.market_data import MarketDataError, YFinanceMarketData
from config import settings as cfg
from config.market_calendar import is_trading_day

#: Enough history before the first session for a 90-day ATR window.
LEAD_DAYS = 150


def _day(value: object) -> date:
    if hasattr(value, "date") and callable(value.date):
        return value.date()
    return pd.Timestamp(value).date()


class Bars:
    """Final daily bars per ticker, indexed by exchange date, on the scale they traded at."""

    def __init__(self, frames: dict[str, pd.DataFrame]) -> None:
        self._frames: dict[str, pd.DataFrame] = {}
        self._rows: dict[str, dict[date, tuple[float, float, float, float, float]]] = {}
        #: Ticker -> {the day a split took effect: its ratio (3.0 for 3-for-1, 0.1 for 1-for-10)}.
        self._splits: dict[str, dict[date, float]] = {}
        for ticker, frame in frames.items():
            self.add(ticker, frame)

    def add(self, ticker: str, frame: pd.DataFrame) -> None:
        ticker = ticker.strip().upper()
        if frame is None or frame.empty:
            self._frames[ticker] = pd.DataFrame(columns=["Open", "High", "Low", "Close"])
            self._rows[ticker] = {}
            self._splits[ticker] = {}
            return
        frame = frame.dropna(subset=["Open", "High", "Low", "Close"]).copy()
        frame.index = pd.DatetimeIndex([pd.Timestamp(_day(ts)) for ts in frame.index])
        frame = frame[~frame.index.duplicated(keep="last")].sort_index()
        frame, self._splits[ticker] = _traded_scale(frame)
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

    def split(self, ticker: str, day: date) -> float:
        """The ratio of a split that took effect on ``day`` (3.0 for 3-for-1), or 1.0 when none did.

        From that day's bar on, the bars are in the new scale; a book
        holding the name applies the same ratio to its shares that morning
        (``SimBroker.apply_split``), as the broker does.
        """
        return self._splits.get(ticker.strip().upper(), {}).get(day, 1.0)

    def sessions(self, calendar_ticker: str, first: date, last: date) -> list[date]:
        """Every session in [first, last] that ``calendar_ticker`` has a final bar for."""
        rows = self._rows.get(calendar_ticker.strip().upper(), {})
        return sorted(d for d in rows if first <= d <= last)

    def history(self, ticker: str, through: date, as_of: Optional[date] = None) -> pd.DataFrame:
        """Bars dated on or before ``through``, on the scale yfinance showed them at the end of ``as_of``.

        ``as_of`` is ``through`` unless given. The bars are kept on the scale
        each traded at; a split dated after a bar and on or before ``as_of``
        divides the bar by its ratio, as Yahoo did from the split's day on.
        That is what the live engine's "last 90 days" looked like at that
        moment -- one continuous series, the split's step taken out -- so
        an ATR read across a split sees no gap, while ``bar`` keeps the
        traded scale for fills, stops and marks. ``SimFeed`` asks for the
        history through the eve of a session as of the session itself: a
        split taking effect that morning is already in Yahoo's history by
        the open.
        """
        ticker = ticker.strip().upper()
        frame = self._frames.get(ticker)
        if frame is None or frame.empty:
            return pd.DataFrame(columns=["Open", "High", "Low", "Close"])
        frame = frame.loc[: pd.Timestamp(through)]
        return _as_shown(frame, self._splits.get(ticker, {}), through if as_of is None else as_of)

    def last_close_before(self, ticker: str, day: date) -> Optional[float]:
        frame = self.history(ticker, day - timedelta(days=1))
        return float(frame["Close"].iloc[-1]) if not frame.empty else None


def _traded_scale(frame: pd.DataFrame) -> tuple[pd.DataFrame, dict[date, float]]:
    """``frame`` with every bar put back on the scale it traded at, and the splits it carried.

    yfinance's ``Stock Splits`` column holds the ratio on the day a split
    took effect and 0 elsewhere; Yahoo's prices are divided by that ratio
    for every day before it. Each bar's open, high, low, close and dividend
    are multiplied back by the product of the ratios of every split dated
    after the bar, so the bars before a 3-for-1 are three times Yahoo's and
    the ones from the split on are unchanged. A frame without the column,
    or with no split in it, is returned as it was.
    """
    if "Stock Splits" not in frame.columns or frame.empty:
        return frame, {}
    ratios = pd.to_numeric(frame["Stock Splits"], errors="coerce").fillna(0.0).astype(float)
    ratios = ratios.where(ratios > 0, 1.0)
    splits = {ts.date(): float(r) for ts, r in ratios.items() if r != 1.0}
    if not splits:
        return frame, {}
    # The product of the ratios of the splits strictly after each bar: the
    # cumulative product from the end, less the bar's own ratio.
    later = (ratios[::-1].cumprod()[::-1] / ratios).astype(float)
    frame = frame.copy()
    for column in ("Open", "High", "Low", "Close", "Dividends"):
        if column in frame.columns:
            frame[column] = frame[column].astype(float) * later
    return frame, splits


def _as_shown(frame: pd.DataFrame, splits: dict[date, float], as_of: date) -> pd.DataFrame:
    """``frame`` (traded scale) as Yahoo showed it at the end of ``as_of``.

    Each bar is divided by the ratio of every split dated after it and on or
    before ``as_of``; a split after ``as_of`` had not happened yet and
    changes nothing. A frame with no such split is returned as it is.
    """
    applicable = [(day, ratio) for day, ratio in splits.items() if day <= as_of]
    if not applicable or frame.empty:
        return frame
    factor = pd.Series(1.0, index=frame.index)
    for day, ratio in applicable:
        before = frame.index < pd.Timestamp(day)
        factor[before] = factor[before] * ratio
    frame = frame.copy()
    for column in ("Open", "High", "Low", "Close", "Dividends"):
        if column in frame.columns:
            frame[column] = frame[column].astype(float) / factor
    return frame


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
        # As of the session: a split taking effect this morning has already
        # divided Yahoo's earlier bars, and the live engine's ATR saw no step.
        past = self._bars.history(ticker, session - timedelta(days=1), as_of=session)
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
    """Sessions: every NYSE trading day in [first, last] any of ``tickers`` has a final bar for.

    The union, not one ticker's dates: a single row yfinance leaves out of
    VT would otherwise drop that whole session for every fund -- its stops
    never checked, its cycle never dispatched. A date that is not a trading
    day by the exchange calendar is left out, whatever a vendor printed.
    """
    days: set[date] = set()
    for ticker in tickers:
        days.update(bars.sessions(ticker, first, last))
    return sorted(d for d in days if is_trading_day(d))


def in_regular_hours(moment: datetime) -> bool:
    """Whether ``moment`` falls in a regular New York session.

    09:30 to the close -- 16:00, or 13:00 on a half day
    (``analysis.cycle_day.closes_at``) -- on a trading day. The close itself
    is outside: at 16:00:00 the broker's clock already says the market is
    shut. A naive ``moment`` is read as UTC, as the journal's are.
    """
    utc = moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)
    local = utc.astimezone(_NY)
    day = local.date()
    return is_trading_day(day) and MARKET_OPEN_NY <= local.time() < closes_at(day)


_NY = ZoneInfo("America/New_York")


__all__ = ["Bars", "LEAD_DAYS", "SimFeed", "calendar", "in_regular_hours"]
