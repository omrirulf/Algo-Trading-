"""What the United States is holding in tanks.

For an oil or gas fund the Wednesday EIA release is the scheduled event of
the week. These pin the arithmetic, the applicability (most of the watchlist
must never see this block), and the behaviour with no key.
"""

from __future__ import annotations

import pytest

from orchestrator import energy


def rows(*values, start="2026-09-04"):
    """EIA's payload shape: newest first, under response.data."""
    return {"response": {"data": [
        {"period": f"2026-{9 - i // 4:02d}-{(28 - i) % 28 + 1:02d}", "value": v}
        for i, v in enumerate(values)
    ]}}


def flat(first, rest, count=40):
    return rows(first, *([rest] * count))


# --- who gets this section ----------------------------------------------------


@pytest.mark.parametrize("ticker,expected", [
    ("USO", ("crude", "gasoline", "distillate")),
    ("UNG", ("natural_gas",)),
    ("XLE", ("crude", "gasoline", "distillate", "natural_gas")),
    ("DBC", ("crude", "natural_gas")),
])
def test_an_energy_ticker_is_asked_about_the_series_that_bear_on_it(ticker, expected):
    assert energy.series_for(ticker) == expected


@pytest.mark.parametrize("ticker", ["GLD", "CORN", "TLT", "RSP", "EWZ", "MSFT", "NVDA"])
def test_everything_else_is_asked_about_nothing(ticker):
    assert energy.series_for(ticker) == ()
    assert energy.build_snapshot(ticker, {"crude": flat(424069, 424460)}) is None


def test_xom_is_deliberately_absent():
    """The most oil-exposed line on the watchlist, and still excluded: the
    company prompt is what every replay baseline was measured against, and XOM
    already has fundamentals, analysts and insider filings of its own."""
    assert "XOM" not in energy.COVERAGE
    assert energy.series_for("XOM") == ()


# --- the arithmetic -----------------------------------------------------------


def test_stocks_are_shown_in_millions_of_barrels():
    """"424,069" is a number nobody holds in their head."""
    stock = energy.build_stock("crude", flat(424069, 424460))
    assert stock.level == pytest.approx(424.069)
    assert "424.1 million barrels" in stock.as_text()


def test_gas_is_left_in_billions_of_cubic_feet_because_that_is_how_it_is_quoted():
    stock = energy.build_stock("natural_gas", flat(3200, 3140))
    assert stock.level == pytest.approx(3200.0)
    assert "3,200.0 billion cubic feet" in stock.as_text()


def test_a_rise_is_a_build_and_a_fall_is_a_draw():
    assert "(a build)" in energy.build_stock("crude", flat(425000, 424000)).as_text()
    assert "(a draw)" in energy.build_stock("crude", flat(424000, 425000)).as_text()


def test_an_unchanged_week_is_neither():
    text = energy.build_stock("crude", flat(424000, 424000)).as_text()
    assert "build" not in text and "draw" not in text


def test_a_single_reading_has_a_level_and_no_change():
    stock = energy.build_stock("crude", rows(424069))
    assert stock.level == pytest.approx(424.069)
    assert stock.change is None


def test_the_level_is_ranked_against_its_own_past_year():
    """"424 million barrels" means nothing to anyone who does not already know
    the range, which is the whole reason the percentile is here."""
    stock = energy.build_stock("crude", rows(*([500000] + [400000] * 40)))
    assert stock.percentile == pytest.approx(1.0)
    assert "100% percentile" in stock.as_text()
    assert "high for the time of year" in stock.as_text()


def test_a_low_level_is_named_too():
    stock = energy.build_stock("crude", rows(*([300000] + [400000] * 40)))
    assert "low for the time of year" in stock.as_text()


def test_an_ordinary_level_is_not_editorialised():
    stock = energy.build_stock("crude", rows(*([400000] + list(range(380000, 420000, 1000)))))
    text = stock.as_text()
    assert "percentile" in text
    assert "high for" not in text and "low for" not in text


def test_too_little_history_reports_no_percentile():
    """A rank over six weeks is not a rank, it is an opinion."""
    stock = energy.build_stock("crude", rows(*([400000] * 6)))
    assert stock.percentile is None
    assert "percentile" not in stock.as_text()

