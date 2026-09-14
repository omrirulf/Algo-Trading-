"""Turn a journalled context dict back into the object that rendered it.

The journal stores ``TickerContext.as_dict()``, but the prompt is built by
``as_prompt()`` from the snapshot *objects*. Rebuilding is therefore the one
place a replay can quietly stop being honest: if reconstruction is lossy, the
prompt the model is re-asked is not the prompt it was originally asked, and
every comparison built on top is measuring the wrong thing.

Two things make it lossy if you are not careful.

``asdict()`` recurses, so ``InsiderSnapshot.buys`` -- a list of
``InsiderTrade`` -- comes back as a list of plain dicts, and ``as_lines()``
raises on the first one. That is not a subtle degradation; it is why
``_NESTED`` exists.

And the schema moves. A line written before ``insiders`` existed has no such
key, and a line written after a field is removed carries one nothing reads.
Both are tolerated here for the same reason the journal reader tolerates them:
the whole value of the archive is that old lines stay readable.

``tests/test_replay_rebuild.py`` pins the guarantee that matters -- a rebuilt
context renders a byte-identical prompt.
"""

from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, Optional

from orchestrator import analysts, fundamentals, insiders, technicals
from orchestrator.context import TickerContext

#: Journal key -> the dataclass that produced it.
SNAPSHOT_TYPES: dict[str, type] = {
    "technicals": technicals.TechnicalSnapshot,
    "fundamentals": fundamentals.FundamentalSnapshot,
    "analysts": analysts.AnalystSnapshot,
    "insiders": insiders.InsiderSnapshot,
}

#: Fields that hold lists of dataclasses, which ``asdict`` flattened.
_NESTED: dict[type, dict[str, type]] = {
    insiders.InsiderSnapshot: {
        "buys": insiders.InsiderTrade,
        "sells": insiders.InsiderTrade,
    },
}


class RebuildError(ValueError):
    """A journal line could not be turned back into a context."""


def _build(cls: type, payload: dict) -> Any:
    """Instantiate ``cls`` from a dict, tolerating schema drift."""
    known = {f.name for f in fields(cls)}
    nested = _NESTED.get(cls, {})
    kwargs: dict[str, Any] = {}

    for name, value in payload.items():
        if name not in known:
            continue  # a field this version no longer has
        item_type = nested.get(name)
        if item_type is not None and isinstance(value, list):
            kwargs[name] = [
                _build(item_type, item) if isinstance(item, dict) else item for item in value
            ]
        else:
            kwargs[name] = value

    try:
        return cls(**kwargs)
    except TypeError as exc:
        # A required field the line does not carry. Reported rather than
        # guessed: substituting a default would render a prompt the model was
        # never shown, which is exactly the dishonesty this module exists to
        # avoid.
        missing = sorted(
            f.name
            for f in fields(cls)
            if f.name not in kwargs and f.default is f.default_factory is not None
        )
        raise RebuildError(
            f"cannot rebuild {cls.__name__} from this journal line "
            f"(missing {', '.join(missing) or 'a required field'}): {exc}"
        ) from exc


def context_from_dict(payload: dict) -> TickerContext:
    """Rebuild the context a journal line recorded.

    Renders the same prompt the model originally saw, or raises rather than
    rendering a different one.
    """
    if not isinstance(payload, dict):
        raise RebuildError(f"context must be an object, got {type(payload).__name__}")
    ticker = payload.get("ticker")
    if not isinstance(ticker, str) or not ticker.strip():
        raise RebuildError("context has no ticker")

    snapshots: dict[str, Any] = {}
    for key, cls in SNAPSHOT_TYPES.items():
        raw = payload.get(key)
        if raw is None:
            snapshots[key] = None          # the source was down that cycle
        elif isinstance(raw, dict):
            snapshots[key] = _build(cls, raw)
        else:
            raise RebuildError(f"{key} must be an object or null, got {type(raw).__name__}")

    return TickerContext(
        ticker=ticker.strip().upper(),
        headlines=list(payload.get("headlines") or []),
        gaps=list(payload.get("gaps") or []),
        **snapshots,
    )


def prompt_from_dict(payload: dict) -> str:
    """The user prompt a journal line's context renders to."""
    return context_from_dict(payload).as_prompt()


__all__ = ["RebuildError", "SNAPSHOT_TYPES", "context_from_dict", "prompt_from_dict"]
