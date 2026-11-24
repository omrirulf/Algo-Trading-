"""Keeps idle money invested: the core, rebalanced once a cycle.

The signal book only invests where the model takes a side, and on most days
it takes a side on few names. On 24 Nov 2026 that left the account 45%
invested and 55% in cash nobody had chosen to hold. This module is where the
remainder goes: three funds no model is asked about
(``config.instruments.CORE_FUNDS``) -- world equity, the bond market, and
Treasury bills -- bought with whatever the signal book leaves under the gross
cap, and sold back down when the signal book grows.

What the core is, and is not
----------------------------
It is the residual. Every limit a signal is sized under is computed on the
book *without* the core (``risk_engine.without_core``), so a core holding can
never refuse a signal its room. The targets here are then computed on top of
that book (``risk_engine.core_targets``): world equity up to the stock-market
limit, bonds up to the Duration ceiling, bills with what is left. The core
fills the limits that bound a loss; it never raises one.

It is not a trade. There is no stop on a core fund and no ladder: it is the
default allocation, and a stop on a benchmark holding only sells it low to
buy it back the next morning. The position manager skips these three tickers
for that reason, and the health check has nothing to say about them because
the manager records nothing for them.

One pass
--------
Run after the cycle's signals, so the book it measures is the one they left:

1. Read equity and the open book; split the core funds from the rest.
2. Add the orders this cycle's engine accepted that the broker's list does
   not show yet (``pending``). An order sent seconds ago has usually not
   filled when the list is read, and a book read as smaller than it is would
   leave the account above the gross cap until tomorrow's pass.
3. Compute each fund's target in dollars, then in whole shares.
4. Sell first, then buy. A fund is traded only when it is at least
   ``CORE_REBALANCE_BAND_PCT`` of equity from its target, so a day's price
   moves are not a day's orders; and buys are cut to what the gross cap still
   allows after the sells, so no order placed here takes the account over it.

What this module can reach
--------------------------
Two broker primitives: ``submit_core_order``, which can only buy and only a
core fund, and ``close_position_partially``, which can only reduce -- and it
is called here with a core ticker and nothing else. Neither can touch a
position in the signal book.

Every action is one ``core_managed`` line in the audit log. Nothing reads
them back as state: the pass is a function of the broker's book alone, so a
crash mid-pass heals on the next one.
"""

from __future__ import annotations

import argparse
import json
import logging
import math
from dataclasses import asdict, dataclass
from typing import Any, Optional, Sequence

from app import logger as audit_log
from app import risk_engine
from app.broker_client import BrokerClient, BrokerError, DuplicateOrderError, OpenPosition
from app.market_data import MarketDataError, MarketDataProvider
from config import settings as cfg
from config.instruments import CORE_FUNDS

log = logging.getLogger(__name__)

#: Audit event name for everything this module does.
EVENT = "core_managed"

BOUGHT = "bought"   #: below target by at least the band; shares bought
SOLD = "sold"       #: above target by at least the band; shares sold
HELD = "held"       #: within the band of its target; nothing done
ERROR = "error"     #: the broker or market data refused; nothing was done


@dataclass(frozen=True)
class CoreAction:
    """What happened to one core fund in one pass. Written to the audit log as-is."""

    ticker: str
    action: str
    qty: int = 0              #: shares bought or sold
    price: float = 0.0        #: the price the shares were counted at
    held_qty: int = 0         #: shares held once this action is done
    target_value: float = 0.0  #: dollars the fund was aimed at
    reason: str = ""

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class CoreReport:
    """One pass, for the cycle summary."""

    actions: tuple[CoreAction, ...] = ()
    market_closed: bool = False
    equity: float = 0.0
    #: Dollars in the signal book, pending orders included.
    book_value: float = 0.0
    #: Dollars in the core once this pass's orders fill, at the prices used.
    core_value: float = 0.0

    def _count(self, kind: str) -> int:
        return sum(1 for a in self.actions if a.action == kind)

    @property
    def errors(self) -> int:
        return self._count(ERROR)

    @property
    def invested_pct(self) -> float:
        """Share of equity invested once this pass's orders fill."""
        return (self.book_value + self.core_value) / self.equity if self.equity > 0 else 0.0

    def as_dict(self) -> dict[str, Any]:
        return {
            "market_closed": self.market_closed,
            "equity": self.equity,
            "book_value": self.book_value,
            "core_value": self.core_value,
            "invested_pct": self.invested_pct,
            "bought": self._count(BOUGHT),
            "sold": self._count(SOLD),
            "errors": self.errors,
            "actions": [a.as_dict() for a in self.actions],
        }


def with_pending(book: Sequence[Any], pending: Sequence[Any]) -> list[Any]:
    """``book`` plus every pending order whose ticker it does not show yet.

    A ticker already in the list is taken as filled and counted once, at
    what the broker says it is worth. One absent from it is counted at the
    notional its order was accepted for.
    """
    shown = {str(p.ticker).upper() for p in book}
    return list(book) + [p for p in pending if str(p.ticker).upper() not in shown]


def _record(action: CoreAction, logger: Optional[logging.Logger] = None) -> None:
    try:
        level = logging.ERROR if action.action == ERROR else logging.INFO
        (logger or audit_log.get_audit_logger()).log(level, EVENT, extra={"action": action.as_dict()})
    except Exception:  # noqa: BLE001 - a full disk must not take the cycle down
        log.exception("could not write the audit record for %s", action.ticker)


class CoreBook:
    """Reads the book, computes the core's targets, trades the difference."""

    def __init__(
        self,
        broker: BrokerClient,
        market_data: MarketDataProvider,
        audit_logger: Optional[logging.Logger] = None,
    ) -> None:
        self._broker = broker
        self._market_data = market_data
        self._audit_logger = audit_logger

    def rebalance(self, pending: Sequence[Any] = ()) -> CoreReport:
        """One pass over the three core funds. Never raises."""
        try:
            if not self._broker.is_market_open():
                return CoreReport(market_closed=True)
            equity = self._broker.get_equity()
            positions = self._broker.get_open_positions()
            book = with_pending(risk_engine.without_core(positions), pending)
            targets = risk_engine.core_targets(equity, book)
            gross_room, _, _ = risk_engine.core_ceilings(equity, book)
        except (BrokerError, risk_engine.RiskViolation) as exc:
            return self._failed("*", f"{type(exc).__name__}: {exc}")
        except Exception as exc:  # noqa: BLE001 - the core must not take the cycle down
            log.exception("unexpected error reading the book for the core pass")
            return self._failed("*", f"unexpected {type(exc).__name__}: {exc}")

        held = {p.ticker.strip().upper(): p for p in positions}
        band = equity * cfg.CORE_REBALANCE_BAND_PCT
        plans: list[_Plan] = []
        actions: list[CoreAction] = []
        for ticker in CORE_FUNDS:
            try:
                plans.append(self._plan(ticker, held.get(ticker), targets[ticker], band))
            except (MarketDataError, risk_engine.RiskViolation) as exc:
                actions.append(self._error(ticker, f"{type(exc).__name__}: {exc}"))
            except Exception as exc:  # noqa: BLE001 - one fund must not stop the others
                log.exception("unexpected error planning the core fund %s", ticker)
                actions.append(self._error(ticker, f"unexpected {type(exc).__name__}: {exc}"))

        # Sells first: they are what makes room, under the gross cap and in
        # the account's buying power, for anything bought after them.
        for plan in plans:
            if plan.change < 0:
                actions.append(self._sell(plan))
        # Buys share out what the gross cap still allows once every fund's
        # holding after the sells is counted -- a fund left above its target
        # inside the band still occupies room -- so no order placed here can
        # take the account over the cap.
        room = gross_room - sum(
            (p.held_qty + min(p.change, 0)) * p.price for p in plans
        )
        for plan in plans:
            if plan.change <= 0:
                continue
            plan.change = min(plan.change, max(0, math.floor(room / plan.price)))
            if plan.change < cfg.MIN_ORDER_QTY or plan.change * plan.price < band:
                plan.change = 0
                continue
            actions.append(self._buy(plan))
            room -= plan.change * plan.price
        for plan in plans:
            if plan.change == 0 and not plan.failed:
                action = CoreAction(
                    ticker=plan.ticker, action=HELD, price=plan.price, held_qty=plan.held_qty,
                    target_value=plan.target, reason="within the band of its target",
                )
                _record(action, self._audit_logger)
                actions.append(action)

        return CoreReport(
            actions=tuple(actions),
            equity=equity,
            book_value=sum(p.market_value for p in book),
            core_value=sum(p.value_after for p in plans),
        )

    # ------------------------------------------------------------------ #

    def _plan(self, ticker: str, position: Optional[OpenPosition], target: float,
              band: float) -> "_Plan":
        held_qty = int(position.qty) if position is not None else 0
        if held_qty < 0:
            raise risk_engine.RiskViolation(
                f"{ticker} is held short ({held_qty}); the core is long-only and will not touch it"
            )
        # A held fund is counted at the price the broker marks it at, so the
        # shares and the dollars this pass reasons about are the same book.
        if position is not None and held_qty > 0 and position.market_value > 0:
            price = position.market_value / held_qty
        else:
            price = self._market_data.get_latest_price(ticker)
        if price <= 0:
            raise risk_engine.RiskViolation(f"price for {ticker} must be positive, got {price}")
        change = math.floor(target / price) - held_qty
        if abs(change) * price < band:
            change = 0
        return _Plan(ticker=ticker, price=price, held_qty=held_qty, target=target, change=change)

    def _sell(self, plan: "_Plan") -> CoreAction:
        qty = -plan.change
        try:
            self._broker.close_position_partially(plan.ticker, qty)
        except BrokerError as exc:
            plan.change, plan.failed = 0, True
            return self._error(plan.ticker, f"{type(exc).__name__}: {exc}", plan)
        action = CoreAction(
            ticker=plan.ticker, action=SOLD, qty=qty, price=plan.price,
            held_qty=plan.held_qty - qty, target_value=plan.target,
            reason="above its target: the signal book grew, or a limit tightened",
        )
        _record(action, self._audit_logger)
        return action

    def _buy(self, plan: "_Plan") -> CoreAction:
        try:
            self._broker.submit_core_order(plan.ticker, plan.change)
        except DuplicateOrderError as exc:
            # The day's buy of this fund already went in. Not an error: it is
            # the idempotency key doing its job on a pass that was run twice.
            plan.change = 0
            action = CoreAction(
                ticker=plan.ticker, action=HELD, price=plan.price, held_qty=plan.held_qty,
                target_value=plan.target, reason=f"already bought today: {exc}",
            )
            plan.failed = True  # reported here; not again as a plain hold
            _record(action, self._audit_logger)
            return action
        except BrokerError as exc:
            plan.change, plan.failed = 0, True
            return self._error(plan.ticker, f"{type(exc).__name__}: {exc}", plan)
        action = CoreAction(
            ticker=plan.ticker, action=BOUGHT, qty=plan.change, price=plan.price,
            held_qty=plan.held_qty + plan.change, target_value=plan.target,
            reason="below its target: idle money invested",
        )
        _record(action, self._audit_logger)
        return action

    def _error(self, ticker: str, reason: str, plan: Optional["_Plan"] = None) -> CoreAction:
        action = CoreAction(
            ticker=ticker, action=ERROR, reason=reason,
            price=plan.price if plan else 0.0, held_qty=plan.held_qty if plan else 0,
            target_value=plan.target if plan else 0.0,
        )
        _record(action, self._audit_logger)
        return action

    def _failed(self, ticker: str, reason: str) -> CoreReport:
        return CoreReport(actions=(self._error(ticker, reason),))


@dataclass
class _Plan:
    """One fund's arithmetic for the pass. ``change`` is in shares, signed."""

    ticker: str
    price: float
    held_qty: int
    target: float
    change: int
    failed: bool = False

    @property
    def value_after(self) -> float:
        return (self.held_qty + self.change) * self.price


def render(report: CoreReport) -> str:
    """The pass as a few lines a person can read."""
    if report.market_closed:
        return "Market closed; the core was not touched."
    lines = [f"Core: {report.invested_pct:.1%} of equity invested once these fill "
             f"(signal book {report.book_value:,.0f}, core {report.core_value:,.0f})."]
    for a in report.actions:
        if a.action in (BOUGHT, SOLD):
            lines.append(f"  {a.ticker}: {a.action} {a.qty} @ ~{a.price:.2f}, {a.held_qty} held ({a.reason})")
        elif a.action == HELD:
            lines.append(f"  {a.ticker}: holding {a.held_qty} ({a.reason})")
        else:
            lines.append(f"  {a.ticker}: {a.action} -- {a.reason}")
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None) -> int:
    """Run one core pass against the paper account, in this process."""
    parser = argparse.ArgumentParser(description="Rebalance the core funds once.")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    from app.broker_client import AlpacaPaperBroker
    from app.market_data import YFinanceMarketData

    report = CoreBook(AlpacaPaperBroker(), YFinanceMarketData()).rebalance()
    print(json.dumps(report.as_dict(), indent=2) if args.as_json else render(report))
    return 1 if report.errors else 0


__all__ = [
    "EVENT", "BOUGHT", "SOLD", "HELD", "ERROR",
    "CoreAction", "CoreReport", "CoreBook", "with_pending", "render", "main",
]


if __name__ == "__main__":
    raise SystemExit(main())
