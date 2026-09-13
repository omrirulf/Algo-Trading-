"""End-to-end decision path with fake broker + market data."""

from __future__ import annotations

import json

from app.broker_client import BrokerError, OpenPosition
from app.execution_engine import ExecutionEngine
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
    decorated = engine.execute(sig(**EXTREME_SCORES))

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
