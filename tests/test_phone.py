"""The phone hears from the workflows directly: no Claude session in the loop.

Three things a push step must never do: put the topic in a URL, print it, or
fail the run. And the failure push must stay quiet when the brief already
carried the alarm.
"""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _steps(workflow: str, job: str) -> dict:
    wf = yaml.safe_load((ROOT / ".github/workflows" / workflow).read_text())
    return {s.get("name"): s for s in wf["jobs"][job]["steps"]}


def _is_a_safe_push(step: dict) -> None:
    run = step["run"]
    assert step["env"]["NTFY_TOPIC"] == "${{ secrets.NTFY_TOPIC }}"
    assert "https://ntfy.sh/" in run and "ntfy.sh/$" not in run and "ntfy.sh/${" not in run   # topic in the body, never the URL
    assert '"topic": os.environ["NTFY_TOPIC"]' in run
    assert 'if [ -z "${NTFY_TOPIC:-}" ]' in run and "exit 0" in run                          # unset: says so, sends nothing
    assert "echo $NTFY_TOPIC" not in run and "echo ${NTFY_TOPIC" not in run
    assert 'rm -f "$RUNNER_TEMP/phone.json"' in run                                          # the file that carried it goes
    assert "-o /dev/null -w '%{http_code}'" in run and "exit 1" not in run                   # never fails the job
    assert "::warning::phone not notified" in run


def test_the_brief_goes_to_the_phone_the_moment_it_is_written():
    steps = _steps("heartbeat.yml", "cycle")
    names = list(steps)
    step = steps["Push the day to the owner's phone"]
    _is_a_safe_push(step)
    assert names.index("Push the day to the owner's phone") == names.index("Write the book snapshot") + 1
    assert step["if"] == steps["Write the book snapshot"]["if"]
    assert step["id"] == "phone"
    run = step["run"]
    assert 'pathlib.Path("logs/brief.txt")' in run
    assert 'priority = 5 if first.startswith("🔴") else 4 if first.startswith("⚠️") else 3' in run
    assert step["env"]["DESK_URL"] == "https://omrirulf.github.io/Algo-Trading-/"


def test_a_red_run_reaches_the_phone_unless_the_brief_already_did():
    steps = _steps("heartbeat.yml", "cycle")
    assert steps["Sound the alarm on anything the record says went quietly wrong"]["id"] == "health"
    step = steps["Push the failure to the owner's phone"]
    _is_a_safe_push(step)
    assert step["if"] == "failure() && steps.guard.outputs.skip != 'yes' && steps.health.outcome != 'failure'"
    assert '"priority": 5' in step["run"] and "run failed" in step["run"]
    names = list(steps)
    assert names.index("Push the failure to the owner's phone") > names.index("Commit the journal")


def test_a_dead_source_reaches_the_phone_as_a_warning():
    steps = _steps("data-sources.yml", "probe")
    step = steps["Push the dead source to the owner's phone"]
    _is_a_safe_push(step)
    assert step["if"] == "failure()"
    assert '"priority": 4' in step["run"]


def test_the_phone_test_button_sends_one_message_and_nothing_else():
    wf = yaml.safe_load((ROOT / ".github/workflows/phone-test.yml").read_text())
    on = wf[True] if True in wf else wf["on"]
    assert on == {"workflow_dispatch": None} or on == "workflow_dispatch" or list(on) == ["workflow_dispatch"]
    assert wf["permissions"] == {"contents": "read"}
    steps = {s.get("name"): s for s in wf["jobs"]["ping"]["steps"]}
    assert list(steps) == ["Push a test message to the owner's phone"]
    step = steps["Push a test message to the owner's phone"]
    _is_a_safe_push(step)
    assert "Phone connected" in step["run"]
    for banned in ("actions/checkout", "pip install", "python -m orchestrator", "alpaca"):
        assert banned not in (ROOT / ".github/workflows/phone-test.yml").read_text(), banned


def test_the_topic_is_read_nowhere_in_the_code():
    # The workflows pass it to curl and nothing else; no module reads it.
    for path in ROOT.rglob("*.py"):
        if "tests" in path.parts or ".git" in path.parts:
            continue
        assert "NTFY" not in path.read_text(), path
