"""The full model on an OpenAI-compatible endpoint, where nothing is behind it.

Every property here used to be somebody else's problem. As the *screening*
stage, a refused call, a throttled one and an off-schema one all meant the
same safe thing -- "the screen failed, ask the full model" -- so the worst
case was the cycle's cost. Since 23 September the endpoint IS the full model
and the screen is off, so each of those is a signal the day never gets.

Two measurements drive the shapes below, both taken against DeepInfra:

* 50 of 300 calls returned HTTP 429 at four in flight, and 39 at eight. A
  ceiling that barely moves with parallelism is a token-per-minute bucket, so
  the fix is waiting, not spreading out.
* gpt-oss-120b answered off-schema on 12 of 300 calls and on 6 of 150 the day
  before -- a steady 4%, which over an eighty-name watchlist is three tickers
  a day with no signal at all.
"""

from __future__ import annotations

import json

import httpx
import pytest

from config import settings as cfg
from config.settings import Settings
from orchestrator import heartbeat as hb
from orchestrator import llm
from orchestrator.llm import LLMError, OpenAICompatibleProvider

SCHEMA = {"type": "object", "properties": {"bias": {"type": "string"}}}
ANSWER = {"ticker": "AAPL", "bias": "NEUTRAL", "conviction": 0.2, "rationale": "r"}


def _body(payload=None):
    return {
        "choices": [{"message": {"content": json.dumps(payload or ANSWER)}}],
        "usage": {"prompt_tokens": 3000, "completion_tokens": 250},
    }


class _Server:
    """Answers a scripted list of responses, recording what it was sent."""

    def __init__(self, *responses: httpx.Response) -> None:
        self._responses = list(responses)
        self.sent: list[dict] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.sent.append(json.loads(request.content))
        if not self._responses:
            raise AssertionError("asked more times than the script allows")
        return self._responses.pop(0)

    @property
    def client(self) -> httpx.Client:
        return httpx.Client(transport=httpx.MockTransport(self), base_url="http://local")


def _provider(server: _Server, slept: list[float] | None = None, **kw):
    return OpenAICompatibleProvider(
        "http://local/v1", "openai/gpt-oss-120b", api_key="k",
        client=server.client, sleep=(slept.append if slept is not None else lambda _: None),
        **kw,
    )


# --- the rate limit --------------------------------------------------------


def test_a_throttled_call_waits_and_is_asked_again():
    server = _Server(httpx.Response(429, text="slow down"), httpx.Response(200, json=_body()))
    slept: list[float] = []
    out = _provider(server, slept).complete_detailed("s", "u", SCHEMA)
    assert json.loads(out.text)["ticker"] == "AAPL"
    assert slept == [llm.RETRY_BASE_SECONDS]
    assert len(server.sent) == 2


def test_the_server_s_own_retry_after_beats_the_ladder():
    """A token bucket knows how much of the minute is left; the ladder guesses."""
    server = _Server(
        httpx.Response(429, headers={"Retry-After": "7"}),
        httpx.Response(429, headers={"Retry-After": "11"}),
        httpx.Response(200, json=_body()),
    )
    slept: list[float] = []
    _provider(server, slept).complete_detailed("s", "u", SCHEMA)
    # Each 429 steers the wait that follows it, so the ladder's opening rung
    # is never used while the server is saying how long it wants.
    assert slept == [7.0, 11.0]


def test_an_absurd_retry_after_is_ignored_for_the_ladder():
    """An hour is not a wait, it is an outage, and the cycle has a session."""
    server = _Server(
        httpx.Response(429, headers={"Retry-After": "3600"}),
        httpx.Response(200, json=_body()),
    )
    slept: list[float] = []
    _provider(server, slept).complete_detailed("s", "u", SCHEMA)
    assert slept == [llm.RETRY_BASE_SECONDS]


def test_a_bad_request_is_not_asked_again():
    """400 and 401 do not become 200 by repetition; they spend the deadline."""
    server = _Server(httpx.Response(400, text="bad schema"))
    with pytest.raises(LLMError, match="HTTP 400"):
        _provider(server).complete_detailed("s", "u", SCHEMA)
    assert len(server.sent) == 1


def test_a_call_that_stays_throttled_gives_up_and_says_how_often_it_asked():
    server = _Server(*[httpx.Response(429) for _ in range(llm.HTTP_ATTEMPTS)])
    with pytest.raises(LLMError, match=f"gave up after {llm.HTTP_ATTEMPTS} attempt"):
        _provider(server).complete_detailed("s", "u", SCHEMA)
    assert len(server.sent) == llm.HTTP_ATTEMPTS


def test_a_transport_failure_is_deliberately_not_retried():
    """It has already spent the whole per-call timeout and been billed for
    whatever it generated. The cycle's budget is the sum of these worst
    cases: eighty tickers four at a time at a 300s ceiling is twenty rounds,
    which fits the job's clock exactly once."""
    def refuse(request):
        raise httpx.ConnectTimeout("timed out", request=request)

    client = httpx.Client(transport=httpx.MockTransport(refuse), base_url="http://local")
    provider = OpenAICompatibleProvider(
        "http://local/v1", "m", api_key="k", client=client, sleep=lambda _: None,
    )
    with pytest.raises(LLMError, match="unreachable"):
        provider.complete_detailed("s", "u", SCHEMA)


# --- the off-schema answer -------------------------------------------------


def test_prose_is_asked_again_with_the_complaint_stated():
    server = _Server(
        httpx.Response(200, json={"choices": [{"message": {"content": "Sure! Here you go."}}]}),
        httpx.Response(200, json=_body()),
    )
    out = _provider(server).complete_detailed("s", "u", SCHEMA)
    assert json.loads(out.text)["ticker"] == "AAPL"
    first, second = server.sent
    assert llm.OFF_SCHEMA_INSTRUCTION not in first["messages"][0]["content"]
    assert llm.OFF_SCHEMA_INSTRUCTION in second["messages"][0]["content"]
    # The question itself is unchanged -- only the complaint is added.
    assert first["messages"][1] == second["messages"][1]


def test_a_second_bad_answer_is_the_real_answer():
    server = _Server(
        httpx.Response(200, json={"choices": [{"message": {"content": "nope"}}]}),
        httpx.Response(200, json={"choices": [{"message": {"content": "still nope"}}]}),
    )
    with pytest.raises(LLMError, match="non-JSON"):
        _provider(server).complete_detailed("s", "u", SCHEMA)
    assert len(server.sent) == llm.SCHEMA_ATTEMPTS


def test_the_re_ask_does_not_mutate_the_caller_s_prompt():
    """The complaint rides a copy, so a retry cannot leave it in the journal's
    record of what the model was actually asked the first time."""
    server = _Server(
        httpx.Response(200, json={"choices": [{"message": {"content": "no"}}]}),
        httpx.Response(200, json=_body()),
    )
    _provider(server).complete_detailed("system prompt", "u", SCHEMA)
    assert server.sent[0]["messages"][0]["content"] == "system prompt"


# --- how the cycle asks ----------------------------------------------------


def _with(settings, call):
    import unittest.mock
    with unittest.mock.patch.object(hb, "get_settings", lambda: settings):
        return call()


def test_the_full_model_stage_is_not_asked_at_the_screen_s_width():
    """Eight in flight is the screen's number, chosen when a stage was 2.4s a
    call. The full model's is measured against the throttle and against the
    job's clock, and they are not the same question."""
    assert cfg.FULL_MODEL_MAX_CONCURRENCY < cfg.SCREEN_MAX_CONCURRENCY
    import inspect
    source = inspect.getsource(hb.run_batched_cycle)
    assert "FULL_MODEL_MAX_CONCURRENCY" in source


def test_a_misconfigured_full_model_fails_the_tickers_not_the_cycle():
    """Raising out of the cycle would take the journal, the report, the ladder
    and the protection pass down with the signals. An unprotected position is
    a worse outcome than a day with no new ones."""
    import inspect
    source = inspect.getsource(hb.run_batched_cycle)
    assert "full_model_provider()" in source
    assert "except LLMError" in source


def test_asking_the_endpoint_anonymously_is_refused():
    """An endpoint answering 401 once per ticker is a session lost quietly,
    and the screen is no longer behind it to catch that."""
    settings = Settings(_env_file=None, full_model_api_key="")
    with pytest.raises(LLMError, match="FULL_MODEL_API_KEY"):
        _with(settings, hb.full_model_provider)



# --- the transport retry, and what bounds it -------------------------------


def test_a_timed_out_call_is_asked_once_more_on_the_full_ceiling():
    """Not retried at all until 23 September, on an argument the first
    production cycle disproved: the worst case was taken to be every call
    running to the 300s ceiling, which left no room to ask twice. The measured
    stage was 32 minutes, not 100, and the three tickers lost that day were
    lost to exactly this.

    The retry then got 120s, which the full model's answers almost never fit
    (median 130-146s): 0 of 7 retries succeeded on 25 Sep. Since 26 Sep (bug
    fix, Amendments table) the second ask gets the same 300s as the first."""
    seen: list[float] = []
    attempts = {"n": 0}

    def flaky(request):
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise httpx.ReadTimeout("timed out", request=request)
        return httpx.Response(200, json=_body())

    def client(timeout):
        seen.append(timeout)
        return httpx.Client(transport=httpx.MockTransport(flaky), base_url="http://local")

    provider = OpenAICompatibleProvider(
        "http://local/v1", "openai/gpt-oss-120b", api_key="k", sleep=lambda _: None,
        timeout=llm.FULL_MODEL_TIMEOUT_SECONDS,
    )
    import unittest.mock
    with unittest.mock.patch.object(llm, "new_http_client", client):
        out = provider.complete_detailed("s", "u", SCHEMA)

    assert json.loads(out.text)["ticker"] == "AAPL"
    assert seen == [300.0, 300.0]


def test_the_retry_ceiling_does_not_leak_into_the_next_ticker():
    """A provider is reused across the watchlist. One slow call must not
    quietly change the ceiling of every call after it."""
    def always_timeout(request):
        raise httpx.ReadTimeout("timed out", request=request)

    seen: list[float] = []

    def client(timeout):
        seen.append(timeout)
        return httpx.Client(transport=httpx.MockTransport(always_timeout), base_url="http://local")

    provider = OpenAICompatibleProvider(
        "http://local/v1", "m", api_key="k", sleep=lambda _: None,
        timeout=llm.FULL_MODEL_TIMEOUT_SECONDS,
    )
    import unittest.mock
    with unittest.mock.patch.object(llm, "new_http_client", client):
        for _ in range(2):
            with pytest.raises(LLMError, match="unreachable"):
                provider.complete_detailed("s", "u", SCHEMA)

    # Two tickers, each asked twice, every ask on the full ceiling.
    assert seen == [300.0, 300.0] * 2


def test_a_shorter_caller_ceiling_is_never_raised_by_the_retry():
    """The screening path asks at REQUEST_TIMEOUT_SECONDS (120s). The retry
    takes the smaller of that and its own ceiling, so fixing the full model's
    retry cannot lengthen the screen's."""
    def always_timeout(request):
        raise httpx.ReadTimeout("timed out", request=request)

    seen: list[float] = []

    def client(timeout):
        seen.append(timeout)
        return httpx.Client(transport=httpx.MockTransport(always_timeout), base_url="http://local")

    provider = OpenAICompatibleProvider("http://local/v1", "m", api_key="k", sleep=lambda _: None,
                                        timeout=llm.REQUEST_TIMEOUT_SECONDS)
    import unittest.mock
    with unittest.mock.patch.object(llm, "new_http_client", client):
        with pytest.raises(LLMError, match="unreachable"):
            provider.complete_detailed("s", "u", SCHEMA)
    assert seen == [llm.REQUEST_TIMEOUT_SECONDS] * 2


def test_the_error_counts_the_asks_actually_made():
    """A timeout and its one retry are two asks. The text used to say
    "gave up after 4 attempt(s)" whatever happened."""
    def always_timeout(request):
        raise httpx.ReadTimeout("timed out", request=request)

    provider = OpenAICompatibleProvider("http://local/v1", "m", api_key="k", sleep=lambda _: None,
                                        timeout=llm.FULL_MODEL_TIMEOUT_SECONDS)
    import unittest.mock
    with unittest.mock.patch.object(
        llm, "new_http_client",
        lambda timeout: httpx.Client(transport=httpx.MockTransport(always_timeout), base_url="http://local"),
    ):
        with pytest.raises(LLMError, match=r"gave up after 2 attempt\(s\)"):
            provider.complete_detailed("s", "u", SCHEMA)


def test_every_ask_is_logged_with_its_ticker_try_duration_and_answer_length(caplog):
    """The call log the owner asked for on 26 Sep: name, start, how long,
    answer length, and first or second try."""
    calls = {"n": 0}

    def flaky(request):
        calls["n"] += 1
        if calls["n"] == 1:
            raise httpx.ReadTimeout("timed out", request=request)
        body = _body()
        body["usage"] = {"prompt_tokens": 900, "completion_tokens": 4321}
        return httpx.Response(200, json=body)

    provider = OpenAICompatibleProvider("http://local/v1", "m", api_key="k", sleep=lambda _: None,
                                        timeout=llm.FULL_MODEL_TIMEOUT_SECONDS)
    import logging
    import unittest.mock
    with unittest.mock.patch.object(
        llm, "new_http_client",
        lambda timeout: httpx.Client(transport=httpx.MockTransport(flaky), base_url="http://local"),
    ), caplog.at_level(logging.INFO, logger=llm.log.name), llm.call_label("INDA"):
        provider.complete_detailed("s", "u", SCHEMA)

    lines = [r.getMessage() for r in caplog.records if r.getMessage().startswith("model call:")]
    assert len(lines) == 2
    assert lines[0].startswith("model call: INDA ask 1 (first) started ")
    assert "ReadTimeout after a 300s limit" in lines[0] and lines[0].endswith("output tokens n/a")
    assert lines[1].startswith("model call: INDA ask 2 (retry after a timeout) started ")
    assert "HTTP 200" in lines[1] and lines[1].endswith("output tokens 4321")


def test_the_call_label_is_per_thread_and_restored():
    import threading
    seen = {}
    with llm.call_label("A"):
        def other():
            seen["other"] = getattr(llm._CALL, "label", None)
        t = threading.Thread(target=other)
        t.start(); t.join()
        seen["inside"] = llm._CALL.label
    assert seen == {"other": None, "inside": "A"}
    assert getattr(llm._CALL, "label", None) is None


def test_a_transport_failure_is_never_asked_a_third_time():
    """It is the most expensive failure there is -- billed for whatever it
    generated before the socket gave up -- so it gets one more ask and no
    more, however many status attempts remain."""
    attempts = {"n": 0}

    def always_timeout(request):
        attempts["n"] += 1
        raise httpx.ReadTimeout("timed out", request=request)

    import unittest.mock
    provider = OpenAICompatibleProvider(
        "http://local/v1", "m", api_key="k", sleep=lambda _: None,
    )
    with unittest.mock.patch.object(
        llm, "new_http_client",
        lambda timeout: httpx.Client(transport=httpx.MockTransport(always_timeout),
                                     base_url="http://local"),
    ):
        with pytest.raises(LLMError, match="unreachable"):
            provider.complete_detailed("s", "u", SCHEMA)

    assert attempts["n"] == llm.TRANSPORT_ATTEMPTS
    assert llm.TRANSPORT_ATTEMPTS < llm.HTTP_ATTEMPTS


# --- the stage budget, which is what makes that retry affordable -----------


def test_a_ticker_the_budget_catches_fails_the_model_stage_and_nothing_else():
    """The honest place to bound the cycle's worst case. The old bound was
    arithmetic -- rounds times the per-call ceiling -- which described a cycle
    that was already broken, and was used to forbid the retry above."""
    asked: list[str] = []

    def slow(system, user, schema):
        asked.append(_ticker(user))
        return "{}"

    # A controlled clock rather than a real wait: the budget is set, and then
    # the stage is told more than that has passed before the first ticker.
    ticks = iter([0.0, 999.0, 999.0, 999.0])
    import unittest.mock
    prepared = [_prepared("AAPL"), _prepared("MSFT")]
    with unittest.mock.patch.object(hb.time, "monotonic", lambda: next(ticks)):
        answers = hb.batch_answers(
            tuple(prepared), slow, provider=_NoBatch(), max_workers=1,
            stage_budget_seconds=60.0,
        )
    assert asked == [], "a spent budget still asked"
    for ticker in ("AAPL", "MSFT"):
        assert isinstance(answers[ticker], LLMError)
        assert "budget" in str(answers[ticker])


def test_no_budget_means_no_deadline():
    """Every other caller -- the screen, the Anthropic fallback -- passes
    nothing and must be unaffected."""
    asked: list[str] = []

    def quick(system, user, schema):
        asked.append(_ticker(user))
        return "{}"

    hb.batch_answers(tuple([_prepared("AAPL")]), quick, provider=_NoBatch(), max_workers=1)
    assert asked == ["AAPL"]


class _NoBatch:
    """A provider with no submit_batch, so batch_answers goes live."""


def _prepared(ticker: str):
    return hb.PreparedTicker(
        ticker=ticker, context=None, system_prompt="sys",
        user_prompt=f"TICKER: {ticker}",
    )


def _ticker(user_prompt: str) -> str:
    return user_prompt.split("TICKER:", 1)[1].strip()
