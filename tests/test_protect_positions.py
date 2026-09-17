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
    assert "12 position(s) seen, 10 given a stop, 1 error(s)" in summary.read_text()
    assert '"protected": 10' in capsys.readouterr().out


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
