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
from dataclasses import dataclass
from typing import Any, Optional

import anthropic

from orchestrator.pricing import Usage, usage_from_response

log = logging.getLogger(__name__)

MODEL = "claude-opus-5"

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
SCREENING_ENABLED = True
SCREENING_MODEL = "claude-haiku-4-5"

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
        return dict(
            model=request.model or MODEL,
            max_tokens=MAX_TOKENS,
            system=cached_system(request.system_prompt),
            messages=[{"role": "user", "content": request.user_prompt}],
            thinking={"type": "adaptive"},
            output_config={
                "effort": request.effort or EFFORT,
                "format": {
                    "type": "json_schema",
                    "schema": build_output_schema(request.json_schema),
                },
            },
        )

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
                    text=text, usage=usage_from_response(message, model or MODEL)
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
            model=model or MODEL,
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
        return Completion(text=text, usage=usage_from_response(response, model or MODEL))
