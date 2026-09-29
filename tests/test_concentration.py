"""The monthly concentration report: descriptive numbers, computed right, fetched once.

The owner's request (27 Sep 2026): the book's beta to VT, each exposure
group against its cap, breadth, and VT's realized volatility. No network
here: every close is built by hand.
"""

from __future__ import annotations

import json
import math
import statistics
from datetime import date, timedelta

import pytest

from analysis import concentration as conc


def sessions(end: date, n: int) -> list[date]:
    days, day = [], end
    while len(days) < n:
        if conc.is_trading_day(day):
            days.append(day)
        day -= timedelta(days=1)
    return sorted(days)


def series(days, returns, start=100.0):
    out, price = [(days[0], start)], start
    for day, r in zip(days[1:], returns):
        price *= 1 + r
        out.append((day, price))
    return out


def wiggle(n, seed=1):
    # A deterministic, zig-zagging return series (no randomness in a test).
    return [0.01 * math.sin(seed * k * 0.7) + 0.002 * ((k % 5) - 2) for k in range(n)]


def test_the_month_ends_on_its_last_trading_day():
    assert conc.last_trading_day("2026-09") == date(2026, 9, 30)
    assert conc.last_trading_day("2026-10") == date(2026, 10, 30)      # 31 Oct 2026 is a Saturday
    assert conc.last_trading_day("2026-12") == date(2026, 12, 31)
    assert conc.previous_month(date(2026, 10, 1)) == "2026-09"
    assert conc.previous_month(date(2027, 1, 4)) == "2026-12"


def test_beta_is_the_slope_of_the_asset_on_the_index():
    end = date(2026, 9, 30)
    days = sessions(end, 300)
    index_returns = wiggle(299)
    index = series(days, index_returns)
    double = series(days, [2 * r for r in index_returns])
    b, n = conc.beta(double, index, end)
    assert n == conc.BETA_SESSIONS and b == pytest.approx(2.0, abs=1e-9)
    b, _ = conc.beta(series(days, [-0.5 * r for r in index_returns]), index, end)
    assert b == pytest.approx(-0.5, abs=1e-9)


def test_a_missing_bar_costs_returns_never_shifts_them():
    end = date(2026, 9, 30)
    days = sessions(end, 300)
    index_returns = wiggle(299)
    index = series(days, index_returns)
    asset = [bar for k, bar in enumerate(series(days, [3 * r for r in index_returns])) if k % 10 != 5]
    b, n = conc.beta(asset, index, end)
    assert n < conc.BETA_SESSIONS and b == pytest.approx(3.0, abs=1e-9)
    b, n = conc.beta(asset[-30:], index, end)
    assert b is None and n < conc.MIN_RETURNS


def test_breadth_compares_the_close_with_its_own_fifty_day_average():
    end = date(2026, 9, 30)
    days = sessions(end, 60)
    rising = [(d, 100.0 + k) for k, d in enumerate(days)]
    falling = [(d, 200.0 - k) for k, d in enumerate(days)]
    assert conc.above_average(rising, end) is True
    assert conc.above_average(falling, end) is False
    assert conc.above_average(rising[:-1], end) is None       # no bar on the day itself
    assert conc.above_average(rising[-30:], end) is None      # fewer than 50 closes


def test_vt_volatility_is_the_months_daily_sd_annualised():
    end = date(2026, 9, 30)
    days = sessions(end, 60)
    returns = wiggle(59)
    bars = series(days, returns)
    in_month = [r for d, r in zip(days[1:], returns) if d.isoformat()[:7] == "2026-09"]
    vol, n = conc.month_volatility(bars, "2026-09")
    assert n == len(in_month)
    assert vol == pytest.approx(statistics.stdev(in_month) * math.sqrt(252), rel=1e-9)


def snapshot(at, positions, equity=100_000.0):
    return json.dumps({"at": at, "account": {"equity": equity}, "positions": positions})


def test_the_book_is_the_last_snapshot_of_the_month():
    lines = [snapshot("2026-09-29T15:00:00Z", []), snapshot("2026-09-30T15:00:00Z", [{"ticker": "MSFT"}]),
             snapshot("2026-10-01T15:00:00Z", [{"ticker": "NVDA"}, {"ticker": "AAPL"}]), "not json"]
    book = conc.book_at(lines, date(2026, 9, 30))
    assert book["at"] == "2026-09-30T15:00:00Z"
    assert conc.book_at(lines, date(2026, 9, 1)) is None


def test_a_month_before_the_account_record_began_says_so():
    """2026-08's report (made 29 Sep 2026) had no book because the account has
    been recorded only since 25 Sep; it said "no account snapshot recorded
    that month", which read like a recorder that had failed."""
    none = lambda t, a, b: []                                          # noqa: E731
    lines = [snapshot("2026-09-25T16:21:20Z", [{"ticker": "MSFT", "qty": 1, "market_value": 500.0}])]
    record = conc.report("2026-08", lines, none, watchlist=())
    assert record["book"] is None
    assert ("- book: not measured: the paper account has been recorded only since 2026-09-25 "
            "(logs/account.jsonl), after this month's last trading day, 2026-08-31") in conc.render(record)
    empty = conc.render(conc.report("2026-08", [], none, watchlist=()))
    assert "- book: not measured: no account snapshot has been recorded yet (logs/account.jsonl)" in empty
    # A record made before the reason was kept (2026-08's) names the day looked for.
    old = {k: v for k, v in record.items() if k != "book_missing"}
    assert "- book: not measured: no account snapshot was recorded on or before 2026-08-31" in conc.render(old)
    assert conc.report("2026-09", lines, none, watchlist=())["book"] is not None


def test_the_report_signs_shorts_and_counts_groups_against_their_caps():
    end = date(2026, 9, 30)
    days = sessions(end, 300)
    index_returns = wiggle(299)
    closes = {
        "VT": series(days, index_returns),
        "MSFT": series(days, [1.5 * r for r in index_returns]),
        "XLE": series(days, [0.5 * r for r in index_returns]),
    }
    account = [snapshot("2026-09-30T15:00:00Z", [
        {"ticker": "MSFT", "qty": 10, "market_value": 5_000.0},
        {"ticker": "XLE", "qty": -20, "market_value": 4_000.0},     # a short: the value is given unsigned
    ])]
    record = conc.report("2026-09", account, lambda t, a, b: closes.get(t, []), watchlist=("MSFT", "XLE", "VT"))
    beta = record["book"]["beta_to_vt"]
    assert beta["long_side"] == pytest.approx(0.05 * 1.5, abs=1e-3)
    assert beta["short_side"] == pytest.approx(-0.04 * 0.5, abs=1e-3)
    assert beta["net"] == pytest.approx(0.075 - 0.02, abs=1e-3)
    groups = {g["group"]: g for g in record["book"]["groups"]}
    assert all(g["cap_pct"] in (25.0, 30.0) for g in groups.values())
    assert sum(g["used_pct"] for g in groups.values()) >= 9.0 - 1e-6
    assert record["breadth"]["of"] == 3
    assert record["vt_volatility"]["sessions"] > 15
    json.loads(json.dumps(record, allow_nan=False))
    text = conc.render(record)
    assert "descriptive only" in text and "beta to VT" in text and "breadth" in text


def test_a_month_already_made_is_printed_back_without_a_fetch(tmp_path, monkeypatch, capsys):
    history = {"kind": "concentration", "latest": "2026-09", "months": {"2026-09": {"month": "2026-09"}}}
    path = tmp_path / "concentration.json"
    path.write_text(json.dumps(history))

    class NoFetch:
        def __init__(self, *a, **k):
            raise AssertionError("a month already in the record must not be fetched again")

    monkeypatch.setattr(conc, "YFinancePriceSource", NoFetch)
    assert conc.main(["--month", "2026-09", "--history", str(path)]) == 0
    assert json.loads(capsys.readouterr().out) == history


def test_a_new_month_is_added_to_the_history(tmp_path, monkeypatch, capsys):
    path = tmp_path / "concentration.json"
    path.write_text(json.dumps({"kind": "concentration", "months": {"2026-08": {"month": "2026-08"}}}))

    class Empty:
        def __init__(self, *a, **k):
            pass

        def closes(self, ticker, start, end):
            class S:
                bars = []
            return S()

    monkeypatch.setattr(conc, "YFinancePriceSource", Empty)
    account = tmp_path / "account.jsonl"
    account.write_text("")
    assert conc.main(["--month", "2026-09", "--history", str(path), "--account", str(account)]) == 0
    out = json.loads(capsys.readouterr().out)
    assert sorted(out["months"]) == ["2026-08", "2026-09"] and out["latest"] == "2026-09"
    assert out["months"]["2026-09"]["book"] is None
