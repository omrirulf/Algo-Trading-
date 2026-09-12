"""The Claude call is constrained at generation time and fails loudly."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

import anthropic
import httpx2
import pytest

from app.schemas import LLMSignal
from orchestrator import heartbeat as hb
from orchestrator import llm
from config.settings import Settings

VALID_SIGNAL = {"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.72, "rationale": "Earnings beat"}


@dataclass
class Block:
    type: str
    text: str = ""


@dataclass
class Response:
    content: list[Block]
    stop_reason: str = "end_turn"
    stop_details: Any = None


@dataclass
class FakeMessages:
    response: Any = None
    error: Exception | None = None
    calls: list[dict] = field(default_factory=list)

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.error is not None:
            raise self.error
        return self.response


class FakeClient:
    def __init__(self, response=None, error=None):
        self.messages = FakeMessages(response=response, error=error)


def _ok_client(payload=None):
    text = json.dumps(payload if payload is not None else VALID_SIGNAL)
    return FakeClient(Response(content=[Block("thinking"), Block("text", text)]))


def _provider(client):
    return llm.AnthropicSignalProvider(api_key="", client=client)


# --------------------------------------------------------------------------- #
# Schema derivation
# --------------------------------------------------------------------------- #


def test_schema_fields_cannot_drift_from_the_validator():
    schema = llm.build_output_schema(LLMSignal.model_json_schema())
    assert set(schema["properties"]) == set(LLMSignal.model_fields)
    assert set(schema["required"]) == set(LLMSignal.model_fields)
    assert schema["additionalProperties"] is False
    assert schema["type"] == "object"


def test_schema_inlines_the_bias_enum():
    schema = llm.build_output_schema(LLMSignal.model_json_schema())
    bias = schema["properties"]["bias"]
    assert bias == {"type": "string", "enum": ["BULLISH", "BEARISH", "NEUTRAL"]}
    assert "$defs" not in schema and "$ref" not in json.dumps(schema)


def test_schema_drops_keywords_constrained_decoding_may_reject():
    schema = llm.build_output_schema(LLMSignal.model_json_schema())
    serialized = json.dumps(schema)
    for keyword in ("pattern", "minLength", "maxLength", "minimum", "maximum", "title", "description"):
        assert keyword not in serialized
    # The dropped bounds are still enforced on the way back in.
    with pytest.raises(Exception):
        LLMSignal.model_validate({**VALID_SIGNAL, "conviction": 1.5})


def test_schema_rejects_an_unresolvable_reference():
    with pytest.raises(llm.LLMError):
        llm.build_output_schema({"type": "object", "properties": {"x": {"$ref": "#/$defs/Missing"}}})


# --------------------------------------------------------------------------- #
# Request shape
# --------------------------------------------------------------------------- #


def test_request_pins_model_schema_and_effort():
    client = _ok_client()
    _provider(client).complete("sys", "user", LLMSignal.model_json_schema())
    sent = client.messages.calls[0]

    assert sent["model"] == "claude-opus-5"
    assert sent["system"] == "sys"
    assert sent["messages"] == [{"role": "user", "content": "user"}]
    assert sent["thinking"] == {"type": "adaptive"}
    assert sent["output_config"]["effort"] == llm.EFFORT
    fmt = sent["output_config"]["format"]
    assert fmt["type"] == "json_schema"
    assert set(fmt["schema"]["properties"]) == set(LLMSignal.model_fields)
    assert "tools" not in sent  # the model has no tools; it can only answer


def test_returned_json_round_trips_through_the_validator():
    raw = _provider(_ok_client()).complete("s", "u", LLMSignal.model_json_schema())
    assert LLMSignal.model_validate(json.loads(raw)).ticker == "AAPL"


def test_missing_api_key_is_reported_before_any_call():
    with pytest.raises(llm.LLMError) as exc:
        llm.AnthropicSignalProvider(api_key="")
    assert "ANTHROPIC_API_KEY" in str(exc.value)


# --------------------------------------------------------------------------- #
# Failure modes
# --------------------------------------------------------------------------- #


def test_refusal_raises_with_its_category():
    @dataclass
    class Details:
        category: str = "cyber"

    client = FakeClient(Response(content=[], stop_reason="refusal", stop_details=Details()))
    with pytest.raises(llm.LLMError) as exc:
        _provider(client).complete("s", "u", LLMSignal.model_json_schema())
    assert "declined" in str(exc.value) and "cyber" in str(exc.value)


def test_truncated_response_is_not_parsed_as_a_signal():
    client = FakeClient(Response(content=[Block("text", '{"ticker": "AA')], stop_reason="max_tokens"))
    with pytest.raises(llm.LLMError) as exc:
        _provider(client).complete("s", "u", LLMSignal.model_json_schema())
    assert "max_tokens" in str(exc.value)


@pytest.mark.parametrize(
    "content",
    [[], [Block("thinking")], [Block("text", "   ")]],
    ids=["empty", "thinking-only", "blank-text"],
)
def test_missing_text_block_raises(content):
    with pytest.raises(llm.LLMError):
        _provider(FakeClient(Response(content=content))).complete("s", "u", LLMSignal.model_json_schema())


def test_non_json_output_raises():
    client = FakeClient(Response(content=[Block("text", "Sorry, I cannot help with that.")]))
    with pytest.raises(llm.LLMError) as exc:
        _provider(client).complete("s", "u", LLMSignal.model_json_schema())
    assert "non-JSON" in str(exc.value)


def test_api_errors_become_llm_errors():
    request = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")
    client = FakeClient(error=anthropic.APIConnectionError(message="boom", request=request))
    with pytest.raises(llm.LLMError) as exc:
        _provider(client).complete("s", "u", LLMSignal.model_json_schema())
    assert "Claude API call failed" in str(exc.value)


# --------------------------------------------------------------------------- #
# Wiring and isolation
# --------------------------------------------------------------------------- #


def test_heartbeat_call_llm_uses_the_configured_key(monkeypatch):
    seen = {}

    class FakeProvider:
        def __init__(self, api_key, client=None):
            seen["key"] = api_key

        def complete(self, system_prompt, user_prompt, json_schema):
            seen["prompts"] = (system_prompt, user_prompt)
            return json.dumps(VALID_SIGNAL)

    monkeypatch.setattr(hb, "AnthropicSignalProvider", FakeProvider)
    monkeypatch.setattr(hb, "get_settings", lambda: Settings(anthropic_api_key="k", _env_file=None))

    raw = hb.call_llm("sys", "user", hb.SIGNAL_JSON_SCHEMA)
    assert json.loads(raw) == VALID_SIGNAL
    assert seen["key"] == "k"
    assert seen["prompts"] == ("sys", "user")


def test_full_cycle_posts_the_signal_the_model_returned(monkeypatch):
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["Apple beats on earnings"])
    monkeypatch.setattr(hb, "call_llm", lambda s, u, j: json.dumps(VALID_SIGNAL))
    posted = []

    def fake_post(signal, client=None):
        posted.append(signal)
        return httpx2.Response(200, text='{"status": "ACCEPTED"}')

    monkeypatch.setattr(hb, "post_signal", fake_post)
    hb.process_ticker("AAPL")
    assert len(posted) == 1
    assert posted[0].bias.value == "BULLISH" and posted[0].conviction == 0.72


def test_llm_module_cannot_reach_the_broker_or_the_engine():
    src = open(llm.__file__).read()
    assert "alpaca" not in src.lower()
    assert "from app.schemas" not in src and "import app" not in src
    assert "requests" not in src  # SDK only, no hand-rolled HTTP
