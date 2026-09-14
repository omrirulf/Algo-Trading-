"""A closed market must cost nothing and trade nothing.

Two layers, deliberately. The engine gate is the safety property: no signal
opens a position into a closed session, however it arrived. The cycle gate is
the cost property: at an hourly cadence roughly two thirds of cycles fall
outside a session, and each one would otherwise spend a Bright Data request
and a model call per ticker.
"""

from __future__ import annotations


def completion(payload: dict | str, model: str = "claude-opus-5"):
    """A Completion the way call_llm now returns one, with plausible usage."""
    from orchestrator.llm import Completion
    from orchestrator.pricing import Usage

    text = payload if isinstance(payload, str) else json.dumps(payload)
    return Completion(
        text=text,
        usage=Usage(model=model, input_tokens=1420, output_tokens=1500),
    )

import json

import pytest

from app.execution_engine import ExecutionEngine
from app.schemas import Bias, ExecutionStatus, LLMSignal
from orchestrator import heartbeat as hb
from orchestrator.dispatch import DirectDispatcher
from tests.conftest import FakeBroker, FakeMarketData


def signal(ticker="AAPL", conviction=0.9):
    return LLMSignal(ticker=ticker, bias=Bias.BULLISH, conviction=conviction, rationale="because")


# --- the engine gate: the safety property --------------------------------


def test_a_closed_market_rejects_the_signal():
    engine = ExecutionEngine(broker=FakeBroker(market_open=False), market_data=FakeMarketData())
    result = engine.execute(signal())
    assert result.status is ExecutionStatus.REJECTED
    assert "market is closed" in result.reason


def test_an_open_market_still_trades():
    broker = FakeBroker(market_open=True)
    engine = ExecutionEngine(broker=broker, market_data=FakeMarketData())
    assert engine.execute(signal()).status is ExecutionStatus.ACCEPTED
    assert len(broker.submitted) == 1


def test_a_closed_market_submits_nothing():
    broker = FakeBroker(market_open=False)
    ExecutionEngine(broker=broker, market_data=FakeMarketData()).execute(signal())
    assert broker.submitted == []


def test_the_closed_check_runs_before_any_market_data_is_fetched():
    """A closed market should not even cost a quote."""

    class ExplodingMarketData:
        def get_latest_price(self, ticker):
            raise AssertionError("fetched a price for a closed market")

        def get_atr(self, ticker):
            raise AssertionError("fetched an ATR for a closed market")

    engine = ExecutionEngine(broker=FakeBroker(market_open=False), market_data=ExplodingMarketData())
    assert engine.execute(signal()).status is ExecutionStatus.REJECTED


def test_a_neutral_signal_is_still_rejected_as_neutral_when_closed():
    """Ordering check: NEUTRAL is reported as NEUTRAL, not mislabelled closed."""
    engine = ExecutionEngine(broker=FakeBroker(market_open=False), market_data=FakeMarketData())
    result = engine.execute(
        LLMSignal(ticker="AAPL", bias=Bias.NEUTRAL, conviction=0.9, rationale="r")
    )
    assert "NEUTRAL" in result.reason


# --- the cycle gate: the cost property -----------------------------------


def test_a_closed_market_skips_the_cycle_entirely(monkeypatch):
    """No news fetch, no model call -- that is the whole point.

    Counted rather than raised: ``process_ticker`` catches broad exceptions,
    so an AssertionError thrown from inside it would be swallowed and this
    test would pass even with the gate removed.
    """
    news_calls, llm_calls = [], []
    monkeypatch.setattr(hb, "fetch_news", lambda t: news_calls.append(t) or ["news"])
    monkeypatch.setattr(hb, "call_llm", lambda *a: llm_calls.append(a) or completion("{}"))
    monkeypatch.setattr(hb, "get_settings", lambda: _settings_with_watchlist("AAPL"))

    engine = ExecutionEngine(broker=FakeBroker(market_open=False), market_data=FakeMarketData())
    hb.run_cycle(dispatcher=DirectDispatcher(engine=engine))

    assert news_calls == []
    assert llm_calls == []


def test_an_open_market_runs_the_cycle(monkeypatch, _journal_to_tmp):
    calls = []
    monkeypatch.setattr(hb, "fetch_news", lambda t: calls.append(t) or ["news"])
    monkeypatch.setattr(
        hb, "call_llm",
        lambda s, u, j: completion({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.9, "rationale": "r"}),
    )
    monkeypatch.setattr(hb, "get_settings", lambda: _settings_with_watchlist("AAPL"))

    engine = ExecutionEngine(broker=FakeBroker(market_open=True), market_data=FakeMarketData())
    hb.run_cycle(dispatcher=DirectDispatcher(engine=engine))
    assert calls == ["AAPL"]


def _settings_with_watchlist(watchlist: str):
    from config.settings import Settings

    return Settings(watchlist=watchlist, _env_file=None)


def test_an_unreadable_clock_does_not_halt_trading(monkeypatch, caplog):
    """Failing closed here would mean one flaky call silently stops the system.

    The engine re-checks anyway, so continuing is safe; silently skipping
    every cycle because a clock call failed would not be.
    """
    from app.broker_client import BrokerError

    class BrokenClock(FakeBroker):
        def is_market_open(self):
            raise BrokerError("get_clock failed: connection reset")

    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    monkeypatch.setattr(
        hb, "call_llm",
        lambda s, u, j: completion({"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.1, "rationale": "r"}),
    )
    monkeypatch.setattr(hb, "get_settings", lambda: _settings_with_watchlist("AAPL"))

    engine = ExecutionEngine(broker=BrokenClock(), market_data=FakeMarketData())
    hb.run_cycle(dispatcher=DirectDispatcher(engine=engine))
    assert "could not read market clock" in caplog.text


# --- the clock comes from Alpaca, not a local guess ----------------------


def test_the_broker_reads_alpacas_clock():
    """A hand-rolled weekday check would miss holidays, half-days and DST."""
    from app import broker_client as bc

    class FakeClock:
        is_open = False

    class FakeClient:
        def get_clock(self):
            return FakeClock()

    broker = object.__new__(bc.AlpacaPaperBroker)
    broker._client = FakeClient()
    assert broker.is_market_open() is False

    FakeClock.is_open = True
    assert broker.is_market_open() is True


def test_a_clock_failure_becomes_a_broker_error():
    from app import broker_client as bc

    class FailingClient:
        def get_clock(self):
            raise RuntimeError("connection reset")

    broker = object.__new__(bc.AlpacaPaperBroker)
    broker._client = FailingClient()
    with pytest.raises(bc.BrokerError) as excinfo:
        broker.is_market_open()
    assert "get_clock failed" in str(excinfo.value)


# --- the --once entrypoint a scheduled job needs --------------------------


def _productive_cycle() -> hb.CycleReport:
    """A report from a cycle that did reach the engine, so --once exits 0."""
    return hb.CycleReport(
        tickers=("AAPL",),
        results=(hb.TickerResult("AAPL", hb.COMPLETED, status="REJECTED"),),
    )


def test_once_runs_a_single_cycle_and_returns(monkeypatch):
    """A cron job's process must terminate, or the run never finishes."""
    cycles = []

    def fake_cycle(*a, **k):
        cycles.append(1)
        return _productive_cycle()

    monkeypatch.setattr(hb, "run_cycle", fake_cycle)
    started = []
    monkeypatch.setattr(hb, "BlockingScheduler", lambda *a, **k: started.append(1))

    hb.main(["--once"])

    assert cycles == [1]
    assert started == [], "--once must not start the scheduler"
