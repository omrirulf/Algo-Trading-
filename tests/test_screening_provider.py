"""The screen can be answered by something other than Claude.

The seam exists so the cheap stage can run on a model nobody bills for. Three
properties matter, and the third is what makes the other two safe to ship:

* unset, the cycle is exactly what it was -- Claude Haiku, one provider;
* configured, the screen goes to the endpoint and the *full model does not*;
* an endpoint that misbehaves in any way raises ``LLMError``, which the funnel
  already treats as "the screen failed, ask the full model". A bad local model
  can cost a cycle its saving. It can never produce a trade.
"""

from __future__ import annotations

import json

import httpx
import pytest

from config.settings import Settings
from orchestrator import heartbeat as hb
from orchestrator import llm
from orchestrator.llm import Completion, LLMError, OpenAICompatibleProvider

SCHEMA = {"type": "object", "properties": {"bias": {"type": "string"}}}
ANSWER = {"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.2, "rationale": "r"}


@pytest.fixture
def configured(monkeypatch):
    """Point the heartbeat's settings at values this test chose."""

    def use(**fields):
        monkeypatch.setattr(
            hb, "get_settings", lambda: Settings(_env_file=None, **fields)
        )

    return use


def _server(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler), base_url="http://local")


def _ok(payload=None, usage=None):
    body = {
        "choices": [{"message": {"content": json.dumps(payload or ANSWER)}}],
        "usage": usage if usage is not None else {"prompt_tokens": 3000, "completion_tokens": 250},
    }
    return _server(lambda request: httpx.Response(200, json=body))


def _provider(client, model="qwen2.5:14b") -> OpenAICompatibleProvider:
    return OpenAICompatibleProvider("http://local/v1", model, client=client)


# --- the happy path --------------------------------------------------------


def test_the_answer_comes_back_as_a_completion():
    out = _provider(_ok()).complete_detailed("sys", "user", SCHEMA)
    assert json.loads(out.text)["bias"] == "NEUTRAL"
    assert out.usage.input_tokens == 3000
    assert out.usage.output_tokens == 250
    assert out.usage.model == "qwen2.5:14b"


def test_an_unpriced_model_costs_none_rather_than_zero():
    """None reads as "unpriced". Zero would read as "free", which is a claim
    about someone else's hardware that this module cannot make."""
    out = _provider(_ok()).complete_detailed("sys", "user", SCHEMA)
    assert out.usage.cost_usd is None


def test_the_request_carries_the_schema_and_nothing_anthropic_shaped():
    sent = {}

    def handler(request: httpx.Request) -> httpx.Response:
        sent.update(json.loads(request.content))
        return httpx.Response(200, json={"choices": [{"message": {"content": json.dumps(ANSWER)}}]})

    # reasoning=True: nothing rewrites the prompt, so this is the plain shape.
    _provider(_server(handler)).complete_detailed("sys", "user", SCHEMA, reasoning=True)
    assert sent["messages"][0] == {"role": "system", "content": "sys"}
    assert sent["messages"][1] == {"role": "user", "content": "user"}
    assert sent["response_format"]["json_schema"]["schema"]["type"] == "object"
    # These have no counterpart here and are dropped, not translated.
    for absent in ("thinking", "output_config", "cache_control", "betas", "fallbacks", "reasoning_effort"):
        assert absent not in sent


# --- reasoning=False, which chat-completions has no native switch for -----


def test_reasoning_off_appends_a_plain_instruction_to_the_system_prompt():
    sent = {}

    def handler(request: httpx.Request) -> httpx.Response:
        sent.update(json.loads(request.content))
        return httpx.Response(200, json={"choices": [{"message": {"content": json.dumps(ANSWER)}}]})

    _provider(_server(handler)).complete_detailed("sys", "user", SCHEMA, reasoning=False)
    system = sent["messages"][0]["content"]
    assert system.startswith("sys")
    assert "do not show your reasoning" in system.lower()
    # The user turn is untouched -- only the system prompt carries the ask.
    assert sent["messages"][1] == {"role": "user", "content": "user"}


def test_reasoning_off_also_sends_a_best_effort_reasoning_effort_field():
    sent = {}

    def handler(request: httpx.Request) -> httpx.Response:
        sent.update(json.loads(request.content))
        return httpx.Response(200, json={"choices": [{"message": {"content": json.dumps(ANSWER)}}]})

    _provider(_server(handler)).complete_detailed("sys", "user", SCHEMA, reasoning=False)
    assert sent["reasoning_effort"] == "low"


def test_reasoning_on_sends_neither():
    sent = {}

    def handler(request: httpx.Request) -> httpx.Response:
        sent.update(json.loads(request.content))
        return httpx.Response(200, json={"choices": [{"message": {"content": json.dumps(ANSWER)}}]})

    _provider(_server(handler)).complete_detailed("sys", "user", SCHEMA, reasoning=True)
    assert sent["messages"][0] == {"role": "system", "content": "sys"}
    assert "reasoning_effort" not in sent


def test_a_key_is_sent_only_when_there_is_one():
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("authorization"))
        return httpx.Response(200, json={"choices": [{"message": {"content": json.dumps(ANSWER)}}]})

    OpenAICompatibleProvider("http://local/v1", "m", client=_server(handler)).complete_detailed(
        "s", "u", SCHEMA
    )
    OpenAICompatibleProvider(
        "http://local/v1", "m", api_key="tok", client=_server(handler)
    ).complete_detailed("s", "u", SCHEMA)
    assert seen == [None, "Bearer tok"]


# --- every way it can go wrong is one the funnel already survives ----------


@pytest.mark.parametrize("handler,reason", [
    (lambda r: httpx.Response(500, text="boom"), "a server error"),
    (lambda r: httpx.Response(200, text="not json at all"), "a non-JSON body"),
    (lambda r: httpx.Response(200, json={"choices": []}), "no choices"),
    (lambda r: httpx.Response(200, json={"choices": [{"message": {"content": ""}}]}), "an empty answer"),
    (lambda r: httpx.Response(200, json={"choices": [{"message": {"content": "I think AAPL looks good!"}}]}), "prose instead of JSON"),
])
def test_a_misbehaving_endpoint_raises_llm_error(handler, reason):
    with pytest.raises(LLMError):
        _provider(_server(handler)).complete_detailed("s", "u", SCHEMA)


def test_an_unreachable_endpoint_raises_llm_error():
    def refuse(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("connection refused")

    with pytest.raises(LLMError):
        _provider(_server(refuse)).complete_detailed("s", "u", SCHEMA)


def test_a_base_url_is_required():
    with pytest.raises(LLMError):
        OpenAICompatibleProvider("", "m")


# --- what the cycle picks --------------------------------------------------


def test_unset_the_screen_is_claude_as_before(configured):
    configured()
    provider, model = hb.screening_provider()
    assert isinstance(provider, llm.AnthropicSignalProvider)
    assert model == hb.SCREENING_MODEL


def test_a_base_url_moves_the_screen_off_claude(configured):
    configured(screening_base_url="http://local/v1", screening_model="qwen2.5:14b")
    provider, model = hb.screening_provider()
    assert isinstance(provider, OpenAICompatibleProvider)
    assert model == "qwen2.5:14b"


def test_a_base_url_without_a_model_is_refused(configured):
    """Better to name the missing setting than to guess a model on someone
    else's server."""
    configured(screening_base_url="http://local/v1")
    with pytest.raises(LLMError):
        hb.screening_provider()


def test_the_model_name_alone_never_changes_which_claude_screens(configured):
    """What the account trades on is meant to be a diff, not an env var."""
    configured(screening_model="claude-opus-5")
    provider, model = hb.screening_provider()
    assert isinstance(provider, llm.AnthropicSignalProvider)
    assert model == hb.SCREENING_MODEL


def test_the_full_model_is_never_the_local_one():
    """The seam is the screen. The call that decides a trade stays Claude."""
    import inspect

    source = inspect.getsource(hb.call_llm)
    assert "AnthropicSignalProvider" in source
    assert "screening_provider" not in source


# --- letting the screen think, when the endpoint needs it to ---------------


def _settings(**kw):
    base = dict(
        screening_base_url="https://api.deepinfra.com/v1/openai",
        screening_model="openai/gpt-oss-20b",
        screening_api_key="k",
    )
    base.update(kw)
    return Settings(**base)


def test_no_effort_configured_still_asks_with_reasoning_off(monkeypatch):
    """The default has to stay the cheap one: every existing deployment that
    set only a base URL and a model must keep the screen it measured."""
    monkeypatch.setattr(hb, "get_settings", lambda: _settings())
    assert hb.screening_effort() is None


def test_an_effort_is_honoured_when_an_endpoint_is_configured(monkeypatch):
    monkeypatch.setattr(hb, "get_settings", lambda: _settings(screening_effort="high"))
    assert hb.screening_effort() == "high"


def test_an_effort_without_an_endpoint_is_ignored_not_obeyed(monkeypatch):
    """Clearing the base URL is how you fall back to Claude in a hurry. If a
    leftover effort followed you there it would break every screen instead."""
    monkeypatch.setattr(hb, "get_settings", lambda: _settings(
        screening_base_url="", screening_model="", screening_effort="high",
    ))
    assert hb.screening_effort() is None


@pytest.mark.parametrize("value", ["High", " high ", "HIGH"])
def test_an_effort_is_read_case_and_space_insensitively(monkeypatch, value):
    monkeypatch.setattr(hb, "get_settings", lambda: _settings(screening_effort=value))
    assert hb.screening_effort() == "high"


@pytest.mark.parametrize("value", ["maximum", "hard", "true", "9"])
def test_an_unusable_effort_is_refused_before_it_reaches_the_endpoint(monkeypatch, value):
    """A typo sent to the endpoint is a 400 per ticker: every one falls
    through to the full model, which is safe and is the whole saving gone
    without a word."""
    monkeypatch.setattr(hb, "get_settings", lambda: _settings(screening_effort=value))
    with pytest.raises(LLMError) as exc:
        hb.screening_effort()
    assert value in str(exc.value)


def test_the_screen_call_carries_the_effort_end_to_end(monkeypatch):
    seen: dict = {}

    class _Provider:
        def __init__(self, **kw):
            pass

        def complete_detailed(self, s, u, j, **kw):
            seen.update(kw)
            return Completion(text=json.dumps(ANSWER), usage=None)

    monkeypatch.setattr(hb, "get_settings", lambda: _settings(screening_effort="high"))
    monkeypatch.setattr(hb, "OpenAICompatibleProvider", _Provider)
    hb.screen_signal("s", "u", SCHEMA)
    assert seen["reasoning"] is True
    assert seen["effort"] == "high"
    assert seen["model"] == "openai/gpt-oss-20b"
