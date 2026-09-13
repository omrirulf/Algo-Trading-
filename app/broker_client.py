"""Alpaca paper-trading client. The ONLY module that imports the Alpaca SDK
or reads the API keys.

``paper=True`` is hard-coded on purpose. Going live requires editing this
file, not flipping an environment variable.

Every entry order goes through ``submit_bracket_order``, which always attaches
a ``StopLossRequest``. There is no other submit path.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Protocol

from config import settings as cfg
from config.settings import get_settings

# One entry order per ticker per side per heartbeat window. Deriving the
# window from the heartbeat interval rather than hard-coding an hour keeps
# the two in step if the cadence ever changes.
IDEMPOTENCY_WINDOW_SECONDS = cfg.HEARTBEAT_INTERVAL_MINUTES * 60

# Alpaca's own cap on client_order_id. Ours are far shorter, but truncating
# to a documented bound beats letting a long ticker produce a 422.
MAX_CLIENT_ORDER_ID = 128

# Substrings that mean "you already sent this one". Alpaca's exact wording
# for a duplicate client_order_id could not be verified from this sandbox
# (its API is unreachable here), so the match is deliberately broad and
# fails *toward* a plain BrokerError: an unrecognised message is reported as
# an ordinary submit failure, never swallowed as a benign duplicate.
_DUPLICATE_MARKERS = ("client_order_id", "duplicate", "already exists")


class BrokerError(RuntimeError):
    """Raised when the broker rejects a request or is unreachable."""


class DuplicateOrderError(BrokerError):
    """The broker refused an order because this one was already submitted.

    A subclass of ``BrokerError`` so nothing that catches broker failures
    stops catching this -- but a distinct type, because it means the opposite
    of a failure. The order exists; the guardrail worked.
    """


def build_client_order_id(ticker: str, side: str, now: datetime | None = None) -> str:
    """A stable id for "this ticker, this side, this heartbeat window".

    The point is that a *retry* collides. A random id per call would give no
    protection at all: the dangerous case is a submit that Alpaca accepted
    but whose response was lost, leaving the caller to believe it failed. The
    next cycle would then open a second position in the same name. Deriving
    the id from the window makes that second submission a duplicate Alpaca
    refuses, rather than a position nobody intended.

    The trade-off, stated plainly: a genuine second entry for the same ticker
    and side inside one window is also refused. At the default hourly cadence
    the pipeline produces at most one signal per ticker per cycle, so that
    should not arise -- and refusing a real order is the safe direction to
    fail when the alternative is doubling a position.
    """
    moment = now or datetime.now(timezone.utc)
    window = int(moment.timestamp()) // IDEMPOTENCY_WINDOW_SECONDS
    return f"{ticker.upper()}-{side.lower()}-{window}"[:MAX_CLIENT_ORDER_ID]


def _is_duplicate_rejection(exc: Exception) -> bool:
    message = str(exc).lower()
    return any(marker in message for marker in _DUPLICATE_MARKERS)


@dataclass(frozen=True)
class OpenPosition:
    ticker: str
    qty: float          # positive for long, negative for short
    market_value: float  # absolute dollar exposure

    @property
    def side(self) -> str:
        return "buy" if self.qty > 0 else "sell"


@dataclass(frozen=True)
class SubmittedOrder:
    order_id: str
    ticker: str
    qty: int
    side: str
    stop_price: float


class BrokerClient(Protocol):
    """What the execution engine needs from a broker."""

    def get_equity(self) -> float: ...

    def get_open_positions(self) -> list[OpenPosition]: ...

    def submit_bracket_order(
        self, ticker: str, qty: int, side: str, stop_price: float
    ) -> SubmittedOrder: ...


class AlpacaPaperBroker:
    """Live implementation against the Alpaca paper endpoint."""

    def __init__(self) -> None:
        from alpaca.trading.client import TradingClient  # only place the SDK is imported

        settings = get_settings()
        if not settings.alpaca_api_key or not settings.alpaca_secret_key:
            raise BrokerError(
                "ALPACA_API_KEY / ALPACA_SECRET_KEY are not set (see .env.example)"
            )
        # paper=True is deliberately hard-coded; see module docstring.
        self._client = TradingClient(
            api_key=settings.alpaca_api_key,
            secret_key=settings.alpaca_secret_key,
            paper=True,
        )

    def get_equity(self) -> float:
        try:
            account = self._client.get_account()
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"get_account failed: {exc}") from exc
        equity = float(account.equity)
        if equity <= 0:
            raise BrokerError(f"account equity is not positive: {equity}")
        return equity

    def get_open_positions(self) -> list[OpenPosition]:
        try:
            positions = self._client.get_all_positions()
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"get_all_positions failed: {exc}") from exc
        return [
            OpenPosition(
                ticker=p.symbol.upper(),
                qty=float(p.qty),
                market_value=abs(float(p.market_value)),
            )
            for p in positions
        ]

    def submit_bracket_order(
        self, ticker: str, qty: int, side: str, stop_price: float
    ) -> SubmittedOrder:
        """Market entry with a mandatory attached stop-loss (Alpaca OTO class).

        OTO = one-triggers-other: the stop-loss child order is created the
        moment the entry fills. A plain ``MarketOrderRequest`` without
        ``stop_loss`` is never constructed anywhere in this codebase.
        """
        from alpaca.trading.enums import OrderClass, OrderSide, OrderType, TimeInForce
        from alpaca.trading.requests import MarketOrderRequest, StopLossRequest

        if qty < 1 or int(qty) != qty:
            raise BrokerError(f"qty must be a positive whole number, got {qty}")
        if stop_price <= 0:
            raise BrokerError(f"stop_price must be positive, got {stop_price}")
        if side not in ("buy", "sell"):
            raise BrokerError(f"side must be 'buy' or 'sell', got {side!r}")

        client_order_id = build_client_order_id(ticker, side)
        request = MarketOrderRequest(
            symbol=ticker,
            qty=int(qty),
            side=OrderSide.BUY if side == "buy" else OrderSide.SELL,
            type=OrderType.MARKET,
            time_in_force=TimeInForce.DAY,
            order_class=OrderClass.OTO,
            stop_loss=StopLossRequest(stop_price=stop_price),
            client_order_id=client_order_id,
        )
        try:
            order = self._client.submit_order(request)
        except Exception as exc:  # noqa: BLE001
            if _is_duplicate_rejection(exc):
                raise DuplicateOrderError(
                    f"{ticker} {side} was already submitted this cycle "
                    f"(client_order_id {client_order_id}): {exc}"
                ) from exc
            raise BrokerError(f"submit_order failed for {ticker}: {exc}") from exc

        return SubmittedOrder(
            order_id=str(order.id),
            ticker=ticker,
            qty=int(qty),
            side=side,
            stop_price=stop_price,
        )
