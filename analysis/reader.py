"""Read journalled signals into records the scorer can work with.

Pure parsing: a path in, a list of dataclasses out, no network and no
statistics. A journal is an append-only file written by a long-running
process, so it is assumed to be imperfect -- a truncated final line from a
killed process, or a line from an older schema, is counted and skipped rather
than allowed to abort a scoring run over months of otherwise good data.

Two sources, one parser. ``read_journal`` reads the log file directly;
``read_database`` reads the byte-exact lines the index in ``store/`` kept
beside every row. Both end up in ``read_lines``, so the scorer cannot give
a different answer depending on where it was pointed -- which is the only
thing that makes a derived index safe to read from at all.

Read-only in both directions. The database is opened through SQLite's
``mode=ro`` URI: a plain connect would *create* an empty file when the path
is wrong, quietly making the scorer a writer and leaving the evidence
behind. A missing database is an error naming it, not zero rows.
"""

from __future__ import annotations

import json
import sqlite3
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

#: Which context sections a score is allowed to be read from. A score whose
#: every source was absent from the prompt has nothing behind it, whatever
#: number the model put there. The cycle nulls such a score before it is
#: journalled; the trainer applies the same rule to lines written before it
#: did. One definition, so the two can never drift apart.
#:
#: A company's analyst read comes from its own coverage; a fund's from the
#: roll-up over what it holds. A company's behaviour signal is Form 4
#: filings; a fund's is who is positioned how, or money moving in and out.
#: A bond fund has neither: nobody rates a bond on a buy-to-sell scale, and
#: no insider files a Form 4 for it.
SCORE_SOURCES: dict[str, tuple[str, ...]] = {
    "analyst_score": ("analysts", "holdings"),
    "insider_score": ("insiders", "positioning", "flows"),
}

#: Every context section named as some score's source.
SOURCE_SECTIONS: frozenset[str] = frozenset(
    name for sources in SCORE_SOURCES.values() for name in sources
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
    #: The learned blend's record for this line, as journalled. Empty on lines
    #: written before it existed and on screened lines, which carry none.
    blend: dict[str, Any] = field(default_factory=dict)
    #: The model that answered, as the API reported it. ``None`` on lines
    #: written before usage was recorded.
    model: Optional[str] = None
    #: ATR(14) as a share of price at signal time, from the journalled
    #: technicals. What the trainer scales a return by.
    atr_pct: Optional[float] = None
    #: The whole journalled technicals section, as written. The rule arms in
    #: ``rules/`` are functions of exactly this, so keeping it on the entry is
    #: what lets ``analysis/horse_race.py`` recompute what each arm would have
    #: said on every line ever journalled -- including every line written
    #: before the arms existed. Empty when the line carried no technicals.
    technicals: dict[str, Any] = field(default_factory=dict)
    #: The journalled INSIDER ACTIVITY section, as written, for the same
    #: reason: the insider arm is a function of exactly this. Empty on a
    #: fund, and on any line that carried none.
    insiders: dict[str, Any] = field(default_factory=dict)
    #: True when the ticker was already in the book and no model was asked.
    #: A race between arms has to leave these out of every arm alike: the
    #: model did not decline the name, it was never offered it, and a
    #: rule-based system holding the same book would not have been either.
    held: bool = False
    #: Source sections the prompt actually carried, out of ``SOURCE_SECTIONS``.
    #: ``None`` on a line that journalled no context at all: an empty set says
    #: the prompt offered nothing, ``None`` says the line cannot tell us, and
    #: the two must not be confused -- one nulls a score, the other must not.
    sections: Optional[frozenset[str]] = None
    #: What the full model's call cost, as journalled (``usage.cost_usd``).
    #: ``None`` when no model was called or the price was unknown.
    cost_usd: Optional[float] = None
    #: What the cheap screen's call cost, when the funnel ran.
    screen_cost_usd: Optional[float] = None
    #: Whether the screen stood in front of the full model on this line.
    #: Journalled explicitly since 24 Sep 2026; on older lines, whether the
    #: line carries a recorded screen answer -- the funnel wrote one on every
    #: line it ran on, and nothing else ever did. ``None`` only on a line
    #: that can say neither (a held or failed line before the field existed).
    screening: Optional[bool] = None
    #: The reasoning level the full model was configured at, as journalled.
    #: ``None`` on lines written before the field existed.
    reasoning_effort: Optional[str] = None
    #: True when ``cost_usd`` is the screen's own call -- a line the screen
    #: ended NEUTRAL, where the journal's usage IS the screen's usage -- so a
    #: spend total counts it once, as screen spend.
    cost_is_screen: bool = False
    #: Where a failed line failed, when that was before the model was asked
    #: (``"context"``). ``None`` on every other line and on older lines.
    stage: Optional[str] = None

    @property
    def model_answered(self) -> bool:
        """The model gave an answer about THIS ticker.

        A signal about a different ticker (journalled with the error
        "answered for X") is not an answer on this line: production refused
        it, and so must every reader that races or watches the model.
        """
        return self.has_signal and not (self.error or "").startswith("answered for")

    @property
    def model_failed(self) -> bool:
        """The model was asked and gave no usable answer: a failed or timed-out call."""
        return not self.model_answered and not self.held and self.stage != "context"

    @property
    def failure_kind(self) -> Optional[str]:
        """For a failed call, ``"setup"`` (our key or configuration) or ``"model"``; else None.

        See ``analysis.call_errors``: only model errors count toward the
        owner's trigger (c).
        """
        if not self.model_failed:
            return None
        from analysis.call_errors import failure_kind

        return failure_kind(self.error)

    def scores_with_a_source(self) -> dict[str, Optional[float]]:
        """The line's scores, with any score that had no source read as null.

        The cycle nulls these before journalling them (``heartbeat``), but
        lines written before it did carry the model's own number -- usually
        0.0, sometimes a confident direction -- for a dimension the prompt
        never showed it. Read from the context the line itself recorded, so
        it is the evidence that decides, not the date.
        """
        if self.sections is None:
            return dict(self.scores)
        return {
            name: (
                None
                if name in SCORE_SOURCES
                and not (self.sections & set(SCORE_SOURCES[name]))
                else value
            )
            for name, value in self.scores.items()
        }

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
        """The scores that are actually usable: not null, and not sourceless."""
        return {
            name: value
            for name, value in self.scores_with_a_source().items()
            if value is not None
        }

    @property
    def composite(self) -> Optional[float]:
        """The blended score, when the line carries one."""
        value = self.blend.get("composite")
        return float(value) if isinstance(value, (int, float)) and not isinstance(value, bool) else None


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


def read_database(path: Path | str, since: Optional[str] = None) -> JournalRead:
    """Parse every journal line the database kept, oldest first.

    The index stores each source line verbatim, so this returns exactly what
    ``read_journal`` would have returned from the file it was built from -- at
    the speed of an indexed scan, and with ``since`` able to skip months of it.

    ``since`` is an ISO date (``2026-09-15``); rows with no timestamp are
    excluded when it is given, because a row that cannot be placed in time
    cannot be said to fall after a date.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"no database at {path}. Build one with: python store/build_db.py"
        )
    sql = "SELECT raw FROM signals"
    params: tuple = ()
    if since:
        sql += " WHERE trade_date IS NOT NULL AND trade_date >= ?"
        params = (since,)
    sql += " ORDER BY ts_utc IS NULL, ts_utc, id"

    connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        rows = connection.execute(sql, params).fetchall()
    finally:
        connection.close()
    return read_lines(row[0] for row in rows)


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
        entry = entry_from(payload)
        if entry is None:
            skipped += 1
            continue
        entries.append(entry)

    return JournalRead(entries=entries, skipped=skipped, total_lines=total)


def entry_from(payload: Any) -> Optional[JournalEntry]:
    """One parsed journal line, or None if it is not one.

    Public because ``store/loader.py`` builds its database rows from this
    rather than re-reading the JSON itself. Two parsers over one format
    would eventually disagree, and the disagreement would show up as a
    report that does not match the file it was built from.
    """
    if not isinstance(payload, dict):
        return None
    ticker = payload.get("ticker")
    if not isinstance(ticker, str) or not ticker.strip():
        return None

    timestamp, exact = parse_timestamp(payload)
    signal = payload.get("signal") if isinstance(payload.get("signal"), dict) else {}
    context = payload.get("context") if isinstance(payload.get("context"), dict) else {}
    outcome = payload.get("outcome") if isinstance(payload.get("outcome"), dict) else {}
    usage = payload.get("usage") if isinstance(payload.get("usage"), dict) else {}
    technicals = context.get("technicals") if isinstance(context.get("technicals"), dict) else {}
    insider_section = context.get("insiders") if isinstance(context.get("insiders"), dict) else {}

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
        blend=payload.get("blend") if isinstance(payload.get("blend"), dict) else {},
        model=_text(usage.get("model")),
        atr_pct=_number(technicals.get("atr_pct_of_price")),
        technicals=dict(technicals),
        insiders=dict(insider_section),
        held=bool(payload.get("held")),
        sections=_sections(payload),
        cost_usd=_number(usage.get("cost_usd")),
        screen_cost_usd=None if _usage_is_the_screens(payload) else _screen_cost(payload.get("screen")),
        cost_is_screen=_usage_is_the_screens(payload),
        stage=_text(payload.get("stage")),
        screening=_screening(payload),
        reasoning_effort=_text(payload.get("reasoning_effort")),
    )


def _usage_is_the_screens(payload: dict) -> bool:
    """A screened-NEUTRAL line: the journal's usage is the screen's own call."""
    screen = payload.get("screen")
    usage = payload.get("usage")
    return (isinstance(screen, dict) and isinstance(usage, dict)
            and isinstance(screen.get("usage"), dict) and screen["usage"] == usage)


def _screen_cost(screen: Any) -> Optional[float]:
    if not isinstance(screen, dict) or not isinstance(screen.get("usage"), dict):
        return None
    return _number(screen["usage"].get("cost_usd"))


def _screening(payload: dict) -> Optional[bool]:
    """Whether the screen ran on this line: the journalled flag, else the evidence."""
    flag = payload.get("screening")
    if isinstance(flag, bool):
        return flag
    if isinstance(payload.get("screen"), dict):
        return True
    if isinstance(payload.get("signal"), dict):
        # A full-model answer with no screen beside it: the funnel was off.
        return False
    return None


def _sections(payload: dict) -> Optional[frozenset[str]]:
    """Which source sections the journalled context carried, if it carried one."""
    context = payload.get("context")
    if not isinstance(context, dict):
        return None
    return frozenset(name for name in SOURCE_SECTIONS if context.get(name))


def parse_timestamp(payload: dict) -> tuple[Optional[datetime], bool]:
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
