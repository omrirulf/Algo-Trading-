"""Join journal entries to realised returns and assemble a run for reporting."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Optional, Sequence

from analysis.reader import JournalEntry, JournalRead
from analysis.returns import (
    ENTRY_AUTO,
    STATUS_OK,
    PriceSource,
    forward_return,
)
from analysis.metrics import ScoredSignal


@dataclass
class ScoringRun:
    """Everything the report needs, and nothing it has to go and fetch."""

    horizon: int
    entry_rule: str
    floor: float
    read: JournalRead
    signals: list[ScoredSignal] = field(default_factory=list)
    statuses: Counter = field(default_factory=Counter)
    neutral_count: int = 0

    @property
    def entries(self) -> list[JournalEntry]:
        return self.read.entries

    @property
    def with_signal(self) -> list[JournalEntry]:
        return [e for e in self.entries if e.has_signal]

    @property
    def directional(self) -> list[JournalEntry]:
        return [e for e in self.entries if e.is_directional]


def score_entries(
    entries: Sequence[JournalEntry],
    source: PriceSource,
    horizon: int,
    entry_rule: str = ENTRY_AUTO,
    today: Optional[date] = None,
) -> tuple[list[ScoredSignal], Counter]:
    """Attach a forward return to every directional signal that has one yet.

    NEUTRAL signals are not scored. A refusal to call a direction has no
    direction to be right or wrong about, and folding them in as zeroes would
    quietly drag every average toward the middle.
    """
    today = today or datetime.now(timezone.utc).date()
    statuses: Counter = Counter()
    scored: list[ScoredSignal] = []

    by_ticker: dict[str, list[JournalEntry]] = {}
    for candidate in entries:
        if candidate.is_directional and candidate.timestamp is not None:
            by_ticker.setdefault(candidate.ticker, []).append(candidate)
        elif candidate.is_directional:
            statuses["no_timestamp"] += 1

    for ticker, ticker_entries in sorted(by_ticker.items()):
        start = min(e.timestamp.date() for e in ticker_entries)
        series = source.closes(ticker, start, today)
        for candidate in ticker_entries:
            lookup = forward_return(
                series,
                candidate.timestamp,
                horizon=horizon,
                timestamp_is_exact=candidate.timestamp_is_exact,
                entry=entry_rule,
            )
            statuses[lookup.status] += 1
            if lookup.status == STATUS_OK and lookup.value is not None:
                scored.append(ScoredSignal(entry=candidate, forward=lookup.value))

    return scored, statuses


def build_run(
    read: JournalRead,
    source: PriceSource,
    horizon: int,
    floor: float,
    entry_rule: str = ENTRY_AUTO,
    today: Optional[date] = None,
) -> ScoringRun:
    signals, statuses = score_entries(read.entries, source, horizon, entry_rule, today)
    return ScoringRun(
        horizon=horizon,
        entry_rule=entry_rule,
        floor=floor,
        read=read,
        signals=signals,
        statuses=statuses,
        neutral_count=sum(1 for e in read.entries if e.bias == "NEUTRAL"),
    )
