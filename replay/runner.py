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
from dataclasses import dataclass
from typing import Any, Callable, Iterator, Optional

from app.schemas import LLMSignal
from orchestrator.heartbeat import SIGNAL_JSON_SCHEMA, SYSTEM_PROMPT
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
            prompt = context_from_dict(context).as_prompt()
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

        yield ReplayEntry(
            ticker=str(context.get("ticker", "")).upper(),
            ts_utc=record.get("ts_utc"),
            prompt=prompt,
            original=original,
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


__all__ = [
    "SYSTEM_PROMPT",
    "Completer",
    "ReplayEntry",
    "ReplayResult",
    "load_entries",
    "replay_one",
    "replay_all",
    "summarise",
    "default_completer",
]
