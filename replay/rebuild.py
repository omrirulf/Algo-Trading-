"""Turn a journalled context dict back into the object that rendered it.

The journal stores ``TickerContext.as_dict()``, but the prompt is built by
``as_prompt()`` from the snapshot *objects*. Rebuilding is therefore the one
place a replay can quietly stop being honest: if reconstruction is lossy, the
prompt the model is re-asked is not the prompt it was originally asked, and
every comparison built on top is measuring the wrong thing.

Three things make it lossy if you are not careful.

``asdict()`` recurses, so ``InsiderSnapshot.buys`` -- a list of
``InsiderTrade`` -- comes back as a list of plain dicts, and ``as_lines()``
raises on the first one. That is not a subtle degradation; it is why the
rebuild reads each field's annotation instead of assigning the value straight
across. JSON flattens further still: a tuple field such as
``outlook.Forecast.next_year`` comes back as a list.

The section list itself used to be hand-written here, and that is how this
module spent four months silently truncating three quarters of the watchlist.
``macro``, ``funds``, ``holdings``, ``positioning``, ``carry``, ``flows``,
``energy``, ``outlook``, ``crops`` and ``earnings`` all reached the journal and
none of them reached the rebuild, so every replayed fund prompt was TICKER,
NEWS and TECHNICALS -- about 290 tokens against the 800-odd the model actually
saw -- while the tests, which only ever built a company, stayed green. The
list is now derived from ``TickerContext``'s own annotations, so a section
added to ``context.py`` is carried here by construction rather than by
somebody remembering. The cost is a little reflection at import and a hard
dependency on the dataclass staying annotated; both are cheap against a
validation instrument that lies.

And the schema moves. A line written before ``insiders`` existed has no such
key, and a line written after a field is removed carries one nothing reads.
Both are tolerated here for the same reason the journal reader tolerates them:
the whole value of the archive is that old lines stay readable.

``tests/test_replay_rebuild.py`` pins the guarantee that matters -- a rebuilt
context renders a byte-identical prompt, for a fund as well as for a company.
"""

from __future__ import annotations

from dataclasses import fields, is_dataclass
from typing import Any, Final, Union, get_args, get_origin, get_type_hints

from orchestrator.context import TickerContext

#: Journal keys that are plain data rather than a snapshot object, handled by
#: ``context_from_dict`` itself. Listed so the test that guards against a new
#: section being dropped can tell "not a snapshot" from "not yet handled".
PASSTHROUGH_KEYS: Final[frozenset[str]] = frozenset(
    {"ticker", "headlines", "sources", "gaps"}
)


def _unwrap_optional(hint: Any) -> Any:
    """``Optional[X]`` -> ``X``; anything else unchanged.

    Only the two-arm ``X | None`` form is unwrapped. A genuine multi-type
    union has no single class to rebuild into, so it is left alone and its
    value passes through as the JSON gave it.
    """
    if get_origin(hint) is not Union:
        return hint
    args = [arg for arg in get_args(hint) if arg is not type(None)]
    return args[0] if len(args) == 1 else hint


def _snapshot_types() -> dict[str, type]:
    """Every ``TickerContext`` field that holds a snapshot dataclass.

    Derived rather than declared: a field typed ``Optional[SomeSnapshot]`` is
    exactly what ``as_dict`` writes as a nested object and what ``as_prompt``
    calls ``as_lines()`` on, so the annotation is a better source of truth
    than a second list kept in step by hand.
    """
    hints = get_type_hints(TickerContext)
    out: dict[str, type] = {}
    for spec in fields(TickerContext):
        inner = _unwrap_optional(hints.get(spec.name))
        if isinstance(inner, type) and is_dataclass(inner):
            out[spec.name] = inner
    return out


#: Journal key -> the dataclass that produced it.
SNAPSHOT_TYPES: Final[dict[str, type]] = _snapshot_types()

#: Resolved annotations per dataclass. ``get_type_hints`` re-parses the
#: module's string annotations on every call, and a fund context is a few
#: hundred nested records; the memo keeps rebuilding a full journal cheap.
_HINTS: Final[dict[type, dict[str, Any]]] = {}


def _hints_for(cls: type) -> dict[str, Any]:
    cached = _HINTS.get(cls)
    if cached is None:
        try:
            cached = get_type_hints(cls)
        except Exception:  # noqa: BLE001 - an unresolvable name is not fatal
            # Without hints every field passes through verbatim, which is what
            # this module did before. Degraded, not broken.
            cached = {}
        _HINTS[cls] = cached
    return cached


class RebuildError(ValueError):
    """A journal line could not be turned back into a context."""


def _coerce(hint: Any, value: Any) -> Any:
    """Rebuild one field's value into the shape its annotation asks for.

    Anything the annotation does not describe -- a dict of floats, a list of
    strings, a value of the wrong JSON type entirely -- is returned untouched.
    A malformed corner of an old line degrades to a raw value the renderer may
    or may not like; it does not take the whole line down with it.
    """
    if value is None:
        return None
    hint = _unwrap_optional(hint)
    if hint is None:
        return value

    if isinstance(hint, type) and is_dataclass(hint):
        return _build(hint, value) if isinstance(value, dict) else value

    origin = get_origin(hint)
    args = get_args(hint)
    if origin is list and isinstance(value, list):
        item = args[0] if args else None
        return [_coerce(item, item_value) for item_value in value]
    if origin is tuple and isinstance(value, (list, tuple)):
        # JSON has no tuples, so every one of them arrives as a list.
        if len(args) == 2 and args[1] is Ellipsis:
            return tuple(_coerce(args[0], item_value) for item_value in value)
        if args and len(args) == len(value):
            return tuple(_coerce(arg, item_value) for arg, item_value in zip(args, value))
        return tuple(value)
    return value


def _build(cls: type, payload: dict) -> Any:
    """Instantiate ``cls`` from a dict, tolerating schema drift."""
    hints = _hints_for(cls)
    known = {spec.name for spec in fields(cls)}
    kwargs: dict[str, Any] = {}

    for name, value in payload.items():
        if name not in known:
            continue  # a field this version no longer has
        kwargs[name] = _coerce(hints.get(name), value)

    try:
        return cls(**kwargs)
    except TypeError as exc:
        # A required field the line does not carry. Reported rather than
        # guessed: substituting a default would render a prompt the model was
        # never shown, which is exactly the dishonesty this module exists to
        # avoid.
        missing = sorted(
            spec.name
            for spec in fields(cls)
            if spec.name not in kwargs and spec.default is spec.default_factory is not None
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
        # Not part of the prompt, but it is what a reviewer opens to check a
        # replayed signal against the article it was drawn from.
        sources=list(payload.get("sources") or []),
        gaps=list(payload.get("gaps") or []),
        **snapshots,
    )


def prompt_from_dict(payload: dict) -> str:
    """The user prompt a journal line's context renders to."""
    return context_from_dict(payload).as_prompt()


__all__ = [
    "PASSTHROUGH_KEYS",
    "RebuildError",
    "SNAPSHOT_TYPES",
    "context_from_dict",
    "prompt_from_dict",
]
