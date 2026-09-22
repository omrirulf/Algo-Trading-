"""A race is only a race if every arm ran the same course.

The properties that decide that: held lines are offered to nobody; the
rule arms are recomputed from the technicals on the line, not read from
anywhere else; every arm is scored against prices fetched once, over the
widest window any of them needs; every arm pays the same cost; and a trade
is scored only once its exit bar is a final close, so two runs of the race
at different times of day agree on every resolved trade.
"""

from __future__ import annotations

import json
import statistics
from datetime import date, datetime, timedelta, timezone

import pandas as pd
import pytest

from analysis import horse_race
from analysis.horse_race import (
    MODEL_ARM,
    BothSides,
    ScoredTrade,
    agreement_breakdown,
    bands_for,
    cumulative,
    daily_net,
    direction_agreement,
    entries_for_arm,
    every_nth,
    flip_trades,
    newey_west_t,
    offered,
    on_grid,
    percentile,
    percentile_of,
    prewarm,
)
from analysis.reader import JournalEntry
from analysis.returns import PriceSeries, final_bars
from backtest.simulate import MIN_WARMUP_BARS, Trade
from rules import control, momentum
from tests.test_backtest_simulate import flat, frame
from tests.test_baseline_compare import FakeFetcher, _at, _warm_frame

UPTREND = {"return_63d": 0.10, "distance_sma50": 0.03, "annualised_volatility": 0.20}
STAMP = datetime(2026, 3, 2, 14, tzinfo=timezone.utc)


def line(ticker="NVDA", bias="BULLISH", conviction=0.72, technicals=UPTREND,
         held=False, stamp=STAMP, signal=True) -> JournalEntry:
    return JournalEntry(
        ticker=ticker, timestamp=stamp, timestamp_is_exact=True,
        bias=bias if signal else None, conviction=conviction if signal else None,
        technicals=dict(technicals) if technicals else {}, held=held,
    )


def _trade(return_pct: float, entry="2026-03-03", exit_="2026-03-06", stopped=False,
           side="buy") -> Trade:
    """A trade whose signed return is ``return_pct`` on either side."""
    move = return_pct if side == "buy" else -return_pct
    return Trade(
        entry_date=entry, side=side, entry_price=100.0, stop_price=98.0, atr=1.0,
        exit_date=exit_, exit_price=100.0 * (1 + move), stopped_out=stopped,
        gapped_through=False, qty=10, equity=100_000.0,
    )


def scored(return_pct: float, arm="model", ticker="NVDA", entry="2026-03-03",
           stamp=STAMP, cost=0.001, fund=False, side="buy") -> ScoredTrade:
    return ScoredTrade(
        arm=arm, ticker=ticker, signal_at=stamp, signal_day=stamp.date(),
        entry_day=date.fromisoformat(entry), exit_day=date(2026, 3, 6), fund=fund,
        trade=_trade(return_pct, entry=entry, side=side), cost_per_side=cost,
    )


# --- who gets asked -------------------------------------------------------------


def test_a_held_line_is_offered_to_no_arm():
    lines = offered([line(), line(held=True), line(stamp=None)])
    assert len(lines) == 1
    assert not lines[0].held


def test_the_model_arm_is_the_journal_as_written():
    lines = offered([line(bias="BEARISH"), line(signal=False)])
    model = entries_for_arm(MODEL_ARM, lines)
    assert [e.bias for e in model] == ["BEARISH"]
    assert model[0] is lines[0]


def test_the_momentum_arm_is_recomputed_from_the_lines_own_technicals():
    lines = offered([line(bias="BEARISH"), line(technicals=None, signal=False)])
    arm = entries_for_arm(momentum.NAME, lines)
    assert len(arm) == 2, "the rule answers every offered line, signal or not"
    assert arm[0].bias == "BULLISH" and arm[0].conviction == pytest.approx(0.5)
    assert arm[1].bias == "NEUTRAL" and arm[1].conviction == 0.0
    assert arm[0].ticker == lines[0].ticker and arm[0].timestamp == lines[0].timestamp


def test_the_control_arm_takes_a_side_on_every_offered_line():
    lines = offered([line(signal=False, technicals=None) for _ in range(5)])
    arm = entries_for_arm(control.NAME, lines)
    assert len(arm) == 5
    assert all(e.is_directional for e in arm)
    assert all(e.conviction == control.CONVICTION for e in arm)


# --- agreement --------------------------------------------------------------------


def test_direction_agreement_counts_only_lines_where_both_took_a_side():
    a = [line(ticker="A", bias="BULLISH"), line(ticker="B", bias="BEARISH"), line(ticker="C", bias="NEUTRAL")]
    b = [line(ticker="A", bias="BULLISH"), line(ticker="B", bias="BULLISH"), line(ticker="C", bias="BULLISH")]
    rate, n = direction_agreement(a, b)
    assert n == 2 and rate == pytest.approx(0.5)


def test_direction_agreement_with_no_overlap_is_not_zero():
    assert direction_agreement([line(bias="NEUTRAL")], [line(bias="BULLISH")]) == (None, 0)


def test_agreement_breakdown_splits_longs_shorts_and_days():
    day2 = STAMP + timedelta(days=1)
    a = [line(ticker="A", bias="BULLISH"), line(ticker="B", bias="BEARISH"),
         line(ticker="C", bias="BEARISH", stamp=day2), line(ticker="D", bias="BULLISH", stamp=day2)]
    b = [line(ticker="A", bias="BULLISH"), line(ticker="B", bias="BEARISH"),
         line(ticker="C", bias="BEARISH", stamp=day2), line(ticker="D", bias="BEARISH", stamp=day2)]
    days = agreement_breakdown(a, b)
    assert [(d.day, d.both, d.agreed_long, d.agreed_short, d.disagreed) for d in days] == [
        (STAMP.date(), 2, 1, 1, 0), (day2.date(), 2, 0, 1, 1),
    ]


def test_the_verdict_calls_one_sided_agreement_automatic():
    assert "automatic" in horse_race._agreement_verdict(longs=19, shorts=1, disagreed=0)
    assert "automatic" not in horse_race._agreement_verdict(longs=12, shorts=8, disagreed=0)
    assert "disagreement" in horse_race._agreement_verdict(longs=5, shorts=5, disagreed=3)


# --- one fetch per ticker, widest window ----------------------------------------


class RecordingSource:
    def __init__(self):
        self.asked: list[tuple] = []

    def closes(self, ticker, start, end):
        self.asked.append((ticker, start, end))
        return PriceSeries(ticker, [])


def test_prewarm_asks_each_source_once_per_ticker_over_the_widest_window():
    early, late = date(2026, 3, 2), date(2026, 3, 9)
    lines = offered([
        line(stamp=_at(late)), line(stamp=_at(early)),          # NVDA, out of order
        line(ticker="XLE", stamp=_at(late)),
    ])
    source, fetcher = RecordingSource(), FakeFetcher({})
    prewarm(lines, source, fetcher, horizon=3, today=date(2026, 3, 20))

    assert [a[0] for a in source.asked] == ["NVDA", "XLE"]
    nvda_close, nvda_ohlc = source.asked[0], fetcher.asked[0]
    assert nvda_close[1] == early and nvda_close[2] == date(2026, 3, 20)
    assert nvda_ohlc[1] == early and nvda_ohlc[2] == late + timedelta(days=3 * 2 + 10)


# --- the arithmetic: costs, hits, days -------------------------------------------


def test_net_return_charges_the_round_trip_and_a_hit_is_net_above_zero():
    t = scored(0.0015, cost=0.001)
    assert t.gross == pytest.approx(0.0015)
    assert t.net == pytest.approx(-0.0005)
    assert not t.hit, "a gross gain smaller than the round trip is not a hit"
    assert scored(0.0025, cost=0.001).hit
    assert not scored(0.0, cost=0.0).hit, "exactly zero net is not a hit"


def test_daily_net_equal_weights_the_trades_opened_on_one_day():
    trades = [scored(0.02, entry="2026-03-03"), scored(-0.04, entry="2026-03-03"),
              scored(0.01, entry="2026-03-04")]
    daily = daily_net(trades)
    assert daily[date(2026, 3, 3)] == pytest.approx(statistics.fmean([0.02 - 0.002, -0.04 - 0.002]))
    assert daily[date(2026, 3, 4)] == pytest.approx(0.008)


def test_a_day_with_no_trade_is_zero_on_the_grid_not_missing():
    grid = [date(2026, 3, 3), date(2026, 3, 4), date(2026, 3, 5)]
    assert on_grid({date(2026, 3, 4): 0.01}, grid) == [0.0, 0.01, 0.0]


def test_cumulative_compounds_the_days():
    assert cumulative([0.10, -0.10]) == pytest.approx(-0.01)
    assert cumulative([]) is None


def test_every_nth_day_starts_from_the_first_and_cannot_overlap():
    grid = [date(2026, 3, d) for d in (2, 3, 4, 5, 6, 9, 10)]
    assert every_nth(grid, 3) == [date(2026, 3, 2), date(2026, 3, 5), date(2026, 3, 10)]


def test_newey_west_at_lag_zero_is_the_plain_t_and_widens_with_autocorrelation():
    xs = [0.01, 0.02, 0.015, 0.012, 0.018, 0.011, 0.02, 0.016]
    plain = newey_west_t(xs, 0)
    mean = statistics.fmean(xs)
    var = sum((x - mean) ** 2 for x in xs) / len(xs)
    assert plain == pytest.approx(mean / (var / len(xs)) ** 0.5)
    # A smooth, positively autocorrelated series has a larger true standard
    # error, so the lagged t must be smaller than the plain one.
    smooth = [0.01, 0.011, 0.012, 0.013, 0.014, 0.015, 0.016, 0.017]
    assert newey_west_t(smooth, 3) < newey_west_t(smooth, 0)


def test_newey_west_refuses_what_it_cannot_compute():
    assert newey_west_t([0.01], 3) is None
    assert newey_west_t([0.01, 0.01, 0.01], 1) is None, "a constant series has no standard error"


def test_percentiles_and_positions():
    sample = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert percentile(sample, 0) == 1.0 and percentile(sample, 100) == 5.0
    assert percentile(sample, 50) == 3.0
    assert percentile(sample, 25) == 2.0
    assert percentile_of(4.5, sample) == pytest.approx(80.0)
    assert percentile_of(3.0, sample) == pytest.approx(50.0), "ties split"
    assert percentile_of(None, sample) is None and percentile([], 50) is None


# --- the coin flip, many times over ---------------------------------------------


def _sides(keys, up=0.02, down=-0.02) -> dict:
    return {
        key: BothSides(
            buy=scored(up, arm=control.NAME, ticker=key[0], stamp=key[1]),
            sell=scored(down, arm=control.NAME, ticker=key[0], stamp=key[1], side="sell"),
        )
        for key in keys
    }


def test_seed_zero_is_the_journalled_flip_and_other_seeds_differ():
    keys = [(f"T{i}", STAMP) for i in range(40)]
    sides = _sides(keys)
    journalled = [control.signal_for(t, STAMP.date()).bias.value for t, _ in keys]
    drawn = flip_trades(keys, sides, seed=0)
    assert [t.trade.side for t in drawn] == ["buy" if b == "BULLISH" else "sell" for b in journalled]
    assert [t.trade.side for t in flip_trades(keys, sides, seed=7)] != [t.trade.side for t in drawn]


def test_bands_bracket_chance_and_place_the_arm_inside_them():
    keys = [(f"T{i}", STAMP) for i in range(60)]
    sides = _sides(keys, up=0.02, down=-0.02)
    # An arm that was right on every one of these lines.
    arm = [sides[k].buy for k in keys]
    bands = bands_for(arm, sides, grid=[date(2026, 3, 3)], seeds=200)
    by = {b.metric: b for b in bands}
    assert by["hit rate"].low is not None and by["hit rate"].low < 0.5 < by["hit rate"].high
    assert by["hit rate"].value == 1.0 and by["hit rate"].percentile == pytest.approx(100.0)
    assert by["mean net"].percentile == pytest.approx(100.0)
    assert by["mean/day"].seeds == 200


def test_a_coin_flip_arm_sits_in_the_middle_of_its_own_band():
    keys = [(f"T{i}", STAMP) for i in range(80)]
    sides = _sides(keys)
    arm = flip_trades(keys, sides, seed=0)
    by = {b.metric: b for b in bands_for(arm, sides, grid=[date(2026, 3, 3)], seeds=300)}
    assert 5.0 < by["mean net"].percentile < 95.0


# --- end to end, no network -----------------------------------------------------------


class FinalAwareSource:
    """Closes from OHLC frames, honouring the finality cutoff like the real one."""

    def __init__(self, frames: dict[str, pd.DataFrame], final_through=None):
        self._frames, self.final_through = frames, final_through

    def closes(self, ticker, start, end):
        df = self._frames.get(ticker)
        if df is None:
            return PriceSeries(ticker, [])
        bars = [(ts.date(), float(c)) for ts, c in df["Close"].items()]
        return PriceSeries(ticker, final_bars(bars, self.final_through))


class FinalAwareFetcher:
    def __init__(self, frames: dict[str, pd.DataFrame], final_through=None):
        self._frames, self.final_through = frames, final_through

    def ohlc(self, ticker, start, end):
        df = self._frames.get(ticker, pd.DataFrame())
        if self.final_through is None or df.empty:
            return df
        return df[[ts.date() <= self.final_through for ts in df.index]]


def _race(tmp_path, monkeypatch, capsys, frames, journal_lines, now, extra=()):
    journal = tmp_path / "signal_journal.log"
    journal.write_text("\n".join(json.dumps(l) for l in journal_lines) + "\n", encoding="utf-8")
    monkeypatch.setattr(horse_race, "_now", lambda: now)
    monkeypatch.setattr(horse_race, "YFinancePriceSource",
                        lambda final_through=None: FinalAwareSource(frames, final_through))
    monkeypatch.setattr(horse_race, "OhlcFetcher",
                        lambda final_through=None: FinalAwareFetcher(frames, final_through))
    code = horse_race.main(["--journal", str(journal), "--seeds", "20", "--per-trade", *extra])
    return code, capsys.readouterr().out


def _journal_line(ticker, stamp, bias="BULLISH"):
    return {"ts_utc": stamp.isoformat(), "ticker": ticker, "context": {"technicals": UPTREND},
            "signal": {"bias": bias, "conviction": 0.72}}


def test_main_races_all_three_arms_on_a_tiny_journal(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    signal_day = warm.index[MIN_WARMUP_BARS].date()
    stamp = _at(signal_day)
    lines = [
        _journal_line("NVDA", stamp),
        {"ts_utc": stamp.isoformat(), "ticker": "NVDA", "context": {"technicals": UPTREND}, "held": True},
    ]
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, lines, now)
    assert code == 0
    assert "THREE ARMS" in out
    for name in ("model", momentum.NAME, control.NAME):
        assert name in out
    # The definitions and the date range are in the header, every run.
    assert "hit          a trade whose net return is strictly greater than zero" in out
    assert "round trip" in out and "final closes through" in out
    assert "== FUNDS" in out and "== COMPANIES" in out and "== ALL NAMES" in out
    assert "Paired difference, model minus momentum" in out
    assert "Every resolved line is scored or named as" in out and "yes" in out


def _two_signal_frame():
    """Warm-up, then a signal bar, an entry/exit bar, a second signal bar's
    exit... laid out so that with horizon 1 the first trade exits on bar
    S+1 and the second on bar S+2, which is 'today'."""
    bars = flat(MIN_WARMUP_BARS + 1) + [
        (100.0, 102.0, 99.0, 101.0),   # S1: first signal bar
        (101.0, 104.0, 100.0, 103.0),  # S1+1: entry of trade 1, exit of trade 1; second signal bar S2
        (103.0, 105.0, 102.0, 104.0),  # S2+1: exit of trade 2 -- 'today'
    ]
    return frame(bars, start="2026-03-02")


def _two_signal_lines(df):
    s1 = df.index[MIN_WARMUP_BARS + 1].date()
    s2 = df.index[MIN_WARMUP_BARS + 2].date()
    return [_journal_line("NVDA", _at(s1) + timedelta(hours=15)),
            _journal_line("NVDA", _at(s2) + timedelta(hours=15))]


def _trade_rows(out: str) -> dict[tuple[str, str], str]:
    rows = {}
    for row in out.splitlines():
        parts = row.split()
        if parts and parts[0] in ("model", momentum.NAME, control.NAME) and len(parts) == 10 \
                and parts[2].count("-") == 2:
            rows[(parts[0], parts[2])] = row
    return rows


def test_two_runs_at_different_times_agree_on_every_resolved_trade(tmp_path, monkeypatch, capsys):
    """Run before today's close: today's bar is not final, so the trade that
    exits on it is pending. Run after the close: it resolves. The trade that
    was already resolved in the morning must read identically in the evening."""
    df = _two_signal_frame()
    today = df.index[-1].date()
    lines = _two_signal_lines(df)
    morning = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc) + timedelta(hours=18)
    evening = morning + timedelta(hours=4)

    _, before = _race(tmp_path, monkeypatch, capsys, {"NVDA": df}, lines, morning, ("--horizon", "1"))
    _, after = _race(tmp_path, monkeypatch, capsys, {"NVDA": df}, lines, evening, ("--horizon", "1"))

    rows_before, rows_after = _trade_rows(before), _trade_rows(after)
    assert rows_before, "the morning run resolved the first trade"
    assert len(rows_after) > len(rows_before), "the evening run resolved today's trade too"
    for key, row in rows_before.items():
        assert rows_after[key] == row, f"a resolved trade changed between runs: {key}"


def test_an_intraday_price_never_reaches_a_score(tmp_path, monkeypatch, capsys):
    """Before the close, today's bar is whatever the vendor is showing right
    now. Change it wildly; the morning run must not notice."""
    df = _two_signal_frame()
    today = df.index[-1].date()
    lines = _two_signal_lines(df)
    morning = datetime.combine(today, datetime.min.time(), tzinfo=timezone.utc) + timedelta(hours=18)

    _, quiet = _race(tmp_path, monkeypatch, capsys, {"NVDA": df}, lines, morning, ("--horizon", "1"))
    wild = df.copy()
    wild.iloc[-1] = [103.0, 150.0, 50.0, 60.0]
    _, crashed = _race(tmp_path, monkeypatch, capsys, {"NVDA": wild}, lines, morning, ("--horizon", "1"))

    assert _trade_rows(quiet) == _trade_rows(crashed)
    assert quiet == crashed


def test_every_arm_pays_the_same_cost_and_the_header_says_so(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    _, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, [_journal_line("NVDA", stamp)], now,
                   ("--cost-per-side", "0.005"))
    assert "cost 0.50% per side (1.00% round trip) on every trade of every arm" in out
    rows = _trade_rows(out)
    # Flat bars: every arm's gross is 0, so every arm's net is exactly -1.00%.
    for row in rows.values():
        assert "-1.00%" in row
