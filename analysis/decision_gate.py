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
    #: Days the index could be priced on, and days it could not.
    index_days: int = 0
    index_missing: int = 0


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
    for independent, bar in CHECKPOINTS:
        final = independent == CHECKPOINTS[-1][0]
        inputs = inputs_by_look.get(independent)
        if inputs is None:
            looks.append(Look(independent, bar, final))
            continue
        candidate, outcome, reason = decide(inputs, bar, final)
        looks.append(Look(independent, bar, final, inputs, candidate, outcome, reason))
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
    #: Of those, no usable answer: a failed or timed-out call.
    failed: int
    #: Of the answers, how many were SHORT.
    shorts: int

    @property
    def answered(self) -> int:
        return self.asked - self.failed


@dataclass(frozen=True)
class Trip:
    first: date
    last: date
    detail: str


def failure_trips(days: Sequence[WatchDay]) -> list[Trip]:
    """Trigger (c): failed or timed-out calls above 5% of names over 5 cycle days."""
    trips: list[Trip] = []
    for i in range(len(days) - WATCH_DAYS + 1):
        run = days[i:i + WATCH_DAYS]
        asked = sum(d.asked for d in run)
        failed = sum(d.failed for d in run)
        if asked and failed / asked > WATCH_MAX_FAILED_SHARE:
            trips.append(Trip(run[0].day, run[-1].day,
                              f"{failed} of {asked} calls failed ({failed / asked:.1%})"))
    return trips


def no_short_trips(days: Sequence[WatchDay], spy_close: Mapping[date, float]) -> list[Trip]:
    """Trigger (b): 5 answered cycle days in a row with no SHORT while SPY fell.

    A day with no answered line at all is skipped rather than counted: a
    lost day says nothing about whether the model would have shorted. "SPY
    fell" is the close of the last day against the last close before the
    first. A run whose closes are not final yet is not judged.
    """
    answered = [d for d in days if d.answered > 0]
    closes = sorted(spy_close.items())
    trips: list[Trip] = []
    for i in range(len(answered) - WATCH_DAYS + 1):
        run = answered[i:i + WATCH_DAYS]
        if any(d.shorts for d in run):
            continue
        before = [price for day, price in closes if day < run[0].day]
        end = spy_close.get(run[-1].day)
        if not before or end is None:
            continue
        if end < before[-1]:
            trips.append(Trip(run[0].day, run[-1].day,
                              f"no SHORT on {WATCH_DAYS} answered days while SPY fell "
                              f"{end / before[-1] - 1.0:+.2%}"))
    return trips


def known_entry_days(cycle_days: Iterable[date]) -> list[date]:
    """The entry day each answered cycle day implies: the next session."""
    return sorted({next_trading_day(day) for day in cycle_days})


__all__ = [
    "CHECKPOINTS",
    "COIN_FLIP_PERCENTILE",
    "DECISION_CUTOFF",
    "INDEX_TICKER",
    "Look",
    "LookInputs",
    "MIN_INDEPENDENT_DAYS",
    "NO_ARM",
    "OUTCOME_TEXT",
    "REGISTERED_HORIZON",
    "Trip",
    "WATCH_DAYS",
    "WATCH_MAX_FAILED_SHARE",
    "WatchDay",
    "decide",
    "entry_days_needed",
    "estimated_readable",
    "evaluate",
    "failure_trips",
    "first_decision",
    "in_window",
    "independent_days",
    "index_window_return",
    "known_entry_days",
    "next_look",
    "next_trading_day",
    "no_short_trips",
    "status_line",
    "trading_days_after",
]
