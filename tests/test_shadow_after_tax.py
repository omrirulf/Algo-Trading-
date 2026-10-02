"""The books after Israeli tax and in shekels (pre-registration sections 5c and 11.9)."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date, datetime, timezone

import pandas as pd
import pytest

from analysis import decision_gate as gate
from analysis.israel_tax import BUY, CHARGE, DIVIDEND, SELL, AfterTaxSeries, Event
from shadow import after_tax as tax
from shadow.broker import DIVIDEND as FILL_DIVIDEND
from shadow.broker import ENTRY, STOP, TRANCHE, Fill
from shadow.calibration import AccountFill, load_snapshots
from shadow.exploratory import TimingFund
from shadow.fund import Day, IndexFund
from shadow.market import Bars

D = [date(2026, 9, 29), date(2026, 9, 30), date(2026, 10, 1), date(2026, 10, 2)]


def frame(rows: dict[date, tuple[float, float, float, float, float]]) -> pd.DataFrame:
    index = pd.DatetimeIndex([pd.Timestamp(d) for d in rows])
    values = list(rows.values())
    return pd.DataFrame({"Open": [v[0] for v in values], "High": [v[1] for v in values], "Low": [v[2] for v in values],
                         "Close": [v[3] for v in values], "Dividends": [v[4] for v in values]}, index=index)


@dataclass
class _Broker:
    fills: list = field(default_factory=list)


@dataclass
class _Fund:
    name: str
    bars: Bars
    broker: _Broker
    days: list


def test_a_funds_fills_become_purchases_sales_dividends_and_charges():
    fills = [Fill(D[0], "AAA", ENTRY, "buy", 10, 100.0, 1.0), Fill(D[0], "BBB", ENTRY, "sell", 5, 50.0, 0.25),
             Fill(D[1], "AAA", FILL_DIVIDEND, "buy", 10, 0.5, 0.0), Fill(D[1], "BBB", FILL_DIVIDEND, "sell", 5, 0.2, 0.0),
             Fill(D[2], "AAA", TRANCHE, "sell", 3, 110.0, 0.33), Fill(D[3], "BBB", STOP, "buy", 5, 52.0, 0.26)]
    events = tax.fund_events(_Fund("model", Bars({}), _Broker(fills), []))
    assert events[D[0]] == [Event(BUY, "AAA", 10, 100.0, 1.0), Event(SELL, "BBB", 5, 50.0, 0.25)]
    assert events[D[1]] == [Event(DIVIDEND, "AAA", 10, 0.5), Event(CHARGE, "BBB", 5, 0.2)]
    assert events[D[2]] == [Event(SELL, "AAA", 3, 110.0, 0.33)] and events[D[3]] == [Event(BUY, "BBB", 5, 52.0, 0.26)]


def test_the_vt_fund_is_one_purchase_and_its_dividends():
    bars = Bars({"VT": frame({D[0]: (100, 101, 99, 100, 0), D[1]: (100, 101, 99, 101, 0.5),
                              D[2]: (101, 102, 100, 102, 0), D[3]: (102, 103, 101, 103, 0)})})
    vt = IndexFund("vt", "VT", bars)
    for d in D:
        vt.session(d)
    events = tax.fund_events(vt)
    [bought] = events[D[0]]
    assert bought.kind == BUY and bought.qty == vt.qty and bought.price_usd == 100
    assert bought.fee_usd == pytest.approx(vt.qty * 100 * 0.001)
    assert events[D[1]] == [Event(DIVIDEND, "VT", vt.qty, 0.5)] and D[2] not in events


def test_b_records_its_legs_and_dividends_for_the_tax_view():
    fund = TimingFund("vt_timing", Bars({}), D[-1])
    fund.trades = [(D[1], "VT", "buy", 10, 100.0, 1.0), (D[3], "VT", "sell", 10, 104.0, 1.04)]
    fund.dividends = [(D[3], "VT", 10, 0.5)]
    events = tax.fund_events(fund)
    assert events[D[1]] == [Event(BUY, "VT", 10, 100.0, 1.0)]
    assert events[D[3]] == [Event(DIVIDEND, "VT", 10, 0.5), Event(SELL, "VT", 10, 104.0, 1.04)]


def test_a_fund_series_is_taxed_if_sold_and_paired_with_the_vt_fund():
    bars = Bars({"AAA": frame({D[0]: (100, 101, 99, 100, 0), D[1]: (100, 121, 99, 120, 0),
                               D[2]: (120, 121, 119, 120, 0), D[3]: (120, 121, 119, 120, 0)})})
    fills = [Fill(D[0], "AAA", ENTRY, "buy", 100, 100.0, 0.0)]
    days = [Day(D[0], 100_000.0, 90_000.0, 10_000.0, 1), Day(D[1], 102_000.0, 90_000.0, 12_000.0, 1),
            Day(D[2], 102_000.0, 90_000.0, 12_000.0, 1), Day(D[3], 102_000.0, 90_000.0, 12_000.0, 1)]
    fund = _Fund("model", bars, _Broker(fills), days)
    series = tax.fund_series(fund, bars, lambda d: 3.5)
    assert series.days[0].after_tax_usd == pytest.approx(100_000)
    assert series.days[1].if_sold_tax_ils == pytest.approx(0.25 * 2_000 * 3.5)
    assert series.days[1].after_tax_usd == pytest.approx(102_000 - 500)
    view = tax.view(series)
    assert view["usd"]["return"] == pytest.approx(0.02) and view["usd"]["after_tax_return"] == pytest.approx(0.015)
    assert view["ils"]["from_usd_ils"] == pytest.approx(0.0) and view["tax_ils"]["if_sold_today"] == pytest.approx(1750)
    flat = _Fund("vt", bars, _Broker([]), [Day(d, 100_000.0, 100_000.0, 0.0, 0) for d in D])
    test = tax.paired(series, tax.fund_series(flat, bars, lambda d: 3.5), through=D[2])
    assert test["days"] == 3 and test["through"] == D[2].isoformat() and test["lag"] == gate.AFTER_TAX_LAG


def test_the_shekel_view_says_what_the_dollar_s_move_did():
    bars = Bars({})
    fund = _Fund("vt", bars, _Broker([]), [Day(D[0], 100_000.0, 0, 0, 0), Day(D[1], 102_000.0, 0, 0, 0)])
    series = tax.fund_series(fund, bars, {D[0]: 3.5, D[1]: 3.395}.__getitem__)    # the dollar fell 3%
    view = tax.view(series)
    assert view["usd"]["return"] == pytest.approx(0.02)
    assert view["ils"]["return"] == pytest.approx(1.02 * 0.97 - 1)
    assert view["ils"]["from_usd_ils"] == pytest.approx(1.02 * 0.97 - 1 - 0.02)
    assert view["usd_ils"]["change"] == pytest.approx(-0.03)


def _snapshot_lines() -> list[str]:
    fills = [{"id": "1", "order_id": "a", "ticker": "AAA", "side": "buy", "qty": 10.0, "price": 100.0,
              "at": "2026-09-16T15:00:00Z"},
             {"id": "2", "order_id": "b", "ticker": "BBB", "side": "sell_short", "qty": 5.0, "price": 50.0,
              "at": "2026-09-17T15:00:00Z"},
             {"id": "3", "order_id": "c", "ticker": "AAA", "side": "sell", "qty": 4.0, "price": 110.0,
              "at": "2026-09-18T15:00:00Z"}]
    first = {"at": "2026-09-18T21:00:00Z", "mode": "cycle", "account": {"equity": 100_100.0, "cash": 99_000.0},
             "positions": [{"ticker": "AAA", "qty": 6.0, "avg_entry_price": 100.0},
                           {"ticker": "BBB", "qty": -5.0, "avg_entry_price": 50.0}],
             "stops": [], "fills": fills,
             "history": {"days": ["2026-09-09", "2026-09-10", "2026-09-16", "2026-09-17", "2026-09-18"],
                         "equity": [0.0, 100_000.0, 100_000.0, 100_050.0, 100_100.0]}}
    again = dict(first, at="2026-09-18T22:00:00Z", fills=fills[2:])           # an overlapping window
    return [json.dumps(first), json.dumps(again)]


def test_the_paper_account_is_rebuilt_from_its_fills_once_each():
    snapshots = load_snapshots(_snapshot_lines())
    bars = Bars({"AAA": frame({date(2026, 9, d): (100, 101, 99, 100 + d - 16, 0) for d in (16, 17, 18)}),
                 "BBB": frame({date(2026, 9, d): (50, 51, 49, 50, 0) for d in (16, 17, 18)})})
    series = tax.account_series(snapshots, bars, lambda d: 3.5, date(2026, 9, 18))
    assert [d.day for d in series.days][0] == tax.FX_TABLE_START            # the first funded close
    assert series.start_equity_usd == 100_000.0
    last = series.days[-1]
    assert last.realised_tax_ils == pytest.approx(0.25 * 4 * 10 * 3.5)       # 4 sold at +$10
    assert tax.account_lot_check(snapshots) == {"checked": True, "at": "2026-09-18T22:00:00+00:00",
                                               "mismatches": []}
    events = tax.account_events([AccountFill("x", "o", "CCC", "sell_short", 2.0, 10.0,
                                             datetime(2026, 9, 21, 15, tzinfo=timezone.utc))])
    assert events == {date(2026, 9, 21): [Event(SELL, "CCC", 2.0, 10.0)]}


def test_a_look_s_record_is_ready_with_funds_and_unavailable_without():
    unavailable = tax.gate_record(1, D[3], D[2], None, reason="calibration had not passed")
    assert unavailable["status"] == gate.AFTER_TAX_UNAVAILABLE and unavailable["tests"] == {}
    assert unavailable["rules"]["offset_losses_vs_dividends"] is True and unavailable["lag"] == 5
    series = AfterTaxSeries(start_equity_usd=1.0, start_fx=3.5)
    ready = tax.gate_record(1, D[3], D[2], {"vt": series, "model": series})
    assert ready["status"] == gate.AFTER_TAX_READY and set(ready["tests"]) == {"model"}


def test_the_report_reads_in_plain_words():
    document = {"final_through": "2026-10-02", "generated_at": "2026-10-02T23:00:00+00:00", "after_tax": {
        "rules": tax.rules_json(), "fx": {"available": True, "first": "2026-09-10", "last": "2026-10-02",
                                         "counts": {"boi": 16, "ecb": 1, "carried": 0},
                                         "fallback_days": [["2026-09-23", "ecb"]], "rates_sha256": "ab" * 32},
        "paper": {"usd": {"equity": 101_000, "after_tax": 100_800, "return": 0.01, "after_tax_return": 0.008},
                  "ils": {"equity": 310_000, "after_tax": 309_000, "return": 0.02, "after_tax_return": 0.017,
                          "from_usd_ils": 0.01}, "tax_ils": {"paid_so_far": 0, "if_sold_today": 600}},
        "paper_lots": {"checked": True, "mismatches": []}, "funds": None, "looks": [],
        "breakeven": {"years": 20, "growth": 0.06, "dividend_yield": 0.02, "extra_per_year": 0.0082}}}
    text = tax.render(document)
    assert "# After Israeli tax and in shekels" in text and "losses also against dividends: on" in text
    assert "1 day(s) from another source: 2026-09-23 (ecb)" in text
    assert "| Paper account (real) | $101,000 (+1.00%) | $100,800 (+0.80%) | ₪310,000 (+2.00%)" in text
    assert "+1.00 points" in text and "₪600" in text
    assert "once calibration has passed" in text and "No look reached yet" in text
    assert "0.82 points a year" in text
    assert "No rate table tonight" in tax.render({"after_tax": {"fx": {"available": False, "reason": "x"}}})


def test_the_report_cli_prints_and_refuses_a_bad_file(tmp_path, capsys):
    path = tmp_path / "funds.json"
    path.write_text(json.dumps({"after_tax": None}))
    assert tax.main([str(path)]) == 0 and "No after-tax part" in capsys.readouterr().out
    assert tax.main([str(tmp_path / "missing.json")]) == 1
    assert tax.main([]) == 2


def test_the_funds_workflow_fetches_the_rates_from_the_tables_start():
    workflow = (tax.__file__.rsplit("/shadow/", 1)[0] + "/.github/workflows/funds.yml")
    text = open(workflow).read()
    assert f"--start {tax.FX_TABLE_START.isoformat()}" in text and "--fx-table" in text
    assert "python -m shadow.after_tax" in text and "logs/fx_rates.json" in text and "secrets." not in text


# --------------------------------------------------------------------------- #
# Wired into the nightly funds run (shadow/run.py)
# --------------------------------------------------------------------------- #

from shadow import run as shadow_run                               # noqa: E402
from shadow import schedule                                        # noqa: E402
from tests.test_exploratory import NOW, NoPrices, build_args, passed_calibration  # noqa: E402


def test_a_look_reached_before_calibration_passes_records_an_unavailable_after_tax_test(monkeypatch, tmp_path):
    monkeypatch.setattr(schedule, "CALIBRATION_START", None)
    monkeypatch.setattr(shadow_run, "OhlcFetcher", NoPrices)
    monkeypatch.setattr(shadow_run, "run_funds", lambda *a, **k: pytest.fail("no fund before calibration"))
    race = {"looks": [{"reached": True, "window_end": "2026-12-22"}, {"reached": False}, {"reached": False}]}
    out = shadow_run.build(build_args(tmp_path, race), NOW)
    (record,) = out["after_tax"]["looks"]
    assert record["look"] == 1 and record["status"] == gate.AFTER_TAX_UNAVAILABLE
    assert "calibration had not passed" in record["reason"] and record["window_end"] == "2026-12-22"
    assert out["after_tax"]["fx"] == {"available": False, "reason": "no rate table was given"}
    assert out["after_tax"]["funds"] is None and out["after_tax"]["paper"] is None
    assert out["after_tax"]["breakeven"]["note"] == "for information only; not a gate"
    # Carried unchanged the night after, and never made twice.
    later = shadow_run.build(build_args(tmp_path, race, previous=out), NOW + pd.Timedelta(days=1))
    assert later["after_tax"]["looks"] == [record]


def test_with_funds_a_look_gets_a_ready_test_cut_at_its_window(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    series = AfterTaxSeries(start_equity_usd=100_000.0, start_fx=3.5)

    def fake(entries, start, final_through, fetcher, **kw):
        calls.append(kw)
        out = {"start": start.isoformat(), "days": [], "band": {},
               "list": [{"name": n, "exploratory": False} for n in ("model", "momentum", "hybrid", "vt")],
               "after_tax": {"vt": None}, "_after_tax_series": {"model": series, "momentum": series,
                                                               "hybrid": series, "vt": series}}
        return out, {"four": {}, "coin": {}}

    monkeypatch.setattr(shadow_run, "run_funds", fake)
    race = {"looks": [{"reached": True, "window_end": "2026-12-22"}, {"reached": False}, {"reached": False}]}
    out = shadow_run.build(build_args(tmp_path, race), NOW)
    (record,) = out["after_tax"]["looks"]
    assert record["status"] == gate.AFTER_TAX_READY and set(record["tests"]) == {"model", "momentum", "hybrid"}
    assert "_after_tax_series" not in out["funds"] and out["after_tax"]["funds"] == {"vt": None}
    json.dumps(out, allow_nan=False)


def test_the_ic_report_shows_counters_nightly_and_its_record_only_from_registration(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    race = {"looks": [{"reached": True}, {"reached": False}, {"reached": False}]}
    early = shadow_run.build(build_args(tmp_path, race), NOW - pd.Timedelta(days=1))
    (record,) = early["exploratory"]["checkpoints"]
    assert "ic" not in record and "ic_main" not in record
    counters = early["exploratory"]["counters"]["ic"]
    assert set(counters) == {"production", "shadow"}
    assert set(counters["production"]) == {"answered_lines", "lines_with_score", "line_days"}
    on_time = shadow_run.build(build_args(tmp_path, race), NOW)
    (record,) = on_time["exploratory"]["checkpoints"]
    assert record["ic"]["registered"] == "2026-12-22"
    assert record["ic"]["universes"]["shadow"] == {"no_data": True}
    names = [row["name"] for row in record["table"]["rows"]]
    assert "IC, production names" in names and "IC, shadow stock universe" in names
