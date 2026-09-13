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
from pathlib import Path
from typing import Any, Optional, Protocol

import yaml

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


class BrokerError(RuntimeError):
    """Raised when the broker rejects a request or is unreachable."""


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
