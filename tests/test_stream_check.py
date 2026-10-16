"""The stream check (replay/stream_check.py, the owner's decision of 16 Oct 2026).

It re-sends archived production asks with ``stream: true``. These pin what it
picks, what it sends, how it reads a stream, and that the workflow asks with
the production key and nothing more.
"""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import yaml

from replay import stream_check

ROOT = Path(__file__).resolve().parent.parent
BODY = {"model": "openai/gpt-oss-120b", "messages": [{"role": "system", "content": "s"}, {"role": "user", "content": "u"}],
        "max_tokens": 16000, "reasoning_effort": "high"}


def record(ticker: str, outcome: str, latency_ms: int, sha: str, body: dict = BODY, **extra) -> dict:
    return {"provider": "openai-compatible", "ticker": ticker, "outcome": outcome, "latency_ms": latency_ms,
            "prompt_sha256": sha, "request": json.dumps(body), "kind": "first", **extra}


# --------------------------------------------------------------------------- #
# Which asks are re-sent
# --------------------------------------------------------------------------- #


def test_the_cut_asks_come_first_then_timeouts_then_the_slowest_answers():
    records = [
        record("AAA", "answer", 100_000, "a"),
        record("BBB", "timeout", 480_000, "b"),
        record("CCC", "transport_error", 270_000, "c"),
        record("DDD", "answer", 250_000, "d"),
    ]
    chosen = stream_check.candidates(records, count=10)
    assert [c.ticker for c in chosen] == ["CCC", "BBB", "DDD", "AAA"]
    assert chosen[0].archived == "transport_error after 270s"


def test_one_body_per_prompt_and_the_count_is_a_cap():
    records = [
        record("CCC", "transport_error", 270_000, "same"),
        record("CCC", "transport_error", 271_000, "same", kind="retry after a timeout"),
        record("EEE", "transport_error", 265_000, "e"),
        record("FFF", "answer", 200_000, "f"),
    ]
    chosen = stream_check.candidates(records, count=2)
    assert [c.ticker for c in chosen] == ["CCC", "EEE"]


def test_records_that_are_not_openai_compatible_bodies_are_skipped():
    records = [
        {"provider": "anthropic", "ticker": "AAA", "outcome": "answer", "latency_ms": 1, "prompt_sha256": "a",
         "request": json.dumps(BODY)},
        record("BBB", "transport_error", 270_000, "b", body={"not": "a chat body"}),
        {**record("CCC", "transport_error", 270_000, "c"), "request": None},   # withheld
        record("DDD", "answer", 50_000, "d"),
    ]
    assert [c.ticker for c in stream_check.candidates(records, count=10)] == ["DDD"]


def test_the_streamed_body_is_the_archived_one_plus_the_stream_flags():
    asked = stream_check.streamed_body(BODY)
    assert asked["stream"] is True and asked["stream_options"] == {"include_usage": True}
    assert {k: v for k, v in asked.items() if k not in ("stream", "stream_options")} == BODY
    assert "stream" not in BODY


# --------------------------------------------------------------------------- #
# Reading a stream
# --------------------------------------------------------------------------- #


def sse(*chunks: dict) -> bytes:
    lines = [f"data: {json.dumps(c)}\n\n" for c in chunks]
    lines.append("data: [DONE]\n\n")
    return "".join(lines).encode()


def test_a_streamed_answer_is_gathered_chunk_by_chunk_with_its_usage():
    answer = json.dumps({"ticker": "XLE", "bias": "NEUTRAL", "conviction": 0.0, "rationale": "r"})
    chunks = [
        {"choices": [{"delta": {"role": "assistant", "reasoning_content": "thinking..."}}]},
        {"choices": [{"delta": {"content": answer[:10]}}]},
        {"choices": [{"delta": {"content": answer[10:]}, "finish_reason": "stop"}]},
        {"choices": [], "usage": {"prompt_tokens": 1000, "completion_tokens": 200}},
    ]
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["body"] = json.loads(request.content)
        seen["auth"] = request.headers.get("Authorization")
        return httpx.Response(200, content=sse(*chunks), headers={"content-type": "text/event-stream"})

    candidate = stream_check.Candidate("XLE", "first", "transport_error", 270_000, "x", BODY)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = stream_check.stream_ask(client, "https://example.test/v1/openai/chat/completions",
                                         {"Authorization": "Bearer k"}, candidate)
    assert seen["body"]["stream"] is True and seen["auth"] == "Bearer k"
    assert result.status == 200 and result.chunks == 4 and result.finish == "stop"
    assert result.content == answer and result.parses and result.verdict == "complete"
    assert result.reasoning_chars == len("thinking...")
    assert result.delta_keys == {"role", "reasoning_content", "content"}
    assert result.usage == {"prompt_tokens": 1000, "completion_tokens": 200}
    assert result.output_tokens == 200
    assert result.first_byte is not None and result.seconds >= 0


def test_a_cut_stream_is_an_error_and_the_key_is_not_in_the_line():
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.RemoteProtocolError("Server disconnected without sending a response.")

    candidate = stream_check.Candidate("JPM", "first", "transport_error", 270_000, "j", BODY)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = stream_check.stream_ask(client, "https://example.test/v1/openai/chat/completions",
                                         {"Authorization": "Bearer secret-key"}, candidate)
    assert result.error and result.error.startswith("RemoteProtocolError")
    assert result.verdict == "error"            # not in the cut band: the mock answers at once
    result.seconds = 270.0
    assert result.verdict == "cut"
    assert "secret-key" not in stream_check.line_for(result)


def test_a_plain_control_reads_the_production_shape():
    payload = {"choices": [{"message": {"content": json.dumps({"ticker": "JPM", "bias": "BULLISH", "conviction": 0.5,
                                                                "rationale": "r"})}, "finish_reason": "stop"}],
               "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
    handler = lambda request: httpx.Response(200, json=payload)  # noqa: E731
    candidate = stream_check.Candidate("JPM", "first", "transport_error", 270_000, "j", BODY)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = stream_check.plain_ask(client, "https://example.test/v1/openai/chat/completions", {}, candidate)
    assert result.mode == "plain" and result.verdict == "complete" and result.output_tokens == 5


def test_the_report_counts_what_matters():
    done = stream_check.Result("A", "streaming", "transport_error after 270s", status=200, seconds=310.0,
                               chunks=50, finish="stop", content=json.dumps({"ticker": "A", "bias": "NEUTRAL",
                                                                              "conviction": 0, "rationale": "r"}),
                               usage={"prompt_tokens": 1, "completion_tokens": 1}, model="openai/gpt-oss-120b")
    cut = stream_check.Result("B", "streaming", "transport_error after 270s", seconds=268.0,
                              error="RemoteProtocolError: Server disconnected")
    control = stream_check.Result("A", "plain", "transport_error after 270s", seconds=271.0,
                                  error="RemoteProtocolError: Server disconnected")
    text = stream_check.report([done, cut, control])
    assert "streaming: 1 of 2 complete (1 of them past 240s; longest 310s), 1 cut, 0 other errors" in text
    assert "control (plain): cut after 271s" in text
    assert "spent about $" in text


# --------------------------------------------------------------------------- #
# The workflow
# --------------------------------------------------------------------------- #


def test_the_workflow_asks_with_the_production_key_and_reads_only_the_artifact():
    wf = yaml.safe_load((ROOT / ".github/workflows/stream-check.yml").read_text(encoding="utf-8"))
    assert wf["permissions"] == {"contents": "read", "actions": "read"}
    job = wf["jobs"]["check"]
    env = next(s for s in job["steps"] if s.get("name", "").startswith("Re-send"))["env"]
    vote = yaml.safe_load((ROOT / ".github/workflows/shadow-universe.yml").read_text(encoding="utf-8"))
    vote_env = next(s for s in vote["jobs"]["vote"]["steps"] if s.get("name") == "Vote")["env"]
    assert env["FULL_MODEL_API_KEY"] == vote_env["FULL_MODEL_API_KEY"]
    assert not any(k.startswith("ALPACA") or k.startswith("ANTHROPIC") or k.startswith("BRIGHTDATA") for k in env)
    triggers = wf.get("on") or wf.get(True)      # yaml reads a bare `on` as the boolean
    assert "replay/stream_check.py" in triggers["pull_request"]["paths"]


# --------------------------------------------------------------------------- #
# "Model busy" is waited out (the first run, 16 Oct 2026, measured nothing)
# --------------------------------------------------------------------------- #


BUSY = {"error": {"message": "Model busy, retry later", "type": "invalid_request_error", "code": "engine_overloaded"}}


def test_a_busy_stream_is_asked_again_after_the_ladder_and_then_counts():
    answer = json.dumps({"ticker": "EWY", "bias": "NEUTRAL", "conviction": 0.0, "rationale": "r"})
    calls = []
    slept = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) <= 2:
            return httpx.Response(429, json=BUSY)
        return httpx.Response(200, content=sse({"choices": [{"delta": {"content": answer}, "finish_reason": "stop"}],
                                                "usage": {"prompt_tokens": 1, "completion_tokens": 2}}))

    candidate = stream_check.Candidate("EWY", "first", "transport_error", 278_000, "e", BODY)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = stream_check.stream_ask(client, "https://example.test/v1/openai/chat/completions", {}, candidate,
                                         sleep=slept.append)
    assert len(calls) == 3 and result.busy == 2 and result.verdict == "complete"
    assert slept == [30.0, 60.0]
    assert "after 2 busy" in stream_check.line_for(result)


def test_retry_after_wins_over_the_ladder_when_sane():
    assert stream_check.busy_wait(httpx.Response(429, headers={"Retry-After": "7"}), 0) == 7.0
    assert stream_check.busy_wait(httpx.Response(429, headers={"Retry-After": "9999"}), 1) == 60.0
    assert stream_check.busy_wait(httpx.Response(429, headers={"Retry-After": "soon"}), 2) == 120.0
    assert stream_check.busy_wait(httpx.Response(429), 5) == 120.0


def test_four_busy_answers_are_the_real_answer():
    calls = []
    handler = lambda request: (calls.append(1), httpx.Response(429, json=BUSY))[1]  # noqa: E731
    candidate = stream_check.Candidate("IWM", "first", "transport_error", 278_000, "i", BODY)
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        streamed = stream_check.stream_ask(client, "https://example.test/v1/openai/chat/completions", {}, candidate,
                                           sleep=lambda s: None)
        plain = stream_check.plain_ask(client, "https://example.test/v1/openai/chat/completions", {}, candidate,
                                       sleep=lambda s: None)
    assert len(calls) == 8 and streamed.busy == 3 and plain.busy == 3
    assert streamed.verdict == "error" and "HTTP 429" in streamed.error
    assert plain.verdict == "error" and "HTTP 429" in plain.error
    text = stream_check.report([streamed, plain])
    assert "6 busy answer(s) waited out" in text
