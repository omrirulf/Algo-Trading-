"""A fund's share count is its money in and out.

The insider slot stood empty for every fund on the watchlist. An ETF has no
insiders, but it does have something better suited to the question: its share
count is not fixed, so creations and redemptions *are* the flow, and unlike a
rating or a target they have already happened.

These pin the windowing -- which is where the honesty lives, because Yahoo's
series is irregular and a window that quietly measured two hundred days while
calling itself a week would be worse than no window at all.
"""

from __future__ import annotations

import pytest

from orchestrator import flows

pd = pytest.importorskip("pandas")


def series(values, start="2026-06-01", freq="7D"):
    return pd.Series(values, index=pd.date_range(start, periods=len(values), freq=freq))


GROWING = series([100e6, 101e6, 103e6, 104e6, 104e6, 106e6, 109e6,
                  112e6, 115e6, 118e6, 121e6, 126e6, 130e6, 134e6])
SHRINKING = series([200e6, 196e6, 191e6, 188e6, 184e6, 180e6, 175e6,
                    171e6, 168e6, 164e6, 160e6, 155e6, 151e6, 148e6])
FLAT = series([50e6] * 14)


# --- what it says -------------------------------------------------------------


def test_creations_read_as_money_coming_in():
    text = "\n".join(flows.build_snapshot("XLE", GROWING, price=92.5).as_lines())
    assert "Direction: money coming in" in text
    assert "1 week: +3.1%" in text


def test_redemptions_read_as_money_going_out():
    text = "\n".join(flows.build_snapshot("XLE", SHRINKING, price=10.0).as_lines())
    assert "Direction: money going out" in text


def test_an_unchanged_share_count_reads_as_flat_not_as_missing():
    """Nobody creating and nobody redeeming is real information."""
    snapshot = flows.build_snapshot("XLE", FLAT, price=10.0)
    assert "Direction: flat" in "\n".join(snapshot.as_lines())
    assert snapshot.windows and all(w.change == 0.0 for w in snapshot.windows)


def test_the_change_is_quoted_in_money_as_well_as_percent():
    """3% of a $70bn fund and 3% of a $400m fund are not the same event."""
    text = "\n".join(flows.build_snapshot("XLE", GROWING, price=100.0).as_lines())
    assert "$" in text or "B" in text or "M" in text
    week = next(w for w in flows.build_snapshot("XLE", GROWING, price=100.0).windows
                if w.label == "1 week")
    assert week.dollars == pytest.approx(4e8)


def test_without_a_price_the_percent_still_lands_and_the_money_does_not():
    snapshot = flows.build_snapshot("XLE", GROWING)
    assert snapshot.windows[0].change is not None
    assert all(w.dollars is None for w in snapshot.windows)
    assert snapshot.net_assets is None


def test_the_caveat_travels_with_the_number():
    """A fund can bleed shares through a rally. The prompt says so rather than
    leaving the model to read a flow as a forecast."""
    text = "\n".join(flows.build_snapshot("XLE", GROWING, price=10.0).as_lines())
    assert "conviction" in text and "forecast" in text


# --- the windowing, which is where it could lie -------------------------------


def test_every_window_reports_the_span_it_actually_measured():
    for window in flows.build_snapshot("XLE", GROWING, price=10.0).windows:
        assert window.days and f"over {window.days}d" in window.as_text()


def test_a_window_is_never_measured_over_less_than_the_span_it_names():
    for window in flows.build_snapshot("XLE", GROWING, price=10.0).windows:
        span = dict(flows.WINDOWS)[window.label]
        assert window.days >= span


def test_a_window_the_series_is_too_short_for_is_dropped_not_stretched():
    """Three weeks of history cannot answer a three-month question."""
    labels = [w.label for w in flows.build_snapshot("XLE", series([1e6, 2e6, 3e6, 4e6])).windows]
    assert "1 week" in labels
    assert "3 months" not in labels


def test_a_sparse_series_does_not_get_a_week_measured_over_a_year():
    """A fund that reports twice a year has no weekly flow to report."""
    sparse = pd.Series(
        [50e6, 52e6, 51e6],
        index=pd.to_datetime(["2025-01-01", "2025-07-01", "2026-01-01"]),
    )
    labels = [w.label for w in flows.build_snapshot("XLE", sparse).windows]
    assert "1 week" not in labels and "1 month" not in labels


def test_two_labels_landing_on_the_same_reading_are_printed_once():
    monthly = series([10e6, 11e6, 12e6, 13e6], freq="30D")
    windows = flows.build_snapshot("XLE", monthly).windows
    assert len({w.days for w in windows}) == len(windows)


# --- degrading rather than raising --------------------------------------------


def test_too_few_readings_is_no_section_rather_than_a_section_of_blanks():
    assert flows.build_snapshot("XLE", series([1e6, 2e6])) is None
    assert flows.build_snapshot("XLE", None) is None
    assert flows.build_snapshot("XLE", series([])) is None


def test_a_zero_or_missing_share_count_is_skipped_not_divided_by():
    mixed = series([0.0, float("nan"), 100e6, 102e6, 105e6, 108e6, 110e6])
    snapshot = flows.build_snapshot("XLE", mixed, price=10.0)
    assert snapshot is not None and snapshot.points == 5
    assert all(w.change is not None for w in snapshot.windows)


@pytest.mark.parametrize("hostile", [{"a": "b"}, 17, object(), [1, 2, 3]])
def test_a_payload_of_the_wrong_shape_degrades_rather_than_raising(hostile):
    assert flows.build_snapshot("XLE", hostile) is None


def test_the_flat_threshold_is_what_separates_noise_from_a_flow():
    tiny = series([100e6, 100e6, 100e6, 100_100_000.0])
    text = "\n".join(flows.build_snapshot("XLE", tiny).as_lines())
    assert "Direction: flat" in text
