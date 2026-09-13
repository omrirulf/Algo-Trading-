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
import logging
from typing import Any

import anthropic

log = logging.getLogger(__name__)

MODEL = "claude-opus-5"

#: Server-side refusal fallback. If a safety classifier declines the request,
#: the API re-runs it on another model inside the same call and marks the
#: switch with a ``fallback`` content block. ``"default"`` routes by refusal
#: category, so there is no model list here to go stale. The beta name and the
#: mode are a matched pair -- the array form of ``fallbacks`` needs the
#: ``2026-06-01`` beta instead, and crossing them is rejected.
FALLBACK_BETA = "server-side-fallback-2026-07-01"
FALLBACK_MODE = "default"

#: Thinking depth / token spend. This is a short judgement over a handful of
#: headlines, not a long-horizon task, so it does not need "high" or above.
EFFORT = "medium"

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

    def complete(self, system_prompt: str, user_prompt: str, json_schema: dict) -> str:
        try:
            response = self._create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
                thinking={"type": "adaptive"},
                output_config={
                    "effort": EFFORT,
                    "format": {
                        "type": "json_schema",
                        "schema": build_output_schema(json_schema),
                    },
                },
            )
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
        return text
