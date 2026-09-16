"""How the crop is actually doing.

A grain fund tracks one thing: how much of it there will be. These pin the
seasonality, which is where this block could most easily lie -- a summer
condition reading shown in January as though it were news would be exactly
the usable-looking wrong number this project keeps having to remove.
"""

from __future__ import annotations

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


IMPROVING = season((20, 50, 10), (21, 49, 11), (22, 52, 10), (23, 53, 12), (24, 54, 12))
WORSENING = season((20, 58, 14), (21, 55, 12), (22, 52, 10), (23, 48, 9), (24, 45, 8))
STEADY = season((22, 52, 10), (23, 52, 11), (24, 53, 10))


# --- who gets this section ----------------------------------------------------


@pytest.mark.parametrize("ticker,crop", [
    ("CORN", "corn"), ("WEAT", "wheat"), ("SOYB", "soybeans"), ("CANE", "sugarcane"),
])
def test_each_grain_fund_maps_to_its_crop(ticker, crop):
    assert crops.commodity_for(ticker)[1] == crop


@pytest.mark.parametrize("ticker", ["GLD", "USO", "UNG", "CPER", "SLV", "XLE", "MSFT"])
def test_everything_else_maps_to_nothing(ticker):
    assert crops.commodity_for(ticker) is None
    assert crops.build_snapshot(ticker, IMPROVING, year=2026) is None


# --- the measure --------------------------------------------------------------


def test_good_and_excellent_are_added_and_the_other_buckets_ignored():
    """It is the figure the grain trade quotes, and "poor" is not part of it."""
    assert crops.good_or_excellent(season((24, 54, 12))) == {24: 66.0}


def test_weeks_come_back_in_order():
    weekly = crops.good_or_excellent(season((24, 54, 12), (20, 50, 10), (22, 52, 10)))
    assert list(weekly) == [20, 22, 24]


def test_a_withheld_value_is_skipped_rather_than_read_as_zero():
    """USDA writes a suppressed figure as "(D)"."""
    rows = [{"reference_period_desc": "WEEK #24", "unit_desc": "PCT GOOD", "Value": "(D)"},
            {"reference_period_desc": "WEEK #24", "unit_desc": "PCT EXCELLENT", "Value": "12"}]
    assert crops.good_or_excellent(rows) == {24: 12.0}


@pytest.mark.parametrize("label", ["WEEK 24", "MARKETING YEAR", "", None, "WEEK #"])
def test_a_row_that_is_not_a_weekly_reading_is_skipped(label):
    rows = [{"reference_period_desc": label, "unit_desc": "PCT GOOD", "Value": "54"}]
    assert crops.good_or_excellent(rows) == {}


@pytest.mark.parametrize("hostile", [None, 17, "nope", [1, 2, 3], [None]])
def test_a_payload_of_the_wrong_shape_degrades_rather_than_raising(hostile):
    assert crops.good_or_excellent(hostile) == {}


# --- the trend, which is the signal -------------------------------------------


def test_an_improving_crop_is_named():
    snapshot = crops.build_snapshot("CORN", IMPROVING, year=2026)
    assert snapshot.condition == 66.0
    assert snapshot.week == 24
    assert "improving" in "\n".join(snapshot.as_lines())


def test_a_deteriorating_crop_is_named():
    """Three weeks running is a supply story whatever the level."""
    assert "deteriorating" in "\n".join(
        crops.build_snapshot("CORN", WORSENING, year=2026).as_lines())


def test_noise_of_a_point_or_two_is_called_steady():
    assert "steady" in "\n".join(
        crops.build_snapshot("CORN", STEADY, year=2026).as_lines())


def test_too_few_weeks_says_so_rather_than_inventing_a_trend():
    snapshot = crops.build_snapshot("CORN", season((24, 54, 12)), year=2026)
    assert snapshot.change is None
    assert "not enough readings to say" in "\n".join(snapshot.as_lines())


def test_the_same_week_last_year_is_the_comparison_that_matters():
    snapshot = crops.build_snapshot(
        "CORN", IMPROVING, season((24, 48, 9)), year=2026)
    text = "\n".join(snapshot.as_lines())
    assert snapshot.last_year == 57.0
    assert "Same week last year: 57%" in text and "+9 points" in text


def test_last_year_is_matched_on_the_week_not_on_the_latest_reading():
    """Week 24 against week 24. Comparing to last year's *final* week would
    flatter or damn the crop by where the season ended, not by how it is."""
    snapshot = crops.build_snapshot(
        "CORN", IMPROVING, season((24, 48, 9), (30, 20, 5)), year=2026)
    assert snapshot.last_year == 57.0


def test_no_prior_year_simply_leaves_the_line_out():
    text = "\n".join(crops.build_snapshot("CORN", IMPROVING, year=2026).as_lines())
    assert "Same week last year" not in text

