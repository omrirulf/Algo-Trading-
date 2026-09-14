"""Delivering a signal without a webhook must not loosen the boundary.

The property under test is that ``direct`` mode is a *transport* change, not
a safety change: the same closed schema, the same engine-owned sizing, the
same rejection for the same reason.
"""

from __future__ import annotations

import json

import httpx
import pytest

from app.schemas import Bias, ExecutionStatus, LLMSignal
from config.settings import Settings
from orchestrator import dispatch
from orchestrator.dispatch import (
    DIRECT,
    WEBHOOK,
    DirectDispatcher,
    WebhookDispatcher,
    build_dispatcher,
)


def signal(ticker="AAPL", bias=Bias.BULLISH, conviction=0.9):
    return LLMSignal(ticker=ticker, bias=bias, conviction=conviction, rationale="because")


class RecordingEngine:
    def __init__(self, status=ExecutionStatus.ACCEPTED, reason="ok", market_open=True):
        self.status, self.reason = status, reason
        self.executed: list[LLMSignal] = []
        self.broker = type("B", (), {"is_market_open": staticmethod(lambda: market_open)})()

    def execute(self, sig):
        self.executed.append(sig)
        from app.schemas import ExecutionResult

        return ExecutionResult(
            status=self.status, ticker=sig.ticker, bias=sig.bias,
            conviction=sig.conviction, reason=self.reason, quantity=7, order_id="oid-1",
        )


# --- mode selection -------------------------------------------------------


def test_direct_is_the_default(monkeypatch):
    monkeypatch.setattr(dispatch, "get_settings", lambda: Settings(_env_file=None))
    assert isinstance(build_dispatcher(), DirectDispatcher)


def test_webhook_mode_is_still_available(monkeypatch):
    monkeypatch.setattr(dispatch, "get_settings", lambda: Settings(execution_mode="webhook", _env_file=None))
    assert isinstance(build_dispatcher(), WebhookDispatcher)


def test_mode_is_case_and_space_insensitive(monkeypatch):
    monkeypatch.setattr(dispatch, "get_settings", lambda: Settings(execution_mode="  WebHook ", _env_file=None))
    assert isinstance(build_dispatcher(), WebhookDispatcher)


def test_an_unknown_mode_is_refused_loudly(monkeypatch):
    """A typo must not silently fall back to a transport nobody chose."""
    monkeypatch.setattr(dispatch, "get_settings", lambda: Settings(execution_mode="drect", _env_file=None))
    with pytest.raises(ValueError) as excinfo:
        build_dispatcher()
    assert "direct" in str(excinfo.value) and "webhook" in str(excinfo.value)


# --- direct mode ----------------------------------------------------------


def test_direct_mode_calls_the_engine_in_process():
    engine = RecordingEngine()
    outcome = DirectDispatcher(engine=engine).dispatch(signal())
    assert len(engine.executed) == 1
    assert outcome["status"] == "ACCEPTED"
    assert outcome["mode"] == DIRECT


def test_direct_mode_needs_no_webhook_secret(monkeypatch):
    """The whole point: one less thing to configure.

    A blank WEBHOOK_SHARED_SECRET is a 503 on the HTTP path, so if direct mode
    read it at all this would fail.
    """
    monkeypatch.setattr(dispatch, "get_settings", lambda: Settings(webhook_shared_secret="", _env_file=None))
    outcome = DirectDispatcher(engine=RecordingEngine()).dispatch(signal())
    assert outcome["status"] == "ACCEPTED"


def test_direct_and_webhook_outcomes_share_a_shape():
    """One journal format, so the scorer needn't learn two."""
    direct = DirectDispatcher(engine=RecordingEngine()).dispatch(signal())
    webhook = dispatch._webhook_outcome(
        httpx.Response(200, json={"status": "ACCEPTED", "reason": "ok", "quantity": 7, "order_id": "oid-1"})
    )
    shared = {"mode", "status", "reason", "quantity", "order_id"}
    assert shared <= set(direct) and shared <= set(webhook)
    assert direct["status"] == webhook["status"]


def test_a_rejection_is_reported_not_raised():
    engine = RecordingEngine(status=ExecutionStatus.REJECTED, reason="market is closed")
    outcome = DirectDispatcher(engine=engine).dispatch(signal())
    assert outcome["status"] == "REJECTED"
    assert outcome["reason"] == "market is closed"


def test_the_engine_is_not_built_at_construction():
    """Importing or constructing the orchestrator must not need Alpaca keys."""
    d = DirectDispatcher()
    assert d._engine is None


# --- the boundary still holds --------------------------------------------


def test_order_parameters_are_still_impossible_in_direct_mode():
    """The webhook's 422 becomes a ValidationError -- same rejection, no HTTP."""
    with pytest.raises(Exception) as excinfo:
        LLMSignal(ticker="AAPL", bias=Bias.BULLISH, conviction=0.9, rationale="r", quantity=999)
    assert "quantity" in str(excinfo.value)


def test_direct_mode_cannot_be_handed_a_quantity():
    """Even reaching the dispatcher, there is no field for it to carry."""
    engine = RecordingEngine()
    DirectDispatcher(engine=engine).dispatch(signal())
    assert not hasattr(engine.executed[0], "quantity")


# --- webhook mode is unchanged -------------------------------------------


def test_webhook_mode_still_sends_the_secret(monkeypatch):
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["headers"] = dict(request.headers)
        captured["body"] = json.loads(request.content)
        return httpx.Response(200, json={"status": "ACCEPTED"})

    monkeypatch.setattr(
        dispatch, "get_settings",
        lambda: Settings(webhook_shared_secret="s3cret", webhook_url="http://engine/webhook/signal", _env_file=None),
    )
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        outcome = WebhookDispatcher(client=client).dispatch(signal())

    assert captured["headers"]["x-webhook-secret"] == "s3cret"
    assert outcome["mode"] == WEBHOOK
    assert set(captured["body"]) <= set(LLMSignal.model_fields)


def test_webhook_mode_reports_open_because_it_cannot_know():
    """No broker on this side, so the engine's own gate has to decide."""
    assert WebhookDispatcher().is_market_open() is True
