"""The day in one phone notification: the worst thing first, nothing invented."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import pytest

from analysis import brief

DAY = date(2026, 9, 17)


def book(**over):
    base = {
        "day": "2026-09-17", "equity": 100_000.0,
        "positions": [{"ticker": "LLY", "has_stop": True}, {"ticker": "XOM", "has_stop": True}],
        "closed": [],
        "exposure": {"positions": 2, "gross": 20_000.0, "at_risk": 800.0, "unrealised": 151.2},
        "cycle": {"tickers": 80, "accepted": [], "directional": [], "cost_usd": 3.91},
        "alarms": [],
    }
    base.update(over)
    return base


def test_a_clean_day_leads_green_and_reads_the_numbers():
    text = brief.compose(book(), DAY)
    lines = text.splitlines()
    assert lines[0] == "🟢 Clean day"
    assert lines[1] == "Equity $100,000 · 2 positions · $20,000 gross · $800 at risk · unrealised +$151"
    assert "No directional call today" in text
    assert "Cycle 80 tickers, $3.91" in text
    assert len(text) <= brief.MAX_CHARS


def test_a_critical_alarm_is_the_headline_and_the_rest_follow():
    alarms = [{"severity": "warning", "title": "2 of 80 ticker(s) produced no signal"},
              {"severity": "critical", "title": "3 position(s) without a working stop"},
              {"severity": "warning", "title": "The screen failed on 1 ticker(s)"}]
    text = brief.compose(book(alarms=alarms, positions=[{"ticker": "XLY", "has_stop": False}]), DAY)
    assert text.splitlines()[0] == "🔴 3 position(s) without a working stop"
    assert "No stop on record: XLY" in text
    assert "Also: 3 position(s) without a working stop; The screen failed" in text  # after the first alarm


def test_warnings_only_lead_yellow_with_a_count():
    alarms = [{"severity": "warning", "title": "A"}, {"severity": "warning", "title": "B"}]
    assert brief.compose(book(alarms=alarms), DAY).splitlines()[0] == "🟡 2 warnings: A"
    assert brief.compose(book(alarms=alarms[:1]), DAY).splitlines()[0] == "🟡 1 warning: A"


def test_a_stale_snapshot_is_the_headline_not_a_number():
    text = brief.compose(book(day="2026-09-16"), DAY)
    assert text.splitlines()[0] == "⚠️ No snapshot for today yet (last: 2026-09-16)"


def test_trades_and_closes_are_named():
    text = brief.compose(book(
        cycle={"tickers": 80, "accepted": ["GOOGL"], "directional": [{"ticker": "GOOGL"}], "cost_usd": 1.0},
        closed=[{"ticker": "TLT", "last_seen": "2026-09-16"}, {"ticker": "OLD", "last_seen": "2026-08-01"}],
    ), DAY)
    assert "Traded: GOOGL" in text
    assert "Closed: TLT" in text and "OLD" not in text


def test_directional_calls_without_a_trade_are_said():
    text = brief.compose(book(cycle={"tickers": 80, "accepted": [], "directional": [{"ticker": "A"}, {"ticker": "B"}], "cost_usd": 2.0}), DAY)
    assert "2 directional calls, none traded" in text


def test_missing_equity_is_said_not_invented():
    text = brief.compose(book(equity=None), DAY)
    assert "Equity not recorded" in text


def test_the_text_never_exceeds_a_notification():
    alarms = [{"severity": "critical", "title": "x" * 300}] + [{"severity": "warning", "title": "y" * 200}] * 3
    text = brief.compose(book(alarms=alarms, positions=[{"ticker": f"T{i}", "has_stop": False} for i in range(20)]), DAY)
    assert len(text) <= brief.MAX_CHARS
    assert "…" in text and text.splitlines()[-1].endswith("2026-09-17")  # the cut spares the day


def test_the_last_line_ends_with_the_snapshot_day_however_the_day_went():
    assert brief.compose(book(), DAY).splitlines()[-1] == "Cycle 80 tickers, $3.91 · 2026-09-17"
    stale = brief.compose(book(day="2026-09-16"), DAY).splitlines()
    assert stale[0].startswith("⚠️") and stale[-1].endswith("2026-09-16")
    no_cost = brief.compose(book(cycle={"tickers": 0, "accepted": [], "directional": []}), DAY)
    assert no_cost.splitlines()[-1] == "Snapshot 2026-09-17"


def test_the_cli_reads_the_snapshot_and_a_missing_one_is_loud(tmp_path, capsys):
    path = tmp_path / "book.json"
    path.write_text(json.dumps(book()))
    assert brief.main(["--book", str(path), "--day", "2026-09-17"]) == 0
    assert capsys.readouterr().out.startswith("🟢 Clean day")
    assert brief.main(["--book", str(tmp_path / "none.json")]) == 1
    assert "No readable snapshot" in capsys.readouterr().out


def test_the_brief_never_reaches_a_broker_or_the_network():
    source = Path(brief.__file__).read_text()
    for banned in ("broker_client", "alpaca", "anthropic", "httpx", "requests", "urllib"):
        assert banned not in source, banned


# --------------------------------------------------------------------------- #
# Who started the day, and the Supabase side of it (26 Sep 2026)
# --------------------------------------------------------------------------- #

RUN = {"source": "supabase-cron", "trigger": "scheduler", "scheduled_for": "2026-09-17T14:40:00+00:00",
       "started_at": "2026-09-17T14:41:05+00:00", "minutes_late": 1}
STARTER = {"day": "2026-09-17", "requested_at": "2026-09-17T14:40:00+00:00", "status_code": 204, "error": None}
ARCHIVE = {"last_attempt": "2026-09-16T16:02:00+00:00", "last_success": "2026-09-16T16:02:00+00:00",
           "ok": True, "error": None}


def test_the_supabase_starters_day_says_who_and_when_and_the_status_code():
    text = brief.compose(book(run=RUN, starter=STARTER, archive=ARCHIVE), DAY)
    lines = text.splitlines()
    assert lines[0] == "🟢 Clean day"
    assert "Started by supabase-cron at 14:41 UTC (1 min after 14:40)" in lines
    assert "Supabase: starter HTTP 204 at 14:40 UTC · archive pushed 2026-09-16" in lines
    assert "⚠️" not in text and len(text) <= brief.MAX_CHARS


def test_a_backup_start_is_a_warning_line_said_once():
    run = dict(RUN, source="claude-bridge", trigger="manual", started_at="2026-09-17T14:43:00+00:00",
               minutes_late=3)
    alarms = [{"severity": "warning", "title": "2 of 80 ticker(s) produced no signal"},
              {"severity": "warning", "title": "The Supabase starter did not start today's run; claude-bridge did"}]
    text = brief.compose(book(run=run, starter=dict(STARTER, status_code=401), archive=ARCHIVE, alarms=alarms), DAY)
    assert "Started by claude-bridge at 14:43 UTC (3 min after 14:40)" in text
    assert "⚠️ The Supabase starter did not start today's run; claude-bridge did" in text
    assert text.count("did not start today's run") == 1, "not repeated under Also"
    assert "Supabase: starter HTTP 401 at 14:40 UTC" in text


def test_the_warning_is_not_repeated_when_it_is_the_headline():
    run = dict(RUN, source="watchdog", trigger="backup", minutes_late=32)
    alarms = [{"severity": "warning", "title": "The Supabase starter did not start today's run; watchdog did"}]
    text = brief.compose(book(run=run, alarms=alarms), DAY)
    assert text.splitlines()[0] == "🟡 1 warning: The Supabase starter did not start today's run; watchdog did"
    assert text.count("did not start today's run") == 1


def test_an_archive_that_is_not_configured_is_warned_about_every_day():
    archive = {"last_attempt": "2026-09-16T16:02:00+00:00", "last_success": None, "ok": False,
               "error": "not configured"}
    starter = {"day": "2026-09-17", "status": "unknown", "why": "not configured: SUPABASE_URL / … are not set"}
    text = brief.compose(book(run=RUN, starter=starter, archive=archive), DAY)
    assert "Supabase: starter: unknown (not configured) · archive not configured" in text
    assert "⚠️ Archive not configured: the Supabase project will pause" in text


def test_a_failed_push_names_the_last_one_that_worked():
    archive = dict(ARCHIVE, ok=False, error="project paused or unreachable",
                   last_success="2026-09-12T16:00:00+00:00")
    text = brief.compose(book(run=RUN, starter=STARTER, archive=archive), DAY)
    assert "archive push failed (project paused or unreachable), last worked 2026-09-12" in text


@pytest.mark.parametrize("starter, said", [
    ({"day": "2026-09-16", "status_code": 204}, "starter: no record for today"),
    ({"day": "2026-09-17", "status_code": None, "error": None}, "starter: no answer from GitHub yet"),
    ({"day": "2026-09-17", "status_code": None, "error": "Timeout of 10000 ms reached"},
     "starter: no answer from GitHub"),
])
def test_what_the_starter_part_says(starter, said):
    text = brief.compose(book(run=RUN, starter=starter, archive=ARCHIVE), DAY)
    assert f"Supabase: {said} · archive pushed 2026-09-16" in text


def test_no_run_block_and_no_records_add_no_lines():
    """A day before any of this existed reads exactly as it did."""
    assert brief.compose(book(), DAY) == brief.compose(book(run=None, starter=None, archive=None), DAY)
    assert "Started by" not in brief.compose(book(), DAY) and "Supabase" not in brief.compose(book(), DAY)


def test_a_run_before_its_time_says_before():
    text = brief.compose(book(run=dict(RUN, started_at="2026-09-17T14:35:00+00:00", minutes_late=-5)), DAY)
    assert "Started by supabase-cron at 14:35 UTC (5 min before 14:40)" in text


def test_the_book_carries_the_run_the_starter_and_the_archive(tmp_path):
    """From the journal's run block and the two records beside it, field by field."""
    from analysis import book as book_module

    journal = tmp_path / "signal_journal.log"
    audit = tmp_path / "execution_audit.log"
    audit.write_text("")
    block = {"trigger": "scheduler", "source": "supabase-cron", "scheduled_for": "2026-09-17T14:40:00+00:00",
             "started_at": "2026-09-17T14:41:05+00:00", "minutes_late": 1, "late": False, "run_id": "3"}
    journal.write_text(json.dumps({"ticker": "AAPL", "ts_utc": "2026-09-17T14:50:00+00:00", "run": block}) + "\n"
                       + json.dumps({"ticker": "XOM", "ts_utc": "2026-09-17T17:00:00+00:00",
                                     "run": dict(block, source="<junk>")}) + "\n")
    (tmp_path / "starter_status.json").write_text(json.dumps(dict(STARTER, extra="dropped")))
    (tmp_path / "archive_status.json").write_text(json.dumps(ARCHIVE))
    snapshot = book_module.build(audit, journal, DAY)
    assert snapshot["run"] == {"source": "supabase-cron", "trigger": "scheduler",
                               "scheduled_for": "2026-09-17T14:40:00+00:00",
                               "started_at": "2026-09-17T14:41:05+00:00", "minutes_late": 1}
    assert snapshot["starter"] == STARTER
    assert snapshot["archive"] == ARCHIVE
    text = brief.compose(snapshot, DAY)
    assert "Started by supabase-cron at 14:41 UTC (1 min after 14:40)" in text
    assert "Supabase: starter HTTP 204 at 14:40 UTC · archive pushed 2026-09-16" in text
