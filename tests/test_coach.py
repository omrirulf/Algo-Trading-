"""The monthly coach, checklist only (the owner's approval of 3 Oct 2026, with conditions)."""

from __future__ import annotations

import ast
import json
import re
from datetime import date
from pathlib import Path

import yaml

from coach import checklist

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "coach" / "checklist.py"
WORKFLOW = ROOT / ".github" / "workflows" / "coach.yml"
GATE = {"next": {"independent": 20, "estimated": "2026-12-22", "bar": 3.47}}


def test_the_owners_conditions_are_the_settings():
    assert checklist.FIRST_MONTH == date(2026, 11, 1)
    assert checklist.CHECKLIST_ONLY_MONTHS == 2
    assert checklist.MONTHLY_COST_CAP_USD == 0.10
    assert checklist.MODEL_CALLS == 0, "the checklist asks no model"
    assert checklist.DATA_ENTRY_BUILT is False, "no data entry until the owner confirms"


def test_it_runs_on_each_months_first_working_day_from_november():
    assert checklist.first_working_day(2026, 11) == date(2026, 11, 2)   # the 1st is a Sunday
    assert checklist.first_working_day(2026, 12) == date(2026, 12, 1)
    assert checklist.first_working_day(2027, 5) == date(2027, 5, 3)     # Saturday the 1st
    assert not checklist.due(date(2026, 10, 1)), "not before November 2026"
    assert not checklist.due(date(2026, 11, 1)) and checklist.due(date(2026, 11, 2))
    assert checklist.due(date(2026, 12, 1)) and not checklist.due(date(2026, 12, 2))
    # The workflow wakes on the 1st to the 3rd: one of them is always the first working day.
    for year, month in ((2026, 11), (2027, 1), (2027, 5), (2028, 4)):
        assert checklist.first_working_day(year, month).day <= 3


def test_the_message_is_fixed_words_and_the_public_checkpoint_date():
    made = checklist.message(date(2026, 11, 2), GATE)
    assert made["title"] == "🗓️ Monthly check-in" and made["month"] == 1
    text = made["message"]
    for question in checklist.QUESTIONS:
        assert question in text
    assert checklist.KEEP_IT_PRIVATE in text and "send no number anywhere" in text
    assert "next checkpoint about 22 Dec 2026. No decisions before it." in text
    # The only digits are the list's numbers, the month's year and the checkpoint date.
    assert set(re.findall(r"\d+", text)) <= {"1", "2", "3", "4", "2026", "22"}
    assert "last of the two checklist-only months" not in text
    second = checklist.message(date(2026, 12, 1), GATE)
    assert second["month"] == 2 and "last of the two checklist-only months" in second["message"]
    assert "no checkpoint date yet" in checklist.message(date(2027, 1, 1), None)["message"]
    assert checklist.next_checkpoint({"next": {"estimated": "soon"}}) is None


def test_it_asks_for_no_number_and_reads_nothing_personal():
    text = SOURCE.read_text(encoding="utf-8")
    tree = ast.parse(text)
    imported = {alias.name.split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.Import)
                for alias in node.names}
    imported |= {(node.module or "").split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert imported <= {"__future__", "argparse", "json", "sys", "datetime", "pathlib", "typing"}
    for forbidden in ("environ", "getenv", "supabase", "requests", "urllib", "SALARY", "open("):
        assert forbidden not in text, forbidden
    for question in checklist.QUESTIONS:
        assert "enter" not in question.lower() and "send" not in question.lower()


def test_the_cli_prints_json_and_sends_nothing(tmp_path, capsys):
    gate = tmp_path / "race_gate.json"
    gate.write_text(json.dumps(GATE))
    assert checklist.main(["--race-gate", str(gate), "--today", "2026-11-03"]) == 0
    assert json.loads(capsys.readouterr().out) == {"date": "2026-11-03", "due": False}
    assert checklist.main(["--race-gate", str(gate), "--today", "2026-11-02"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["due"] is True and "22 Dec 2026" in out["message"]
    assert checklist.main(["--race-gate", str(tmp_path / "missing.json"), "--today", "2026-11-04", "--force"]) == 0
    assert "no checkpoint date yet" in json.loads(capsys.readouterr().out)["message"]


def test_the_workflow_holds_only_the_phone_topic_and_commits_nothing():
    text = WORKFLOW.read_text(encoding="utf-8")
    wf = yaml.safe_load(text)
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"schedule", "workflow_dispatch"}
    assert [c["cron"] for c in triggers["schedule"]] == ["10 6 1-3 * *"]
    assert wf["permissions"] == {"contents": "read"}
    assert set(re.findall(r"secrets\.([A-Z_]+)", text)) == {"NTFY_TOPIC"}
    for word in ("git push", "git commit", "SUPABASE", "API_KEY", "upload-artifact"):
        assert word not in text, word
    send = next(s for s in wf["jobs"]["checklist"]["steps"] if s.get("name") == "Send it to the owner's phone")
    assert '"topic": os.environ["NTFY_TOPIC"]' in send["run"] and 'rm -f "$RUNNER_TEMP/phone.json"' in send["run"]
    assert "https://ntfy.sh/" in send["run"] and "ntfy.sh/$" not in send["run"], "the topic never goes in a URL"


def test_the_plan_records_the_owners_conditions():
    plan = " ".join((ROOT / "docs" / "research" / "monthly-coach-plan.md").read_text(encoding="utf-8").split())
    for phrase in ("approved by the owner on 3 Oct 2026", "Checklist only for the first two months",
                   "Collect no personal numbers yet", "$0.10 a month", "private Supabase project",
                   "percentages only", "not built until the owner confirms"):
        assert phrase in plan, phrase
