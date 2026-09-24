"""Alpaca paper-trading client. The ONLY module that imports the Alpaca SDK
or reads the API keys.

``paper=True`` is hard-coded on purpose. Going live requires editing this
file, not flipping an environment variable.

Every entry order goes through ``submit_bracket_order``, which always attaches
a ``StopLossRequest``. There is no other submit path.

Credentials may also come from the Alpaca CLI's stored profile, so
``alpaca profile login`` is an alternative to copying keys out of the
dashboard. A profile that targets LIVE trading is refused outright -- see
``credentials_from_cli``.
"""

from __future__ import annotations

import logging
import math
import os
import re
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Optional, Protocol
from zoneinfo import ZoneInfo

import yaml

from config import settings as cfg
from config.settings import get_settings

logger = logging.getLogger(__name__)

# Where the Alpaca CLI keeps its state. Read from the CLI's own Go source
# (alpacahq/cli, internal/config/config.go) rather than guessed: the config
# directory is ``$ALPACA_CONFIG_DIR`` or ``~/.config/alpaca`` on every
# platform -- it builds the path with ``filepath.Join(home, ".config",
# "alpaca")`` unconditionally, so there is no macOS/Windows special case to
# mirror here.
CLI_CONFIG_DIR_ENV = "ALPACA_CONFIG_DIR"
CLI_PROFILE_ENV = "ALPACA_PROFILE"
CLI_CONFIG_FILENAME = "config.yaml"
CLI_PROFILES_DIRNAME = "profiles"
CLI_DEFAULT_PROFILE = "paper"

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

# Alpaca's refusal to change the quantity of an *advanced* order -- which is
# what a stop that is still a leg of the bracket that opened the position is.
# The code is the reliable half; the wording is matched too in case a future
# message drops it. Anything that does not match is an ordinary rejection and
# is reported as one: the fallback below is narrow on purpose.
_ADVANCED_QTY_MARKERS = ("42210000", "qty cannot be changed for advanced")

# Alpaca's refusal when the shares a new order needs are still reserved by
# another one. The cancel-and-replace fallback below hits this if it asks for
# the replacement before the cancelled stop has let go of them.
_INSUFFICIENT_QTY_MARKERS = ("40310000", "insufficient qty available")

# How long to wait for a cancelled order to stop holding its shares. Alpaca
# accepts a cancel straight away and settles it a moment later, so a
# replacement submitted in that moment is refused for shares the position
# plainly has -- TEVA, 22 Sep 2026: 128 held, 127 still "held_for_orders" by
# the stop that had just been cancelled, 1 available. Four seconds is far
# longer than the settle takes and still far shorter than the position can
# afford to wait, and the wait ends the instant the order reports terminal.
CANCEL_SETTLE_ATTEMPTS = 20
CANCEL_SETTLE_SECONDS = 0.2

# The account snapshot (``AlpacaPaperBroker.account_snapshot``). Fills are
# read a page at a time; 100 is Alpaca's own page maximum, and 20 pages is a
# bound on a runaway loop rather than on a real day -- the book holds at most
# MAX_OPEN_POSITIONS names, so two thousand fills between two heartbeats would
# be a bug somewhere else. With no earlier snapshot to start from, ten
# calendar days covers a week of sessions and a long weekend.
SNAPSHOT_FILL_PAGE_SIZE = 100
SNAPSHOT_FILL_MAX_PAGES = 20
SNAPSHOT_FILL_LOOKBACK_DAYS = 10
# Alpaca answers an order query with 50 orders unless asked for more, and the
# book may hold 40 positions, each with a stop that can surface both as its
# own order and as a leg. 500 is the most Alpaca will return in one call.
SNAPSHOT_OPEN_ORDER_LIMIT = 500
# Daily portfolio history is stamped in the exchange's day, so the dates are
# read in the exchange's zone: a stamp late on a New York evening is already
# the next day in UTC, and would file that close under the wrong session.
_MARKET_TZ = ZoneInfo("America/New_York")
# How much of a failure's text a snapshot keeps. One line, bounded: it goes
# into a committed log, and a whole HTML error page from a proxy is not a
# record anyone needs.
_SNAPSHOT_ERROR_CHARS = 300


class BrokerError(RuntimeError):
    """Raised when the broker rejects a request or is unreachable."""


class DuplicateOrderError(BrokerError):
    """The broker refused an order because this one was already submitted.

    A subclass of ``BrokerError`` so nothing that catches broker failures
    stops catching this -- but a distinct type, because it means the opposite
    of a failure. The order exists; the guardrail worked.
    """


class UnprotectedPositionError(BrokerError):
    """The one failure that leaves a position with no stop at all.

    Raised only from the cancel-and-replace fallback in
    ``replace_stop_order``, and only when the old stop was cancelled and the
    replacement could not be placed. Everything else in this module fails
    *before* touching the live stop, so a plain ``BrokerError`` there means
    "nothing happened". This one means the opposite, and it is a distinct
    type so the position manager can say so in the record rather than
    reporting it as one more broker refusal.
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


def _is_advanced_order_qty_rejection(exc: Exception) -> bool:
    """True only for "you may not change the quantity of an advanced order"."""
    message = str(exc).lower()
    return any(marker in message for marker in _ADVANCED_QTY_MARKERS)


def _is_insufficient_qty_rejection(exc: Exception) -> bool:
    """True only for "those shares are already spoken for"."""
    message = str(exc).lower()
    return any(marker in message for marker in _INSUFFICIENT_QTY_MARKERS)


# --- account snapshot helpers ---------------------------------------------- #


def _number(value: Any) -> Optional[float]:
    """A plain float, or ``None`` for anything that is not a finite number.

    Alpaca sends money as strings and leaves a field out rather than zeroing
    it. A missing value stays missing: writing 0.0 for "not reported" would
    tell a calibration the account held no cash.
    """
    if value is None or isinstance(value, bool):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) else None


def _enum_text(value: Any) -> str:
    """An SDK enum's wire value, or the plain string the REST API sent."""
    return str(getattr(value, "value", value) if value is not None else "")


def _field(item: Any, name: str) -> Any:
    """One field of a REST dict or an SDK model, whichever came back."""
    if isinstance(item, dict):
        return item.get(name)
    return getattr(item, name, None)


def _utc_iso(moment: datetime) -> str:
    """``2026-09-25T15:40:12Z`` -- UTC, with the microseconds only if there are any."""
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    moment = moment.astimezone(timezone.utc)
    fraction = f".{moment.microsecond:06d}" if moment.microsecond else ""
    return moment.strftime("%Y-%m-%dT%H:%M:%S") + fraction + "Z"


def _parse_utc(text: Any) -> Optional[datetime]:
    """An ISO timestamp as an aware UTC datetime, or ``None``.

    Alpaca's activity times carry up to nine fractional digits and a ``Z``;
    ``fromisoformat`` takes six, so the rest is dropped -- nanoseconds do not
    change which fill came first to anyone reading a daily record.
    """
    if not isinstance(text, str) or not text.strip():
        return None
    cleaned = re.sub(r"(\.\d{6})\d+", r"\1", text.strip())
    if cleaned.endswith(("Z", "z")):
        cleaned = cleaned[:-1] + "+00:00"
    try:
        moment = datetime.fromisoformat(cleaned)
    except ValueError:
        return None
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(timezone.utc)


def _failure_text(exc: BaseException) -> str:
    """``Type: message`` on one bounded line, for a snapshot's errors list."""
    text = " ".join(f"{type(exc).__name__}: {exc}".split())
    return text[:_SNAPSHOT_ERROR_CHARS]


@dataclass(frozen=True)
class AlpacaCredentials:
    """One credential bundle, never mixed across sources.

    The CLI resolves credentials atomically -- a key from the environment is
    never paired with a secret from a profile -- because the winning source
    fully determines which auth headers get sent. Mirroring that here means a
    half-configured environment fails with a clear message instead of sending
    a mismatched pair to Alpaca and getting a generic 403 back.
    """

    api_key: str = ""
    secret_key: str = ""
    access_token: str = ""
    source: str = ""

    @property
    def is_oauth(self) -> bool:
        return bool(self.access_token)


@dataclass(frozen=True)
class OpenPosition:
    ticker: str
    qty: float          # positive for long, negative for short
    market_value: float  # absolute dollar exposure
    #: What the shares actually cost, from the broker. The baseline every
    #: profit-ladder rung is measured from; zero means the broker did not say.
    avg_entry_price: float = 0.0

    @property
    def side(self) -> str:
        return "buy" if self.qty > 0 else "sell"


@dataclass(frozen=True)
class StopOrder:
    """The live stop-loss protecting a position -- the OTO child, once the entry fills."""

    order_id: str
    ticker: str
    qty: int
    stop_price: float
    side: str  # the stop's own side: "sell" protects a long, "buy" a short


@dataclass(frozen=True)
class SubmittedOrder:
    order_id: str
    ticker: str
    qty: int
    side: str
    stop_price: float


class BrokerClient(Protocol):
    """What the execution engine and the position manager need from a broker."""

    def is_market_open(self) -> bool: ...

    def get_equity(self) -> float: ...

    def get_open_positions(self) -> list[OpenPosition]: ...

    def submit_bracket_order(
        self, ticker: str, qty: int, side: str, stop_price: float
    ) -> SubmittedOrder: ...

    # --- position management: the only four things the ladder may do ---

    def get_open_stop_order(self, ticker: str) -> Optional[StopOrder]: ...

    def replace_stop_order(self, order_id: str, qty: int, stop_price: float,
                           current_qty: Optional[int] = None) -> StopOrder: ...

    def close_position_partially(self, ticker: str, qty: int) -> str: ...

    def submit_stop_order(self, ticker: str, qty: int, side: str, stop_price: float) -> StopOrder: ...


def cli_config_dir() -> Path:
    """The Alpaca CLI's config directory, honouring its own override."""
    override = os.environ.get(CLI_CONFIG_DIR_ENV, "").strip()
    if override:
        return Path(override)
    return Path.home() / ".config" / "alpaca"


def _text(value: Any) -> str:
    """A trimmed string, or empty for anything that is not one."""
    return value.strip() if isinstance(value, str) else ""


def _read_yaml_mapping(path: Path) -> dict:
    """Parse a CLI YAML file, treating every failure as "not configured".

    A missing file is the ordinary case -- most people will never run the
    CLI. A malformed or unreadable one is logged and then treated the same
    way, because a broken profile should fall through to the explicit
    environment variables rather than take the whole heartbeat down.
    """
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = yaml.safe_load(handle)
    except FileNotFoundError:
        return {}
    except (OSError, yaml.YAMLError) as exc:
        logger.warning("could not read Alpaca CLI file %s: %s", path, exc)
        return {}
    return loaded if isinstance(loaded, dict) else {}


def cli_profile_name() -> str:
    """Which profile the CLI would use: env, then config.yaml, then "paper"."""
    explicit = _text(os.environ.get(CLI_PROFILE_ENV))
    if explicit:
        return explicit
    config = _read_yaml_mapping(cli_config_dir() / CLI_CONFIG_FILENAME)
    return _text(config.get("default_profile")) or CLI_DEFAULT_PROFILE


def credentials_from_cli() -> Optional[AlpacaCredentials]:
    """Read the CLI's stored login, or ``None`` if there isn't one.

    Raises ``BrokerError`` -- rather than returning ``None`` -- when the
    profile targets live trading. Silently ignoring it would report "no
    credentials found" for a machine that plainly has some, and the person
    debugging that would reasonably try to make the profile *more* reachable.
    Saying exactly why it was refused is the safer failure.
    """
    name = cli_profile_name()
    path = cli_config_dir() / CLI_PROFILES_DIRNAME / f"{name}.yaml"
    profile = _read_yaml_mapping(path)
    if not profile:
        return None

    # The CLI writes live_trade only for live profiles; paper ones omit it.
    # Anything truthy here is refused: this system is paper-only, and
    # borrowing a live bundle would point real money at a strategy whose
    # whole safety argument is that it cannot reach a live endpoint.
    if profile.get("live_trade") is True:
        raise BrokerError(
            f"Alpaca CLI profile {name!r} ({path}) targets LIVE trading. "
            f"This system is paper-only and will not borrow live credentials. "
            f"Use a paper profile (`alpaca profile login`), point "
            f"{CLI_PROFILE_ENV} at one, or set ALPACA_API_KEY / "
            f"ALPACA_SECRET_KEY explicitly."
        )

    # Same precedence the CLI itself uses: an OAuth access token outranks a
    # stored key pair. Only the path is logged, never the credential.
    access_token = _text(profile.get("access_token"))
    if access_token:
        logger.info("using Alpaca OAuth login from CLI profile %s", path)
        return AlpacaCredentials(access_token=access_token, source=f"cli-oauth:{name}")

    api_key = _text(profile.get("api_key"))
    secret_key = _text(profile.get("secret_key"))
    if api_key and secret_key:
        logger.info("using Alpaca API keys from CLI profile %s", path)
        return AlpacaCredentials(
            api_key=api_key, secret_key=secret_key, source=f"cli-apikey:{name}"
        )

    return None


def resolve_credentials() -> AlpacaCredentials:
    """Settings first, then the CLI's stored login. Never a mix of the two."""
    settings = get_settings()
    api_key = (settings.alpaca_api_key or "").strip()
    secret_key = (settings.alpaca_secret_key or "").strip()

    if api_key and secret_key:
        return AlpacaCredentials(api_key=api_key, secret_key=secret_key, source="settings")
    if api_key or secret_key:
        missing = "ALPACA_SECRET_KEY" if api_key else "ALPACA_API_KEY"
        raise BrokerError(
            f"{missing} is not set. ALPACA_API_KEY and ALPACA_SECRET_KEY are "
            f"used as a pair; setting only one would send a mismatched "
            f"credential to Alpaca (see .env.example)."
        )

    from_cli = credentials_from_cli()
    if from_cli is not None:
        return from_cli

    raise BrokerError(
        "No Alpaca credentials found: set ALPACA_API_KEY / ALPACA_SECRET_KEY, "
        "or run `alpaca profile login` (see .env.example)"
    )


class AlpacaPaperBroker:
    """Live implementation against the Alpaca paper endpoint."""

    def __init__(self) -> None:
        from alpaca.trading.client import TradingClient  # only place the SDK is imported

        credentials = resolve_credentials()
        # paper=True is deliberately hard-coded; see module docstring. It also
        # pins the SDK's base URL to the paper endpoint, so even a live key
        # that reached this point could not trade a funded account.
        self._client = TradingClient(
            api_key=credentials.api_key or None,
            secret_key=credentials.secret_key or None,
            oauth_token=credentials.access_token or None,
            paper=True,
        )

    def is_market_open(self) -> bool:
        """Whether the US equity market is open right now.

        Alpaca's own clock is the authority rather than a local weekday and
        time-of-day calculation. A hand-rolled check would have to carry the
        exchange holiday calendar, the half-day schedule, and the fact that
        US market hours move against UTC twice a year on a DST schedule that
        is not the same as Europe's. Getting any of those wrong means either
        trading into a closed market or skipping a real session.
        """
        try:
            clock = self._client.get_clock()
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"get_clock failed: {exc}") from exc
        return bool(clock.is_open)

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
                avg_entry_price=float(getattr(p, "avg_entry_price", 0) or 0),
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
            # Good-till-cancelled, and the reason is a day's evidence: with
            # DAY, Alpaca cancels the unfilled stop leg at the close, so every
            # position opened before today woke up with no stop at all. The
            # market parent fills at once either way; the TIF only ever
            # governs the stop, and a stop that expires nightly protects
            # nothing overnight -- which is the only time it cannot be
            # watched.
            time_in_force=TimeInForce.GTC,
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

    # ------------------------------------------------------------------ #
    # Position management
    # ------------------------------------------------------------------ #
    # Three primitives, and deliberately no fourth. Between them a winning
    # position can be scaled out and its stop walked up; none of them can
    # open a position, add to one, or reverse one. The rule that every entry
    # carries a stop is untouched because nothing here is an entry.

    #: Order states in which a stop is no longer protecting anything.
    _TERMINAL_ORDER_STATES = frozenset(
        {"filled", "canceled", "cancelled", "expired", "rejected", "replaced", "done_for_day"}
    )

    def get_open_stop_order(self, ticker: str) -> Optional[StopOrder]:
        """The live stop protecting ``ticker``, or ``None`` if there is not one.

        The OTO child is born ``held`` and becomes its own open order once the
        entry fills, so it can surface either as a top-level open order or as
        a leg of a still-open parent. Both are scanned; the first live stop
        for the symbol wins. ``None`` is a real answer -- the position manager
        treats it as "leave this one alone and say so", never as permission to
        act unprotected.
        """
        from alpaca.trading.enums import QueryOrderStatus
        from alpaca.trading.requests import GetOrdersRequest

        symbol = ticker.strip().upper()
        try:
            orders = self._client.get_orders(
                GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[symbol], nested=True)
            )
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"get_orders failed for {symbol}: {exc}") from exc
        return next(self._live_stops(orders, symbol), None)

    def _live_stops(self, orders: Optional[Iterable[Any]],
                    symbol: Optional[str] = None) -> Iterator[StopOrder]:
        """Every live STOP in an open-orders answer, legs included, each once.

        The one definition of "a live stop" in this module: the position
        manager's lookup takes the first for its symbol, and the account
        snapshot records them all (``symbol`` None), so what the record calls
        a stop is exactly what the ladder would have acted on.
        """
        from alpaca.trading.enums import OrderType

        seen: set[str] = set()
        for parent in orders or []:
            for candidate in (parent, *(getattr(parent, "legs", None) or [])):
                order_id = str(getattr(candidate, "id", ""))
                if not order_id or order_id in seen:
                    continue
                seen.add(order_id)
                candidate_symbol = str(getattr(candidate, "symbol", "")).upper()
                if symbol is not None and candidate_symbol != symbol:
                    continue
                kind = getattr(candidate, "order_type", None) or getattr(candidate, "type", None)
                if str(getattr(kind, "value", kind)) != OrderType.STOP.value:
                    continue
                state = str(getattr(getattr(candidate, "status", ""), "value", getattr(candidate, "status", "")))
                if state in self._TERMINAL_ORDER_STATES:
                    continue
                stop_price = getattr(candidate, "stop_price", None)
                if stop_price is None:
                    continue
                side = getattr(candidate, "side", "")
                yield StopOrder(
                    order_id=order_id,
                    ticker=symbol if symbol is not None else candidate_symbol,
                    qty=int(float(candidate.qty)),
                    stop_price=float(stop_price),
                    side=str(getattr(side, "value", side)),
                )

    def replace_stop_order(self, order_id: str, qty: int, stop_price: float,
                           current_qty: Optional[int] = None) -> StopOrder:
        """Move a live stop and shrink it to the shares it still protects.

        One call, so there is no moment between "old stop cancelled" and "new
        stop placed" in which the position is naked -- Alpaca applies a
        replace atomically or refuses it. The position manager calls this
        *before* selling a tranche, for the same reason: a stop that still
        covers the old size would reserve shares the exit needs.

        ``current_qty`` is what the live stop covers right now. When it equals
        ``qty`` the field is left out of the request entirely, and that is not
        a micro-optimisation -- it is the whole point.

        A stop that is still the leg of the bracket that opened the position
        is an *advanced* order to Alpaca, and Alpaca refuses to change the
        quantity of one: ``42210000 qty cannot be changed for advanced
        orders``. It refuses on the presence of the field, not on the value,
        so sending an unchanged qty is rejected exactly as hard as a real
        resize. Every trail on such a stop therefore failed, the stop never
        ratcheted, and the manager recorded an error that read like a missing
        stop. TEVA on 21 Sep 2026 (issue #93) was one share -- too small for
        any tranche, so the trail was the only thing that ever ran on it.

        Leaving the field out fixes the trail. It cannot fix a *genuine*
        resize, and that was first left to fail loudly. It was the wrong
        call. TEVA's live stop still covered the 127 shares of its original
        bracket against the 1 share left; a 127-share sell-stop on a 1-share
        position cannot execute, so the position was effectively unprotected
        and no amount of failing loudly was going to change its size. A stop
        that is permanently the wrong size is worse than a stop that is
        briefly absent.

        So a genuine resize the broker refuses falls back, and only then, to
        cancelling that one order by its id and placing a standalone stop in
        its place. The window is real -- roughly a second, once per stuck
        stop, after which the stop is an ordinary order that replaces
        normally forever after. It is bounded four ways: nothing else in this
        module or the codebase can cancel an order; the fallback runs only on
        that one rejection code; the book is read and the replacement is
        validated *before* the cancel, so every foreseeable refusal happens
        while the old stop is still live; and if the placement fails anyway
        the failure is an ``UnprotectedPositionError``, which the health
        check treats as critical rather than as one more broker refusal.
        """
        from alpaca.trading.requests import ReplaceOrderRequest

        if qty < 1 or int(qty) != qty:
            raise BrokerError(f"qty must be a positive whole number, got {qty}")
        if stop_price <= 0:
            raise BrokerError(f"stop_price must be positive, got {stop_price}")
        resizing = current_qty is None or int(current_qty) != int(qty)
        request = (
            ReplaceOrderRequest(qty=int(qty), stop_price=stop_price) if resizing
            else ReplaceOrderRequest(stop_price=stop_price)
        )
        try:
            order = self._client.replace_order_by_id(order_id, request)
        except Exception as exc:  # noqa: BLE001
            # NOT gated on `resizing`, though it was until 23 Sep 2026. The
            # same 42210000 family refuses a price-only replace with "order
            # chain not fully replaced", and TLT hit exactly that: the
            # rejection was recognised, the fallback was skipped because
            # nothing was being resized, the error propagated, and the
            # position finished the day with no stop. An advanced order that
            # will not take a replacement needs cancelling and replacing
            # whether or not the quantity is what it objected to.
            if _is_advanced_order_qty_rejection(exc):
                return self._resize_by_replacing_the_order(order_id, qty, stop_price, exc)
            raise BrokerError(f"replace_order failed for {order_id}: {exc}") from exc

        # The replacement is live, but the order it superseded is not
        # necessarily gone, and until it is it goes on reserving the shares it
        # covered. Every caller of this method follows it immediately with
        # close_position_partially for the shares the resize was meant to
        # free -- "protect first, then sell" -- so without this wait that
        # ordering is nominal rather than real. TIP and UUP on 23 Sep 2026:
        # the stop was resized down, the trim was refused for shares the
        # position plainly held (available 0, held_for_orders the whole
        # position), and both ended the day unprotected.
        self._wait_until_terminal(str(order.symbol).upper(), order_id)
        side = getattr(order, "side", "")
        returned_qty = getattr(order, "qty", None)
        return StopOrder(
            order_id=str(order.id),
            ticker=str(order.symbol).upper(),
            qty=int(float(returned_qty)) if returned_qty is not None else int(qty),
            stop_price=float(order.stop_price if order.stop_price is not None else stop_price),
            side=str(getattr(side, "value", side)),
        )

    def _resize_by_replacing_the_order(self, order_id: str, qty: int, stop_price: float,
                                       refusal: Exception) -> StopOrder:
        """Cancel one stuck stop by its id and place a correctly sized one.

        The only path in this system that cancels anything, reached only from
        the one Alpaca rejection that makes a resize impossible. Everything
        that can be checked is checked first, while the old stop is still
        live: which symbol and side the order belongs to, that the position
        is still open, and that the new size is a reduction of it. Only then
        is the old order cancelled, and the replacement goes in through
        ``submit_stop_order``, which is close-only by construction and
        good-till-cancelled.

        Between the two sits a wait, and it is not optional. Alpaca accepts a
        cancel before the order is gone, and until it is gone it still
        reserves the shares it covered -- so the replacement is refused for
        shares the position plainly holds. That is what happened to TEVA on
        22 Sep 2026 on this path's first live run: 128 shares held, 127 of
        them still ``held_for_orders`` by the stop just cancelled, 1
        available, and the position left with nothing. So the cancelled order
        is polled until it reports terminal before the replacement is asked
        for, and a refusal that still blames the share count buys one more
        full window and one more attempt.
        """
        try:
            stuck = self._client.get_order_by_id(order_id)
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(
                f"replace_order failed for {order_id} ({refusal}), and the order "
                f"itself could not be read to resize it another way: {exc}"
            ) from exc

        symbol = str(getattr(stuck, "symbol", "")).upper()
        raw_side = getattr(stuck, "side", "")
        side = str(getattr(raw_side, "value", raw_side)).lower()
        if not symbol or side not in ("buy", "sell"):
            raise BrokerError(
                f"replace_order failed for {order_id} ({refusal}), and the order "
                f"does not name a symbol and side to resize it another way"
            )

        # Everything submit_stop_order would refuse, refused here -- while the
        # old stop is still live and the position is still protected.
        held = next((p for p in self.get_open_positions() if p.ticker == symbol), None)
        if held is None:
            raise BrokerError(
                f"replace_order failed for {symbol} ({refusal}); not cancelling it "
                f"either, because there is no open position it would protect"
            )
        closing = "sell" if held.qty > 0 else "buy"
        if side != closing or qty > abs(held.qty):
            raise BrokerError(
                f"replace_order failed for {symbol} ({refusal}); not cancelling it "
                f"either, because a {side} stop for {int(qty)} would not be a "
                f"reduction of the {int(held.qty)} held"
            )

        try:
            self._client.cancel_order_by_id(order_id)
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(
                f"replace_order failed for {symbol} ({refusal}) and the stop could "
                f"not be cancelled to replace it: {exc}"
            ) from exc

        logger.warning(
            "%s stop %s could not be resized to %d shares (%s); cancelled it and "
            "placing a standalone stop in its place",
            symbol, order_id, int(qty), refusal,
        )
        # The cancel is accepted before it takes effect, and until it does the
        # shares are still reserved by the order being cancelled. Wait for it.
        self._wait_until_terminal(symbol, order_id)
        try:
            return self.submit_stop_order(symbol, int(qty), side, stop_price)
        except Exception as exc:  # noqa: BLE001
            if _is_insufficient_qty_rejection(exc):
                # The shares were still spoken for. That is the cancel not yet
                # settled almost every time, so give it one more full window
                # and ask again rather than leaving the position bare over a
                # race with the broker's own bookkeeping.
                logger.warning(
                    "%s replacement stop refused for want of shares (%s); waiting "
                    "for the cancelled order to release them and trying once more",
                    symbol, exc,
                )
                self._wait_until_terminal(symbol, order_id)
                try:
                    return self.submit_stop_order(symbol, int(qty), side, stop_price)
                except Exception as retry_exc:  # noqa: BLE001
                    raise UnprotectedPositionError(
                        self._naked_message(symbol, order_id, qty, side, stop_price, retry_exc)
                    ) from retry_exc
            raise UnprotectedPositionError(
                self._naked_message(symbol, order_id, qty, side, stop_price, exc)
            ) from exc

    def _wait_until_terminal(self, symbol: str, order_id: str) -> bool:
        """Block until a superseded order is terminal, or the patience runs out.

        Alpaca's cancel returns before the order is actually gone, and a stop
        that is still winding down goes on reserving the shares it covered.
        TEVA on 22 Sep 2026 was refused its replacement on exactly that: 128
        shares held, 127 of them still ``held_for_orders`` by the stop that
        had just been cancelled, 1 available.

        Returns whether it settled. A timeout is not raised on: the caller's
        next move is to try the replacement anyway, and a stop that is placed
        beats a wait that gave up. An order that cannot be read at all counts
        as settled -- a stop nobody can find is not holding anything.
        """
        for _ in range(CANCEL_SETTLE_ATTEMPTS):
            try:
                order = self._client.get_order_by_id(order_id)
            except Exception:  # noqa: BLE001
                return True
            raw = getattr(order, "status", "")
            state = str(getattr(raw, "value", raw)).lower()
            if state in self._TERMINAL_ORDER_STATES:
                return True
            time.sleep(CANCEL_SETTLE_SECONDS)
        logger.warning(
            "%s cancelled stop %s is still not terminal after %.1fs; placing the "
            "replacement anyway", symbol, order_id,
            CANCEL_SETTLE_ATTEMPTS * CANCEL_SETTLE_SECONDS,
        )
        return False

    @staticmethod
    def _naked_message(symbol: str, order_id: str, qty: int, side: str,
                       stop_price: float, exc: Exception) -> str:
        """What a person needs to fix this by hand, in the order they need it."""
        return (
            f"{symbol} has NO live stop: the {int(qty)}-share replacement for "
            f"cancelled order {order_id} was refused ({exc}). Place a "
            f"good-till-cancelled {side} stop for {int(qty)} share(s) at "
            f"{stop_price} now."
        )

    def close_position_partially(self, ticker: str, qty: int) -> str:
        """Sell (or cover) ``qty`` shares of an open position. Returns the order id.

        This is the one exit path, and it is close-only by the broker's own
        definition: it maps to ``DELETE /v2/positions/{symbol}?qty=N``, which
        reduces the named position and cannot open, add to, or reverse one.
        That property is what lets a partial exit exist at all without
        weakening the rule that every *entry* is a bracket with a stop -- a
        ``MarketOrderRequest`` without ``stop_loss`` is still never built.
        """
        from alpaca.trading.requests import ClosePositionRequest

        if qty < 1 or int(qty) != qty:
            raise BrokerError(f"qty must be a positive whole number, got {qty}")
        symbol = ticker.strip().upper()
        request = ClosePositionRequest(qty=str(int(qty)))
        try:
            order = self._client.close_position(symbol, request)
        except Exception as exc:  # noqa: BLE001
            # "Those shares are already spoken for" is the one refusal here
            # worth a second ask. The caller has just resized the stop to free
            # exactly these shares, and the order it superseded may still have
            # been holding them; replace_stop_order now waits for that, and
            # this is the belt to its braces, because the reservation can also
            # be let go a moment after the order reports terminal. A refusal
            # placed nothing, so asking again cannot double the exit.
            if not _is_insufficient_qty_rejection(exc):
                raise BrokerError(f"close_position failed for {symbol}: {exc}") from exc
            logger.warning(
                "%s: %d share(s) still reserved by another order; waiting %.1fs "
                "and asking once more", symbol, int(qty),
                CANCEL_SETTLE_ATTEMPTS * CANCEL_SETTLE_SECONDS,
            )
            time.sleep(CANCEL_SETTLE_ATTEMPTS * CANCEL_SETTLE_SECONDS)
            try:
                order = self._client.close_position(symbol, request)
            except Exception as again:  # noqa: BLE001
                raise BrokerError(
                    f"close_position failed for {symbol} ({exc}), and again after "
                    f"waiting for the shares to be released: {again}"
                ) from again
        return str(getattr(order, "id", "") or "")

    def submit_stop_order(self, ticker: str, qty: int, side: str, stop_price: float) -> StopOrder:
        """Give a position that has no stop one back. Close-only by construction.

        A stop order on its own is *not* close-only the way ``close_position``
        is: a STOP sell for a symbol nobody holds would open a short. So the
        book is read first and the order is refused unless it can only reduce
        an existing position -- the position exists, ``side`` is the side that
        closes it, and ``qty`` is no more than it holds. That check is what lets
        a fourth primitive exist without weakening the rule that nothing here
        opens, adds to, or reverses a position.

        Good-till-cancelled, because a DAY stop is exactly how eleven of twelve
        positions came to have none: the bracket's leg expired at the close and
        nothing put one back. Idempotent within the heartbeat window through
        the same client-order-id mechanism as an entry, so a retry after a lost
        response finds the stop it already placed rather than placing a second.
        """
        from alpaca.trading.enums import OrderSide, TimeInForce
        from alpaca.trading.requests import StopOrderRequest

        symbol = ticker.strip().upper()
        if qty < 1 or int(qty) != qty:
            raise BrokerError(f"qty must be a positive whole number, got {qty}")
        if stop_price <= 0:
            raise BrokerError(f"stop_price must be positive, got {stop_price}")
        if side not in ("buy", "sell"):
            raise BrokerError(f"side must be 'buy' or 'sell', got {side!r}")

        held = next((p for p in self.get_open_positions() if p.ticker == symbol), None)
        if held is None:
            raise BrokerError(f"refusing a stop for {symbol}: there is no open position to protect")
        closing = "sell" if held.qty > 0 else "buy"
        if side != closing:
            raise BrokerError(
                f"refusing a stop for {symbol}: side {side!r} would not close a "
                f"{'long' if held.qty > 0 else 'short'} position"
            )
        if qty > abs(held.qty):
            raise BrokerError(
                f"refusing a stop for {symbol}: {int(qty)} exceeds the {int(abs(held.qty))} held"
            )

        client_order_id = build_client_order_id(symbol, f"protect-{side}")
        request = StopOrderRequest(
            symbol=symbol,
            qty=int(qty),
            side=OrderSide.SELL if side == "sell" else OrderSide.BUY,
            time_in_force=TimeInForce.GTC,
            stop_price=stop_price,
            client_order_id=client_order_id,
        )
        try:
            order = self._client.submit_order(request)
        except Exception as exc:  # noqa: BLE001
            if _is_duplicate_rejection(exc):
                existing = self.get_open_stop_order(symbol)
                if existing is not None:
                    return existing
                raise DuplicateOrderError(
                    f"{symbol} protective stop was already submitted this window "
                    f"(client_order_id {client_order_id}) but cannot be found: {exc}"
                ) from exc
            raise BrokerError(f"submit_order (stop) failed for {symbol}: {exc}") from exc
        placed = getattr(order, "stop_price", None)
        return StopOrder(
            order_id=str(order.id),
            ticker=symbol,
            qty=int(qty),
            stop_price=float(placed if placed is not None else stop_price),
            side=side,
        )

    # ------------------------------------------------------------------ #
    # The account, read for the record
    # ------------------------------------------------------------------ #
    # Nothing below places, replaces or cancels anything. It exists so the
    # shadow funds can be calibrated against the real account -- same engine,
    # same position manager, simulated broker -- without any measurement
    # workflow ever holding these keys: the heartbeat, which holds them
    # anyway, reads the account once a run and commits the answer as a line
    # of logs/account.jsonl (app/account_snapshot.py). Until this, the record
    # had no cash, no closing equity, no fill prices and no stop exits: the
    # audit log says what was asked for, never what the broker did.

    def account_snapshot(self, since: Optional[datetime]) -> dict:
        """The account as the broker sees it now, in five independent reads.

        ``account`` (equity, cash, long and short market value, last close's
        equity), ``positions`` (signed quantity, short negative), ``stops``
        (every live STOP order, by the same rule the position manager uses),
        ``fills`` (every fill and partial fill after ``since``, or over the
        last ten calendar days when there is no ``since``, oldest first) and
        ``history`` (a month of the account's equity at each day's close,
        dated in New York; read during a session, the last point is today's
        and still moving).

        Each read stands alone. One that fails leaves its part ``None`` and
        adds ``{"part", "error"}`` to ``errors``, and the other four are still
        recorded: a broker that answers four questions out of five has told
        the record four true things. ``None`` rather than ``[]`` on purpose --
        an empty list is a real answer ("no open positions"), and a
        calibration that read a failed read as a flat book would be comparing
        the simulation with an account that never existed.

        ``fills_after`` says which window ``fills`` covers, so a reader can
        tell a quiet day from a narrow window. Consecutive windows overlap by
        the few seconds a snapshot takes (``app.account_snapshot`` stamps the
        time before it reads), so the same fill can appear in two snapshots;
        its ``id`` is the key to deduplicate on.
        """
        after = since if since is not None else (
            datetime.now(timezone.utc) - timedelta(days=SNAPSHOT_FILL_LOOKBACK_DAYS)
        )
        snapshot: dict[str, Any] = {
            "account": None, "positions": None, "stops": None, "fills": None,
            "history": None, "fills_after": _utc_iso(after), "errors": [],
        }
        errors: list[dict] = snapshot["errors"]
        readers = (
            ("account", self._read_account),
            ("positions", self._read_positions),
            ("stops", self._read_stops),
            ("fills", lambda: self._read_fills(after, errors)),
            ("history", self._read_history),
        )
        for part, read in readers:
            try:
                snapshot[part] = read()
            except Exception as exc:  # noqa: BLE001 -- one part, never the whole record
                errors.append({"part": part, "error": _failure_text(exc)})
        return snapshot

    def _read_account(self) -> dict:
        account = self._client.get_account()
        # short_market_value is reported as Alpaca sends it: negative for a
        # short book. Only the position rows are made absolute, as
        # OpenPosition already is.
        return {
            name: _number(getattr(account, name, None))
            for name in ("equity", "cash", "long_market_value", "short_market_value", "last_equity")
        }

    def _read_positions(self) -> list[dict]:
        rows = []
        for p in self._client.get_all_positions() or []:
            qty = _number(getattr(p, "qty", None))
            # Signed by the side, not by trusting the quantity's own sign:
            # the SDK's model carries a side, and a short must come out
            # negative whether the number arrived as "-10" or as "10".
            if qty is not None and _enum_text(getattr(p, "side", "")).lower() == "short":
                qty = -abs(qty)
            value = _number(getattr(p, "market_value", None))
            rows.append({
                "ticker": str(getattr(p, "symbol", "")).upper(),
                "qty": qty,
                "avg_entry_price": _number(getattr(p, "avg_entry_price", None)),
                "market_value": abs(value) if value is not None else None,
                "current_price": _number(getattr(p, "current_price", None)),
            })
        return rows

    def _read_stops(self) -> list[dict]:
        from alpaca.trading.enums import QueryOrderStatus
        from alpaca.trading.requests import GetOrdersRequest

        orders = self._client.get_orders(
            GetOrdersRequest(status=QueryOrderStatus.OPEN, nested=True,
                             limit=SNAPSHOT_OPEN_ORDER_LIMIT)
        )
        return [asdict(stop) for stop in self._live_stops(orders)]

    def _read_fills(self, after: datetime, errors: list[dict]) -> list[dict]:
        """Every FILL and PARTIAL_FILL activity after ``after``, oldest first.

        Paged by the last activity's id while a page comes back full. A page
        that fails fails the whole part, so the snapshot says ``None`` and
        the next one reads this window again. Hitting the page cap is
        different: what was read is kept and the truncation is written into
        ``errors``, because the next window starts after this snapshot and
        what lay beyond the cap would otherwise vanish without a word.
        """
        params: dict[str, Any] = {
            "after": _utc_iso(after), "direction": "asc", "page_size": SNAPSHOT_FILL_PAGE_SIZE,
        }
        fills: list[dict] = []
        seen: set[str] = set()
        complete = False
        for _ in range(SNAPSHOT_FILL_MAX_PAGES):
            page = self._client.get("/account/activities/FILL", params)
            if not isinstance(page, list):
                raise BrokerError(f"fill activities came back as {type(page).__name__}, not a list")
            for activity in page:
                fill_id = str(_field(activity, "id") or "")
                if fill_id and fill_id in seen:
                    continue
                seen.add(fill_id)
                fills.append({
                    "id": fill_id,
                    "order_id": str(_field(activity, "order_id") or ""),
                    "ticker": str(_field(activity, "symbol") or "").upper(),
                    "side": _enum_text(_field(activity, "side")).lower(),
                    "qty": _number(_field(activity, "qty")),
                    "price": _number(_field(activity, "price")),
                    "at": _field(activity, "transaction_time"),
                })
            last_id = _field(page[-1], "id") if page else None
            if len(page) < SNAPSHOT_FILL_PAGE_SIZE or not last_id:
                complete = len(page) < SNAPSHOT_FILL_PAGE_SIZE
                break
            params = {**params, "page_token": str(last_id)}
        if not complete:
            errors.append({
                "part": "fills",
                "error": f"stopped after {len(fills)} fills; any later in the window were not read",
            })

        # Asked for in ascending order already; sorted again on the parsed
        # time because the record promises oldest first and a lexical sort
        # of mixed-precision stamps does not keep that promise. A time that
        # does not parse keeps its place at the end, verbatim.
        def moment(fill: dict) -> tuple[bool, datetime]:
            parsed = _parse_utc(fill["at"])
            return (parsed is None, parsed or datetime.min.replace(tzinfo=timezone.utc))

        fills.sort(key=moment)
        for fill in fills:
            parsed = _parse_utc(fill["at"])
            fill["at"] = _utc_iso(parsed) if parsed is not None else fill["at"]
        return fills

    def _read_history(self) -> dict:
        raw = self._client.get("/account/portfolio/history", {"period": "1M", "timeframe": "1D"})
        if not isinstance(raw, dict):
            raise BrokerError(f"portfolio history came back as {type(raw).__name__}, not an object")
        days: list[str] = []
        equity: list[Optional[float]] = []
        for stamp, value in zip(raw.get("timestamp") or [], raw.get("equity") or []):
            moment = datetime.fromtimestamp(int(stamp), tz=timezone.utc).astimezone(_MARKET_TZ)
            days.append(moment.date().isoformat())
            equity.append(_number(value))
        return {"days": days, "equity": equity}
