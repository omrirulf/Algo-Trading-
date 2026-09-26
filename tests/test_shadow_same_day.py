"""The owner's decisions of 26 Sep 2026 on the shadow funds.

* The exploratory fund ``model_same_day``: each line entered on its own
  session, at the price recorded when its signal was made, after that
  session's stops; lines with no usable price, or recorded outside regular
  hours, not entered and counted.
* Every other fund's output byte-identical with and without it (hashes
  recorded from the code before the change, ``tests/shadow_golden.py``).
* Short refusals dated: never backwards.
* The fund test's fixed start (the 28 Sep cycle, from the 29 Sep open), and
  the hard gate: nothing about a fund is computed before calibration passes.
* The price source's gaps per month, the held names per day, and the health
  check's warning above 2%.
* The fund test's bars by an O'Brien-Fleming-type spending rule; the race's
  bars untouched.
"""

from __future__ import annotations

import json
import sys
from datetime import date, datetime, timedelta, timezone
from types import SimpleNamespace

import pandas as pd
import pytest

from analysis import decision_gate as gate
from analysis.reader import JournalEntry
from shadow import run as shadow_run
from shadow import schedule
from shadow.broker import DEFAULT_COST_PER_SIDE, ENTRY, STOP
from shadow.fund import (
    NO_PRICE,
    OTHER_DAY,
    OUTSIDE_HOURS,
    SAME_DAY,
    Fund,
    cycle_days,
    lines_by_day,
    model_signal,
    recorded_fill,
    refusal_days,
    refused_by,
    run,
)
from shadow.market import Bars, SimFeed, in_regular_hours
from tests.shadow_golden import REFUSED, SESSIONS, golden_parts
from tests.test_shadow_fund import S, flat, said

# --------------------------------------------------------------------------- #
# Every other fund is exactly what it was
# --------------------------------------------------------------------------- #

#: sha256 of each part of the funds document, from ``golden_parts()`` run on
#: the code before this change (commit dc9fe11), where the list held the four
#: and the two earlier exploratory funds -- on Python 3.11. Float arithmetic
#: is not bit-identical across Python versions (3.12 made ``sum()`` of floats
#: compensated, which moves the last digits of some sums), so these recorded
#: hashes are checked on 3.11 only; on every version the same property is
#: also shown in-process, with and without the new fund, below.
BEFORE = {
    "row:model": "124c8a7cbedf03bf5fbb4ab8b7d2edba7675cd538b5761ebd80e3c298e481a59",
    "row:momentum": "d0a71e397f5f48a16e606b7a7d241bffbdb40b8c62198d210377b18f71b4cb93",
    "row:hybrid": "8347889692892b8cfb94d762245537be9a2a331082d9535aad1965db92632352",
    "row:vt": "e1d9476cddd6a9ccf7562331f01841a0157df1b46dde8d997ccc68a876456865",
    "row:model_by_conviction": "65beb8e2e7440efaa9698347a4a4fe2ae336687d981badce574e6ec31ebe89d8",
    "row:model_sized": "5097b3de53b87422dd5725b49ae0842788972595e661afb91522c01f7bc21d11",
    "days": "225bb666697cfc15702b9c16bcd248f1ea0b74f0221fe61d38ad40dd79697760",
    "start": "3c4c54d6835358d7e8b1691acdf90d00f5e8c6ef02039a8bb65c632773c49a4f",
    "band": "87a0cf5599494c2bda989bd011bea2ce53bc7fded5403db4eca1043dd0d3cd5d",
    "checks:coin": "0ec3ed3ece4fd4004dd757abcbd8d5abc85fef74a4b5704e0f7e5fa738fcfaf4",
}


@pytest.mark.skipif(sys.version_info[:2] != (3, 11),
                    reason="the recorded hashes are from Python 3.11 (see BEFORE); "
                           "the in-process test below covers every version")
def test_every_other_fund_is_byte_identical_to_the_code_before_the_change():
    """Same journal (with recorded prices of every kind), same prices, same
    refusals: every row that existed before, the days, the band and the
    coin-flip funds' check hash exactly as they did on the code before the
    change. The one new row is the same-day fund's."""
    after = golden_parts()
    assert {k: v for k, v in after.items() if k in BEFORE} == BEFORE
    assert set(after) - set(BEFORE) == {"row:model_same_day"}


def test_adding_the_same_day_fund_changes_no_other_part():
    """On any Python: the funds document with the same-day fund and without
    it are identical in every other part."""
    with_it, without = golden_parts(), golden_parts(without_same_day=True)
    assert set(with_it) - set(without) == {"row:model_same_day"}
    assert {k: v for k, v in with_it.items() if k in without} == without


def test_dated_refusals_all_before_the_start_are_the_undated_ones():
    """The refusals as ``not_shortable`` now reads them -- dated -- change
    nothing for a cycle after every one of them (compared in-process, so on
    any Python)."""
    dated = {name: SESSIONS[0] - timedelta(days=3) for name in REFUSED}
    assert golden_parts(dated) == golden_parts()


# --------------------------------------------------------------------------- #
# model_same_day
# --------------------------------------------------------------------------- #


def live(day: date, *, price=100.5, bid=100.4, ask=100.6, hour=15, minute=0, **extra) -> dict:
    asked = datetime(day.year, day.month, day.day, hour, minute, 5, tzinfo=timezone.utc).isoformat()
    return {"price": price, "bid": bid, "ask": ask, "quote_at": asked, "asked_at": asked,
            "source": "alpaca-iex"} | extra


def same_day_run(entries, bars, sessions, **kw):
    feed = SimFeed(bars)
    fund = Fund("model_same_day", model_signal, feed, bars, entry=SAME_DAY, keep_actions=True, **kw)
    run([fund], sessions, lines_by_day(entries), cycle_days(entries), feed)
    return fund


def entries_of(fund, kind=ENTRY):
    return [f for f in fund.broker.fills if f.kind == kind]


def test_a_buy_fills_at_the_recorded_ask_and_a_short_at_the_recorded_bid_on_the_lines_own_day():
    bars = Bars({"MSFT": flat(100.0), "JPM": flat(50.0), "VT": flat(100.0)})
    entries = [said("MSFT", S[1], "BULLISH", 0.6, live_record=live(S[1], price=101.0, bid=100.9, ask=101.1)),
               said("JPM", S[1], "BEARISH", 0.6, live_record=live(S[1], price=50.5, bid=50.4, ask=50.6))]
    fund = same_day_run(entries, bars, S[:3])

    fills = {f.ticker: f for f in entries_of(fund)}
    assert set(fills) == {"MSFT", "JPM"}
    assert (fills["MSFT"].day, fills["MSFT"].side, fills["MSFT"].price) == (S[1], "buy", 101.1)
    assert (fills["JPM"].day, fills["JPM"].side, fills["JPM"].price) == (S[1], "sell", 50.4)
    for f in fills.values():                                            # the same 0.10% a side
        assert f.cost == pytest.approx(f.qty * f.price * DEFAULT_COST_PER_SIDE)
    # Sized by the production engine on the recorded price, under the 5% cap.
    assert fills["MSFT"].qty == int(100_000 * 0.05 / 101.1)
    assert fund.not_entered == {}
    # Marked at the close of its own day.
    assert fund.days[1].positions == 2 and fund.days[0].positions == 0


def test_without_a_quote_the_recorded_last_trade_is_used():
    bars = Bars({"MSFT": flat(100.0), "VT": flat(100.0)})
    entries = [said("MSFT", S[1], "BULLISH", 0.6, live_record=live(S[1], price=101.0, bid=None, ask=None))]
    fund = same_day_run(entries, bars, S[:3])
    assert [f.price for f in entries_of(fund)] == [101.0]


def test_the_entry_comes_after_the_days_stops_so_its_own_stop_is_first_checked_at_the_next_open():
    """S[1]'s low would reach the new position's stop, but the entry is made
    after that session's stop checks; at S[2] the price opens through it,
    and it fills at that open."""
    bars = Bars({"MSFT": flat(100.0, {1: {"Low": 80.0}, 2: {"Open": 85.0, "Low": 84.0}}), "VT": flat(100.0)})
    entries = [said("MSFT", S[1], "BULLISH", 0.6, live_record=live(S[1], price=100.0, bid=99.9, ask=100.1))]
    fund = same_day_run(entries, bars, S[:4])

    assert [f.day for f in entries_of(fund)] == [S[1]]
    stops = entries_of(fund, STOP)
    assert [(s.day, s.price, s.gapped) for s in stops] == [(S[2], 85.0, True)]


def test_a_position_already_held_has_its_stops_checked_before_the_days_entries():
    """A position entered on S[1] is stopped out during S[2]; the S[2] line
    for the same name is entered after that, at its recorded price."""
    bars = Bars({"MSFT": flat(100.0, {2: {"Low": 80.0}}), "VT": flat(100.0)})
    entries = [said("MSFT", S[1], "BULLISH", 0.6, live_record=live(S[1], price=100.0, bid=99.9, ask=100.1)),
               said("MSFT", S[2], "BULLISH", 0.6, live_record=live(S[2], price=95.0, bid=94.9, ask=95.1))]
    fund = same_day_run(entries, bars, S[:3])
    kinds = [(f.day, f.kind) for f in fund.broker.fills]
    assert kinds == [(S[1], ENTRY), (S[2], STOP), (S[2], ENTRY)]
    assert entries_of(fund)[1].price == 95.1


def test_lines_with_no_usable_price_or_outside_hours_are_not_entered_and_counted():
    bars = Bars({t: flat(100.0) for t in ("MSFT", "NVDA", "JPM", "XOM", "RSP", "IWM", "TLT", "VT")})
    day = S[1]
    entries = [
        said("MSFT", day, "BULLISH", 0.6),                                                   # no record at all
        said("NVDA", day, "BULLISH", 0.6, live_record=live(day, price=None, bid=None, ask=None,
                                                             error="timed out")),
        said("JPM", day, "BULLISH", 0.6, live_record=live(day, hour=21, minute=30)),        # after the close
        said("XOM", day, "BULLISH", 0.6, live_record=live(day, hour=13, minute=0)),         # before the open
        said("RSP", day, "BULLISH", 0.6, live_record=live(day - timedelta(days=1))),        # another day
        said("IWM", day, "NEUTRAL", 0.2),                                                   # never entered anyway
        said("TLT", day, "BULLISH", 0.6, live_record=live(day, bid=None, ask=0.0, price=-1)),
    ]
    fund = same_day_run(entries, bars, S[:3])
    assert entries_of(fund) == []
    assert fund.not_entered == {NO_PRICE: 3, OUTSIDE_HOURS: 2, OTHER_DAY: 1}
    skipped = {d.ticker: d.reason for d in fund.decisions if d.status == "SKIPPED"}
    assert skipped == {"MSFT": NO_PRICE, "NVDA": NO_PRICE, "TLT": NO_PRICE, "JPM": OUTSIDE_HOURS,
                       "XOM": OUTSIDE_HOURS, "RSP": OTHER_DAY}

    row = shadow_run.summarise_exploratory(fund, fund, None)
    assert row["not_entered"] == {"no_price": 3, "outside_hours": 2, "other_day": 1, "total": 6}


def test_regular_hours_follow_the_market_calendar_half_days_included():
    """09:30 to 16:00 New York, 13:00 on a half day (27 Nov 2026), nothing on a holiday."""
    def at(y, m, d, hh, mm):
        return datetime(y, m, d, hh, mm, tzinfo=timezone.utc)

    assert in_regular_hours(at(2026, 11, 27, 17, 59))                  # 12:59 New York, a half day
    assert not in_regular_hours(at(2026, 11, 27, 18, 0))               # 13:00: shut
    assert in_regular_hours(at(2026, 11, 30, 20, 59))                  # 15:59 on a full day (EST)
    assert not in_regular_hours(at(2026, 11, 26, 16, 0))               # Thanksgiving
    assert not in_regular_hours(at(2026, 9, 28, 13, 29))               # 09:29 EDT
    entry = JournalEntry(ticker="MSFT", timestamp=at(2026, 11, 27, 17, 0),
                         live_record={"price": 10.0, "asked_at": "2026-11-27T18:10:00Z"})
    assert recorded_fill(entry, "buy", date(2026, 11, 27)) == (None, OUTSIDE_HOURS)
    entry = JournalEntry(ticker="MSFT", timestamp=at(2026, 11, 27, 17, 0),
                         live_record={"price": 10.0, "asked_at": "2026-11-27T17:10:00Z"})
    assert recorded_fill(entry, "buy", date(2026, 11, 27)) == (10.0, None)


def test_the_same_day_fund_manages_at_the_next_open_as_the_model_fund():
    """The manager runs at the open of the session after a cycle, for both;
    only the entries move. With nothing to enter at the open, a same-day
    fund's session on a day with no own cycle is stops and marks only."""
    import inspect

    from shadow.fund import IndexFund

    assert inspect.signature(Fund.session).parameters["today"].default is None
    assert "today" not in inspect.signature(IndexFund.session).parameters
    bars = Bars({"MSFT": flat(100.0), "VT": flat(100.0)})
    feed = SimFeed(bars)
    fund = Fund("x", model_signal, feed, bars, entry=SAME_DAY)
    calls = []
    fund._manage = lambda: calls.append(fund.broker.day)
    entries = [said("MSFT", S[1], "BULLISH", 0.6, live_record=live(S[1]))]
    run([fund], S[:4], lines_by_day(entries), cycle_days(entries), feed)
    assert calls == [S[2]]


def test_the_same_day_fund_is_refused_bad_settings():
    bars = Bars({"MSFT": flat(100.0)})
    feed = SimFeed(bars)
    with pytest.raises(ValueError):
        Fund("x", model_signal, feed, bars, entry="tomorrow")
    with pytest.raises(ValueError):
        Fund("x", model_signal, feed, bars, entry=SAME_DAY, priority="conviction")


# --------------------------------------------------------------------------- #
# Short refusals, dated
# --------------------------------------------------------------------------- #


def refused_run(refusals, line_day):
    bars = Bars({"JPM": flat(50.0), "VT": flat(100.0)})
    feed = SimFeed(bars)
    fund = Fund("model", model_signal, feed, bars, not_shortable=refusals, keep_actions=True)
    entries = [said("JPM", line_day, "BEARISH", 0.6)]
    run([fund], [d for d in S[:6] if d > line_day][:2], lines_by_day(entries), cycle_days(entries), feed,
        previous=line_day)
    return [(d.status, d.reason) for d in fund.decisions]


def test_a_refusal_counts_from_its_own_day_never_backwards():
    day = S[2]
    later = refused_run({"JPM": S[3]}, day)                        # refused the day after the cycle
    assert [s for s, _ in later] == ["ACCEPTED"]
    same = refused_run({"JPM": day}, day)                          # refused on the cycle's own day
    assert same[0][0] == "ERROR" and "cannot be sold short" in same[0][1]
    earlier = refused_run({"JPM": S[0]}, day)
    assert earlier[0][0] == "ERROR"
    undated = refused_run(frozenset({"JPM"}), day)                 # a plain set: from the start
    assert undated[0][0] == "ERROR"


def test_refusal_helpers():
    assert refusal_days(frozenset({"lqd"})) == {"LQD": date.min}
    assert refusal_days({"lqd": date(2026, 9, 16)}) == {"LQD": date(2026, 9, 16)}
    days = {"LQD": date(2026, 9, 16), "USO": date(2026, 9, 22)}
    assert refused_by(days, date(2026, 9, 21)) == frozenset({"LQD"})
    assert refused_by(days, date(2026, 9, 22)) == frozenset({"LQD", "USO"})
    assert refused_by(days, date(2026, 9, 15)) == frozenset()


def test_the_calibration_copy_takes_the_dated_refusals_too():
    """It mirrors the real account, which could not know a refusal before it happened either."""
    from shadow import calibration as calib

    bars = Bars({"VT": flat(100.0)})
    seed = calib.Seed(S[0], datetime(2026, 4, 13, 20, 30, tzinfo=timezone.utc), 100_000.0, (), ())
    fund = calib.seed_fund(seed, SimFeed(bars), bars, [], {"LQD": date(2026, 9, 16)})
    assert fund.refused_on == {"LQD": date(2026, 9, 16)}


# --------------------------------------------------------------------------- #
# The fixed start, and the hard gate
# --------------------------------------------------------------------------- #


def test_the_first_session_acts_on_the_first_cycle():
    bars = Bars({"MSFT": flat(100.0), "VT": flat(100.0)})
    entries = [said("MSFT", S[0], "BULLISH", 0.6)]
    cycles, ran = lines_by_day(entries), cycle_days(entries)
    for previous, bought in ((S[0], 1), (None, 0)):
        feed = SimFeed(bars)
        fund = Fund("model", model_signal, feed, bars)
        run([fund], S[1:3], cycles, ran, feed, previous)
        assert len(entries_of(fund)) == bought
        if bought:
            assert entries_of(fund)[0].day == S[1] and entries_of(fund)[0].price == 100.0


class NoPrices:
    """An ``OhlcFetcher`` stand-in with no bar at all: no network."""

    def __init__(self, **kw):
        pass

    def ohlc(self, ticker, start, end):
        return pd.DataFrame()


FUND_WORDS = ("equity", "total_return", "vs_model", "vs_vt", "band", "max_drawdown", "win_rate", "sides",
              "not_entered", "open_positions", "cash", "trades")


def keys_of(value) -> set:
    if isinstance(value, dict):
        return set(value) | {k for v in value.values() for k in keys_of(v)}
    if isinstance(value, list):
        return {k for v in value for k in keys_of(v)}
    return set()


@pytest.mark.parametrize("status", ["not_started", "running", "failed", "stopped"])
def test_no_fund_number_exists_before_calibration_passes(monkeypatch, tmp_path, status):
    """The owner's hard gate: the fund start is fixed, but until calibration's
    verdict is a pass no fund is built, nothing is computed for one, and the
    document carries no fund number anywhere."""
    from shadow import calibration as calib
    from shadow import fund as fund_module

    if status == "not_started":
        monkeypatch.setattr(schedule, "CALIBRATION_START", None)
    else:
        monkeypatch.setattr(schedule, "CALIBRATION_START", date(2026, 9, 28))
        monkeypatch.setattr(calib, "calibration_report", lambda **kw: {"status": status, "series": []})

    def never(*a, **kw):
        raise AssertionError("a fund was computed before calibration passed")

    monkeypatch.setattr(shadow_run, "run_funds", never)
    monkeypatch.setattr(fund_module.Fund, "__init__", never)
    monkeypatch.setattr(fund_module.IndexFund, "__init__", never)
    monkeypatch.setattr(shadow_run, "OhlcFetcher", NoPrices)
    journal = tmp_path / "journal"
    journal.mkdir()
    (journal / "2026-10.log").write_text(json.dumps({
        "ts_utc": "2026-10-05T15:00:00+00:00", "ticker": "MSFT", "held": True}) + "\n")
    args = SimpleNamespace(journal=journal, audit=tmp_path / "audit.log", account=tmp_path / "account.jsonl",
                           random=3, processes=1)
    out = shadow_run.build(args, datetime(2026, 10, 20, 23, 0, tzinfo=timezone.utc))

    assert out["funds"] is None and out["integrity"] is None
    assert out["fund_test"]["status"] == "not_started" and out["fund_test"]["sessions"] == 0
    assert out["fund_test"]["start"] == "2026-09-29" and out["fund_test"]["first_cycle"] == "2026-09-28"
    assert out["fund_test"]["waiting_for"] == "calibration"
    assert not keys_of(out) & set(FUND_WORDS), keys_of(out) & set(FUND_WORDS)
    assert set(out["order_matters"]) == {"real"}                     # the real account's own record only
    # What is there is not a fund result: the price source's gaps and the held names.
    assert out["price_gaps"]["from"] == "2026-09-29" and out["price_gaps"]["months"]
    json.dumps(out, allow_nan=False)


def test_once_calibration_passes_every_fund_runs_from_the_fixed_start(monkeypatch, tmp_path):
    from shadow import calibration as calib

    monkeypatch.setattr(schedule, "CALIBRATION_START", date(2026, 9, 28))
    monkeypatch.setattr(calib, "calibration_report", lambda **kw: {"status": "passed"})
    monkeypatch.setattr(shadow_run, "OhlcFetcher", NoPrices)
    asked = {}

    def fake(entries, start, final_through, fetcher, **kw):
        asked.update(kw, start=start, final_through=final_through)
        return {"start": start.isoformat(), "days": [], "list": [], "band": {}}, {"four": {}, "coin": {}}

    monkeypatch.setattr(shadow_run, "run_funds", fake)
    journal = tmp_path / "journal"
    journal.mkdir()
    (journal / "2026-10.log").write_text("")
    args = SimpleNamespace(journal=journal, audit=tmp_path / "audit.log", account=tmp_path / "account.jsonl",
                           random=3, processes=1)
    out = shadow_run.build(args, datetime(2026, 10, 20, 23, 0, tzinfo=timezone.utc))
    assert asked["start"] == date(2026, 9, 29) and asked["first_cycle"] == date(2026, 9, 28)
    assert out["fund_test"]["status"] == "running" and out["fund_test"]["waiting_for"] is None


def test_the_smoke_never_runs_a_session_of_the_sample_before_calibration_passes():
    from shadow import smoke

    assert smoke.gated_through(date(2026, 10, 20), False) == date(2026, 9, 28)
    assert smoke.gated_through(date(2026, 10, 20), True) == date(2026, 10, 20)
    assert smoke.gated_through(date(2026, 9, 25), False) == date(2026, 9, 25)
    assert smoke.calibration_passed(json.dumps({"calibration": {"status": "passed"}}))
    for record in (json.dumps({"calibration": {"status": "running"}}), "junk", None, "[]"):
        assert not smoke.calibration_passed(record)


# --------------------------------------------------------------------------- #
# Price gaps and held names
# --------------------------------------------------------------------------- #


class Gappy:
    """Bars every trading day from 1 Sep to 30 Oct 2026, less the given (ticker, day) pairs."""

    def __init__(self, missing):
        self.missing = missing

    def ohlc(self, ticker, start, end):
        days = [d for d in pd.bdate_range("2026-09-01", "2026-10-30") if (ticker, d.date()) not in self.missing]
        return pd.DataFrame({"Open": 10.0, "High": 11.0, "Low": 9.0, "Close": 10.0, "Dividends": 0.0},
                            index=pd.DatetimeIndex(days))


def test_the_share_of_missing_ticker_days_is_counted_per_month():
    missing = {("AAA", date(2026, 9, 29)), ("BBB", date(2026, 9, 29)), ("AAA", date(2026, 10, 5))}
    got = shadow_run.price_gaps(Gappy(missing), date(2026, 9, 29), date(2026, 10, 9), tickers=("AAA", "BBB"))
    assert got["tickers"] == 2 and got["limit"] == 0.02
    sep, oct_ = got["months"]
    assert (sep["month"], sep["sessions"], sep["missing"]) == ("2026-09", 2, 2)
    assert sep["share"] == pytest.approx(2 / 4) and sep["over"] is True
    assert sep["by_day"] == {"2026-09-29": 2}
    assert (oct_["month"], oct_["sessions"], oct_["missing"]) == ("2026-10", 7, 1)
    assert oct_["share"] == pytest.approx(1 / 14)
    clean = shadow_run.price_gaps(Gappy(set()), date(2026, 9, 29), date(2026, 10, 9), tickers=("AAA",))
    assert [m["missing"] for m in clean["months"]] == [0, 0] and not any(m["over"] for m in clean["months"])
    assert shadow_run.price_gaps(Gappy(set()), date(2026, 9, 29), date(2026, 9, 28))["months"] == []


def test_the_held_names_are_counted_per_cycle_day():
    def line(day, ticker, held, hour=15):
        return JournalEntry(ticker=ticker, timestamp=datetime(2026, 9, day, hour, 0, tzinfo=timezone.utc),
                            held=held)

    entries = [line(25, "MSFT", True),                                       # before the first cycle
               line(28, "MSFT", True), line(28, "NVDA", True), line(28, "JPM", False),
               line(28, "MSFT", True, hour=17),                               # a second cycle: one name
               line(29, "JPM", False)]
    got = shadow_run.held_names(entries, date(2026, 9, 28))
    assert got == {"from": "2026-09-28", "days": [{"day": "2026-09-28", "names": 2, "lines": 3, "of": 3},
                                                  {"day": "2026-09-29", "names": 0, "lines": 0, "of": 1}]}


def test_the_health_check_warns_above_two_percent_in_the_latest_month():
    from analysis import health
    from config.settings import MAX_PRICE_GAP_SHARE

    assert MAX_PRICE_GAP_SHARE == 0.02

    def record(*months):
        return {"final_through": "2026-10-09", "price_gaps": {"tickers": 80, "months": list(months)}}

    over = {"month": "2026-10", "sessions": 7, "missing": 12, "share": 12 / 560}
    at = {"month": "2026-10", "sessions": 5, "missing": 8, "share": 0.02}
    old = {"month": "2026-09", "sessions": 2, "missing": 27, "share": 27 / 160}

    alarm = health.price_gaps(record(old, over))
    assert alarm is not None and alarm.severity == health.WARNING
    assert "2026-10" in alarm.title and "2.1%" in alarm.title
    assert "12 of 560 ticker-days" in alarm.detail and "2%" in alarm.detail
    assert health.price_gaps(record(old, at)) is None                      # exactly 2% is not above it
    assert health.price_gaps(record(at, old)) is None                      # the latest month is October
    only_old = health.price_gaps(record(old))
    assert only_old is not None and "2026-09" in only_old.title
    for junk in (None, {}, {"price_gaps": None}, {"price_gaps": {"months": "x"}},
                 {"price_gaps": {"months": [{"month": 5}]}}):
        assert health.price_gaps(junk) is None


def test_the_health_check_reads_the_funds_record_for_it(tmp_path):
    from analysis import health

    journal = tmp_path / "journal"
    journal.mkdir()
    (tmp_path / "funds.json").write_text(json.dumps({"price_gaps": {"tickers": 80, "months": [
        {"month": "2026-10", "sessions": 5, "missing": 40, "share": 0.1}]}}))
    alarms = health.check(journal, tmp_path / "audit.log", date(2026, 10, 7), token_expires=None)
    assert any(a.title.startswith("Price gaps: 10.0% of ticker-days missing in 2026-10") for a in alarms)


# --------------------------------------------------------------------------- #
# The spending rule
# --------------------------------------------------------------------------- #


def test_the_spending_rules_reference_values():
    for shares, want in (((45 / 165, 105 / 165, 1.0), [3.753, 2.459, 2.007]),
                         ((46 / 166, 106 / 166, 1.0), [3.723, 2.455, 2.008]),
                         ((1 / 3, 2 / 3, 1.0), [3.395, 2.407, 2.015])):
        assert [round(b, 3) for b in gate.spending_bars(shares)] == want
    # The first bar is the normal quantile of what may be spent by then.
    assert gate.spending_bars([0.25])[0] == pytest.approx(1.959964 / 0.5, abs=1e-4)
    assert gate.spent_by(1.0) == gate.spent_by(1.3) == 0.05 and gate.spent_by(0.0) == 0.0


def test_bars_already_used_never_change():
    bars = gate.spending_bars([1 / 3, 2 / 3, 1.0], used=[3.40])
    assert bars[0] == 3.40
    total = gate._crossing(bars, [1 / 3, 2 / 3, 1.0], 1001)
    assert total == pytest.approx(0.05, abs=1e-6)
    with pytest.raises(ValueError):
        gate.spending_bars([0.5, 0.4])
    with pytest.raises(ValueError):
        gate.spending_bars([0.5], used=[3.0, 2.0])


def test_the_races_bars_are_untouched():
    assert gate.CHECKPOINTS == ((20, 3.47), (40, 2.45), (60, 2.00))
    assert [round(b, 2) for b in gate.obrien_fleming_bars([1, 2, 3])] == [3.47, 2.45, 2.00]


# --------------------------------------------------------------------------- #
# The pre-registration's sections 11 and 12 say what the code does
# --------------------------------------------------------------------------- #


def test_the_fund_test_sections_name_the_numbers_the_code_runs():
    from pathlib import Path

    from config.settings import MAX_PRICE_GAP_SHARE

    raw = (Path(__file__).resolve().parents[1] / "docs" / "horse-race-preregistration.md").read_text()
    body, _, amendments = raw.partition("## Amendments")
    text = " ".join(body.split())
    # The sections, in order, after section 10 and before the Amendments table.
    heads = [line for line in body.splitlines() if line.startswith("## ")]
    assert heads[-3:] == ["## 10. Model watch (Amendment 2026-09-24; operational, not a decision rule)",
                          "## 11. The fund test (Amendment 2026-09-24)",
                          "## 12. Calibration (before the fund test counts)"]
    assert "draft" not in heads[-2] and "Amendments rows this section would add" not in raw
    # The start, the gate, the looks and the bars.
    assert (schedule.FUND_FIRST_CYCLE, schedule.FUND_START) == (date(2026, 9, 28), date(2026, 9, 29))
    assert "The funds act on the cycle journalled on **Monday 2026-09-28**" in text
    assert "the first fund session is **2026-09-29**" in text
    assert "The fund test still **counts only after calibration passes** (section 12)." in text
    assert schedule.FUND_TEST_PLANNED_SESSIONS == (60, 120, 180) and "**60, 120 and 180** fund sessions" in text
    for look, n, exact, bar in zip(("2026-12-22", "2027-03-22", "2027-06-16"), schedule.FUND_TEST_PLANNED_SESSIONS,
                                   ("3.395", "2.407", "2.015"), schedule.FUND_TEST_BARS):
        assert f"(≈ {look}) | {n} |" in text and f"| {exact} | **{bar:.2f}** |" in text
    assert "α(t) = 2 − 2Φ(1.96 / √t)" in text and "`analysis.decision_gate.spending_bars`" in text
    assert "the planned final sessions (180)" in text
    # The exploratory funds, the lag, the gaps, the refusals.
    for name in shadow_run.EXPLORATORY_FUNDS:
        assert f"| `{name}` (exploratory) |" in text
    assert shadow_run.VS_MODEL_LAG == 5 and "**Lag 5**" in text
    assert MAX_PRICE_GAP_SHARE == 0.02 and "If a month's share goes above 2%" in text
    assert "blocked only by refusals recorded on day D or earlier" in text
    assert "The number of names skipped for this reason is reported every day" in text
    # The two rows, dated the day they were committed, in order.
    rows = [r for r in amendments.splitlines() if r.startswith("| 20")]
    fund_test = [r for r in rows if "| **Fund test** (new registration) |" in r]
    start = [r for r in rows if "| **Fund test start: 2026-09-28**" in r]
    assert len(fund_test) == len(start) == 1
    assert fund_test[0][2:12] == start[0][2:12] >= "2026-09-26"
    assert rows.index(fund_test[0]) + 1 == rows.index(start[0]) == len(rows) - 1
    assert [r[2:12] for r in rows] == sorted(r[2:12] for r in rows)
