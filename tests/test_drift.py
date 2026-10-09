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
         technicals=None, error=None, held=False, stage=None, setup=SETUP, run=None, minute=0,
         headlines=None, gaps=None):
    at = datetime(day.year, day.month, day.day, 15, minute, tzinfo=timezone.utc)
    news = {} if headlines is None else {"headlines": headlines, "gaps": gaps or []}
    return json.dumps({
        "ts_utc": at.isoformat(), "ticker": ticker,
        "context": {"ticker": ticker, "technicals": technicals or {}, **news},
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


def test_the_band_is_every_week_before_with_two_sample_standard_deviations():
    values = [10.0, 12.0, 14.0, 16.0, 30.0]
    limits = drift.band(values)
    sd = statistics.stdev(values)
    assert limits["mean"] == pytest.approx(statistics.fmean(values), abs=1e-4)
    assert limits["sd"] == pytest.approx(sd, abs=1e-4)
    assert limits["low"] == pytest.approx(statistics.fmean(values) - 2 * sd, abs=1e-4)
    assert drift.band([10.0, 12.0, 14.0]) is None               # fewer than 4 weeks: no band
    assert drift.band([10.0, None, 14.0, 16.0]) is None          # only 3 weeks have the number
    assert drift.band([10.0, None, 14.0, 16.0, 11.0]) is not None


def drifting(weeks_out):
    """Four ordinary weeks, then weeks at the given NEUTRAL counts (of 10 answers), then an ordinary one."""
    lines = []
    for monday, neutral in zip(MONDAYS[:4], (8, 9, 8, 9)):
        lines += week_of_lines(monday, neutral=neutral, longs=10 - neutral)
    for k, neutral in enumerate(weeks_out):
        lines += week_of_lines(MONDAYS[4 + k], neutral=neutral, longs=10 - neutral)
    today = MONDAYS[4 + len(weeks_out)]
    lines += week_of_lines(today, neutral=8, longs=2)
    return build(lines, today), today


def test_one_week_outside_its_band_does_not_alert():
    record, _ = drifting([5])
    week = record["weeks"][4]
    assert week["outside"]["neutral_pct"] is True
    assert week["alerts"] == [] and record["alerts"] == [] and record["alert_on"] is None


def test_two_weeks_in_a_row_outside_alert_on_the_first_day_of_the_next_week():
    record, today = drifting([5, 0])
    weeks = record["weeks"]
    assert all(not w["alerts"] for w in weeks[:5])
    assert any(a.startswith("NEUTRAL share (%): 0 is outside its band") and a.endswith("2 weeks in a row")
               for a in weeks[5]["alerts"])
    assert record["judged_week"] == weeks[5]["week"] and record["alert_on"] == today.isoformat()
    alarm = health.drift_alert(record, today)
    assert alarm.severity == health.WARNING and "2 weeks running" in alarm.title
    assert health.drift_alert(record, today + timedelta(days=1)) is None


def test_no_band_and_no_alert_in_the_first_four_weeks():
    lines = []
    for monday, neutral in zip(MONDAYS[:4], (1, 9, 0, 10)):
        lines += week_of_lines(monday, neutral=neutral, longs=10 - neutral)
    record = build(lines, MONDAYS[4])
    assert all(w["bands"].get("neutral_pct") is None for w in record["weeks"][:4])
    assert record["alerts"] == []


def test_the_floor_share_and_the_starter_share_are_shown_with_no_band():
    record, _ = drifting([5, 0])
    week = record["weeks"][5]
    assert "at_floor_pct" not in week["bands"] and "primary_start_pct" not in week["bands"]
    assert "at_floor_pct" in week["values"] and "primary_start_pct" in week["values"]


def test_a_changed_setting_alerts_the_same_day():
    first, second = MONDAYS[0], MONDAYS[0] + timedelta(days=1)
    changed = dict(SETUP, prompt="ffffffffffff", provider="api.other.example")
    lines = week_of_lines(first, neutral=8, longs=2) + week_of_lines(second, neutral=8, longs=2, setup=changed)
    record = build(lines, second)
    assert "prompt fingerprint changed: abcdef012345 -> ffffffffffff" in record["setting_alerts"]
    assert "host changed: api.deepinfra.com -> api.other.example" in record["setting_alerts"]
    assert record["setting_alert_on"] == second.isoformat()
    alarm = health.setting_changed(record, second)
    assert alarm.severity == health.WARNING and alarm.title.startswith("Model setup changed today")
    # The day after, with the new setting kept, nothing is said.
    third = second + timedelta(days=1)
    record = build(lines + week_of_lines(third, neutral=8, longs=2, setup=changed), third)
    assert record["setting_alerts"] == [] and health.setting_changed(record, third) is None


def test_two_settings_on_one_day_alert_and_the_first_day_never_does():
    other = dict(SETUP, model="another/model")
    lines = week_of_lines(MONDAYS[0], neutral=4, longs=1) + week_of_lines(MONDAYS[0], neutral=4, longs=1, setup=other)
    record = build(lines, MONDAYS[0])
    assert any(a.endswith("on the same day") and a.startswith("model:") for a in record["setting_alerts"])
    record = build(week_of_lines(MONDAYS[0], neutral=8, longs=2), MONDAYS[0])
    assert record["setting_alerts"] == []


def test_a_steady_record_raises_nothing():
    lines = []
    for monday in MONDAYS[:7]:
        lines += week_of_lines(monday, neutral=8, longs=2)
    record = build(lines, MONDAYS[6])
    assert record["alerts"] == [] and record["alert_on"] is None and record["setting_alerts"] == []
    assert health.drift_alert(record, MONDAYS[6]) is None and health.setting_changed(record, MONDAYS[6]) is None


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
    assert any(a.title.startswith("Drift: 1 value(s) outside their normal band 2 weeks running, to 2026-W44")
               for a in alarms)
    alarms = health.check(journal, audit, day + timedelta(days=1), token_expires=None)
    assert not any(a.title.startswith("Drift:") for a in alarms)


# --------------------------------------------------------------------------- #
# Names with no headlines all week (the owner's request of 3 Oct 2026; a report only)
# --------------------------------------------------------------------------- #


def _days(monday: date, n: int = 5) -> list[date]:
    return [monday + timedelta(days=k) for k in range(n)]


def test_a_name_is_listed_only_when_every_line_of_its_week_had_no_headline():
    monday = MONDAYS[0]
    lines = [line(d, "EWU", headlines=[]) for d in _days(monday)]                       # silent all week
    lines += [line(d, "WEAT", headlines=[] if d != monday + timedelta(days=2) else ["one"]) for d in _days(monday)]
    lines += [line(d, "NVDA", headlines=["a", "b"]) for d in _days(monday)]
    lines += [line(d, "CANE", None, held=True, headlines=[]) for d in _days(monday)]     # held all week: counted
    lines += [line(d, "EWT", headlines=[]) for d in _days(monday, 2)]                    # silent when asked...
    lines.append(line(monday + timedelta(days=4), "EWT", None, held=True, headlines=["held-day news"]))  # ...not held
    week = build(lines, MONDAYS[1])["weeks"][0]
    assert week["news"] == {"names": 5, "no_headlines": ["CANE", "EWU"], "search_failed": []}


def test_a_failed_search_is_named_apart_and_a_line_failed_before_asking_or_without_the_field_is_not_counted():
    monday = MONDAYS[0]
    gap = [f"{health.NEWS_GAP_PREFIX}: Bright Data returned an empty body with its 200; nothing to parse"]
    lines = [line(monday, "EWN", headlines=[], gaps=gap)] + [line(d, "EWN", headlines=[]) for d in _days(monday)[1:]]
    lines += [line(d, "OLD", headlines=None) for d in _days(monday)]                      # no field: cannot say
    lines += [line(d, "CTX", None, error="yfinance fell over", stage="context", headlines=[]) for d in _days(monday)]
    week = build(lines, MONDAYS[1])["weeks"][0]
    assert week["news"] == {"names": 1, "no_headlines": ["EWN"], "search_failed": ["EWN"]}


def test_the_failed_news_fetches_of_the_week_are_counted_per_line_and_per_day():
    """The owner, 6 Oct 2026: once a week, how many of production's own news fetches failed. A report only."""
    monday = MONDAYS[0]
    gap = [f"{health.NEWS_GAP_PREFIX}: Bright Data returned an empty body with its 200; nothing to parse"]
    other_gap = ["fundamentals unavailable: yfinance said no"]
    lines = [line(d, "XLB", headlines=["a"]) for d in _days(monday)]
    lines += [line(monday, "DBC", headlines=[], gaps=gap), line(monday, "TLT", headlines=[], gaps=gap)]
    lines += [line(monday + timedelta(days=2), "DBC", None, held=True, headlines=[], gaps=gap)]   # held: counted
    lines += [line(monday + timedelta(days=1), "EWU", headlines=[], gaps=other_gap)]           # not a news gap
    lines += [line(monday, "CTX", None, error="yfinance fell over", stage="context", headlines=[])]  # never searched
    lines += [line(monday, "OLD", headlines=None)]                                              # cannot say
    week = build(lines, MONDAYS[1])["weeks"][0]
    days = [d.isoformat() for d in _days(monday)]
    assert week["news_fetches"] == {
        "lines": 9, "failed": 3, "names": ["DBC", "TLT"],
        "by_day": {days[0]: [2, 3], days[1]: [0, 2], days[2]: [1, 2], days[3]: [0, 1], days[4]: [0, 1]}}
    assert drift.news_fetches_line(week["news_fetches"]) == (
        "production news fetches that failed: 3 of 9 lines (by day: Mon 2, Tue 0, Wed 1, Thu 0, Fri 0)")
    assert "- production news fetches that failed: 3 of 9 lines (by day: Mon 2, Tue 0, Wed 1, Thu 0, Fri 0)" in drift.render_week(week)
    # A week with a day missing (Thanksgiving 2026) still says which day each count is.
    holiday = {"lines": 320, "failed": 3, "names": ["A"], "by_day": {
        "2026-11-23": [1, 80], "2026-11-24": [0, 80], "2026-11-25": [2, 80], "2026-11-27": [0, 80]}}
    assert drift.news_fetches_line(holiday) == (
        "production news fetches that failed: 3 of 320 lines (by day: Mon 1, Tue 0, Wed 2, Fri 0)")
    # Not a number with a band: it can never alert.
    assert "news_fetches" not in week["values"] and not any("fetch" in key for key in drift.NUMBERS)
    assert drift.news_fetches_line({"lines": 0, "failed": 0, "names": [], "by_day": {}}) is None
    assert drift.news_fetches_line(None) is None


def test_a_prompt_that_failed_to_render_still_counts_the_news_it_gathered():
    """A failed gather journals an empty context; a failed render journals what was gathered, headlines included."""
    monday = MONDAYS[0]
    lines = [line(d, "XLE", None, error="template broke", stage="context", headlines=["a", "b", "c"])
             for d in _days(monday, 4)]
    lines.append(line(monday + timedelta(days=4), "XLE", headlines=[]))
    lines += [line(d, "EWU", headlines=[]) for d in _days(monday)]
    week = build(lines, MONDAYS[1])["weeks"][0]
    assert week["news"] == {"names": 2, "no_headlines": ["EWU"], "search_failed": []}


def test_the_count_has_no_band_and_no_alert_and_the_text_shows_it():
    """One silent name a week for four weeks, then six two weeks running: a band on the count would alert."""
    weeks = []
    for k in range(6):
        silent = 1 if k < 4 else 6
        weeks += week_of_lines(MONDAYS[k], neutral=8, longs=2)
        weeks += [line(MONDAYS[k], f"Q{k}{i}", headlines=[]) for i in range(silent)]
        weeks.append(line(MONDAYS[k], "NVDA", headlines=["x"]))
    record = build(weeks, MONDAYS[6])
    last = record["weeks"][5]
    assert len(last["news"]["no_headlines"]) == 6 and last["news"]["names"] == 7
    assert set(last["bands"]) == {key for key, _ in drift.BANDED} == {
        "neutral_pct", "conviction_mean", "agreement_pct", "long_pct", "setup_error_pct", "model_error_pct",
        "minutes_late_mean"}
    assert record["alerts"] == [] and all(w["alerts"] == [] for w in record["weeks"])
    assert not any("headline" in key for key, _ in drift.NUMBERS) and set(last["values"]) == {
        key for key, _ in drift.NUMBERS}
    text = "\n".join(drift.render_week(last))
    assert "- names with no headlines all week: 6 of 7 (Q50, Q51, Q52, Q53, Q54, Q55)" in text
    assert "band" not in next(l for l in drift.render_week(last) if "no headlines" in l)
    assert json.loads(json.dumps(record, allow_nan=False)) == record


def test_the_line_caps_the_names_only_when_asked_and_says_nothing_when_nothing_was_counted():
    news = {"names": 80, "no_headlines": [f"T{i:02d}" for i in range(15)], "search_failed": ["T00"]}
    full = drift.no_headlines_line(news)
    assert full.startswith("names with no headlines all week: 15 of 80 (T00, T01,") and "T14" in full
    assert full.endswith("; the news search failed at least once for 1 of them (T00)")
    short = drift.no_headlines_line(news, limit=12)
    assert "T11, …)" in short and "T12" not in short and drift.PHONE_NAMES == 12
    assert drift.no_headlines_line({"names": 3, "no_headlines": [], "search_failed": []}) == \
        "names with no headlines all week: 0 of 3"
    assert drift.no_headlines_line({"names": 0, "no_headlines": [], "search_failed": []}) is None
    assert drift.no_headlines_line(None) is None


def test_the_reader_counts_headlines_and_never_reads_a_missing_field_as_zero():
    entries = read_lines([line(MONDAYS[0], "A", headlines=["x", "y"]), line(MONDAYS[0], "B", headlines=[]),
                          line(MONDAYS[0], "C")]).entries
    assert [e.headline_count for e in entries] == [2, 0, None]
