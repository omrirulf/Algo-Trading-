"""Read ``logs/signal_journal.log`` into records the scorer can work with.

Pure parsing: a path in, a list of dataclasses out, no network and no
statistics. A journal is an append-only file written by a long-running
process, so it is assumed to be imperfect -- a truncated final line from a
killed process, or a line from an older schema, is counted and skipped rather
than allowed to abort a scoring run over months of otherwise good data.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

#: Score fields the model reports, in the order they are shown in reports.
SCORE_FIELDS = (
    "news_score",
    "technical_score",
    "fundamental_score",
    "analyst_score",
    "insider_score",
)

#: Format of the logging module's ``asctime``, used by journal lines written
#: before ``ts_utc`` existed. It carries no offset, so it is read as UTC and
#: flagged; see ``JournalEntry.timestamp_is_exact``.
_ASCTIME_FORMAT = "%Y-%m-%d %H:%M:%S,%f"


@dataclass(frozen=True)
class JournalEntry:
    """One cycle for one ticker: what the model saw and what it concluded."""

    ticker: str
    timestamp: Optional[datetime]
    #: False when the timestamp came from the tz-naive ``ts`` fallback.
    timestamp_is_exact: bool = False
    bias: Optional[str] = None
    conviction: Optional[float] = None
    scores: dict[str, Optional[float]] = field(default_factory=dict)
    key_factors: list[str] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)
    outcome_status: Optional[str] = None
    error: Optional[str] = None

    @property
    def has_signal(self) -> bool:
        return self.bias is not None and self.conviction is not None

    @property
    def is_directional(self) -> bool:
        """BULLISH or BEARISH. NEUTRAL is a refusal to call, not a wrong call."""
        return self.bias in ("BULLISH", "BEARISH")

    @property
    def direction(self) -> int:
        return {"BULLISH": 1, "BEARISH": -1}.get(self.bias or "", 0)

    def available_scores(self) -> dict[str, float]:
        return {name: value for name, value in self.scores.items() if value is not None}


@dataclass
class JournalRead:
    entries: list[JournalEntry]
    #: Lines that were not valid JSON or not shaped like a journal record.
    skipped: int = 0
    total_lines: int = 0

    def __len__(self) -> int:
        return len(self.entries)


def read_journal(path: Path | str) -> JournalRead:
    """Parse every usable line of a journal file."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"no journal at {path}")
    with path.open(encoding="utf-8") as handle:
        return read_lines(handle)


def read_lines(lines: Iterable[str]) -> JournalRead:
    entries: list[JournalEntry] = []
    skipped = 0
    total = 0

    for line in lines:
        if not line.strip():
            continue
        total += 1
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            skipped += 1
            continue
        entry = _entry_from(payload)
        if entry is None:
            skipped += 1
            continue
        entries.append(entry)

    return JournalRead(entries=entries, skipped=skipped, total_lines=total)


def _entry_from(payload: Any) -> Optional[JournalEntry]:
    if not isinstance(payload, dict):
        return None
    ticker = payload.get("ticker")
    if not isinstance(ticker, str) or not ticker.strip():
        return None

    timestamp, exact = _parse_timestamp(payload)
    signal = payload.get("signal") if isinstance(payload.get("signal"), dict) else {}
    context = payload.get("context") if isinstance(payload.get("context"), dict) else {}
    outcome = payload.get("outcome") if isinstance(payload.get("outcome"), dict) else {}

    return JournalEntry(
        ticker=ticker.strip().upper(),
        timestamp=timestamp,
        timestamp_is_exact=exact,
        bias=_text(signal.get("bias")),
        conviction=_number(signal.get("conviction")),
        scores={name: _number(signal.get(name)) for name in SCORE_FIELDS},
        key_factors=[f for f in signal.get("key_factors", []) or [] if isinstance(f, str)],
        gaps=[g for g in context.get("gaps", []) or [] if isinstance(g, str)],
        outcome_status=_text(outcome.get("status")),
        error=_text(payload.get("error")),
    )


def _parse_timestamp(payload: dict) -> tuple[Optional[datetime], bool]:
    """Prefer the explicit UTC field; fall back to the tz-naive formatter one."""
    raw_utc = payload.get("ts_utc")
    if isinstance(raw_utc, str):
        try:
            parsed = datetime.fromisoformat(raw_utc)
        except ValueError:
            parsed = None
        if parsed is not None:
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed.astimezone(timezone.utc), True

    raw = payload.get("ts")
    if isinstance(raw, str):
        try:
            return datetime.strptime(raw, _ASCTIME_FORMAT).replace(tzinfo=timezone.utc), False
        except ValueError:
            pass
    return None, False


def _number(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if number == number and abs(number) != float("inf") else None


def _text(value: Any) -> Optional[str]:
    return value.strip() if isinstance(value, str) and value.strip() else None
