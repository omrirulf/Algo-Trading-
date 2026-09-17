"""Walks a winning position up the profit ladder, and its stop up behind it.

The execution engine opens positions; nothing, until this module, ever
managed one afterwards. A trade was entered with a stop and then left alone:
the only way out was that stop, so a winner sat in the book indefinitely
while a loser left on schedule. That is backwards, and it blocks new signals
once ``MAX_OPEN_POSITIONS`` fills.

Once per cycle, before any new signal is judged, every open position is
measured in **R** -- the distance from its entry to its initial stop, which
is what the trade risked. ``config.settings.PROFIT_LADDER`` says what happens
at each multiple of it: at +1R a third is sold and the stop moves to the
entry; at +3R another third is sold and the stop moves to +1R; the last third
runs. Independently of the rungs, every cycle the stop is also trailed up to
``price - ATR_STOP_MULTIPLIER x ATR`` where that is tighter -- the initial
stop's own formula, re-anchored to today -- so the stop follows the price and
is the only exit. Rungs and trail both raise the stop; nothing ever lowers it.

What this module cannot do, by construction
-------------------------------------------
It reaches the broker through exactly four primitives -- read a stop,
replace a stop, close *part* of a position, and place a stop on a position
that has none -- and every one of them can only reduce a position. There is
no path here that opens, adds to, or reverses one, so the rule that every
entry is a bracket with a stop is not weakened by the existence of exits.

The fourth was added on 17 Sep, and it reversed an earlier rule. This module
used to leave a position with no live stop exactly as found, on the grounds
that acting on an unprotected position could only make things worse. That
held while stops were assumed to exist; the day it was measured, eleven of
twelve positions had none -- the bracket's DAY stop leg had expired at each
close and nothing put one back -- and "leave it as found" meant "leave it
unprotected, indefinitely". So a position found without a stop is now given
one at the last level the record says it had, and only then managed. The
stop is the only exit; a position without one is not being managed at all.

Where the state lives
---------------------
Nowhere new. R comes from the audit log's own ``ACCEPTED`` record for the
entry (its ``entry_price`` and ``stop_price``); which rungs are already taken
comes from the ``position_managed`` records written here after it. The audit
log is the system of record for what the engine did, and this is the engine
doing something. A crash between "stop replaced" and "tranche sold" heals on
the next cycle: the rung is still due, the stop is already where it should
be, and the replace becomes a no-op.
"""

from __future__ import annotations

import argparse
import json
import logging
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Optional

from app import risk_engine
from app.broker_client import BrokerClient, BrokerError, OpenPosition, StopOrder
from app import logger as audit_log
from app.market_data import MarketDataError, MarketDataProvider
from config import settings as cfg

log = logging.getLogger(__name__)

#: Audit event name for everything this module does.
EVENT = "position_managed"

#: The four things that can happen to a position in one pass.
TRANCHE_TAKEN = "tranche_taken"   #: part of it sold, stop raised
STOP_RAISED = "stop_raised"       #: a rung reached, stop raised, nothing sold (too small to split)
HELD = "held"                     #: checked, no rung reached
UNMANAGED = "unmanaged"           #: (historical) left alone -- no live stop; no longer emitted
PROTECTED = "protected"           #: had no live stop; one was placed at the last recorded level
ERROR = "error"                   #: the broker or market data refused; nothing was done

#: Actions that mean "this rung has been dealt with", for counting on re-run.
_RUNG_COMPLETING = frozenset({TRANCHE_TAKEN, STOP_RAISED})


@dataclass(frozen=True)
class ManagementAction:
    """One thing that happened to one position. Written to the audit log as-is."""

    ticker: str
    action: str
    side: str = ""
    gain_r: float = 0.0
    price: float = 0.0
    qty_closed: int = 0
    remaining_qty: int = 0
    rung: Optional[int] = None
    old_stop: Optional[float] = None
    new_stop: Optional[float] = None
    order_id: str = ""
    r: float = 0.0
    r_estimated: bool = False
    reason: str = ""

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ManagementReport:
    """What one pass over the book did."""

    actions: tuple[ManagementAction, ...] = ()
    positions_seen: int = 0
    market_closed: bool = False

    def _count(self, kind: str) -> int:
        return sum(1 for a in self.actions if a.action == kind)

    @property
    def tranches(self) -> int:
        return self._count(TRANCHE_TAKEN)

    @property
    def raises(self) -> int:
        return self._count(STOP_RAISED) + self._count(TRANCHE_TAKEN)

    @property
    def unmanaged(self) -> int:
        return self._count(UNMANAGED)

    @property
    def protected(self) -> int:
        return self._count(PROTECTED)

    @property
    def errors(self) -> int:
        return self._count(ERROR)

    def as_dict(self) -> dict[str, Any]:
        return {
            "positions_seen": self.positions_seen,
            "market_closed": self.market_closed,
            "tranches": self.tranches,
            "stops_raised": self.raises,
            "unmanaged": self.unmanaged,
            "protected": self.protected,
            "errors": self.errors,
            "actions": [a.as_dict() for a in self.actions],
        }


@dataclass(frozen=True)
class LadderState:
    """Where one position stands on the ladder, reconstructed from the record."""

    entry_price: float
    r: float
    base_qty: int
    rungs_taken: int
    r_estimated: bool


def ladder_history(ticker: str, audit_path: Path) -> tuple[Optional[dict], list[dict]]:
    """The latest ``ACCEPTED`` entry for ``ticker`` and the rung records after it.

    File order is time order. A fresh entry resets the list: an add-on to an
    existing position restarts the ladder on the enlarged position, measured
    from the broker's new average price -- and since the stop only tightens,
    a restart can never give back protection the position already had.
    Unreadable or malformed lines are skipped; the audit log must not be able
    to take the cycle down.
    """
    entry, actions = _history(ticker, audit_path)
    rungs = [
        a for a in actions
        if a.get("action") in _RUNG_COMPLETING and isinstance(a.get("rung"), int)
    ]
    return entry, rungs


def last_recorded_stop(ticker: str, audit_path: Path) -> Optional[float]:
    """The stop the record says this position last had, or ``None`` with no entry.

    The most recent ``new_stop`` any management pass wrote after the latest
    entry -- a rung, a trail, or an earlier protection -- and failing that the
    entry's own stop. This is what a position gets back when the broker has
    lost its stop: not a fresh guess, but the level the system had already
    decided on and recorded, which a lost order does not un-decide.
    """
    entry, actions = _history(ticker, audit_path)
    for action in reversed(actions):
        stop = action.get("new_stop")
        if isinstance(stop, (int, float)) and not isinstance(stop, bool) and stop > 0:
            return float(stop)
    if entry is not None:
        return float(entry["stop_price"])
    return None


def _history(ticker: str, audit_path: Path) -> tuple[Optional[dict], list[dict]]:
    """The latest ``ACCEPTED`` entry for ``ticker`` and every management record after it."""
    entry: Optional[dict] = None
    actions: list[dict] = []
    try:
        text = audit_path.read_text(encoding="utf-8")
    except OSError:
        return None, []
    symbol = ticker.strip().upper()
    for raw in text.splitlines():
        raw = raw.strip()
        if not raw:
            continue
        try:
            record = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue
        # ``event`` is what the production formatter names the message field;
        # a plain JsonFormatter leaves it as ``message``. Read either, so a
        # log written by any handler configuration is still the manager's
        # state and not silently empty.
        event = record.get("event") or record.get("message")
        if event == "signal_processed":
            result = record.get("result") or {}
            if (
                str(result.get("ticker") or "").upper() == symbol
                and result.get("status") == "ACCEPTED"
                and isinstance(result.get("entry_price"), (int, float))
                and isinstance(result.get("stop_price"), (int, float))
            ):
                entry = result
                actions = []
        elif event == EVENT:
            action = record.get("action") or {}
            if str(action.get("ticker") or "").upper() == symbol:
                actions.append(action)
    return entry, actions


def _record(action: ManagementAction) -> None:
    """One audit line per action, written *before* the next rung is considered.

    That ordering is the idempotency mechanism: the count of rung records is
    what stops a re-run taking the same tranche twice.
    """
    try:
        level = logging.ERROR if action.action == ERROR else logging.INFO
        # Resolved at call time through the module, not bound at import: the
        # test suite redirects the audit log by patching this name, and a
        # binding taken at import would write past the redirect into the
        # repository's own log file.
        audit_log.get_audit_logger().log(level, EVENT, extra={"action": action.as_dict()})
    except Exception:  # noqa: BLE001 - a full disk must not take the cycle down
        log.exception("could not write the audit record for %s", action.ticker)


class PositionManager:
    """Reads the book, applies the ladder, records what it did."""

    def __init__(
        self,
        broker: BrokerClient,
        market_data: MarketDataProvider,
        audit_path: Path = cfg.AUDIT_LOG_PATH,
        ladder: tuple[cfg.LadderRung, ...] = cfg.PROFIT_LADDER,
    ) -> None:
        self._broker = broker
        self._market_data = market_data
        self._audit_path = audit_path
        self._ladder = ladder

    def manage(self, protect_only: bool = False) -> ManagementReport:
        """One pass over every open position. Never raises.

        ``protect_only`` does one thing and skips the market-hours gate to do
        it: any position with no live stop gets one, at the last recorded
        level, and nothing else is touched. A protective stop is the one order
        that is *more* useful placed after the close than before -- a GTC stop
        submitted overnight is live at the open, which is exactly when a
        position that lost its stop yesterday is exposed.
        """
        try:
            if not protect_only and not self._broker.is_market_open():
                return ManagementReport(market_closed=True)
            positions = self._broker.get_open_positions()
        except BrokerError as exc:
            action = ManagementAction(ticker="*", action=ERROR, reason=f"{type(exc).__name__}: {exc}")
            _record(action)
            return ManagementReport(actions=(action,))

        actions: list[ManagementAction] = []
        for position in positions:
            try:
                if protect_only:
                    actions += self._protect_if_naked(position)
                else:
                    actions += self._manage_one(position)
            except (BrokerError, MarketDataError, risk_engine.RiskViolation) as exc:
                action = ManagementAction(
                    ticker=position.ticker, action=ERROR, side=position.side,
                    reason=f"{type(exc).__name__}: {exc}",
                )
                _record(action)
                actions.append(action)
            except Exception as exc:  # noqa: BLE001 - one position must not stop the rest
                log.exception("unexpected error managing %s", position.ticker)
                action = ManagementAction(
                    ticker=position.ticker, action=ERROR, side=position.side,
                    reason=f"unexpected {type(exc).__name__}: {exc}",
                )
                _record(action)
                actions.append(action)
        return ManagementReport(actions=tuple(actions), positions_seen=len(positions))

    # ------------------------------------------------------------------ #

    def _state_for(self, position: OpenPosition, qty: int) -> LadderState:
        """Entry, R and rungs already taken, from the record; R from ATR if there is none."""
        entry, rungs = ladder_history(position.ticker, self._audit_path)
        rungs_taken = 1 + max(int(r["rung"]) for r in rungs) if rungs else 0
        closed_so_far = sum(int(r.get("qty_closed") or 0) for r in rungs)
        base_qty = qty + closed_so_far

        entry_price = float(position.avg_entry_price or 0.0)
        if entry_price <= 0 and entry is not None:
            entry_price = float(entry["entry_price"])
        if entry_price <= 0:
            raise risk_engine.RiskViolation("no entry price from the broker or the record")

        if entry is not None:
            r = risk_engine.initial_r(float(entry["entry_price"]), float(entry["stop_price"]))
            estimated = False
        else:
            # The stop was placed at ATR_STOP_MULTIPLIER x ATR, so that is R,
            # from today's ATR rather than the entry day's. Said so in the record.
            r = cfg.ATR_STOP_MULTIPLIER * self._market_data.get_atr(position.ticker)
            if r <= 0:
                raise risk_engine.RiskViolation("could not estimate R: ATR is not positive")
            estimated = True
        return LadderState(entry_price, r, base_qty, rungs_taken, estimated)

    def _protect_if_naked(self, position: OpenPosition) -> list[ManagementAction]:
        qty = int(abs(position.qty))
        if qty < 1 or self._broker.get_open_stop_order(position.ticker) is not None:
            return []
        return [self._protect(position, qty)]

    def _protect(self, position: OpenPosition, qty: int) -> ManagementAction:
        """Place the stop the record says this position should have."""
        ticker, side = position.ticker, position.side
        closing = "sell" if side == "buy" else "buy"
        recorded = last_recorded_stop(ticker, self._audit_path)
        if recorded is not None:
            stop, estimated = recorded, False
            reason = "no live stop order; placed one at the last recorded level"
        else:
            # Nothing on record -- a position opened outside this system, or
            # before the audit log. The initial stop's own formula, from
            # today's price and ATR, and said so.
            price = self._market_data.get_latest_price(ticker)
            atr = self._market_data.get_atr(ticker)
            stop = risk_engine.calculate_stop_price(price, atr, side)
            estimated = True
            reason = "no live stop order and no record; placed one at ATR distance from the last price"
        placed = self._broker.submit_stop_order(ticker, qty, closing, stop)
        action = ManagementAction(
            ticker=ticker, action=PROTECTED, side=side, remaining_qty=qty,
            old_stop=None, new_stop=placed.stop_price, order_id=placed.order_id,
            r_estimated=estimated, reason=reason,
        )
        _record(action)
        return action

    def _manage_one(self, position: OpenPosition) -> list[ManagementAction]:
        ticker, side = position.ticker, position.side
        qty = int(abs(position.qty))
        if qty < 1:
            return []

        stop = self._broker.get_open_stop_order(ticker)
        if stop is None:
            # Protect first; manage next cycle. A position with no stop is
            # not being managed at all, and putting the stop back is the whole
            # of what this pass owes it.
            return [self._protect(position, qty)]

        state = self._state_for(position, qty)
        price = self._market_data.get_latest_price(ticker)
        gain = risk_engine.r_multiple(state.entry_price, price, state.r, side)
        due = risk_engine.rungs_due(gain, state.rungs_taken, self._ladder)

        # The trail. Today's price less the same ATR distance the entry was
        # protected by -- the initial stop's own formula, re-anchored to now
        # -- taken only where it tightens. It runs every cycle, rung or no
        # rung, so the stop follows the price up and the stop is the only
        # exit: a runner at +10R is not left to ride back to +1R. A widening
        # ATR cannot lower it, and an ATR so large the formula goes negative
        # simply leaves the stop where it is rather than failing the position.
        broker_stop = stop.stop_price
        trailed = broker_stop
        try:
            atr = self._market_data.get_atr(ticker)
            if atr > 0:
                trailed = risk_engine.tighter_stop(
                    broker_stop, risk_engine.calculate_stop_price(price, atr, side), side
                )
        except risk_engine.RiskViolation:
            trailed = broker_stop

        if not due:
            if trailed != broker_stop:
                self._broker.replace_stop_order(stop.order_id, qty, trailed)
                action = ManagementAction(
                    ticker=ticker, action=STOP_RAISED, side=side, gain_r=round(gain, 2),
                    price=price, remaining_qty=qty, rung=None,
                    old_stop=broker_stop, new_stop=trailed,
                    r=round(state.r, 4), r_estimated=state.r_estimated,
                    reason="trailing stop",
                )
            else:
                action = ManagementAction(
                    ticker=ticker, action=HELD, side=side, gain_r=round(gain, 2), price=price,
                    remaining_qty=qty, old_stop=broker_stop, new_stop=broker_stop,
                    r=round(state.r, 4), r_estimated=state.r_estimated,
                )
            _record(action)
            return [action]

        actions: list[ManagementAction] = []
        current_stop = trailed
        remaining = qty
        for index in due:
            rung = self._ladder[index]
            tranche = risk_engine.tranche_size(state.base_qty, rung.take_fraction)
            # The ladder never closes the last share: that is the runner's.
            tranche = min(tranche, max(remaining - 1, 0))
            target = risk_engine.stop_for_rung(state.entry_price, state.r, side, rung.stop_to_r)
            new_stop = risk_engine.tighter_stop(current_stop, target, side)
            after = remaining - tranche

            # Protect first, then sell. A stop still sized for the old
            # position would reserve the shares the exit needs, and a moment
            # with no stop at all is the one thing this must not create.
            # Compared against what the broker actually holds, so a trail
            # that tightened above the rung's own target is still applied.
            if tranche > 0 or new_stop != broker_stop:
                self._broker.replace_stop_order(stop.order_id, after, new_stop)

            if tranche > 0:
                order_id = self._broker.close_position_partially(ticker, tranche)
                action = ManagementAction(
                    ticker=ticker, action=TRANCHE_TAKEN, side=side, gain_r=round(gain, 2),
                    price=price, qty_closed=tranche, remaining_qty=after, rung=index,
                    old_stop=broker_stop, new_stop=new_stop, order_id=order_id,
                    r=round(state.r, 4), r_estimated=state.r_estimated,
                )
            else:
                action = ManagementAction(
                    ticker=ticker, action=STOP_RAISED, side=side, gain_r=round(gain, 2),
                    price=price, remaining_qty=after, rung=index,
                    old_stop=broker_stop, new_stop=new_stop,
                    r=round(state.r, 4), r_estimated=state.r_estimated,
                    reason="too small to split; stop ratcheted only",
                )
            _record(action)
            actions.append(action)
            current_stop, broker_stop, remaining = new_stop, new_stop, after
        return actions


def main(argv: Optional[list[str]] = None) -> int:
    """Run one management pass against the paper account, in this process."""
    parser = argparse.ArgumentParser(description="Walk open positions up the profit ladder once.")
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument(
        "--protect-only", action="store_true",
        help="only place a stop on any position that has none; works after hours",
    )
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")

    from app.broker_client import AlpacaPaperBroker
    from app.market_data import YFinanceMarketData

    report = PositionManager(AlpacaPaperBroker(), YFinanceMarketData()).manage(
        protect_only=args.protect_only
    )
    if args.as_json:
        print(json.dumps(report.as_dict(), indent=2))
    else:
        print(render(report))
    return 1 if report.errors else 0


def render(report: ManagementReport) -> str:
    """The pass as a few lines a person can read."""
    if report.market_closed:
        return "Market closed; positions not touched."
    lines = [
        f"{report.positions_seen} open position(s): {report.tranches} tranche(s) sold, "
        f"{report.raises} stop(s) raised, {report.protected} protected, "
        f"{report.unmanaged} unmanaged, {report.errors} error(s)."
    ]
    for a in report.actions:
        if a.action == TRANCHE_TAKEN:
            lines.append(
                f"  {a.ticker}: +{a.gain_r:.2f}R -> sold {a.qty_closed}, {a.remaining_qty} left; "
                f"stop {a.old_stop:.2f} -> {a.new_stop:.2f}"
            )
        elif a.action == STOP_RAISED:
            lines.append(f"  {a.ticker}: +{a.gain_r:.2f}R -> stop {a.old_stop:.2f} -> {a.new_stop:.2f} ({a.reason})")
        elif a.action == HELD:
            lines.append(f"  {a.ticker}: {a.gain_r:+.2f}R, holding {a.remaining_qty}; stop {a.old_stop:.2f}")
        elif a.action == PROTECTED:
            lines.append(f"  {a.ticker}: no stop found -> placed at {a.new_stop:.2f} ({a.reason})")
        else:
            lines.append(f"  {a.ticker}: {a.action} -- {a.reason}")
    return "\n".join(lines)


__all__ = [
    "EVENT", "TRANCHE_TAKEN", "STOP_RAISED", "HELD", "UNMANAGED", "PROTECTED", "ERROR",
    "ManagementAction", "ManagementReport", "LadderState", "PositionManager",
    "ladder_history", "last_recorded_stop", "render", "main",
]


if __name__ == "__main__":
    raise SystemExit(main())
