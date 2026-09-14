"""One synthetic trade at a time, through the engine's real arithmetic.

Three modelling decisions decide whether the output means anything, and each
is the kind of thing that quietly flatters a backtest if you get it wrong.

**No look-ahead.** The ATR behind a stop is computed from bars up to and
including the signal bar; entry is the *next* bar's open. A stop sized with
volatility the trader could not yet have seen would understate stop-outs.

**Stops are intraday.** A stop is hit when the bar's Low crosses it, not when
its Close does. Checking closes would understate stop-outs dramatically --
most stops are hit and recovered within a session.

**Gaps fill worse than the stop.** If a bar opens through the stop, the fill
is the open, not the stop price. Assuming you always get your stop price is
the single most common way a backtest invents money it would not have had.

The stop and size come from ``app.risk_engine`` itself rather than a
reimplementation, so this measures the code that actually trades.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd

from app import risk_engine
from app.market_data import calculate_atr
from config import settings as cfg

#: How long a position is held if the stop is never touched.
DEFAULT_HORIZON_DAYS = 10

#: Bars of history required before the first trade, so ATR is warmed up.
MIN_WARMUP_BARS = cfg.ATR_PERIOD + 1


@dataclass(frozen=True)
class Trade:
    """One synthetic round trip."""

    entry_date: str
    side: str
    entry_price: float
    stop_price: float
    atr: float
    exit_date: str
    exit_price: float
    stopped_out: bool
    gapped_through: bool
    qty: int
    equity: float

    @property
    def return_pct(self) -> float:
        """Per-share return, signed by direction."""
        move = (self.exit_price - self.entry_price) / self.entry_price
        return move if self.side == "buy" else -move

    @property
    def pnl(self) -> float:
        per_share = self.exit_price - self.entry_price
        if self.side == "sell":
            per_share = -per_share
        return per_share * self.qty

    @property
    def risk_pct_of_equity(self) -> float:
        """What this trade put at risk when it was opened.

        The number the position cap and the stop multiplier jointly decide,
        and the one worth tuning: ``qty * stop distance``, as a fraction of
        equity. A 5% cap does not mean 5% at risk.
        """
        if self.equity <= 0:
            return 0.0
        return (abs(self.entry_price - self.stop_price) * self.qty) / self.equity

    @property
    def realised_pct_of_equity(self) -> float:
        return self.pnl / self.equity if self.equity > 0 else 0.0


def _exit_for(
    bars: pd.DataFrame, side: str, stop: float
) -> tuple[int, float, bool, bool]:
    """Walk bars forward and return (index, fill, stopped_out, gapped_through)."""
    for offset in range(len(bars)):
        bar = bars.iloc[offset]
        open_, high, low = float(bar["Open"]), float(bar["High"]), float(bar["Low"])

        if side == "buy":
            if open_ <= stop:                      # gapped through overnight
                return offset, open_, True, True
            if low <= stop:
                return offset, stop, True, False
        else:
            if open_ >= stop:
                return offset, open_, True, True
            if high >= stop:
                return offset, stop, True, False

    last = len(bars) - 1
    return last, float(bars.iloc[last]["Close"]), False, False


def simulate_trade(
    ohlc: pd.DataFrame,
    signal_index: int,
    side: str = "buy",
    equity: float = 100_000.0,
    horizon_days: int = DEFAULT_HORIZON_DAYS,
    stop_multiplier: float = cfg.ATR_STOP_MULTIPLIER,
    max_position_pct: float = cfg.MAX_POSITION_PCT,
) -> Optional[Trade]:
    """One trade signalled at ``signal_index``, entered on the next bar.

    Returns ``None`` when the trade could not be opened at all -- not enough
    warm-up, no bar to enter on, a degenerate ATR the engine would reject, or
    no room under the cap. Those are outcomes, not errors.
    """
    if signal_index < MIN_WARMUP_BARS or signal_index >= len(ohlc) - 1:
        return None

    # Only bars the trader could have seen. The slice is exclusive of the
    # entry bar by construction, which is what keeps this honest.
    history = ohlc.iloc[: signal_index + 1]
    try:
        atr = calculate_atr(history)
    except Exception:  # noqa: BLE001 - thin history is an outcome, not a crash
        return None

    entry_bar = ohlc.iloc[signal_index + 1]
    entry_price = float(entry_bar["Open"])
    if entry_price <= 0 or atr <= 0:
        return None

    # The same sanity gate the engine applies before it will size anything.
    if not risk_engine.check_atr_sanity(atr, entry_price):
        return None

    try:
        stop = risk_engine.calculate_stop_price(entry_price, atr, side, stop_multiplier)
        qty = risk_engine.calculate_position_size(
            equity=equity, price=entry_price, max_position_pct=max_position_pct
        )
    except risk_engine.RiskViolation:
        return None
    if qty < cfg.MIN_ORDER_QTY:
        return None

    forward = ohlc.iloc[signal_index + 1 : signal_index + 1 + horizon_days]
    if forward.empty:
        return None

    offset, exit_price, stopped, gapped = _exit_for(forward, side, stop)
    return Trade(
        entry_date=str(ohlc.index[signal_index + 1].date()),
        side=side,
        entry_price=entry_price,
        stop_price=stop,
        atr=atr,
        exit_date=str(forward.index[offset].date()),
        exit_price=exit_price,
        stopped_out=stopped,
        gapped_through=gapped,
        qty=qty,
        equity=equity,
    )


def simulate_series(
    ohlc: pd.DataFrame,
    side: str = "buy",
    every: int = 5,
    equity: float = 100_000.0,
    horizon_days: int = DEFAULT_HORIZON_DAYS,
    stop_multiplier: float = cfg.ATR_STOP_MULTIPLIER,
    max_position_pct: float = cfg.MAX_POSITION_PCT,
) -> list[Trade]:
    """A trade every ``every`` bars across the history.

    Sampled rather than every bar so the trades overlap less; heavily
    overlapping trades share the same price moves and would make any
    hit-rate look more precise than it is.
    """
    trades = []
    for index in range(MIN_WARMUP_BARS, len(ohlc) - 1, max(1, every)):
        trade = simulate_trade(
            ohlc, index, side=side, equity=equity, horizon_days=horizon_days,
            stop_multiplier=stop_multiplier, max_position_pct=max_position_pct,
        )
        if trade is not None:
            trades.append(trade)
    return trades


__all__ = [
    "DEFAULT_HORIZON_DAYS",
    "MIN_WARMUP_BARS",
    "Trade",
    "simulate_trade",
    "simulate_series",
]
