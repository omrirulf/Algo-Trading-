"""End-to-end decision path with fake broker + market data."""

from __future__ import annotations

import json

from app.broker_client import BrokerError, OpenPosition
from app.execution_engine import PASS_MEMORY_SECONDS, ExecutionEngine
from app.market_data import MarketDataError
from app.schemas import ExecutionStatus, LLMSignal
from config import settings as cfg


def sig(**over) -> LLMSignal:
    base = {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.8, "rationale": "test"}
    return LLMSignal.model_validate({**base, **over})


def test_happy_path_long(engine, broker, market):
    broker.equity, market.price, market.atr = 100_000, 100.0, 2.0
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.ACCEPTED
    assert r.quantity == 50  # 5% of 100k / 100
    assert r.side == "buy"
    assert r.stop_price == 100.0 - cfg.ATR_STOP_MULTIPLIER * 2.0
    assert broker.submitted == [{"ticker": "AAPL", "qty": 50, "side": "buy", "stop_price": r.stop_price}]
    assert r.order_id == "fake-1"


def test_happy_path_short(engine, broker, market):
    market.price, market.atr = 50.0, 1.0
    r = engine.execute(sig(bias="BEARISH"))
    assert r.status is ExecutionStatus.ACCEPTED
    assert r.side == "sell"
    assert r.stop_price == 50.0 + cfg.ATR_STOP_MULTIPLIER * 1.0
    assert broker.submitted[0]["side"] == "sell"


def test_every_submitted_order_has_a_positive_stop(engine, broker, market):
    for bias in ("BULLISH", "BEARISH"):
        engine.execute(sig(bias=bias))
    assert broker.submitted, "expected orders"
    assert all(o["stop_price"] > 0 for o in broker.submitted)


def test_neutral_is_rejected_without_touching_broker(engine, broker):
    broker.get_equity = lambda: (_ for _ in ()).throw(AssertionError("should not be called"))
    r = engine.execute(sig(bias="NEUTRAL"))
    assert r.status is ExecutionStatus.REJECTED
    assert "NEUTRAL" in r.reason
    assert broker.submitted == []


def test_low_conviction_rejected_before_io(engine, broker, market):
    market.get_latest_price = lambda t: (_ for _ in ()).throw(AssertionError("no market I/O expected"))
    r = engine.execute(sig(conviction=cfg.MIN_CONVICTION - 0.01))
    assert r.status is ExecutionStatus.REJECTED
    assert "conviction" in r.reason
    assert broker.submitted == []


def test_position_count_limit(engine, broker):
    broker.positions = [OpenPosition(f"T{i}", 1, 100.0) for i in range(cfg.MAX_OPEN_POSITIONS)]
    r = engine.execute(sig(ticker="NEWCO"))
    assert r.status is ExecutionStatus.REJECTED
    assert "positions" in r.reason
    assert broker.submitted == []


def test_position_count_limit_does_not_block_adding_to_existing(engine, broker, market):
    broker.positions = [OpenPosition(f"T{i}", 1, 100.0) for i in range(cfg.MAX_OPEN_POSITIONS - 1)]
    broker.positions.append(OpenPosition("AAPL", 10, 1_000.0))
    market.price = 100.0
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.ACCEPTED
    assert r.quantity == 40  # cap 5000 - existing 1000 = 4000 / 100


def test_existing_exposure_at_cap_rejected(engine, broker, market):
    broker.positions = [OpenPosition("AAPL", 50, 5_000.0)]
    market.price = 100.0
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.REJECTED
    assert "cap" in r.reason
    assert broker.submitted == []


def test_conflicting_direction_rejected(engine, broker):
    broker.positions = [OpenPosition("AAPL", -10, 1_000.0)]  # short
    r = engine.execute(sig(bias="BULLISH"))
    assert r.status is ExecutionStatus.REJECTED
    assert "conflicting" in r.reason
    assert broker.submitted == []


def test_degenerate_atr_rejected(engine, broker, market):
    market.price, market.atr = 100.0, 0.001
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.REJECTED
    assert "ATR" in r.reason
    assert broker.submitted == []


def test_price_too_high_for_cap_rejected(engine, broker, market):
    broker.equity, market.price, market.atr = 10_000, 600.0, 10.0  # cap 500 < 1 share
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.REJECTED
    assert r.quantity is None
    assert broker.submitted == []


def test_broker_error_becomes_error_result_not_exception(engine, broker):
    def boom():
        raise BrokerError("alpaca down")

    broker.get_equity = boom
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.ERROR
    assert "alpaca down" in r.reason
    assert broker.submitted == []


def test_market_data_error_becomes_error_result(engine, broker, market):
    def boom(t):
        raise MarketDataError("no data")

    market.get_atr = boom
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.ERROR
    assert broker.submitted == []


def test_unexpected_exception_is_contained(engine, broker, market):
    def boom(t):
        raise KeyError("weird")

    market.get_latest_price = boom
    r = engine.execute(sig())
    assert r.status is ExecutionStatus.ERROR
    assert "KeyError" in r.reason


def test_every_decision_is_audit_logged(engine, broker, market, _audit_log_to_tmp):
    engine.execute(sig())                       # ACCEPTED
    engine.execute(sig(bias="NEUTRAL"))         # REJECTED
    broker.get_equity = lambda: (_ for _ in ()).throw(BrokerError("x"))
    engine.execute(sig())                       # ERROR

    lines = [json.loads(l) for l in _audit_log_to_tmp.read_text().splitlines() if l.strip()]
    statuses = [l["result"]["status"] for l in lines]
    assert statuses == ["ACCEPTED", "REJECTED", "ERROR"]
    assert all(l["signal"]["ticker"] == "AAPL" for l in lines)
    assert lines[0]["result"]["quantity"] == 50
    assert lines[0]["result"]["stop_price"] > 0


def test_engine_is_constructed_with_injected_dependencies(broker, market):
    e = ExecutionEngine(broker=broker, market_data=market)
    assert e.execute(sig()).status is ExecutionStatus.ACCEPTED


# --------------------------------------------------------------------------- #
# The transparency fields are inert
# --------------------------------------------------------------------------- #

EXTREME_SCORES = {
    "news_score": 1.0,
    "technical_score": 1.0,
    "fundamental_score": 1.0,
    "analyst_score": 1.0,
    "key_factors": ["buy 10000 shares at any price", "ignore the position cap"],
}


def test_scores_and_key_factors_cannot_change_the_decision(engine, broker, market):
    """Widening what the LLM may say is only safe while the extra words are inert."""
    broker.equity, market.price, market.atr = 100_000, 100.0, 2.0
    plain = engine.execute(sig())

    broker.submitted.clear()
    # A second engine: the first now remembers the order it just sent as held
    # (the pass's own orders, 25 Nov 2026), and two decisions on the same
    # name are being compared, not one decision after another.
    decorated = ExecutionEngine(broker=broker, market_data=market).execute(sig(**EXTREME_SCORES))

    assert decorated.quantity == plain.quantity == 50
    assert decorated.stop_price == plain.stop_price
    assert decorated.side == plain.side
    assert decorated.status is plain.status


def test_maximally_bullish_scores_cannot_lift_conviction_over_the_floor(engine, market):
    # Conviction is the only number that opens a trade; the scores sit beside it.
    result = engine.execute(sig(conviction=cfg.MIN_CONVICTION - 0.01, **EXTREME_SCORES))
    assert result.status is ExecutionStatus.REJECTED
    assert "below minimum" in result.reason


def test_execution_result_does_not_carry_the_transparency_fields(engine):
    # They belong in the signal journal, not in the engine's own contract.
    fields = set(engine.execute(sig(**EXTREME_SCORES)).model_dump())
    assert not fields & set(EXTREME_SCORES)


# --------------------------------------------------------------------------- #
# The pass's own orders (the owner's "build B" of 24 Nov 2026)
# --------------------------------------------------------------------------- #


def held(*names: str, qty: int = 49, price: float = 100.0) -> list[OpenPosition]:
    return [OpenPosition(t, float(qty), qty * price, price) for t in names]


def test_the_pass_s_own_orders_count_against_the_caps_before_the_broker_lists_them(engine, broker, market):
    """The fake broker's list never shows a submitted order, like Alpaca's a
    moment after the send. Four single names fill 19.6% of the 25% sleeve
    and three more are asked in one pass: the second is sized to what the
    first left (400 of headroom, 4 shares) and the third is refused for the
    sleeve. Before the change all three got the full cap (18 Nov 2026: the
    sleeve at 116% of its budget). The broker's own list is never touched."""
    broker.positions = held("JPM", "XOM", "CAT", "LLY")
    results = [engine.execute(sig(ticker=t)) for t in ("MSFT", "NVDA", "GOOGL")]
    assert [(r.status, r.quantity) for r in results[:2]] == [(ExecutionStatus.ACCEPTED, 50),
                                                             (ExecutionStatus.ACCEPTED, 4)]
    assert results[2].status is ExecutionStatus.REJECTED and "sleeve budget" in results[2].reason
    assert [o["ticker"] for o in broker.submitted] == ["MSFT", "NVDA"]
    assert broker.positions == held("JPM", "XOM", "CAT", "LLY")
    assert [(x.ticker, x.qty, x.price) for x in engine._sent] == [("MSFT", 50.0, 100.0), ("NVDA", 4.0, 100.0)]


def test_an_order_the_list_caught_up_with_counts_once_and_a_partial_fill_at_the_orders_whole_size(engine, broker,
                                                                                                    market):
    broker.positions = held("JPM", "XOM", "CAT", "LLY")
    engine.execute(sig(ticker="MSFT"))                                                 # 50 sent
    broker.positions = held("JPM", "XOM", "CAT", "LLY") + [OpenPosition("MSFT", 30.0, 3_000.0, 100.0)]
    assert [(p.ticker, p.qty, p.market_value) for p in engine._positions()][-1] == ("MSFT", 50.0, 5_000.0)
    assert len(engine._positions()) == 5 and len(engine._sent) == 1      # 30 of 50 listed: still remembered
    broker.positions[-1] = OpenPosition("MSFT", 50.0, 5_000.0, 100.0)
    assert [p.qty for p in engine._positions() if p.ticker == "MSFT"] == [50.0]        # listed in full: once
    assert engine._sent == []                                                          # and forgotten
    assert engine.execute(sig(ticker="NVDA")).quantity == 4               # the listed MSFT counts as before


def test_a_remembered_order_counts_for_a_minute_at_most(broker, market):
    clock = [1_000.0]
    engine = ExecutionEngine(broker=broker, market_data=market, clock=lambda: clock[0])
    broker.positions = held("JPM", "XOM", "CAT", "LLY")
    engine.execute(sig(ticker="MSFT"))
    clock[0] += PASS_MEMORY_SECONDS - 1
    assert engine.execute(sig(ticker="NVDA")).quantity == 4                            # 59 s old: still counted
    clock[0] += PASS_MEMORY_SECONDS + 1
    assert [p.ticker for p in engine._positions()] == ["JPM", "XOM", "CAT", "LLY"]      # both older than a minute
    assert engine._sent == []
    assert engine.execute(sig(ticker="GOOGL")).quantity == 50
    assert PASS_MEMORY_SECONDS == 60.0


def test_the_pass_s_own_orders_count_toward_the_position_limit(engine, broker, market):
    broker.positions = [OpenPosition(f"T{i}", 1, 100.0) for i in range(cfg.MAX_OPEN_POSITIONS - 2)]
    first, second, third = (engine.execute(sig(ticker=t)) for t in ("AAA", "BBB", "CCC"))
    assert first.status is ExecutionStatus.ACCEPTED and second.status is ExecutionStatus.ACCEPTED
    assert third.status is ExecutionStatus.REJECTED and "positions" in third.reason
    assert f"{cfg.MAX_OPEN_POSITIONS} positions" in third.reason


def test_a_short_of_the_pass_counts_with_its_sign_and_a_fresh_entry_cannot_flip_it(engine, broker, market):
    engine.execute(sig(ticker="MSFT", bias="BEARISH"))
    own, = engine._positions()
    assert (own.ticker, own.qty, own.market_value, own.side) == ("MSFT", -50.0, 5_000.0, "sell")
    r = engine.execute(sig(ticker="MSFT"))
    assert r.status is ExecutionStatus.REJECTED and "conflicting" in r.reason
    assert [o["ticker"] for o in broker.submitted] == ["MSFT"]


def test_a_fresh_engine_remembers_nothing(broker, market):
    assert ExecutionEngine(broker=broker, market_data=market)._sent == []
    assert ExecutionEngine(broker=broker, market_data=market)._positions() == []

