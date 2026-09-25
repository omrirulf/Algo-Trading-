"""Longs vs shorts in the fund output: the owner's decision 6 of 25 Sep 2026. Report only.

For each fund but VT, and for each side: the number of closed trades, their
mean net return and their hit rate, with "too few" until a side has 20. A
trade's net return is its pnl -- costs and dividends in -- over the notional
it was opened at, which the simulated broker now records on every closed
trade.
"""

from __future__ import annotations

import json
import pytest

from shadow import run as shadow_run
from shadow.broker import DEFAULT_COST_PER_SIDE, ENTRY, STOP, ClosedTrade
from shadow.fund import IndexFund, run
from shadow.market import Bars, SimFeed
from tests.test_shadow_broker import D1, D2, D3, book
from tests.test_shadow_fund import S, flat, fund, line, said

COST = DEFAULT_COST_PER_SIDE


def test_a_side_is_too_few_until_it_has_twenty_trades():
    assert shadow_run.MIN_SIDE_TRADES == 20


# --------------------------------------------------------------------------- #
# The notional a trade was opened at
# --------------------------------------------------------------------------- #


def test_a_closed_trade_carries_the_notional_it_was_opened_at():
    """Entry quantity x average entry price, before costs; a partial close
    and a dividend leave it alone, as they leave the entry price alone."""
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.day = D2
    held = broker.held_quantities()
    broker.pay_dividends({"AAA": 0.5}, held)
    quotes["AAA"] = 105.0
    stop = broker.get_open_stop_order("AAA")
    broker.replace_stop_order(stop.order_id, 6, 100.0, current_qty=10)
    broker.close_position_partially("AAA", 4)
    broker.day = D3
    broker.fill_touched_stops({"AAA": 99.0}, {"AAA": 104.0})
    [trade] = broker.closed
    assert trade.notional == 1_000.0
    assert trade.pnl == pytest.approx(-1_000.0 - 1.0 + 5.0 + (420.0 - 0.42) + (600.0 - 0.60))


def test_a_short_and_an_added_to_position_carry_every_share_they_opened():
    broker, quotes = book(AAA=100.0, SSS=50.0)
    broker.submit_bracket_order("SSS", 20, "sell", 55.0)
    broker.submit_bracket_order("AAA", 10, "buy", 90.0)
    broker.day = D2
    quotes["AAA"] = 110.0
    broker.submit_bracket_order("AAA", 5, "buy", 100.0)                  # an add: 15 at an average of 103.33
    assert broker.positions["AAA"].avg_entry_price == pytest.approx(1_550.0 / 15)
    broker.day = D3
    broker.fill_gapped_stops({"AAA": 80.0, "SSS": 56.0})                  # both stopped at the open
    trades = {t.ticker: t for t in broker.closed}
    assert trades["SSS"].side == "sell" and trades["SSS"].notional == 1_000.0
    assert trades["AAA"].side == "buy" and trades["AAA"].notional == pytest.approx(15 * 1_550.0 / 15)


def test_a_seeded_position_is_opened_at_its_own_quantity_and_price():
    broker, quotes = book()
    broker.seed_position("AAA", -7, 120.0, D1, stops=[(7, 130.0)])
    broker.day = D2
    broker.fill_gapped_stops({"AAA": 131.0})
    [trade] = broker.closed
    assert trade.notional == pytest.approx(840.0)


# --------------------------------------------------------------------------- #
# The side summary
# --------------------------------------------------------------------------- #


def trade(side: str, ret: float, notional: float = 1_000.0) -> ClosedTrade:
    return ClosedTrade("AAA", side, D1, D2, ret * notional, notional)


def test_each_side_counts_its_trades_their_mean_net_return_and_hit_rate():
    closed = [trade("buy", 0.10), trade("buy", -0.02, 5_000.0), trade("buy", 0.0), trade("buy", 0.04, 250.0),
              trade("sell", -0.05), trade("sell", 0.03, 2_000.0)]
    got = shadow_run.sides(closed)
    # Each trade counts once, whatever its size: the mean of the returns.
    assert got["long"] == {"n": 4, "mean_return": pytest.approx((0.10 - 0.02 + 0.0 + 0.04) / 4),
                           "hit_rate": 0.5, "too_few": True}           # a flat trade is not a hit
    assert got["short"] == {"n": 2, "mean_return": pytest.approx(-0.01), "hit_rate": 0.5, "too_few": True}
    json.dumps(got, allow_nan=False)


def test_too_few_turns_off_at_twenty_trades_on_that_side_alone():
    got = shadow_run.sides([trade("buy", 0.01)] * 19 + [trade("sell", -0.01)] * 20)
    assert (got["long"]["n"], got["long"]["too_few"]) == (19, True)
    assert (got["short"]["n"], got["short"]["too_few"]) == (20, False)
    got = shadow_run.sides([trade("buy", 0.01)] * 20)
    assert got["long"]["too_few"] is False and got["long"]["hit_rate"] == 1.0


def test_a_side_with_no_trades_has_no_mean_and_no_hit_rate():
    assert shadow_run.sides([]) == {
        "long": {"n": 0, "mean_return": None, "hit_rate": None, "too_few": True},
        "short": {"n": 0, "mean_return": None, "hit_rate": None, "too_few": True},
    }


# --------------------------------------------------------------------------- #
# In the fund output
# --------------------------------------------------------------------------- #


def test_a_funds_row_says_how_its_closed_longs_and_shorts_did_net_of_costs_and_vt_says_nothing():
    """MSFT bought and stopped out; XOM shorted and stopped out; JPM still
    open, so not counted. Each closed trade's return is its own pnl -- both
    sides' costs in -- over what it was opened at."""
    bars = Bars({"MSFT": flat(changes={2: {"Low": 90.0}}), "XOM": flat(50.0, {2: {"High": 60.0}}),
                 "JPM": flat(80.0), "VT": flat(110.0)})
    feed = SimFeed(bars)
    f = fund("model", bars, feed)
    index = IndexFund("vt", "VT", bars)
    cycles = {S[0]: [line(said("MSFT", S[0])), line(said("XOM", S[0], bias="BEARISH")), line(said("JPM", S[0]))]}
    run([f, index], S[:4], cycles, {S[0]}, feed)
    assert {t.ticker for t in f.broker.closed} == {"MSFT", "XOM"} and "JPM" in f.broker.positions

    row = shadow_run.summarise(f, None)
    msft = next(t for t in f.broker.closed if t.ticker == "MSFT")
    xom = next(t for t in f.broker.closed if t.ticker == "XOM")
    entry_msft = next(x for x in f.broker.fills if x.ticker == "MSFT" and x.kind == ENTRY)
    stop_msft = next(x for x in f.broker.fills if x.ticker == "MSFT" and x.kind == STOP)
    assert msft.notional == entry_msft.qty * 100.0
    assert msft.pnl == pytest.approx(entry_msft.qty * (stop_msft.price - 100.0)
                                     - entry_msft.qty * (100.0 + stop_msft.price) * COST)
    assert row["sides"]["long"] == {"n": 1, "mean_return": pytest.approx(msft.pnl / msft.notional),
                                    "hit_rate": 0.0, "too_few": True}
    assert row["sides"]["short"] == {"n": 1, "mean_return": pytest.approx(xom.pnl / xom.notional),
                                     "hit_rate": 0.0, "too_few": True}
    assert row["sides"]["long"]["mean_return"] < -0.001 * 2              # lost the move and both costs
    assert shadow_run.summarise(index, None)["sides"] is None
    assert row["exploratory"] is False
    json.dumps(row, allow_nan=False)


def test_every_row_of_the_fund_output_has_sides_but_vt():
    """The four and the two exploratory funds alike; VT's is null."""
    from tests.test_shadow_variants import Walks, journal_with_every_band, wider

    bars = wider()
    sessions = S[:30]
    funds, _ = shadow_run.run_funds(journal_with_every_band(sessions), sessions[0], sessions[-1], Walks(bars),
                                    random_funds=0, processes=1, shortable_no=frozenset())
    for row in funds["list"]:
        if row["name"] == "vt":
            assert row["sides"] is None
            continue
        assert set(row["sides"]) == {"long", "short"}, row["name"]
        for side in row["sides"].values():
            assert set(side) == {"n", "mean_return", "hit_rate", "too_few"}
            assert side["too_few"] == (side["n"] < 20)
        assert sum(s["n"] for s in row["sides"].values()) <= row["trades"]
    assert any(row["sides"]["long"]["n"] and row["sides"]["short"]["n"] for row in funds["list"] if row["sides"])
