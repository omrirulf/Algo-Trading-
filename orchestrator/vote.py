"""The voting arm ``model_vote``: four more calls of the production model on each answered line. Shadow only.

Why (the owner's instruction of 4 Oct 2026, item 1). One call of the model
is one draw: asked the same question again, the same model can answer
differently. So every answered production line gets four more calls, with
the same model, the same settings and the same input, and the five answers
vote. The rule is fixed in ``config/model_vote.py`` and applied by
``analysis/vote.py``: at least 3 of the 5 votes must succeed, the side
needs at least 3 of the 5, a tie is NEUTRAL. The race arm and the fund that
read the votes are shadow only. Nothing here is ever traded.

The same input, proved. Each vote re-sends the archived request of the
production line's first ask: the heartbeat's capture of that call
(``orchestrator/model_io.py``), downloaded from the production run's
artifact (``--model-io``). Before any call, the body production's call path
would send today is rebuilt from the archived prompts
(``OpenAICompatibleProvider.request_body``), and its SHA-256 is compared with
the one on the production line. Equal means the same model, the same
reasoning level, the same answer schema and the same prompt. Anything else,
and the line is written with the reason and nothing is asked. The four calls
then go through ``heartbeat.call_llm``, production's own call path, so its
retries and re-asks are production's. Each answer is read with
``heartbeat.parse_signal`` and ``scores_without_a_source``, against the
production line's own context. No context is gathered and no news is fetched.

What it never does. No signal goes to the engine: there is no dispatcher
here, no broker, no order, and no line in the production journal
(``journal.record`` is never called). The model's key reaches the call only
through heartbeat's own functions; this module reads no key itself. Its
lines go to ``logs/model_vote/``, one per production line, one file per UTC
month. ``tests/test_model_vote_runner.py`` checks all of this by reading this
file.

Timing. The vote runs in the shadow-universe workflow, in the run's first
job, once the day's production run has finished; the universe's job waits
for it (the owner's order of 6 Oct 2026: production, the vote, the
universe, so a late day reaches the cut-off in the universe, not here). So
it never runs at the same time as either of them, and the model provider is
never asked by two of them at once. No new name is started from 23:15 UTC,
so no line is dated the next day. A name, once started, gets its four calls.

Every answered line is recorded or counted (pre-registration section 13.11).
A name the cut-off stops gets its line all the same, with vote 1 only, no
call, and the reason (``analysis.vote.NOT_ASKED_LATE``); so does a name the
day's cost cap stops (``NOT_ASKED_CAP``). Both are final, like a line with
no archived input. A name the run's time budget stops, or one the clock
reaches after midnight, gets no line: a later run today may still vote the
first, and the second would be dated the next day. A line with no vote line
at all is counted by the nightly counters as ``missing``.

The cost cap. At most ``DAILY_COST_CAP_USD`` ($1.00) a UTC day; about $0.70
is expected. The day's total starts from the lines already written today.
Every HTTP ask is charged as the capture recorded it: retries, re-asks and
timeouts too (an ask with no price is charged the estimate). Before a name
starts, its four calls are held at the estimate; at the cap no new name
starts. The run that first stops a name at the cap today ends with exit
code 3, so the workflow tells the owner's phone, once a day: a later run
that day, which finds a cap line already written, ends with 0, and so does
a run that reaches the cap with the last name it started and stops none.
When a run takes the day past ``DAILY_COST_WARN_USD`` ($0.80), the summary
says ``warn_crossed`` and the phone is told once. The run goes on.

Off until 2026-12-22. Nothing happens unless ``MODEL_VOTE_ENABLED`` is on,
today (UTC) is on or after ``START``, and today is a trading day. Two more
conditions: it is before 23:15 UTC, and the production journal already holds
today's cycle. ``--check`` says which one stops it.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Final, Mapping, Optional, Sequence

from pydantic import ValidationError

from analysis import vote as rule
from analysis.cycle_day import cycle_ran_on
from analysis.reader import SCORE_FIELDS, SOURCE_SECTIONS, JournalEntry, entry_from, read_journal
from config import journal_files
from config import model_vote as mv
from config import settings as cfg
from config.market_calendar import is_trading_day
from orchestrator import heartbeat, llm, model_io
from orchestrator.llm import Completion, LLMError
from orchestrator.pricing import Usage

log = logging.getLogger("vote")

#: Calls asked at the same time. Production's full-model setting
#: (``FULL_MODEL_MAX_CONCURRENCY``, four, measured against the provider's
#: rate limit), so the vote asks the provider no harder than the cycle does.
WORKERS: Final[int] = cfg.FULL_MODEL_MAX_CONCURRENCY

#: The answered lines a day the cost estimate is made for (the owner's figure
#: of 4 Oct 2026: about $0.70 a day, four calls a line at the estimate).
EXPECTED_LINES: Final[int] = round(
    mv.ESTIMATED_DAILY_COST_USD / (mv.EXTRA_CALLS * mv.ESTIMATED_COST_PER_CALL_USD)
)

#: No new name is started after this many seconds, so a slow day still ends
#: inside the job's clock with its lines committed. 58 lines, four calls
#: each, four at a time, take about 140 minutes at production's median
#: answered call at high effort (146 seconds) and 205 at the universe's
#: slowest measured pace (212 seconds); ``tests/test_model_vote_runner.py``
#: keeps this and the workflow's ``timeout-minutes`` in step.
RUN_BUDGET_SECONDS: Final[float] = 210 * 60

#: Exit codes of ``python -m orchestrator.vote``.
EXIT_OK: Final[int] = 0
EXIT_FAILED: Final[int] = 1
EXIT_CAP_REACHED: Final[int] = 3

#: Why a line was written without a call. Final: such a line is never voted again.
NO_ARCHIVE: Final[str] = "no archived input for this line"
ARCHIVE_DIFFERS: Final[str] = (
    "the input differs from the archive: the model, a setting or the prompt changed since the production call"
)

#: Why a run asked nothing and wrote nothing: the production run's model
#: calls were not downloaded. A later run of the same day tries again.
NO_DOWNLOAD: Final[str] = "no archived input was downloaded"

#: Why a name was not started, when no line is written for it: the run's
#: time budget is spent (a later run today may still vote the line), or the
#: clock has left the run's UTC day (a line written now would be dated the
#: next day). The two final reasons, the cut-off and the day's cost cap, are
#: ``analysis.vote.NOT_ASKED_LATE`` and ``NOT_ASKED_CAP``: their line says so.
OUT_OF_TIME: Final[str] = "the run's time budget is spent"
DAY_OVER: Final[str] = "the clock has left the run's UTC day"

#: What became of one production line in a run.
VOTED: Final[str] = "voted"
NOT_VOTED: Final[str] = "not voted"
NOT_ASKED: Final[str] = "not asked"
UNRECORDED: Final[str] = "unrecorded"

#: The longest reason kept for a failed vote, so a line stays one short record.
ERROR_MAX_CHARS: Final[int] = 300

_RUN_ID: Final[re.Pattern[str]] = re.compile(r"[A-Za-z0-9_-]{1,64}")
_DIGITS: Final[re.Pattern[str]] = re.compile(r"[0-9]{1,20}")


def utc_now() -> datetime:
    """Now, in UTC. A function so a test can freeze the clock."""
    return datetime.now(timezone.utc)


def _utc(moment: datetime) -> datetime:
    return moment.replace(tzinfo=timezone.utc) if moment.tzinfo is None else moment.astimezone(timezone.utc)


# --------------------------------------------------------------------------- #
# Would it run today?
# --------------------------------------------------------------------------- #


def why_not(day: date) -> Optional[str]:
    """Why no line is voted on ``day`` (a UTC date), or None when it may be.

    Read from ``config.model_vote`` at call time, in this order: the flag,
    the start date, the NYSE calendar.
    """
    if not mv.MODEL_VOTE_ENABLED:
        return "the flag MODEL_VOTE_ENABLED is off"
    if day < mv.START:
        return f"{day.isoformat()} is before the start date {mv.START.isoformat()}"
    if not is_trading_day(day):
        return f"{day.isoformat()} is not a trading day"
    return None


def too_late(now: datetime) -> Optional[str]:
    """The reason no new name may be started at ``now``, or None while it still may."""
    moment = _utc(now)
    if moment.time() >= mv.NO_NEW_NAME_AFTER_UTC:
        return (f"{moment.strftime('%H:%M')} UTC is too late in the UTC day: no new name is started "
                f"from {mv.NO_NEW_NAME_AFTER_UTC.strftime('%H:%M')} UTC, so no line is dated the next day")
    return None


def production_ran(day: date) -> bool:
    """Whether the production journal (``cfg.SIGNAL_JOURNAL_PATH``) has a cycle on ``day``.

    The same evidence the production guard reads (``analysis.cycle_day``), as
    the shadow universe reads it. An unreadable journal counts as no cycle.
    """
    try:
        return cycle_ran_on(read_journal(cfg.SIGNAL_JOURNAL_PATH).entries, day)
    except (OSError, ValueError):
        return False


def waiting_for_production(day: date) -> Optional[str]:
    """The reason to wait for production on ``day``, or None once its cycle is journalled."""
    if production_ran(day):
        return None
    return (f"no production cycle is journalled for {day.isoformat()} yet: the vote waits for it, "
            "so the two never ask the model provider at the same time")


def _reason(moment: datetime) -> Optional[str]:
    """Every reason not to start at ``moment``, in order; None when it may."""
    day = moment.date()
    return why_not(day) or too_late(moment) or waiting_for_production(day)


def check(now: Optional[datetime] = None, journal_dir: Path | str | None = None) -> dict[str, Any]:
    """``{"date", "run", "reason", "runs"}`` for today (UTC). Asks nothing, writes nothing.

    ``runs`` are the production runs whose model calls the vote needs: the
    GitHub run ids of today's answered lines not yet voted, digits only,
    sorted. The workflow downloads those runs' artifacts and nothing else.
    """
    moment = _utc(now or utc_now())
    reason = _reason(moment)
    runs: list[str] = []
    if reason is None:
        directory = mv.JOURNAL_DIR if journal_dir is None else journal_dir
        runs = production_runs(due_lines(moment.date(), directory))
    return {"date": moment.date().isoformat(), "run": reason is None, "reason": reason, "runs": runs}


# --------------------------------------------------------------------------- #
# The day's production lines, and the ones already voted
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class ProductionLine:
    """One answered production line, as the journal holds it."""

    payload: Mapping[str, Any]
    entry: JournalEntry

    @property
    def ticker(self) -> str:
        return self.entry.ticker

    @property
    def key(self) -> rule.Key:
        return (self.entry.ticker, self.entry.timestamp)

    @property
    def line_ts_utc(self) -> str:
        """The line's own ``ts_utc``, exactly as written: the vote line names it by this."""
        return str(self.payload.get("ts_utc"))

    @property
    def run_id(self) -> Optional[str]:
        """The production run's GitHub id, from the line's ``run`` block, or None."""
        block = self.payload.get("run")
        value = block.get("run_id") if isinstance(block, Mapping) else None
        return value if isinstance(value, str) and value else None

    @property
    def first_call(self) -> Optional[Mapping[str, Any]]:
        """The line's first model call as the journal names it: ``{"call_id", "prompt_sha256", ...}``."""
        calls = self.payload.get("model_calls")
        if isinstance(calls, list) and calls and isinstance(calls[0], Mapping):
            return calls[0]
        return None

    @property
    def prompt_sha256(self) -> Optional[str]:
        first = self.first_call
        value = first.get("prompt_sha256") if first is not None else None
        return value if isinstance(value, str) and value else None

    @property
    def sources(self) -> SimpleNamespace:
        """The line's own context, as much of it as ``scores_without_a_source`` reads."""
        context = self.payload.get("context")
        context = context if isinstance(context, Mapping) else {}
        return SimpleNamespace(ticker=self.ticker, **{name: context.get(name) for name in SOURCE_SECTIONS})

    def production_vote(self) -> dict[str, Any]:
        """Vote 1: the production answer, as journalled."""
        return {
            "vote": 1,
            "source": "production",
            "bias": self.entry.bias,
            "conviction": self.entry.conviction,
            "scores": {name: self.entry.scores.get(name) for name in SCORE_FIELDS},
            "error": None,
        }


def production_lines(day: date) -> list[ProductionLine]:
    """``day``'s answered production lines (UTC), in journal order. Held lines are not offered.

    Read as raw JSON lines, so the line's ``model_calls`` and ``run`` are at
    hand; the race's own reader (``analysis.reader.entry_from``) decides
    what counts as answered. Never raises: an unreadable journal has no lines.
    """
    path = cfg.SIGNAL_JOURNAL_PATH
    out: list[ProductionLine] = []
    try:
        if not journal_files.exists(path):
            return out
        for raw in journal_files.iter_lines(path):
            try:
                payload = json.loads(raw)
            except ValueError:
                continue
            entry = entry_from(payload)
            if (entry is None or entry.timestamp is None or not entry.timestamp_is_exact
                    or entry.timestamp.date() != day or entry.held or not entry.model_answered):
                continue
            out.append(ProductionLine(payload, entry))
    except OSError:
        log.exception("could not read the production journal")
        return []
    return out


@dataclass(frozen=True)
class DayVotes:
    """What the vote lines already written today say."""

    #: Model cost so far today: the ``cost_usd`` of every vote line written today.
    spent_usd: float = 0.0
    #: Production lines with a vote line: final, never voted again.
    voted: frozenset = frozenset()
    #: A line written today says the day's cost cap stopped it: the phone has been told.
    cap_noted: bool = False


def _written_day(payload: Mapping[str, Any]) -> Optional[date]:
    raw = payload.get("ts_utc")
    if not isinstance(raw, str):
        return None
    try:
        return _utc(datetime.fromisoformat(raw)).date()
    except ValueError:
        return None


def _usd(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not value >= 0:
        return 0.0
    return float(value)


def day_votes(directory: Path | str, day: date) -> DayVotes:
    """Read today's vote lines from the month's file in ``directory``. Never raises on a bad line."""
    path = journal_files.month_file(directory, datetime(day.year, day.month, day.day, tzinfo=timezone.utc))
    if not path.is_file():
        return DayVotes()
    spent = 0.0
    voted: set = set()
    cap_noted = False
    for raw in journal_files.iter_lines(path):
        try:
            payload = json.loads(raw)
        except ValueError:
            continue
        if not isinstance(payload, dict) or payload.get("event") != mv.EVENT:
            continue
        if _written_day(payload) == day:
            spent += _usd(payload.get("cost_usd"))
            cap_noted = cap_noted or payload.get("error") == rule.NOT_ASKED_CAP
        line = rule.line_from(payload)
        if line is not None and line.day == day:
            voted.add(line.key)
    return DayVotes(spent, frozenset(voted), cap_noted)


def due_lines(day: date, directory: Path | str) -> list[ProductionLine]:
    """``day``'s answered production lines that have no vote line yet, in journal order."""
    voted = day_votes(directory, day).voted
    return [line for line in production_lines(day) if line.key not in voted]


def production_runs(lines: Sequence[ProductionLine]) -> list[str]:
    """The production runs behind ``lines``: GitHub run ids, digits only, sorted, each once."""
    return sorted({line.run_id for line in lines if line.run_id and _DIGITS.fullmatch(line.run_id)})


# --------------------------------------------------------------------------- #
# The archived input
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Prompt:
    """The archived prompts of a production line's first ask."""

    system: str
    user: str


def archived_calls(directory: Path | str | None) -> Optional[dict[str, dict[str, Any]]]:
    """Every call record under ``directory`` (the downloaded production artifact), by call id.

    Reads every ``*.jsonl`` file below it, at any depth, and skips a line
    that does not parse. None when there is no such file at all: the
    download failed, and nothing may be voted on.
    """
    if directory is None:
        return None
    root = Path(directory)
    if not root.is_dir():
        return None
    files = sorted(path for path in root.rglob("*.jsonl") if path.is_file())
    if not files:
        return None
    out: dict[str, dict[str, Any]] = {}
    for path in files:
        try:
            with path.open(encoding="utf-8") as handle:
                for raw in handle:
                    try:
                        item = json.loads(raw)
                    except ValueError:
                        continue
                    if isinstance(item, dict) and isinstance(item.get("call_id"), str):
                        out.setdefault(item["call_id"], item)
        except OSError:
            log.exception("could not read %s", path)
    return out


def _messages(request: str) -> Optional[Prompt]:
    try:
        body = json.loads(request)
    except ValueError:
        return None
    messages = body.get("messages") if isinstance(body, dict) else None
    if not isinstance(messages, list) or len(messages) != 2:
        return None
    system, user = messages
    if not (isinstance(system, dict) and isinstance(user, dict)
            and system.get("role") == "system" and user.get("role") == "user"
            and isinstance(system.get("content"), str) and isinstance(user.get("content"), str)):
        return None
    return Prompt(system["content"], user["content"])


def archived_prompt(line: ProductionLine, calls: Mapping[str, Mapping[str, Any]],
                    provider: Any) -> tuple[Optional[Prompt], Optional[str]]:
    """The line's archived prompts, checked to be what production's call path sends today.

    ``(prompt, None)`` when the archived first ask exists, matches the hash
    on the production line, and the body rebuilt from its prompts today has
    that same hash: the same model, the same settings, the same input.
    Otherwise ``(None, reason)``, and the line is not voted.
    """
    first = line.first_call
    expected = line.prompt_sha256
    call_id = first.get("call_id") if first is not None else None
    if not isinstance(call_id, str) or expected is None:
        return None, NO_ARCHIVE
    archived = calls.get(call_id)
    request = archived.get("request") if isinstance(archived, Mapping) else None
    if (not isinstance(request, str) or archived.get("kind") != "first"
            or model_io.sha256_text(request) != expected):
        return None, NO_ARCHIVE
    prompt = _messages(request)
    if prompt is None:
        return None, NO_ARCHIVE
    rebuild = getattr(provider, "request_body", None)
    if rebuild is None:
        return None, ARCHIVE_DIFFERS
    try:
        body = rebuild(prompt.system, prompt.user, heartbeat.SIGNAL_JSON_SCHEMA,
                       model=llm.MODEL, effort=heartbeat.full_model_effort())
    except Exception:  # noqa: BLE001 - a body that cannot be rebuilt is not the same input
        log.exception("%s: could not rebuild the production request", line.ticker)
        return None, ARCHIVE_DIFFERS
    if model_io.sha256_text(model_io.canonical(body)) != expected:
        return None, ARCHIVE_DIFFERS
    return prompt, None


# --------------------------------------------------------------------------- #
# The day's spending, and the cap
# --------------------------------------------------------------------------- #


class CostGuard:
    """The day's model cost against the cap, safe to share between threads.

    ``reserve`` is the check before a name starts: under the lock it refuses
    once the money spent plus the estimate held for calls in flight has
    reached the cap, and otherwise holds one estimate for each of the name's
    calls. ``settle`` swaps one call's estimate for what it really cost. A
    call in flight always finishes, so the real total can end slightly above
    the cap; the summary reports it. ``refused`` counts the refusals: the
    names the cap stopped in this run.
    """

    def __init__(self, cap_usd: float, spent_usd: float = 0.0,
                 per_call_usd: float = mv.ESTIMATED_COST_PER_CALL_USD) -> None:
        self.cap_usd = cap_usd
        self._per_call = per_call_usd
        self._spent = max(0.0, spent_usd)
        self._held = 0.0
        self._calls = 0
        self._refused = 0
        self._stopped = False
        self._lock = threading.Lock()

    def _full(self) -> bool:
        if self._spent + self._held >= self.cap_usd:
            self._stopped = True
            return True
        return False

    def has_room(self) -> bool:
        with self._lock:
            return not self._full()

    def reserve(self, calls: int = 1) -> bool:
        """Check, and hold room for ``calls`` calls; False once the cap is reached."""
        with self._lock:
            if self._full():
                self._refused += 1
                return False
            self._held += calls * self._per_call
            self._calls += calls
            return True

    def settle(self, cost_usd: float) -> None:
        """Replace one call's held estimate with what it really cost."""
        with self._lock:
            self._held = max(0.0, self._held - self._per_call)
            self._spent += max(0.0, cost_usd)

    @property
    def spent_usd(self) -> float:
        with self._lock:
            return self._spent

    @property
    def calls(self) -> int:
        """Calls reserved in this run."""
        with self._lock:
            return self._calls

    @property
    def refused(self) -> int:
        """``reserve`` calls refused in this run: one a name the cap stopped."""
        with self._lock:
            return self._refused

    @property
    def cap_reached(self) -> bool:
        with self._lock:
            return self._stopped or self._spent >= self.cap_usd


def ask_cost_usd(call: Mapping[str, Any], per_call_usd: float) -> float:
    """What one captured HTTP ask is charged: its tokens at the model's price, else the estimate.

    An ask with no usage (a timeout, an HTTP error) or a model with no price
    row is charged the estimate, so nothing that was billed can hide from
    the cap.
    """
    usage = call.get("usage")
    if isinstance(usage, Mapping):
        tokens_in, tokens_out = usage.get("prompt_tokens"), usage.get("completion_tokens")
        if all(isinstance(n, int) and not isinstance(n, bool) and n >= 0 for n in (tokens_in, tokens_out)):
            model = call.get("model")
            cost = Usage(model=model if isinstance(model, str) else "", input_tokens=tokens_in,
                         output_tokens=tokens_out).cost_usd
            if cost is not None:
                return cost
    return per_call_usd


class CaptureLedger:
    """This run's model-call capture, read as it grows: every HTTP ask, by its call label.

    Each ask the provider makes is one record in the capture file
    (``model_io.current_path()``), labelled with the ``call_label`` it was
    made under. Read from where the last reading stopped, and only up to the
    last complete line, so a record being written by another thread is read
    next time. Safe to share between threads.
    """

    def __init__(self, per_call_usd: float) -> None:
        self._per_call = per_call_usd
        self._lock = threading.Lock()
        self._path: Optional[Path] = None
        self._offset = 0
        self._asks: dict[str, list[float]] = {}

    def _catch_up(self) -> bool:
        path = model_io.current_path()
        if path is None or not path.is_file():
            return False
        if path != self._path:
            self._path, self._offset, self._asks = path, 0, {}
        with path.open("rb") as handle:
            handle.seek(self._offset)
            chunk = handle.read()
        end = chunk.rfind(b"\n")
        if end < 0:
            return True
        self._offset += end + 1
        for raw in chunk[:end].split(b"\n"):
            try:
                call = json.loads(raw)
            except ValueError:
                continue
            if isinstance(call, dict) and isinstance(call.get("ticker"), str):
                self._asks.setdefault(call["ticker"], []).append(ask_cost_usd(call, self._per_call))
        return True

    def asks(self, label: str, *, forget: bool = False) -> Optional[list[float]]:
        """The cost of each ask made under ``label``; None when the capture cannot be read.

        ``forget`` takes them, as ``model_io.take`` takes a line's calls: a
        later call under the same label (the same name twice in a day) is
        then charged its own asks only.
        """
        with self._lock:
            try:
                if not self._catch_up():
                    return None
            except OSError:
                log.exception("could not read the model-call capture")
                return None
            found = self._asks.pop(label, []) if forget else self._asks.get(label, [])
            return list(found)

    def charge(self, label: str, answer: "Completion | BaseException") -> tuple[int, float]:
        """``(asks, cost)`` of the call just made under ``label``: every ask the capture recorded.

        When the capture cannot be read or holds nothing for the label, the
        call counts as one ask, charged the estimate or the answer's own
        measured cost, whichever is more.
        """
        found = self.asks(label, forget=True)
        if found:
            return len(found), sum(found)
        measured = answer.usage.cost_usd if isinstance(answer, Completion) else None
        return 1, max(self._per_call, measured or 0.0)


# --------------------------------------------------------------------------- #
# The line
# --------------------------------------------------------------------------- #


def vote_line(line: ProductionLine, now: datetime, *, votes: Sequence[Mapping[str, Any]] = (),
              asks: int = 0, cost_usd: float = 0.0, error: Optional[str] = None,
              setup: Optional[dict[str, Any]] = None, effort: Optional[str] = None) -> dict[str, Any]:
    """One line of ``logs/model_vote/``: the production line's five votes, or why it was not voted.

    ``answer`` is written for the record, by ``analysis.vote.aggregate``;
    every reader makes it again from ``votes``. A line with ``error`` set
    holds only vote 1, asked nothing, and is final.
    """
    every = [line.production_vote(), *sorted(votes, key=lambda vote: vote["vote"])]
    parsed = [rule.vote_from(vote) for vote in every]
    answer = None if error is not None else rule.aggregate(v for v in parsed if v is not None)
    return {
        "ts_utc": _utc(now).isoformat(),
        "event": mv.EVENT,
        "ticker": line.ticker,
        "line_ts_utc": line.line_ts_utc,
        "run_id": line.run_id,
        "prompt_sha256": line.prompt_sha256,
        "model_setup": setup,
        "reasoning_effort": effort,
        "votes": every,
        "answer": answer.as_dict() if answer is not None else None,
        "asks": asks,
        "cost_usd": round(cost_usd, 6),
        "error": error,
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
# One name, four calls
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class _Shared:
    """What every worker of one run reads."""

    guard: CostGuard
    ledger: CaptureLedger
    writer: LineWriter
    setup: Optional[dict[str, Any]]
    effort: Optional[str]
    deadline: float
    #: The run's UTC day: no name is started once the clock has left it.
    day: date


class _Name:
    """One production line being voted on: whether it started, and its votes so far."""

    def __init__(self, line: ProductionLine, prompt: Prompt, copy: int = 1) -> None:
        self.line = line
        self.prompt = prompt
        #: Which of the day's lines for this ticker it is (1 almost always), so every call's label is its own.
        self.copy = copy
        self.outcome = NOT_ASKED
        self.votes: dict[int, dict[str, Any]] = {}
        self._started: Optional[bool] = None
        self._lock = threading.Lock()

    def start(self, shared: _Shared) -> bool:
        """Whether this name's calls are asked. Decided once, by the first of its calls to run.

        A name the cut-off or the day's cost cap stops gets its final line
        here, under the name's lock, so it is written once however many of
        its calls ask.
        """
        with self._lock:
            if self._started is None:
                now = _utc(utc_now())
                why = _may_start(self.line.ticker, shared, now)
                self._started = why is None
                if why in (rule.NOT_ASKED_LATE, rule.NOT_ASKED_CAP):
                    _write_not_asked(self, why, now, shared)
            return self._started

    def label(self, number: int) -> str:
        """The call log's and the capture's name for one of its calls: ``XLE vote 2``."""
        ticker = self.line.ticker if self.copy == 1 else f"{self.line.ticker} ({self.copy})"
        return f"{ticker} vote {number}"

    def add(self, vote: dict[str, Any]) -> bool:
        """Keep one vote; True when it was the name's last."""
        with self._lock:
            self.votes[vote["vote"]] = vote
            return len(self.votes) == mv.EXTRA_CALLS


def _may_start(ticker: str, shared: _Shared, now: datetime) -> Optional[str]:
    """Why ``ticker``'s name may not start at ``now``; None when it may, and its four calls are held.

    In this order: the run's time budget and the clock leaving the run's UTC
    day (``OUT_OF_TIME``, ``DAY_OVER``: nothing is written), then the 23:15
    cut-off and the day's cost cap (``rule.NOT_ASKED_LATE``,
    ``rule.NOT_ASKED_CAP``: final, the line says so).
    """
    if time.monotonic() >= shared.deadline:
        return OUT_OF_TIME
    if now.date() != shared.day:
        return DAY_OVER
    if too_late(now) is not None:
        log.warning("%s: it is past the cut-off; not voted", ticker)
        return rule.NOT_ASKED_LATE
    if not shared.guard.reserve(mv.EXTRA_CALLS):
        log.warning("%s: the day's cost cap is reached; not voted", ticker)
        return rule.NOT_ASKED_CAP
    return None


def _write_not_asked(name: _Name, reason: str, now: datetime, shared: _Shared) -> None:
    """The final line of a name that was not started: vote 1 only, no call, the reason. Never raises."""
    try:
        shared.writer.write(vote_line(name.line, now, error=reason, setup=shared.setup, effort=shared.effort), now)
    except Exception:  # noqa: BLE001 - one line must not end the run
        log.exception("%s: could not write its vote line", name.line.ticker)
        name.outcome = UNRECORDED


def _short(text: str) -> str:
    return text[:ERROR_MAX_CHARS]


def read_vote(number: int, line: ProductionLine, answer: "Completion | BaseException") -> dict[str, Any]:
    """One vote from one call's answer, read as ``heartbeat.judge_answer`` reads one, minus the engine."""
    try:
        if isinstance(answer, BaseException):
            raise answer
        signal = heartbeat.scores_without_a_source(heartbeat.parse_signal(answer.text), line.sources)
    except LLMError as exc:
        error = _short(str(exc))
    except (json.JSONDecodeError, ValidationError) as exc:
        error = _short(f"invalid LLM output: {exc}")
    except Exception as exc:  # noqa: BLE001 - one vote must not end the name
        error = _short(f"unexpected {type(exc).__name__}: {exc}")
    else:
        if signal.ticker == line.ticker:
            said = signal.model_dump(mode="json")
            return {"vote": number, "bias": said["bias"], "conviction": said["conviction"],
                    "scores": {name: said.get(name) for name in SCORE_FIELDS}, "error": None}
        error = f"answered for {signal.ticker}"
    return {"vote": number, "bias": None, "conviction": None, "scores": None, "error": error}


def _ask(name: _Name, number: int, shared: _Shared) -> dict[str, Any]:
    """One extra call: the archived prompts, through production's call path, under its own label."""
    label = name.label(number)
    answer: "Completion | BaseException"
    try:
        with llm.call_label(label):
            answer = heartbeat.call_llm(name.prompt.system, name.prompt.user, heartbeat.SIGNAL_JSON_SCHEMA)
    except (LLMError, json.JSONDecodeError, ValidationError) as exc:
        answer = exc
    except Exception as exc:  # noqa: BLE001 - a call that broke is a vote that failed
        log.exception("%s: unexpected failure of the call", label)
        answer = exc
    asks, cost = shared.ledger.charge(label, answer)
    shared.guard.settle(cost)
    vote = read_vote(number, name.line, answer)
    if vote["error"] is not None:
        log.error("%s: %s", label, vote["error"])
    return vote | {"asks": asks, "cost_usd": round(cost, 6)}


def _write_name(name: _Name, shared: _Shared) -> None:
    votes = list(name.votes.values())
    now = utc_now()
    try:
        shared.writer.write(vote_line(name.line, now, votes=votes, asks=sum(v["asks"] for v in votes),
                                      cost_usd=sum(v["cost_usd"] for v in votes),
                                      setup=shared.setup, effort=shared.effort), now)
    except Exception:  # noqa: BLE001 - one line must not end the run
        log.exception("%s: could not write its vote line", name.line.ticker)
        name.outcome = UNRECORDED
        return
    name.outcome = VOTED


def _vote_task(name: _Name, number: int, shared: _Shared) -> None:
    """One of a name's four calls, start to end. Never raises: one call must not end the run."""
    try:
        if not name.start(shared):
            return
        if name.add(_ask(name, number, shared)):
            _write_name(name, shared)
    except Exception:  # noqa: BLE001
        log.exception("%s vote %d: unexpected failure", name.line.ticker, number)
        name.outcome = UNRECORDED


# --------------------------------------------------------------------------- #
# The run
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class VoteRun:
    """What one run did. ``summary()`` is the one JSON line the CLI prints."""

    day: date
    ran: bool
    reason: Optional[str] = None
    #: Today's answered production lines not voted before this run.
    lines: int = 0
    already_voted: int = 0
    #: Lines written with their four calls; of those, with an answer and without one.
    voted: int = 0
    answered: int = 0
    dropped: int = 0
    #: Lines written without a call: no archived input, or an input that differs.
    not_voted: int = 0
    #: Lines not started: the cap or the cut-off (each written, final), the
    #: time budget or the clock leaving the day (not written).
    not_asked: int = 0
    unrecorded: int = 0
    calls: int = 0
    asks: int = 0
    failed_calls: int = 0
    #: The day's total so far, as the cap counts it.
    cost_usd: float = 0.0
    cap_usd: float = mv.DAILY_COST_CAP_USD
    #: The state: the day's total, with the estimates held, is at the cap.
    cap_reached: bool = False
    #: Names the cap stopped in this run, and whether a line written earlier
    #: today already said the cap stopped one, so ``cap_stopped`` fires once a day.
    cap_refused: int = 0
    cap_noted_before: bool = False
    #: The day's total before this run, so ``warn_crossed`` fires once a day.
    spent_before_usd: float = 0.0
    warn_usd: float = mv.DAILY_COST_WARN_USD
    error: Optional[str] = None

    @property
    def warn_crossed(self) -> bool:
        """The day's total passed the alert line during this run (not before it)."""
        return self.spent_before_usd < self.warn_usd <= self.cost_usd

    @property
    def cap_stopped(self) -> bool:
        """The cap stopped a name in this run, and in no earlier run today: the phone is told once a day."""
        return self.cap_refused > 0 and not self.cap_noted_before

    @property
    def estimated_usd(self) -> float:
        """The expected cost of the lines this run was given: four calls each, at the estimate."""
        return round(self.lines * mv.EXTRA_CALLS * mv.ESTIMATED_COST_PER_CALL_USD, 4)

    @property
    def exit_code(self) -> int:
        """3 when the cap first stopped a name today; 1 when nothing could be asked, or every call failed."""
        if self.error is not None:
            return EXIT_FAILED
        if self.cap_stopped:
            return EXIT_CAP_REACHED
        if self.calls > 0 and self.failed_calls == self.calls:
            return EXIT_FAILED
        return EXIT_OK

    def summary(self) -> dict[str, Any]:
        return {
            "date": self.day.isoformat(),
            "ran": self.ran,
            "reason": self.reason,
            "lines": self.lines,
            "already_voted": self.already_voted,
            "voted": self.voted,
            "answered": self.answered,
            "dropped": self.dropped,
            "not_voted": self.not_voted,
            "not_asked": self.not_asked,
            "unrecorded": self.unrecorded,
            "calls": self.calls,
            "asks": self.asks,
            "failed_calls": self.failed_calls,
            "cost_usd": round(self.cost_usd, 6),
            "cap_usd": self.cap_usd,
            "cap_reached": self.cap_reached,
            "cap_stopped": self.cap_stopped,
            "warn_usd": self.warn_usd,
            "warn_crossed": self.warn_crossed,
            "estimated_usd": self.estimated_usd,
            "error": self.error,
        }


def vote_today(
    *,
    model_io_dir: Path | str | None = None,
    journal_dir: Path | str | None = None,
    capture_dir: Path | str | None = None,
    run_id: str = "local",
    workers: Optional[int] = None,
    cap_usd: Optional[float] = None,
    budget_seconds: float = RUN_BUDGET_SECONDS,
) -> VoteRun:
    """Vote on every answered production line of today not voted yet, if today is a day to.

    Does nothing at all (no file read, no call) when ``why_not`` gives a
    reason. Otherwise reads today's production lines and vote lines, checks
    each line's archived input (``model_io_dir``, the downloaded production
    artifact), and asks the four calls of each line that passes, ``workers``
    (default ``WORKERS``) calls at a time, until the lines, the cap or the
    time budget run out. Every ask is captured under ``capture_dir``
    (default ``cfg.MODEL_IO_DIR``), never with production's calls.
    """
    started = _utc(utc_now())
    day = started.date()
    reason = _reason(started)
    if reason is not None:
        log.info("model_vote not run: %s", reason)
        return VoteRun(day=day, ran=False, reason=reason)

    directory = Path(mv.JOURNAL_DIR if journal_dir is None else journal_dir)
    cap = mv.DAILY_COST_CAP_USD if cap_usd is None else cap_usd
    workers = WORKERS if workers is None else workers
    today = day_votes(directory, day)
    candidates = production_lines(day)
    due = [line for line in candidates if line.key not in today.voted]
    guard = CostGuard(cap, today.spent_usd)
    base = dict(day=day, ran=True, lines=len(due), already_voted=len(candidates) - len(due), cap_usd=cap,
                spent_before_usd=today.spent_usd, cap_noted_before=today.cap_noted)
    if not due:
        return VoteRun(**base, cost_usd=guard.spent_usd, cap_reached=guard.cap_reached)

    calls = archived_calls(model_io_dir)
    if calls is None:
        log.error("model_vote: %s; nothing is voted, and a later run today tries again", NO_DOWNLOAD)
        return VoteRun(**base, not_asked=len(due), cost_usd=guard.spent_usd, cap_reached=guard.cap_reached,
                       error=NO_DOWNLOAD)
    # Checked once, before any line is judged: with no model to ask, no body
    # can be rebuilt, and a line written "differs" would be final for nothing.
    try:
        provider = heartbeat.full_model_provider()
    except LLMError as exc:
        log.error("no full model to ask: %s", exc)
        return VoteRun(**base, not_asked=len(due), cost_usd=guard.spent_usd, cap_reached=guard.cap_reached,
                       error=f"no full model to ask: {exc}")

    writer = LineWriter(directory)
    setup = heartbeat.model_setup()
    effort = llm.configured_effort()
    names: list[_Name] = []
    copies: Counter = Counter()
    not_voted = unrecorded = 0
    for line in due:
        prompt, problem = archived_prompt(line, calls, provider)
        if prompt is not None:
            copies[line.ticker] += 1
            names.append(_Name(line, prompt, copies[line.ticker]))
            continue
        log.warning("%s: %s", line.ticker, problem)
        now = utc_now()
        try:
            writer.write(vote_line(line, now, error=problem, setup=setup, effort=effort), now)
            not_voted += 1
        except Exception:  # noqa: BLE001 - one line must not end the run
            log.exception("%s: could not write its vote line", line.ticker)
            unrecorded += 1

    shared = _Shared(guard=guard, ledger=CaptureLedger(mv.ESTIMATED_COST_PER_CALL_USD), writer=writer,
                     setup=setup, effort=effort, deadline=time.monotonic() + budget_seconds, day=day)
    tasks = [(name, number) for name in names for number in range(2, mv.VOTES + 1)]
    if tasks:
        log.info("model_vote: %d line(s) to vote, %d already voted today, %d call(s) at a time, "
                 "$%.4f spent so far today of a $%.2f cap",
                 len(names), base["already_voted"], workers, today.spent_usd, cap)
        capture = Path(cfg.MODEL_IO_DIR if capture_dir is None else capture_dir)
        with model_io.capture(capture, run_id=f"vote-{run_id}"):
            with ThreadPoolExecutor(max_workers=max(1, min(workers, len(tasks)))) as pool:
                list(pool.map(lambda task: _vote_task(*task, shared), tasks))

    written = [name for name in names if name.outcome == VOTED]
    every_vote = [vote for name in names for vote in name.votes.values()]
    answered = 0
    for name in written:
        parsed = [rule.vote_from(vote) for vote in (name.line.production_vote(), *name.votes.values())]
        if rule.aggregate(v for v in parsed if v is not None) is not None:
            answered += 1
    run = VoteRun(
        **base,
        voted=len(written),
        answered=answered,
        dropped=len(written) - answered,
        not_voted=not_voted,
        not_asked=sum(1 for name in names if name.outcome == NOT_ASKED),
        unrecorded=unrecorded + sum(1 for name in names if name.outcome == UNRECORDED),
        calls=len(every_vote),
        asks=sum(vote["asks"] for vote in every_vote),
        failed_calls=sum(1 for vote in every_vote if vote["error"] is not None),
        cost_usd=guard.spent_usd,
        cap_reached=guard.cap_reached,
        cap_refused=guard.refused,
    )
    log.info("model_vote: %s", json.dumps(run.summary(), sort_keys=True))
    return run


# --------------------------------------------------------------------------- #
# Command line
# --------------------------------------------------------------------------- #


def _run_id(text: str) -> str:
    if not _RUN_ID.fullmatch(text):
        raise argparse.ArgumentTypeError("letters, digits, '-' and '_' only, at most 64")
    return text


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m orchestrator.vote",
        description="Vote on today's answered production lines (shadow only: nothing is traded).",
    )
    parser.add_argument("--check", action="store_true",
                        help="only say whether it would run today, why not, and which production runs it needs")
    parser.add_argument("--model-io", type=Path, default=None,
                        help="the downloaded model calls of today's production runs (searched at any depth)")
    parser.add_argument("--capture", type=Path, default=None,
                        help="where this run's own model calls are captured (default: logs/model_io)")
    parser.add_argument("--run-id", type=_run_id, default="local",
                        help="this run's id, in the capture file's name")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, stream=sys.stderr,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    if args.check:
        print(json.dumps(check(), sort_keys=True))
        return EXIT_OK
    run = vote_today(model_io_dir=args.model_io, capture_dir=args.capture, run_id=args.run_id)
    print(json.dumps(run.summary(), sort_keys=True))
    return run.exit_code


__all__ = [
    "ARCHIVE_DIFFERS",
    "CaptureLedger",
    "CostGuard",
    "DAY_OVER",
    "DayVotes",
    "ERROR_MAX_CHARS",
    "EXIT_CAP_REACHED",
    "EXIT_FAILED",
    "EXIT_OK",
    "EXPECTED_LINES",
    "LineWriter",
    "NOT_ASKED",
    "NOT_VOTED",
    "NO_ARCHIVE",
    "NO_DOWNLOAD",
    "OUT_OF_TIME",
    "ProductionLine",
    "Prompt",
    "RUN_BUDGET_SECONDS",
    "UNRECORDED",
    "VOTED",
    "VoteRun",
    "WORKERS",
    "archived_calls",
    "archived_prompt",
    "ask_cost_usd",
    "check",
    "day_votes",
    "due_lines",
    "main",
    "production_lines",
    "production_ran",
    "production_runs",
    "read_vote",
    "too_late",
    "utc_now",
    "vote_line",
    "vote_today",
    "waiting_for_production",
    "why_not",
]


if __name__ == "__main__":
    raise SystemExit(main())
