"""The thesis-check logger in the funds program: nothing before 2027-04-01, then a description only.

Pre-registration section 13.12 (the owner's instruction of 4 Oct 2026,
item 2). This file pins the read side: the logger's line format as the
runner writes it, the counters (whole numbers, from the start only), and
the checkpoint description -- the forward return after each verdict,
signed by the side the position was opened on, over 5 sessions, BROKEN
minus VALID with a Welch t for reading -- and that none of it is in the
Benjamini-Hochberg family or in the funds document before its date.

Offline throughout: made-up lines and prices.
"""

from __future__ import annotations

import json
import statistics
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

from analysis import thesis as thesis_check
from config import thesis_check as tc
from shadow import exploratory as xp
from shadow import run as shadow_run
from tests.test_exploratory import build_args, passed_calibration

#: The night before the logger's start, and its first night (23:00 UTC).
THE_NIGHT_BEFORE = datetime(2027, 3, 31, 23, 0, tzinfo=timezone.utc)
THE_FIRST_NIGHT = datetime(2027, 4, 1, 23, 0, tzinfo=timezone.utc)

LOOK_TWO = {"looks": [{"reached": True}, {"reached": True}, {"reached": False}]}
ALL_LOOKS = {"looks": [{"reached": True}] * 3}

APR1 = date(2027, 4, 1)


def check_json(ticker: str, day: date, verdict: str | None = "VALID", side: str | None = "long", *,
               error: str | None = None, hour: int = 20) -> str:
    """One logger line in the runner's format (scratchpad spec, Part A3)."""
    at = datetime(day.year, day.month, day.day, hour, 0, tzinfo=timezone.utc)
    return json.dumps({
        "ts_utc": at.isoformat(), "event": tc.EVENT, "week": thesis_check.week_of(day), "ticker": ticker,
        "side": side, "entry": {"ts": "2027-03-20T14:00:00+00:00", "rationale": "Momentum and a clean balance sheet.",
                                "key_factors": ["trend"], "bias": "BULLISH" if side == "long" else "BEARISH"},
        "headline_count": 3, "verdict": None if error else verdict,
        "reason": None if error else "The trend still holds.", "asks": 0 if error else 1,
        "cost_usd": 0.0 if error else 0.0026, "model_setup": {}, "reasoning_effort": "high", "error": error,
    })


def write_checks(directory: Path, lines: list[str]) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "2027-04.log").write_text("\n".join(lines) + "\n")
    return directory


# --------------------------------------------------------------------------- #
# The line format
# --------------------------------------------------------------------------- #


def test_a_line_is_read_as_the_runner_writes_it():
    (check,) = thesis_check.read_lines([check_json("XLE", APR1, "BROKEN", "short")])
    assert (check.ticker, check.day, check.week, check.side, check.verdict) == ("XLE", APR1, "2027-W13", "short",
                                                                               "BROKEN")
    assert check.ok and check.sign == -1 and check.asks == 1 and check.cost_usd == pytest.approx(0.0026)


def test_an_error_line_or_an_unknown_verdict_is_a_failed_check_and_junk_is_skipped():
    lines = [check_json("XLE", APR1, error="no entry record for this name"),
             check_json("GLD", APR1, "MAYBE"),
             "not json", json.dumps({"event": "model_vote", "ticker": "XLE"}),
             json.dumps({"event": tc.EVENT, "ticker": "TLT"})]                         # no time: not a line
    first, second = thesis_check.read_lines(lines)
    assert not first.ok and first.error == "no entry record for this name"
    assert not second.ok and second.verdict == "MAYBE"


def test_a_long_reason_is_cut_to_one_sentence_s_length():
    payload = json.loads(check_json("XLE", APR1))
    payload["reason"] = "x" * 1000
    (check,) = thesis_check.read_lines([json.dumps(payload)])
    assert len(check.reason) == tc.REASON_MAX_CHARS


# --------------------------------------------------------------------------- #
# When anything may be computed
# --------------------------------------------------------------------------- #


def test_the_gates_open_on_the_start_and_never_before():
    assert tc.START == date(2027, 4, 1)
    assert not thesis_check.active(date(2027, 3, 31)) and thesis_check.active(APR1)
    assert not thesis_check.due(True, date(2027, 3, 31)) and thesis_check.due(True, APR1)
    assert not thesis_check.due(False, APR1)


def test_the_counters_are_whole_numbers_from_the_start_only():
    lines = thesis_check.read_lines([
        check_json("XLE", date(2027, 3, 30)),                                     # before START: never counted
        check_json("XLE", APR1, "VALID"),
        check_json("XLE", APR1, "VALID", hour=21),                                # the same name and week: once
        check_json("GLD", APR1, error=thesis_check.NO_ENTRY),
        check_json("SLV", APR1, error="model call failed: timeout"),
        check_json("TLT", date(2027, 4, 6), "BROKEN", "short"),
        check_json("XHB", date(2027, 4, 6), error=thesis_check.NOT_ASKED_CAP),
    ])
    counts = thesis_check.counters(lines, date(2027, 4, 9))
    assert counts == {"checks": 2, "names": 2, "weeks": 2, "failed": 1, "no_entry": 1, "not_asked": 1}
    assert set(counts) == set(thesis_check.COUNTER_KEYS) and all(type(v) is int for v in counts.values())
    assert thesis_check.counters(lines, date(2027, 4, 5)) == {"checks": 1, "names": 1, "weeks": 1, "failed": 1,
                                                              "no_entry": 1, "not_asked": 0}


def test_a_document_before_the_start_has_no_key_of_the_thesis_check(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    monkeypatch.setattr(shadow_run, "thesis_lines_in", lambda path: pytest.fail("the checks read early"))
    args = build_args(tmp_path, LOOK_TWO)
    args.thesis = write_checks(tmp_path / "thesis_check", [check_json("XLE", APR1)])
    out = shadow_run.build(args, THE_NIGHT_BEFORE)
    assert tc.EVENT not in out["exploratory"]["counters"]
    (record,) = out["exploratory"]["checkpoints"]
    assert tc.EVENT not in record and tc.EVENT not in record["counters"]
    assert "thesis" not in json.dumps(out)


def test_from_the_start_the_counters_and_a_looks_description_are_there(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    args = build_args(tmp_path, LOOK_TWO)
    args.thesis = write_checks(tmp_path / "thesis_check", [check_json("XLE", APR1, "BROKEN")])
    out = shadow_run.build(args, THE_FIRST_NIGHT)
    assert out["exploratory"]["counters"][tc.EVENT] == {"checks": 1, "names": 1, "weeks": 1, "failed": 0,
                                                         "no_entry": 0, "not_asked": 0}
    (record,) = out["exploratory"]["checkpoints"]
    block = record[tc.EVENT]
    assert block["descriptive"] is True and block["in_family"] is False and block["checks"] == 1
    assert block["no_price"] == 1 and block["not_tested"] is False      # no price in this test; not the final look
    # Not in the family: the table has no row for it.
    assert not any("thesis" in r["name"] for r in record["table"]["rows"])
    json.dumps(out, allow_nan=False)


def test_without_a_path_there_are_no_checks():
    assert shadow_run.thesis_lines_in(None) == []
    assert shadow_run.build_parser().parse_args([]).thesis is None


# --------------------------------------------------------------------------- #
# The checkpoint description
# --------------------------------------------------------------------------- #


def tape(day: date, opens_closes: list[tuple[float, float]]) -> list[tuple]:
    """Bars for the sessions after ``day``: (date, open, close)."""
    return [(d, o, c) for d, (o, c) in zip(xp.sessions_after(day, len(opens_closes)), opens_closes)]


def test_the_forward_return_is_next_open_to_the_fifth_close_signed_by_the_side():
    day = APR1
    rising = tape(day, [(100.0, 101.0), (101.0, 102.0), (102.0, 103.0), (103.0, 104.0), (104.0, 110.0),
                        (110.0, 200.0)])                                          # the 6th session is never read
    bars = {"XLE": rising, "GLD": rising}
    lines = thesis_check.read_lines([check_json("XLE", day, "VALID", "long"),
                                     check_json("GLD", day, "BROKEN", "short")])
    out = thesis_check.checkpoint(lines, bars, rising[-1][0])
    assert out["horizon"] == tc.FORWARD_SESSIONS == 5
    assert out["verdicts"]["VALID"]["mean"] == pytest.approx(110.0 / 100.0 - 1.0)
    assert out["verdicts"]["BROKEN"]["mean"] == pytest.approx(-(110.0 / 100.0 - 1.0))     # a short: -1
    assert out["verdicts"]["BROKEN"]["hit_rate"] == 0.0 and out["verdicts"]["VALID"]["hit_rate"] == 1.0
    # Bars to ``through`` only: on the 4th session the return is still pending.
    early = thesis_check.checkpoint(lines, bars, rising[3][0])
    assert early["pending"] == 2 and early["verdicts"]["VALID"]["n"] == 0


def test_broken_minus_valid_is_a_difference_of_means_with_a_welch_t_for_reading_only():
    day = APR1
    moves = {"A": 1.02, "B": 1.05, "C": 0.99, "D": 0.97, "E": 0.95, "F": 1.01}
    verdicts = {"A": "VALID", "B": "VALID", "C": "VALID", "D": "BROKEN", "E": "BROKEN", "F": "WEAKENED"}
    bars = {t: tape(day, [(100.0, 100.0)] * 4 + [(100.0, 100.0 * m)]) for t, m in moves.items()}
    lines = thesis_check.read_lines([check_json(t, day, verdicts[t]) for t in moves])
    out = thesis_check.checkpoint(lines, bars, date(2027, 4, 30))
    valid, broken = [0.02, 0.05, -0.01], [-0.03, -0.05]
    assert out["verdicts"]["WEAKENED"]["n"] == 1
    diff = out["broken_minus_valid"]
    assert diff["mean_diff"] == pytest.approx(statistics.fmean(broken) - statistics.fmean(valid))
    se = (statistics.variance(broken) / 2 + statistics.variance(valid) / 3) ** 0.5
    assert diff["welch_t"] == pytest.approx((statistics.fmean(broken) - statistics.fmean(valid)) / se)
    assert diff["note"] == "for reading only: checks on the same day are not independent"
    # A description: no t and no stats a table could read, in no family.
    assert out["descriptive"] is True and out["in_family"] is False and "t" not in out and "stats" not in out
    assert not any(row[1] == tc.EVENT or "thesis" in row[0] for row in shadow_run.FAMILY)


def test_only_checks_with_a_verdict_from_the_start_count_once_per_name_and_week():
    day = APR1
    bars = {"XLE": tape(date(2027, 3, 25), [(100.0, 101.0)] * 12)}
    lines = thesis_check.read_lines([
        check_json("XLE", date(2027, 3, 26), "BROKEN"),                          # before START
        check_json("XLE", day, error="the model gave no answer"),
        check_json("XLE", day, "VALID", hour=21),
        check_json("XLE", day, "BROKEN", hour=22),                               # a copy in the same week
        check_json("XLE", day, "VALID", side=None, hour=23)])
    out = thesis_check.checkpoint(lines, bars, date(2027, 4, 30))
    assert out["checks"] == 1 and out["verdicts"]["VALID"]["n"] == 1 and out["verdicts"]["BROKEN"]["n"] == 0


def test_too_few_broken_checks_at_the_final_look_are_not_tested():
    day = APR1
    bars = {t: tape(day, [(100.0, 101.0)] * 5) for t in ("A", "B")}
    lines = thesis_check.read_lines([check_json("A", day, "BROKEN"), check_json("B", day, "VALID")])
    assert thesis_check.checkpoint(lines, bars, date(2027, 4, 30))["not_tested"] is False
    final = thesis_check.checkpoint(lines, bars, date(2027, 4, 30), final=True)
    assert final["not_tested"] is True and final["broken"] == 1 and final["min_broken"] == tc.MIN_BROKEN == 20
    assert thesis_check.checkpoint([], {}, date(2027, 4, 30))["no_data"] is True


def test_the_final_look_is_passed_through_and_prices_come_through_a_fetcher_of_its_own(monkeypatch, tmp_path):
    seen = {}
    real = shadow_run.thesis_record

    def spy(lines, final_through, fetchers, final):
        seen["final"] = final
        return real(lines, final_through, fetchers, final)

    calls = []
    passed_calibration(monkeypatch, calls)
    monkeypatch.setattr(shadow_run, "thesis_record", spy)
    args = build_args(tmp_path, ALL_LOOKS)
    args.thesis = write_checks(tmp_path / "thesis_check", [check_json("XLE", APR1, "BROKEN")])
    used: list = []
    out = shadow_run.build(args, THE_FIRST_NIGHT, used)
    assert seen["final"] is True and "ohlc_thesis" in [name for name, _ in used]
    (record,) = out["exploratory"]["checkpoints"]
    assert record["look"] == shadow_run.FINAL_LOOK and record[tc.EVENT]["not_tested"] is True


def test_the_read_side_writes_nothing_asks_nothing_and_never_names_the_model_call_capture():
    import ast

    source = (Path(__file__).resolve().parents[1] / "analysis" / "thesis.py").read_text()
    tree = ast.parse(source)
    imported = {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
    imported |= {n.module or "" for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
    assert not any(m.split(".")[0] in ("orchestrator", "store", "app", "shadow") for m in imported), imported
    calls = {getattr(n.func, "attr", getattr(n.func, "id", "")) for n in ast.walk(tree) if isinstance(n, ast.Call)}
    assert not calls & {"open", "write_text", "write_bytes", "now", "today", "utcnow"}
    code = source.split('"""', 2)[2]                                     # the module's prose may name it
    assert "logs/model_io" not in code and "MODEL_IO_DIR" not in code
    assert thesis_check.read_checks(Path("/nonexistent/thesis_check")) == []
