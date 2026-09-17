"""The record is read, and what it says went wrong is said out loud.

Each rule is tested from the day it was learned: a line that reproduces the
17 Sep 2026 record must raise the alarm, and the same line one day later, or
after the manager protected the position, must not.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest
import yaml

from analysis import health

DAY = date(2026, 9, 17)


def journal_line(ticker, when="2026-09-17T15:48:00+00:00", error=None, gaps=(), screen=None):
    return json.dumps({
        "ticker": ticker, "ts_utc": when,
        "context": {"ticker": ticker, "gaps": list(gaps)},
        "signal": None if error else {"ticker": ticker, "bias": "NEUTRAL", "conviction": 0.2},
        "outcome": None if error else {"status": "REJECTED", "reason": "bias is NEUTRAL; no trade"},
        "error": error, "screen": screen,
        "ts": "2026-09-17 15:48:00,000", "level": "INFO", "event": "signal_journal",
    })


def audit_line(ticker, action, reason="", when="2026-09-17 15:47:41,444"):
    return json.dumps({
        "action": {"ticker": ticker, "action": action, "reason": reason, "new_stop": 96.0},
        "ts": when, "level": "INFO", "event": "position_managed",
    })


@pytest.fixture
def logs(tmp_path):
    journal = tmp_path / "signal_journal.log"
    audit = tmp_path / "execution_audit.log"
    journal.write_text("")
    audit.write_text("")
    return journal, audit


def write(path: Path, *lines: str) -> None:
    path.write_text("\n".join(lines) + "\n")


def titles(alarms):
    return [a.title for a in alarms]


# --------------------------------------------------------------------------- #
# Clean days are clean
# --------------------------------------------------------------------------- #


def test_a_clean_day_raises_nothing_and_exits_zero(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"), journal_line("XOM"))
    write(audit, audit_line("XOM", "held"))
    alarms = health.check(journal, audit, DAY)
    assert alarms == []
    assert health.exit_code(alarms) == 0
    assert "Clean." in health.render(alarms, DAY)


# --------------------------------------------------------------------------- #
# 16 Sep: the schedule never fired
# --------------------------------------------------------------------------- #


def test_no_journal_line_today_is_critical(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL", when="2026-09-16T15:48:00+00:00"))
    alarms = health.check(journal, audit, DAY)
    assert titles(alarms) == ["No cycle ran today"]
    assert alarms[0].is_critical and health.exit_code(alarms) == 2


def test_a_missing_journal_file_is_no_cycle_not_a_crash(tmp_path):
    alarms = health.check(tmp_path / "nope.log", tmp_path / "nope2.log", DAY)
    assert titles(alarms) == ["No cycle ran today"]


# --------------------------------------------------------------------------- #
# 17 Sep: eleven positions with no stop
# --------------------------------------------------------------------------- #


def test_positions_the_manager_left_without_a_stop_are_critical(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit,
          audit_line("XLY", "unmanaged", "no live stop order; left untouched"),
          audit_line("TLT", "error", "BrokerError: refusing a stop for TLT"),
          audit_line("GOOGL", "held"))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.is_critical
    assert alarm.title == "2 position(s) without a working stop"
    assert "TLT, XLY" in alarm.detail and "no live stop order" in alarm.detail


def test_a_position_protected_later_in_the_day_is_no_longer_an_alarm(logs):
    """The last word counts: the protection pass ran after the cycle."""
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit,
          audit_line("XLY", "unmanaged", "no live stop order; left untouched", when="2026-09-17 15:47:41,444"),
          audit_line("XLY", "protected", "placed one at the last recorded level", when="2026-09-17 19:40:02,000"))
    assert health.check(journal, audit, DAY) == []


def test_yesterdays_naked_position_is_not_todays_alarm(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit, audit_line("XLY", "unmanaged", when="2026-09-16 15:47:41,444"))
    assert health.check(journal, audit, DAY) == []


def test_a_book_that_could_not_be_read_is_critical(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit, audit_line("*", "error", "BrokerError: get_all_positions failed"))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.is_critical and alarm.title == "The open book could not be read"


# --------------------------------------------------------------------------- #
# Tickers that produced no signal, and a screen that broke
# --------------------------------------------------------------------------- #


def test_one_failed_ticker_is_a_warning(logs):
    journal, audit = logs
    write(journal, *[journal_line(t) for t in "ABCDEFGHIJK"], journal_line("XOM", error="context: TimeoutError"))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.severity == health.WARNING
    assert alarm.title == "1 of 12 ticker(s) produced no signal"
    assert "TimeoutError" in alarm.detail
    assert health.exit_code([alarm]) == 1


def test_a_tenth_of_the_watchlist_failing_is_critical(logs):
    journal, audit = logs
    write(journal, *[journal_line(t) for t in "ABCDEFGHI"], journal_line("X", error="e"), journal_line("Y", error="e"))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.is_critical and alarm.title == "2 of 11 ticker(s) produced no signal"


def test_a_screen_error_is_a_warning_with_the_first_line_of_the_error(logs):
    journal, audit = logs
    error = "1 validation error for LLMSignal\nanalyst_score\n  Input should be less than or equal to 1"
    write(journal, journal_line("AAPL", screen={"model": "haiku", "error": error}), journal_line("XOM", screen={"model": "haiku"}))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.severity == health.WARNING
    assert alarm.title == "The screen failed on 1 ticker(s)"
    assert "validation error" in alarm.detail and "analyst_score" not in alarm.detail


# --------------------------------------------------------------------------- #
# A mapped contract that said nothing, and a day that ran twice
# --------------------------------------------------------------------------- #


def test_a_silent_cftc_contract_is_a_warning(logs):
    journal, audit = logs
    gap = "CFTC positioning unavailable: ULTRA UST BOND is not reporting"
    write(journal, journal_line("TLT", gaps=[gap]), journal_line("GLD", gaps=["news: nothing found"]))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.severity == health.WARNING
    assert alarm.title == "CFTC positioning is silent for 1 mapped contract(s)"
    assert "TLT" in alarm.detail and "GLD" not in alarm.detail


def test_the_gap_prefix_is_the_one_the_context_writer_uses():
    from orchestrator import context

    assert context._POSITIONING_GAP == health.CFTC_GAP_PREFIX


def test_a_ticker_judged_twice_is_a_warning(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"), journal_line("AAPL", when="2026-09-17T19:10:00+00:00"), journal_line("XOM"))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.severity == health.WARNING
    assert alarm.title == "1 ticker(s) were judged more than once today"
    assert "AAPL" in alarm.detail


# --------------------------------------------------------------------------- #
# Ordering, rendering, the CLI
# --------------------------------------------------------------------------- #


def test_critical_alarms_come_first_and_the_markdown_marks_them(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"), journal_line("AAPL"))
    write(audit, audit_line("XLY", "unmanaged"))
    alarms = health.check(journal, audit, DAY)
    assert [a.severity for a in alarms] == [health.CRITICAL, health.WARNING]
    text = health.render(alarms, DAY)
    assert text.startswith("## Health of the record for 2026-09-17")
    assert "**1 critical, 1 warning(s).**" in text
    assert "🔴 **1 position(s) without a working stop.**" in text
    assert "🟡 **1 ticker(s) were judged more than once today.**" in text


def test_the_cli_prints_markdown_and_exits_with_the_severity(logs, capsys):
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit, audit_line("XLY", "unmanaged"))
    code = health.main(["--journal", str(journal), "--audit", str(audit), "--day", "2026-09-17"])
    assert code == 2
    assert "without a working stop" in capsys.readouterr().out


def test_unreadable_lines_are_skipped_not_fatal(logs):
    journal, audit = logs
    journal.write_text("not json\n" + journal_line("AAPL") + "\n[1,2]\n")
    audit.write_text("{broken\n")
    assert health.check(journal, audit, DAY) == []


def test_health_never_imports_a_broker_or_a_model():
    source = Path(health.__file__).read_text()
    for banned in ("broker_client", "alpaca", "anthropic", "httpx", "requests", "ExecutionEngine", "submit_"):
        assert banned not in source, banned


# --------------------------------------------------------------------------- #
# The workflow runs it, after the commit, and never on a protect-only run
# --------------------------------------------------------------------------- #


def _heartbeat() -> dict:
    return yaml.safe_load((Path(__file__).resolve().parents[1] / ".github/workflows/heartbeat.yml").read_text())


def test_the_alarm_step_runs_after_the_commit_on_every_cycle_run():
    steps = _heartbeat()["jobs"]["cycle"]["steps"]
    names = [s.get("name") for s in steps]
    alarm = names.index("Sound the alarm on anything the record says went quietly wrong")
    assert alarm > names.index("Commit the journal")
    step = steps[alarm]
    assert step["if"] == "always() && steps.guard.outputs.ran != 'yes' && inputs.mode != 'protect'"
    run = step["run"]
    assert "python -m analysis.health --journal logs/signal_journal.log --audit logs/execution_audit.log" in run
    assert "GITHUB_STEP_SUMMARY" in run
    assert "--label health-alarm" in run and "--assignee \"$OWNER\"" in run
    assert 'if [ "$code" = "2" ]' in run and "exit 1" in run
    assert "gh issue close" in run  # a clean day closes the open alarm


def test_data_sources_runs_daily_before_the_cycle_and_a_dead_mapping_is_red():
    wf = yaml.safe_load((Path(__file__).resolve().parents[1] / ".github/workflows/data-sources.yml").read_text())
    [cron] = [e["cron"] for e in wf[True]["schedule"]]
    assert cron == "20 14 * * 1-5"
    hb = _heartbeat()
    first_cycle_cron = hb[True]["schedule"][0]["cron"]
    assert first_cycle_cron == "5 15 * * 1-5"  # the check lands before the cycle
    steps = wf["jobs"]["probe"]["steps"]
    cftc = next(s for s in steps if s.get("name") == "CFTC positioning answers")
    assert "continue-on-error" not in cftc
    assert "raise SystemExit(1 if broken else 0)" in cftc["run"]
    issue = next(s for s in steps if s.get("name") == "Open the issue that says a source died")
    assert issue["if"] == "failure()" and "--label data-sources" in issue["run"]
    assert wf["permissions"]["issues"] == "write"
