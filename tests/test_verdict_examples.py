"""The guards of the owner's Addition 2 (6 Oct 2026): a TEST DATA example can never reach a real output.

The owner: "before the verdict build is merged, show me one printed example
of each table made from test data, clearly marked "TEST DATA". A test must
fail if any example value can appear in a real output."
``tests/verdict_examples.py`` holds the examples; each test below fails if
one of the ways an example could leak opens:

1. a printed example line without the "TEST DATA" mark;
2. an example table that a real writer would accept (``table_json``,
   ``render_real``, ``block``), or a real output (the race's gate JSON and
   report block, the funds run's records) written other than through them;
3. an example's inputs that a real builder would build into a real table
   (every example date is in 2099, outside the experiment);
4. a module outside ``tests/`` that imports the examples, or a workflow,
   shell script, page or setting file outside ``tests/`` that names them
   (it could run them into a step summary, a log or a page);
5. a committed real output (``logs/``, ``dashboard/*.html``) that already
   holds "TEST DATA" or a 2099 date.
"""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

from analysis import verdict
from tests import verdict_examples as examples

ROOT = Path(__file__).resolve().parent.parent
ISO_DAY = re.compile(r"\b(\d{4})-\d{2}-\d{2}\b")


# --- 1. every printed line is marked -------------------------------------------------------------------


def test_every_printed_example_line_says_test_data():
    lines = examples.printout()
    assert lines[0] == "TEST DATA — every number below is made up. None is a result."
    unmarked = [line for line in lines if line.strip() and "TEST DATA" not in line]
    assert unmarked == []


def test_every_date_in_the_printout_is_in_2099():
    years = {match.group(1) for line in examples.printout() for match in ISO_DAY.finditer(line)}
    assert years == {"2099"}


def test_the_printout_has_one_example_of_each_table():
    text = "\n".join(examples.printout())
    for n in range(1, 7):
        assert f"TEST DATA · Example {n} of 6:" in text
    assert "EARLY STOP AT 20: REPLACE THE MODEL WITH MOMENTUM — NOT TESTED IN A DOWNTURN" in text
    assert "NO DECISION AT THIS LOOK — read again at checkpoint 2" in text
    assert "combined: NO DECISION YET — waiting for the fund test" in text
    assert "TEST DATA · CHECKPOINT VERDICT\nTEST DATA · no decision yet" in text
    assert "Fund test, checkpoint 1 of 3: SKIPPED." in text
    assert "· n/a (final look)" in text


def test_the_examples_print_the_same_when_run_as_a_script():
    """``python tests/verdict_examples.py`` from the repo root, as the owner will run it."""
    out = subprocess.run([sys.executable, "tests/verdict_examples.py"], cwd=ROOT, capture_output=True, text=True,
                         check=True, timeout=120)
    assert out.stdout.splitlines() == examples.printout()


# --- 2. no real writer accepts an example table -------------------------------------------------------------


@pytest.mark.parametrize("table", examples.tables(), ids=lambda t: f"{t.kind} {t.look} {t.status}")
def test_no_real_writer_accepts_an_example_table(table):
    assert table.test_data
    with pytest.raises(ValueError, match="TEST DATA"):
        verdict.table_json(table)
    with pytest.raises(ValueError, match="TEST DATA"):
        verdict.render_real(table)
    with pytest.raises(ValueError, match="TEST DATA"):
        verdict.block([table])


def test_the_mark_is_what_stops_the_writers():
    """It is the mark, and nothing else about an example, that the writers refuse: the same table unmarked
    would be written. That is why the real builders must refuse the examples' 2099 dates too (guard 3)."""
    table = replace(examples.race_early_stop(), test_data=False)
    assert verdict.table_json(table)["kind"] == "race"


def test_the_races_real_writers_refuse_an_example_table(monkeypatch):
    """The gate JSON's ``verdict`` and the report's CHECKPOINT VERDICT block are written only through
    ``table_json`` and ``block``: an example table handed to them, in place of a real one, is refused."""
    from datetime import date

    from analysis import horse_race
    from tests.test_horse_race import _view
    from tests.test_verdict import plan_inputs

    example, every = examples.race_early_stop(), examples.tables()
    # Last night's frozen table read look 1 as undecided: tonight's table is not stored, only its words
    # under ``differs_tonight`` and in the report's note, and those too go through ``table_json``.
    real = horse_race.race_verdict(_view(plan_inputs()), None, date(2026, 12, 23))
    previous = {"verdict": json.loads(json.dumps(real.data))}
    frozen = previous["verdict"]["looks"][0]["table"]
    frozen["status"], frozen["outcome"] = verdict.NO_DECISION, None
    monkeypatch.setattr(verdict, "race_table", lambda *a, **k: example)
    with pytest.raises(ValueError, match="TEST DATA"):
        horse_race.race_verdict(_view(plan_inputs()), None, date(2026, 12, 23))
    with pytest.raises(ValueError, match="TEST DATA"):
        horse_race.race_verdict(_view(plan_inputs()), previous, date(2026, 12, 24))
    for table in every:
        with pytest.raises(ValueError, match="TEST DATA"):
            horse_race.checkpoint_lines(horse_race.RaceVerdict({"text": "x"}, (table,)))


@pytest.mark.parametrize("example", ["fund_no_decision", "fund_skipped"])
def test_the_funds_runs_real_writer_refuses_an_example_table(monkeypatch, example):
    """Every fund-test table the funds run writes goes through ``table_json``: an example table in place of a
    real one, read or skipped, is refused, so the document is never printed."""
    from datetime import datetime, timezone

    from shadow import run as shadow_run

    table = getattr(examples, example)()
    monkeypatch.setattr(verdict, "fund_test_table", lambda *a, **k: table)
    race = {"looks": [{"reached": True, "readable": True, "window_end": "2026-12-22"}, {"reached": False},
                      {"reached": False}]}
    with pytest.raises(ValueError, match="TEST DATA"):
        shadow_run.fund_test_part(datetime(2026, 12, 23, 23, tzinfo=timezone.utc), race, [], False, None, None, [],
                                  {})
    from tests.test_fund_test_verdict import record_at

    with pytest.raises(ValueError, match="TEST DATA"):
        record_at(1, 60)


# --- 3. no real builder accepts an example's inputs ---------------------------------------------------------


def test_the_real_race_builder_refuses_the_examples_dates():
    from analysis import decision_gate as gate

    look = gate.evaluate({20: gate.LookInputs(
        entry_days=60, t_model_momentum=-3.62, t_model_hybrid=-1.05, t_hybrid_momentum=0.84, model_mean=0.00012,
        model_band_high=0.00071, window_end=examples.LOOK_DAYS[0])})[0]
    with pytest.raises(ValueError, match="outside the experiment"):
        verdict.race_table(look, 1, window_start=examples.RACE_START)
    with pytest.raises(ValueError, match="outside the experiment"):
        verdict.race_table(look, 1)  # the look's own 2099 window end


def test_the_real_fund_test_builder_refuses_the_examples_records():
    with pytest.raises(ValueError, match="outside the experiment"):
        verdict.fund_test_table(examples.fund_record_no_decision())
    skipped = {"look": 1, "made_on": examples.MADE_ON.isoformat(), "window_end": examples.LOOK_DAYS[0].isoformat(),
               "status": verdict.FUND_SKIPPED}
    with pytest.raises(ValueError, match="outside the experiment"):
        verdict.fund_test_table(skipped)


def test_the_funds_runs_record_builder_refuses_the_examples_dates():
    from shadow import run as shadow_run

    record = examples.fund_record_no_decision()
    with pytest.raises(ValueError, match="outside the experiment"):
        shadow_run.fund_test_record(1, examples.MADE_ON, examples.LOOK_DAYS[0], [examples.LOOK_DAYS[0].isoformat()],
                                    {"funds": {}, "coin": []}, record["after_tax"], 0.041, [],
                                    examples.CALIBRATION_PASSED.isoformat())
    race = {"looks": [{"reached": True, "readable": True, "window_end": examples.LOOK_DAYS[0].isoformat()},
                      {"reached": False}, {"reached": False}]}
    from datetime import datetime, timezone

    # The look is refused, not built: no record, and the note says why (the funds run still prints).
    records: list = []
    note = shadow_run.fund_test_part(datetime(2026, 12, 23, 23, tzinfo=timezone.utc), race, records, False, None,
                                     None, [], {})
    assert records == [] and "outside the experiment" in note


def test_the_combined_line_refuses_the_examples_dates():
    race = {"decided_at": 1, "outcome": "momentum", "look": 1, "window_end": examples.LOOK_DAYS[0].isoformat()}
    with pytest.raises(ValueError, match="outside the experiment"):
        verdict.combined(race, {"look": 1})


# Each printed date on its own: a real-dated input (2026) with exactly one field set to the example's 2099
# value is refused, so dropping the check on any one date fails a test.

def _real_race_look():
    from analysis import decision_gate as gate
    from tests.test_verdict import plan_inputs

    return gate.evaluate({20: plan_inputs()})[0]


def _race_with(field):
    from datetime import date

    from analysis import decision_gate as gate
    from tests.test_verdict import END, plan_inputs

    look = _real_race_look()
    if field == "after_tax_window":
        return verdict.race_table(look, 1, after_tax_window=(examples.FUND_START, END))
    if field == "after_tax_record_window":
        record = replace(plan_inputs().after_tax, window=(date(2026, 9, 29), examples.LOOK_DAYS[0]))
        return verdict.race_table(gate.evaluate({20: plan_inputs(after_tax=record)})[0], 1)
    if field == "next_look":
        return verdict.race_table(look, 1, next_look=(2, examples.LOOK_DAYS[1], 2.45))
    if field == "window_end":
        return verdict.race_table(look, 1, window_end=examples.LOOK_DAYS[0])
    assert field is None
    return verdict.race_table(look, 1, next_look=(2, date(2027, 3, 22), 2.45))


@pytest.mark.parametrize("field", ["after_tax_window", "after_tax_record_window", "next_look", "window_end"])
def test_the_real_race_builder_refuses_each_example_date_on_its_own(field):
    _race_with(None)                                       # the same input with real dates is built
    with pytest.raises(ValueError, match="outside the experiment"):
        _race_with(field)


def _fund_with(field):
    from datetime import date

    from tests.test_verdict import fund_record

    record = fund_record()
    planned_next = (2, date(2027, 3, 22), 2.41)
    if field in ("calibration_passed_on", "made_on"):
        record[field] = (examples.CALIBRATION_PASSED if field == "calibration_passed_on"
                         else examples.MADE_ON).isoformat()
    elif field == "window_end":
        record["window_end"] = examples.LOOK_DAYS[0].isoformat()
    elif field == "start":
        record["start"] = examples.FUND_START.isoformat()
    elif field in ("from", "through"):
        pair = "model-momentum"
        record["tests"][pair] = dict(record["tests"][pair], **{
            field: (examples.FUND_START if field == "from" else examples.LOOK_DAYS[0]).isoformat()})
    elif field == "planned_next":
        planned_next = (2, examples.LOOK_DAYS[1], 2.41)
    else:
        assert field is None
    return verdict.fund_test_table(record, planned_next=planned_next)


@pytest.mark.parametrize("field", ["calibration_passed_on", "made_on", "window_end", "start", "from", "through",
                                   "planned_next"])
def test_the_real_fund_test_builder_refuses_each_example_date_on_its_own(field):
    _fund_with(None)                                       # the same record with real dates is built
    with pytest.raises(ValueError, match="outside the experiment"):
        _fund_with(field)


@pytest.mark.parametrize("side,field", [("race", "window_end"), ("race", "next"), ("fund", "window_end"),
                                        ("fund", "next")])
def test_the_combined_line_refuses_each_example_date_on_its_own(side, field):
    def sides(swap=None):
        race = {"decided_at": 1, "outcome": "momentum", "look": 1, "window_end": "2026-12-22", "next": None}
        fund = {"decided_at": None, "outcome": None, "look": 1, "window_end": "2026-12-22",
                "next": {"look": 2, "estimated": "2027-03-22"}}
        if swap is not None:
            target = race if swap[0] == "race" else fund
            if swap[1] == "window_end":
                target["window_end"] = examples.LOOK_DAYS[0].isoformat()
            else:
                target["next"] = {"look": 2, "estimated": examples.LOOK_DAYS[1].isoformat()}
        return race, fund

    verdict.combined(*sides())                             # real dates: the line is made
    with pytest.raises(ValueError, match="outside the experiment"):
        verdict.combined(*sides((side, field)))


# --- 4. nothing outside tests/ imports the examples ----------------------------------------------------------


def test_no_module_outside_tests_imports_the_examples():
    skip = {".git", "tests", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache"}
    bad = []
    for path in sorted(ROOT.rglob("*.py")):
        if any(part in skip for part in path.relative_to(ROOT).parts):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        # A string on its own as a statement (a docstring) loads nothing; any other string naming the
        # examples might (importlib.import_module("tests.verdict_examples"), __import__, runpy).
        prose = {id(node.value) for node in ast.walk(tree) if isinstance(node, ast.Expr)
                 and isinstance(node.value, ast.Constant)}
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""] + [alias.name for alias in node.names]
            elif isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in prose:
                names = [node.value]
            if any("verdict_examples" in name for name in names):
                bad.append(f"{path.relative_to(ROOT)}:{node.lineno}")
    assert bad == []


#: Files outside tests/ that can run a script into a real output: everything under .github/, and any
#: shell script, workflow or setting file, page or script of the site wherever it is.
RUNNERS = {".sh", ".bash", ".yml", ".yaml", ".html", ".js", ".mjs", ".toml", ".cfg", ".ini"}


def test_no_workflow_script_or_page_outside_tests_names_the_examples():
    """``python tests/verdict_examples.py >> "$GITHUB_STEP_SUMMARY"`` in a workflow would print the examples
    into a real output without importing them: no such file outside ``tests/`` may name them at all."""
    skip = {".git", "tests", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache"}
    bad = []
    for path in sorted(ROOT.rglob("*")):
        parts = path.relative_to(ROOT).parts
        if not path.is_file() or any(part in skip for part in parts):
            continue
        if parts[0] != ".github" and path.suffix not in RUNNERS and path.name not in ("Makefile", "Dockerfile"):
            continue
        if b"verdict_examples" in path.read_bytes():
            bad.append(str(path.relative_to(ROOT)))
    assert bad == []


# --- 5. the committed real outputs hold no example ------------------------------------------------------------


def test_the_committed_outputs_hold_no_test_data_and_no_2099_date():
    paths = [p for p in sorted((ROOT / "logs").rglob("*")) if p.is_file()]
    paths += sorted((ROOT / "dashboard").glob("*.html"))
    assert paths, "no committed output found"
    bad = [str(p.relative_to(ROOT)) for p in paths
           if b"TEST DATA" in (data := p.read_bytes()) or b"2099-" in data]
    assert bad == []
