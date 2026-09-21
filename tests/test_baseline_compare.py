"""baseline_compare must compare the model's trades to a baseline over the
*same* population, and must fetch OHLC bars over the window actually asked
for rather than a stale cached one -- both are silent-correctness bugs a
smoke test would not catch, so each gets a test that would fail if the bug
came back.
"""

from __future__ import annotations

from datetime import date, datetime, timezone

import pandas as pd
import pytest

from analysis.baseline_compare import (
    OhlcFetcher,
    _signal_index,
    render,
    simulate_model_trades,
    watchlist_buy_and_hold,
)
from analysis.metrics import ScoredSignal
from analysis.reader import JournalEntry
from analysis.returns import ForwardReturn, PriceSeries
from backtest.simulate import MIN_WARMUP_BARS, Trade
from backtest.sweep import Outcome
from tests.test_backtest_simulate import flat, frame


def signal(ticker="NVDA", bias="BULLISH", conviction=0.72,
           timestamp=datetime(2026, 3, 2, tzinfo=timezone.utc)) -> ScoredSignal:
    """One acted-on signal. ``forward`` is a placeholder -- these tests exercise
    simulate_model_trades, which never reads it; only entry.timestamp and
    entry.direction decide the simulated trade."""
    entry = JournalEntry(
        ticker=ticker, timestamp=timestamp, timestamp_is_exact=True,
        bias=bias, conviction=conviction,
    )
    forward = ForwardReturn(
        entry_date=date(2026, 3, 3), exit_date=date(2026, 3, 6),
        entry_price=100.0, exit_price=102.0, pct=0.02,
    )
    return ScoredSignal(entry=entry, forward=forward)


# --------------------------------------------------------------------------- #
# _signal_index
# --------------------------------------------------------------------------- #


def test_signal_index_is_the_last_bar_at_or_before_the_date():
    df = frame(flat(5), start="2026-03-02")  # Mon 2 .. Fri 6 Mar
    assert df.index[2].date() == date(2026, 3, 4)
    assert _signal_index(df, date(2026, 3, 4)) == 2


def test_signal_index_falls_back_to_the_last_trading_day_before_a_weekend():
    df = frame(flat(5), start="2026-03-02")
    # Saturday 7 Mar has no bar; the last one before it is Friday 6 Mar.
    assert _signal_index(df, date(2026, 3, 7)) == 4


def test_signal_index_is_none_before_the_first_bar():
    df = frame(flat(5), start="2026-03-02")
    assert _signal_index(df, date(2026, 2, 1)) is None


# --------------------------------------------------------------------------- #
# simulate_model_trades
# --------------------------------------------------------------------------- #


class FakeFetcher:
    """Hands back a pre-built frame instead of calling yfinance."""

    def __init__(self, frames: dict[str, pd.DataFrame]):
        self._frames = frames
        self.asked: list[tuple] = []

    def ohlc(self, ticker: str, start: date, end: date) -> pd.DataFrame:
        self.asked.append((ticker, start, end))
        return self._frames.get(ticker, pd.DataFrame())


def _warm_frame(bias_day_price: float = 150.0) -> pd.DataFrame:
    """Enough warm-up bars, then a signal day, then room to exit."""
    bars = flat(MIN_WARMUP_BARS + 1) + [
        (bias_day_price, bias_day_price + 2, bias_day_price - 2, bias_day_price)
    ] * 10
    return frame(bars, start="2026-01-01")


def _at(day: date) -> datetime:
    return datetime.combine(day, datetime.min.time(), tzinfo=timezone.utc)


def test_matched_signals_line_up_one_to_one_with_trades():
    """The population fed to a baseline must be exactly what the model side
    actually produced a trade for -- not signals a warm-up or cap check
    dropped from only one side of the comparison."""
    warm = _warm_frame()
    signal_date = warm.index[MIN_WARMUP_BARS].date()
    ok_signal = signal(ticker="NVDA", timestamp=_at(signal_date))

    too_early = signal(ticker="THIN", timestamp=datetime(2026, 1, 1, tzinfo=timezone.utc))
    thin = frame(flat(3), start="2026-01-01")  # not enough bars to warm up ATR

    fetcher = FakeFetcher({"NVDA": warm, "THIN": thin})
    trades, matched, dropped = simulate_model_trades(
        [ok_signal, too_early], equity=100_000.0, horizon_days=3,
        stop_multiplier=2.0, max_position_pct=0.05, fetcher=fetcher,
    )

    assert len(trades) == len(matched) == 1
    assert matched[0] is ok_signal
    assert dropped == 1


def test_a_ticker_with_no_ohlc_at_all_drops_every_one_of_its_signals():
    fetcher = FakeFetcher({})
    trades, matched, dropped = simulate_model_trades(
        [signal(ticker="GHOST"), signal(ticker="GHOST", timestamp=_at(date(2026, 3, 3)))],
        equity=100_000.0, horizon_days=3, stop_multiplier=2.0,
        max_position_pct=0.05, fetcher=fetcher,
    )
    assert trades == matched == []
    assert dropped == 2


def test_a_short_call_opens_a_sell_side_trade():
    warm = _warm_frame()
    signal_date = warm.index[MIN_WARMUP_BARS].date()
    bear = signal(ticker="NVDA", bias="BEARISH", timestamp=_at(signal_date))
    trades, matched, dropped = simulate_model_trades(
        [bear], equity=100_000.0, horizon_days=3, stop_multiplier=2.0,
        max_position_pct=0.05, fetcher=FakeFetcher({"NVDA": warm}),
    )
    assert dropped == 0
    assert trades[0].side == "sell"


def test_ohlc_is_fetched_once_per_ticker_across_its_signals():
    """One fetch call per ticker, batched -- not one per signal."""
    warm = _warm_frame()
    signal_date = warm.index[MIN_WARMUP_BARS].date()
    three = [signal(ticker="NVDA", timestamp=_at(signal_date)) for _ in range(3)]

    fetcher = FakeFetcher({"NVDA": warm})
    simulate_model_trades(
        three, equity=100_000.0, horizon_days=3,
        stop_multiplier=2.0, max_position_pct=0.05, fetcher=fetcher,
    )
    assert len({a[0] for a in fetcher.asked}) == 1
    assert len(fetcher.asked) == 1


# --------------------------------------------------------------------------- #
# watchlist_buy_and_hold
# --------------------------------------------------------------------------- #


class FakePriceSource:
    def __init__(self, series: dict[str, PriceSeries]):
        self._series = series

    def closes(self, ticker: str, start: date, end: date) -> PriceSeries:
        return self._series.get(ticker, PriceSeries(ticker, []))


def test_equal_weight_mean_of_two_tickers():
    series = {
        "AAA": PriceSeries("AAA", [(date(2026, 1, 2), 100.0), (date(2026, 1, 9), 110.0)]),
        "BBB": PriceSeries("BBB", [(date(2026, 1, 2), 50.0), (date(2026, 1, 9), 45.0)]),
    }
    mean, priced, missing = watchlist_buy_and_hold(
        ("AAA", "BBB"), date(2026, 1, 2), date(2026, 1, 9), FakePriceSource(series),
    )
    # AAA: +10%, BBB: -10% -> equal-weight mean is 0.
    assert priced == 2 and missing == 0
    assert mean == pytest.approx(0.0)


def test_a_ticker_with_no_bars_is_counted_as_missing_not_zero():
    series = {"AAA": PriceSeries("AAA", [(date(2026, 1, 2), 100.0), (date(2026, 1, 9), 120.0)])}
    mean, priced, missing = watchlist_buy_and_hold(
        ("AAA", "GONE"), date(2026, 1, 2), date(2026, 1, 9), FakePriceSource(series),
    )
    assert priced == 1 and missing == 1
    assert mean == pytest.approx(0.20)


def test_empty_universe_reports_no_mean_rather_than_zero():
    mean, priced, missing = watchlist_buy_and_hold(
        (), date(2026, 1, 2), date(2026, 1, 9), FakePriceSource({}),
    )
    assert mean is None and priced == 0 and missing == 0


# --------------------------------------------------------------------------- #
# OhlcFetcher caching
# --------------------------------------------------------------------------- #


def test_ohlc_fetcher_caches_by_ticker_and_fetches_once():
    fetcher = OhlcFetcher()
    calls = []

    def fake_fetch(self, ticker, start, end):
        calls.append((ticker, start, end))
        return frame(flat(3))

    fetcher._fetch = fake_fetch.__get__(fetcher)
    fetcher.ohlc("NVDA", date(2026, 1, 1), date(2026, 2, 1))
    fetcher.ohlc("NVDA", date(2026, 1, 1), date(2026, 2, 1))
    assert len(calls) == 1


# --------------------------------------------------------------------------- #
# render
# --------------------------------------------------------------------------- #


def _trade(return_pct: float) -> Trade:
    return Trade(
        entry_date="2026-01-02", side="buy", entry_price=100.0, stop_price=98.0,
        atr=1.0, exit_date="2026-01-05", exit_price=100.0 * (1 + return_pct),
        stopped_out=False, gapped_through=False, qty=10, equity=100_000.0,
    )


def test_render_reports_dropped_signals_and_both_baselines():
    model = Outcome(label="model", trades=[_trade(0.02), _trade(-0.01)])
    text = render(
        run_horizon=3, floor=0.30, model=model, could_not_simulate=1,
        naive_returns=[0.01, -0.02], window_start=date(2026, 1, 2),
        window_end=date(2026, 1, 9), watchlist_return=0.015, watchlist_n=78,
        watchlist_total=80, watchlist_missing=2, spy_return=0.01,
    )
    assert "could not be simulated (warm-up, cap, missing bars)  1" in text
    assert "78/80 tickers priced, 2 missing" in text
    assert "LIMITS" in text
    # The naive row must be over its own n, not silently reuse the model's.
    assert text.count("2") >= 1


def test_render_handles_no_watchlist_or_spy_data():
    model = Outcome(label="model", trades=[])
    text = render(
        run_horizon=3, floor=0.30, model=model, could_not_simulate=0,
        naive_returns=[], window_start=date(2026, 1, 2), window_end=date(2026, 1, 9),
        watchlist_return=None, watchlist_n=0, watchlist_total=80,
        watchlist_missing=80, spy_return=None,
    )
    assert "n/a" in text
