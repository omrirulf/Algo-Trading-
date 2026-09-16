"""The book reconstructed from the record, and the arithmetic over it.

These matter more than most report tests: this page is what its owner will
look at to answer "how much can I lose", so a number being merely plausible is
not good enough.
"""

from __future__ import annotations

import json

import pytest

from analysis import portfolio as pf
from config import settings as cfg
from config.instruments import InstrumentKind, kind_for


def entry(
    ticker="LLY", side="buy", qty=10, price=100.0, stop=90.0, ts="2026-09-16 16:35:00",
    status="ACCEPTED", atr=2.5,
) -> str:
    return json.dumps({
        "ts": ts,
        "event": "signal_processed",
        "result": {
            "ticker": ticker, "side": side, "quantity": qty, "status": status,
            "entry_price": price, "stop_price": stop, "atr": atr,
            "order_id": f"oid-{ticker}",
        },
    })


def managed(ticker="LLY", action="stop_raised", ts="2026-09-17 16:35:00", **kw) -> str:
    payload = {"ticker": ticker, "action": action}
    payload.update(kw)
    return json.dumps({"ts": ts, "event": "position_managed", "action": payload})


def audit(tmp_path, *lines):
    path = tmp_path / "audit.log"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


# --- reading the record ---------------------------------------------------


def test_an_accepted_entry_becomes_an_open_position(tmp_path):
    book = pf.read_book(audit(tmp_path, entry()))
    assert len(book.positions) == 1
    assert book.positions[0].ticker == "LLY"
    assert book.positions[0].quantity == 10


def test_a_rejected_signal_is_not_a_position(tmp_path):
    """The journal records refusals on purpose; the book must not hold them."""
    book = pf.read_book(audit(tmp_path, entry(status="REJECTED")))
    assert book.positions == ()


def test_a_missing_audit_log_is_an_empty_book_not_a_crash(tmp_path):
    assert pf.read_book(tmp_path / "nope.log").positions == ()


def test_a_truncated_line_does_not_lose_the_rest_of_the_book(tmp_path):
    """A runner dying mid-write must not cost every other position."""
    path = audit(tmp_path, entry(ticker="LLY"), '{"ts": "x", "even')
    path.write_text(path.read_text() + entry(ticker="TEVA") + "\n", encoding="utf-8")
    assert {p.ticker for p in pf.read_book(path).positions} == {"LLY", "TEVA"}


def test_a_boolean_quantity_is_not_one_share(tmp_path):
    """``True`` is an int in Python. It is not a position."""
    line = json.dumps({
        "ts": "2026-09-16 16:35:00", "event": "signal_processed",
        "result": {"ticker": "LLY", "side": "buy", "quantity": True,
                   "status": "ACCEPTED", "entry_price": 100.0, "stop_price": 90.0},
    })
    assert pf.read_book(audit(tmp_path, line)).positions == ()


def test_a_later_entry_replaces_the_earlier_one_and_resets_the_ladder(tmp_path):
    """An add-on restarts the ladder, matching ``ladder_history``."""
    book = pf.read_book(audit(
        tmp_path,
        entry(ticker="LLY", qty=10, price=100.0),
        managed(ticker="LLY", action="tranche_taken", rung=1, remaining_qty=7,
                new_stop=100.0),
        entry(ticker="LLY", qty=20, price=110.0, stop=99.0,
              ts="2026-09-18 16:35:00"),
    ))
    position = book.positions[0]
    assert position.quantity == 20
    assert position.rungs_taken == 0
    assert position.stop == 99.0, "a reset must drop the old ladder's stop"


# --- the ladder -----------------------------------------------------------


def test_a_tranche_reduces_the_quantity_held(tmp_path):
    book = pf.read_book(audit(
        tmp_path,
        entry(qty=9),
        managed(action="tranche_taken", rung=1, remaining_qty=6, new_stop=100.0),
    ))
    assert book.positions[0].quantity == 6
    assert book.positions[0].rungs_taken == 1


def test_a_position_sold_down_to_nothing_leaves_the_book(tmp_path):
    book = pf.read_book(audit(
        tmp_path,
        entry(qty=9),
        managed(action="tranche_taken", rung=1, remaining_qty=0, new_stop=100.0),
    ))
    assert book.positions == ()


def test_the_stop_in_force_is_the_ladders_once_it_has_moved(tmp_path):
    book = pf.read_book(audit(
        tmp_path, entry(price=100.0, stop=90.0), managed(new_stop=95.0),
    ))
    position = book.positions[0]
    assert position.stop == 95.0
    assert position.stop_price == 90.0, "the entry stop stays readable as 1R"


def test_a_stop_past_entry_reports_a_locked_in_gain_not_a_risk(tmp_path):
    """The whole point of the ladder. Clamping this to zero would hide it."""
    book = pf.read_book(audit(
        tmp_path, entry(price=100.0, stop=90.0, qty=10), managed(new_stop=105.0),
    ))
    position = book.positions[0]
    assert position.risk_dollars == pytest.approx(-50.0)
    assert position.protected is True


# --- the arithmetic -------------------------------------------------------


def test_risk_and_notional_for_a_long():
    p = pf.Position("LLY", "buy", 10, 100.0, 90.0)
    assert p.notional == pytest.approx(1000.0)
    assert p.risk_dollars == pytest.approx(100.0)
    assert p.stop_distance_pct == pytest.approx(10.0)


def test_risk_and_notional_for_a_short():
    """A short's stop sits above entry, and its exposure still counts."""
    p = pf.Position("TLT", "sell", 10, 100.0, 110.0)
    assert p.notional == pytest.approx(1000.0)
    assert p.risk_dollars == pytest.approx(100.0)
    assert p.direction == "Short"


def test_a_short_that_moves_the_right_way_is_a_gain():
    p = pf.Position("TLT", "sell", 10, 100.0, 110.0)
    mark = p.mark(90.0)
    assert mark.unrealised == pytest.approx(100.0)
    assert mark.pct == pytest.approx(10.0)
    assert mark.r_multiple == pytest.approx(1.0)


def test_a_long_r_multiple_is_measured_from_the_entry_stop():
    p = pf.Position("LLY", "buy", 10, 100.0, 90.0)
    assert p.mark(120.0).r_multiple == pytest.approx(2.0)


def test_no_price_means_no_invented_pnl():
    """A stale entry must never be dressed up as a mark."""
    mark = pf.Position("LLY", "buy", 10, 100.0, 90.0).mark(None)
    assert mark.known is False
    assert mark.unrealised is None and mark.r_multiple is None


def test_book_pnl_is_none_until_some_price_is_supplied():
    book = pf.Book(positions=(pf.Position("LLY", "buy", 10, 100.0, 90.0),))
    assert book.unrealised is None
    priced = pf.Book(
        positions=(pf.Position("LLY", "buy", 10, 100.0, 90.0),), prices={"LLY": 110.0}
    )
    assert priced.unrealised == pytest.approx(100.0)


def test_book_risk_is_what_every_stop_filling_at_once_costs():
    book = pf.Book(positions=(
        pf.Position("LLY", "buy", 10, 100.0, 90.0),
        pf.Position("TLT", "sell", 10, 100.0, 110.0),
    ))
    assert book.risk_dollars == pytest.approx(200.0)


# --- exposure -------------------------------------------------------------


def test_share_of_book_needs_no_equity_but_cap_use_does():
    """The distinction that keeps this page honest when equity is unknown."""
    book = pf.Book(positions=(
        pf.Position("LLY", "buy", 10, 100.0, 90.0),
        pf.Position("TEVA", "buy", 10, 300.0, 270.0),
    ))
    groups = book.by_group()
    assert sum(e.share_of_book for e in groups) == pytest.approx(100.0)
    assert all(e.used_pct is None for e in groups)

    with_equity = pf.Book(positions=book.positions, equity=10_000.0)
    assert with_equity.gross().used_pct == pytest.approx(40.0)


def test_headroom_goes_negative_when_a_cap_is_breached():
    exposure = pf.Exposure("Duration", 3_000.0, 0.25, 10_000.0, 3_000.0)
    assert exposure.used_pct == pytest.approx(30.0)
    assert exposure.headroom_pct == pytest.approx(-5.0)
    assert exposure.over_cap is True


def test_the_sleeve_split_is_the_one_the_engine_enforces():
    """Two budgets, not four.

    ``sleeve_label`` names four kinds of instrument, but
    ``risk_engine.sleeve_headroom`` buckets EQUITY against everything else.
    Reporting four budgets here would make this page disagree with the code
    that actually refuses a trade.
    """
    book = pf.Book(positions=(
        pf.Position("LLY", "buy", 10, 100.0, 90.0),     # EQUITY
        pf.Position("TLT", "sell", 10, 100.0, 110.0),   # a fund
        pf.Position("GLD", "buy", 10, 100.0, 90.0),     # a different kind of fund
    ))
    sleeves = {e.label: e for e in book.by_sleeve()}
    assert set(sleeves) == {"Single names", "Funds"}
    assert sleeves["Single names"].cap_pct == cfg.MAX_SINGLE_NAME_SLEEVE_PCT
    assert sleeves["Funds"].cap_pct == cfg.MAX_FUND_SLEEVE_PCT
    # Every non-EQUITY kind lands in the fund budget, whatever its label.
    assert sleeves["Funds"].notional == pytest.approx(2_000.0)
    assert kind_for("LLY") is InstrumentKind.EQUITY


def test_sleeve_totals_agree_with_the_engines_own_headroom():
    """Cross-checked against the engine rather than restated from it."""
    from app.risk_engine import sleeve_headroom

    equity = 100_000.0
    positions = (
        pf.Position("LLY", "buy", 10, 100.0, 90.0),
        pf.Position("TLT", "sell", 10, 100.0, 110.0),
    )
    book = pf.Book(positions=positions, equity=equity)
    sleeves = {e.label: e for e in book.by_sleeve()}

    class _P:
        def __init__(self, ticker, market_value):
            self.ticker, self.market_value = ticker, market_value

    engine_view = [_P(p.ticker, p.notional) for p in positions]
    engine_headroom = sleeve_headroom(equity, "LLY", engine_view)
    ours = equity * cfg.MAX_SINGLE_NAME_SLEEVE_PCT - sleeves["Single names"].notional
    assert engine_headroom == pytest.approx(ours)


def test_the_group_cap_spans_both_sleeves():
    """A single name and a fund in the same group are one bet, not two."""
    book = pf.Book(positions=(
        pf.Position("TLT", "sell", 10, 100.0, 110.0),
        pf.Position("IEF", "sell", 10, 100.0, 110.0),
    ))
    groups = book.by_group()
    assert len(groups) == 1, "both are duration; they must share a group"
    assert groups[0].notional == pytest.approx(2_000.0)


# --- the constants this module mirrors ------------------------------------


def test_the_rung_actions_match_the_position_manager():
    """Pinned here rather than remembered, so a rename cannot go unnoticed."""
    from app import position_manager as pm

    assert pf.TRANCHE in pm._RUNG_COMPLETING
    assert pf.STOP_RAISED in pm._RUNG_COMPLETING


def test_the_managed_event_name_matches_the_position_manager():
    from app import position_manager as pm

    assert pf.MANAGED_EVENT == pm.EVENT


# --- rendering ------------------------------------------------------------


def test_an_empty_book_says_so_rather_than_printing_a_header():
    assert "No open positions" in pf.render(pf.Book())


def test_the_text_view_names_a_protected_position():
    book = pf.Book(positions=(
        pf.Position("LLY", "buy", 10, 100.0, 90.0, current_stop=105.0),
    ))
    assert "protected" in pf.render(book)


def test_the_text_view_says_when_equity_is_missing():
    book = pf.Book(positions=(pf.Position("LLY", "buy", 10, 100.0, 90.0),))
    assert "equity is not in the record" in pf.render(book)
