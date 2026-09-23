"""Getting a stop back when Alpaca refuses the ordinary way.

Three positions finished 23 September 2026 with no live stop -- TIP, TLT and
UUP -- on two refusals that the code either did not recognise or did not wait
out. None of it was caused by the model switch that landed the same day; the
audit log carries the same failures on 21 and 22 September. What they have in
common is that a stop is a *reservation*: while one exists it holds the shares
it covers, and every exit here is "protect first, then sell", which only works
if the resize has actually let go before the sell is asked for.
"""

from __future__ import annotations

import pytest

from app import broker_client as bc
from app.broker_client import BrokerError, OpenPosition


class _Order:
    def __init__(self, oid="o1", symbol="TLT", side="sell", qty=10,
                 stop_price=90.0, status="canceled"):
        self.id, self.symbol, self.side = oid, symbol, side
        self.qty, self.stop_price, self.status = qty, stop_price, status


class _Sdk:
    """Just the four calls the recovery paths make."""

    def __init__(self, *, replace_raises=None, close_raises=(), terminal_after=0):
        self.replace_raises = replace_raises
        self.close_raises = list(close_raises)
        self.terminal_after = terminal_after
        self.reads = 0
        self.calls: list[str] = []

    def replace_order_by_id(self, order_id, request):
        self.calls.append("replace")
        if self.replace_raises is not None:
            raise self.replace_raises
        return _Order(oid="new", status="new")

    def get_order_by_id(self, order_id):
        self.calls.append("read")
        self.reads += 1
        return _Order(status="canceled" if self.reads > self.terminal_after else "pending_cancel")

    def cancel_order_by_id(self, order_id):
        self.calls.append("cancel")

    def close_position(self, symbol, request):
        self.calls.append("close")
        if self.close_raises:
            raise self.close_raises.pop(0)
        return _Order(oid="closed")


def _broker(sdk, positions=(OpenPosition(ticker="TLT", qty=10, market_value=900.0,
                                         avg_entry_price=90.0),)):
    broker = object.__new__(bc.AlpacaPaperBroker)
    broker._client = sdk
    broker.get_open_positions = lambda: list(positions)
    return broker


@pytest.fixture(autouse=True)
def _no_real_waiting(monkeypatch):
    monkeypatch.setattr(bc, "CANCEL_SETTLE_SECONDS", 0.0)


# --- "order chain not fully replaced" --------------------------------------


def test_a_chain_that_refuses_a_price_only_replace_is_cancelled_and_replaced():
    """The fallback used to be gated on whether a resize was being asked for.

    TLT's replace changed only the stop price, so `resizing` was False, the
    42210000 rejection was recognised and then skipped, the error propagated,
    and the position finished the day unprotected. An advanced order that will
    not take a replacement needs the same treatment whatever it objected to.
    """
    sdk = _Sdk(replace_raises=Exception('{"code":42210000,"message":"order chain not fully replaced"}'))
    broker = _broker(sdk)
    broker.submit_stop_order = lambda t, q, s, p: bc.StopOrder(
        order_id="fresh", ticker=t, qty=q, stop_price=p, side=s
    )

    # Same quantity as the live order: a price-only replace.
    out = broker.replace_stop_order("o1", 10, 88.0, current_qty=10)

    assert "cancel" in sdk.calls, "the stuck chain was never cancelled"
    assert out.order_id == "fresh"


def test_an_ordinary_refusal_still_raises_rather_than_cancelling_a_live_stop():
    """Cancelling is the dangerous move; it stays reserved for the one
    rejection that makes a replace impossible."""
    sdk = _Sdk(replace_raises=Exception("500 internal server error"))
    with pytest.raises(BrokerError, match="replace_order failed"):
        _broker(sdk).replace_stop_order("o1", 7, 88.0, current_qty=10)
    assert "cancel" not in sdk.calls


# --- the reservation the replacement leaves behind -------------------------


def test_a_successful_replace_waits_for_the_order_it_superseded():
    """Alpaca returns the new order before the old one is gone, and until it
    is gone it still reserves the shares. Every caller sells straight after
    this returns, so the wait is what makes "protect first, then sell" real.
    """
    sdk = _Sdk(terminal_after=2)
    _broker(sdk).replace_stop_order("o1", 7, 88.0, current_qty=10)
    assert sdk.calls[0] == "replace"
    assert sdk.calls.count("read") == 3, "did not poll the superseded order to terminal"


# --- "insufficient qty available" ------------------------------------------


def test_a_trim_refused_for_reserved_shares_is_asked_once_more():
    """TIP and UUP: available 0, held_for_orders the whole position, because
    the superseded stop had not let go yet. A refusal placed nothing, so the
    second ask cannot double the exit."""
    refusal = Exception('{"code":40310000,"message":"insufficient qty available for order '
                        '(requested: 3, available: 0)","held_for_orders":"10"}')
    sdk = _Sdk(close_raises=[refusal])
    assert _broker(sdk).close_position_partially("TIP", 3)
    assert sdk.calls.count("close") == 2


def test_a_trim_that_stays_refused_says_both_refusals():
    sdk = _Sdk(close_raises=[Exception("40310000 insufficient qty available"),
                             Exception("40310000 insufficient qty available")])
    with pytest.raises(BrokerError, match="again after waiting"):
        _broker(sdk).close_position_partially("TIP", 3)
    assert sdk.calls.count("close") == 2


def test_any_other_close_refusal_is_not_retried():
    """A rejected exit is not a queue to hammer; only the reservation race
    earns a second ask."""
    sdk = _Sdk(close_raises=[Exception("403 forbidden")])
    with pytest.raises(BrokerError, match="close_position failed"):
        _broker(sdk).close_position_partially("TIP", 3)
    assert sdk.calls.count("close") == 1
