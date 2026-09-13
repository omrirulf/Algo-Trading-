"""Join each journalled signal to the return that actually followed it.

The only thing that makes a scoring tool worth running is that it cannot
flatter the strategy. There is exactly one way this module could do that, and
it is the reason most of the code below exists: **entering at a price that was
already known when the signal was produced.** A signal generated at 22:00
because of a stock's 6% move that day, "entered" at that day's close, scores
as a brilliant call. It is not a call at all.

So the entry bar is chosen from the signal's timestamp, not its date:

* ``auto`` (default) -- if the journal recorded an exact UTC timestamp and the
  signal fired before the session close, that day's close is still in the
  future and is used. Otherwise the next session's close is used.
* ``next`` -- always the next session's close. Never wrong, mildly pessimistic:
  it gives up the same-day move a news signal is trying to capture.
* ``same`` -- always the signal date's own close. Only honest if you know your
  heartbeat runs during the session; offered because forcing ``next`` on an
  intraday strategy understates it.

Lines written before ``ts_utc`` existed have a timezone-naive timestamp. Those
are never trusted with a same-day entry under ``auto``.

Fetching is isolated behind ``PriceSource`` so every rule above is tested
against hand-built series with no network.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from typing import Optional, Protocol, Sequence

log = logging.getLogger(__name__)

ENTRY_AUTO = "auto"
ENTRY_NEXT = "next"
ENTRY_SAME = "same"
ENTRY_RULES = (ENTRY_AUTO, ENTRY_NEXT, ENTRY_SAME)

#: US equities close at 16:00 ET, which is 20:00 UTC under EDT and 21:00 under
#: EST. The earlier of the two is used deliberately: in winter it misclassifies
#: a 20:30 signal as after-hours and falls back to the next session, which
#: costs a little realism and cannot manufacture a look-ahead.
SESSION_CLOSE_UTC = time(20, 0)

#: Calendar days of history fetched before the first signal, so there is always
#: a bar to anchor on even across a long weekend or holiday.
HISTORY_LEAD_DAYS = 10

STATUS_OK = "ok"
STATUS_PENDING = "pending"
STATUS_NO_ENTRY_BAR = "no_entry_bar"
STATUS_NO_HISTORY = "no_history"
STATUS_NO_TIMESTAMP = "no_timestamp"


@dataclass(frozen=True)
class PriceSeries:
    """Daily closes for one ticker, ascending by date."""

    ticker: str
    bars: Sequence[tuple[date, float]] = ()

    def __len__(self) -> int:
        return len(self.bars)


@dataclass(frozen=True)
class ForwardReturn:
    entry_date: date
    exit_date: date
    entry_price: float
    exit_price: float
    pct: float


@dataclass(frozen=True)
class ReturnLookup:
    status: str
    value: Optional[ForwardReturn] = None

    @property
    def ok(self) -> bool:
        return self.status == STATUS_OK and self.value is not None


class PriceSource(Protocol):
    def closes(self, ticker: str, start: date, end: date) -> PriceSeries: ...


# --------------------------------------------------------------------------- #
# Entry selection -- the part that must never look backwards
# --------------------------------------------------------------------------- #


def entry_rule_for(
    timestamp: Optional[datetime],
    timestamp_is_exact: bool,
    entry: str = ENTRY_AUTO,
    session_close: time = SESSION_CLOSE_UTC,
) -> str:
    """Resolve ``auto`` to ``same`` or ``next`` for one signal."""
    if entry in (ENTRY_SAME, ENTRY_NEXT):
        return entry
    if timestamp is None or not timestamp_is_exact:
        return ENTRY_NEXT
    return ENTRY_SAME if timestamp.astimezone(timezone.utc).timetz().replace(
        tzinfo=None
    ) < session_close else ENTRY_NEXT


def forward_return(
    series: PriceSeries,
    timestamp: Optional[datetime],
    horizon: int,
    timestamp_is_exact: bool = False,
    entry: str = ENTRY_AUTO,
    session_close: time = SESSION_CLOSE_UTC,
) -> ReturnLookup:
    """Return over ``horizon`` sessions after the signal, or why there isn't one."""
    if horizon < 1:
        raise ValueError(f"horizon must be at least 1 session, got {horizon}")
    if timestamp is None:
        return ReturnLookup(STATUS_NO_TIMESTAMP)
    if not series.bars:
        return ReturnLookup(STATUS_NO_HISTORY)

    rule = entry_rule_for(timestamp, timestamp_is_exact, entry, session_close)
    signal_date = timestamp.astimezone(timezone.utc).date()

    entry_index = _first_bar_index(series.bars, signal_date, inclusive=rule == ENTRY_SAME)
    if entry_index is None:
        return ReturnLookup(STATUS_NO_ENTRY_BAR)

    exit_index = entry_index + horizon
    if exit_index >= len(series.bars):
        # The future this signal predicted has not happened yet.
        return ReturnLookup(STATUS_PENDING)

    entry_date, entry_price = series.bars[entry_index]
    exit_date, exit_price = series.bars[exit_index]
    if entry_price <= 0:
        return ReturnLookup(STATUS_NO_ENTRY_BAR)

    return ReturnLookup(
        STATUS_OK,
        ForwardReturn(
            entry_date=entry_date,
            exit_date=exit_date,
            entry_price=entry_price,
            exit_price=exit_price,
            pct=exit_price / entry_price - 1.0,
        ),
    )


def _first_bar_index(
    bars: Sequence[tuple[date, float]], signal_date: date, inclusive: bool
) -> Optional[int]:
    for index, (bar_date, _) in enumerate(bars):
        if bar_date > signal_date or (inclusive and bar_date == signal_date):
            return index
    return None


# --------------------------------------------------------------------------- #
# Price fetching
# --------------------------------------------------------------------------- #


class YFinancePriceSource:
    """Daily closes from yfinance, one fetch per ticker, cached in memory."""

    def __init__(self) -> None:
        self._cache: dict[str, PriceSeries] = {}

    def closes(self, ticker: str, start: date, end: date) -> PriceSeries:
        cached = self._cache.get(ticker)
        if cached is not None:
            return cached
        series = PriceSeries(ticker, self._fetch(ticker, start, end))
        self._cache[ticker] = series
        return series

    def _fetch(self, ticker: str, start: date, end: date) -> list[tuple[date, float]]:
        try:
            import yfinance as yf
        except ImportError as exc:  # pragma: no cover - dependency is pinned
            log.error("yfinance unavailable: %s", exc)
            return []

        try:
            frame = yf.Ticker(ticker).history(
                start=(start - timedelta(days=HISTORY_LEAD_DAYS)).isoformat(),
                # yfinance treats ``end`` as exclusive.
                end=(end + timedelta(days=1)).isoformat(),
                interval="1d",
                auto_adjust=False,
            )
        except Exception as exc:  # noqa: BLE001 - a missing series is a status, not a crash
            log.warning("price history unavailable for %s: %s", ticker, exc)
            return []
        if frame is None or getattr(frame, "empty", True) or "Close" not in frame.columns:
            log.warning("no price history returned for %s", ticker)
            return []

        bars: list[tuple[date, float]] = []
        for index, value in frame["Close"].dropna().items():
            try:
                bars.append((_as_date(index), float(value)))
            except (TypeError, ValueError):
                continue
        bars.sort(key=lambda bar: bar[0])
        return bars


def _as_date(value: object) -> date:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    import pandas as pd

    return pd.Timestamp(value).date()
