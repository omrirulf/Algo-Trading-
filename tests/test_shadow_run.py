"""The nightly runner: summaries, the band, and what it refuses to show before its time."""

from __future__ import annotations

import json
from datetime import date

import pytest

from shadow import run as shadow_run
from shadow import schedule


def _audit(reason: str, ts: str = "2026-09-16 16:06:17,809") -> str:
    return json.dumps({"event": "signal_processed", "ts": ts, "result": {"status": "ERROR", "reason": reason}})


def test_the_paper_accounts_own_short_refusals_are_read_from_its_log():
    lines = [
        _audit("BrokerError: asset LQD cannot be sold short"),
        _audit("BrokerError: asset XHB cannot be sold short"),
        _audit("BrokerError: only day orders are allowed for hard-to-borrow asset USO"),
        _audit("no room under the gross exposure limit"),
        "not json",
    ]
    assert shadow_run.not_shortable(lines) == {"LQD": date(2026, 9, 16), "XHB": date(2026, 9, 16),
                                               "USO": date(2026, 9, 16)}


def test_the_brokers_own_wording_with_the_ticker_quoted_is_read():
    """The paper account's log, verbatim: the broker's message is JSON
    inside the reason, so the ticker arrives as \\"LQD\\". A pattern that
    wants a bare ticker reads none of these, and every fund could then
    short what the paper account cannot."""
    reasons = [
        'BrokerError: submit_order failed for LQD: {"code":42210000,"message":"asset \\"LQD\\" cannot be sold short"}',
        'BrokerError: submit_order failed for TUR: {"code":42210000,"message":"asset \\"TUR\\" cannot be sold short"}',
        'BrokerError: submit_order failed for USO: {"code":42210000,"message":"only day orders are allowed for '
        'hard-to-borrow asset \\"USO\\""}',
        'asset "EWA" cannot be sold short',
    ]
    assert set(shadow_run.not_shortable([_audit(r) for r in reasons])) == {"LQD", "TUR", "USO", "EWA"}


def test_a_refusal_is_dated_by_its_first_utc_day():
    """The owner's decision of 26 Sep 2026: a refusal counts from the day it
    happened. The day is the audit line's UTC day (``ts`` is UTC), the
    calendar the funds date cycles on; a name refused twice keeps its first
    day, whatever order the lines come in; a line with no time at all is
    refused from the start, as every refusal was before they were dated."""
    lines = [
        _audit("BrokerError: asset XHB cannot be sold short", "2026-09-22 15:45:13,806"),
        _audit("BrokerError: asset XHB cannot be sold short", "2026-09-16 19:13:07,901"),
        _audit('asset "USO" cannot be sold short', "2026-09-23 23:59:59,000"),        # 19:59 New York
        json.dumps({"result": {"reason": "asset TUR cannot be sold short", "timestamp": "2026-09-24T14:00:00Z"}}),
        json.dumps({"result": {"reason": "asset EWA cannot be sold short"}}),
    ]
    assert shadow_run.not_shortable(lines) == {"EWA": date.min, "TUR": date(2026, 9, 24),
                                               "USO": date(2026, 9, 23), "XHB": date(2026, 9, 16)}


@pytest.mark.parametrize("equity, drawdown", [
    ([100.0, 110.0, 99.0, 120.0], 0.1),
    ([100.0, 90.0, 80.0], 0.2),
    ([100.0, 101.0, 102.0], 0.0),
    ([], 0.0),
])
def test_max_drawdown_is_the_worst_fall_from_a_running_peak(equity, drawdown):
    assert shadow_run.max_drawdown(equity) == pytest.approx(drawdown)


def test_the_band_is_the_5th_to_95th_percentile_day_by_day():
    curves = [[100.0 + i, 200.0 - i] for i in range(101)]
    result = shadow_run.band(curves)
    assert result["funds"] == 101
    assert result["p5"] == [105.0, 105.0]
    assert result["p95"] == [195.0, 195.0]
    assert shadow_run.band([]) == {"p5": [], "p95": [], "funds": 0}


def test_nothing_starts_until_the_owner_sets_a_date():
    """Calibration waits for the owner's approval of its pass rule. The fund
    start is the owner's fixed date (26 Sep 2026: the 28 Sep cycle, acted on
    from the 29 Sep open); the funds still wait for calibration to pass
    before anything about them is computed (``build``)."""
    assert schedule.CALIBRATION_START is None
    assert schedule.FUND_FIRST_CYCLE == date(2026, 9, 28)
    assert schedule.FUND_START == date(2026, 9, 29)
    assert schedule.CALIBRATION_DAYS == 15
    # The owner's fail rule of 25 Sep 2026: no fix yet, and five calibration
    # days after the last one. A fix is added only in a reviewed change,
    # with its row in the Amendments table.
    assert schedule.CALIBRATION_FIXES == ()
    assert schedule.AFTER_FIX_DAYS == 5
    assert schedule.RANDOM_FUNDS == 1000
    assert schedule.FUNDS == ("model", "momentum", "hybrid", "vt")


def test_calibration_cannot_start_under_a_rule_the_owner_has_not_approved():
    """Setting the start date is only half the owner's decision. The date
    and the approval change together, in one reviewed change, or not at all."""
    from shadow.calibration import PASS_RULE

    assert (schedule.CALIBRATION_START is None) == (not PASS_RULE.approved)
    # The fund start no longer waits on calibration's date (the owner's
    # decision of 26 Sep 2026); what waits is the reading, in ``build``.
    assert schedule.FUND_START > schedule.FUND_FIRST_CYCLE


def test_every_calibration_fix_is_dated_described_and_in_the_amendments_table():
    """A fix exists only after calibration started, is dated the day it was
    merged, says what it fixed, and is logged in the pre-registration's
    Amendments table on that day (the owner's fail rule)."""
    from pathlib import Path

    fixes = schedule.CALIBRATION_FIXES
    assert not fixes or schedule.CALIBRATION_START is not None
    doc = (Path(__file__).resolve().parents[1] / "docs" / "horse-race-preregistration.md").read_text()
    amendments = doc.partition("## Amendments")[2]
    rows = [row for row in amendments.splitlines() if row.startswith("| 20")]
    for day, what in fixes:
        assert isinstance(day, date) and isinstance(what, str) and what.strip()
        assert day > schedule.CALIBRATION_START
        assert any(row.startswith(f"| {day.isoformat()} |") and "alibration" in row for row in rows), day


def test_the_fund_tests_bars_come_from_its_own_share_of_the_data():
    """The owner's decisions of 24 and 26 Sep 2026. The race keeps its
    O'Brien-Fleming bars for three equal looks; the fund test's come from
    an O'Brien-Fleming-type spending rule at its own shares of its planned
    60, 120 and 180 sessions: sessions from its fixed start to each of the
    race's estimated look days."""
    from datetime import timedelta

    from analysis import decision_gate as gate
    from config.market_calendar import is_trading_day

    race = gate.obrien_fleming_bars([1, 2, 3])
    assert tuple(round(b, 2) for b in race) == tuple(bar for _, bar in gate.CHECKPOINTS)

    def sessions(first, last):
        return sum(1 for i in range((last - first).days + 1) if is_trading_day(first + timedelta(days=i)))

    looks = (date(2026, 12, 22), date(2027, 3, 22), date(2027, 6, 16))
    assert schedule.FUND_TEST_LOOK_ESTIMATES == looks
    assert tuple(sessions(schedule.FUND_TEST_PLANNED_START, look) for look in looks) == \
        schedule.FUND_TEST_PLANNED_SESSIONS == (60, 120, 180)
    final = schedule.FUND_TEST_PLANNED_SESSIONS[-1]
    exact = gate.spending_bars([n / final for n in schedule.FUND_TEST_PLANNED_SESSIONS])
    assert [round(b, 3) for b in exact] == [3.395, 2.407, 2.015]
    assert tuple(gate.rounded_bar(b) for b in exact) == schedule.FUND_TEST_BARS == (3.40, 2.41, 2.02)
