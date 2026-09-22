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


# --------------------------------------------------------------------------- #
# Finality: a bar is a close only once the session that made it is over
# --------------------------------------------------------------------------- #

from datetime import datetime as _dt, timezone as _tz  # noqa: E402

from analysis.returns import (  # noqa: E402
    MARKET_TZ,
    YFinancePriceSource,
    final_bars,
    last_final_session,
)


def test_before_the_close_the_last_final_session_is_yesterday():
    # 14:27 New York on Monday 21 Sep 2026 (18:27 UTC under EDT): the day's
    # bar is an intraday print. The 37.0% run was made at exactly this time.
    now = _dt(2026, 9, 21, 18, 27, tzinfo=_tz.utc)
    assert now.astimezone(MARKET_TZ).hour == 14
    assert last_final_session(now) == date(2026, 9, 20)


def test_after_the_close_and_the_grace_the_last_final_session_is_today():
    # 17:05 New York (21:05 UTC): the 32.6% run.
    assert last_final_session(_dt(2026, 9, 21, 21, 5, tzinfo=_tz.utc)) == date(2026, 9, 21)


def test_the_minutes_right_after_the_bell_are_not_final_yet():
    # 16:10 New York: the closing auction has printed but the vendor's bar
    # may still be settling. Yesterday is the last bar trusted.
    assert last_final_session(_dt(2026, 9, 21, 20, 10, tzinfo=_tz.utc)) == date(2026, 9, 20)
    assert last_final_session(_dt(2026, 9, 21, 20, 30, tzinfo=_tz.utc)) == date(2026, 9, 21)


def test_finality_is_judged_on_the_exchange_clock_not_utc():
    # 01:06 UTC on Tuesday 22 Sep is still Monday evening in New York, and
    # Monday's bar is final. A UTC-date rule would have said Sunday.
    assert last_final_session(_dt(2026, 9, 22, 1, 6, tzinfo=_tz.utc)) == date(2026, 9, 21)


def test_a_naive_clock_is_refused():
    with pytest.raises(ValueError):
        last_final_session(_dt(2026, 9, 21, 18, 0))


def test_final_bars_drops_everything_after_the_cutoff_and_keeps_all_without_one():
    bars = [(date(2026, 9, 18), 1.0), (date(2026, 9, 21), 2.0), (date(2026, 9, 22), 3.0)]
    assert final_bars(bars, date(2026, 9, 21)) == bars[:2]
    assert final_bars(bars, None) == bars


def test_the_price_source_never_hands_out_a_bar_after_its_cutoff():
    source = YFinancePriceSource(final_through=date(2026, 9, 21))
    source._fetch = lambda ticker, start, end: [
        (date(2026, 9, 18), 1.0), (date(2026, 9, 21), 2.0), (date(2026, 9, 22), 3.0),
    ]
    series = source.closes("NVDA", date(2026, 9, 1), date(2026, 9, 30))
    assert [b[0] for b in series.bars] == [date(2026, 9, 18), date(2026, 9, 21)]
    # And the cache holds the truncated series, so a later call cannot see more.
    assert source.closes("NVDA", date(2026, 9, 1), date(2026, 9, 30)).bars == series.bars
