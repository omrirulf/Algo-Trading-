"""The investor simulator, on sample data only: the plan's tests T11 to T41 (4 Oct 2026, approved 16 Oct 2026).

Numbered after the owner's tax cases T1 to T10 (``tests/test_israel_tax.py``),
in the same style: fees 0 and tax 25% unless a case says otherwise. "B" is
a made-up bond fund at $50 (180 ILS at 3.60); "KH" is a keren hishtalmut.
Every number in the asserts is the plan's.
"""

from __future__ import annotations

import logging
import shutil
from datetime import date, timedelta
from pathlib import Path

import pytest

from analysis import israel_tax as tax
from config import israel_tax as cfg
from investor import PRIVATE_MARKER, REPOSITORY, SAMPLE_MARKER, benchmark as bm, files, forms, funds, report
from investor import harvest as hv, ledger, market as mk, rebalance as rb

#: Weekdays: a Thursday, and three Mondays.
D = date(2026, 10, 1)
D1, D2, D3 = date(2026, 1, 5), date(2026, 2, 2), date(2026, 3, 2)
SAMPLE = REPOSITORY / "tests" / "data" / "investor_sample"
STOCKS_BONDS = {"stocks": 60, "bonds": 40}


def approx(value: float) -> object:
    return pytest.approx(value, abs=1e-6)


def rate_of(rates):
    return (lambda d: rates[d]) if isinstance(rates, dict) else (lambda d: rates)


def T(row, day, account, kind, ticker="", qty=0.0, price=0.0, **extra) -> files.Transaction:
    return files.Transaction(row, day, account, kind, ticker, qty, price, **extra)


def deposit(row, day, account, usd) -> files.Transaction:
    return T(row, day, account, "deposit", amount=usd, currency="USD")


def person(rates, rows, plan=None, accounts=(("Broker", "taxable", "USD"),), tracks=()) -> ledger.Person:
    named = {n: files.Account(n, k, c) for n, k, c in accounts}
    p = ledger.Person(named, plan or files.Plan(), rate_of(rates))
    p.apply(rows)
    p.set_tracks([files.TrackValue(i, D, a, t, v) for i, (a, t, v) in enumerate(tracks, 1)], D)
    return p


def plan_of(targets=STOCKS_BONDS, classes=None, mixes=None, buy_first=None, contributions=None, **rest) -> files.Plan:
    return files.Plan(targets=dict(targets), classes=dict(classes or {"VT": "stocks", "B": "bonds"}),
                      track_mix=dict(mixes or {}), buy_first=dict(buy_first or {"stocks": "VT", "bonds": "B"}),
                      contributions=dict(contributions or {}), **rest)


KH_TRACKS = {("KH", "stocks"): {"stocks": 100}, ("KH", "bonds"): {"bonds": 100}}
BROKER_AND_KH = (("Broker", "taxable", "USD"), ("KH", "tax_free", "ILS"))
NO = funds.NO_COSTS


def sales(result: rb.Rebalance) -> list[rb.Line]:
    return [line for line in result.sales if line.step == rb.SALE]


def weights(result: rb.Rebalance) -> dict[str, float]:
    return {row.name: round(row.weight, 2) for row in result.after}


# --------------------------------------------------------------------------- #
# Rebalancing
# --------------------------------------------------------------------------- #


def test_t11_bands_and_trade_to_points():
    rows = {t: rb.ClassRow("c", t, rb.band_for(t), 0, 0) for t in (60, 20, 10, 3)}
    assert [rows[t].band for t in (60, 20, 10, 3)] == [5, 5, 2.5, 0.75]
    assert (rows[60].trade_to_above, rows[60].trade_to_below) == (64, 56)
    assert (rows[20].trade_to_above, rows[20].trade_to_below) == (24, 16)
    assert (rows[10].trade_to_above, rows[10].trade_to_below) == (11.5, 8.5)
    assert (rows[3].trade_to_above, rows[3].trade_to_below) == (3, 3)                  # D5
    assert not rb.ClassRow("c", 60, 5, 0, 65).above_band
    assert not rb.ClassRow("c", 60, 5, 0, 65.00000000000001).above_band
    assert rb.ClassRow("c", 60, 5, 0, 65.01).above_band


def test_t12_contributions_first_to_the_class_below_its_band_then_towards_target():
    plan = plan_of(classes={}, mixes=KH_TRACKS, buy_first={}, contributions={"KH": (20_000, "ILS")})
    p = person(3.6, [], plan, (("KH", "tax_free", "ILS"),), [("KH", "stocks", 70_000), ("KH", "bonds", 30_000)])
    result = rb.rebalance(p, plan, {}, 3.6, D, NO)
    [bonds, stocks] = result.contributions
    assert (bonds.klass, bonds.amount_ils, bonds.tax_cost_ils) == ("bonds", approx(18_000), 0)
    assert (stocks.klass, stocks.amount_ils) == ("stocks", approx(2_000))
    assert weights(result) == {"stocks": 60.0, "bonds": 40.0} and not sales(result)


def test_t13_tax_free_accounts_second():
    plan = plan_of(mixes=KH_TRACKS)
    p = person(4.0, [deposit(1, D1, "Broker", 25_000), T(2, D1, "Broker", "buy", "VT", 100, 250)], plan,
               BROKER_AND_KH, [("KH", "stocks", 50_000), ("KH", "bonds", 50_000)])
    result = rb.rebalance(p, plan, {"VT": 250.0}, 4.0, D, NO)
    [move] = result.moves
    assert (move.account, move.ticker, move.to, move.amount_ils, move.tax_cost_ils) == ("KH", "stocks", "bonds", approx(22_000), 0)
    assert weights(result)["stocks"] == 64.0 and not sales(result)


def test_t14_a_mixed_track_moves_each_class_by_its_mix():
    mixes = {("KH", "general"): {"stocks": 40, "bonds": 60}, ("KH", "bonds"): {"bonds": 100}}
    plan = plan_of(mixes=mixes)
    p = person(4.0, [deposit(1, D1, "Broker", 25_000), T(2, D1, "Broker", "buy", "VT", 100, 250)], plan,
               BROKER_AND_KH, [("KH", "general", 100_000)])
    result = rb.rebalance(p, plan, {"VT": 250.0}, 4.0, D, NO)
    [move] = result.moves
    assert (move.ticker, move.to, move.amount_ils, move.tax_cost_ils) == ("general", "bonds", approx(30_000), 0)
    assert weights(result) == {"stocks": 64.0, "bonds": 36.0} and not sales(result)


def t15_person(vt_fx=3.70, nb=103):
    rates = {D1: vt_fx, D2: 3.60, D: 3.60}
    return person(rates, [deposit(1, D1, "Broker", 10_000), T(2, D1, "Broker", "buy", "VT", 100, 100),
                          deposit(3, D2, "Broker", 50 * nb), T(4, D2, "Broker", "buy", "B", nb, 50)])


def test_t15_a_taxable_sale_under_half_a_percent():
    plan = plan_of()
    result = rb.rebalance(t15_person(), plan, {"VT": 104.0, "B": 50.0}, 3.60, D, NO)
    assert result.classes[0].weight == pytest.approx(66.88, abs=0.005)
    [sale] = sales(result)
    assert (sale.ticker, sale.shares, sale.amount_ils) == ("VT", 4, approx(1_497.60))
    assert sale.tax_cost_ils == approx(4.40) and sale.cost_share == pytest.approx(0.0029, abs=5e-5)
    assert sale.suggested
    [buy] = sale.buys
    assert (buy.ticker, buy.shares, buy.amount_ils) == ("B", 8, approx(1_440))
    assert sale.cash_left_ils == approx(57.60)
    assert weights(result)["stocks"] == 64.21


def t16_person(nb=100):
    rates = {D1: 3.40, D2: 3.60, D: 3.60}
    return person(rates, [deposit(1, D1, "Broker", 6_000), T(2, D1, "Broker", "buy", "VT", 100, 60),
                          deposit(3, D2, "Broker", 50 * nb), T(4, D2, "Broker", "buy", "B", nb, 50)])


def test_t16_over_half_a_percent_with_a_drift_of_ten_or_less_is_not_suggested():
    result = rb.rebalance(t16_person(), plan_of(), {"VT": 100.0, "B": 50.0}, 3.60, D, NO)
    [sale] = sales(result)
    assert (sale.shares, sale.amount_ils, sale.tax_cost_ils) == (4, approx(1_440), approx(144))
    assert sale.cost_share == approx(0.10) and not sale.suggested
    assert "drift is 6.67 points, not above 10" in sale.reason and not sale.buys


def test_t17_the_same_lot_with_a_drift_over_ten_is_suggested():
    result = rb.rebalance(t16_person(67), plan_of(), {"VT": 100.0, "B": 50.0}, 3.60, D, NO)
    assert result.classes[0].weight == pytest.approx(74.91, abs=0.005)
    [sale] = sales(result)
    assert (sale.shares, sale.amount_ils, sale.tax_cost_ils) == (15, approx(5_400), approx(540))
    assert sale.cost_share == approx(0.10) and sale.suggested and "14.91 points, above 10" in sale.reason
    assert weights(result)["stocks"] == 63.67


def test_t18_fifo_decides_the_cost_and_the_cheaper_specific_lot_is_shown_not_used():
    p = person({D1: 3.40, D2: 3.70, D: 3.60}, [deposit(1, D1, "Broker", 600), T(2, D1, "Broker", "buy", "VT", 10, 60),
                                                deposit(3, D2, "Broker", 1_100), T(4, D2, "Broker", "buy", "VT", 10, 110)])
    cost = p.sale_cost("Broker", "VT", 10, 100.0, 3.60, D)
    assert cost.amount == approx(1_440) and cost.tax_delta == approx(360) and cost.cost == approx(360)
    assert cost.lots == ((D1, 10, approx(1_440)),)
    assert cost.best_specific == (2, approx(-360))


def test_t19_the_loss_carried_forward_is_a_cost_unless_it_would_go_against_dividends_anyway():
    rates = {D1: 3.40, D2: 3.40, D3: 3.40, D: 3.60}
    rows = [deposit(1, D1, "Broker", 7_000), T(2, D1, "Broker", "buy", "VT", 100, 60),
            T(3, D2, "Broker", "buy", "Z", 10, 100), T(4, D3, "Broker", "sell", "Z", 10, 100 - 1_000 / 34)]
    p = person(rates, rows)
    assert p.year_tax(2026).losses == approx(-1_000)
    cost = p.sale_cost("Broker", "VT", 4, 100.0, 3.60, D)
    assert (cost.tax_delta, cost.loss_used, cost.cost) == (0, approx(576), approx(144))
    assert cost.share == approx(0.10)
    p.apply([T(5, D3, "Broker", "dividend", "VT", amount=1_000 / 3.4, currency="USD", withheld_usd=250 / 3.4)])
    cost = p.sale_cost("Broker", "VT", 4, 100.0, 3.60, D)
    assert (cost.tax_delta, cost.loss_used, cost.cost) == (0, approx(0), approx(0))


def t20_person(lot_a_price=98, lot_a_fx=3.62):
    plan = plan_of(mixes=KH_TRACKS, contributions={"Broker": (2_700, "ILS")})
    rates = {D1: lot_a_fx, D2: 3.50, D: 3.60}
    rows = [deposit(1, D1, "Broker", 100 * lot_a_price), T(2, D1, "Broker", "buy", "VT", 100, lot_a_price),
            deposit(3, D2, "Broker", 3_500), T(4, D2, "Broker", "buy", "VT", 50, 70)]
    return person(rates, rows, plan, BROKER_AND_KH, [("KH", "stocks", 6_000), ("KH", "bonds", 20_000)]), plan


def test_t20_the_whole_order_new_money_tax_free_moves_then_a_taxable_sale():
    p, plan = t20_person()
    result = rb.rebalance(p, plan, {"VT": 100.0, "B": 50.0}, 3.60, D, NO)
    assert result.classes[0].weight == approx(75.0)
    [money] = result.contributions
    assert (money.ticker, money.shares, money.amount_ils) == ("B", 15, approx(2_700))
    [move] = result.moves
    assert (move.amount_ils, move.ticker, move.to) == (approx(6_000), "stocks", "bonds")
    [sale] = sales(result)
    assert (sale.shares, sale.amount_ils, sale.tax_cost_ils) == (3, approx(1_080), approx(3.93))
    assert sale.cost_share == pytest.approx(0.0036, abs=5e-5) and sale.suggested
    [buy] = sale.buys
    assert (buy.ticker, buy.shares) == ("B", 6) and sale.cash_left_ils == approx(0)
    assert weights(result)["stocks"] == 63.99


def test_t20_variant_the_drift_at_the_taxable_step_decides():
    p, plan = t20_person(90, 3.60)
    result = rb.rebalance(p, plan, {"VT": 100.0, "B": 50.0}, 3.60, D, NO)
    [sale] = sales(result)
    assert (sale.shares, sale.tax_cost_ils, sale.cost_share) == (3, approx(27.00), approx(0.025))
    assert not sale.suggested and "drift is 5.30 points" in sale.reason                     # D7


def test_t21_the_fund_with_the_lowest_tax_per_shekel_goes_first_and_the_other_is_shown():
    plan = plan_of(classes={"VT": "stocks", "VWRA": "stocks", "B": "bonds"}, mixes={("KH", "bonds"): {"bonds": 100}})
    rates = {D1: 3.40, D2: 3.70, D3: 3.62, D: 3.60}
    rows = [deposit(1, D1, "Broker", 3_000), T(2, D1, "Broker", "buy", "VT", 50, 60),
            deposit(3, D2, "Broker", 5_500), T(4, D2, "Broker", "buy", "VT", 50, 110),
            deposit(5, D3, "Broker", 6_200), T(6, D3, "Broker", "buy", "VWRA", 50, 124)]
    p = person(rates, rows, plan, BROKER_AND_KH, [("KH", "bonds", 30_000)])
    result = rb.rebalance(p, plan, {"VT": 100.0, "VWRA": 125.0, "B": 50.0}, 3.60, D, NO)
    assert result.classes[0].weight == pytest.approx(66.10, abs=0.005)
    [sale] = sales(result)
    assert (sale.ticker, sale.shares, sale.tax_cost_ils) == ("VWRA", 4, approx(1.12))
    assert sale.cost_share == pytest.approx(0.0006, abs=5e-5) and sale.suggested
    assert sale.notes == ["5 VT in Broker would cost 180.00 ILS (10.00%)"]


def test_t22_three_classes_out_at_once():
    plan = plan_of({"us": 30, "exus": 30, "bonds": 40}, {"VTI": "us", "VXUS": "exus", "B": "bonds"},
                   {("KH", "bonds"): {"bonds": 100}}, {"bonds": "B"})
    rates = {D1: 3.62, D2: 3.50, D: 3.60}
    rows = [deposit(1, D1, "Broker", 40 * 248), T(2, D1, "Broker", "buy", "VTI", 40, 248),
            deposit(3, D2, "Broker", 8_000), T(4, D2, "Broker", "buy", "VXUS", 160, 50)]
    p = person(rates, rows, plan, BROKER_AND_KH, [("KH", "bonds", 28_000)])
    result = rb.rebalance(p, plan, {"VTI": 250.0, "VXUS": 62.5, "B": 50.0}, 3.60, D, NO)
    assert [round(r.weight, 2) for r in result.classes] == [36.0, 36.0, 28.0]
    vti, vxus = sales(result)
    assert (vti.ticker, vti.shares, vti.tax_cost_ils, vti.suggested) == ("VTI", 6, approx(3.36), True)
    assert vti.cost_share == pytest.approx(0.0006, abs=5e-5)
    assert (vxus.ticker, vxus.shares, vxus.tax_cost_ils, vxus.cost_share) == ("VXUS", 12, approx(135.00), approx(0.05))
    assert vxus.suggested and "drift is 12.00 points, above 10" in vxus.reason
    assert [(b.ticker, b.shares) for b in vti.buys + vxus.buys] == [("B", 30), ("B", 15)]
    assert vti.cash_left_ils == approx(0) and vxus.cash_left_ils == approx(0)
    assert weights(result) == {"us": 30.6, "exus": 33.3, "bonds": 36.1}


def test_t23_a_band_narrower_than_one_share():
    plan = plan_of({"stocks": 60, "bonds": 37, "gold": 3}, {"VT": "stocks", "B": "bonds", "GOLD": "gold"}, KH_TRACKS,
                   {"stocks": "VT", "bonds": "B", "gold": "GOLD"})
    rows = [deposit(1, D1, "Broker", 100), T(2, D1, "Broker", "buy", "GOLD", 1, 100)]
    p = person(3.60, rows, plan, BROKER_AND_KH, [("KH", "stocks", 10_980), ("KH", "bonds", 6_660)])
    closes = {"VT": 100.0, "B": 50.0, "GOLD": 100.0}
    first = rb.rebalance(p, plan, closes, 3.60, D, NO)
    assert first.classes[2].weight == approx(2.0) and first.classes[2].out_of_band
    assert not first.lines
    assert first.notes == ["gold: no whole number of shares of GOLD puts it inside its band today; "
                           "it fits once the total is 19,200 ILS"]
    plan.contributions = {"Broker": (1_200, "ILS")}
    second = rb.rebalance(p, plan, closes, 3.60, D, NO)
    assert [(line.ticker, line.shares) for line in second.contributions] == [("GOLD", 1), ("VT", 1), ("B", 2)]
    assert second.cash_ils["Broker"] == approx(120)
    assert weights(second) == {"stocks": 59.06, "bonds": 36.56, "gold": 3.75}
    assert not second.notes and not sales(second)


# --------------------------------------------------------------------------- #
# Harvesting
# --------------------------------------------------------------------------- #

CLOSES = {"VT": 100.0, "VWRA": 130.0, "ACWI": 125.0}           # IMID has no price: skipped
STOCKS = {"VT": "stocks"}


def gain_rows(row, day, usd_gain, fx) -> list[files.Transaction]:
    """A realised gain of ``usd_gain * fx`` shekels this year, with no currency part."""
    return [T(row, day, "Broker", "buy", "Z", 100, 100), T(row + 1, day, "Broker", "sell", "Z", 100, 100 + usd_gain / 100)]


def test_t24_a_loss_worth_taking_suggests_the_first_fund_and_shows_the_other():
    rows = [deposit(1, D1, "Broker", 22_000), T(2, D1, "Broker", "buy", "VT", 100, 120), *gain_rows(3, D2, 10_000 / 3.7, 3.7)]
    p = person(3.70, rows)
    assert p.year_tax(2026).gains == approx(10_000)
    result = hv.harvest(p, CLOSES, 3.70, D, STOCKS)
    [s] = result.suggestions
    g = s.group
    assert (g.ticker, g.shares, g.loss_ils, g.value_ils) == ("VT", 100, approx(7_400), approx(37_000))
    assert g.floor_ils == approx(2_000) and g.tax_value_ils == approx(1_850)
    assert [(c.ticker, c.shares, round(c.trading_cost_ils, 2), c.passes) for c in g.candidates] == [
        ("VWRA", 76, 43.96, True), ("ACWI", 79, 14.75, True)]
    assert s.fund == "VWRA" and s.tax_delta_ils == approx(-1_850)
    assert (s.worth_now_ils, s.against_gains_ils, s.against_dividends_ils, s.carried_forward_ils) == (
        approx(1_850), approx(7_400), approx(0), approx(0))
    assert result.sold == {"VT"} and result.bought == {"stocks": "VWRA"}


def test_t25_what_the_loss_is_really_worth():
    rates = {D1: 3.60, D2: 3.60, D3: 3.60, D: 3.75}
    rows = [deposit(1, D1, "Broker", 22_000), T(2, D1, "Broker", "buy", "VT", 100, 120), *gain_rows(3, D2, 3_000 / 3.6, 3.6),
            T(5, D3, "Broker", "dividend", "VT", amount=1_000 / 3.6, currency="USD", withheld_usd=250 / 3.6)]
    p = person(rates, rows)
    [s] = hv.harvest(p, CLOSES, 3.75, D, STOCKS).suggestions
    assert s.group.loss_ils == approx(5_700) and s.group.tax_value_ils == approx(1_425)
    assert round(s.group.candidates[0].trading_cost_ils, 2) == 44.55
    assert s.tax_delta_ils == approx(-750) and s.worth_now_ils == approx(750)
    assert (s.against_gains_ils, s.against_dividends_ils, s.credit_lost_ils, s.carried_forward_ils) == (
        approx(3_000), approx(1_000), approx(250), approx(1_700))
    assert any("question 2" in w for w in s.warnings)


def test_t26_a_loss_made_only_by_the_exchange_rate_is_not_flagged_and_says_what_t5_decides():
    rows = [deposit(1, D1, "Broker", 40_000), T(2, D1, "Broker", "buy", "VT", 300, 100), *gain_rows(3, D2, 10_000 / 3.7, 3.7)]
    p = person({D1: 3.70, D2: 3.70, D: 3.45}, rows)
    result = hv.harvest(p, {**CLOSES, "VT": 102.0}, 3.45, D, STOCKS)
    assert not result.suggestions
    [g] = result.not_flagged
    assert g.net_ils == 0 and g.nominal_ils == approx(-5_430) and not g.passes_a
    assert g.if_t5_rejected == "it would be flagged (tax value 1,357.50 against 5 x 121.13) if the accountant rejects T5"


def test_t27_a_small_loss_is_not_flagged():
    p = person(4.0, [deposit(1, D1, "Broker", 5_000), T(2, D1, "Broker", "buy", "VT", 50, 100)])
    [g] = hv.harvest(p, {**CLOSES, "VT": 92.5}, 4.0, D, STOCKS).not_flagged
    assert g.loss_ils == approx(1_500) and g.floor_ils == approx(2_000) and not g.passes_a


def test_t28_a_small_share_of_a_large_lot_is_not_flagged():
    p = person(3.7, [deposit(1, D1, "Broker", 100_000), T(2, D1, "Broker", "buy", "VT", 1_000, 100)])
    [g] = hv.harvest(p, {**CLOSES, "VT": 96.0}, 3.7, D, STOCKS).not_flagged
    assert g.loss_ils == approx(14_800) and g.floor_ils == approx(17_760) and not g.passes_a


def test_t29_no_gain_this_year_and_none_expected_still_flags_a_domicile_switch():
    rows = [deposit(1, D1, "Broker", 12_000), T(2, D1, "Broker", "buy", "VT", 100, 120),
            T(3, D3, "Broker", "dividend", "VT", amount=1_200 / 3.7, currency="USD", withheld_usd=300 / 3.7)]
    p = person(3.70, rows)
    [s] = hv.harvest(p, CLOSES, 3.70, D, STOCKS).suggestions
    assert s.fund == "VWRA" and s.tax_delta_ils == approx(0) and s.worth_now_ils == approx(0)
    vwra, acwi = s.group.candidates
    assert vwra.passes and vwra.switch and not acwi.passes_c and acwi.failed == "C"
    assert (s.against_dividends_ils, s.credit_lost_ils, s.carried_forward_ils) == (approx(1_200), approx(300), approx(6_200))


def test_t30_a_fifo_group_is_tested_as_a_whole():
    rows = [deposit(1, D1, "Broker", 27_000), T(2, D1, "Broker", "buy", "VT", 300, 90),
            deposit(3, D2, "Broker", 12_500), T(4, D2, "Broker", "buy", "VT", 100, 125), *gain_rows(5, D2, 6_000 / 3.55, 3.55)]
    p = person({D1: 3.90, D2: 3.55, D: 3.60}, rows)
    result = hv.harvest(p, CLOSES, 3.60, D, STOCKS)
    assert not result.suggestions
    [g] = result.not_flagged
    assert (g.lots, g.net_ils, g.value_ils, g.floor_ils) == (2, approx(-5_675), approx(144_000), approx(7_200))
    assert not g.passes_a
    # The loss lot alone would pass A, but it cannot be sold first.
    alone = tax.lot_gain(12_500, 3.55, 10_000, 3.60)
    assert alone.amount == approx(-8_375)


def test_t31_the_cost_test_fails():
    p = person(4.0, [deposit(1, D1, "Broker", 10_600), T(2, D1, "Broker", "buy", "VT", 100, 106)])
    result = hv.harvest(p, CLOSES, 4.0, D, STOCKS, expects=files.Dated(True, D), cost_override=150.0)
    [g] = result.not_flagged
    assert g.loss_ils == approx(2_400) and g.value_ils == approx(40_000) and g.passes_a
    assert g.tax_value_ils == approx(600) and all(c.failed == "B" for c in g.candidates) and not g.flagged


def test_t32_a_loss_carried_in_that_covers_this_years_gain():
    plan = files.Plan(carry_in=-5_000, carry_in_year=2025)
    rows = [deposit(1, D1, "Broker", 23_000), T(2, D1, "Broker", "buy", "VT", 100, 130), *gain_rows(3, D2, 4_000 / 3.5, 3.5)]
    p = person(3.5, rows, plan)
    year = p.year_tax(2026)
    assert (year.gains, year.carry_in, year.taxable_capital) == (approx(4_000), -5_000, approx(0))
    [s] = hv.harvest(p, CLOSES, 3.5, D, STOCKS).suggestions
    vwra, acwi = s.group.candidates
    assert vwra.passes and acwi.failed == "C"                       # under the literal reading ACWI would pass
    assert s.net_gain_this_year_ils == approx(0) and s.gains_less_losses_ils == approx(4_000)
    assert s.tax_delta_ils == approx(0) and s.worth_now_ils == approx(0) and s.carried_forward_ils == approx(10_500)


def test_the_substitutes_table_never_pairs_the_same_index_or_the_same_fund(monkeypatch):
    assert funds.check_substitutes() is None                         # the table as shipped is clean
    assert funds.identical(funds.fund("ACWI"), funds.fund("ISAC"))    # the same index: never a pair
    assert funds.identical(funds.fund("VWRA"), funds.fund("VWRA"))    # the same fund
    assert not funds.identical(funds.fund("VT"), funds.fund("VWRA"))
    monkeypatch.setitem(funds.SUBSTITUTES, "ACWI", ("ISAC",))
    with pytest.raises(ValueError, match="ACWI and ISAC share an index or a fund ID"):
        funds.check_substitutes()
    assert funds.domicile_switch(funds.fund("VT"), funds.fund("VWRA")) and not funds.domicile_switch(funds.fund("VT"), funds.fund("ACWI"))


# --------------------------------------------------------------------------- #
# The outputs
# --------------------------------------------------------------------------- #


def test_t33_half_years():
    rows = [deposit(1, D1, "Broker", 2_000), T(2, D1, "Broker", "buy", "X", 10, 100), T(3, D1, "Broker", "buy", "Y", 10, 100),
            T(4, D3, "Broker", "sell", "X", 10, 200), T(5, date(2026, 9, 1), "Broker", "sell", "Y", 10, 75)]
    p = person(4.0, rows)
    first, second = p.half_years(2026)
    assert (first.gains_ils, first.on_gains, first.on_net, first.on_year) == (approx(4_000), approx(1_000), approx(1_000), approx(1_000))
    assert (second.losses_ils, second.on_gains, second.on_net, second.on_year) == (approx(-1_000), 0, 0, approx(-250))
    assert p.year_tax(2026).capital_tax == approx(750)


def test_t34_form_1325_rows_from_t9s_sale():
    rates = {date(2026, 10, 1): 3.5, date(2026, 10, 2): 3.6, date(2026, 10, 5): 3.55}
    p = person(rates, [T(1, date(2026, 10, 1), "Broker", "buy", "X", 10, 100), T(2, date(2026, 10, 2), "Broker", "buy", "X", 10, 120),
                       T(3, date(2026, 10, 5), "Broker", "sell", "X", 10, 130)])
    [row] = forms.rows_1325(p, 2026)
    assert (row.bought_on, row.sold_on, row.fx_open, row.fx_close) == (date(2026, 10, 1), date(2026, 10, 5), 3.5, 3.55)
    assert (row.cost_ils, row.proceeds_ils, row.nominal_ils, row.inflation_ils, row.real_ils) == (
        approx(3_500), approx(4_615), approx(1_115), approx(50), approx(1_065))
    assert row.ratio == approx(3.55 / 3.5) and row.adjusted_cost_ils == approx(3_550)
    assert (row.usd_cost, row.usd_proceeds) == (approx(1_000), approx(1_300))


def test_t35_one_person_two_accounts():
    accounts = (("A", "taxable", "USD"), ("B", "taxable", "USD"))
    rows = [T(1, D1, "A", "buy", "X", 10, 100), T(2, D1, "B", "buy", "Y", 10, 100),
            T(3, D3, "A", "sell", "X", 10, 150), T(4, D3, "B", "sell", "Y", 10, 50)]
    p = person(4.0, rows, accounts=accounts)
    year = p.year_tax(2026)
    assert year.net_capital == approx(0) and year.capital_tax == 0
    assert tax.year_tax(2026, [2_000], []).capital_tax == approx(500)           # two books would wrongly give this


def test_t36_no_tax_is_taken_off_twice():
    jan, mar, jun, today = date(2026, 1, 5), date(2026, 3, 20), date(2026, 6, 1), date(2027, 3, 1)
    rates = {jan: 3.70, mar: 3.65, jun: 3.60, today: 3.50}
    rows = [deposit(1, jan, "Broker", 10_000), T(2, jan, "Broker", "buy", "VT", 100, 100),
            T(3, mar, "Broker", "dividend", "VT", amount=50, currency="USD", withheld_usd=12.5),
            T(4, jun, "Broker", "sell", "VT", 40, 110)]
    p = person(rates, rows)
    state = p.if_sold(today, {"VT": 120.0}, 3.50, costs=NO)
    assert state.market_ils == approx(40_731.25)
    assert state.value_ils == approx(39_981.25)                   # not 39,677.50
    assert state.tax_paid_so_far_ils == approx(305.625)
    assert state.finished_tax_ils == approx(260) and state.us_withheld_ils == approx(12.5 * 3.65)


def test_t37_an_advance_already_paid_is_not_taken_off_again_and_comes_back_when_the_year_nets_a_loss():
    jan, mar, aug = date(2027, 1, 4), date(2027, 3, 1), date(2027, 8, 2)
    rates = {jan: 3.70, mar: 3.60, aug: 3.50}
    p = person(rates, [deposit(1, jan, "Broker", 10_000), T(2, jan, "Broker", "buy", "VT", 100, 100), T(3, mar, "Broker", "sell", "VT", 40, 110)])
    paid = [files.Payment(1, date(2027, 7, 20), 2027, "1", 260)]
    up = p.if_sold(aug, {"VT": 120.0}, 3.50, paid, NO)
    assert (up.market_ils, up.tax_if_sold_ils, up.advances_paid_ils, up.value_ils) == (
        approx(40_600), approx(1_010), approx(260), approx(39_850))
    down = p.if_sold(aug, {"VT": 95.0}, 3.50, paid, NO)
    assert (down.market_ils, down.tax_if_sold_ils, down.value_ils) == (approx(35_350), 0, approx(35_610))


class _History:
    """A price history for the benchmark: VT and VWRA at $100 on the deposit day, VT at $105 on its dividend day."""

    def __init__(self, deposit_day: date, dividend_day: date) -> None:
        self.deposit_day, self.dividend_day = deposit_day, dividend_day

    def first_day(self, ticker):
        return date(2019, 7, 23) if ticker == "VWRA" else date(2008, 6, 26)

    def close_on_or_after(self, ticker, day):
        return (day, 100.0 if day == self.deposit_day else 105.0)

    def dividends(self, ticker, start, end):
        return [(self.dividend_day, 2.0)] if ticker == "VT" and start < self.dividend_day <= end else []


def test_t38_the_same_shekels_in_vt_and_in_vwra():
    deposit_day, dividend_day, today = D1, date(2026, 3, 20), D
    rates = {deposit_day: 3.70, dividend_day: 3.60, today: 3.60}
    flows = [ledger.Flow(deposit_day, "Broker", "deposit", 37_000.0, 10_000.0, 3.70, False)]
    vt, vwra = bm.benchmark(flows, _History(deposit_day, dividend_day), rate_of(rates), today,
                            {"VT": 110.0, "VWRA": 112.0}, 3.60, NO)
    assert (vt.shares, vt.cash_usd) == (101, approx(45))
    assert (vt.market_ils, vt.tax_if_sold_ils, vt.after_tax_ils) == (approx(40_158), approx(654.50), approx(39_503.50))
    assert (vwra.shares, vwra.market_ils, vwra.tax_if_sold_ils, vwra.after_tax_ils) == (
        100, approx(40_320), approx(830), approx(39_490))
    assert 0.08 < vt.money_weighted < 0.10 and vwra.money_weighted < vt.money_weighted


def test_money_that_went_in_before_vwras_first_price_is_not_available():
    flows = [ledger.Flow(date(2018, 1, 5), "Broker", "deposit", 37_000.0, 10_000.0, 3.70, False)]
    vt, vwra = bm.benchmark(flows, _History(date(2018, 1, 5), date(2018, 3, 20)), rate_of(3.7), D,
                            {"VT": 110.0, "VWRA": 112.0}, 3.60, NO)
    assert vt.available and not vwra.available and "before 2019-07-23" in vwra.reason


def test_t39_the_surtax_from_the_other_income_in_the_plan():
    plan = files.Plan(surtax=True, other_income_ils=712_345, other_income_year=2026)
    rows = [deposit(1, D1, "Broker", 10_000), T(2, D1, "Broker", "buy", "X", 10, 1_000), T(3, D3, "Broker", "sell", "X", 10, 2_000)]
    on = person(4.0, rows, plan)
    year = on.year_tax(2026)
    assert year.capital_tax == approx(10_000) and year.surtax == approx(0.03 * (712_345 + 40_000 - 721_560))
    off = person(4.0, rows)
    assert off.year_tax(2026).surtax == 0
    assert cfg.SALARY_ILS == 0.0                                       # the salary stays an input


def test_t40_a_transfer_between_the_owners_accounts_is_not_a_sale():
    accounts = (("A", "taxable", "USD"), ("B", "taxable", "USD"))
    rows = [deposit(1, D1, "A", 1_000), T(2, D1, "A", "buy", "VT", 10, 100), T(3, D2, "A", "transfer", "VT", 10, to_account="B"),
            T(4, D3, "B", "sell", "VT", 10, 110)]
    p = person({D1: 3.70, D2: 3.65, D3: 3.60}, rows, accounts=accounts)
    [(account, sold)] = p.realised_rows(2026)
    assert account == "B" and sold.opened == D1 and sold.fx_open == 3.70
    assert (sold.gain.cost_ils, sold.gain.proceeds_ils, sold.amount) == (approx(3_700), approx(3_960), approx(260))
    assert p.year_tax(2026).capital_tax == approx(65)
    assert p.books["A"].open_quantity("VT") == 0
    assert [f.kind for f in p.flows] == ["deposit"]                  # the transfer is neither a deposit nor a withdrawal


# --------------------------------------------------------------------------- #
# T41: privacy, and the files
# --------------------------------------------------------------------------- #

#: Made-up, distinctive values of the sample folder: none may reach the screen, a log or an error.
SAMPLE_SECRETS = ("Sample-Broker-A", "Sample-Broker-B", "Sample-Keren", "QQXY", "73310", "7331", "48930", "17310",
                  "2140", "61.57", "9173")


def weekdays(start: date, end: date) -> list[date]:
    out, day = [], start
    while day <= end:
        if day.weekday() < 5:
            out.append(day)
        day += timedelta(days=1)
    return out


def fake_market(as_of: date = date(2026, 10, 15), failing: str = "") -> mk.TableMarket:
    days = weekdays(date(2023, 1, 2), as_of)
    series = {}
    for ticker, base in (("VT", 100.0), ("VWRA", 90.0), ("VXUS", 55.0), ("QQXY", 48.0), ("ACWI", 95.0), ("IMID", 120.0), ("ISAC", 60.0)):
        divs = {d: 0.6 for d in days if ticker == "VT" and d.month in (3, 6, 9, 12) and d.weekday() == 0 and 20 <= d.day < 27}
        series[ticker] = mk.Series(days, [base + 0.01 * i for i in range(len(days))], divs)
    if failing:
        series.pop(failing, None)
    rates = {d: 3.60 + 0.0001 * (i % 50) for i, d in enumerate(days)}
    return mk.TableMarket(as_of, series, rates)


@pytest.fixture
def sample(tmp_path) -> Path:
    data = tmp_path / "data"
    shutil.copytree(SAMPLE, data)
    return data


def test_the_sample_folder_is_marked_and_holds_only_sample_data():
    for path in sorted(SAMPLE.glob("*.csv")):
        assert path.read_text().splitlines()[0] == SAMPLE_MARKER, path.name
    tracked = [p for p in REPOSITORY.rglob("*.csv") if ".git" not in p.parts and "node_modules" not in p.parts
               and not p.is_relative_to(SAMPLE)]
    assert not [p for p in tracked if not any(part.startswith(".") for part in p.relative_to(REPOSITORY).parts)]


def test_the_report_runs_on_the_sample_folder_outside_the_repository(sample, tmp_path):
    written = report.run(sample, tmp_path / "reports", fake_market(), costs=NO)
    text = written.read_text()
    assert written.name == "2026-10-15.md" and (tmp_path / "reports" / "latest.md").read_text() == text
    for heading in ("## 1. Summary", "## 2. Allocation and rebalancing", "## 3. Harvest suggestions",
                    "## 4. Against buy-and-hold VT and VWRA", "## 5. The annual report pack", "## 6. What is assumed"):
        assert heading in text
    assert text.count(report.SUGGESTION_ONLY) >= 1 and "Tax cost: " in text
    assert "Sample-Keren" in text and "QQXY" in text                 # the report file is the one place they go


def test_t41_nothing_personal_reaches_the_screen_the_log_or_an_error(sample, tmp_path, capsys, caplog):
    caplog.set_level(logging.DEBUG)
    out = tmp_path / "reports"

    def fetch(symbol, start, end):
        if symbol == "QQXY":
            raise RuntimeError(f"{symbol}: 73310 shares could not be read")       # a failing fetch, with a secret in it
        return fake_market().series.get(symbol.replace(".L", ""))

    def factory(tickers, start, as_of):
        return mk.fetch_market(tickers, start=start, as_of=as_of or date(2026, 10, 15), fetch=fetch,
                               currency_of=lambda s: "USD", rates=lambda a, b: _RateStub(fake_market()))

    code = report.main(["--data", str(sample), "--out", str(out)], market_factory=factory)
    captured = capsys.readouterr()
    assert code == 0 and captured.out.startswith("report written: ") and captured.err == ""
    printed = captured.out + captured.err + caplog.text
    for secret in SAMPLE_SECRETS:
        assert secret not in printed, secret
    assert "fetch failed (RuntimeError)" in caplog.text or caplog.text == ""


class _RateStub:
    def __init__(self, market):
        self._m = market
        self.entries = [type("E", (), {"day": d, "source": "boi"})() for d in sorted(market.rates)]

    def as_dict(self):
        return dict(self._m.rates)


def test_t41_an_error_names_the_file_and_the_row_never_a_value(sample, tmp_path, capsys):
    path = sample / "transactions.csv"
    lines = path.read_text().splitlines()
    lines.append("2026-10-02,Sample-Broker-A,sell,VT,99999,131.10,1.00,,,,,,,")
    path.write_text("\n".join(lines) + "\n")
    code = report.main(["--data", str(sample), "--out", str(tmp_path / "r")], market_factory=lambda *a: fake_market())
    err = capsys.readouterr().err
    assert code == 2 and err == "refused: transactions.csv, row 18: a sale larger than the account holds\n"
    for secret in SAMPLE_SECRETS:
        assert secret not in err


def test_a_file_without_the_sample_or_private_marker_is_refused(sample, tmp_path):
    path = sample / "plan.csv"
    path.write_text("\n".join(path.read_text().splitlines()[1:]) + "\n")
    with pytest.raises(files.DataError, match="plan.csv, row 1: the first line is not the sample or the private marker"):
        files.read_folder(sample)


def test_a_private_file_and_a_sample_file_cannot_be_mixed(sample):
    path = sample / "payments.csv"
    path.write_text(path.read_text().replace(SAMPLE_MARKER, PRIVATE_MARKER, 1))
    with pytest.raises(files.DataError, match="do not all carry the same marker"):
        files.read_folder(sample)


def test_a_data_or_report_folder_inside_the_repository_is_refused(tmp_path, capsys):
    with pytest.raises(files.DataError, match="inside the repository"):
        files.read_folder(SAMPLE)
    with pytest.raises(files.DataError, match="inside the repository"):
        report.run(tmp_path, REPOSITORY / "logs" / "investor", fake_market())
    assert report.main(["--data", str(SAMPLE), "--out", str(tmp_path)], market_factory=lambda *a: fake_market()) == 2
    assert "must be outside the repository" in capsys.readouterr().err
    with pytest.raises(SystemExit):
        report.main(["--out", str(tmp_path)])                        # --data has no default


def test_a_dividend_of_a_fund_that_is_not_us_listed_needs_the_tax_withheld(sample):
    path = sample / "transactions.csv"
    path.write_text(path.read_text() + "2026-10-02,Sample-Broker-B,dividend,VWRA,,,,10.00,USD,,,,,\n")
    inputs = files.read_folder(sample)
    p = ledger.Person(inputs.accounts, inputs.plan, rate_of(3.6))
    with pytest.raises(files.DataError, match="row 18: the US tax withheld must be filled in"):
        p.apply(inputs.transactions)


def test_the_quiet_switch_silences_the_price_librarys_loggers(caplog):
    caplog.set_level(logging.DEBUG)
    mk.quiet()
    logging.getLogger("yfinance").error("VT: 73310 shares failed")
    logging.getLogger("httpx").warning("GET https://example/VT")
    assert caplog.text == ""


def test_the_engine_imports_no_broker_model_or_phone_code():
    import ast

    allowed = ("investor", "analysis.israel_tax", "analysis.boi_rates", "config.israel_tax")
    for path in sorted((REPOSITORY / "investor").rglob("*.py")):
        for node in ast.walk(ast.parse(path.read_text())):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else (
                [node.module or ""] if isinstance(node, ast.ImportFrom) else [])
            for name in names:
                root = name.split(".")[0]
                if name.startswith(allowed) or name == "yfinance" and path.name == "market.py":
                    continue
                assert root not in ("app", "orchestrator", "shadow", "store", "coach", "learn", "dashboard", "alpaca",
                                    "anthropic", "openai", "httpx", "requests"), f"{path.name} imports {name}"


def test_the_lock_pins_the_engines_packages_with_hashes():
    lock = (REPOSITORY / "investor" / "requirements-lock.txt").read_text()
    wanted = (REPOSITORY / "investor" / "requirements.in").read_text()
    for line in wanted.splitlines():
        if line and not line.startswith("#"):
            assert line in lock, line
    assert lock.count("--hash=sha256:") >= 20 and "alpaca" not in lock and "anthropic" not in lock
