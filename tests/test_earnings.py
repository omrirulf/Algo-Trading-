"""Whether a company beats its own guidance.

The analyst block says what is expected. This says whether this particular
company tends to meet expectations -- which is the thing that bears on
whether the next one will be met, and which two companies on the same
consensus can differ on completely.
"""

from __future__ import annotations

import pytest

from orchestrator import earnings


def quarter(period, actual, estimate, surprise):
    return {"period": period, "actual": actual, "estimate": estimate,
            "surprisePercent": surprise}


MSFT = [
    quarter("2026-06-30", 4.74, 4.3274, 9.5346),
    quarter("2026-03-31", 3.46, 3.22, 7.45),
    quarter("2025-12-31", 3.23, 3.22, 0.31),
    quarter("2025-09-30", 2.99, 3.10, -3.55),
]


# --- the record ---------------------------------------------------------------


def test_the_record_is_counted_and_then_spelled_out():
    snapshot = earnings.build_snapshot("MSFT", MSFT)
    assert (snapshot.beats, snapshot.in_line, snapshot.misses) == (2, 1, 1)
    lines = snapshot.as_lines()
    assert lines[0] == "Earnings record, last 4 quarters: 2 beats, 1 in line, 1 missed"
    assert "2026-06-30 beat by 10%" in lines[1]
    assert "2025-12-31 in line" in lines[1]
    assert "2025-09-30 missed by 4%" in lines[1]


def test_a_rounding_difference_is_not_a_beat():
    """Consensus is an average of estimates that were never meant to be
    exact, so a third of a per cent is in line."""
    assert earnings.build_snapshot("X", [quarter("q", 3.23, 3.22, 0.31)]).in_line == 1


@pytest.mark.parametrize("surprise,verdict", [
    (9.5, "beat"), (2.1, "beat"), (2.0, "in line"), (0.0, "in line"),
    (-2.0, "in line"), (-2.1, "missed"), (-92.0, "missed"),
])
def test_the_line_between_a_beat_and_noise_is_where_it_says_it_is(surprise, verdict):
    snapshot = earnings.build_snapshot("X", [quarter("q", 1.0, 1.0, surprise)])
    assert snapshot.quarters[0].verdict == verdict


def test_only_a_year_is_read_back():
    """Four quarters is where a habit is a habit rather than a run."""
    many = [quarter(f"q{i}", 1.0, 0.9, 11.0) for i in range(12)]
    assert len(earnings.build_snapshot("X", many).quarters) == earnings.MAX_QUARTERS


def test_one_quarter_is_not_pluralised():
    assert earnings.build_snapshot("TEVA", MSFT[:1]).as_lines()[0].startswith(
        "Earnings record, last quarter:")


# --- the number that is not a number ------------------------------------------


def test_an_absurd_surprise_keeps_its_direction_and_drops_its_percentage():
    """A penny against a forecast of nothing prints thousands of per cent.
    "Beat" is still true; "beat by 9,900%" is not worth saying."""
    snapshot = earnings.build_snapshot("X", [quarter("q", 0.01, 0.0001, 9900.0)])
    assert snapshot.quarters[0].surprise_pct is None
    assert snapshot.quarters[0].verdict == "beat"
    assert snapshot.as_lines()[1].strip() == "q beat"


def test_a_missing_surprise_falls_back_to_comparing_the_two_numbers():
    snapshot = earnings.build_snapshot("X", [quarter("q", 2.0, 3.0, None)])
    assert snapshot.quarters[0].verdict == "missed"


def test_with_neither_a_percentage_nor_both_numbers_it_says_unknown():
    snapshot = earnings.build_snapshot("X", [quarter("q", None, None, None)])
    assert snapshot.quarters[0].verdict == "unknown"
    assert "unknown" in snapshot.as_lines()[1]

