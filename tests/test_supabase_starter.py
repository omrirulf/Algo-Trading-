"""The Supabase starter: the day's main start, and everything that says what it did.

Since 26 Sep 2026 the owner's main starter for the daily run is a pg_cron job
in the Supabase project that asks GitHub to dispatch heartbeat.yml at 14:40
UTC (``supabase/heartbeat_starter.sql``). Every other starter -- GitHub's own
cron, the Claude Routines, a temporary Claude bridge, the watchdog -- is a
backup, and all of them go through the same guard. What is pinned here:

* the SQL holds no token and names the one Vault secret it reads;
* every run says which starter asked for it (``source``), validated, in the
  run block, the run's title, the race and the report -- and nothing about
  the source can change what the guard decides;
* a starter that fires on a market holiday, or after the latest safe start,
  trades nothing;
* the workflow reads the starter's log, commits it, records the archive push
  and pages the phone when the push fails, without ever failing the run for
  any of that.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import pytest
import yaml

from analysis import cycle_day, watchdog
from analysis.cycle_day import main as cycle_day_main
from analysis.cycle_day import run_block, source_for, start_decision, trigger_for
from analysis.reader import read_lines
from tests.test_phone import _is_a_safe_push

ROOT = Path(__file__).resolve().parents[1]
SQL = ROOT / "supabase" / "heartbeat_starter.sql"
HEARTBEAT = ROOT / ".github/workflows/heartbeat.yml"
WATCHDOG = ROOT / ".github/workflows/heartbeat-watchdog.yml"
VAULT_NAME = "github_heartbeat_dispatch"

UTC = timezone.utc
#: Thanksgiving 2026: a Thursday the NYSE is shut, and a weekday every
#: starter still fires on.
THANKSGIVING = date(2026, 11, 26)

#: Anything shaped like a credential: a GitHub token of any kind, a JWT (a
#: Supabase key is one), a Supabase secret or personal key, or a bearer
#: header with its value written out.
TOKEN_SHAPES = re.compile(
    r"gh[pousr]_[A-Za-z0-9]{8,}|github_pat_[A-Za-z0-9_]{8,}|eyJ[A-Za-z0-9_-]{10,}"
    # A real secret key is the prefix plus a long random part. The bare prefix
    # is allowed: the docs must name it ("sb_secret_…") so a person can tell
    # the new key from the legacy one.
    r"|sb_secret_[A-Za-z0-9_-]{8,}|sbp_[A-Za-z0-9]{8,}|Bearer\s+[A-Za-z0-9_.-]{12,}"
)


def _steps(path: Path, job: str) -> list[dict]:
    return yaml.safe_load(path.read_text())["jobs"][job]["steps"]


def _named(path: Path, job: str) -> dict:
    return {s.get("name"): s for s in _steps(path, job)}


# --------------------------------------------------------------------------- #
# The SQL: no token, one Vault secret, the owner's schedule
# --------------------------------------------------------------------------- #


def _sql() -> str:
    return SQL.read_text(encoding="utf-8")


def _code(sql: str) -> str:
    """The SQL without its comments."""
    return "\n".join(line.split("--", 1)[0] for line in sql.splitlines())


def test_the_sql_holds_nothing_that_looks_like_a_token():
    text = _sql()
    found = TOKEN_SHAPES.findall(text)
    assert found == [], found
    # The bearer header is built from the Vault value, never written out.
    assert "'Bearer ' || dispatch_token" in text
    for line in _code(text).splitlines():
        if "Bearer" in line:
            assert "'Bearer ' || dispatch_token" in line, line


def test_the_sql_reads_exactly_one_vault_secret_and_it_is_github_heartbeat_dispatch():
    text = _sql()
    code = _code(text)
    assert re.findall(r"where secret\.name = '([^']*)'", code) == [VAULT_NAME]
    assert code.count("vault.decrypted_secrets") == 1
    assert f"`{VAULT_NAME}`" not in text and f"    {VAULT_NAME}\n" in text   # named in the header, exactly
    # With no token in Vault it writes a row that says so, and asks nothing.
    assert "values ('supabase-cron', 'no token in vault');" in code
    missing = code.index("if dispatch_token is null")
    assert code.index("return null;", missing) < code.index("net.http_post", missing)


def test_the_token_never_reaches_the_log_table():
    code = _code(_sql())
    inserts = re.findall(r"insert into public\.starter_log[^;]*;", code, flags=re.S)
    assert len(inserts) == 2
    for insert in inserts:
        assert "dispatch_token" not in insert and "Bearer" not in insert
    # The answer is copied as a status code and pg_net's error text only.
    record = code[code.index("function public.record_starter_status"):]
    assert "response.status_code" in record and "response.error_msg" in record
    for banned in ("response.content", "response.headers", "content_type"):
        assert banned not in record, banned


def test_the_request_is_the_dispatch_the_owner_asked_for():
    code = _code(_sql())
    assert ("url := 'https://api.github.com/repos/omrirulf/Algo-Trading-/actions/workflows/"
            "heartbeat.yml/dispatches'") in code
    assert "'ref', 'main'" in code
    for pair in ("'mode', 'cycle'", "'started_by', 'scheduler'", "'source', 'supabase-cron'"):
        assert pair in code, pair
    assert "rerun" not in code, "the starter must never pass the one input that bypasses the guard"
    for header in ("'Accept', 'application/vnd.github+json'", "'X-GitHub-Api-Version', '2022-11-28'",
                   "'User-Agent', 'algo-trading-supabase-cron'", "'Content-Type', 'application/json'"):
        assert header in code, header
    assert "timeout_milliseconds := 10000" in code
    # The inputs it sends are inputs the workflow has.
    inputs = yaml.safe_load(HEARTBEAT.read_text())[True]["workflow_dispatch"]["inputs"]
    assert "scheduler" in inputs["started_by"]["options"] and "source" in inputs
    assert cycle_day.SOURCE_PATTERN.fullmatch("supabase-cron")
    assert "204" in _sql(), "the comments say what a good answer looks like"


def test_the_functions_are_locked_down():
    code = _code(_sql())
    for name in ("start_heartbeat", "record_starter_status"):
        body = code[code.index(f"function public.{name}()"):]
        body = body[:body.index("$$;")]
        assert "security definer" in body and "set search_path = ''" in body, name
        assert (f"revoke execute on function public.{name}() from public, anon, authenticated;"
                in code), name
    assert "alter table public.starter_log enable row level security;" in code
    assert "create policy" not in code.lower(), "service role only: no policy at all"
    flat = " ".join(code.split())
    for column in ("id bigint generated always as identity primary key", "requested_at timestamptz",
                   "source text", "request_id bigint", "status_code int", "error text"):
        assert column in flat, column


def test_the_schedule_is_idempotent_and_on_the_owners_minutes():
    code = _code(_sql())
    assert "create extension if not exists pg_cron;" in code
    assert "create extension if not exists pg_net with schema extensions;" in code
    unschedule = code.index("cron.unschedule(jobid)")
    assert "where jobname in ('heartbeat-start', 'heartbeat-start-status')" in code[unschedule:]
    start = code.index("cron.schedule('heartbeat-start', '40 14 * * 1-5', 'select public.start_heartbeat()')")
    status = code.index("cron.schedule('heartbeat-start-status', '43 14 * * 1-5', "
                        "'select public.record_starter_status()')")
    assert unschedule < start < status
    # The same minute the workflow's own cron and the run block call "due".
    minute, hour = "40 14 * * 1-5".split()[:2]
    assert (int(hour), int(minute)) == (cycle_day.SCHEDULED_START_UTC.hour, cycle_day.SCHEDULED_START_UTC.minute)


def test_the_settings_keep_the_expiry_date_and_never_the_token():
    from config import settings

    assert hasattr(settings, "GITHUB_DISPATCH_TOKEN_EXPIRES")
    assert settings.GITHUB_DISPATCH_TOKEN_EXPIRES is None or isinstance(settings.GITHUB_DISPATCH_TOKEN_EXPIRES, date)
    assert settings.GITHUB_DISPATCH_TOKEN_WARN_DAYS == 14
    text = (ROOT / "config/settings.py").read_text()
    assert f"``{VAULT_NAME}``" in text and "never in this repository" in text
    for path in (ROOT / "config/settings.py", HEARTBEAT, WATCHDOG, ROOT / "store/starter_status.py"):
        assert TOKEN_SHAPES.findall(path.read_text()) == [], path


# --------------------------------------------------------------------------- #
# Which starter asked: validated once, carried everywhere
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("given, kept", [
    ("supabase-cron", "supabase-cron"), ("claude-bridge", "claude-bridge"), ("watchdog", "watchdog"),
    (" claude-routine ", "claude-routine"), ("", "manual"), (None, "manual"), ("manual", "manual"),
    ("Supabase-Cron", "unknown"), ("supabase cron", "unknown"), ("x" * 41, "unknown"), ("x" * 40, "x" * 40),
    ("a;rm -rf /", "unknown"), ("<b>hi</b>", "unknown"), ("ghp_" + "a" * 36, "unknown"),
    ("supabase-cron\nprotect", "unknown"), ("été", "unknown"),
])
def test_a_source_is_a_short_safe_token_or_it_is_unknown(given, kept):
    assert source_for("workflow_dispatch", given) == kept


def test_a_scheduled_run_is_github_schedule_whatever_it_says():
    assert source_for("schedule", "") == "github-schedule"
    assert source_for("schedule", "supabase-cron") == "github-schedule"


def test_the_scheduler_is_its_own_trigger():
    assert trigger_for("workflow_dispatch", "scheduler") == "scheduler"
    assert trigger_for("workflow_dispatch", " Scheduler ") == "scheduler"
    assert trigger_for("schedule", "scheduler") == "schedule"


def test_the_run_block_carries_the_source(capsys):
    block = run_block(event="workflow_dispatch", started_by="scheduler", run_id=5, source="supabase-cron",
                      started_at=datetime(2026, 9, 28, 14, 41, 3, tzinfo=UTC))
    assert (block["trigger"], block["source"], block["minutes_late"], block["late"]) == (
        "scheduler", "supabase-cron", 1, False)
    assert cycle_day_main(["--run-block", "--event", "workflow_dispatch", "--started-by", "manual",
                           "--source", "<script>", "--run-id", "9", "--now", "2026-09-28T14:42:00Z"]) == 0
    printed = json.loads(capsys.readouterr().out)
    assert printed["source"] == "unknown"


def test_the_journal_refuses_a_source_that_is_not_a_token(monkeypatch):
    """The last door before a public, committed file checks it again."""
    from orchestrator import journal

    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps({"trigger": "manual", "source": "free text here"}))
    assert journal.run_block() == {"trigger": "manual", "source": "unknown"}
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps({"trigger": "manual", "source": 7}))
    assert journal.run_block()["source"] == "unknown"
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps({"trigger": "scheduler", "source": "supabase-cron"}))
    assert journal.run_block() == {"trigger": "scheduler", "source": "supabase-cron"}
    monkeypatch.setenv("HEARTBEAT_RUN", json.dumps({"trigger": "schedule"}))
    assert journal.run_block() == {"trigger": "schedule"}, "a block without a source gains none"


def test_the_race_and_the_report_say_the_source_and_never_echo_junk():
    from analysis import cycle_report as cr
    from analysis.run_timing import day_timings, parse_run_block, render

    good = {"trigger": "scheduler", "source": "supabase-cron", "scheduled_for": "2026-09-28T14:40:00+00:00",
            "started_at": "2026-09-28T14:41:00+00:00", "minutes_late": 1, "late": False, "run_id": "1"}
    assert parse_run_block(good).source == "supabase-cron" and parse_run_block(good).trigger == "scheduler"
    assert parse_run_block(dict(good, source="<b>")).source == "unknown"
    assert parse_run_block({k: v for k, v in good.items() if k != "source"}).source is None
    line = json.dumps({"ticker": "NVDA", "ts_utc": "2026-09-28T14:50:00+00:00", "run": good,
                       "signal": {"bias": "NEUTRAL", "conviction": 0.1}})
    (timing,) = day_timings(read_lines([line]).entries)
    assert timing.run_source == "supabase-cron"
    row = [r for r in render([timing]) if r.startswith("2026-09-28")][0]
    assert row.endswith("scheduler run block via supabase-cron")
    said = cr.run_line([cr.Line(json.loads(line))])
    assert said == ("**Run:** started by the outside scheduler (via supabase-cron), 1 minutes after "
                    "the planned 14:40 UTC.")
    junk = cr.run_line([cr.Line({**json.loads(line), "run": dict(good, source="<img src=x>")})])
    assert "<img" not in junk and "an unknown source" in junk


def test_the_starter_is_never_counted_as_the_watchdogs_backup():
    """The watchdog stops after two backups of its own. A run the Supabase
    starter (or a Routine, or a person) started is not one of them, and no
    source, however it is spelled, can make a cycle look like a protection
    pass -- which the guard would not count."""
    def run(title):
        return {"id": 1, "display_title": title, "status": "completed", "conclusion": "success",
                "created_at": "2026-09-28T14:41:00Z"}

    assert not watchdog.is_backup_run(run("heartbeat cycle (scheduler) via supabase-cron"))
    assert not watchdog.is_backup_run(run("heartbeat cycle (manual) via claude-bridge"))
    assert not watchdog.is_backup_run(run("heartbeat cycle (manual) via x (backup)"))
    assert watchdog.is_backup_run(run("heartbeat cycle (backup) via watchdog"))
    assert watchdog.is_backup_run(run("heartbeat cycle (backup)"))
    assert watchdog.is_cycle_run(run("heartbeat cycle (manual) via protect-test"))
    assert watchdog.is_cycle_run(run("heartbeat cycle (scheduler) via supabase-cron"))
    assert not watchdog.is_cycle_run(run("heartbeat protect"))
    now = datetime(2026, 9, 28, 16, 0, tzinfo=UTC)
    three = [run("heartbeat cycle (scheduler) via supabase-cron"), run("heartbeat cycle (manual) via claude-bridge"),
             run("heartbeat cycle (backup) via watchdog")]
    assert len(watchdog.todays_cycle_runs(three, now)) == 3


# --------------------------------------------------------------------------- #
# The guard decides the same way whoever asked -- a holiday and a late start
# --------------------------------------------------------------------------- #


def _supabase_block(started: datetime) -> str:
    return json.dumps(run_block(event="workflow_dispatch", started_by="scheduler", run_id="77",
                                source="supabase-cron", started_at=started))


def test_the_guard_never_reads_the_source():
    """The source is a label. The guard step is given nothing that could carry
    it, so no starter can talk its way past the guard or be stopped by it."""
    guard = next(s for s in _steps(HEARTBEAT, "cycle") if s.get("id") == "guard")
    assert "source" not in str(guard.get("env")) and "source" not in guard["run"]
    assert "started_by" not in str(guard.get("env")) and "started_by" not in guard["if"]


def test_a_supabase_start_after_the_latest_safe_start_is_too_late(tmp_path, capsys):
    """The starter fires at 14:40 UTC; if its run only reaches the guard after
    14:30 New York (18:30 UTC in summer), it trades nothing."""
    journal = tmp_path / "signal_journal.log"
    journal.write_text("")
    assert cycle_day_main(["--journal", str(journal), "--decide", "--now", "2026-09-28T18:31:00Z"]) == 0
    assert capsys.readouterr().out.strip() == "too_late"
    assert start_decision([], datetime(2026, 9, 28, 14, 40, tzinfo=UTC)) == "run"
    assert start_decision([], datetime(2026, 12, 2, 19, 30, tzinfo=UTC)) == "too_late"   # winter: 14:30 EST


def test_a_supabase_start_on_a_market_holiday_trades_nothing_and_writes_nothing(tmp_path, monkeypatch):
    """Thanksgiving: the starter fires anyway (pg_cron knows no holidays), the
    guard says run (the calendar is the cycle's business, not the guard's),
    and the cycle stands down before it asks the broker, the model or anyone
    else: no journal line, no order, exit 0."""
    from config import settings as cfg
    from orchestrator import heartbeat as hb
    from orchestrator import journal

    assert start_decision([], datetime(2026, 11, 26, 14, 40, tzinfo=UTC)) == "run"

    class _MustNotBeAsked:
        def __getattr__(self, name):
            raise AssertionError(f"the dispatcher's {name} was used on a market holiday")

    monkeypatch.setattr(hb, "today_et", lambda: THANKSGIVING)
    monkeypatch.setattr(hb, "build_dispatcher", lambda *a, **k: _MustNotBeAsked())
    monkeypatch.setattr(hb.cfg, "USE_BATCH_API", True)
    monkeypatch.delenv("GITHUB_STEP_SUMMARY", raising=False)
    monkeypatch.setenv("HEARTBEAT_RUN", _supabase_block(datetime(2026, 11, 26, 14, 41, tzinfo=UTC)))
    assert hb.main(["--once"]) is None             # returns: exit 0, no SystemExit
    path = journal.cfg.SIGNAL_JOURNAL_PATH
    assert not path.exists() or path.read_text().strip() == ""
    assert cfg.USE_BATCH_API is True


def test_the_holiday_leaves_no_false_alarm(tmp_path):
    """No journal line on a holiday is the cycle working, not a lost day."""
    from analysis import health

    journal, audit = tmp_path / "signal_journal.log", tmp_path / "execution_audit.log"
    journal.write_text("")
    audit.write_text("")
    assert health.check(journal, audit, THANKSGIVING, token_expires=None) == []
    assert [a.title for a in health.check(journal, audit, date(2026, 11, 25), token_expires=None)] == [
        "No cycle ran today"]


# --------------------------------------------------------------------------- #
# The workflow: read the log, commit it, record the push, page on failure
# --------------------------------------------------------------------------- #


def test_the_starters_log_is_read_before_the_book_and_never_fails_the_run():
    steps = _steps(HEARTBEAT, "cycle")
    names = [s.get("name") for s in steps]
    step = _named(HEARTBEAT, "cycle")["Read the Supabase starter's log"]
    assert names.index("Read the Supabase starter's log") + 1 == names.index("Write the book snapshot")
    assert step["if"] == "always() && steps.guard.outputs.skip != 'yes' && inputs.mode != 'protect'"
    assert step["continue-on-error"] is True and step["timeout-minutes"] <= 3
    assert step["env"] == {"SUPABASE_URL": "${{ secrets.SUPABASE_URL }}",
                           "SUPABASE_SERVICE_KEY": "${{ secrets.SUPABASE_SERVICE_KEY }}"}
    run = step["run"]
    assert 'python store/starter_status.py > "$RUNNER_TEMP/starter_status.json"' in run
    assert "mv \"$RUNNER_TEMP/starter_status.json\" logs/starter_status.json" in run
    assert '"status": "unknown"' in run, "a script that cannot run still leaves a record"
    for line in run.splitlines():
        assert "SUPABASE_SERVICE_KEY" not in line and "SUPABASE_URL" not in line, line
    assert "curl" not in run, "read through the one reader of the key, not by hand"


def test_the_journal_commit_carries_the_starters_record_on_its_own_line():
    run = _named(HEARTBEAT, "cycle")["Commit the journal"]["run"]
    assert "git add -f logs/starter_status.json 2>/dev/null || true" in run
    main_add = next(line for line in run.splitlines() if line.strip().startswith("git add -f logs/journal "))
    assert "starter_status" not in main_add, "one missing path would make that add add nothing"
    assert "logs/starter_status.json" in run[run.index("sync_with_branch()"):]


def test_the_journal_commit_adds_the_starters_record_when_there_is_one(tmp_path):
    if not shutil.which("git"):
        pytest.skip("needs git")
    env = {**os.environ, "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
           "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@t", "GITHUB_REF_NAME": "main"}

    def git(*args, cwd=tmp_path):
        return subprocess.run(["git", *args], cwd=cwd, env=env, check=True, capture_output=True, text=True).stdout

    git("init", "-q", "--bare", "-b", "main", "origin.git")
    work = tmp_path / "work"
    git("clone", "-q", str(tmp_path / "origin.git"), str(work))
    (work / "logs" / "journal").mkdir(parents=True)
    for name in ("journal/2026-09.log", "execution_audit.log", "cycle_report.md", "fund_size.log",
                 "blend_weights.json", "score_report.md", "book.json", "brief.txt", "account.jsonl"):
        (work / "logs" / name).write_text("yesterday\n")
    git("add", "-f", ".", cwd=work)
    git("commit", "-qm", "yesterday", cwd=work)
    git("push", "-q", "origin", "HEAD:main", cwd=work)
    (work / "logs" / "journal" / "2026-09.log").write_text("yesterday\ntoday\n")
    (work / "logs" / "starter_status.json").write_text('{"day": "2026-09-28", "status_code": 204}\n')
    script = _named(HEARTBEAT, "cycle")["Commit the journal"]["run"].replace(
        "${{ inputs.mode == 'protect' && 'protection pass' || 'cycle' }}", "cycle")
    done = subprocess.run(["bash", "-e", "-c", script], cwd=work, env=env, capture_output=True, text=True,
                          timeout=60)
    assert done.returncode == 0, done.stdout + done.stderr
    origin = ["--git-dir", str(tmp_path / "origin.git")]
    assert "today" in git(*origin, "show", "main:logs/journal/2026-09.log")
    assert "204" in git(*origin, "show", "main:logs/starter_status.json")


def test_the_archive_push_records_how_it_went_and_still_fails_loudly():
    step = _named(HEARTBEAT, "cycle")["Push the archive to Supabase"]
    assert step["id"] == "archive"
    assert step["run"].strip() == "python store/push_remote.py --status logs/archive_status.json"
    assert "continue-on-error" not in step, "a failed push still turns the run red, as before"


def test_a_failed_archive_push_reaches_the_phone_the_same_day():
    steps = _steps(HEARTBEAT, "cycle")
    names = [s.get("name") for s in steps]
    step = _named(HEARTBEAT, "cycle")["Tell the owner's phone the archive push failed"]
    _is_a_safe_push(step)
    assert names.index("Push the archive to Supabase") < names.index("Tell the owner's phone the archive push failed")
    assert step["if"].startswith("always() && ")
    assert step["env"]["PUSH_OUTCOME"] == "${{ steps.archive.outcome }}"
    run = step["run"]
    assert '"priority": 4' in run and "Archive push to Supabase failed" in run
    assert 'error != "not configured"' in run, "not configured is the brief's daily warning, not a page"
    assert "may be paused; restore it" in run
    assert 'pathlib.Path("logs/archive_status.json")' in run
    assert "SUPABASE" not in str(step["env"]), "the phone step holds no Supabase secret"


def _phone_payload(tmp_path: Path, status, outcome: str = "failure") -> dict | None:
    """The alert step's Python, run against a record, with the post itself left out."""
    run = _named(HEARTBEAT, "cycle")["Tell the owner's phone the archive push failed"]["run"]
    start = run.index("\n", run.index("<<'EOF'")) + 1
    code = run[start:run.index("\nEOF", start)]
    import textwrap

    (tmp_path / "logs").mkdir(parents=True, exist_ok=True)
    if status is not None:
        (tmp_path / "logs" / "archive_status.json").write_text(json.dumps(status))
    done = subprocess.run([sys.executable, "-c", textwrap.dedent(code)], cwd=tmp_path, capture_output=True, text=True,
                          env={**os.environ, "NTFY_TOPIC": "topic-under-test", "PUSH_OUTCOME": outcome,
                               "RUN_URL": "https://example.invalid/run"}, timeout=60)
    assert done.returncode == 0, done.stderr
    return json.loads(done.stdout) if done.stdout.strip() else None


def test_what_the_archive_alert_says(tmp_path):
    now = datetime.now(UTC).isoformat(timespec="seconds")
    paused = _phone_payload(tmp_path / "a", {"last_attempt": now, "last_success": "2026-09-20T15:00:00+00:00",
                                             "ok": False, "error": "project paused or unreachable"})
    assert paused["title"] == "⚠️ Archive push to Supabase failed" and paused["priority"] == 4
    assert "the Supabase project may be paused; restore it" in paused["message"].replace("The Supabase", "the Supabase")
    assert "2026-09-20" in paused["message"]
    assert _phone_payload(tmp_path / "b", {"last_attempt": now, "ok": False, "error": "not configured"}) is None
    assert _phone_payload(tmp_path / "c", {"last_attempt": now, "ok": True, "error": None}, "success") is None
    http = _phone_payload(tmp_path / "d", {"last_attempt": now, "ok": False, "error": "HTTP 401"})
    assert "HTTP 401" in http["message"] and "SUPABASE_SERVICE_KEY" in http["message"]
    odd = _phone_payload(tmp_path / "e", {"last_attempt": now, "ok": False, "error": "key=abc123 leaked"})
    assert "abc123" not in odd["message"] and "an unrecognised error" in odd["message"]
    stale = _phone_payload(tmp_path / "f", {"last_attempt": "2026-09-01T15:00:00+00:00", "ok": True})
    assert "failed before it could say why" in stale["message"]


def test_the_archive_record_gets_its_own_commit_that_never_fails_the_run():
    steps = _steps(HEARTBEAT, "cycle")
    names = [s.get("name") for s in steps]
    step = _named(HEARTBEAT, "cycle")["Commit the archive push record"]
    assert names.index("Push the archive to Supabase") < names.index("Commit the archive push record")
    assert step["if"].startswith("always() && ") and step["continue-on-error"] is True
    run = step["run"]
    assert "git add -f logs/archive_status.json" in run
    assert "git pull --rebase --autostash" in run and "for attempt in 1 2 3; do" in run
    assert "git checkout --theirs -- logs/archive_status.json" in run
    lines = [line.strip() for line in run.strip().splitlines()]
    assert lines[-1] == "exit 0" and "exit 1" not in run


def test_the_watchdog_names_itself_as_the_source():
    run = _named(WATCHDOG, "watch")["Start the day's run as the backup"]["run"]
    assert "-f started_by=backup -f source=watchdog" in run
    assert "rerun" not in run


# --------------------------------------------------------------------------- #
# The documents say what the code does
# --------------------------------------------------------------------------- #


def test_the_d_amendment_says_closing_equity_only_and_mid_day_warns():
    text = (ROOT / "docs/horse-race-preregistration.md").read_text()
    row = next(line for line in text.splitlines()
               if line.startswith("| 2026-09-26 | **Trigger (b) retired, drawdown trigger (d) added**"))
    assert "**(d) trips only on closing equity**" in row
    assert "marked mid-day" in row and "does not trip (d)" in row and "no (d) alarm" in row
    assert "an intraday number when recorded before the close, marked so" not in row
    race = (ROOT / "docs/horse-race.mdx").read_text()
    assert "(d) trips only on\n  closing equity" in race and "marked mid-day" in race


def test_the_deployment_doc_explains_the_supabase_starter():
    text = (ROOT / "docs/deployment.mdx").read_text()
    section = text[text.index("## The Supabase starter"):]
    section = section[:section.index("\n## ", 1)]
    for needed in (VAULT_NAME, "supabase/heartbeat_starter.sql", "public.starter_log", "204",
                   "GITHUB_DISPATCH_TOKEN_EXPIRES", "claude-bridge", "14:40", "SUPABASE_SERVICE_KEY",
                   "logs/archive_status.json", "logs/starter_status.json"):
        assert needed in section, needed
    assert TOKEN_SHAPES.findall(text) == []
