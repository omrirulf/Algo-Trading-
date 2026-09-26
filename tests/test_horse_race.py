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
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone

import pandas as pd
import pytest

from analysis import decision_gate, horse_race
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
from rules import control, hybrid, momentum
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
           stamp=STAMP, cost=0.001, fund=False, side="buy", conviction=None) -> ScoredTrade:
    return ScoredTrade(
        arm=arm, ticker=ticker, signal_at=stamp, signal_day=stamp.date(),
        entry_day=date.fromisoformat(entry), exit_day=date(2026, 3, 6), fund=fund,
        trade=_trade(return_pct, entry=entry, side=side), cost_per_side=cost, conviction=conviction,
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


def _race(tmp_path, monkeypatch, capsys, frames, journal_lines, now, extra=(),
          cutoff=date(2000, 1, 1), account=None):
    """Run the race on a tiny journal. These journals are dated early 2026,
    before the real cutoff, so by default the cutoff is moved back to take
    them in; a test about the cutoff itself passes ``cutoff=None``.

    ``account`` is the paper account's record for trigger (d): lines to
    write, or raw text; by default there is none, so no test here reads the
    repository's own ``logs/account.jsonl``."""
    journal = tmp_path / "signal_journal.log"
    journal.write_text("\n".join(json.dumps(l) for l in journal_lines) + "\n", encoding="utf-8")
    record = tmp_path / "account.jsonl"
    if account is None:
        record.unlink(missing_ok=True)
    else:
        record.write_text(account if isinstance(account, str)
                          else "\n".join(json.dumps(l) for l in account) + "\n", encoding="utf-8")
    extra = ("--account", str(record), *extra)
    if cutoff is not None:
        monkeypatch.setattr(decision_gate, "DECISION_CUTOFF", cutoff)
        monkeypatch.setattr(decision_gate, "FAILURE_WATCH_START", cutoff)
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


# --- the hybrid and the exploratory arm ---------------------------------------------


def test_seen_on_hands_each_arm_exactly_what_the_line_carried():
    entry = replace(line(), scores={"news_score": -0.4},
                    insiders={"buys": [{"when": "2026-02-20", "who": "Ann", "role": "Director",
                                        "shares": 10.0, "value": None}], "sells": []})
    seen = horse_race.seen_on(entry)
    assert seen.ticker == "NVDA" and seen.day == STAMP.date()
    assert seen.technicals.return_63d == 0.10
    assert seen.insiders.buys[0].who == "Ann"
    assert seen.news_score == -0.4
    bare = horse_race.seen_on(line(technicals=None))
    assert bare.technicals is None and bare.insiders is None and bare.news_score is None


def test_the_hybrid_arm_is_momentum_vetoed_by_the_lines_own_news_score():
    agree = replace(line(), scores={"news_score": 0.6})
    veto = replace(line(), scores={"news_score": -0.6})
    arm = entries_for_arm(hybrid.NAME, [agree, veto])
    assert arm[0].bias == "BULLISH" and arm[0].conviction == pytest.approx(0.55)
    assert arm[1].bias == "NEUTRAL"


def _insider_journal_line(ticker, stamp, buyers):
    buys = [{"when": (stamp - timedelta(days=10)).date().isoformat(), "who": who, "role": "Director",
             "shares": 100.0, "value": None} for who in buyers]
    return {"ts_utc": stamp.isoformat(), "ticker": ticker,
            "context": {"technicals": UPTREND, "insiders": {"buys": buys, "sells": []}},
            "signal": {"bias": "BEARISH", "conviction": 0.72, "news_score": 0.1}}


def test_the_exploratory_arm_is_raced_on_its_own_lines_only_and_paired(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    signal_day = warm.index[MIN_WARMUP_BARS].date()
    stamp = _at(signal_day) + timedelta(hours=15)
    lines = [
        _insider_journal_line("CAT", stamp, ["Ann", "Bob"]),      # the arm takes a side here
        _insider_journal_line("LLY", stamp, ["Ann"]),             # and not here
        _journal_line("NVDA", stamp),                             # no insider section at all
    ]
    frames = {t: warm for t in ("CAT", "LLY", "NVDA")}
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, frames, lines, now)
    assert code == 0
    assert "== EXPLORATORY: insiders" in out
    assert "took a side on 1" in out
    assert "cannot change the main decision" in out
    section = out[out.index("== EXPLORATORY"):out.index("AGREEMENT")]
    # Both horizons are printed, each paired with the model and the rule.
    assert "horizon 3 session(s)" in section and f"horizon {horse_race.EXPLORATORY_HORIZON} session(s)" in section
    assert "<- too few" in section
    rows = [l for l in section.splitlines() if l.startswith(("insiders", "model", "momentum"))]
    assert len(rows) == 6
    # On the one line it took a side on, the arm has one trade at horizon 3
    # and the model (BEARISH there, above the floor) has one too: paired.
    assert rows[0].split()[1] == "1" and rows[1].split()[1] == "1"
    # The main tables carry the hybrid as a main arm, not the insider arm.
    main = out[:out.index("== EXPLORATORY")]
    assert hybrid.NAME in main and "insiders" not in main
    assert "Paired difference, model minus hybrid" in main


# --- the pre-registration and the code say the same numbers -----------------------


def test_the_registered_parameters_are_the_ones_the_code_runs():
    """docs/horse-race-preregistration.md is locked; if a constant here has
    to change, the file needs a dated amendment first, not the other way
    round. This is the mirror that keeps the two from drifting."""
    from pathlib import Path

    from config import settings as cfg
    from rules import insider_buying, momentum

    raw = (Path(__file__).resolve().parents[1] / "docs/horse-race-preregistration.md").read_text()
    text = " ".join(raw.split())  # the file wraps lines; the phrases must not care
    assert "IN FORCE" in text
    assert horse_race.DEFAULT_COST_PER_SIDE == 0.001 and "0.10% per side" in text
    assert horse_race.DEFAULT_HORIZON == 3 and "3 sessions for every arm" in text
    assert horse_race.DEFAULT_SEEDS == 1000 and "1000 seeds" in text
    assert horse_race.EXPLORATORY_HORIZON == 20 and "20 sessions" in text
    assert (horse_race.EXPLORATORY_MIN_TRADES, horse_race.EXPLORATORY_MIN_DAYS) == (20, 20)
    assert "20 scored trades on at least 20 distinct entry days" in text
    assert "60 non-overlapping entry days" in text
    assert cfg.MIN_CONVICTION == 0.30 and "0.30" in text
    assert momentum.LOOKBACK_BARS == 63 and momentum.CONFIRMATION_SMA == 50
    assert insider_buying.WINDOW_DAYS == 180 and insider_buying.MIN_DISTINCT_BUYERS == 2
    assert "180 calendar days" in text and "two or more distinct insiders" in text
    assert [pair[1] for pair in horse_race.PAIRED] == ["momentum", "hybrid"]

    # The model arm is whoever production answers with, so the file has to
    # name the model the code actually runs. Amendment 1 exists because that
    # changed; a silent change is the failure this line catches.
    from orchestrator import llm

    assert llm.MODEL in text, (
        f"the pre-registration does not name {llm.MODEL}; the model arm changed "
        "without an amendment"
    )

    # The model arm's settings. Screening on, or a different reasoning
    # level, is a different contestant: the file has to say so first.
    registered_screening = "Screening (`SCREENING_ENABLED`): **off**" in text
    assert registered_screening or "Screening (`SCREENING_ENABLED`): **on**" in text
    assert llm.SCREENING_ENABLED is (not registered_screening), (
        "SCREENING_ENABLED is on but the pre-registration says off; amend the file first"
    )
    assert llm.MODEL_EFFORT == "high" and "reasoning level **high**" in text, (
        f"MODEL_EFFORT is {llm.MODEL_EFFORT!r}; the pre-registration registers 'high'"
    )
    assert llm.configured_effort() == "high"

    # The gate: applied by code, and the code's numbers are the file's.
    from datetime import date

    from analysis import decision_gate as gate

    assert gate.DECISION_CUTOFF == date(2026, 9, 23)
    assert "lines journalled on or after **2026-09-23**" in text
    assert gate.MIN_INDEPENDENT_DAYS == 60 and gate.REGISTERED_HORIZON == horse_race.DEFAULT_HORIZON
    assert "independent days since 2026-09-23: X of 60 (= 180 trading days) — NO DECISION YET" in text
    assert gate.CHECKPOINTS == ((20, 3.47), (40, 2.45), (60, 2.00))
    assert "**20, 40 and 60 independent days**" in text and "**t > 3.47, 2.45, 2.00**" in text
    for independent, bar in gate.CHECKPOINTS:
        assert f"| {independent} | {independent * 3} | {bar:.2f} |" in text
    assert gate.CHECKPOINTS[-1][1] == 2.0 and "t above 2.0" in text
    assert gate.INDEX_TICKER == "VT" and "**VT**" in text
    assert gate.INDEX_GAP_SETTLE_SESSIONS == 5 and "published five later VT sessions" in text
    assert gate.FAILURE_WATCH_START == date(2026, 9, 25) and "counted from **2026-09-25**" in text
    assert gate.RUN_ALERT_FAILED_SHARE == 0.20 and "more than **20%** of one run's calls fail" in text
    # Trigger (a): closed on the owner's decision of 25 Sep, with the replay's own counts.
    assert gate.TRIGGER_A_CLOSED == date(2026, 9, 25) and "**Closed on 2026-09-25**" in text
    assert gate.TRIGGER_A_RESULT == (1, 31)
    assert "gpt-oss shorted 1 of the 31 lines where Opus shorted" in text
    # Trigger (b): retired on the owner's decision of 26 Sep; (d) replaces it, with the file's numbers.
    assert gate.TRIGGER_B_RETIRED == date(2026, 9, 26) and "**Retired on 2026-09-26**" in text
    assert gate.DRAWDOWN_START == date(2026, 9, 23) and gate.MAX_DRAWDOWN == 0.08
    assert "more than **8%** below its highest close since **2026-09-23**" in text
    assert gate.MAX_BEHIND_VT == 0.05 and "more than **5 percentage points** behind VT's" in text
    assert "| 2026-09-26 | **Trigger (b) retired, drawdown trigger (d) added**" in text
    assert "equity < peak × (1 − 0.08)" in text and "account return − VT return < −0.05" in text
    # The two exploratory reports (reporting only): the owner's groups and "too few" line.
    assert horse_race.MIN_REPORT_TRADES == 20
    assert '"too few" until a group or side has 20 trades' in text
    assert [g[0] for g in horse_race.CONVICTION_GROUPS] == ["0.30-0.40", "0.40-0.50", "0.50-0.60", "0.60+"]
    assert "(0.30-0.40, 0.40-0.50, 0.50-0.60, 0.60 and above;" in text
    assert gate.COIN_FLIP_PERCENTILE == 95.0 and "95th percentile" in text
    assert horse_race.BAND == (5.0, 95.0)  # the band condition 3 actually reads
    assert "**no arm trades**" in text
    assert "**none before the June 2027 verdict.**" in text
    # No early stop may be contradicted by the file's own text.
    assert "A partial window, except a planned look" in text
    assert "except bug fixes and the owner's new registrations" in text


# --- the decision gate, applied by the race itself ---------------------------------------


def test_lines_before_the_cutoff_never_reach_the_decision(tmp_path, monkeypatch, capsys):
    """The race applies the cutoff itself. A journal that is all before it
    has nothing to decide on, says so in the header, and prints the whole
    journal only after the gate, marked for reading."""
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, [_journal_line("NVDA", stamp)],
                      now, extra=("--seeds", "1000"), cutoff=None)
    assert code == 0
    assert ("independent days since 2026-09-23: 0 of 60 (= 180 trading days) — NO DECISION YET"
            in out)
    assert "Next checkpoint: 20 independent days (= 60 trading days), estimated" in out
    assert "bar t > 3.47" in out
    assert "No trade in the decision window has resolved yet" in out
    assert out.index("DECISION GATE") < out.index("WHOLE JOURNAL, FOR READING ONLY")
    assert "== WHOLE JOURNAL, ALL NAMES" in out
    assert "SENSITIVITY RUN" not in out


def test_a_sensitivity_run_says_it_cannot_decide(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, [_journal_line("NVDA", stamp)],
                      now, extra=("--horizon", "5"))
    assert code == 0
    assert "SENSITIVITY RUN" in out and "horizon 5 (registered 3)" in out


def test_a_line_the_model_did_not_answer_is_offered_to_no_arm(tmp_path, monkeypatch, capsys):
    """The bug fix of 24 Sep: a timed-out line used to be traded by every
    rule while the model sat it out. Now it leaves every arm alike."""
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    failed = {"ts_utc": (stamp + timedelta(seconds=1)).isoformat(), "ticker": "NVDA",
              "context": {"technicals": UPTREND}, "error": "timed out"}
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm},
                      [_journal_line("NVDA", stamp), failed], now)
    assert code == 0
    assert "no model answer, offered to no arm 1" in out
    rows = {l.split()[0]: l.split() for l in out.splitlines()
            if l.split() and l.split()[0] in ("model", "momentum", "hybrid", "random")
            and len(l.split()) == 9 and l.split()[1].isdigit()}
    assert {name: row[1] for name, row in rows.items()} == {
        "model": "1", "momentum": "1", "hybrid": "1", "random": "1"}


def test_split_answered_keeps_screened_lines():
    screened = line(bias="NEUTRAL", conviction=0.0)
    failed = line(signal=False)
    answered, dropped = horse_race.split_answered([screened, failed])
    assert answered == [screened] and dropped == [failed]


def test_the_race_warns_about_lines_made_under_other_settings(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    lines = [
        dict(_journal_line("NVDA", stamp), screening=True, reasoning_effort="high",
             usage={"model": "openai/gpt-oss-120b", "cost_usd": 0.004}),
        dict(_journal_line("LLY", stamp), screening=False, reasoning_effort="low",
             usage={"model": "claude-opus-5", "cost_usd": 0.041},
             screen={"model": "h", "usage": {"cost_usd": 0.007}}),
    ]
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm, "LLY": warm}, lines, now)
    assert code == 0
    assert "WARNING: 1 line(s) in the decision window were made with the screen ON" in out
    assert "reasoning low, not the registered high" in out
    assert "came from claude-opus-5, not the registered openai/gpt-oss-120b" in out
    assert "LLM SPEND over the decision window: $0.05 (model $0.04, screen $0.01)" in out


def test_vt_is_printed_beside_spy_and_the_watchlist(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm, "VT": warm, "SPY": warm},
                      [_journal_line("NVDA", stamp)], now)
    assert code == 0
    vt_rows = [l for l in out.splitlines() if l.startswith("VT ")]
    assert vt_rows and all("world index fund, bought and held" in l for l in vt_rows)


def test_the_model_watch_is_printed_every_run(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    _, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, [_journal_line("NVDA", stamp)], now)
    assert "MODEL WATCH" in out
    # Trigger (b) is retired (the owner's decision of 26 Sep 2026): recorded, never evaluated.
    assert ("(b) retired 2026-09-26 (owner's decision: the model is long-only, so (b) would only say "
            "SPY fell); replaced by (d)") in out
    assert "no SHORT" not in out
    assert ("(d) the paper account: more than 8% below its peak since 2026-09-23, or more than 5 points "
            "behind VT: not judged: no account record") in out
    assert "(c) model errors above 5% of the calls that reached the model over 5 cycle days" in out
    assert "not yet judged (1 of 5 cycle day(s)" in out
    assert "setup errors (our key or configuration; shown, never counted by (c)): none" in out
    # Trigger (a) is closed: the watch records how it ended, and no longer
    # points anyone at the replay to judge it again.
    start = out.index("MODEL WATCH")
    watch = out[start:out.index("decision window:", start)]
    assert ("(a) closed 2026-09-25: the zero-shorts replay tripped it (gpt-oss shorted 1 of the 31 "
            "lines Opus shorted); the owner kept gpt-oss: the model arm is effectively long-only.") in watch
    assert "is read from the zero-shorts replay" not in out


def test_a_news_outage_is_not_a_failed_model_call_and_a_wrong_ticker_answer_is_no_answer():
    from analysis.reader import entry_from

    stamp = "2026-09-25T15:00:00+00:00"
    context_failure = entry_from({"ts_utc": stamp, "ticker": "NVDA", "error": "Bright Data unreachable",
                                  "stage": "context"})
    timeout = entry_from({"ts_utc": stamp, "ticker": "LLY", "error": "read timed out"})
    wrong = entry_from({"ts_utc": stamp, "ticker": "MSFT", "error": "answered for NVDA",
                        "signal": {"bias": "BEARISH", "conviction": 0.8}})
    fine = entry_from({"ts_utc": stamp, "ticker": "JPM", "signal": {"bias": "BEARISH", "conviction": 0.8}})
    unauthorised = entry_from({"ts_utc": stamp, "ticker": "XOM", "error": (
        'https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: {"error":{"message":'
        '"User is not authorized"}}')})
    (day,) = horse_race.watch_days([context_failure, timeout, wrong, fine, unauthorised])
    assert (day.asked, day.failed, day.shorts, day.setup_failed) == (4, 2, 1, 1)
    assert (day.attempted, day.answered) == (3, 1)
    answered, dropped = horse_race.split_answered([context_failure, timeout, wrong, fine])
    assert answered == [fine] and len(dropped) == 3


def test_the_spend_counts_a_screened_lines_call_once():
    from analysis.reader import entry_from

    screened_usage = {"model": "claude-haiku-4-5", "cost_usd": 0.007}
    screened = entry_from({"ts_utc": "2026-09-16T15:00:00+00:00", "ticker": "A",
                           "signal": {"bias": "NEUTRAL", "conviction": 0.1}, "usage": screened_usage,
                           "screen": {"model": "claude-haiku-4-5", "bias": "NEUTRAL", "usage": screened_usage}})
    escalated = entry_from({"ts_utc": "2026-09-16T15:00:00+00:00", "ticker": "B",
                            "signal": {"bias": "BULLISH", "conviction": 0.6},
                            "usage": {"model": "claude-opus-5", "cost_usd": 0.041},
                            "screen": {"model": "claude-haiku-4-5", "bias": "BULLISH",
                                       "usage": {"model": "claude-haiku-4-5", "cost_usd": 0.007}}})
    spend = horse_race.llm_spend([screened, escalated])
    assert spend.model_usd == pytest.approx(0.041)
    assert spend.screen_usd == pytest.approx(0.014)
    assert spend.total == pytest.approx(0.055)


def _arm(name, trades):
    return horse_race.ArmResult(name=name, offered=len(trades), directional=len(trades), below_floor=0,
                                pending=0, acted_on=len(trades), could_not_simulate=0, trades=tuple(trades))


def test_a_look_reads_its_own_entry_days_and_nothing_after_them():
    """Computed from the journal every night, a look must say the same thing
    every night: trades opened after its last entry day cannot reach it."""
    days = [date(2026, 3, 2) + timedelta(days=i) for i in range(8)]
    make = lambda arm, r, d: scored(r, arm=arm, entry=d.isoformat(), ticker=f"T{d.day}",
                                    stamp=datetime.combine(d, datetime.min.time(), tzinfo=timezone.utc))
    results = [
        _arm(MODEL_ARM, [make(MODEL_ARM, 0.02 + 0.001 * i, d) for i, d in enumerate(days)]),
        _arm(momentum.NAME, [make(momentum.NAME, -0.01 + 0.001 * i, d) for i, d in enumerate(days)]),
        _arm(hybrid.NAME, [make(hybrid.NAME, 0.0, d) for d in days]),
        _arm(control.NAME, []),
    ]
    index = {d: 0.001 for d in days}
    first = horse_race.look_inputs(results, {}, days, index, 6, 3, 10)
    # A wildly different last two days must not move a look over the first six.
    late = [replace(t, trade=_trade(-0.5, entry=t.entry_day.isoformat())) if t.entry_day > days[5] else t
            for t in results[0].trades]
    again = horse_race.look_inputs([_arm(MODEL_ARM, late), *results[1:]], {}, days, index, 6, 3, 10)
    assert first == again
    assert first.entry_days == 6 and first.index_days == 6 and first.index_missing == 0
    assert first.t_model_momentum is not None and first.t_model_momentum > 0
    assert set(first.t_vs_index) == {MODEL_ARM, momentum.NAME, hybrid.NAME}

    # A day with no index return is an outage the look waits for, unless the
    # source will never price it; then it is left out of the index test only.
    holed = {d: r for d, r in index.items() if d != days[2]}
    waiting = horse_race.look_inputs(results, {}, days, holed, 6, 3, 10)
    assert (waiting.index_days, waiting.index_missing, waiting.index_gaps) == (5, 1, 0)
    settled = horse_race.look_inputs(results, {}, days, holed, 6, 3, 10, index_gaps=frozenset({days[2]}))
    assert (settled.index_days, settled.index_missing, settled.index_gaps) == (5, 0, 1)
    assert settled.t_model_momentum == first.t_model_momentum          # the paired arm tests keep the day


def test_the_gate_json_is_the_headers_numbers(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, [_journal_line("NVDA", stamp)],
                      now, extra=("--seeds", "1000", "--gate-json"), cutoff=None)
    assert code == 0
    data = json.loads(out)
    assert data["status_line"].startswith("independent days since 2026-09-23: 0 of 60")
    assert (data["independent"], data["of"], data["trading_days"]) == (0, 60, 180)
    assert data["decided"] is False and data["outcome"] is None
    assert data["next"]["independent"] == 20 and data["next"]["bar"] == 3.47
    assert data["next"]["entry_days"] == 60 and data["next"]["estimated"]
    assert [look["independent"] for look in data["looks"]] == [20, 40, 60]
    # The exploratory reports ride along: nothing in the window has resolved,
    # so every slice is empty, and an empty slice's numbers are null, not 0.
    assert data["report_since"] == "2026-09-23"
    assert set(data["conviction_groups"]) == {"model", "momentum", "hybrid"}
    for groups in data["conviction_groups"].values():
        assert [g["group"] for g in groups] == ["0.30-0.40", "0.40-0.50", "0.50-0.60", "0.60+"]
        assert all(g == {"group": g["group"], "n": 0, "mean_net": None, "hit_rate": None, "too_few": True}
                   for g in groups)
    assert set(data["sides"]) == {"model", "momentum", "hybrid", "random"}
    assert all(set(per) == {"long", "short"} for per in data["sides"].values())


def test_a_look_waits_for_a_line_written_after_the_close():
    """A cycle straddling 20:00 UTC: the scorer resolves the late line a night
    after its simulated trade is dated, so the look must wait for it."""
    warm = _warm_frame()
    signal_day = warm.index[MIN_WARMUP_BARS].date()
    early = replace(line(ticker="AAA", stamp=datetime.combine(signal_day, datetime.min.time(),
                                                               tzinfo=timezone.utc) + timedelta(hours=19)))
    late = replace(line(ticker="BBB", stamp=datetime.combine(signal_day, datetime.min.time(),
                                                              tzinfo=timezone.utc) + timedelta(hours=20, minutes=5)))
    entry_day = warm.index[MIN_WARMUP_BARS + 1].date()
    exit_day = warm.index[MIN_WARMUP_BARS + 3].date()
    frames = {"AAA": warm, "BBB": warm}
    # Final through the simulated exit only: the late line's scorer exit is one close later.
    source = FinalAwareSource(frames, exit_day)
    fetcher = FinalAwareFetcher(frames, exit_day)
    problem = horse_race.look_data_problem([early, late], fetcher, [entry_day], 1, 3, exit_day,
                                           source=source)
    assert problem and "not resolved yet" in problem
    later = warm.index[MIN_WARMUP_BARS + 4].date()
    resolved = horse_race.look_data_problem([early, late], FinalAwareFetcher(frames, later), [entry_day], 1, 3,
                                            later, source=FinalAwareSource(frames, later))
    assert resolved is None


# --- the owner's exploratory reports: by conviction, longs and shorts --------------------


@pytest.mark.parametrize("conviction, group", [
    (0.30, "0.30-0.40"),
    (0.399999, "0.30-0.40"),
    (0.3999999, "0.40-0.50"),          # rounded to six places: arithmetic noise, not a lower group
    (0.40, "0.40-0.50"),
    (0.5, "0.50-0.60"),
    (0.5999999999, "0.60+"),
    (0.6, "0.60+"),
    (0.95, "0.60+"),
    (1.0, "0.60+"),
])
def test_a_trade_is_grouped_by_the_conviction_of_the_line_that_opened_it(conviction, group):
    assert horse_race.conviction_group(conviction) == group


def test_a_trade_below_the_lowest_group_is_left_out_and_counted():
    assert horse_race.conviction_group(0.2999) is None
    assert horse_race.conviction_group(None) is None
    trades = [scored(0.01, conviction=c) for c in (0.25, None, 0.30, 0.45, 0.45, 0.72)]
    groups, outside = horse_race.by_conviction(trades)
    assert outside == 2
    assert [(g.label, g.n) for g in groups] == [("0.30-0.40", 1), ("0.40-0.50", 2), ("0.50-0.60", 0),
                                                ("0.60+", 1)]


def test_a_group_reports_the_per_trade_tables_own_net_and_hit():
    trades = [scored(0.02, conviction=0.45), scored(-0.01, conviction=0.45), scored(0.5, conviction=0.72)]
    groups, _ = horse_race.by_conviction(trades)
    middle = groups[1]
    assert middle.mean_net == pytest.approx(horse_race.mean_net(trades[:2]))
    assert middle.mean_net == pytest.approx(statistics.fmean([0.02 - 0.002, -0.01 - 0.002]))
    assert middle.hit_rate == pytest.approx(0.5)
    empty = groups[2]
    assert (empty.n, empty.mean_net, empty.hit_rate, empty.too_few) == (0, None, None, True)


def test_too_few_until_a_group_or_a_side_has_twenty_trades():
    assert horse_race.MIN_REPORT_TRADES == 20
    nineteen = [scored(0.01, conviction=0.5) for _ in range(19)]
    twenty = nineteen + [scored(0.01, conviction=0.5)]
    assert horse_race.by_conviction(nineteen)[0][2].too_few
    assert not horse_race.by_conviction(twenty)[0][2].too_few
    assert horse_race.by_side(nineteen)["long"].too_few
    assert not horse_race.by_side(twenty)["long"].too_few


def test_a_slice_with_twenty_trades_shows_its_numbers_in_the_text_and_to_the_page():
    """The case the reports exist for. Twenty model longs at 0.50 (net +0.80%
    each, all hits) and nineteen model shorts at 0.72 (net -1.20% each): the
    0.50-0.60 group and the long side show their numbers, while the 0.60+
    group and the short side, one trade short, still say "too few"."""
    trades = ([scored(0.01, conviction=0.5, side="buy") for _ in range(20)]
              + [scored(-0.01, conviction=0.72, side="sell") for _ in range(19)])
    splits = horse_race.trade_splits([_arm(MODEL_ARM, trades)])
    text = horse_race._render_splits(splits)
    assert "model     0.50-0.60     20    +0.80%   +100.0%" in text
    assert "model     0.60+        too few (n=19)" in text
    assert "model     long          20    +0.80%   +100.0%" in text
    assert "model     short        too few (n=19)" in text
    assert not any(l.startswith(("model     0.50-0.60", "model     long")) and "too few" in l for l in text)

    view = horse_race.GateView(registered=True, mismatches=(), window_lines=39, window_cycle_days=1,
                               unanswered_in_window=0, entry_days=1, independent=0,
                               looks=tuple(decision_gate.evaluate({})), next_estimate=None)
    data = json.loads(json.dumps(horse_race.gate_json(view, 3, STAMP, splits=splits)))
    groups = data["conviction_groups"]["model"]
    assert groups[2] == {"group": "0.50-0.60", "n": 20, "mean_net": pytest.approx(0.008), "hit_rate": 1.0,
                         "too_few": False}
    assert groups[3] == {"group": "0.60+", "n": 19, "mean_net": pytest.approx(-0.012), "hit_rate": 0.0,
                         "too_few": True}
    assert data["sides"]["model"]["long"] == {"n": 20, "mean_net": pytest.approx(0.008), "hit_rate": 1.0,
                                              "too_few": False}
    assert data["sides"]["model"]["short"] == {"n": 19, "mean_net": pytest.approx(-0.012), "hit_rate": 0.0,
                                               "too_few": True}


def test_trades_split_into_longs_and_shorts_by_the_side_they_were_opened_on():
    trades = [scored(0.02, side="buy"), scored(0.01, side="buy"), scored(-0.03, side="buy"),
              scored(0.04, side="sell")]
    split = horse_race.by_side(trades)
    assert list(split) == ["long", "short"]
    assert split["long"].n == 3 and split["short"].n == 1
    assert split["long"].hit_rate == pytest.approx(2 / 3)
    # The short's return is already signed: a price fall is a gain for it.
    assert split["short"].mean_net == pytest.approx(0.04 - 0.002)
    assert split["short"].hit_rate == 1.0


def _split_results():
    make = lambda arm, conviction, side, r: scored(r, arm=arm, conviction=conviction, side=side)
    return [
        _arm(MODEL_ARM, [make(MODEL_ARM, 0.72, "buy", 0.01), make(MODEL_ARM, 0.35, "buy", -0.02),
                         make(MODEL_ARM, 0.25, "sell", 0.03)]),
        _arm(momentum.NAME, [make(momentum.NAME, 0.5, "buy", 0.01)]),
        _arm(hybrid.NAME, [make(hybrid.NAME, 0.55, "sell", 0.01)]),
        _arm(control.NAME, [make(control.NAME, control.CONVICTION, "sell", -0.01)]),
    ]


def test_the_splits_cover_the_owners_arms_and_the_coin_flip_only_by_side():
    splits = horse_race.trade_splits(_split_results())
    assert list(splits.conviction) == [MODEL_ARM, momentum.NAME, hybrid.NAME]
    assert splits.outside == {MODEL_ARM: 1, momentum.NAME: 0, hybrid.NAME: 0}
    assert list(splits.sides) == [MODEL_ARM, momentum.NAME, hybrid.NAME, control.NAME]
    assert splits.sides[MODEL_ARM]["short"].n == 1, "a trade outside every group is still a short"
    assert splits.sides[control.NAME]["short"].n == 1
    text = "\n".join(horse_race._render_splits(splits))
    assert "note: 1 trade(s) below 0.30 or with no conviction, left out of every group: model 1" in text


def test_the_gate_json_carries_both_reports_and_serialises():
    splits = horse_race.trade_splits(_split_results())
    view = horse_race.GateView(registered=True, mismatches=(), window_lines=4, window_cycle_days=1,
                               unanswered_in_window=0, entry_days=1, independent=0,
                               looks=tuple(decision_gate.evaluate({})), next_estimate=None)
    data = json.loads(json.dumps(horse_race.gate_json(view, 3, STAMP, splits=splits)))
    assert data["report_since"] == decision_gate.DECISION_CUTOFF.isoformat() == "2026-09-23"
    model = data["conviction_groups"]["model"]
    assert [g["group"] for g in model] == ["0.30-0.40", "0.40-0.50", "0.50-0.60", "0.60+"]
    assert model[0] == {"group": "0.30-0.40", "n": 1, "mean_net": pytest.approx(-0.022),
                        "hit_rate": 0.0, "too_few": True}
    assert model[1] == {"group": "0.40-0.50", "n": 0, "mean_net": None, "hit_rate": None, "too_few": True}
    # Numbers are given under "too few" too: the page decides how to show them.
    assert model[3]["mean_net"] == pytest.approx(0.008) and model[3]["hit_rate"] == 1.0
    assert set(data["conviction_groups"]) == {"model", "momentum", "hybrid"}
    assert set(data["sides"]) == {"model", "momentum", "hybrid", "random"}
    assert data["sides"]["model"]["long"] == {"n": 2, "mean_net": pytest.approx(-0.007), "hit_rate": 0.5,
                                              "too_few": True}
    assert data["sides"]["momentum"]["short"] == {"n": 0, "mean_net": None, "hit_rate": None, "too_few": True}


def test_the_reports_move_no_look_bar_or_verdict():
    """A crafted race that decides at the first look: the model clearly worse
    than momentum, and momentum clearly ahead of the index. The gate's JSON is
    the same field for field with and without the reports, and the look's
    inputs are the same computed before and after the split."""
    days = [date(2026, 10, 1) + timedelta(days=i) for i in range(60)]
    noise = lambda i: 0.001 * ((i * 7) % 5 - 2)
    stamp = lambda d: datetime.combine(d, datetime.min.time(), tzinfo=timezone.utc)
    make = lambda arm, r, d, conviction, side: scored(r, arm=arm, entry=d.isoformat(), ticker=f"T{d.toordinal()}",
                                                      stamp=stamp(d), conviction=conviction, side=side)
    results = [
        _arm(MODEL_ARM, [make(MODEL_ARM, -0.02 + noise(i), d, 0.3 + 0.01 * (i % 40), "buy" if i % 3 else "sell")
                         for i, d in enumerate(days)]),
        _arm(momentum.NAME, [make(momentum.NAME, 0.02 + noise(i + 1), d, 0.5, "buy") for i, d in enumerate(days)]),
        _arm(hybrid.NAME, [make(hybrid.NAME, noise(i + 2), d, 0.55, "buy") for i, d in enumerate(days)]),
        _arm(control.NAME, []),
    ]
    index = {d: 0.0 for d in days}
    before = horse_race.look_inputs(results, {}, days, index, 60, 3, 10)
    looks = tuple(decision_gate.evaluate({20: before}))
    assert looks[0].outcome == momentum.NAME, "the crafted race decides at the first look"
    view = horse_race.GateView(registered=True, mismatches=(), window_lines=60, window_cycle_days=60,
                               unanswered_in_window=0, entry_days=60, independent=20, looks=looks,
                               next_estimate=None)
    plain = horse_race.gate_json(view, 3, STAMP)
    splits = horse_race.trade_splits(results)
    reported = horse_race.gate_json(view, 3, STAMP, splits=splits)
    new = {"conviction_groups", "sides", "report_since"}
    assert {k: v for k, v in reported.items() if k not in new} == {k: v for k, v in plain.items() if k not in new}
    assert horse_race.look_inputs(results, {}, days, index, 60, 3, 10) == before
    assert sum(g.n for g in splits.conviction[MODEL_ARM]) == 60
    json.dumps(reported)


def test_the_race_prints_both_reports_after_the_per_trade_table(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, [_journal_line("NVDA", stamp)], now)
    assert code == 0
    head = "BY CONVICTION (exploratory; report only; decides nothing)"
    sides = "LONGS VS SHORTS (exploratory; report only; decides nothing)"
    assert out.index("EVERY SCORED TRADE") < out.index(head) < out.index(sides)
    assert out.index(sides) < out.index("WHOLE JOURNAL, FOR READING ONLY")
    by_conviction = out[out.index(head):out.index(sides)].splitlines()
    rows = [l.split() for l in by_conviction if l.split() and l.split()[0] in ("model", "momentum", "hybrid")]
    assert len(rows) == 12, "one row per arm and group"
    assert not any(l.startswith("random") for l in by_conviction)
    # The model's one line was 0.72: one trade in the top group, hidden under "too few".
    assert "model     0.60+        too few (n=1)" in by_conviction
    assert "model     0.30-0.40    too few (n=0)" in by_conviction
    by_side = out[out.index(sides):out.index("WHOLE JOURNAL")].splitlines()
    assert "model     long         too few (n=1)" in by_side
    assert "model     short        too few (n=0)" in by_side
    assert any(l.startswith("random    long") or l.startswith("random    short") for l in by_side)
    # Hidden in the text under "too few"; given in full to the page.
    assert not any("%" in l for l in by_conviction + by_side if l.startswith(("model", "momentum", "hybrid",
                                                                                "random")))


def test_the_gate_json_reads_the_decision_races_trades_and_the_gate_is_unchanged(tmp_path, monkeypatch, capsys):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime.combine(warm.index[-1].date(), datetime.min.time(), tzinfo=timezone.utc) + timedelta(days=1)
    lines = [_journal_line("NVDA", stamp)]
    code, out = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, lines, now, extra=("--gate-json",))
    assert code == 0
    data = json.loads(out)
    top = data["conviction_groups"]["model"][3]
    assert top["group"] == "0.60+" and top["n"] == 1 and top["too_few"] is True
    assert isinstance(top["mean_net"], float) and top["hit_rate"] in (0.0, 1.0)
    assert data["sides"]["model"]["long"]["n"] == 1 and data["sides"]["model"]["short"]["n"] == 0
    assert data["sides"]["random"]["long"]["n"] + data["sides"]["random"]["short"]["n"] == 1

    # With the reports emptied out, every gate field reads the same.
    monkeypatch.setattr(horse_race, "trade_splits",
                        lambda results: horse_race.TradeSplits(conviction={}, outside={}, sides={}))
    _, bare = _race(tmp_path, monkeypatch, capsys, {"NVDA": warm}, lines, now, extra=("--gate-json",))
    without = json.loads(bare)
    new = {"conviction_groups", "sides", "report_since"}
    assert {k: v for k, v in data.items() if k not in new} == {k: v for k, v in without.items() if k not in new}


# --- trigger (d): the real paper account ---------------------------------------------------


def _account_line(at, days, equity, now_equity=None, **extra):
    return {"at": at, "sha": None, "mode": "cycle",
            "account": None if now_equity is None else {"equity": now_equity, "cash": 1.0},
            "history": {"days": days, "equity": equity}, **extra}


SEP_DAYS = ["2026-09-22", "2026-09-23", "2026-09-24", "2026-09-25", "2026-09-28", "2026-09-29", "2026-09-30"]


def _vt_frame():
    """VT from 21 Sep 2026: 100 on 23 Sep, 104 on 30 Sep."""
    closes = [99.0, 99.5, 100.0, 101.0, 102.0, 103.0, 103.5, 104.0]       # 21 Sep .. 30 Sep
    return frame([(c, c + 1, c - 1, c) for c in closes], start="2026-09-21")


def test_read_account_takes_closes_from_every_line_and_the_latest_equity_for_its_day(tmp_path):
    path = tmp_path / "account.jsonl"
    lines = [
        # Written during the 24 Sep session: its history ends with that
        # session's equity so far, which is not a close.
        _account_line("2026-09-24T17:00:00Z", SEP_DAYS[:3], [0.0, 100_000.0, 123_456.0], 100_500.0),
        "not json",
        {"at": "2026-09-29T15:00:00Z", "sha": None, "mode": "cycle", "error": "RuntimeError: boom"},
        # A later record wins a day both give; the union may list it first.
        _account_line("2026-09-25T19:15:32Z", SEP_DAYS[1:3], [100_000.0, 101_000.0], 102_000.0),
    ]
    path.write_text("\n".join(l if isinstance(l, str) else json.dumps(l) for l in reversed(lines)) + "\n")
    record = horse_race.read_account(path)
    assert record.equity == {date(2026, 9, 23): 100_000.0, date(2026, 9, 24): 101_000.0,
                             date(2026, 9, 25): 102_000.0}
    assert record.intraday == date(2026, 9, 25)
    assert record.at == datetime(2026, 9, 29, 15, tzinfo=timezone.utc)


def test_an_old_lines_history_keeps_days_the_latest_month_no_longer_reaches(tmp_path):
    """Alpaca's history is one month: by late October the latest line no
    longer holds 23 Sep, and (d) still needs it as the peak's start and the base."""
    path = tmp_path / "account.jsonl"
    old = _account_line("2026-09-24T21:00:00Z", ["2026-09-23", "2026-09-24"], [100_000.0, 101_000.0], 101_000.0)
    new = _account_line("2026-10-27T21:00:00Z", ["2026-10-26", "2026-10-27"], [99_000.0, 98_000.0], 98_000.0)
    path.write_text(json.dumps(old) + "\n" + json.dumps(new) + "\n")
    record = horse_race.read_account(path)
    assert list(record.equity) == [date(2026, 9, 23), date(2026, 9, 24), date(2026, 10, 26), date(2026, 10, 27)]
    assert record.intraday is None, "a record taken after the close carries closes only"


@pytest.mark.parametrize("text", [None, "", "garbage\n{\n[1]\n", json.dumps({"at": "2026-09-25T19:00:00Z"}),
                                  json.dumps(_account_line("2026-09-25T19:00:00Z", [], [], float("nan")))])
def test_a_missing_or_useless_account_record_is_no_record_never_an_error(tmp_path, text):
    path = tmp_path / "account.jsonl"
    if text is not None:
        path.write_text(text)
    assert horse_race.read_account(path) is None
    watch = horse_race.account_watch(None, {})
    assert watch.problem == "no account record" and not watch.tripped
    data = horse_race.account_watch_json(watch)
    assert data["judged"] is False and data["not_judged"] == "no account record" and data["tripped"] is False
    json.dumps(data, allow_nan=False)


def _sep_account(equity_by_day, at="2026-09-30T21:00:00Z"):
    days = list(equity_by_day)
    return [_account_line(at, days, [equity_by_day[d] for d in days], equity_by_day[days[-1]])]


def _race_sep(tmp_path, monkeypatch, capsys, account, extra=()):
    warm = _warm_frame()
    stamp = _at(warm.index[MIN_WARMUP_BARS].date())
    now = datetime(2026, 10, 1, 2, tzinfo=timezone.utc)
    return _race(tmp_path, monkeypatch, capsys, {"NVDA": warm, "VT": _vt_frame()},
                 [_journal_line("NVDA", stamp)], now, extra=extra, account=account)


def test_trigger_d_is_printed_with_tonights_numbers_when_it_has_not_tripped(tmp_path, monkeypatch, capsys):
    account = _sep_account(dict(zip(SEP_DAYS, [99_000.0, 100_000.0, 101_000.0, 103_000.0, 102_000.0,
                                               101_500.0, 101_000.0])))
    code, out = _race_sep(tmp_path, monkeypatch, capsys, account)
    assert code == 0
    watch = out[out.index("MODEL WATCH"):out.index("decision window:", out.index("MODEL WATCH"))]
    assert ("(d) the paper account: more than 8% below its peak since 2026-09-23, or more than 5 points "
            "behind VT: not tripped") in watch
    assert ("    now 2026-09-30 close: equity 101,000.00 | peak 103,000.00 on 2026-09-25 | "
            "1.94% below the peak (trips beyond 8%)") in watch
    assert ("    vs VT since the 2026-09-23 close, at the 2026-09-30 close: account +1.00%, VT +4.00%: "
            "-3.00 points (trips below -5)") in watch
    assert watch.index("(d) the paper account") < watch.index("(b) retired") < watch.index("(a) closed")


def test_trigger_d_trips_in_the_text_and_the_gate_json(tmp_path, monkeypatch, capsys):
    account = _sep_account(dict(zip(SEP_DAYS, [99_000.0, 100_000.0, 101_000.0, 100_000.0, 98_000.0,
                                               98_500.0, 98_900.0])))
    # 28 and 29 Sep are exactly 5 points behind VT (-2.00% against +3.00%,
    # -1.50% against +3.50%), which does not trip; 30 Sep is 5.10 behind.
    _, out = _race_sep(tmp_path, monkeypatch, capsys, account)
    assert ("behind VT: TRIPPED 1 time(s); latest 2026-09-30: the account is 5.10 points behind VT since "
            "the 2026-09-23 close (account -1.10%, VT +4.00%; more than 5 points)") in out
    _, raw = _race_sep(tmp_path, monkeypatch, capsys, account, extra=("--gate-json",))
    d = json.loads(raw)["watch"]["d"]
    assert d["judged"] is True and d["tripped"] is True and d["vt_not_judged"] is None
    assert [t["day"] for t in d["trips"]] == ["2026-09-30"]
    assert d["trips"][-1]["behind_vt"] is True and d["trips"][-1]["below_peak"] is False
    assert d["latest"] == {"day": "2026-09-30", "equity": 98_900.0, "intraday": False, "peak": 101_000.0,
                           "peak_day": "2026-09-24", "drawdown": pytest.approx(98_900 / 101_000 - 1, abs=1e-6),
                           "account_return": pytest.approx(-0.011), "vt_return": pytest.approx(0.04),
                           "gap": pytest.approx(-0.051)}
    assert d["latest_vt"]["day"] == "2026-09-30"
    assert (d["start"], d["max_drawdown"], d["max_behind_vt"]) == ("2026-09-23", 0.08, 0.05)
    json.dumps(d, allow_nan=False)


def test_trigger_d_moves_no_look_bar_or_verdict(tmp_path, monkeypatch, capsys):
    """Nothing that decides the race reads (d): every gate field reads the
    same with no account record, a calm one, a tripped one and a garbage one."""
    calm = _sep_account(dict(zip(SEP_DAYS, [99_000.0, 100_000.0, 101_000.0, 103_000.0, 102_000.0,
                                            101_500.0, 101_000.0])))
    tripped = _sep_account(dict(zip(SEP_DAYS, [99_000.0, 100_000.0, 80_000.0, 70_000.0, 60_000.0,
                                               50_000.0, 40_000.0])))
    runs = {}
    for name, account in (("none", None), ("calm", calm), ("tripped", tripped), ("garbage", "{{nope\n")):
        _, raw = _race_sep(tmp_path, monkeypatch, capsys, account, extra=("--gate-json",))
        runs[name] = json.loads(raw)
    assert runs["none"]["watch"]["d"]["not_judged"] == "no account record"
    assert runs["garbage"]["watch"]["d"]["not_judged"] == "no account record"
    assert runs["tripped"]["watch"]["d"]["tripped"] is True and runs["calm"]["watch"]["d"]["tripped"] is False
    strip = lambda data: {k: v for k, v in data.items() if k not in ("watch", "generated_at")}
    assert strip(runs["none"]) == strip(runs["calm"]) == strip(runs["tripped"]) == strip(runs["garbage"])
    # And gate_json itself: the same fields with and without the account.
    view = horse_race.GateView(registered=True, mismatches=(), window_lines=1, window_cycle_days=1,
                               unanswered_in_window=0, entry_days=0, independent=0,
                               looks=tuple(decision_gate.evaluate({})), next_estimate=None)
    record = horse_race.AccountRecord(equity={date(2026, 9, 23): 100_000.0, date(2026, 9, 24): 50_000.0},
                                      at=STAMP)
    with_d = horse_race.gate_json(view, 3, STAMP, account=horse_race.account_watch(record, {}))
    without = horse_race.gate_json(view, 3, STAMP)
    assert without["watch"] is None and with_d["watch"]["d"]["tripped"] is True
    assert {k: v for k, v in with_d.items() if k != "watch"} == {k: v for k, v in without.items() if k != "watch"}
    json.dumps(with_d, allow_nan=False)


def test_an_intraday_record_is_shown_apart_and_a_missing_vt_close_is_said(tmp_path):
    """Since 26 Sep 2026 (d) is judged on closes only: the intraday number is
    its own mid-day line, after the close it does not replace."""
    record = horse_race.AccountRecord(
        equity={date(2026, 9, 23): 100_000.0, date(2026, 9, 24): 100_800.0, date(2026, 9, 25): 100_926.06},
        at=datetime(2026, 9, 25, 19, 15, 32, tzinfo=timezone.utc), intraday=date(2026, 9, 25))
    vt = {date(2026, 9, 23): 100.0, date(2026, 9, 24): 100.5}
    lines = horse_race.account_lines(horse_race.account_watch(record, vt))
    assert lines[1].startswith("    now 2026-09-24 close: equity 100,800.00")
    assert ("vs VT since the 2026-09-23 close, at the 2026-09-24 close: account +0.80%, VT +0.50%: "
            "+0.30 points") in lines[2]
    assert lines[3].startswith("    mid-day 2026-09-25 (recorded 19:15 UTC, not a close; never trips (d)): "
                               "equity 100,926.06")
    assert len(lines) == 4, "a mid-day reading above both lines warns of nothing"
    no_base = horse_race.account_lines(horse_race.account_watch(record, {date(2026, 9, 24): 100.5}))
    assert no_base[2] == "    vs VT: not judged: no final VT close for 2026-09-23, the base"
    before = horse_race.AccountRecord(equity={date(2026, 9, 22): 100_000.0}, at=STAMP)
    assert horse_race.account_lines(horse_race.account_watch(before, vt)) == [
        horse_race.trigger_d_label() + ": not judged: no account close on or after 2026-09-23"]


def test_an_intraday_reading_below_the_line_is_a_mid_day_warning_never_a_trip(tmp_path):
    """26 Sep 2026: (d) trips on closing equity only. A latest intraday
    reading 9% below the peak is shown, in the text and the gate JSON, as a
    separate warning marked mid-day; `tripped` stays false, so the daily
    health check raises no (d) alarm for it."""
    record = horse_race.AccountRecord(
        equity={date(2026, 9, 23): 100_000.0, date(2026, 9, 24): 101_000.0, date(2026, 9, 25): 91_000.0},
        at=datetime(2026, 9, 25, 15, 30, tzinfo=timezone.utc), intraday=date(2026, 9, 25))
    watch = horse_race.account_watch(record, {date(2026, 9, 23): 100.0, date(2026, 9, 24): 100.0})
    assert not watch.tripped
    lines = horse_race.account_lines(watch)
    assert lines[0].endswith(": not tripped")
    assert lines[1].startswith("    now 2026-09-24 close: equity 101,000.00")
    assert lines[3].startswith("    mid-day 2026-09-25 (recorded 15:30 UTC, not a close; never trips (d)): "
                               "equity 91,000.00 | 9.90% below the peak")
    assert lines[4].startswith("    WARNING (mid-day, does not trip (d)): mid-day 2026-09-25: equity 91,000.00")
    data = horse_race.account_watch_json(watch)
    json.dumps(data, allow_nan=False)
    assert data["tripped"] is False and data["trips"] == []
    assert data["latest"]["day"] == "2026-09-24" and data["latest"]["intraday"] is False
    assert data["midday"]["day"] == "2026-09-25" and data["midday"]["intraday"] is True
    warning = data["midday_warning"]
    assert (warning["mid_day"], warning["trips_d"], warning["below_peak"], warning["behind_vt"]) == (
        True, False, True, True)
    from analysis import health

    assert health.drawdown_tripped({"watch": {"d": data}}) is None
    calm = horse_race.account_watch_json(horse_race.account_watch(
        horse_race.AccountRecord(equity=dict(record.equity, **{}) | {date(2026, 9, 25): 100_500.0},
                                 at=record.at, intraday=date(2026, 9, 25)), {}))
    assert calm["midday"]["equity"] == 100_500.0 and calm["midday_warning"] is None
