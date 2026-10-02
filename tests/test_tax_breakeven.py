"""The break-even simulator: the tax drag of turning a book over, against VT held 20 years."""

from __future__ import annotations

import pytest

from analysis import tax_breakeven as be
from analysis.israel_tax import TaxRules


def closed_form(growth: float, dividend_yield: float, years: int = 20) -> float:
    """The same two books by hand: VT compounds at growth + 75% of the yield and is taxed once at
    the end on everything above what went in; the active fund compounds at 75% of its whole return."""
    step = 1 + growth + 0.75 * dividend_yield
    wealth = step ** years
    basis = 1 + 0.75 * dividend_yield * sum(step ** t for t in range(years))
    after = wealth - 0.25 * (wealth - basis)
    return (after ** (1 / years) - 1) / 0.75 - growth - dividend_yield


@pytest.mark.parametrize("growth, dividend_yield", [(0.06, 0.02), (0.04, 0.015), (0.08, 0.025)])
def test_the_engine_agrees_with_the_books_done_by_hand(growth, dividend_yield):
    result = be.breakeven(growth=growth, dividend_yield=dividend_yield)
    assert result["extra_per_year"] == pytest.approx(closed_form(growth, dividend_yield), abs=1e-6)
    assert be.active(result["extra_per_year"], growth=growth, dividend_yield=dividend_yield) \
        == pytest.approx(result["vt_after_tax"], rel=1e-6)


def test_the_owners_rough_estimate_of_about_point_eight_with_a_two_percent_yield():
    result = be.breakeven()
    assert (result["years"], result["growth"], result["dividend_yield"]) == (20, 0.06, 0.02)
    assert 0.7 < result["extra_per_year"] * 100 < 0.9
    assert result["active_after_tax_at_zero"] < result["vt_after_tax"]


def test_the_drag_grows_with_the_return_and_vanishes_without_tax():
    rows = be.table(growths=(0.04, 0.06, 0.08), yields=(0.02,))
    extras = [r["extra_per_year"] for r in rows]
    assert extras == sorted(extras) and extras[0] > 0
    # No Israeli tax: only the US tax on dividends is left, and both books pay it alike.
    untaxed = TaxRules(capital_rate=0.0, dividend_rate=0.0)
    assert be.held(rules=untaxed) == pytest.approx(be.active(0.0, rules=untaxed), rel=1e-9)
    assert be.breakeven(rules=untaxed)["extra_per_year"] == pytest.approx(0.0, abs=1e-6)


def test_the_report_says_it_is_for_information_only(capsys):
    assert be.main(["--growth", "0.06", "--dividend-yield", "0.02"]) == 0
    out = capsys.readouterr().out
    assert "for information only; not a gate" in out and "| 6.0% | 2.0% |" in out
    assert be.main(["--years", "0"]) == 2


def test_an_answer_outside_the_search_range_is_refused_not_clipped(capsys):
    low, high = be.SEARCH_RANGE
    assert (low, high) == (-0.05, 0.20)
    with pytest.raises(ValueError, match=r"more than \+20 points a year"):
        be.breakeven(growth=1.0)
    assert be.main(["--growth", "1.0"]) == 2
    captured = capsys.readouterr()
    assert "no break-even inside the search range" in captured.err and captured.out == ""
