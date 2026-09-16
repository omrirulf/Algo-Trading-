"""What it costs to hold a commodity through a fund.

Gold, silver and copper had four sections and no numbers. This is the number
that belongs there, and for a commodity fund it is arguably the most
important fact about the instrument: USO once lost most of its value over a
stretch in which crude oil ended where it started, and the difference went
into rolling contracts.
"""

from __future__ import annotations

import pytest

from orchestrator import carry

pd = pytest.importorskip("pandas")

DAYS = 300


def hist(values):
    return pd.DataFrame({"Close": values})


def flat(price, n=DAYS):
    return hist([price] * n)


def bleeding(start, yearly_pct, n=DAYS):
    """A fund losing ``yearly_pct`` a year against a flat commodity."""
    daily = yearly_pct / 100.0 / 252.0
    return hist([start * (1 + daily) ** i for i in range(n)])


# --- who gets this section ----------------------------------------------------


@pytest.mark.parametrize("ticker,symbol,name", [
    ("GLD", "GC=F", "gold"), ("SLV", "SI=F", "silver"), ("CPER", "HG=F", "copper"),
    ("USO", "CL=F", "crude oil"), ("UNG", "NG=F", "natural gas"),
    ("CORN", "ZC=F", "corn"), ("WEAT", "ZW=F", "wheat"),
    ("SOYB", "ZS=F", "soybeans"), ("CANE", "SB=F", "sugar"),
])
def test_every_single_commodity_fund_has_a_reference(ticker, symbol, name):
    assert carry.reference_for(ticker) == (symbol, name)


def test_the_nine_commodity_funds_are_exactly_the_ones_covered():
    from config.instruments import COMMODITY_FUNDS

    assert set(carry.REFERENCES) == set(COMMODITY_FUNDS)


@pytest.mark.parametrize("ticker", ["DBC", "DBA"])
def test_a_basket_is_absent_because_it_has_no_single_commodity(ticker):
    """A basket spanning a dozen contracts has nothing to be measured
    against, and inventing one would be worse than leaving it out."""
    assert carry.reference_for(ticker) is None
    assert carry.build_snapshot(ticker, flat(20.0), flat(70.0)) is None


@pytest.mark.parametrize("ticker", ["XLE", "TLT", "RSP", "MSFT", "EWZ"])
def test_everything_that_is_not_a_commodity_fund_is_absent(ticker):
    assert carry.build_snapshot(ticker, flat(100.0), flat(70.0)) is None


# --- the measurement ----------------------------------------------------------


def test_a_fund_bleeding_to_contango_is_measured_and_named():
    """The USO case: crude flat, the fund down, the gap is the roll."""
    snapshot = carry.build_snapshot("USO", bleeding(100.0, -9.0), flat(70.0))
    annual = snapshot.headline.annualised_pct
    assert annual == pytest.approx(-9.0, abs=0.6)
    text = "\n".join(snapshot.as_lines())
    assert "rolling contracts costs this fund real money" in text
    assert "crude oil" in text


def test_a_physically_backed_fund_costs_about_its_fee():
    """GLD holds bullion. Near zero here is a finding, not a missing number."""
    snapshot = carry.build_snapshot("GLD", bleeding(200.0, -0.4), flat(2000.0))
    assert snapshot.headline.annualised_pct == pytest.approx(-0.4, abs=0.3)
    assert "close to nothing, as a physically backed fund should be" in \
        "\n".join(snapshot.as_lines())


def test_backwardation_is_reported_as_the_roll_paying_the_fund():
    snapshot = carry.build_snapshot("USO", bleeding(100.0, +6.0), flat(70.0))
    assert "the roll has been paying this fund" in "\n".join(snapshot.as_lines())


def test_the_gap_is_the_fund_minus_the_commodity_not_the_funds_own_return():
    """A fund that rose 20% while the commodity rose 30% still lost 10 points
    to its structure. Reading the fund's return alone would miss that."""
    n = DAYS
    commodity = hist([100.0 * (1.30 ** (i / 252.0)) for i in range(n)])
    fund = hist([50.0 * (1.20 ** (i / 252.0)) for i in range(n)])
    snapshot = carry.build_snapshot("CPER", fund, commodity)
    year = next(w for w in snapshot.windows if w.label == "12 months")
    assert year.fund > 0 and year.commodity > 0
    assert year.gap < 0


def test_every_window_that_both_histories_reach_is_measured():
    labels = [w.label for w in carry.build_snapshot(
        "GLD", flat(200.0), flat(2000.0)).windows]
    assert labels == ["3 months", "6 months", "12 months"]


def test_a_short_history_keeps_the_windows_it_can_reach():
    """Four months of bars answers the quarter and nothing longer."""
    labels = [w.label for w in carry.build_snapshot(
        "GLD", flat(200.0, n=80), flat(2000.0, n=80)).windows]
    assert labels == ["3 months"]


def test_the_headline_is_the_longest_window_because_a_year_of_rolls_beats_a_quarter():
    snapshot = carry.build_snapshot("USO", bleeding(100.0, -9.0), flat(70.0))
    assert snapshot.headline.label == "12 months"


# --- degrading rather than raising --------------------------------------------


def test_too_little_overlap_is_no_section_rather_than_a_gap_of_zero():
    """"No difference" and "we could not compare" are opposite findings, and
    only one of them is good news."""
    assert carry.build_snapshot("GLD", flat(200.0, n=10), flat(2000.0)) is None
    assert carry.build_snapshot("GLD", flat(200.0), flat(2000.0, n=10)) is None


def test_a_missing_history_is_no_section():
    assert carry.build_snapshot("GLD", None, flat(2000.0)) is None
    assert carry.build_snapshot("GLD", flat(200.0), None) is None


@pytest.mark.parametrize("hostile", [
    17, "nope", pd.DataFrame({"Open": [1.0]}), hist([float("nan")] * DAYS),
    hist([0.0] * DAYS), hist([-5.0] * DAYS),
])
def test_a_payload_of_the_wrong_shape_degrades_rather_than_raising(hostile):
    assert carry.build_snapshot("GLD", hostile, flat(2000.0)) is None
    assert carry.build_snapshot("GLD", flat(200.0), hostile) is None


def test_a_gap_in_the_bars_is_skipped_rather_than_read_as_a_price():
    values = [200.0] * DAYS
    values[5] = float("nan")
    snapshot = carry.build_snapshot("GLD", hist(values), flat(2000.0))
    assert snapshot is not None
    assert all(w.gap == pytest.approx(0.0) for w in snapshot.windows)


# --- the caveats travel with the number ---------------------------------------


def test_the_three_limits_are_stated_rather_than_left_implied():
    text = "\n".join(carry.build_snapshot("USO", bleeding(100.0, -9.0), flat(70.0)).as_lines())
    assert "it is history rather than a forecast" in text
    assert "it is not a direction" in text
    assert "a tailwind for a short" in text


def test_the_mechanism_is_explained_not_just_the_number():
    """The model should not have to already know what a roll is."""
    text = "\n".join(carry.build_snapshot("UNG", bleeding(20.0, -20.0), flat(3.0)).as_lines())
    assert "holds futures, not natural gas" in text
    assert "sell each expiring contract to buy the next one" in text


def test_the_block_reaches_the_journal():
    record = carry.build_snapshot("USO", bleeding(100.0, -9.0), flat(70.0)).as_dict()
    assert record["commodity"] == "crude oil"
    assert len(record["windows"]) == 3
