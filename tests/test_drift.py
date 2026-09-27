"""The weekly drift report: the owner's band, the numbers it judges, and the one day it speaks.

The owner's rule (27 Sep 2026): a number leaves its normal band outside the
mean plus or minus 2 standard deviations of the 4 weeks before; no band, so
no alert, until 4 weeks of data exist; the phone hears it once.
"""

from __future__ import annotations

import json
import statistics
from datetime import date, datetime, timedelta, timezone

import pytest

from analysis import drift, health
from analysis.reader import read_lines

SETUP = {"model": "openai/gpt-oss-120b", "provider": "api.deepinfra.com", "prompt": "abcdef012345"}
UP = {"return_63d": 0.10, "distance_sma50": 0.03, "annualised_volatility": 0.20}
DOWN = {"return_63d": -0.10, "distance_sma50": -0.03, "annualised_volatility": 0.20}


def line(day: date, ticker: str, bias: str | None = "NEUTRAL", conviction: float = 0.2, *,
         technicals=None, error=None, held=False, stage=None, setup=SETUP, run=None, minute=0):
    at = datetime(day.year, day.month, day.day, 15, minute, tzinfo=timezone.utc)
    return json.dumps({
        "ts_utc": at.isoformat(), "ticker": ticker,
        "context": {"ticker": ticker, "technicals": technicals or {}},
        "signal": None if bias is None else {"ticker": ticker, "bias": bias, "conviction": conviction},
        "error": error, "held": held, "stage": stage, "screening": False, "reasoning_effort": "high",
        "usage": {"model": SETUP["model"]} if bias is not None else None,
        **({"model_setup": setup} if setup else {}),
        **({"run": run} if run else {}),
    })


def week_of_lines(monday: date, neutral: int, longs: int, shorts: int = 0, *, setup=SETUP,
                  failed_model: int = 0, failed_setup: int = 0) -> list[str]:
    """One cycle day (the Monday) with the given answers, each on its own ticker."""
    run = {"trigger": "schedule", "source": "supabase-cron", "scheduled_for": f"{monday}T14:40:00+00:00",
           "started_at": f"{monday}T14:41:00+00:00", "minutes_late": 1, "late": False, "run_id": str(monday)}
    out, n = [], 0
    for _ in range(neutral):
        out.append(line(monday, f"N{n}", "NEUTRAL", 0.1, technicals=UP, setup=setup, run=run)); n += 1
    for _ in range(longs):
        out.append(line(monday, f"L{n}", "BULLISH", 0.45, technicals=UP, setup=setup, run=run)); n += 1
    for _ in range(shorts):
        out.append(line(monday, f"S{n}", "BEARISH", 0.45, technicals=UP, setup=setup, run=run)); n += 1
    for _ in range(failed_model):
        out.append(line(monday, f"F{n}", None, error="read timeout", setup=setup, run=run)); n += 1
    for _ in range(failed_setup):
        out.append(line(monday, f"X{n}", None, error="HTTP 401 Unauthorized", setup=setup, run=run)); n += 1
    return out


def build(lines, today):
    return drift.build(read_lines(lines).entries, today)


MONDAYS = [drift.START + timedelta(days=7 * k) for k in range(8)]


def test_one_week_of_numbers_is_counted_from_the_calls_the_model_got():
    lines = week_of_lines(MONDAYS[0], neutral=6, longs=3, shorts=1, failed_model=1, failed_setup=1)
    lines.append(line(MONDAYS[0], "HELD", None, held=True))                   # not asked: left out
    lines.append(line(MONDAYS[0], "CTX", None, error="news down", stage="context"))  # not asked either
    record = build(lines, MONDAYS[1])
    week = record["weeks"][0]
    assert week["complete"] is True
    assert week["counts"]["asked"] == 12 and week["counts"]["answered"] == 10
    v = week["values"]
    assert v["neutral_pct"] == 60.0
    assert v["long_pct"] == 75.0
    assert v["conviction_mean"] == 0.45 and v["at_floor_pct"] == 100.0
    # Momentum says long on every line (UP): the 3 longs agree, the short does not.
    assert v["agreement_pct"] == 75.0
    assert v["model_error_pct"] == pytest.approx(100 / 12, abs=0.01)
    assert v["setup_error_pct"] == pytest.approx(100 / 12, abs=0.01)
    assert v["minutes_late_mean"] == 1.0 and v["primary_start_pct"] == 100.0
    assert week["names"]["prompt"] == ["abcdef012345"]
    assert week["names"]["provider"] == ["api.deepinfra.com"]


def test_the_band_is_the_mean_plus_or_minus_two_sample_standard_deviations():
    limits = drift.band([10.0, 12.0, 14.0, 16.0])
    sd = statistics.stdev([10.0, 12.0, 14.0, 16.0])
    assert limits["mean"] == 13.0 and limits["sd"] == pytest.approx(sd, abs=1e-4)
    assert limits["low"] == pytest.approx(13 - 2 * sd, abs=1e-4)
    assert limits["high"] == pytest.approx(13 + 2 * sd, abs=1e-4)
    assert drift.band([10.0, 12.0, 14.0]) is None               # fewer than 4 weeks: no band
    assert drift.band([10.0, None, 14.0, 16.0]) is None          # a week without the number: no band


def test_no_alert_until_four_weeks_of_data_exist_then_a_drifting_week_alerts():
    lines = []
    # Four ordinary weeks with a little movement, then a week where the model
    # suddenly says NEUTRAL to everything.
    for monday, neutral in zip(MONDAYS[:4], (8, 9, 8, 9)):
        lines += week_of_lines(monday, neutral=neutral, longs=2)
    lines += week_of_lines(MONDAYS[4], neutral=20, longs=0)
    # Judged on the first cycle day of the week after.
    lines += week_of_lines(MONDAYS[5], neutral=8, longs=2)
    record = build(lines, MONDAYS[5])
    weeks = record["weeks"]
    assert all(not w["alerts"] for w in weeks[:4])               # no band, no alert, in weeks 1 to 4
    assert weeks[4]["bands"]["neutral_pct"] is not None
    assert any(a.startswith("NEUTRAL share (%): 100") for a in weeks[4]["alerts"])
    assert record["judged_week"] == weeks[4]["week"]
    assert record["alert_on"] == MONDAYS[5].isoformat()
    assert weeks[5]["complete"] is False and weeks[5]["alerts"] == []


def test_the_alert_is_said_once_on_the_first_cycle_day_of_the_next_week():
    lines = []
    for monday, neutral in zip(MONDAYS[:4], (8, 9, 8, 9)):
        lines += week_of_lines(monday, neutral=neutral, longs=2)
    lines += week_of_lines(MONDAYS[4], neutral=20, longs=0)
    lines += week_of_lines(MONDAYS[5], neutral=8, longs=2)
    tuesday = MONDAYS[5] + timedelta(days=1)
    lines += [line(tuesday, "T1", "NEUTRAL", technicals=UP)]
    monday_record = build(lines, MONDAYS[5])
    tuesday_record = build(lines, tuesday)
    assert monday_record["alert_on"] == MONDAYS[5].isoformat()
    # Tuesday's record still names Monday: the health check says it on Monday only.
    assert tuesday_record["alert_on"] == MONDAYS[5].isoformat()
    assert health.drift_alert(monday_record, MONDAYS[5]) is not None
    assert health.drift_alert(tuesday_record, tuesday) is None
    alarm = health.drift_alert(monday_record, MONDAYS[5])
    assert alarm.severity == health.WARNING
    assert alarm.title.startswith("Drift: ") and monday_record["judged_week"] in alarm.title


def test_a_new_prompt_or_host_leaves_its_band_as_a_name():
    lines = []
    for monday in MONDAYS[:4]:
        lines += week_of_lines(monday, neutral=8, longs=2)
    changed = dict(SETUP, prompt="ffffffffffff", provider="api.other.example")
    lines += week_of_lines(MONDAYS[4], neutral=8, longs=2, setup=changed)
    lines += week_of_lines(MONDAYS[5], neutral=8, longs=2)
    week = build(lines, MONDAYS[5])["weeks"][4]
    assert "prompt fingerprint: ffffffffffff was not seen in the 4 weeks before" in week["alerts"]
    assert "host: api.other.example was not seen in the 4 weeks before" in week["alerts"]


def test_a_steady_week_raises_nothing_and_the_health_check_stays_quiet():
    lines = []
    for monday in MONDAYS[:6]:
        lines += week_of_lines(monday, neutral=8, longs=2)
    record = build(lines, MONDAYS[5])
    assert record["alerts"] == [] and record["alert_on"] is None
    assert health.drift_alert(record, MONDAYS[5]) is None


def test_weeks_before_the_start_are_not_read():
    early = drift.START - timedelta(days=7)
    record = build(week_of_lines(early, neutral=5, longs=5), drift.START)
    assert record["weeks"][0]["counts"]["lines"] == 0


def test_the_record_is_plain_json_and_the_text_names_every_number():
    lines = week_of_lines(MONDAYS[0], neutral=6, longs=3)
    record = build(lines, MONDAYS[1])
    json.loads(json.dumps(record, allow_nan=False))
    text = drift.render(record)
    for _, words in drift.NUMBERS:
        assert words in text
    assert "no band yet" in text


def test_the_health_check_reads_the_record_beside_the_journal(tmp_path):
    journal = tmp_path / "journal"
    journal.mkdir()
    (journal / "2026-11.log").write_text("")
    audit = tmp_path / "execution_audit.log"
    audit.write_text("")
    day = date(2026, 11, 2)
    (tmp_path / "drift.json").write_text(json.dumps({
        "alert_on": day.isoformat(), "judged_week": "2026-W44",
        "alerts": ["NEUTRAL share (%): 99 is outside its band 85 to 93"]}))
    alarms = health.check(journal, audit, day, token_expires=None)
    assert any(a.title.startswith("Drift: 1 value(s) left their normal band in 2026-W44") for a in alarms)
    alarms = health.check(journal, audit, day + timedelta(days=1), token_expires=None)
    assert not any(a.title.startswith("Drift:") for a in alarms)
