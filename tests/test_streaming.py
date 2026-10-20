"""The full model's answer is streamed (the owner's decision of 16 Oct 2026).

From 12 Oct 2026 DeepInfra ended a request that had carried nothing for
about 270 seconds; with ``stream: true`` the connection is never silent.
These pin that the body asks for the stream, that a streamed answer is put
back together into the plain answer's shape before anything reads it (the
parsing, the re-asks and the record are unchanged), that a plain answer is
still read plainly, that the ceiling bounds the whole answer, and that a
stream cut by the server is the transport failure it always was.
"""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from orchestrator import llm, model_io

URL = "https://api.example.test/v1/openai"
SCHEMA = {"type": "object", "properties": {"ticker": {"type": "string"}, "bias": {"type": "string"},
                                           "conviction": {"type": "number"}, "rationale": {"type": "string"}},
          "required": ["ticker", "bias", "conviction", "rationale"]}
ANSWER = json.dumps({"ticker": "XLE", "bias": "NEUTRAL", "conviction": 0.0, "rationale": "r"})


def sse(*chunks) -> bytes:
    lines = []
    for chunk in chunks:
        lines.append(f"data: {json.dumps(chunk)}\n\n" if not isinstance(chunk, str) else chunk + "\n\n")
    lines.append("data: [DONE]\n\n")
    return "".join(lines).encode()


def stream_response(*chunks, status: int = 200) -> httpx.Response:
    return httpx.Response(status, content=sse(*chunks), headers={"content-type": "text/event-stream"})


def provider(handler, **kwargs) -> llm.OpenAICompatibleProvider:
    client = httpx.Client(transport=httpx.MockTransport(handler))
    return llm.OpenAICompatibleProvider(base_url=URL, model="openai/gpt-oss-120b", api_key="k", client=client,
                                        sleep=lambda s: None, **kwargs)


# --------------------------------------------------------------------------- #
# The body
# --------------------------------------------------------------------------- #


def test_the_body_asks_for_the_stream_and_its_usage():
    sent = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(json.loads(request.content))
        return stream_response({"choices": [{"delta": {"content": ANSWER}, "finish_reason": "stop"}]})

    p = provider(handler)
    p.complete_detailed("s", "u", SCHEMA)
    assert llm.STREAMING is True
    assert sent[0]["stream"] is True and sent[0]["stream_options"] == {"include_usage": True}
    assert p.request_body("s", "u", SCHEMA) == sent[0]          # what the voting arm rebuilds


# --------------------------------------------------------------------------- #
# A streamed answer
# --------------------------------------------------------------------------- #


def test_a_streamed_answer_is_put_back_together_and_recorded_as_one_document(tmp_path: Path):
    chunks = [
        {"id": "chatcmpl-1", "object": "chat.completion.chunk", "created": 1, "model": "openai/gpt-oss-120b",
         "choices": [{"index": 0, "delta": {"role": "assistant", "reasoning_content": "think"}}]},
        {"choices": [{"index": 0, "delta": {"reasoning_content": "ing"}}]},
        {"choices": [{"index": 0, "delta": {"content": ANSWER[:12]}}]},
        ": keep-alive",
        {"choices": [{"index": 0, "delta": {"content": ANSWER[12:]}, "finish_reason": "stop"}]},
        {"choices": [], "usage": {"prompt_tokens": 1234, "completion_tokens": 567}},
    ]
    handler = lambda request: stream_response(*chunks)  # noqa: E731
    with model_io.capture(tmp_path, "run-1"):
        completion = provider(handler).complete_detailed("s", "u", SCHEMA)
    assert completion.text == ANSWER
    assert completion.usage.input_tokens == 1234 and completion.usage.output_tokens == 567
    records = [json.loads(line) for path in tmp_path.rglob("*.jsonl") for line in path.read_text().splitlines()]
    assert len(records) == 1 and records[0]["outcome"] == "answer" and records[0]["status"] == 200
    kept = json.loads(records[0]["response"])
    assert kept["choices"][0]["message"] == {"role": "assistant", "content": ANSWER, "reasoning_content": "thinking"}
    assert kept["choices"][0]["finish_reason"] == "stop"
    assert kept["usage"] == {"prompt_tokens": 1234, "completion_tokens": 567}
    assert kept["id"] == "chatcmpl-1" and kept["model"] == "openai/gpt-oss-120b" and kept["object"] == "chat.completion"
    assert records[0]["usage"] == {"prompt_tokens": 1234, "completion_tokens": 567}
    assert "data:" not in records[0]["response"]                # the document, not the event stream


def test_a_streamed_answer_with_nothing_in_it_is_the_empty_answer_it_always_was():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) < llm.SCHEMA_ATTEMPTS:
            return stream_response({"choices": [{"delta": {"reasoning_content": "hm"}, "finish_reason": "length"}]})
        return stream_response({"choices": [{"delta": {"content": ANSWER}, "finish_reason": "stop"}]})

    completion = provider(handler).complete_detailed("s", "u", SCHEMA)
    assert completion.text == ANSWER and len(calls) == llm.SCHEMA_ATTEMPTS     # re-asked, as an empty message is


def test_a_plain_answer_is_still_read_plainly():
    """A server that ignores ``stream`` (and every fake server in this suite) answers with one JSON body."""
    payload = {"choices": [{"message": {"content": ANSWER}, "finish_reason": "stop"}],
               "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
    completion = provider(lambda request: httpx.Response(200, json=payload)).complete_detailed("s", "u", SCHEMA)
    assert completion.text == ANSWER and completion.usage.output_tokens == 5


def test_a_busy_answer_while_streaming_is_waited_out_as_before():
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(429, json={"error": {"message": "Model busy, retry later"}},
                                  headers={"Retry-After": "3"})
        return stream_response({"choices": [{"delta": {"content": ANSWER}, "finish_reason": "stop"}]})

    slept = []
    client = httpx.Client(transport=httpx.MockTransport(handler))
    p = llm.OpenAICompatibleProvider(base_url=URL, model="m", api_key="k", client=client, sleep=slept.append)
    assert p.complete_detailed("s", "u", SCHEMA).text == ANSWER
    assert len(calls) == 2 and slept == [3.0]


# --------------------------------------------------------------------------- #
# The ceiling, and a cut
# --------------------------------------------------------------------------- #


class _Slow(httpx.SyncByteStream):
    """A stream whose second chunk arrives after the clock has jumped past the ceiling."""

    def __init__(self, clock: list[float]) -> None:
        self._clock = clock

    def __iter__(self):
        yield sse({"choices": [{"delta": {"content": "{"}}]})[:-len("data: [DONE]\n\n")]
        self._clock[0] += 10_000.0
        yield sse({"choices": [{"delta": {"content": "}"}, "finish_reason": "stop"}]})


def test_a_stream_that_runs_past_the_ceiling_is_a_timeout_and_gets_the_one_retry(monkeypatch):
    clock = [1000.0]
    monkeypatch.setattr(llm.time, "monotonic", lambda: clock[0])
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(200, stream=_Slow(clock), headers={"content-type": "text/event-stream"})
        return stream_response({"choices": [{"delta": {"content": ANSWER}, "finish_reason": "stop"}]})

    completion = provider(handler, timeout=480.0).complete_detailed("s", "u", SCHEMA)
    assert completion.text == ANSWER and len(calls) == 2


def test_a_stream_the_server_cuts_is_the_transport_failure_it_always_was(tmp_path: Path):
    class _Cut(httpx.SyncByteStream):
        def __iter__(self):
            yield b"data: {\"choices\": [{\"delta\": {\"content\": \"{\"}}]}\n\n"
            raise httpx.RemoteProtocolError("Server disconnected without sending a response.")

    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(200, stream=_Cut(), headers={"content-type": "text/event-stream"})

    with model_io.capture(tmp_path, "run-2"):
        with pytest.raises(llm.LLMError) as caught:
            provider(handler).complete_detailed("s", "u", SCHEMA)
    assert "Server disconnected" in str(caught.value) and f"gave up after {llm.TRANSPORT_ATTEMPTS} attempt" in str(caught.value)
    assert len(calls) == llm.TRANSPORT_ATTEMPTS
    records = [json.loads(line) for path in tmp_path.rglob("*.jsonl") for line in path.read_text().splitlines()]
    assert [r["outcome"] for r in records] == ["transport_error"] * llm.TRANSPORT_ATTEMPTS
    assert records[1]["kind"] == "retry after a timeout"


def test_assemble_stream_skips_what_is_not_a_chunk():
    lines = ["", ": ping", "data: not json", "data: [1, 2]", 'data: {"choices": [{"delta": {"content": "ok"}}]}',
             "data: [DONE]", 'data: {"choices": [{"delta": {"content": "ignored after DONE"}}]}']
    payload = llm._assemble_stream(lines, deadline=float("inf"), timeout=480.0)
    assert payload["choices"][0]["message"] == {"role": "assistant", "content": "ok"}
    assert payload["choices"][0]["finish_reason"] is None and "usage" not in payload


def test_an_event_stream_without_its_content_type_is_still_read_as_the_stream():
    body = sse({"choices": [{"delta": {"content": ANSWER}, "finish_reason": "stop"}]})
    handler = lambda request: httpx.Response(200, content=body, headers={"content-type": "text/plain"})  # noqa: E731
    assert provider(handler).complete_detailed("s", "u", SCHEMA).text == ANSWER
