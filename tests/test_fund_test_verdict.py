"""The fund test's verdict in the nightly funds run (``shadow/run.py``; build section C).

The fund test decided nowhere before (the plan's section 1). Now each planned
look gets one record, made once on the night the race's look is readable and
frozen after it (owner readings 2 and 3), read at the fund test's own bar by
the spending rule of 11.7, decided by ``decision_gate.decide`` at that bar,
and shown as the plan's table (ii) or its SKIPPED block (v). The top-level
``verdict`` combines it with the race's (section 11.8, owner reading 1).

The owner's identity condition: calibration and every existing key of
``logs/funds.json`` and ``logs/race_gate.json`` stay exactly as they were;
the verdict only adds keys (``test_every_existing_key_is_as_the_code_before_wrote_it``).
"""

from __future__ import annotations

import json
import os
import statistics
import subprocess
import sys
from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from analysis import decision_gate as gate
from analysis import verdict as v
from config.market_calendar import is_trading_day
from shadow import run as shadow_run
from shadow import schedule
from shadow.fund import STARTING_CASH
from tests.test_exploratory import NoPrices, build_args

ROOT = Path(__file__).resolve().parent.parent


def fund_days(n: int, first: date = date(2026, 9, 29)) -> list[date]:
    out, day = [], first
    while len(out) < n:
        if is_trading_day(day):
            out.append(day)
        day += timedelta(days=1)
    return out


DAYS = fund_days(185)                   # 2026-09-29 ...; DAYS[59] = 2026-12-22, DAYS[119] = 2027-03-22
LOOK_DAYS = {1: DAYS[59], 2: DAYS[119], 3: DAYS[179]}


def noise(i: int) -> float:
    return 0.001 * ((i * 7) % 5 - 2)


def a_fund(name: str, returns) -> SimpleNamespace:
    equity, days = STARTING_CASH, []
    for day, r in zip(DAYS, returns):
        equity *= 1 + r
        days.append(SimpleNamespace(day=day, equity=equity))
    return SimpleNamespace(name=name, days=days)


def raw(n: int = 185, *, model=-0.002, momentum=0.004, hybrid=0.0, vt=0.0, coin=1000, coin_top=None) -> dict:
    """The fund test's materials as ``run_funds`` hands them over (``_fund_test``): the four funds and the
    coin-flip funds' raw equity. By default momentum clearly beats the model and the VT fund."""
    funds = {name: a_fund(name, [base + noise(i + k) for i in range(n)])
             for k, (name, base) in enumerate((("model", model), ("momentum", momentum), ("hybrid", hybrid),
                                               ("vt", vt)))}
    curves = [[STARTING_CASH * (1 + 0.00001 * s * (i + 1) / n) for i in range(n)] for s in range(coin)]
    if coin_top is not None:
        curves = [[STARTING_CASH * (1 + coin_top(s, i)) for i in range(n)] for s in range(coin)]
    return {"funds": funds, "coin": curves}


def days_text(n: int = 185) -> list[str]:
    return [d.isoformat() for d in DAYS[:n]]


def tax_record(look: int, end: date, t=None, status=gate.AFTER_TAX_READY) -> dict:
    t = t or {"model": -1.0, "momentum": 9.0, "hybrid": 0.5}
    if status != gate.AFTER_TAX_READY:
        return {"look": look, "made_on": end.isoformat(), "window_end": end.isoformat(), "lag": 5,
                "status": status, "reason": "calibration had not passed when the race reached this look",
                "tests": {}}
    return {"look": look, "made_on": end.isoformat(), "window_end": end.isoformat(), "lag": 5, "status": status,
            "reason": "", "tests": {arm: {"t": value, "from": "2026-09-29", "through": end.isoformat(), "lag": 5}
                                    for arm, value in t.items()}}


def record_at(look: int, sessions: int, records=(), material=None, after=None, dd=0.041, made_on=None):
    end = DAYS[sessions - 1]
    return shadow_run.fund_test_record(
        look, made_on or end, end, days_text(), material or raw(), after or {
            "status": gate.AFTER_TAX_READY, "t": {"model": -1.0, "momentum": 9.0, "hybrid": 0.5}},
        dd, list(records), "2026-10-19")


# --- the spending rule of 11.7, at the looks actually read ---------------------------------------------------


def test_sixty_sessions_give_the_planned_bar_and_sixty_one_a_lower_one():
    first = record_at(1, 60)
    assert (first["sessions"], first["share"], first["bar"], first["planned_bar"]) == (60, 60 / 180, 3.40, 3.40)
    assert first["bar_exact"] == 3.3948 and first["bar_differs"] is False
    late = record_at(1, 61)
    assert (late["sessions"], late["bar"], late["bar_differs"]) == (61, 3.37, True)
    assert late["sessions_calendar"] == 61


def test_a_bar_that_differs_from_the_plan_asks_for_an_amendment_in_the_table():
    late = record_at(1, 61)
    assert late["table"]["title"].endswith("Bar 3.37 (planned 3.40): log it in the Amendments table.")
    assert "bar t > 3.37 (by the spending rule of 11.7; planned 3.40)" in late["table"]["title"]


def test_a_skipped_first_look_spends_nothing():
    skipped = {"look": 1, "status": v.FUND_SKIPPED, "made_on": "2026-12-22", "window_end": "2026-12-22"}
    second = record_at(2, 120, records=[skipped])
    third = record_at(3, 180, records=[skipped, second])
    assert (second["bar"], second["bar_exact"], third["bar"]) == (2.41, 2.4005, 2.02)
    assert third["share"] == 1.0


def test_the_final_look_read_alone_is_at_one_point_nine_six():
    skipped = [{"look": k, "status": v.FUND_SKIPPED} for k in (1, 2)]
    assert record_at(3, 180, records=skipped)["bar"] == 1.96
    # The final look's share is 1 whatever the sessions say (11.7: it counts as 1).
    assert record_at(3, 170, records=skipped)["share"] == 1.0


def test_bars_already_used_stay_as_they_were():
    first = record_at(1, 61)
    second = record_at(2, 120, records=[first])
    exact = gate.spending_bars([61 / 180, 120 / 180], used=[3.37])
    assert exact[0] == 3.37 and second["bar_exact"] == round(exact[1], 4)
    assert second["bar"] == gate.rounded_bar(exact[1])
    assert first["bar"] == 3.37                                  # the record read back is not touched


def test_a_look_with_180_sessions_before_the_final_one_is_left_to_the_owner():
    owner = record_at(2, 180, records=[record_at(1, 60)])
    assert owner["status"] == v.FUND_OWNER and owner["reason"] == v.FUND_OWNER_REASON
    assert "bar" not in owner and "decision" not in owner
    assert owner["table"]["verdict"].startswith("THE OWNER DECIDES")


# --- the record: the tests, the coin flip, the after-tax record, the decision ---------------------------------


def test_a_read_record_has_every_field_and_is_cut_at_the_looks_close():
    record = record_at(1, 60)
    assert list(record) == ["look", "made_on", "window_end", "start", "status", "sessions", "sessions_calendar",
                            "share", "bar", "bar_exact", "planned_bar", "bar_differs", "calibration_passed_on",
                            "tests", "coin_flip", "after_tax", "downturn", "decision", "table"]
    assert set(record["tests"]) == {"model-momentum", "model-hybrid", "hybrid-momentum", "model-vt",
                                    "momentum-vt", "hybrid-vt"}
    for test in record["tests"].values():
        assert (test["days"], test["from"], test["through"], test["lag"]) == (60, "2026-09-29", "2026-12-22", 5)
        assert set(test) == {"days", "from", "through", "t", "mean_daily_diff", "lag"}
    funds = raw()["funds"]
    expected = shadow_run.paired(funds["model"], funds["momentum"], through=DAYS[59])["t"]
    assert record["tests"]["model-momentum"]["t"] == expected
    assert record["coin_flip"]["funds"] == 1000
    assert record["coin_flip"]["model_total"] == pytest.approx(
        [d.equity for d in funds["model"].days][59] / STARTING_CASH - 1)
    json.dumps(record, allow_nan=False)


def test_momentum_stops_the_model_early_and_the_table_says_so():
    record = record_at(1, 60)
    assert record["decision"]["candidate"] == "momentum" and record["decision"]["outcome"] == "momentum"
    table = v.table_from_json(record["table"])
    assert table.verdict == "EARLY STOP AT CHECKPOINT 1: REPLACE THE MODEL FUND WITH THE MOMENTUM FUND — NOT TESTED IN A DOWNTURN"
    assert table.status == v.DECIDED and table.outcome == "momentum"


def test_the_record_agrees_with_decide_on_its_own_inputs():
    """The equivalence on fund inputs: whatever the funds did, the record's decision is decide()'s at the
    record's bar, and its table adds up to the same thing."""
    cases = [dict(), dict(model=0.004, momentum=-0.002), dict(momentum=0.0005), dict(hybrid=0.006),
             dict(vt=0.01), dict(model=0.003, momentum=0.0, hybrid=0.0)]
    for material in cases:
        for look, sessions, before in ((1, 60, []), (3, 180, [{"look": 1, "status": "skipped"},
                                                             {"look": 2, "status": "skipped"}])):
            record = record_at(look, sessions, records=before, material=raw(**material))
            decided = gate.decide(v.fund_inputs(record), record["bar"], look == 3)
            assert (record["decision"]["candidate"], record["decision"]["outcome"]) == decided[:2], material
            table = v.table_from_json(record["table"])
            assert (table.outcome is not None) == (decided[1] is not None)
            assert (v.FUND_OUTCOME_TEXT[decided[1]].upper() in table.verdict) if decided[1] else True


def test_a_coin_flip_tie_fails():
    """Section 11.5: "above" the 95th percentile is strict. Every coin-flip fund ends exactly where the model
    fund does, so the model fund ties its 95th percentile and row 3 fails."""
    material = raw(model=0.004, momentum=-0.002, hybrid=-0.002)
    model = [d.equity for d in material["funds"]["model"].days]
    material["coin"] = [list(model) for _ in range(1000)]
    record = record_at(1, 60, material=material)
    assert record["coin_flip"]["model_total"] == record["coin_flip"]["p95_total"]
    table = v.table_from_json(record["table"])
    assert next(r for r in table.rows if r.n == "3").result == "FAIL"
    assert record["decision"]["candidate"] != "model"


def test_the_coin_flip_reads_the_raw_curves_not_the_band():
    material = raw()
    record = record_at(1, 60, material=material)
    totals = [c[59] / STARTING_CASH - 1 for c in material["coin"]]
    assert record["coin_flip"]["p95_total"] == shadow_run.percentile(totals, 95.0)


def test_the_record_refuses_a_date_outside_the_experiment():
    with pytest.raises(ValueError, match="outside the experiment"):
        shadow_run.fund_test_record(1, date(2099, 12, 22), DAYS[59], days_text(), raw(),
                                    {"status": "ready", "t": {}}, None, [], None)


# --- paired(..., through=) leaves the exploratory tests as they were -------------------------------------------


def _paired_before(fund, other) -> dict:
    """``shadow.run.paired`` as it was before ``through`` (commit ccdb477), for the byte-for-byte check."""
    from analysis.horse_race import newey_west_t
    from analysis.multiple_tests import p_two_sided, series_stats

    def by_day(f) -> dict:
        equity = [STARTING_CASH] + [round(d.equity, 2) for d in f.days]
        return {d.day: today / before - 1.0 for d, before, today in zip(f.days, equity, equity[1:])}

    mine, theirs = by_day(fund), by_day(other)
    days = sorted(set(mine) & set(theirs))
    diffs = [mine[d] - theirs[d] for d in days]
    t = newey_west_t(diffs, shadow_run.VS_MODEL_LAG)
    return {"compare_to": other.name, "days": len(diffs), "from": days[0].isoformat() if days else None,
            "mean_daily_diff": statistics.fmean(diffs) if diffs else None, "t": t, "p": p_two_sided(t),
            "stats": series_stats(diffs),
            "total_return": shadow_run.total_return(fund), "compare_total_return": shadow_run.total_return(other),
            "max_drawdown": shadow_run.max_drawdown([d.equity for d in fund.days]),
            "compare_max_drawdown": shadow_run.max_drawdown([d.equity for d in other.days])}


def test_paired_without_through_is_byte_for_byte_what_it_was():
    funds = raw()["funds"]
    for a, b in (("model", "momentum"), ("hybrid", "vt"), ("vt", "model")):
        dumped = json.dumps(shadow_run.paired(funds[a], funds[b]), allow_nan=False)
        assert dumped == json.dumps(_paired_before(funds[a], funds[b]), allow_nan=False)
    cut = shadow_run.paired(funds["model"], funds["momentum"], through=DAYS[59])
    assert cut["days"] == 60 and cut["through"] == "2026-12-22" and cut["from"] == "2026-09-29"
    assert "through" not in shadow_run.paired(funds["model"], funds["momentum"])


def test_handing_over_the_fund_tests_materials_changes_nothing_else_in_the_funds_run():
    """``run_funds(..., fund_test=True)`` adds only ``_fund_test`` (taken out by ``build``): every other part
    of the output is the same, on the golden journal and prices of ``tests/shadow_golden.py``."""
    from tests.shadow_golden import REFUSED, SESSIONS, golden_inputs
    from tests.test_shadow_variants import Walks

    entries, bars = golden_inputs()
    runs = [shadow_run.run_funds(entries, SESSIONS[0], SESSIONS[-1], Walks(bars), random_funds=3, processes=1,
                                 shortable_no=REFUSED, fund_test=flag) for flag in (False, True)]
    (plain, plain_checks), (handed, handed_checks) = runs
    materials = handed.pop("_fund_test")
    assert json.dumps(handed, sort_keys=True) == json.dumps(plain, sort_keys=True) and handed_checks == plain_checks
    assert set(materials["funds"]) == {"model", "momentum", "hybrid", "vt"} and len(materials["coin"]) == 3
    assert [round(c, 2) for c in materials["coin"][0]][:1] and len(materials["coin"][0]) == len(plain["days"])


# --- one night after another in build() ----------------------------------------------------------------------


NIGHT = datetime(2026, 12, 23, 23, 0, tzinfo=timezone.utc)


def gate_entry(end: date = LOOK_DAYS[1], readable=True, dd=0.041) -> dict:
    return {"independent": 20, "bar": 3.47, "reached": True, "outcome": None, "reason": "", "after_tax": "ready",
            "vt_max_drawdown": dd, "window_end": end.isoformat(), "readable": readable}


def race_gate(*looks, verdict=None, upcoming=None) -> dict:
    entries = list(looks) + [{"reached": False}] * (3 - len(looks))
    out = {"looks": entries, "next": upcoming}
    if verdict is not None:
        out["verdict"] = verdict
    return out


def night(monkeypatch, tmp_path, race, previous=None, *, passed=True, material=None, n=60, now=NIGHT):
    """``build`` with calibration ``passed`` or running and the funds' materials ``material`` (``n`` sessions)."""
    from shadow import calibration as calib

    monkeypatch.setattr(schedule, "CALIBRATION_START", date(2026, 9, 28))
    monkeypatch.setattr(calib, "calibration_report", lambda **kw: (
        {"status": "passed", "end_estimate": "2026-10-19"} if passed else {"status": "running"}))
    monkeypatch.setattr(shadow_run, "OhlcFetcher", NoPrices)
    stuff = material if material is not None else raw(n)

    def fake(entries, start, final_through, fetcher, **kw):
        return ({"start": start.isoformat(), "days": days_text(n), "band": {},
                 "list": [{"name": name, "exploratory": False} for name in ("model", "momentum", "hybrid", "vt")],
                 "_fund_test": stuff}, {"four": {}, "coin": {}})

    monkeypatch.setattr(shadow_run, "run_funds", fake if passed else (
        lambda *a, **k: pytest.fail("no fund before calibration")))
    return shadow_run.build(build_args(tmp_path, race, previous), now)


def with_tax(*records) -> dict:
    return {"after_tax": {"looks": list(records)}}


def test_a_look_read_on_its_night_is_frozen_after_it(monkeypatch, tmp_path):
    race = race_gate(gate_entry())
    first = night(monkeypatch, tmp_path, race, with_tax(tax_record(1, LOOK_DAYS[1])))
    (record,) = first["fund_test"]["looks"]
    assert record["status"] == "read" and record["made_on"] == "2026-12-23" and record["bar"] == 3.40
    assert record["calibration_passed_on"] == "2026-10-19"
    assert "_fund_test" not in first["funds"]
    assert first["fund_test"]["verdict"] == {"text": record["table"]["verdict"], "decided_at": 1,
                                             "outcome": "momentum"}
    # The night after, with the funds moved on: the record is carried unchanged, nothing recomputed.
    later = night(monkeypatch, tmp_path, race, first, material=raw(model=0.01, momentum=-0.01), n=61,
                  now=NIGHT + timedelta(days=1))
    assert later["fund_test"]["looks"] == [record]
    assert later["fund_test"]["verdict"] == first["fund_test"]["verdict"]
    json.dumps(later, allow_nan=False)


def test_a_record_cut_at_another_close_is_made_again_and_keeps_the_old_one(monkeypatch, tmp_path):
    """A bug fix moved look 1's window: the record is made again at the new close, once, the old one inside."""
    old = record_at(1, 59)
    race = race_gate(gate_entry(LOOK_DAYS[1]))
    previous = with_tax(tax_record(1, LOOK_DAYS[1])) | {"fund_test": {"looks": [old]}}
    out = night(monkeypatch, tmp_path, race, previous)
    (record,) = out["fund_test"]["looks"]
    assert record["window_end"] == "2026-12-22" and record["sessions"] == 60
    assert json.loads(json.dumps(record["superseded"])) == json.loads(json.dumps(old))
    later = night(monkeypatch, tmp_path, race, out, now=NIGHT + timedelta(days=1))
    assert later["fund_test"]["looks"] == out["fund_test"]["looks"]


def test_a_look_readable_before_calibration_passes_is_skipped_for_good(monkeypatch, tmp_path):
    race = race_gate(gate_entry())
    out = night(monkeypatch, tmp_path, race, passed=False)
    (record,) = out["fund_test"]["looks"]
    assert {k: record[k] for k in ("look", "status", "reason", "window_end")} == {
        "look": 1, "status": "skipped", "window_end": "2026-12-22",
        "reason": "calibration had not passed on the night the race's look was readable"}
    assert "bar" not in record
    assert record["table"]["title"] == "Fund test, checkpoint 1 of 3: SKIPPED."
    assert record["table"]["verdict"].endswith("(planned: checkpoint 2 at 2.41, checkpoint 3 at 2.02).")
    # The same night the race's after-tax record is unavailable: the two agree (owner reading 3).
    assert out["after_tax"]["looks"][0]["status"] == gate.AFTER_TAX_UNAVAILABLE
    assert out["fund_test"]["next_checkpoint"] == {"look": 2, "estimated": "2027-03-22", "bar": 2.41,
                                                   "planned_bar": 2.41}
    # Calibration passes later: the skipped look stays skipped, even on a moved window.
    later = night(monkeypatch, tmp_path, race_gate(gate_entry(LOOK_DAYS[1] + timedelta(days=1))), out,
                  now=NIGHT + timedelta(days=2))
    assert later["fund_test"]["looks"] == [record]


def test_a_look_waits_for_the_after_tax_record_and_for_the_funds_to_reach_its_close(monkeypatch, tmp_path):
    race = race_gate(gate_entry())
    no_tax = night(monkeypatch, tmp_path, race)                       # no rate table: no after-tax record
    assert no_tax["fund_test"]["looks"] == [] and no_tax["fund_test"]["note"] is None
    short = night(monkeypatch, tmp_path, race, with_tax(tax_record(1, LOOK_DAYS[1])), n=59)
    assert short["fund_test"]["looks"] == []                         # the funds end the day before the close
    elsewhere = night(monkeypatch, tmp_path, race, with_tax(tax_record(1, DAYS[58])))
    assert elsewhere["fund_test"]["looks"] == []                     # a record cut at another close does not count
    unreadable = night(monkeypatch, tmp_path, race_gate(gate_entry(readable=False)),
                       with_tax(tax_record(1, LOOK_DAYS[1])))
    assert unreadable["fund_test"]["looks"] == []


def test_an_unavailable_after_tax_record_lets_the_look_be_read_with_row_8_unable_to_pass(monkeypatch, tmp_path):
    out = night(monkeypatch, tmp_path, race_gate(gate_entry()),
                with_tax(tax_record(1, DAYS[40], status=gate.AFTER_TAX_UNAVAILABLE)))
    (record,) = out["fund_test"]["looks"]
    assert record["after_tax"]["status"] == gate.AFTER_TAX_UNAVAILABLE
    row8 = next(r for r in record["table"]["rows"] if r["n"] == "8")
    assert row8["result"] == v.CANNOT_PASS and record["decision"]["outcome"] is None


def test_fewer_than_a_thousand_coin_flip_funds_make_no_record_and_say_why(monkeypatch, tmp_path):
    out = night(monkeypatch, tmp_path, race_gate(gate_entry()), with_tax(tax_record(1, LOOK_DAYS[1])),
                material=raw(coin=999))
    assert out["fund_test"]["looks"] == []
    assert out["fund_test"]["note"] == ("checkpoint 1: this run had 999 coin-flip funds, not the registered "
                                        "1,000 (sections 11.1 and 11.5), so no fund-test record was made")


def test_a_later_look_waits_for_an_earlier_one(monkeypatch, tmp_path):
    race = race_gate(gate_entry(readable=False), gate_entry(LOOK_DAYS[2]))
    out = night(monkeypatch, tmp_path, race, with_tax(tax_record(2, LOOK_DAYS[2])), n=120)
    assert out["fund_test"]["looks"] == []


def test_after_the_deciding_look_a_later_one_is_recorded_for_reading_only(monkeypatch, tmp_path):
    first = night(monkeypatch, tmp_path, race_gate(gate_entry()), with_tax(tax_record(1, LOOK_DAYS[1])))
    race = race_gate(gate_entry(), gate_entry(LOOK_DAYS[2]))
    previous = first | with_tax(tax_record(1, LOOK_DAYS[1]), tax_record(2, LOOK_DAYS[2]))
    later = night(monkeypatch, tmp_path, race, previous, n=120, now=datetime(2027, 3, 23, 23, tzinfo=timezone.utc))
    one, two = later["fund_test"]["looks"]
    assert one == first["fund_test"]["looks"][0]
    assert two["table"]["verdict"] == "FOR READING ONLY"
    assert two["table"]["title"].endswith("For reading only: the fund test was decided at checkpoint 1.")
    assert later["fund_test"]["verdict"]["decided_at"] == 1


def test_the_fund_test_block_and_the_document_end_with_the_new_keys(monkeypatch, tmp_path):
    out = night(monkeypatch, tmp_path, race_gate())
    block = out["fund_test"]
    assert list(block)[:7] == ["status", "start", "sessions", "independent", "next_checkpoint", "first_cycle",
                               "waiting_for"]
    assert list(block)[7:] == ["planned_sessions", "looks", "verdict", "note"]
    assert block["planned_sessions"] == 180
    assert block["next_checkpoint"] == {"look": 1, "estimated": "2026-12-22", "bar": 3.40, "planned_bar": 3.40}
    assert block["verdict"] == {"text": "no decision yet", "decided_at": None, "outcome": None}
    assert list(out)[-2:] == ["after_tax", "verdict"]
    assert out["verdict"] == {"text": "no decision yet"}


def test_a_damaged_record_from_last_night_is_made_again(monkeypatch, tmp_path):
    previous = with_tax(tax_record(1, LOOK_DAYS[1])) | {"fund_test": {"looks": [
        {"look": 1, "status": "read"}, "junk", {"look": 7, "status": "skipped"}]}}
    out = night(monkeypatch, tmp_path, race_gate(gate_entry()), previous)
    (record,) = out["fund_test"]["looks"]
    assert record["status"] == "read" and "superseded" not in record


# --- the combined line, from tonight's race gate and the fund test's records ----------------------------------


def race_verdict(decided_at, outcome, final_complete=False) -> dict:
    looks = [{"look": decided_at, "table": {"outcome": outcome, "complete": True}}] if decided_at else []
    if final_complete and decided_at != 3:
        looks.append({"look": 3, "table": {"outcome": None, "complete": True}})
    return {"text": "x", "decided_at": decided_at, "looks": looks}


def fund_records(*items) -> list[dict]:
    """``(look, status, outcome)`` for each record."""
    return [{"look": k, "status": status, "window_end": LOOK_DAYS[k].isoformat(),
             **({"share": k / 3, "bar": schedule.FUND_TEST_BARS[k - 1]} if status == "read" else {}),
             "table": {"status": v.DECIDED if outcome else v.NO_DECISION, "verdict": "x", "outcome": outcome}}
            for k, status, outcome in items]


@pytest.mark.parametrize("race, records, text", [
    (race_verdict(1, "none"), fund_records((1, "read", "momentum")),
     'HOLD THE INDEX — the race decided "no arm trades" (11.8)'),
    (race_verdict(1, "momentum"), fund_records((1, "read", "none")),
     'HOLD THE INDEX — the fund test decided "no arm trades" (11.8)'),
    (race_verdict(1, "momentum"), fund_records((1, "read", "hybrid")),
     "HOLD THE INDEX — the race picked momentum, the fund test picked the hybrid (11.8)"),
    (race_verdict(1, "momentum"), fund_records((1, "read", None), (2, "read", "momentum")),
     "MOMENTUM WINS BOTH — no real money before the June 2027 verdict (section 9); after it, real money for "
     "momentum, starting small if NOT TESTED IN A DOWNTURN"),
    (race_verdict(None, None), fund_records((1, "read", "momentum")), "NO DECISION YET — waiting for the race"),
    (race_verdict(1, "momentum"), fund_records((1, "read", None)), "NO DECISION YET — waiting for the fund test"),
    (race_verdict(3, "momentum", final_complete=True),
     fund_records((1, "skipped", None), (2, "skipped", None), (3, "skipped", None)),
     "HOLD THE INDEX — the fund test could not be read (calibration never passed)"),
], ids=["race no arm", "fund no arm", "different arms", "same arm at different looks", "race not decided",
        "fund not decided", "fund skipped at every look"])
def test_the_combined_line_in_every_row_of_the_table(race, records, text):
    gate_record = race_gate(gate_entry(), gate_entry(LOOK_DAYS[2]), gate_entry(LOOK_DAYS[3]), verdict=race)
    out = shadow_run.combined_verdict(gate_record, records, shadow_run.fund_test_verdict(records),
                                      shadow_run.fund_test_next(records))
    assert out["text"] == text
    assert out["note"] == "No real money before the June 2027 verdict (section 9)."


def test_the_combined_line_before_any_look_and_with_an_older_race_gate():
    assert shadow_run.combined_verdict(race_gate(), [], shadow_run.fund_test_verdict([]),
                                       shadow_run.fund_test_next([])) == {"text": "no decision yet"}
    assert shadow_run.combined_verdict(None, [], shadow_run.fund_test_verdict([]), None) == {"text": "no decision yet"}
    # A race gate written before the verdict existed (no "verdict" key): the race has not decided.
    out = shadow_run.combined_verdict(race_gate(gate_entry()), fund_records((1, "read", "momentum")),
                                      {"decided_at": 1, "outcome": "momentum"}, None)
    assert out["text"] == "NO DECISION YET — waiting for the race"
    # The race's estimate of its next look, if outside the experiment, is not printed (and not refused).
    late = race_gate(gate_entry(), upcoming={"independent": 40, "estimated": "2028-02-01"})
    out = shadow_run.combined_verdict(late, [], shadow_run.fund_test_verdict([]), None)
    assert out["line"].endswith("combined: NO DECISION YET — waiting for the race.")


def test_the_fund_tests_next_look_and_bar_follow_the_looks_read():
    assert shadow_run.fund_test_next([]) == {"look": 1, "estimated": "2026-12-22", "bar": 3.40, "planned_bar": 3.40}
    late = record_at(1, 61)
    assert shadow_run.fund_test_next([late])["bar"] == gate.rounded_bar(
        gate.spending_bars([61 / 180, 120 / 180], used=[3.37])[1])
    three = [{"look": k, "status": "skipped"} for k in (1, 2, 3)]
    assert shadow_run.fund_test_next(three) is None


# --- guards of the owner's Addition 2 for the funds run ----------------------------------------------------------


def test_the_funds_run_writes_its_tables_only_through_table_json(monkeypatch, tmp_path):
    """Guard 2: a test-data table reaching the funds run's record is refused, not written."""
    real = v.fund_test_table
    monkeypatch.setattr(v, "fund_test_table", lambda *a, **k: replace(real(*a, **k), test_data=True))
    with pytest.raises(ValueError, match="TEST DATA"):
        night(monkeypatch, tmp_path, race_gate(gate_entry()), with_tax(tax_record(1, LOOK_DAYS[1])))
    with pytest.raises(ValueError, match="TEST DATA"):
        night(monkeypatch, tmp_path, race_gate(gate_entry()), passed=False)


# --- the owner's identity condition: nothing that was there moves -----------------------------------------------


def test_every_existing_key_is_as_the_code_before_wrote_it():
    """``tests/verdict_identity.py``: the funds document (calibration running, on the night look 1 is
    readable and the night after; calibration passed with the real funds) and the race gate (no look, a
    decided look, a waiting look, a final look), with the verdict's new keys removed, hash part for part
    exactly as the code before the verdict wrote them (``tests/verdict_identity_before.json``, recorded at
    commit ccdb477). Run in a fresh interpreter with a fixed hash seed, as they were recorded."""
    before = json.loads((ROOT / "tests" / "verdict_identity_before.json").read_text())
    done = subprocess.run([sys.executable, "-m", "tests.verdict_identity"], cwd=ROOT, capture_output=True,
                          text=True, timeout=600, env={**os.environ, "PYTHONHASHSEED": "0"}, check=True)
    after = json.loads(done.stdout.strip().splitlines()[-1])
    assert set(after) == set(before)
    assert [k for k in sorted(before) if after[k] != before[k]] == []


def test_the_identity_check_sees_the_new_keys_it_removes():
    """The check above is not empty: the documents it reads do carry the verdict, and the one existing key
    the verdict fills (``fund_test.next_checkpoint``, null before) is the only one it puts back."""
    from tests import verdict_identity as identity

    funds = identity.funds_documents()
    running = funds["running_1"]
    assert running["fund_test"]["looks"][0]["status"] == "skipped"
    assert running["verdict"]["text"] == "NO DECISION YET — waiting for the race"
    assert running["fund_test"]["next_checkpoint"]["look"] == 2
    stripped = identity.without_new_keys(running, "funds")
    assert stripped["fund_test"]["next_checkpoint"] is None and "verdict" not in stripped
    gates = identity.gate_documents()
    assert gates["crafted"]["verdict"]["decided_at"] == 1 and list(gates["crafted"])[-1] == "verdict"
