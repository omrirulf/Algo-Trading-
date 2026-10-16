#!/usr/bin/env python3
"""Does streaming get past the provider's ~270-second cut? Archived production asks, re-sent with ``stream``.

    python replay/stream_check.py --model-io "$RUNNER_TEMP/model_io" [--count 10] [--control 1] [--workers 4]

Since 12 Oct 2026 DeepInfra has ended long answers without a response
("Server disconnected without sending a response") at about 260-280
seconds: on 15 Oct 25 of 88 asks, every one between 262 and 273 seconds,
and no answer that day took longer than 273. A connection that carries
nothing for that long looks idle to whatever sits in front of the model.
Streaming sends the answer as it is generated, so the connection is never
silent; this asks whether that is enough -- the owner's decision of 16 Oct
2026 to test it before building it.

It reads the model-io archive of a production run (the artifact
``heartbeat.yml`` keeps of ``logs/model_io/``), takes the asks the transport
cut -- the disconnects first, then the timeouts, then the slowest answers --
one body per prompt, and re-sends each through the production provider's
URL and key with ``stream: true`` and ``stream_options: {"include_usage":
true}``, the body otherwise byte-for-byte the archived one. For each ask it
prints the time to the first byte, the time to the end, the chunks, how the
stream ended, whether the answer parses as a signal, the tokens and the
cost. A control sends the same body the production way, without streaming,
to see whether the cut is still there today.

It asks the model and pays for it (about a cent an ask) and otherwise only
prints: no journal, no file, no trade, no broker key. The key goes only into
the Authorization header and never into the output.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from orchestrator import heartbeat, llm, pricing  # noqa: E402

#: The outcomes a cut ask was recorded with (orchestrator/llm.py): the
#: disconnect is "transport_error", the 480-second ceiling is "timeout".
CUT_OUTCOMES = ("transport_error", "timeout")
#: The band the cut was seen in on 15 and 16 Oct 2026: 262 to 278 seconds.
#: An error inside it is read as the cut; one elsewhere is something else.
CUT_BAND_SECONDS = (240.0, 300.0)
CONNECT_SECONDS = 30.0
#: Between two chunks of a stream, or for the whole of a plain answer: the
#: production ceiling, so the comparison is on the same terms.
READ_SECONDS = llm.FULL_MODEL_TIMEOUT_SECONDS
#: "Model busy, retry later" (HTTP 429) is waited out, as production waits
#: it out: the first run of this check (16 Oct 2026, 19:52 UTC) got it on
#: all eleven asks within eight seconds and measured nothing. The server's
#: own Retry-After wins when it gives one and it is sane; otherwise the
#: ladder below, and at most BUSY_ASKS asks of one body.
BUSY_ASKS = 4
BUSY_WAITS = (30.0, 60.0, 120.0)
RETRY_AFTER_CAP_SECONDS = 120.0
REQUIRED_KEYS = tuple(heartbeat.SIGNAL_JSON_SCHEMA.get("required") or ("ticker", "bias", "conviction", "rationale"))


@dataclass
class Candidate:
    """One archived ask worth re-sending."""

    ticker: str
    kind: str
    outcome: str
    latency_ms: int
    prompt_sha256: str
    body: dict[str, Any]

    @property
    def archived(self) -> str:
        return f"{self.outcome} after {self.latency_ms / 1000:.0f}s"


@dataclass
class Result:
    """What one re-sent ask came back with."""

    ticker: str
    mode: str
    archived: str
    status: Optional[int] = None
    first_byte: Optional[float] = None
    seconds: float = 0.0
    chunks: int = 0
    finish: Optional[str] = None
    content: str = ""
    reasoning_chars: int = 0
    delta_keys: set = field(default_factory=set)
    usage: Optional[dict[str, Any]] = None
    error: Optional[str] = None
    model: str = ""
    #: "Model busy" answers waited out before this one.
    busy: int = 0
    #: The HTTP response of this ask, for its Retry-After; never printed.
    response: Any = None

    @property
    def parses(self) -> bool:
        try:
            answer = json.loads(self.content)
        except (TypeError, ValueError):
            return False
        return isinstance(answer, dict) and all(key in answer for key in REQUIRED_KEYS)

    @property
    def verdict(self) -> str:
        if self.error is None and self.status == 200 and self.content:
            return "complete" if self.parses else "answered, not a signal"
        low, high = CUT_BAND_SECONDS
        if self.error and low <= self.seconds <= high:
            return "cut"
        return "error"

    @property
    def output_tokens(self) -> Optional[int]:
        usage = self.usage or {}
        tokens = usage.get("completion_tokens")
        return tokens if isinstance(tokens, int) else None

    @property
    def cost_usd(self) -> Optional[float]:
        usage = self.usage or {}
        if not isinstance(usage.get("completion_tokens"), int):
            return None
        return pricing.cost_usd(llm.Usage(model=self.model,
                                          input_tokens=int(usage.get("prompt_tokens") or 0),
                                          output_tokens=int(usage.get("completion_tokens") or 0)))


# --------------------------------------------------------------------------- #
# The archive
# --------------------------------------------------------------------------- #


def read_records(directory: Path) -> list[dict[str, Any]]:
    """Every call record under ``directory`` (the artifact's ``*.jsonl`` files)."""
    records: list[dict[str, Any]] = []
    for path in sorted(directory.rglob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(record, dict):
                records.append(record)
    return records


def _rank(record: dict[str, Any]) -> tuple[int, int]:
    outcome = record.get("outcome")
    order = 0 if outcome == "transport_error" else 1 if outcome == "timeout" else 2
    return order, -int(record.get("latency_ms") or 0)


def candidates(records: list[dict[str, Any]], count: int) -> list[Candidate]:
    """One body per prompt: the cut asks first (disconnects, then timeouts), then the slowest answers."""
    seen: set[str] = set()
    out: list[Candidate] = []
    usable = (r for r in records
              if r.get("provider") == "openai-compatible" and isinstance(r.get("request"), str))
    for record in sorted(usable, key=_rank):
        sha = record.get("prompt_sha256")
        if not isinstance(sha, str) or sha in seen:
            continue
        try:
            body = json.loads(record["request"])
        except json.JSONDecodeError:
            continue
        if not isinstance(body, dict) or not isinstance(body.get("messages"), list):
            continue
        seen.add(sha)
        out.append(Candidate(str(record.get("ticker") or "?"), str(record.get("kind") or "?"),
                             str(record.get("outcome") or "?"), int(record.get("latency_ms") or 0), sha, body))
        if len(out) >= count:
            break
    return out


# --------------------------------------------------------------------------- #
# The asks
# --------------------------------------------------------------------------- #


def streamed_body(body: dict[str, Any]) -> dict[str, Any]:
    """The archived body with streaming asked for, nothing else changed."""
    asked = json.loads(json.dumps(body))
    asked["stream"] = True
    asked["stream_options"] = {"include_usage": True}
    return asked


def busy_wait(response: Any, attempt: int) -> float:
    """How long to wait after the ``attempt``-th busy answer: Retry-After when sane, else the ladder."""
    raw = (getattr(response, "headers", None) or {}).get("Retry-After")
    try:
        seconds = float(str(raw).strip()) if raw else None
    except ValueError:
        seconds = None
    if seconds is not None and 0 <= seconds <= RETRY_AFTER_CAP_SECONDS:
        return seconds
    return BUSY_WAITS[min(attempt, len(BUSY_WAITS) - 1)]


def stream_ask(client: httpx.Client, url: str, headers: dict[str, str], candidate: Candidate,
               sleep: Any = time.sleep) -> Result:
    """One ask with ``stream: true``, busy answers waited out: the answer gathered chunk by chunk, timed."""
    busy = 0
    for attempt in range(BUSY_ASKS):
        result = _stream_once(client, url, headers, candidate)
        result.busy = busy
        if result.status != 429 or attempt == BUSY_ASKS - 1:
            return result
        busy += 1
        sleep(busy_wait(result.response, attempt))
    return result  # pragma: no cover - the loop always returns


def _stream_once(client: httpx.Client, url: str, headers: dict[str, str], candidate: Candidate) -> Result:
    body = streamed_body(candidate.body)
    result = Result(candidate.ticker, "streaming", candidate.archived, model=str(body.get("model") or ""))
    clock = time.monotonic()
    try:
        with client.stream("POST", url, json=body, headers=headers) as response:
            result.status = response.status_code
            result.response = response
            if response.status_code != 200:
                result.error = f"HTTP {response.status_code}: {response.read()[:300]!r}"
            else:
                for raw in response.iter_lines():
                    if result.first_byte is None:
                        result.first_byte = time.monotonic() - clock
                    if not raw.startswith("data:"):
                        continue
                    data = raw[5:].strip()
                    if data == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data)
                    except json.JSONDecodeError:
                        continue
                    result.chunks += 1
                    _take_chunk(result, chunk)
    except httpx.HTTPError as exc:
        result.error = f"{type(exc).__name__}: {str(exc)[:160]}"
    result.seconds = time.monotonic() - clock
    return result


def _take_chunk(result: Result, chunk: Any) -> None:
    if not isinstance(chunk, dict):
        return
    if isinstance(chunk.get("usage"), dict):
        result.usage = chunk["usage"]
    for choice in chunk.get("choices") or []:
        if not isinstance(choice, dict):
            continue
        delta = choice.get("delta") if isinstance(choice.get("delta"), dict) else {}
        result.delta_keys |= set(delta)
        piece = delta.get("content")
        if isinstance(piece, str):
            result.content += piece
        for key in ("reasoning_content", "reasoning"):
            thought = delta.get(key)
            if isinstance(thought, str):
                result.reasoning_chars += len(thought)
        finish = choice.get("finish_reason")
        if isinstance(finish, str) and finish:
            result.finish = finish


def plain_ask(client: httpx.Client, url: str, headers: dict[str, str], candidate: Candidate,
              sleep: Any = time.sleep) -> Result:
    """The same body the production way, busy answers waited out: one POST, one answer, the production ceiling."""
    busy = 0
    for attempt in range(BUSY_ASKS):
        result = _plain_once(client, url, headers, candidate)
        result.busy = busy
        if result.status != 429 or attempt == BUSY_ASKS - 1:
            return result
        busy += 1
        sleep(busy_wait(result.response, attempt))
    return result  # pragma: no cover - the loop always returns


def _plain_once(client: httpx.Client, url: str, headers: dict[str, str], candidate: Candidate) -> Result:
    result = Result(candidate.ticker, "plain", candidate.archived, model=str(candidate.body.get("model") or ""))
    clock = time.monotonic()
    try:
        response = client.post(url, json=candidate.body, headers=headers)
        result.status = response.status_code
        result.response = response
        result.first_byte = result.seconds = time.monotonic() - clock
        if response.status_code != 200:
            result.error = f"HTTP {response.status_code}: {response.text[:300]!r}"
        else:
            payload = response.json()
            choice = (payload.get("choices") or [{}])[0] if isinstance(payload, dict) else {}
            message = choice.get("message") if isinstance(choice, dict) else {}
            if isinstance(message, dict) and isinstance(message.get("content"), str):
                result.content = message["content"]
            if isinstance(choice, dict) and isinstance(choice.get("finish_reason"), str):
                result.finish = choice["finish_reason"]
            if isinstance(payload, dict) and isinstance(payload.get("usage"), dict):
                result.usage = payload["usage"]
    except (httpx.HTTPError, ValueError) as exc:
        result.error = f"{type(exc).__name__}: {str(exc)[:160]}"
    result.seconds = time.monotonic() - clock
    return result


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


def line_for(result: Result) -> str:
    first = f"{result.first_byte:6.1f}s" if result.first_byte is not None else "     -"
    tokens = f"{result.output_tokens:6d}" if result.output_tokens is not None else "     -"
    cost = f"${result.cost_usd:.4f}" if result.cost_usd is not None else "$-"
    tail = result.error or f"finish {result.finish or '-'}, {len(result.content)} chars, parses {'yes' if result.parses else 'no'}"
    waited = f" after {result.busy} busy" if result.busy else ""
    return (f"{result.ticker:<6} {result.mode:<9} archived {result.archived:<24} -> {result.verdict:<22} "
            f"first byte {first} end {result.seconds:7.1f}s chunks {result.chunks:5d} out tokens {tokens} {cost}{waited} | {tail}")


def report(results: list[Result]) -> str:
    streaming = [r for r in results if r.mode == "streaming"]
    plain = [r for r in results if r.mode == "plain"]
    lines = [line_for(r) for r in results]
    keys = sorted(set().union(*(r.delta_keys for r in streaming))) if streaming else []
    lines.append("")
    lines.append(f"delta keys seen: {', '.join(keys) or '-'}; usage in the stream: "
                 f"{sum(1 for r in streaming if r.usage)} of {len(streaming)}")
    complete = [r for r in streaming if r.verdict == "complete"]
    cut = [r for r in streaming if r.verdict == "cut"]
    longest = max((r.seconds for r in complete), default=0.0)
    past = sum(1 for r in complete if r.seconds > CUT_BAND_SECONDS[0])
    spent = sum(r.cost_usd or 0.0 for r in results)
    lines.append(f"streaming: {len(complete)} of {len(streaming)} complete ({past} of them past "
                 f"{CUT_BAND_SECONDS[0]:.0f}s; longest {longest:.0f}s), {len(cut)} cut, "
                 f"{len(streaming) - len(complete) - len(cut)} other errors")
    for r in plain:
        lines.append(f"control (plain): {r.verdict} after {r.seconds:.0f}s"
                     + (f" ({r.error})" if r.error else ""))
    waited = sum(r.busy for r in results)
    lines.append(f"spent about ${spent:.3f} on {len(results)} asks; {waited} busy answer(s) waited out")
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--model-io", required=True, type=Path, help="directory with the run's model-io files")
    parser.add_argument("--count", type=int, default=10, help="archived asks to re-send with streaming")
    parser.add_argument("--control", type=int, default=1, help="of those, also sent the production way")
    parser.add_argument("--workers", type=int, default=4, help="asks in flight at once (production asks 4)")
    args = parser.parse_args(argv)

    records = read_records(args.model_io)
    chosen = candidates(records, max(0, args.count))
    if not chosen:
        print(f"no archived openai-compatible ask under {args.model_io} ({len(records)} records)")
        return 1
    provider = heartbeat.full_model_provider()
    url = getattr(provider, "_url", None)
    key = getattr(provider, "_api_key", "")
    if not isinstance(url, str) or not url:
        print("the production provider is not an OpenAI-compatible endpoint; nothing to stream")
        return 1
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    cuts = sum(1 for c in chosen if c.outcome in CUT_OUTCOMES)
    print(f"{len(chosen)} archived asks ({cuts} cut by the transport, {len(chosen) - cuts} slow answers), "
          f"{args.workers} at a time, streaming, against {llm._hostname(url)}")
    timeout = httpx.Timeout(connect=CONNECT_SECONDS, read=READ_SECONDS, write=CONNECT_SECONDS, pool=CONNECT_SECONDS)
    with httpx.Client(timeout=timeout) as client:
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
            results = list(pool.map(lambda c: stream_ask(client, url, headers, c), chosen))
        for candidate in chosen[:max(0, args.control)]:
            results.append(plain_ask(client, url, headers, candidate))
    print(report(results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
