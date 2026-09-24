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


def _race(tmp_path, monkeypatch, capsys, frames, journal_lines, now, extra=(),
          cutoff=date(2000, 1, 1)):
    """Run the race on a tiny journal. These journals are dated early 2026,
    before the real cutoff, so by default the cutoff is moved back to take
    them in; a test about the cutoff itself passes ``cutoff=None``."""
    journal = tmp_path / "signal_journal.log"
    journal.write_text("\n".join(json.dumps(l) for l in journal_lines) + "\n", encoding="utf-8")
    if cutoff is not None:
        monkeypatch.setattr(decision_gate, "DECISION_CUTOFF", cutoff)
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
    assert "(b) 5 answered days in a row with no SHORT while SPY fell: not yet judged (1 of 5" in out
    assert "(c) failed or timed-out calls above 5% of names over 5 cycle days: not yet judged (1 of 5" in out


def test_a_news_outage_is_not_a_failed_model_call_and_a_wrong_ticker_answer_is_no_answer():
    from analysis.reader import entry_from

    stamp = "2026-09-25T15:00:00+00:00"
    context_failure = entry_from({"ts_utc": stamp, "ticker": "NVDA", "error": "Bright Data unreachable",
                                  "stage": "context"})
    timeout = entry_from({"ts_utc": stamp, "ticker": "LLY", "error": "read timed out"})
    wrong = entry_from({"ts_utc": stamp, "ticker": "MSFT", "error": "answered for NVDA",
                        "signal": {"bias": "BEARISH", "conviction": 0.8}})
    fine = entry_from({"ts_utc": stamp, "ticker": "JPM", "signal": {"bias": "BEARISH", "conviction": 0.8}})
    (day,) = horse_race.watch_days([context_failure, timeout, wrong, fine])
    assert (day.asked, day.failed, day.shorts) == (3, 2, 1)
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
