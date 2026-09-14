"""A backtest that flatters itself is worse than none.

Three properties decide whether this measures anything: the stop cannot be
sized with volatility the trader had not yet seen, a stop is hit intraday
rather than at the close, and a gap fills worse than the stop. Each is tested
against a hand-built price series where the right answer is arithmetic.
"""

from __future__ import annotations

import pandas as pd
import pytest

from app import risk_engine
from backtest.simulate import MIN_WARMUP_BARS, simulate_series, simulate_trade
from config import settings as cfg


def frame(bars: list[tuple[float, float, float, float]], start="2026-01-01") -> pd.DataFrame:
    """OHLC from (open, high, low, close) tuples on business days."""
    index = pd.bdate_range(start=start, periods=len(bars))
    return pd.DataFrame(
        {
            "Open": [b[0] for b in bars],
            "High": [b[1] for b in bars],
            "Low": [b[2] for b in bars],
            "Close": [b[3] for b in bars],
        },
        index=index,
    )


def flat(n: int, price: float = 100.0, spread: float = 1.0) -> list[tuple]:
    """Warm-up bars with a steady range, so ATR is well defined."""
    return [(price, price + spread, price - spread, price)] * n


# --- no look-ahead --------------------------------------------------------


def test_entry_is_the_bar_after_the_signal():
    """A signal at the close of D cannot be filled at D's open."""
    bars = flat(MIN_WARMUP_BARS + 1) + [(150.0, 151.0, 149.0, 150.0), (160.0, 161.0, 159.0, 160.0)]
    df = frame(bars)
    signal_index = MIN_WARMUP_BARS
    trade = simulate_trade(df, signal_index, horizon_days=1)
    assert trade is not None
    assert trade.entry_price == float(df.iloc[signal_index + 1]["Open"])
    assert trade.entry_date == str(df.index[signal_index + 1].date())


def test_the_stop_uses_only_volatility_available_at_the_signal():
    """A later volatility explosion must not change a stop set before it."""
    calm = flat(MIN_WARMUP_BARS + 1)
    entry = [(100.0, 101.0, 99.0, 100.0)]

    quiet = frame(calm + entry + flat(5))
    wild = frame(calm + entry + [(100.0, 180.0, 20.0, 100.0)] * 5)

    signal_index = MIN_WARMUP_BARS
    a = simulate_trade(quiet, signal_index, horizon_days=5)
    b = simulate_trade(wild, signal_index, horizon_days=5)
    assert a is not None and b is not None
    assert a.atr == b.atr, "ATR leaked from bars after the signal"
    assert a.stop_price == b.stop_price


def test_a_signal_too_early_for_a_warm_atr_is_skipped():
    assert simulate_trade(frame(flat(MIN_WARMUP_BARS + 5)), 2) is None


def test_a_signal_on_the_last_bar_has_nothing_to_enter_on():
    df = frame(flat(MIN_WARMUP_BARS + 5))
    assert simulate_trade(df, len(df) - 1) is None


# --- stops are intraday ---------------------------------------------------


def test_a_stop_touched_intraday_counts_even_if_the_close_recovers():
    """Checking closes instead of lows would understate stop-outs badly."""
    bars = flat(MIN_WARMUP_BARS + 1) + [
        (100.0, 101.0, 99.0, 100.0),     # entry bar
        (100.0, 101.0, 80.0, 100.5),     # dips deep, closes higher
    ]
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=3)
    assert trade is not None
    assert trade.stopped_out
    assert trade.exit_price == trade.stop_price


def test_a_stop_can_be_hit_on_the_entry_bar_itself():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0, 101.0, 50.0, 60.0), (60.0, 61.0, 59.0, 60.0)]
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=2)
    assert trade is not None and trade.stopped_out


def test_an_untouched_stop_exits_at_the_horizon_close():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0, 101.0, 99.5, 100.0)] * 4
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=3)
    assert trade is not None
    assert not trade.stopped_out
    assert trade.exit_price == 100.0


# --- gaps fill worse than the stop ---------------------------------------


def test_a_gap_through_the_stop_fills_at_the_open_not_the_stop():
    """Assuming you always get your stop price invents money."""
    bars = flat(MIN_WARMUP_BARS + 1) + [
        (100.0, 101.0, 99.0, 100.0),     # entry
        (70.0, 72.0, 68.0, 71.0),        # opens far below the stop
    ]
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=3)
    assert trade is not None
    assert trade.stopped_out and trade.gapped_through
    assert trade.exit_price == 70.0
    assert trade.exit_price < trade.stop_price, "filled better than the gap allowed"


def test_a_normal_stop_is_not_marked_as_gapped():
    bars = flat(MIN_WARMUP_BARS + 1) + [
        (100.0, 101.0, 99.0, 100.0),
        (100.0, 100.5, 80.0, 85.0),
    ]
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=3)
    assert trade.stopped_out and not trade.gapped_through


def test_a_short_gaps_upward_through_its_stop():
    bars = flat(MIN_WARMUP_BARS + 1) + [
        (100.0, 101.0, 99.0, 100.0),
        (130.0, 132.0, 128.0, 131.0),
    ]
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, side="sell", horizon_days=3)
    assert trade.stopped_out and trade.gapped_through
    assert trade.exit_price == 130.0


# --- the arithmetic is the engine's, not a copy --------------------------


def test_the_stop_matches_the_risk_engine():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0, 101.0, 99.0, 100.0)] * 3
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=2)
    assert trade.stop_price == risk_engine.calculate_stop_price(
        trade.entry_price, trade.atr, "buy", cfg.ATR_STOP_MULTIPLIER
    )


def test_the_size_matches_the_risk_engine():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0, 101.0, 99.0, 100.0)] * 3
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, equity=100_000.0, horizon_days=2)
    assert trade.qty == risk_engine.calculate_position_size(
        equity=100_000.0, price=trade.entry_price, max_position_pct=cfg.MAX_POSITION_PCT
    )


def test_a_wider_multiplier_gives_a_further_stop():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0, 101.0, 99.0, 100.0)] * 3
    tight = simulate_trade(frame(bars), MIN_WARMUP_BARS, stop_multiplier=1.0, horizon_days=2)
    wide = simulate_trade(frame(bars), MIN_WARMUP_BARS, stop_multiplier=3.0, horizon_days=2)
    assert wide.stop_price < tight.stop_price


def test_a_degenerate_atr_is_skipped_as_the_engine_would():
    """Flat bars give an ATR the engine refuses to size against."""
    bars = [(100.0, 100.0, 100.0, 100.0)] * (MIN_WARMUP_BARS + 5)
    assert simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=2) is None


# --- the number worth tuning ---------------------------------------------


def test_risk_per_trade_is_far_below_the_position_cap():
    """A 5% cap does not mean 5% at risk -- the stop distance decides."""
    bars = flat(MIN_WARMUP_BARS + 1, price=100.0, spread=1.0) + [(100.0, 101.0, 99.0, 100.0)] * 3
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, equity=100_000.0, horizon_days=2)
    assert 0 < trade.risk_pct_of_equity < cfg.MAX_POSITION_PCT
    expected = (trade.entry_price - trade.stop_price) * trade.qty / 100_000.0
    assert trade.risk_pct_of_equity == pytest.approx(expected)


def test_a_long_that_rises_has_a_positive_return():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0, 101.0, 99.0, 100.0), (110.0, 111.0, 109.0, 110.0)]
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, horizon_days=2)
    assert trade.return_pct > 0 and trade.pnl > 0


def test_a_short_that_rises_has_a_negative_return():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0, 101.0, 99.0, 100.0), (105.0, 106.0, 104.0, 105.0)]
    trade = simulate_trade(frame(bars), MIN_WARMUP_BARS, side="sell", horizon_days=2)
    assert trade.return_pct < 0


# --- sweeping a whole history --------------------------------------------


def test_a_series_produces_non_overlapping_sampled_trades():
    bars = flat(MIN_WARMUP_BARS + 1) + [(100.0 + i, 101.0 + i, 99.0 + i, 100.0 + i) for i in range(60)]
    trades = simulate_series(frame(bars), every=10, horizon_days=5)
    assert len(trades) >= 3
    dates = [t.entry_date for t in trades]
    assert len(dates) == len(set(dates))


def test_an_empty_history_yields_no_trades():
    assert simulate_series(frame(flat(3))) == []
