"""Alpaca paper-trading client. The ONLY module that imports the Alpaca SDK
or reads the API keys.

``paper=True`` is hard-coded on purpose. Going live requires editing this
file, not flipping an environment variable.

Every entry order goes through ``submit_bracket_order``, which always attaches
a ``StopLossRequest``. There is no other submit path.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from config.settings import get_settings


class BrokerError(RuntimeError):
    """Raised when the broker rejects a request or is unreachable."""


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

        request = MarketOrderRequest(
            symbol=ticker,
            qty=int(qty),
            side=OrderSide.BUY if side == "buy" else OrderSide.SELL,
            type=OrderType.MARKET,
            time_in_force=TimeInForce.DAY,
            order_class=OrderClass.OTO,
            stop_loss=StopLossRequest(stop_price=stop_price),
        )
        try:
            order = self._client.submit_order(request)
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"submit_order failed for {ticker}: {exc}") from exc

        return SubmittedOrder(
            order_id=str(order.id),
            ticker=ticker,
            qty=int(qty),
            side=side,
            stop_price=stop_price,
        )
