"""The nightly runner: summaries, the band, and what it refuses to show before its time."""

from __future__ import annotations

import json
from datetime import date

import pytest

from shadow import run as shadow_run
from shadow import schedule


def _audit(reason: str) -> str:
    return json.dumps({"event": "signal_processed", "result": {"status": "ERROR", "reason": reason}})


def test_the_paper_accounts_own_short_refusals_are_read_from_its_log():
    lines = [
        _audit("BrokerError: asset LQD cannot be sold short"),
        _audit("BrokerError: asset XHB cannot be sold short"),
        _audit("BrokerError: only day orders are allowed for hard-to-borrow asset USO"),
        _audit("no room under the gross exposure limit"),
        "not json",
    ]
    assert shadow_run.not_shortable(lines) == frozenset({"LQD", "XHB", "USO"})


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
    """Calibration waits for the owner's approval of its pass rule; the funds
    wait for calibration to pass. The code never sets either date."""
    assert schedule.CALIBRATION_START is None
    assert schedule.FUND_START is None
    assert schedule.CALIBRATION_DAYS == 15
    assert schedule.RANDOM_FUNDS == 1000
    assert schedule.FUNDS == ("model", "momentum", "hybrid", "vt")
