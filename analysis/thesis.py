"""The thesis-check logger, read side: its weekly lines, its counters, and the checkpoint description.

Pre-registration section 13.12 (the owner's instruction of 4 Oct 2026,
item 2; registered at the 2027-03-22 checkpoint, on from 2027-04-01). Once
a week, for each name the paper account holds, ``orchestrator/thesis.py``
asks the production model whether the reason the name was bought still
holds -- VALID, WEAKENED or BROKEN, with one sentence of reason -- and
writes one line per check to ``logs/thesis_check/``. This module reads
those lines.

Log only. Nothing here trades, changes a stop, or feeds any arm or fund.
At a checkpoint the forward returns of the names called BROKEN are set
beside those called VALID (``checkpoint``), as a description only: not a
test, not in the Benjamini-Hochberg family, no Deflated Sharpe Ratio, and
no ``t`` or ``stats`` of its own for a table to read.

Nothing is computed before ``config.thesis_check.START``: ``active`` and
``due`` are the date gates the funds program reads; between checkpoints it
shows ``counters`` only, whole numbers and nothing else.

Pure: reads files, writes nothing, asks nothing, reads no clock. Imported
by the funds program, so it never names the model-call capture: the
logger's own lines, in git, are all it reads.
"""

from __future__ import annotations

import json
import math
import re
import statistics
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Final, Iterable, Mapping, Optional, Sequence

from analysis.ic import OK, PENDING, Bar, forward_return
from analysis.reader import parse_timestamp
from config import journal_files
from config import thesis_check as tc

#: The label the checkpoint description carries.
LABEL: Final[str] = "BROKEN minus VALID: descriptive only"

#: What the Welch t is, in words, wherever it is shown.
WELCH_NOTE: Final[str] = "for reading only: checks on the same day are not independent"

#: The sign of a check's forward return, by the side the position was opened on.
SIGNS: Final[dict[str, int]] = {"long": 1, "short": -1}

#: An ISO week as the logger writes it: ``2027-W14``.
_WEEK = re.compile(r"^\d{4}-W\d{2}$")

#: Why a line was written with no call: the audit log has no accepted entry
#: for the name (no reasoning to check), or the name was not started because
#: the week's cost cap was reached. One spelling, here: the runner
#: (``orchestrator/thesis.py``) writes these very strings, and the read side
#: never imports the runner. Each is final for the name and the ISO week: no
#: line repeats it on a later day of the week.
NO_ENTRY: Final[str] = "no entry record for this name"
NOT_ASKED_PREFIX: Final[str] = "not asked:"
NOT_ASKED_CAP: Final[str] = "not asked: the week's cost cap was reached"


# --------------------------------------------------------------------------- #
# One check
# --------------------------------------------------------------------------- #


def _finite(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


def week_of(day: date) -> str:
    """The ISO week of a UTC day, as the logger writes it (``2027-W14``)."""
    year, week, _ = day.isocalendar()
    return f"{year}-W{week:02d}"


@dataclass(frozen=True)
class Check:
    """One line of the logger: one held name, one week, one verdict -- or why there is none."""

    ticker: str
    #: When the line was written (UTC), and its UTC day: the check's day.
    written: datetime
    day: date
    #: The ISO week the check belongs to.
    week: str
    #: The side the position was opened on: "long" or "short" (None when the line cannot say).
    side: Optional[str] = None
    verdict: Optional[str] = None
    reason: Optional[str] = None
    #: Why no verdict was asked for or given, when none was.
    error: Optional[str] = None
    #: HTTP asks the check made, and what they cost (every ask counted).
    asks: int = 0
    cost_usd: float = 0.0

    @property
    def ok(self) -> bool:
        """A check with a verdict: no error, and one of VALID, WEAKENED or BROKEN."""
        return self.error is None and self.verdict in tc.VERDICTS

    @property
    def sign(self) -> Optional[int]:
        return SIGNS.get(self.side or "")


def line_from(payload: Any) -> Optional[Check]:
    """One logger line, or None for anything that is not one (another event, no ticker, no time)."""
    if not isinstance(payload, dict) or payload.get("event") != tc.EVENT:
        return None
    ticker = payload.get("ticker")
    if not isinstance(ticker, str) or not ticker.strip():
        return None
    written, exact = parse_timestamp({"ts_utc": payload.get("ts_utc")})
    if written is None or not exact:
        return None
    day = written.date()
    week = payload.get("week")
    side = payload.get("side")
    verdict = payload.get("verdict")
    reason = payload.get("reason")
    error = payload.get("error")
    asks = payload.get("asks")
    cost = _finite(payload.get("cost_usd"))
    return Check(
        ticker=ticker.strip().upper(), written=written, day=day,
        week=week if isinstance(week, str) and _WEEK.match(week) else week_of(day),
        side=side.strip().lower() if isinstance(side, str) and side.strip().lower() in SIGNS else None,
        verdict=verdict.strip().upper() if isinstance(verdict, str) else None,
        reason=reason.strip()[:tc.REASON_MAX_CHARS] if isinstance(reason, str) else None,
        error=str(error) if error is not None else None,
        asks=asks if isinstance(asks, int) and not isinstance(asks, bool) and asks >= 0 else 0,
        cost_usd=cost if cost is not None and cost >= 0 else 0.0,
    )


def read_lines(lines: Iterable[str]) -> list[Check]:
    """Every logger line, in the order written. A line that does not parse is skipped."""
    out: list[Check] = []
    for raw in lines:
        text = raw.strip()
        if not text:
            continue
        try:
            payload = json.loads(text)
        except ValueError:
            continue
        check = line_from(payload)
        if check is not None:
            out.append(check)
    return out


def read_checks(directory: Optional[Path | str] = None) -> list[Check]:
    """Every logger line in ``directory`` (default ``logs/thesis_check``), one file per UTC month."""
    path = Path(tc.JOURNAL_DIR if directory is None else directory)
    if not journal_files.exists(path):
        return []
    return read_lines(journal_files.iter_lines(path))


def in_window(lines: Iterable[Check], through: Optional[date] = None) -> list[Check]:
    """The lines from ``START`` to ``through``: nothing written before the start is ever read."""
    return [c for c in lines if c.day >= tc.START and (through is None or c.day <= through)]


def one_per_name_and_week(lines: Iterable[Check]) -> list[Check]:
    """The first check with a verdict for each name and week: the runner writes at most one, and a copy counts once."""
    seen: set[tuple[str, str]] = set()
    out: list[Check] = []
    for check in lines:
        if not check.ok or (check.ticker, check.week) in seen:
            continue
        seen.add((check.ticker, check.week))
        out.append(check)
    return out


# --------------------------------------------------------------------------- #
# When anything may be computed
# --------------------------------------------------------------------------- #


def active(today: date) -> bool:
    """Whether anything of the logger may be computed or shown on ``today``: from ``START``, never before."""
    return today >= tc.START


def due(new_look_reached: bool, today: date) -> bool:
    """Whether a checkpoint record carries the logger's description: on a look's night, from ``START``."""
    return bool(new_look_reached) and active(today)


# --------------------------------------------------------------------------- #
# The counters between checkpoints
# --------------------------------------------------------------------------- #

#: The counters' keys: whole numbers only, never a return or a verdict's share.
COUNTER_KEYS: Final[tuple[str, ...]] = ("checks", "names", "weeks", "failed", "no_entry", "not_asked")


def _not_asked(check: Check) -> bool:
    return (check.error or "").startswith(NOT_ASKED_PREFIX)


def counters(lines: Sequence[Check], through: date) -> dict[str, int]:
    """What is shown about the logger between checkpoints: counts, nothing else.

    From ``START`` to ``through``: ``checks`` with a verdict (one per name
    and week), the distinct ``names`` checked, the ISO ``weeks`` with any
    line; the lines that ``failed`` to give a verdict (a failed call, an
    answer that did not parse); the lines with ``no_entry`` record to check
    against; and the names ``not_asked`` because the week's cost cap was
    reached. Each line is in one of the last three or has a verdict.
    """
    window = in_window(lines, through)
    done = one_per_name_and_week(window)
    out = {"checks": len(done), "names": len({c.ticker for c in done}),
           "weeks": len({c.week for c in window}),
           "failed": sum(1 for c in window if not c.ok and c.error != NO_ENTRY and not _not_asked(c)),
           "no_entry": sum(1 for c in window if c.error == NO_ENTRY),
           "not_asked": sum(1 for c in window if _not_asked(c))}
    assert set(out) == set(COUNTER_KEYS) and all(type(v) is int for v in out.values())
    return out


# --------------------------------------------------------------------------- #
# The checkpoint description
# --------------------------------------------------------------------------- #


def _group(values: Sequence[float]) -> dict:
    n = len(values)
    return {"n": n, "mean": statistics.fmean(values) if values else None,
            "hit_rate": sum(1 for v in values if v > 0) / n if n else None}


def welch_t(first: Sequence[float], second: Sequence[float]) -> Optional[float]:
    """Welch's t of mean(first) - mean(second); None under two values in either group or with no spread."""
    if len(first) < 2 or len(second) < 2:
        return None
    se = math.sqrt(statistics.variance(first) / len(first) + statistics.variance(second) / len(second))
    return (statistics.fmean(first) - statistics.fmean(second)) / se if se > 0 else None


def checkpoint(lines: Sequence[Check], bars: Mapping[str, Sequence[Bar]], through: date, *,
               final: bool = False) -> dict:
    """BROKEN against VALID at a checkpoint: what came after each verdict. A description, never a test.

    For each check with a verdict from ``START`` to ``through`` (one per
    name and week): the forward return from the open of the first session
    after the check's UTC day to the close of the ``FORWARD_SESSIONS``-th
    session, that one counted -- the IC report's rule
    (``analysis.ic.forward_return``), on bars to ``through`` only, price
    only -- times the side's sign (+1 bought, -1 sold short). Per verdict:
    the number, the mean and the hit rate; and BROKEN minus VALID, the
    difference of the means with a Welch t, for reading only. A return
    whose bars are not there yet is pending, and counted.

    ``final``: the last planned look. There, fewer than ``MIN_BROKEN``
    BROKEN checks with a return mean "not tested".
    """
    done = one_per_name_and_week(in_window(lines, through))
    groups: dict[str, list[float]] = {verdict: [] for verdict in tc.VERDICTS}
    pending = no_price = no_side = 0
    for check in done:
        if check.sign is None:
            no_side += 1
            continue
        rows = [bar for bar in bars.get(check.ticker) or () if bar[0] <= through]
        forward = forward_return(rows, check.day, tc.FORWARD_SESSIONS)
        if forward.status == PENDING:
            pending += 1
        elif forward.status != OK or forward.pct is None:
            no_price += 1
        else:
            groups[check.verdict].append(check.sign * forward.pct)
    broken, valid = groups["BROKEN"], groups["VALID"]
    return {
        "label": LABEL, "descriptive": True, "in_family": False,
        "rule": (f"open of the first session after the check's UTC day to the close of session "
                 f"{tc.FORWARD_SESSIONS}, price only, times +1 for a long and -1 for a short"),
        "horizon": tc.FORWARD_SESSIONS, "from": tc.START.isoformat(), "through": through.isoformat(),
        "checks": len(done), "pending": pending, "no_price": no_price, "no_side": no_side,
        "verdicts": {verdict: _group(values) for verdict, values in groups.items()},
        "broken_minus_valid": {
            "mean_diff": statistics.fmean(broken) - statistics.fmean(valid) if broken and valid else None,
            "welch_t": welch_t(broken, valid), "note": WELCH_NOTE,
        },
        "broken": len(broken), "min_broken": tc.MIN_BROKEN,
        "not_tested": bool(final) and len(broken) < tc.MIN_BROKEN,
        "no_data": not done,
    }


def tickers_of(lines: Iterable[Check], through: Optional[date] = None) -> list[str]:
    """The names with a verdict from ``START`` to ``through``, sorted: what the nightly run fetches bars for."""
    return sorted({c.ticker for c in one_per_name_and_week(in_window(lines, through))})


__all__ = [
    "COUNTER_KEYS",
    "Check",
    "LABEL",
    "NOT_ASKED_CAP",
    "NOT_ASKED_PREFIX",
    "NO_ENTRY",
    "SIGNS",
    "WELCH_NOTE",
    "active",
    "checkpoint",
    "counters",
    "due",
    "in_window",
    "line_from",
    "one_per_name_and_week",
    "read_checks",
    "read_lines",
    "tickers_of",
    "week_of",
    "welch_t",
]
