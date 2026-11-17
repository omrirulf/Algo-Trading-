#!/usr/bin/env python3
"""Does the second host answer production's question? One ask, production's request shape, nothing traded.

    python replay/model_fallback_check.py [--model-io DIR] [--count 1] [--workers 4]

The owner's fallback of 17 Nov 2026 (``orchestrator.llm.FallbackSignalProvider``):
when the configured host cannot answer at all, the same model is asked at a
second host (``FALLBACK_MODEL_BASE_URL``). That host is never asked until
its key is set, and it should be asked once by hand before the cycle relies
on it. This script is that ask. It builds the fallback provider exactly as
the cycle does (``heartbeat.fallback_model_provider``) and asks it through
production's own call path -- ``complete_detailed`` with the production
schema, the production reasoning effort, streaming with usage, the schema
check and the re-asks -- then prints what came back: the seconds, whether
the answer parses as a signal for the right name, the token counts and
whether the host reported usage at all. The request's shape is printed too
(its parameters, never the messages), so a host that rejects a field is
found here and not at 15:00 on a cycle day.

The question is a production one when it can be: an archived first ask
from a production run's model calls (the artifact ``heartbeat.yml`` keeps of
``logs/model_io/``, ``--model-io``), its system and user prompt re-sent as
they were. Without an archive, the prompt production would build from an
empty context, which checks the shape and the schema but not a real answer's
length. ``--count`` asks that many distinct names, ``--workers`` at a time
(production asks four at a time, and a host's rate limit is part of what is
being checked).

It asks the model and pays for it (a cent or so an ask) and otherwise only
prints: no journal, no file, no trade, no broker key. The key goes only
into the Authorization header and never into the output. Exit 0 when every
answer was a signal for its name, 1 when one was not, 2 when there is no
key to check with.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from orchestrator import heartbeat, llm  # noqa: E402
from orchestrator.context import TickerContext  # noqa: E402
from replay.stream_check import read_records  # noqa: E402

#: The exit codes, so a workflow can tell "the host failed" from "nothing to check".
EXIT_OK = 0
EXIT_FAILED = 1
EXIT_NO_KEY = 2

#: The name the built-in question is about when there is no archive to take one from.
BUILTIN_TICKER = "SPY"

#: The request fields the report shows, in this order; the messages are never shown.
SHOWN_FIELDS = ("model", "max_tokens", "reasoning_effort", "stream", "stream_options", "response_format")


@dataclass
class Question:
    """One ask: the prompts production sent, or would send."""

    ticker: str
    system: str
    user: str
    source: str


@dataclass
class Result:
    """What one ask came back with."""

    ticker: str
    source: str
    seconds: float = 0.0
    text: str = ""
    model: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    error: Optional[str] = None

    @property
    def parsed_for(self) -> Optional[str]:
        """The ticker the answer is a signal for, or None when it is not a signal."""
        if self.error is not None:
            return None
        try:
            return heartbeat.parse_signal(self.text).ticker
        except Exception:  # noqa: BLE001 - any failure to parse is "not a signal"
            return None

    @property
    def ok(self) -> bool:
        return self.parsed_for == self.ticker

    @property
    def verdict(self) -> str:
        if self.error is not None:
            return "error"
        answered = self.parsed_for
        if answered is None:
            return "answered, not a signal"
        if answered != self.ticker:
            return f"a signal for {answered}, not {self.ticker}"
        return "a signal"

    @property
    def usage_reported(self) -> bool:
        return self.input_tokens > 0 or self.output_tokens > 0


# --------------------------------------------------------------------------- #
# The questions
# --------------------------------------------------------------------------- #


def archived_questions(directory: Path, count: int) -> list[Question]:
    """``count`` production first asks, one per name, from the archive under ``directory``; newest first."""
    out: list[Question] = []
    seen: set[str] = set()
    usable = [r for r in read_records(directory)
              if r.get("provider") == "openai-compatible" and r.get("kind") == "first"
              and isinstance(r.get("request"), str) and r.get("ticker")]
    for record in sorted(usable, key=lambda r: str(r.get("ts") or ""), reverse=True):
        ticker = str(record["ticker"])
        if ticker in seen:
            continue
        try:
            body = json.loads(record["request"])
            system, user = body["messages"][0]["content"], body["messages"][1]["content"]
        except (ValueError, KeyError, IndexError, TypeError):
            continue
        if not isinstance(system, str) or not isinstance(user, str):
            continue
        seen.add(ticker)
        out.append(Question(ticker, system, user, f"archived ask of {str(record.get('ts') or '?')[:16]}"))
        if len(out) >= count:
            break
    return out


def builtin_question() -> Question:
    """The question production would ask about ``BUILTIN_TICKER`` with nothing gathered: the shape, not the length."""
    context = TickerContext(BUILTIN_TICKER)
    return Question(BUILTIN_TICKER, heartbeat.system_prompt_for(BUILTIN_TICKER, context),
                    heartbeat.build_user_prompt(context), "built-in question, empty context")


def questions(model_io: Optional[Path], count: int) -> list[Question]:
    if model_io is not None and model_io.is_dir():
        found = archived_questions(model_io, max(1, count))
        if found:
            return found
    return [builtin_question()]


# --------------------------------------------------------------------------- #
# The asks
# --------------------------------------------------------------------------- #


def ask(provider: Any, question: Question) -> Result:
    """One ask through production's call path, timed as a whole; the answer judged as the cycle judges it."""
    result = Result(question.ticker, question.source)
    clock = time.monotonic()
    try:
        completion = provider.complete_detailed(
            question.system, question.user, heartbeat.SIGNAL_JSON_SCHEMA,
            model=None, effort=heartbeat.full_model_effort(), check=heartbeat.parse_signal,
        )
        result.text = completion.text
        result.model = completion.usage.model
        result.input_tokens = completion.usage.input_tokens
        result.output_tokens = completion.usage.output_tokens
    except llm.LLMError as exc:
        result.error = f"LLMError: {str(exc)[:300]}"
    result.seconds = time.monotonic() - clock
    return result


def request_shape(provider: Any, question: Question) -> dict[str, Any]:
    """The request's parameters as production would send them to this host; the messages left out."""
    body = provider.request_body(question.system, question.user, heartbeat.SIGNAL_JSON_SCHEMA,
                                 model=None, effort=heartbeat.full_model_effort())
    shape = {key: body.get(key) for key in SHOWN_FIELDS if key in body}
    fmt = shape.get("response_format")
    if isinstance(fmt, dict):
        inner = fmt.get("json_schema") if isinstance(fmt.get("json_schema"), dict) else {}
        shape["response_format"] = {"type": fmt.get("type"), "name": inner.get("name"),
                                    "strict": inner.get("strict"), "schema_keys": len(inner.get("schema") or {})}
    return shape


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


def line_for(result: Result) -> str:
    tokens = f"in {result.input_tokens} out {result.output_tokens}" if result.usage_reported else "no usage reported"
    tail = result.error or f"{len(result.text)} chars, {tokens}"
    return f"{result.ticker:<6} {result.seconds:7.1f}s -> {result.verdict:<26} | {tail} ({result.source})"


def report(host: Optional[str], shape: dict[str, Any], results: list[Result]) -> str:
    lines = [f"fallback host: {host or '?'}",
             "request shape: " + json.dumps(shape, ensure_ascii=False, sort_keys=True),
             ""]
    lines.extend(line_for(r) for r in results)
    good = sum(1 for r in results if r.ok)
    longest = max((r.seconds for r in results), default=0.0)
    with_usage = sum(1 for r in results if r.error is None and r.usage_reported)
    answered = sum(1 for r in results if r.error is None)
    lines.append("")
    lines.append(f"fallback check: {good} of {len(results)} answered with a signal for the name asked; "
                 f"longest {longest:.0f}s; usage reported on {with_usage} of {answered} answer(s)")
    lines.append("verdict: " + ("OK, the second host answers production's question"
                                if results and good == len(results)
                                else "NOT OK, do not rely on this host yet"))
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--model-io", type=Path, default=None,
                        help="directory with a production run's model-io files (archived asks); else a built-in question")
    parser.add_argument("--count", type=int, default=1, help="how many distinct names to ask (archived asks only)")
    parser.add_argument("--workers", type=int, default=4, help="asks in flight at once (production asks 4)")
    args = parser.parse_args(argv)

    provider = heartbeat.fallback_model_provider()
    if provider is None:
        print("FULL_MODEL_FALLBACK_API_KEY is empty (or the full model is not on an OpenAI-compatible host): "
              "nothing to check. Add the secret, then run this again.")
        return EXIT_NO_KEY
    host = llm.configured_fallback_provider()
    chosen = questions(args.model_io, args.count)
    effort = heartbeat.full_model_effort() or "the host's default"
    print(f"asking {host} {len(chosen)} question(s), {min(len(chosen), max(1, args.workers))} at a time, "
          f"as {llm.FALLBACK_MODEL} at {effort} effort")
    shape = request_shape(provider, chosen[0])
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        results = list(pool.map(lambda q: ask(provider, q), chosen))
    print(report(host, shape, results))
    return EXIT_OK if results and all(r.ok for r in results) else EXIT_FAILED


if __name__ == "__main__":
    sys.exit(main())
