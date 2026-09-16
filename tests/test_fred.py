"""What the economy actually did, as opposed to what traders think it will.

`MACRO` gives prices, which are free. These are the official releases, which
arrive through the one module allowed to hold a key. Pure parsing here: what
is pinned is the arithmetic and the one shape FRED uses that reads wrong if
taken at face value.
"""

from __future__ import annotations

import pytest

from orchestrator import fred


def obs(*pairs):
    return {"observations": [{"date": d, "value": v} for d, v in pairs]}


RELEASES = {
    "inflation": fred.Release("inflation", 2.9, "2026-08-01", "percent"),
    "unemployment": fred.Release("unemployment", 4.1, "2026-08-01", "percent"),
    "jobless_claims": fred.Release("jobless_claims", 206000.0, "2026-09-05", "thousands"),
    "policy_rate": fred.Release("policy_rate", 4.25, "2026-09-15", "percent"),
    "breakeven": fred.Release("breakeven", 2.44, "2026-09-15", "percent"),
}


# --- FRED writes a missing value as a full stop -------------------------------

# --- FRED writes a missing value as a full stop -------------------------------


def test_a_missing_observation_is_skipped_rather_than_read_as_zero():
    """FRED writes an absent value as "." rather than omitting the row. Read
    carelessly that floats to zero, and an unemployment rate of 0.0% is
    exactly the kind of usable-looking wrong number this project keeps
    finding."""
    release = fred.parse_release("unemployment", "percent",
                                 obs(("2026-09-01", "."), ("2026-08-01", "4.1")))
    assert release.value == 4.1
    assert release.date == "2026-08-01"


def test_a_series_that_is_nothing_but_gaps_reports_nothing():
    assert fred.parse_release("unemployment", "percent",
                              obs(("2026-09-01", "."), ("2026-08-01", "."))) is None


@pytest.mark.parametrize("payload", [None, {}, {"observations": "nope"}, 17, []])
def test_a_payload_of_the_wrong_shape_degrades_rather_than_raising(payload):
    assert fred.parse_release("inflation", "percent", payload) is None


# --- how the numbers read -----------------------------------------------------


def test_the_two_lines_separate_what_happened_from_what_is_priced():
    lines = fred.as_lines(RELEASES)
    assert len(lines) == 2
    assert lines[0].startswith("Latest US data:")
    assert lines[1].startswith("Policy and expectations:")


def test_claims_read_in_thousands_because_206000_is_not_how_anyone_says_it():
    assert "jobless claims 206k" in fred.as_lines(RELEASES)[0]


def test_inflation_is_asked_for_as_a_year_on_year_percentage():
    """Deriving it here from index levels would put an off-by-one month
    somewhere nobody would ever look."""
    units = {series: unit for series, _, unit, _ in fred.SERIES}
    assert units["CPIAUCSL"] == "pc1"


def test_the_breakeven_is_described_rather_than_left_as_a_number():
    assert "market expects 2.4% inflation over 10 years" in fred.as_lines(RELEASES)[1]


def test_a_partial_set_prints_only_what_arrived():
    lines = fred.as_lines({"unemployment": RELEASES["unemployment"]})
    assert lines == ["Latest US data: unemployment 4.1% (2026-08-01)"]


def test_only_the_priced_half_still_prints():
    lines = fred.as_lines({"policy_rate": RELEASES["policy_rate"]})
    assert lines == ["Policy and expectations: Fed target 4.25%"]


def test_releases_are_built_from_raw_payloads_keyed_by_label():
    """`orchestrator.sources` hands over raw observations; turning them into
    numbers is this module's job, and it is the only job it has."""
    built = fred.build_releases({
        "unemployment": obs(("2026-08-01", "4.1")),
        "inflation": obs(("2026-09-01", "."), ("2026-08-01", "2.9")),
    })
    assert set(built) == {"unemployment", "inflation"}
    assert built["inflation"].value == 2.9
    assert built["unemployment"].render == "percent"


def test_a_series_that_never_arrived_is_simply_not_in_the_result():
    assert fred.build_releases({}) == {}
    assert fred.build_releases(None) == {}
    assert fred.build_releases({"inflation": obs(("2026-08-01", "."))}) == {}
