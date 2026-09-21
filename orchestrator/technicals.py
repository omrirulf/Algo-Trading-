"""Technical indicators over a daily OHLCV frame.

Every function here is a pure function of a DataFrame, so the whole snapshot
can be unit-tested against reference values with no network access -- the same
arrangement as ``app.market_data.calculate_atr``, which this module reuses
rather than growing a second ATR implementation.

Nothing here raises on thin data. An indicator that does not have enough bars
to be meaningful reports ``None``, which renders as ``n/a`` in the prompt, so a
freshly listed ticker produces a short snapshot instead of no snapshot at all.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Optional

import numpy as np
import pandas as pd

from app.market_data import MarketDataError, calculate_atr
from orchestrator import formatting as fmt

#: Bars in a trading year, used for the 52-week range and to annualise vol.
TRADING_DAYS_YEAR = 252

RSI_PERIOD = 14
MACD_FAST, MACD_SLOW, MACD_SIGNAL = 12, 26, 9
VOLUME_AVG_PERIOD = 20
VOLATILITY_PERIOD = 20

REQUIRED_COLUMNS = ("High", "Low", "Close")


# --------------------------------------------------------------------------- #
# Indicator math
# --------------------------------------------------------------------------- #


def _wilder_average(values: np.ndarray, period: int) -> float:
    """Wilder smoothing seeded with the simple mean of the first ``period`` values."""
    average = float(values[:period].mean())
    for value in values[period:]:
        average = (average * (period - 1) + float(value)) / period
    return average


def simple_moving_average(close: pd.Series, period: int) -> Optional[float]:
    if len(close) < period:
        return None
    return fmt.clean(close.iloc[-period:].mean())


def relative_strength_index(close: pd.Series, period: int = RSI_PERIOD) -> Optional[float]:
    """Wilder's RSI in [0, 100]. ``None`` when there are too few bars."""
    if len(close) < period + 1:
        return None
    delta = close.diff().dropna().to_numpy(dtype=float)
    if len(delta) < period:
        return None

    average_gain = _wilder_average(np.clip(delta, 0.0, None), period)
    average_loss = _wilder_average(np.clip(-delta, 0.0, None), period)
    if average_loss == 0:
        # No down move in the window: RSI is 100 by definition, and dividing
        # through would give an infinity that has to be special-cased anyway.
        return 100.0 if average_gain > 0 else 50.0
    return fmt.clean(100.0 - 100.0 / (1.0 + average_gain / average_loss))


def macd(
    close: pd.Series,
    fast: int = MACD_FAST,
    slow: int = MACD_SLOW,
    signal: int = MACD_SIGNAL,
) -> tuple[Optional[float], Optional[float], Optional[float]]:
    """``(macd, signal, histogram)`` from the standard EMA pair."""
    if len(close) < slow + signal:
        return None, None, None
    fast_ema = close.ewm(span=fast, adjust=False).mean()
    slow_ema = close.ewm(span=slow, adjust=False).mean()
    line = fast_ema - slow_ema
    signal_line = line.ewm(span=signal, adjust=False).mean()
    macd_value = fmt.clean(line.iloc[-1])
    signal_value = fmt.clean(signal_line.iloc[-1])
    if macd_value is None or signal_value is None:
        return None, None, None
    return macd_value, signal_value, macd_value - signal_value


def trailing_return(close: pd.Series, bars: int) -> Optional[float]:
    """Fractional return over the last ``bars`` bars, e.g. ``0.048`` for +4.8%."""
    if len(close) < bars + 1:
        return None
    start = float(close.iloc[-bars - 1])
    if start <= 0:
        return None
    return fmt.clean(float(close.iloc[-1]) / start - 1.0)


def annualised_volatility(close: pd.Series, period: int = VOLATILITY_PERIOD) -> Optional[float]:
    if len(close) < period + 1:
        return None
    returns = close.pct_change().dropna().iloc[-period:]
    if len(returns) < 2:
        return None
    return fmt.clean(returns.std(ddof=1) * np.sqrt(TRADING_DAYS_YEAR))


def relative_volume(volume: pd.Series, period: int = VOLUME_AVG_PERIOD) -> Optional[float]:
    """Latest volume as a multiple of its trailing average."""
    if len(volume) < period:
        return None
    average = float(volume.iloc[-period:].mean())
    if average <= 0:
        return None
    return fmt.clean(float(volume.iloc[-1]) / average)


def _distance_from(price: float, level: Optional[float]) -> Optional[float]:
    if level is None or level <= 0:
        return None
    return price / level - 1.0


# --------------------------------------------------------------------------- #
# Snapshot
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class TechnicalSnapshot:
    """What the price series says, as plain data. No behaviour beyond rendering."""

    bars: int
    as_of: Optional[str]
    last_close: Optional[float]
    sma20: Optional[float]
    sma50: Optional[float]
    sma200: Optional[float]
    distance_sma20: Optional[float]
    distance_sma50: Optional[float]
    distance_sma200: Optional[float]
    rsi14: Optional[float]
    macd: Optional[float]
    macd_signal: Optional[float]
    macd_histogram: Optional[float]
    atr14: Optional[float]
    atr_pct_of_price: Optional[float]
    return_1d: Optional[float]
    return_5d: Optional[float]
    return_21d: Optional[float]
    return_63d: Optional[float]
    high_52w: Optional[float]
    low_52w: Optional[float]
    position_in_52w_range: Optional[float]
    relative_volume: Optional[float]
    annualised_volatility: Optional[float]

    def as_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "TechnicalSnapshot":
        """The inverse of ``as_dict``, tolerant of a journal line written
        before a field existed: anything missing reads as ``None``, exactly
        as thin history would have set it, and anything unknown is ignored."""
        return cls(**{name: data.get(name) for name in cls.__dataclass_fields__})

    def as_lines(self) -> list[str]:
        trend = (
            f"vs 20d SMA {fmt.num(self.sma20)} ({fmt.pct(self.distance_sma20)}), "
            f"50d {fmt.num(self.sma50)} ({fmt.pct(self.distance_sma50)}), "
            f"200d {fmt.num(self.sma200)} ({fmt.pct(self.distance_sma200)})"
        )
        if self.sma50 is not None and self.sma200 is not None:
            cross = "50d above 200d" if self.sma50 > self.sma200 else "50d below 200d"
            trend += f"; {cross}"

        return [
            f"Last close {fmt.num(self.last_close)}"
            + (f" (bar of {self.as_of})" if self.as_of else "")
            + f", from {self.bars} daily bars",
            f"Trend: {trend}",
            f"Momentum: RSI(14) {fmt.num(self.rsi14, 1)} | "
            f"MACD {fmt.num(self.macd, 3)} vs signal {fmt.num(self.macd_signal, 3)} "
            f"(histogram {fmt.num(self.macd_histogram, 3)})",
            f"Returns: 1d {fmt.pct(self.return_1d)} | 5d {fmt.pct(self.return_5d)} | "
            f"1m {fmt.pct(self.return_21d)} | 3m {fmt.pct(self.return_63d)}",
            f"52-week range: {fmt.num(self.low_52w)} - {fmt.num(self.high_52w)} "
            f"(now {fmt.pct(self.position_in_52w_range, signed=False)} of the way up)",
            f"Volatility: ATR(14) {fmt.num(self.atr14)} "
            f"({fmt.pct(self.atr_pct_of_price, signed=False)} of price) | "
            f"annualised 20d {fmt.pct(self.annualised_volatility, signed=False)}",
            f"Volume: {fmt.ratio(self.relative_volume)} the {VOLUME_AVG_PERIOD}-day average",
        ]


def build_snapshot(ohlc: pd.DataFrame) -> TechnicalSnapshot:
    """Compute every indicator that the supplied history supports.

    Raises ``ValueError`` only when the frame is unusable altogether (missing
    columns or no rows); thin-but-valid history is reported field by field.
    """
    missing = set(REQUIRED_COLUMNS) - set(ohlc.columns)
    if missing:
        raise ValueError(f"OHLC frame missing columns: {sorted(missing)}")

    frame = ohlc.dropna(subset=list(REQUIRED_COLUMNS))
    if frame.empty:
        raise ValueError("OHLC frame has no usable rows")

    close = frame["Close"].astype(float)
    last_close = float(close.iloc[-1])

    sma20 = simple_moving_average(close, 20)
    sma50 = simple_moving_average(close, 50)
    sma200 = simple_moving_average(close, 200)
    macd_value, macd_signal_value, macd_histogram = macd(close)

    year = close.iloc[-TRADING_DAYS_YEAR:]
    high_52w, low_52w = float(year.max()), float(year.min())
    span = high_52w - low_52w
    position = (last_close - low_52w) / span if span > 0 else None

    try:
        atr14 = calculate_atr(frame)
    except MarketDataError:
        atr14 = None

    volume = frame["Volume"].astype(float) if "Volume" in frame.columns else None

    return TechnicalSnapshot(
        bars=len(frame),
        as_of=_index_date(frame),
        last_close=last_close,
        sma20=sma20,
        sma50=sma50,
        sma200=sma200,
        distance_sma20=_distance_from(last_close, sma20),
        distance_sma50=_distance_from(last_close, sma50),
        distance_sma200=_distance_from(last_close, sma200),
        rsi14=relative_strength_index(close),
        macd=macd_value,
        macd_signal=macd_signal_value,
        macd_histogram=macd_histogram,
        atr14=atr14,
        atr_pct_of_price=(atr14 / last_close if atr14 and last_close > 0 else None),
        return_1d=trailing_return(close, 1),
        return_5d=trailing_return(close, 5),
        return_21d=trailing_return(close, 21),
        return_63d=trailing_return(close, 63),
        high_52w=high_52w,
        low_52w=low_52w,
        position_in_52w_range=position,
        relative_volume=relative_volume(volume) if volume is not None else None,
        annualised_volatility=annualised_volatility(close),
    )


def _index_date(frame: pd.DataFrame) -> Optional[str]:
    try:
        return pd.Timestamp(frame.index[-1]).date().isoformat()
    except (TypeError, ValueError):
        return None
