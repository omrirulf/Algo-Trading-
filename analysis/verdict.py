"""The checkpoint verdict: one look of the race or of the fund test, as a table.

The owner's item 6 of 3 Oct 2026 asked for an automatic checkpoint verdict
for both the race and the fund test; he approved the layout on 6 Oct 2026
(``docs/research/checkpoint-verdict-plan.md``, all five readings "yes", and
two additions). This module is the one place that turns a look into that
table: six columns (# · Rule (section) · What is measured · Value · Bar ·
Result), rows 1 to 9, and a last "→" row that carries the verdict.

It decides nothing of its own. The race's decision is
``analysis.decision_gate.decide``, word for word; the fund test's decision
is the same function at the fund test's own bar (section 11.6, "exactly as
section 5a"). The rows are recomputed from the look's numbers with the
decision gate's own predicates (``above``, ``below``,
``after_tax_result``), and the outcome the rows add up to is checked
against ``decide`` every time a table is made: a table that disagreed with
the decision would raise instead of being written.

The combined line (section 11.8, owner reading 1) is ``combined``: real
money only if the same arm wins both tests, the index as soon as either
says "no arm trades" or the two pick different arms, and "no decision yet"
otherwise.

The owner's Addition 2 (6 Oct 2026): printed examples made from test data
(``tests/verdict_examples.py``) must never reach a real output. A table
made with ``test_data=True`` is marked "TEST DATA" on every line it renders
and cannot be written: ``table_json``, ``render_real`` and ``block`` raise
on it. The real builders refuse any date outside the experiment
(``check_dates``: 2026-09-23 to 2027-12-31), so the examples, whose dates
are all in 2099, cannot be built into a real table either.

Pure: no prices, no files, no clock, no network.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, datetime
from typing import Final, Mapping, Optional, Sequence, Union

from analysis import decision_gate as gate
from analysis.decision_gate import AfterTax, Look, LookInputs
from shadow import schedule

# --------------------------------------------------------------------------- #
# Vocabulary (the plan's section 2, approved 6 Oct 2026)
# --------------------------------------------------------------------------- #

#: The leading word of a result cell. A cell may carry a short note after a
#: colon or a comma, as the plan's tables do ("FAIL, so momentum").
PASS: Final[str] = "PASS"
FAIL: Final[str] = "FAIL"
#: The row's record is not made yet (the after-tax record): the look waits.
WAITING: Final[str] = "WAITING"
#: The after-tax record was made without a fund: calibration had not passed.
CANNOT_PASS: Final[str] = "CANNOT PASS"
#: No arm reached that step.
NOT_APPLIED: Final[str] = "NOT APPLIED"
#: A row that does not apply at this look (the early stop at the final look).
NA: Final[str] = "n/a"
#: The downturn row (section 5d) labels a verdict; it never decides one.
LABEL: Final[str] = "LABEL"
#: Row 4's two results.
KEPT: Final[str] = "KEPT"
NOT_KEPT: Final[str] = "NOT KEPT"
RESULT_WORDS: Final[tuple[str, ...]] = (PASS, FAIL, WAITING, CANNOT_PASS, NOT_APPLIED, NA, LABEL, KEPT, NOT_KEPT)

#: What the block, the JSON and the page say before any look, and between
#: looks after one that decided nothing (the plan's (iv)).
NO_DECISION_YET: Final[str] = "no decision yet"

#: The two kinds of table.
RACE: Final[str] = "race"
FUND_TEST: Final[str] = "fund_test"

#: The six columns, in the plan's order, and the verdict row's number.
COLUMNS: Final[tuple[str, ...]] = ("#", "Rule (section)", "What is measured", "Value", "Bar", "Result")
VERDICT_ROW: Final[str] = "→"
#: The true minus sign the plan prints (``t = −3.62``), never a hyphen.
MINUS: Final[str] = "−"
#: An empty value: a row with nothing to measure at this look.
DASH: Final[str] = "—"

#: What a table is, in one word, beside its verdict text: the freezing rule
#: (only a complete table is frozen) and the page read it.
DECIDED: Final[str] = "decided"
NO_DECISION: Final[str] = "no_decision"
STATUS_WAITING: Final[str] = "waiting"
UNREADABLE: Final[str] = "unreadable"
READING_ONLY: Final[str] = "reading_only"
SKIPPED: Final[str] = "skipped"
OWNER: Final[str] = "owner"
STATUSES: Final[tuple[str, ...]] = (DECIDED, NO_DECISION, STATUS_WAITING, UNREADABLE, READING_ONLY, SKIPPED, OWNER)

#: The number of planned looks, the same for both tests (sections 5a, 11.7).
LOOKS: Final[int] = len(gate.CHECKPOINTS)

#: The owner's Addition 2 (6 Oct 2026): how a table made from test data is
#: marked, on every line it renders, and the last line under it.
TEST_DATA: Final[str] = "TEST DATA"
TEST_DATA_FOOTER: Final[str] = "TEST DATA: every number above is made up."

#: The experiment's dates (owner Addition 2, the guard): a real table holds
#: no date before the decision window opens (``DECISION_CUTOFF``, Amendment
#: 1) or after the end of 2027 (the final look is planned for June 2027;
#: section 9's verdict follows it). Only a test-data table may hold others.
EXPERIMENT_START: Final[date] = gate.DECISION_CUTOFF
EXPERIMENT_END: Final[date] = date(2027, 12, 31)

#: The race's rows 1, 2, 5 and 7 are read at this Newey-West lag (section 5:
#: the registered horizon of three sessions).
RACE_LAG: Final[int] = gate.REGISTERED_HORIZON

#: The fund test's outcome words (the plan's (ii)), beside the race's
#: ``decision_gate.OUTCOME_TEXT``.
FUND_OUTCOME_TEXT: Final[Mapping[str, str]] = {
    "model": "keep the model fund",
    "momentum": "replace the model fund with the momentum fund",
    "hybrid": "replace the model fund with the hybrid fund",
    gate.NO_ARM: "no arm trades: hold the index",
}

#: An arm as the combined line names it.
ARM_NAMES: Final[Mapping[str, str]] = {"model": "the model", "momentum": "momentum", "hybrid": "the hybrid"}

#: The fund test's six paired before-tax tests, as the look record names
#: them under ``tests`` (section C of the build): the first fund minus the
#: second, daily net returns, Newey-West t at lag 5, cut at the look's
#: window end. ``fund_pair(a, b)`` gives the key.
FUND_TEST_PAIRS: Final[tuple[tuple[str, str], ...]] = (
    ("model", "momentum"), ("model", "hybrid"), ("hybrid", "momentum"),
    ("model", "vt"), ("momentum", "vt"), ("hybrid", "vt"),
)
#: The planned day of each look, 1 to 3 (the race's estimates when the bars
#: were registered; the fund test is read on the race's look days, 11.7):
#: what "read again at checkpoint 2 (about ...)" prints when tonight has no
#: estimate of its own.
LOOK_ESTIMATES: Final[tuple[date, ...]] = schedule.FUND_TEST_LOOK_ESTIMATES
#: The fund test's planned final sample, in fund sessions (section 11.7).
FUND_PLANNED_SESSIONS: Final[int] = schedule.FUND_TEST_PLANNED_SESSIONS[-1]
#: A fund-test look record's status: read, skipped (calibration had not
#: passed on the night the race's look was readable; owner reading 3), or
#: left to the owner (180 or more fund sessions before the final look).
FUND_READ: Final[str] = "read"
FUND_SKIPPED: Final[str] = "skipped"
FUND_OWNER: Final[str] = "owner"
#: Why a look was skipped, as the record says it.
FUND_SKIP_REASON: Final[str] = "calibration had not passed on the night the race's look was readable"
#: Why a look is left to the owner, as the record says it.
FUND_OWNER_REASON: Final[str] = "180 or more fund sessions before the final look: the owner decides"

#: The race's row 8 when the after-tax record was made without a fund (the
#: plan's (v)).
UNAVAILABLE_VALUE: Final[str] = "record UNAVAILABLE: calibration had not passed when the race reached this look"
#: The combined line's last line (section 9).
MONEY_NOTE: Final[str] = "No real money before the June 2027 verdict (section 9)."


# --------------------------------------------------------------------------- #
# The data model
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Row:
    """One row of a verdict table, every cell already in words."""

    #: "1" to "9", or "→" for the verdict row.
    n: str
    rule: str
    measured: str
    value: str
    bar: str
    result: str


@dataclass(frozen=True)
class Table:
    """One look of one test, as the plan lays it out.

    ``complete`` is True when the look was readable and no row is WAITING:
    only then may the table be frozen (the race's gate JSON, the fund-test
    record). ``status`` says what kind of verdict it is (``STATUSES``) and
    ``outcome`` is what it decided (an arm or ``NO_ARM``), ``None`` when it
    decided nothing. ``test_data`` is True only for the printed examples
    (``tests/verdict_examples.py``), and such a table can never be written.
    """

    kind: str
    look: int
    title: str
    rows: tuple[Row, ...]
    verdict: str
    complete: bool
    status: str = NO_DECISION
    outcome: Optional[str] = None
    test_data: bool = False

    @property
    def decided(self) -> bool:
        return self.status == DECIDED


def table_json(table: Table) -> dict:
    """The table as the real outputs write it. Raises ``ValueError`` on a test-data table.

    Keys, in order: kind, look, title, rows (each n, rule, measured, value,
    bar, result), verdict, complete, status, outcome. ``test_data`` is never
    written: a real output never carries an example (owner Addition 2).
    """
    if table.test_data:
        raise ValueError("a TEST DATA table cannot be written to a real output (owner Addition 2, 6 Oct 2026)")
    return {
        "kind": table.kind,
        "look": table.look,
        "title": table.title,
        "rows": [{"n": r.n, "rule": r.rule, "measured": r.measured, "value": r.value, "bar": r.bar,
                  "result": r.result} for r in table.rows],
        "verdict": table.verdict,
        "complete": table.complete,
        "status": table.status,
        "outcome": table.outcome,
    }


def table_from_json(data: Mapping) -> Table:
    """The table ``table_json`` wrote, back (a frozen table carried from last night).

    ``status`` and ``outcome`` may be absent (read as "no decision" and
    ``None``). Anything else missing or of the wrong type raises
    ``ValueError``, so a damaged file is never read as a verdict.
    """
    try:
        rows = tuple(Row(*(_text(r[key]) for key in ("n", "rule", "measured", "value", "bar", "result")))
                     for r in data["rows"])
        kind, look, title, verdict = data["kind"], data["look"], data["title"], data["verdict"]
        complete = data["complete"]
    except (KeyError, TypeError) as error:
        raise ValueError(f"not a verdict table: {error!r}") from None
    if kind not in (RACE, FUND_TEST) or not isinstance(look, int) or isinstance(look, bool):
        raise ValueError(f"not a verdict table: kind {kind!r}, look {look!r}")
    if not isinstance(complete, bool):
        raise ValueError(f"not a verdict table: complete {complete!r}")
    status = data.get("status", NO_DECISION)
    outcome = data.get("outcome")
    if status not in STATUSES or (outcome is not None and not isinstance(outcome, str)):
        raise ValueError(f"not a verdict table: status {status!r}, outcome {outcome!r}")
    return Table(kind, look, _text(title), rows, _text(verdict), complete, status, outcome)


def _text(value: object) -> str:
    if not isinstance(value, str):
        raise ValueError(f"not a verdict table: {value!r} is not text")
    return value


def render(table: Table) -> list[str]:
    """The table as plain-text lines: the title, the column line, one line per row.

    A table with no rows (a skipped fund-test look) is its title and its
    verdict. A test-data table carries "TEST DATA" as the first words of
    every line and ends with ``TEST_DATA_FOOTER`` (owner Addition 2).
    """
    mark = f"{TEST_DATA} · " if table.test_data else ""
    lines = [mark + table.title]
    if table.rows:
        lines.append(mark + "Columns: " + " · ".join(COLUMNS))
        lines.extend(f"- {mark}" + " · ".join((r.n, r.rule, r.measured, r.value, r.bar, r.result))
                     for r in table.rows)
    else:
        lines.append(mark + table.verdict)
    if table.test_data:
        lines.append(TEST_DATA_FOOTER)
    return lines


def render_real(table: Table) -> list[str]:
    """``render`` for a real output (the race's report): raises ``ValueError`` on a test-data table."""
    if table.test_data:
        raise ValueError("a TEST DATA table cannot be printed in a real output (owner Addition 2, 6 Oct 2026)")
    return render(table)


def block(tables: Sequence[Table] = ()) -> list[str]:
    """The report's CHECKPOINT VERDICT block (the plan's (iv)).

    With no table to show (before the first look, and between looks after
    one that decided nothing), the header and "no decision yet"; otherwise
    each table, a blank line between them. A real output only: it raises on
    a test-data table.
    """
    lines = ["CHECKPOINT VERDICT", ""]
    if not tables:
        return lines + [NO_DECISION_YET]
    for i, table in enumerate(tables):
        if i:
            lines.append("")
        lines.extend(render_real(table))
    return lines


# --------------------------------------------------------------------------- #
# Dates and numbers
# --------------------------------------------------------------------------- #

DateLike = Union[date, str]


def as_date(value: DateLike) -> date:
    """A ``date``, or an ISO day (``YYYY-MM-DD``, the first ten characters of a stamp)."""
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value[:10])
        except ValueError:
            pass
    raise ValueError(f"not a date: {value!r}")


def check_dates(*days: Optional[DateLike], test_data: bool = False) -> None:
    """Refuse any date outside the experiment (``EXPERIMENT_START`` to ``EXPERIMENT_END``).

    The guard of the owner's Addition 2: every real table builder calls this
    on every date it prints, so the examples' 2099 dates can never be built
    into a real table. ``None`` is skipped (a date not known yet). Only
    ``test_data=True`` lets other dates through, and a test-data table
    cannot be written.
    """
    if test_data:
        return
    for day in days:
        if day is None:
            continue
        value = as_date(day)
        if not inside_experiment(value):
            raise ValueError(f"{value.isoformat()} is outside the experiment ({gate.DECISION_CUTOFF.isoformat()} "
                             f"to {EXPERIMENT_END.isoformat()}): a real verdict cannot hold it")


def inside_experiment(day: DateLike) -> bool:
    """Whether ``day`` is inside the experiment: from the decision window's opening to ``EXPERIMENT_END``.

    The opening is read from ``decision_gate.DECISION_CUTOFF`` when asked
    (it is ``EXPERIMENT_START`` unless a test moves the window), so a race
    run on an older journal with the window moved back can still print its
    tables; the 2099 examples are refused either way.
    """
    value = as_date(day)
    return gate.DECISION_CUTOFF <= value <= EXPERIMENT_END


def _minus(text: str) -> str:
    return text.replace("-", MINUS)


def t_text(t: Optional[float]) -> str:
    """``t = −3.62``, ``t = 0.84``; ``t = n/a`` when there is no t. A t that rounds to zero is ``t = 0.00``."""
    return "t = n/a" if not _number(t) else "t = " + _minus(f"{t:z.2f}")


def bar_text(bar: float) -> str:
    return f"{bar:.2f}"


def daily_text(x: Optional[float]) -> str:
    """A mean daily net return, a fraction, as ``+0.012%``; one that rounds to zero as ``+0.000%``."""
    return NA if not _number(x) else _minus(f"{x * 100:+z.3f}%")


def total_text(x: Optional[float]) -> str:
    """A fund's total return, a fraction, as ``+3.90%``; one that rounds to zero as ``+0.00%``."""
    return NA if not _number(x) else _minus(f"{x * 100:+z.2f}%")


def drawdown_text(dd: Optional[float]) -> str:
    """VT's largest fall, a fraction, as ``4.1%``; ``not measured`` when it could not be."""
    return "not measured" if not _number(dd) else f"{dd:.1%}"


def _number(x: object) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _iso(day: Optional[DateLike]) -> str:
    return "not known" if day is None else as_date(day).isoformat()


# --------------------------------------------------------------------------- #
# The steps of a look, recomputed with the gate's own predicates
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class Steps:
    """Rows 1 to 8 of one readable look, as facts, before any wording.

    Computed by ``steps`` with ``decision_gate.above``, ``below`` and
    ``after_tax_result`` -- the functions ``decide`` itself uses -- so the
    rows cannot read the numbers differently from the decision.
    """

    keep_a: bool
    keep_b: bool
    keep_c: bool
    replacement: str
    #: The model minus the replacement: what the early stop reads.
    against: Optional[float]
    #: True / False at an early look the model did not pass; None when the
    #: model is kept or at the final look.
    early_stop: Optional[bool]
    #: The arm the rule picks before the index step; None when none.
    candidate: Optional[str]
    #: The arm rows 7 and 8 measure: the candidate, or the replacement when
    #: there is none (the fund-test table shows it as NOT APPLIED).
    shown: str
    t_index: Optional[float]
    #: Row 7: "beats", "trails", "neither", "not_final" (did not beat VT at
    #: the final look) or "none" (no candidate).
    index: str
    #: Row 8: "pass", "fail", "waiting", "cannot" or "not_applied".
    after_tax: str
    t_after_tax: Optional[float]
    #: What the rows add up to: an arm, ``NO_ARM``, or None.
    outcome: Optional[str]

    @property
    def kept(self) -> bool:
        return self.keep_a and self.keep_b and self.keep_c

    @property
    def passed(self) -> int:
        return sum((self.keep_a, self.keep_b, self.keep_c))


def steps(inputs: LookInputs, bar: float, final: bool) -> Steps:
    """The rows of a readable look as facts (see ``Steps``).

    The order and the predicates are the registration's (section 5, 5a, 5c,
    as ``decision_gate._decide`` applies them); ``race_table`` and
    ``fund_test_table`` check the outcome against ``decide`` every time.
    """
    keep_a = gate.above(inputs.t_model_momentum, bar)
    keep_b = gate.above(inputs.t_model_hybrid, bar)
    keep_c = (inputs.model_mean is not None and inputs.model_band_high is not None
              and inputs.model_mean > inputs.model_band_high)
    replacement = "hybrid" if gate.above(inputs.t_hybrid_momentum, bar) else "momentum"
    against = inputs.t_model_momentum if replacement == "momentum" else inputs.t_model_hybrid
    kept = keep_a and keep_b and keep_c
    early_stop: Optional[bool] = None
    if kept:
        candidate: Optional[str] = "model"
    elif final:
        candidate = replacement
    else:
        early_stop = gate.below(against, bar)
        candidate = replacement if early_stop else None
    shown = candidate or replacement
    t_index = inputs.t_vs_index.get(shown)
    record = inputs.after_tax
    t_after_tax = None
    if record is not None and record.status == gate.AFTER_TAX_READY:
        t_after_tax = record.t_vs_index.get(shown)
    if candidate is None:
        index, after_tax, outcome = "none", "not_applied", None
    elif gate.above(t_index, bar):
        index = "beats"
        passed, _ = gate.after_tax_result(inputs, candidate, bar)
        if passed:
            after_tax, outcome = "pass", candidate
        elif passed is None:
            after_tax, outcome = "waiting", None
        else:
            after_tax = "fail" if record is not None and record.status == gate.AFTER_TAX_READY else "cannot"
            outcome = gate.NO_ARM if final else None
    else:
        after_tax = "not_applied"
        if final:
            index, outcome = "not_final", gate.NO_ARM
        elif gate.below(t_index, bar):
            index, outcome = "trails", gate.NO_ARM
        else:
            index, outcome = "neither", None
    return Steps(keep_a, keep_b, keep_c, replacement, against, early_stop, candidate, shown, t_index, index,
                 after_tax, t_after_tax, outcome)


def _checked(inputs: LookInputs, bar: float, final: bool) -> tuple[Steps, Optional[str], Optional[str], str]:
    """``steps`` and ``decide`` together; raises if they ever disagree (a table must not contradict the gate)."""
    found = steps(inputs, bar, final)
    candidate, outcome, reason = gate.decide(inputs, bar, final)
    if (found.candidate, found.outcome) != (candidate, outcome):
        raise RuntimeError(f"the verdict table disagrees with decision_gate.decide: rows give "
                           f"{(found.candidate, found.outcome)}, decide gives {(candidate, outcome)}")
    return found, candidate, outcome, reason


def _unreadable(inputs: LookInputs, bar: float, final: bool) -> Optional[str]:
    """Why the look cannot be read tonight, in ``decide``'s own words; None when it can."""
    if inputs.unreadable is None and not inputs.index_missing:
        return None
    reason = gate.decide(inputs, bar, final)[2]
    prefix = "this look cannot be read tonight: "
    return reason[len(prefix):] if reason.startswith(prefix) else reason


def _downturn_suffix(dd: Optional[float]) -> str:
    """The verdict's label (section 5d, owner reading 4): ``status_line``'s words, and the owner's when unmeasured."""
    tested = gate.tested_in_a_downturn(dd if _number(dd) else None)
    if tested is None:
        return " — DOWNTURN NOT MEASURED: the owner decides"
    if tested is False:
        return f" — {gate.DOWNTURN_LABEL.upper()}"
    return ""


def _pass_fail(ok: bool) -> str:
    return PASS if ok else FAIL


# --------------------------------------------------------------------------- #
# The race's table (the plan's (i))
# --------------------------------------------------------------------------- #


def race_table(
    look: Look, number: int, *, of: int = LOOKS, entry_days: Optional[int] = None,
    window_start: DateLike = gate.DECISION_CUTOFF, window_end: Optional[DateLike] = None,
    vt_priced: Optional[tuple[int, int]] = None, after_tax_window: Optional[tuple[DateLike, DateLike]] = None,
    next_look: Optional[tuple[int, DateLike, float]] = None, decided_at: Optional[int] = None,
    test_data: bool = False,
) -> Table:
    """One reached look of the race as the plan's table (i).

    ``look`` is the race's own ``decision_gate.Look`` (from ``evaluate``)
    and ``number`` its checkpoint number, 1 to 3. The look's numbers are
    ``look.inputs``; what is not given is taken from them: ``entry_days``
    from ``inputs.entry_days``, ``window_end`` from ``inputs.window_end``,
    ``vt_priced`` (days VT was priced on, of the entry days) from
    ``inputs.index_days`` and ``inputs.entry_days``, and row 8's
    ``after_tax_window`` (from, through) from the after-tax record's
    ``window``. ``next_look`` is ``(checkpoint, estimated date, bar)`` of
    the next look, for "read again at checkpoint 2"; ``decided_at`` is the
    checkpoint the race was decided at, if any: a later look is shown for
    reading only.

    The decision is ``decide(look.inputs, look.bar, look.final)``; the rows
    are recomputed with the gate's predicates and checked against it. A
    look that cannot be read tonight shows every row WAITING and is not
    complete; so does a look whose after-tax record is not made yet
    (row 8 WAITING). Raises ``ValueError`` for a look not reached, and for
    any date outside the experiment unless ``test_data`` (owner Addition 2).
    """
    inputs = look.inputs
    if inputs is None:
        raise ValueError(f"checkpoint {number} is not reached: it has no table yet")
    if entry_days is None:
        entry_days = inputs.entry_days
    if window_end is None:
        window_end = inputs.window_end
    if vt_priced is None:
        vt_priced = (inputs.index_days, inputs.entry_days)
    record = inputs.after_tax
    if after_tax_window is None and record is not None:
        after_tax_window = record.window
    check_dates(window_start, window_end, inputs.window_end, *(after_tax_window or ()),
                next_look[1] if next_look else None, test_data=test_data)

    bar, final = look.bar, look.final
    reading_only = decided_at is not None and decided_at < number
    problem = _unreadable(inputs, bar, final)
    title = (f"Race, checkpoint {number} of {of}: {look.independent} independent days ({entry_days} entry days), "
             f"window {_iso(window_start)} to {_iso(window_end)}, bar t > {bar_text(bar)}. "
             f"Readable tonight: {'yes' if problem is None else 'no'}. "
             f"VT priced on {vt_priced[0]} of {vt_priced[1]} entry days.")
    if reading_only:
        title += f" For reading only: the race was decided at checkpoint {decided_at}."

    b, minus_b = bar_text(bar), MINUS + bar_text(bar)
    lag = record.lag if record is not None and record.lag is not None else gate.AFTER_TAX_LAG
    window = f", {_iso(after_tax_window[0])} to {_iso(after_tax_window[1])}" if after_tax_window else ""
    downturn = (f"VT's largest fall from its high, dividends added back, {_iso(window_start)} to "
                f"{_iso(window_end)}")
    index_bar = f"> {b}, or no arm trades" if final else f"> {b} beats VT; < {minus_b} hold the index"

    if problem is not None:
        cells = [
            ("Keep (a), 5 and 5a", f"model − momentum, mean daily net return, Newey-West t, lag {RACE_LAG}",
             f"> {b}"),
            ("Keep (b), 5 and 5a", "model − hybrid, the same test", f"> {b}"),
            ("Keep (c), coin flip, 5", "model's mean daily net return against the 95th percentile of 1,000 coin "
             "flips on its own lines", "above"),
            ("Keep rule, 5", "rows 1, 2 and 3 all pass", "all 3"),
            ("Replacement, 5", f"hybrid − momentum, Newey-West t, lag {RACE_LAG}", f"> {b}"),
            ("Early stop, 5a (looks 1 and 2 only)", "against the model: model − the replacement", f"< {minus_b}"),
            ("Index first, 5 and 5a", f"the candidate − VT, same entry days and windows, Newey-West t, lag "
             f"{RACE_LAG}", index_bar),
            ("After-tax gate, 5c", f"the candidate fund − VT fund, daily after-tax return \"if sold today\", "
             f"Newey-West t, lag {lag}{window}", f"> {b}"),
            ("Downturn, 5d", downturn, "10% or more = tested"),
        ]
        rows = [Row(str(i), rule, measured, DASH, bar_cell, WAITING)
                for i, (rule, measured, bar_cell) in enumerate(cells, start=1)]
        verdict = f"NOT READABLE TONIGHT: {problem}"
        rows.append(Row(VERDICT_ROW, "Race verdict", "", "", "", verdict))
        return Table(RACE, number, title, tuple(rows), verdict, False, UNREADABLE, None, test_data)

    if look.reason and not reading_only:
        expected = gate.decide(inputs, bar, final)
        if (look.candidate, look.outcome) != expected[:2]:
            raise ValueError(f"the look's decision {(look.candidate, look.outcome)} is not decide()'s "
                             f"{expected[:2]} (a look shown for reading only needs decided_at)")
    s, candidate, outcome, _ = _checked(inputs, bar, final)

    repl = s.replacement
    if s.kept:
        replacement = f"{NOT_APPLIED} (the model is kept)"
        early = f"{NOT_APPLIED} (the model is kept)"
    else:
        replacement = f"PASS, so {repl}" if repl == "hybrid" else f"FAIL, so {repl}"
        if final:
            early = f"{NA} (final look)"
        elif s.early_stop:
            early = f"PASS: {repl} is the candidate"
        else:
            early = "FAIL: no early stop"
    if candidate is None:
        index_row = Row("7", "Index first, 5 and 5a", f"the candidate − VT, same entry days and windows, "
                        f"Newey-West t, lag {RACE_LAG}", DASH, index_bar, NOT_APPLIED)
        after_name, after_value = "the candidate", DASH
    else:
        index_result = {
            "beats": "PASS: beats VT",
            "not_final": "FAIL: no arm trades",
            "trails": "FAIL: trails VT, hold the index",
            "neither": "FAIL: clears neither bar, this look decides nothing",
        }[s.index]
        index_row = Row("7", "Index first, 5 and 5a", f"{candidate} − VT, same entry days and windows, "
                        f"Newey-West t, lag {RACE_LAG}", t_text(s.t_index), index_bar, index_result)
        after_name = candidate
        if record is None:
            after_value = "record not made yet"
        elif record.status != gate.AFTER_TAX_READY:
            after_value = UNAVAILABLE_VALUE
        else:
            after_value = t_text(s.t_after_tax)
    after_result = {
        "pass": PASS,
        "fail": "FAIL: no arm trades" if final else "FAIL: this look decides nothing",
        "waiting": WAITING,
        "cannot": CANNOT_PASS,
        "not_applied": NOT_APPLIED,
    }[s.after_tax]
    rows = [
        Row("1", "Keep (a), 5 and 5a", f"model − momentum, mean daily net return, Newey-West t, lag {RACE_LAG}",
            t_text(inputs.t_model_momentum), f"> {b}", _pass_fail(s.keep_a)),
        Row("2", "Keep (b), 5 and 5a", "model − hybrid, the same test", t_text(inputs.t_model_hybrid), f"> {b}",
            _pass_fail(s.keep_b)),
        Row("3", "Keep (c), coin flip, 5", "model's mean daily net return against the 95th percentile of 1,000 "
            "coin flips on its own lines", f"{daily_text(inputs.model_mean)} vs {daily_text(inputs.model_band_high)}",
            "above", _pass_fail(s.keep_c)),
        Row("4", "Keep rule, 5", "rows 1, 2 and 3 all pass", f"{s.passed} of 3", "all 3",
            KEPT if s.kept else NOT_KEPT),
        Row("5", "Replacement, 5", f"hybrid − momentum, Newey-West t, lag {RACE_LAG}",
            t_text(inputs.t_hybrid_momentum), f"> {b}", replacement),
        Row("6", "Early stop, 5a (looks 1 and 2 only)", f"against the model: model − {repl} (the replacement)",
            t_text(s.against), f"< {minus_b}", early),
        index_row,
        Row("8", "After-tax gate, 5c", f"{after_name} fund − VT fund, daily after-tax return \"if sold today\", "
            f"Newey-West t, lag {lag}{window}", after_value, f"> {b}", after_result),
        Row("9", "Downturn, 5d", downturn, drawdown_text(inputs.vt_max_drawdown), "10% or more = tested", LABEL),
    ]

    if reading_only:
        verdict, status, decided = "FOR READING ONLY", READING_ONLY, None
    elif outcome is not None:
        kind = "FINAL" if final else f"EARLY STOP AT {look.independent}"
        verdict = f"{kind}: {gate.OUTCOME_TEXT[outcome].upper()}{_downturn_suffix(inputs.vt_max_drawdown)}"
        status, decided = DECIDED, outcome
    elif s.after_tax == "waiting":
        verdict = ("WAITING FOR THE AFTER-TAX RECORD (5c): the funds run makes it on the first night it can, "
                   "and this look is read again every night until then")
        status, decided = STATUS_WAITING, None
    else:
        verdict, status, decided = _no_decision(number, next_look, "bar"), NO_DECISION, None
    rows.append(Row(VERDICT_ROW, "Race verdict", "", "", "", verdict))
    complete = s.after_tax != "waiting"
    return Table(RACE, number, title, tuple(rows), verdict, complete, status, decided, test_data)


def _no_decision(number: int, next_look: Optional[tuple[int, DateLike, float]], bar_word: str) -> str:
    if next_look is None:
        return "NO DECISION AT THIS LOOK"
    k, when, bar = next_look
    return (f"NO DECISION AT THIS LOOK — read again at checkpoint {k} (about {_iso(when)}; "
            f"{bar_word} {bar_text(bar)})")


# --------------------------------------------------------------------------- #
# The fund test's table (the plan's (ii) and (v))
# --------------------------------------------------------------------------- #


def fund_pair(first: str, second: str) -> str:
    """The key of a paired fund test in a look record's ``tests``: ``"model-momentum"``."""
    return f"{first}-{second}"


def _test_t(record: Mapping, first: str, second: str) -> Optional[float]:
    test = (record.get("tests") or {}).get(fund_pair(first, second)) or {}
    t = test.get("t")
    return float(t) if _number(t) else None


def fund_inputs(record: Mapping) -> LookInputs:
    """A read fund-test look record (section C of the build) as the gate's ``LookInputs``.

    The keep rule's paired tests are the funds' (11.6), the coin flip is
    the model fund's total return against the 95th percentile of the coin-
    flip funds' (11.5), the index test is each arm's fund against the VT
    fund before tax, and the after-tax record is the race's own record for
    the look (5c). ``entry_days`` holds the fund sessions.
    """
    coin = record.get("coin_flip") or {}
    after = record.get("after_tax")
    after_tax = None
    if isinstance(after, Mapping) and after.get("status") in (gate.AFTER_TAX_READY, gate.AFTER_TAX_UNAVAILABLE):
        ts = {arm: (float(t) if _number(t) else None) for arm, t in (after.get("t") or {}).items()}
        after_tax = AfterTax(after["status"], ts, after.get("reason") or "")
    dd = record.get("downturn")
    end = record.get("window_end")
    return LookInputs(
        entry_days=int(record.get("sessions") or 0),
        t_model_momentum=_test_t(record, "model", "momentum"),
        t_model_hybrid=_test_t(record, "model", "hybrid"),
        t_hybrid_momentum=_test_t(record, "hybrid", "momentum"),
        model_mean=coin.get("model_total") if _number(coin.get("model_total")) else None,
        model_band_high=coin.get("p95_total") if _number(coin.get("p95_total")) else None,
        t_vs_index={arm: _test_t(record, arm, "vt") for arm in ("model", "momentum", "hybrid")},
        after_tax=after_tax,
        vt_max_drawdown=float(dd) if _number(dd) else None,
        window_end=as_date(end) if end is not None else None,
    )


def fund_decision(record: Mapping) -> tuple[Optional[str], Optional[str], str]:
    """The fund test's decision at a read look: ``decide`` at the record's own bar (11.6, 11.7)."""
    look = int(record["look"])
    return gate.decide(fund_inputs(record), float(record["bar"]), final=look == LOOKS)


def planned_fund_bars(read: Sequence[tuple[float, float]] = (), *, after_look: int) -> list[tuple[int, float]]:
    """The fund test's planned bars for the looks after ``after_look``, by the spending rule of 11.7.

    ``read`` is ``(share, bar used)`` of every look actually read so far, in
    order; a skipped look is not in it (it spent nothing). The looks still
    to come are planned at their registered fund sessions (60, 120, 180 of
    180), the last at a share of 1. Returns ``(checkpoint, bar rounded up)``.
    """
    last = read[-1][0] if read else 0.0
    planned = [(k, (1.0 if k == LOOKS else schedule.FUND_TEST_PLANNED_SESSIONS[k - 1] / FUND_PLANNED_SESSIONS))
               for k in range(after_look + 1, LOOKS + 1)]
    planned = [(k, share) for k, share in planned if share > last]
    if not planned:
        return []
    bars = gate.spending_bars([s for s, _ in read] + [s for _, s in planned], used=[b for _, b in read])
    return [(k, gate.rounded_bar(bar)) for (k, _), bar in zip(planned, bars[len(read):])]


def fund_test_table(
    record: Mapping, *, planned_next: Optional[tuple[int, DateLike, float]] = None,
    decided_at: Optional[int] = None, read_before: Sequence[tuple[float, float]] = (),
    test_data: bool = False,
) -> Table:
    """One fund-test look record (section C of the build) as the plan's table (ii), or its (v) block.

    A read record gives rows 1 to 9 and the verdict; the decision is
    ``fund_decision(record)`` (``decide`` at the fund test's own bar), the
    rows are checked against it, and against the record's own
    ``decision`` when it has one. ``planned_next`` is ``(checkpoint,
    estimated date, planned bar)`` for "read again at checkpoint 2";
    ``decided_at`` the checkpoint the fund test was decided at, if any (a
    later look is for reading only). The fund sessions start at the
    record's ``start`` (default ``schedule.FUND_START``).

    A skipped record gives the (v) block, no rows: its planned next bars are
    computed by the spending rule from ``read_before`` (``(share, bar
    used)`` of the looks read before it) and the planned sessions of the
    looks to come. A record left to the owner (180 or more fund sessions
    before the final look) gives one line saying so.

    Raises ``ValueError`` for an unknown status, a decision that disagrees
    with the record's, and any date outside the experiment unless
    ``test_data`` (owner Addition 2).
    """
    look = int(record["look"])
    status = record.get("status")
    start = record.get("start") or schedule.FUND_START
    tests = record.get("tests") or {}
    check_dates(record.get("made_on"), record.get("window_end"), record.get("calibration_passed_on"),
                record.get("start"), *(t.get(key) for t in tests.values() if isinstance(t, Mapping)
                                       for key in ("from", "through")),
                planned_next[1] if planned_next else None, test_data=test_data)
    head = f"Fund test, checkpoint {look} of {LOOKS}"
    if status == FUND_SKIPPED:
        later = planned_fund_bars(read_before, after_look=look)
        if later:
            planned = ", ".join(f"checkpoint {k} at {bar_text(bar)}" for k, bar in later)
            rest = (" The next bars come from the same rule using only the looks actually read "
                    f"(planned: {planned}).")
        else:
            rest = " No later look is left."
        verdict = ("SKIPPED. Calibration had not passed on the night the race's look was readable. Not read, no "
                   f"part of the 5% spent, no bar used.{rest}")
        return Table(FUND_TEST, look, f"{head}: SKIPPED.", (), verdict, True, SKIPPED, None, test_data)
    if status == FUND_OWNER:
        reason = record.get("reason") or FUND_OWNER_REASON
        return Table(FUND_TEST, look, f"{head}: THE OWNER DECIDES.", (), f"THE OWNER DECIDES: {reason}.", True,
                     OWNER, None, test_data)
    if status != FUND_READ:
        raise ValueError(f"fund-test checkpoint {look}: unknown record status {status!r}")

    inputs = fund_inputs(record)
    bar, final = float(record["bar"]), look == LOOKS
    planned_bar = record.get("planned_bar")
    coin = record.get("coin_flip") or {}
    funds = coin.get("funds")
    funds_text = f"{funds:,}" if isinstance(funds, int) else "the"
    sessions = record.get("sessions")
    share = record.get("share")
    share_text = f"{share:.3f}" if _number(share) else NA
    planned_text = bar_text(planned_bar) if _number(planned_bar) else NA
    title = (f"{head}, read on the race's look day: fund sessions {_iso(start)} to "
             f"{_iso(record.get('window_end'))}, {sessions} of {FUND_PLANNED_SESSIONS} planned (share {share_text}); "
             f"bar t > {bar_text(bar)} (by the spending rule of 11.7; planned {planned_text}); calibration passed "
             f"{_iso(record.get('calibration_passed_on'))}; {funds_text} coin-flip funds.")
    if _number(planned_bar) and bar_text(bar) != bar_text(planned_bar):
        title += f" Bar {bar_text(bar)} (planned {bar_text(planned_bar)}): log it in the Amendments table."
    reading_only = decided_at is not None and decided_at < look
    if reading_only:
        title += f" For reading only: the fund test was decided at checkpoint {decided_at}."

    s, candidate, outcome, _ = _checked(inputs, bar, final)
    recorded = record.get("decision")
    if isinstance(recorded, Mapping) and (recorded.get("candidate"), recorded.get("outcome")) != (candidate, outcome):
        raise ValueError(f"fund-test checkpoint {look}: the record's decision "
                         f"{(recorded.get('candidate'), recorded.get('outcome'))} is not decide()'s "
                         f"{(candidate, outcome)}")

    lag = _fund_lag(record)
    b, minus_b = bar_text(bar), MINUS + bar_text(bar)
    repl = s.replacement
    if s.kept:
        replacement = early = f"{NOT_APPLIED} (the model fund is kept)"
    else:
        replacement = f"PASS, so the {repl} fund" if repl == "hybrid" else f"FAIL, so the {repl} fund"
        if final:
            early = f"{NA} (final look)"
        elif s.early_stop:
            early = f"PASS: the {repl} fund is the candidate"
        else:
            early = "FAIL: no early stop"
    shown = s.shown
    index_result = NOT_APPLIED if candidate is None else {
        "beats": "PASS: beats the VT fund",
        "not_final": "FAIL: no arm trades",
        "trails": "FAIL: trails the VT fund, hold the index",
        "neither": "FAIL: clears neither bar, this look decides nothing",
    }[s.index]
    after_result = {
        "pass": PASS,
        "fail": "FAIL: no arm trades" if final else "FAIL: this look decides nothing",
        "waiting": WAITING,
        "cannot": CANNOT_PASS,
        "not_applied": NOT_APPLIED,
    }[s.after_tax]
    record_after = inputs.after_tax
    if record_after is None:
        after_value = "record not made yet"
    elif record_after.status != gate.AFTER_TAX_READY:
        after_value = UNAVAILABLE_VALUE
    else:
        after_value = t_text(s.t_after_tax)
    rows = [
        Row("1", "Keep (a), 11.6", f"model fund − momentum fund, daily net return, Newey-West t, lag {lag}",
            t_text(inputs.t_model_momentum), f"> {b}", _pass_fail(s.keep_a)),
        Row("2", "Keep (b), 11.6", "model fund − hybrid fund, the same test", t_text(inputs.t_model_hybrid),
            f"> {b}", _pass_fail(s.keep_b)),
        Row("3", "Keep (c), coin flip, 11.5", f"model fund's total return since {_iso(start)} against the 95th "
            f"percentile of the {funds_text} coin-flip funds' total returns",
            f"{total_text(inputs.model_mean)} vs {total_text(inputs.model_band_high)}", "above",
            _pass_fail(s.keep_c)),
        Row("4", "Keep rule, 11.6", "rows 1, 2 and 3 all pass", f"{s.passed} of 3", "all 3",
            KEPT if s.kept else NOT_KEPT),
        Row("5", "Replacement, 11.6", f"hybrid fund − momentum fund, Newey-West t, lag {lag}",
            t_text(inputs.t_hybrid_momentum), f"> {b}", replacement),
        Row("6", "Early stop, 11.6 (as 5a)", f"against the model: model fund − {repl} fund", t_text(s.against),
            f"< {minus_b}", early),
        Row("7", "Index first, before tax, 11.6", f"{shown} fund − VT fund, daily, Newey-West t, lag {lag}",
            t_text(s.t_index), f"> {b}, or no arm trades" if final else f"> {b} / < {minus_b}", index_result),
        Row("8", "Index first, after tax, 11.6 and 5c", f"{shown} fund − VT fund after tax (the same record as "
            "race row 8: the same t, the fund test's own bar)", after_value, f"> {b}", after_result),
        Row("9", "Downturn, 5d", "the same number as the race's", drawdown_text(inputs.vt_max_drawdown),
            "10% or more = tested",
            LABEL if outcome is not None and not reading_only else "no label (nothing decided)"),
    ]
    if reading_only:
        verdict, table_status, decided = "FOR READING ONLY", READING_ONLY, None
    elif outcome is not None:
        kind = "FINAL" if final else f"EARLY STOP AT CHECKPOINT {look}"
        verdict = f"{kind}: {FUND_OUTCOME_TEXT[outcome].upper()}{_downturn_suffix(inputs.vt_max_drawdown)}"
        table_status, decided = DECIDED, outcome
    elif s.after_tax == "waiting":
        verdict = ("WAITING FOR THE AFTER-TAX RECORD (5c): the funds run makes it on the first night it can, "
                   "and this look is read again every night until then")
        table_status, decided = STATUS_WAITING, None
    else:
        verdict, table_status, decided = _no_decision(look, planned_next, "planned bar"), NO_DECISION, None
    rows.append(Row(VERDICT_ROW, "Fund-test verdict", "", "", "", verdict))
    return Table(FUND_TEST, look, title, tuple(rows), verdict, s.after_tax != "waiting", table_status, decided,
                 test_data)


def _fund_lag(record: Mapping) -> int:
    for test in (record.get("tests") or {}).values():
        if isinstance(test, Mapping) and isinstance(test.get("lag"), int):
            return test["lag"]
    return gate.AFTER_TAX_LAG


# --------------------------------------------------------------------------- #
# The one combined line (the plan's (iii), section 11.8, owner reading 1)
# --------------------------------------------------------------------------- #


def combined(race: Mapping, fund: Mapping, *, test_data: bool = False) -> dict:
    """The combined answer of the race and the fund test (section 11.8; owner reading 1).

    Each side is its state tonight: ``{"decided_at": checkpoint or None,
    "outcome": arm, "none" or None, "final_read": True once the final look
    was read or skipped, "skipped_all": True when every look so far was
    skipped, "look": the latest checkpoint reached or None, "window_end":
    its window end, "next": {"look", "estimated"} of the next look or
    None}``. Each test is frozen at its first deciding look and an early
    answer is final; section 9 only delays the money.

    The rows, first match wins: the race said "no arm trades"; the fund test
    said it; the fund test was skipped at every look through the final one
    (calibration never passed); the two picked different arms; the same arm
    won both; the race has not decided; the fund test has not decided.
    Before any look of either test: ``{"text": "no decision yet"}``.

    Returns ``{"text", "race", "fund_test", "line", "note"}``. Raises
    ``ValueError`` on a date outside the experiment unless ``test_data``.
    """
    for side in (race, fund):
        check_dates(side.get("window_end"), (side.get("next") or {}).get("estimated"), test_data=test_data)
    if race.get("look") is None and fund.get("look") is None:
        return {"text": NO_DECISION_YET}
    r, f = race.get("outcome"), fund.get("outcome")
    r_arm = r if race.get("decided_at") is not None else None
    f_arm = f if fund.get("decided_at") is not None else None
    wait: Optional[Mapping] = None
    if r_arm == gate.NO_ARM:
        text = 'HOLD THE INDEX — the race decided "no arm trades" (11.8)'
    elif f_arm == gate.NO_ARM:
        text = 'HOLD THE INDEX — the fund test decided "no arm trades" (11.8)'
    elif fund.get("skipped_all") and fund.get("final_read"):
        text = "HOLD THE INDEX — the fund test could not be read (calibration never passed)"
    elif r_arm is not None and f_arm is not None and r_arm != f_arm:
        text = f"HOLD THE INDEX — the race picked {ARM_NAMES[r_arm]}, the fund test picked {ARM_NAMES[f_arm]} (11.8)"
    elif r_arm is not None and r_arm == f_arm:
        name = ARM_NAMES[r_arm]
        text = (f"{name.upper()} WINS BOTH — no real money before the June 2027 verdict (section 9); after it, "
                f"real money for {name}, starting small if NOT TESTED IN A DOWNTURN")
    elif r_arm is None:
        text, wait = "NO DECISION YET — waiting for the race", race.get("next")
    else:
        text, wait = "NO DECISION YET — waiting for the fund test", fund.get("next")
    race_word = _side_word(race, gate.OUTCOME_TEXT)
    fund_word = _side_word(fund, FUND_OUTCOME_TEXT)
    k = race.get("look") if race.get("look") is not None else fund.get("look")
    end = race.get("window_end") if race.get("look") is not None else fund.get("window_end")
    after = (f" (checkpoint {wait['look']}, about {_iso(wait['estimated'])})"
             if isinstance(wait, Mapping) and wait.get("look") and wait.get("estimated") else "")
    line = (f"CHECKPOINT {k} ({_iso(end)}) — race: {race_word} · fund test: {fund_word} · "
            f"combined: {text}{after}.")
    return {"text": text, "race": race_word, "fund_test": fund_word, "line": line, "note": MONEY_NOTE}


def _side_word(side: Mapping, words: Mapping[str, str]) -> str:
    decided_at, outcome = side.get("decided_at"), side.get("outcome")
    if decided_at is not None and outcome in words:
        return f"{words[outcome].upper()} ({'final' if decided_at == LOOKS else 'early stop'})"
    if side.get("skipped_all"):
        return "skipped"
    return "no decision"


__all__ = [
    "ARM_NAMES",
    "CANNOT_PASS",
    "COLUMNS",
    "DASH",
    "DECIDED",
    "EXPERIMENT_END",
    "EXPERIMENT_START",
    "FAIL",
    "FUND_OUTCOME_TEXT",
    "FUND_OWNER",
    "FUND_OWNER_REASON",
    "FUND_PLANNED_SESSIONS",
    "FUND_READ",
    "FUND_SKIPPED",
    "FUND_SKIP_REASON",
    "FUND_TEST",
    "FUND_TEST_PAIRS",
    "KEPT",
    "LABEL",
    "LOOKS",
    "LOOK_ESTIMATES",
    "MINUS",
    "MONEY_NOTE",
    "NA",
    "NOT_APPLIED",
    "NOT_KEPT",
    "NO_DECISION",
    "NO_DECISION_YET",
    "OWNER",
    "PASS",
    "RACE",
    "RACE_LAG",
    "READING_ONLY",
    "RESULT_WORDS",
    "Row",
    "SKIPPED",
    "STATUSES",
    "STATUS_WAITING",
    "Steps",
    "TEST_DATA",
    "TEST_DATA_FOOTER",
    "Table",
    "UNAVAILABLE_VALUE",
    "UNREADABLE",
    "VERDICT_ROW",
    "WAITING",
    "as_date",
    "bar_text",
    "block",
    "check_dates",
    "combined",
    "daily_text",
    "drawdown_text",
    "fund_decision",
    "fund_inputs",
    "fund_pair",
    "fund_test_table",
    "inside_experiment",
    "planned_fund_bars",
    "race_table",
    "render",
    "render_real",
    "steps",
    "t_text",
    "table_from_json",
    "table_json",
    "total_text",
]
