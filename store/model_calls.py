"""The model-call capture, packaged for the archive: a table row per call, a file per run.

``orchestrator/model_io.py`` writes one JSON line per model ask -- the full
request body, the full response body with its reasoning text, and how the
ask ended -- to ``logs/model_io/YYYY/MM/YYYY-MM-DD/<run>.jsonl``. This turns
one such file into what the archive keeps of it:

* one ``model_calls`` row per line: who was asked, when, how it ended, the
  token counts, the parameters, and the two SHA-256 hashes -- never a body;
* one xz object in the private Storage bucket ``model-io``, at the same
  relative path plus ``.xz``, holding the lines themselves;
* one ``model_io_files`` row naming that object, its size and its hash.

Every line is checked for credentials again here, on the way out, with the
same shapes the capture used (``config/redaction.py``): a line that matches
is withheld whole -- bodies dropped, hashes and a "withheld" marker kept --
in the object and in its row, and counted, so the push can say so.

Pure: reads a file, returns bytes and rows. Nothing here writes a file or
touches the network; ``store/push_remote.py`` does the sending.
"""

from __future__ import annotations

import hashlib
import json
import lzma
import math
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from config.redaction import credential_shape
from orchestrator.model_io import checked_text, withhold

#: xz (LZMA2), the owner's choice of 26 Sep 2026: about 60% smaller than
#: gzip on these files (~85 MB a year instead of ~205 MB), and a format any
#: computer opens -- ``xz -d`` or ``unxz`` on Linux and macOS, the Archive
#: Utility on macOS, 7-Zip on Windows, ``lzma`` in Python's standard
#: library. The settings are fixed, and xz writes no timestamp, so the same
#: lines always make the same bytes and a re-sent object is the same object.
XZ_PRESET = 9
#: The object's suffix and its media type, as Storage is told.
SUFFIX = ".xz"
MEDIA_TYPE = "application/x-xz"

#: How much of a call's ``error`` the table keeps. The capture writes short
#: ones (an exception class, an HTTP status, a parse complaint).
MAX_ERROR_CHARS = 300


@dataclass
class Package:
    """One capture file, ready to send."""

    source: Path
    #: The object's path inside the bucket: ``YYYY/MM/YYYY-MM-DD/<run>.jsonl.xz``.
    object_path: str
    data: bytes
    sha256: str
    rows: list[dict[str, Any]] = field(default_factory=list)
    #: Lines withheld here, on top of any the capture already withheld.
    withheld: int = 0
    #: Lines already marked withheld by the capture.
    withheld_before: int = 0
    unreadable: int = 0
    raw_bytes: int = 0

    def file_row(self, run_id: Optional[str]) -> dict[str, Any]:
        return {
            "object_path": self.object_path,
            "ingested_at": _now(),
            "day": _day_of(self.object_path),
            "run_id": run_id,
            "calls": len(self.rows),
            "withheld": self.withheld + self.withheld_before,
            "unreadable": self.unreadable,
            "raw_bytes": self.raw_bytes,
            "compressed_bytes": len(self.data),
            "sha256": self.sha256,
        }


def capture_files(directory: Path) -> list[Path]:
    """Every capture file under ``directory``, oldest path first. Missing is empty."""
    directory = Path(directory)
    if not directory.is_dir():
        return []
    return sorted(p for p in directory.rglob("*.jsonl") if p.is_file())


def object_path(path: Path, directory: Path) -> str:
    """The Storage path for ``path``: its place under ``directory``, plus ``.xz``."""
    relative = Path(path).resolve().relative_to(Path(directory).resolve())
    return "/".join(relative.parts) + SUFFIX


def redact(record: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    """``record``, or a withheld copy of it if it looks like it holds a credential.

    The second value is True when this check withheld it. A record the
    capture already withheld has no bodies left and passes as it is.
    """
    shape = credential_shape(checked_text(record))
    if shape is None:
        return record, False
    return withhold(record, shape), True


def package(path: Path, directory: Path) -> Package:
    """Read one capture file, check every line, and build the object and the rows."""
    lines_out: list[str] = []
    rows: list[dict[str, Any]] = []
    unreadable = withheld = withheld_before = 0
    key = object_path(path, directory)
    with Path(path).open("rb") as handle:
        raw = handle.read()
    for text in raw.decode("utf-8", errors="replace").splitlines():
        if not text.strip():
            continue
        try:
            record = json.loads(text)
        except json.JSONDecodeError:
            # A line cut short by a killed process. Not sent: it cannot be
            # checked for a credential, and it is not a whole record anyway.
            unreadable += 1
            continue
        if not isinstance(record, dict) or not isinstance(record.get("call_id"), str):
            unreadable += 1
            continue
        if record.get("withheld"):
            withheld_before += 1
        record, caught = redact(record)
        withheld += int(caught)
        lines_out.append(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
        rows.append(call_row(record, key))
    body = ("\n".join(lines_out) + "\n").encode("utf-8") if lines_out else b""
    data = lzma.compress(body, format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=XZ_PRESET)
    return Package(
        source=Path(path), object_path=key, data=data, sha256=hashlib.sha256(data).hexdigest(),
        rows=rows, withheld=withheld, withheld_before=withheld_before, unreadable=unreadable,
        raw_bytes=len(body),
    )


def call_row(record: dict[str, Any], object_key: Optional[str]) -> dict[str, Any]:
    """One captured ask as a ``model_calls`` row: everything but the bodies."""
    usage = record.get("usage") if isinstance(record.get("usage"), dict) else {}
    details = usage.get("completion_tokens_details") if isinstance(usage.get("completion_tokens_details"), dict) else {}
    moment = _instant(record.get("ts"))
    error = record.get("error")
    return {
        "call_id": record["call_id"],
        "ingested_at": _now(),
        "ts_utc": moment.isoformat() if moment else None,
        "trade_date": moment.date().isoformat() if moment else None,
        "run_id": _text(record.get("run_id")),
        "ticker": _text(record.get("ticker")),
        "provider": _text(record.get("provider")),
        "host": _text(record.get("host")),
        "model": _text(record.get("model")),
        "attempt": _int(record.get("attempt")),
        "kind": _text(record.get("kind")),
        "outcome": _text(record.get("outcome")),
        "http_status": _int(record.get("status")),
        "error": error[:MAX_ERROR_CHARS] if isinstance(error, str) and error else None,
        "latency_ms": _int(record.get("latency_ms")),
        "batch_id": _text(record.get("batch_id")),
        "custom_id": _text(record.get("custom_id")),
        # Parameters only when the record still has them: a withheld record
        # keeps none of its request.
        "params": record.get("params") if isinstance(record.get("params"), dict) else None,
        "input_tokens": _int(usage.get("prompt_tokens", usage.get("input_tokens"))),
        "output_tokens": _int(usage.get("completion_tokens", usage.get("output_tokens"))),
        "reasoning_tokens": _int(details.get("reasoning_tokens")),
        "prompt_sha256": _text(record.get("prompt_sha256")),
        "answer_sha256": _text(record.get("answer_sha256")),
        "request_chars": len(record["request"]) if isinstance(record.get("request"), str) else None,
        "response_chars": len(record["response"]) if isinstance(record.get("response"), str) else None,
        "withheld": _text(record.get("withheld")),
        "object_path": object_key,
    }


def verify(record: dict[str, Any]) -> list[str]:
    """What does not match in one stored record: its bodies against its own hashes.

    Empty when the record is whole. The check any copy of the archive can be
    put through with nothing but the journal line that names the call.
    """
    problems = []
    request, response = record.get("request"), record.get("response")
    if isinstance(request, str) and _sha(request) != record.get("prompt_sha256"):
        problems.append("request does not match prompt_sha256")
    if isinstance(response, str) and _sha(response) != record.get("answer_sha256"):
        problems.append("response does not match answer_sha256")
    return problems


def run_of(rows: list[dict[str, Any]]) -> Optional[str]:
    """The run id the rows share, or None."""
    ids = {row.get("run_id") for row in rows if row.get("run_id")}
    return ids.pop() if len(ids) == 1 else None


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _day_of(key: str) -> Optional[str]:
    parts = key.split("/")
    return parts[2] if len(parts) >= 4 else None


def _instant(value: Any) -> Optional[datetime]:
    if not isinstance(value, str) or not value:
        return None
    try:
        moment = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return (moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)).astimezone(timezone.utc)


def _int(value: Any) -> Optional[int]:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        return None
    return int(value)


def _text(value: Any) -> Optional[str]:
    return value.strip() if isinstance(value, str) and value.strip() else None


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


__all__ = ["GZIP_LEVEL", "Package", "call_row", "capture_files", "object_path",
           "package", "redact", "run_of", "verify"]
