"""The guards of the owner's Addition 2 (6 Oct 2026): a TEST DATA example can never reach a real output.

The owner: "before the verdict build is merged, show me one printed example
of each table made from test data, clearly marked "TEST DATA". A test must
fail if any example value can appear in a real output."
``tests/verdict_examples.py`` holds the examples; each test below fails if
one of the ways an example could leak opens:

1. a printed example line without the "TEST DATA" mark;
2. an example table that a real writer would accept (``table_json``,
   ``render_real``, ``block``);
3. an example's inputs that a real builder would build into a real table
   (every example date is in 2099, outside the experiment);
4. a module outside ``tests/`` that imports the examples;
5. a committed real output (``logs/``, ``dashboard/*.html``) that already
   holds "TEST DATA" or a 2099 date.
"""

from __future__ import annotations

import ast
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


def test_the_combined_line_refuses_the_examples_dates():
    race = {"decided_at": 1, "outcome": "momentum", "look": 1, "window_end": examples.LOOK_DAYS[0].isoformat()}
    with pytest.raises(ValueError, match="outside the experiment"):
        verdict.combined(race, {"look": 1})


# --- 4. nothing outside tests/ imports the examples ----------------------------------------------------------


def test_no_module_outside_tests_imports_the_examples():
    skip = {".git", "tests", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache"}
    bad = []
    for path in sorted(ROOT.rglob("*.py")):
        if any(part in skip for part in path.relative_to(ROOT).parts):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""] + [alias.name for alias in node.names]
            if any("verdict_examples" in name for name in names):
                bad.append(f"{path.relative_to(ROOT)}:{node.lineno}")
    assert bad == []


# --- 5. the committed real outputs hold no example ------------------------------------------------------------


def test_the_committed_outputs_hold_no_test_data_and_no_2099_date():
    paths = [p for p in sorted((ROOT / "logs").rglob("*")) if p.is_file()]
    paths += sorted((ROOT / "dashboard").glob("*.html"))
    assert paths, "no committed output found"
    bad = [str(p.relative_to(ROOT)) for p in paths
           if b"TEST DATA" in (data := p.read_bytes()) or b"2099-" in data]
    assert bad == []
