"""The pre-registered decision gate, applied by code rather than by a reader.

``docs/horse-race-preregistration.md`` says which lines count, how many
independent days a decision needs, when the planned looks are, what bar each
look must clear, and what happens when the winner cannot beat a world index
fund. Until 24 Sep 2026 a human had to read the file and apply it to the
race's output. Every number that decides anything now lives here, is pinned
to the file by ``tests/test_horse_race.py``, and is applied by
``analysis/horse_race.py`` on every run.

Pure arithmetic over numbers the race has already computed: no prices, no
files, no clock. Read-only in every direction.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Iterable, Mapping, Optional, Sequence

from config.market_calendar import is_trading_day

#: Lines journalled on or after this UTC day are the decision window. The
#: model arm changed on this day (Amendment 1): earlier lines were answered
#: by a different model and cannot be added to the new one's days.
DECISION_CUTOFF = date(2026, 9, 23)

#: The registered horizon, in sessions. Also the length of the block that
#: makes one independent day: trades opened on consecutive entry days share
#: sessions of market until they are this many entry days apart.
REGISTERED_HORIZON = 3

#: Minimum sample before the final decision, in independent days.
MIN_INDEPENDENT_DAYS = 60

#: The three planned looks: (independent days, the Newey-West t bar at that
#: look). O'Brien-Fleming boundaries for three equally spaced looks at an
#: overall two-sided alpha of 0.05: 2.004 x sqrt(3/k) for k = 1, 2, 3. The
#: last is the registered 2.0. Amendment 2026-09-24 (planned checkpoints).
CHECKPOINTS: tuple[tuple[int, float], ...] = ((20, 3.47), (40, 2.45), (60, 2.00))

#: The world index fund every winner must also beat (Amendment 2026-09-24,
#: index-first). Held, not traded: no stop, no per-window cost.
INDEX_TICKER = "VT"

#: A day the price source has no index bar for is an outage -- the look
#: waits -- until the source has published this many later sessions without
#: it. After that it is a gap that will not be filled (the source printed a
#: week of VT after it and never that day), and the day is left out of the
#: index comparison only, for every arm alike. Without this, one missing row
#: would hold every look unreadable for good. Amendment 2026-09-24 (bug fix):
#: the source had no VT bar for 22 Sep 2026 while it had SPY's.
INDEX_GAP_SETTLE_SESSIONS = 5

#: Keep-rule condition 3: the model's mean daily net return must sit above
#: this percentile of the coin flip drawn on its own lines. Unchanged at
#: every look.
COIN_FLIP_PERCENTILE = 95.0

#: The fourth outcome (Amendment 2026-09-24): no arm trades.
NO_ARM = "none"

OUTCOME_TEXT = {
    "model": "keep the model",
    "momentum": "replace the model with momentum",
    "hybrid": "replace the model with the hybrid",
    NO_ARM: "no arm trades -- hold the index (VT); the repo stays for learning and research",
}

#: The owner's model-watch triggers (24 Sep 2026). Tripping one means: stop
#: and tell the owner. Nothing here reverts, switches or trades anything.
WATCH_DAYS = 5
WATCH_MAX_FAILED_SHARE = 0.05
#: Trigger (c) counts from this cycle day (Amendment 2026-09-24, the owner's
#: decision after it tripped on the 2026-09-24 key outage). Earlier days are
#: shown, never counted.
FAILURE_WATCH_START = date(2026, 9, 25)
#: The same-day phone alert: more than this share of one run's model calls
#: failed, setup and model errors together (``analysis.health``).
RUN_ALERT_FAILED_SHARE = 0.20

#: Trigger (a) was a one-time check on the zero-shorts replay, not on the
#: journal, so nothing here computes it. It tripped and the owner kept
#: gpt-oss on this day (Amendment 2026-09-25): the model arm is effectively
#: long-only. It is closed. Kept as constants so the race prints the owner's
#: record rather than a paraphrase of it.
TRIGGER_A_CLOSED = date(2026, 9, 25)
#: What the replay found: (lines gpt-oss shorted, of the lines Opus shorted).
TRIGGER_A_RESULT = (1, 31)

#: Trigger (b) -- 5 answered cycle days in a row with no SHORT while SPY
#: fell -- was retired on this day (the owner's decision, Amendment
#: 2026-09-26). The model is long-only by the owner's decision of 25 Sep, so
#: (b) could only ever say that SPY fell. Nothing computes it any more; it is
#: replaced by trigger (d), the paper account's drawdown.
TRIGGER_B_RETIRED = date(2026, 9, 26)

#: Trigger (d), the real paper account (Amendment 2026-09-26): its closing
#: equity from this day on. Also the base of the comparison with VT: the
#: first day of the period with a close for both the account and VT (the
#: period starts here, and the price source has no VT bar for 22 Sep).
DRAWDOWN_START = date(2026, 9, 23)
#: (d) trips when equity is more than this far below its highest close since
#: ``DRAWDOWN_START``: equity < peak x (1 - 0.08).
MAX_DRAWDOWN = 0.08
#: (d) trips when the account's return since the base close trails VT's over
#: the same days by more than this, in percentage points of return (0.05 is
#: 5 points): account return - VT return < -0.05.
MAX_BEHIND_VT = 0.05


# --------------------------------------------------------------------------- #
# Which lines, and how many independent days they make
# --------------------------------------------------------------------------- #


def in_window(day: date, cutoff: Optional[date] = None) -> bool:
    """Whether a line journalled on ``day`` (UTC) counts toward the decision."""
    return day >= (cutoff or DECISION_CUTOFF)


def independent_days(entry_days: int, horizon: int = REGISTERED_HORIZON) -> int:
    """Complete, non-overlapping blocks of ``horizon`` scored entry days.

    Counted down, never up: 59 entry days are 19 independent days, not 20,
    because the 20th block is not complete. This is what makes "60
    independent days" the same thing as "180 entry days".
    """
    return max(0, entry_days) // max(1, horizon)


def entry_days_needed(independent: int, horizon: int = REGISTERED_HORIZON) -> int:
    return independent * max(1, horizon)


# --------------------------------------------------------------------------- #
# When a look should be readable
# --------------------------------------------------------------------------- #


def next_trading_day(day: date) -> date:
    probe = day + timedelta(days=1)
    while not is_trading_day(probe):
        probe += timedelta(days=1)
    return probe


def trading_days_after(day: date, n: int) -> date:
    """The ``n``-th trading day after ``day`` (``day`` itself when ``n`` is 0)."""
    for _ in range(max(0, n)):
        day = next_trading_day(day)
    return day


def estimated_readable(
    target_entry_days: int, known_entry_days: Sequence[date],
    horizon: int = REGISTERED_HORIZON, cutoff: Optional[date] = None,
    last_cycle_day: Optional[date] = None,
) -> date:
    """The trading day a look's last trades close, if nothing else is lost.

    ``known_entry_days`` are the entry days the journal already implies --
    the session after every cycle day in the window that produced at least
    one answered line -- scored or still pending. A cycle day lost to an
    outage is simply absent from it, which is how a lost day pushes every
    later look back by one. Beyond the known days, every trading day is
    assumed to be an entry day. The look is readable at the close of the
    last of its entry days' horizon bars.

    ``last_cycle_day`` is the latest cycle day the journal has at all,
    answered or not. The entry day it implies is spoken for either way --
    an entry day if it produced an answer, a lost day if it did not -- so
    the days still to come start after it.
    """
    known = sorted(set(known_entry_days))
    if target_entry_days <= len(known):
        last_entry = known[target_entry_days - 1]
    else:
        start = known[-1] if known else (cutoff or DECISION_CUTOFF)
        if last_cycle_day is not None:
            start = max(start, next_trading_day(last_cycle_day))
        last_entry = trading_days_after(start, target_entry_days - len(known))
    return trading_days_after(last_entry, max(0, horizon - 1))


# --------------------------------------------------------------------------- #
# One look
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class LookInputs:
    """Everything one look reads, computed on that look's own entry days only."""

    entry_days: int
    t_model_momentum: Optional[float]
    t_model_hybrid: Optional[float]
    t_hybrid_momentum: Optional[float]
    #: The model's mean daily net return and the coin flip's 95th percentile
    #: of the same number, drawn on the model's own lines.
    model_mean: Optional[float]
    model_band_high: Optional[float]
    #: Newey-West t of (arm minus the index), per arm, over the same days.
    t_vs_index: Mapping[str, Optional[float]] = field(default_factory=dict)
    #: Days the index could be priced on, and days it could not yet (an
    #: outage: the look waits for them).
    index_days: int = 0
    index_missing: int = 0
    #: Days the source will not price: a missing index bar with at least
    #: ``INDEX_GAP_SETTLE_SESSIONS`` later bars published. Left out of the
    #: index comparison; they do not hold the look.
    index_gaps: int = 0
    #: Why the look cannot be read tonight, if it cannot: a price the race
    #: needs for the look's own days did not arrive. A data outage is never
    #: allowed to read as a result; the look waits for the data instead.
    unreadable: Optional[str] = None


@dataclass(frozen=True)
class Look:
    independent: int
    bar: float
    final: bool
    #: ``None`` until the look's entry days have all been scored.
    inputs: Optional[LookInputs] = None
    #: The arm the current rule picks at this look's bar, before the index
    #: rule; ``None`` when this look decides nothing.
    candidate: Optional[str] = None
    #: What is decided: an arm, ``NO_ARM``, or ``None`` (no decision here).
    outcome: Optional[str] = None
    reason: str = ""

    @property
    def reached(self) -> bool:
        return self.inputs is not None

    @property
    def decided(self) -> bool:
        return self.outcome is not None


def _above(t: Optional[float], bar: float) -> bool:
    return t is not None and t > bar


def _below(t: Optional[float], bar: float) -> bool:
    return t is not None and t < -bar


def decide(inputs: LookInputs, bar: float, final: bool) -> tuple[Optional[str], Optional[str], str]:
    """``(candidate, outcome, reason)`` for one look, per the registration.

    The keep rule (section 5), with ``bar`` in place of 2.0 for both paired
    tests: the model beats momentum and the hybrid at the bar, and its mean
    daily net return is above the 95th percentile of its own coin flip.

    If it is not kept, the replacement is momentum, unless the hybrid beats
    momentum at the bar. At the final look that is the answer. At an earlier
    look nothing is decided unless the model is WORSE than that replacement
    at the bar -- an early stop needs its bar met in the direction it stops.

    Whatever the candidate, it must then beat the index at the same bar, or
    no arm trades (the index-first rule, applied at every look). At the
    final look that is the whole of it: the burden is on the arm. At an
    earlier look the index test must be decisive too, in the direction it
    stops -- the candidate beats the index at t > bar (trade it), or trails
    it at t < -bar (hold the index) -- or the look decides nothing and the
    race goes on to the next one.
    """
    problem = inputs.unreadable
    if problem is None and inputs.index_missing:
        problem = f"{INDEX_TICKER} could not be priced on {inputs.index_missing} of the look's days"
    if problem is not None:
        return None, None, f"this look cannot be read tonight: {problem}"

    keep = (
        _above(inputs.t_model_momentum, bar)
        and _above(inputs.t_model_hybrid, bar)
        and inputs.model_mean is not None
        and inputs.model_band_high is not None
        and inputs.model_mean > inputs.model_band_high
    )
    replacement = "hybrid" if _above(inputs.t_hybrid_momentum, bar) else "momentum"
    if keep:
        candidate, why = "model", f"the model beat momentum and the hybrid at t > {bar:.2f} and its coin flip"
    elif final:
        candidate = replacement
        why = (f"the model did not meet the keep rule; the replacement is {replacement}"
               + (f" (the hybrid beat momentum at t > {bar:.2f})" if replacement == "hybrid" else ""))
    else:
        against = inputs.t_model_momentum if replacement == "momentum" else inputs.t_model_hybrid
        if not _below(against, bar):
            return None, None, (
                f"no early stop: neither 'model better than both' nor 'model worse than "
                f"{replacement}' clears t > {bar:.2f}"
            )
        candidate = replacement
        why = f"the model was worse than {replacement} at t < -{bar:.2f}"

    t_index = inputs.t_vs_index.get(candidate)
    shown = "n/a" if t_index is None else f"{t_index:.2f}"
    if _above(t_index, bar):
        return candidate, candidate, f"{why}; it also beat {INDEX_TICKER} at t > {bar:.2f} (t = {shown})"
    if final:
        return candidate, NO_ARM, (
            f"{why}; but it did not beat {INDEX_TICKER} at t > {bar:.2f} (t = {shown}), "
            "so no arm trades"
        )
    if _below(t_index, bar):
        return candidate, NO_ARM, (
            f"{why}; but it trailed {INDEX_TICKER} at t < -{bar:.2f} (t = {shown}), "
            "so no arm trades"
        )
    return candidate, None, (
        f"{why}; but against {INDEX_TICKER} it cleared neither t > {bar:.2f} nor "
        f"t < -{bar:.2f} (t = {shown}), so this look decides nothing"
    )


def evaluate(inputs_by_look: Mapping[int, Optional[LookInputs]]) -> list[Look]:
    """Every planned look, in order, decided where it has been reached.

    A look after one that already decided is still computed and shown, but
    the race's answer is the first look that decided: there are no
    decisions between looks, and none after a stop.
    """
    looks: list[Look] = []
    decided_at: Optional[int] = None
    for independent, bar in CHECKPOINTS:
        final = independent == CHECKPOINTS[-1][0]
        inputs = inputs_by_look.get(independent)
        if inputs is None:
            looks.append(Look(independent, bar, final))
            continue
        if decided_at is not None:
            looks.append(Look(independent, bar, final, inputs, None, None,
                              f"the race was already decided at the {decided_at}-day look; "
                              "shown for reading only"))
            continue
        candidate, outcome, reason = decide(inputs, bar, final)
        looks.append(Look(independent, bar, final, inputs, candidate, outcome, reason))
        if outcome is not None:
            decided_at = independent
    return looks


def first_decision(looks: Sequence[Look]) -> Optional[Look]:
    return next((look for look in looks if look.decided), None)


def next_look(looks: Sequence[Look]) -> Optional[Look]:
    return next((look for look in looks if not look.reached), None)


def status_line(independent: int, looks: Sequence[Look]) -> str:
    """The header line the owner asked for, word for word until a decision."""
    head = (f"independent days since {DECISION_CUTOFF.isoformat()}: {min(independent, MIN_INDEPENDENT_DAYS)} "
            f"of {MIN_INDEPENDENT_DAYS} (= {entry_days_needed(MIN_INDEPENDENT_DAYS)} trading days)")
    decided = first_decision(looks)
    if decided is None:
        return f"{head} — NO DECISION YET"
    kind = "FINAL" if decided.final else f"EARLY STOP AT {decided.independent}"
    return f"{head} — {kind}: {OUTCOME_TEXT[decided.outcome].upper()}"


# --------------------------------------------------------------------------- #
# The index's own windows
# --------------------------------------------------------------------------- #


# --------------------------------------------------------------------------- #
# O'Brien-Fleming bars for any spacing of the looks
# --------------------------------------------------------------------------- #


def _crossing(bars: Sequence[float], fractions: Sequence[float], points: int) -> float:
    """P(|Z_k| >= bars[k] at some look) with no effect, by exact recursion on a grid.

    Z_k = S(t_k) / sqrt(t_k) for a Brownian motion S, the joint law of a
    statistic read at information fractions t_1 < ... < t_K = 1. The density
    of S over the region still running is carried from one look to the
    next by the normal kernel of the increment (Armitage, McPherson and Rowe
    1969), integrated by the trapezoid rule.
    """
    import numpy as np

    def phi(x):
        return np.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)

    def tail(x):
        return 0.5 * np.vectorize(math.erfc)(np.asarray(x) / math.sqrt(2.0))

    def weights(grid):
        w = np.full(len(grid), grid[1] - grid[0])
        w[0] = w[-1] = w[0] / 2.0
        return w

    edge = bars[0] * math.sqrt(fractions[0])
    total = 2.0 * float(tail(bars[0]))
    grid = np.linspace(-edge, edge, points)
    density = phi(grid / math.sqrt(fractions[0])) / math.sqrt(fractions[0])
    for k in range(1, len(fractions)):
        sd = math.sqrt(fractions[k] - fractions[k - 1])
        edge = bars[k] * math.sqrt(fractions[k])
        mass = weights(grid) * density
        total += float(np.sum(mass * (tail((edge - grid) / sd) + tail((edge + grid) / sd))))
        if k < len(fractions) - 1:
            new = np.linspace(-edge, edge, points)
            density = (phi((new[:, None] - grid[None, :]) / sd) / sd) @ mass
            grid = new
    return total


def obrien_fleming_bars(information: Sequence[float], alpha: float = 0.05, points: int = 1001) -> list[float]:
    """The two-sided O'Brien-Fleming bars for looks at the given amounts of information.

    Bar k is C / sqrt(t_k), t_k the look's share of the final information,
    with C set so the chance of crossing any bar when nothing is there is
    exactly ``alpha``. Three equal looks give 3.471, 2.454, 2.004 -- the
    race's ``CHECKPOINTS``; the fund test's own looks give its own bars.
    """
    fractions = [x / information[-1] for x in information]
    low, high = 1.0, 5.0
    for _ in range(50):
        c = (low + high) / 2.0
        if _crossing([c / math.sqrt(t) for t in fractions], fractions, points) > alpha:
            low = c
        else:
            high = c
    c = (low + high) / 2.0
    return [c / math.sqrt(t) for t in fractions]


def index_gaps(bars: Sequence[tuple[date, float, float, float]], days: Sequence[date]) -> set[date]:
    """The entry days the index has no bar for and never will: see ``INDEX_GAP_SETTLE_SESSIONS``."""
    have = {bar[0] for bar in bars}
    out = set()
    for day in days:
        if day not in have and sum(1 for d in have if d > day) >= INDEX_GAP_SETTLE_SESSIONS:
            out.add(day)
    return out


def index_window_return(
    bars: Sequence[tuple[date, float, float, float]], entry_day: date, horizon: int,
) -> Optional[float]:
    """The index bought at ``entry_day``'s open and held ``horizon`` sessions.

    ``bars`` are ``(day, open, close, dividend)`` in date order, final bars
    only. The same window every arm's trade opened that day is measured on:
    the open of the entry bar to the close of the horizon bar. No stop and
    no cost -- holding the index is one purchase, not a trade every three
    sessions -- and a dividend going ex inside the window is added back,
    because the close alone would understate what holding it paid. A
    dividend going ex on the entry day itself is not: the open is already
    ex-dividend. ``None`` when the entry bar or the horizon bar is missing.
    """
    index = next((i for i, bar in enumerate(bars) if bar[0] == entry_day), None)
    if index is None:
        return None
    last = index + max(1, horizon) - 1
    if last >= len(bars):
        return None
    opened = bars[index][1]
    if opened <= 0:
        return None
    paid = sum(bar[3] for bar in bars[index + 1:last + 1])
    return (bars[last][2] + paid) / opened - 1.0


# --------------------------------------------------------------------------- #
# The owner's model-watch triggers
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class WatchDay:
    """One cycle day of the model arm, as the journal recorded it."""

    day: date
    #: Names the model was asked about (not held).
    asked: int
    #: Of those, no usable answer because of the model: a timeout, a server
    #: error, an empty or off-schema answer. What trigger (c) counts.
    failed: int
    #: Of the answers, how many were SHORT.
    shorts: int
    #: Of those asked, no answer because of our own setup: a bad key, an
    #: account or model name the provider refused (``analysis.call_errors``).
    #: Shown, never counted by trigger (c).
    setup_failed: int = 0

    @property
    def attempted(self) -> int:
        """Calls that reached the model: what trigger (c) divides by."""
        return self.asked - self.setup_failed

    @property
    def answered(self) -> int:
        return self.asked - self.failed - self.setup_failed


@dataclass(frozen=True)
class Trip:
    first: date
    last: date
    detail: str


def failure_trips(days: Sequence[WatchDay], max_names_per_day: Optional[int] = None) -> list[Trip]:
    """Trigger (c): model errors above 5% of the calls that reached the model, over 5 cycle days.

    Setup errors (``WatchDay.setup_failed``) are not counted, and days
    before ``FAILURE_WATCH_START`` are not judged (Amendment 2026-09-24).

    With fewer than 5 cycle days so far, the run of days there are is still
    judged when the answer is already certain: if the failures exceed 5% of
    the most calls a 5-day window could possibly hold (the days so far, plus
    ``max_names_per_day`` for each day still to come), no later day can
    bring the window back under. Otherwise it waits for the fifth day.
    """
    days = [d for d in days if d.day >= FAILURE_WATCH_START]
    trips: list[Trip] = []
    if days and len(days) < WATCH_DAYS and max_names_per_day:
        asked = sum(d.attempted for d in days)
        failed = sum(d.failed for d in days)
        ceiling = asked + max_names_per_day * (WATCH_DAYS - len(days))
        if failed > WATCH_MAX_FAILED_SHARE * ceiling:
            trips.append(Trip(days[0].day, days[-1].day,
                              f"{failed} of {asked} calls failed in the first {len(days)} cycle day(s); "
                              f"above 5% of any {WATCH_DAYS}-day window that contains them"))
    for i in range(len(days) - WATCH_DAYS + 1):
        run = days[i:i + WATCH_DAYS]
        asked = sum(d.attempted for d in run)
        failed = sum(d.failed for d in run)
        if asked and failed / asked > WATCH_MAX_FAILED_SHARE:
            trips.append(Trip(run[0].day, run[-1].day,
                              f"{failed} of {asked} calls failed ({failed / asked:.1%})"))
    return trips


def _usable(value: object) -> bool:
    """A price or an equity that can be divided by: a finite number above zero."""
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and value > 0)


@dataclass(frozen=True)
class DrawdownDay:
    """One day of trigger (d): the account's equity against its peak, and against VT."""

    day: date
    equity: float
    #: The highest closing equity from ``DRAWDOWN_START`` to this day,
    #: this day included, and the day it was set.
    peak: float
    peak_day: date
    #: Both since the base close (``DRAWDOWN_START``). ``None`` on a day VT
    #: has no final close, or when either base close is missing: that day's
    #: VT part is not judged.
    account_return: Optional[float] = None
    vt_return: Optional[float] = None

    @property
    def drawdown(self) -> float:
        """``equity / peak - 1``: 0 at a new high, -0.05 five per cent below it."""
        return self.equity / self.peak - 1.0

    @property
    def gap(self) -> Optional[float]:
        """Account return minus VT return, as a fraction (-0.05 is 5 points behind)."""
        if self.account_return is None or self.vt_return is None:
            return None
        return self.account_return - self.vt_return

    # Both compared rounded to ten places, so float noise can never make
    # exactly 8% (or exactly 5 points) read as more than it.
    @property
    def too_deep(self) -> bool:
        return round(self.drawdown, 10) < -MAX_DRAWDOWN

    @property
    def too_far_behind(self) -> bool:
        gap = self.gap
        return gap is not None and round(gap, 10) < -MAX_BEHIND_VT


@dataclass(frozen=True)
class DrawdownWatch:
    """Trigger (d) over every day of the period, and the days it tripped on."""

    days: tuple[DrawdownDay, ...]
    trips: tuple[Trip, ...]
    #: Why the VT part can judge no day at all, if it cannot: a base close
    #: is missing. ``None`` when it judges every day VT has a final close.
    vt_problem: Optional[str] = None

    @property
    def latest(self) -> Optional[DrawdownDay]:
        return self.days[-1] if self.days else None

    @property
    def latest_vt(self) -> Optional[DrawdownDay]:
        """The latest day the VT part was judged on."""
        return next((d for d in reversed(self.days) if d.gap is not None), None)


def drawdown_watch(equity: Mapping[date, float], vt_close: Mapping[date, float]) -> DrawdownWatch:
    """Trigger (d): the real paper account, more than 8% below its peak or 5 points behind VT.

    The owner's decision of 26 Sep 2026, replacing (b). A trip means stop and
    tell the owner; nothing here reverts, switches or trades anything.

    ``equity`` is the account's closing equity per trading day, as the
    heartbeat recorded Alpaca's daily portfolio history in
    ``logs/account.jsonl``, plus the latest record's own equity for its day
    when that day is newer than every close (so the latest day can be an
    intraday number). ``vt_close`` is VT's close per day, final closes only.
    Days before ``DRAWDOWN_START`` are ignored in both, and so is any value
    that is not a finite number above zero.

    Drawdown: the peak is the highest closing equity from ``DRAWDOWN_START``
    to the day, that day included. The day trips when equity < peak x (1 -
    ``MAX_DRAWDOWN``), i.e. more than 8% below the peak; exactly 8% does not.

    Behind VT: both returns are measured from the same base, the close of
    ``DRAWDOWN_START`` (2026-09-23) -- the first day of the period with a
    close for both, since the price source has no VT bar for 22 Sep -- to
    the same day's close: account equity / base equity - 1 and VT close /
    base VT close - 1. The day trips when account return - VT return <
    -``MAX_BEHIND_VT``, i.e. more than 5 percentage points behind; exactly 5
    does not. A day VT has no final close for is not judged on this part
    (the drawdown part still is); if either base close is missing, no day is.

    Every day that trips is one ``Trip``, both reasons in its detail when
    both apply. The latest values are in ``days`` whether or not anything
    tripped, so the owner can see how close it is.
    """
    closes = sorted((day, float(value)) for day, value in equity.items()
                    if day >= DRAWDOWN_START and _usable(value))
    vt = {day: float(value) for day, value in vt_close.items() if day >= DRAWDOWN_START and _usable(value)}
    base_account = dict(closes).get(DRAWDOWN_START)
    base_vt = vt.get(DRAWDOWN_START)
    vt_problem: Optional[str] = None
    if base_account is None:
        vt_problem = f"the account has no close for {DRAWDOWN_START.isoformat()}, the base"
    elif base_vt is None:
        vt_problem = f"no final {INDEX_TICKER} close for {DRAWDOWN_START.isoformat()}, the base"

    days: list[DrawdownDay] = []
    trips: list[Trip] = []
    peak, peak_day = 0.0, DRAWDOWN_START
    for day, value in closes:
        if value > peak:
            peak, peak_day = value, day
        account_return = vt_return = None
        if vt_problem is None and day in vt:
            account_return = value / base_account - 1.0
            vt_return = vt[day] / base_vt - 1.0
        row = DrawdownDay(day, value, peak, peak_day, account_return, vt_return)
        days.append(row)
        reasons = []
        if row.too_deep:
            reasons.append(f"equity {value:,.2f} is {-row.drawdown:.2%} below its peak {peak:,.2f} "
                           f"of {peak_day.isoformat()} (more than {MAX_DRAWDOWN:.0%})")
        if row.too_far_behind:
            reasons.append(f"the account is {-row.gap * 100:.2f} points behind {INDEX_TICKER} since the "
                           f"{DRAWDOWN_START.isoformat()} close (account {account_return:+.2%}, "
                           f"{INDEX_TICKER} {vt_return:+.2%}; more than {MAX_BEHIND_VT * 100:.0f} points)")
        if reasons:
            trips.append(Trip(day, day, "; ".join(reasons)))
    return DrawdownWatch(tuple(days), tuple(trips), vt_problem)


def drawdown_trips(equity: Mapping[date, float], vt_close: Mapping[date, float]) -> list[Trip]:
    """Trigger (d)'s trips only: see ``drawdown_watch`` for the definitions."""
    return list(drawdown_watch(equity, vt_close).trips)


def known_entry_days(cycle_days: Iterable[date]) -> list[date]:
    """The entry day each answered cycle day implies: the next session."""
    return sorted({next_trading_day(day) for day in cycle_days})


__all__ = [
    "CHECKPOINTS",
    "COIN_FLIP_PERCENTILE",
    "DECISION_CUTOFF",
    "DRAWDOWN_START",
    "DrawdownDay",
    "DrawdownWatch",
    "FAILURE_WATCH_START",
    "INDEX_GAP_SETTLE_SESSIONS",
    "INDEX_TICKER",
    "Look",
    "LookInputs",
    "MAX_BEHIND_VT",
    "MAX_DRAWDOWN",
    "MIN_INDEPENDENT_DAYS",
    "NO_ARM",
    "OUTCOME_TEXT",
    "REGISTERED_HORIZON",
    "RUN_ALERT_FAILED_SHARE",
    "TRIGGER_A_CLOSED",
    "TRIGGER_A_RESULT",
    "TRIGGER_B_RETIRED",
    "Trip",
    "WATCH_DAYS",
    "WATCH_MAX_FAILED_SHARE",
    "WatchDay",
    "decide",
    "drawdown_trips",
    "drawdown_watch",
    "entry_days_needed",
    "estimated_readable",
    "evaluate",
    "failure_trips",
    "first_decision",
    "in_window",
    "independent_days",
    "index_gaps",
    "index_window_return",
    "known_entry_days",
    "next_look",
    "next_trading_day",
    "obrien_fleming_bars",
    "status_line",
    "trading_days_after",
]
