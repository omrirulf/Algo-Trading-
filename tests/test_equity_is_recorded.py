"""Every decision the engine makes after reading the account records the equity it saw.

Asked for on 17 Sep 2026: the audit log said what was traded but not what
the book was worth at the time, so a return had nothing to be measured
against. Now it does -- on the trade, and on the refusal that came after the
account was read. A refusal that never consulted the account says None,
because a number the engine did not use would be a claim it cannot back.
"""

from __future__ import annotations

import json

from app.broker_client import OpenPosition
from app.execution_engine import ExecutionEngine
from app.schemas import ExecutionStatus, LLMSignal
from config import settings as cfg
from orchestrator import dispatch
from tests.conftest import FakeBroker, FakeMarketData


def sig(**over) -> LLMSignal:
    base = {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.8, "rationale": "test"}
    return LLMSignal.model_validate({**base, **over})


def engine(broker, market):
    return ExecutionEngine(broker=broker, market_data=market)


def test_an_accepted_trade_records_the_equity_it_was_sized_against(_audit_log_to_tmp):
    broker, market = FakeBroker(equity=123_456.0), FakeMarketData(price=100.0, atr=2.0)
    r = engine(broker, market).execute(sig())
    assert r.status is ExecutionStatus.ACCEPTED
    assert r.equity == 123_456.0
    [line] = [json.loads(l) for l in _audit_log_to_tmp.read_text().splitlines() if l.strip()]
    assert line["result"]["equity"] == 123_456.0


def test_a_refusal_after_the_account_was_read_records_it_too(_audit_log_to_tmp):
    broker, market = FakeBroker(equity=50_000.0), FakeMarketData(price=100.0, atr=2.0)
    broker.positions = [OpenPosition(f"T{i}", 1, 100.0) for i in range(cfg.MAX_OPEN_POSITIONS)]
    r = engine(broker, market).execute(sig(ticker="NEWCO"))
    assert r.status is ExecutionStatus.REJECTED and "positions" in r.reason
    assert r.equity == 50_000.0


def test_a_refusal_before_the_account_was_read_says_none(_audit_log_to_tmp):
    broker, market = FakeBroker(equity=50_000.0), FakeMarketData()
    neutral = engine(broker, market).execute(sig(bias="NEUTRAL"))
    assert neutral.status is ExecutionStatus.REJECTED and neutral.equity is None
    broker.market_open = False
    closed = engine(broker, market).execute(sig())
    assert closed.status is ExecutionStatus.REJECTED and closed.equity is None


def test_the_journal_outcome_carries_the_equity(_audit_log_to_tmp):
    broker, market = FakeBroker(equity=77_000.0), FakeMarketData(price=100.0, atr=2.0)
    outcome = dispatch.DirectDispatcher(engine=engine(broker, market)).dispatch(sig())
    assert outcome["status"] == "ACCEPTED" and outcome["equity"] == 77_000.0
