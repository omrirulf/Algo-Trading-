"""The fund test's start and bars, worked out again from wherever calibration ends.

The owner's fail rule of 25 Sep 2026: calibration ends at day 15 or at the
last fix + 5 days, whichever is later, and if that end moves, the fund
test's start and bars are recalculated and logged. The registered numbers
were worked out from the planned end, 2026-10-16.
"""

from __future__ import annotations

from datetime import date

from analysis import decision_gate as gate
from shadow import schedule
from shadow.fund_test import fund_test_plan, next_trading_day, sessions_through


def test_the_planned_end_gives_the_registered_start_and_bars():
    plan = fund_test_plan(date(2026, 10, 16))

    assert plan["start"] == "2026-10-19" == schedule.FUND_TEST_PLANNED_START.isoformat()
    assert plan["sessions"] == [46, 106, 166] == list(schedule.FUND_TEST_PLANNED_SESSIONS)
    assert plan["bars"] == [3.80, 2.50, 2.00]
    assert plan["exact"] == [3.797, 2.501, 1.999]
    assert plan["registered"] == [3.80, 2.50, 2.00] and plan["registered_start"] == "2026-10-19"
    assert plan["matches_registered"] is True


def test_a_later_end_is_a_later_start_fewer_sessions_and_other_bars():
    """A fix after day 15 (16 Oct) moves the end a week, to 2026-10-23. A
    fix after day 12 (13 Oct) moves it to day 17, 2026-10-20."""
    plan = fund_test_plan(date(2026, 10, 23))

    assert plan["start"] == "2026-10-26"
    assert plan["sessions"] == [41, 101, 161]
    assert plan["bars"] != [3.80, 2.50, 2.00]
    assert plan["bars"] == [round(b, 2) for b in gate.obrien_fleming_bars([41, 101, 161])]
    assert plan["registered"] == [3.80, 2.50, 2.00] and plan["registered_start"] == "2026-10-19"
    assert plan["matches_registered"] is False


def test_the_start_is_the_next_trading_day():
    assert next_trading_day(date(2026, 10, 16)) == date(2026, 10, 19)          # Friday to Monday
    assert next_trading_day(date(2026, 11, 25)) == date(2026, 11, 27)          # over Thanksgiving
    assert fund_test_plan(date(2026, 11, 25))["start"] == "2026-11-27"
    assert sessions_through(date(2026, 10, 19), date(2026, 10, 19)) == 1       # both ends counted
    assert sessions_through(date(2026, 10, 19), date(2026, 10, 16)) == 0


def test_the_looks_are_the_races_estimated_look_days():
    assert schedule.FUND_TEST_LOOK_ESTIMATES == (date(2026, 12, 22), date(2027, 3, 22), date(2027, 6, 16))
    other = fund_test_plan(date(2026, 10, 16), (date(2026, 12, 22), date(2027, 3, 22)))
    assert other["sessions"] == [46, 106] and other["matches_registered"] is False


def test_a_look_before_the_start_cannot_be_read_and_is_never_a_match():
    """An end so late the first look is gone: that is a new design for the
    owner, so the plan says so instead of quietly reusing three bars."""
    plan = fund_test_plan(date(2026, 12, 22))

    assert plan["start"] == "2026-12-23"
    assert plan["sessions"][0] == 0 and plan["bars"][0] is None and plan["exact"][0] is None
    assert plan["bars"][1:] == [round(b, 2) for b in gate.obrien_fleming_bars(plan["sessions"][1:])]
    assert plan["matches_registered"] is False
    gone = fund_test_plan(date(2027, 7, 1))
    assert gone["sessions"] == [0, 0, 0] and gone["bars"] == [None, None, None]


def test_a_look_on_the_start_day_cannot_be_read_either():
    """Ending the day before a look starts the fund test on it: one session
    of data, a bar of about 22. That look is gone too, as the page says."""
    plan = fund_test_plan(date(2026, 12, 21))

    assert plan["start"] == "2026-12-22" == schedule.FUND_TEST_LOOK_ESTIMATES[0].isoformat()
    assert plan["sessions"] == [0, 61, 121]
    assert plan["bars"][0] is None and plan["exact"][0] is None
    assert plan["bars"][1:] == [round(b, 2) for b in gate.obrien_fleming_bars([61, 121])]
    assert plan["matches_registered"] is False
    # The day before, the first look is read after two sessions: still a bar.
    assert fund_test_plan(date(2026, 12, 18))["sessions"][0] == 2
