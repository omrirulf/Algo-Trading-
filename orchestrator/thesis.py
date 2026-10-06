"""The thesis-check logger: once a week, does the reason a held name was bought still hold? Log only.

Why (the owner's instruction of 4 Oct 2026, item 2). Once a week, for each
name the paper account holds, the same model is asked, with the same
settings as production: given the reasoning recorded when the position was
opened and today's headlines for the name, is the thesis VALID, WEAKENED or
BROKEN? With one sentence of reason. ``config/thesis_check.py`` holds the
dates, the cap and the forward return the checkpoints read.

What it reads. The entry reasoning is the audit log's record of the accepted
entry (``cfg.AUDIT_LOG_PATH``, the latest ``signal_processed`` record that
was ACCEPTED for the name, as ``analysis/book.py`` reads the book): the
signal's rationale, key factors and bias, and the side the position was
opened on. Today's headlines are the ones on the name's held line in
today's production cycle, so nothing is gathered and no news search is paid.

Log only. It never trades, never changes a stop, and never feeds any arm or
fund: there is no dispatcher here, no engine, no broker, no line in the
production journal (``journal.record`` is never called), and nothing is
written but this logger's own lines, in ``logs/thesis_check/``, one file per
UTC month. Nothing in the cycle reads them. ``tests/test_thesis_check_runner.py``
checks this by reading this file.

When. Once a week. The week's check day is the first UTC day of the ISO
week, from ``START``, on which the production journal holds a cycle; the
names are the ones held in that day's cycle. A name whose check failed is
asked again on a later day of the same week while it is still held, at most
once a day. A name with a successful check this week is done, and so is a
name with no entry record or one the week's cost cap stopped: each gets one
line saying so, and waits for the next week. The job runs
in the shadow-universe workflow last, after the vote and the universe, so the
model provider is never asked by two of them at once, and starts no new name
from 23:15 UTC.

The cost cap. At most ``WEEKLY_COST_CAP_USD`` ($0.10) an ISO week, about
$0.06 expected. Every HTTP ask counts (an ask with no price is charged the
estimate). At the cap no new name starts; each name it stops gets its line
(``analysis.thesis.NOT_ASKED_CAP``). The run that first stops a name at the
cap this week ends with exit code 3, so the workflow tells the owner's phone
once a week: a later run that week, which finds a cap line already written,
ends with 0, and so does a run that reaches the cap with the last name it
started and stops none.

Off until 2027-04-01. Nothing happens unless ``THESIS_CHECK_ENABLED`` is on,
today (UTC) is on or after ``START``, today is a trading day, it is before
23:15 UTC, and the production journal already holds today's cycle.
``--check`` says which one stops it.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import date, datetime, time as clock_time, timedelta, timezone
from pathlib import Path
from typing import Any, Final, Literal, Mapping, Optional, Sequence

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from analysis import thesis as checks
from analysis.cycle_day import cycle_ran_on
from analysis.reader import JournalEntry, entry_from, read_journal
from config import journal_files
from config import settings as cfg
from config import thesis_check as tc
from config.market_calendar import is_trading_day
from orchestrator import heartbeat, llm, model_io
from orchestrator.llm import Completion, LLMError
from orchestrator.vote import CaptureLedger, CostGuard, LineWriter

log = logging.getLogger("thesis")

#: Names asked at the same time: production's full-model setting, as the vote.
WORKERS: Final[int] = cfg.FULL_MODEL_MAX_CONCURRENCY

#: No new name is started after this many seconds. About 20 held names, four
#: at a time, take about 15 minutes at the slowest measured pace (212 seconds
#: a call); ``tests/test_thesis_check_runner.py`` keeps this and the
#: workflow's ``timeout-minutes`` in step.
RUN_BUDGET_SECONDS: Final[float] = 30 * 60

#: No new name is started at or after this UTC time (``config/thesis_check.py``).
NO_NEW_NAME_AFTER_UTC: Final[clock_time] = tc.NO_NEW_NAME_AFTER_UTC

#: Exit codes of ``python -m orchestrator.thesis``.
EXIT_OK: Final[int] = 0
EXIT_FAILED: Final[int] = 1
EXIT_CAP_REACHED: Final[int] = 3

#: What became of one name in a run.
CHECKED: Final[str] = "checked"
FAILED: Final[str] = "failed"
NOT_ASKED: Final[str] = "not asked"
UNRECORDED: Final[str] = "unrecorded"

#: Why a name was written without a call: the audit log has no accepted entry
#: for it, or the week's cost cap stopped it. Both final for the week; one
#: spelling, the read side's (``analysis/thesis.py``).
NO_ENTRY: Final[str] = checks.NO_ENTRY
NOT_ASKED_CAP: Final[str] = checks.NOT_ASKED_CAP

#: The audit log's record of a signal the engine decided on.
ENTRY_EVENT: Final[str] = "signal_processed"

#: The side a position was opened on, from the engine's order side, else the signal's bias.
SIDES: Final[dict[str, str]] = {"buy": "long", "sell": "short"}
BIAS_SIDES: Final[dict[str, str]] = {"BULLISH": "long", "BEARISH": "short"}

#: The longest reason kept for a failed check, so a line stays one short record.
ERROR_MAX_CHARS: Final[int] = 300

#: The question, fixed. The model judges only from the text it is given.
SYSTEM_PROMPT: Final[str] = """\
You review an open position in a paper trading account. You are given the \
reasoning recorded when the position was opened, and today's news headlines \
about the name. Judge only from the text given here: do not use anything you \
may know about prices or events that is not in it.

Answer whether the reason the position was opened still holds:
- VALID: the reasoning still holds.
- WEAKENED: part of it no longer holds, or today's headlines cut against it.
- BROKEN: its main point no longer holds.

Give the reason in one sentence. Reply with the JSON object required by the \
schema and nothing else."""

#: The fixed words after the name's facts in the user prompt.
USER_PROMPT_TAIL: Final[str] = "\n\nRespond with the JSON thesis check for {ticker}."

#: What the user prompt says in place of an empty list.
NONE_RECORDED: Final[str] = "(none recorded)"
NO_HEADLINES: Final[str] = "no headlines today"

_SIDE_WORDS: Final[dict[str, str]] = {"long": "long (bought)", "short": "short (sold short)"}


class ThesisCheck(BaseModel):
    """The model's answer: the name, the verdict, and one sentence of reason."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    ticker: str = Field(..., min_length=1, max_length=10, description="The ticker the check is for")
    verdict: Literal["VALID", "WEAKENED", "BROKEN"] = Field(
        ..., description="VALID: the reasoning still holds. WEAKENED: part of it no longer holds. "
                         "BROKEN: its main point no longer holds.")
    reason: str = Field(..., min_length=1, description="One sentence: why")


#: The answer schema the model is held to, derived from ``ThesisCheck``.
SCHEMA: Final[dict] = ThesisCheck.model_json_schema()


def parse_check(text: str) -> ThesisCheck:
    """The model's answer, validated. Raises ``ValueError`` (a ``ValidationError`` is one) on a bad answer."""
    return ThesisCheck.model_validate(json.loads(text))


def utc_now() -> datetime:
    """Now, in UTC. A function so a test can freeze the clock."""
    return datetime.now(timezone.utc)


def _utc(moment: datetime) -> datetime:
    return moment.replace(tzinfo=timezone.utc) if moment.tzinfo is None else moment.astimezone(timezone.utc)


def week_of(day: date) -> str:
    """The ISO week of ``day``, as the lines name it: ``2027-W14``."""
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


# --------------------------------------------------------------------------- #
# Would it run today?
# --------------------------------------------------------------------------- #


def why_not(day: date) -> Optional[str]:
    """Why no name is checked on ``day`` (a UTC date), or None when it may be.

    Read from ``config.thesis_check`` at call time, in this order: the flag,
    the start date, the NYSE calendar.
    """
    if not tc.THESIS_CHECK_ENABLED:
        return "the flag THESIS_CHECK_ENABLED is off"
    if day < tc.START:
        return f"{day.isoformat()} is before the start date {tc.START.isoformat()}"
    if not is_trading_day(day):
        return f"{day.isoformat()} is not a trading day"
    return None


def too_late(now: datetime) -> Optional[str]:
    """The reason no new name may be started at ``now``, or None while it still may."""
    moment = _utc(now)
    if moment.time() >= NO_NEW_NAME_AFTER_UTC:
        return (f"{moment.strftime('%H:%M')} UTC is too late in the UTC day: no new name is started "
                f"from {NO_NEW_NAME_AFTER_UTC.strftime('%H:%M')} UTC, so no line is dated the next day")
    return None


def production_ran(day: date) -> bool:
    """Whether the production journal has a cycle on ``day``. An unreadable journal counts as no cycle."""
    try:
        return cycle_ran_on(read_journal(cfg.SIGNAL_JOURNAL_PATH).entries, day)
    except (OSError, ValueError):
        return False


def waiting_for_production(day: date) -> Optional[str]:
    """The reason to wait for production on ``day``, or None once its cycle is journalled."""
    if production_ran(day):
        return None
    return (f"no production cycle is journalled for {day.isoformat()} yet: the thesis check reads "
            "today's held lines, and never asks the model provider at the same time as production")


def _reason(moment: datetime) -> Optional[str]:
    day = moment.date()
    return why_not(day) or too_late(moment) or waiting_for_production(day)


def check(now: Optional[datetime] = None) -> dict[str, Any]:
    """``{"date", "run", "reason"}`` for today (UTC). Asks nothing, writes nothing."""
    moment = _utc(now or utc_now())
    reason = _reason(moment)
    return {"date": moment.date().isoformat(), "run": reason is None, "reason": reason}


# --------------------------------------------------------------------------- #
# The week: its check day, its names, and the lines already written
# --------------------------------------------------------------------------- #


def _usd(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not value >= 0:
        return 0.0
    return float(value)


def _written_day(payload: Mapping[str, Any]) -> Optional[date]:
    raw = payload.get("ts_utc")
    if not isinstance(raw, str):
        return None
    try:
        return _utc(datetime.fromisoformat(raw)).date()
    except ValueError:
        return None


@dataclass(frozen=True)
class WeekLines:
    """What this logger's lines of one ISO week say."""

    #: Model cost so far this week: the ``cost_usd`` of every line of the week.
    spent_usd: float = 0.0
    #: Names done until next week: a successful check, no entry record, or the cap.
    done: frozenset[str] = frozenset()
    #: Names with any line written today: asked at most once a day.
    tried_today: frozenset[str] = frozenset()
    #: A line of this week says the week's cost cap stopped it: the phone has been told.
    cap_noted: bool = False


def week_lines(directory: Path | str, week: str, day: date) -> WeekLines:
    """Read the week's lines from every month's file in ``directory``. Never raises on a bad line."""
    path = Path(directory)
    if not journal_files.exists(path):
        return WeekLines()
    spent = 0.0
    done: set[str] = set()
    tried: set[str] = set()
    cap_noted = False
    for raw in journal_files.iter_lines(path):
        try:
            payload = json.loads(raw)
        except ValueError:
            continue
        if not isinstance(payload, dict) or payload.get("event") != tc.EVENT or payload.get("week") != week:
            continue
        spent += _usd(payload.get("cost_usd"))
        ticker = payload.get("ticker")
        if not isinstance(ticker, str):
            continue
        name = ticker.strip().upper()
        error = payload.get("error")
        if (error is None and payload.get("verdict") in tc.VERDICTS) or error in (NO_ENTRY, NOT_ASKED_CAP):
            done.add(name)
        cap_noted = cap_noted or error == NOT_ASKED_CAP
        if _written_day(payload) == day:
            tried.add(name)
    return WeekLines(spent, frozenset(done), frozenset(tried), cap_noted)


@dataclass(frozen=True)
class Due:
    """The names to check today."""

    week: str
    #: The week's check day: its first day (from ``START``) with a production cycle.
    check_day: Optional[date] = None
    #: Held on the check day, held today, not done this week, not tried today; journal order.
    names: tuple[str, ...] = ()
    #: Each held name's headlines, from its latest held line of today's cycle.
    headlines: Mapping[str, tuple[str, ...]] = field(default_factory=dict)


def _production(first: date, last: date) -> list[tuple[Mapping[str, Any], JournalEntry]]:
    """The production journal's lines from ``first`` to ``last`` (UTC days), in order. Never raises."""
    path = cfg.SIGNAL_JOURNAL_PATH
    out: list[tuple[Mapping[str, Any], JournalEntry]] = []
    try:
        if not journal_files.exists(path):
            return out
        for raw in journal_files.iter_lines(path):
            try:
                payload = json.loads(raw)
            except ValueError:
                continue
            entry = entry_from(payload)
            if entry is None or entry.timestamp is None or not first <= entry.timestamp.date() <= last:
                continue
            out.append((payload, entry))
    except OSError:
        log.exception("could not read the production journal")
        return []
    return out


def _headlines(payload: Mapping[str, Any]) -> tuple[str, ...]:
    context = payload.get("context")
    found = context.get("headlines") if isinstance(context, Mapping) else None
    if not isinstance(found, list):
        return ()
    return tuple(text.strip() for text in found if isinstance(text, str) and text.strip())


def due_names(day: date, seen: WeekLines) -> Due:
    """The names to check on ``day``, by the week's rule (see the module docstring)."""
    week = week_of(day)
    monday = day - timedelta(days=day.weekday())
    lines = _production(max(monday, tc.START), day)
    if not lines:
        return Due(week, None, (), {})
    check_day = min(entry.timestamp.date() for _, entry in lines)
    on_check_day = list(dict.fromkeys(entry.ticker for _, entry in lines
                                      if entry.held and entry.timestamp.date() == check_day))
    held_today: dict[str, tuple[str, ...]] = {}
    for payload, entry in lines:
        if entry.held and entry.timestamp.date() == day:
            held_today[entry.ticker] = _headlines(payload)   # the latest held line wins
    names = tuple(name for name in on_check_day
                  if name in held_today and name not in seen.done and name not in seen.tried_today)
    return Due(week, check_day, names, held_today)


# --------------------------------------------------------------------------- #
# The entry reasoning, from the audit log
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Entry:
    """The record of a position's opening: when, which side, and the reasoning the signal gave."""

    ticker: str
    at: datetime
    side: str
    bias: Optional[str]
    rationale: Optional[str]
    key_factors: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return {"ts": self.at.isoformat(), "rationale": self.rationale, "key_factors": list(self.key_factors),
                "bias": self.bias}


def _number(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _audit_time(item: Mapping[str, Any], result: Mapping[str, Any]) -> Optional[datetime]:
    """The decision's time: the engine's own UTC timestamp, else the log line's clock read as UTC."""
    raw = result.get("timestamp")
    if isinstance(raw, str):
        try:
            return _utc(datetime.fromisoformat(raw))
        except ValueError:
            pass
    raw = item.get("ts")
    if isinstance(raw, str):
        try:
            return datetime.strptime(raw, "%Y-%m-%d %H:%M:%S,%f").replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    return None


def entry_from_audit(item: Any) -> Optional[Entry]:
    """An accepted entry from one audit record, or None for anything else.

    The rule ``analysis.book.positions_from`` reads the book by: a
    ``signal_processed`` record whose result is ACCEPTED, for a ticker, with
    an entry price and a stop.
    """
    if not isinstance(item, dict) or (item.get("event") or item.get("message")) != ENTRY_EVENT:
        return None
    result = item.get("result")
    if not isinstance(result, dict) or result.get("status") != "ACCEPTED":
        return None
    ticker = str(result.get("ticker") or "").strip().upper()
    if not ticker or not _number(result.get("entry_price")) or not _number(result.get("stop_price")):
        return None
    at = _audit_time(item, result)
    signal = item.get("signal") if isinstance(item.get("signal"), dict) else {}
    bias = signal.get("bias") if isinstance(signal.get("bias"), str) else None
    side = SIDES.get(str(result.get("side") or "")) or BIAS_SIDES.get(bias or "")
    if at is None or side is None:
        return None
    rationale = signal.get("rationale")
    factors = signal.get("key_factors")
    return Entry(
        ticker=ticker, at=at, side=side, bias=bias,
        rationale=rationale.strip() if isinstance(rationale, str) and rationale.strip() else None,
        key_factors=tuple(f.strip() for f in factors if isinstance(f, str) and f.strip())
        if isinstance(factors, list) else (),
    )


def latest_entries(now: datetime, path: Path | str | None = None) -> dict[str, Entry]:
    """Each name's latest accepted entry on or before ``now``, from the audit log. Never raises."""
    source = Path(cfg.AUDIT_LOG_PATH if path is None else path)
    moment = _utc(now)
    out: dict[str, Entry] = {}
    try:
        with source.open(encoding="utf-8") as handle:
            for raw in handle:
                if ENTRY_EVENT not in raw:
                    continue
                try:
                    item = json.loads(raw)
                except ValueError:
                    continue
                entry = entry_from_audit(item)
                if entry is None or entry.at > moment:
                    continue
                known = out.get(entry.ticker)
                if known is None or entry.at >= known.at:
                    out[entry.ticker] = entry
    except OSError:
        log.warning("could not read the audit log at %s", source)
        return {}
    return out


# --------------------------------------------------------------------------- #
# The question, the answer, the line
# --------------------------------------------------------------------------- #


def user_prompt(ticker: str, entry: Entry, headlines: Sequence[str]) -> str:
    """The name's facts: the side and day it was opened, the reasoning then, and today's headlines."""
    lines = [
        f"TICKER: {ticker}",
        f"POSITION: {_SIDE_WORDS.get(entry.side, entry.side)}",
        f"OPENED: {entry.at.date().isoformat()}",
        "",
        "REASONING RECORDED WHEN THE POSITION WAS OPENED:",
        entry.rationale or NONE_RECORDED,
        "",
        "KEY FACTORS RECORDED THEN:",
        *([f"- {factor}" for factor in entry.key_factors] or [NONE_RECORDED]),
        "",
        "TODAY'S HEADLINES:",
        *([f"- {headline}" for headline in headlines] or [NO_HEADLINES]),
    ]
    return "\n".join(lines) + USER_PROMPT_TAIL.format(ticker=ticker)


def read_answer(ticker: str, answer: "Completion | BaseException") -> tuple[Optional[str], Optional[str], Optional[str]]:
    """``(verdict, reason, error)`` from one call's answer. A bad verdict is a failed check."""
    try:
        if isinstance(answer, BaseException):
            raise answer
        said = parse_check(answer.text)
    except LLMError as exc:
        error = str(exc)
    except (json.JSONDecodeError, ValidationError) as exc:
        error = f"invalid model output: {exc}"
    except Exception as exc:  # noqa: BLE001 - one name must not end the run
        error = f"unexpected {type(exc).__name__}: {exc}"
    else:
        if said.ticker.strip().upper() == ticker:
            return said.verdict, said.reason[:tc.REASON_MAX_CHARS], None
        error = f"answered for {said.ticker}"
    return None, None, error[:ERROR_MAX_CHARS]


def thesis_line(ticker: str, now: datetime, week: str, *, entry: Optional[Entry], headline_count: int,
                verdict: Optional[str] = None, reason: Optional[str] = None, asks: int = 0,
                cost_usd: float = 0.0, setup: Optional[dict[str, Any]] = None, effort: Optional[str] = None,
                error: Optional[str] = None) -> dict[str, Any]:
    """One line of ``logs/thesis_check/``: the check of one held name, or why it was not made."""
    return {
        "ts_utc": _utc(now).isoformat(),
        "event": tc.EVENT,
        "week": week,
        "ticker": ticker,
        "side": entry.side if entry is not None else None,
        "entry": entry.as_dict() if entry is not None else None,
        "headline_count": headline_count,
        "verdict": verdict,
        "reason": reason,
        "asks": asks,
        "cost_usd": round(cost_usd, 6),
        "model_setup": setup,
        "reasoning_effort": effort,
        "error": error,
    }


# --------------------------------------------------------------------------- #
# One name
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class _Shared:
    """What every worker of one run reads."""

    provider: Any
    ask_effort: Optional[str]
    guard: CostGuard
    ledger: CaptureLedger
    writer: LineWriter
    week: str
    setup: Optional[dict[str, Any]]
    effort: Optional[str]
    deadline: float
    day: date


def _check(ticker: str, entry: Entry, headlines: tuple[str, ...], shared: _Shared) -> tuple[str, int]:
    """``(what became of the name, the HTTP asks its call made)``."""
    if time.monotonic() >= shared.deadline:
        return NOT_ASKED, 0
    now = _utc(utc_now())
    if now.date() != shared.day or too_late(now) is not None:
        return NOT_ASKED, 0
    if not shared.guard.reserve():
        log.warning("%s: the week's cost cap is reached; not checked", ticker)
        try:
            shared.writer.write(thesis_line(ticker, now, shared.week, entry=entry, headline_count=len(headlines),
                                            setup=shared.setup, effort=shared.effort, error=NOT_ASKED_CAP), now)
        except Exception:  # noqa: BLE001 - one line must not end the run
            log.exception("%s: could not write its line", ticker)
            return UNRECORDED, 0
        return NOT_ASKED, 0
    label = f"{ticker} thesis"
    answer: "Completion | BaseException"
    try:
        with llm.call_label(label):
            answer = shared.provider.complete_detailed(
                SYSTEM_PROMPT, user_prompt(ticker, entry, headlines), SCHEMA,
                model=llm.MODEL, effort=shared.ask_effort, check=parse_check,
            )
    except Exception as exc:  # noqa: BLE001 - a call that broke is a failed check
        answer = exc
    asks, cost = shared.ledger.charge(label, answer)
    shared.guard.settle(cost)
    verdict, reason, error = read_answer(ticker, answer)
    if error is not None:
        log.error("%s: %s", label, error)
    now = utc_now()
    try:
        shared.writer.write(thesis_line(ticker, now, shared.week, entry=entry, headline_count=len(headlines),
                                        verdict=verdict, reason=reason, asks=asks, cost_usd=cost,
                                        setup=shared.setup, effort=shared.effort, error=error), now)
    except Exception:  # noqa: BLE001 - one line must not end the run
        log.exception("%s: could not write its line", ticker)
        return UNRECORDED, asks
    return (CHECKED if error is None else FAILED), asks


def _check_name(job: tuple[str, Entry, tuple[str, ...]], shared: _Shared) -> tuple[str, int]:
    """One name, start to end. Never raises: one name must not end the run."""
    try:
        return _check(*job, shared)
    except Exception:  # noqa: BLE001
        log.exception("%s: unexpected failure; no line written", job[0])
        return UNRECORDED, 0


# --------------------------------------------------------------------------- #
# The run
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ThesisRun:
    """What one run did. ``summary()`` is the one JSON line the CLI prints."""

    day: date
    ran: bool
    reason: Optional[str] = None
    week: Optional[str] = None
    check_day: Optional[date] = None
    #: Names due today; of those, checked, failed, with no entry record, not started.
    names: int = 0
    checked: int = 0
    failed: int = 0
    no_entry: int = 0
    not_asked: int = 0
    unrecorded: int = 0
    asks: int = 0
    #: The week's total so far, as the cap counts it.
    cost_usd: float = 0.0
    cap_usd: float = tc.WEEKLY_COST_CAP_USD
    #: The state: the week's total, with the estimates held, is at the cap.
    cap_reached: bool = False
    #: Names the cap stopped in this run, and whether a line of this week
    #: already said the cap stopped one, so ``cap_stopped`` fires once a week.
    cap_refused: int = 0
    cap_noted_before: bool = False
    error: Optional[str] = None

    @property
    def cap_stopped(self) -> bool:
        """The cap stopped a name in this run, and in no earlier run this week: the phone is told once a week."""
        return self.cap_refused > 0 and not self.cap_noted_before

    @property
    def estimated_usd(self) -> float:
        """The expected cost of the names this run was given, at the estimate."""
        return round(self.names * tc.ESTIMATED_COST_PER_CALL_USD, 4)

    @property
    def exit_code(self) -> int:
        """3 when the cap first stopped a name this week; 1 when nothing could be asked, or every asked name failed."""
        if self.error is not None:
            return EXIT_FAILED
        if self.cap_stopped:
            return EXIT_CAP_REACHED
        if self.checked == 0 and self.failed > 0:
            return EXIT_FAILED
        return EXIT_OK

    def summary(self) -> dict[str, Any]:
        return {
            "date": self.day.isoformat(),
            "ran": self.ran,
            "reason": self.reason,
            "week": self.week,
            "check_day": self.check_day.isoformat() if self.check_day is not None else None,
            "names": self.names,
            "checked": self.checked,
            "failed": self.failed,
            "no_entry": self.no_entry,
            "not_asked": self.not_asked,
            "unrecorded": self.unrecorded,
            "asks": self.asks,
            "cost_usd": round(self.cost_usd, 6),
            "cap_usd": self.cap_usd,
            "cap_reached": self.cap_reached,
            "cap_stopped": self.cap_stopped,
            "estimated_usd": self.estimated_usd,
            "error": self.error,
        }


def check_theses(
    *,
    journal_dir: Path | str | None = None,
    audit_path: Path | str | None = None,
    capture_dir: Path | str | None = None,
    run_id: str = "local",
    workers: Optional[int] = None,
    cap_usd: Optional[float] = None,
    budget_seconds: float = RUN_BUDGET_SECONDS,
) -> ThesisRun:
    """Check every name due today, if today is a day to; write one line per name.

    Does nothing at all (no file read, no call) when ``why_not`` gives a
    reason. Every ask is captured under ``capture_dir`` (default
    ``cfg.MODEL_IO_DIR``) and charged to the week's cap.
    """
    started = _utc(utc_now())
    day = started.date()
    reason = _reason(started)
    if reason is not None:
        log.info("thesis check not run: %s", reason)
        return ThesisRun(day=day, ran=False, reason=reason)

    directory = Path(tc.JOURNAL_DIR if journal_dir is None else journal_dir)
    cap = tc.WEEKLY_COST_CAP_USD if cap_usd is None else cap_usd
    workers = WORKERS if workers is None else workers
    week = week_of(day)
    seen = week_lines(directory, week, day)
    due = due_names(day, seen)
    guard = CostGuard(cap, seen.spent_usd, per_call_usd=tc.ESTIMATED_COST_PER_CALL_USD)
    base = dict(day=day, ran=True, week=week, check_day=due.check_day, names=len(due.names), cap_usd=cap,
                cap_noted_before=seen.cap_noted)
    if not due.names:
        return ThesisRun(**base, cost_usd=guard.spent_usd, cap_reached=guard.cap_reached)
    try:
        provider = heartbeat.full_model_provider()
        ask_effort = heartbeat.full_model_effort()
    except LLMError as exc:
        log.error("no full model to ask: %s", exc)
        return ThesisRun(**base, not_asked=len(due.names), cost_usd=guard.spent_usd,
                         error=f"no full model to ask: {exc}")

    writer = LineWriter(directory)
    setup = heartbeat.model_setup()
    effort = llm.configured_effort()
    opened = latest_entries(started, audit_path)
    jobs: list[tuple[str, Entry, tuple[str, ...]]] = []
    outcomes: Counter = Counter()
    asks = 0
    for ticker in due.names:
        headlines = due.headlines.get(ticker, ())
        entry = opened.get(ticker)
        if entry is not None:
            jobs.append((ticker, entry, headlines))
            continue
        now = utc_now()
        try:
            writer.write(thesis_line(ticker, now, week, entry=None, headline_count=len(headlines), setup=setup,
                                     effort=effort, error=NO_ENTRY), now)
            outcomes[NO_ENTRY] += 1
        except Exception:  # noqa: BLE001 - one line must not end the run
            log.exception("%s: could not write its line", ticker)
            outcomes[UNRECORDED] += 1

    shared = _Shared(provider=provider, ask_effort=ask_effort, guard=guard,
                     ledger=CaptureLedger(tc.ESTIMATED_COST_PER_CALL_USD), writer=writer, week=week,
                     setup=setup, effort=effort, deadline=time.monotonic() + budget_seconds, day=day)
    if jobs:
        log.info("thesis check %s: %d name(s) to check (check day %s), $%.4f spent so far this week of a "
                 "$%.2f cap", week, len(jobs), due.check_day, seen.spent_usd, cap)
        capture = Path(cfg.MODEL_IO_DIR if capture_dir is None else capture_dir)
        with model_io.capture(capture, run_id=f"thesis-{run_id}"):
            with ThreadPoolExecutor(max_workers=max(1, min(workers, len(jobs)))) as pool:
                for outcome, made in pool.map(lambda job: _check_name(job, shared), jobs):
                    outcomes[outcome] += 1
                    asks += made

    run = ThesisRun(
        **base,
        checked=outcomes[CHECKED],
        failed=outcomes[FAILED],
        no_entry=outcomes[NO_ENTRY],
        not_asked=outcomes[NOT_ASKED],
        unrecorded=outcomes[UNRECORDED],
        asks=asks,
        cost_usd=guard.spent_usd,
        cap_reached=guard.cap_reached,
        cap_refused=guard.refused,
    )
    log.info("thesis check: %s", json.dumps(run.summary(), sort_keys=True))
    return run


# --------------------------------------------------------------------------- #
# Command line
# --------------------------------------------------------------------------- #


def _run_id(text: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", text):
        raise argparse.ArgumentTypeError("letters, digits, '-' and '_' only, at most 64")
    return text


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m orchestrator.thesis",
        description="Check the theses of the held names, once a week (log only: nothing is traded).",
    )
    parser.add_argument("--check", action="store_true",
                        help="only say whether it would run today, and why not; asks nothing")
    parser.add_argument("--capture", type=Path, default=None,
                        help="where this run's model calls are captured (default: logs/model_io)")
    parser.add_argument("--run-id", type=_run_id, default="local",
                        help="this run's id, in the capture file's name")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if args.check:
        print(json.dumps(check(), sort_keys=True))
        return EXIT_OK
    run = check_theses(capture_dir=args.capture, run_id=args.run_id)
    print(json.dumps(run.summary(), sort_keys=True))
    return run.exit_code


__all__ = [
    "BIAS_SIDES",
    "CHECKED",
    "Due",
    "ENTRY_EVENT",
    "ERROR_MAX_CHARS",
    "EXIT_CAP_REACHED",
    "EXIT_FAILED",
    "EXIT_OK",
    "Entry",
    "FAILED",
    "NONE_RECORDED",
    "NOT_ASKED",
    "NOT_ASKED_CAP",
    "NO_ENTRY",
    "NO_HEADLINES",
    "NO_NEW_NAME_AFTER_UTC",
    "RUN_BUDGET_SECONDS",
    "SCHEMA",
    "SIDES",
    "SYSTEM_PROMPT",
    "ThesisCheck",
    "ThesisRun",
    "UNRECORDED",
    "USER_PROMPT_TAIL",
    "WORKERS",
    "WeekLines",
    "check",
    "check_theses",
    "due_names",
    "entry_from_audit",
    "latest_entries",
    "main",
    "parse_check",
    "production_ran",
    "read_answer",
    "thesis_line",
    "too_late",
    "user_prompt",
    "utc_now",
    "waiting_for_production",
    "week_lines",
    "week_of",
    "why_not",
]


if __name__ == "__main__":
    raise SystemExit(main())
