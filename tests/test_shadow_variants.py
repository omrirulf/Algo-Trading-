"""The two exploratory funds: highest conviction first, and sized by conviction.

The owner's decisions 3 and 4 of 25 Sep 2026. Each is the model fund with
one thing changed -- the buying order, or the size -- so these tests check
that one thing and that nothing else moved: the order within a cycle,
chosen only when watchlist order runs out of room (a refusal or a cut),
tried on a copy of the book that leaves the fund untouched, ties and cycles
and held names; the size factor per conviction band, applied
inside the unchanged production engine and put back after every call; the
portfolio limits still binding; the funds run and reported after the four,
compared with the model fund, without changing the four; and the smoke
check running them. Production, and the calibration copy, are untouched.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict
from datetime import date
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from analysis.horse_race import newey_west_t
from analysis.reader import JournalEntry
from app import risk_engine
from app.schemas import Bias, LLMSignal
from config import settings as cfg
from config.watchlist import DEFAULT_WATCHLIST
from shadow import order_matters as om
from shadow import run as shadow_run
from shadow import smoke
from shadow.broker import ENTRY
from shadow.fund import (
    CONVICTION_FIRST,
    CONVICTION_SIZES,
    STARTING_CASH,
    WATCHLIST_FIRST,
    Day,
    Fund,
    Line,
    by_conviction,
    conviction_factor,
    cycle_days,
    lines_by_day,
    model_signal,
    run,
)
from shadow.market import Bars, SimFeed
from tests.test_shadow_fund import (
    UNIVERSE,
    S,
    CheckedFund,
    _held_on_fills,
    book_before,
    expected_qty,
    flat,
    said,
    sizing_mismatches,
    stamp,
    universe,
    walk,
)

NORMAL = risk_engine.max_position_pct_for


def fund(name: str, bars: Bars, feed: SimFeed, **kw) -> Fund:
    return Fund(name, model_signal, feed, bars, keep_actions=True, **kw)


def one_session(f: Fund, feed: SimFeed, entries: list[JournalEntry]) -> None:
    """The cycle journalled on S[0], acted on at the S[1] open."""
    feed.at_open(S[1])
    f.session(S[1], lines_by_day(entries)[S[0]])


def entries_of(f: Fund) -> list[tuple[str, int]]:
    return [(x.ticker, x.qty) for x in f.broker.fills if x.kind == ENTRY]


# --------------------------------------------------------------------------- #
# The owner's numbers, pinned
# --------------------------------------------------------------------------- #


def test_the_exploratory_funds_are_named_labelled_and_listed_after_the_four():
    from shadow.fund import NEXT_OPEN, SAME_DAY

    assert shadow_run.EXPLORATORY_FUNDS == ("model_by_conviction", "model_sized", "model_same_day")
    assert shadow_run.LABELS["model_by_conviction"] == "Model, highest conviction first"
    assert shadow_run.LABELS["model_sized"] == "Model, sized by conviction"
    assert shadow_run.LABELS["model_same_day"] == "Model, entered the same day"
    assert shadow_run.COMPARE_TO == "model" and shadow_run.VS_MODEL_LAG == 5
    feed = SimFeed(Bars({"MSFT": flat()}))
    funds = shadow_run.exploratory_funds(feed, feed._bars, frozenset({"LQD"}))
    assert [f.name for f in funds] == list(shadow_run.EXPLORATORY_FUNDS)
    by_order, sized, same_day = funds
    assert (by_order.priority, by_order.sized_by_conviction, by_order.entry) == (CONVICTION_FIRST, False, NEXT_OPEN)
    assert (sized.priority, sized.sized_by_conviction, sized.entry) == (WATCHLIST_FIRST, True, NEXT_OPEN)
    assert (same_day.priority, same_day.sized_by_conviction, same_day.entry) == (WATCHLIST_FIRST, False, SAME_DAY)
    for f in funds:                                                 # same cash, costs and refusals
        assert f.broker.cash == STARTING_CASH and f.broker.not_shortable == frozenset({"LQD"})
        assert f.signal_for is model_signal
    # A fund built without saying otherwise -- every other fund, and the
    # calibration copy -- keeps production's order and size.
    plain = Fund("model", model_signal, feed, feed._bars)
    assert (plain.priority, plain.sized_by_conviction, plain.entry) == (WATCHLIST_FIRST, False, NEXT_OPEN)
    assert plain.quotes is None                                     # it reads the feed itself


def test_the_size_factors_are_the_owners_and_cover_everything_the_floor_lets_through():
    assert CONVICTION_SIZES == ((0.30, 0.25), (0.40, 0.5), (0.50, 1.0), (0.60, 1.5))
    # The table starts where the engine's floor does: nothing that reaches
    # sizing is off the table.
    assert cfg.MIN_CONVICTION == CONVICTION_SIZES[0][0] == 0.30


@pytest.mark.parametrize("conviction, factor", [
    (0.30, 0.25), (0.35, 0.25), (0.3999, 0.25),
    (0.40, 0.5), (0.39999999, 0.5), (0.7 - 0.3, 0.5), (0.45, 0.5),
    (0.50, 1.0), (0.59, 1.0),
    (0.60, 1.5), (0.65, 1.5), (0.95, 1.5), (1.0, 1.5),
    (0.29, None), (0.0, None),
])
def test_each_conviction_gets_its_bands_factor_read_at_six_decimals(conviction, factor):
    assert conviction_factor(conviction) == factor


def test_the_largest_cap_times_the_largest_factor_is_still_a_legal_cap():
    """``calculate_position_size`` refuses a cap above 100%: the biggest
    scaled cap must stay under it, for every kind of instrument."""
    largest = max(factor for _, factor in CONVICTION_SIZES)
    caps = (cfg.MAX_POSITION_PCT, cfg.MAX_BROAD_FUND_PCT, cfg.MAX_FOCUSED_FUND_PCT, cfg.MAX_COMMODITY_FUND_PCT)
    assert max(caps) * largest <= 1.0
    assert max(NORMAL(t) for t in DEFAULT_WATCHLIST) * largest <= 1.0


def test_a_fund_refuses_a_buying_order_it_does_not_know():
    bars = Bars({"MSFT": flat()})
    with pytest.raises(ValueError, match="priority"):
        Fund("x", model_signal, SimFeed(bars), bars, priority="alphabetical")


# --------------------------------------------------------------------------- #
# Fund 5: highest conviction first
# --------------------------------------------------------------------------- #

#: Six Technology names, more than the group's 25% can hold (the setting of
#: test_shadow_fund's priority test), with the lowest conviction first in
#: the watchlist and the highest last.
TECH = {"MSFT": 0.35, "NVDA": 0.5, "XLK": 0.5, "XLC": 0.5, "SMH": 0.7, "IGV": 0.9}


def test_highest_conviction_first_changes_who_gets_the_room_and_keeps_ties_in_watchlist_order():
    """In watchlist order MSFT, NVDA, XLK, XLC and a sliver of SMH take the
    room and IGV -- the model's surest -- is refused. By conviction IGV and SMH go first,
    the three at 0.5 follow in watchlist order (NVDA, XLK, XLC), and MSFT,
    the least sure, is the one left out. Every size is still the engine's,
    on the book as it stood just before it."""
    bars = Bars({t: flat() for t in TECH})
    feed = SimFeed(bars)
    entries = [said(t, S[0], conviction=c) for t, c in TECH.items()]
    model, by_order = fund("model", bars, feed), fund("model_by_conviction", bars, feed, priority=CONVICTION_FIRST)
    feed.at_open(S[1])
    cycle = lines_by_day(entries)[S[0]]
    model.session(S[1], cycle)
    by_order.session(S[1], cycle)

    assert [x.ticker for x in model.decisions] == ["MSFT", "NVDA", "XLK", "XLC", "SMH", "IGV"]
    assert [x.ticker for x in by_order.decisions] == ["IGV", "SMH", "NVDA", "XLK", "XLC", "MSFT"]
    assert [t for t, _ in entries_of(model)] == ["MSFT", "NVDA", "XLK", "XLC", "SMH"]
    assert [t for t, _ in entries_of(by_order)] == ["IGV", "SMH", "NVDA", "XLK"]
    refused = {x.ticker: x.reason for x in by_order.decisions if x.status != "ACCEPTED"}
    assert set(refused) == {"XLC", "MSFT"}
    assert all("'Technology' group" in reason for reason in refused.values())
    fills = [x for x in by_order.broker.fills if x.kind == ENTRY]
    opens = {t: 100.0 for t in TECH}
    for i, fill in enumerate(fills):
        assert fill.qty == expected_qty(fills[:i], fill.ticker, "buy", opens, STARTING_CASH), fill.ticker
    assert [q for _, q in entries_of(by_order)] == [70, 69, 49, 61]           # the arithmetic, spelled out
    # And the order report sees the difference: the model fund left out a
    # name that outranked every purchase; this one left out only the least sure.
    [model_day] = om.fund_summary(model)["list"]
    [own_day] = om.fund_summary(by_order)["list"]
    assert [s["ticker"] for s in model_day["skipped"]] == ["IGV"] and model_day["skipped"][0]["outranks"]
    assert {s["ticker"] for s in own_day["skipped"]} == {"XLC", "MSFT"}
    assert all(not s["outranks"] for s in own_day["skipped"])


def test_a_second_cycle_still_comes_after_the_first_and_a_held_name_is_still_skipped():
    """Each cycle is tried, and ordered, on its own, on the book the cycle
    before it left. Short of room in both, a second cycle's surest line waits
    for the first cycle's least sure one, and a name bought in the first
    cycle is held -- skipped, not added to -- when its second line comes up.
    With room in both, each keeps watchlist order."""
    bars = Bars({t: flat() for t in ("MSFT", "XOM", "JPM")})
    feed = SimFeed(bars)
    entries = [said("MSFT", S[0], conviction=0.35, hour=14), said("XOM", S[0], conviction=0.4, hour=14),
               said("JPM", S[0], bias="NEUTRAL", conviction=0.3, hour=14),
               said("JPM", S[0], conviction=0.99, hour=18), said("MSFT", S[0], conviction=0.95, hour=18)]
    f = fund("model_by_conviction", bars, feed, priority=CONVICTION_FIRST)
    tried = []

    def short(batch):
        tried.append(([line.ticker for line, _ in batch], sorted(f.broker.positions)))
        return True

    f._short_of_room = short
    one_session(f, feed, entries)
    assert tried == [(["MSFT", "JPM", "XOM"], []),                             # cycle 1, in watchlist order
                     (["MSFT", "JPM"], ["MSFT", "XOM"])]                       # cycle 2, after cycle 1's fills
    assert [(x.ticker, x.status) for x in f.decisions] == [
        ("XOM", "ACCEPTED"), ("MSFT", "ACCEPTED"), ("JPM", "REJECTED"),              # cycle 1
        ("JPM", "ACCEPTED"), ("MSFT", "SKIPPED")]                                    # cycle 2
    [msft] = [x for x in f.broker.fills if x.ticker == "MSFT"]
    assert f.broker.positions["MSFT"].qty == msft.qty                         # not added to

    roomy = fund("model_by_conviction", bars, feed, priority=CONVICTION_FIRST)
    one_session(roomy, feed, entries)
    assert [(x.ticker, x.status) for x in roomy.decisions] == [
        ("MSFT", "ACCEPTED"), ("JPM", "REJECTED"), ("XOM", "ACCEPTED"),              # cycle 1
        ("MSFT", "SKIPPED"), ("JPM", "ACCEPTED")]                                    # cycle 2


def test_by_conviction_is_stable_and_puts_a_line_with_no_signal_last_in_its_cycle():
    d = S[0]
    lines = [Line(t, d, c, said(t, d)) for t, c in (("MSFT", 1), ("NVDA", 1), ("JPM", 1), ("LLY", 1), ("XOM", 2))]

    def sig(ticker, conviction):
        return LLMSignal(ticker=ticker, bias=Bias.BULLISH, conviction=conviction, rationale="t")

    pairs = list(zip(lines, [sig("MSFT", 0.5), None, sig("JPM", 0.5), sig("LLY", 0.8), sig("XOM", 0.9)]))
    assert [(ln.ticker, ln.cycle) for ln, _ in by_conviction(pairs)] == [
        ("LLY", 1), ("MSFT", 1), ("JPM", 1), ("NVDA", 1), ("XOM", 2)]


def test_with_room_for_every_line_the_fund_is_the_model_fund_exactly():
    """Four names in four groups, far under every limit. Watchlist order has
    room for every line, so the fund keeps it: the same orders, in the same
    order, to the share, and the same book to the cent."""
    names = {"MSFT": 0.35, "XOM": 0.5, "JPM": 0.9, "LLY": 0.6}
    bars = Bars({t: flat() for t in names})
    feed = SimFeed(bars)
    entries = [said(t, S[0], conviction=c) for t, c in names.items()]
    model, by_order = fund("model", bars, feed), fund("model_by_conviction", bars, feed, priority=CONVICTION_FIRST)
    feed.at_open(S[1])
    cycle = lines_by_day(entries)[S[0]]
    model.session(S[1], cycle)
    by_order.session(S[1], cycle)
    assert entries_of(by_order) == entries_of(model)
    assert [t for t, _ in entries_of(by_order)] == ["MSFT", "JPM", "LLY", "XOM"]          # watchlist order
    assert [(x.ticker, x.reason) for x in by_order.decisions] == [(x.ticker, x.reason) for x in model.decisions]
    assert by_order.days == model.days


#: A book just under the stock-market limit's 60% net: seven names in
#: seven groups at conviction 0.5, the review's case.
NEAR_THE_NET = ("NVDA", "JPM", "HDB", "CAT", "MELI", "RSP", "IWM")


def test_a_short_that_makes_room_for_a_long_is_not_a_lack_of_room():
    """The stock-market limit is on the net, longs less shorts, so a short
    dispatched first makes room for a long after it. Next day the model says
    XHB BEARISH at 0.35 and EWJ BULLISH at 0.9; in watchlist order the short
    goes first and both fill in full, so there is room for every line and the
    fund buys what the model fund buys. Had it sorted by conviction anyway,
    EWJ would have gone first and got 10 shares of its 69 -- a difference the
    owner's rule ("when there is not enough room") does not ask for."""
    names = NEAR_THE_NET + ("XHB", "EWJ")
    bars = Bars({t: flat() for t in names})
    feed = SimFeed(bars)
    entries = [said(t, S[0], conviction=0.5) for t in NEAR_THE_NET] + [
        said("XHB", S[1], bias="BEARISH", conviction=0.35), said("EWJ", S[1], conviction=0.9)]
    cycles = lines_by_day(entries)
    model = fund("model", bars, feed)
    by_order = fund("model_by_conviction", bars, feed, priority=CONVICTION_FIRST)
    sorted_anyway = fund("sorted_anyway", bars, feed, priority=CONVICTION_FIRST)
    sorted_anyway._short_of_room = lambda batch: True
    funds = (model, by_order, sorted_anyway)
    for session, cycle_day in ((S[1], S[0]), (S[2], S[1])):
        feed.at_open(session)
        for f in funds:
            f.session(session, cycles[cycle_day])

    def second_day(f):
        return [(x.ticker, x.side, x.qty) for x in f.broker.fills if x.kind == ENTRY and x.day == S[2]]

    assert second_day(model) == [("XHB", "sell", 69), ("EWJ", "buy", 69)]
    assert second_day(by_order) == second_day(model)
    assert by_order.days == model.days
    assert second_day(sorted_anyway) == [("EWJ", "buy", 10), ("XHB", "sell", 69)]


def test_a_line_cut_short_by_a_limit_means_the_book_ran_out_of_room():
    """Five Technology names, the surest last. In watchlist order every one
    is bought and none refused, but SMH -- the model's surest -- gets only 12
    shares of its 70: the group's 25% is spent. The book ran out of room and
    the order decided who got it, so the fund buys by conviction: SMH in
    full, then the three at 0.5, and MSFT, the least sure, is left out."""
    names = {"MSFT": 0.35, "NVDA": 0.5, "XLK": 0.5, "XLC": 0.5, "SMH": 0.9}
    bars = Bars({t: flat() for t in names})
    feed = SimFeed(bars)
    entries = [said(t, S[0], conviction=c) for t, c in names.items()]
    model, by_order = fund("model", bars, feed), fund("model_by_conviction", bars, feed, priority=CONVICTION_FIRST)
    for f in (model, by_order):
        one_session(f, feed, entries)
    assert all(x.status == "ACCEPTED" for x in model.decisions)
    assert entries_of(model) == [("MSFT", 50), ("NVDA", 49), ("XLK", 69), ("XLC", 69), ("SMH", 12)]
    assert entries_of(by_order) == [("SMH", 70), ("NVDA", 49), ("XLK", 69), ("XLC", 61)]
    [refused] = [x for x in by_order.decisions if x.status != "ACCEPTED"]
    assert refused.ticker == "MSFT" and "'Technology' group" in refused.reason


def test_trying_a_cycle_leaves_the_fund_exactly_as_it_was():
    """The trial runs the production engine on a copy of the book, with a
    record of its own: the fund's cash, positions, stops, fills, trades,
    audit record, tally and reports are untouched, whichever answer it
    gives."""
    bars = Bars({t: flat() for t in ("JPM", "XOM") + tuple(TECH)})
    feed = SimFeed(bars)
    f = fund("model_by_conviction", bars, feed, priority=CONVICTION_FIRST)
    one_session(f, feed, [said("JPM", S[0], conviction=0.5)])
    feed.at_open(S[2])
    f.broker.day = S[2]
    broker = f.broker

    def state():
        return (broker.cash, {t: vars(p).copy() for t, p in broker.positions.items()}, broker.live_stops(),
                list(broker.fills), list(broker.closed), set(broker._entries_today), broker._next_id,
                dict(broker._marks), f.audit.read_text(), f.audit.dropped, asdict(f.tally),
                list(f.decisions), list(f.order_events), set(f.order_days_seen), f.cycles_dispatched)

    before = state()
    short = [(line, model_signal(line)) for line in lines_by_day(
        [said(t, S[1], conviction=c) for t, c in TECH.items()])[S[1]]]
    roomy = [(line, model_signal(line)) for line in lines_by_day([said("XOM", S[1])])[S[1]]]
    assert f._short_of_room(short) is True                  # six Technology names: IGV finds no room
    assert f._short_of_room(roomy) is False
    assert state() == before


# --------------------------------------------------------------------------- #
# Fund 6: sized by conviction
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("conviction, factor", [(0.35, 0.25), (0.45, 0.5), (0.55, 1.0), (0.65, 1.5)])
def test_with_plenty_of_room_each_band_buys_its_factor_of_the_model_funds_shares(conviction, factor):
    """MSFT at 10, one line, an empty book: the model fund buys its 5% cap,
    500 shares; the sized fund buys the factor times that -- 125, 250, 500
    or 750 -- and its stop is the model fund's, since the ATR sets the stop
    and not the size."""
    bars = Bars({"MSFT": flat(10.0)})
    feed = SimFeed(bars)
    model, sized = fund("model", bars, feed), fund("model_sized", bars, feed, sized_by_conviction=True)
    for f in (model, sized):
        one_session(f, feed, [said("MSFT", S[0], conviction=conviction)])
    [(_, normal)], [(_, scaled)] = entries_of(model), entries_of(sized)
    assert normal == 500
    assert scaled == math.floor(STARTING_CASH * NORMAL("MSFT") * factor / 10.0) == round(500 * factor)
    assert sized.broker.live_stops()[0].stop_price == model.broker.live_stops()[0].stop_price
    assert risk_engine.max_position_pct_for is NORMAL


def test_a_short_is_scaled_too():
    bars = Bars({"XOM": flat(10.0)})
    feed = SimFeed(bars)
    sized = fund("model_sized", bars, feed, sized_by_conviction=True)
    one_session(sized, feed, [said("XOM", S[0], bias="BEARISH", conviction=0.65)])
    assert sized.broker.positions["XOM"].qty == -750


def test_the_scaled_cap_is_in_place_only_during_this_funds_own_call_and_always_put_back():
    bars = Bars({"MSFT": flat(10.0)})
    feed = SimFeed(bars)
    feed.at_open(S[1])
    sized = fund("model_sized", bars, feed, sized_by_conviction=True)
    model = fund("model", bars, feed)
    signal = LLMSignal(ticker="MSFT", bias=Bias.BULLISH, conviction=0.35, rationale="t")
    seen = []

    def look(engine_signal):
        seen.append((risk_engine.max_position_pct_for is NORMAL, risk_engine.max_position_pct_for("MSFT")))
        raise RuntimeError("the engine fell over")

    sized.engine.execute = look
    with pytest.raises(RuntimeError):
        sized._execute(signal)
    assert risk_engine.max_position_pct_for is NORMAL                          # put back, even so
    assert seen == [(False, pytest.approx(NORMAL("MSFT") * 0.25))]

    model.engine.execute = look                                              # another fund: never scaled
    with pytest.raises(RuntimeError):
        model._execute(signal)
    assert seen[-1] == (True, NORMAL("MSFT"))
    assert risk_engine.max_position_pct_for is NORMAL


def test_below_the_floor_nothing_is_scaled_and_the_engine_refuses_it():
    bars = Bars({"MSFT": flat(10.0)})
    feed = SimFeed(bars)
    feed.at_open(S[1])
    sized = fund("model_sized", bars, feed, sized_by_conviction=True)
    result, cap = sized._execute(LLMSignal(ticker="MSFT", bias=Bias.BULLISH, conviction=0.2, rationale="t"))
    assert result.status.value == "REJECTED" and "below minimum" in result.reason and cap is None
    assert risk_engine.max_position_pct_for is NORMAL


def test_a_scaled_cap_above_100_percent_is_an_integrity_problem_not_a_refusal(monkeypatch):
    """Should a cap ever be set so large that x1.5 passes 100%, the fund
    says so loudly -- an "unexpected" error the integrity check reports --
    rather than letting the risk engine's refusal read as an ordinary one."""
    monkeypatch.setattr(risk_engine, "max_position_pct_for", lambda ticker: 0.8)
    bars = Bars({"MSFT": flat(10.0)})
    feed = SimFeed(bars)
    sized = fund("model_sized", bars, feed, sized_by_conviction=True)
    one_session(sized, feed, [said("MSFT", S[0], conviction=0.65)])
    assert sized.broker.positions == {}
    assert len(sized.tally.unexpected) == 1 and "outside (0, 1]" in sized.tally.unexpected[0]
    assert not shadow_run.integrity([sized])["ok"]


def scaled_expected(fills_before, ticker: str, side: str, opens, conviction: float) -> int:
    """floor(min(equity x cap x factor, the tightest portfolio headroom) / price), on the book before."""
    equity, positions, _ = book_before(fills_before, opens, STARTING_CASH)
    headroom, _ = risk_engine.budget_ceiling_for(equity, ticker, positions, side)
    cap = equity * NORMAL(ticker) * conviction_factor(conviction)
    return max(0, math.floor(min(cap, headroom) / opens[ticker]))


@pytest.mark.parametrize("names, limit, bought, left_out", [
    # The Technology group's 25%: 7.5% + 7.5% + XLK's 7% x 1.5, cut to what
    # the group has left; XLC finds no room at all.
    (("MSFT", "NVDA", "XLK", "XLC"), "'Technology' group", ["MSFT", "NVDA", "XLK"], ["XLC"]),
    # The single-name sleeve's 25%: four names in four groups at 7.5% each;
    # the fourth gets what the sleeve has left, the fifth nothing.
    (("MSFT", "JPM", "LLY", "CAT", "PG"), "sleeve budget", ["MSFT", "JPM", "LLY", "CAT"], ["PG"]),
])
def test_a_group_or_sleeve_cap_still_binds_the_sized_fund(names, limit, bought, left_out):
    bars = Bars({t: flat() for t in names})
    feed = SimFeed(bars)
    sized = fund("model_sized", bars, feed, sized_by_conviction=True)
    one_session(sized, feed, [said(t, S[0], conviction=0.65) for t in names])

    fills = [x for x in sized.broker.fills if x.kind == ENTRY]
    assert [x.ticker for x in fills] == bought
    opens = {t: 100.0 for t in names}
    for i, fill in enumerate(fills):
        assert fill.qty == scaled_expected(fills[:i], fill.ticker, "buy", opens, 0.65), fill.ticker
    # The first is the full 1.5x; the last one bought was cut by the limit.
    assert fills[0].qty == 75 and fills[-1].qty < math.floor(STARTING_CASH * NORMAL(fills[-1].ticker) * 1.5 / 100)
    equity = sized.days[-1].equity
    assert sized.days[-1].gross <= equity * 0.25 + 1e-6
    refused = [x for x in sized.decisions if x.status != "ACCEPTED"]
    assert [x.ticker for x in refused] == left_out and all(limit in x.reason for x in refused)
    # The order report reads the limit, with the fund's exact scaled cap.
    [day] = om.fund_summary(sized)["list"]
    assert [(s["ticker"], s["kind"]) for s in day["skipped"]] == [
        (t, om.GROUP if "group" in limit else om.SLEEVE) for t in left_out]


def test_the_order_report_reads_a_scaled_cap_exactly_not_as_the_engine_rounds_it():
    """5% x 0.25 is 1.25%, which the engine prints as "1%". With 1,100 of
    headroom left the ticker's own 1.25% (1,250) was not what bound it --
    the limit was -- but read at the printed 1% it would seem to be."""
    reason = ("no room for equity MSFT under its 1% cap or the sleeve budget limit: equity 100000.00, "
              "price 1200.00, existing exposure 0.00, headroom 1100.00")
    assert om.capacity_kind(reason) is None
    assert om.capacity_kind(reason, 0.0125) == om.SLEEVE


def test_the_sized_fund_hands_its_exact_cap_to_the_order_report():
    """The same case, through the fund. The fund's own engine call says
    which cap it sized under, and the order report is given that cap. JPM,
    LLY and CAT at 0.65 (7.5% each) and PG at 0.45 (what the sleeve has left)
    leave the single-name sleeve 293.83. MSFT at 1,200, conviction 0.35 in a
    second cycle, has a 1.25% cap: 1,249.69, a share's worth. So the sleeve,
    not its own cap, refused it, and the report must say so. Read at the
    engine's printed 1% it would be dropped as "its own cap bound it"."""
    small = flat(10.0)
    feed = SimFeed(Bars({"MSFT": small}))
    feed.at_open(S[1])
    alone = fund("model_sized", feed._bars, feed, sized_by_conviction=True)
    result, cap = alone._execute(LLMSignal(ticker="MSFT", bias=Bias.BULLISH, conviction=0.35, rationale="t"))
    assert result.status.value == "ACCEPTED" and cap == pytest.approx(NORMAL("MSFT") * 0.25)

    dear = flat(1200.0)
    dear["High"], dear["Low"] = 1210.0, 1190.0                    # an ATR the engine's sanity check accepts
    bars = Bars({"JPM": flat(), "LLY": flat(), "CAT": flat(), "PG": flat(), "MSFT": dear})
    feed = SimFeed(bars)
    entries = ([said(t, S[0], conviction=0.65, hour=14) for t in ("JPM", "LLY", "CAT")]
               + [said("PG", S[0], conviction=0.45, hour=14),
                  said("MSFT", S[0], bias="NEUTRAL", conviction=0.3, hour=14),   # so the next is cycle 2
                  said("MSFT", S[0], conviction=0.35, hour=18)])
    sized = fund("model_sized", bars, feed, sized_by_conviction=True)
    one_session(sized, feed, entries)
    msft = sized.decisions[-1]
    assert (msft.ticker, msft.status) == ("MSFT", "REJECTED")
    assert "under its 1% cap or the sleeve budget limit" in msft.reason and "headroom 293.83" in msft.reason
    [day] = om.fund_summary(sized)["list"]
    assert [(s["ticker"], s["kind"]) for s in day["skipped"]] == [("MSFT", om.SLEEVE)]
    assert om.capacity_kind(msft.reason) is None                  # what the rounded cap alone would say


# --------------------------------------------------------------------------- #
# Long runs: the same invariants as every fund
# --------------------------------------------------------------------------- #


#: Three more Technology funds beside MSFT, NVDA and XLK: six names the
#: group's 25% cannot all hold, so the book runs out of room on some days and
#: the buying order has something to decide.
MORE_TECH = ("SMH", "XLC", "IGV")
NAMES = UNIVERSE + MORE_TECH


def wider() -> Bars:
    base = universe()
    frames = {t: base._frames[t] for t in base.tickers()}
    frames.update({t: walk(20 + i, 40.0 + 10 * i, 0.012) for i, t in enumerate(MORE_TECH)})
    return Bars(frames)


def journal_with_every_band(sessions, seed: int = 5) -> list[JournalEntry]:
    rng = np.random.RandomState(seed)
    out = []
    for day in sessions:
        for ticker in NAMES:
            u = rng.rand()
            if u < 0.05:
                out.append(JournalEntry(ticker=ticker, timestamp=stamp(day), held=True))
            else:
                out.append(said(ticker, day, bias=("BULLISH", "BEARISH", "NEUTRAL")[int(rng.rand() * 3)],
                                conviction=float(rng.choice([0.2, 0.35, 0.45, 0.55, 0.65, 0.85]))))
    return out


def sized_mismatches(f: Fund) -> list[str]:
    """``sizing_mismatches`` with each entry's cap scaled by its signal's factor."""
    conviction = {(x.session, x.ticker): x.conviction for x in f.decisions if x.status == "ACCEPTED"}
    out = []
    fills = f.broker.fills
    for i, x in enumerate(fills):
        if x.kind != ENTRY:
            continue
        held = _held_on_fills(fills[:i])
        opens = {}
        for ticker in held | {x.ticker}:
            bar = f.bars.bar(ticker, x.day)
            opens[ticker] = bar[0] if bar else f.bars.last_close_before(ticker, x.day)
        want = scaled_expected(fills[:i], x.ticker, x.side, opens, conviction[(x.day, x.ticker)])
        if x.qty != want:
            out.append(f"{f.name} {x.day} {x.ticker}: {x.qty}, expected {want}")
    return out


def test_a_long_run_keeps_every_invariant_for_both_exploratory_funds():
    """Sixty sessions, fifteen names, every conviction band: stops cover every
    position, cash is the fills, the trades account for it, the book is
    marked at the close; no unexpected engine error, no manager error, R
    never estimated; each entry is the engine's size on the book before it
    (scaled, for the sized fund); the cap is back to production's after;
    and each fund really did something the model fund did not."""
    bars = wider()
    sessions = S[:60]
    entries = journal_with_every_band(sessions)
    feed = SimFeed(bars)
    model = CheckedFund("model", model_signal, feed, bars, keep_actions=True)
    by_order = CheckedFund("model_by_conviction", model_signal, feed, bars, keep_actions=True,
                           priority=CONVICTION_FIRST)
    sized = CheckedFund("model_sized", model_signal, feed, bars, keep_actions=True, sized_by_conviction=True)
    run([model, by_order, sized], sessions, lines_by_day(entries), cycle_days(entries), feed)

    assert risk_engine.max_position_pct_for is NORMAL
    for f in (model, by_order, sized):
        assert f.violations == [], f.name
        assert f.tally.unexpected == [] and f.tally.manager_errors == [] and f.tally.estimated_r == 0, f.name
        assert len(f.days) == len(sessions)
    assert sizing_mismatches(model) == [] and sizing_mismatches(by_order) == []
    assert sized_mismatches(sized) == []
    assert entries_of(by_order) != entries_of(model)
    assert entries_of(sized) != entries_of(model)
    factors = {conviction_factor(x.conviction) for x in sized.decisions if x.status == "ACCEPTED"}
    assert factors == {0.25, 0.5, 1.0, 1.5}
    # The ladder is the manager's, unchanged: rungs are taken on scaled positions too.
    assert any(a["action"] == "tranche_taken" for a in sized.audit.actions)


# --------------------------------------------------------------------------- #
# The fund output
# --------------------------------------------------------------------------- #


def test_vs_model_is_the_daily_difference_its_newey_west_t_and_both_drawdowns():
    def days(values):
        return SimpleNamespace(days=[Day(S[i], v, 0.0, 0.0, 0) for i, v in enumerate(values)])

    model = days([101_000.0, 102_010.0, 99_000.0])
    other = days([100_000.0, 101_000.0, 101_500.0])
    got = shadow_run.vs_model(other, model)
    diffs = [0.0 - 0.01, 0.01 - 0.01, 101_500.0 / 101_000.0 - 1 - (99_000.0 / 102_010.0 - 1)]
    assert got["days"] == 3
    assert got["mean_daily_diff"] == pytest.approx(sum(diffs) / 3)
    assert got["t"] == pytest.approx(newey_west_t(diffs, 5))
    assert got["total_return_diff"] == pytest.approx(0.015 - (-0.01))
    assert got["max_drawdown"] == 0.0
    assert got["model_max_drawdown"] == pytest.approx(1 - 99_000.0 / 102_010.0)
    # Two books equal to the cent differ by exactly nothing: no t of float noise.
    same = shadow_run.vs_model(days([100_000.004, 101_000.0]), days([100_000.0, 101_000.001]))
    assert (same["mean_daily_diff"], same["t"], same["days"]) == (0.0, None, 2)
    empty = shadow_run.vs_model(days([]), days([]))
    assert (empty["days"], empty["mean_daily_diff"], empty["t"], empty["total_return_diff"]) == (0, None, None, 0.0)


class Walks:
    """An ``OhlcFetcher`` stand-in: made-up bars, no network."""

    def __init__(self, bars: Bars):
        self.frames = {t: bars._frames[t] for t in bars.tickers()}

    def ohlc(self, ticker, start, end):
        frame = self.frames.get(ticker)
        return frame.copy() if frame is not None else pd.DataFrame()


def test_the_fund_output_lists_the_three_after_the_four_compared_with_the_model_fund(monkeypatch):
    bars = wider()
    sessions = S[:40]
    entries = journal_with_every_band(sessions)
    checked = []
    real_integrity = shadow_run.integrity
    monkeypatch.setattr(shadow_run, "integrity", lambda funds: checked.append([f.name for f in funds])
                        or real_integrity(funds))

    funds, checks = shadow_run.run_funds(entries, sessions[0], sessions[-1], Walks(bars), random_funds=2,
                                         processes=1, shortable_no=frozenset())

    json.dumps(funds, allow_nan=False)                                       # what the page parses
    json.dumps(checks, allow_nan=False)
    rows = {r["name"]: r for r in funds["list"]}
    assert [r["name"] for r in funds["list"]] == ["model", "momentum", "hybrid", "vt",
                                                   "model_by_conviction", "model_sized", "model_same_day"]
    assert [r["exploratory"] for r in funds["list"]] == [False] * 4 + [True] * 3
    assert [r["label"] for r in funds["list"]][4:] == ["Model, highest conviction first", "Model, sized by conviction",
                                                       "Model, entered the same day"]
    # The integrity check covers all seven (the key keeps its name).
    assert ["model", "momentum", "hybrid", "vt", "model_by_conviction", "model_sized", "model_same_day"] in checked
    # This journal has no recorded prices: the same-day fund enters nothing, and says why.
    assert rows["model_same_day"]["trades"] == 0
    assert rows["model_same_day"]["not_entered"]["no_price"] == rows["model_same_day"]["not_entered"]["total"] > 0
    assert all("not_entered" not in rows[n] for n in ("model", "model_by_conviction", "model_sized"))
    assert checks["four"]["ok"], checks["four"]["problems"]
    model = rows["model"]
    assert model["order_matters"]["days"] > 0                                # the order had room to matter
    for name in shadow_run.EXPLORATORY_FUNDS:
        row = rows[name]
        assert row["compare_to"] == "model"
        vs = row["vs_model"]
        assert set(vs) == {"total_return_diff", "max_drawdown", "model_max_drawdown", "mean_daily_diff", "t", "days"}
        assert vs["total_return_diff"] == pytest.approx(row["total_return"] - model["total_return"])
        assert vs["max_drawdown"] == row["max_drawdown"] and vs["model_max_drawdown"] == model["max_drawdown"]
        assert vs["days"] == len(funds["days"]) == len(row["equity"])
        assert row["sides"] is not None and row["order_matters"] is not None
        assert row["equity"] != model["equity"]                               # the change did something
    for name in ("model", "momentum", "hybrid", "vt"):
        assert "vs_model" not in rows[name] and "compare_to" not in rows[name]
    assert risk_engine.max_position_pct_for is NORMAL

    # The four are exactly what they were without the two beside them.
    feed = SimFeed(Bars({t: Walks(bars).ohlc(t, None, None) for t in bars.tickers()}))
    alone = Fund("model", model_signal, feed, feed._bars)
    days = [date.fromisoformat(d) for d in funds["days"]]
    run([alone], days, lines_by_day(entries), cycle_days(entries), feed)
    assert [round(d.equity, 2) for d in alone.days] == model["equity"]


def test_the_smoke_check_runs_the_three_exploratory_funds_and_reports_only_health(monkeypatch, capsys, tmp_path):
    from tests.test_shadow_smoke import ALLOWED, Flat, entry

    entries = [entry(1, "NVDA"), entry(1, "XOM", "BEARISH"), entry(2, "MSFT"), entry(5, "LQD", "BEARISH")]
    report = smoke.smoke(entries, 5, 2, Flat(), date(2026, 10, 7), frozenset({"LQD"}), exploratory=True)
    assert [r["name"] for r in report] == ["model", "momentum", "hybrid", "vt", "model_by_conviction",
                                           "model_sized", "model_same_day", "coin-0", "coin-1"]
    for row in report:
        assert set(row) <= ALLOWED, row
    for row in report[4:6]:
        assert row["problems"] == [] and row["sessions"] == 5 and row["accepted"] == 3
    # These lines carry no recorded price: the same-day fund enters none of them.
    assert report[6]["problems"] == [] and report[6]["sessions"] == 5 and report[6]["accepted"] == 0

    # The command line always asks for them.
    asked = {}

    def fake(*args, **kw):
        asked.update(kw)
        return [{"name": "model", "problems": []}]

    monkeypatch.setattr(smoke, "smoke", fake)
    monkeypatch.setattr(smoke, "read_journal", lambda path: SimpleNamespace(entries=[]))
    monkeypatch.setattr(smoke, "OhlcFetcher", lambda **kw: None)
    assert smoke.main(["--journal", str(tmp_path / "journal.log"), "--audit", str(tmp_path / "none.log")]) == 0
    assert asked == {"exploratory": True}
