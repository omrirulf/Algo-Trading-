"""The insider arm is a fixed function of the snapshot the model saw.

It must be deterministic and recomputable from the journal, it must count
only what a person spent their own money on, and it must be NEUTRAL --
not BEARISH -- when the evidence is thin, because selling is not evidence.
"""

from __future__ import annotations

from datetime import date

from app.schemas import Bias
from config import settings as cfg
from orchestrator.insiders import InsiderSnapshot, InsiderTrade
from rules import insider_buying

DAY = date(2026, 9, 21)


def trade(who, when="2026-09-01", shares=1_000.0, role="Director") -> InsiderTrade:
    return InsiderTrade(when=when, who=who, role=role, shares=shares, value=None)


def snapshot(buys=(), sells=()) -> InsiderSnapshot:
    return InsiderSnapshot(buys=list(buys), sells=list(sells))


# --- the rule -----------------------------------------------------------------


def test_two_leaders_buying_with_net_buying_is_bullish():
    sig = insider_buying.signal_for("CAT", snapshot(buys=[trade("Ann"), trade("Bob")]), DAY)
    assert sig.bias is Bias.BULLISH
    assert sig.conviction == insider_buying.CONVICTION
    assert sig.ticker == "CAT"


def test_one_buyer_is_not_a_cluster():
    sig = insider_buying.signal_for("CAT", snapshot(buys=[trade("Ann"), trade("Ann", "2026-08-01")]), DAY)
    assert sig.bias is Bias.NEUTRAL
    assert "1 distinct" in sig.rationale


def test_buying_that_is_outweighed_by_selling_is_neutral_not_bearish():
    snap = snapshot(buys=[trade("Ann", shares=100), trade("Bob", shares=100)],
                    sells=[trade("Cy", shares=10_000)])
    sig = insider_buying.signal_for("CAT", snap, DAY)
    assert sig.bias is Bias.NEUTRAL
    assert "sold" in sig.rationale


def test_it_is_never_bearish():
    sig = insider_buying.signal_for("CAT", snapshot(sells=[trade("Ann"), trade("Bob"), trade("Cy")]), DAY)
    assert sig.bias is Bias.NEUTRAL


def test_its_conviction_clears_the_floor():
    assert insider_buying.CONVICTION >= cfg.MIN_CONVICTION


# --- what counts as a purchase ------------------------------------------------


def test_the_issuer_buying_back_its_own_shares_is_not_a_leader():
    """Royal Bank of Canada 'purchasing' RY is a buyback, not a person's view."""
    snap = snapshot(buys=[trade("Royal Bank of Canada", role="Issuer"), trade("Royal Bank of Canada", role="Issuer"),
                          trade("Ann")])
    assert insider_buying.signal_for("RY", snap, DAY).bias is Bias.NEUTRAL


def test_a_ten_percent_owner_is_a_fund_not_a_leader():
    snap = snapshot(buys=[trade("Big Fund LP", role="10% Owner"), trade("Ann")])
    assert insider_buying.signal_for("CAT", snap, DAY).bias is Bias.NEUTRAL


def test_a_purchase_outside_the_window_does_not_count():
    old = DAY.replace(year=DAY.year - 1).isoformat()
    snap = snapshot(buys=[trade("Ann", when=old), trade("Bob")])
    assert insider_buying.signal_for("CAT", snap, DAY).bias is Bias.NEUTRAL
    edge = (DAY.toordinal() - insider_buying.WINDOW_DAYS)
    snap = snapshot(buys=[trade("Ann", when=date.fromordinal(edge).isoformat()), trade("Bob")])
    assert insider_buying.signal_for("CAT", snap, DAY).bias is Bias.BULLISH


def test_a_trade_with_no_date_cannot_be_placed_in_the_window():
    snap = snapshot(buys=[trade("Ann", when=None), trade("Bob")])
    assert insider_buying.signal_for("CAT", snap, DAY).bias is Bias.NEUTRAL


# --- thin inputs are outcomes, not errors -------------------------------------


def test_no_section_is_neutral_with_the_reason():
    sig = insider_buying.signal_for("XLE", None, DAY)
    assert sig.bias is Bias.NEUTRAL and "no insider section" in sig.rationale


def test_no_day_is_neutral():
    assert insider_buying.signal_for("CAT", snapshot(buys=[trade("Ann"), trade("Bob")]), None).bias is Bias.NEUTRAL


# --- recomputable from the journal --------------------------------------------


def test_the_same_journalled_section_gives_the_same_call():
    snap = snapshot(buys=[trade("Ann"), trade("Bob")], sells=[trade("Cy", shares=5.0)])
    again = InsiderSnapshot.from_dict(snap.as_dict())
    assert again == snap
    assert insider_buying.signal_for("CAT", again, DAY) == insider_buying.signal_for("CAT", snap, DAY)


def test_from_dict_tolerates_a_sparse_or_older_line():
    snap = InsiderSnapshot.from_dict({"buys": [{"who": "Ann", "when": "2026-09-01"}], "distinct_buyers": None})
    assert snap.buys[0].who == "Ann" and snap.buys[0].shares is None
    assert snap.distinct_buyers == 0 and snap.window_days == 180


# --- the parameters are fixed ---------------------------------------------------


def test_the_parameters_are_the_registered_ones():
    """Lakonishok and Lee's six months; the smallest cluster. If this test
    is being edited to make a number look better, stop."""
    assert insider_buying.WINDOW_DAYS == 180
    assert insider_buying.MIN_DISTINCT_BUYERS == 2
    assert insider_buying.CONVICTION == 0.5
