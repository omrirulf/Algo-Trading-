"""The core: idle money is invested, inside the limits, and never in the way.

Three properties matter, in this order:

* the core can never refuse a signal its room -- every signal-side limit is
  computed on the book without it;
* the core never takes the account past a limit that bounds a loss -- gross,
  net stock-market risk, Duration;
* nothing treats a core holding as a trade -- no stop is placed on it, no
  ladder walks it, and no signal can name it.
"""

from __future__ import annotations

import json

import pytest

from app import core_book, risk_engine
from app.broker_client import BrokerError, DuplicateOrderError, OpenPosition
from app.core_book import CoreBook
from app.execution_engine import ExecutionEngine
from app.position_manager import PositionManager
from app.schemas import ExecutionStatus, LLMSignal
from config import settings as cfg
from config.instruments import (
    CORE_BILLS, CORE_BONDS, CORE_EQUITY, CORE_EQUITY_BETA, CORE_FUNDS, is_core,
)
from config.watchlist import DEFAULT_WATCHLIST
from tests.conftest import FakeBroker, FakeMarketData

EQUITY = 100_000.0


def pos(ticker: str, value: float, price: float = 100.0, short: bool = False) -> OpenPosition:
    qty = value / price
    return OpenPosition(ticker, -qty if short else qty, value, price)


def sig(**over) -> LLMSignal:
    base = {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.8, "rationale": "test"}
    return LLMSignal.model_validate({**base, **over})


def bought(broker: FakeBroker) -> dict[str, int]:
    return {o["ticker"]: o["qty"] for o in broker.core_bought}


def sold(broker: FakeBroker) -> dict[str, int]:
    return {o["ticker"]: o["qty"] for o in broker.closed}


# --- the roster -------------------------------------------------------------


def test_no_core_fund_is_on_the_watchlist():
    """A shared ticker would merge the two books at the broker."""
    assert not set(CORE_FUNDS) & {t.upper() for t in DEFAULT_WATCHLIST}


def test_is_core_is_exactly_the_three_funds():
    assert all(is_core(t) for t in CORE_FUNDS)
    assert is_core(" vt ") and not is_core("RSP") and not is_core("AAPL")


# --- the targets ------------------------------------------------------------


def test_an_empty_book_is_split_by_the_equity_share_and_fills_the_gross_cap():
    targets = risk_engine.core_targets(EQUITY, [])
    gross = EQUITY * cfg.MAX_GROSS_EXPOSURE_PCT
    assert targets[CORE_EQUITY] == pytest.approx(gross * cfg.CORE_EQUITY_SHARE)
    assert targets[CORE_BONDS] == pytest.approx(min(gross - targets[CORE_EQUITY], EQUITY * 0.30))
    assert sum(targets.values()) == pytest.approx(gross)


def test_the_targets_always_sum_to_what_the_signal_book_left():
    book = [pos("NVDA", 5_000), pos("XLE", 7_000), pos("TLT", 12_000), pos("GLD", 4_000)]
    targets = risk_engine.core_targets(EQUITY, book)
    assert sum(targets.values()) == pytest.approx(EQUITY * cfg.MAX_GROSS_EXPOSURE_PCT - 28_000)
    assert all(v >= 0 for v in targets.values())


def test_world_equity_is_cut_to_the_stock_market_limit():
    """The core fills the limit; it does not raise it."""
    # 50% of the account in beta-1.00 stock funds leaves 10% under the 60% limit.
    book = [pos("VGK", 12_000), pos("EWP", 7_000), pos("EWU", 7_000), pos("EWC", 7_000),
            pos("VWO", 12_000), pos("EPOL", 5_000)]
    used = risk_engine.net_equity_risk(book)
    targets = risk_engine.core_targets(EQUITY, book)
    assert targets[CORE_EQUITY] == pytest.approx(
        (EQUITY * cfg.MAX_EQUITY_RISK_PCT - used) / CORE_EQUITY_BETA)
    with_core = used + targets[CORE_EQUITY] * CORE_EQUITY_BETA
    assert with_core <= EQUITY * cfg.MAX_EQUITY_RISK_PCT + 1e-6


def test_a_book_at_the_stock_market_limit_gets_no_world_equity():
    book = [pos(t, 12_000) for t in ("VGK", "VWO")] + [pos(t, 7_000) for t in (
        "EWP", "EWU", "EWC", "EWG", "EWN", "EWI")]
    assert risk_engine.net_equity_risk(book) >= EQUITY * cfg.MAX_EQUITY_RISK_PCT
    assert risk_engine.core_targets(EQUITY, book)[CORE_EQUITY] == 0.0


def test_bonds_are_cut_to_what_the_duration_ceiling_has_left():
    book = [pos("TLT", 12_000), pos("IEF", 12_000)]
    targets = risk_engine.core_targets(EQUITY, book)
    assert targets[CORE_BONDS] == pytest.approx(EQUITY * 0.30 - 24_000)


def test_the_rate_risk_of_credit_funds_counts_against_the_bond_leg():
    """EMB is not a Duration member, and still owes that ceiling 65% of itself."""
    plain = risk_engine.core_targets(EQUITY, [pos("GLD", 4_000)])[CORE_BONDS]
    with_emb = risk_engine.core_targets(EQUITY, [pos("EMB", 4_000)])[CORE_BONDS]
    assert plain - with_emb == pytest.approx(4_000 * 0.65)


def test_bills_take_whatever_the_two_limits_pushed_out():
    # Stock limit full and Duration full: everything left is bills.
    book = [pos(t, 12_000) for t in ("VGK", "VWO")] + [pos(t, 7_000) for t in (
        "EWP", "EWU", "EWC", "EWG", "EWN", "EWI")] + [pos("TLT", 12_000), pos("IEF", 12_000), pos("SHY", 6_000)]
    targets = risk_engine.core_targets(EQUITY, book)
    assert targets[CORE_EQUITY] == 0.0 and targets[CORE_BONDS] == 0.0
    assert targets[CORE_BILLS] == pytest.approx(
        max(0.0, EQUITY * cfg.MAX_GROSS_EXPOSURE_PCT - sum(p.market_value for p in book)))


def test_a_full_signal_book_leaves_the_core_nothing():
    book = [pos("X%d" % i, 9_500) for i in range(10)]
    assert sum(risk_engine.core_targets(EQUITY, book).values()) == 0.0


def test_a_short_stock_position_makes_room_for_more_world_equity():
    long_only = risk_engine.core_ceilings(EQUITY, [pos("VGK", 12_000)])[1]
    hedged = risk_engine.core_ceilings(EQUITY, [pos("VGK", 12_000), pos("EWG", 7_000, short=True)])[1]
    assert hedged > long_only


def test_without_core_drops_only_the_core_funds():
    book = [pos("RSP", 1), pos(CORE_EQUITY, 1), pos(CORE_BONDS, 1), pos(CORE_BILLS, 1), pos("TLT", 1)]
    assert [p.ticker for p in risk_engine.without_core(book)] == ["RSP", "TLT"]


# --- the pass ---------------------------------------------------------------


def test_idle_cash_is_invested_up_to_the_gross_cap():
    broker, market = FakeBroker(equity=EQUITY), FakeMarketData(price=100.0)
    report = CoreBook(broker, market).rebalance()

    orders = bought(broker)
    assert set(orders) == set(CORE_FUNDS) and broker.closed == []
    invested = sum(orders.values()) * 100.0
    assert invested <= EQUITY * cfg.MAX_GROSS_EXPOSURE_PCT
    assert invested >= EQUITY * 0.94
    assert report.invested_pct == pytest.approx(invested / EQUITY)
    assert report.errors == 0


def test_the_account_ends_above_ninety_percent_invested_whatever_the_book():
    """The owner's requirement, stated as the property it is."""
    books = [
        [],
        [pos("NVDA", 5_000), pos("MSFT", 5_000), pos("XLE", 7_000)],
        [pos("VGK", 12_000), pos("VWO", 12_000), pos("TLT", 12_000), pos("IEF", 12_000)],
        [pos("NVDA", 5_000, short=True), pos("GLD", 4_000)],
    ]
    for book in books:
        broker = FakeBroker(equity=EQUITY, positions=list(book))
        report = CoreBook(broker, FakeMarketData(price=100.0)).rebalance()
        assert 0.90 <= report.invested_pct <= cfg.MAX_GROSS_EXPOSURE_PCT + 1e-9, book


def test_the_core_is_sold_down_when_the_signal_book_grows():
    # Yesterday: an empty signal book, the core at its targets.
    core = [pos(CORE_EQUITY, 57_000), pos(CORE_BONDS, 30_000), pos(CORE_BILLS, 8_000)]
    # Today: the signals bought 20% of the account in stock funds.
    signals = [pos("VGK", 12_000), pos("EWG", 7_000)]
    broker = FakeBroker(equity=EQUITY, positions=core + signals)
    report = CoreBook(broker, FakeMarketData()).rebalance()

    assert broker.closed, "the core had to make room"
    after = {p.ticker: p.market_value for p in broker.positions}
    total = sum(after.values()) + sum(o["qty"] * 100.0 for o in broker.core_bought)
    assert total <= EQUITY * cfg.MAX_GROSS_EXPOSURE_PCT + EQUITY * cfg.CORE_REBALANCE_BAND_PCT * 2
    stock_risk = risk_engine.net_equity_risk(signals) + after[CORE_EQUITY] * CORE_EQUITY_BETA
    assert stock_risk <= EQUITY * (cfg.MAX_EQUITY_RISK_PCT + cfg.CORE_REBALANCE_BAND_PCT)
    assert report.errors == 0


def test_sells_go_in_before_buys():
    calls: list[str] = []

    class Ordered(FakeBroker):
        def close_position_partially(self, ticker, qty):
            calls.append("sell")
            return super().close_position_partially(ticker, qty)

        def submit_core_order(self, ticker, qty):
            calls.append("buy")
            return super().submit_core_order(ticker, qty)

    # Too much world equity, too few bills.
    broker = Ordered(equity=EQUITY, positions=[pos(CORE_EQUITY, 80_000)])
    CoreBook(broker, FakeMarketData()).rebalance()
    assert "sell" in calls and "buy" in calls
    assert calls == sorted(calls, key=lambda c: c != "sell")


def test_a_fund_inside_the_band_is_left_alone():
    targets = risk_engine.core_targets(EQUITY, [])
    drift = EQUITY * cfg.CORE_REBALANCE_BAND_PCT * 0.5
    core = [pos(CORE_EQUITY, targets[CORE_EQUITY] - drift), pos(CORE_BONDS, targets[CORE_BONDS] + drift),
            pos(CORE_BILLS, targets[CORE_BILLS])]
    broker = FakeBroker(equity=EQUITY, positions=core)
    report = CoreBook(broker, FakeMarketData()).rebalance()
    assert broker.core_bought == [] and broker.closed == []
    assert {a.action for a in report.actions} == {core_book.HELD}


def test_no_buy_takes_the_account_over_the_gross_cap():
    """A fund left above target inside the band still occupies the room."""
    targets = risk_engine.core_targets(EQUITY, [])
    over = EQUITY * cfg.CORE_REBALANCE_BAND_PCT * 0.9
    core = [pos(CORE_EQUITY, targets[CORE_EQUITY] + over), pos(CORE_BONDS, targets[CORE_BONDS] + over)]
    broker = FakeBroker(equity=EQUITY, positions=core)
    CoreBook(broker, FakeMarketData()).rebalance()
    total = sum(p.market_value for p in broker.positions) + sum(o["qty"] * 100.0 for o in broker.core_bought)
    assert total <= EQUITY * cfg.MAX_GROSS_EXPOSURE_PCT + 1e-6


def test_an_order_the_broker_has_not_shown_yet_still_counts():
    """The position list lags the fills; the engine's own record does not."""
    pending = [pos("VGK", 12_000), pos("TLT", 12_000)]
    seen = FakeBroker(equity=EQUITY, positions=list(pending))
    lagging = FakeBroker(equity=EQUITY)

    CoreBook(seen, FakeMarketData()).rebalance()
    CoreBook(lagging, FakeMarketData()).rebalance(pending=pending)

    assert bought(lagging) == bought(seen)


def test_a_pending_order_already_in_the_list_is_not_counted_twice():
    book = [pos("VGK", 12_000)]
    once = FakeBroker(equity=EQUITY, positions=list(book))
    twice = FakeBroker(equity=EQUITY, positions=list(book))
    CoreBook(once, FakeMarketData()).rebalance()
    CoreBook(twice, FakeMarketData()).rebalance(pending=book)
    assert bought(twice) == bought(once)


def test_a_closed_market_touches_nothing():
    broker = FakeBroker(equity=EQUITY, market_open=False)
    report = CoreBook(broker, FakeMarketData()).rebalance()
    assert report.market_closed and broker.core_bought == [] and broker.closed == []


def test_one_refused_order_does_not_stop_the_other_funds():
    class Refusing(FakeBroker):
        def submit_core_order(self, ticker, qty):
            if ticker == CORE_EQUITY:
                raise BrokerError("insufficient buying power")
            return super().submit_core_order(ticker, qty)

    broker = Refusing(equity=EQUITY)
    report = CoreBook(broker, FakeMarketData()).rebalance()
    assert report.errors == 1
    assert set(bought(broker)) == {CORE_BONDS, CORE_BILLS}


def test_a_second_pass_on_the_same_day_is_not_an_error():
    class AlreadyBought(FakeBroker):
        def submit_core_order(self, ticker, qty):
            raise DuplicateOrderError("client_order_id must be unique")

    report = CoreBook(AlreadyBought(equity=EQUITY), FakeMarketData()).rebalance()
    assert report.errors == 0
    assert all(a.action == core_book.HELD for a in report.actions)


def test_a_broker_that_cannot_be_read_is_reported_not_raised():
    class Down(FakeBroker):
        def get_equity(self):
            raise BrokerError("get_account failed")

    report = CoreBook(Down(), FakeMarketData()).rebalance()
    assert report.errors == 1 and "get_account failed" in report.actions[0].reason


def test_every_action_is_one_audit_line(_audit_log_to_tmp):
    CoreBook(FakeBroker(equity=EQUITY), FakeMarketData()).rebalance()
    records = [json.loads(line) for line in _audit_log_to_tmp.read_text().splitlines()]
    core = [r for r in records if (r.get("event") or r.get("message")) == core_book.EVENT]
    assert {r["action"]["ticker"] for r in core} == set(CORE_FUNDS)
    assert all(r["action"]["action"] == core_book.BOUGHT for r in core)


def test_the_core_pass_never_touches_a_signal_position():
    signals = [pos("NVDA", 5_000), pos("TLT", 12_000)]
    broker = FakeBroker(equity=EQUITY, positions=list(signals) + [pos(CORE_EQUITY, 90_000)])
    CoreBook(broker, FakeMarketData()).rebalance()
    assert all(is_core(o["ticker"]) for o in broker.closed + broker.core_bought)
    assert broker.submitted == [] and broker.replaced == [] and broker.protected == []


def test_the_fake_broker_refuses_a_core_order_for_anything_else():
    with pytest.raises(BrokerError):
        FakeBroker().submit_core_order("RSP", 1)


# --- the signal book does not see the core ----------------------------------


def core_engine(broker, market) -> ExecutionEngine:
    return ExecutionEngine(broker, market, core=True)


def test_a_full_core_never_refuses_a_signal():
    """95% of the account in the core, and the signal is sized as if it were cash."""
    core = [pos(CORE_EQUITY, 57_000), pos(CORE_BONDS, 30_000), pos(CORE_BILLS, 8_000)]
    with_core = FakeBroker(equity=EQUITY, positions=core)
    without = FakeBroker(equity=EQUITY)
    market = FakeMarketData()

    a = core_engine(with_core, market).execute(sig())
    b = core_engine(without, market).execute(sig())

    assert a.status is ExecutionStatus.ACCEPTED
    assert a.quantity == b.quantity == 50


def test_core_holdings_do_not_use_up_the_position_count():
    core = [pos(t, 1_000) for t in CORE_FUNDS]
    others = [pos(f"T{i}", 100) for i in range(cfg.MAX_OPEN_POSITIONS - 1)]
    broker = FakeBroker(equity=EQUITY, positions=core + others)
    assert core_engine(broker, FakeMarketData()).execute(sig()).status is ExecutionStatus.ACCEPTED


def test_a_signal_cannot_trade_a_core_fund():
    broker = FakeBroker(equity=EQUITY)
    for bias in ("BULLISH", "BEARISH", "NEUTRAL"):
        result = core_engine(broker, FakeMarketData()).execute(sig(ticker=CORE_EQUITY, bias=bias))
        assert result.status is ExecutionStatus.REJECTED
        assert "core holding" in result.reason
    assert broker.submitted == []


def test_an_engine_built_without_the_core_is_unchanged():
    """The simulated books build the engine with neither switch."""
    core = [pos(CORE_EQUITY, 95_000)]
    broker = FakeBroker(equity=EQUITY, positions=core)
    result = ExecutionEngine(broker, FakeMarketData()).execute(sig())
    assert result.status is ExecutionStatus.REJECTED and "gross exposure" in result.reason


def test_the_engine_remembers_what_it_just_accepted():
    broker = FakeBroker(equity=EQUITY)
    engine = core_engine(broker, FakeMarketData())
    assert engine.recent_orders() == []
    engine.execute(sig())
    engine.execute(sig(ticker="XOM", bias="BEARISH"))
    recent = {p.ticker: p for p in engine.recent_orders()}
    assert recent["AAPL"].market_value == 5_000.0 and recent["AAPL"].side == "buy"
    assert recent["XOM"].side == "sell"


def test_a_rejected_signal_is_not_remembered():
    engine = core_engine(FakeBroker(equity=EQUITY), FakeMarketData())
    engine.execute(sig(conviction=0.0))
    assert engine.recent_orders() == []


# --- the position manager leaves the core alone ------------------------------


def test_the_position_manager_places_no_stop_on_a_core_fund(_audit_log_to_tmp):
    """Left in the manager's list, a core fund would be 'found without a stop'."""
    broker = FakeBroker(equity=EQUITY, positions=[pos(t, 10_000) for t in CORE_FUNDS])
    for protect_only in (False, True):
        report = PositionManager(broker, FakeMarketData(), audit_path=_audit_log_to_tmp).manage(
            protect_only=protect_only)
        assert report.actions == () and report.positions_seen == 0
    assert broker.protected == [] and broker.closed == [] and broker.stop_orders == {}


def test_core_bonds_are_not_trimmed_as_an_over_cap_duration_group(_audit_log_to_tmp):
    """The bond leg is sized by the core pass, not by the manager's group trim."""
    broker = FakeBroker(equity=EQUITY, positions=[pos(CORE_BONDS, 60_000)])
    PositionManager(broker, FakeMarketData(), audit_path=_audit_log_to_tmp).manage()
    assert broker.closed == []


# --- how the core funds read in a report -------------------------------------


def test_the_core_funds_report_as_their_own_group_not_as_ungrouped():
    from config.instruments import CORE_GROUP, EXPOSURE_GROUPS, group_for

    assert {group_for(t) for t in CORE_FUNDS} == {CORE_GROUP}
    assert CORE_GROUP not in EXPOSURE_GROUPS, "a name for reports, not a group with a cap"


def test_only_world_equity_counts_as_stock_market_risk():
    """An unrecognised ticker fails closed to beta 1.0; a bond or bill fund must not."""
    from config.instruments import equity_risk_beta

    assert equity_risk_beta(CORE_EQUITY) == CORE_EQUITY_BETA
    assert equity_risk_beta(CORE_BONDS) is None and equity_risk_beta(CORE_BILLS) is None
    book = [pos(CORE_EQUITY, 30_000), pos(CORE_BONDS, 30_000), pos(CORE_BILLS, 30_000)]
    assert risk_engine.net_equity_risk(book) == pytest.approx(30_000 * CORE_EQUITY_BETA)
