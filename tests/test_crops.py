"""How the crop is actually doing.

A grain fund tracks one thing: how much of it there will be. These pin the
seasonality, which is where this block could most easily lie -- a summer
condition reading shown in January as though it were news would be exactly
the usable-looking wrong number this project keeps having to remove.
"""

from __future__ import annotations

from datetime import date

import pytest

from orchestrator import crops


def season(*weeks, poor=9):
    """USDA's row shape: one row per bucket per week."""
    rows = []
    for week, good, excellent in weeks:
        rows += [
            {"reference_period_desc": f"WEEK #{week}", "unit_desc": "PCT GOOD",
             "Value": str(good)},
            {"reference_period_desc": f"WEEK #{week}", "unit_desc": "PCT EXCELLENT",
             "Value": str(excellent)},
            {"reference_period_desc": f"WEEK #{week}", "unit_desc": "PCT POOR",
             "Value": str(poor)},
        ]
    return rows


IMPROVING = season((34, 50, 10), (35, 49, 11), (36, 52, 10), (37, 53, 12), (38, 54, 12))
WORSENING = season((34, 58, 14), (35, 55, 12), (36, 52, 10), (37, 48, 9), (38, 45, 8))
STEADY = season((36, 52, 10), (37, 52, 11), (38, 53, 10))


# --- who gets this section ----------------------------------------------------


@pytest.mark.parametrize("ticker,crop", [
    ("CORN", "corn"), ("WEAT", "wheat"), ("SOYB", "soybeans"), ("CANE", "sugarcane"),
])
def test_each_grain_fund_maps_to_its_crop(ticker, crop):
    assert crops.commodity_for(ticker)[1] == crop


@pytest.mark.parametrize("ticker", ["GLD", "USO", "UNG", "CPER", "SLV", "XLE", "MSFT"])
def test_everything_else_maps_to_nothing(ticker):
    assert crops.commodity_for(ticker) is None
    assert crops.build_snapshot(ticker, IMPROVING, year=2026, today=SEPTEMBER) is None


# --- the measure --------------------------------------------------------------


def test_good_and_excellent_are_added_and_the_other_buckets_ignored():
    """It is the figure the grain trade quotes, and "poor" is not part of it."""
    assert crops.good_or_excellent(season((38, 54, 12))) == {38: 66.0}


def test_weeks_come_back_in_order():
    weekly = crops.good_or_excellent(season((38, 54, 12), (34, 50, 10), (36, 52, 10)))
    assert list(weekly) == [34, 36, 38]


def test_a_withheld_value_is_skipped_rather_than_read_as_zero():
    """USDA writes a suppressed figure as "(D)"."""
    rows = [{"reference_period_desc": "WEEK #38", "unit_desc": "PCT GOOD", "Value": "(D)"},
            {"reference_period_desc": "WEEK #38", "unit_desc": "PCT EXCELLENT", "Value": "12"}]
    assert crops.good_or_excellent(rows) == {38: 12.0}


@pytest.mark.parametrize("label", ["WEEK 24", "MARKETING YEAR", "", None, "WEEK #"])
def test_a_row_that_is_not_a_weekly_reading_is_skipped(label):
    rows = [{"reference_period_desc": label, "unit_desc": "PCT GOOD", "Value": "54"}]
    assert crops.good_or_excellent(rows) == {}


@pytest.mark.parametrize("hostile", [None, 17, "nope", [1, 2, 3], [None]])
def test_a_payload_of_the_wrong_shape_degrades_rather_than_raising(hostile):
    assert crops.good_or_excellent(hostile) == {}


# --- the trend, which is the signal -------------------------------------------


def test_an_improving_crop_is_named():
    snapshot = crops.build_snapshot("CORN", IMPROVING, year=2026, today=SEPTEMBER)
    assert snapshot.condition == 66.0
    assert snapshot.week == 38
    assert "improving" in "\n".join(snapshot.as_lines())


def test_a_deteriorating_crop_is_named():
    """Three weeks running is a supply story whatever the level."""
    assert "deteriorating" in "\n".join(
        crops.build_snapshot("CORN", WORSENING, year=2026, today=SEPTEMBER).as_lines())


def test_noise_of_a_point_or_two_is_called_steady():
    assert "steady" in "\n".join(
        crops.build_snapshot("CORN", STEADY, year=2026, today=SEPTEMBER).as_lines())


def test_too_few_weeks_says_so_rather_than_inventing_a_trend():
    snapshot = crops.build_snapshot("CORN", season((38, 54, 12)), year=2026, today=SEPTEMBER)
    assert snapshot.change is None
    assert "not enough readings to say" in "\n".join(snapshot.as_lines())


def test_the_same_week_last_year_is_the_comparison_that_matters():
    snapshot = crops.build_snapshot(
        "CORN", IMPROVING, season((38, 48, 9)), year=2026, today=SEPTEMBER)
    text = "\n".join(snapshot.as_lines())
    assert snapshot.last_year == 57.0
    assert "Same week last year: 57%" in text and "+9 points" in text


def test_last_year_is_matched_on_the_week_not_on_the_latest_reading():
    """Week 38 against week 38. Comparing to last year's *final* week would
    flatter or damn the crop by where the season ended, not by how it is."""
    snapshot = crops.build_snapshot(
        "CORN", IMPROVING, season((38, 48, 9), (30, 20, 5)), year=2026,
        today=SEPTEMBER)
    assert snapshot.last_year == 57.0


def test_no_prior_year_simply_leaves_the_line_out():
    text = "\n".join(crops.build_snapshot("CORN", IMPROVING, year=2026, today=SEPTEMBER).as_lines())
    assert "Same week last year" not in text



# --- the reading that looked freshest and was ten months old -------------------
#
# The live probe printed, in September:
#
#     CORN:  week 37 of 2026
#     SOYB:  week 37 of 2026
#     WEAT:  week 47 of 2026
#
# Week 47 had not happened yet. USDA labels winter wheat by its *harvest*
# year, so a request for 2026 returns the reading from November 2025 under a
# 2026 label -- which prints as the freshest number in the block while being
# ten months old. Exactly the class of usable-looking wrong number this
# project keeps finding, and the reason every reading is now aged against the
# calendar rather than against the other readings.

SEPTEMBER = date(2026, 9, 16)  # week 38


@pytest.mark.parametrize("week,age", [
    (38, 0), (37, 1), (36, 2), (33, 5), (32, 6), (47, 43), (1, 37), (39, 51),
])
def test_a_reading_is_aged_against_the_calendar_and_wraps_the_year(week, age):
    assert crops.weeks_old(week, SEPTEMBER) == age


def test_the_winter_wheat_reading_that_started_this_is_dropped():
    rows = season((45, 38, 8), (46, 39, 9), (47, 40, 8))
    assert crops.build_snapshot("WEAT", rows, year=2026, today=SEPTEMBER) is None


def test_a_crop_actually_in_the_ground_is_kept():
    rows = season((35, 45, 10), (36, 46, 11), (37, 47, 10))
    snapshot = crops.build_snapshot("CORN", rows, year=2026, today=SEPTEMBER)
    assert snapshot.week == 37 and snapshot.condition == 57.0


def test_a_harvested_crop_stops_being_reported_rather_than_going_stale():
    """Corn's last reading is week 37. Read in November it is two months old,
    and two months of silence is not a steady crop."""
    rows = season((35, 45, 10), (36, 46, 11), (37, 47, 10))
    assert crops.build_snapshot("CORN", rows, year=2026, today=date(2026, 11, 18)) is None


def test_stale_weeks_are_dropped_while_fresh_ones_in_the_same_set_survive():
    """A set of rows can be internally consistent and still be half stale."""
    rows = season((47, 40, 8), (36, 46, 11), (37, 47, 10))
    snapshot = crops.build_snapshot("CORN", rows, year=2026, today=SEPTEMBER)
    assert snapshot.history == [57.0, 57.0]
    assert 40 + 8 not in snapshot.history


def test_the_boundary_is_where_the_constant_says_it_is():
    edge = 38 - crops.MAX_READING_AGE_WEEKS
    assert crops.build_snapshot(
        "CORN", season((edge, 45, 10)), year=2026, today=SEPTEMBER) is not None
    assert crops.build_snapshot(
        "CORN", season((edge - 1, 45, 10)), year=2026, today=SEPTEMBER) is None
