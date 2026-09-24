"""The simulated book refuses what Alpaca refuses and counts money the way the account does.

``SimBroker`` is the one part of a shadow fund that is not production code,
so every refusal the real client (or the paper account behind it) makes is
checked here with the same exception type, and every cash movement is
checked to the cent: fills, the 0.10% cost per side, dividends on the
shares held at the previous close, stops that gap, touch or are already
through, and the trade record a closed position leaves behind.
"""

from __future__ import annotations

from datetime import date

import pytest

from app import position_manager as pm
from app.broker_client import BrokerError, DuplicateOrderError, OpenPosition
from app.logger import log_execution
from app.market_data import MarketDataError
from app.schemas import Bias, ExecutionResult, ExecutionStatus, LLMSignal
from shadow.audit import FundAudit
from shadow.broker import DEFAULT_COST_PER_SIDE, DIVIDEND, ENTRY, STOP, TRANCHE, ClosedTrade, SimBroker

D1, D2, D3 = date(2026, 3, 2), date(2026, 3, 3), date(2026, 3, 4)
COST = DEFAULT_COST_PER_SIDE


class Quotes(dict):
    """The feed's price right now, per ticker; a ticker with no bar raises as the feed does."""

    def __call__(self, ticker: str) -> float:
        try:
            return self[ticker]
        except KeyError:
            raise MarketDataError(f"no bar for {ticker}") from None


def book(cash: float = 100_000.0, day: date = D1, **prices) -> tuple[SimBroker, Quotes]:
    quotes = Quotes(prices or {"AAA": 100.0})
    return SimBroker("t", cash, quote=quotes, day=day, not_shortable=frozenset({"HTB"})), quotes


def stops_of(broker: SimBroker, ticker: str) -> list[tuple[int, float, str]]:
    return [(s.qty, s.stop_price, s.side) for s in broker.live_stops() if s.ticker == ticker]


# --------------------------------------------------------------------------- #
# Refusals: what the real client and the paper account refuse
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("qty", [0, -3, 2.5, "3", None])
def test_an_entry_refuses_a_quantity_that_is_not_a_whole_number_of_at_least_one(qty):
    broker, _ = book()
    with pytest.raises(BrokerError):
        broker.submit_bracket_order("AAA", qty, "buy", 95.0)
    assert broker.positions == {} and broker.cash == 100_000.0 and broker.live_stops() == []


@pytest.mark.parametrize("stop", [0.0, -1.0])
def test_an_entry_refuses_a_stop_that_is_not_positive(stop):
    broker, _ = book()
    with pytest.raises(BrokerError, match="stop_price must be positive"):
        broker.submit_bracket_order("AAA", 10, "buy", stop)
    assert broker.positions == {}


@pytest.mark.parametrize("side", ["long", "BUY", "", "short"])
def test_an_entry_refuses_a_side_that_is_not_buy_or_sell(side):
    broker, _ = book()
    with pytest.raises(BrokerError, match="side must be"):
        broker.submit_bracket_order("AAA", 10, side, 95.0)
    assert broker.positions == {}


def test_a_second_same_side_entry_on_one_day_is_a_duplicate_and_the_next_day_is_not():
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    cash = broker.cash
    with pytest.raises(DuplicateOrderError):
        broker.submit_bracket_order("aaa", 5, "buy", 95.0)
    # The refusal moved nothing: no fill, no cash, no second stop.
    assert broker.cash == cash and broker.positions["AAA"].qty == 10 and len(broker.live_stops()) == 1
    assert issubclass(DuplicateOrderError, BrokerError)

    broker.day = D2
    quotes["AAA"] = 110.0
    broker.submit_bracket_order("AAA", 5, "buy", 104.0)
    assert broker.positions["AAA"].qty == 15


def test_a_short_the_paper_account_refused_is_refused_and_a_long_is_not():
    broker, _ = book(HTB=50.0)
    with pytest.raises(BrokerError, match="cannot be sold short"):
        broker.submit_bracket_order("HTB", 10, "sell", 55.0)
    assert broker.positions == {}
    # The refusal did not spend the day's idempotency key, and buying is fine.
    broker.submit_bracket_order("HTB", 10, "buy", 45.0)
    assert broker.positions["HTB"].qty == 10


@pytest.mark.parametrize("held, entry", [("buy", "sell"), ("sell", "buy")])
def test_an_entry_may_not_reverse_an_open_position(held, entry):
    broker, _ = book()
    broker.submit_bracket_order("AAA", 10, held, 95.0 if held == "buy" else 105.0)
    broker.day = D2
    cash = broker.cash
    with pytest.raises(BrokerError, match="reverse"):
        broker.submit_bracket_order("AAA", 10, entry, 105.0 if entry == "sell" else 95.0)
    assert broker.cash == cash and abs(broker.positions["AAA"].qty) == 10


def test_replacing_an_order_that_is_not_live_is_refused():
    broker, _ = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    with pytest.raises(BrokerError, match="no open stop order"):
        broker.replace_stop_order("no-such-order", 10, 96.0)
    old = broker.get_open_stop_order("AAA").order_id
    broker.replace_stop_order(old, 10, 96.0, current_qty=10)
    with pytest.raises(BrokerError, match="no open stop order"):
        broker.replace_stop_order(old, 10, 97.0, current_qty=10)     # the replaced one is gone


@pytest.mark.parametrize("qty, stop", [(0, 96.0), (2.5, 96.0), (10, 0.0), (10, -5.0)])
def test_a_replace_refuses_bad_quantities_and_prices(qty, stop):
    broker, _ = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    order = broker.get_open_stop_order("AAA")
    with pytest.raises(BrokerError):
        broker.replace_stop_order(order.order_id, qty, stop)
    assert broker.get_open_stop_order("AAA") == order


def test_a_replace_for_more_than_the_free_shares_is_insufficient_qty():
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    order = broker.get_open_stop_order("AAA")
    with pytest.raises(BrokerError, match="insufficient qty available.*requested: 11, available: 10"):
        broker.replace_stop_order(order.order_id, 11, 96.0, current_qty=10)
    # With an add-on's own stop reserving five of fifteen, the first stop may
    # cover at most ten -- the live account's refusal for two bracket legs.
    broker.day = D2
    broker.submit_bracket_order("AAA", 5, "buy", 95.0)
    with pytest.raises(BrokerError, match="insufficient qty available.*requested: 15, available: 10"):
        broker.replace_stop_order(order.order_id, 15, 96.0, current_qty=10)
    assert broker.get_open_stop_order("AAA").qty == 5                  # newest first, as Alpaca lists them
    assert sorted(q for q, _, _ in stops_of(broker, "AAA")) == [5, 10]


def test_a_price_only_replace_keeps_the_orders_own_size_even_when_current_qty_is_stale():
    """``current_qty == qty`` means the real client leaves qty out of the
    request, so Alpaca keeps whatever the order covers. A caller whose
    ``current_qty`` is stale gets exactly that, here as live."""
    broker, _ = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    order = broker.get_open_stop_order("AAA")
    moved = broker.replace_stop_order(order.order_id, 7, 96.0, current_qty=7)
    assert (moved.qty, moved.stop_price) == (10, 96.0)
    resized = broker.replace_stop_order(moved.order_id, 7, 96.5, current_qty=10)
    assert (resized.qty, resized.stop_price) == (7, 96.5)
    unsaid = broker.replace_stop_order(resized.order_id, 6, 97.0)       # no current_qty: a resize
    assert unsaid.qty == 6


def test_every_replace_is_a_new_order_id_and_only_the_newest_is_live():
    broker, _ = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    ids = [broker.get_open_stop_order("AAA").order_id]
    for price in (95.5, 96.0, 96.5):
        ids.append(broker.replace_stop_order(ids[-1], 10, price, current_qty=10).order_id)
    assert len(set(ids)) == 4
    assert [s.order_id for s in broker.live_stops()] == [ids[-1]]
    assert stops_of(broker, "AAA") == [(10, 96.5, "sell")]


def test_a_partial_close_is_refused_for_more_than_the_free_shares_and_for_nothing_held():
    broker, _ = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    with pytest.raises(BrokerError, match="insufficient qty available.*requested: 1, available: 0"):
        broker.close_position_partially("AAA", 1)                       # the stop holds all ten
    order = broker.get_open_stop_order("AAA")
    broker.replace_stop_order(order.order_id, 7, 95.0, current_qty=10)
    with pytest.raises(BrokerError, match="insufficient qty available.*requested: 4, available: 3"):
        broker.close_position_partially("AAA", 4)
    broker.close_position_partially("AAA", 3)
    assert broker.positions["AAA"].qty == 7
    with pytest.raises(BrokerError, match="position does not exist"):
        broker.close_position_partially("BBB", 1)
    for qty in (0, -1, 1.5):
        with pytest.raises(BrokerError):
            broker.close_position_partially("AAA", qty)


def test_a_protective_stop_must_reduce_a_position_and_fit_in_its_free_shares():
    broker, _ = book(AAA=100.0, SSS=50.0)
    with pytest.raises(BrokerError, match="no open position"):
        broker.submit_stop_order("AAA", 1, "sell", 90.0)                 # would open a short
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.submit_bracket_order("SSS", 10, "sell", 55.0)
    with pytest.raises(BrokerError, match="would not reduce"):
        broker.submit_stop_order("AAA", 1, "buy", 110.0)                 # would add to a long
    with pytest.raises(BrokerError, match="would not reduce"):
        broker.submit_stop_order("SSS", 1, "sell", 45.0)                 # would add to a short
    with pytest.raises(BrokerError, match="exceeds the free 0"):
        broker.submit_stop_order("AAA", 1, "sell", 90.0)                 # the bracket stop holds all ten
    for bad in ((0, "sell", 90.0), (2.5, "sell", 90.0), (1, "sell", 0.0), (1, "hold", 90.0)):
        with pytest.raises(BrokerError):
            broker.submit_stop_order("AAA", *bad)
    assert len(broker.live_stops()) == 2


# --------------------------------------------------------------------------- #
# Cash
# --------------------------------------------------------------------------- #


def test_a_long_round_trip_moves_cash_by_its_fills_and_costs_and_its_trade_says_so():
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    assert broker.cash == pytest.approx(100_000.0 - 1_000.0 - 1_000.0 * COST)
    order = broker.get_open_stop_order("AAA")

    broker.day = D2
    quotes["AAA"] = 105.0
    order = broker.replace_stop_order(order.order_id, 6, 100.0, current_qty=10)
    broker.close_position_partially("AAA", 4)                             # a rung: 4 at the price
    assert broker.cash == pytest.approx(98_999.0 + 420.0 - 420.0 * COST)
    broker.day = D3
    broker.fill_touched_stops({"AAA": 99.0}, {"AAA": 104.0})              # the rest at the stop
    expected = 100_000.0 - 1_001.0 + (420.0 - 0.42) + (600.0 - 0.60)
    assert broker.cash == pytest.approx(expected)
    assert broker.positions == {} and broker.live_stops() == []
    [trade] = broker.closed
    assert trade == ClosedTrade("AAA", "buy", D1, D3, pytest.approx(expected - 100_000.0))
    assert [(f.kind, f.side, f.qty, f.price) for f in broker.fills] == [
        (ENTRY, "buy", 10, 100.0), (TRANCHE, "sell", 4, 105.0), (STOP, "sell", 6, 100.0)]
    assert [f.cost for f in broker.fills] == pytest.approx([1.0, 0.42, 0.60])
    assert broker.equity() == pytest.approx(broker.cash)


def test_a_short_round_trip_credits_the_sale_and_pays_to_cover():
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "sell", 105.0)
    assert broker.cash == pytest.approx(100_000.0 + 1_000.0 - 1.0)
    assert broker.positions["AAA"].qty == -10
    assert stops_of(broker, "AAA") == [(10, 105.0, "buy")]
    broker.day = D2
    quotes["AAA"] = 90.0
    order = broker.get_open_stop_order("AAA")
    broker.replace_stop_order(order.order_id, 7, 100.0, current_qty=10)
    broker.close_position_partially("AAA", 3)                             # covers 3 at 90
    broker.day = D3
    broker.fill_gapped_stops({"AAA": 102.0})                              # gaps up through 100: covers at 102
    expected = 100_000.0 + (1_000.0 - 1.0) - (270.0 + 0.27) - (714.0 + 0.714)
    assert broker.cash == pytest.approx(expected)
    [trade] = broker.closed
    assert (trade.side, trade.opened, trade.closed) == ("sell", D1, D3)
    assert trade.pnl == pytest.approx(expected - 100_000.0)
    assert broker.fills[-1].gapped and broker.fills[-1].price == 102.0


def test_dividends_credit_a_long_charge_a_short_and_only_on_shares_held_at_the_previous_close():
    broker, quotes = book(AAA=100.0, SSS=50.0, NEW=20.0)
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.submit_bracket_order("SSS", 20, "sell", 55.0)
    broker.day = D2
    held = broker.held_quantities()                                       # the book at the previous close
    broker.submit_bracket_order("NEW", 50, "buy", 19.0)                   # bought today: not entitled
    cash = broker.cash
    broker.pay_dividends({"AAA": 0.5, "SSS": 0.1, "NEW": 1.0}, held)
    assert broker.cash == pytest.approx(cash + 10 * 0.5 - 20 * 0.1)
    paid = [(f.ticker, f.side, f.qty, f.price, f.cost) for f in broker.fills if f.kind == DIVIDEND]
    assert paid == [("AAA", "buy", 10, 0.5, 0.0), ("SSS", "sell", 20, 0.1, 0.0)]
    assert broker.positions["AAA"].realised == pytest.approx(-1_000.0 - 1.0 + 5.0)
    assert broker.positions["SSS"].realised == pytest.approx(1_000.0 - 1.0 - 2.0)
    assert broker.positions["NEW"].realised == pytest.approx(-1_000.0 - 1.0)


def test_a_dividend_on_shares_stopped_out_at_the_ex_date_open_belongs_to_that_trade():
    """The ex-date's open is already net of the dividend, and the holder at
    the previous close is paid it -- even when its stop fills at that open,
    and even if the name is traded again the same day. The money is the
    closed trade's, not the new position's: otherwise a win rate reads a
    dividend as the next trade's gain (or a short's charge as its loss)."""
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.day = D2
    held = broker.held_quantities()
    broker.fill_gapped_stops({"AAA": 94.0})
    quotes["AAA"] = 94.0
    broker.submit_bracket_order("AAA", 5, "sell", 99.0)                   # a fresh short, same day
    broker.pay_dividends({"AAA": 0.5}, held)
    [trade] = broker.closed
    assert trade.pnl == pytest.approx(-1_000.0 - 1.0 + 940.0 - 0.94 + 5.0)
    assert broker.positions["AAA"].realised == pytest.approx(5 * 94.0 - 5 * 94.0 * COST)
    assert broker.cash == pytest.approx(100_000.0 + trade.pnl + broker.positions["AAA"].realised)


def test_average_entry_is_weighted_on_an_add_and_unchanged_on_a_reduction():
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.day = D2
    quotes["AAA"] = 110.0
    broker.submit_bracket_order("AAA", 5, "buy", 104.0)
    assert broker.positions["AAA"].avg_entry_price == pytest.approx((10 * 100.0 + 5 * 110.0) / 15)
    stop = broker.get_open_stop_order("AAA")                             # the add-on's own, 5 shares
    broker.replace_stop_order(stop.order_id, 1, 104.0, current_qty=5)
    broker.close_position_partially("AAA", 4)
    assert broker.positions["AAA"].qty == 11
    assert broker.positions["AAA"].avg_entry_price == pytest.approx(1_550.0 / 15)
    assert broker.positions["AAA"].opened == D1


def test_equity_is_cash_plus_signed_marks_and_gross_is_absolute():
    broker, quotes = book(AAA=100.0, SSS=50.0)
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.submit_bracket_order("SSS", 20, "sell", 55.0)
    quotes.update(AAA=120.0, SSS=40.0)
    assert broker.equity() == pytest.approx(broker.cash + 10 * 120.0 - 20 * 40.0)
    assert broker.gross() == pytest.approx(10 * 120.0 + 20 * 40.0)
    assert broker.get_equity() == pytest.approx(broker.equity())
    marks = {"AAA": 130.0, "SSS": 30.0}
    assert broker.equity(marks) == pytest.approx(broker.cash + 1_300.0 - 600.0)
    assert broker.gross(marks) == pytest.approx(1_300.0 + 600.0)
    positions = {p.ticker: p for p in broker.get_open_positions()}
    assert positions["AAA"] == OpenPosition("AAA", 10.0, 1_200.0, 100.0)
    assert positions["SSS"] == OpenPosition("SSS", -20.0, 800.0, 50.0)
    assert positions["SSS"].side == "sell" and positions["AAA"].side == "buy"


def test_a_position_with_no_bar_now_is_marked_at_its_last_close():
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.remember_marks({"AAA": 103.0})
    del quotes["AAA"]
    assert broker.equity() == pytest.approx(broker.cash + 1_030.0)
    assert broker.get_open_positions()[0].market_value == pytest.approx(1_030.0)


@pytest.mark.parametrize("cash", [0.0, -50.0])
def test_get_equity_refuses_an_account_that_is_not_worth_anything(cash):
    broker, _ = book(cash=cash)
    with pytest.raises(BrokerError, match="not positive"):
        broker.get_equity()


def test_get_equity_refuses_a_book_that_has_lost_everything():
    broker, quotes = book(cash=1_000.0)
    broker.submit_bracket_order("AAA", 10, "sell", 150.0)
    quotes["AAA"] = 300.0                                                  # a short gone badly wrong
    with pytest.raises(BrokerError):
        broker.get_equity()


def test_slippage_is_against_the_trader_on_both_sides():
    broker, _ = book()
    broker.slippage = 0.01
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    assert broker.fills[-1].price == pytest.approx(101.0)
    broker2, _ = book()
    broker2.slippage = 0.01
    broker2.submit_bracket_order("AAA", 10, "sell", 105.0)
    assert broker2.fills[-1].price == pytest.approx(99.0)


# --------------------------------------------------------------------------- #
# Stops against the tape
# --------------------------------------------------------------------------- #


def test_a_stop_already_through_the_market_fills_at_once_at_the_market():
    broker, quotes = book()
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    stop = broker.get_open_stop_order("AAA")
    broker.replace_stop_order(stop.order_id, 6, 95.0, current_qty=10)
    broker.day = D2
    quotes["AAA"] = 93.0
    broker.submit_stop_order("AAA", 4, "sell", 94.0)                      # through: fills at 93 now
    assert broker.positions["AAA"].qty == 6
    assert (broker.fills[-1].kind, broker.fills[-1].price, broker.fills[-1].gapped) == (STOP, 93.0, True)
    # A replace through the market does the same.
    stop = broker.get_open_stop_order("AAA")
    broker.replace_stop_order(stop.order_id, 6, 93.5, current_qty=6)
    assert broker.positions == {} and broker.fills[-1].price == 93.0


def test_a_stop_the_open_gaps_through_fills_at_the_open():
    broker, _ = book(AAA=100.0, SSS=50.0)
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.submit_bracket_order("SSS", 10, "sell", 55.0)
    broker.day = D2
    broker.fill_gapped_stops({"AAA": 96.0, "SSS": 54.0})                  # not through
    assert len(broker.live_stops()) == 2
    broker.fill_gapped_stops({"AAA": 95.0, "SSS": 56.5})                  # at and beyond
    assert broker.positions == {}
    fills = {f.ticker: (f.price, f.gapped, f.side) for f in broker.fills if f.kind == STOP}
    assert fills == {"AAA": (95.0, True, "sell"), "SSS": (56.5, True, "buy")}


def test_a_stop_the_session_touches_fills_at_the_stop_and_an_untouched_one_rests():
    broker, _ = book(AAA=100.0, SSS=50.0, CCC=10.0)
    broker.submit_bracket_order("AAA", 10, "buy", 95.0)
    broker.submit_bracket_order("SSS", 10, "sell", 55.0)
    broker.submit_bracket_order("CCC", 10, "buy", 9.0)
    broker.day = D2
    broker.fill_touched_stops({"AAA": 94.2, "SSS": 49.0, "CCC": 9.01},
                              {"AAA": 99.0, "SSS": 55.0, "CCC": 11.0})
    fills = {f.ticker: (f.price, f.gapped) for f in broker.fills if f.kind == STOP}
    assert fills == {"AAA": (95.0, False), "SSS": (55.0, False)}
    assert list(broker.positions) == ["CCC"]
    # A ticker with no bar today is not touched by anything.
    broker.fill_touched_stops({}, {})
    broker.fill_gapped_stops({})
    assert list(broker.positions) == ["CCC"]


def test_a_position_closed_to_zero_cancels_its_remaining_stops_so_none_can_open_one():
    broker, _ = book()
    broker.seed_position("AAA", 10, 100.0, D1, stops=[(10, 95.0), (10, 90.0)])
    broker.day = D2
    broker.fill_touched_stops({"AAA": 94.0}, {"AAA": 101.0})
    assert broker.positions == {} and broker.live_stops() == []
    assert broker.get_open_stop_order("AAA") is None
    broker.fill_touched_stops({"AAA": 80.0}, {"AAA": 101.0})              # the 90 stop is gone
    assert broker.positions == {}
    assert len([f for f in broker.fills if f.kind == STOP]) == 1


def test_the_closed_trades_pnl_is_every_cash_flow_of_that_position():
    broker, quotes = book(AAA=100.0, BBB=10.0)
    broker.submit_bracket_order("BBB", 100, "buy", 9.0)                   # another position, left open
    start = broker.cash
    broker.submit_bracket_order("AAA", 9, "buy", 95.0)
    broker.day = D2
    held = broker.held_quantities()
    broker.pay_dividends({"AAA": 1.0}, held)
    quotes["AAA"] = 104.0
    stop = broker.get_open_stop_order("AAA")
    broker.replace_stop_order(stop.order_id, 6, 100.0, current_qty=9)
    broker.close_position_partially("AAA", 3)
    broker.day = D3
    broker.fill_gapped_stops({"AAA": 99.0})
    [trade] = broker.closed
    assert trade.pnl == pytest.approx(broker.cash - start)
    assert trade.pnl == pytest.approx(-900.9 + 9.0 + (312.0 - 0.312) + (594.0 - 0.594))


# --------------------------------------------------------------------------- #
# The production manager on this broker
# --------------------------------------------------------------------------- #


class _Feed:
    def __init__(self, quotes: Quotes, atr: float) -> None:
        self.quotes, self.atr = quotes, atr

    def get_latest_price(self, ticker: str) -> float:
        return self.quotes(ticker)

    def get_atr(self, ticker: str) -> float:
        return self.atr


def test_the_real_ladder_protects_first_then_sells_within_this_brokers_reservations(tmp_path):
    """Rung 1 on a 9-share long: the stop is resized to 6 before 3 are sold.
    Were the order reversed, the stop would still hold all nine and the sale
    would be refused for want of free shares -- as it is live."""
    broker, quotes = book()
    audit = FundAudit("ladder")
    broker.submit_bracket_order("AAA", 9, "buy", 96.0)
    log_execution(LLMSignal(ticker="AAA", bias=Bias.BULLISH, conviction=0.6, rationale="r"),
                  ExecutionResult(status=ExecutionStatus.ACCEPTED, ticker="AAA", bias=Bias.BULLISH,
                                  conviction=0.6, reason="r", entry_price=100.0, stop_price=96.0),
                  logger=audit.logger)
    broker.day = D2
    quotes["AAA"] = 104.0
    manager = pm.PositionManager(broker, _Feed(quotes, atr=5.0), audit_path=audit, audit_logger=audit.logger)
    [action] = manager.manage().actions
    assert (action.action, action.qty_closed, action.remaining_qty, action.stop_qty) == (pm.TRANCHE_TAKEN, 3, 6, 6)
    assert broker.positions["AAA"].qty == 6 and stops_of(broker, "AAA") == [(6, 100.0, "sell")]

    # Out of order, the same broker refuses the sale -- the reservation is real.
    broker2, _ = book(AAA=104.0)
    broker2.submit_bracket_order("AAA", 9, "buy", 96.0)
    with pytest.raises(BrokerError, match="insufficient qty available"):
        broker2.close_position_partially("AAA", 3)
