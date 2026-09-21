"""Re-ask the model, with whatever prompt you want to try.

The harness never trades. It reads the journal, rebuilds each context, calls
the model, and reports the difference. There is no path from here to the
execution engine, and CI checks that there isn't -- the same guarantee the
scorer carries, for the same reason: a tool you run repeatedly while iterating
must not be able to move money.

It also never writes the journal it is reading. Appending replayed signals to
the archive would corrupt the only record of what the model actually said at
the time.
"""

from __future__ import annotations

import json
import logging
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Any, Callable, Iterator, Optional

from app.schemas import Bias, LLMSignal
from orchestrator.context import TickerContext
from orchestrator.heartbeat import SIGNAL_JSON_SCHEMA, SYSTEM_PROMPT, system_prompt_for
from orchestrator.llm import LLMError
from replay.compare import ReplaySummary, SignalDiff
from replay.rebuild import RebuildError, context_from_dict

log = logging.getLogger(__name__)

#: Signature of the model call, so tests inject a fake instead of the SDK.
Completer = Callable[[str, str, dict], str]


@dataclass(frozen=True)
class ReplayEntry:
    """One journal line, ready to re-ask."""

    ticker: str
    ts_utc: Optional[str]
    prompt: str
    original: Optional[LLMSignal]
    #: The rebuilt context, kept alongside the rendered ``prompt`` string
    #: rather than instead of it -- most callers only ever need the string,
    #: but a caller comparing a *screening* candidate needs to know whether
    #: this ticker is a fund and, for a fund, which sections it actually
    #: carried, to pick the same system prompt production would have sent.
    #: ``None`` on any line old enough to predate this field.
    context: Optional[TickerContext] = None
    #: The cheap first stage's own recorded answer, exactly as journalled --
    #: ``{"model", "bias", "conviction", "usage"}`` on a normal line,
    #: ``{"model", "error"}`` on a screen that failed, ``None`` when
    #: screening was off or the line predates the funnel. This is what a
    #: screening-candidate comparison must diff against; ``original`` is the
    #: wrong baseline for it on any line that escalated, because on those
    #: lines ``original`` is the *full model's* answer, not the screen's.
    recorded_screen: Optional[dict] = None


@dataclass(frozen=True)
class ReplayResult:
    entry: ReplayEntry
    replayed: Optional[LLMSignal]
    error: Optional[str] = None

    @property
    def diff(self) -> SignalDiff:
        return SignalDiff(ticker=self.entry.ticker, before=self.entry.original, after=self.replayed)


def load_entries(lines: list[str], ticker: Optional[str] = None) -> Iterator[ReplayEntry]:
    """Parse journal lines into replayable entries, skipping unusable ones.

    A truncated final line is ordinary -- the journal is append-only and may
    be read mid-write -- so it is skipped rather than fatal, matching the
    scorer's reader.
    """
    wanted = ticker.strip().upper() if ticker else None
    for number, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            log.debug("journal line %d is not JSON; skipping", number)
            continue
        context = record.get("context")
        if not isinstance(context, dict):
            continue
        if wanted and str(context.get("ticker", "")).upper() != wanted:
            continue
        try:
            rebuilt = context_from_dict(context)
        except RebuildError as exc:
            log.warning("journal line %d cannot be rebuilt: %s", number, exc)
            continue

        raw_signal = record.get("signal")
        original: Optional[LLMSignal] = None
        if isinstance(raw_signal, dict):
            try:
                original = LLMSignal.model_validate(raw_signal)
            except Exception:  # noqa: BLE001 - an old line may predate a field
                log.debug("journal line %d has an unparseable signal", number)

        screen = record.get("screen")

        yield ReplayEntry(
            ticker=str(context.get("ticker", "")).upper(),
            ts_utc=record.get("ts_utc"),
            prompt=rebuilt.as_prompt(),
            original=original,
            context=rebuilt,
            recorded_screen=screen if isinstance(screen, dict) else None,
        )


def replay_one(entry: ReplayEntry, system_prompt: str, complete: Completer) -> ReplayResult:
    """Ask the model this entry's question again. Never raises."""
    user_prompt = f"{entry.prompt}\n\nRespond with the JSON signal for {entry.ticker}."
    try:
        raw = complete(system_prompt, user_prompt, SIGNAL_JSON_SCHEMA)
        signal = LLMSignal.model_validate(json.loads(raw))
    except LLMError as exc:
        return ReplayResult(entry=entry, replayed=None, error=str(exc))
    except (json.JSONDecodeError, ValueError) as exc:
        # A prompt edit that makes the model emit something off-schema is a
        # finding about the prompt, not a crash -- report it and keep going.
        return ReplayResult(entry=entry, replayed=None, error=f"invalid output: {exc}")
    except Exception as exc:  # noqa: BLE001
        return ReplayResult(entry=entry, replayed=None, error=f"unexpected {type(exc).__name__}: {exc}")

    if signal.ticker != entry.ticker:
        return ReplayResult(entry=entry, replayed=None, error=f"answered for {signal.ticker}")
    return ReplayResult(entry=entry, replayed=signal)


def replay_all(
    entries: list[ReplayEntry], system_prompt: str, complete: Completer
) -> list[ReplayResult]:
    return [replay_one(entry, system_prompt, complete) for entry in entries]


def replay_each(
    entries: list[ReplayEntry],
    prompt_for: Callable[[ReplayEntry], str],
    complete: Completer,
    max_workers: int = 1,
) -> list[ReplayResult]:
    """Replay every entry with its own system prompt, optionally in parallel.

    Differs from ``replay_all`` in taking a prompt *per entry*, which is what
    a faithful comparison needs: production sends a fund the macro prompt
    trimmed to the sections it carried, so grading every line against one
    shared string asks a question nobody was asked.

    ``max_workers`` above one is what makes a large sample affordable in wall
    time rather than in money. A reasoning model answers the full-model
    question in ~97s, so 469 recorded contexts is twelve hours in a row and
    about ninety minutes eight at a time -- and a sample small enough to
    finish sequentially is a sample too small to separate 97% from 90%.

    Left at one by default. Anthropic is the caller that would otherwise fire
    a whole journal at a rate limit, and a rate-limited context is a *lost*
    one, where a slow one is only slow. Callers that know their endpoint
    tolerates it opt in.

    Results come back in the order the entries were given, whatever order the
    calls finished in, so a run is reproducible and a diff cannot be silently
    attributed to the wrong ticker.
    """
    if max_workers > 1 and len(entries) > 1:
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            return list(pool.map(
                lambda e: replay_one(e, prompt_for(e), complete), entries
            ))
    return [replay_one(entry, prompt_for(entry), complete) for entry in entries]


def system_prompt_for_entry(entry: ReplayEntry) -> str:
    """The system prompt production would have sent for this exact line.

    Differs from the single shared ``SYSTEM_PROMPT`` every other tool in this
    module uses: a fund gets the macro prompt rather than the company one,
    trimmed to the sections ``entry.context`` actually carried -- the same
    rule ``orchestrator.heartbeat.system_prompt_for`` applies live. An entry
    old enough to predate ``ReplayEntry.context`` falls back to whichever
    prompt the ticker's *kind* alone implies, untrimmed -- still correct for
    a single name, and for a fund closer than the one shared prompt every
    other replay tool sends every ticker.
    """
    return system_prompt_for(entry.ticker, entry.context)


def recorded_screen_signal(entry: ReplayEntry) -> Optional[LLMSignal]:
    """The cheap first stage's own recorded call, as a comparable ``LLMSignal``.

    ``None`` when there is nothing to compare against: screening was off,
    the line predates the funnel, or the recorded screen itself failed (it
    carries ``error`` rather than a ``bias``) -- a failed screen is a data
    point about that day's screen, not a baseline call to hold a candidate
    to. ``entry.original`` is deliberately not used for this: on a line the
    screen escalated, ``original`` is the *full model's* answer, and diffing
    a screening candidate against the full model would grade it on a
    question production never asked it.

    The rationale is a fixed placeholder rather than anything recorded --
    the production screen's rationale was thrown away because the funnel
    only kept ``bias`` and ``conviction`` (see ``orchestrator/heartbeat.py``,
    ``apply_screen``) -- and every comparison here reads ``bias`` and
    ``conviction`` only, so the placeholder is never inspected.
    """
    screen = entry.recorded_screen
    if not screen or "bias" not in screen or screen.get("conviction") is None:
        return None
    try:
        return LLMSignal(
            ticker=entry.ticker,
            bias=Bias(screen["bias"]),
            conviction=float(screen["conviction"]),
            rationale="(recorded production screen; not itself recorded)",
        )
    except (ValueError, KeyError):
        return None


def screening_candidate_completer(provider, model: str, effort: Optional[str] = None):
    """A completer for a screening candidate, called as production calls it.

    ``reasoning=False`` is the default because it is what "screening" means in
    this codebase: the production screen is asked with reasoning off (see
    ``orchestrator/heartbeat.py``'s ``screen_signal``), and a candidate
    answering *with* reasoning on is being asked a question the cycle does not
    ask it.

    ``effort`` deliberately breaks that symmetry, and is the only reason to.
    A reasoning model asked at the cheap setting may be failing the screen
    because it is a weak model or because the setting crippled it, and those
    have opposite conclusions: the first says pick another model, the second
    says pay slightly more for the same one. Passing an effort asks the second
    question -- reasoning on, at that level -- which is a *proposal* for what
    production would then have to do, not a measurement of what it does today.
    A run that used one says so in its own header, because a recall number
    from a configuration the cycle does not use would otherwise read as a
    verdict on the configuration it does.

    ``provider`` is anything implementing ``orchestrator.llm.SignalProvider``
    -- in practice ``OpenAICompatibleProvider`` for a candidate, or
    ``AnthropicSignalProvider`` to price the incumbent Haiku screen the same
    way for a side-by-side.

    Returns ``(complete, usages)``, the same shape as ``measured_completer``,
    for the same reason: a validation run should price itself from measured
    tokens, and an unpriced local model is expected to report ``cost_usd`` of
    ``None`` rather than a guessed number.
    """
    from orchestrator.pricing import Usage

    usages: list[Usage] = []

    def complete(system_prompt: str, user_prompt: str, schema: dict[str, Any]) -> str:
        result = provider.complete_detailed(
            system_prompt, user_prompt, schema, model=model,
            reasoning=bool(effort), effort=effort,
        )
        usages.append(result.usage)
        return result.text

    return complete, usages


def summarise(results: list[ReplayResult]) -> ReplaySummary:
    return ReplaySummary(diffs=[r.diff for r in results if r.error is None])


def default_completer() -> Completer:
    """The real model call, built lazily so a dry run needs no credentials."""
    from config.settings import get_settings
    from orchestrator.llm import AnthropicSignalProvider

    provider = AnthropicSignalProvider(get_settings().anthropic_api_key)

    def complete(system_prompt: str, user_prompt: str, schema: dict[str, Any]) -> str:
        return provider.complete(system_prompt, user_prompt, schema)

    return complete


def measured_completer(
    model: Optional[str] = None,
    effort: Optional[str] = None,
    base_url: str = "",
    api_key: str = "",
    timeout: Optional[float] = None,
):
    """A completer that also reports what each call cost.

    Returns ``(complete, usages)`` -- the list fills as calls are made, so a
    config comparison prices itself from measured tokens rather than an
    assumed output length.

    ``base_url`` sends the question to an OpenAI-compatible endpoint instead
    of Claude. That exists to ask the *full model's* question of something
    that is not Claude, which is a much larger claim than moving the screen:
    the screen only decides who gets asked, and this decides what is traded.
    The harness takes no view on that -- it reports agreement and cost, and
    agreement with the incumbent is not correctness. What it does guarantee
    is that both sides answered the same recorded contexts.

    Reasoning is on either way, because that is how the full model is asked
    in the cycle. ``effort`` is passed through, so a reasoning model that has
    no true off switch is compared at the setting it would really run at.

    ``timeout`` exists because the default one silently decides *which*
    contexts get graded. A 250-context run of gpt-oss-120b at high effort put
    67 of its 68 failures down to timeouts, and a timeout is not a coin flip:
    the calls that run long are the ones the model found hard, so cutting
    them drops the hard contexts and grades the candidate on the easy
    remainder. Raising it costs wall time and buys a number that is about the
    candidate rather than about the deadline.
    """
    from config.settings import get_settings
    from orchestrator.llm import AnthropicSignalProvider, OpenAICompatibleProvider
    from orchestrator.pricing import Usage

    if base_url:
        if not model:
            raise ValueError("--base-url needs a model name to ask for")
        kwargs = {"base_url": base_url, "model": model, "api_key": api_key}
        if timeout is not None:
            kwargs["timeout"] = timeout
        provider = OpenAICompatibleProvider(**kwargs)
    else:
        provider = AnthropicSignalProvider(get_settings().anthropic_api_key)
    usages: list[Usage] = []

    def complete(system_prompt: str, user_prompt: str, schema: dict[str, Any]) -> str:
        result = provider.complete_detailed(
            system_prompt, user_prompt, schema, model=model, effort=effort
        )
        usages.append(result.usage)
        return result.text

    return complete, usages


__all__ = [
    "SYSTEM_PROMPT",
    "Completer",
    "ReplayEntry",
    "ReplayResult",
    "load_entries",
    "replay_one",
    "replay_each",
    "replay_all",
    "summarise",
    "default_completer",
    "measured_completer",
    "system_prompt_for_entry",
    "recorded_screen_signal",
    "screening_candidate_completer",
]
