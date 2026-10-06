"""The card's rule (2), pooled over five weekday checks (the owner's decision of 6 Oct 2026)."""

from __future__ import annotations

import ast
import json
import re
from datetime import date
from pathlib import Path

import pytest

from analysis import news_pooled as npool
from config import shadow_universe as su

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "analysis" / "news_pooled.py"
DAY_ONE = npool.CHECKS_DIR / "2026-10-05.json"
#: Five weekdays over two weeks (2026-10-05 is a Monday).
FIVE = (date(2026, 10, 5), date(2026, 10, 8), date(2026, 10, 13), date(2026, 10, 15), date(2026, 10, 20))


def _days(per_name: dict, dates=FIVE) -> list[npool.DayCheck]:
    """Five checks: every name 10 of 10 on every day, except the names given (one value per day)."""
    out = []
    for i, day in enumerate(dates):
        names = {t: (10, 10, 10) for t in su.TICKERS}
        for ticker, values in per_name.items():
            names[ticker] = values[i]
        out.append(npool.DayCheck(day=day, runs=(i + 1,), names=names))
    return out


def _decided(per_name: dict) -> dict:
    return {p.ticker: (p.decision, p.reason) for p in npool.pool(_days(per_name))}


# --------------------------------------------------------------------------- #
# The owner's rule


def test_under_30_percent_with_at_least_10_pooled_headlines_is_replaced():
    found = _decided({"APD": [(2, 0, 0)] * 5, "ECL": [(2, 1, 1)] * 5})
    assert found["APD"] == (npool.REPLACE, "0 of 10 pooled headlines relevant, under 30%")
    assert found["ECL"] == (npool.KEEP, "5 of 10 pooled headlines relevant, 30% or more")


def test_exactly_30_percent_is_kept():
    found = _decided({"GD": [(2, 1, 1), (2, 1, 1), (2, 1, 0), (2, 0, 0), (2, 0, 0)]})
    assert found["GD"][0] == npool.KEEP and "3 of 10" in found["GD"][1]


def test_fewer_than_10_pooled_headlines_is_kept_unless_zero_on_all_five_days():
    found = _decided({"ORLY": [(1, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)],
                      "OKE": [(0, 0, 0)] * 5,
                      "NMR": [(0, 0, 0), None, (0, 0, 0), None, (0, 0, 0)],
                      "ZTO": [None] * 5,
                      "HSY": [(1, 0, 0), None, None, (8, 1, 1), None]})
    assert found["ORLY"] == (npool.KEEP, "fewer than 10 pooled headlines (1), not zero on all five days")
    assert found["OKE"] == (npool.REPLACE, "zero headlines on all five days")
    assert found["NMR"] == (npool.REPLACE, "zero headlines on all five days")       # no answer counts as zero
    assert found["ZTO"] == (npool.REPLACE, "no answer on any of the five days: zero headlines on all five days")
    assert found["HSY"][0] == npool.KEEP                                            # 9 pooled headlines


def test_a_day_with_no_answer_adds_nothing_to_the_pooled_share():
    found = {p.ticker: p for p in npool.pool(_days({"IBN": [None, (10, 1, 1), (10, 1, 1), None, None]}))}
    assert (found["IBN"].answered, found["IBN"].headlines, found["IBN"].relevant) == (2, 20, 2)
    assert found["IBN"].decision == npool.REPLACE


def test_stt_and_irm_are_kept_whatever_the_pooled_result():
    found = _decided({"STT": [(0, 0, 0)] * 5, "IRM": [(4, 0, 0)] * 5})
    assert found["STT"][0] == found["IRM"][0] == npool.KEEP
    assert "owner's decision of 6 Oct 2026" in found["STT"][1] and set(npool.KEPT) == {"STT", "IRM"}


def test_the_rule_applies_to_every_name_of_the_list():
    found = _decided({"AAPL": [(10, 2, 2)] * 5})
    assert found["AAPL"][0] == npool.REPLACE
    assert sum(1 for d, _ in _decided({}).values() if d == npool.REPLACE) == 0


def test_the_numbers_are_the_owners():
    assert (npool.DAYS_NEEDED, npool.MIN_POOLED_HEADLINES, npool.FAIL_BELOW) == (5, 10, 0.30)
    assert npool.LAST_DAY == date(2026, 12, 22) == su.REGISTRATION


# --------------------------------------------------------------------------- #
# Only five checks, on five weekdays, before the freeze


def test_no_decision_before_five_checks():
    days = _days({"APD": [(2, 0, 0)] * 5})[:4]
    assert npool.problems(days) == ["4 of 5 checks so far"]
    assert all(p.decision is None for p in npool.pool(days))
    assert "**No decision yet**: 4 of 5 checks so far." in npool.report(days, npool.pool(days))


@pytest.mark.parametrize("dates, problem", [
    ((*FIVE[:4], date(2026, 10, 10)), "2026-10-10 is not a weekday the market traded"),       # a Saturday
    ((*FIVE[:4], date(2026, 11, 26)), "2026-11-26 is not a weekday the market traded"),      # Thanksgiving
    ((*FIVE[:4], date(2026, 12, 23)), "2026-12-23 is after the list freezes (2026-12-22)"),
    ((*FIVE[:4], FIVE[0]), "two checks on the same day"),
])
def test_a_check_that_cannot_count(dates, problem):
    assert problem in npool.problems(_days({}, dates))


def test_more_than_five_checks_is_not_five():
    six = _days({}, (*FIVE, date(2026, 10, 21)))
    assert npool.problems(six) == ["6 checks: the rule pools exactly 5"]


def test_the_report_shows_the_weeks_and_the_replacements():
    days = _days({"APD": [(2, 0, 0)] * 5})
    text = npool.report(days, npool.pool(days))
    assert "Weeks: 3 different (2026-W41, 2026-W42, 2026-W43)." in text
    assert "**Replace: 1 name(s)**: APD (0 of 10 pooled headlines relevant, under 30%)" in text
    assert "Kept by the owner's decision: STT (50 of 50, 100%), IRM (50 of 50, 100%)" in text
    assert "| APD | 5 of 5 | 10 | 0 | 0% | 0 | replace |" in text


# --------------------------------------------------------------------------- #
# The day files


def test_the_first_check_is_the_one_written_up_on_5_october():
    """2026-10-05: the recheck's counts for the 44 names it asked, the first run's for the others."""
    day = npool.load_day(DAY_ONE)
    assert day.day == date(2026, 10, 5) and day.runs == (37345386044, 37351217326)
    answered = [c for c in day.names.values() if c is not None]
    assert [t for t, c in day.names.items() if c is None] == ["ZTO"]
    assert (len(answered), sum(c[0] for c in answered), sum(c[1] for c in answered)) == (250, 1537, 1149)
    # The same numbers as the table in docs/research/news-relevance.md.
    section = (ROOT / "docs" / "research" / "news-relevance.md").read_text(encoding="utf-8")
    section = section.split("## 1.")[1].split("## 2.")[0]
    rows = re.findall(r"^\| ([A-Z.]+) \| [^|]+ \| ([^|]*) \| ([^|]*) \| [^|]* \| [^|]* \|$", section, re.M)
    assert len(rows) == 251
    for ticker, headlines, relevant in rows:
        counts = day.names[ticker]
        assert (counts is None and headlines == "—") or (str(counts[0]), str(counts[1])) == (headlines, relevant)


def test_every_day_file_is_a_whole_check_of_the_list():
    files = sorted(npool.CHECKS_DIR.glob("*.json"))
    assert files and files[0].name == "2026-10-05.json"
    for path in files:
        day = npool.load_day(path)
        assert path.stem == day.day.isoformat()
        assert list(day.names) == list(su.TICKERS)
        assert npool.day_json(json.loads(path.read_text(encoding="utf-8"))) == path.read_text(encoding="utf-8")


def test_a_day_file_with_a_name_missing_or_extra_is_refused(tmp_path):
    made = json.loads(DAY_ONE.read_text(encoding="utf-8"))
    del made["names"]["BKR"]
    made["names"]["XYZ"] = [1, 1, 1]
    (tmp_path / "bad.json").write_text(json.dumps(made), encoding="utf-8")
    with pytest.raises(ValueError, match=r"missing \['BKR'\], not in the list \['XYZ'\]"):
        npool.load_day(tmp_path / "bad.json")


def test_a_day_is_made_from_the_runs_logs_a_recheck_replacing_what_it_asked():
    first = {t: [5, 4, 4] for t in su.TICKERS if t not in ("ZTO", "OKE")}
    log = "\n".join([
        "2026-10-08T17:00:01Z RESULT " + json.dumps(first),
        "2026-10-08T17:00:01Z FAILED " + json.dumps(["ZTO", "OKE"]),
        "2026-10-08T17:20:00Z RESULT " + json.dumps({"OKE": [3, 3, 3], "BKR": [6, 1, 1]}),
        "2026-10-08T17:20:00Z FAILED " + json.dumps(["ZTO"]),
    ])
    made = npool.day_from_log(log, date(2026, 10, 8), [1, 2])
    assert made["names"]["OKE"] == [3, 3, 3] and made["names"]["BKR"] == [6, 1, 1] and made["names"]["ZTO"] is None
    assert list(made["names"]) == list(su.TICKERS) and made["runs"] == [1, 2]
    with pytest.raises(ValueError, match="not asked that day: OKE, ZTO"):
        npool.day_from_log("RESULT " + json.dumps(first) + "\nFAILED []", date(2026, 10, 8), [1])


def test_the_module_is_pure():
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
    imported = {alias.name.split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.Import)
                for alias in node.names}
    imported |= {(node.module or "").split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    assert not imported & {"httpx", "requests", "urllib", "anthropic", "orchestrator", "socket"}
    text = SOURCE.read_text(encoding="utf-8")
    for call in ("write_text", "write_bytes", "open("):
        assert call not in text, call
