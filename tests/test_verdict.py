"""The checkpoint verdict tables (``analysis.verdict``): every row, every verdict, and the gate's own answer.

The owner approved the layout on 6 Oct 2026
(``docs/research/checkpoint-verdict-plan.md``). The most important test here
is the equivalence: on every branch of ``decision_gate._decide`` the table's
rows and verdict say what ``decide`` says, for the race and for the fund
test. The rest pins every row's wording, the combined line in every row of
its table, the rendering, the JSON round trip and the date guard.
"""

from __future__ import annotations

import itertools
from dataclasses import replace
from datetime import date

import pytest

from analysis import decision_gate as gate
from analysis import verdict as v
from analysis.decision_gate import AfterTax, Look, LookInputs
from tests.test_decision_gate import after, inputs

END = date(2026, 12, 22)
NEXT = (2, date(2027, 3, 22), 2.45)


def look_at(look_inputs: LookInputs, k: int = 1) -> Look:
    """A bare look (no decision fields) at checkpoint ``k``: the table decides through ``decide`` itself."""
    independent, bar = gate.CHECKPOINTS[k - 1]
    return Look(independent, bar, k == 3, look_inputs)


def race(look_inputs: LookInputs, k: int = 1, **kw) -> v.Table:
    kw.setdefault("window_end", END if k == 1 else date(2027, 6, 16))
    kw.setdefault("next_look", NEXT if k < 3 else None)
    return v.race_table(look_at(look_inputs, k), k, **kw)


def row(table: v.Table, n: str) -> v.Row:
    return next(r for r in table.rows if r.n == n)


def plan_inputs(**changes) -> LookInputs:
    """The plan's example (i): an early stop for momentum at checkpoint 1, not tested in a downturn."""
    base = LookInputs(
        entry_days=60, t_model_momentum=-3.62, t_model_hybrid=-1.05, t_hybrid_momentum=0.84,
        model_mean=0.00012, model_band_high=0.00071, t_vs_index={"model": 0.1, "momentum": 3.55, "hybrid": 0.2},
        index_days=60, vt_max_drawdown=0.041, window_end=END,
        after_tax=AfterTax(gate.AFTER_TAX_READY, {"momentum": 3.52}, window_end=END,
                           window=(date(2026, 9, 29), END), lag=5),
    )
    return replace(base, **changes)


def fund_record(mm=-2.31, mh=-0.40, hm=-1.90, total=0.039, p95=0.027, after_tax="ready", look=1, bar=3.40,
                planned=3.40, dd=0.041, **vs) -> dict:
    """A read fund-test look record (section C of the build); the plan's example (ii) by default."""
    t_vs = {"model": 0.3, "momentum": 1.12, "hybrid": 0.5}
    t_vs.update(vs)
    end = {1: "2026-12-22", 2: "2027-03-22", 3: "2027-06-16"}[look]
    ts = {"model-momentum": mm, "model-hybrid": mh, "hybrid-momentum": hm,
          **{f"{arm}-vt": t for arm, t in t_vs.items()}}
    if after_tax == "ready":
        after_tax = {"status": gate.AFTER_TAX_READY, "t": {"momentum": 3.52, "model": 0.2, "hybrid": 0.1}}
    return {
        "look": look, "made_on": "2026-12-23", "window_end": end, "status": "read", "sessions": 60,
        "share": 60 / 180, "bar": bar, "planned_bar": planned, "bar_differs": bar != planned,
        "calibration_passed_on": "2026-10-19",
        "tests": {pair: {"t": t, "lag": 5, "from": "2026-09-29", "through": end, "days": 60}
                  for pair, t in ts.items()},
        "coin_flip": {"model_total": total, "p95_total": p95, "funds": 1000},
        "after_tax": after_tax, "downturn": dd,
    }


# --- the gate's public names are the gate's own functions --------------------------------------------


def test_the_public_aliases_are_the_gates_own_predicates_not_copies():
    assert gate.above is gate._above and gate.below is gate._below and gate.after_tax_result is gate._after_tax
    assert {"above", "below", "after_tax_result"} <= set(gate.__all__)


def test_the_after_tax_records_new_fields_are_optional_and_ignored_by_decide():
    plain = AfterTax(gate.AFTER_TAX_READY, {"model": 2.2})
    assert plain.window is None and plain.lag is None
    widened = AfterTax(gate.AFTER_TAX_READY, {"model": 2.2}, window=(date(2026, 9, 29), END), lag=5)
    a = gate.decide(inputs(mm=3.0, mh=2.5, model=2.1, after_tax=plain), 2.0, final=True)
    b = gate.decide(inputs(mm=3.0, mh=2.5, model=2.1, after_tax=widened), 2.0, final=True)
    assert a == b


# --- the equivalence: the table says what decide() says, on every branch ---------------------------------


T_VALUES = (None, -4.0, -3.47, 0.0, 3.47, 4.0)
COINS = ((0.002, 0.001), (0.001, 0.001), (0.0005, 0.001), (None, 0.001))
AFTER = ("waiting", "unavailable", 4.0, 3.47, -4.0, None)


def after_record(kind, arm_t_vs):
    if kind == "waiting":
        return None
    if kind == "unavailable":
        return AfterTax(gate.AFTER_TAX_UNAVAILABLE, {}, "calibration had not passed when the race reached this look")
    return AfterTax(gate.AFTER_TAX_READY, {arm: kind for arm in arm_t_vs})


def grid(final: bool):
    """Every keep / replacement / early-stop branch, with the index and after-tax cases cycled through them."""
    bar = 2.0 if final else 3.47
    scale = bar / 3.47
    ts = tuple(None if t is None else t * scale for t in T_VALUES)
    for i, (mm, mh, hm, (mean, band)) in enumerate(itertools.product(ts, ts, ts, COINS)):
        vs = ts[i % len(ts)]
        kind = AFTER[(i // len(ts)) % len(AFTER)]
        kind = kind * scale if isinstance(kind, float) else kind
        t_vs = {"model": vs, "momentum": vs, "hybrid": vs}
        yield bar, LookInputs(entry_days=60, t_model_momentum=mm, t_model_hybrid=mh, t_hybrid_momentum=hm,
                              model_mean=mean, model_band_high=band, t_vs_index=t_vs, index_days=60,
                              after_tax=after_record(kind, t_vs), vt_max_drawdown=(0.05, 0.12, None)[i % 3],
                              window_end=END)
    # Every index case against every after-tax case, for each way an arm can be the candidate.
    for mm, mh, hm, mean in ((4.0, 4.0, 0.0, 0.002), (-4.0, 0.0, 0.0, 0.0), (0.0, -4.0, 4.0, 0.0)):
        for vs, kind in itertools.product(ts, AFTER):
            kind = kind * scale if isinstance(kind, float) else kind
            t_vs = {"model": vs, "momentum": vs, "hybrid": vs}
            yield bar, LookInputs(entry_days=60, t_model_momentum=mm * scale, t_model_hybrid=mh * scale,
                                  t_hybrid_momentum=hm * scale, model_mean=mean, model_band_high=0.001,
                                  t_vs_index=t_vs, index_days=60, after_tax=after_record(kind, t_vs),
                                  vt_max_drawdown=0.05, window_end=END)


def assert_agrees(table: v.Table, look_inputs: LookInputs, bar: float, final: bool, words) -> None:
    candidate, outcome, _ = gate.decide(look_inputs, bar, final)
    assert (row(table, "4").result == v.KEPT) == (candidate == "model")
    early_stop = not final and candidate is not None and candidate != "model"
    assert row(table, "6").result.startswith("PASS") == early_stop
    assert (table.status == v.DECIDED) == (outcome is not None)
    assert table.outcome == outcome
    if outcome is not None:
        assert words[outcome].upper() in table.verdict
        assert table.verdict.startswith("FINAL: " if final else "EARLY STOP AT ")
    else:
        assert not table.verdict.startswith(("FINAL", "EARLY STOP"))
    assert row(table, "1").result == ("PASS" if gate.above(look_inputs.t_model_momentum, bar) else "FAIL")
    assert row(table, "2").result == ("PASS" if gate.above(look_inputs.t_model_hybrid, bar) else "FAIL")
    index_passed = candidate is not None and gate.above(look_inputs.t_vs_index.get(candidate), bar)
    assert row(table, "7").result.startswith("PASS") == index_passed
    assert (row(table, "8").result == v.PASS) == (candidate is not None and outcome == candidate)
    waiting = index_passed and look_inputs.after_tax is None
    assert (row(table, "8").result == v.WAITING) == waiting
    assert table.complete == (not waiting)
    assert table.rows[-1] == v.Row(v.VERDICT_ROW, table.rows[-1].rule, "", "", "", table.verdict)


@pytest.mark.parametrize("final", [False, True], ids=["early look", "final look"])
def test_the_race_table_agrees_with_decide_on_every_branch(final):
    seen = set()
    for bar, look_inputs in grid(final):
        k = 3 if final else 1
        table = race(look_inputs, k)
        assert_agrees(table, look_inputs, bar, final, gate.OUTCOME_TEXT)
        candidate, outcome, reason = gate.decide(look_inputs, bar, final)
        seen.add((candidate, outcome, reason.split(";")[0].split(" at t")[0][:40]))
    # The grid really does visit kept / replaced / no early stop, and all four outcomes.
    outcomes = {o for _, o, _ in seen}
    assert {None, "model", "momentum", "hybrid", gate.NO_ARM} <= outcomes


@pytest.mark.parametrize("final", [False, True], ids=["early look", "final look"])
def test_the_fund_test_table_agrees_with_decide_on_fund_inputs(final):
    look = 3 if final else 1
    for bar, look_inputs in grid(final):
        after = look_inputs.after_tax
        record = fund_record(
            mm=look_inputs.t_model_momentum, mh=look_inputs.t_model_hybrid, hm=look_inputs.t_hybrid_momentum,
            total=look_inputs.model_mean, p95=look_inputs.model_band_high, look=look, bar=bar, planned=bar,
            dd=look_inputs.vt_max_drawdown,
            after_tax=None if after is None else {"status": after.status, "t": dict(after.t_vs_index),
                                                  "reason": after.reason},
            **look_inputs.t_vs_index)
        table = v.fund_test_table(record, planned_next=None if final else (2, date(2027, 3, 22), 2.41))
        fund = v.fund_inputs(record)
        assert gate.decide(fund, bar, final)[:2] == gate.decide(replace(look_inputs, entry_days=60), bar, final)[:2]
        assert_agrees(table, fund, bar, final, v.FUND_OUTCOME_TEXT)
        assert v.fund_decision(record) == gate.decide(fund, bar, final)


def test_the_coin_flip_tie_fails_in_both_tables():
    """Strict "above" (sections 5 and 11.5): a tie is not above."""
    tie = inputs(mm=4.0, mh=4.0, mean=0.001, band=0.001, model=4.0)
    table = race(replace(tie, window_end=END))
    assert row(table, "3").result == v.FAIL and row(table, "4").result == v.NOT_KEPT
    assert gate.decide(tie, 3.47, final=False)[0] != "model"
    fund = v.fund_test_table(fund_record(mm=4.0, mh=4.0, total=0.027, p95=0.027))
    assert row(fund, "3").result == v.FAIL and row(fund, "4").result == v.NOT_KEPT


def test_a_missing_t_fails_its_row_and_shows_n_a():
    table = race(plan_inputs(t_model_momentum=None, t_model_hybrid=None))
    assert row(table, "1").value == "t = n/a" and row(table, "1").result == v.FAIL
    assert row(table, "6").value == "t = n/a" and row(table, "6").result == "FAIL: no early stop"
    missing = race(plan_inputs(model_mean=None))
    assert row(missing, "3").value == "n/a vs +0.071%" and row(missing, "3").result == v.FAIL


def test_the_tables_built_from_evaluates_looks_agree_with_evaluate():
    looks = gate.evaluate({20: plan_inputs(), 40: replace(plan_inputs(), window_end=date(2027, 3, 22))})
    first = v.race_table(looks[0], 1)
    assert first.outcome == looks[0].outcome == "momentum"
    later = v.race_table(looks[1], 2, decided_at=1)
    assert later.status == v.READING_ONLY and later.outcome is None


# --- the race's rows, one wording at a time ----------------------------------------------------------------


def test_the_plans_race_example_renders_line_for_line():
    assert v.render(race(plan_inputs())) == [
        "Race, checkpoint 1 of 3: 20 independent days (60 entry days), window 2026-09-23 to 2026-12-22, bar "
        "t > 3.47. Readable tonight: yes. VT priced on 60 of 60 entry days.",
        "Columns: # · Rule (section) · What is measured · Value · Bar · Result",
        "- 1 · Keep (a), 5 and 5a · model − momentum, mean daily net return, Newey-West t, lag 3 · t = −3.62 · "
        "> 3.47 · FAIL",
        "- 2 · Keep (b), 5 and 5a · model − hybrid, the same test · t = −1.05 · > 3.47 · FAIL",
        "- 3 · Keep (c), coin flip, 5 · model's mean daily net return against the 95th percentile of 1,000 coin "
        "flips on its own lines · +0.012% vs +0.071% · above · FAIL",
        "- 4 · Keep rule, 5 · rows 1, 2 and 3 all pass · 0 of 3 · all 3 · NOT KEPT",
        "- 5 · Replacement, 5 · hybrid − momentum, Newey-West t, lag 3 · t = 0.84 · > 3.47 · FAIL, so momentum",
        "- 6 · Early stop, 5a (looks 1 and 2 only) · against the model: model − momentum (the replacement) · "
        "t = −3.62 · < −3.47 · PASS: momentum is the candidate",
        "- 7 · Index first, 5 and 5a · momentum − VT, same entry days and windows, Newey-West t, lag 3 · "
        "t = 3.55 · > 3.47 beats VT; < −3.47 hold the index · PASS: beats VT",
        "- 8 · After-tax gate, 5c · momentum fund − VT fund, daily after-tax return \"if sold today\", "
        "Newey-West t, lag 5, 2026-09-29 to 2026-12-22 · t = 3.52 · > 3.47 · PASS",
        "- 9 · Downturn, 5d · VT's largest fall from its high, dividends added back, 2026-09-23 to 2026-12-22 · "
        "4.1% · 10% or more = tested · LABEL",
        "- → · Race verdict ·  ·  ·  · EARLY STOP AT 20: REPLACE THE MODEL WITH MOMENTUM — NOT TESTED IN A "
        "DOWNTURN",
    ]


def test_a_kept_model_leaves_the_replacement_and_the_early_stop_not_applied():
    kept = race(plan_inputs(t_model_momentum=4.0, t_model_hybrid=4.0, model_mean=0.002,
                            t_vs_index={"model": 4.0},
                            after_tax=AfterTax(gate.AFTER_TAX_READY, {"model": 4.0}, window_end=END)))
    assert row(kept, "4").value == "3 of 3" and row(kept, "4").result == v.KEPT
    assert row(kept, "5").result == "NOT APPLIED (the model is kept)"
    assert row(kept, "6").result == "NOT APPLIED (the model is kept)"
    assert row(kept, "7").measured.startswith("model − VT")
    assert kept.verdict == "EARLY STOP AT 20: KEEP THE MODEL — NOT TESTED IN A DOWNTURN"


def test_the_replacement_row_names_the_hybrid_when_it_beats_momentum():
    table = race(plan_inputs(t_hybrid_momentum=3.9, t_model_hybrid=-3.8, t_vs_index={"hybrid": 3.6},
                             after_tax=AfterTax(gate.AFTER_TAX_READY, {"hybrid": 3.6}, window_end=END)))
    assert row(table, "5").result == "PASS, so hybrid"
    assert row(table, "6").measured == "against the model: model − hybrid (the replacement)"
    assert row(table, "6").result == "PASS: hybrid is the candidate" and row(table, "6").value == "t = −3.80"
    assert table.outcome == "hybrid"


def test_no_early_stop_leaves_rows_7_and_8_not_applied_and_decides_nothing():
    table = race(plan_inputs(t_model_momentum=-1.0))
    assert row(table, "6").result == "FAIL: no early stop"
    assert row(table, "7") == v.Row("7", "Index first, 5 and 5a", "the candidate − VT, same entry days and "
                                    "windows, Newey-West t, lag 3", "—",
                                    "> 3.47 beats VT; < −3.47 hold the index", v.NOT_APPLIED)
    assert row(table, "8").result == v.NOT_APPLIED and row(table, "8").value == "—"
    assert row(table, "8").measured.startswith("the candidate fund − VT fund")
    assert table.verdict == ("NO DECISION AT THIS LOOK — read again at checkpoint 2 (about 2027-03-22; "
                             "bar 2.45)")
    assert table.status == v.NO_DECISION and table.complete


def test_the_index_row_in_each_direction():
    trails = race(plan_inputs(t_vs_index={"momentum": -3.6}))
    assert row(trails, "7").result == "FAIL: trails VT, hold the index"
    assert trails.outcome == gate.NO_ARM and trails.verdict.startswith("EARLY STOP AT 20: NO ARM TRADES")
    neither = race(plan_inputs(t_vs_index={"momentum": 1.0}))
    assert row(neither, "7").result == "FAIL: clears neither bar, this look decides nothing"
    assert neither.outcome is None and row(neither, "8").result == v.NOT_APPLIED
    final = race(plan_inputs(t_vs_index={"momentum": 1.0}, entry_days=180), 3)
    assert row(final, "7").bar == "> 2.00, or no arm trades" and row(final, "7").result == "FAIL: no arm trades"
    assert final.verdict.startswith("FINAL: " + gate.OUTCOME_TEXT[gate.NO_ARM].upper())


def test_the_after_tax_row_in_every_state():
    def with_record(record, k=1):
        return race(plan_inputs(after_tax=record), k)

    early_fail = with_record(AfterTax(gate.AFTER_TAX_READY, {"momentum": 1.0}))
    assert row(early_fail, "8").result == "FAIL: this look decides nothing" and early_fail.outcome is None
    assert row(early_fail, "8").measured.endswith("Newey-West t, lag 5")  # no window known: no dates
    final_fail = with_record(AfterTax(gate.AFTER_TAX_READY, {"momentum": 1.0}), 3)
    assert row(final_fail, "8").result == "FAIL: no arm trades" and final_fail.outcome == gate.NO_ARM
    waiting = with_record(None)
    assert row(waiting, "8").result == v.WAITING and row(waiting, "8").value == "record not made yet"
    assert not waiting.complete and waiting.status == v.STATUS_WAITING
    assert waiting.verdict.startswith("WAITING FOR THE AFTER-TAX RECORD (5c)")
    unavailable = with_record(AfterTax(gate.AFTER_TAX_UNAVAILABLE, {}, "calibration had not passed"))
    assert row(unavailable, "8").result == v.CANNOT_PASS
    assert row(unavailable, "8").value == ("record UNAVAILABLE: calibration had not passed when the race reached "
                                           "this look")
    assert unavailable.outcome is None and unavailable.complete
    assert with_record(AfterTax(gate.AFTER_TAX_UNAVAILABLE, {}), 3).outcome == gate.NO_ARM
    not_applied = race(plan_inputs(t_vs_index={"momentum": 1.0}))
    assert row(not_applied, "8").result == v.NOT_APPLIED and row(not_applied, "8").value == "t = 3.52"


def test_the_downturn_row_and_the_verdicts_label():
    tested = race(plan_inputs(vt_max_drawdown=0.124))
    assert row(tested, "9").value == "12.4%" and row(tested, "9").result == v.LABEL
    assert tested.verdict == "EARLY STOP AT 20: REPLACE THE MODEL WITH MOMENTUM"
    exactly = race(plan_inputs(vt_max_drawdown=0.10))
    assert "DOWNTURN" not in exactly.verdict
    unmeasured = race(plan_inputs(vt_max_drawdown=None))
    assert row(unmeasured, "9").value == "not measured"
    assert unmeasured.verdict.endswith(" — DOWNTURN NOT MEASURED: the owner decides")
    assert row(unmeasured, "9").bar == "10% or more = tested"


def test_the_final_look_reads_the_early_stop_as_not_applying():
    table = race(plan_inputs(entry_days=180, t_vs_index={"momentum": 2.5},
                             after_tax=AfterTax(gate.AFTER_TAX_READY, {"momentum": 2.1})), 3)
    assert row(table, "6").result == "n/a (final look)" and row(table, "6").value == "t = −3.62"
    assert table.verdict == "FINAL: REPLACE THE MODEL WITH MOMENTUM — NOT TESTED IN A DOWNTURN"
    assert table.title.startswith("Race, checkpoint 3 of 3: 60 independent days (180 entry days)")


def test_an_unreadable_look_waits_on_every_row():
    table = race(plan_inputs(unreadable="the source has no close for 2026-12-22 yet"))
    assert [r.result for r in table.rows[:-1]] == [v.WAITING] * 9
    assert table.verdict == "NOT READABLE TONIGHT: the source has no close for 2026-12-22 yet"
    assert not table.complete and table.status == v.UNREADABLE and "Readable tonight: no." in table.title
    missing = race(plan_inputs(index_missing=3))
    assert missing.verdict == "NOT READABLE TONIGHT: VT could not be priced on 3 of the look's days"


def test_a_look_after_the_deciding_one_is_for_reading_only():
    table = race(plan_inputs(window_end=date(2027, 3, 22)), 2, window_end=date(2027, 3, 22), decided_at=1)
    assert table.title.endswith(" For reading only: the race was decided at checkpoint 1.")
    assert table.verdict == "FOR READING ONLY" and table.outcome is None and table.complete


def test_no_decision_without_a_next_look_says_so_plainly():
    assert race(plan_inputs(t_model_momentum=-1.0), next_look=None).verdict == "NO DECISION AT THIS LOOK"


def test_the_race_table_refuses_a_look_not_reached_and_a_decision_that_is_not_decides():
    with pytest.raises(ValueError, match="not reached"):
        v.race_table(Look(20, 3.47, False), 1)
    wrong = Look(20, 3.47, False, plan_inputs(), "model", "model", "made up")
    with pytest.raises(ValueError, match="decide"):
        v.race_table(wrong, 1)


def test_the_race_defaults_come_from_the_looks_own_numbers():
    table = v.race_table(look_at(plan_inputs(index_days=58, index_gaps=2)), 1)
    assert "window 2026-09-23 to 2026-12-22" in table.title
    assert table.title.endswith("VT priced on 58 of 60 entry days.")
    assert "2026-09-29 to 2026-12-22" in row(table, "8").measured


# --- the fund test's table ---------------------------------------------------------------------------------


def test_the_plans_fund_test_example_renders_line_for_line():
    table = v.fund_test_table(fund_record(), planned_next=(2, date(2027, 3, 22), 2.41))
    assert v.render(table) == [
        "Fund test, checkpoint 1 of 3, read on the race's look day: fund sessions 2026-09-29 to 2026-12-22, 60 of "
        "180 planned (share 0.333); bar t > 3.40 (by the spending rule of 11.7; planned 3.40); calibration passed "
        "2026-10-19; 1,000 coin-flip funds.",
        "Columns: # · Rule (section) · What is measured · Value · Bar · Result",
        "- 1 · Keep (a), 11.6 · model fund − momentum fund, daily net return, Newey-West t, lag 5 · t = −2.31 · "
        "> 3.40 · FAIL",
        "- 2 · Keep (b), 11.6 · model fund − hybrid fund, the same test · t = −0.40 · > 3.40 · FAIL",
        "- 3 · Keep (c), coin flip, 11.5 · model fund's total return since 2026-09-29 against the 95th percentile "
        "of the 1,000 coin-flip funds' total returns · +3.90% vs +2.70% · above · PASS",
        "- 4 · Keep rule, 11.6 · rows 1, 2 and 3 all pass · 1 of 3 · all 3 · NOT KEPT",
        "- 5 · Replacement, 11.6 · hybrid fund − momentum fund, Newey-West t, lag 5 · t = −1.90 · > 3.40 · FAIL, "
        "so the momentum fund",
        "- 6 · Early stop, 11.6 (as 5a) · against the model: model fund − momentum fund · t = −2.31 · < −3.40 · "
        "FAIL: no early stop",
        "- 7 · Index first, before tax, 11.6 · momentum fund − VT fund, daily, Newey-West t, lag 5 · t = 1.12 · "
        "> 3.40 / < −3.40 · NOT APPLIED",
        "- 8 · Index first, after tax, 11.6 and 5c · momentum fund − VT fund after tax (the same record as race "
        "row 8: the same t, the fund test's own bar) · t = 3.52 · > 3.40 · NOT APPLIED",
        "- 9 · Downturn, 5d · the same number as the race's · 4.1% · 10% or more = tested · no label (nothing "
        "decided)",
        "- → · Fund-test verdict ·  ·  ·  · NO DECISION AT THIS LOOK — read again at checkpoint 2 (about "
        "2027-03-22; planned bar 2.41)",
    ]


def test_a_bar_that_differs_from_the_plan_asks_for_an_amendment_in_the_title():
    """Section 11.7 and the owner's Addition 1: the bar used, the planned bar, and what to do."""
    table = v.fund_test_table(fund_record(bar=3.37, planned=3.40))
    assert "bar t > 3.37 (by the spending rule of 11.7; planned 3.40)" in table.title
    assert table.title.endswith(" Bar 3.37 (planned 3.40): log it in the Amendments table.")
    assert "Amendments" not in v.fund_test_table(fund_record()).title


def test_the_fund_test_decides_in_its_own_words():
    early = v.fund_test_table(fund_record(mm=-3.5, momentum=3.6,
                                          after_tax={"status": "ready", "t": {"momentum": 3.45}}))
    assert row(early, "6").result == "PASS: the momentum fund is the candidate"
    assert row(early, "7").result == "PASS: beats the VT fund" and row(early, "8").result == v.PASS
    assert row(early, "9").result == v.LABEL
    assert early.verdict == ("EARLY STOP AT CHECKPOINT 1: REPLACE THE MODEL FUND WITH THE MOMENTUM FUND — "
                             "NOT TESTED IN A DOWNTURN")
    kept = v.fund_test_table(fund_record(mm=2.5, mh=2.5, hm=2.3, total=0.05, look=3, bar=2.02, planned=2.02,
                                         model=2.6, after_tax={"status": "ready", "t": {"model": 2.4}}, dd=0.15))
    assert row(kept, "5").result == "NOT APPLIED (the model fund is kept)"
    assert kept.verdict == "FINAL: KEEP THE MODEL FUND"
    hybrid = v.fund_test_table(fund_record(hm=2.5, look=3, bar=2.02, planned=2.02, hybrid=0.1))
    assert row(hybrid, "5").result == "PASS, so the hybrid fund" and row(hybrid, "6").result == "n/a (final look)"
    assert row(hybrid, "7").result == "FAIL: no arm trades" and row(hybrid, "7").bar == "> 2.02, or no arm trades"
    assert hybrid.verdict == "FINAL: NO ARM TRADES: HOLD THE INDEX — NOT TESTED IN A DOWNTURN"
    trails = v.fund_test_table(fund_record(mm=-3.5, momentum=-3.6))
    assert row(trails, "7").result == "FAIL: trails the VT fund, hold the index"


def test_the_fund_tests_after_tax_row_reads_the_races_record_at_its_own_bar():
    """One record, one t per fund; the fund test compares it with its own bar (5c, 11.7)."""
    record = fund_record(mm=-3.5, momentum=3.6, after_tax={"status": "ready", "t": {"momentum": 3.45}})
    assert row(v.fund_test_table(record), "8").result == v.PASS  # 3.45 > 3.40, though below the race's 3.47
    unavailable = fund_record(mm=-3.5, momentum=3.6, after_tax={"status": "unavailable", "t": {}})
    table = v.fund_test_table(unavailable)
    assert row(table, "8").result == v.CANNOT_PASS and row(table, "8").value == v.UNAVAILABLE_VALUE
    waiting = v.fund_test_table(fund_record(mm=-3.5, momentum=3.6, after_tax=None))
    assert row(waiting, "8").result == v.WAITING and not waiting.complete


def test_a_skipped_look_is_the_plans_block_with_its_bars_computed():
    record = {"look": 1, "made_on": "2026-12-23", "window_end": "2026-12-22", "status": "skipped",
              "reason": v.FUND_SKIP_REASON}
    table = v.fund_test_table(record)
    assert table.rows == () and table.status == v.SKIPPED and table.complete
    assert table.title == "Fund test, checkpoint 1 of 3: SKIPPED."
    assert table.verdict == (
        "SKIPPED. Calibration had not passed on the night the race's look was readable. Not read, no part of the "
        "5% spent, no bar used. The next bars come from the same rule using only the looks actually read "
        "(planned: checkpoint 2 at 2.41, checkpoint 3 at 2.02).")
    second = v.fund_test_table({**record, "look": 2, "window_end": "2027-03-22"}, read_before=[(60 / 180, 3.40)])
    assert second.verdict.endswith(f"(planned: checkpoint 3 at "
                                   f"{v.bar_text(v.planned_fund_bars([(60 / 180, 3.40)], after_look=2)[0][1])}).")
    last = v.fund_test_table({**record, "look": 3, "window_end": "2027-06-16"})
    assert last.verdict.endswith("no bar used. No later look is left.")


def test_the_planned_bars_follow_the_spending_rule():
    assert v.planned_fund_bars(after_look=0) == [(1, 3.40), (2, 2.41), (3, 2.02)]
    assert v.planned_fund_bars(after_look=1) == [(2, 2.41), (3, 2.02)]
    assert v.planned_fund_bars(after_look=2) == [(3, 1.96)]  # the final look alone spends all 5%
    kept = v.planned_fund_bars([(61 / 180, 3.37)], after_look=1)
    assert [k for k, _ in kept] == [2, 3] and kept[0][1] >= 2.40
    assert v.planned_fund_bars(after_look=3) == []


def test_a_look_left_to_the_owner_and_an_unknown_status():
    owner = v.fund_test_table({"look": 2, "status": "owner", "window_end": "2027-03-22",
                               "reason": v.FUND_OWNER_REASON})
    assert owner.title == "Fund test, checkpoint 2 of 3: THE OWNER DECIDES." and owner.status == v.OWNER
    assert owner.verdict == "THE OWNER DECIDES: 180 or more fund sessions before the final look: the owner decides."
    with pytest.raises(ValueError, match="unknown record status"):
        v.fund_test_table({"look": 1, "status": "maybe"})


def test_a_record_whose_decision_is_not_decides_is_refused():
    record = {**fund_record(), "decision": {"candidate": "momentum", "outcome": "momentum", "reason": "made up"}}
    with pytest.raises(ValueError, match="decide"):
        v.fund_test_table(record)
    candidate, outcome, reason = v.fund_decision(fund_record())
    agreed = {**fund_record(), "decision": {"candidate": candidate, "outcome": outcome, "reason": reason}}
    assert v.fund_test_table(agreed).status == v.NO_DECISION


def test_a_fund_test_look_after_its_deciding_one_is_for_reading_only():
    table = v.fund_test_table(fund_record(look=2, bar=2.41, planned=2.41, mm=-3.5, momentum=3.6), decided_at=1)
    assert table.title.endswith(" For reading only: the fund test was decided at checkpoint 1.")
    assert table.verdict == "FOR READING ONLY" and row(table, "9").result == "no label (nothing decided)"


# --- the combined line, every row of the plan's table ------------------------------------------------------


def side(decided_at=None, outcome=None, look=1, final_read=False, skipped_all=False, next_look=2):
    return {"decided_at": decided_at, "outcome": outcome, "final_read": final_read, "skipped_all": skipped_all,
            "look": look, "window_end": {1: "2026-12-22", 2: "2027-03-22", 3: "2027-06-16"}.get(look),
            "next": None if next_look is None else {"look": next_look,
                                                    "estimated": {2: "2027-03-22", 3: "2027-06-16"}[next_look]}}


@pytest.mark.parametrize("race_side, fund_side, text", [
    (side(1, "none"), side(), 'HOLD THE INDEX — the race decided "no arm trades" (11.8)'),
    (side(1, "none"), side(1, "momentum"), 'HOLD THE INDEX — the race decided "no arm trades" (11.8)'),
    (side(), side(1, "none"), 'HOLD THE INDEX — the fund test decided "no arm trades" (11.8)'),
    (side(1, "momentum"), side(1, "none"), 'HOLD THE INDEX — the fund test decided "no arm trades" (11.8)'),
    (side(1, "momentum"), side(2, "hybrid", look=2),
     "HOLD THE INDEX — the race picked momentum, the fund test picked the hybrid (11.8)"),
    (side(1, "model"), side(1, "model"),
     "THE MODEL WINS BOTH — no real money before the June 2027 verdict (section 9); after it, real money for "
     "the model, starting small if NOT TESTED IN A DOWNTURN"),
    (side(3, "hybrid", look=3, final_read=True, next_look=None), side(3, "hybrid", look=3, final_read=True,
                                                                      next_look=None),
     "THE HYBRID WINS BOTH — no real money before the June 2027 verdict (section 9); after it, real money for "
     "the hybrid, starting small if NOT TESTED IN A DOWNTURN"),
    (side(), side(), "NO DECISION YET — waiting for the race"),
    (side(), side(1, "momentum"), "NO DECISION YET — waiting for the race"),
    (side(1, "momentum"), side(), "NO DECISION YET — waiting for the fund test"),
    (side(1, "momentum"), side(skipped_all=True), "NO DECISION YET — waiting for the fund test"),
    (side(3, "momentum", look=3, final_read=True, next_look=None),
     side(look=3, final_read=True, skipped_all=True, next_look=None),
     "HOLD THE INDEX — the fund test could not be read (calibration never passed)"),
], ids=["race no arm", "race no arm wins over a fund arm", "fund no arm", "fund no arm against a race arm",
        "different arms", "same arm early", "same arm final", "neither decided", "race not decided",
        "fund not decided", "fund skipped so far", "fund skipped at every look"])
def test_the_combined_line_in_every_row_of_the_table(race_side, fund_side, text):
    out = v.combined(race_side, fund_side)
    assert out["text"] == text
    assert list(out) == ["text", "race", "fund_test", "line", "note"]
    assert out["note"] == "No real money before the June 2027 verdict (section 9)."
    assert out["line"].endswith(".") and f"combined: {text}" in out["line"]


def test_the_combined_line_reads_as_the_plan_prints_it():
    out = v.combined(side(1, "momentum", next_look=None), side())
    assert out["line"] == ("CHECKPOINT 1 (2026-12-22) — race: REPLACE THE MODEL WITH MOMENTUM (early stop) · fund "
                           "test: no decision · combined: NO DECISION YET — waiting for the fund test (checkpoint 2, "
                           "about 2027-03-22).")
    final = v.combined(side(3, "model", look=3, next_look=None), side(3, "model", look=3, next_look=None))
    assert "race: KEEP THE MODEL (final) · fund test: KEEP THE MODEL FUND (final)" in final["line"]
    skipped = v.combined(side(1, "momentum"), side(skipped_all=True))
    assert skipped["fund_test"] == "skipped"


def test_before_any_look_the_combined_line_is_no_decision_yet():
    assert v.combined(side(look=None), side(look=None)) == {"text": "no decision yet"}
    assert v.combined({}, {}) == {"text": v.NO_DECISION_YET}


# --- rendering, the block and the JSON ---------------------------------------------------------------------


def test_a_test_data_table_is_marked_on_every_line_and_cannot_be_written():
    table = replace(race(plan_inputs()), test_data=True)
    lines = v.render(table)
    assert lines[0].startswith("TEST DATA · Race, checkpoint 1")
    assert all(line.startswith(("TEST DATA", "- TEST DATA · ")) for line in lines)
    assert lines[-1] == "TEST DATA: every number above is made up."
    assert lines[2].startswith("- TEST DATA · 1 · Keep (a)")
    for writer in (v.table_json, v.render_real, lambda t: v.block([t])):
        with pytest.raises(ValueError, match="TEST DATA"):
            writer(table)


def test_a_real_table_carries_no_mark():
    lines = v.render_real(race(plan_inputs()))
    assert not any("TEST DATA" in line for line in lines) and len(lines) == 12


def test_the_block_says_no_decision_yet_with_nothing_to_show():
    assert v.block() == ["CHECKPOINT VERDICT", "", "no decision yet"]
    tables = [race(plan_inputs()), v.fund_test_table(fund_record())]
    lines = v.block(tables)
    assert lines[:3] == ["CHECKPOINT VERDICT", "", tables[0].title] and lines[14] == ""
    assert lines[15] == tables[1].title


def test_a_table_without_rows_renders_its_title_and_verdict():
    skipped = v.fund_test_table({"look": 1, "status": "skipped", "window_end": "2026-12-22"})
    assert v.render(skipped) == [skipped.title, skipped.verdict]


@pytest.mark.parametrize("make", [
    lambda: race(plan_inputs()),
    lambda: race(plan_inputs(after_tax=None)),
    lambda: race(plan_inputs(unreadable="no close yet")),
    lambda: v.fund_test_table(fund_record()),
    lambda: v.fund_test_table({"look": 1, "status": "skipped", "window_end": "2026-12-22"}),
], ids=["decided", "waiting", "unreadable", "fund test", "skipped"])
def test_the_json_round_trips(make):
    table = make()
    data = v.table_json(table)
    assert list(data) == ["kind", "look", "title", "rows", "verdict", "complete", "status", "outcome"]
    assert v.table_from_json(data) == table
    import json
    assert v.table_from_json(json.loads(json.dumps(data, ensure_ascii=False))) == table


def test_an_older_or_damaged_table_json():
    data = v.table_json(race(plan_inputs()))
    older = {k: data[k] for k in ("kind", "look", "title", "rows", "verdict", "complete")}
    assert v.table_from_json(older).status == v.NO_DECISION and v.table_from_json(older).outcome is None
    for broken in ({**data, "kind": "other"}, {**data, "look": "1"}, {**data, "complete": "yes"},
                   {**data, "rows": [{"n": 1}]}, {**data, "status": "great"}, {k: data[k] for k in ("kind",)},
                   {**data, "title": None}):
        with pytest.raises(ValueError):
            v.table_from_json(broken)


# --- numbers and dates -----------------------------------------------------------------------------------------


def test_numbers_are_printed_as_the_plan_prints_them():
    assert v.t_text(-3.624) == "t = −3.62" and v.t_text(0.84) == "t = 0.84" and v.t_text(None) == "t = n/a"
    assert v.t_text(float("nan")) == "t = n/a"
    assert v.daily_text(0.00012) == "+0.012%" and v.daily_text(-0.00012) == "−0.012%"
    assert v.total_text(0.039) == "+3.90%" and v.total_text(-0.039) == "−3.90%"
    assert v.drawdown_text(0.041) == "4.1%" and v.drawdown_text(None) == "not measured"
    assert v.bar_text(2.0) == "2.00"


def test_dates_outside_the_experiment_are_refused():
    v.check_dates(date(2026, 9, 23), "2027-12-31", None)
    for bad in (date(2026, 9, 22), "2028-01-01", "2099-06-22T00:00:00Z"):
        with pytest.raises(ValueError, match="outside the experiment"):
            v.check_dates(bad)
    v.check_dates(date(2099, 1, 1), test_data=True)
    with pytest.raises(ValueError, match="not a date"):
        v.check_dates("soon")


def test_the_real_builders_refuse_a_date_outside_the_experiment():
    with pytest.raises(ValueError, match="outside the experiment"):
        race(plan_inputs(), window_start=date(2026, 9, 1))
    with pytest.raises(ValueError, match="outside the experiment"):
        race(plan_inputs(), next_look=(2, date(2028, 3, 22), 2.45))
    with pytest.raises(ValueError, match="outside the experiment"):
        v.fund_test_table({**fund_record(), "made_on": "2028-01-02"})
    with pytest.raises(ValueError, match="outside the experiment"):
        v.combined(side(1, "momentum"), {**side(), "window_end": "2026-01-01"})
