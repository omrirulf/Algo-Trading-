"""The profit ladder: sell a winner down in thirds, walk its stop up, never loosen.

Every test runs against the fake broker and a fake feed. The audit log is a
real file in tmp_path, because the log *is* the manager's state: which rungs
were taken comes from it, and the idempotency tests are tests of that.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import pytest

from app import position_manager as pm
from app.broker_client import BrokerError, OpenPosition, StopOrder
from app.market_data import MarketDataError
from config import settings as cfg
from tests.conftest import FakeBroker, FakeMarketData

R1 = cfg.PROFIT_LADDER[0]
R2 = cfg.PROFIT_LADDER[1]


def _entry_line(ticker, entry, stop, qty, side):
    return json.dumps({
        "ts": "2026-09-15 18:45:10,457", "level": "INFO", "event": "signal_processed",
        "signal": {"ticker": ticker},
        "result": {"status": "ACCEPTED", "ticker": ticker, "entry_price": entry,
                   "stop_price": stop, "quantity": qty, "side": side},
    })


def enter(broker, audit_path, ticker="LLY", qty=9, entry=100.0, stop=96.0, side="buy"):
    """A position the engine opened: the broker holds it, the stop is live, the log says so."""
    signed = qty if side == "buy" else -qty
    broker.positions.append(OpenPosition(ticker, signed, qty * entry, avg_entry_price=entry))
    broker.stop_orders[ticker] = StopOrder(
        f"stop-{ticker}", ticker, qty, stop, "sell" if side == "buy" else "buy"
    )
    with audit_path.open("a") as fh:
        fh.write(_entry_line(ticker, entry, stop, qty, side) + "\n")
    return abs(entry - stop)


@dataclass
class SequencedBroker(FakeBroker):
    """Records the order of broker calls, so 'protect first' is provable."""

    calls: list[str] = field(default_factory=list)

    def replace_stop_order(self, order_id, qty, stop_price, current_qty=None):
        self.calls.append("replace")
        return super().replace_stop_order(order_id, qty, stop_price, current_qty)

    def close_position_partially(self, ticker, qty):
        self.calls.append("close")
        return super().close_position_partially(ticker, qty)


@pytest.fixture
def audit(_audit_log_to_tmp):
    return _audit_log_to_tmp


@pytest.fixture
def broker():
    return SequencedBroker()


@pytest.fixture
def market():
    return FakeMarketData(price=100.0, atr=2.0)


def manager(broker, market, audit):
    return pm.PositionManager(broker, market, audit_path=audit)


def audit_actions(audit):
    """Management records in the tmp log. The test formatter names the message
    field ``message`` where production names it ``event``; both are the log."""
    out = []
    for raw in audit.read_text().splitlines():
        rec = json.loads(raw)
        if (rec.get("event") or rec.get("message")) == pm.EVENT:
            out.append(rec["action"])
    return out


# --------------------------------------------------------------------------- #
# Rungs
# --------------------------------------------------------------------------- #


def test_below_the_first_rung_nothing_is_touched(broker, market, audit):
    r = enter(broker, audit)
    market.price = 100.0 + 0.5 * r
    market.atr = 5.0  # trail would sit at 92, below the 96 stop: nothing to tighten
    report = manager(broker, market, audit).manage()
    assert [a.action for a in report.actions] == [pm.HELD]
    assert broker.replaced == [] and broker.closed == []
    assert report.positions_seen == 1
    assert audit_actions(audit)[-1]["action"] == pm.HELD


def test_at_one_r_a_third_is_sold_and_the_stop_goes_to_breakeven(broker, market, audit):
    r = enter(broker, audit, qty=9, entry=100.0, stop=96.0)
    market.price = 100.0 + R1.take_at_r * r
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.TRANCHE_TAKEN
    assert action.qty_closed == 3 and action.remaining_qty == 6
    assert action.rung == 0
    assert broker.closed == [{"ticker": "LLY", "qty": 3}]
    # A real resize: the stop covered 9 and must now cover 6, so the broker
    # client sends a qty. current_qty is what it compares against.
    assert broker.replaced == [{"order_id": "stop-LLY", "ticker": "LLY", "qty": 6,
                                "stop_price": 100.0, "was": 96.0, "current_qty": 9}]
    assert broker.stop_orders["LLY"].stop_price == 100.0  # breakeven
    assert broker.positions[0].qty == 6


def test_the_stop_is_replaced_before_the_tranche_is_sold(broker, market, audit):
    """A stop still sized for the old position reserves the shares the exit needs,
    and a moment with no stop is the one thing the ladder must not create."""
    r = enter(broker, audit)
    market.price = 100.0 + r
    manager(broker, market, audit).manage()
    assert broker.calls == ["replace", "close"]


def test_at_three_r_the_second_third_goes_and_the_stop_locks_in_one_r(broker, market, audit):
    r = enter(broker, audit, qty=9, entry=100.0, stop=96.0)
    # Rung 1 already taken on an earlier day.
    market.price = 100.0 + r
    manager(broker, market, audit).manage()
    # Today: +3R.
    market.price = 100.0 + R2.take_at_r * r
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.TRANCHE_TAKEN and action.rung == 1
    assert action.qty_closed == 3 and action.remaining_qty == 3
    # The rung would put the stop at +1R (104); the trail at 112 - 2xATR is
    # 108 and tighter, and the tighter one always wins.
    rung_target = 100.0 + R2.stop_to_r * r
    trail = market.price - cfg.ATR_STOP_MULTIPLIER * market.atr
    assert trail > rung_target
    assert broker.stop_orders["LLY"].stop_price == pytest.approx(trail)
    assert broker.stop_orders["LLY"].qty == 3


def test_a_gap_through_both_rungs_takes_both_in_order(broker, market, audit):
    r = enter(broker, audit, qty=9, entry=100.0, stop=96.0)
    market.price = 100.0 + 3.5 * r
    report = manager(broker, market, audit).manage()
    assert [a.rung for a in report.actions] == [0, 1]
    assert [a.qty_closed for a in report.actions] == [3, 3]
    assert broker.calls == ["replace", "close", "replace", "close"]
    assert broker.positions[0].qty == 3  # the runner
    # +3.5R with the trail: 114 - 2xATR = 110, above the rung's +1R.
    assert broker.stop_orders["LLY"].stop_price == pytest.approx(market.price - cfg.ATR_STOP_MULTIPLIER * market.atr)


def test_the_runner_is_never_sold_by_the_ladder(broker, market, audit):
    """The fractions sum to under one, and the last share is guarded besides."""
    for base in (3, 4, 5, 9, 10, 100):
        b, m, a = SequencedBroker(), FakeMarketData(), audit
        a.write_text("")
        r = enter(b, a, qty=base)
        m.price = 100.0 + 10 * r
        pm.PositionManager(b, m, audit_path=a).manage()
        assert b.positions and abs(b.positions[0].qty) >= 1, base


def test_a_short_position_is_the_mirror_image(broker, market, audit):
    r = enter(broker, audit, qty=9, entry=100.0, stop=104.0, side="sell")
    market.price = 100.0 - r  # +1R for a short is the price falling
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.TRANCHE_TAKEN and action.side == "sell"
    assert broker.stop_orders["LLY"].stop_price == 100.0  # tightened *down* to breakeven
    assert broker.positions[0].qty == -6


def test_a_short_that_rises_is_a_loser_and_is_held(broker, market, audit):
    r = enter(broker, audit, entry=100.0, stop=104.0, side="sell")
    market.price = 100.0 + r
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.HELD
    assert report.actions[0].gain_r == pytest.approx(-1.0)


# --------------------------------------------------------------------------- #
# Never worse
# --------------------------------------------------------------------------- #


def test_the_stop_is_never_lowered(broker, market, audit):
    """A stop someone already raised past the rung's target keeps its height."""
    r = enter(broker, audit, qty=9, entry=100.0, stop=96.0)
    already_higher = 100.0 + 0.5 * r
    broker.stop_orders["LLY"] = StopOrder("stop-LLY", "LLY", 9, already_higher, "sell")
    market.price = 100.0 + r  # rung 1 would put it at 100.0, below where it is
    manager(broker, market, audit).manage()
    assert broker.stop_orders["LLY"].stop_price == already_higher
    assert broker.closed == [{"ticker": "LLY", "qty": 3}]  # the tranche still goes


def test_a_position_with_no_live_stop_is_given_one_and_nothing_else(broker, market, audit):
    """17 Sep 2026: eleven positions woke up without a stop. The manager now
    places one from the trade's own record instead of leaving it alone; the
    ladder itself waits for the next pass, so nothing is sold or replaced."""
    enter(broker, audit)  # entry stop 96.0 is in the audit log
    del broker.stop_orders["LLY"]
    market.price = 1000.0
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.PROTECTED
    assert action.new_stop == 96.0 and action.r_estimated is False
    assert broker.protected == [{"ticker": "LLY", "qty": 9, "side": "sell", "stop_price": 96.0}]
    assert broker.replaced == [] and broker.closed == []
    assert broker.positions[0].qty == 9
    assert report.protected == 1 and report.unmanaged == 0


def test_a_position_too_small_to_split_gets_the_ratchet_only(broker, market, audit):
    r = enter(broker, audit, qty=2)
    market.price = 100.0 + r
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.STOP_RAISED and action.qty_closed == 0
    assert broker.closed == []
    assert broker.stop_orders["LLY"].stop_price == 100.0
    assert broker.stop_orders["LLY"].qty == 2


def test_the_manager_can_only_ever_reduce_a_position(broker, market, audit):
    """No path here submits an entry: the fake's entry list stays empty whatever happens."""
    r = enter(broker, audit)
    market.price = 100.0 + 5 * r
    manager(broker, market, audit).manage()
    assert broker.submitted == []
    assert all(c["qty"] > 0 for c in broker.closed)


# --------------------------------------------------------------------------- #
# State comes from the record, and survives a re-run
# --------------------------------------------------------------------------- #


def test_running_twice_at_the_same_price_does_not_take_the_same_rung_twice(broker, market, audit):
    r = enter(broker, audit, qty=9)
    market.price = 100.0 + r
    first = manager(broker, market, audit).manage()
    second = manager(broker, market, audit).manage()
    assert first.tranches == 1
    assert second.tranches == 0 and second.actions[0].action == pm.HELD
    assert broker.closed == [{"ticker": "LLY", "qty": 3}]


def test_a_crash_between_replace_and_close_heals_on_the_next_pass(broker, market, audit):
    """Stop already at breakeven, tranche never sold, no rung record: still due."""
    r = enter(broker, audit, qty=9)
    broker.stop_orders["LLY"] = StopOrder("stop-LLY", "LLY", 6, 100.0, "sell")  # replaced, then crashed
    market.price = 100.0 + r
    report = manager(broker, market, audit).manage()
    assert report.tranches == 1
    assert broker.closed == [{"ticker": "LLY", "qty": 3}]
    assert broker.stop_orders["LLY"].stop_price == 100.0  # replace was a no-op on price


def test_a_fresh_entry_resets_the_ladder(broker, market, audit):
    """Two ACCEPTED records: the rungs taken after the first do not count against the second."""
    r = enter(broker, audit, qty=9)
    market.price = 100.0 + r
    manager(broker, market, audit).manage()          # rung 0 taken
    broker.positions.clear()
    broker.stop_orders.clear()
    enter(broker, audit, qty=9)                       # re-entered later
    market.price = 100.0 + r
    report = manager(broker, market, audit).manage()
    assert report.actions[0].rung == 0 and report.tranches == 1


def test_rungs_taken_counts_a_stop_raise_as_a_completed_rung(broker, market, audit):
    """A too-small position raised at rung 0 must not be re-evaluated for rung 0 forever."""
    r = enter(broker, audit, qty=2)
    market.price = 100.0 + r
    manager(broker, market, audit).manage()           # STOP_RAISED, rung 0
    entry, rungs = pm.ladder_history("LLY", audit)
    assert [x["rung"] for x in rungs] == [0]
    market.price = 100.0 + 3 * r
    report = manager(broker, market, audit).manage()
    assert [a.rung for a in report.actions] == [1]


def test_r_is_estimated_from_atr_when_the_record_is_missing(broker, market, audit):
    broker.positions.append(OpenPosition("LLY", 9, 900.0, avg_entry_price=100.0))
    broker.stop_orders["LLY"] = StopOrder("stop-LLY", "LLY", 9, 96.0, "sell")
    market.atr = 2.0                                  # R = 2 x ATR_STOP_MULTIPLIER
    r = cfg.ATR_STOP_MULTIPLIER * market.atr
    market.price = 100.0 + r
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.TRANCHE_TAKEN
    assert action.r_estimated is True
    assert action.r == pytest.approx(r)


def test_a_malformed_audit_line_is_skipped_not_fatal(broker, market, audit):
    r = enter(broker, audit)
    with audit.open("a") as fh:
        fh.write("{ this is not json\n")
    market.price = 100.0 + r
    assert manager(broker, market, audit).manage().tranches == 1


# --------------------------------------------------------------------------- #
# Failure is contained
# --------------------------------------------------------------------------- #


def test_market_closed_reads_nothing(broker, market, audit):
    enter(broker, audit)
    broker.market_open = False
    report = manager(broker, market, audit).manage()
    assert report.market_closed and report.actions == ()
    assert broker.replaced == [] and broker.closed == []


def test_one_broken_position_does_not_stop_the_others(broker, market, audit):
    r = enter(broker, audit, ticker="AAA", qty=9)
    enter(broker, audit, ticker="BBB", qty=9)

    original = broker.replace_stop_order

    def flaky(order_id, qty, stop_price, current_qty=None):
        if order_id == "stop-AAA":
            raise BrokerError("AAA is broken")
        return original(order_id, qty, stop_price, current_qty)

    broker.replace_stop_order = flaky
    market.price = 100.0 + r
    report = manager(broker, market, audit).manage()
    by = {a.ticker: a.action for a in report.actions}
    assert by == {"AAA": pm.ERROR, "BBB": pm.TRANCHE_TAKEN}
    assert report.errors == 1
    assert broker.closed == [{"ticker": "BBB", "qty": 3}]


def test_a_feed_error_is_an_error_action_not_an_exception(broker, market, audit):
    enter(broker, audit)

    def boom(ticker):
        raise MarketDataError("no quote")

    market.get_latest_price = boom
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.ERROR
    assert "MarketDataError" in report.actions[0].reason


def test_every_action_is_written_to_the_audit_log(broker, market, audit):
    r = enter(broker, audit, qty=9)
    market.price = 100.0 + 3.5 * r
    manager(broker, market, audit).manage()
    recorded = audit_actions(audit)
    assert [a["action"] for a in recorded] == [pm.TRANCHE_TAKEN, pm.TRANCHE_TAKEN]
    assert [a["rung"] for a in recorded] == [0, 1]
    assert all(a["ticker"] == "LLY" for a in recorded)


def test_render_reads_like_a_sentence(broker, market, audit):
    r = enter(broker, audit, qty=9)
    market.price = 100.0 + r
    text = pm.render(manager(broker, market, audit).manage())
    assert "1 tranche(s) sold" in text
    assert "LLY: +1.00R -> sold 3, 6 left; stop 96.00 -> 100.00" in text


# --------------------------------------------------------------------------- #
# The audit logger is resolved at call time, so a redirect actually redirects
# --------------------------------------------------------------------------- #


def test_the_manager_resolves_the_audit_logger_through_the_module(broker, market, audit, monkeypatch):
    """Regression: a binding taken at import wrote 42 fake records into the
    repository's real audit log on the first run of this suite, straight past
    the fixture that exists to prevent exactly that."""
    import logging

    seen = []

    class Spy:
        def log(self, level, event, extra=None):
            seen.append((event, extra["action"]["action"]))

    monkeypatch.setattr(pm.audit_log, "get_audit_logger", lambda: Spy())
    r = enter(broker, audit)
    market.price = 100.0 + r
    manager(broker, market, audit).manage()
    assert seen == [(pm.EVENT, pm.TRANCHE_TAKEN)]


def test_the_suite_never_writes_into_the_repositorys_audit_log(broker, market, audit):
    """The fixture's redirect must hold for the manager as it does for the engine.

    Addressed by repository path on purpose: inside the suite the fixture has
    already repointed ``cfg.AUDIT_LOG_PATH`` at the tmp file, so reading the
    setting here would compare the tmp log with itself and prove nothing.
    """
    real = Path(__file__).resolve().parent.parent / "logs" / "execution_audit.log"
    assert real != audit
    before = real.read_text() if real.exists() else None
    r = enter(broker, audit)
    market.price = 100.0 + 5 * r
    manager(broker, market, audit).manage()
    after = real.read_text() if real.exists() else None
    assert before == after



# --------------------------------------------------------------------------- #
# The stop trails the price, every cycle, rung or no rung
# --------------------------------------------------------------------------- #


def test_the_stop_trails_the_price_up_with_no_rung_due(broker, market, audit):
    """Halfway to the first rung the stop already follows: 102 - 2x2 = 98 > 96."""
    r = enter(broker, audit, qty=9, entry=100.0, stop=96.0)
    market.price, market.atr = 102.0, 2.0
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.STOP_RAISED and action.reason == "trailing stop"
    assert action.rung is None and action.qty_closed == 0
    # Nothing is sold, so the stop still covers all 9 shares. The manager must
    # say so -- qty == current_qty is what lets the broker client leave the
    # field out, and a bracket leg refuses a trail that carries one (issue #93).
    assert broker.replaced == [{"order_id": "stop-LLY", "ticker": "LLY", "qty": 9,
                                "stop_price": 98.0, "was": 96.0, "current_qty": 9}]
    assert broker.closed == []


def test_a_trailing_raise_is_not_a_rung(broker, market, audit):
    """Trailing every day must not make the ladder think a rung was taken."""
    r = enter(broker, audit, qty=9)
    market.price, market.atr = 102.0, 2.0
    manager(broker, market, audit).manage()                 # trailed to 98
    _, rungs = pm.ladder_history("LLY", audit)
    assert rungs == []
    market.price = 100.0 + r                                # now +1R
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.TRANCHE_TAKEN and report.actions[0].rung == 0


def test_the_trail_never_loosens_when_atr_widens(broker, market, audit):
    enter(broker, audit, qty=9)
    market.price, market.atr = 102.0, 2.0
    manager(broker, market, audit).manage()                 # 98
    market.atr = 5.0                                        # candidate 92
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.HELD
    assert broker.stop_orders["LLY"].stop_price == 98.0


def test_a_falling_price_does_not_move_the_stop(broker, market, audit):
    enter(broker, audit, qty=9)
    market.price, market.atr = 99.0, 2.0                    # candidate 95 < 96
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.HELD
    assert broker.replaced == []


def test_trail_and_rung_in_the_same_cycle_apply_the_tighter_and_record_the_true_old_stop(broker, market, audit):
    r = enter(broker, audit, qty=9, entry=100.0, stop=96.0)
    market.price, market.atr = 104.0, 0.5                   # +1R; trail = 103 > rung's 100
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.TRANCHE_TAKEN
    assert action.old_stop == 96.0 and action.new_stop == 103.0
    assert broker.stop_orders["LLY"].stop_price == 103.0
    assert broker.calls == ["replace", "close"]


def test_a_rung_too_small_to_split_still_carries_the_trail(broker, market, audit):
    """qty 2: no tranche, but the replace must still land the trailed stop."""
    r = enter(broker, audit, qty=2, entry=100.0, stop=96.0)
    market.price, market.atr = 104.0, 0.5                   # +1R; trail 103
    report = manager(broker, market, audit).manage()
    [action] = report.actions
    assert action.action == pm.STOP_RAISED and action.rung == 0
    assert broker.stop_orders["LLY"].stop_price == 103.0


def test_a_short_trails_down(broker, market, audit):
    enter(broker, audit, qty=9, entry=100.0, stop=104.0, side="sell")
    market.price, market.atr = 98.0, 2.0                    # candidate 102 < 104
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.STOP_RAISED
    assert broker.stop_orders["LLY"].stop_price == 102.0


def test_an_absurd_atr_leaves_the_stop_alone_rather_than_failing(broker, market, audit):
    """102 - 2x100 is negative; the stop formula refuses; the position is simply held."""
    enter(broker, audit, qty=9)
    market.price, market.atr = 102.0, 100.0
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.HELD
    assert report.errors == 0 and broker.replaced == []


def test_a_zero_atr_skips_the_trail(broker, market, audit):
    enter(broker, audit, qty=9)
    market.price, market.atr = 102.0, 0.0
    report = manager(broker, market, audit).manage()
    assert report.actions[0].action == pm.HELD


def test_render_says_trailing(broker, market, audit):
    enter(broker, audit, qty=9)
    market.price, market.atr = 102.0, 2.0
    text = pm.render(manager(broker, market, audit).manage())
    assert "LLY: +0.50R -> stop 96.00 -> 98.00 (trailing stop)" in text


# --------------------------------------------------------------------------- #
# Group-cap trim: a cap that tightens applies to what is already held, too
# --------------------------------------------------------------------------- #


def test_an_over_cap_group_is_trimmed_pro_rata(broker, market, audit):
    """A group over its ceiling is trimmed back toward it on the very next
    pass, largest exposure first.

    Equity is 100k and Duration's ceiling is 30%, so the cap is $30,000. TLT
    $18,300 + IEF $17,700 + TIP $6,000 = $42,000, a $12,000 excess split
    pro-rata by each ticker's share of that $42,000 and floored to whole
    shares at the $100 price.
    """
    enter(broker, audit, ticker="TLT", qty=183, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="IEF", qty=177, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="TIP", qty=60, entry=100.0, stop=104.0, side="sell")

    report = manager(broker, market, audit).manage()

    trims = {a.ticker: a for a in report.actions if a.action == pm.GROUP_CAP_TRIMMED}
    assert set(trims) == {"TLT", "IEF", "TIP"}
    assert trims["TLT"].qty_closed == 52 and trims["TLT"].remaining_qty == 131
    assert trims["IEF"].qty_closed == 50 and trims["IEF"].remaining_qty == 127
    assert trims["TIP"].qty_closed == 17 and trims["TIP"].remaining_qty == 43
    assert report.group_trims == 3
    assert all("'Duration' group" in a.reason for a in trims.values())
    # The stop shrinks with the position, before the sell -- same order as a
    # ladder tranche -- and the broker's own book reflects the smaller size.
    tlt_replace = next(r for r in broker.replaced if r["ticker"] == "TLT")
    assert tlt_replace["qty"] == 131 and tlt_replace["stop_price"] == 104.0 and tlt_replace["was"] == 104.0
    assert {"ticker": "TLT", "qty": 52} in broker.closed
    by_ticker = {p.ticker: abs(p.qty) for p in broker.positions}
    assert by_ticker == {"TLT": 131, "IEF": 127, "TIP": 43}


def test_a_group_within_its_cap_is_left_alone(broker, market, audit):
    enter(broker, audit, ticker="TLT", qty=50, entry=100.0, stop=104.0, side="sell")  # 5% of equity
    report = manager(broker, market, audit).manage()
    assert report.group_trims == 0
    assert all(a.action != pm.GROUP_CAP_TRIMMED for a in report.actions)


def test_the_trim_never_takes_the_last_share(broker, market, audit):
    """A position too small to leave a runner is skipped, not fully closed --
    a forced trim is a reduction, never a liquidation."""
    enter(broker, audit, ticker="TLT", qty=400, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="IEF", qty=1, entry=100.0, stop=104.0, side="sell")
    report = manager(broker, market, audit).manage()
    trims = {a.ticker for a in report.actions if a.action == pm.GROUP_CAP_TRIMMED}
    assert "IEF" not in trims
    assert any(p.ticker == "IEF" and abs(p.qty) == 1 for p in broker.positions)


def test_the_ladder_uses_post_trim_size_not_the_stale_snapshot(broker, market, audit):
    """The positions list read before the trim is stale the moment it runs.

    Both legs are at exactly +1R when the pass runs, due a ladder tranche
    the same cycle the trim runs in. If the ladder sized that tranche off
    the pre-trim qty instead of what the trim actually left behind, it
    would try to sell a third of a position bigger than the one it is
    holding -- silently wrong rather than a crash, since the broker still
    has enough shares to permit the oversized sell.

    The trim's own sizing uses today's price (96, not the $100 entry), so
    TLT's $3,050 pro-rata share buys 31 shares at 96 and IEF's $2,950 buys
    30 -- the dollar shares, not the share counts, are what the split is
    pro-rata in.
    """
    enter(broker, audit, ticker="TLT", qty=183, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="IEF", qty=177, entry=100.0, stop=104.0, side="sell")
    market.price = 96.0  # short, entry 100, stop 104 -> R = 4; (100-96)/4 = +1R
    report = manager(broker, market, audit).manage()

    trims = {a.ticker: a for a in report.actions if a.action == pm.GROUP_CAP_TRIMMED}
    assert trims["TLT"].qty_closed == 31 and trims["TLT"].remaining_qty == 152
    assert trims["IEF"].qty_closed == 30 and trims["IEF"].remaining_qty == 147

    rungs = {a.ticker: a for a in report.actions if a.action == pm.TRANCHE_TAKEN}
    assert rungs["TLT"].qty_closed == 50 and rungs["TLT"].remaining_qty == 102
    assert rungs["IEF"].qty_closed == 49 and rungs["IEF"].remaining_qty == 98
    assert report.positions_seen == 2


def test_one_broken_trim_does_not_stop_the_rest_of_the_group(broker, market, audit):
    enter(broker, audit, ticker="TLT", qty=183, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="IEF", qty=177, entry=100.0, stop=104.0, side="sell")

    original = broker.replace_stop_order

    def flaky(order_id, qty, stop_price, current_qty=None):
        if order_id == "stop-TLT":
            raise BrokerError("TLT stop replace is broken")
        return original(order_id, qty, stop_price, current_qty)

    broker.replace_stop_order = flaky
    report = manager(broker, market, audit).manage()
    by_ticker = {
        a.ticker: a.action for a in report.actions
        if a.action in (pm.GROUP_CAP_TRIMMED, pm.ERROR)
    }
    assert by_ticker.get("TLT") == pm.ERROR
    assert by_ticker.get("IEF") == pm.GROUP_CAP_TRIMMED


def test_group_trim_is_skipped_when_equity_is_not_positive(broker, market, audit):
    enter(broker, audit, ticker="TLT", qty=183, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="IEF", qty=177, entry=100.0, stop=104.0, side="sell")
    broker.equity = 0.0
    report = manager(broker, market, audit).manage()
    assert report.group_trims == 0
    assert not any(a.action == pm.ERROR for a in report.actions)


def test_render_reports_group_trims(broker, market, audit):
    enter(broker, audit, ticker="TLT", qty=183, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="IEF", qty=177, entry=100.0, stop=104.0, side="sell")
    enter(broker, audit, ticker="TIP", qty=60, entry=100.0, stop=104.0, side="sell")
    text = pm.render(manager(broker, market, audit).manage())
    assert "3 trimmed for a group cap" in text
    assert "'Duration' group exposure over its cap; trimmed pro-rata" in text
