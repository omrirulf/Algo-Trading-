"""Turn headlines into a signal using the Claude API's structured outputs.

The model is constrained at generation time by a JSON schema derived from
``LLMSignal``, so it cannot invent fields. The caller still re-validates the
result against ``LLMSignal`` itself, and the webhook validates it a third
time on receipt; this module is only the first of those three gates.

No broker credentials are visible here, and nothing in this module can place
an order -- the most it can do is return a JSON string.
"""

from __future__ import annotations

import json
import time
import logging
import re
import threading
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Optional, Protocol

import anthropic
import httpx

from orchestrator.pricing import Usage, usage_from_response

log = logging.getLogger(__name__)

MODEL = "openai/gpt-oss-120b"

#: Where to ask for MODEL. Blank -- the historical value -- means Anthropic,
#: with the Batch API and its half price. Anything else is an
#: OpenAI-compatible endpoint, asked one ticker at a time because there is no
#: batch to submit.
#:
#: This is a constant and not a setting on purpose, and it is the one place
#: that rule is load-bearing. ``screening_base_url`` is an environment
#: variable because moving the *screen* is a cost question whose worst case is
#: a trade not taken. Moving the *full* model changes what is traded, and the
#: repo's standing rule is that what gets traded shows up in a diff. An
#: environment variable could change it with no commit and no review.
#:
#: Only the bearer token comes from settings, because a secret cannot be
#: committed. A base URL set with no token, or a token with no base URL, is
#: refused rather than half-applied.
MODEL_BASE_URL = "https://api.deepinfra.com/v1/openai"

#: Reasoning depth for MODEL. Read only on the OpenAI-compatible path;
#: the Anthropic path has EFFORT below, which is a different vocabulary.
MODEL_EFFORT = "high"

#: What AnthropicSignalProvider asks for when the caller names nothing.
#:
#: Separate from MODEL since 23 September, when MODEL stopped being a Claude
#: name. That class used to default to MODEL, which was right while the two
#: were the same thing and became a request for "openai/gpt-oss-120b" from
#: api.anthropic.com the moment they were not -- a 404 per ticker on the
#: fallback path, reached only on the day the primary one is already broken.
ANTHROPIC_MODEL = "claude-opus-5"

#: The two-stage funnel. A cheap model reads the same prompt first; only a
#: ticker it does not call NEUTRAL goes on to MODEL. On a day when most of the
#: watchlist has nothing happening, most of the expensive calls never happen.
#:
#: The risk is a false negative -- the screen saying NEUTRAL where MODEL would
#: have taken a side. Every screen answer is journalled beside the final one,
#: which makes the filter rate and the disagreement on escalated tickers a
#: query over the journal; the false-negative rate itself needs a run with
#: this off, or a replay of journalled contexts through both models, because
#: a NEUTRAL screen is precisely the case where MODEL was not asked. A screen
#: that *fails* (an API error) falls through to MODEL; a broken screen must
#: never silence the system.
#:
#: Haiku 4.5 takes neither adaptive thinking nor ``effort`` -- it is asked
#: with reasoning off, which is also what makes it the cheap stage.
#:
#: OFF since 23 September 2026. The funnel existed to keep an expensive model
#: off the names that did not need it: measured over six cycles, the screen
#: ended about two thirds of the watchlist and the escalations cost $0.041 a
#: call against the screen's $0.007. MODEL now costs a fifth of a cent, so the
#: stage is saving roughly a tenth of a cent a ticker and costing every name
#: the chance of the better answer. What it is *not* is free insurance: a
#: NEUTRAL screen is exactly the case where MODEL was never asked, so what the
#: funnel filtered out was never measured.
#:
#: Turning it back on is this constant and nothing else; SCREENING_MODEL and
#: the screening settings are all still wired.
SCREENING_ENABLED = False
SCREENING_MODEL = "claude-haiku-4-5"

#: Every name the screening endpoint's bearer token might plausibly have been
#: stored under, in the order they are tried. ``SCREENING_API_KEY`` is the one
#: ``config/settings.py`` declares and the only one the running code reads;
#: the rest exist because the obvious thing to call a Gemini key is
#: GEMINI_API_KEY, and a key stored under a name nothing reads is silent --
#: the screen simply stays on Haiku and no error says why. The workflow maps
#: the alternatives onto the canonical name, and
#: ``tests/test_workflow_keys.py`` pins that mapping to this tuple.
SCREENING_KEY_ENV_VARS: tuple[str, ...] = (
    "SCREENING_API_KEY",
    "GEMINI_API_KEY",
    "GOOGLE_API_KEY",
    "GROQ_API_KEY",
)

#: Server-side refusal fallback. If a safety classifier declines the request,
#: the API re-runs it on another model inside the same call and marks the
#: switch with a ``fallback`` content block. ``"default"`` routes by refusal
#: category, so there is no model list here to go stale. The beta name and the
#: mode are a matched pair -- the array form of ``fallbacks`` needs the
#: ``2026-06-01`` beta instead, and crossing them is rejected.
FALLBACK_BETA = "server-side-fallback-2026-07-01"
FALLBACK_MODE = "default"

#: Thinking depth / token spend. Output is ~84% of the bill and thinking bills
#: at the output rate, so this is the biggest cost lever there is -- larger
#: than model tier. "low" for a short judgement over a handful of headlines;
#: replay/compare_configs.py is where a higher notch would have to earn its
#: place on the same inputs before it is turned back up.
EFFORT = "low"

#: Generous ceiling, not a target: the signal itself is a few hundred tokens.
#: Only what the model actually generates is billed.
MAX_TOKENS = 16000

REQUEST_TIMEOUT_SECONDS = 120.0


def configured_effort() -> Optional[str]:
    """The reasoning level the full model is asked at, as configured here.

    ``MODEL_EFFORT`` on the OpenAI-compatible path, ``EFFORT`` on the
    Anthropic one: the two vocabularies reach different fields, and which
    one applies is decided by ``MODEL_BASE_URL``. Recorded on every journal
    line, so a line can say how it was made without anyone having to know
    what the code said on that day.
    """
    effort = MODEL_EFFORT if MODEL_BASE_URL else EFFORT
    return (effort or "").strip().lower() or None

#: The same, for the full model on the OpenAI-compatible path. Separate
#: because 120 is not a timeout for a reasoning model at high effort, it is a
#: coin toss: gpt-oss-120b measured ~128s a call, and a 120s deadline lost 286
#: of 300 calls on 22 September -- every one of them billed.
FULL_MODEL_TIMEOUT_SECONDS = 300.0

#: JSON Schema keywords kept when deriving the generation-time schema. Value
#: constraints (pattern, minLength, minimum, ...) are deliberately dropped:
#: constrained decoding does not accept every keyword pydantic emits, and the
#: real enforcement of those bounds is ``LLMSignal`` on the way back.
#: ``description`` is kept because it is the only place the *meaning* of a
#: field travels with the schema -- what the score scale is, what a key factor
#: should contain -- and a field the model misunderstands is worse than one it
#: cannot emit.
_KEEP = (
    "type",
    "enum",
    "properties",
    "required",
    "additionalProperties",
    "items",
    "description",
)


def new_http_client(timeout: float) -> httpx.Client:
    """The one place this module opens a connection it was not handed.

    A seam, not an abstraction: every other caller passes its own client, so
    this is the only path a test cannot intercept by construction. The suite
    closes it (``tests/conftest.py``), because faking the provider stopped
    being enough the moment the full model moved to an OpenAI-compatible
    endpoint -- a test that faked ``AnthropicSignalProvider`` was faking
    nothing, and the call went out for real.
    """
    return httpx.Client(timeout=timeout)


@dataclass(frozen=True)
class Completion:
    """What the model said, and what saying it cost."""

    text: str
    usage: Usage


class LLMError(Exception):
    """The model was unreachable, declined, or returned nothing usable."""


def _inline_refs(node: Any, defs: dict[str, Any]) -> Any:
    if isinstance(node, dict):
        if "$ref" in node:
            name = node["$ref"].rsplit("/", 1)[-1]
            if name not in defs:
                raise LLMError(f"cannot resolve schema reference {node['$ref']}")
            return _inline_refs(defs[name], defs)
        return {k: _inline_refs(v, defs) for k, v in node.items()}
    if isinstance(node, list):
        return [_inline_refs(item, defs) for item in node]
    return node


def _denullify(node: Any) -> Any:
    """Collapse pydantic's ``Optional[T]`` -- ``anyOf: [T, null]`` -- down to ``T``.

    Without this, ``_prune`` drops the unrecognised ``anyOf`` and leaves ``{}``:
    an empty schema constrains nothing, so an optional field would silently
    become the one place the model could emit an arbitrary value. Optionality
    is a concession to callers posting the older payload shape by hand, not an
    invitation for the model to answer ``null``.
    """
    if isinstance(node, dict):
        options = node.get("anyOf")
        if isinstance(options, list):
            concrete = [
                option
                for option in options
                if not (isinstance(option, dict) and option.get("type") == "null")
            ]
            if len(concrete) == 1:
                merged = {k: v for k, v in node.items() if k != "anyOf"}
                merged.update(concrete[0])
                return _denullify(merged)
        return {k: _denullify(v) for k, v in node.items()}
    if isinstance(node, list):
        return [_denullify(item) for item in node]
    return node


def _prune(node: Any) -> Any:
    if isinstance(node, dict):
        out: dict[str, Any] = {}
        for key, value in node.items():
            if key not in _KEEP:
                continue
            # ``properties`` maps field names to subschemas: the names are data,
            # not keywords, so only the values are pruned.
            if key == "properties" and isinstance(value, dict):
                out[key] = {name: _prune(sub) for name, sub in value.items()}
            else:
                out[key] = _prune(value)
        return out
    if isinstance(node, list):
        return [_prune(item) for item in node]
    return node


def build_output_schema(model_schema: dict[str, Any]) -> dict[str, Any]:
    """Derive the generation-time schema from a pydantic model's JSON schema.

    Derived rather than hand-written so the fields the model may emit cannot
    drift away from the fields ``LLMSignal`` accepts.

    Every property is marked required, which is stricter than ``LLMSignal``
    itself: the webhook still accepts a payload without the transparency
    fields, but a model that has been handed every kind of context has no
    excuse for declining to report its read on any of them.
    """
    resolved = _inline_refs(
        {k: v for k, v in model_schema.items() if k != "$defs"},
        model_schema.get("$defs", {}),
    )
    pruned = _prune(_denullify(resolved))
    pruned["additionalProperties"] = False
    if pruned.get("properties"):
        pruned["required"] = list(pruned["properties"])
    return pruned


def _model_of(info: Any) -> str | None:
    return getattr(info, "model", None)


def _extract_text(response: Any) -> str:
    stop_reason = getattr(response, "stop_reason", None)
    if stop_reason == "refusal":
        # Every model in the chain declined, fallback included.
        details = getattr(response, "stop_details", None)
        category = getattr(details, "category", None) if details else None
        raise LLMError(f"model declined to answer (category: {category})")
    if stop_reason == "max_tokens":
        raise LLMError("response hit max_tokens; JSON would be truncated")

    blocks = list(getattr(response, "content", []) or [])
    switches = [i for i, b in enumerate(blocks) if getattr(b, "type", None) == "fallback"]
    for i in switches:
        log.warning(
            "%s declined; %s answered instead",
            _model_of(getattr(blocks[i], "from_", None)),
            _model_of(getattr(blocks[i], "to", None)),
        )

    # A model that declines mid-turn can leave partial text behind, so only
    # what the model that actually answered emitted is eligible.
    for block in blocks[(switches[-1] + 1) if switches else 0:]:
        if getattr(block, "type", None) == "text":
            text = (block.text or "").strip()
            if text:
                return text
    raise LLMError(f"no text block in response (stop_reason: {stop_reason})")


#: What the Batches API accepts as a ``custom_id``. Anything else is rejected
#: for the whole batch with a 400 -- after the prompts were built, the news
#: fetched and the OHLC pulled, which is the expensive end of a replay to
#: find out at. Checked here, at construction, instead.
CUSTOM_ID_PATTERN = re.compile(r"^[a-zA-Z0-9_-]{1,64}$")


def batch_custom_id(*parts: object) -> str:
    """Join ``parts`` into an id the Batches API accepts.

    Each part is stringified; any character outside ``[a-zA-Z0-9_-]`` becomes
    ``-`` and the parts are joined with ``_``, so ``("BRK.B", date(2025, 3,
    14))`` becomes ``BRK-B_2025-03-14``. Callers that need the parts back
    should keep them rather than parse the id.
    """
    joined = "_".join(str(p) for p in parts)
    safe = re.sub(r"[^a-zA-Z0-9_-]", "-", joined)
    if not safe:
        raise ValueError("a batch custom_id cannot be empty")
    return safe[:64]


@dataclass(frozen=True)
class BatchRequest:
    """One prompt for the Message Batches API, keyed for reassembly.

    Results come back in any order, so ``custom_id`` is the only link between
    a request and its answer -- never rely on position.
    """

    custom_id: str
    system_prompt: str
    user_prompt: str
    json_schema: dict
    model: Optional[str] = None
    effort: Optional[str] = None
    #: ``False`` omits adaptive thinking and effort, exactly as it does on the
    #: live path. The screening stage needs it: Haiku 4.5 takes neither, so a
    #: batch of screens built the other way is rejected for the whole batch.
    reasoning: bool = True

    def __post_init__(self) -> None:
        if not CUSTOM_ID_PATTERN.match(self.custom_id):
            raise ValueError(
                f"custom_id {self.custom_id!r} is not accepted by the Batches API "
                f"(must match {CUSTOM_ID_PATTERN.pattern}); build it with "
                f"batch_custom_id()"
            )


#: How long to wait on a batch before giving up and handing back the id.
#: Most small batches finish in minutes, but the API allows up to 24 hours,
#: and an Actions job cannot outlive its own timeout -- so this is a default
#: for callers that do not care, not a ceiling. Every batch CLI takes
#: ``--timeout-minutes``, and the workflow that runs it sets that from its own
#: ``timeout-minutes`` so the two clocks cannot disagree. They must not: the
#: job's clock kills the process, while this one raises ``BatchTimeout``, which
#: prints the id the batch can be resumed from. Giving up first is the whole
#: point -- a batch that outlives its job is still finished and still paid for,
#: and the id is the only way back to it.
BATCH_TIMEOUT_SECONDS = 55 * 60
BATCH_POLL_SECONDS = 30


class BatchTimeout(LLMError):
    """The batch did not finish in time. Carries the id so it can be resumed."""

    def __init__(self, batch_id: str, message: str) -> None:
        super().__init__(message)
        self.batch_id = batch_id


class SignalProvider(Protocol):
    """What the cycle needs from whatever answers a prompt.

    Narrow on purpose: one method, taking text and a schema and returning
    text plus what it cost. The batch methods below it are not in here,
    because they are the Message Batches API rather than a property of
    "something that can answer a prompt" -- a second provider is not obliged
    to have an offline mode, and the funnel does not require one of it.
    """

    def complete_detailed(
        self,
        system_prompt: str,
        user_prompt: str,
        json_schema: dict,
        model: Optional[str] = None,
        effort: Optional[str] = None,
        reasoning: bool = True,
    ) -> "Completion": ...


def cached_system(system_prompt: str) -> list[dict]:
    """The system prompt as one cacheable block, with the breakpoint on it.

    Placement is the whole point, and getting it wrong is silent. Passing
    ``cache_control`` as a top-level request parameter caches *the last
    cacheable block*, which in this request is the per-ticker user prompt --
    a different string every call. That is what the cycle did until now, and
    the journal recorded the result exactly: across 934 calls,
    1,869,345 tokens written to cache and **zero** ever read, with Opus
    reporting 406 uncached input tokens in total because the entire request
    was being billed as a cache write at 1.25x and then thrown away.

    Attached here instead, the breakpoint sits after the system prompt --
    byte-identical across every ticker in a cycle -- and the volatile user
    prompt falls outside it. The first call of a cycle writes; the rest read
    at 0.1x.

    Two things bound the saving, and neither is a reason to move it back: the
    cache is scoped per model, so the screen and the full model each pay one
    write; and a prompt under the model's minimum cacheable prefix does not
    cache at all. ``cache_read_input_tokens`` in the journal is how either
    shows up, which is why it is recorded rather than assumed.
    """
    return [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]


class AnthropicSignalProvider:
    def __init__(self, api_key: str, client: Any | None = None) -> None:
        # ``api_key or None`` turns a blank ANTHROPIC_API_KEY into "let the
        # SDK resolve it": ANTHROPIC_AUTH_TOKEN, an ``ant auth login``
        # profile, or Workload Identity Federation, in that order. None of
        # those require anything from this module -- the SDK reads them
        # itself. Construction never fails even with nothing configured;
        # see the TypeError handling in ``complete()`` for why the actual
        # check is deferred to there.
        self._client = client or anthropic.Anthropic(
            api_key=api_key or None, timeout=REQUEST_TIMEOUT_SECONDS
        )
        self._use_fallback = True

    def _create(self, **kwargs: Any) -> Any:
        if self._use_fallback:
            try:
                return self._client.beta.messages.create(
                    betas=[FALLBACK_BETA], fallbacks=FALLBACK_MODE, **kwargs
                )
            except anthropic.BadRequestError as exc:
                # The beta may not be enabled for this account. Going without
                # the rescue costs one skipped ticker on a refusal; letting a
                # rejected parameter stand would cost every cycle.
                log.warning("refusal fallback rejected, continuing without it: %s", exc)
                self._use_fallback = False
        return self._client.beta.messages.create(**kwargs)

    def _batch_params(self, request: BatchRequest) -> dict:
        """The same request shape as the live path, minus what Batches rejects.

        Server-side ``fallbacks`` (and their beta header) are refused by the
        Batches API, so an offline call runs without them. Everything else --
        cache_control on the shared system prompt, adaptive thinking, effort,
        the JSON-schema output format -- is identical, so a batch answer is
        priced and shaped like a live one and can stand in for it.
        """
        output_config: dict[str, Any] = {
            "format": {
                "type": "json_schema",
                "schema": build_output_schema(request.json_schema),
            },
        }
        params = dict(
            model=request.model or ANTHROPIC_MODEL,
            max_tokens=MAX_TOKENS,
            system=cached_system(request.system_prompt),
            messages=[{"role": "user", "content": request.user_prompt}],
            output_config=output_config,
        )
        if request.reasoning:
            params["thinking"] = {"type": "adaptive"}
            output_config["effort"] = request.effort or EFFORT
        return params

    def submit_batch(self, prompts: list[BatchRequest]) -> str:
        """Create a batch and return its id without waiting."""
        if not prompts:
            raise LLMError("cannot submit an empty batch")
        ids = [r.custom_id for r in prompts]
        if len(set(ids)) != len(ids):
            raise LLMError("batch custom_ids must be unique")
        try:
            batch = self._client.messages.batches.create(
                requests=[
                    {"custom_id": r.custom_id, "params": self._batch_params(r)}
                    for r in prompts
                ]
            )
        except TypeError as exc:
            raise LLMError(
                f"No Claude credentials found: set ANTHROPIC_API_KEY, or run "
                f"`ant auth login` ({exc})"
            ) from exc
        except anthropic.APIError as exc:
            raise LLMError(f"batch submission failed: {exc}") from exc
        return batch.id

    def collect_batch(
        self,
        batch_id: str,
        model: Optional[str] = None,
        poll_seconds: float = BATCH_POLL_SECONDS,
        timeout_seconds: float = BATCH_TIMEOUT_SECONDS,
        sleep=time.sleep,
    ) -> dict[str, "Completion | LLMError"]:
        """Wait for a batch and key its results by custom_id.

        A request that errored maps to an ``LLMError`` rather than being
        dropped, so the caller can count and name the failures instead of
        discovering a shorter list than it submitted.
        """
        deadline = time.monotonic() + timeout_seconds
        while True:
            try:
                batch = self._client.messages.batches.retrieve(batch_id)
            except anthropic.APIError as exc:
                raise LLMError(f"could not read batch {batch_id}: {exc}") from exc
            if batch.processing_status == "ended":
                break
            if time.monotonic() >= deadline:
                raise BatchTimeout(
                    batch_id,
                    f"batch {batch_id} still {batch.processing_status} after "
                    f"{timeout_seconds:.0f}s; resume with --resume {batch_id}",
                )
            sleep(poll_seconds)

        out: dict[str, Completion | LLMError] = {}
        for item in self._client.messages.batches.results(batch_id):
            kind = item.result.type
            if kind == "succeeded":
                message = item.result.message
                text = _extract_text(message)
                try:
                    json.loads(text)
                except json.JSONDecodeError as exc:
                    out[item.custom_id] = LLMError(f"model returned non-JSON output: {exc}")
                    continue
                out[item.custom_id] = Completion(
                    text=text, usage=usage_from_response(message, model or ANTHROPIC_MODEL)
                )
            elif kind == "errored":
                out[item.custom_id] = LLMError(f"batch item errored: {item.result.error}")
            else:
                out[item.custom_id] = LLMError(f"batch item {kind}")
        return out

    def complete_batch(
        self, prompts: list[BatchRequest], model: Optional[str] = None, **kw
    ) -> dict[str, "Completion | LLMError"]:
        """Submit, wait, collect. Half price, and no latency to care about."""
        return self.collect_batch(self.submit_batch(prompts), model=model, **kw)

    def complete(self, system_prompt: str, user_prompt: str, json_schema: dict) -> str:
        """The model's JSON, for callers that do not care what it cost."""
        return self.complete_detailed(system_prompt, user_prompt, json_schema).text

    def complete_detailed(
        self,
        system_prompt: str,
        user_prompt: str,
        json_schema: dict,
        model: Optional[str] = None,
        effort: Optional[str] = None,
        reasoning: bool = True,
    ) -> Completion:
        """The model's JSON plus what the call actually cost.

        ``model`` and ``effort`` exist so the replay harness can price one
        configuration against another on identical recorded context. The
        production path passes neither and gets the module constants, so
        changing what trades the account is still a visible diff.

        ``reasoning=False`` omits adaptive thinking and the effort setting.
        That is the request shape Haiku 4.5 accepts, and it is what makes the
        screening stage cheap: the same prompt, answered without deliberation.
        """
        output_config: dict[str, Any] = {
            "format": {"type": "json_schema", "schema": build_output_schema(json_schema)},
        }
        kwargs: dict[str, Any] = dict(
            model=model or ANTHROPIC_MODEL,
            max_tokens=MAX_TOKENS,
            system=cached_system(system_prompt),
            messages=[{"role": "user", "content": user_prompt}],
            output_config=output_config,
        )
        if reasoning:
            kwargs["thinking"] = {"type": "adaptive"}
            output_config["effort"] = effort or EFFORT
        try:
            response = self._create(**kwargs)
        except TypeError as exc:
            # Not an APIError: the SDK raises a bare TypeError, before
            # opening any connection, when it cannot resolve a credential
            # from any source at all. Still a same-cycle, no-network
            # failure -- just not the exception type request failures use.
            raise LLMError(
                f"No Claude credentials found: set ANTHROPIC_API_KEY, or run "
                f"`ant auth login` ({exc})"
            ) from exc
        except anthropic.APIError as exc:
            raise LLMError(f"Claude API call failed: {exc}") from exc

        text = _extract_text(response)
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            raise LLMError(f"model returned non-JSON output: {exc}") from exc
        return Completion(text=text, usage=usage_from_response(response, model or ANTHROPIC_MODEL))


#: What ``reasoning=False`` becomes on a chat-completions endpoint, since that
#: shape has no ``thinking: {type: "disabled"}`` of its own. Provider-agnostic
#: by construction: it is plain text appended to the system prompt, not a
#: field a specific API has to recognise, so it does something on every model
#: that reads a system prompt -- which is every one of them -- rather than
#: only the ones that happen to support a vendor-specific switch.
#: Statuses worth asking again about. 429 is the one that matters here: a
#: token-per-minute ceiling is a wait, not a refusal. The 5xx family is the
#: ordinary transient. Everything else -- 400, 401, 404 -- means the request
#: itself is wrong, and asking again only spends the deadline.
RETRY_STATUSES: frozenset[int] = frozenset({429, 500, 502, 503, 504})

#: The backoff ladder, doubling from base to cap. Deliberately no jitter:
#: the calls that collide were started at different moments by different
#: workers, so their retries are already spread, and a deterministic ladder
#: is one a test can assert on.
RETRY_BASE_SECONDS = 2.0
RETRY_CAP_SECONDS = 60.0

#: A ``Retry-After`` longer than this is not a wait, it is an outage, and the
#: cycle has a session to catch. The ladder takes over.
RETRY_AFTER_CAP_SECONDS = 120.0

#: Asks per call. Four gets through a minute-long token bucket on the ladder
#: above (2 + 4 + 8) without letting one ticker eat the cycle.
HTTP_ATTEMPTS = 4

#: Asks per call when the socket, rather than the server, is what failed.
#: Two: the ask, and one more on a fresh connection. A transport failure has
#: already spent its whole ceiling and been billed for it, so it is the one
#: retry worth counting separately from the statuses above.
TRANSPORT_ATTEMPTS = 2

#: The ceiling on that second ask: the same as the first (bug fix, 26 Sep
#: 2026, logged in the pre-registration's Amendments table).
#:
#: It was 120s, on the reasoning that a call which hung for the full 300s once
#: is unlikely to be quick. The production log said otherwise. Only 29-45% of
#: the full model's *successful* answers on 23 and 25 Sep arrived within 120s
#: (median 130-146s at high effort), so a retry cut to 120s could almost never
#: succeed: on 25 Sep it failed 7 times out of 7, and every one of those
#: tickers was lost. A fresh ask on a fresh connection is a new call and gets
#: a new call's ceiling. It changes no model, provider, prompt, answer length
#: or reasoning effort -- only how long we wait.
#:
#: ``min`` with the caller's own timeout below still applies, so the screening
#: path (asked at REQUEST_TIMEOUT_SECONDS) keeps its shorter ceiling.
TRANSPORT_RETRY_TIMEOUT_SECONDS = FULL_MODEL_TIMEOUT_SECONDS

#: Asks per call when the answer parsed as the wrong shape. Two: the first is
#: the question, the second is the question with the complaint stated.
SCHEMA_ATTEMPTS = 2

#: Which ticker the current thread is asking about, for the call log below.
#: Set by the cycle around each live call (``call_label``); thread-local
#: because the full model is asked four tickers at a time.
_CALL = threading.local()


@contextmanager
def call_label(label: str):
    """Name the model calls made inside this block in the call log."""
    previous = getattr(_CALL, "label", None)
    _CALL.label = label
    try:
        yield
    finally:
        _CALL.label = previous


def _log_call(ask: int, kind: str, started: datetime, seconds: float, outcome: str,
              output_tokens: Optional[int]) -> None:
    """One line per HTTP ask to an OpenAI-compatible model.

    Added 26 Sep 2026 because the timeouts of 23 and 25 Sep could only be
    diagnosed by rebuilding each call's start and end from a queue model of
    the four workers: the log had no ticker, no duration and no attempt
    number. With this line the next cycle says directly how many first asks
    timed out, how many second asks rescued a ticker, and whether a name is
    slow because it answers at length or because the provider stalled.
    """
    log.info(
        "model call: %s ask %d (%s) started %s, %.1fs, %s, output tokens %s",
        getattr(_CALL, "label", None) or "-", ask, kind,
        started.strftime("%H:%M:%SZ"), seconds, outcome,
        "n/a" if output_tokens is None else output_tokens,
    )

OFF_SCHEMA_INSTRUCTION = (
    "\n\nYour previous answer could not be parsed. Reply with the JSON object "
    "required by the schema and nothing else: no prose before it, no code "
    "fence around it, no commentary after it."
)

NO_REASONING_INSTRUCTION = (
    "\n\nAnswer directly and immediately: do not show your reasoning, chain "
    "of thought, or an internal monologue before the final JSON object."
)


class OpenAICompatibleProvider:
    """A second provider, for anything serving the OpenAI chat-completions shape.

    That covers Ollama, llama.cpp's server, vLLM and LM Studio, which is what
    makes this the seam for running the screening stage on a model that is not
    billed per token. It implements ``SignalProvider`` and nothing else; it has
    no batch mode and is never the provider for the full model.

    Where it must not be run, and why this is a seam rather than a default:
    the cycle's host is ``ubuntu-latest``, four CPUs with no GPU and a disk
    that is discarded after every run, so weights would be re-downloaded each
    cycle and eighty CPU inferences would not fit in the job's remaining time
    -- it already spends 42 minutes of its 90-minute ceiling on I/O alone.
    A model reached through this class has to be somewhere else: a self-hosted
    runner, or a machine on the network serving the endpoint.

    Two Anthropic-shaped request parts are dropped rather than translated,
    because they have no counterpart here: adaptive thinking's own on/off
    switch, and the cache breakpoint. ``effort`` has no counterpart either and
    stays unused -- nothing in this codebase calls this class with
    ``reasoning=True``, so there is nothing to tune the depth of.

    ``reasoning=False`` is different: production's whole reason for asking
    with reasoning off is that the screen is meant to be a fast, cheap read,
    not a deliberation, and a candidate that reasons anyway is answering a
    different question than Haiku was asked -- silently, since a chat
    endpoint's response carries no flag saying it thought first. So this is
    honoured two ways, because no single mechanism is honoured everywhere:
    a plain-English instruction appended to the system prompt, which every
    model that reads a system prompt at all will read, and a best-effort
    ``reasoning_effort: "low"`` field, which several providers (Groq's
    ``gpt-oss`` family, OpenAI's own o-series among them) read directly. A
    server that does not recognise that field is expected to ignore an
    unrecognised top-level key rather than reject the request -- the same
    tolerance that lets ``response_format`` be sent at all without knowing in
    advance whether the far end honours it.

    A server that ignores ``response_format`` and answers in prose raises
    ``LLMError`` like any other bad answer, which the funnel already treats as
    "the screen failed, ask the full model". So the worst a flaky local model
    can do is cost a cycle its saving -- never place a trade on a bad parse.
    """

    def __init__(
        self,
        base_url: str,
        model: str,
        api_key: str = "",
        client: httpx.Client | None = None,
        timeout: float = REQUEST_TIMEOUT_SECONDS,
        attempts: int = HTTP_ATTEMPTS,
        schema_attempts: int = SCHEMA_ATTEMPTS,
        sleep: Any = time.sleep,
    ) -> None:
        if not base_url:
            raise LLMError("an OpenAI-compatible provider needs a base URL")
        self._url = base_url.rstrip("/") + "/chat/completions"
        self._model = model
        self._api_key = api_key
        self._client = client
        self._timeout = timeout
        self._attempts = max(1, attempts)
        self._schema_attempts = max(1, schema_attempts)
        self._sleep = sleep

    def _retry_after(self, response: Any) -> float | None:
        """The server's own instruction, when it gives one.

        Guessing a backoff against a token-per-minute limit is guessing how
        much of the minute is left. ``Retry-After`` is the one number that
        knows, so it wins over the ladder whenever it is present and sane.
        """
        raw = (response.headers or {}).get("Retry-After")
        if not raw:
            return None
        try:
            seconds = float(str(raw).strip())
        except ValueError:
            return None            # the HTTP-date form; fall back to the ladder
        if seconds < 0 or seconds > RETRY_AFTER_CAP_SECONDS:
            return None
        return seconds

    def _post(self, body: dict) -> dict:
        """One answer, retrying the statuses that mean 'ask me again'.

        As the *screening* stage a refused call was survivable: the funnel
        treats a failed screen as "ask the full model", so the worst case was
        the cycle's cost. As the *full* model there is nothing behind it, and
        a throttled ticker is a signal the day never gets. Measured against
        DeepInfra on 23 September: 50 of 300 calls returned 429 at four in
        flight and 39 at eight, which is a token-per-minute ceiling rather
        than a parallelism one -- so waiting is the fix and spreading out is
        not.
        """
        # A local endpoint usually wants no key at all, so the header is sent
        # only when there is something to send: a bare "Bearer " is rejected
        # by some servers that would otherwise have let the request through.
        headers = {"Authorization": f"Bearer {self._api_key}"} if self._api_key else {}
        delay = RETRY_BASE_SECONDS
        last = ""
        transport_asks = 1
        # How many times the server was actually asked. The error below used
        # to print ``self._attempts`` (4) whatever happened, so a ticker lost
        # after two asks -- a timeout and its one retry -- read "gave up after
        # 4 attempt(s)". The count now says what was done.
        asks = 0
        kind = "first"
        # Local, never self._timeout: a provider is reused across tickers,
        # and one slow call must not quietly shorten every call after it.
        timeout = self._timeout
        for attempt in range(self._attempts):
            if attempt:
                self._sleep(delay)
                delay = min(delay * 2, RETRY_CAP_SECONDS)
            asks += 1
            started = datetime.now(timezone.utc)
            clock = time.monotonic()
            try:
                if self._client is None:
                    with new_http_client(timeout) as client:
                        response = client.post(self._url, json=body, headers=headers)
                else:
                    response = self._client.post(self._url, json=body, headers=headers)
            except httpx.HTTPError as exc:
                _log_call(asks, kind, started, time.monotonic() - clock,
                          f"{type(exc).__name__} after a {timeout:.0f}s limit", None)
                # Retried once, and only once, since 23 Sep 2026. It was not
                # retried at all before that, on an argument that the first
                # production cycle disproved: the worst case was taken to be
                # every call running to the 300s ceiling, twenty rounds of
                # it, which left no room to ask twice. The measured stage took
                # 32 minutes, not 100 -- and the two failures that argument
                # was protecting against, the 429 and the off-schema answer,
                # did not occur once between them, while three tickers were
                # lost to exactly this. The budget is now bounded by the stage
                # deadline below rather than by refusing to ask again, which
                # is the honest place to bound it.
                #
                # A retry is still the most expensive thing here -- the call
                # was billed for whatever it generated before the socket gave
                # up -- so it gets one, on a shorter ceiling, and a transport
                # failure is never retried more than that however many
                # attempts remain.
                last = f"{self._url} unreachable: {exc}"
                if transport_asks >= TRANSPORT_ATTEMPTS:
                    break
                transport_asks += 1
                # A fresh connection, with a new call's ceiling (see
                # TRANSPORT_RETRY_TIMEOUT_SECONDS for why it is no longer cut).
                timeout = min(timeout, TRANSPORT_RETRY_TIMEOUT_SECONDS)
                kind = "retry after a timeout"
                continue
            seconds = time.monotonic() - clock
            if response.status_code == 200:
                try:
                    payload = response.json()
                except ValueError as exc:
                    _log_call(asks, kind, started, seconds, "HTTP 200, body not JSON", None)
                    raise LLMError(f"{self._url} returned a non-JSON body: {exc}") from exc
                usage = payload.get("usage") if isinstance(payload, dict) else None
                tokens = usage.get("completion_tokens") if isinstance(usage, dict) else None
                _log_call(asks, kind, started, seconds, "HTTP 200",
                          tokens if isinstance(tokens, int) else None)
                return payload
            _log_call(asks, kind, started, seconds, f"HTTP {response.status_code}", None)
            last = f"{self._url} returned HTTP {response.status_code}: {response.text[:300]}"
            if response.status_code not in RETRY_STATUSES:
                break              # 400, 401, 404: asking again changes nothing
            kind = f"retry after HTTP {response.status_code}"
            told = self._retry_after(response)
            if told is not None:
                delay = told
        raise LLMError(f"{last} (gave up after {asks} attempt(s))")

    def _body(
        self,
        system_prompt: str,
        user_prompt: str,
        json_schema: dict,
        name: str,
        effort: Optional[str],
        reasoning: bool,
    ) -> dict:
        if not reasoning:
            system_prompt = system_prompt + NO_REASONING_INSTRUCTION
        body: dict[str, Any] = {
            "model": name,
            "max_tokens": MAX_TOKENS,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "response_format": {
                "type": "json_schema",
                "json_schema": {
                    "name": "signal",
                    "strict": True,
                    "schema": build_output_schema(json_schema),
                },
            },
        }
        # Reasoning off: "low", because this family has no true off switch, so
        # the floor is the least it will do. That is how the screen asks.
        #
        # Reasoning on: only what the caller named. ``effort`` used to be
        # accepted here and dropped on the floor, which made the one question
        # worth asking about a reasoning model -- does it get the screen right
        # when it is allowed to think -- unaskable through the replay harness.
        # gpt-oss-20b scored 11% escalation recall asked the cheap way, and
        # whether that is the model or the handicap is a measurement rather
        # than an opinion. An unspecified effort still sends nothing, leaving
        # the endpoint's own default alone: imposing one here would silently
        # change what every non-screen caller of this class asks for.
        if not reasoning:
            body["reasoning_effort"] = "low"
        elif effort:
            body["reasoning_effort"] = effort
        return body

    @staticmethod
    def _insist(body: dict) -> dict:
        """The same question, with the schema complaint said out loud."""
        retold = json.loads(json.dumps(body))
        retold["messages"][0]["content"] += OFF_SCHEMA_INSTRUCTION
        return retold

    def _answer(self, payload: dict, name: str) -> "Completion":
        try:
            text = payload["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise LLMError(f"no answer in the response from {self._url}: {exc}") from exc
        if not isinstance(text, str) or not text.strip():
            raise LLMError(f"{self._url} answered with an empty message")
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            raise LLMError(f"model returned non-JSON output: {exc}") from exc

        # Counted the same way as a Claude call so one journal line means the
        # same thing whoever answered. ``cost_usd`` is None for a model the
        # price table does not carry -- the honest answer, because this module
        # cannot know what someone else's hardware costs to run, and None
        # reads as "unpriced" rather than as "free".
        usage = payload.get("usage") or {}
        return Completion(
            text=text,
            usage=Usage(
                model=name,
                input_tokens=int(usage.get("prompt_tokens") or 0),
                output_tokens=int(usage.get("completion_tokens") or 0),
            ),
        )

    def complete_detailed(
        self,
        system_prompt: str,
        user_prompt: str,
        json_schema: dict,
        model: Optional[str] = None,
        effort: Optional[str] = None,
        reasoning: bool = True,
    ) -> "Completion":
        """One signal, re-asking once if the answer came back off-schema.

        A server that ignores ``response_format`` and answers in prose used to
        raise straight out of here, which the funnel read as "the screen
        failed, ask the full model" -- safe, because something better was
        behind it. As the full model there is nothing behind it, and this is
        not a rare shape: gpt-oss-120b answered off-schema on 12 of 300 calls
        on 23 September and on 6 of 150 the day before, a steady 4% rather
        than a fluke. Four percent of an eighty-name watchlist is three
        tickers a day with no signal at all.

        So a bad parse is re-asked with the complaint stated, and only a
        second bad parse raises. The re-ask is a second billed call, which is
        the point: it is cheaper than the trade it would otherwise skip.
        """
        name = model or self._model
        body = self._body(system_prompt, user_prompt, json_schema, name, effort, reasoning)
        for attempt in range(self._schema_attempts):
            payload = self._post(body)
            try:
                return self._answer(payload, name)
            except LLMError:
                if attempt == self._schema_attempts - 1:
                    raise
                log.warning(
                    "%s answered off-schema; asking once more with the complaint stated",
                    name,
                )
                body = self._insist(body)
        raise LLMError("unreachable")   # pragma: no cover - the loop always returns or raises
