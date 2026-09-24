"""Orchestrates: validate -> size -> stop -> submit.

The engine takes a broker and a market-data provider by constructor injection
so the full decision path is testable with fakes. It never reads the LLM's
rationale for anything other than logging: the LLM's opinion is an *input*
to the risk engine, never an instruction to it.
"""

from __future__ import annotations

import logging
from typing import Optional

from app import risk_engine
from app.broker_client import BrokerClient, BrokerError, DuplicateOrderError, OpenPosition
from app.logger import log_execution
from app.market_data import MarketDataError, MarketDataProvider
from app.schemas import Bias, ExecutionResult, ExecutionStatus, LLMSignal
from config import settings as cfg

log = logging.getLogger(__name__)

_SIDE_FOR_BIAS = {Bias.BULLISH: "buy", Bias.BEARISH: "sell"}


class ExecutionEngine:
    def __init__(
        self, broker: BrokerClient, market_data: MarketDataProvider,
        audit_logger: Optional[logging.Logger] = None,
    ) -> None:
        self._broker = broker
        self._market_data = market_data
        # Where the decision line goes. ``None`` is the live audit log. Set
        # only by a simulated book (``shadow/``), which must keep its own
        # record: the position manager reads that record back as its state,
        # so a shadow line in the live log would reset a live position's
        # ladder.
        self._audit_logger = audit_logger

    @property
    def broker(self) -> BrokerClient:
        """Read-only access for callers that need the market clock.

        Deliberately not a setter: the engine is constructed with its broker
        and nothing may swap it afterwards.
        """
        return self._broker

    @property
    def market_data(self) -> MarketDataProvider:
        """Read-only, for the position manager to share the engine's feed."""
        return self._market_data

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def execute(self, signal: LLMSignal) -> ExecutionResult:
        """Run every guardrail and, if all pass, submit one stop-protected order."""
        try:
            result = self._execute(signal)
        except DuplicateOrderError as exc:
            # Deliberately REJECTED, not ERROR. The order exists -- this is the
            # idempotency key doing its job. Reporting it as an error would
            # invite exactly the retry the key was added to make harmless, and
            # would pollute the audit log's error rate with a working guardrail.
            result = self._result(
                signal, ExecutionStatus.REJECTED, f"duplicate order suppressed: {exc}"
            )
        except (BrokerError, MarketDataError, risk_engine.RiskViolation) as exc:
            result = self._result(signal, ExecutionStatus.ERROR, f"{type(exc).__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001 - never let a bug submit an order
            log.exception("unexpected error while executing %s", signal.ticker)
            result = self._result(signal, ExecutionStatus.ERROR, f"unexpected {type(exc).__name__}: {exc}")

        log_execution(signal, result, logger=self._audit_logger)
        return result

    # ------------------------------------------------------------------ #
    # Decision path
    # ------------------------------------------------------------------ #

    def _execute(self, signal: LLMSignal) -> ExecutionResult:
        # Filled in once the account has been read, so every decision made
        # after that point -- accepted or refused -- records the equity it
        # was made against. Decisions before it (NEUTRAL, closed market, the
        # conviction floor) never consulted the account and say so with None.
        account: dict[str, float] = {}
        reject = lambda reason, **kw: self._result(  # noqa: E731
            signal, ExecutionStatus.REJECTED, reason, **account, **kw
        )

        # 1. NEUTRAL is a valid thing for the LLM to say; it just means "do nothing".
        side = _SIDE_FOR_BIAS.get(signal.bias)
        if side is None:
            return reject("bias is NEUTRAL; no trade")

        # 2. Market hours. This lives here, not only in the scheduler, because
        #    it is a trading decision rather than a scheduling convenience: a
        #    signal replayed by hand, or delivered late by a webhook retry,
        #    must not open a position into a closed session. Checked before
        #    any market-data fetch so a closed market costs no quote either.
        if not self._broker.is_market_open():
            return reject("market is closed")

        # 3. Conviction floor (cheap; checked before any network I/O).
        if not risk_engine.check_conviction_threshold(signal.conviction):
            return reject(
                f"conviction {signal.conviction:.2f} below minimum {cfg.MIN_CONVICTION:.2f}"
            )

        # 4. Account state.
        equity = self._broker.get_equity()
        account["equity"] = equity
        positions = self._broker.get_open_positions()
        existing = next((p for p in positions if p.ticker == signal.ticker), None)

        # 5. Position-count limit only applies when opening a *new* ticker.
        if existing is None and not risk_engine.check_position_count_limit(len(positions)):
            return reject(
                f"already holding {len(positions)} positions (max {cfg.MAX_OPEN_POSITIONS})"
            )

        # 5b. Portfolio-level exposure. Four limits, not one: the gross cap
        #     bounds the whole account, the sleeve budget keeps funds as the
        #     core and names as the satellite, the exposure-group cap is what
        #     stops a diversified watchlist producing a one-bet book -- five
        #     technology names, or a driller plus two energy funds -- and the
        #     stock-market limit bounds what all the equity groups share. All
        #     run before any market-data fetch, so a full book costs no quote.
        headroom, binding_limit = risk_engine.budget_ceiling_for(
            equity, signal.ticker, positions, side
        )
        if headroom <= 0:
            return reject(f"no room under the {binding_limit} limit")

        # 6. Never flip an existing position via a fresh entry order.
        if existing is not None and existing.side != side:
            return reject(
                f"conflicting open {existing.side} position of {existing.qty:g} shares"
            )

        # 7. Market data (price + volatility).
        price = self._market_data.get_latest_price(signal.ticker)
        atr = self._market_data.get_atr(signal.ticker)
        if not risk_engine.check_atr_sanity(atr, price):
            return reject(
                f"ATR {atr:.4f} is below {cfg.MIN_ATR_PCT_OF_PRICE:.2%} of price {price:.2f}",
                entry_price=price, atr=atr,
            )

        # 8. Stop-loss from real volatility.
        stop_price = risk_engine.calculate_stop_price(price, atr, side)

        # 9. Size under whichever per-ticker cap applies, bounded by whatever
        #    portfolio limit is tightest. The cap comes from the ticker's
        #    instrument kind in config.instruments -- never from the signal,
        #    which has no field that could carry one.
        existing_value = existing.market_value if existing else 0.0
        max_pct = risk_engine.max_position_pct_for(signal.ticker)
        qty = risk_engine.calculate_position_size(
            equity=equity,
            price=price,
            max_position_pct=max_pct,
            existing_position_value=existing_value,
            budget_ceiling=headroom,
        )
        if qty < cfg.MIN_ORDER_QTY:
            return reject(
                f"no room for {risk_engine.kind_for(signal.ticker).value} "
                f"{signal.ticker} under its {max_pct:.0%} cap or the "
                f"{binding_limit} limit: equity {equity:.2f}, price {price:.2f}, "
                f"existing exposure {existing_value:.2f}, headroom {headroom:.2f}",
                entry_price=price, stop_price=stop_price, atr=atr,
            )

        # 10. Submit. The broker method *requires* a stop price; there is no
        #     overload that submits a naked entry.
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
            equity=equity,
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
