"""HTTP-level guardrails: auth, 422 on smuggled fields, and the happy path."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from app import main as app_main
from app.execution_engine import ExecutionEngine
from config.settings import Settings

SECRET = "test-secret"
VALID = {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.75, "rationale": "Strong earnings beat"}


@pytest.fixture
def client(broker, market, monkeypatch):
    monkeypatch.setattr(
        app_main, "get_settings", lambda: Settings(webhook_shared_secret=SECRET, _env_file=None)
    )
    app_main.app.dependency_overrides[app_main.get_engine] = lambda: ExecutionEngine(broker, market)
    with TestClient(app_main.app) as c:
        yield c
    app_main.app.dependency_overrides.clear()


def _post(client, payload, secret=SECRET):
    headers = {"x-webhook-secret": secret} if secret is not None else {}
    return client.post("/webhook/signal", json=payload, headers=headers)


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


def test_valid_signal_is_executed(client, broker):
    r = _post(client, VALID)
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["status"] == "ACCEPTED"
    assert body["quantity"] == 50
    assert body["stop_price"] > 0
    assert len(broker.submitted) == 1


@pytest.mark.parametrize("extra", [{"quantity": 500}, {"price": 1}, {"side": "buy"}, {"stop_price": 0.01}])
def test_smuggled_fields_are_422_before_execution(client, broker, extra):
    r = _post(client, {**VALID, **extra})
    assert r.status_code == 422
    assert any(e["type"] == "extra_forbidden" for e in r.json()["detail"])
    assert broker.submitted == []


def test_missing_secret_is_401(client, broker):
    assert _post(client, VALID, secret=None).status_code == 401
    assert broker.submitted == []


def test_wrong_secret_is_401(client, broker):
    assert _post(client, VALID, secret="nope").status_code == 401
    assert broker.submitted == []


def test_wrong_secret_with_bad_payload_still_401_not_422(client):
    """Auth is checked before the body is validated: no schema oracle for unauthenticated callers."""
    assert _post(client, {**VALID, "quantity": 1}, secret="nope").status_code == 401


def test_unconfigured_secret_is_503(client, broker, monkeypatch):
    monkeypatch.setattr(app_main, "get_settings", lambda: Settings(webhook_shared_secret="", _env_file=None))
    assert _post(client, VALID).status_code == 503
    assert broker.submitted == []


def test_non_json_body_is_422(client):
    r = client.post("/webhook/signal", content="not json", headers={"x-webhook-secret": SECRET, "content-type": "application/json"})
    assert r.status_code == 422


def test_rejection_is_200_with_rejected_status(client, broker):
    r = _post(client, {**VALID, "bias": "NEUTRAL"})
    assert r.status_code == 200
    assert r.json()["status"] == "REJECTED"
    assert broker.submitted == []
