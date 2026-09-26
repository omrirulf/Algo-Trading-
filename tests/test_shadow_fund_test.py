"""The fund test's looks and bars, from its fixed start.

The owner's decision of 26 Sep 2026: the funds act on the cycle journalled
on 2026-09-28, so the first fund session is 2026-09-29 whenever calibration
ends; the fund test counts only after calibration passes, and a look before
that is skipped, spending nothing. The bars come from an O'Brien-Fleming-
type alpha-spending rule (``analysis.decision_gate.spending_bars``) at the
look's share of the planned final sessions (180).
"""

from __future__ import annotations

from datetime import date

import pytest

from analysis import decision_gate as gate
from shadow import schedule
from shadow.fund_test import fund_test_plan, next_trading_day, sessions_through, skipped_look


def test_the_start_is_fixed_on_the_owners_day():
    assert schedule.FUND_FIRST_CYCLE == date(2026, 9, 28)                       # a Monday
    assert schedule.FUND_FIRST_CYCLE.weekday() == 0
    assert schedule.FUND_START == date(2026, 9, 29) == next_trading_day(schedule.FUND_FIRST_CYCLE)
    assert schedule.FUND_TEST_PLANNED_START == schedule.FUND_START


def test_the_planned_looks_are_60_120_and_180_sessions_with_the_spending_rules_bars():
    looks = schedule.FUND_TEST_LOOK_ESTIMATES
    assert looks == (date(2026, 12, 22), date(2027, 3, 22), date(2027, 6, 16))
    assert tuple(sessions_through(date(2026, 9, 29), look) for look in looks) == (60, 120, 180)
    assert schedule.FUND_TEST_PLANNED_SESSIONS == (60, 120, 180)

    exact = gate.spending_bars([60 / 180, 120 / 180, 1.0])
    assert [round(b, 3) for b in exact] == [3.395, 2.407, 2.015]
    assert tuple(gate.rounded_bar(b) for b in exact) == schedule.FUND_TEST_BARS == (3.40, 2.41, 2.02)


@pytest.mark.parametrize("end", [None, date(2026, 10, 16), date(2026, 10, 23), date(2026, 12, 21)])
def test_an_end_before_the_first_look_moves_nothing(end):
    """Calibration's end, early or late, does not move the start or the plan:
    only a look on or before it would change anything."""
    plan = fund_test_plan(end)

    assert plan["start"] == "2026-09-29" and plan["first_cycle"] == "2026-09-28"
    assert plan["sessions"] == [60, 120, 180] and plan["skipped"] == [False, False, False]
    assert plan["bars"] == [3.40, 2.41, 2.02] and plan["exact"] == [3.395, 2.407, 2.015]
    assert plan["registered"] == [3.40, 2.41, 2.02] and plan["registered_start"] == "2026-09-29"
    assert plan["registered_sessions"] == [60, 120, 180]
    assert plan["matches_registered"] is True


def test_a_look_before_calibration_has_passed_is_skipped_and_spends_nothing():
    """Calibration ending on the first look's day, or after it: that look is
    not read and uses no bar, and the next look's bar spends what the rule
    allows by its own share, with no earlier bar."""
    for end in (date(2026, 12, 22), date(2027, 1, 15)):
        assert skipped_look(date(2026, 12, 22), end)
        plan = fund_test_plan(end)
        assert plan["skipped"] == [True, False, False]
        assert plan["bars"][0] is None and plan["exact"][0] is None
        rest = gate.spending_bars([120 / 180, 1.0])
        assert plan["exact"][1:] == [round(b, 3) for b in rest]
        assert plan["bars"][1:] == [gate.rounded_bar(b) for b in rest]
        # Nothing spent at look 1, so look 2's bar is lower than planned.
        assert plan["bars"][1] < schedule.FUND_TEST_BARS[1]
        assert plan["matches_registered"] is False
    assert not skipped_look(date(2026, 12, 22), date(2026, 12, 21))
    gone = fund_test_plan(date(2027, 7, 1))
    assert gone["skipped"] == [True, True, True] and gone["bars"] == [None, None, None]


def test_other_look_days_get_the_rule_at_their_own_shares():
    """A look that moves is read at its actual share of the planned final
    sessions; the last look counts as 1."""
    moved = fund_test_plan(None, (date(2026, 12, 29), date(2027, 3, 22), date(2027, 6, 23)))
    assert moved["sessions"] == [64, 120, 184]
    exact = gate.spending_bars([64 / 180, 120 / 180, 1.0])
    assert moved["bars"] == [gate.rounded_bar(b) for b in exact]
    assert moved["matches_registered"] is False
    two = fund_test_plan(None, (date(2026, 12, 22), date(2027, 3, 22)))
    assert two["sessions"] == [60, 120] and two["matches_registered"] is False
    assert two["exact"] == [round(b, 3) for b in gate.spending_bars([60 / 180, 1.0])]


def test_the_calendar_helpers():
    assert next_trading_day(date(2026, 10, 16)) == date(2026, 10, 19)          # Friday to Monday
    assert next_trading_day(date(2026, 11, 25)) == date(2026, 11, 27)          # over Thanksgiving
    assert sessions_through(date(2026, 10, 19), date(2026, 10, 19)) == 1       # both ends counted
    assert sessions_through(date(2026, 10, 19), date(2026, 10, 16)) == 0
