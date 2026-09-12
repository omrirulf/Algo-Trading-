"""Orchestrates: validate -> size -> stop -> submit.

The engine takes a broker and a market-data provider by constructor injection
so the full decision path is testable with fakes. It never reads the LLM's
rationale for anything other than logging: the LLM's opinion is an *input*
to the risk engine, never an instruction to it.
"""

from __future__ import annotations

import logging

from app import risk_engine
from app.broker_client import BrokerClient, BrokerError, OpenPosition
from app.logger import log_execution
from app.market_data import MarketDataError, MarketDataProvider
from app.schemas import Bias, ExecutionResult, ExecutionStatus, LLMSignal
from config import settings as cfg

log = logging.getLogger(__name__)

_SIDE_FOR_BIAS = {Bias.BULLISH: "buy", Bias.BEARISH: "sell"}


class ExecutionEngine:
    def __init__(self, broker: BrokerClient, market_data: MarketDataProvider) -> None:
        self._broker = broker
        self._market_data = market_data

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def execute(self, signal: LLMSignal) -> ExecutionResult:
        """Run every guardrail and, if all pass, submit one stop-protected order."""
        try:
            result = self._execute(signal)
        except (BrokerError, MarketDataError, risk_engine.RiskViolation) as exc:
            result = self._result(signal, ExecutionStatus.ERROR, f"{type(exc).__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001 - never let a bug submit an order
            log.exception("unexpected error while executing %s", signal.ticker)
            result = self._result(signal, ExecutionStatus.ERROR, f"unexpected {type(exc).__name__}: {exc}")

        log_execution(signal, result)
        return result

    # ------------------------------------------------------------------ #
    # Decision path
    # ------------------------------------------------------------------ #

    def _execute(self, signal: LLMSignal) -> ExecutionResult:
        reject = lambda reason, **kw: self._result(signal, ExecutionStatus.REJECTED, reason, **kw)  # noqa: E731

        # 1. NEUTRAL is a valid thing for the LLM to say; it just means "do nothing".
        side = _SIDE_FOR_BIAS.get(signal.bias)
        if side is None:
            return reject("bias is NEUTRAL; no trade")

        # 2. Conviction floor (cheap; checked before any network I/O).
        if not risk_engine.check_conviction_threshold(signal.conviction):
            return reject(
                f"conviction {signal.conviction:.2f} below minimum {cfg.MIN_CONVICTION:.2f}"
            )

        # 3. Account state.
        equity = self._broker.get_equity()
        positions = self._broker.get_open_positions()
        existing = next((p for p in positions if p.ticker == signal.ticker), None)

        # 4. Position-count limit only applies when opening a *new* ticker.
        if existing is None and not risk_engine.check_position_count_limit(len(positions)):
            return reject(
                f"already holding {len(positions)} positions (max {cfg.MAX_OPEN_POSITIONS})"
            )

        # 5. Never flip an existing position via a fresh entry order.
        if existing is not None and existing.side != side:
            return reject(
                f"conflicting open {existing.side} position of {existing.qty:g} shares"
            )

        # 6. Market data (price + volatility).
        price = self._market_data.get_latest_price(signal.ticker)
        atr = self._market_data.get_atr(signal.ticker)
        if not risk_engine.check_atr_sanity(atr, price):
            return reject(
                f"ATR {atr:.4f} is below {cfg.MIN_ATR_PCT_OF_PRICE:.2%} of price {price:.2f}",
                entry_price=price, atr=atr,
            )

        # 7. Stop-loss from real volatility.
        stop_price = risk_engine.calculate_stop_price(price, atr, side)

        # 8. Size under the per-ticker equity cap (existing exposure counts).
        existing_value = existing.market_value if existing else 0.0
        qty = risk_engine.calculate_position_size(
            equity=equity, price=price, existing_position_value=existing_value
        )
        if qty < cfg.MIN_ORDER_QTY:
            return reject(
                f"no room under {cfg.MAX_POSITION_PCT:.0%} cap: equity {equity:.2f}, "
                f"price {price:.2f}, existing exposure {existing_value:.2f}",
                entry_price=price, stop_price=stop_price, atr=atr,
            )

        # 9. Submit. The broker method *requires* a stop price; there is no
        #    overload that submits a naked entry.
        order = self._broker.submit_bracket_order(
            ticker=signal.ticker, qty=qty, side=side, stop_price=stop_price
        )
        return self._result(
            signal,
            ExecutionStatus.ACCEPTED,
            f"submitted {side} {qty} {signal.ticker} @ ~{price:.2f}, stop {stop_price:.2f}",
            quantity=qty,
            side=side,
            entry_price=price,
            stop_price=stop_price,
            atr=atr,
            order_id=order.order_id,
        )

    @staticmethod
    def _result(signal: LLMSignal, status: ExecutionStatus, reason: str, **fields) -> ExecutionResult:
        return ExecutionResult(
            status=status,
            ticker=signal.ticker,
            bias=signal.bias,
            conviction=signal.conviction,
            reason=reason,
            **fields,
        )


__all__ = ["ExecutionEngine", "OpenPosition"]
