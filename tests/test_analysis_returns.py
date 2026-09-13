"""Joining signals to outcomes — above all, never looking backwards.

The failure this file exists to prevent: entering at a price that was already
known when the signal was produced. A scorer with that bug reports a brilliant
strategy and is worse than having no scorer at all, because it is believed.
"""

from __future__ import annotations

from datetime import date, datetime, time, timezone

import pytest

from analysis import returns
from analysis.returns import (
    ENTRY_AUTO,
    ENTRY_NEXT,
    ENTRY_SAME,
    STATUS_NO_ENTRY_BAR,
    STATUS_NO_HISTORY,
    STATUS_NO_TIMESTAMP,
    STATUS_OK,
    STATUS_PENDING,
    PriceSeries,
    forward_return,
)

#: Five consecutive sessions, one clean 10% step per day.
BARS = [
    (date(2026, 3, 2), 100.0),
    (date(2026, 3, 3), 110.0),
    (date(2026, 3, 4), 120.0),
    (date(2026, 3, 5), 130.0),
    (date(2026, 3, 6), 140.0),
]
SERIES = PriceSeries("TEST", BARS)


def at(day: int, hour: int = 14) -> datetime:
    return datetime(2026, 3, day, hour, 0, tzinfo=timezone.utc)


# --------------------------------------------------------------------------- #
# Look-ahead safety
# --------------------------------------------------------------------------- #


def test_entry_price_is_never_from_before_the_signal():
    """The whole point. Sweep every rule, hour and day; no entry may predate."""
    for rule in (ENTRY_AUTO, ENTRY_NEXT, ENTRY_SAME):
        for day in range(2, 7):
            for hour in (0, 9, 14, 19, 20, 23):
                lookup = forward_return(
                    SERIES, at(day, hour), horizon=1,
                    timestamp_is_exact=True, entry=rule,
                )
                if lookup.ok:
                    assert lookup.value.entry_date >= at(day, hour).date(), (
                        f"rule={rule} day={day} hour={hour} entered on "
                        f"{lookup.value.entry_date}, before the signal"
                    )


def test_after_hours_signal_does_not_enter_at_that_days_close():
    """22:00 is after the close: that day's close is already history."""
    lookup = forward_return(
        SERIES, at(3, 22), horizon=1, timestamp_is_exact=True, entry=ENTRY_AUTO
    )
    assert lookup.value.entry_date == date(2026, 3, 4)
    assert lookup.value.entry_price == 120.0


def test_intraday_signal_does_enter_at_that_days_close():
    """14:00 is before the close, so the same session is still tradeable."""
    lookup = forward_return(
        SERIES, at(3, 14), horizon=1, timestamp_is_exact=True, entry=ENTRY_AUTO
    )
    assert lookup.value.entry_date == date(2026, 3, 3)
    assert lookup.value.entry_price == 110.0


def test_a_naive_timestamp_is_never_trusted_with_a_same_day_entry():
    """Without an offset we cannot know if the close had already happened."""
    lookup = forward_return(
        SERIES, at(3, 14), horizon=1, timestamp_is_exact=False, entry=ENTRY_AUTO
    )
    assert lookup.value.entry_date == date(2026, 3, 4)


@pytest.mark.parametrize("hour", [0, 9, 19])
def test_auto_resolves_to_same_only_before_the_close(hour):
    assert returns.entry_rule_for(at(3, hour), True, ENTRY_AUTO) == ENTRY_SAME


@pytest.mark.parametrize("hour", [20, 21, 23])
def test_auto_resolves_to_next_at_or_after_the_close(hour):
    assert returns.entry_rule_for(at(3, hour), True, ENTRY_AUTO) == ENTRY_NEXT


def test_explicit_rules_ignore_the_timestamp():
    assert returns.entry_rule_for(at(3, 22), True, ENTRY_SAME) == ENTRY_SAME
    assert returns.entry_rule_for(at(3, 9), True, ENTRY_NEXT) == ENTRY_NEXT


def test_session_close_cutoff_is_configurable():
    late = returns.entry_rule_for(at(3, 20), True, ENTRY_AUTO, session_close=time(21, 0))
    assert late == ENTRY_SAME


# --------------------------------------------------------------------------- #
# The arithmetic
# --------------------------------------------------------------------------- #


def test_return_is_close_to_close_over_the_horizon():
    lookup = forward_return(SERIES, at(2, 14), horizon=2, timestamp_is_exact=True)
    assert lookup.status == STATUS_OK
    assert lookup.value.entry_price == 100.0
    assert lookup.value.exit_price == 120.0
    assert lookup.value.pct == pytest.approx(0.20)
    assert lookup.value.exit_date == date(2026, 3, 4)


def test_horizon_counts_sessions_not_calendar_days():
    # 3 Mar -> 6 Mar is 3 sessions here even though a weekend would intervene
    # in a real series; the index, not the date, does the counting.
    lookup = forward_return(SERIES, at(3, 14), horizon=3, timestamp_is_exact=True)
    assert lookup.value.entry_date == date(2026, 3, 3)
    assert lookup.value.exit_date == date(2026, 3, 6)


def test_horizon_must_be_positive():
    with pytest.raises(ValueError, match="at least 1 session"):
        forward_return(SERIES, at(2), horizon=0)


# --------------------------------------------------------------------------- #
# Everything that is not a return
# --------------------------------------------------------------------------- #


def test_a_signal_whose_future_has_not_happened_is_pending_not_zero():
    lookup = forward_return(SERIES, at(6, 14), horizon=1, timestamp_is_exact=True)
    assert lookup.status == STATUS_PENDING
    assert lookup.value is None


def test_signal_after_the_last_bar_has_no_entry():
    lookup = forward_return(SERIES, at(9, 14), horizon=1, timestamp_is_exact=True)
    assert lookup.status == STATUS_NO_ENTRY_BAR


def test_empty_history_is_reported_not_guessed():
    assert forward_return(PriceSeries("X", []), at(2), horizon=1).status == STATUS_NO_HISTORY


def test_missing_timestamp_is_reported():
    assert forward_return(SERIES, None, horizon=1).status == STATUS_NO_TIMESTAMP


def test_a_non_positive_entry_price_is_refused():
    series = PriceSeries("X", [(date(2026, 3, 2), 0.0), (date(2026, 3, 3), 10.0)])
    lookup = forward_return(series, at(1), horizon=1, timestamp_is_exact=True)
    assert lookup.status == STATUS_NO_ENTRY_BAR
