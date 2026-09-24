"""How often the buying order mattered: the owner's report of 24 Sep 2026. Report only."""

from __future__ import annotations

import json
from datetime import date

import pytest

from shadow import order_matters as om
from shadow.fund import cycle_days, lines_by_day, model_signal, run
from shadow.market import SimFeed
from tests.test_shadow_fund import S, CheckedFund, journal, universe


@pytest.mark.parametrize("reason, kind", [
    ("no room under the sleeve budget limit", om.SLEEVE),
    ("no room under the gross exposure limit", om.GROSS),
    ("no room under the 'Duration' group limit", om.GROUP),
    ("no room under the stock-market (by beta) limit", om.STOCK_MARKET),
    ("already holding 40 positions (max 40)", om.POSITIONS),
    ('BrokerError: submit_order failed for XOM: {"message":"insufficient buying power"}', om.CASH),
    # The group had 80 left, less than one share of TIP; the ticker's own 12%
    # cap had 11,994 -- the group bound it, so the order it came in mattered.
    ("no room for broad fund TIP under its 12% cap or the 'Duration' group limit: equity 99951.23, "
     "price 108.26, existing exposure 0.00, headroom 80.17", om.GROUP),
])
def test_a_portfolio_limit_is_running_out_of_room(reason, kind):
    assert om.capacity_kind(reason) == kind


@pytest.mark.parametrize("reason", [
    # The real log: NVDA already held above its own 5% cap; the sleeve had
    # room. No buying order would have changed this.
    "no room for equity NVDA under its 5% cap or the sleeve budget limit: equity 99515.68, price 219.10, "
    "existing exposure 5039.41, headroom 10238.75",
    # The real log, 18 Sep IEF: its own 12% cap left 79.58, under one share at
    # 90.84, so it was refused whatever the sleeve had (61.06).
    "no room for broad fund IEF under its 12% cap or the sleeve budget limit: equity 99830.14, price 90.84, "
    "existing exposure 11900.04, headroom 61.06",
    "bias is NEUTRAL; no trade",
    "conviction 0.10 below minimum 0.30",
    'BrokerError: submit_order failed for LQD: {"message":"asset \\"LQD\\" cannot be sold short"}',
    "",
])
def test_anything_else_is_not(reason):
    assert om.capacity_kind(reason) is None


def test_a_day_says_what_was_skipped_and_whether_it_outranked_a_purchase():
    d1, d2, d3 = date(2026, 9, 22), date(2026, 9, 23), date(2026, 9, 24)
    events = [
        om.Event(d1, "KRE", 0.32, "ACCEPTED", "submitted"),
        om.Event(d1, "EWT", 0.35, "ACCEPTED", "submitted"),
        om.Event(d1, "ASML", 0.55, "REJECTED", "no room under the sleeve budget limit"),
        om.Event(d2, "XOM", 0.68, "ACCEPTED", "submitted"),
        om.Event(d2, "IGV", 0.45, "REJECTED", "no room under the gross exposure limit"),
        om.Event(d2, "TIP", 0.60, "ACCEPTED", "submitted"),
        om.Event(d2, "TIP", 0.70, "REJECTED", "no room under the 'Duration' group limit"),   # bought: not skipped
        om.Event(d3, "JPM", 0.55, "ACCEPTED", "submitted"),                                  # room all day
    ]
    days, cycles = om.order_days(events)
    assert cycles == 3 and [d.day for d in days] == [d1, d2]
    (asml,) = days[0].skipped
    assert (asml.ticker, asml.conviction, asml.kind, asml.outranks) == ("ASML", 0.55, om.SLEEVE, ("KRE", "EWT"))
    assert [s.ticker for s in days[1].skipped] == ["IGV"]              # TIP was bought that day
    out = om.summary(days, cycles)
    assert (out["cycle_days"], out["days"], out["skipped"], out["outranked_days"]) == (3, 2, 2, 1)
    assert out["by_kind"] == {om.GROSS: 1, om.SLEEVE: 1}
    assert out["list"][0] == {"day": "2026-09-22",
                              "bought": [{"ticker": "KRE", "conviction": 0.32}, {"ticker": "EWT", "conviction": 0.35}],
                              "skipped": [{"ticker": "ASML", "conviction": 0.55, "kind": om.SLEEVE,
                                           "outranks": ["KRE", "EWT"]}]}
    json.dumps(out)


def test_the_real_account_is_read_from_its_own_audit_log():
    def audit(ts, ticker, conviction, status, reason):
        return json.dumps({"signal": {"ticker": ticker, "bias": "BULLISH", "conviction": conviction},
                           "result": {"status": status, "ticker": ticker, "reason": reason},
                           "ts": ts, "level": "INFO", "event": "signal_processed"})
    lines = [
        audit("2026-09-23 16:20:00,000", "XOM", 0.68, "ACCEPTED", "submitted buy 10 XOM"),
        audit("2026-09-23 16:20:05,000", "ARGT", 0.60, "REJECTED", "no room under the gross exposure limit"),
        audit("2026-09-24 16:20:00,000", "JPM", 0.55, "REJECTED", "bias is NEUTRAL; no trade"),
        json.dumps({"action": {"ticker": "XOM", "action": "held"}, "ts": "2026-09-24 15:00:00,000",
                    "event": "position_managed"}),
        "not json",
    ]
    out = om.real_summary(lines)
    assert (out["cycle_days"], out["days"], out["outranked_days"]) == (2, 1, 0)
    assert out["list"][0]["skipped"] == [{"ticker": "ARGT", "conviction": 0.6, "kind": om.GROSS, "outranks": []}]


def test_a_fund_keeps_the_same_record_and_changes_nothing():
    """Every name bullish every day fills the book: the fund runs out of room,
    records it, and trades exactly as a fund that is not being watched."""
    bars = universe()
    sessions = S[:30]
    entries = journal(sessions)
    feed = SimFeed(bars)
    f = CheckedFund("model", model_signal, feed, bars, keep_actions=True)
    run([f], sessions, lines_by_day(entries), cycle_days(entries), feed)
    out = om.fund_summary(f)
    assert out["cycle_days"] == f.cycles_dispatched > 0
    assert out["days"] > 0 and out["skipped"] > 0
    capacity = [d for d in f.decisions if om.capacity_kind(d.reason)]
    assert out["skipped"] == len(capacity)
    accepted = sum(1 for d in f.decisions if d.status == "ACCEPTED")
    assert sum(1 for e in f.order_events if e.status == "ACCEPTED") == accepted


def test_the_coin_flip_funds_keep_only_the_days():
    """A thousand funds that are never NEUTRAL meet a limit nearly every day;
    keeping every refusal would hold gigabytes. They keep the count only."""
    bars = universe()
    sessions = S[:20]
    entries = journal(sessions)
    feed = SimFeed(bars)
    detailed = CheckedFund("a", model_signal, feed, bars)
    light = CheckedFund("b", model_signal, feed, bars, order_detail=False)
    run([detailed, light], sessions, lines_by_day(entries), cycle_days(entries), feed)
    assert light.order_events is None
    assert om.fund_summary(light)["days"] == om.fund_summary(detailed)["days"] > 0
    assert [d.equity for d in light.days] == [d.equity for d in detailed.days]
