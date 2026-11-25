"""Orchestrates: validate -> size -> stop -> submit.

The engine takes a broker and a market-data provider by constructor injection
so the full decision path is testable with fakes. It never reads the LLM's
rationale for anything other than logging: the LLM's opinion is an *input*
to the risk engine, never an instruction to it.

The engine also remembers the orders it has just sent (the owner's "build B"
of 24 Nov 2026, Amendment 2026-11-25). The cycle dispatches a pass's orders
within a few seconds and sizes each against the broker's list of positions,
which at Alpaca shows a fill about a tenth of a second after it lands, so the
list the next order was sized against did not show the one just sent, and a
pass could carry the book past the caps this engine enforces (18 Nov 2026:
four single names each at the full cap, the sleeve at 116% of its budget).
An accepted order now counts as held -- the shares it was sent for, at the
price it was sized at -- until the list shows that many shares of the name
or for ``PASS_MEMORY_SECONDS``, whichever comes first (``_positions``). The
caps themselves are unchanged.
"""

from __future__ import annotations

import logging
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Optional

from app import risk_engine
from app.broker_client import BrokerClient, BrokerError, DuplicateOrderError, OpenPosition
from app.logger import log_execution
from app.market_data import MarketDataError, MarketDataProvider
from app.schemas import Bias, ExecutionResult, ExecutionStatus, LLMSignal
from config import settings as cfg

log = logging.getLogger(__name__)

_SIDE_FOR_BIAS = {Bias.BULLISH: "buy", Bias.BEARISH: "sell"}

#: How long an order this engine accepted keeps counting as held before the
#: broker's own list shows it (the owner's "build B" of 24 Nov 2026,
#: Amendment 2026-11-25). A market order fills within a second or two and
#: the list shows it a tenth of a second later; a pass takes a few seconds;
#: an order the list still does not show after a minute was not filled, and
#: must not be carried as exposure for the rest of a long-lived process (the
#: webhook engine lives for days; the cycle's engine for one cycle).
PASS_MEMORY_SECONDS = 60.0


@dataclass(frozen=True)
class _Sent:
    """An order this engine accepted, counted as held until the broker's list shows it in full."""

    ticker: str
    qty: float          # signed, as OpenPosition.qty: positive long, negative short
    price: float        # the price it was sized at
    at: float           # the engine's clock when it was sent


class ExecutionEngine:
    def __init__(
        self, broker: BrokerClient, market_data: MarketDataProvider,
        audit_logger: Optional[logging.Logger] = None,
        clock: Callable[[], float] = time.monotonic,
        counts_sent_orders: bool = True,
    ) -> None:
        self._broker = broker
        self._market_data = market_data
        #: A monotonic clock, injected so a test can age a remembered order.
        self._clock = clock
        #: The orders of the current pass the broker's list may not show yet.
        self._sent: list[_Sent] = []
        #: Whether those orders count as held (``_positions``). Always, live.
        #: A simulated fund (``shadow/``) replaying a cycle from before 25 Nov
        #: 2026 turns it off, because the real engine of that day did not
        #: count them; nothing in production reads it.
        self.counts_sent_orders = counts_sent_orders
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

    def _positions(self) -> list[OpenPosition]:
        """The broker's list, plus the orders of this pass it has not caught up with.

        The owner's "build B" of 24 Nov 2026 (Amendment 2026-11-25). An
        order this engine accepted counts as held -- at the shares it was
        sent for and the price it was sized at -- until the broker's list
        shows that many shares of the name, or for ``PASS_MEMORY_SECONDS``,
        whichever comes first. A name the list shows in part (a fill landing
        in pieces) is counted at the order's whole size. Orders the list has
        caught up with, and orders older than the memory, are forgotten here,
        so the list is read exactly as before once the pass has settled.
        """
        listed = self._broker.get_open_positions()
        if not self.counts_sent_orders:
            self._sent = []
            return listed
        shown = {p.ticker: p for p in listed}
        now = self._clock()
        kept: list[_Sent] = []
        merged = list(listed)
        for sent in self._sent:
            have = shown.get(sent.ticker)
            if have is not None and abs(have.qty) + 1e-9 >= abs(sent.qty):
                continue                                    # the list caught up: nothing to add
            if now - sent.at > PASS_MEMORY_SECONDS:
                continue                                    # not filled within the memory: forgotten
            kept.append(sent)
            own = OpenPosition(sent.ticker, sent.qty, abs(sent.qty) * sent.price, sent.price)
            if have is None:
                merged.append(own)
            else:
                merged = [own if p.ticker == sent.ticker else p for p in merged]
        self._sent = kept
        return merged

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

        # 4. Account state: the broker's list, plus this pass's own orders
        #    the list has not caught up with (``_positions``).
        equity = self._broker.get_equity()
        account["equity"] = equity
        positions = self._positions()
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
        # Counted as held from now on, until the list shows it (``_positions``).
        if self.counts_sent_orders:
            self._sent.append(_Sent(signal.ticker, float(qty if side == "buy" else -qty), price, self._clock()))
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
