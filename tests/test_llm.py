"""The Claude call is constrained at generation time and fails loudly."""

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
import time
from dataclasses import dataclass, field
from types import SimpleNamespace
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
class Switch:
    """A ``fallback`` content block: model ``from_`` declined, ``to`` answered."""

    from_model: str
    to_model: str
    type: str = "fallback"

    @property
    def from_(self):
        return SimpleNamespace(model=self.from_model)

    @property
    def to(self):
        return SimpleNamespace(model=self.to_model)


@dataclass
class FakeMessages:
    response: Any = None
    error: Exception | None = None
    fail_first: Exception | None = None
    calls: list[dict] = field(default_factory=list)

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.fail_first is not None and len(self.calls) == 1:
            raise self.fail_first
        if self.error is not None:
            raise self.error
        return self.response


class FakeClient:
    """Exposes only ``beta.messages``, which is all the provider may touch."""

    def __init__(self, response=None, error=None, fail_first=None):
        self.api = FakeMessages(response=response, error=error, fail_first=fail_first)
        self.beta = SimpleNamespace(messages=self.api)


def _bad_request(message="unknown beta"):
    request = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")
    return anthropic.BadRequestError(
        message, response=httpx2.Response(400, request=request), body=None
    )


def _ok_client(payload=None, **kwargs):
    text = json.dumps(payload if payload is not None else VALID_SIGNAL)
    return FakeClient(Response(content=[Block("thinking"), Block("text", text)]), **kwargs)


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
    for keyword in ("pattern", "minLength", "maxLength", "minimum", "maximum", "title"):
        assert keyword not in serialized
    # The dropped bounds are still enforced on the way back in.
    with pytest.raises(Exception):
        LLMSignal.model_validate({**VALID_SIGNAL, "conviction": 1.5})


def test_schema_keeps_descriptions_so_field_meaning_survives():
    # The score scale lives only in the description; without it the model is
    # told to emit a number with no idea which end is bullish.
    schema = llm.build_output_schema(LLMSignal.model_json_schema())
    assert "maximally bearish" in schema["properties"]["news_score"]["description"]


def test_optional_fields_are_not_left_unconstrained():
    """``Optional[float]`` must reach the model as a number, not an empty schema.

    Pruning an ``anyOf`` without collapsing it first leaves ``{}``, which
    constrains nothing -- the one hole through which a model could emit an
    arbitrary value into an otherwise closed schema.
    """
    schema = llm.build_output_schema(LLMSignal.model_json_schema())
    for field in ("news_score", "technical_score", "fundamental_score", "analyst_score"):
        assert schema["properties"][field]["type"] == "number"
    assert "anyOf" not in json.dumps(schema)


def test_every_property_is_required_of_the_model():
    # Optional on the way in (old payloads still validate), mandatory on the
    # way out: a model handed all four kinds of context must score all four.
    schema = llm.build_output_schema(LLMSignal.model_json_schema())
    assert set(schema["required"]) == set(schema["properties"])
    assert "news_score" in schema["required"]
    assert "news_score" not in LLMSignal.model_json_schema()["required"]


def test_schema_rejects_an_unresolvable_reference():
    with pytest.raises(llm.LLMError):
        llm.build_output_schema({"type": "object", "properties": {"x": {"$ref": "#/$defs/Missing"}}})


# --------------------------------------------------------------------------- #
# Request shape
# --------------------------------------------------------------------------- #


def test_request_pins_model_schema_and_effort():
    client = _ok_client()
    _provider(client).complete("sys", "user", LLMSignal.model_json_schema())
    sent = client.api.calls[0]

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


def test_blank_api_key_defers_to_the_sdks_own_resolution():
    """A blank key no longer means "fail immediately" -- it means "let the
    SDK try ANTHROPIC_AUTH_TOKEN, an `ant auth login` profile, or WIF"."""
    llm.AnthropicSignalProvider(api_key="")  # must not raise


def test_missing_credentials_anywhere_are_reported_at_first_call(monkeypatch):
    # Hermetic: a real key or token in the environment running this test
    # would otherwise make the "nothing resolvable" case unreachable. (An
    # ambient `ant auth login` profile or WIF env vars on a dev machine
    # could still do the same; not defended against here.)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)

    provider = llm.AnthropicSignalProvider(api_key="")
    with pytest.raises(llm.LLMError) as exc:
        provider.complete("s", "u", LLMSignal.model_json_schema())

    assert "ANTHROPIC_API_KEY" in str(exc.value)
    assert "ant auth login" in str(exc.value)


def test_missing_credentials_are_detected_without_touching_the_network(monkeypatch):
    """The SDK raises before opening a connection; this proves it stays
    that way, since the whole point is a fast, offline failure."""
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_AUTH_TOKEN", raising=False)
    provider = llm.AnthropicSignalProvider(api_key="")

    start = time.monotonic()
    with pytest.raises(llm.LLMError):
        provider.complete("s", "u", LLMSignal.model_json_schema())
    assert time.monotonic() - start < 2.0


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
# Refusal fallback
# --------------------------------------------------------------------------- #


def test_request_asks_for_the_server_side_refusal_fallback():
    client = _ok_client()
    _provider(client).complete("s", "u", LLMSignal.model_json_schema())
    sent = client.api.calls[0]
    assert sent["fallbacks"] == "default"
    assert sent["betas"] == ["server-side-fallback-2026-07-01"]


def test_fallback_mode_and_beta_stay_a_matched_pair():
    # The array form of fallbacks needs the 2026-06-01 beta; crossing the two
    # is a 400. Pin the pairing so a future edit cannot silently split them.
    assert (llm.FALLBACK_MODE, llm.FALLBACK_BETA) == (
        "default",
        "server-side-fallback-2026-07-01",
    )


def test_answer_is_taken_from_the_model_that_did_not_decline():
    client = FakeClient(Response(content=[
        Block("text", "I can't help with that"),          # partial, declining model
        Switch("claude-opus-5", "claude-opus-4-8"),
        Block("thinking"),
        Block("text", json.dumps(VALID_SIGNAL)),          # the real answer
    ]))
    raw = _provider(client).complete("s", "u", LLMSignal.model_json_schema())
    assert json.loads(raw) == VALID_SIGNAL


def test_fallback_switch_is_logged(caplog):
    client = FakeClient(Response(content=[
        Switch("claude-opus-5", "claude-opus-4-8"),
        Block("text", json.dumps(VALID_SIGNAL)),
    ]))
    _provider(client).complete("s", "u", LLMSignal.model_json_schema())
    assert "claude-opus-5 declined; claude-opus-4-8 answered instead" in caplog.text


def test_whole_chain_refusing_is_still_an_error():
    client = FakeClient(Response(
        content=[Switch("claude-opus-5", "claude-opus-4-8")], stop_reason="refusal"
    ))
    with pytest.raises(llm.LLMError):
        _provider(client).complete("s", "u", LLMSignal.model_json_schema())


def test_rejected_fallback_beta_does_not_kill_the_cycle(caplog):
    client = _ok_client(fail_first=_bad_request("unsupported beta"))
    raw = _provider(client).complete("s", "u", LLMSignal.model_json_schema())

    assert json.loads(raw) == VALID_SIGNAL
    assert "continuing without it" in caplog.text
    first, retry = client.api.calls
    assert first["fallbacks"] == "default"
    assert "fallbacks" not in retry and "betas" not in retry
    # The retry is otherwise the same request.
    assert retry["output_config"] == first["output_config"]
    assert retry["model"] == first["model"]


def test_fallback_is_dropped_for_the_rest_of_the_provider_s_life():
    client = _ok_client(fail_first=_bad_request())
    provider = _provider(client)
    provider.complete("s", "u", LLMSignal.model_json_schema())
    provider.complete("s", "u", LLMSignal.model_json_schema())
    # First attempt, its retry, then a single un-decorated call.
    assert len(client.api.calls) == 3
    assert "fallbacks" not in client.api.calls[2]


def test_other_bad_requests_are_not_swallowed_as_fallback_problems():
    client = FakeClient(error=_bad_request("schema is invalid"))
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

        def complete_detailed(self, system_prompt, user_prompt, json_schema):
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
    monkeypatch.setattr(hb, "call_llm", lambda s, u, j: completion(VALID_SIGNAL))
    posted = []

    def fake_post(signal, dispatcher=None):
        posted.append(signal)
        return {"mode": "direct", "status": "ACCEPTED", "reason": "ok"}

    monkeypatch.setattr(hb, "post_signal", fake_post)
    hb.process_ticker("AAPL")
    assert len(posted) == 1
    assert posted[0].bias.value == "BULLISH" and posted[0].conviction == 0.72


def test_llm_module_cannot_reach_the_broker_or_the_engine():
    src = open(llm.__file__).read()
    assert "alpaca" not in src.lower()
    assert "from app.schemas" not in src and "import app" not in src
    assert "requests" not in src  # SDK only, no hand-rolled HTTP
