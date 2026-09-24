"""A book in memory that behaves like the paper account, on daily bars.

``SimBroker`` implements ``app.broker_client.BrokerClient`` -- the eight
methods the real engine and position manager call -- over a cash ledger and
a list of stop orders. It stands in for Alpaca, so it is the one part of a
shadow fund that is NOT production code; everything it does is written down
here, and every choice is one the paper account also makes, or is named as
a simplification:

* **Fills.** A market order (an entry, a ladder tranche, a group-cap trim)
  fills at once, at the price the feed quotes at that moment -- the open of
  the session the cycle acts in (see ``shadow.fund``). No slippage unless
  one is set.
* **Costs.** ``cost_per_side`` of notional on every fill, stops included:
  0.10%, the race's registered cost.
* **Stops.** GTC, one order per entry, never a stop-limit. At the open a
  stop the price gapped through fills at the open; during the session a
  stop the bar's low (high, for a short) reaches fills at the stop price.
  That is ``backtest.simulate._exit_for``'s rule, the race's.
* **Replace.** A new order id every time, as Alpaca does. A price-only
  replace (``current_qty`` equal to ``qty``) keeps the order's own size, so
  a stale ``current_qty`` shows up exactly as it would live.
* **Refusals.** Everything the real client refuses, this refuses with the
  same exception type: bad quantities and prices, a stop that is not a
  reduction, more shares than are free (``insufficient qty available``), a
  second same-side entry in one ticker on one day (``DuplicateOrderError``),
  and a short in a ticker the paper account has refused to short
  (``not_shortable``, read from the live audit log's own refusals).
* **Cash.** Short-sale proceeds are credited; cash may go below zero, as on
  a margin account. The engine's 95% gross cap is what keeps it positive at
  entry, live and here alike. No buying-power rule, no borrow fee.
* **Dividends.** Credited to a long, charged to a short, on the ex-date, for
  the shares held at the previous close.
* **A position closed to zero** cancels the ticker's remaining stops, so a
  stop can never open a position by itself. Alpaca would leave it resting;
  the position manager never closes the last share, so this only matters
  when a stop fills.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Callable, Iterable, Optional

from app.broker_client import (
    BrokerError,
    DuplicateOrderError,
    OpenPosition,
    StopOrder,
    SubmittedOrder,
)

#: The race's registered cost, per side, as a fraction of notional.
DEFAULT_COST_PER_SIDE = 0.001

#: What a fill was, for the trade list.
ENTRY = "entry"
TRANCHE = "close"          # close_position_partially: a ladder rung or a group-cap trim
STOP = "stop"
DIVIDEND = "dividend"


@dataclass
class _Position:
    qty: int                # signed: + long, - short
    avg_entry_price: float
    opened: date
    #: Money in and out of this position so far, costs and dividends included,
    #: for "did this trade make money" once it is closed.
    realised: float = 0.0


@dataclass
class _Stop:
    order_id: str
    ticker: str
    qty: int
    stop_price: float
    side: str               # the stop's own side: "sell" protects a long
    live: bool = True


@dataclass(frozen=True)
class Fill:
    """One thing that moved cash, in the order it happened."""

    day: date
    ticker: str
    kind: str               # ENTRY, TRANCHE, STOP or DIVIDEND
    side: str               # "buy" or "sell"; for a dividend, the position's side
    qty: int
    price: float
    cost: float
    #: For a stop: whether the open gapped through it.
    gapped: bool = False


@dataclass(frozen=True)
class ClosedTrade:
    """A position from its entry to its last share, for win rate and holding time."""

    ticker: str
    side: str
    opened: date
    closed: date
    pnl: float


@dataclass
class SimBroker:
    """See the module docstring."""

    name: str
    cash: float
    #: The feed's price for a ticker at this moment; fills and marks use it.
    quote: Callable[[str], float] = field(repr=False, default=lambda ticker: 0.0)
    cost_per_side: float = DEFAULT_COST_PER_SIDE
    slippage: float = 0.0
    not_shortable: frozenset[str] = frozenset()
    #: Today's session; set by the fund each day. Idempotency is per day.
    day: Optional[date] = None
    market_open: bool = True
    positions: dict[str, _Position] = field(default_factory=dict)
    fills: list[Fill] = field(default_factory=list)
    closed: list[ClosedTrade] = field(default_factory=list)
    _stops: list[_Stop] = field(default_factory=list, repr=False)
    _entries_today: set[tuple[str, str, date]] = field(default_factory=set, repr=False)
    _next_id: int = field(default=0, repr=False)
    #: Last known price per ticker, for marking a position with no bar today.
    _marks: dict[str, float] = field(default_factory=dict, repr=False)

    # ------------------------------------------------------------------ #
    # BrokerClient
    # ------------------------------------------------------------------ #

    def is_market_open(self) -> bool:
        return self.market_open

    def get_equity(self) -> float:
        equity = self.equity()
        if equity <= 0:
            raise BrokerError(f"{self.name}: account equity is not positive ({equity:.2f})")
        return equity

    def get_open_positions(self) -> list[OpenPosition]:
        out = []
        for ticker, pos in self.positions.items():
            price = self._mark(ticker)
            out.append(OpenPosition(ticker, float(pos.qty), abs(pos.qty) * price, pos.avg_entry_price))
        return out

    def submit_bracket_order(self, ticker: str, qty: int, side: str, stop_price: float) -> SubmittedOrder:
        ticker = ticker.strip().upper()
        if not isinstance(qty, int) or qty < 1:
            raise BrokerError(f"bracket qty must be a whole number of at least 1, got {qty!r}")
        if stop_price <= 0:
            raise BrokerError(f"stop_price must be positive, got {stop_price}")
        if side not in ("buy", "sell"):
            raise BrokerError(f"side must be 'buy' or 'sell', got {side!r}")
        key = (ticker, side, self.day)
        if key in self._entries_today:
            raise DuplicateOrderError(f"client_order_id must be unique: {ticker}-{side}-{self.day}")
        held = self.positions.get(ticker)
        if side == "sell" and held is None and ticker in self.not_shortable:
            raise BrokerError(f"asset {ticker} cannot be sold short")
        if held is not None and (held.qty > 0) != (side == "buy"):
            raise BrokerError(f"{ticker}: an entry may not reverse an open position")
        self._entries_today.add(key)

        price = self._fill_price(ticker, side)
        self._trade(ticker, side, qty, price, ENTRY)
        order_id = self._mint("entry")
        self._place_stop(ticker, qty, "sell" if side == "buy" else "buy", stop_price)
        return SubmittedOrder(order_id=order_id, ticker=ticker, qty=qty, side=side, stop_price=stop_price)

    def get_open_stop_order(self, ticker: str) -> Optional[StopOrder]:
        ticker = ticker.strip().upper()
        for stop in reversed(self._stops):          # newest first, as Alpaca lists them
            if stop.live and stop.ticker == ticker:
                return StopOrder(stop.order_id, ticker, stop.qty, stop.stop_price, stop.side)
        return None

    def replace_stop_order(self, order_id: str, qty: int, stop_price: float,
                           current_qty: Optional[int] = None) -> StopOrder:
        if not isinstance(qty, int) or qty < 1:
            raise BrokerError(f"stop qty must be a whole number of at least 1, got {qty!r}")
        if stop_price <= 0:
            raise BrokerError(f"stop_price must be positive, got {stop_price}")
        old = next((s for s in self._stops if s.order_id == order_id and s.live), None)
        if old is None:
            raise BrokerError(f"no open stop order {order_id}")
        price_only = current_qty is not None and int(current_qty) == int(qty)
        new_qty = old.qty if price_only else qty
        free = self._free_qty(old.ticker, excluding=old)
        if new_qty > free:
            raise BrokerError(
                f"insufficient qty available for order (requested: {new_qty}, available: {free})"
            )
        old.live = False
        stop = self._place_stop(old.ticker, new_qty, old.side, stop_price)
        return StopOrder(stop.order_id, stop.ticker, stop.qty, stop.stop_price, stop.side)

    def close_position_partially(self, ticker: str, qty: int) -> str:
        ticker = ticker.strip().upper()
        if not isinstance(qty, int) or qty < 1:
            raise BrokerError(f"close qty must be a whole number of at least 1, got {qty!r}")
        pos = self.positions.get(ticker)
        if pos is None:
            raise BrokerError(f"position does not exist: {ticker}")
        free = self._free_qty(ticker)
        if qty > free:
            raise BrokerError(f"insufficient qty available for order (requested: {qty}, available: {free})")
        side = "sell" if pos.qty > 0 else "buy"
        self._trade(ticker, side, qty, self._fill_price(ticker, side), TRANCHE)
        return self._mint("close")

    def submit_stop_order(self, ticker: str, qty: int, side: str, stop_price: float) -> StopOrder:
        ticker = ticker.strip().upper()
        if not isinstance(qty, int) or qty < 1:
            raise BrokerError(f"stop qty must be a whole number of at least 1, got {qty!r}")
        if stop_price <= 0:
            raise BrokerError(f"stop_price must be positive, got {stop_price}")
        if side not in ("buy", "sell"):
            raise BrokerError(f"side must be 'buy' or 'sell', got {side!r}")
        pos = self.positions.get(ticker)
        if pos is None:
            raise BrokerError(f"refusing a stop for {ticker}: there is no open position to protect")
        closing = "sell" if pos.qty > 0 else "buy"
        if side != closing:
            raise BrokerError(f"refusing a stop for {ticker}: {side} would not reduce a {closing}-to-close position")
        if qty > self._free_qty(ticker):
            raise BrokerError(f"refusing a stop for {ticker}: {qty} exceeds the free {self._free_qty(ticker)}")
        stop = self._place_stop(ticker, qty, side, stop_price)
        return StopOrder(stop.order_id, stop.ticker, stop.qty, stop.stop_price, stop.side)

    # ------------------------------------------------------------------ #
    # What the fund drives: stops against a bar, dividends, marks
    # ------------------------------------------------------------------ #

    def fill_gapped_stops(self, opens: dict[str, float]) -> None:
        """At the open: every stop the price gapped through fills at the open."""
        for stop in list(self._stops):
            if not stop.live or stop.ticker not in opens:
                continue
            open_ = opens[stop.ticker]
            through = open_ <= stop.stop_price if stop.side == "sell" else open_ >= stop.stop_price
            if through:
                self._fill_stop(stop, open_, gapped=True)

    def fill_touched_stops(self, lows: dict[str, float], highs: dict[str, float]) -> None:
        """During the session: every stop the bar's range reached fills at its price."""
        for stop in list(self._stops):
            if not stop.live or stop.ticker not in lows:
                continue
            touched = (lows[stop.ticker] <= stop.stop_price if stop.side == "sell"
                       else highs[stop.ticker] >= stop.stop_price)
            if touched:
                self._fill_stop(stop, stop.stop_price, gapped=False)

    def pay_dividends(self, per_share: dict[str, float], held: dict[str, int]) -> None:
        """Credit longs, charge shorts, for the shares held at the previous close."""
        for ticker, amount in per_share.items():
            qty = held.get(ticker, 0)
            if not qty or not amount:
                continue
            cash = qty * amount                     # negative for a short
            self.cash += cash
            if ticker in self.positions:
                self.positions[ticker].realised += cash
            self.fills.append(Fill(self.day, ticker, DIVIDEND, "buy" if qty > 0 else "sell",
                                   abs(qty), amount, 0.0))

    def held_quantities(self) -> dict[str, int]:
        return {ticker: pos.qty for ticker, pos in self.positions.items()}

    def remember_marks(self, closes: dict[str, float]) -> None:
        self._marks.update(closes)

    def equity(self, marks: Optional[dict[str, float]] = None) -> float:
        total = self.cash
        for ticker, pos in self.positions.items():
            price = (marks or {}).get(ticker)
            total += pos.qty * (price if price is not None else self._mark(ticker))
        return total

    def gross(self, marks: Optional[dict[str, float]] = None) -> float:
        return sum(
            abs(pos.qty) * ((marks or {}).get(ticker) or self._mark(ticker))
            for ticker, pos in self.positions.items()
        )

    def live_stops(self) -> list[StopOrder]:
        return [StopOrder(s.order_id, s.ticker, s.qty, s.stop_price, s.side) for s in self._stops if s.live]

    # ------------------------------------------------------------------ #
    # Seeding a book that already exists (calibration)
    # ------------------------------------------------------------------ #

    def seed_position(self, ticker: str, qty: int, avg_entry_price: float, opened: date,
                      stops: Iterable[tuple[int, float]] = ()) -> None:
        """Hold ``qty`` (signed) at ``avg_entry_price`` with the given live stops.

        No cash moves: the caller sets ``cash`` to the account's own cash.
        """
        ticker = ticker.strip().upper()
        self.positions[ticker] = _Position(int(qty), float(avg_entry_price), opened)
        for stop_qty, stop_price in stops:
            self._place_stop(ticker, int(stop_qty), "sell" if qty > 0 else "buy", float(stop_price))

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _mint(self, kind: str) -> str:
        self._next_id += 1
        return f"{self.name}-{kind}-{self._next_id}"

    def _mark(self, ticker: str) -> float:
        try:
            price = self.quote(ticker)
        except Exception:  # noqa: BLE001 - no bar now: the last known mark
            price = None
        if price and price > 0:
            return price
        return self._marks.get(ticker, self.positions[ticker].avg_entry_price if ticker in self.positions else 0.0)

    def _fill_price(self, ticker: str, side: str) -> float:
        price = self.quote(ticker)
        if not price or price <= 0:
            raise BrokerError(f"no price for {ticker} to fill at")
        return price * (1 + self.slippage) if side == "buy" else price * (1 - self.slippage)

    def _free_qty(self, ticker: str, excluding: Optional[_Stop] = None) -> int:
        pos = self.positions.get(ticker)
        if pos is None:
            return 0
        reserved = sum(s.qty for s in self._stops if s.live and s.ticker == ticker and s is not excluding)
        return abs(pos.qty) - reserved

    def _place_stop(self, ticker: str, qty: int, side: str, stop_price: float) -> _Stop:
        stop = _Stop(self._mint("stop"), ticker, qty, stop_price, side)
        self._stops.append(stop)
        # A stop already through the market triggers at once, at the market.
        price = None
        try:
            price = self.quote(ticker)
        except Exception:  # noqa: BLE001 - no quote: it rests until the next bar
            price = None
        if price and price > 0:
            through = price <= stop_price if side == "sell" else price >= stop_price
            if through:
                self._fill_stop(stop, price, gapped=True)
        return stop

    def _fill_stop(self, stop: _Stop, price: float, gapped: bool) -> None:
        pos = self.positions.get(stop.ticker)
        stop.live = False
        if pos is None:
            return
        qty = min(stop.qty, abs(pos.qty))
        if qty < 1:
            return
        self._trade(stop.ticker, stop.side, qty, price, STOP, gapped=gapped)

    def _trade(self, ticker: str, side: str, qty: int, price: float, kind: str, gapped: bool = False) -> None:
        notional = qty * price
        cost = notional * self.cost_per_side
        signed = qty if side == "buy" else -qty
        self.cash -= signed * price + cost
        self.fills.append(Fill(self.day, ticker, kind, side, qty, price, cost, gapped))
        pos = self.positions.get(ticker)
        if pos is None:
            self.positions[ticker] = _Position(signed, price, self.day, realised=-(signed * price) - cost)
            return
        if (pos.qty > 0) == (signed > 0):
            total = abs(pos.qty) + qty
            pos.avg_entry_price = (pos.avg_entry_price * abs(pos.qty) + price * qty) / total
            pos.qty += signed
            pos.realised += -(signed * price) - cost
            return
        # A reduction: the cost basis stays; the position may go flat.
        pos.qty += signed
        pos.realised += -(signed * price) - cost
        if pos.qty == 0:
            self.closed.append(ClosedTrade(ticker, "buy" if signed < 0 else "sell", pos.opened,
                                           self.day, pos.realised))
            del self.positions[ticker]
            for other in self._stops:
                if other.live and other.ticker == ticker:
                    other.live = False


__all__ = ["ClosedTrade", "DEFAULT_COST_PER_SIDE", "DIVIDEND", "ENTRY", "Fill", "STOP",
           "SimBroker", "TRANCHE"]
