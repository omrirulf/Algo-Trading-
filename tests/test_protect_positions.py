"""A position with no stop gets one back. Nothing else may happen to it.

On 17 Sep 2026 eleven of twelve open positions woke up unprotected: the
bracket's stop leg was DAY, Alpaca cancelled it at the close, and the manager
recorded them as ``unmanaged`` and moved on. These tests pin the reversal:

* the manager *places* a stop for a naked position, at the level the audit
  log already decided on, and estimates one only when there is no record;
* ``protect_only`` does that and only that, and works after the close;
* the broker primitive is close-only by construction, GTC, and lives in one
  place; the bracket it repairs is GTC too.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from types import SimpleNamespace

import pytest

from analysis import health
from app import broker_client as bc
from app import position_manager as pm
from app.broker_client import BrokerError, OpenPosition, StopOrder
from config import settings as cfg
from orchestrator import heartbeat as hb
from tests.conftest import FakeBroker, FakeMarketData
from tests.test_position_manager import enter

R1 = cfg.PROFIT_LADDER[0].take_at_r


@pytest.fixture
def audit(_audit_log_to_tmp):
    return _audit_log_to_tmp


@pytest.fixture
def broker():
    return FakeBroker()


@pytest.fixture
def market():
    return FakeMarketData(price=100.0, atr=2.0)


def manager(broker, market, audit):
    return pm.PositionManager(broker, market, audit_path=audit)


def _managed_line(ticker, action, new_stop):
    return json.dumps({
        "ts": "2026-09-16 18:45:10,457", "level": "INFO", "event": pm.EVENT,
        "action": {"ticker": ticker, "action": action, "old_stop": 96.0, "new_stop": new_stop},
    })


def records(audit: Path, ticker: str) -> list[dict]:
    out = []
    for raw in audit.read_text().splitlines():
        rec = json.loads(raw)
        # The production formatter names the field ``event``; the test logger
        # leaves it as ``message``. The manager reads either, and so do we.
        if (rec.get("event") or rec.get("message")) == pm.EVENT and rec["action"]["ticker"] == ticker:
            out.append(rec["action"])
    return out


# --------------------------------------------------------------------------- #
# The manager: which stop, and nothing else
# --------------------------------------------------------------------------- #


def test_a_naked_position_gets_the_entry_stop_back(broker, market, audit):
    enter(broker, audit, ticker="XOM", qty=7, entry=100.0, stop=96.0)
    del broker.stop_orders["XOM"]

    report = manager(broker, market, audit).manage(protect_only=True)

    [action] = report.actions
    assert action.action == pm.PROTECTED
    assert action.new_stop == 96.0 and action.old_stop is None
    assert action.r_estimated is False
    assert broker.protected == [{"ticker": "XOM", "qty": 7, "side": "sell", "stop_price": 96.0}]
    assert broker.stop_orders["XOM"].stop_price == 96.0
    assert report.protected == 1 and report.errors == 0
    # The record says what was done, so tomorrow's report and the next pass can read it.
    [rec] = records(audit, "XOM")
    assert rec["action"] == pm.PROTECTED and rec["new_stop"] == 96.0


def test_the_stop_that_comes_back_is_the_latest_one_the_ladder_recorded(broker, market, audit):
    """A rung or a trail already moved the stop up; a lost order does not un-decide that."""
    enter(broker, audit, ticker="LLY", qty=9, entry=100.0, stop=96.0)
    with audit.open("a") as fh:
        fh.write(_managed_line("LLY", pm.TRANCHE_TAKEN, 100.0) + "\n")
        fh.write(_managed_line("LLY", pm.STOP_RAISED, 101.5) + "\n")
    del broker.stop_orders["LLY"]

    manager(broker, market, audit).manage(protect_only=True)

    assert broker.protected == [{"ticker": "LLY", "qty": 9, "side": "sell", "stop_price": 101.5}]
    assert pm.last_recorded_stop("LLY", audit) == 101.5


def test_a_position_with_no_record_gets_an_atr_stop_and_says_it_was_estimated(broker, market, audit):
    """Opened outside this system, or before the log: the entry formula, and honesty about it."""
    broker.positions.append(OpenPosition("GLD", 5, 500.0, avg_entry_price=100.0))
    market.price, market.atr = 110.0, 3.0
    expected = pm.risk_engine.calculate_stop_price(110.0, 3.0, "buy")

    report = manager(broker, market, audit).manage(protect_only=True)

    [action] = report.actions
    assert action.action == pm.PROTECTED and action.r_estimated is True
    assert action.new_stop == expected and expected < 110.0
    assert broker.protected == [{"ticker": "GLD", "qty": 5, "side": "sell", "stop_price": expected}]
    assert pm.last_recorded_stop("GLD", audit) == expected  # the estimate is now the record


def test_a_short_is_protected_with_a_buy_stop(broker, market, audit):
    enter(broker, audit, ticker="USO", qty=4, entry=100.0, stop=104.0, side="sell")
    del broker.stop_orders["USO"]

    manager(broker, market, audit).manage(protect_only=True)

    assert broker.protected == [{"ticker": "USO", "qty": 4, "side": "buy", "stop_price": 104.0}]


def test_protect_only_leaves_a_protected_position_untouched(broker, market, audit):
    """Even one sitting past a rung: protect-only is not the ladder."""
    r = enter(broker, audit, ticker="LLY", qty=9)
    market.price = 100.0 + 5 * r

    report = manager(broker, market, audit).manage(protect_only=True)

    assert report.actions == () and report.positions_seen == 1
    assert broker.protected == [] and broker.closed == [] and broker.replaced == []


def test_protect_only_works_with_the_market_closed(broker, market, audit):
    """The whole point: a GTC stop placed overnight is live at the open."""
    enter(broker, audit, ticker="XOM", qty=7)
    del broker.stop_orders["XOM"]
    broker.market_open = False

    report = manager(broker, market, audit).manage(protect_only=True)

    assert report.market_closed is False and report.protected == 1
    assert broker.protected == [{"ticker": "XOM", "qty": 7, "side": "sell", "stop_price": 96.0}]


def test_the_ordinary_pass_still_stops_at_the_close(broker, market, audit):
    enter(broker, audit, ticker="XOM", qty=7)
    del broker.stop_orders["XOM"]
    broker.market_open = False

    report = manager(broker, market, audit).manage()

    assert report.market_closed is True and broker.protected == []


def test_the_ordinary_pass_protects_instead_of_leaving_alone(broker, market, audit):
    """During the day the manager no longer records 'unmanaged' for a naked position."""
    enter(broker, audit, ticker="LLY", qty=9)
    del broker.stop_orders["LLY"]
    market.price = 100.0 + 5 * R1

    report = manager(broker, market, audit).manage()

    [action] = report.actions
    assert action.action == pm.PROTECTED
    assert report.unmanaged == 0
    assert broker.closed == [] and broker.replaced == []  # the ladder waits for the next pass
    assert broker.protected == [{"ticker": "LLY", "qty": 9, "side": "sell", "stop_price": 96.0}]


def test_a_broker_refusal_is_an_error_and_nothing_is_placed(broker, market, audit):
    enter(broker, audit, ticker="XOM", qty=7)
    del broker.stop_orders["XOM"]

    def refuse(ticker, qty, side, stop_price):
        raise BrokerError("refusing a stop for XOM: not a reduction")

    broker.submit_stop_order = refuse
    report = manager(broker, market, audit).manage(protect_only=True)

    [action] = report.actions
    assert action.action == pm.ERROR and "refusing" in action.reason
    assert report.protected == 0 and report.errors == 1
    assert "XOM" not in broker.stop_orders


def test_one_refusal_does_not_stop_the_others(broker, market, audit):
    enter(broker, audit, ticker="XOM", qty=7)
    enter(broker, audit, ticker="LLY", qty=9)
    del broker.stop_orders["XOM"], broker.stop_orders["LLY"]
    real = broker.submit_stop_order

    def flaky(ticker, qty, side, stop_price):
        if ticker == "XOM":
            raise BrokerError("boom")
        return real(ticker, qty, side, stop_price)

    broker.submit_stop_order = flaky
    report = manager(broker, market, audit).manage(protect_only=True)

    assert report.protected == 1 and report.errors == 1
    assert [p["ticker"] for p in broker.protected] == ["LLY"]


def test_the_report_counts_protected_separately(broker, market, audit):
    enter(broker, audit, ticker="XOM", qty=7)
    del broker.stop_orders["XOM"]
    out = manager(broker, market, audit).manage(protect_only=True).as_dict()
    assert out["protected"] == 1 and out["unmanaged"] == 0 and out["errors"] == 0
    assert out["actions"][0]["action"] == "protected"


# --------------------------------------------------------------------------- #
# A stop that exists but covers the wrong number of shares
# --------------------------------------------------------------------------- #


def _missize(broker, ticker, covers):
    """Leave the live stop covering a share count the position no longer holds."""
    stop = broker.stop_orders[ticker]
    broker.stop_orders[ticker] = StopOrder(stop.order_id, ticker, covers,
                                           stop.stop_price, stop.side)
    return stop.stop_price


def test_the_protection_pass_resizes_a_stop_that_covers_more_than_is_held(
    broker, market, audit
):
    """TEVA: 1 share held, 127 covered. Present, live, and unable to execute."""
    enter(broker, audit, ticker="TEVA", qty=1, entry=40.0, stop=37.0)
    level = _missize(broker, "TEVA", covers=127)

    report = manager(broker, market, audit).manage(protect_only=True)

    [action] = report.actions
    assert action.action == "stop_resized"
    assert action.remaining_qty == 1 and action.stop_qty == 1
    assert "127" in action.reason and "1 held" in action.reason
    assert broker.stop_orders["TEVA"].qty == 1
    assert [r["qty"] for r in broker.replaced] == [1]
    assert broker.stop_orders["TEVA"].stop_price == level, "size only; the ladder moves it"


def test_a_stop_of_the_right_size_is_still_left_completely_alone(broker, market, audit):
    enter(broker, audit, ticker="XOM", qty=7)
    assert manager(broker, market, audit).manage(protect_only=True).actions == ()
    assert broker.replaced == [] and broker.protected == []


def test_a_stop_covering_less_than_is_held_is_resized_too(broker, market, audit):
    """The uncovered shares are the ones with no protection at all."""
    enter(broker, audit, ticker="LLY", qty=9)
    _missize(broker, "LLY", covers=4)

    [action] = manager(broker, market, audit).manage(protect_only=True).actions
    assert action.action == "stop_resized" and action.stop_qty == 9


def test_the_full_pass_resizes_first_and_then_manages_the_position(broker, market, audit):
    """A wrong-sized stop is fixed *and* the ladder still runs the same cycle.

    Only the order matters: every later step reads the stop it just
    corrected, so the trail is measured against a stop that can actually
    execute.
    """
    enter(broker, audit, ticker="TEVA", qty=1, entry=40.0, stop=37.0)
    _missize(broker, "TEVA", covers=127)
    market.price = 41.0

    actions = manager(broker, market, audit).manage().actions
    assert [a.action for a in actions] == ["stop_resized", "held"]
    assert actions[0].stop_qty == 1 and actions[1].stop_qty == 1
    assert [r["qty"] for r in broker.replaced] == [1]


def test_a_resize_that_fails_is_recorded_as_an_error_and_alarms(broker, market, audit):
    enter(broker, audit, ticker="TEVA", qty=1, entry=40.0, stop=37.0)
    _missize(broker, "TEVA", covers=127)

    def refuse(*_args, **_kwargs):
        raise BrokerError("42210000 qty cannot be changed for advanced orders")

    broker.replace_stop_order = refuse
    [action] = manager(broker, market, audit).manage(protect_only=True).actions
    assert action.action == "error" and "42210000" in action.reason
    assert action.action in health.NAKED_ACTIONS


def test_a_cancelled_stop_with_no_replacement_is_recorded_as_no_stop(broker, market, audit):
    """Worse than an error, so it must not read like one in the record."""
    enter(broker, audit, ticker="TEVA", qty=1, entry=40.0, stop=37.0)
    _missize(broker, "TEVA", covers=127)

    def naked(*_args, **_kwargs):
        raise bc.UnprotectedPositionError("TEVA has NO live stop: ...")

    broker.replace_stop_order = naked
    [action] = manager(broker, market, audit).manage(protect_only=True).actions
    assert action.action == "no_stop"
    assert action.action in health.NAKED_ACTIONS


# --------------------------------------------------------------------------- #
# The broker primitive: close-only by construction, GTC, one place
# --------------------------------------------------------------------------- #


class _Client:
    """Just enough of the SDK client for the primitive: a book and a recorder."""

    def __init__(self, positions=(), fail=None):
        self._positions = list(positions)
        self.requests = []
        self.fail = fail

    def get_all_positions(self):
        return [SimpleNamespace(symbol=t, qty=q, market_value=abs(q) * 100.0, avg_entry_price=100.0)
                for t, q in self._positions]

    def submit_order(self, request):
        self.requests.append(request)
        if self.fail is not None:
            raise self.fail
        return SimpleNamespace(id="ord-1", stop_price=getattr(request, "stop_price", None))

    def get_orders(self, _request):
        return []


def real_broker(client):
    broker = bc.AlpacaPaperBroker.__new__(bc.AlpacaPaperBroker)
    broker._client = client
    return broker


def test_the_primitive_places_a_gtc_closing_stop_with_a_window_id():
    from alpaca.trading.enums import OrderSide, TimeInForce
    from alpaca.trading.requests import StopOrderRequest

    client = _Client(positions=[("XOM", 7)])
    placed = real_broker(client).submit_stop_order("xom", 7, "sell", 96.0)

    [request] = client.requests
    assert isinstance(request, StopOrderRequest)
    assert request.symbol == "XOM" and request.qty == 7
    assert request.side == OrderSide.SELL
    assert request.time_in_force == TimeInForce.GTC
    assert request.stop_price == 96.0
    assert request.client_order_id == bc.build_client_order_id("XOM", "protect-sell")
    assert placed == StopOrder("ord-1", "XOM", 7, 96.0, "sell")


def test_the_primitive_refuses_a_symbol_nobody_holds():
    """A STOP sell with no position would open a short. Refused before the SDK sees it."""
    client = _Client(positions=[("LLY", 9)])
    with pytest.raises(BrokerError, match="no open position"):
        real_broker(client).submit_stop_order("XOM", 7, "sell", 96.0)
    assert client.requests == []


def test_the_primitive_refuses_the_side_that_would_add():
    client = _Client(positions=[("XOM", 7)])
    with pytest.raises(BrokerError, match="would not close"):
        real_broker(client).submit_stop_order("XOM", 7, "buy", 96.0)
    assert client.requests == []


def test_the_primitive_refuses_more_than_is_held():
    client = _Client(positions=[("XOM", 7)])
    with pytest.raises(BrokerError, match="exceeds the 7 held"):
        real_broker(client).submit_stop_order("XOM", 8, "sell", 96.0)
    assert client.requests == []


def test_the_primitive_closes_a_short_with_a_buy():
    from alpaca.trading.enums import OrderSide

    client = _Client(positions=[("USO", -4)])
    real_broker(client).submit_stop_order("USO", 4, "buy", 104.0)
    assert client.requests[0].side == OrderSide.BUY


def test_a_duplicate_rejection_returns_the_stop_already_there(monkeypatch):
    client = _Client(positions=[("XOM", 7)], fail=RuntimeError("client_order_id must be unique"))
    broker = real_broker(client)
    existing = StopOrder("earlier", "XOM", 7, 96.0, "sell")
    monkeypatch.setattr(broker, "get_open_stop_order", lambda _t: existing)
    assert broker.submit_stop_order("XOM", 7, "sell", 96.0) is existing


def test_a_duplicate_rejection_with_nothing_to_show_for_it_is_loud(monkeypatch):
    client = _Client(positions=[("XOM", 7)], fail=RuntimeError("client_order_id must be unique"))
    broker = real_broker(client)
    monkeypatch.setattr(broker, "get_open_stop_order", lambda _t: None)
    with pytest.raises(bc.DuplicateOrderError):
        broker.submit_stop_order("XOM", 7, "sell", 96.0)


def test_the_bracket_stop_leg_is_good_till_cancelled():
    """DAY is how the book lost its stops overnight. Pinned in the source, not just the enum."""
    from alpaca.trading.enums import TimeInForce

    client = _Client(positions=[])
    real_broker(client).submit_bracket_order("XOM", 7, "buy", 96.0)
    [request] = client.requests
    assert request.time_in_force == TimeInForce.GTC
    assert request.stop_loss.stop_price == 96.0


def test_stop_orders_are_constructed_in_exactly_one_file():
    """The fourth primitive does not weaken the rule: one file may talk to the broker."""
    root = Path(__file__).resolve().parents[1]
    hits = []
    for path in root.rglob("*.py"):
        if any(part in {".venv", "venv", "node_modules", ".git"} for part in path.parts):
            continue
        if re.search(r"StopOrderRequest\(", path.read_text(encoding="utf-8")):
            hits.append(path.relative_to(root).as_posix())
    assert hits == ["app/broker_client.py"]


# --------------------------------------------------------------------------- #
# The heartbeat entry point: protect-only is a separate door
# --------------------------------------------------------------------------- #


class _Dispatcher:
    def __init__(self, outcome=None, exc=None):
        self.calls = []
        self.outcome = outcome
        self.exc = exc

    def manage_positions(self, protect_only=False):
        self.calls.append(protect_only)
        if self.exc:
            raise self.exc
        return self.outcome


def test_protect_positions_asks_the_dispatcher_for_protect_only():
    d = _Dispatcher(outcome={"positions_seen": 12, "protected": 11, "errors": 0})
    assert hb.protect_positions(d) == {"positions_seen": 12, "protected": 11, "errors": 0}
    assert d.calls == [True]


def test_protect_positions_reports_rather_than_raises():
    out = hb.protect_positions(_Dispatcher(exc=RuntimeError("no broker")))
    assert out == {"error": "RuntimeError: no broker"}


def test_the_direct_dispatcher_passes_protect_only_through(monkeypatch):
    from orchestrator import dispatch

    seen = {}

    class Manager:
        def __init__(self, broker, market_data, **_kw):
            seen["broker"], seen["market"] = broker, market_data

        def manage(self, protect_only=False):
            seen["protect_only"] = protect_only
            return pm.ManagementReport(positions_seen=3)

    monkeypatch.setattr(pm, "PositionManager", Manager)
    engine = SimpleNamespace(broker="the-broker", market_data="the-feed")
    out = dispatch.DirectDispatcher(engine=engine).manage_positions(protect_only=True)
    assert seen == {"broker": "the-broker", "market": "the-feed", "protect_only": True}
    assert out["positions_seen"] == 3


def test_the_cli_exits_non_zero_when_a_position_stays_naked(monkeypatch, tmp_path, capsys):
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    monkeypatch.setattr(hb, "protect_positions",
                        lambda dispatcher=None: {"positions_seen": 12, "protected": 10, "errors": 1})
    with pytest.raises(SystemExit) as exc:
        hb.main(["--protect-only"])
    assert exc.value.code == 1
    assert "12 position(s) seen, 10 given a stop, 0 stop(s) resized, 1 error(s)" in summary.read_text()
    assert '"protected": 10' in capsys.readouterr().out


def test_the_cli_exits_non_zero_when_a_stop_was_cancelled_and_not_replaced(
    monkeypatch, tmp_path, capsys
):
    """The loudest failure there is, and it is counted apart from ``errors``.

    A pass that cancels a stop and cannot place its replacement leaves the
    position with nothing. Without this it would exit green, because
    ``errors`` is zero.
    """
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    monkeypatch.setattr(hb, "protect_positions",
                        lambda dispatcher=None: {"positions_seen": 3, "protected": 0,
                                                 "errors": 0, "unprotected": 1})
    with pytest.raises(SystemExit) as exc:
        hb.main(["--protect-only"])
    assert exc.value.code == 1
    assert "1 position(s) have NO stop at all" in summary.read_text()


def test_the_cli_exits_zero_when_every_position_is_protected(monkeypatch, tmp_path):
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(tmp_path / "summary.md"))
    monkeypatch.setattr(hb, "protect_positions",
                        lambda dispatcher=None: {"positions_seen": 12, "protected": 11, "errors": 0})
    assert hb.main(["--protect-only"]) is None


def test_the_cli_never_runs_a_cycle_in_protect_mode(monkeypatch, tmp_path):
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(tmp_path / "summary.md"))
    monkeypatch.setattr(hb, "protect_positions", lambda dispatcher=None: {"positions_seen": 0})

    def no(*_a, **_k):
        raise AssertionError("run_cycle must not be called")

    monkeypatch.setattr(hb, "run_cycle", no)
    hb.main(["--protect-only", "--once"])


# --------------------------------------------------------------------------- #
# A trail must not carry a quantity it is not changing (issue #93)
# --------------------------------------------------------------------------- #


class _ReplacingClient:
    """Alpaca as it actually behaved on 21 Sep 2026, for a bracket leg.

    The real endpoint refuses ``qty`` on an order that belongs to a bracket,
    on the *presence* of the field rather than its value: an unchanged
    quantity is rejected exactly as hard as a resize.
    """

    def __init__(self, *, advanced: bool = True, covers: int = 9):
        self.advanced = advanced
        self.covers = covers
        self.requests: list = []

    def replace_order_by_id(self, order_id, request):
        self.requests.append(request)
        sent = request.to_request_fields()
        if self.advanced and "qty" in sent:
            raise RuntimeError(
                '{"code":42210000,"message":"qty cannot be changed for advanced orders"}'
            )
        return SimpleNamespace(
            id=order_id, symbol="TEVA", side="sell",
            qty=sent.get("qty", self.covers), stop_price=sent["stop_price"],
        )


def test_a_trail_that_changes_no_quantity_sends_no_quantity():
    """The whole fix. TEVA was one share, so the trail was all that ever ran."""
    client = _ReplacingClient(covers=1)
    stop = real_broker(client).replace_stop_order(
        "aae42775", qty=1, stop_price=37.20, current_qty=1,
    )
    [request] = client.requests
    assert request.to_request_fields() == {"stop_price": 37.20}
    assert request.qty is None, "a trail must not carry a qty at all"
    assert stop.stop_price == 37.20 and stop.qty == 1


def test_the_same_call_without_the_hint_is_the_bug_it_replaces():
    """Proof the fix is load-bearing, not decoration.

    Omitting ``current_qty`` is what every caller used to do, and against a
    bracket leg it reproduces 42210000 exactly.
    """
    client = _ReplacingClient(covers=1)
    with pytest.raises(BrokerError, match="qty cannot be changed for advanced orders"):
        real_broker(client).replace_stop_order("aae42775", qty=1, stop_price=37.20)
    assert client.requests[0].qty == 1, "the old shape sent a qty it never needed to"


def test_a_genuine_resize_still_sends_the_quantity():
    """Shrinking before a tranche is a real change and must still be asked for."""
    client = _ReplacingClient(advanced=False, covers=9)
    stop = real_broker(client).replace_stop_order(
        "stop-1", qty=6, stop_price=100.0, current_qty=9,
    )
    [request] = client.requests
    assert request.to_request_fields() == {"qty": 6, "stop_price": 100.0}
    assert stop.qty == 6


# --------------------------------------------------------------------------- #
# A resize the broker refuses: cancel that one order, place the right stop
# --------------------------------------------------------------------------- #


class _StuckBracketClient(_ReplacingClient):
    """A bracket leg Alpaca will not resize, over a real book.

    The one case the replace cannot serve: TEVA held 1 share behind the
    127-share stop leg of the bracket that opened it. Alpaca refuses to
    change that quantity, so the only way to make the stop the right size is
    to cancel it and place a new one.
    """

    def __init__(self, *, positions=(("TEVA", 1),), symbol="TEVA", side="sell",
                 covers=127, submit_fails=None, cancel_fails=None, readable=True,
                 settles_after=0, refuse_submits=0):
        super().__init__(advanced=True, covers=covers)
        self._positions = list(positions)
        self._symbol = symbol
        self._side = side
        self._submit_fails = submit_fails
        self._cancel_fails = cancel_fails
        self._readable = readable
        #: How many polls the cancelled order keeps reporting pending_cancel.
        self.settles_after = settles_after
        #: How many submits are refused for want of shares before one lands.
        self.refuse_submits = refuse_submits
        self._polls = 0
        self.cancelled: list[str] = []
        self.submitted: list = []
        self.calls: list[str] = []

    def replace_order_by_id(self, order_id, request):
        self.calls.append("replace")
        return super().replace_order_by_id(order_id, request)

    def get_order_by_id(self, order_id):
        # Read once to learn the symbol and side, then polled after the cancel
        # until the order reports terminal. ``still_held_for`` is how many
        # polls it keeps saying "pending_cancel" -- Alpaca settles a cancel a
        # moment after accepting it, and that moment is what stranded TEVA.
        self.calls.append("read")
        if not self._readable:
            raise RuntimeError("order not found")
        status = "new"
        if order_id in self.cancelled:
            self._polls += 1
            status = "pending_cancel" if self._polls <= self.settles_after else "canceled"
        return SimpleNamespace(id=order_id, symbol=self._symbol, side=self._side,
                               qty=self.covers, stop_price=37.0, status=status)

    def get_all_positions(self):
        self.calls.append("book")
        return [SimpleNamespace(symbol=t, qty=q, market_value=abs(q) * 100.0,
                                avg_entry_price=100.0)
                for t, q in self._positions]

    def cancel_order_by_id(self, order_id):
        self.calls.append("cancel")
        if self._cancel_fails is not None:
            raise self._cancel_fails
        self.cancelled.append(order_id)

    def submit_order(self, request):
        self.calls.append("submit")
        if self._submit_fails is not None:
            raise self._submit_fails
        if self.refuse_submits > 0:
            self.refuse_submits -= 1
            raise RuntimeError(
                '{"available":"1","code":40310000,"existing_qty":"128",'
                '"held_for_orders":"127","message":"insufficient qty available '
                'for order (requested: 128, available: 1)","symbol":"TEVA"}'
            )
        self.submitted.append(request)
        return SimpleNamespace(id="ord-new", stop_price=request.stop_price)

    def get_orders(self, _request):
        return []


def test_a_resize_the_broker_refuses_cancels_that_one_stop_and_places_a_right_sized_one():
    """TEVA, exactly. 1 share held, 127 covered, and no way to edit the number.

    A 127-share sell-stop on a 1-share position cannot execute, so the
    position was unprotected for six days while every check said it had a
    stop. A second of exposure, once, beats that.
    """
    from alpaca.trading.enums import TimeInForce

    client = _StuckBracketClient()
    stop = real_broker(client).replace_stop_order(
        "aae42775", qty=1, stop_price=37.20, current_qty=127,
    )

    assert client.cancelled == ["aae42775"]
    [request] = client.submitted
    assert request.symbol == "TEVA" and request.qty == 1
    assert request.stop_price == 37.20
    assert request.time_in_force == TimeInForce.GTC, "a DAY stop is how this started"
    assert stop == StopOrder("ord-new", "TEVA", 1, 37.20, "sell")


def test_the_replacement_is_placed_the_instant_the_old_stop_is_gone():
    """Order of operations is the whole safety argument.

    Everything that can be refused is refused while the old stop is still
    live: the order is read, the book is read, the reduction is checked.
    Only then is anything cancelled. After it, exactly two things stand
    between the cancel and the replacement, and both earn their place: one
    poll confirming the cancelled order is really gone (it holds the shares
    until it is), and ``submit_stop_order`` reading the book of its own
    accord, which is the check that makes it close-only whoever calls it.
    """
    client = _StuckBracketClient()
    real_broker(client).replace_stop_order("aae42775", qty=1, stop_price=37.20,
                                           current_qty=127)
    cut = client.calls.index("cancel")
    assert client.calls[:cut] == ["replace", "read", "book"]
    assert client.calls[cut:] == ["cancel", "read", "book", "submit"]


def test_the_replacement_waits_for_the_cancelled_stop_to_let_go_of_the_shares(monkeypatch):
    """The 22 Sep 2026 regression, pinned.

    Alpaca accepted the cancel and then went on reserving TEVA's 127 shares
    for the order it was cancelling, so the 128-share replacement was refused
    for want of shares the position plainly held -- and the position was left
    bare. The cancelled order is now polled until it reports terminal before
    the replacement is asked for at all.
    """
    slept: list[float] = []
    monkeypatch.setattr(bc.time, "sleep", slept.append)
    client = _StuckBracketClient(positions=(("TEVA", 128),), covers=127,
                                 settles_after=3)

    stop = real_broker(client).replace_stop_order("aae42775", qty=128,
                                                  stop_price=36.63, current_qty=127)

    assert stop.qty == 128 and client.submitted, "the replacement was placed"
    assert len(slept) == 3, "it waited out each pending_cancel poll and no longer"
    # The submit came after the polls, not racing them.
    assert client.calls.index("submit") > len(client.calls) - 4


def test_a_replacement_refused_for_want_of_shares_is_tried_once_more(monkeypatch):
    """Belt and braces for the same race, seen from the other side.

    If the poll says terminal but the shares are still spoken for, one
    refusal is not a reason to leave the position bare: wait out another full
    window and ask again.
    """
    monkeypatch.setattr(bc.time, "sleep", lambda _s: None)
    client = _StuckBracketClient(positions=(("TEVA", 128),), covers=127,
                                 refuse_submits=1)

    stop = real_broker(client).replace_stop_order("aae42775", qty=128,
                                                  stop_price=36.63, current_qty=127)

    assert stop.qty == 128
    assert client.calls.count("submit") == 2, "refused once, placed on the retry"


def test_a_second_refusal_for_want_of_shares_is_reported_as_naked(monkeypatch):
    """One retry, not an unbounded loop. After that a person has to be told."""
    monkeypatch.setattr(bc.time, "sleep", lambda _s: None)
    client = _StuckBracketClient(positions=(("TEVA", 128),), covers=127,
                                 refuse_submits=5)

    with pytest.raises(bc.UnprotectedPositionError) as caught:
        real_broker(client).replace_stop_order("aae42775", qty=128,
                                               stop_price=36.63, current_qty=127)
    assert client.calls.count("submit") == 2
    message = str(caught.value)
    assert "TEVA has NO live stop" in message
    assert "128 share(s) at 36.63" in message


def test_a_cancel_that_never_settles_still_gets_a_replacement_attempted(monkeypatch):
    """A wait that gave up must not become a position with no stop placed.

    The patience is bounded, and when it runs out the right move is to ask
    for the stop anyway: a stop that is refused is no worse than a stop that
    was never requested, and it might well be accepted.
    """
    monkeypatch.setattr(bc.time, "sleep", lambda _s: None)
    client = _StuckBracketClient(positions=(("TEVA", 128),), covers=127,
                                 settles_after=10_000)

    stop = real_broker(client).replace_stop_order("aae42775", qty=128,
                                                  stop_price=36.63, current_qty=127)

    assert stop.qty == 128
    assert client.calls.count("read") == 1 + bc.CANCEL_SETTLE_ATTEMPTS


def test_an_unreadable_cancelled_order_is_treated_as_gone(monkeypatch):
    """A stop nobody can find is not holding any shares; do not wait for it."""
    monkeypatch.setattr(bc.time, "sleep", lambda _s: None)

    class _VanishesAfterCancel(_StuckBracketClient):
        def get_order_by_id(self, order_id):
            if order_id in self.cancelled:
                self.calls.append("read")
                raise RuntimeError("order not found")
            return super().get_order_by_id(order_id)

    client = _VanishesAfterCancel(positions=(("TEVA", 128),), covers=127)
    stop = real_broker(client).replace_stop_order("aae42775", qty=128,
                                                  stop_price=36.63, current_qty=127)
    assert stop.qty == 128 and client.calls.count("read") == 2


def test_a_refusal_that_is_not_about_shares_is_not_retried(monkeypatch):
    """Only the race is worth another attempt. Everything else is told at once."""
    monkeypatch.setattr(bc.time, "sleep", lambda _s: None)
    client = _StuckBracketClient(positions=(("TEVA", 128),), covers=127,
                                 submit_fails=RuntimeError("market is closed"))

    with pytest.raises(bc.UnprotectedPositionError, match="market is closed"):
        real_broker(client).replace_stop_order("aae42775", qty=128,
                                               stop_price=36.63, current_qty=127)
    assert client.calls.count("submit") == 1


def test_nothing_is_cancelled_when_the_replacement_would_not_be_a_reduction():
    """The close-only rule outranks the fix. A stop still live protects something."""
    client = _StuckBracketClient(positions=(("TEVA", 1),))
    with pytest.raises(BrokerError, match="not cancelling it either"):
        real_broker(client).replace_stop_order("aae42775", qty=5, stop_price=37.20,
                                               current_qty=127)
    assert client.cancelled == [] and client.submitted == []


def test_nothing_is_cancelled_when_the_position_is_already_gone():
    client = _StuckBracketClient(positions=())
    with pytest.raises(BrokerError, match="no open position"):
        real_broker(client).replace_stop_order("aae42775", qty=1, stop_price=37.20,
                                               current_qty=127)
    assert client.cancelled == []


def test_nothing_is_cancelled_when_the_stuck_order_cannot_be_read():
    client = _StuckBracketClient(readable=False)
    with pytest.raises(BrokerError, match="could not be read"):
        real_broker(client).replace_stop_order("aae42775", qty=1, stop_price=37.20,
                                               current_qty=127)
    assert client.cancelled == []


def test_a_cancelled_stop_whose_replacement_is_refused_says_the_position_is_naked():
    """The one failure that is worse than an error, and it gets its own type.

    Every other failure in this module happens before the live stop is
    touched, so a BrokerError there means "nothing happened". This one means
    the opposite, and the message has to be actionable by a person.
    """
    client = _StuckBracketClient(submit_fails=RuntimeError("market closed"))
    with pytest.raises(bc.UnprotectedPositionError) as caught:
        real_broker(client).replace_stop_order("aae42775", qty=1, stop_price=37.20,
                                               current_qty=127)
    assert client.cancelled == ["aae42775"]
    message = str(caught.value)
    assert "TEVA has NO live stop" in message
    assert "37.2" in message and "1 share" in message


def test_a_failed_cancel_is_an_ordinary_error_because_the_stop_is_still_there():
    client = _StuckBracketClient(cancel_fails=RuntimeError("already filled"))
    with pytest.raises(BrokerError, match="could not be cancelled") as caught:
        real_broker(client).replace_stop_order("aae42775", qty=1, stop_price=37.20,
                                               current_qty=127)
    assert not isinstance(caught.value, bc.UnprotectedPositionError)
    assert client.submitted == []


def test_an_ordinary_rejection_never_reaches_the_cancel_path():
    """The fallback is gated on one rejection code, not on failure in general."""

    class _Refuses(_StuckBracketClient):
        def replace_order_by_id(self, order_id, request):
            self.calls.append("replace")
            raise RuntimeError("stop price must be below the last trade")

    client = _Refuses()
    with pytest.raises(BrokerError, match="must be below the last trade"):
        real_broker(client).replace_stop_order("aae42775", qty=1, stop_price=37.20,
                                               current_qty=127)
    assert client.calls == ["replace"], "nothing was read and nothing was cancelled"


def test_a_trail_that_is_refused_never_cancels_anything():
    """A trail sends no qty, so 42210000 cannot be about the quantity it sent."""
    client = _StuckBracketClient()
    client.advanced = False  # the request carries no qty, so it would succeed

    stop = real_broker(client).replace_stop_order("aae42775", qty=127, stop_price=37.20,
                                                  current_qty=127)
    assert client.cancelled == [] and stop.qty == 127


def test_a_reply_that_omits_the_quantity_keeps_the_one_we_know():
    """A response carrying no qty must not become a stop covering None shares."""
    class _Terse(_ReplacingClient):
        def replace_order_by_id(self, order_id, request):
            self.requests.append(request)
            return SimpleNamespace(id=order_id, symbol="TEVA", side="sell",
                                   qty=None, stop_price=37.20)

    stop = real_broker(_Terse(covers=1)).replace_stop_order(
        "aae42775", qty=1, stop_price=37.20, current_qty=1,
    )
    assert stop.qty == 1
