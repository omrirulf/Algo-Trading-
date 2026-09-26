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


def audit_line(ticker, action, reason="", when="2026-09-17 15:47:41,444",
               stop_qty=None, remaining_qty=0):
    return json.dumps({
        "action": {"ticker": ticker, "action": action, "reason": reason, "new_stop": 96.0,
                   "stop_qty": stop_qty, "remaining_qty": remaining_qty},
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
# 22 Sep: a stop that was live, and sized for shares that were not held
# --------------------------------------------------------------------------- #


def test_a_stop_sized_for_shares_that_are_not_held_is_critical(logs):
    """TEVA: 1 share behind a 127-share stop, for six days, reported healthy.

    Every check asked whether a stop existed. None asked whether it could
    execute, and a sell order for 127 shares against 1 share held cannot.
    """
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit, audit_line("TEVA", "held", stop_qty=127, remaining_qty=1))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.is_critical
    assert alarm.title == "1 stop(s) sized for shares that are not held"
    assert "TEVA: stop covers 127 against 1 held" in alarm.detail


def test_a_stop_that_matches_the_position_raises_nothing(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit, audit_line("TEVA", "held", stop_qty=1, remaining_qty=1))
    assert health.check(journal, audit, DAY) == []


def test_a_stop_resized_later_in_the_day_is_no_longer_an_alarm(logs):
    """The last word counts, same as the naked-position rule."""
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit,
          audit_line("TEVA", "held", stop_qty=127, remaining_qty=1,
                     when="2026-09-17 15:47:41,444"),
          audit_line("TEVA", "stop_resized", stop_qty=1, remaining_qty=1,
                     when="2026-09-17 19:40:02,000"))
    assert health.check(journal, audit, DAY) == []


def test_an_action_that_read_no_stop_cannot_look_like_a_mismatch(logs):
    """``stop_qty`` is absent, not zero, when nothing was read or placed."""
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit, audit_line("TEVA", "error", "MarketDataError: no price", remaining_qty=0))
    assert titles(health.check(journal, audit, DAY)) == [
        "1 position(s) without a working stop"
    ]


def test_a_cancelled_stop_whose_replacement_failed_is_counted_as_naked(logs):
    journal, audit = logs
    write(journal, journal_line("AAPL"))
    write(audit, audit_line("TEVA", "no_stop", "UnprotectedPositionError: TEVA has NO live stop"))
    [alarm] = health.check(journal, audit, DAY)
    assert alarm.is_critical and alarm.title == "1 position(s) without a working stop"
    assert "NO live stop" in alarm.detail


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


UNAUTHORISED = ('https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 401: '
                '{"error":{"message":"User is not authorized"}}')
TIMEOUT = "https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out"


def test_more_than_a_fifth_of_the_runs_calls_failing_pings_the_phone(logs):
    """The owner's rule of 24 Sep 2026: above 20% of one run's calls failed,
    of either kind, is a critical alarm, which the brief pushes as urgent."""
    journal, audit = logs
    write(journal, *[journal_line(t) for t in "ABCDEFG"], journal_line("X", error=UNAUTHORISED),
          journal_line("Y", error=UNAUTHORISED), journal_line("Z", error=TIMEOUT))
    alarms = health.check(journal, audit, DAY)
    assert alarms[0].is_critical and alarms[0].title == "3 of 10 model calls failed today (2 setup, 1 model)"
    assert "HTTP 401" in alarms[0].detail


def test_exactly_a_fifth_failing_or_a_news_outage_is_not_the_call_alarm(logs):
    journal, audit = logs
    write(journal, *[journal_line(t) for t in "ABCDEFGH"], journal_line("X", error=TIMEOUT),
          journal_line("Y", error=TIMEOUT))                                # 2 of 10: not above 20%
    assert not [a for a in health.check(journal, audit, DAY) if "model calls failed" in a.title]
    context = json.loads(journal_line("W", error="Bright Data unreachable"))
    context["stage"] = "context"                                           # never put to the model
    write(journal, *[journal_line(t) for t in "ABCD"], json.dumps(context), json.dumps(context))
    assert not [a for a in health.check(journal, audit, DAY) if "model calls failed" in a.title]


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
    assert step["if"] == "always() && steps.guard.outputs.skip != 'yes' && inputs.mode != 'protect'"
    run = step["run"]
    assert "python -m analysis.health --journal logs/journal --audit logs/execution_audit.log" in run
    assert "GITHUB_STEP_SUMMARY" in run
    assert "--label health-alarm" in run and "--assignee \"$OWNER\"" in run
    assert 'if [ "$code" = "2" ]' in run and "exit 1" in run
    assert "gh issue close" in run  # a clean day closes the open alarm


def test_data_sources_runs_daily_before_the_cycle_and_a_dead_mapping_is_red():
    wf = yaml.safe_load((Path(__file__).resolve().parents[1] / ".github/workflows/data-sources.yml").read_text())
    [cron] = [e["cron"] for e in wf[True]["schedule"]]
    assert cron == "50 11 * * 1-5"
    hb = _heartbeat()
    first_cycle_cron = hb[True]["schedule"][0]["cron"]
    assert first_cycle_cron == "40 14 * * 1-5"

    # The property, rather than the two literals above: the probe has to land
    # before the cycle, or a dead source is reported after the model was
    # already fed blanks from it. Both moved back together when the cycle
    # started running pre-market to wait on its batch; the cycle moved after
    # the open again on 25 Sep, and the probe simply stays ahead of it.
    def _minutes(expression: str) -> int:
        minute, hour = expression.split()[:2]
        return int(hour) * 60 + int(minute)

    assert _minutes(cron) < _minutes(first_cycle_cron)
    steps = wf["jobs"]["probe"]["steps"]
    cftc = next(s for s in steps if s.get("name") == "CFTC positioning answers")
    assert "continue-on-error" not in cftc
    assert "raise SystemExit(1 if broken else 0)" in cftc["run"]
    issue = next(s for s in steps if s.get("name") == "Open the issue that says a source died")
    assert issue["if"] == "failure()" and "--label data-sources" in issue["run"]
    assert wf["permissions"]["issues"] == "write"


# --------------------------------------------------------------------------- #
# Two runs landing at once must not lose either one's record
# --------------------------------------------------------------------------- #


def test_the_append_only_logs_merge_as_a_union():
    """17 Sep 2026: a rebase conflict on the end of the audit log lost eleven stop records."""
    attributes = (Path(__file__).resolve().parents[1] / ".gitattributes").read_text()
    for log in ("logs/journal/*.log", "logs/execution_audit.log", "logs/fund_size.log"):
        assert f"{log} merge=union" in attributes, log


def test_the_commit_step_finishes_the_rebase_when_the_rendered_files_conflict():
    steps = _heartbeat()["jobs"]["cycle"]["steps"]
    run = next(s for s in steps if s.get("name") == "Commit the journal")["run"]
    assert 'if ! git pull --rebase --autostash origin "${GITHUB_REF_NAME}"; then' in run
    assert "git checkout --theirs -- logs/cycle_report.md logs/score_report.md logs/blend_weights.json" in run
    assert "GIT_EDITOR=true git rebase --continue" in run
    assert run.rstrip().endswith('git push origin "HEAD:${GITHUB_REF_NAME}"')


# --------------------------------------------------------------------------- #
# News that could not be fetched, now that it no longer stops the ticker (#69)
# --------------------------------------------------------------------------- #

NEWS_GAP = f"{health.NEWS_GAP_PREFIX}: Bright Data returned an empty body with its 200"


def test_the_gap_prefix_is_the_same_string_both_sides_write():
    """A contract split across two modules is a contract that drifts."""
    from orchestrator import context

    assert health.NEWS_GAP_PREFIX == context.NEWS_GAP_PREFIX


def test_one_ticker_judged_without_news_is_a_warning():
    """TM on 18 Sep: a flake, and the other four dimensions carried the day."""
    today = [json.loads(journal_line("TM", gaps=[NEWS_GAP]))]
    today += [json.loads(journal_line(f"T{i}")) for i in range(19)]
    alarm = health.news_gaps(today)
    assert alarm is not None and alarm.severity == health.WARNING
    assert "TM" in alarm.detail
    assert "still produced signals" in alarm.detail


def test_a_tenth_of_the_watchlist_without_news_is_the_vendor_being_down():
    """The reason this alarm exists: the failure is now silent without it."""
    today = [json.loads(journal_line(f"T{i}", gaps=[NEWS_GAP])) for i in range(5)]
    today += [json.loads(journal_line(f"U{i}")) for i in range(15)]
    alarm = health.news_gaps(today)
    assert alarm is not None and alarm.severity == health.CRITICAL


def test_a_day_whose_news_all_arrived_raises_nothing():
    today = [json.loads(journal_line(f"T{i}")) for i in range(20)]
    assert health.news_gaps(today) is None


def test_an_unrelated_gap_is_not_mistaken_for_a_news_outage():
    today = [json.loads(journal_line("USO", gaps=["CFTC positioning unavailable: no rows"]))]
    assert health.news_gaps(today) is None


def test_the_alarm_reaches_the_report(tmp_path):
    """Wired into check(), not merely defined beside it."""
    journal = tmp_path / "journal.log"
    audit = tmp_path / "audit.log"
    journal.write_text(
        "\n".join([journal_line("TM", gaps=[NEWS_GAP])]
                  + [journal_line(f"T{i}") for i in range(19)]),
        encoding="utf-8",
    )
    audit.write_text("", encoding="utf-8")
    alarms = health.check(journal, audit, date(2026, 9, 17))
    assert any("without news" in a.title for a in alarms)


# --------------------------------------------------------------------------- #
# Trigger (d): the owner's drawdown trigger on the paper account (26 Sep 2026)
# --------------------------------------------------------------------------- #


def race_record(tripped=True, trips=None):
    trips = trips if trips is not None else [
        {"day": "2026-10-08", "detail": "equity 91,500.00 is 8.50% below its peak 100,000.00 of 2026-09-24 "
                                        "(more than 8%)",
         "below_peak": True, "behind_vt": False, "drawdown": -0.085, "gap": -0.031},
    ]
    return {"generated_at": "2026-10-08T22:56:00+00:00", "status_line": "…",
            "watch": {"d": {"start": "2026-09-23", "tripped": tripped, "trips": trips if tripped else []}}}


def _day_with_a_record(logs, race):
    journal, audit = logs
    write(journal, journal_line("AAPL", when="2026-10-08T15:00:00+00:00"))
    if race is not None:
        (journal.parent / health.RACE_GATE_FILE).write_text(race if isinstance(race, str) else json.dumps(race))
    return journal, audit


def test_a_tripped_trigger_d_is_a_warning_with_a_clear_headline(logs):
    journal, audit = _day_with_a_record(logs, race_record())
    alarms = health.check(journal, audit, date(2026, 10, 8))
    [alarm] = alarms
    assert alarm.severity == health.WARNING and not alarm.is_critical
    assert alarm.title == "Trigger (d) tripped: the paper account is 8.5% below its peak on 2026-10-08"
    assert "8.50% below its peak 100,000.00" in alarm.detail
    assert "Stop and tell the owner; nothing reverts or trades" in alarm.detail
    assert health.exit_code(alarms) == 1
    assert "Trigger (d) tripped" in health.render(alarms, date(2026, 10, 8))


def test_trigger_d_names_both_reasons_when_both_tripped():
    both = race_record(trips=[{"day": "2026-10-08", "detail": "x; y", "below_peak": True, "behind_vt": True,
                               "drawdown": -0.09, "gap": -0.062}])
    alarm = health.drawdown_tripped(both)
    assert alarm.title == "Trigger (d) tripped: the paper account is 9.0% below its peak and 6.2 points behind VT on 2026-10-08"
    behind = race_record(trips=[{"day": "2026-10-08", "detail": "z", "below_peak": False, "behind_vt": True,
                                 "drawdown": -0.02, "gap": -0.051}])
    assert health.drawdown_tripped(behind).title == \
        "Trigger (d) tripped: the paper account is 5.1 points behind VT on 2026-10-08"
    # A record that says tripped but lost its detail still warns.
    bare = {"watch": {"d": {"tripped": True, "trips": "?"}}}
    assert health.drawdown_tripped(bare).title == "Trigger (d) tripped: the paper account is past the owner's limit"


@pytest.mark.parametrize("race", [
    None, "not json", "[1, 2]", {"watch": None}, {"watch": {"d": None}}, {"watch": {"d": {"tripped": "yes"}}},
    race_record(tripped=False), {"status_line": "an older record, from before (d)"},
])
def test_no_trip_no_trigger_d_alarm(logs, race):
    journal, audit = _day_with_a_record(logs, race)
    assert health.check(journal, audit, date(2026, 10, 8)) == []


def test_the_cli_reads_the_race_record_beside_the_journal_or_the_one_it_is_given(logs, tmp_path):
    journal, audit = _day_with_a_record(logs, race_record())
    calm = tmp_path / "elsewhere.json"
    calm.write_text(json.dumps(race_record(tripped=False)))
    args = ["--journal", str(journal), "--audit", str(audit), "--day", "2026-10-08"]
    assert health.main(args) == 1
    assert health.main(args + ["--race", str(calm)]) == 0


def test_trigger_d_heads_the_brief_that_goes_to_the_phone(logs):
    """The heartbeat writes the book, the brief reads its alarms, and the
    phone step sends the brief: the real account's trigger is the headline,
    ahead of a stopped calibration."""
    from analysis import book, brief

    journal, audit = _day_with_a_record(logs, race_record())
    (journal.parent / health.FUNDS_FILE).write_text(json.dumps(
        {"calibration": {"status": "stopped", "mirrored_day_count": 3, "mirror_limit": 2}}))
    snapshot = book.build(audit, journal, date(2026, 10, 8))
    text = brief.compose(snapshot, date(2026, 10, 8))
    assert text.splitlines()[0] == ("🟡 2 warnings: Trigger (d) tripped: the paper account is 8.5% below "
                                    "its peak on 2026-10-08")


def test_a_mid_day_reading_below_the_line_raises_no_trigger_d_alarm(logs):
    """26 Sep 2026: (d) trips on closing equity only. A mid-day reading below
    the 8% line is in the race record as a warning marked mid-day, and the
    health check stays quiet about it: the close decides."""
    record = race_record(tripped=False)
    record["watch"]["d"]["midday_warning"] = {"day": "2026-10-08", "mid_day": True, "trips_d": False,
                                              "below_peak": True, "behind_vt": False, "detail": "mid-day ..."}
    journal, audit = _day_with_a_record(logs, record)
    assert health.check(journal, audit, date(2026, 10, 8), token_expires=None) == []


# --------------------------------------------------------------------------- #
# The Supabase starter, the archive and the token (26 Sep 2026)
# --------------------------------------------------------------------------- #


def started_line(source, when="2026-09-28T14:50:00+00:00", trigger="scheduler", ticker="AAPL"):
    payload = json.loads(journal_line(ticker, when=when))
    payload["run"] = {"trigger": trigger, "scheduled_for": "2026-09-28T14:40:00+00:00",
                      "started_at": "2026-09-28T14:43:00+00:00", "minutes_late": 3, "late": False, "run_id": "1"}
    if source is not None:
        payload["run"]["source"] = source
    return json.dumps(payload)


SEP28 = date(2026, 9, 28)


def _starter_day(logs, *lines, starter=None, archive=None):
    journal, audit = logs
    write(journal, *lines)
    if starter is not None:
        (journal.parent / health.STARTER_FILE).write_text(json.dumps(starter))
    if archive is not None:
        (journal.parent / health.ARCHIVE_FILE).write_text(json.dumps(archive))
    return health.check(journal, audit, SEP28, token_expires=None)


def test_a_day_the_supabase_starter_started_is_clean(logs):
    assert _starter_day(logs, started_line("supabase-cron"),
                        starter={"day": "2026-09-28", "status_code": 204},
                        archive={"ok": True, "error": None, "last_success": "2026-09-25T15:30:00+00:00"}) == []


def test_a_day_a_backup_started_is_a_warning_with_the_starters_own_answer(logs):
    alarms = _starter_day(logs, started_line("claude-bridge", trigger="manual"),
                          starter={"day": "2026-09-28", "requested_at": "2026-09-28T14:40:00+00:00",
                                   "status_code": 401, "error": None})
    (alarm,) = alarms
    assert alarm.severity == health.WARNING
    assert alarm.title == "The Supabase starter did not start today's run; claude-bridge did"
    assert "HTTP 401 (GitHub refused the token: it has expired or was revoked)" in alarm.detail
    assert "The day still ran once" in alarm.detail
    assert health.exit_code(alarms) == 1


def test_the_first_run_of_the_day_is_the_one_judged(logs):
    """A person re-running a day the starter started is not a failed starter."""
    assert _starter_day(logs, started_line("supabase-cron"),
                        started_line("manual", when="2026-09-28T17:00:00+00:00", trigger="manual",
                                     ticker="XOM")) == []


@pytest.mark.parametrize("source, shown", [("github-schedule", "github-schedule"), ("watchdog", "watchdog"),
                                           ("unknown", "unknown"), ("<b>bad</b>", "an unknown source"),
                                           (5, "an unknown source")])
def test_any_other_starter_is_named_and_junk_is_not_echoed(logs, source, shown):
    (alarm,) = _starter_day(logs, started_line(source))
    assert alarm.title == f"The Supabase starter did not start today's run; {shown} did"


def test_no_source_says_nothing_about_the_starter(logs):
    """A block from before the field, or no block at all, is not a failed starter."""
    assert _starter_day(logs, started_line(None)) == []
    assert _starter_day(logs, journal_line("AAPL", when="2026-09-28T14:50:00+00:00")) == []


def test_an_unreadable_starter_record_is_said_in_the_detail(logs):
    (alarm,) = _starter_day(logs, started_line("watchdog"),
                            starter={"day": "2026-09-28", "status": "unknown", "why": "project paused or unreachable"})
    assert "could not be read (project paused or unreachable)" in alarm.detail


def test_an_archive_that_is_not_configured_is_a_warning_every_day(logs):
    (alarm,) = _starter_day(logs, started_line("supabase-cron"),
                            archive={"ok": False, "error": "not configured", "last_success": None})
    assert alarm.severity == health.WARNING
    assert alarm.title == "Archive not configured: the Supabase project will pause"
    assert "SUPABASE_URL / SUPABASE_SERVICE_KEY" in alarm.detail and "No push has worked yet." in alarm.detail


def test_a_failed_archive_push_is_a_warning_that_says_restore_when_paused(logs):
    (alarm,) = _starter_day(logs, started_line("supabase-cron"),
                            archive={"ok": False, "error": "project paused or unreachable",
                                     "last_success": "2026-09-20T15:00:00+00:00"})
    assert alarm.title == "The archive push to Supabase failed: project paused or unreachable"
    assert "may be paused; restore it" in alarm.detail and "2026-09-20" in alarm.detail
    (odd,) = _starter_day(logs, started_line("supabase-cron"), archive={"ok": False, "error": "secret=abc"})
    assert odd.title == "The archive push to Supabase failed: an unrecognised error" and "abc" not in odd.detail
    assert _starter_day(logs, started_line("supabase-cron"), archive={"ok": True}) == []
    assert _starter_day(logs, started_line("supabase-cron"), archive=["not", "a", "record"]) == []


@pytest.mark.parametrize("today, severity, title", [
    (date(2026, 10, 1), None, None),
    (date(2026, 10, 12), health.WARNING,
     "The GitHub token the Supabase starter uses expires on 2026-10-26: make a new one"),
    (date(2026, 10, 25), health.WARNING,
     "The GitHub token the Supabase starter uses expires on 2026-10-26: make a new one"),
    (date(2026, 10, 26), health.CRITICAL,
     "The GitHub token the Supabase starter uses expired on 2026-10-26: make a new one"),
    (date(2026, 11, 3), health.CRITICAL,
     "The GitHub token the Supabase starter uses expired on 2026-10-26: make a new one"),
])
def test_the_starters_token_warns_fourteen_days_before_and_is_critical_once_expired(today, severity, title):
    alarm = health.dispatch_token_expiry(date(2026, 10, 26), today)
    if severity is None:
        assert alarm is None
        return
    assert (alarm.severity, alarm.title) == (severity, title)
    assert "github_heartbeat_dispatch" in alarm.detail and "GITHUB_DISPATCH_TOKEN_EXPIRES" in alarm.detail
    assert health.dispatch_token_expiry(None, today) is None


def test_the_token_date_comes_from_the_settings_by_default(logs, monkeypatch):
    from config import settings

    journal, audit = logs
    write(journal, journal_line("AAPL", when="2026-09-28T14:50:00+00:00"))
    monkeypatch.setattr(settings, "GITHUB_DISPATCH_TOKEN_EXPIRES", date(2026, 10, 1))
    assert [a.title for a in health.check(journal, audit, SEP28)] == [
        "The GitHub token the Supabase starter uses expires on 2026-10-01: make a new one"]
    monkeypatch.setattr(settings, "GITHUB_DISPATCH_TOKEN_EXPIRES", None)
    assert health.check(journal, audit, SEP28) == []


def test_a_weekend_or_holiday_with_no_cycle_is_not_an_alarm(logs):
    """Every weekday starter fires on a holiday and the cycle stands down by
    design: no line is the right record, not a lost day."""
    journal, audit = logs
    assert health.check(journal, audit, date(2026, 11, 26), token_expires=None) == []   # Thanksgiving
    assert health.check(journal, audit, date(2026, 9, 27), token_expires=None) == []    # a Sunday
    assert [a.title for a in health.check(journal, audit, SEP28, token_expires=None)] == ["No cycle ran today"]
