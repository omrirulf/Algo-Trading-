"""The orchestrator can only ever send the closed signal shape."""

from __future__ import annotations

import json

import httpx
import pytest
from pydantic import ValidationError

from orchestrator import heartbeat as hb
from config.settings import Settings


def test_schema_handed_to_llm_is_closed():
    assert hb.SIGNAL_JSON_SCHEMA["additionalProperties"] is False
    assert set(hb.SIGNAL_JSON_SCHEMA["properties"]) == {"ticker", "bias", "conviction", "rationale"}


def test_parse_signal_rejects_smuggled_fields():
    raw = json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.9, "rationale": "x", "quantity": 9999})
    with pytest.raises(ValidationError):
        hb.parse_signal(raw)


def test_process_ticker_logs_missing_llm_credentials(monkeypatch, caplog):
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    monkeypatch.setattr(hb, "get_settings", lambda: Settings(_env_file=None))
    hb.process_ticker("AAPL")  # must not raise; scheduler would otherwise die
    assert "ANTHROPIC_API_KEY" in caplog.text


def test_process_ticker_logs_missing_news_credentials(monkeypatch, caplog):
    monkeypatch.setattr(hb, "get_settings", lambda: Settings(_env_file=None))
    hb.process_ticker("AAPL")  # no Bright Data token configured
    assert "BRIGHTDATA_API_TOKEN" in caplog.text


def test_system_prompt_asks_for_calibrated_conviction():
    # A model that always answers 0.9 makes the conviction floor meaningless.
    assert "Calibrate conviction" in hb.SYSTEM_PROMPT
    assert "NEUTRAL" in hb.SYSTEM_PROMPT


def test_post_signal_sends_only_signal_fields_with_secret(monkeypatch):
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["headers"] = dict(request.headers)
        captured["body"] = json.loads(request.content)
        return httpx.Response(200, json={"status": "ACCEPTED"})

    monkeypatch.setattr(
        hb, "get_settings",
        lambda: Settings(webhook_shared_secret="s3cret", webhook_url="http://engine/webhook/signal", _env_file=None),
    )
    signal = hb.parse_signal(json.dumps({"ticker": "aapl", "bias": "BEARISH", "conviction": 0.7, "rationale": "r"}))
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        resp = hb.post_signal(signal, client=client)

    assert resp.status_code == 200
    assert captured["headers"]["x-webhook-secret"] == "s3cret"
    assert captured["body"] == {"ticker": "AAPL", "bias": "BEARISH", "conviction": 0.7, "rationale": "r"}


def test_process_ticker_drops_signal_for_wrong_ticker(monkeypatch, caplog):
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    monkeypatch.setattr(hb, "call_llm", lambda s, u, j: json.dumps({"ticker": "MSFT", "bias": "BULLISH", "conviction": 0.9, "rationale": "r"}))
    posted = []
    monkeypatch.setattr(hb, "post_signal", lambda s, client=None: posted.append(s))
    hb.process_ticker("AAPL")
    assert posted == []
    assert "instead" in caplog.text


def test_process_ticker_posts_valid_signal(monkeypatch):
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["news"])
    monkeypatch.setattr(hb, "call_llm", lambda s, u, j: json.dumps({"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.9, "rationale": "r"}))
    posted = []
    monkeypatch.setattr(hb, "post_signal", lambda s, client=None: (posted.append(s), httpx.Response(200, text=""))[1])
    hb.process_ticker("AAPL")
    assert len(posted) == 1 and posted[0].ticker == "AAPL"
