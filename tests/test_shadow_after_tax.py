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


def test_the_view_shows_tax_paid_so_far_and_if_sold_today_in_both_currencies():
    from analysis.israel_tax import AfterTaxDay

    series = AfterTaxSeries(start_equity_usd=100_000.0, start_fx=3.5)
    # Equity $110,000 at 3.6; ₪3,600 of tax already due ($1,000), ₪10,800 if all were sold today.
    series.days.append(AfterTaxDay(D[0], 3.6, 110_000.0, 396_000.0, 107_000.0, 385_200.0, 3_600.0, 10_800.0,
                                   realised_tax_usd=1_000.0))
    v = tax.view(series)
    assert v["usd"]["paid_so_far"] == 109_000.0 and v["usd"]["paid_so_far_return"] == pytest.approx(0.09)
    assert v["ils"]["paid_so_far"] == 392_400.0 and v["ils"]["paid_so_far_return"] == pytest.approx(392_400 / 350_000 - 1)
    assert v["ils"]["after_tax_from_usd_ils"] == pytest.approx((385_200 / 350_000 - 1) - 0.07)
    assert v["tax_ils"] == {"paid_so_far": 3_600.0, "if_sold_today": 10_800.0}


def test_the_report_reads_in_plain_words():
    document = {"final_through": "2026-10-02", "generated_at": "2026-10-02T23:00:00+00:00", "after_tax": {
        "rules": tax.rules_json(), "fx": {"available": True, "first": "2026-09-10", "last": "2026-10-02",
                                         "counts": {"boi": 16, "ecb": 1, "carried": 0},
                                         "fallback_days": [["2026-09-23", "ecb"]], "rates_sha256": "ab" * 32},
        "paper": {"usd": {"equity": 101_000, "after_tax": 100_800, "return": 0.01, "after_tax_return": 0.008,
                          "paid_so_far": 101_000, "paid_so_far_return": 0.01},
                  "ils": {"equity": 310_000, "after_tax": 309_000, "return": 0.02, "after_tax_return": 0.017,
                          "paid_so_far": 310_000, "paid_so_far_return": 0.02,
                          "from_usd_ils": 0.01, "after_tax_from_usd_ils": 0.009},
                  "tax_ils": {"paid_so_far": 0, "if_sold_today": 600}},
        "paper_lots": {"checked": True, "mismatches": []}, "funds": None, "looks": [],
        "breakeven": {"years": 20, "growth": 0.06, "dividend_yield": 0.02, "extra_per_year": 0.0082}}}
    text = tax.render(document)
    assert "# After Israeli tax and in shekels" in text and "losses also against dividends: on" in text
    assert "1 day(s) from another source: 2026-09-23 (ecb)" in text
    assert ("| Paper account (real) | $101,000 (+1.00%) | $100,800 (+0.80%) | $101,000 (+1.00%) "
            "| ₪310,000 (+2.00%) | ₪309,000 (+1.70%) | ₪310,000 (+2.00%) | +1.00 points | +0.90 points | ₪0 | ₪600 |") in text
    assert "After tax, if sold today (₪) | After tax, tax paid so far (₪)" in text
    assert "once calibration has passed" in text and "No look reached yet" in text
    # After calibration has passed, a night with no funds after tax (no rate table) does not blame calibration.
    assert "once calibration has passed" not in tax.render(document | {"calibration": {"status": "passed"}})
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
    race = {"looks": [{"reached": True, "readable": True, "window_end": "2026-12-22"}, {"reached": False},
                      {"reached": False}]}
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


def _series_through(last: date, step: float) -> AfterTaxSeries:
    from analysis.israel_tax import AfterTaxDay
    days = [d.date() for d in pd.bdate_range(date(2026, 9, 29), last)]
    out = AfterTaxSeries(start_equity_usd=100_000.0, start_fx=3.5)
    for i, d in enumerate(days):
        value = 100_000.0 * (1 + step * ((i * 7) % 5 - 2))
        out.days.append(AfterTaxDay(d, 3.5, value, value * 3.5, value, value * 3.5, 0.0, 0.0))
    return out


def _with_series(monkeypatch, calls, series, coverage=None):
    """``run_funds`` as it is with a rate table: the series, and the funds' own price coverage (all complete
    unless ``coverage`` says otherwise)."""
    def fake(entries, start, final_through, fetcher, **kw):
        calls.append(kw)
        out = {"start": start.isoformat(), "days": [], "band": {},
               "list": [{"name": n, "exploratory": False} for n in ("model", "momentum", "hybrid", "vt")],
               "after_tax": {"vt": None}, "_after_tax_series": series,
               "_after_tax_coverage": {} if coverage is None else coverage}
        return out, {"four": {}, "coin": {}}

    monkeypatch.setattr(shadow_run, "run_funds", fake)


def test_with_funds_a_look_gets_a_ready_test_cut_at_its_window(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    series = {n: _series_through(date(2026, 12, 31), 0.001 * (k + 1))
              for k, n in enumerate(("model", "momentum", "hybrid", "vt"))}
    _with_series(monkeypatch, calls, series)
    race = {"looks": [{"reached": True, "readable": True, "window_end": "2026-12-22"}, {"reached": False},
                      {"reached": False}]}
    out = shadow_run.build(build_args(tmp_path, race), NOW)
    (record,) = out["after_tax"]["looks"]
    assert record["status"] == gate.AFTER_TAX_READY and set(record["tests"]) == {"model", "momentum", "hybrid"}
    assert all(test["through"] == "2026-12-22" for test in record["tests"].values())   # cut at the look's close
    assert "_after_tax_series" not in out["funds"] and "_after_tax_coverage" not in out["funds"]
    assert out["after_tax"]["funds"] == {"vt": None}
    json.dumps(out, allow_nan=False)


READABLE_AT_22 = {"looks": [{"reached": True, "readable": True, "window_end": "2026-12-22"}, {"reached": False},
                            {"reached": False}]}


def test_a_ready_record_cut_at_another_close_is_made_again_at_the_new_close(monkeypatch, tmp_path):
    """A bug fix re-ran the race and moved look 1's window: the old record is replaced, once, and kept inside."""
    calls = []
    passed_calibration(monkeypatch, calls)
    series = {n: _series_through(date(2026, 12, 31), 0.001 * (k + 1))
              for k, n in enumerate(("model", "momentum", "hybrid", "vt"))}
    _with_series(monkeypatch, calls, series)
    old = tax.gate_record(1, date(2026, 12, 21), date(2026, 12, 21), series)
    previous = {"after_tax": {"looks": [old]}}
    out = shadow_run.build(build_args(tmp_path, READABLE_AT_22, previous=previous), NOW)
    (record,) = out["after_tax"]["looks"]
    assert record["window_end"] == "2026-12-22" and record["status"] == gate.AFTER_TAX_READY
    assert json.loads(json.dumps(record["superseded"])) == json.loads(json.dumps(old))
    # Carried unchanged after that.
    later = shadow_run.build(build_args(tmp_path, READABLE_AT_22, previous=out), NOW + pd.Timedelta(days=1))
    assert later["after_tax"]["looks"] == out["after_tax"]["looks"]


def test_an_unavailable_record_is_never_made_again(monkeypatch, tmp_path):
    """"Unavailable" says calibration had not passed when the race reached the look; a moved window does not
    change that, so the record is carried as it was."""
    calls = []
    passed_calibration(monkeypatch, calls)
    _with_series(monkeypatch, calls, {n: _series_through(date(2026, 12, 31), 0.001)
                                      for n in ("model", "momentum", "hybrid", "vt")})
    old = tax.gate_record(1, date(2026, 12, 21), date(2026, 12, 21), None, reason="calibration had not passed")
    previous = {"after_tax": {"looks": [old]}}
    out = shadow_run.build(build_args(tmp_path, READABLE_AT_22, previous=previous), NOW)
    assert out["after_tax"]["looks"] == [old]


def test_a_look_waits_when_the_funds_own_prices_lack_a_name(monkeypatch, tmp_path):
    """Section 5c: the funds' prices must reach the look's last close for every name a cycle named by then,
    checked on the funds' own fetch, not the race's."""
    calls = []
    passed_calibration(monkeypatch, calls)
    series = {n: _series_through(date(2026, 12, 31), 0.001) for n in ("model", "momentum", "hybrid", "vt")}
    coverage = {"NVDA": (date(2026, 9, 28), date(2026, 12, 18)), "VT": (date(2026, 9, 29), date(2026, 12, 22)),
                "LATE": (date(2026, 12, 23), None)}       # named only after the look's close: does not count
    _with_series(monkeypatch, calls, series, coverage)
    assert shadow_run.build(build_args(tmp_path, READABLE_AT_22), NOW)["after_tax"]["looks"] == []
    assert shadow_run.missing_prices(coverage, date(2026, 12, 22)) == ["NVDA"]
    assert shadow_run.missing_prices(None, date(2026, 12, 22)) is None


def test_price_coverage_reads_the_funds_own_bars():
    days = [date(2026, 9, 29), date(2026, 9, 30), date(2026, 10, 1)]
    bars = Bars({"AAA": frame({d: (10, 11, 9, 10, 0) for d in days}),
                 "BBB": frame({d: (10, 11, 9, 10, 0) for d in days[:2]}),
                 "VT": frame({d: (100, 101, 99, 100, 0) for d in days})})

    @dataclass
    class _Line:
        ticker: str

    cycles = {days[0]: [_Line("AAA")], days[1]: [_Line("BBB"), _Line("AAA")], days[2]: [_Line("CCC")]}
    coverage = shadow_run.price_coverage(cycles, bars, days[0], days[2])
    assert coverage == {"AAA": (days[0], days[2]), "BBB": (days[1], days[1]), "CCC": (days[2], None),
                        "VT": (days[0], days[2])}
    assert shadow_run.missing_prices(coverage, days[2]) == ["BBB", "CCC"]
    assert shadow_run.missing_prices(coverage, days[1]) == []


def test_a_rate_table_that_ends_before_the_last_session_is_not_used(monkeypatch, tmp_path):
    from analysis import boi_rates

    calls = []
    passed_calibration(monkeypatch, calls)
    _with_series(monkeypatch, calls, None)
    entries = tuple(boi_rates.DayRate(d.date(), 3.70, boi_rates.BOI) for d in pd.bdate_range("2026-09-10", "2026-12-21"))
    tape = boi_rates.tape(boi_rates.RateTable(entries), datetime(2026, 12, 21, 23, tzinfo=timezone.utc),
                          date(2026, 12, 21))
    path = tmp_path / "fx.json"
    path.write_text(json.dumps(tape))
    args = build_args(tmp_path, READABLE_AT_22)
    args.fx_table = path
    out = shadow_run.build(args, NOW)                       # the last final session is 2026-12-22
    assert calls[-1]["rates"] is None
    assert out["after_tax"]["fx"] == {"available": False, "reason": (
        "the rate table ends 2026-12-21, before the last final session 2026-12-22")}
    assert out["after_tax"]["looks"] == []


def test_a_look_waits_when_the_race_cannot_read_it_or_the_funds_do_not_reach_its_close(monkeypatch, tmp_path):
    calls = []
    passed_calibration(monkeypatch, calls)
    short = {n: _series_through(date(2026, 12, 21), 0.001) for n in ("model", "momentum", "hybrid", "vt")}
    _with_series(monkeypatch, calls, short)
    unreadable = {"looks": [{"reached": True, "readable": False, "window_end": "2026-12-22"}, {"reached": False},
                            {"reached": False}]}
    assert shadow_run.build(build_args(tmp_path, unreadable), NOW)["after_tax"]["looks"] == []
    readable = {"looks": [{"reached": True, "readable": True, "window_end": "2026-12-22"}, {"reached": False},
                          {"reached": False}]}
    assert shadow_run.build(build_args(tmp_path, readable), NOW)["after_tax"]["looks"] == []   # funds end on the 21st


def test_the_rate_table_is_read_from_its_tape_and_refused_when_it_does_not_check_out(tmp_path):
    from analysis import boi_rates

    entries = tuple(boi_rates.DayRate(d.date(), 3.70, boi_rates.BOI) for d in pd.bdate_range("2026-09-10", "2026-09-18"))
    table = boi_rates.RateTable(entries)
    tape = boi_rates.tape(table, datetime(2026, 9, 18, 23, tzinfo=timezone.utc), date(2026, 9, 18))
    path = tmp_path / "fx.json"
    path.write_text(json.dumps(tape))
    rates, meta = shadow_run.load_rates(path)
    assert rates.rate(date(2026, 9, 14)) == 3.70 and meta["available"] is True
    assert meta["counts"] == {"boi": 7, "ecb": 0, "carried": 0} and meta["rates_sha256"] == tape["prices_sha256"]
    tape["rows"][0]["close"] = 3.71
    path.write_text(json.dumps(tape))
    rates, meta = shadow_run.load_rates(path)
    assert rates is None and meta["available"] is False and "could not be read" in meta["reason"]
    assert shadow_run.load_rates(tmp_path / "missing.json")[0] is None
    assert shadow_run.load_rates(None) == (None, {"available": False, "reason": "no rate table was given"})


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
    # Section 13.10: the regime split is in the look's record; between looks only sessions per state.
    assert set(record["regimes"]) == {"race", "funds", "counters", "cutoffs"}
    assert set(early["exploratory"]["counters"]["regimes"]) == {"sessions", "first", "last", "trend", "vol"}


def test_the_regime_split_reads_the_race_and_the_funds_by_vt_s_state(monkeypatch):
    """checkpoint_regimes on crafted race trades and fund equity: every series is split, VT's own window is the
    race's comparator, and the funds are paired with the VT fund."""
    from types import SimpleNamespace as NS

    from analysis import regimes
    from shadow import exploratory as xp

    days = [d.date() for d in pd.bdate_range("2025-10-01", "2026-12-31")]
    vt = frame({d: (100 + i * 0.05, 101 + i * 0.05, 99 + i * 0.05, 100 + i * 0.05, 0.0) for i, d in enumerate(days)})
    long_bars = Bars({"VT": vt})
    entry = [d for d in days if d >= date(2026, 10, 1)][:5]
    trades = {"model": [NS(entry_day=d, net=0.01) for d in entry], "momentum": [NS(entry_day=d, net=0.0) for d in entry],
              "hybrid": []}
    monkeypatch.setattr(xp, "race_settings", lambda today, final_through, lines: None)
    monkeypatch.setattr(xp, "arm_trades", lambda name, entries, how: trades[name])
    funds = {"days": [d.isoformat() for d in entry],
             "list": [{"name": n, "equity": [100_000.0 * (1 + 0.001 * (i + 1)) for i in range(5)]}
                      for n in ("model", "momentum", "hybrid", "vt")]}
    out = shadow_run.checkpoint_regimes([], long_bars, date(2026, 12, 31), date(2026, 12, 31), funds)
    assert out["cutoffs"] == list(regimes.VOL_CUTOFFS) and set(out["race"]["vol"]) == set(regimes.VOL_STATES)
    above = out["race"]["trend"]["above"]
    assert above["model"]["days"] == 5 and above["model"]["mean"] == pytest.approx(0.01)
    assert above["model - momentum"]["mean"] == pytest.approx(0.01) and "model - vt" in above
    assert out["funds"]["trend"]["above"]["model - vt"]["mean"] == pytest.approx(0.0)
