"""The day in one phone notification: the worst thing first, nothing invented."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

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
