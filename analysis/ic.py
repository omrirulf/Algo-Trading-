"""The daily IC report: do the model's scores rank the names in the order they then move?

The owner's instruction of 2 Oct 2026 (item 4): for every journal line the
model answered, take its scores -- the blended score and each of the five
dimensions -- and each day measure the rank correlation between each score
and the names' forward returns, at 1 session and at 3 sessions, entered at
the next open as the race enters. Do the same for the momentum rule's score,
as a comparator. Report the mean IC, a Newey-West t, the number of days, the
measured effective number of independent names, and the smallest IC that
could be detected at t = 2.4. Between checkpoints show only counters; no IC
value is written to any file, page or log before the checkpoint. Registered
at the 22 Dec 2026 checkpoint, over every line from 28 Sep 2026.

The IC (information coefficient) of a day is that rank correlation. A score
that knows nothing has ICs around 0; a score that puts the names in exactly
the order they then move has an IC of 1.

**What the journal stores** (checked on 2 Oct 2026, the answered lines from
28 Sep to 1 Oct): ``blend.composite``, ``signal.news_score``,
``signal.technical_score`` and ``signal.fundamental_score`` on every answered
line; ``signal.analyst_score`` on 189 of 233 (null by design on bond and
commodity funds: no analysts rate them and they have no holdings roll-up);
``signal.insider_score`` on 230 of 233 (null on three lines whose prompt had
no insider, positioning or flow section); ``arms.momentum`` (bias and
conviction) on every line. A null score leaves the line out of that score's
IC, and only that score's.

How each number is made (every setting is a ``Final`` constant below):

* **Lines.** Answered lines only, by the race's rule: a signal about this
  ticker (``JournalEntry.model_answered``) and not held (a held name was
  never offered to the model). A line with such a signal and an error
  written after the answer (``"webhook unreachable: ..."``, ``"engine
  unavailable: ..."``) counts, as it does in the race; a signal about another
  ticker (``"answered for X"``) does not. Journalled on or after ``IC_START``,
  by the UTC day of ``ts_utc``. The production lines are ``logs/journal/``;
  the shadow stock universe's (``logs/shadow_universe/``, same format, same
  reader) count from ``SHADOW_START``.
* **Scores.** blend = ``blend.composite``; a dimension =
  ``signal.<dimension>_score``; momentum = +conviction when
  ``arms.momentum.bias`` is BULLISH, -conviction when BEARISH, 0 when
  NEUTRAL. A missing value leaves the line out of that score.
* **Forward return.** A line of UTC day D enters at the Open of the first bar
  dated after D -- the race's entry rule (``tests/test_race_entry_timing.py``):
  a Friday line enters on Monday, a line written after midnight UTC enters
  the session after that UTC day -- and exits at the Close of the h-th bar,
  the entry bar counted as the first. Return = exit / entry - 1: the price
  only, no dividend and no cost. Bars are counted by position, as the race
  counts them. A return whose bars are not there yet is pending, and counted.
* **Daily IC.** Lines are grouped by entry day (the date of the entry bar).
  For each entry day, score and horizon: Spearman's rank correlation, average
  ranks for ties (``analysis.metrics.spearman``), over the names with both
  the score and a resolved return. Fewer than ``MIN_NAMES`` such names, or a
  score or a return that does not vary that day: no IC, and the day is
  counted as skipped. A ticker twice on one entry day: the last line counts.
* **Summary.** The mean of the daily ICs; its Newey-West standard error with
  lag = horizon (the race's convention, and the same variance as
  ``analysis.horse_race.newey_west_t``); t = mean / standard error; the
  two-sided p (``analysis.multiple_tests.p_two_sided``); and
  ``series_stats`` of the daily ICs, for the Deflated Sharpe Ratio. The
  blended score minus momentum, day by day, is shown for reading only.
* **n_eff**, the effective number of independent names, measured from the
  daily close-to-close returns of the universe's names over the IC window
  (the first entry day to the last resolved day).
  - *Which names and dates.* The window's dates are the dates on which any
    name has a return there. A name whose returns cover less than
    ``N_EFF_MIN_COVERAGE`` of them, or with fewer than ``N_EFF_MIN_RETURNS``
    returns, is dropped first, so one name with a short history (a new
    listing, a takeover) does not cut the window for every other name. Then
    only the dates on which every kept name has a return are used (fewer
    than ``N_EFF_MIN_DATES``: no n_eff, and the reason), and a name whose
    price never moves on them is dropped.
  - *The common move is taken out.* Each date's mean return across the
    kept names is subtracted from every name's return that date. Moving
    every name by the same amount does not change their ranks, so it does
    not change a day's IC; left in, that one common move (the market)
    would make the names look far less independent than a rank IC sees
    them, and the smallest detectable IC far too large.
  - *Two numbers.* C is the correlation matrix of these returns, over the
    N names and T dates. ``n_eff_raw`` = N^2 / sum(C^2), the participation
    ratio (sum of eigenvalues)^2 / (sum of squared eigenvalues). It reads
    low on a short window: pure noise over T dates adds about
    N(N - 1) / (T - 1) to sum(C^2), so it can never pass about
    N / (1 + (N - 1) / (T - 1)). ``n_eff`` takes that noise out:
    N^2 / max(sum(C^2) - N(N - 1) / (T - 1), N), so it is at most N.
    Names that move independently apart from the common move give about
    N - 1 (taking out the mean uses up one name); names that also move
    together in groups give fewer. ``n_eff`` is the number reported and
    used below; ``n_eff_raw`` is shown for reading.
* **Smallest detectable IC** at t = ``MDE_T``. Measured: ``MDE_T`` x the
  Newey-West standard error. In theory: ``MDE_T`` / sqrt((n_eff - 1) x days /
  h), with the noise-corrected ``n_eff``, because a day's IC over n_eff
  independent names has a standard error of about 1 / sqrt(n_eff - 1), and
  3-session windows that overlap give about days / 3 independent days.

**Hidden until the checkpoint.** ``counters`` is the only function the
nightly run calls before the checkpoint: answered lines, lines with each
score, and line days -- counts only. It is given no prices, so it cannot
compute a return, and it checks its own output. ``due`` is True only on a
night a new look of the race is reached on or after ``IC_REGISTRATION``;
``record`` is then made once and kept unchanged, like the exploratory
tests' records (``shadow/run.py``). The main test, PROPOSED as the blended
score at 3 sessions (``MAIN_SCORE``, ``MAIN_HORIZON``; the owner confirms it
at registration), enters the Benjamini-Hochberg family and the Deflated
Sharpe Ratio; every other number is for reading. ``card`` is the
pre-registration card, made from these same constants.

Pure computation: bars come in (``bars_from_fetcher`` builds them from a
fetcher for the nightly run), nothing is fetched here, no file is written,
no clock is read. ``read_universe`` only reads a journal. Shadow only:
nothing is traded on any number here, and no rule is tuned on it.
"""

from __future__ import annotations

import bisect
import json
import math
import statistics
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Final, Iterable, Mapping, Optional, Sequence

from analysis.metrics import spearman
from analysis.multiple_tests import p_two_sided, series_stats
from analysis.reader import entry_from
from config import journal_files

#: Lines journalled on or after this UTC day are in the test ("over all lines from 2026-09-28").
IC_START: Final[date] = date(2026, 9, 28)
#: The checkpoint at which the card is registered; no IC is computed before it (``due``).
IC_REGISTRATION: Final[date] = date(2026, 12, 22)
#: The shadow stock universe's first scored day (``config.shadow_universe.START``).
SHADOW_START: Final[date] = date(2027, 1, 1)
#: The two universes: the production names and the shadow stock universe.
UNIVERSES: Final[tuple[str, ...]] = ("production", "shadow")
#: The first line day of each universe.
UNIVERSE_START: Final[dict[str, date]] = {"production": IC_START, "shadow": SHADOW_START}
#: Forward-return horizons, in sessions, the entry bar counted as the first.
HORIZONS: Final[tuple[int, ...]] = (1, 3)
#: The five dimension scores, each journalled as ``signal.<name>_score``.
DIMENSIONS: Final[tuple[str, ...]] = ("news", "technical", "fundamental", "analyst", "insider")
#: The model's scores under test: the blended score (``blend.composite``) and the five dimensions.
SCORES: Final[tuple[str, ...]] = ("blend",) + DIMENSIONS
#: The comparator: the momentum rule's signed conviction (``arms.momentum``).
COMPARATOR: Final[str] = "momentum"
#: Every score a line is read for, the model's first.
ALL_SCORES: Final[tuple[str, ...]] = SCORES + (COMPARATOR,)
#: A day's IC needs at least this many names with both the score and a resolved return.
MIN_NAMES: Final[int] = 10
#: The t at which the smallest detectable IC is measured.
MDE_T: Final[float] = 2.4
#: The Newey-West lag at each horizon: the horizon itself, the race's convention.
NW_LAG: Final[dict[int, int]] = {1: 1, 3: 3}
#: n_eff: a name needs at least this many daily returns in the IC window to be kept.
N_EFF_MIN_RETURNS: Final[int] = 20
#: n_eff: and returns on at least this share of the window's dates, checked before the dates are intersected,
#: so one name with a short history does not cut the window for every other name.
N_EFF_MIN_COVERAGE: Final[float] = 0.9
#: n_eff: and at least this many dates on which every kept name has a return, or n_eff is not measured.
N_EFF_MIN_DATES: Final[int] = 20
#: n_eff: a name whose returns, once each date's mean is taken out, vary by less than this share of its own
#: returns' spread moves exactly with the others (what is left is rounding, not a move). Not a setting.
_FLAT_SHARE: Final[float] = 1e-9
#: The main test, PROPOSED: the blended score's IC at 3 sessions. The owner confirms it at registration.
MAIN_SCORE: Final[str] = "blend"
#: The main test's horizon, in sessions (proposed with ``MAIN_SCORE``).
MAIN_HORIZON: Final[int] = 3
#: For reading only: the blended score's daily IC minus the comparator's, on the days both have one.
PAIRED: Final[tuple[str, str]] = ("blend", COMPARATOR)
#: Everything ``counters`` may show, per universe, and nothing else.
COUNTER_KEYS: Final[tuple[str, ...]] = ("answered_lines", "lines_with_score", "line_days")

#: A forward return's status: resolved, its bars not there yet, or no usable price for the name.
OK: Final[str] = "ok"
PENDING: Final[str] = "pending"
NO_PRICE: Final[str] = "no_price"

#: Why a day has no IC for a score.
FEW_NAMES: Final[str] = "few_names"
NO_SPREAD: Final[str] = "no_spread"

#: One daily bar, as the module takes it: (date, open, close).
Bar = tuple[date, float, float]


@dataclass(frozen=True)
class IcLine:
    """One answered line: the name, its UTC day and time, and each score (None where the line has none)."""

    ticker: str
    day: date
    timestamp: datetime
    scores: dict[str, Optional[float]] = field(default_factory=dict)


@dataclass(frozen=True)
class Forward:
    """A line's forward return at one horizon: its status and, when resolved, its days and value."""

    status: str
    entry_day: Optional[date] = None
    exit_day: Optional[date] = None
    pct: Optional[float] = None


@dataclass(frozen=True)
class DailyIcs:
    """One universe's daily ICs at one horizon.

    ``ics`` is score -> entry day -> IC; ``skipped`` is score -> reason -> days;
    ``pairs`` is score -> the name-returns used on the days with an IC.
    ``pending`` and ``no_price`` count lines (after one line per name and
    entry day). ``first_entry`` and ``last_exit`` bound the resolved returns.
    """

    horizon: int
    ics: dict[str, dict[date, float]]
    skipped: dict[str, dict[str, int]]
    pairs: dict[str, int]
    pending: int
    no_price: int
    first_entry: Optional[date]
    last_exit: Optional[date]


@dataclass(frozen=True)
class _Tape:
    """One name's bars, by position: dates in order, with each bar's open and close."""

    dates: list[date]
    opens: list[Optional[float]]
    closes: list[Optional[float]]


# --------------------------------------------------------------------------- #
# Reading lines
# --------------------------------------------------------------------------- #


def momentum_score(arms: Any) -> Optional[float]:
    """The momentum rule's signed score from a line's ``arms`` record; None when it has none.

    +conviction for BULLISH, -conviction for BEARISH, 0 for NEUTRAL. An arm
    that failed (``{"error": ...}``) or a missing record gives None.
    """
    record = arms.get(COMPARATOR) if isinstance(arms, dict) else None
    if not isinstance(record, dict):
        return None
    bias = record.get("bias")
    if bias == "NEUTRAL":
        return 0.0
    sign = {"BULLISH": 1.0, "BEARISH": -1.0}.get(bias) if isinstance(bias, str) else None
    conviction = _finite(record.get("conviction"))
    if sign is None or conviction is None:
        return None
    return sign * conviction


def line_from(payload: Any) -> Optional[IcLine]:
    """An answered line's scores, or None for anything else.

    Answered, by the race's rule: a signal about this ticker
    (``JournalEntry.model_answered``: a bias and a conviction, and not
    journalled as "answered for X") and not held. An error written after
    the answer -- "webhook unreachable: ...", "engine unavailable: ..." --
    does not take the line out, as it does not in the race; the shadow
    universe's failed lines carry no signal, so the same rule reads both.
    The common fields come from ``analysis.reader.entry_from``, so this
    reads a line exactly as every other reader of the journal does; only
    ``arms`` is read here.
    """
    try:
        entry = entry_from(payload)
    except (TypeError, ValueError, AttributeError):
        return None
    if entry is None or entry.timestamp is None:
        return None
    if not entry.model_answered or entry.held:
        return None
    scores: dict[str, Optional[float]] = {"blend": entry.composite}
    for name in DIMENSIONS:
        scores[name] = entry.scores.get(f"{name}_score")
    scores[COMPARATOR] = momentum_score(payload.get("arms"))
    utc = entry.timestamp.astimezone(timezone.utc)
    return IcLine(ticker=entry.ticker, day=utc.date(), timestamp=utc, scores=scores)


def read_lines(lines: Iterable[str]) -> list[IcLine]:
    """Every answered line among raw journal lines, in order. Unreadable lines are skipped."""
    out: list[IcLine] = []
    for raw in lines:
        if not raw.strip():
            continue
        try:
            payload = json.loads(raw)
        except ValueError:
            continue
        line = line_from(payload)
        if line is not None:
            out.append(line)
    return out


def read_universe(path: Path | str) -> list[IcLine]:
    """Every answered line of a journal -- the monthly directory or one file; none when there is none yet.

    One reader for both universes: ``logs/journal`` and ``logs/shadow_universe``
    are both one file per UTC month, joined by ``config.journal_files``.
    """
    if not journal_files.exists(path):
        return []
    return read_lines(journal_files.iter_lines(path))


def in_window(lines: Iterable[IcLine], universe: str, through: Optional[date] = None) -> list[IcLine]:
    """The lines of ``universe`` journalled from its first day (``UNIVERSE_START``) to ``through``."""
    first = UNIVERSE_START.get(universe, IC_START)
    return [line for line in lines if line.day >= first and (through is None or line.day <= through)]


def tickers_of(lines: Iterable[IcLine]) -> list[str]:
    """The names the lines are about, sorted: what the nightly run fetches bars for."""
    return sorted({line.ticker for line in lines})


# --------------------------------------------------------------------------- #
# Counters: the only thing shown between checkpoints
# --------------------------------------------------------------------------- #


def counters(lines_by_universe: Mapping[str, Sequence[IcLine]], through: Optional[date] = None) -> dict:
    """What may be shown before the checkpoint, per universe: counts, and nothing else.

    ``answered_lines`` since the universe's first day, ``lines_with_score``
    (a count per score, momentum included) and ``line_days`` (distinct UTC
    days with an answered line). No IC, no return, no mean: this function is
    given no prices, so it cannot compute one, and its output is checked to
    hold exactly ``COUNTER_KEYS`` with whole-number values.
    """
    out: dict[str, dict] = {}
    for universe in UNIVERSES:
        lines = in_window(lines_by_universe.get(universe) or (), universe, through)
        out[universe] = {
            "answered_lines": len(lines),
            "lines_with_score": {name: sum(1 for line in lines if line.scores.get(name) is not None)
                                 for name in ALL_SCORES},
            "line_days": len({line.day for line in lines}),
        }
    return _counts_only(out)


def _counts_only(out: dict) -> dict:
    """``out`` unchanged when it holds counts only, in the allowed shape; else an error, never a number."""
    for universe, block in out.items():
        if universe not in UNIVERSES or set(block) != set(COUNTER_KEYS):
            raise ValueError(f"counters may hold only {COUNTER_KEYS}")
        if set(block["lines_with_score"]) != set(ALL_SCORES):
            raise ValueError("counters count lines per score, and only that")
        values = [block["answered_lines"], block["line_days"], *block["lines_with_score"].values()]
        if any(isinstance(v, bool) or not isinstance(v, int) for v in values):
            raise ValueError("counters hold whole-number counts only")
    return out


def due(new_look_reached: bool, today: date) -> bool:
    """Whether tonight's run makes the IC record: a new look is reached, on or after registration."""
    return bool(new_look_reached) and today >= IC_REGISTRATION


# --------------------------------------------------------------------------- #
# Prices and forward returns
# --------------------------------------------------------------------------- #


def bars_from_fetcher(fetcher: Any, tickers: Iterable[str], start: date, end: date) -> dict[str, list[Bar]]:
    """Each ticker's daily ``(date, open, close)`` bars, sorted, from an ``OhlcFetcher``-like object.

    ``fetcher.ohlc(ticker, start, end)`` returns a frame with Open and Close
    columns indexed by the bar's timestamp (``analysis.baseline_compare``).
    For the nightly run, use a fetcher whose first call for each name covers
    ``start`` (an ``OhlcFetcher`` keeps its first fetch) and that keeps final
    closes only (``final_through``). A name the fetcher cannot price gets
    an empty list, so its lines are counted as having no price.
    """
    out: dict[str, list[Bar]] = {}
    for ticker in tickers:
        try:
            frame = fetcher.ohlc(ticker, start, end)
        except Exception:  # noqa: BLE001 - a name without prices is a status, not a crash
            frame = None
        out[ticker] = _rows(frame)
    return out


def _rows(frame: Any) -> list[Bar]:
    if frame is None or getattr(frame, "empty", True):
        return []
    try:
        opens, closes = list(frame["Open"]), list(frame["Close"])
    except (KeyError, TypeError):
        return []
    by_day: dict[date, Bar] = {}
    for stamp, open_, close in zip(frame.index, opens, closes):
        day, o, c = _bar_date(stamp), _finite(open_), _finite(close)
        if day is not None and o is not None and c is not None:
            by_day[day] = (day, o, c)
    return [by_day[d] for d in sorted(by_day)]


def _bar_date(stamp: Any) -> Optional[date]:
    """A bar's session day: yfinance dates a bar at midnight in the exchange's own zone."""
    if isinstance(stamp, datetime):
        return stamp.date()
    if isinstance(stamp, date):
        return stamp
    to_date = getattr(stamp, "date", None)
    if callable(to_date):
        value = to_date()
        return value if isinstance(value, date) else None
    try:
        return date.fromisoformat(str(stamp)[:10])
    except ValueError:
        return None


def _tape(rows: Optional[Sequence[Sequence[Any]]], through: Optional[date] = None) -> Optional[_Tape]:
    """A name's bars by position, through ``through``; the last bar given for a date wins."""
    if rows is None:
        return None
    by_day: dict[date, tuple[Optional[float], Optional[float]]] = {}
    for row in rows:
        day = row[0]
        if through is not None and day > through:
            continue
        by_day[day] = (_finite(row[1]), _finite(row[2]))
    days = sorted(by_day)
    return _Tape(days, [by_day[d][0] for d in days], [by_day[d][1] for d in days])


def _entry_index(tape: Optional[_Tape], day: date) -> Optional[int]:
    """Position of the first bar dated after ``day``, or None when there is none yet."""
    if tape is None or not tape.dates:
        return None
    index = bisect.bisect_right(tape.dates, day)
    return index if index < len(tape.dates) else None


def _forward(tape: Optional[_Tape], day: date, horizon: int) -> Forward:
    if horizon < 1:
        raise ValueError("a horizon is at least 1 session")
    if tape is None or not tape.dates:
        return Forward(NO_PRICE)
    entry = _entry_index(tape, day)
    if entry is None:
        return Forward(PENDING)
    exit_ = entry + horizon - 1
    if exit_ >= len(tape.dates):
        return Forward(PENDING, entry_day=tape.dates[entry])
    price_in, price_out = tape.opens[entry], tape.closes[exit_]
    if not (_positive(price_in) and _positive(price_out)):
        return Forward(NO_PRICE, entry_day=tape.dates[entry])
    return Forward(OK, tape.dates[entry], tape.dates[exit_], price_out / price_in - 1.0)


def forward_return(bars: Optional[Sequence[Bar]], day: date, horizon: int) -> Forward:
    """The forward return of a line of UTC day ``day``: next open to the h-th bar's close, price only.

    ``bars`` is the name's ``(date, open, close)`` list (None or empty: no
    price). Entry: the Open of the first bar dated after ``day``. Exit: the
    Close of bar ``horizon``, the entry bar counted as the first. Pending
    while either bar is not there yet.
    """
    return _forward(_tape(bars), day, horizon)


# --------------------------------------------------------------------------- #
# Daily ICs
# --------------------------------------------------------------------------- #


def _one_per_name_and_day(lines: Sequence[IcLine], tapes: Mapping[str, Optional[_Tape]]) -> list[IcLine]:
    """The last line (by time, then order) of each name on each entry day.

    A line whose entry bar is not there yet is kept per name and line day.
    """
    latest: dict[tuple, IcLine] = {}
    for line in sorted(lines, key=lambda x: x.timestamp):
        tape = tapes.get(line.ticker)
        index = _entry_index(tape, line.day)
        key = ("entry", tape.dates[index], line.ticker) if index is not None else ("line", line.day, line.ticker)
        latest[key] = line
    return list(latest.values())


def daily_ics(lines: Sequence[IcLine], bars: Mapping[str, Sequence[Bar]], horizon: int,
              through: Optional[date] = None) -> DailyIcs:
    """Each entry day's IC for every score at one horizon, with the skipped days and pending lines counted.

    ``bars`` maps a ticker to its sorted ``(date, open, close)`` bars; bars
    after ``through`` are not read. A day enters once at least one of its
    lines has a resolved return; it has an IC for a score when ``MIN_NAMES``
    names carry both the score and a return and neither series is constant.
    """
    tapes = {ticker: _tape(rows, through) for ticker, rows in bars.items()}
    kept = _one_per_name_and_day(lines, tapes)
    by_day: dict[date, list[tuple[IcLine, float]]] = {}
    status: Counter = Counter()
    first_entry: Optional[date] = None
    last_exit: Optional[date] = None
    for line in kept:
        result = _forward(tapes.get(line.ticker), line.day, horizon)
        status[result.status] += 1
        if result.status != OK:
            continue
        by_day.setdefault(result.entry_day, []).append((line, result.pct))
        first_entry = result.entry_day if first_entry is None else min(first_entry, result.entry_day)
        last_exit = result.exit_day if last_exit is None else max(last_exit, result.exit_day)

    ics: dict[str, dict[date, float]] = {name: {} for name in ALL_SCORES}
    skipped: dict[str, dict[str, int]] = {name: {FEW_NAMES: 0, NO_SPREAD: 0} for name in ALL_SCORES}
    pairs: dict[str, int] = {name: 0 for name in ALL_SCORES}
    for day in sorted(by_day):
        for name in ALL_SCORES:
            both = [(line.scores[name], pct) for line, pct in by_day[day] if line.scores.get(name) is not None]
            if len(both) < MIN_NAMES:
                skipped[name][FEW_NAMES] += 1
                continue
            rho = spearman([s for s, _ in both], [r for _, r in both]).rho
            if rho is None:
                skipped[name][NO_SPREAD] += 1
                continue
            ics[name][day] = max(-1.0, min(1.0, rho))
            pairs[name] += len(both)
    return DailyIcs(horizon=horizon, ics=ics, skipped=skipped, pairs=pairs, pending=status[PENDING],
                    no_price=status[NO_PRICE], first_entry=first_entry, last_exit=last_exit)


# --------------------------------------------------------------------------- #
# Summaries
# --------------------------------------------------------------------------- #


def newey_west_se(xs: Sequence[float], lag: int) -> Optional[float]:
    """The Newey-West (Bartlett) standard error of the mean of ``xs``; None when it cannot be computed.

    The same variance as ``analysis.horse_race.newey_west_t`` -- 1/n
    autocovariances, weights 1 - k / (lag + 1), the lag cut to n - 1, None
    under 2 values or without a positive variance -- so mean / this is that
    t (``tests/test_ic.py`` pins it).
    """
    n = len(xs)
    if n < 2:
        return None
    mean = statistics.fmean(xs)
    e = [x - mean for x in xs]
    var = sum(v * v for v in e) / n
    for k in range(1, min(lag, n - 1) + 1):
        gamma = sum(e[i] * e[i - k] for i in range(k, n)) / n
        var += 2.0 * (1.0 - k / (lag + 1.0)) * gamma
    if var <= 0:
        return None
    return math.sqrt(var / n)


def mde_theory(n_eff: Optional[float], days: int, horizon: int) -> Optional[float]:
    """``MDE_T`` / sqrt((n_eff - 1) x days / horizon); None without n_eff above 1 or without days.

    ``n_eff`` is the noise-corrected one, with the common move taken out
    (``effective_names``). A day's IC over n_eff independent names has a
    standard error of about 1 / sqrt(n_eff - 1); windows of ``horizon``
    sessions that overlap give about days / horizon independent days.
    """
    if n_eff is None or n_eff <= 1 or days <= 0 or horizon < 1:
        return None
    return MDE_T / math.sqrt((n_eff - 1.0) * days / horizon)


def summarise(daily: Mapping[date, float], horizon: int, n_eff: Optional[float] = None,
              skipped: Optional[Mapping[str, int]] = None, pairs: int = 0) -> dict:
    """One score's summary at one horizon, from its daily ICs (entry day -> IC).

    ``days``, ``skipped_days`` (and why), ``pairs``, ``mean_ic``, ``nw_se``,
    ``t`` = mean / nw_se, ``p``, ``stats`` (``series_stats``, for the
    Deflated Sharpe Ratio), ``mde_measured`` = ``MDE_T`` x nw_se and
    ``mde_theory``.
    """
    series = [daily[d] for d in sorted(daily)]
    lag = NW_LAG.get(horizon, horizon)
    mean = statistics.fmean(series) if series else None
    se = newey_west_se(series, lag)
    t = mean / se if mean is not None and se else None
    why = {FEW_NAMES: 0, NO_SPREAD: 0} | dict(skipped or {})
    return {
        "days": len(series),
        "skipped_days": sum(why.values()),
        "skipped": why,
        "pairs": pairs,
        "mean_ic": mean,
        "nw_se": se,
        "nw_lag": lag,
        "t": t,
        "p": p_two_sided(t),
        "stats": series_stats(series),
        "mde_measured": MDE_T * se if se else None,
        "mde_theory": mde_theory(n_eff, len(series), horizon),
    }


def paired(first: Mapping[date, float], second: Mapping[date, float], horizon: int) -> dict:
    """``first`` minus ``second`` on the days both have an IC: days, mean and Newey-West t. For reading."""
    days = sorted(set(first) & set(second))
    diffs = [first[d] - second[d] for d in days]
    mean = statistics.fmean(diffs) if diffs else None
    se = newey_west_se(diffs, NW_LAG.get(horizon, horizon))
    return {"days": len(diffs), "mean": mean, "t": mean / se if mean is not None and se else None}


# --------------------------------------------------------------------------- #
# The effective number of independent names
# --------------------------------------------------------------------------- #


def effective_names(bars: Mapping[str, Sequence[Bar]], names: Iterable[str], first: Optional[date],
                    last: Optional[date], through: Optional[date] = None) -> dict:
    """n_eff from the names' daily close-to-close returns dated ``first`` to ``last``, the common move taken out.

    Returns ``{"n_eff", "n_eff_raw", "names", "dates", "window_dates",
    "mean_corr", "reason"}``:

    * ``window_dates``: the dates in the window on which any name has a
      return. A name with returns on less than ``N_EFF_MIN_COVERAGE`` of
      them, or with fewer than ``N_EFF_MIN_RETURNS``, is dropped before the
      dates are intersected, so it cannot cut the window for the others.
    * ``dates``: T, the dates on which every kept name has a return (at
      least ``N_EFF_MIN_DATES``, or no n_eff). A name whose price never
      moves on them is dropped too; ``names`` are the N names used.
    * ``mean_corr``: the mean correlation between two different names'
      returns as they are, the common move still in: for reading.
    * Then each date's mean return across the names is subtracted from
      every name's return that date (a move shared by every name does not
      change their ranks, so it is no part of a rank IC), and C is the
      correlation matrix of what is left. ``n_eff_raw`` = N^2 / sum(C^2),
      the participation ratio (sum(C^2) is the sum of squared
      eigenvalues, N their sum). ``n_eff`` = N^2 / max(sum(C^2) -
      N(N - 1) / (T - 1), N): the same with the sampling noise of T dates
      taken out (pure noise adds about N(N - 1) / (T - 1) to sum(C^2)).
      Independent names give about N - 1; names that move as one leave
      nothing to rank once the common move is out, and give no n_eff.
    * ``reason``: why n_eff is None when it is.
    """
    import numpy as np

    out: dict[str, Any] = {"n_eff": None, "n_eff_raw": None, "names": [], "dates": 0, "window_dates": 0,
                           "mean_corr": None, "reason": None}
    if first is None or last is None:
        out["reason"] = "no resolved return yet"
        return out
    every: dict[str, dict[date, float]] = {}
    for name in sorted(set(names)):
        tape = _tape(bars.get(name), through)
        if tape is None:
            continue
        series = {}
        for i in range(1, len(tape.dates)):
            day, before, now = tape.dates[i], tape.closes[i - 1], tape.closes[i]
            if first <= day <= last and _positive(before) and _positive(now):
                series[day] = now / before - 1.0
        every[name] = series
    window = set().union(*every.values()) if every else set()
    out["window_dates"] = len(window)
    returns = {name: series for name, series in every.items()
               if window and len(series) >= N_EFF_MIN_RETURNS and len(series) / len(window) >= N_EFF_MIN_COVERAGE}
    if len(returns) < 2:
        out["reason"] = (f"{len(returns)} name(s) with at least {N_EFF_MIN_RETURNS} daily returns, on at least "
                         f"{N_EFF_MIN_COVERAGE:.0%} of the {len(window)} dates from {first.isoformat()} to "
                         f"{last.isoformat()}; n_eff needs 2")
        return out
    common = sorted(set.intersection(*(set(s) for s in returns.values())))
    out["dates"] = len(common)
    if len(common) < N_EFF_MIN_DATES:
        out["reason"] = (f"only {len(common)} date(s) on which every one of {len(returns)} names has a return; "
                         f"n_eff needs {N_EFF_MIN_DATES}")
        return out
    moving = [name for name in returns if np.std([returns[name][d] for d in common]) > 0]
    if len(moving) < 2:
        out["reason"] = "fewer than 2 names whose price moves in the window"
        return out
    raw = np.array([[returns[name][d] for d in common] for name in moving], dtype=float)
    out["mean_corr"] = float(np.corrcoef(raw)[~np.eye(len(moving), dtype=bool)].mean())
    apart = raw - raw.mean(axis=0, keepdims=True)
    spread = apart.std(axis=1) > _FLAT_SHARE * raw.std(axis=1)
    if int(spread.sum()) < 2:
        out["reason"] = ("the names move as one: once each date's mean return is taken out, "
                         "fewer than 2 names move apart from the others")
        return out
    corr = np.corrcoef(apart[spread])
    n, t = int(spread.sum()), len(common)
    squares = float((corr ** 2).sum())
    out.update({
        "n_eff": float(n * n / max(squares - n * (n - 1) / (t - 1), n)),
        "n_eff_raw": float(n * n / squares),
        "names": [name for name, keep in zip(moving, spread) if keep],
    })
    return out


# --------------------------------------------------------------------------- #
# The checkpoint record
# --------------------------------------------------------------------------- #


def settings() -> dict:
    """The registered settings, as the record carries them."""
    return {
        "start": IC_START.isoformat(),
        "universe_start": {u: d.isoformat() for u, d in UNIVERSE_START.items()},
        "horizons": list(HORIZONS),
        "scores": list(SCORES),
        "comparator": COMPARATOR,
        "min_names": MIN_NAMES,
        "mde_t": MDE_T,
        "nw_lag": {str(h): lag for h, lag in NW_LAG.items()},
        "n_eff_min_returns": N_EFF_MIN_RETURNS,
        "n_eff_min_dates": N_EFF_MIN_DATES,
        "n_eff_min_coverage": N_EFF_MIN_COVERAGE,
        "n_eff": ("daily close-to-close returns over the window; names with returns on less than "
                  f"{N_EFF_MIN_COVERAGE:.0%} of its dates or fewer than {N_EFF_MIN_RETURNS} returns dropped, then the "
                  "dates every kept name has; each date's mean return across the names taken out (a common move "
                  "does not change ranks); C = their correlation matrix, N names, T dates: "
                  "n_eff = N^2 / max(sum(C^2) - N(N - 1) / (T - 1), N), n_eff_raw = N^2 / sum(C^2)"),
        "main": {"score": MAIN_SCORE, "horizon": MAIN_HORIZON},
        "return": "price only: the next open to the close of the h-th session, no dividend, no cost",
    }


def universe_record(lines: Sequence[IcLine], bars: Mapping[str, Sequence[Bar]], through: date,
                    name: str = "production") -> dict:
    """One universe's checkpoint numbers, from its lines already in the window (``in_window``)."""
    by_horizon = {h: daily_ics(lines, bars, h, through) for h in HORIZONS}
    firsts = [d.first_entry for d in by_horizon.values() if d.first_entry is not None]
    lasts = [d.last_exit for d in by_horizon.values() if d.last_exit is not None]
    first, last = (min(firsts) if firsts else None), (max(lasts) if lasts else None)
    spread = effective_names(bars, tickers_of(lines), first, last, through)
    horizons: dict[str, dict] = {}
    for h, found in by_horizon.items():
        row = {score: summarise(found.ics[score], h, spread["n_eff"], found.skipped[score], found.pairs[score])
               for score in ALL_SCORES}
        row[f"{PAIRED[0]}_minus_{PAIRED[1]}"] = paired(found.ics[PAIRED[0]], found.ics[PAIRED[1]], h)
        horizons[str(h)] = row
    main = horizons[str(MAIN_HORIZON)][MAIN_SCORE]
    return {
        "lines": len(lines),
        "window": {"first": first.isoformat() if first else None, "last": last.isoformat() if last else None},
        "n_eff": spread["n_eff"],
        "n_eff_raw": spread["n_eff_raw"],
        "n_eff_dates": spread["dates"],
        "n_eff_window_dates": spread["window_dates"],
        "n_eff_reason": spread["reason"],
        "names": spread["names"],
        "mean_corr": spread["mean_corr"],
        "horizons": horizons,
        "pending": by_horizon[max(HORIZONS)].pending,
        "pending_by_horizon": {str(h): d.pending for h, d in by_horizon.items()},
        "no_price": by_horizon[max(HORIZONS)].no_price,
        "main": {
            "name": f"ic_{name}_{MAIN_SCORE}_{MAIN_HORIZON}",
            "score": MAIN_SCORE,
            "horizon": MAIN_HORIZON,
            "t": main["t"],
            "p": main["p"],
            "stats": main["stats"],
            "mean_daily_diff": main["mean_ic"],
            "days": main["days"],
        },
    }


def record(lines_by_universe: Mapping[str, Sequence[IcLine]],
           bars_by_universe: Mapping[str, Mapping[str, Sequence[Bar]]], through: date) -> dict:
    """The checkpoint record: every number of the IC report, once, through ``through``.

    Made only when ``due`` says so, and then kept unchanged. Lines after
    ``through`` and bars after it are not read. A universe with no line in
    its window yet is ``{"no_data": True}``. Each universe's ``main`` is the
    test that enters the Benjamini-Hochberg family and the Deflated Sharpe
    Ratio, with the keys the family reads (``t``, ``stats``,
    ``mean_daily_diff`` -- here the mean IC -- and ``days``).
    """
    universes: dict[str, dict] = {}
    for universe in UNIVERSES:
        lines = in_window(lines_by_universe.get(universe) or (), universe, through)
        if not lines:
            universes[universe] = {"no_data": True}
            continue
        universes[universe] = universe_record(lines, bars_by_universe.get(universe) or {}, through, universe)
    return {
        "through": through.isoformat(),
        "registered": IC_REGISTRATION.isoformat(),
        "start": IC_START.isoformat(),
        "settings": settings(),
        "universes": universes,
    }


# --------------------------------------------------------------------------- #
# The pre-registration card
# --------------------------------------------------------------------------- #


def card() -> str:
    """The pre-registration card, in Markdown, made from the constants above, for the 22 Dec 2026 checkpoint."""
    horizons = " and ".join(str(h) for h in HORIZONS)
    lags = ", ".join(f"{lag} at {h} session{'s' if h > 1 else ''}" for h, lag in NW_LAG.items())
    return "\n".join([
        "### IC test: do the model's scores rank the names in the order they then move?",
        "",
        f"Prepared on 2 Oct 2026 (the owner's item 4). Registration: the {_day(IC_REGISTRATION)} checkpoint. "
        "Shadow only: nothing is traded on it and no rule changes because of it. Code: `analysis/ic.py`.",
        "",
        f"- **Lines.** Every line the model answered (a signal about this ticker, not held), journalled on or "
        f"after **{IC_START.isoformat()}** (UTC day): the race's rule, so a line with an error written after the "
        "answer (\"webhook unreachable\", \"engine unavailable\") counts and one \"answered for\" another ticker "
        f"does not. Two universes: the production names (`logs/journal/`) and, from "
        f"**{SHADOW_START.isoformat()}**, the shadow stock universe (`logs/shadow_universe/`).",
        f"- **Scores.** The blended score (`blend.composite`) and the five dimensions "
        f"({', '.join(f'`signal.{d}_score`' for d in DIMENSIONS)}). A null score leaves the line out of that "
        "score only. Comparator: the momentum rule, +conviction when BULLISH, -conviction when BEARISH, "
        "0 when NEUTRAL (`arms.momentum`).",
        "- **What is stored.** The blended, news, technical and fundamental scores are on every answered line. "
        "The analyst score is null on bond and commodity funds (no analysts rate them, and they have no holdings "
        "roll-up). The insider score is null when the prompt had no insider, positioning or flow section. "
        "Momentum is on every answered line.",
        f"- **Return.** Entry at the Open of the first session after the line's UTC day (the race's rule); exit "
        f"at the Close of session h, the entry session counted as the first; h = {horizons}. Price only: "
        "no dividend, no cost. A return whose prices are not there yet is pending and counted.",
        f"- **Daily IC.** For each entry day, score and horizon: the Spearman rank correlation (average ranks "
        f"for ties) between the score and the return, over the names that have both. At least **{MIN_NAMES} "
        "names**, or no IC that day (the day is counted as skipped). A name twice on one entry day: the last line.",
        f"- **Reported.** Mean IC, Newey-West t (lag = horizon: {lags}), two-sided p, days, the measured "
        f"effective number of independent names (n_eff, below), and the smallest IC detectable at "
        f"**t = {MDE_T}**: measured ({MDE_T} x the Newey-West standard error) and in theory "
        f"({MDE_T} / sqrt((n_eff - 1) x days / h)). The same for momentum, and the daily difference blend minus "
        "momentum, for reading.",
        f"- **n_eff.** From the names' daily close-to-close returns over the window (first entry day to last "
        f"resolved day). A name with returns on less than **{N_EFF_MIN_COVERAGE:.0%}** of the window's dates, or "
        f"with fewer than {N_EFF_MIN_RETURNS} returns, is left out first, so one short history does not cut the "
        f"window; then only the dates every kept name has (at least {N_EFF_MIN_DATES}, or no n_eff), and a name "
        "whose price never moves is left out. The common move is taken out: each date's mean return across the "
        "names is subtracted from every name's return that date, because a move shared by every name does not "
        "change their ranks. With C the correlation matrix of what is left (N names, T dates): "
        "n_eff = N^2 / max(sum of C^2 - N(N - 1) / (T - 1), N), the participation ratio with the sampling noise "
        "of T dates taken out; the uncorrected N^2 / sum of C^2 is shown as n_eff_raw, for reading.",
        f"- **Main test (proposed; the owner confirms at registration).** The {_label(MAIN_SCORE)}'s IC at "
        f"{MAIN_HORIZON} sessions, one test per universe. It enters the Benjamini-Hochberg family and the "
        "Deflated Sharpe Ratio. Every other number is for reading only.",
        f"- **Hidden until the checkpoint.** Before {_day(IC_REGISTRATION)} only counters are shown: answered "
        "lines, lines with each score, and days. No IC value is written to any file, page or log before it. "
        "The record is made once at each checkpoint from then on and kept unchanged.",
    ])


def _label(score: str) -> str:
    return "blended score" if score == "blend" else f"{score} score"


def _day(day: date) -> str:
    return f"{day.day} {day:%b %Y}"


def _finite(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    number = float(value)
    return number if math.isfinite(number) else None


def _positive(value: Any) -> bool:
    number = _finite(value)
    return number is not None and number > 0


__all__ = [
    "ALL_SCORES", "Bar", "COMPARATOR", "COUNTER_KEYS", "DIMENSIONS", "DailyIcs", "FEW_NAMES", "Forward", "HORIZONS",
    "IC_REGISTRATION", "IC_START", "IcLine", "MAIN_HORIZON", "MAIN_SCORE", "MDE_T", "MIN_NAMES", "NO_PRICE",
    "NO_SPREAD", "NW_LAG", "N_EFF_MIN_COVERAGE", "N_EFF_MIN_DATES", "N_EFF_MIN_RETURNS", "OK", "PAIRED", "PENDING",
    "SCORES", "SHADOW_START", "UNIVERSES", "UNIVERSE_START", "bars_from_fetcher", "card", "counters", "daily_ics",
    "due", "effective_names", "forward_return", "in_window", "line_from", "mde_theory", "momentum_score",
    "newey_west_se", "paired", "read_lines", "read_universe", "record", "settings", "summarise", "tickers_of",
    "universe_record",
]
