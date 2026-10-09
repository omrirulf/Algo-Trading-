"""The voting arm ``model_vote``, read side: each line's five votes, its answer, and where it acts differently.

Pre-registration section 13.11 (prepared 2026-10-04, registered at the
2026-12-22 checkpoint). ``orchestrator/vote.py`` asks the model four more
times on each answered production line and writes one line per production
line to ``logs/model_vote/``. This module reads those lines and makes, by
the rule fixed in ``config/model_vote.py``, each line's answer: the side
with at least 3 of the 5 votes, its conviction the share of the 5 votes that
agree times their mean conviction, or no answer at all when fewer than 3
votes succeeded. The race arm and the fund (``shadow/vote.py``), the
descriptive IC comparison (``ic_comparison`` below) and the nightly counters
all read the answers from here, so there is one rule and one reading of it.

Nothing is computed before the registration date: ``due`` and ``active``
are the date gates the funds program reads, and the runner writes no line
before it (``config.model_vote.MODEL_VOTE_ENABLED`` and ``START``).

Pure: reads files, writes nothing, asks nothing. Imported by the race's and
the funds' code, so it never names the model-call capture (the CI guardrail
"Nothing that scores or trades can read the archive"): the vote's own lines,
in git, are all it reads.
"""

from __future__ import annotations

import json
import math
import statistics
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Final, Iterable, Mapping, Optional, Sequence

from analysis.blend import composite as blend_composite
from analysis.reader import SCORE_FIELDS, JournalEntry, parse_timestamp
from config import journal_files
from config import model_vote as mv

#: A production line's identity: its ticker (upper case) and its own UTC
#: time, exactly as the race keys a line (``ScoredTrade.key``).
Key = tuple[str, datetime]

#: What the side of a vote, or of an answer, is when it does not trade: the
#: conviction is under the floor, or the side is NEUTRAL.
NO_TRADE: Final[str] = "no trade"

#: The label every descriptive block of this module carries.
IC_LABEL: Final[str] = "vote score minus single-call score: descriptive only"

#: Why a line was written with no call although its archived input was
#: there: the runner would not start it (pre-registration section 13.11, "and
#: is counted"). Each is final, like a line with no archived input: the
#: production line is never voted again. One spelling, here; the runner
#: (``orchestrator/vote.py``) writes these very strings, and the counters
#: below tell them from the other reasons by the prefix.
NOT_ASKED_PREFIX: Final[str] = "not asked:"
NOT_ASKED_CAP: Final[str] = "not asked: the day's cost cap was reached"
NOT_ASKED_LATE: Final[str] = "not asked: it was 23:15 UTC or later"


# --------------------------------------------------------------------------- #
# One vote, one line, one answer
# --------------------------------------------------------------------------- #


def _finite(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


@dataclass(frozen=True)
class Vote:
    """One of a line's five votes: its bias, conviction and five scores, or why it failed."""

    number: int
    bias: Optional[str] = None
    conviction: Optional[float] = None
    scores: dict[str, Optional[float]] = field(default_factory=dict)
    error: Optional[str] = None

    @property
    def ok(self) -> bool:
        """A successful vote: no error, a known bias and a conviction from 0 to 1."""
        return (self.error is None and self.bias in mv.SIDES and self.conviction is not None
                and 0.0 <= self.conviction <= 1.0)

    @property
    def side(self) -> Optional[str]:
        return mv.SIDES.get(self.bias or "") if self.ok else None


@dataclass(frozen=True)
class Answer:
    """A line's answer by the vote: a side (LONG, SHORT or NEUTRAL), its conviction, and the count behind it."""

    side: str
    conviction: float
    #: Votes for ``side`` (0 for a NEUTRAL that no side won).
    agree: int
    #: Successful votes, the production answer counted (3 to 5).
    successful: int

    @property
    def bias(self) -> str:
        """The side as the race and the funds read a signal: BULLISH, BEARISH or NEUTRAL."""
        return mv.BIASES[self.side]

    def as_dict(self) -> dict[str, Any]:
        return {"side": self.side, "bias": self.bias, "conviction": self.conviction, "agree": self.agree,
                "successful": self.successful}


def aggregate(votes: Iterable[Vote]) -> Optional[Answer]:
    """A line's answer from its votes (``config/model_vote.py``), or None when fewer than 3 succeeded.

    The side with the most successful votes wins if it has at least
    ``MIN_VOTES`` (3) of the ``VOTES`` (5); otherwise, or on a tie for the
    most, the answer is NEUTRAL. Conviction = (votes for the side / 5) x
    (their mean conviction): a failed vote is a vote that does not agree. A
    NEUTRAL answer never trades; its conviction is 0.
    """
    ok = [v for v in votes if v.ok]
    if len(ok) < mv.MIN_VOTES:
        return None
    counts = Counter(v.side for v in ok)
    top = max(counts.values())
    leaders = [side for side, count in counts.items() if count == top]
    if len(leaders) != 1 or top < mv.MIN_VOTES:
        return Answer("NEUTRAL", 0.0, 0, len(ok))
    side = leaders[0]
    if side == "NEUTRAL":
        return Answer("NEUTRAL", 0.0, top, len(ok))
    agreeing = [v.conviction for v in ok if v.side == side]
    conviction = (len(agreeing) / mv.VOTES) * statistics.fmean(agreeing)
    return Answer(side, min(1.0, max(0.0, conviction)), len(agreeing), len(ok))


def tradeable(bias: Optional[str], conviction: Optional[float], floor: float) -> str:
    """What a signal does: LONG or SHORT at or above the floor, else ``NO_TRADE`` (section 13.11, acting differently)."""
    side = mv.SIDES.get(bias or "")
    if side in ("LONG", "SHORT") and conviction is not None and conviction >= floor:
        return side
    return NO_TRADE


@dataclass(frozen=True)
class VoteLine:
    """One production line's vote record, as the runner wrote it."""

    key: Key
    ticker: str
    #: The production line's UTC day (the day the race and the funds give it).
    day: date
    votes: tuple[Vote, ...]
    #: Why the line was not voted, when it was not: no archived input, an input
    #: that differs, or not started (``NOT_ASKED_PREFIX``: the cap, the cut-off).
    error: Optional[str] = None
    #: HTTP asks the four calls made, and what they cost (every ask counted).
    asks: int = 0
    cost_usd: float = 0.0
    #: When the line was written (UTC), and its day.
    written: Optional[datetime] = None

    @property
    def answer(self) -> Optional[Answer]:
        return None if self.error is not None else aggregate(self.votes)

    @property
    def extra_calls(self) -> int:
        """The calls this line asked beyond the production answer."""
        return sum(1 for v in self.votes if v.number > 1)

    @property
    def failed_calls(self) -> int:
        return sum(1 for v in self.votes if v.number > 1 and not v.ok)


def vote_from(raw: Any) -> Optional[Vote]:
    """A vote as the runner wrote it (``{"vote", "bias", "conviction", "scores", "error"}``), or None."""
    if not isinstance(raw, dict):
        return None
    number = raw.get("vote")
    if isinstance(number, bool) or not isinstance(number, int) or not 1 <= number <= mv.VOTES:
        return None
    scores_raw = raw.get("scores") if isinstance(raw.get("scores"), dict) else {}
    scores = {name: _finite(scores_raw.get(name)) for name in SCORE_FIELDS}
    error = raw.get("error")
    bias = raw.get("bias")
    return Vote(number=number, bias=bias if isinstance(bias, str) else None,
                conviction=_finite(raw.get("conviction")), scores=scores,
                error=str(error) if error is not None else None)


def line_from(payload: Any) -> Optional[VoteLine]:
    """One vote line, or None for anything that is not one (another event, no key, a broken record)."""
    if not isinstance(payload, dict) or payload.get("event") != mv.EVENT:
        return None
    ticker = payload.get("ticker")
    if not isinstance(ticker, str) or not ticker.strip():
        return None
    stamp, exact = parse_timestamp({"ts_utc": payload.get("line_ts_utc")})
    if stamp is None or not exact:
        return None
    votes: list[Vote] = []
    seen: set[int] = set()
    for raw in payload.get("votes") or []:
        vote = vote_from(raw)
        if vote is not None and vote.number not in seen:
            votes.append(vote)
            seen.add(vote.number)
    written, _ = parse_timestamp({"ts_utc": payload.get("ts_utc")})
    error = payload.get("error")
    asks = payload.get("asks")
    cost = _finite(payload.get("cost_usd"))
    symbol = ticker.strip().upper()
    return VoteLine(
        key=(symbol, stamp), ticker=symbol, day=stamp.date(), votes=tuple(sorted(votes, key=lambda v: v.number)),
        error=str(error) if error is not None else None,
        asks=asks if isinstance(asks, int) and not isinstance(asks, bool) and asks >= 0 else 0,
        cost_usd=cost if cost is not None and cost >= 0 else 0.0, written=written,
    )


def read_lines(lines: Iterable[str]) -> dict[Key, VoteLine]:
    """Vote lines by production line. A key voted twice keeps its first line (the runner never re-votes one)."""
    out: dict[Key, VoteLine] = {}
    for raw in lines:
        text = raw.strip()
        if not text:
            continue
        try:
            payload = json.loads(text)
        except ValueError:
            continue
        line = line_from(payload)
        if line is not None and line.key not in out:
            out[line.key] = line
    return out


def read_votes(directory: Optional[Path | str] = None) -> dict[Key, VoteLine]:
    """Every vote line in ``directory`` (default ``logs/model_vote``), one file per UTC month."""
    path = Path(mv.JOURNAL_DIR if directory is None else directory)
    if not journal_files.exists(path):
        return {}
    return read_lines(journal_files.iter_lines(path))


def answers(lines: Mapping[Key, VoteLine], *, start: date = mv.START,
            through: Optional[date] = None) -> dict[Key, Answer]:
    """The lines with an answer, from ``start`` (the registration date) to ``through``."""
    out: dict[Key, Answer] = {}
    for key, line in lines.items():
        if line.day < start or (through is not None and line.day > through):
            continue
        answer = line.answer
        if answer is not None:
            out[key] = answer
    return out


def key_of(entry: JournalEntry) -> Optional[Key]:
    """A journal entry's key, as a vote line names it."""
    if entry.timestamp is None:
        return None
    return (entry.ticker.strip().upper(), entry.timestamp)


# --------------------------------------------------------------------------- #
# When anything may be computed
# --------------------------------------------------------------------------- #


def active(today: date) -> bool:
    """Whether anything of the vote may be computed or shown on ``today``: from ``START``, never before."""
    return today >= mv.START


def due(new_look_reached: bool, today: date) -> bool:
    """Whether a checkpoint record carries the vote's results: on a look's night, from ``START`` (section 13.1)."""
    return bool(new_look_reached) and active(today)


# --------------------------------------------------------------------------- #
# Acting differently, and the counters between checkpoints
# --------------------------------------------------------------------------- #


def acted_differently(entries: Sequence[JournalEntry], found: Mapping[Key, Answer], floor: float) -> int:
    """Lines where the vote's signal differs from the single call's (section 13.7).

    Over the answered production lines that have a vote answer: after the
    floor, one of the two trades and the other does not, or they take
    opposite sides. Held and unanswered lines are not offered to either.
    """
    count = 0
    for entry in entries:
        key = key_of(entry)
        if key is None or entry.held or not entry.model_answered or key not in found:
            continue
        answer = found[key]
        if tradeable(answer.bias, answer.conviction, floor) != tradeable(entry.bias, entry.conviction, floor):
            count += 1
    return count


#: The counters' keys: whole numbers only, never a return, a signal or a difference.
COUNTER_KEYS: Final[tuple[str, ...]] = ("lines", "answered", "dropped", "not_voted", "not_asked", "missing",
                                        "extra_calls", "failed_calls")


def counters(lines: Mapping[Key, VoteLine], through: date, entries: Sequence[JournalEntry] = ()) -> dict[str, int]:
    """What is shown about the vote between checkpoints (section 13.1): counts, nothing else.

    From ``START`` to ``through`` (the production line's UTC day):
    ``lines``: production lines with a vote record; ``answered``: with at
    least 3 successful votes; ``dropped``: voted, with fewer; ``not_voted``:
    a record that says why no call was made (no archived input, an input
    that differs); ``not_asked``: a record that says the line was not
    started (the day's cost cap, the 23:15 cut-off); ``extra_calls`` and
    ``failed_calls``: the four calls a line, and the ones that gave no vote.

    ``missing``: the answered, not held lines of the production journal
    (``entries``) that the runner would offer -- an exact UTC time -- and
    that have no vote record at all: a download that failed, a run out of
    time, a run that never came. So every answered line is in one count or
    another (section 13.11: "and is counted"). With no ``entries``, 0.
    """
    out = {name: 0 for name in COUNTER_KEYS}
    for line in lines.values():
        if line.day < mv.START or line.day > through:
            continue
        out["lines"] += 1
        if line.error is not None:
            out["not_asked" if line.error.startswith(NOT_ASKED_PREFIX) else "not_voted"] += 1
        elif line.answer is not None:
            out["answered"] += 1
        else:
            out["dropped"] += 1
        out["extra_calls"] += line.extra_calls
        out["failed_calls"] += line.failed_calls
    missing: set[Key] = set()
    for entry in entries:
        key = key_of(entry)
        if (key is None or not entry.timestamp_is_exact or entry.held or not entry.model_answered
                or not mv.START <= key[1].date() <= through):
            continue
        if key not in lines:
            missing.add(key)
    out["missing"] = len(missing)
    assert set(out) == set(COUNTER_KEYS) and all(type(v) is int for v in out.values())
    return out


# --------------------------------------------------------------------------- #
# The vote score, and the descriptive IC comparison
# --------------------------------------------------------------------------- #


def vote_score(entry: JournalEntry, line: VoteLine) -> Optional[float]:
    """The mean blended score of a line's successful votes; None when there is none to average.

    Vote 1 is the production line's own blended score, as journalled. Each
    other successful vote is blended with the weights the production line
    itself applied (``blend.applied``), so the five scores are made the same
    way. A vote with no score to blend adds nothing. A line that recorded no
    weights has no vote score: its other votes could not be blended alike.
    """
    applied = entry.blend.get("applied") if isinstance(entry.blend, dict) else None
    weights = ({name: float(w) for name, w in applied.items() if _finite(w) is not None}
               if isinstance(applied, dict) else None)
    if not weights or entry.composite is None:
        return None
    values: list[float] = []
    for vote in line.votes:
        if not vote.ok:
            continue
        if vote.number == 1:
            values.append(entry.composite)
            continue
        made = blend_composite(vote.scores, weights)
        if made is not None:
            values.append(made.value)
    return statistics.fmean(values) if values else None


def ic_comparison(entries: Sequence[JournalEntry], lines: Mapping[Key, VoteLine],
                  bars: Mapping[str, Sequence[Any]], through: date) -> dict:
    """The daily IC of the vote score minus the daily IC of the single-call score, on the same lines.

    Descriptive only (section 13.11): not in the Benjamini-Hochberg family,
    no Deflated Sharpe Ratio, no trial of its own. The lines are the answered
    production lines from ``START`` with a vote answer and both scores; each
    day's IC follows the IC report's rule (``analysis.ic.daily_ics``: entry
    at the next open, at least ``MIN_NAMES`` names), at 1 and 3 sessions,
    and the daily difference is read with a Newey-West t (lag = horizon).
    """
    from analysis import ic

    found = answers(lines, through=through)
    single: list = []
    voted: list = []
    without = 0
    for entry in entries:
        key = key_of(entry)
        if key is None or entry.held or not entry.model_answered or key not in found:
            continue
        line = lines[key]
        own = entry.composite
        score = vote_score(entry, line)
        if own is None or score is None:
            without += 1
            continue
        day = key[1].date()
        single.append(ic.IcLine(key[0], day, key[1], {ic.MAIN_SCORE: own}))
        voted.append(ic.IcLine(key[0], day, key[1], {ic.MAIN_SCORE: score}))
    base = {"label": IC_LABEL, "descriptive": True, "in_family": False,
            "rule": "mean blended score of the successful votes, against the line's own blended score",
            "lines": len(single), "lines_without_a_score": without}
    if not single:
        return base | {"no_data": True}
    horizons: dict[str, dict] = {}
    for h in ic.HORIZONS:
        mine = ic.daily_ics(voted, bars, h, through)
        theirs = ic.daily_ics(single, bars, h, through)
        a, b = mine.ics[ic.MAIN_SCORE], theirs.ics[ic.MAIN_SCORE]
        horizons[str(h)] = {
            "vote": {k: v for k, v in ic.summarise(a, h).items() if k not in ("p", "stats")},
            "single_call": {k: v for k, v in ic.summarise(b, h).items() if k not in ("p", "stats")},
            "vote_minus_single_call": ic.paired(a, b, h),
        }
    return base | {"horizons": horizons}


__all__ = [
    "Answer",
    "COUNTER_KEYS",
    "IC_LABEL",
    "Key",
    "NOT_ASKED_CAP",
    "NOT_ASKED_LATE",
    "NOT_ASKED_PREFIX",
    "NO_TRADE",
    "Vote",
    "VoteLine",
    "acted_differently",
    "active",
    "aggregate",
    "answers",
    "counters",
    "due",
    "ic_comparison",
    "key_of",
    "line_from",
    "read_lines",
    "read_votes",
    "tradeable",
    "vote_from",
    "vote_score",
]
