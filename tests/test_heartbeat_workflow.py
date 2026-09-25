"""The daily run's wiring: when it starts, what can start it, and why a day
cannot run twice.

The logic is tested in test_cycle_day.py and test_watchdog.py. This file
pins the two workflow files that connect it, because a YAML condition is
code nothing else runs until the day it matters.

PyYAML reads a bare ``on:`` key as the boolean True, hence ``wf[True]``.
"""

from __future__ import annotations

import ast
import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path

import pytest
import yaml

from analysis import watchdog
from analysis.cycle_day import LATEST_START_NY, SCHEDULED_START_UTC
from tests.test_phone import _is_a_safe_push

ROOT = Path(__file__).resolve().parents[1]
HEARTBEAT = ROOT / ".github/workflows/heartbeat.yml"
WATCHDOG = ROOT / ".github/workflows/heartbeat-watchdog.yml"

CHECKOUT = "actions/checkout@11d5960a326750d5838078e36cf38b85af677262"
SETUP_PYTHON = "actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065"


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text())


def _steps(path: Path, job: str) -> list[dict]:
    return _load(path)["jobs"][job]["steps"]


def _named(path: Path, job: str) -> dict:
    return {s.get("name"): s for s in _steps(path, job)}


def _minutes(cron: str) -> int:
    minute, hour = cron.split()[:2]
    return int(hour) * 60 + int(minute)


# --------------------------------------------------------------------------- #
# heartbeat.yml: when
# --------------------------------------------------------------------------- #

def test_the_crons_are_the_after_open_start_and_the_catch_up():
    crons = [e["cron"] for e in _load(HEARTBEAT)[True]["schedule"]]
    assert crons == ["40 14 * * 1-5", "35 17 * * 1-5"]


def test_no_heartbeat_cron_starts_before_the_open_in_either_season():
    """The winter open is 14:30 UTC (09:30 EST). A cron before it starts a
    cycle that sends orders into a closed market -- what 12:35 would have
    done every day since 23 Sep had GitHub delivered it on time."""
    for entry in _load(HEARTBEAT)[True]["schedule"]:
        assert _minutes(entry["cron"]) >= 14 * 60 + 30, entry["cron"]


def test_the_scheduled_start_constant_is_the_first_cron():
    first = _load(HEARTBEAT)[True]["schedule"][0]["cron"]
    assert _minutes(first) == SCHEDULED_START_UTC.hour * 60 + SCHEDULED_START_UTC.minute


def test_nothing_in_the_heartbeat_passes_the_premarket_flag():
    """Not in a step, not in a condition, not even in a comment someone
    might copy back into a step."""
    assert "--premarket" not in HEARTBEAT.read_text()
    cycle = _named(HEARTBEAT, "cycle")["Run one cycle"]
    assert cycle["run"].strip().endswith("python -m orchestrator.heartbeat --once")
    assert "github.event.schedule" not in cycle["run"]


# --------------------------------------------------------------------------- #
# heartbeat.yml: who
# --------------------------------------------------------------------------- #

def test_the_dispatch_inputs():
    inputs = _load(HEARTBEAT)[True]["workflow_dispatch"]["inputs"]
    assert inputs["mode"]["options"] == ["cycle", "protect"] and inputs["mode"]["default"] == "cycle"
    assert inputs["started_by"]["type"] == "choice"
    assert inputs["started_by"]["options"] == ["manual", "backup"]
    assert inputs["started_by"]["default"] == "manual"
    assert inputs["rerun"]["type"] == "boolean" and inputs["rerun"]["default"] is False
    assert "only for a person" in inputs["rerun"]["description"]


def test_the_run_name_tells_the_runs_apart():
    """The watchdog tells cycles from protection passes, and its own backups
    from everything else, by this title."""
    name = _load(HEARTBEAT)["run-name"]
    for piece in ("'heartbeat protect'", "heartbeat cycle ({0})", "inputs.mode == 'protect'",
                  "github.event_name == 'schedule' && 'schedule'", "inputs.started_by", "'manual'"):
        assert piece in name, piece
    # The words the watchdog matches on.
    assert "protect" in name and "{0}" in name


# --------------------------------------------------------------------------- #
# heartbeat.yml: never twice
# --------------------------------------------------------------------------- #

def test_the_checkout_reads_the_branch_tip_not_the_commit_the_run_was_created_on():
    for path, job in ((HEARTBEAT, "cycle"), (WATCHDOG, "watch")):
        checkout = next(s for s in _steps(path, job) if str(s.get("uses", "")).startswith("actions/checkout"))
        assert checkout["uses"] == CHECKOUT, path.name
        assert checkout["with"]["ref"] == "${{ github.ref }}", path.name


def test_the_guard_covers_every_cycle_run_and_only_rerun_bypasses_it():
    """Only on its first attempt: "Re-run" replays the dispatch, `rerun`
    included, and would otherwise trade a day its first attempt traded."""
    guard = next(s for s in _steps(HEARTBEAT, "cycle") if s.get("id") == "guard")
    condition = guard["if"]
    assert condition == "inputs.mode != 'protect' && (inputs.rerun != true || github.run_attempt != '1')"
    # Nothing about the event: a schedule and a dispatch are asked alike.
    assert "event_name" not in condition and "schedule" not in condition


def test_the_guard_runs_before_anything_that_trades():
    names = [s.get("name") or s.get("id") for s in _steps(HEARTBEAT, "cycle")]
    ids = [s.get("id") for s in _steps(HEARTBEAT, "cycle")]
    guard = ids.index("guard")
    assert guard < names.index("Protect every open position")
    assert guard < names.index("Run one cycle")


def test_the_cycle_step_requires_the_guard_not_to_have_said_skip():
    cycle = _named(HEARTBEAT, "cycle")["Run one cycle"]
    assert "steps.guard.outputs.skip != 'yes'" in cycle["if"]
    assert "inputs.mode != 'protect'" in cycle["if"]


def test_no_step_still_reads_the_old_guard_output():
    text = HEARTBEAT.read_text()
    assert "outputs.ran" not in text
    for step in _steps(HEARTBEAT, "cycle"):
        assert "outputs.ran" not in str(step.get("if", "")), step.get("name")


def test_only_one_heartbeat_run_at_a_time_and_none_cancelled():
    concurrency = _load(HEARTBEAT)["concurrency"]
    assert concurrency == {"group": "heartbeat", "cancel-in-progress": False}


def test_a_backup_that_reaches_the_guard_too_late_tells_the_phone():
    """The watchdog's message said "the backup has started it". If GitHub
    brought that run to the guard after the latest safe start anyway, the
    owner hears that nothing traded -- only for the backup, which is the
    only trigger that promised anything."""
    steps = _steps(HEARTBEAT, "cycle")
    names = [s.get("name") for s in steps]
    step = _named(HEARTBEAT, "cycle")["Tell the owner's phone the backup started too late"]
    _is_a_safe_push(step)
    assert step["if"] == "steps.guard.outputs.why == 'too_late' && inputs.started_by == 'backup'"
    guard = [s.get("id") for s in steps].index("guard")
    assert names.index("Tell the owner's phone the backup started too late") == guard + 1
    assert '"priority": 5' in step["run"] and "backup started too late" in step["run"]
    for banned in ("ALPACA", "ANTHROPIC", "API_KEY"):
        assert banned not in str(step["env"]), banned


def test_the_cycle_step_hands_the_journal_its_run_block():
    cycle = _named(HEARTBEAT, "cycle")["Run one cycle"]
    run = cycle["run"]
    assert "python analysis/cycle_day.py --run-block" in run
    assert "export HEARTBEAT_RUN" in run
    # A block that cannot be built must never stop the cycle.
    assert '|| HEARTBEAT_RUN=""' in run
    env = cycle["env"]
    assert env["RUN_EVENT"] == "${{ github.event_name }}"
    assert env["RUN_STARTED_BY"] == "${{ inputs.started_by }}"
    assert env["RUN_ID"] == "${{ github.run_id }}"
    # Only this step: nothing else in the job is described as the cycle.
    others = [s.get("name") for s in _steps(HEARTBEAT, "cycle")
              if s.get("name") != "Run one cycle" and "HEARTBEAT_RUN" in str(s)]
    assert others == []


# --------------------------------------------------------------------------- #
# heartbeat.yml: the guard reads GitHub's record, not only the journal
# --------------------------------------------------------------------------- #

def _guard() -> dict:
    return next(s for s in _steps(HEARTBEAT, "cycle") if s.get("id") == "guard")


def test_the_heartbeat_may_push_open_issues_and_read_its_own_runs_nothing_more():
    """`actions: read` is for the guard alone: listing today's heartbeat runs
    and the steps they reached. Not write: this workflow never starts,
    cancels or re-runs anything."""
    wf = _load(HEARTBEAT)
    assert wf["permissions"] == {"contents": "write", "issues": "write", "actions": "read"}
    assert "permissions" not in wf["jobs"]["cycle"], "a job-level block would override the workflow's"


def test_the_guard_asks_github_for_todays_runs_and_the_steps_they_reached():
    """The journal cannot show a run that traded and whose commit never reached
    the branch; GitHub's record can. Every attempt's jobs (`filter=all`), for
    every run whatever its status (a run re-run from its page waits as
    "pending" with the attempt that traded still in its jobs), and this
    run's own id, attempt and `rerun` so the script can leave this attempt
    out and tell a re-run of a rerun from anything else. Every call has a
    time limit: gh has none, and a stalled answer would hold the concurrency
    group for the job's 180 minutes."""
    guard = _guard()
    assert guard["env"] == {"GH_TOKEN": "${{ github.token }}", "THIS_RUN": "${{ github.run_id }}",
                            "THIS_ATTEMPT": "${{ github.run_attempt }}", "RERUN": "${{ inputs.rerun }}"}
    run = guard["run"]
    assert ('timeout 30 gh api -X GET "repos/${{ github.repository }}/actions/workflows/heartbeat.yml/runs"'
            in run)
    # Today in New York, the day the script counts runs by -- not the UTC date,
    # which is already tomorrow for the last hours of a New York evening.
    assert '-f created=">=$(TZ=America/New_York date +%F)" -f per_page=100' in run
    assert "jq -r '.workflow_runs[]? | .id | numbers'" in run
    assert "select(" not in run and ".status" not in run, "every run's jobs are read, whatever its status"
    assert ('timeout 30 gh api "repos/${{ github.repository }}/actions/runs/$id/jobs?filter=all&per_page=100"'
            in run)
    assert all(line.lstrip().startswith(("timeout 30 gh api", "if timeout 30 gh api"))
               for line in run.splitlines() if "gh api" in line), "every call is time-limited"
    assert 'rm -f "$record/jobs/$id.json"' in run, "a failed read must not leave half a file"
    assert 'rm -f "$record/runs.json"' in run
    assert '--runs "$record/runs.json" --jobs "$record/jobs"' in run
    assert '--this-run "$THIS_RUN" --this-attempt "$THIS_ATTEMPT" --rerun "$RERUN"' in run
    assert '>> "$GITHUB_STEP_SUMMARY"' in run
    assert "secrets." not in str(guard)


def _run_the_guard(tmp_path: Path, *, runs, jobs: dict, this_run: str = "99",
                   this_attempt: str = "1", rerun: str = "") -> tuple[int, dict, str, str]:
    """heartbeat.yml's guard step, as bash runs it on the runner, against a
    fake `gh` that answers from ``runs`` and ``jobs`` (None: the call fails;
    STALL: the call never answers). The time limit on each call is cut from
    30 seconds to 1, so a stalled call does not hold the test.

    The journal is empty, so any "already" comes from GitHub's record.
    Returns the exit code, the step's outputs, its summary and its log.
    """
    if not (shutil.which("jq") and shutil.which("bash")):
        pytest.skip("needs bash and jq, as the runner has")
    work = tmp_path / "work"
    (work / "logs").mkdir(parents=True)
    (work / "analysis").symlink_to(ROOT / "analysis")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "python").write_text(f'#!/bin/sh\nexec "{sys.executable}" "$@"\n')
    (bin_dir / "python").chmod(0o755)
    answers = tmp_path / "answers"
    answers.mkdir()
    if runs is not None:
        (answers / "runs.json").write_text(runs if isinstance(runs, str) else json.dumps(runs))
    for run_id, answer in jobs.items():
        if answer is not None:
            (answers / f"{run_id}.json").write_text(json.dumps(answer))
    gh = bin_dir / "gh"
    gh.write_text(f"#!{sys.executable}\n" + textwrap.dedent(f"""
        import pathlib, re, sys
        path = next(a for a in sys.argv[1:] if a.startswith("repos/"))
        with open({str(tmp_path / "calls.log")!r}, "a") as log:
            log.write(" ".join(sys.argv[1:]) + "\\n")
        match = re.search(r"/runs/(\\d+)/jobs\\?filter=all", path)
        answer = pathlib.Path({str(answers)!r}) / (match.group(1) + ".json" if match else "runs.json")
        if not answer.exists():
            print("HTTP 502: Bad Gateway", file=sys.stderr)
            raise SystemExit(1)
        if answer.read_text().strip().strip('"') == "STALL":
            import time
            time.sleep(20)
        print(answer.read_text())
    """))
    gh.chmod(0o755)
    outputs, summary = tmp_path / "outputs", tmp_path / "summary.md"
    outputs.write_text("")
    summary.write_text("")
    script = _guard()["run"].replace("${{ github.repository }}", "owner/repo")
    assert "${{" not in script and script.count("timeout 30 gh api") == 2
    script = script.replace("timeout 30 gh api", "timeout 1 gh api")
    env = {**os.environ, "PATH": f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
           "RUNNER_TEMP": str(tmp_path / "runner"), "GITHUB_OUTPUT": str(outputs),
           "GITHUB_STEP_SUMMARY": str(summary), "GH_TOKEN": "not-a-token",
           "THIS_RUN": this_run, "THIS_ATTEMPT": this_attempt, "RERUN": rerun}
    (tmp_path / "runner").mkdir()
    done = subprocess.run(["bash", "-e", "-c", script], cwd=work, env=env,
                          capture_output=True, text=True, timeout=60)
    found = dict(line.split("=", 1) for line in outputs.read_text().splitlines() if "=" in line)
    return done.returncode, found, summary.read_text(), done.stdout + done.stderr


def _github_run(id: int, status: str = "completed", conclusion: str | None = "failure") -> dict:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {"id": id, "display_title": "heartbeat cycle (manual)", "status": status,
            "conclusion": conclusion, "created_at": now, "run_started_at": now}


def _steps_reached(trading: str | None, attempt: int = 1, status: str = "completed") -> dict:
    return {"total_count": 1, "jobs": [{"name": "cycle", "run_attempt": attempt, "status": status, "steps": [
        {"name": "May this run start a cycle?", "status": "completed", "conclusion": "success"},
        {"name": "Run one cycle", "status": status if trading is None else "completed", "conclusion": trading},
    ]}]}


def _attempts(*jobs: dict) -> dict:
    """One run's jobs answer with ``filter=all``: every attempt's job, newest first."""
    return {"total_count": len(jobs), "jobs": [answer["jobs"][0] for answer in jobs]}


def test_the_guard_stops_after_another_run_today_reached_its_trading_step(tmp_path):
    """The owner's case, end to end: a run traded at 15:05 and its commit never
    reached the branch; the journal is empty; the late cron must stop."""
    me = _github_run(99, "in_progress", None)
    code, outputs, summary, log = _run_the_guard(
        tmp_path, runs={"total_count": 2, "workflow_runs": [me, _github_run(41)]},
        jobs={"41": _steps_reached("success"), "99": _steps_reached(None, status="in_progress")})
    assert code == 0, log
    assert outputs == {"skip": "yes", "why": "already"}
    assert ("Another run today already reached its trading step (run 41, failure); a second cycle "
            "could repeat profit-ladder sales.") in summary
    assert "Re-run by hand with rerun only after checking the account" in summary
    assert "filter=all" in (tmp_path / "calls.log").read_text()


def test_the_guard_does_not_count_this_run_but_does_count_its_earlier_attempts(tmp_path):
    """This run's own trading step is listed while its guard runs; it must not
    stop itself. A re-run from GitHub's page after an attempt that traded
    must stop, or "Re-run" is a way past the guard."""
    me = _github_run(99, "in_progress", None)
    this_attempt = _steps_reached(None, attempt=1, status="in_progress")
    code, outputs, summary, log = _run_the_guard(
        tmp_path / "first", runs={"workflow_runs": [me]}, jobs={"99": this_attempt})
    assert code == 0, log
    assert outputs.get("why") != "already", summary
    rerun = {"jobs": [_steps_reached(None, attempt=2, status="in_progress")["jobs"][0],
                      _steps_reached("failure", attempt=1)["jobs"][0]]}
    code, outputs, summary, log = _run_the_guard(
        tmp_path / "second", runs={"workflow_runs": [me]}, jobs={"99": rerun}, this_attempt="2")
    assert code == 0, log
    assert outputs == {"skip": "yes", "why": "already"}
    assert "an earlier attempt of this run" in summary


def test_the_guard_reads_a_run_that_traded_while_its_re_run_waits(tmp_path):
    """Run 41 traded and lost its record; this run took the concurrency group;
    someone pressed "Re-run" on 41 while this one was still installing. 41
    is "pending" again, and its jobs (every attempt) still hold the attempt
    that traded -- the guard must ask for them, whatever the status says."""
    me = _github_run(99, "in_progress", None)
    pending = _github_run(41, "pending", None)
    waiting = {"jobs": [{"name": "cycle", "run_attempt": 2, "status": "queued", "steps": []},
                        _steps_reached("success")["jobs"][0]]}
    code, outputs, summary, log = _run_the_guard(
        tmp_path, runs={"workflow_runs": [me, pending]},
        jobs={"41": waiting, "99": _steps_reached(None, status="in_progress")})
    assert code == 0, log
    assert outputs == {"skip": "yes", "why": "already"}
    assert "(run 41, pending)" in summary
    assert "actions/runs/41/jobs?filter=all" in (tmp_path / "calls.log").read_text()


def test_the_guard_stops_a_re_run_of_a_rerun_whose_first_attempt_traded(tmp_path):
    """The rescue traded, its push was refused, and "Re-run failed jobs"
    replayed `rerun`. Attempt 2 reaches the guard (heartbeat.yml runs it on
    any attempt after the first) and stops; had attempt 1 never reached its
    trading step, attempt 2 would run, as rerun asked -- even though another
    run today did."""
    me = _github_run(99, "in_progress", None)
    this_attempt = _steps_reached(None, attempt=2, status="in_progress")
    traded = _attempts(this_attempt, _steps_reached("success", attempt=1))
    code, outputs, summary, log = _run_the_guard(
        tmp_path / "traded", runs={"workflow_runs": [me]}, jobs={"99": traded},
        this_attempt="2", rerun="true")
    assert code == 0, log
    assert outputs == {"skip": "yes", "why": "already"}
    assert "An earlier attempt of this run already reached its trading step." in summary
    never = _attempts(this_attempt, _steps_reached("skipped", attempt=1))
    code, outputs, summary, log = _run_the_guard(
        tmp_path / "never", runs={"workflow_runs": [me, _github_run(41)]},
        jobs={"99": never, "41": _steps_reached("success")}, this_attempt="2", rerun="true")
    assert code == 0, log
    assert outputs == {"skip": "no"}
    assert "so it runs, as rerun asked" in summary


def test_the_guard_does_not_count_a_run_that_was_over_before_the_open(tmp_path):
    """A dispatch at 04:00 New York stopped at the market-closed gate, green,
    with nothing journalled: it placed nothing, so a later cycle today is the
    day's, not a second one. The same run still going at 10:00 counts."""
    from zoneinfo import ZoneInfo

    new_york = ZoneInfo("America/New_York")
    today = datetime.now(new_york).date()

    def stamp(hour: int, minute: int) -> str:
        moment = datetime(today.year, today.month, today.day, hour, minute, tzinfo=new_york)
        return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    me = _github_run(99, "in_progress", None)
    early = {**_github_run(7, conclusion="success"), "created_at": stamp(4, 0)}
    for ended, counts in ((stamp(4, 1), False), (stamp(10, 0), True)):
        reached = _steps_reached("success")
        for step in reached["jobs"][0]["steps"]:
            step["started_at"], step["completed_at"] = stamp(4, 0), ended
        code, outputs, summary, log = _run_the_guard(
            tmp_path / str(counts), runs={"workflow_runs": [me, early]},
            jobs={"7": reached, "99": _steps_reached(None, status="in_progress")})
        assert code == 0, log
        # "yes" without "already" only as too_late, by the clock this test runs at.
        assert (outputs.get("why") == "already") is counts, summary


def test_a_stalled_github_is_a_github_that_cannot_be_read(tmp_path):
    """gh has no time limit of its own. A call that never answers is cut off
    and handled like one that failed: the guard decides without it."""
    code, outputs, summary, log = _run_the_guard(
        tmp_path / "list", runs="STALL", jobs={})
    assert code == 0, log
    assert "could not list today's heartbeat runs" in log and "journal alone" in summary
    code, outputs, summary, log = _run_the_guard(
        tmp_path / "steps", runs={"workflow_runs": [_github_run(41)]}, jobs={"41": "STALL"})
    assert code == 0, log
    assert "could not read the steps of run 41" in log
    assert outputs.get("why") != "already"


@pytest.mark.parametrize("runs, jobs, says", [
    (None, {}, "could not list today's heartbeat runs"),                 # GitHub down
    ("<html>rate limited</html>", {}, "decided from the journal alone"),  # junk
    ({"workflow_runs": [_github_run(41)]}, {"41": None}, "could not read the steps of run 41"),
])
def test_a_github_that_cannot_be_read_never_fails_the_guard(tmp_path, runs, jobs, says):
    """It decides from the journal alone, as before 25 Sep, and says so --
    never a red run, never a lost day, for an API hiccup."""
    code, outputs, summary, log = _run_the_guard(tmp_path, runs=runs, jobs=jobs)
    assert code == 0, log
    assert outputs.get("why") != "already"
    assert outputs["skip"] in ("no", "yes")          # "yes" only as too_late, by the clock
    assert says in log + summary
    assert "journal alone" in summary


# --------------------------------------------------------------------------- #
# heartbeat.yml: the journal push is tried three times
# --------------------------------------------------------------------------- #

def _commit_step() -> str:
    return _named(HEARTBEAT, "cycle")["Commit the journal"]["run"]


def test_the_journal_push_is_retried_a_bounded_number_of_times():
    """A refused push loses the audit log the profit ladder counts from, and
    the guard then stops the day for everyone but a person. Three tries, a
    few seconds apart; the last one outside the loop, so its failure still
    fails the step."""
    run = _commit_step()
    assert "for attempt in 1 2; do" in run
    assert 'if sync_with_branch && git push origin "HEAD:${GITHUB_REF_NAME}"; then' in run
    assert "exit 0" in run and "sleep 5" in run
    assert "git rebase --abort 2>/dev/null || true" in run, "a half-done rebase is undone before the next try"
    assert "try $attempt of 3" in run
    lines = [line.strip() for line in run.strip().splitlines()]
    assert lines[-2:] == ["sync_with_branch", 'git push origin "HEAD:${GITHUB_REF_NAME}"']
    code = [line for line in lines if not line.startswith("#")]
    assert not any(line.startswith(("while ", "until ")) for line in code), \
        "bounded, never a loop that could spin until the job's timeout"


def _run_the_commit(tmp_path: Path, *, refuse: int) -> tuple[int, str, Path]:
    """The commit step, as bash runs it, against a local remote that refuses
    the first ``refuse`` pushes. ``sleep`` is stubbed so the test does not wait."""
    if not shutil.which("git"):
        pytest.skip("needs git")
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
           "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@t", "GITHUB_REF_NAME": "main"}

    def git(*args: str, cwd: Path = tmp_path) -> None:
        subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True)

    git("init", "-q", "--bare", "-b", "main", "origin.git")
    work = tmp_path / "work"
    git("clone", "-q", str(tmp_path / "origin.git"), str(work))
    (work / "logs").mkdir()
    for name in ("signal_journal.log", "execution_audit.log", "cycle_report.md", "fund_size.log",
                 "blend_weights.json", "score_report.md", "book.json", "brief.txt", "account.jsonl"):
        (work / "logs" / name).write_text(f"yesterday's {name}\n")
    (work / ".gitattributes").write_text((ROOT / ".gitattributes").read_text())
    git("add", "-f", ".", cwd=work)
    git("commit", "-qm", "yesterday", cwd=work)
    git("push", "-q", "origin", "HEAD:main", cwd=work)
    hook = tmp_path / "origin.git" / "hooks" / "pre-receive"
    count = tmp_path / "pushes"
    hook.write_text(f"#!/bin/sh\nn=$(cat {count} 2>/dev/null || echo 0); n=$((n+1)); echo $n > {count}\n"
                    f"[ $n -le {refuse} ] && {{ echo refused >&2; exit 1; }}\nexit 0\n")
    hook.chmod(0o755)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "sleep").write_text("#!/bin/sh\nexit 0\n")
    (bin_dir / "sleep").chmod(0o755)
    with (work / "logs" / "signal_journal.log").open("a") as journal:
        journal.write("today's line\n")
    script = _commit_step().replace("${{ inputs.mode == 'protect' && 'protection pass' || 'cycle' }}", "cycle")
    assert "${{" not in script
    done = subprocess.run(["bash", "-e", "-c", script], cwd=work, capture_output=True, text=True,
                          env={**env, "PATH": f"{bin_dir}{os.pathsep}{env['PATH']}"}, timeout=60)
    return done.returncode, done.stdout + done.stderr, tmp_path / "origin.git"


def test_every_rendered_file_that_conflicts_is_taken_from_this_run(tmp_path):
    """The branch moved while this run ran, and the other push rewrote every
    file this run renders whole -- the book and the brief included. The
    append-only logs merge as a union; each rendered file is this run's,
    the newer. A rendered file left out of that list would stop the rebase
    on all three tries and lose the day's record."""
    if not shutil.which("git"):
        pytest.skip("needs git")
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
           "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@t", "GITHUB_REF_NAME": "main"}

    def git(*args: str, cwd: Path = tmp_path) -> str:
        return subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True,
                              text=True).stdout

    rendered = ("cycle_report.md", "score_report.md", "blend_weights.json", "book.json", "brief.txt")
    logs = ("signal_journal.log", "execution_audit.log", "fund_size.log", "account.jsonl")
    git("init", "-q", "--bare", "-b", "main", "origin.git")
    work, other = tmp_path / "work", tmp_path / "other"
    git("clone", "-q", str(tmp_path / "origin.git"), str(work))
    (work / "logs").mkdir()
    for name in rendered + logs:
        (work / "logs" / name).write_text(f"yesterday's {name}\n")
    (work / ".gitattributes").write_text((ROOT / ".gitattributes").read_text())
    git("add", "-f", ".", cwd=work)
    git("commit", "-qm", "yesterday", cwd=work)
    git("push", "-q", "origin", "HEAD:main", cwd=work)
    # Another run pushes first, rewriting every rendered file.
    git("clone", "-q", str(tmp_path / "origin.git"), str(other))
    for name in rendered:
        (other / "logs" / name).write_text(f"the other run's {name}\n")
    with (other / "logs" / "signal_journal.log").open("a") as journal:
        journal.write("the other run's line\n")
    git("add", "-f", "logs", cwd=other)
    git("commit", "-qm", "the other run", cwd=other)
    git("push", "-q", "origin", "HEAD:main", cwd=other)
    # This run rewrote them too, from the older checkout.
    for name in rendered:
        (work / "logs" / name).write_text(f"this run's {name}\n")
    with (work / "logs" / "signal_journal.log").open("a") as journal:
        journal.write("this run's line\n")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "sleep").write_text("#!/bin/sh\nexit 0\n")
    (bin_dir / "sleep").chmod(0o755)
    script = _commit_step().replace("${{ inputs.mode == 'protect' && 'protection pass' || 'cycle' }}", "cycle")
    done = subprocess.run(["bash", "-e", "-c", script], cwd=work, capture_output=True, text=True,
                          env={**env, "PATH": f"{bin_dir}{os.pathsep}{env['PATH']}"}, timeout=60)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "did not go through" not in done.stdout + done.stderr, "the first try gets through"
    origin = ["--git-dir", str(tmp_path / "origin.git")]
    for name in rendered:
        assert git(*origin, "show", f"main:logs/{name}") == f"this run's {name}\n", name
    journal = git(*origin, "show", "main:logs/signal_journal.log")
    assert "the other run's line" in journal and "this run's line" in journal


@pytest.mark.parametrize("refuse, pushed", [(0, True), (1, True), (2, True), (3, False)])
def test_a_refused_push_is_tried_again_and_the_third_refusal_fails_the_step(tmp_path, refuse, pushed):
    code, log, origin = _run_the_commit(tmp_path, refuse=refuse)
    assert (code == 0) is pushed, log
    assert log.count("::warning::the journal push did not go through") == min(refuse, 2)
    remote = subprocess.run(["git", "--git-dir", str(origin), "show", "main:logs/signal_journal.log"],
                            capture_output=True, text=True, check=True).stdout
    assert ("today's line" in remote) is pushed


# --------------------------------------------------------------------------- #
# heartbeat-watchdog.yml
# --------------------------------------------------------------------------- #

def test_the_watchdog_checks_from_thirty_minutes_after_the_start():
    wf = _load(WATCHDOG)
    crons = [e["cron"] for e in wf[True]["schedule"]]
    assert crons == ["10 15 * * 1-5", "40 15 * * 1-5", "40 16 * * 1-5", "40 17 * * 1-5"]
    start = SCHEDULED_START_UTC.hour * 60 + SCHEDULED_START_UTC.minute
    assert _minutes(crons[0]) == start + 30
    # On time, every check is early enough to start a backup before the
    # latest safe start in summer (14:30 New York = 18:30 UTC), less the time
    # GitHub takes to bring a dispatched run to its guard, so each can still
    # rescue the day.
    lead = int(watchdog.DISPATCH_LEAD.total_seconds() // 60)
    for cron in crons:
        assert _minutes(cron) + lead < (LATEST_START_NY.hour + 4) * 60 + LATEST_START_NY.minute, cron
    assert "workflow_dispatch" in wf[True]
    assert not (wf[True]["workflow_dispatch"] or {}).get("inputs")


def test_the_watchdog_can_list_and_start_runs_and_nothing_else():
    wf = _load(WATCHDOG)
    assert wf["permissions"] == {"actions": "write", "contents": "read"}
    assert wf["concurrency"] == {"group": "heartbeat-watchdog", "cancel-in-progress": False}
    assert wf["jobs"]["watch"]["timeout-minutes"] == 10
    assert "permissions" not in wf["jobs"]["watch"], "a job-level block would override the workflow's"


def test_the_watchdog_asks_github_before_it_reads_the_journal():
    steps = _steps(WATCHDOG, "watch")
    kinds = [s.get("name") or s.get("uses") or s.get("run") for s in steps]
    listing = kinds.index("List today's heartbeat runs")
    checkout = next(i for i, s in enumerate(steps) if str(s.get("uses", "")).startswith("actions/checkout"))
    assert listing < checkout
    run = steps[listing]["run"]
    assert "gh api -X GET repos/${{ github.repository }}/actions/workflows/heartbeat.yml/runs" in run
    assert '-f created=">=$(date -u +%F)"' in run and "-f per_page=100" in run
    assert '"$RUNNER_TEMP/runs.json"' in run
    assert steps[listing]["env"] == {"GH_TOKEN": "${{ github.token }}"}
    setup = next(s for s in steps if str(s.get("uses", "")).startswith("actions/setup-python"))
    assert setup["uses"] == SETUP_PYTHON


def test_the_watchdog_reads_the_steps_of_every_run_that_finished():
    """A run that reached "Run one cycle" may have traded with its record lost,
    and heartbeat.yml's guard stops every later cycle after one, green or red.
    The watchdog must tell that from a run that never got that far, so it asks
    GitHub for the steps of every finished run -- in every attempt, since a
    run re-run from GitHub's page shows only its latest attempt otherwise."""
    steps = _named(WATCHDOG, "watch")
    listing = steps["List today's heartbeat runs"]["run"]
    assert "select(.status == \"completed\") | .id" in listing
    assert '.conclusion != "success"' not in listing
    assert ('gh api "repos/${{ github.repository }}/actions/runs/$id/jobs?filter=all&per_page=100"'
            ' > "$RUNNER_TEMP/jobs/$id.json"') in listing
    assert 'rm -f "$RUNNER_TEMP/jobs/$id.json"' in listing, "a failed read must not leave half a file"
    assert '--jobs "$RUNNER_TEMP/jobs"' in steps["Has today's run started?"]["run"]
    # gh has no time limit of its own; a stalled call would hold the job until
    # its 10 minutes ran out and it was cancelled, which reaches no phone.
    calls = [line for line in listing.splitlines() if "gh api" in line]
    assert len(calls) == 2 and all("timeout 30 gh api" in line for line in calls), calls


def test_the_trading_step_the_watchdog_and_the_guard_look_for_is_the_heartbeats():
    """A rename in heartbeat.yml would otherwise make every run look as if it
    never reached the trading step: the backup would run a traded day again,
    and so would every late cron and Routine that passed the guard. One name,
    one step, and it is the one that trades."""
    named = [s for s in _steps(HEARTBEAT, "cycle") if s.get("name") == watchdog.TRADING_STEP]
    assert watchdog.TRADING_STEP == "Run one cycle"
    assert len(named) == 1
    assert "python -m orchestrator.heartbeat --once" in named[0]["run"]
    # The guard reads it through the watchdog's helpers, not a copy of its own.
    source = (ROOT / "analysis/cycle_day.py").read_text()
    literals = {node.value for node in ast.walk(ast.parse(source)) if isinstance(node, ast.Constant)}
    assert watchdog.TRADING_STEP not in literals
    assert "from analysis.watchdog import todays_cycle_runs, trading_step_ran" in source


def _imports(path: Path) -> set[str]:
    """Every absolute module ``path`` imports, lazily imported ones included."""
    found = set()
    for node in ast.walk(ast.parse(path.read_text())):
        if isinstance(node, ast.Import):
            found |= {alias.name for alias in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            found.add(node.module)
    return found


def test_the_watchdog_needs_nothing_from_pypi():
    """No `pip install` in the watchdog: a PyPI outage or a pin that stops
    resolving would skip the decision, and with it the phone. That only
    holds while everything it imports, all the way down, is the standard
    library or this repository -- so the whole import graph is walked."""
    for step in _steps(WATCHDOG, "watch"):
        assert "pip install" not in str(step.get("run", "")), step.get("name")
        assert "cache" not in (step.get("with") or {}), step.get("uses")
    seen, todo = set(), ["analysis.watchdog"]
    while todo:
        module = todo.pop()
        if module in seen:
            continue
        seen.add(module)
        for name in _imports(ROOT / (module.replace(".", "/") + ".py")):
            top = name.split(".")[0]
            if top in ("analysis", "config", "orchestrator", "app", "rules"):
                assert (ROOT / (name.replace(".", "/") + ".py")).exists(), name
                todo.append(name)
            else:
                assert top in sys.stdlib_module_names or top == "__future__", f"{module} imports {name}"
    assert {"analysis.cycle_day", "analysis.reader", "config.market_calendar"} <= seen


def test_the_watchdog_decides_in_python_and_the_outputs_feed_the_rest():
    steps = _named(WATCHDOG, "watch")
    decide = steps["Has today's run started?"]
    assert decide["id"] == "decide"
    assert "python -m analysis.watchdog --runs \"$RUNNER_TEMP/runs.json\"" in decide["run"]
    assert "--journal logs/signal_journal.log" in decide["run"]
    assert '>> "$GITHUB_OUTPUT"' in decide["run"] and '>> "$GITHUB_STEP_SUMMARY"' in decide["run"]


def test_the_watchdog_starts_a_backup_cycle_and_never_a_rerun():
    step = _named(WATCHDOG, "watch")["Start the day's run as the backup"]
    assert step["if"] == "steps.decide.outputs.action == 'dispatch'"
    assert step["id"] == "dispatch"
    run = step["run"]
    assert 'gh workflow run heartbeat.yml --ref "$GITHUB_REF_NAME" -f mode=cycle -f started_by=backup' in run
    assert step["env"]["GH_TOKEN"] == "${{ github.token }}"
    # `rerun` is the one input that bypasses heartbeat.yml's guard. No step
    # here may pass it, in any spelling.
    for other in _steps(WATCHDOG, "watch"):
        assert "rerun" not in str(other.get("run", "")), other.get("name")
    assert not re.search(r"(-f|-F|--field|--raw-field)\s*rerun", WATCHDOG.read_text())


def test_the_watchdog_holds_the_phone_topic_and_no_other_secret():
    text = WATCHDOG.read_text()
    assert set(re.findall(r"secrets\.([A-Za-z_]+)", text)) == {"NTFY_TOPIC"}
    assert "GITHUB_TOKEN" not in text
    for banned in ("ALPACA", "ANTHROPIC", "API_KEY", "SUPABASE"):
        assert banned not in text, banned


def test_the_watchdog_never_prints_the_topic_and_posts_it_only_in_the_body():
    step = _named(WATCHDOG, "watch")["Tell the owner's phone"]
    _is_a_safe_push(step)
    # A watchdog that broke before it decided still reaches the phone, with
    # a message of its own rather than an empty one.
    assert step["if"] == "always() && (steps.decide.outputs.ping == 'yes' || failure())"
    assert step["env"]["PING"] == "${{ steps.decide.outputs.ping }}"
    assert 'if os.environ.get("PING") != "yes":' in step["run"]
    assert "The watchdog could not check today's run" in step["run"]
    run = step["run"]
    assert "https://ntfy.sh/" in run and "ntfy.sh/$" not in run
    for line in WATCHDOG.read_text().splitlines():
        if "echo" in line or "printf" in line:
            assert "$NTFY_TOPIC" not in line and "${NTFY_TOPIC" not in line, line
    # A refused dispatch still reaches the phone, and says so.
    assert step["env"]["DISPATCH"] == "${{ steps.dispatch.outcome }}"
    assert 'os.environ.get("DISPATCH") == "failure"' in run
