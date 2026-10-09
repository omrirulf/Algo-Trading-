"""Score the shadow stock universe once a trading day. Shadow only: nothing is traded.

Why (the owner's instruction of 2 Oct 2026, item 5). The IC report from item 4
judges the model's scores by rank against the next sessions' returns, and 80
production names a day is a small sample for that. So about 250 more names
(``config/shadow_universe.py``) are scored every trading day by the same
model, with the same settings and the same prompt as production, one call per
name, and written to their own journal for the IC report. They are never
traded.

The same path as production, step by step. For each name this module calls
the production functions in ``orchestrator.heartbeat`` and nothing else, with
one exception: the context is ``orchestrator.universe_news.build_context``,
which is ``heartbeat.build_context`` (news, technicals, fundamentals,
analysts, insiders, earnings, the keyed sources) with the universe's own
news query, company name plus ticker (the owner's decision of 3 Oct 2026;
production's query is unchanged). Then ``system_prompt_for`` and
``build_user_prompt`` (the same texts, so the same prompt fingerprint),
``call_llm`` through the same ``_ask`` and ``call_label`` wrapper the cycle
uses, ``parse_signal`` and ``scores_without_a_source``; the learned blend (the
weights read once per run, like the cycle) and the rule arms are computed by
``orchestrator/journal.py`` (``journal.universe_records``), exactly as it
computes them for a production line. The model's key reaches the call only through
heartbeat's own functions; this module reads no key itself.

What it never does. No signal goes to the engine: there is no dispatcher
here, no broker, no order, and no line in the production journal
(``journal.record`` is never called). The screen is not used: every name gets
the full model, once. The live price reader is not imported. The blend's and
the arms' records are written down here and read by nothing.
``tests/test_shadow_universe.py`` checks all of this by reading this file.

Its own journal. One JSON line per name per day in
``logs/shadow_universe/YYYY-MM.log`` (``config.journal_files.month_file``),
appended. The line format is shared with the IC report. To keep the
repository small (250 names is three times the production journal), the
line's ``context`` keeps the structured sections and the gaps but not the
news text: ``headline_count`` says how many headlines the model saw.

The cost cap. At most ``DAILY_COST_CAP_USD`` ($1.50) per UTC day for the
model and the Bright Data news searches together (the owner's instruction of
3 Oct 2026). The running total starts from the lines already written today
and adds each call's measured ``usage.cost_usd`` and each news request at
``NEWS_USD_PER_REQUEST`` (counted by ``orchestrator.news.requests_sent`` and
written on the line as ``news_requests``). Before each name and each new call
the total is checked; at the cap no new name starts and the run ends with
``cap_reached`` (exit code 3, so the workflow can alert the owner's phone). Calls run four names at a time
(of those, at most two search the news at once, and a failed search is asked up to four times:
``orchestrator.universe_news``, the owner's decision of 6 Oct 2026), so the check-and-reserve is done
under a lock, and calls already in flight may finish slightly above the cap:
the summary reports the real total. An answer with no known price is charged
at the estimate, and so is a call that failed with no usage (it is billed for
what it generated), so neither can hide spending from the cap. Before the
cap, when the day's total passes ``DAILY_COST_WARN_USD`` ($1.20) during a
run, the summary says ``warn_crossed`` and the workflow tells the owner's
phone (the owner's decision of 3 Oct 2026); the run goes on.

Off until 2027-01-01. Nothing happens unless ``SHADOW_UNIVERSE_ENABLED`` is
on, today (UTC) is on or after ``START``, and today is a trading day
(``config.market_calendar``). Two more conditions keep a run in its place on
the day: it is before ``NO_NEW_NAME_AFTER_UTC`` (23:15 UTC, so no line is
dated the next day), and the production journal already holds today's cycle
(so the universe never asks the model provider at the same time as
production, and no catch-up cycle starts once it runs). ``--check`` says
which one stops it.
"""

from __future__ import annotations

import argparse
import functools
import json
import logging
import sys
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, datetime, time as clock_time, timezone
from pathlib import Path
from typing import Any, Final, Mapping, Optional, Sequence

from pydantic import ValidationError

from analysis.cycle_day import cycle_ran_on
from analysis.reader import read_journal
from app.schemas import LLMSignal
from config import journal_files
from config import settings as cfg
from config import shadow_universe as su
from config.market_calendar import is_trading_day
from orchestrator import blend, heartbeat, journal, llm, news, universe_news
from orchestrator.context import TickerContext
from orchestrator.llm import Completion, LLMError
from orchestrator.pricing import Usage

log = logging.getLogger("universe")

#: The ``universe`` field on every line this module writes.
UNIVERSE: Final[str] = "shadow"

#: The ``event`` field on every line this module writes.
EVENT: Final[str] = "shadow_universe_scored"

#: Names scored at the same time. Production's full-model setting
#: (``FULL_MODEL_MAX_CONCURRENCY``, four, measured against the provider's
#: rate limit), so the universe asks the provider no harder than the cycle
#: does. Each worker gathers one name's context and asks its one call. The
#: shared context provider's caches are plain dictionaries: two workers
#: filling the same entry at once only fetch it twice, which is harmless.
WORKERS: Final[int] = cfg.FULL_MODEL_MAX_CONCURRENCY

#: No new name is started after this many seconds, so a slow day still ends
#: inside the workflow's clock with its lines committed. 251 names, four at a
#: time, take about 190 to 205 minutes on a typical day and 222 on the slowest
#: day measured (production's cycles of 23 Sep to 2 Oct 2026: 196 and 212
#: seconds a name per worker).
RUN_BUDGET_SECONDS: Final[float] = 240 * 60

#: No new name is started at or after this UTC time, and a run that starts
#: after it asks nothing. Each line is dated by the UTC time it is written,
#: and the IC report enters a line at the open after that date, so a name
#: asked after midnight would be dated the next day: missing from its own
#: day's cross-section, and counted as the next day's answer. GitHub's crons
#: in this repository arrive hours late (``heartbeat.yml``), so a run can
#: reach midnight. 23:15 leaves room for the slowest name (a context gather
#: plus two full-length model attempts, about 37 minutes) to finish before
#: midnight.
NO_NEW_NAME_AFTER_UTC: Final[clock_time] = clock_time(23, 15)

#: What one name is expected to cost: the day's estimate shared over the
#: list. Held in reserve for each call in flight, and charged for an answer
#: whose price is unknown.
ESTIMATED_COST_PER_NAME_USD: Final[float] = su.ESTIMATED_DAILY_MODEL_COST_USD / len(su.TICKERS)

#: What one Bright Data news request is charged to the cap (``config.shadow_universe``).
NEWS_USD_PER_REQUEST: Final[float] = su.NEWS_USD_PER_REQUEST

#: What one name's news is expected to cost: the day's news estimate shared over the list. For the summary only.
ESTIMATED_NEWS_PER_NAME_USD: Final[float] = su.ESTIMATED_DAILY_NEWS_COST_USD / len(su.TICKERS)

#: The context sections kept on each line: the structured ones the scores
#: are read from (and that ``analysis.reader`` checks to tell a null score
#: from a missing source) and the gaps. The news text (``headlines`` and
#: ``sources``) is left off to keep the repository small; the line says how
#: many headlines there were instead.
CONTEXT_KEPT: Final[tuple[str, ...]] = (
    "ticker", "technicals", "fundamentals", "analysts", "insiders", "earnings", "gaps",
)

#: Exit codes of ``python -m orchestrator.universe``.
EXIT_OK: Final[int] = 0
EXIT_FAILED: Final[int] = 1
EXIT_CAP_REACHED: Final[int] = 3

#: What became of one name in a run.
ANSWERED: Final[str] = "answered"
NOT_ASKED: Final[str] = "not asked"
CONTEXT_FAILED: Final[str] = heartbeat.CONTEXT_FAILED
MODEL_FAILED: Final[str] = heartbeat.MODEL_FAILED
UNRECORDED: Final[str] = "unrecorded"


def utc_now() -> datetime:
    """Now, in UTC. A function so a test can freeze the clock."""
    return datetime.now(timezone.utc)


# --------------------------------------------------------------------------- #
# Would it run today?
# --------------------------------------------------------------------------- #


def why_not(day: date) -> Optional[str]:
    """Why the universe is not scored on ``day`` (a UTC date), or None when it is.

    Read from ``config.shadow_universe`` at call time, in this order: the
    flag, the start date, the NYSE calendar.
    """
    if not su.SHADOW_UNIVERSE_ENABLED:
        return "the flag SHADOW_UNIVERSE_ENABLED is off"
    if day < su.START:
        return f"{day.isoformat()} is before the start date {su.START.isoformat()}"
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
    """Whether the production journal (``cfg.SIGNAL_JOURNAL_PATH``) has a cycle on ``day``.

    The same evidence the production guard reads (``analysis.cycle_day``):
    once a cycle is journalled, no catch-up cycle starts that day, so the
    universe, which waits for it, never asks the model provider at the same
    time as production. An unreadable journal counts as no cycle.
    """
    try:
        return cycle_ran_on(read_journal(cfg.SIGNAL_JOURNAL_PATH).entries, day)
    except (OSError, ValueError):
        return False


def waiting_for_production(day: date) -> Optional[str]:
    """The reason to wait for production on ``day``, or None once its cycle is journalled."""
    if production_ran(day):
        return None
    return (f"no production cycle is journalled for {day.isoformat()} yet: the universe waits for it, "
            "so the two never ask the model provider at the same time")


def _reason(moment: datetime) -> Optional[str]:
    """Every reason not to start at ``moment``, in order; None when it may."""
    day = moment.date()
    return why_not(day) or too_late(moment) or waiting_for_production(day)


def check(now: Optional[datetime] = None) -> dict[str, Any]:
    """``{"date", "run", "reason"}`` for today (UTC). Asks nothing, writes nothing."""
    moment = _utc(now or utc_now())
    reason = _reason(moment)
    return {"date": moment.date().isoformat(), "run": reason is None, "reason": reason}


def _utc(moment: datetime) -> datetime:
    return moment.replace(tzinfo=timezone.utc) if moment.tzinfo is None else moment.astimezone(timezone.utc)


# --------------------------------------------------------------------------- #
# The day's spending, and the cap
# --------------------------------------------------------------------------- #


def charged_usd(usage: Any, per_name_usd: float = ESTIMATED_COST_PER_NAME_USD, *,
                asked: bool = False) -> float:
    """What one line's call counts against the cap, from its ``usage`` record.

    The measured ``cost_usd`` when there is one; the estimate when the call
    was recorded but could not be priced (so a missing price row cannot
    blind the cap). With no usage at all: the estimate when the model was
    ``asked`` (a call that timed out or failed is still billed for what it
    generated, ``orchestrator/llm.py``), nothing when it was not.
    """
    if not isinstance(usage, Mapping):
        return per_name_usd if asked else 0.0
    cost = usage.get("cost_usd")
    if isinstance(cost, (int, float)) and not isinstance(cost, bool) and cost >= 0:
        return float(cost)
    return per_name_usd


@dataclass(frozen=True)
class DayLines:
    """What the lines already written today say."""

    #: Model cost so far today, as ``charged_usd`` counts it.
    spent_usd: float = 0.0
    #: Names with an answered line today: they are not asked again.
    answered: frozenset[str] = frozenset()


def _line_day(payload: Mapping[str, Any]) -> Optional[date]:
    raw = payload.get("ts_utc")
    if not isinstance(raw, str):
        return None
    try:
        return _utc(datetime.fromisoformat(raw)).date()
    except ValueError:
        return None


def news_charged_usd(requests: Any) -> float:
    """What a line's news searches count against the cap: ``news_requests`` at ``NEWS_USD_PER_REQUEST``."""
    if isinstance(requests, bool) or not isinstance(requests, int) or requests < 0:
        return 0.0
    return requests * NEWS_USD_PER_REQUEST


def _was_asked(payload: Mapping[str, Any]) -> bool:
    """Whether a line's name reached the model: every line but a context-stage failure."""
    return payload.get("stage") != CONTEXT_FAILED


def day_lines(directory: Path | str, day: date) -> DayLines:
    """Read today's lines from the month's file in ``directory``. Never raises on a bad line."""
    path = journal_files.month_file(directory, datetime(day.year, day.month, day.day, tzinfo=timezone.utc))
    if not path.is_file():
        return DayLines()
    spent = 0.0
    answered: set[str] = set()
    for raw in journal_files.iter_lines(path):
        try:
            payload = json.loads(raw)
        except ValueError:
            continue
        if not isinstance(payload, dict) or _line_day(payload) != day:
            continue
        spent += charged_usd(payload.get("usage"), asked=_was_asked(payload))
        spent += news_charged_usd(payload.get("news_requests"))
        ticker = payload.get("ticker")
        if isinstance(ticker, str) and payload.get("signal") is not None and payload.get("error") is None:
            answered.add(ticker)
    return DayLines(spent, frozenset(answered))


class CostGuard:
    """The day's cost, model and news, against the cap, safe to share between threads.

    ``reserve`` is the check before a call: under the lock it refuses once
    the money spent plus the estimate held for calls in flight has reached
    the cap, and otherwise holds one estimate for the new call. ``settle``
    swaps that estimate for what the call really cost. ``charge_news`` adds a
    name's news requests as they are made. A call in flight always finishes,
    so the real total can end slightly above the cap.
    """

    def __init__(self, cap_usd: float, spent_usd: float = 0.0,
                 per_name_usd: float = ESTIMATED_COST_PER_NAME_USD) -> None:
        self.cap_usd = cap_usd
        self._per_name = per_name_usd
        self._spent = max(0.0, spent_usd)
        self._held = 0.0
        self._asked = 0
        self._news_requests = 0
        self._news_usd = 0.0
        self._stopped = False
        self._lock = threading.Lock()

    def _full(self) -> bool:
        if self._spent + self._held >= self.cap_usd:
            self._stopped = True
            return True
        return False

    def has_room(self) -> bool:
        """Whether a new name may still be started (checked before its context is gathered)."""
        with self._lock:
            return not self._full()

    def reserve(self) -> bool:
        """Check and hold room for one call; False once the cap is reached."""
        with self._lock:
            if self._full():
                return False
            self._held += self._per_name
            self._asked += 1
            return True

    def settle(self, cost_usd: float) -> None:
        """Replace one call's held estimate with what it really cost."""
        with self._lock:
            self._held = max(0.0, self._held - self._per_name)
            self._spent += max(0.0, cost_usd)

    def charge_news(self, requests: int) -> None:
        """Add one name's news requests, at ``NEWS_USD_PER_REQUEST`` each."""
        cost = news_charged_usd(requests)
        with self._lock:
            self._news_requests += max(0, requests)
            self._news_usd += cost
            self._spent += cost

    @property
    def spent_usd(self) -> float:
        with self._lock:
            return self._spent

    @property
    def news_requests(self) -> int:
        """News requests made in this run."""
        with self._lock:
            return self._news_requests

    @property
    def news_usd(self) -> float:
        """What this run's news requests cost."""
        with self._lock:
            return self._news_usd

    @property
    def asked(self) -> int:
        with self._lock:
            return self._asked

    @property
    def cap_reached(self) -> bool:
        with self._lock:
            return self._stopped or self._spent >= self.cap_usd


# --------------------------------------------------------------------------- #
# The line
# --------------------------------------------------------------------------- #


def compact_context(context: TickerContext) -> dict[str, Any]:
    """The context as the line keeps it: ``CONTEXT_KEPT`` plus ``headline_count``."""
    full = context.as_dict()
    kept = {key: full.get(key) for key in CONTEXT_KEPT}
    kept["headline_count"] = len(context.headlines)
    return kept


def journal_line(
    context: TickerContext,
    now: datetime,
    *,
    signal: Optional[LLMSignal] = None,
    weights: Any = None,
    usage: Optional[Usage] = None,
    error: Optional[str] = None,
    stage: Optional[str] = None,
    setup: Optional[dict[str, Any]] = None,
    effort: Optional[str] = None,
    news_requests: int = 0,
) -> dict[str, Any]:
    """One line of the shadow universe's journal (the format the IC report reads).

    ``signal``, ``blend`` and ``arms`` are exactly what a production line
    carries; the journal computes the last two (``journal.universe_records``)
    from the same context, day and blend weights, as ``journal.record`` does. ``stage`` is ``"context"`` when the
    name failed before the model was asked, as on a production line.
    """
    now = _utc(now)
    shadow = journal.universe_records(context, signal, weights, now)
    return {
        "ts_utc": now.isoformat(),
        "ticker": context.ticker,
        "universe": UNIVERSE,
        "signal": signal.model_dump(mode="json") if signal is not None else None,
        "blend": shadow["blend"],
        "arms": shadow["arms"],
        "context": compact_context(context),
        "usage": usage.as_dict() if usage is not None else None,
        "news_requests": news_requests,
        "error": error,
        "stage": stage,
        "held": False,
        "screening": False,
        "model_setup": setup,
        "reasoning_effort": effort,
        "event": EVENT,
    }


class LineWriter:
    """Appends lines to the month's file in one directory, one thread at a time."""

    def __init__(self, directory: Path | str) -> None:
        self.directory = Path(directory)
        self._lock = threading.Lock()

    def write(self, line: Mapping[str, Any], when: datetime) -> Path:
        text = json.dumps(line, default=str) + "\n"
        with self._lock:
            self.directory.mkdir(parents=True, exist_ok=True)
            path = journal_files.month_file(self.directory, _utc(when))
            with path.open("a", encoding="utf-8") as handle:
                handle.write(text)
        return path


# --------------------------------------------------------------------------- #
# One name
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class _Shared:
    """What every worker of one run reads."""

    guard: CostGuard
    writer: LineWriter
    weights: blend.LoadedWeights
    setup: Optional[dict[str, Any]]
    effort: Optional[str]
    deadline: float
    #: The run's UTC day: no name is started once the clock has left it.
    day: date


def _write(shared: _Shared, context: TickerContext, *, signal: Optional[LLMSignal] = None,
           usage: Optional[Usage] = None, error: Optional[str] = None, stage: Optional[str] = None,
           news_requests: int = 0) -> str:
    """Write the name's line and say what became of the name."""
    now = utc_now()
    try:
        line = journal_line(context, now, signal=signal, weights=shared.weights, usage=usage,
                            error=error, stage=stage, setup=shared.setup, effort=shared.effort,
                            news_requests=news_requests)
        shared.writer.write(line, now)
    except Exception:  # noqa: BLE001 - one name's line must not end the run
        log.exception("%s: could not write its line", context.ticker)
        return UNRECORDED
    if signal is not None and error is None:
        return ANSWERED
    return CONTEXT_FAILED if stage == CONTEXT_FAILED else MODEL_FAILED


def _judge(ticker: str, context: TickerContext, answer: "Completion | BaseException",
           shared: _Shared, news_requests: int = 0) -> str:
    """Everything after the model answered, as ``heartbeat.judge_answer`` does it, minus the engine."""
    usage = answer.usage if isinstance(answer, Completion) else None
    write = functools.partial(_write, shared, context, news_requests=news_requests)
    try:
        if isinstance(answer, BaseException):
            raise answer
        signal = heartbeat.scores_without_a_source(heartbeat.parse_signal(answer.text), context)
    except LLMError as exc:
        log.error("%s: %s", ticker, exc)
        return write(usage=usage, error=str(exc))
    except (json.JSONDecodeError, ValidationError) as exc:
        log.error("%s: model output rejected: %s", ticker, exc)
        return write(usage=usage, error=f"invalid LLM output: {exc}")
    except Exception as exc:  # noqa: BLE001
        log.exception("%s: failed to produce a signal", ticker)
        return write(usage=usage, error=f"unexpected {type(exc).__name__}: {exc}")

    if signal.ticker != ticker:
        log.error("%s: the model answered for %s instead", ticker, signal.ticker)
        return write(signal=signal, usage=usage, error=f"answered for {signal.ticker}")
    return write(signal=signal, usage=usage)


def _score(ticker: str, shared: _Shared) -> str:
    if time.monotonic() >= shared.deadline:
        return NOT_ASKED
    now = _utc(utc_now())
    if now.date() != shared.day or too_late(now) is not None:
        return NOT_ASKED
    if not shared.guard.has_room():
        return NOT_ASKED

    # The news searches are made in this thread, inside the context gather:
    # every request is charged to the cap, whatever the gather's outcome.
    before = news.requests_sent()
    try:
        context = universe_news.build_context(ticker)
    except Exception as exc:  # noqa: BLE001
        log.exception("%s: failed to gather context", ticker)
        requests = news.requests_sent() - before
        shared.guard.charge_news(requests)
        return _write(shared, TickerContext(ticker=ticker), error=str(exc) or repr(exc), stage=CONTEXT_FAILED,
                      news_requests=requests)
    requests = news.requests_sent() - before
    shared.guard.charge_news(requests)
    try:
        system_prompt = heartbeat.system_prompt_for(context.ticker, context)
        user_prompt = heartbeat.build_user_prompt(context)
    except Exception as exc:  # noqa: BLE001
        log.exception("%s: failed to render context into a prompt", ticker)
        return _write(shared, context, error=str(exc) or repr(exc), stage=CONTEXT_FAILED, news_requests=requests)

    if not shared.guard.reserve():
        # Its news is paid for: a line says so, so a re-run today counts it too.
        log.warning("%s: the day's cost cap is reached; not asked", ticker)
        _write(shared, context, error="not asked: the day's cost cap is reached", stage=CONTEXT_FAILED,
               news_requests=requests)
        return NOT_ASKED
    prepared = heartbeat.PreparedTicker(ticker, context, system_prompt, user_prompt, len(context.gaps))
    try:
        answer: "Completion | BaseException" = heartbeat._ask(heartbeat.call_llm, prepared)
    except Exception as exc:  # noqa: BLE001 - _ask hands back only the model's own failures
        answer = exc
    usage = answer.usage if isinstance(answer, Completion) else None
    shared.guard.settle(charged_usd(usage.as_dict() if usage is not None else None, asked=True))
    return _judge(ticker, context, answer, shared, requests)


def _score_name(ticker: str, shared: _Shared) -> str:
    """One name, start to end. Never raises: one name must not end the run."""
    try:
        return _score(ticker, shared)
    except Exception:  # noqa: BLE001
        log.exception("%s: unexpected failure; no line written", ticker)
        return UNRECORDED


# --------------------------------------------------------------------------- #
# The run
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class UniverseRun:
    """What one run did. ``summary()`` is the one JSON line the CLI prints."""

    day: date
    ran: bool
    reason: Optional[str] = None
    names: int = 0
    asked: int = 0
    answered: int = 0
    failed: int = 0
    not_asked: int = 0
    already_answered: int = 0
    #: The day's total so far, model and news, as the cap counts it.
    cost_usd: float = 0.0
    #: This run's news requests and what they cost (inside ``cost_usd``).
    news_requests: int = 0
    news_cost_usd: float = 0.0
    cap_usd: float = su.DAILY_COST_CAP_USD
    cap_reached: bool = False
    #: The day's total before this run, so ``warn_crossed`` fires once a day.
    spent_before_usd: float = 0.0
    warn_usd: float = su.DAILY_COST_WARN_USD
    error: Optional[str] = None

    @property
    def warn_crossed(self) -> bool:
        """The day's total passed the alert line during this run (not before it)."""
        return self.spent_before_usd < self.warn_usd <= self.cost_usd

    @property
    def estimated_usd(self) -> float:
        """The expected cost of the names this run was given, model and news."""
        return round(self.names * (ESTIMATED_COST_PER_NAME_USD + ESTIMATED_NEWS_PER_NAME_USD), 4)

    @property
    def exit_code(self) -> int:
        """3 when the cap stopped the run; 1 when nothing could be asked or every asked name failed."""
        if self.error is not None:
            return EXIT_FAILED
        if self.cap_reached:
            return EXIT_CAP_REACHED
        if self.ran and self.answered == 0 and self.failed > 0:
            return EXIT_FAILED
        return EXIT_OK

    def summary(self) -> dict[str, Any]:
        return {
            "date": self.day.isoformat(),
            "ran": self.ran,
            "reason": self.reason,
            "names": self.names,
            "asked": self.asked,
            "answered": self.answered,
            "failed": self.failed,
            "not_asked": self.not_asked,
            "already_answered": self.already_answered,
            "cost_usd": round(self.cost_usd, 6),
            "news_requests": self.news_requests,
            "news_cost_usd": round(self.news_cost_usd, 6),
            "cap_usd": self.cap_usd,
            "cap_reached": self.cap_reached,
            "warn_usd": self.warn_usd,
            "warn_crossed": self.warn_crossed,
            "estimated_usd": self.estimated_usd,
            "error": self.error,
        }


def score_universe(
    tickers: Optional[Sequence[str]] = None,
    *,
    journal_dir: Path | str | None = None,
    limit: Optional[int] = None,
    workers: Optional[int] = None,
    cap_usd: Optional[float] = None,
    budget_seconds: float = RUN_BUDGET_SECONDS,
) -> UniverseRun:
    """Score every due name once, if today is a day to; write one line per name asked.

    Does nothing at all (no file read, no context, no call) when ``why_not``
    gives a reason. Otherwise reads today's lines, skips the names already
    answered today, and asks the rest, ``workers`` (default ``WORKERS``) at a
    time, until the list, the cap or the time budget runs out.
    """
    started = _utc(utc_now())
    day = started.date()
    reason = _reason(started)
    if reason is not None:
        log.info("shadow universe not scored: %s", reason)
        return UniverseRun(day=day, ran=False, reason=reason)

    names = tuple(su.TICKERS if tickers is None else tickers)
    workers = WORKERS if workers is None else workers
    if limit is not None:
        names = names[:max(0, limit)]
    directory = Path(su.JOURNAL_DIR if journal_dir is None else journal_dir)
    cap = su.DAILY_COST_CAP_USD if cap_usd is None else cap_usd

    today = day_lines(directory, day)
    due = tuple(t for t in names if t not in today.answered)
    guard = CostGuard(cap, today.spent_usd)
    base = dict(day=day, ran=True, names=len(names), already_answered=len(names) - len(due), cap_usd=cap,
                spent_before_usd=today.spent_usd)
    if not due or not guard.has_room():
        return UniverseRun(**base, not_asked=len(due), cost_usd=guard.spent_usd,
                           cap_reached=guard.cap_reached)

    # Checked once, before any context is gathered: a missing model key is
    # every name's failure, and finding it out 250 news fetches later would
    # be paying for nothing.
    try:
        heartbeat.full_model_provider()
    except LLMError as exc:
        log.error("no full model to ask: %s", exc)
        return UniverseRun(**base, not_asked=len(due), cost_usd=guard.spent_usd,
                           error=f"no full model to ask: {exc}")

    shared = _Shared(
        guard=guard,
        writer=LineWriter(directory),
        weights=blend.load_weights(model=llm.MODEL),
        setup=heartbeat.model_setup(),
        effort=llm.configured_effort(),
        deadline=time.monotonic() + budget_seconds,
        day=day,
    )
    log.info("shadow universe: %d name(s) due, %d already answered today, %d at a time, "
             "$%.4f spent so far today of a $%.2f cap",
             len(due), len(names) - len(due), workers, today.spent_usd, cap)
    with ThreadPoolExecutor(max_workers=max(1, min(workers, len(due)))) as pool:
        outcomes = Counter(pool.map(lambda ticker: _score_name(ticker, shared), due))

    run = UniverseRun(
        **base,
        asked=guard.asked,
        answered=outcomes[ANSWERED],
        failed=outcomes[CONTEXT_FAILED] + outcomes[MODEL_FAILED] + outcomes[UNRECORDED],
        not_asked=outcomes[NOT_ASKED],
        cost_usd=guard.spent_usd,
        news_requests=guard.news_requests,
        news_cost_usd=guard.news_usd,
        cap_reached=guard.cap_reached,
    )
    log.info("shadow universe: %s", json.dumps(run.summary(), sort_keys=True))
    return run


# --------------------------------------------------------------------------- #
# Command line
# --------------------------------------------------------------------------- #


def _positive_int(text: str) -> int:
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("must be 1 or more")
    return value


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m orchestrator.universe",
        description="Score the shadow stock universe once (shadow only: nothing is traded).",
    )
    parser.add_argument("--check", action="store_true",
                        help="only say whether it would run today, and why not; asks nothing")
    parser.add_argument("--limit", type=_positive_int, default=None,
                        help="score only the first N names of the list")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if args.check:
        print(json.dumps(check(), sort_keys=True))
        return EXIT_OK
    run = score_universe(limit=args.limit)
    print(json.dumps(run.summary(), sort_keys=True))
    return run.exit_code


__all__ = [
    "ANSWERED",
    "CONTEXT_FAILED",
    "CONTEXT_KEPT",
    "CostGuard",
    "DayLines",
    "ESTIMATED_COST_PER_NAME_USD",
    "ESTIMATED_NEWS_PER_NAME_USD",
    "EVENT",
    "EXIT_CAP_REACHED",
    "EXIT_FAILED",
    "EXIT_OK",
    "LineWriter",
    "MODEL_FAILED",
    "NEWS_USD_PER_REQUEST",
    "NOT_ASKED",
    "NO_NEW_NAME_AFTER_UTC",
    "RUN_BUDGET_SECONDS",
    "UNIVERSE",
    "UNRECORDED",
    "UniverseRun",
    "WORKERS",
    "charged_usd",
    "check",
    "compact_context",
    "day_lines",
    "journal_line",
    "main",
    "news_charged_usd",
    "production_ran",
    "score_universe",
    "too_late",
    "utc_now",
    "waiting_for_production",
    "why_not",
]


if __name__ == "__main__":
    raise SystemExit(main())
