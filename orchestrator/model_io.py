"""Every model call a cycle makes, in full, written down as it happens.

The journal says what the model answered and what it was shown, as
structured fields. It does not keep the thing itself: the exact request body
that went to the provider (every message, every parameter) and the exact
body that came back, reasoning text included. Neither can be fetched again
later -- a provider does not keep them, and a re-ask is a different answer --
so a question like "what did the model reason before it said BEARISH" or
"was that timeout billed" had no answer. This keeps both, one JSON line per
HTTP ask, retries and failures included.

Four rules shape it.

**It cannot fail or slow a cycle.** Every function here swallows its own
errors, exactly like ``journal.record``: a capture that breaks costs the
record of a call, never the call. Writing is a local append of a few tens of
kilobytes under a lock; nothing here touches the network.

**Off unless a cycle opened it.** ``capture()`` opens it, and only the
heartbeat's ``main`` does. A call made from a test, a replay or a notebook is
exactly the call it was, and writes nothing.

**Never a header, never a key.** Only the request *body* is recorded -- the
headers, the client and its configuration never reach this module. And every
record is checked before it is written (``config/redaction.py``), against
the shapes credentials take and against the exact key the provider holds: a
record that looks like it carries one is withheld whole -- its bodies are
dropped, its hashes and a "withheld" marker are kept.

**Checkable from git alone.** The body text is not committed (it is about
ten times the journal's size), but each call's id and the SHA-256 of both
bodies go onto the journal line of the ticker it was for (``take``). Any
copy of the body -- the workflow artifact, the archive's Storage object --
can then be checked against the committed record without trusting where it
came from.

``prompt_sha256`` is the SHA-256 of the request body as canonical JSON
(sorted keys, no spaces, UTF-8), which is the ``request`` string the record
stores; ``answer_sha256`` is the SHA-256 of the ``response`` string, which
for an HTTP call is the body exactly as received.
"""

from __future__ import annotations

import hashlib
import json
import logging
import threading
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Optional

from config.redaction import credential_shape

log = logging.getLogger(__name__)

#: Bumped when a record's shape changes in a way a reader has to know about.
RECORD_VERSION = 1

#: What ``params`` keeps of a request body: everything except the text. The
#: messages (and a system prompt given apart from them) are the bulk of the
#: body and live in ``request``; the output schema is a few kilobytes that
#: are the same on every call, so it is kept as its hash.
_TEXT_KEYS = ("messages", "system")


def canonical(value: Any) -> str:
    """``value`` as the one JSON text its hash is taken over."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def params_of(body: Any) -> dict[str, Any]:
    """The request's parameters without its text: model, max tokens, effort, format.

    A nested ``schema`` is replaced by its hash -- the same few kilobytes on
    every call, which would otherwise be most of what the archive's table
    holds per row.
    """
    if not isinstance(body, dict):
        return {}

    def shrink(node: Any) -> Any:
        if isinstance(node, dict):
            out = {}
            for key, value in node.items():
                if key == "schema" and isinstance(value, dict):
                    out["schema_sha256"] = sha256_text(canonical(value))
                else:
                    out[key] = shrink(value)
            return out
        if isinstance(node, list):
            return [shrink(item) for item in node]
        return node

    return shrink({k: v for k, v in body.items() if k not in _TEXT_KEYS})


# --------------------------------------------------------------------------- #
# The open capture
# --------------------------------------------------------------------------- #


@dataclass
class _Sink:
    """One run's file, and what each ticker's calls were, until its line takes them."""

    path: Path
    run_id: str
    lock: threading.Lock = field(default_factory=threading.Lock)
    #: label (the ticker, or a batch custom id) -> the refs its journal line carries.
    refs: dict[str, list[dict[str, Any]]] = field(default_factory=dict)
    written: int = 0
    withheld: int = 0


#: The open capture, or None. Only ``capture()`` opens one.
_sink: Optional[_Sink] = None


def file_for(directory: Path, run_id: str, opened: datetime) -> Path:
    """``<dir>/YYYY/MM/YYYY-MM-DD/<run id>-<HHMMSS>.jsonl``.

    The time is in the name because a re-run attempt of a GitHub run keeps
    its run id: two attempts of one run must be two files, never one
    overwriting the other in the archive.
    """
    safe = "".join(ch if ch.isalnum() or ch in "-_" else "-" for ch in (run_id or "local"))[:64] or "local"
    day = opened.strftime("%Y-%m-%d")
    return directory / opened.strftime("%Y") / opened.strftime("%m") / day / f"{safe}-{opened:%H%M%S}.jsonl"


@contextmanager
def capture(directory: Optional[Path], run_id: Optional[str] = None) -> Iterator[None]:
    """Record every model call made inside this block to a file under ``directory``.

    ``None`` records nothing, which is what every caller but the heartbeat
    passes. Closed in ``finally``, so a cycle that raised cannot leave its
    capture open for the next cycle in the same process.
    """
    global _sink
    if directory is None:
        yield
        return
    try:
        opened = datetime.now(timezone.utc)
        _sink = _Sink(path=file_for(Path(directory), run_id or "local", opened), run_id=run_id or "")
    except Exception:  # noqa: BLE001 - no capture, never no cycle
        log.exception("could not open the model-call capture; this cycle's calls go unrecorded")
        _sink = None
    try:
        yield
    finally:
        closing, _sink = _sink, None
        if closing is not None and (closing.written or closing.withheld):
            log.info("model calls captured: %d written to %s (%d withheld)",
                     closing.written, closing.path, closing.withheld)


def active() -> bool:
    return _sink is not None


def current_path() -> Optional[Path]:
    return _sink.path if _sink is not None else None


def take(*labels: Optional[str]) -> list[dict[str, Any]]:
    """The calls made under ``labels`` since their last line, and forget them.

    What ``journal.record`` puts on a ticker's line: each call's id and the
    two hashes. Taken rather than read, so the next line for the same
    ticker carries only its own calls. Never raises.
    """
    sink = _sink
    if sink is None:
        return []
    try:
        out: list[dict[str, Any]] = []
        with sink.lock:
            for label in dict.fromkeys(l for l in labels if l):
                out.extend(sink.refs.pop(label, ()))
        return out
    except Exception:  # noqa: BLE001
        log.exception("could not read the captured calls")
        return []


# --------------------------------------------------------------------------- #
# One ask
# --------------------------------------------------------------------------- #


class Attempt:
    """One HTTP ask, from the moment it is sent until its answer is judged.

    Built by ``begin`` just before the request goes out, finished once with
    ``finish``. Every method is safe to call on a capture that is not open
    (``begin`` then returns None, and callers use ``finish_attempt``).
    """

    def __init__(self, sink: _Sink, *, provider: str, model: Optional[str], request: Any,
                 label: Optional[str], attempt: int, kind: str, host: Optional[str],
                 batch_id: Optional[str], custom_id: Optional[str],
                 known: Iterable[Optional[str]]) -> None:
        self._sink = sink
        self._known = tuple(known)
        self.call_id = uuid.uuid4().hex
        self._clock = time.monotonic()
        self.started = datetime.now(timezone.utc)
        self.request_text = canonical(request) if request is not None else None
        self.record: dict[str, Any] = {
            "v": RECORD_VERSION,
            "call_id": self.call_id,
            "ts": self.started.isoformat(),
            "run_id": sink.run_id or None,
            "ticker": label,
            "provider": provider,
            "host": host,
            "model": model,
            "attempt": attempt,
            "kind": kind,
            "batch_id": batch_id,
            "custom_id": custom_id,
            "params": params_of(request),
            "prompt_sha256": sha256_text(self.request_text) if self.request_text is not None else None,
        }
        self._done = False

    def finish(self, *, outcome: str, status: Optional[int] = None, response: Optional[str] = None,
               usage: Optional[dict[str, Any]] = None, error: Optional[str] = None,
               batch_id: Optional[str] = None) -> None:
        """Write the record: how the ask ended, and what came back. Never raises; once only."""
        if self._done:
            return
        self._done = True
        try:
            record = dict(self.record)
            if batch_id:
                record["batch_id"] = batch_id
            record.update({
                "latency_ms": round((time.monotonic() - self._clock) * 1000),
                "status": status,
                "outcome": outcome,
                "error": error,
                "usage": usage or None,
                "answer_sha256": sha256_text(response) if isinstance(response, str) else None,
                "request": self.request_text,
                "response": response if isinstance(response, str) else None,
            })
            _write(self._sink, record, self._known)
        except Exception:  # noqa: BLE001 - see the module docstring
            log.exception("could not record a model call")


def begin(provider: str, model: Optional[str], request: Any, *, label: Optional[str] = None,
          attempt: int = 1, kind: str = "first", host: Optional[str] = None,
          batch_id: Optional[str] = None, custom_id: Optional[str] = None,
          known: Iterable[Optional[str]] = ()) -> Optional[Attempt]:
    """Start recording one ask, or None when no capture is open. Never raises.

    ``request`` is the request BODY and nothing else -- never headers, never
    the client. ``known`` are exact values that must not appear in the
    record (the provider's own key); they are compared and dropped, never
    stored.
    """
    sink = _sink
    if sink is None:
        return None
    try:
        return Attempt(sink, provider=provider, model=model, request=request, label=label,
                       attempt=attempt, kind=kind, host=host, batch_id=batch_id,
                       custom_id=custom_id, known=known)
    except Exception:  # noqa: BLE001
        log.exception("could not start recording a model call")
        return None


def finish_attempt(attempt: Optional[Attempt], **kwargs: Any) -> None:
    """``attempt.finish(**kwargs)`` when there is an attempt; nothing otherwise."""
    if attempt is not None:
        attempt.finish(**kwargs)


def _write(sink: _Sink, record: dict[str, Any], known: Iterable[Optional[str]]) -> None:
    """Append ``record`` to the run's file, withheld whole if it looks like it holds a credential."""
    shape = credential_shape(checked_text(record), known)
    if shape is not None:
        record = withhold(record, shape)
    line = json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
    ref = {"call_id": record["call_id"], "prompt_sha256": record.get("prompt_sha256"),
           "answer_sha256": record.get("answer_sha256")}
    with sink.lock:
        sink.path.parent.mkdir(parents=True, exist_ok=True)
        with sink.path.open("a", encoding="utf-8") as handle:
            handle.write(line)
        if record.get("ticker"):
            sink.refs.setdefault(record["ticker"], []).append(ref)
        if record.get("withheld"):
            sink.withheld += 1
        else:
            sink.written += 1


#: The fields that hold text as a string of their own. Checked as they are,
#: not inside the record's JSON, where every quote around a header name
#: would be escaped and a pattern written for a header would not see one.
BODY_FIELDS = ("request", "response", "error")


def checked_text(record: dict[str, Any]) -> str:
    """Everything in ``record`` a credential could hide in, as one text to search."""
    parts = [record[k] for k in BODY_FIELDS if isinstance(record.get(k), str)]
    parts.append(canonical({k: v for k, v in record.items() if k not in BODY_FIELDS}))
    return "\n".join(parts)


#: The fields a withheld record keeps: who, when, how it ended, and the two
#: hashes -- never a body, and never free text that came from outside.
KEPT_WHEN_WITHHELD = (
    "v", "call_id", "ts", "run_id", "ticker", "provider", "host", "model", "attempt", "kind",
    "batch_id", "custom_id", "latency_ms", "status", "outcome", "usage",
    "prompt_sha256", "answer_sha256",
)


def withhold(record: dict[str, Any], shape: str) -> dict[str, Any]:
    """``record`` without its bodies, marked withheld, naming only the shape it matched."""
    kept = {k: record.get(k) for k in KEPT_WHEN_WITHHELD if k in record}
    kept["withheld"] = f"looked like it held a credential ({shape})"
    kept["request"] = None
    kept["response"] = None
    return kept


__all__ = [
    "Attempt", "BODY_FIELDS", "KEPT_WHEN_WITHHELD", "RECORD_VERSION", "active", "begin", "canonical",
    "capture", "checked_text", "current_path", "file_for", "finish_attempt", "params_of", "sha256_text", "take", "withhold",
]
