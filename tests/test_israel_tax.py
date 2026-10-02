"""The owner's ten tax cases (2 Oct 2026), reproduced by ``analysis.israel_tax``.

Fees 0 and tax 25% throughout, as the owner wrote them. Each test is named
after its case; the numbers in the asserts are the owner's.
"""

from __future__ import annotations

from datetime import date

import pytest

from analysis import israel_tax as tax
from config import israel_tax as cfg

ON = tax.TaxRules(offset_losses_vs_dividends=True)
OFF = tax.TaxRules(offset_losses_vs_dividends=False)


def approx(value: float) -> object:
    return pytest.approx(value, abs=1e-6)


def test_the_rules_live_in_one_config_file_with_the_owners_numbers():
    assert cfg.CAPITAL_GAINS_RATE == cfg.DIVIDEND_RATE == 0.25
    assert (cfg.US_WITHHOLDING_W8BEN, cfg.US_WITHHOLDING_NO_W8BEN) == (0.25, 0.30)
    assert cfg.OFFSET_LOSSES_VS_DIVIDENDS is True          # the harsher case, until the accountant answers
    assert cfg.SURTAX_ENABLED is False
    assert (cfg.SURTAX_THRESHOLD_ILS, cfg.SURTAX_RATE, cfg.SURTAX_CAPITAL_RATE) == (721_560.0, 0.03, 0.02)
    assert cfg.SALARY_ILS == 0.0                            # an input: no personal number in the repository
    assert cfg.LOT_METHOD == "FIFO" and cfg.CARRY_FORWARD_YEARS is None
    assert "Bank of Israel representative rate" in cfg.FX_SOURCE
    assert tax.DEFAULT_RULES == tax.TaxRules()


def test_t1_a_gain_in_shekels_after_the_dollar_fell_is_taxed_on_the_shekel_gain():
    g = tax.lot_gain(10_000, 3.70, 11_000, 3.40)
    assert (g.cost_ils, g.proceeds_ils) == (approx(37_000), approx(37_400))
    assert g.nominal == approx(400) and g.inflation == approx(-3_000)
    assert g.taxable_gain == approx(400) and g.allowable_loss == 0
    assert tax.year_tax(2026, [g.taxable_gain], []).capital_tax == approx(100)


def test_t2_a_gain_after_the_dollar_rose_is_taxed_on_the_real_part_only():
    g = tax.lot_gain(10_000, 3.40, 11_000, 3.70)
    assert (g.cost_ils, g.proceeds_ils) == (approx(34_000), approx(40_700))
    assert g.nominal == approx(6_700) and g.inflation == approx(3_000)
    assert g.taxable_gain == approx(3_700)
    assert tax.year_tax(2026, [g.taxable_gain], []).capital_tax == approx(925)


def test_t3_a_loss_after_the_dollar_fell_is_allowed_net_of_the_currency_part():
    g = tax.lot_gain(10_000, 3.70, 9_000, 3.40)
    assert (g.cost_ils, g.proceeds_ils) == (approx(37_000), approx(30_600))
    assert g.nominal == approx(-6_400) and g.inflation == approx(-3_000)
    assert g.allowable_loss == approx(-3_400) and g.taxable_gain == 0
    assert -cfg.CAPITAL_GAINS_RATE * g.allowable_loss == approx(850)   # the tax shield


def test_t4_a_nominal_gain_smaller_than_the_currency_gain_is_not_taxed():
    g = tax.lot_gain(10_000, 3.40, 9_500, 3.80)
    assert (g.cost_ils, g.proceeds_ils) == (approx(34_000), approx(36_100))
    assert g.nominal == approx(2_100) and g.inflation == approx(4_000)
    assert g.amount == 0 and g.taxable_gain == 0


def test_t5_a_loss_made_only_by_the_exchange_rate_is_not_deductible():
    """The owner's reading of the circular's two-step rule: NEEDS CONFIRMATION by the accountant
    (``docs/research/cpa-questions.md``, question 2)."""
    g = tax.lot_gain(10_000, 3.70, 10_500, 3.40)
    assert (g.cost_ils, g.proceeds_ils) == (approx(37_000), approx(35_700))
    assert g.nominal == approx(-1_300) and g.inflation == approx(-3_000)
    assert g.amount == 0 and g.allowable_loss == 0


def test_t6_a_loss_after_the_dollar_rose_is_allowed_in_full():
    g = tax.lot_gain(10_000, 3.40, 8_000, 3.70)
    assert (g.cost_ils, g.proceeds_ils) == (approx(34_000), approx(29_600))
    assert g.nominal == approx(-4_400) and g.inflation == approx(3_000)
    assert g.allowable_loss == approx(-4_400)
    assert -cfg.CAPITAL_GAINS_RATE * g.allowable_loss == approx(1_100)


@pytest.mark.parametrize("rules, carry, israeli, credit, lost, year2_taxable, year2_tax", [
    (ON, -2_600, 0.0, 0.0, 350.0, 3_400, 850),
    (OFF, -4_000, 350.0, 350.0, 0.0, 2_000, 500),
])
def test_t7_a_net_loss_against_the_dividend_and_the_carry_forward(rules, carry, israeli, credit, lost,
                                                                   year2_taxable, year2_tax):
    """Year 1: gain 10,000 (lot A), allowable loss -14,000 (lot B), a VT dividend of $400 at 3.50 =
    1,400 ILS with 350 ILS of US tax. Year 2: a gain of 6,000."""
    year1 = tax.year_tax(2026, [10_000], [-14_000], [(1_400, 350)], 0.0, rules)
    assert year1.net_capital == approx(-4_000)
    assert year1.capital_tax == 0 and year1.extra_dividend_tax == 0
    assert year1.israeli_dividend_tax == approx(israeli) and year1.credit == approx(credit)
    assert year1.lost_credit == approx(lost)                         # ON: the 350 credit is wasted
    assert year1.dividend_offset == approx(1_400 if rules is ON else 0)
    assert year1.carry_out == approx(carry)
    year2 = tax.year_tax(2027, [6_000], [], [], year1.carry_out, rules)
    assert year2.taxable_capital == approx(year2_taxable) and year2.capital_tax == approx(year2_tax)


def test_t7_the_carry_forward_is_never_set_against_a_later_years_dividends():
    year2 = tax.year_tax(2027, [], [], [(1_000, 250)], carry_in=-2_600, rules=ON)
    assert year2.dividend_offset == 0 and year2.israeli_dividend_tax == approx(250)
    assert year2.carry_out == approx(-2_600)


def test_t8_the_surtax_on_a_salary_and_a_large_gain():
    assert tax.surtax(300_000, 900_000) == approx(14_353.20 + 3_568.80)
    assert tax.surtax(300_000, 900_000) == approx(17_922)
    on = tax.TaxRules(surtax_enabled=True, salary_ils=300_000)
    year = tax.year_tax(2026, [900_000], [], [], 0.0, on)
    assert year.capital_tax == approx(225_000) and year.surtax == approx(17_922)
    assert tax.year_tax(2026, [900_000], []).surtax == 0              # off by default


def test_t9_fifo_sells_the_first_lot_first():
    book = tax.TaxBook()
    day = date(2026, 10, 1)
    book.buy(day, "X", 10, 100, 3.50)
    book.buy(date(2026, 10, 2), "X", 10, 120, 3.60)
    book.sell(date(2026, 10, 5), "X", 10, 130, 3.55)
    [sold] = book.realised
    assert sold.gain.cost_ils == approx(3_500) and sold.gain.proceeds_ils == approx(4_615)
    assert sold.gain.nominal == approx(1_115) and sold.gain.inflation == approx(50)
    assert sold.amount == approx(1_065)
    assert tax.year_tax(2026, [sold.amount], []).capital_tax == approx(266.25)
    [left] = book.open_lots()
    assert (left.qty, left.usd, left.fx) == (10, approx(1_200), 3.60)


@pytest.mark.parametrize("w8ben, us, extra, lost", [(True, 900, 0, 0), (False, 1_080, 0, 180)])
def test_t10_a_dividend_with_and_without_a_w8ben(w8ben, us, extra, lost):
    d = tax.dividend_tax(1_000 * 3.60, tax.TaxRules(w8ben=w8ben))
    assert d.gross_ils == approx(3_600)
    assert d.us_withheld_ils == approx(us) and d.israeli_tax_ils == approx(900)
    assert d.credit_ils == approx(900) and d.extra_ils == approx(extra) and d.lost_ils == approx(lost)


# --------------------------------------------------------------------------- #
# The book and the walk the gate reads
# --------------------------------------------------------------------------- #


def test_fees_are_in_the_cost_and_out_of_the_proceeds():
    book = tax.TaxBook()
    book.buy(date(2026, 10, 1), "X", 10, 100, 3.5, fee_usd=1.0)
    book.sell(date(2026, 10, 2), "X", 4, 110, 3.5, fee_usd=0.44)
    [sold] = book.realised
    assert sold.gain.cost_ils == approx(4 * (100 + 0.1) * 3.5)
    assert sold.gain.proceeds_ils == approx((440 - 0.44) * 3.5)
    assert book.open_lots()[0].usd == approx(6 * 100.1)


def test_a_short_is_opened_by_a_sale_and_closed_by_a_purchase():
    book = tax.TaxBook()
    book.sell(date(2026, 10, 1), "X", 10, 50, 3.6)
    assert book.open_quantity("X") == -10
    book.buy(date(2026, 10, 2), "X", 10, 40, 3.6)
    [covered] = book.realised
    assert covered.kind == "cover" and covered.amount == approx(100 * 3.6)
    assert book.open_quantity("X") == 0


def test_a_reinvested_dividend_is_a_new_lot():
    book = tax.TaxBook()
    book.buy(date(2026, 1, 2), "VT", 100, 100, 3.5)
    book.dividend(date(2026, 3, 20), "VT", 50.0, 3.5, reinvest=(0.375, 100.0))
    lots = book.open_lots()
    assert len(lots) == 2 and lots[1].qty == 0.375 and lots[1].day == date(2026, 3, 20)
    assert book.received[0].us_withheld_ils == approx(50 * 3.5 * 0.25)


def test_if_sold_today_is_floored_at_zero_and_carries_finished_years():
    book = tax.TaxBook(OFF)
    book.buy(date(2026, 11, 2), "X", 10, 100, 3.5)
    book.sell(date(2026, 12, 1), "X", 10, 120, 3.5)       # 2026: a gain of 700 ILS, tax 175
    book.buy(date(2027, 1, 4), "Y", 10, 100, 3.5)
    down = book.state(date(2027, 1, 5), {"Y": 90.0}, 3.5)  # an open loss this year: no negative tax
    assert down.realised_ils == approx(175) and down.if_sold_ils == approx(175)
    assert down.realised_usd == approx(50)
    up = book.state(date(2027, 1, 6), {"Y": 110.0}, 3.5)
    assert up.if_sold_ils == approx(175 + 0.25 * 350)


def test_after_tax_equity_is_equity_minus_the_tax_if_sold_today():
    days = [date(2026, 10, 1), date(2026, 10, 2)]
    events = {days[0]: [tax.Event(tax.BUY, "X", 10, 100.0)]}
    closes = {days[0]: {"X": 100.0}, days[1]: {"X": 120.0}}
    series = tax.after_tax_series(days, [1_000.0, 1_200.0], events, lambda d: closes[d],
                                  {days[0]: 3.5, days[1]: 3.5}, start_equity_usd=1_000.0)
    first, second = series.days
    assert first.after_tax_usd == approx(1_000) and first.if_sold_tax_ils == 0
    assert second.if_sold_tax_ils == approx(0.25 * 200 * 3.5)
    assert second.after_tax_usd == approx(1_200 - 50) and second.after_tax_ils == approx(1_200 * 3.5 - 175)
    returns = series.returns()
    assert returns[days[0]] == 0 and returns[days[1]] == approx(1_150 / 1_000 - 1)
    assert series.returns(after_tax=False)[days[1]] == approx(0.2)


def test_a_dividend_credited_gross_owes_the_us_tax_withheld_too():
    days = [date(2026, 10, 1), date(2026, 10, 2)]
    events = {days[0]: [tax.Event(tax.BUY, "VT", 10, 100.0)], days[1]: [tax.Event(tax.DIVIDEND, "VT", 10, 1.0)]}
    series = tax.after_tax_series(days, [1_000.0, 1_010.0], events, lambda d: {"VT": 100.0},
                                  {d: 3.5 for d in days}, start_equity_usd=1_000.0)
    assert series.days[1].realised_tax_ils == approx(0.25 * 10 * 3.5)
    assert series.days[1].after_tax_usd == approx(1_010 - 2.5)


def test_a_book_refuses_what_it_cannot_price():
    with pytest.raises(ValueError):
        tax.lot_gain(1, 0, 1, 3.5)
    with pytest.raises(ValueError):
        tax.after_tax_series([date(2026, 10, 1)], [1.0], {}, lambda d: {}, {}, start_equity_usd=1.0)
    with pytest.raises(ValueError):
        tax.year_tax(2026, [-1], [])
