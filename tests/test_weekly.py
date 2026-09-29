"""The weekly report and how it reaches the phone.

Once a week, after the daily brief: last week's drift numbers, the risk
digest and, when new, the monthly concentration report (27 Sep 2026). The
model key and the phone topic never share a step, and nothing here can fail
the trading run.
"""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from analysis import weekly
from orchestrator import llm
from tests.test_phone import _is_a_safe_push

ROOT = Path(__file__).resolve().parents[1]
WEEK = "2026-W45"
URL = "https://github.com/o/r/blob/main/logs/weekly/2026-W45.md"


def drift_record(alerts=()):
    week = {"week": "2026-W44", "monday": "2026-10-26", "complete": True, "days": ["2026-10-26"],
            "counts": {"asked": 50, "answered": 49}, "alerts": list(alerts),
            "values": {"neutral_pct": 88.0, "conviction_mean": 0.45, "at_floor_pct": 100.0,
                       "agreement_pct": 70.0, "long_pct": 90.0, "setup_error_pct": 0.0,
                       "model_error_pct": 2.0, "minutes_late_mean": 1.0, "primary_start_pct": 100.0},
            "bands": {"neutral_pct": {"low": 80.0, "high": 95.0, "mean": 87.5, "sd": 3.75}},
            "conviction_groups": {"below the floor": 0, "0.30-0.40": 3},
            "starts": [{"source": "supabase-cron"}],
            "names": {"model": ["openai/gpt-oss-120b"], "provider": ["api.deepinfra.com"],
                      "reasoning_effort": ["high"], "screening": ["off"], "prompt": ["0123456789ab"]}}
    current = dict(week, week="2026-W45", monday="2026-11-02", complete=False, alerts=[])
    return {"rule": "the band", "weeks": [week, current]}


def digest_record(flags=1):
    return {"status": "ok", "held": {"NVDA": "long"}, "cost_usd": 0.004, "cap_usd": 1.0, "dropped": 0,
            "headlines_read": 30,
            "earnings": [{"ticker": "NVDA", "date": "2026-11-19", "days_away": 17,
                          "link": "https://finance.yahoo.com/calendar/earnings?symbol=NVDA"}],
            "flags": [{"ticker": "NVDA", "kind": "major_news", "note": f"Event number {k} happened.",
                       "title": f"Title {k}", "source": "Reuters", "seen": "2026-11-02",
                       "link": f"https://news.example.com/{k}/" + "x" * 80} for k in range(flags)]}


def logs(tmp_path, drift=None, digest=None, conc=None):
    (tmp_path / "digest").mkdir(exist_ok=True)
    if drift is not None:
        (tmp_path / "drift.json").write_text(json.dumps(drift))
    if digest is not None:
        (tmp_path / "digest" / f"{WEEK}.json").write_text(json.dumps(digest))
    if conc is not None:
        (tmp_path / "concentration.json").write_text(json.dumps(conc))
    return tmp_path


def test_the_phone_text_leads_with_drift_alerts_and_ends_with_the_link(tmp_path):
    path = logs(tmp_path, drift_record(["NEUTRAL share (%): 99 is outside its band 80 to 95"]), digest_record())
    text = weekly.phone(WEEK, URL, path)
    first = text.split("\n", 1)[0]
    assert first == "Weekly report 2026-W45: 1 drift alert(s)"
    assert "- NEUTRAL share (%): 99 is outside its band" in text
    assert "NVDA earnings 2026-11-19" in text and "https://news.example.com/0/" in text
    assert text.rstrip().endswith(f"Full report: {URL}")


def test_a_long_digest_is_cut_to_one_notification_and_keeps_the_link(tmp_path):
    path = logs(tmp_path, drift_record(), digest_record(flags=25))
    text = weekly.phone(WEEK, URL, path)
    assert len(text.encode()) <= weekly.PHONE_BYTES
    assert text.rstrip().endswith(f"Full report: {URL}")
    assert "…" in text


def test_the_report_says_plainly_what_is_missing(tmp_path):
    text = weekly.phone(WEEK, URL, logs(tmp_path))
    assert "Drift: no complete week recorded yet." in text
    assert "Risk digest: not made this week." in text
    md = weekly.markdown(WEEK, tmp_path)
    assert "## Drift" in md and "## Risk digest for the held names" in md and "Not made this week." in md


def test_the_concentration_report_is_shown_the_week_after_it_is_made_only(tmp_path):
    month = {"month": "2026-10", "as_of": "2026-10-30", "made_on": "2026-11-02",
             "book": None, "breadth": {"above": 30, "of": 80, "pct": 37.5, "no_data": []},
             "vt_volatility": {"annualised_pct": 12.0, "sessions": 22}}
    conc = {"kind": "concentration", "latest": "2026-10", "months": {"2026-10": month}}
    assert weekly.new_concentration(conc, "2026-W45") is month       # made on this week's Monday
    assert weekly.new_concentration(conc, "2026-W46") is month       # the week after: still within 7 days
    assert weekly.new_concentration(conc, "2026-W47") is None
    text = weekly.phone(WEEK, URL, logs(tmp_path, drift_record(), digest_record(), conc))
    assert "Concentration, 2026-10" in text and "descriptive only" in text


def test_the_markdown_says_which_month_the_concentration_report_is_for(tmp_path):
    """2026-W40 showed 2026-08's report under a heading with no month, and "book:
    no account snapshot recorded that month" read as if this month's were missing."""
    month = {"month": "2026-10", "as_of": "2026-10-30", "made_on": "2026-11-02",
             "book": None, "breadth": {"above": 30, "of": 80, "pct": 37.5, "no_data": []},
             "vt_volatility": {"annualised_pct": 12.0, "sessions": 22}}
    conc = {"kind": "concentration", "latest": "2026-10", "months": {"2026-10": month}}
    md = weekly.markdown(WEEK, logs(tmp_path, drift_record(), digest_record(), conc))
    assert "## Concentration for 2026-10 (as of 2026-10-30; monthly, descriptive only)" in md
    assert "- book: not measured: no account snapshot was recorded on or before 2026-10-30" in md


def test_the_markdown_lists_every_flag_with_its_source_and_link(tmp_path):
    md = weekly.markdown(WEEK, logs(tmp_path, drift_record(), digest_record(flags=3)))
    for k in range(3):
        assert f"[Title {k}](https://news.example.com/{k}/" in md
    assert "Cost: $0.0040 (cap $1.00 a week)" in md


# --------------------------------------------------------------------------- #
# The workflows
# --------------------------------------------------------------------------- #


def _steps(workflow: str, job: str) -> dict:
    wf = yaml.safe_load((ROOT / ".github/workflows" / workflow).read_text())
    return {s.get("name"): s for s in wf["jobs"][job]["steps"]}


def test_the_drift_record_is_written_before_the_book_reads_it():
    steps = _steps("heartbeat.yml", "cycle")
    names = list(steps)
    step = steps["Measure the model's drift, week by week"]
    assert names.index("Measure the model's drift, week by week") < names.index("Write the book snapshot")
    assert "python -m analysis.drift" in step["run"] and "logs/drift.json" in step["run"]
    assert step["continue-on-error"] is True
    assert "env" not in step                                                    # no key, no network
    commit = steps["Commit the journal"]["run"]
    for path in ("logs/drift.json", "logs/weekly", "logs/digest"):
        assert f"git add -f {path} 2>/dev/null || true" in commit


def test_the_weekly_report_holds_the_model_key_and_nothing_else():
    steps = _steps("heartbeat.yml", "cycle")
    names = list(steps)
    step = steps["Make the weekly report"]
    assert names.index("Make the weekly report") > names.index("Push the day to the owner's phone")
    assert step["id"] == "weekly" and step["continue-on-error"] is True
    assert "steps.guard.outputs.skip != 'yes'" in step["if"] and "inputs.mode != 'protect'" in step["if"]
    assert set(step["env"]) == {"FULL_MODEL_API_KEY", "REPORTS_URL"}   # the model reading is back (29 Sep 2026)
    assert step["env"]["FULL_MODEL_API_KEY"] == steps["Run one cycle"]["env"]["FULL_MODEL_API_KEY"]
    run = step["run"]
    assert "python -m orchestrator.heartbeat --weekly-digest" in run
    assert 'if [ -f "logs/weekly/$week.md" ]' in run                              # once a week
    assert "--once" not in run and "NTFY" not in run


def test_the_weekly_step_outlasts_a_digest_call_and_its_retry():
    """2026-W40 (29 Sep 2026): the digest's call and its one retry each ran to
    the 300-second read timeout, which was all ten of the step's minutes, and
    the step was stopped as the report was being written. The digest's
    batches are asked at once, so its worst case is still one call's."""
    step = _steps("heartbeat.yml", "cycle")["Make the weekly report"]
    two_asks = llm.TRANSPORT_ATTEMPTS * llm.FULL_MODEL_TIMEOUT_SECONDS
    assert step["timeout-minutes"] * 60 >= two_asks + 3 * 60


def test_the_weekly_report_reaches_the_phone_as_a_safe_push_after_the_commit():
    steps = _steps("heartbeat.yml", "cycle")
    names = list(steps)
    step = steps["Push the weekly report to the owner's phone"]
    _is_a_safe_push(step)
    assert set(step["env"]) == {"NTFY_TOPIC"}
    assert step["if"] == "always() && steps.guard.outputs.skip != 'yes' && steps.weekly.outputs.made == 'yes'"
    assert names.index("Push the weekly report to the owner's phone") > names.index("Commit the journal")
    assert '"priority": 3' in step["run"]


def test_the_concentration_report_is_made_by_the_credential_free_funds_workflow():
    steps = _steps("funds.yml", "funds")
    step = steps["The monthly concentration report"]
    assert step["continue-on-error"] is True and "env" not in step
    assert "python -m analysis.concentration --previous --history logs/concentration.json" in step["run"]
    assert "git add -f logs/concentration.json 2>/dev/null || true" in steps["Commit the two files"]["run"]
