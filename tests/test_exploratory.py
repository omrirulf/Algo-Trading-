"""Exploratory tests A, B and C, their counters, and results hidden until a checkpoint.

Pre-registration section 13 (2026-09-28). Every rule is checked on
hand-built prices: A's veto against the 200-day average of closes before
the signal's day, B's month-end decisions and switches, C's limit orders
and fill rule; then that between checkpoints the funds document carries
counters and no exploratory result, and that a look's record is made once
and kept.
"""

from __future__ import annotations

import json
import math
from datetime import date, datetime, timedelta, timezone
from types import SimpleNamespace

import pandas as pd
import pytest

from analysis import multiple_tests as mt
from analysis.reader import JournalEntry
from app.schemas import Bias, LLMSignal
from shadow import exploratory as xp
from shadow import run as shadow_run
from shadow import schedule
from shadow.fund import Line, STARTING_CASH
from shadow.market import Bars, SimFeed
from tests.test_shadow_fund import COST, S, said, universe


def signal(bias: str, ticker: str = "MSFT", conviction: float = 0.5) -> LLMSignal:
    return LLMSignal(ticker=ticker, bias=Bias(bias), conviction=conviction, rationale="test")


def daily(start: str, closes, ticker_open=None, dividends=None) -> pd.DataFrame:
    days = pd.bdate_range(start, periods=len(closes))
    frame = pd.DataFrame({"Open": closes if ticker_open is None else ticker_open, "High": closes,
                          "Low": closes, "Close": closes, "Dividends": dividends or 0.0}, index=days)
    return frame


# --------------------------------------------------------------------------- #
# A: the 200-day veto
# --------------------------------------------------------------------------- #


def test_the_veto_keeps_a_side_only_on_its_side_of_the_average():
    assert xp.veto(signal("BULLISH"), 101.0, 100.0).bias is Bias.BULLISH
    assert xp.veto(signal("BULLISH"), 99.0, 100.0).bias is Bias.NEUTRAL
    assert xp.veto(signal("BULLISH"), 100.0, 100.0).bias is Bias.NEUTRAL      # strict: equal is NEUTRAL
    assert xp.veto(signal("BEARISH"), 99.0, 100.0).bias is Bias.BEARISH
    assert xp.veto(signal("BEARISH"), 101.0, 100.0).bias is Bias.NEUTRAL
    # No live price or no average: the momentum signal is kept as it is.
    assert xp.veto(signal("BULLISH"), None, 100.0).bias is Bias.BULLISH
    assert xp.veto(signal("BULLISH"), 99.0, None).bias is Bias.BULLISH
    assert xp.veto(signal("NEUTRAL"), 99.0, 100.0).bias is Bias.NEUTRAL
    kept = signal("BULLISH", conviction=0.42)
    assert xp.veto(kept, 101.0, 100.0) is kept                                # conviction unchanged


def test_the_average_is_of_the_200_final_closes_before_the_signal_day():
    closes = [float(i) for i in range(1, 251)]
    bars = Bars({"MSFT": daily("2025-10-01", closes)})
    days = [d.date() for d in pd.bdate_range("2025-10-01", periods=250)]
    signal_day = days[-1]                                   # its own close (250) is never read
    assert xp.sma_before(bars, "MSFT", signal_day) == pytest.approx(sum(closes[-201:-1]) / 200)
    assert xp.sma_before(bars, "MSFT", days[150]) is None     # fewer than 200 closes before it


def line(ticker: str, day: date, *, live=None, technicals=None) -> Line:
    entry = said(ticker, day, live_record=live, technicals=technicals or {})
    return Line(ticker, day, 1, entry)


def test_the_counter_counts_momentum_signals_and_those_the_veto_removes(monkeypatch):
    closes = [100.0] * 250
    bars = Bars({"MSFT": daily("2025-10-01", closes), "NVDA": daily("2025-10-01", closes),
                 "JPM": daily("2025-10-01", closes)})
    day = date(2026, 9, 28)
    live = lambda p: {"price": p, "asked_at": "2026-09-28T15:00:00+00:00"}  # noqa: E731
    cycles = {day: [line("MSFT", day, live=live(101.0)), line("NVDA", day, live=live(99.0)),
                    line("JPM", day)]}
    monkeypatch.setattr(xp, "rule_signal", lambda name: lambda ln: signal("BULLISH", ln.ticker))
    counts = xp.veto_counters(cycles, bars, day)
    assert counts["signals"] == 3 and counts["vetoed"] == 1 and counts["no_live_price"] == 1
    assert counts["vetoed_share"] == pytest.approx(1 / 3) and counts["under_ten_percent"] is False


# --------------------------------------------------------------------------- #
# B: 10-month timing
# --------------------------------------------------------------------------- #


def month_bars(month_closes: dict[str, float], ticker: str = "VT") -> pd.DataFrame:
    """One bar per trading day, each month flat at its given close."""
    rows = {}
    for d in pd.bdate_range("2025-11-03", "2027-01-29"):
        key = d.strftime("%Y-%m")
        if key in month_closes and xp.is_trading_day(d.date()):
            rows[d] = month_closes[key]
    frame = pd.DataFrame({"Close": pd.Series(rows)})
    frame["Open"] = frame["High"] = frame["Low"] = frame["Close"]
    frame["Dividends"] = 0.0
    return frame


MONTHS = [f"{y}-{m:02d}" for y, m in [(2025, 11), (2025, 12)] + [(2026, k) for k in range(1, 13)]]


def test_each_month_end_decides_on_the_close_against_its_ten_month_average():
    closes = {m: 100.0 for m in MONTHS} | {"2026-09": 110.0, "2026-10": 90.0}
    bars = Bars({"VT": month_bars(closes), "BIL": month_bars({m: 50.0 for m in MONTHS})})
    signals = xp.timing_signals(bars, date(2026, 11, 30))
    assert [s["day"] for s in signals] == ["2026-09-30", "2026-10-30", "2026-11-30"]
    assert [s["hold"] for s in signals] == ["VT", "BIL", "BIL"]
    assert signals[0]["average"] == pytest.approx((9 * 100 + 110) / 10)
    counts = xp.timing_counters(bars, date(2026, 11, 30))
    assert counts["switches"] == 1 and counts["state"] == "BIL" and counts["last_signal"] == "2026-11-30"


def test_the_timing_fund_switches_at_the_next_open_and_pays_both_sides():
    closes = {m: 100.0 for m in MONTHS} | {"2026-09": 110.0, "2026-10": 90.0}
    bars = Bars({"VT": month_bars(closes), "BIL": month_bars({m: 50.0 for m in MONTHS})})
    fund = xp.TimingFund("vt_timing", bars, date(2026, 11, 30))
    days = [d.date() for d in pd.bdate_range("2026-09-28", "2026-11-06") if xp.is_trading_day(d.date())]
    for d in days:
        fund.session(d)
    assert fund.days[0].day == date(2026, 10, 1)            # nothing before the first decision's next open
    shares = math.floor(STARTING_CASH / (90.0 * (1 + COST)))
    assert fund.qty and fund.holding == "BIL" and fund.switches == 1
    # Bought VT at 90 on 1 Oct, sold at November's 100 on 2 Nov, bought BIL at 50: two sides each way.
    cash_after_vt = STARTING_CASH - shares * 90.0 * (1 + COST)
    after_sale = cash_after_vt + shares * 100.0 * (1 - COST)
    bil = math.floor(after_sale / (50.0 * (1 + COST)))
    assert fund.qty == bil and fund.cash == pytest.approx(after_sale - bil * 50.0 * (1 + COST))


def test_a_missing_bar_makes_a_leg_wait_in_cash():
    closes = {m: 100.0 for m in MONTHS} | {"2026-09": 110.0}
    bil = month_bars({m: 50.0 for m in MONTHS})
    vt = month_bars(closes).drop(pd.Timestamp("2026-10-01"))
    fund = xp.TimingFund("vt_timing", Bars({"VT": vt, "BIL": bil}), date(2026, 10, 31))
    fund.session(date(2026, 10, 1))
    assert fund.holding is None and fund.waited == 1 and fund.days[-1].equity == STARTING_CASH
    fund.session(date(2026, 10, 2))
    assert fund.holding == "VT"


# --------------------------------------------------------------------------- #
# C: pullback limit entry
# --------------------------------------------------------------------------- #


def test_the_fill_rule_is_the_open_past_the_limit_else_the_limit_in_the_range():
    buy = Bias.BULLISH
    assert xp.touches(buy, 100.0, (99.0, 103.0, 98.0, 101.0, 0.0)) == (99.0, "open")
    assert xp.touches(buy, 100.0, (101.0, 103.0, 99.5, 101.0, 0.0)) == (100.0, "range")
    assert xp.touches(buy, 100.0, (101.0, 103.0, 100.5, 101.0, 0.0)) is None
    sell = Bias.BEARISH
    assert xp.touches(sell, 100.0, (101.0, 103.0, 98.0, 99.0, 0.0)) == (101.0, "open")
    assert xp.touches(sell, 100.0, (99.0, 100.2, 98.0, 99.0, 0.0)) == (100.0, "range")
    assert xp.touches(sell, 100.0, (99.0, 99.5, 98.0, 99.0, 0.0)) is None


def test_the_limit_is_the_signal_price_less_half_an_atr_or_the_technicals_price():
    day = date(2026, 9, 28)
    with_live = line("MSFT", day, live={"price": 200.0}, technicals={"last_close": 190.0, "atr14": 4.0})
    assert xp.limit_price(with_live, Bias.BULLISH) == (198.0, None)
    assert xp.limit_price(with_live, Bias.BEARISH) == (202.0, None)
    fallback = line("MSFT", day, technicals={"last_close": 190.0, "atr14": 4.0})
    assert xp.limit_price(fallback, Bias.BULLISH) == (188.0, "technicals price")
    assert xp.limit_price(line("MSFT", day, technicals={"last_close": 190.0}), Bias.BULLISH)[0] is None


def pullback_setup(atr: float):
    bars = universe()
    feed = SimFeed(bars)
    close = bars.bar("MSFT", S[0])[3]
    ln = line("MSFT", S[0], live={"price": close}, technicals={"last_close": close, "atr14": atr})
    fund = xp.PullbackFund("momentum_pullback", feed, bars)
    fund.signal_for = lambda _: signal("BULLISH", "MSFT", 0.6)
    return bars, feed, fund, ln, close


def run_sessions(fund, feed, cycle, days):
    for k, d in enumerate(days):
        feed.at_open(d)
        fund.session(d, cycle if k == 0 else None)


def test_an_order_fills_where_the_bars_say_and_is_sized_by_the_engine():
    bars, feed, fund, ln, close = pullback_setup(atr=0.4)
    limit = close - 0.2
    expected = None
    for d in S[1:4]:
        expected = xp.touches(Bias.BULLISH, limit, bars.bar("MSFT", d))
        if expected:
            break
    assert expected is not None, "the tape must reach a limit this close"
    run_sessions(fund, feed, [ln], S[1:5])
    entry = next(f for f in fund.broker.fills if f.kind == "entry")
    assert entry.ticker == "MSFT" and entry.price == pytest.approx(expected[0]) and entry.qty > 0
    assert fund.pullback.placed == 1 and fund.pullback.filled_open + fund.pullback.filled_range == 1


def test_an_order_the_bars_never_reach_is_cancelled_after_three_sessions():
    bars, feed, fund, ln, close = pullback_setup(atr=1.0)
    ln = line("MSFT", S[0], live={"price": close}, technicals={"last_close": close, "atr14": close})  # half below
    run_sessions(fund, feed, [ln], S[1:6])
    assert fund.pullback.placed == 1 and fund.pullback.missed == 1
    assert not fund.broker.positions and not fund.orders


def test_the_signal_level_counter_says_filled_missed_or_still_open():
    bars = universe()
    close = bars.bar("MSFT", S[0])[3]
    near = line("MSFT", S[0], live={"price": close}, technicals={"last_close": close, "atr14": 0.4})
    far = line("NVDA", S[0], live={"price": 1.0}, technicals={"last_close": 1.0, "atr14": 1.0})     # limit 0.5
    import shadow.exploratory as module
    original = module.rule_signal
    module.rule_signal = lambda name: lambda ln: signal("BULLISH", ln.ticker)
    try:
        done = xp.pullback_counters({S[0]: [near, far]}, bars, S[0], S[10])
        early = xp.pullback_counters({S[0]: [far]}, bars, S[0], S[1])
    finally:
        module.rule_signal = original
    assert done["filled"] + done["missed"] == 2 and done["fill_rate"] is not None
    assert early["still_open"] == 1 and early["fill_rate"] is None


# --------------------------------------------------------------------------- #
# Between checkpoints: counters only; at a look: one record, kept
# --------------------------------------------------------------------------- #


class NoPrices:
    def __init__(self, **kw):
        pass

    def ohlc(self, ticker, start, end):
        return pd.DataFrame()


def build_args(tmp_path, race=None, previous=None):
    journal = tmp_path / "journal"
    journal.mkdir(exist_ok=True)
    (journal / "2026-10.log").write_text("")
    gate = tmp_path / "race_gate.json"
    gate.write_text(json.dumps(race or {"looks": [{"reached": False}] * 3}))
    prev = tmp_path / "funds.json"
    prev.write_text(json.dumps(previous or {}))
    return SimpleNamespace(journal=journal, audit=tmp_path / "audit.log", account=tmp_path / "account.jsonl",
                           random=2, processes=1, race_gate=gate, previous=prev)


FUND_ROWS = [{"name": n, "exploratory": n.startswith("model_")} for n in
             ("model", "momentum", "hybrid", "vt", "model_by_conviction", "model_sized", "model_same_day")]


def passed_calibration(monkeypatch, calls):
    from shadow import calibration as calib

    monkeypatch.setattr(schedule, "CALIBRATION_START", date(2026, 9, 28))
    monkeypatch.setattr(calib, "calibration_report", lambda **kw: {"status": "passed"})
    monkeypatch.setattr(shadow_run, "OhlcFetcher", NoPrices)

    def fake(entries, start, final_through, fetcher, **kw):
        calls.append(kw)
        rows = FUND_ROWS if kw.get("exploratory") else [r for r in FUND_ROWS if not r["exploratory"]]
        out = {"start": start.isoformat(), "days": [], "list": [dict(r) for r in rows], "band": {}}
        if kw.get("exploratory"):
            out["tests"] = {"momentum_200": {"t": 1.0}}
        return out, {"four": {}, "coin": {}}

    monkeypatch.setattr(shadow_run, "run_funds", fake)


NOW = datetime(2026, 12, 22, 23, 0, tzinfo=timezone.utc)


def test_between_checkpoints_there_are_counters_and_no_exploratory_result(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    out = shadow_run.build(build_args(tmp_path), NOW)
    assert calls[-1]["exploratory"] is False
    assert [r["name"] for r in out["funds"]["list"]] == ["model", "momentum", "hybrid", "vt"]
    assert out["exploratory"]["checkpoints"] == []
    assert set(out["exploratory"]["counters"]) == {"momentum_200", "vt_timing", "momentum_pullback",
                                                   "model_same_day"}
    json.dumps(out, allow_nan=False)


def test_a_look_reached_makes_one_record_and_later_nights_keep_it(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    race = {"looks": [{"reached": True}, {"reached": False}, {"reached": False}]}
    first = shadow_run.build(build_args(tmp_path, race), NOW)
    assert calls[-1]["exploratory"] is True
    (record,) = first["exploratory"]["checkpoints"]
    assert record["look"] == 1 and record["made_on"] == "2026-12-22"
    assert set(record["funds"]) == {"model_by_conviction", "model_sized", "model_same_day"}
    assert record["tests"] == {"momentum_200": {"t": 1.0}}
    assert [r["name"] for r in first["funds"]["list"]] == ["model", "momentum", "hybrid", "vt"]
    later = shadow_run.build(build_args(tmp_path, race, previous=first), NOW + timedelta(days=1))
    assert calls[-1]["exploratory"] is False
    assert later["exploratory"]["checkpoints"] == [record]


def test_a_look_before_calibration_passes_records_counters_only(monkeypatch, tmp_path):
    monkeypatch.setattr(schedule, "CALIBRATION_START", None)
    monkeypatch.setattr(shadow_run, "OhlcFetcher", NoPrices)
    monkeypatch.setattr(shadow_run, "run_funds", lambda *a, **k: pytest.fail("no fund before calibration"))
    race = {"looks": [{"reached": True}, {"reached": False}, {"reached": False}]}
    out = shadow_run.build(build_args(tmp_path, race), NOW)
    (record,) = out["exploratory"]["checkpoints"]
    assert record["status"].startswith("calibration has not passed") and "funds" not in record


# --------------------------------------------------------------------------- #
# The checkpoint arithmetic
# --------------------------------------------------------------------------- #


def test_benjamini_hochberg_matches_the_textbook_steps():
    p = [0.01, 0.04, 0.03, 0.005]
    # Ordered 0.005, 0.01, 0.03, 0.04 -> 4p/rank = 0.02, 0.02, 0.04, 0.04.
    assert mt.bh_adjust(p) == pytest.approx([0.02, 0.04, 0.04, 0.02])
    assert mt.bh_adjust([0.9, 0.95]) == pytest.approx([0.95, 0.95])
    assert mt.bh_adjust([]) == []


def test_p_values_and_the_deflated_sharpe_ratio():
    assert mt.p_two_sided(1.959964) == pytest.approx(0.05, abs=1e-5)
    assert mt.p_two_sided(None) is None
    # With N trials and normal returns, the DSR asks the t to clear the expected best of N null trials.
    assert mt.expected_max_sr(18, 100) * 10 == pytest.approx(1.853, abs=0.01)
    good = {"sr": 0.4, "t_days": 100, "skew": 0.0, "kurt": 3.0}
    weak = {"sr": 0.1, "t_days": 100, "skew": 0.0, "kurt": 3.0}
    assert mt.deflated_sharpe(good, 18) > 0.95 > mt.deflated_sharpe(weak, 18)
    stats = mt.series_stats([0.01, -0.02, 0.03, 0.0, 0.01])
    assert stats["t_days"] == 5 and stats["kurt"] > 0
    assert mt.series_stats([0.0, 0.0, 0.0]) is None


def test_n_is_the_graveyard_count_and_the_table_leaves_out_tests_with_no_data():
    # 18 ideas at registration, and the 13 history screens logged on 2026-09-27: they count in N too.
    assert mt.graveyard_n() == 31
    table = mt.checkpoint_table([{"name": "a", "t": 3.0, "stats": {"sr": 0.3, "t_days": 100, "skew": 0.0,
                                                                     "kurt": 3.0}},
                                 {"name": "b", "t": None}], 18)
    assert table[0]["p_bh"] == pytest.approx(mt.p_two_sided(3.0)) and table[0]["passes_bh"] is True
    assert table[1]["no_data"] is True and table[1]["p_bh"] is None


# --------------------------------------------------------------------------- #
# The race side at a checkpoint
# --------------------------------------------------------------------------- #

UP = {"return_63d": 0.10, "distance_sma50": 0.03, "annualised_volatility": 0.20, "atr14": 2.0,
      "last_close": 100.0}


def test_the_race_side_pairs_a_with_momentum_and_splits_filled_from_missed(monkeypatch):
    from types import SimpleNamespace as NS

    d = date(2026, 10, 1)
    at = datetime(2026, 10, 1, 15, 0, tzinfo=timezone.utc)
    lines = [said("MSFT", d, technicals=UP, live_record={"price": 100.0}),
             said("NVDA", d, technicals=UP, live_record={"price": 100.0})]
    after = [x.date() for x in pd.bdate_range("2026-10-02", periods=5)]
    msft = pd.DataFrame({"Open": 101.0, "High": 101.5, "Low": 98.5, "Close": 100.0, "Dividends": 0.0},
                        index=pd.DatetimeIndex([pd.Timestamp(x) for x in after]))
    nvda = msft.assign(Low=100.5)                                   # never reaches its limit of 99
    long_bars = Bars({"MSFT": msft, "NVDA": nvda})
    entry = after[0]
    fake = {"momentum": [NS(ticker="MSFT", signal_at=at, net=0.01, entry_day=entry),
                         NS(ticker="NVDA", signal_at=at, net=0.03, entry_day=entry)],
            xp.VETO: [NS(ticker="MSFT", signal_at=at, net=0.01, entry_day=entry)],
            "insiders": [NS(ticker="MSFT", signal_at=at, net=0.02, entry_day=entry)]}
    monkeypatch.setattr(xp, "arm_trades", lambda name, entries, how: fake[name])
    how = xp.RaceSettings(0.30, 3, "auto", date(2026, 10, 20), None, None, 100_000.0, 2.0, 0.05, 0.001)
    out = xp.race_tests(lines, long_bars, how, date(2026, 9, 28), date(2026, 9, 23))
    assert out[xp.VETO]["days"] == 1 and out[xp.VETO]["mean_daily_diff"] == pytest.approx(0.01 - 0.02)
    assert out["insiders"]["mean_daily_diff"] == pytest.approx(0.02 - 0.01)
    split = out["pullback_filled_vs_missed"]
    assert split["filled"]["n"] == 1 and split["missed"]["n"] == 1
    assert split["missed_minus_filled"] == pytest.approx(0.03 - 0.01)


def test_the_checkpoint_table_reads_every_test_of_the_family():
    record = {"race": {"insiders": {"t": 1.0, "stats": None}, xp.VETO: {"t": None}},
              "tests": {xp.TIMING: {"t": 2.5, "stats": {"sr": 0.2, "t_days": 60, "skew": 0.0, "kurt": 3.0}}}}
    table = shadow_run.checkpoint_table_for(record)
    assert table["n_trials"] == mt.graveyard_n() == 31
    rows = {r["name"]: r for r in table["rows"]}
    assert len(rows) == 8 and rows["B, fund"]["dsr"] is not None
    assert rows["A, race arm"]["no_data"] is True and rows["C, fund"]["no_data"] is True


# --------------------------------------------------------------------------- #
# Section 13.7: acting differently, and "not tested"
# --------------------------------------------------------------------------- #


def test_b_counts_trading_days_meant_to_be_out_of_vt():
    closes = {m: 100.0 for m in MONTHS} | {"2026-09": 110.0, "2026-10": 90.0}
    bars = Bars({"VT": month_bars(closes), "BIL": month_bars({m: 50.0 for m in MONTHS})})
    counts = xp.timing_counters(bars, date(2026, 11, 6))
    # Out of VT from the 2 Nov open (after the 30 Oct decision) through 6 Nov: 5 trading days.
    assert counts["days_out_of_vt"] == 5


def row(t=None, passes=False, no_data=False):
    return {"t": t, "passes_bh": passes, "no_data": no_data}


@pytest.mark.parametrize("args, expected", [
    ((row(3.0, True), 0.01, 50, False, True), "promising"),
    ((row(-3.0, True), -0.01, 50, False, True), "dead"),
    ((row(-0.5), -0.001, 50, True, True), "dead"),            # final look, mean at or below zero
    ((row(-0.5), -0.001, 50, True, False), "not proven"),     # B: that rule does not apply
    ((row(-3.0, True), -0.01, 50, True, False), "dead"),      # B can die through Benjamini-Hochberg
    ((row(-0.5), -0.001, 19, True, True), "not tested"),      # acted fewer than 20 times
    ((row(-3.0, True), -0.01, 5, True, False), "not tested"),
    ((row(-0.5), -0.001, 5, False, True), "not proven"),      # only the final look says "not tested"
    ((row(-0.5), -0.001, None, True, True), "dead"),          # always acts: never "not tested"
    ((row(no_data=True), None, None, False, True), "no data"),
])
def test_the_outcome_of_each_test(args, expected):
    assert shadow_run.outcome(*args) == expected


def test_the_table_reads_how_often_each_idea_acted_differently():
    record = {"look": 3, "counters": {xp.VETO: {"vetoed": 7}, xp.TIMING: {"days_out_of_vt": 40}},
              "race": {"insiders": {"t": 0.5, "mean_daily_diff": 0.001, "trades": 30}},
              "tests": {xp.TIMING: {"t": -0.4, "mean_daily_diff": -0.0002},
                        "model_by_conviction": {"t": 0.1, "mean_daily_diff": 0.0, "acted": 3}}}
    rows = {r["name"]: r for r in shadow_run.checkpoint_table_for(record)["rows"]}
    assert rows["A, race arm"]["acted_differently"] == 7 and rows["A, race arm"]["outcome"] == "not tested"
    assert rows["model_by_conviction"]["outcome"] == "not tested"
    assert rows["B, fund"]["acted_differently"] == 40 and rows["B, fund"]["outcome"] == "not proven"
    assert rows["insider arm"]["outcome"] == "not proven"
    assert rows["C, fund"]["acted_differently"] == 0 and rows["C, fund"]["outcome"] == "not tested"
    assert rows["model_same_day"]["acted_differently"] is None                  # always acts


def test_the_same_day_counter_counts_only_from_the_fund_start():
    before, start = date(2026, 9, 25), date(2026, 9, 28)
    entries = [said("MSFT", before, bias="BULLISH"), said("MSFT", start, bias="BULLISH")]
    bars = Bars({})
    counts = shadow_run.exploratory_counters(entries, bars, date(2026, 10, 2))
    # Neither line has a recorded price; only the one from the 28 Sep cycle is counted.
    assert counts["model_same_day"]["lines_without_usable_price"]["no_price"] == 1


def test_c_acts_differently_only_where_its_outcome_differs_from_the_momentum_funds():
    from types import SimpleNamespace as NS

    from shadow.broker import Fill

    d = date(2026, 10, 1)
    next_day = xp.sessions_after(d, 1)[0]
    later = xp.sessions_after(d, 2)[1]
    considered = [("MSFT", d), ("NVDA", d), ("JPM", d), ("AAPL", d), ("KO", d), ("XOM", d), ("PG", d)]
    stats = xp.PullbackStats(missed=2, skipped_held=2, considered=considered,
                             filled=[("MSFT", d, next_day, 99.0), ("NVDA", d, later, 50.0),
                                     ("JPM", d, next_day, 30.0)])
    momentum = NS(broker=NS(fills=[Fill(next_day, "MSFT", "entry", "buy", 10, 99.0, 1.0),
                                   Fill(next_day, "NVDA", "entry", "buy", 10, 51.0, 1.0),
                                   Fill(next_day, "AAPL", "entry", "buy", 10, 200.0, 1.0)]))
    # Same: MSFT (both bought at 99); KO, XOM, PG (neither bought: held or missed in both).
    # Different: NVDA (both bought, other prices); JPM (only C bought); AAPL (only momentum bought).
    assert xp.pullback_acted(NS(pullback=stats), momentum) == 3


def test_model_sized_acts_differently_only_where_its_factor_is_not_one():
    from types import SimpleNamespace as NS

    from shadow.order_matters import Event

    d = date(2026, 10, 1)
    events = [Event(d, "A", c, status, "") for c, status in
              ((0.35, "ACCEPTED"), (0.45, "ACCEPTED"), (0.55, "ACCEPTED"), (0.59, "ACCEPTED"),
               (0.65, "ACCEPTED"), (0.35, "REJECTED"), (0.2, "ACCEPTED"))]
    assert shadow_run.sized_trades_scaled(NS(order_events=events)) == 3


def test_a_checkpoint_run_of_every_fund_carries_each_test_and_its_count():
    from tests.test_shadow_variants import Walks, journal_with_every_band, wider

    bars = wider()
    sessions = S[:30]
    entries = [e if i % 3 else said(e.ticker, e.timestamp.date(), bias=e.bias or "NEUTRAL",
                                    conviction=e.conviction or 0.5, technicals=UP,
                                    live_record={"price": 100.0})
               for i, e in enumerate(journal_with_every_band(sessions))]
    funds, checks = shadow_run.run_funds(entries, sessions[0], sessions[-1], Walks(bars), random_funds=1,
                                         processes=1, shortable_no=frozenset(), long_bars=bars)
    tests = funds["tests"]
    assert set(tests) >= {"model_by_conviction", "model_sized", "model_same_day", xp.VETO, xp.TIMING, xp.LIMIT}
    for name in ("model_by_conviction", "model_sized", xp.LIMIT):
        assert isinstance(tests[name]["acted"], int)
    assert tests[xp.LIMIT]["orders"]["placed"] > 0
    json.dumps(funds, allow_nan=False)
