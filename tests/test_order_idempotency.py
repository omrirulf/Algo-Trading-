"""A retried submit must not become a second position.

The dangerous case is narrow but real: Alpaca accepts an order and the
response is lost in transit. The caller sees a failure, the next cycle
produces the same signal, and the account ends up with twice the intended
exposure -- past the 5% cap that was checked against the *first* order only.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

import pytest

from app import broker_client as bc
from app.broker_client import DuplicateOrderError, OpenPosition, SubmittedOrder
from app.execution_engine import ExecutionEngine
from app.schemas import Bias, ExecutionStatus, LLMSignal
from config import settings as cfg
from config.settings import Settings
from tests.conftest import FakeMarketData

NOON = datetime(2026, 9, 13, 12, 0, tzinfo=timezone.utc)


def signal(ticker="AAPL", bias=Bias.BULLISH, conviction=0.9):
    return LLMSignal(ticker=ticker, bias=bias, conviction=conviction, rationale="because")


# --- the id itself --------------------------------------------------------


def test_the_same_decision_in_the_same_window_gets_the_same_id():
    first = bc.build_client_order_id("AAPL", "buy", NOON)
    second = bc.build_client_order_id("AAPL", "buy", NOON + timedelta(seconds=30))
    assert first == second


def test_a_different_ticker_gets_a_different_id():
    assert bc.build_client_order_id("AAPL", "buy", NOON) != bc.build_client_order_id(
        "MSFT", "buy", NOON
    )


def test_a_different_side_gets_a_different_id():
    assert bc.build_client_order_id("AAPL", "buy", NOON) != bc.build_client_order_id(
        "AAPL", "sell", NOON
    )


def test_the_next_window_gets_a_different_id():
    later = NOON + timedelta(seconds=bc.IDEMPOTENCY_WINDOW_SECONDS)
    assert bc.build_client_order_id("AAPL", "buy", NOON) != bc.build_client_order_id(
        "AAPL", "buy", later
    )


def test_the_window_is_the_heartbeat_interval():
    """If the cadence changes, the suppression window must follow it."""
    assert bc.IDEMPOTENCY_WINDOW_SECONDS == cfg.HEARTBEAT_INTERVAL_MINUTES * 60


def test_ids_are_normalised_so_case_cannot_split_a_window():
    assert bc.build_client_order_id("aapl", "BUY", NOON) == bc.build_client_order_id(
        "AAPL", "buy", NOON
    )


def test_one_second_before_the_boundary_is_still_the_same_window():
    """Windows are epoch-aligned buckets, so measure from the bucket's start.

    NOON sits on an hour boundary but not on a day boundary. When the window
    was an hour that coincidence made NOON a valid window start; at a daily
    window it is not, and NOON + (window - 1s) crosses midnight. The property
    under test is about the bucket, so derive the bucket's start explicitly.
    """
    window = bc.IDEMPOTENCY_WINDOW_SECONDS
    start = datetime.fromtimestamp((NOON.timestamp() // window) * window, tz=timezone.utc)
    edge = start + timedelta(seconds=window - 1)
    assert bc.build_client_order_id("AAPL", "buy", start) == bc.build_client_order_id(
        "AAPL", "buy", edge
    )


def test_the_id_fits_alpacas_limit():
    longest = bc.build_client_order_id("A" * 40, "sell", NOON)
    assert len(longest) <= bc.MAX_CLIENT_ORDER_ID


def test_an_id_is_generated_without_an_explicit_clock():
    assert bc.build_client_order_id("AAPL", "buy").startswith("AAPL-buy-")


# --- recognising a duplicate rejection ------------------------------------


@pytest.mark.parametrize(
    "message",
    [
        "client_order_id must be unique",
        "{'code': 42210000, 'message': 'client_order_id must be unique'}",
        "order with this client_order_id already exists",
        "duplicate order",
    ],
)
def test_duplicate_messages_are_recognised(message):
    assert bc._is_duplicate_rejection(Exception(message))


@pytest.mark.parametrize(
    "message",
    [
        "insufficient buying power",
        "connection reset by peer",
        "account is not authorized to trade",
        "",
    ],
)
def test_unrelated_failures_are_not_mistaken_for_duplicates(message):
    """An unrecognised failure must stay a failure.

    Failing this way round matters: a real error misread as a benign duplicate
    would be reported as a working guardrail and quietly dropped.
    """
    assert not bc._is_duplicate_rejection(Exception(message))


def test_a_duplicate_error_is_still_a_broker_error():
    """Anything already catching BrokerError keeps catching this."""
    assert issubclass(DuplicateOrderError, bc.BrokerError)


# --- what reaches the SDK -------------------------------------------------


class RecordingClient:
    def __init__(self, raises: Exception | None = None):
        self.raises = raises
        self.requests: list = []

    def submit_order(self, request):
        self.requests.append(request)
        if self.raises is not None:
            raise self.raises

        @dataclass
        class _Order:
            id: str = "order-1"

        return _Order()


@pytest.fixture
def broker(monkeypatch):
    """A real AlpacaPaperBroker with its SDK client swapped out."""
    import alpaca.trading.client as sdk

    monkeypatch.setattr(
        bc, "get_settings", lambda: Settings(_env_file=None, alpaca_api_key="k", alpaca_secret_key="s")
    )
    monkeypatch.setattr(sdk, "TradingClient", lambda **kw: None)

    def build(raises=None):
        instance = bc.AlpacaPaperBroker()
        instance._client = RecordingClient(raises)
        return instance

    return build


def test_the_client_order_id_is_sent_with_every_order(broker):
    b = broker()
    b.submit_bracket_order(ticker="AAPL", qty=10, side="buy", stop_price=95.0)
    sent = b._client.requests[0]
    assert sent.client_order_id.startswith("AAPL-buy-")


def test_two_submits_in_one_window_send_the_same_id(broker):
    b = broker()
    b.submit_bracket_order(ticker="AAPL", qty=10, side="buy", stop_price=95.0)
    b.submit_bracket_order(ticker="AAPL", qty=10, side="buy", stop_price=95.0)
    first, second = b._client.requests
    # Asserting equality alone would pass vacuously if the field were dropped
    # and both came back None, so pin the shape too.
    assert first.client_order_id == second.client_order_id
    assert first.client_order_id.startswith("AAPL-buy-")


def test_a_duplicate_rejection_becomes_a_duplicate_order_error(broker):
    b = broker(raises=Exception("client_order_id must be unique"))
    with pytest.raises(DuplicateOrderError) as excinfo:
        b.submit_bracket_order(ticker="AAPL", qty=10, side="buy", stop_price=95.0)
    assert "already submitted" in str(excinfo.value)


def test_an_ordinary_failure_is_still_a_plain_broker_error(broker):
    b = broker(raises=Exception("insufficient buying power"))
    with pytest.raises(bc.BrokerError) as excinfo:
        b.submit_bracket_order(ticker="AAPL", qty=10, side="buy", stop_price=95.0)
    assert not isinstance(excinfo.value, DuplicateOrderError)


def test_the_stop_loss_still_rides_along(broker):
    """Idempotency must not have loosened the mandatory-stop guarantee."""
    b = broker()
    b.submit_bracket_order(ticker="AAPL", qty=10, side="buy", stop_price=95.0)
    assert b._client.requests[0].stop_loss.stop_price == 95.0


# --- how the engine reports it --------------------------------------------


@dataclass
class DuplicatingBroker:
    equity: float = 100_000.0
    positions: list = field(default_factory=list)
    calls: int = 0
    market_open: bool = True

    def is_market_open(self) -> bool:
        return self.market_open

    def get_equity(self) -> float:
        return self.equity

    def get_open_positions(self) -> list[OpenPosition]:
        return list(self.positions)

    def submit_bracket_order(self, ticker, qty, side, stop_price) -> SubmittedOrder:
        self.calls += 1
        raise DuplicateOrderError(f"{ticker} {side} was already submitted this cycle")


def test_a_suppressed_duplicate_is_rejected_not_errored():
    engine = ExecutionEngine(broker=DuplicatingBroker(), market_data=FakeMarketData())
    result = engine.execute(signal())
    assert result.status is ExecutionStatus.REJECTED
    assert "duplicate order suppressed" in result.reason


def test_a_suppressed_duplicate_does_not_look_like_a_failure():
    """ERROR would invite the retry the whole mechanism exists to defuse."""
    engine = ExecutionEngine(broker=DuplicatingBroker(), market_data=FakeMarketData())
    assert engine.execute(signal()).status is not ExecutionStatus.ERROR


def test_a_real_broker_failure_is_still_an_error():
    @dataclass
    class FailingBroker(DuplicatingBroker):
        def submit_bracket_order(self, ticker, qty, side, stop_price):
            raise bc.BrokerError("insufficient buying power")

    engine = ExecutionEngine(broker=FailingBroker(), market_data=FakeMarketData())
    assert engine.execute(signal()).status is ExecutionStatus.ERROR
