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
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional, Protocol

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

    # --- position management: the only three things the ladder may do ---

    def get_open_stop_order(self, ticker: str) -> Optional[StopOrder]: ...

    def replace_stop_order(self, order_id: str, qty: int, stop_price: float) -> StopOrder: ...

    def close_position_partially(self, ticker: str, qty: int) -> str: ...


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
        from alpaca.trading.enums import OrderType, QueryOrderStatus
        from alpaca.trading.requests import GetOrdersRequest

        symbol = ticker.strip().upper()
        try:
            orders = self._client.get_orders(
                GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[symbol], nested=True)
            )
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"get_orders failed for {symbol}: {exc}") from exc

        seen: set[str] = set()
        for parent in orders or []:
            for candidate in (parent, *(getattr(parent, "legs", None) or [])):
                order_id = str(getattr(candidate, "id", ""))
                if not order_id or order_id in seen:
                    continue
                seen.add(order_id)
                if str(getattr(candidate, "symbol", "")).upper() != symbol:
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
                return StopOrder(
                    order_id=order_id,
                    ticker=symbol,
                    qty=int(float(candidate.qty)),
                    stop_price=float(stop_price),
                    side=str(getattr(side, "value", side)),
                )
        return None

    def replace_stop_order(self, order_id: str, qty: int, stop_price: float) -> StopOrder:
        """Move a live stop and shrink it to the shares it still protects.

        One call, so there is no moment between "old stop cancelled" and "new
        stop placed" in which the position is naked -- Alpaca applies a
        replace atomically or refuses it. The position manager calls this
        *before* selling a tranche, for the same reason: a stop that still
        covers the old size would reserve shares the exit needs.
        """
        from alpaca.trading.requests import ReplaceOrderRequest

        if qty < 1 or int(qty) != qty:
            raise BrokerError(f"qty must be a positive whole number, got {qty}")
        if stop_price <= 0:
            raise BrokerError(f"stop_price must be positive, got {stop_price}")
        try:
            order = self._client.replace_order_by_id(
                order_id, ReplaceOrderRequest(qty=int(qty), stop_price=stop_price)
            )
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"replace_order failed for {order_id}: {exc}") from exc
        side = getattr(order, "side", "")
        return StopOrder(
            order_id=str(order.id),
            ticker=str(order.symbol).upper(),
            qty=int(float(order.qty)),
            stop_price=float(order.stop_price if order.stop_price is not None else stop_price),
            side=str(getattr(side, "value", side)),
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
        try:
            order = self._client.close_position(symbol, ClosePositionRequest(qty=str(int(qty))))
        except Exception as exc:  # noqa: BLE001
            raise BrokerError(f"close_position failed for {symbol}: {exc}") from exc
        return str(getattr(order, "id", "") or "")
