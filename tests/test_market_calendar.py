"""The free gate: a weekend or a listed NYSE holiday, known without asking anyone."""

from __future__ import annotations

import logging
from datetime import date, timedelta

from config.market_calendar import LAST_COVERED_YEAR, NYSE_HOLIDAYS, is_trading_day


def test_an_ordinary_weekday_trades():
    assert is_trading_day(date(2026, 9, 16))  # a Wednesday, not listed


def test_weekends_do_not_trade():
    assert not is_trading_day(date(2026, 9, 19))  # Saturday
    assert not is_trading_day(date(2026, 9, 20))  # Sunday


def test_every_listed_holiday_is_a_weekday():
    """A holiday landing on a weekend would be a data-entry mistake here --
    the observed-day shift belongs in the list, not left for a weekend that
    already doesn't trade to quietly absorb it."""
    for day in NYSE_HOLIDAYS:
        assert day.weekday() < 5, f"{day} is a weekend; check the observed-date shift"


def test_a_listed_holiday_does_not_trade():
    assert not is_trading_day(date(2026, 12, 25))  # Christmas, a Friday


def test_good_friday_has_no_calendar_rule_so_it_is_checked_by_hand():
    assert date(2026, 4, 3) in NYSE_HOLIDAYS


def test_a_half_day_is_not_in_the_list():
    """The day after Thanksgiving: the market is open, just shorter. Treating
    it as closed would cost a real session rather than a wasted one."""
    assert date(2026, 11, 27) not in NYSE_HOLIDAYS
    assert is_trading_day(date(2026, 11, 27))


def test_a_year_past_the_list_still_answers_but_says_so(caplog):
    with caplog.at_level(logging.WARNING):
        result = is_trading_day(date(LAST_COVERED_YEAR + 1, 6, 15))
    assert result is True  # degrades to "trading", the pre-existing behaviour
    assert "assuming" in caplog.text
    assert str(LAST_COVERED_YEAR + 1) in caplog.text


def test_a_year_past_the_list_logs_nothing_when_it_lands_on_a_weekend():
    # The weekday check runs regardless; only the "no data either way" case
    # needs a log line, and a weekend never reaches that ambiguity.
    jan1 = date(LAST_COVERED_YEAR + 1, 1, 1)
    future_saturday = jan1 + timedelta(days=(5 - jan1.weekday()) % 7)
    assert future_saturday.weekday() == 5
    assert not is_trading_day(future_saturday)
