"""Single source of truth for every guardrail constant and runtime setting.

Two kinds of values live here, and the distinction is deliberate:

* ``GUARDRAILS``: hard-coded ``Final`` constants. They are *not* read from
  the environment, so a misconfigured ``.env`` can never loosen them.
  Loosening a guardrail requires a code change that shows up in review.
* ``Settings``: secrets and wiring (API keys, webhook secret, URLs) that
  legitimately differ per deployment and are read from ``.env`` / env vars.
"""

from __future__ import annotations

from pathlib import Path
from typing import Final

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# --------------------------------------------------------------------------- #
# Guardrails (code-only; NOT environment-configurable)
# --------------------------------------------------------------------------- #

#: Maximum fraction of account equity that may be allocated to a single ticker,
#: including any position already held in that ticker.
MAX_POSITION_PCT: Final[float] = 0.05

#: Signals with conviction below this are rejected before any market data is
#: fetched.
MIN_CONVICTION: Final[float] = 0.60

#: Maximum number of distinct tickers that may be held at once.
MAX_OPEN_POSITIONS: Final[int] = 10

#: Wilder ATR lookback, in trading days.
ATR_PERIOD: Final[int] = 14

#: Stop-loss distance from entry, in multiples of ATR.
ATR_STOP_MULTIPLIER: Final[float] = 2.0

#: Guard against a degenerate ATR (illiquid ticker, bad data). If ATR is less
#: than this fraction of price the signal is rejected rather than placing a
#: stop a few cents away.
MIN_ATR_PCT_OF_PRICE: Final[float] = 0.002

#: How much daily history to pull for the ATR calculation. Needs comfortably
#: more than ATR_PERIOD bars so the Wilder smoothing has warmed up.
OHLC_LOOKBACK_DAYS: Final[int] = 90

#: Minimum trade size. Fractional shares are never used: the stop-loss leg of
#: an Alpaca OTO/bracket order requires whole shares.
MIN_ORDER_QTY: Final[int] = 1

#: Orchestrator cadence.
HEARTBEAT_INTERVAL_MINUTES: Final[int] = 60

# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent
LOG_DIR: Final[Path] = PROJECT_ROOT / "logs"
AUDIT_LOG_PATH: Final[Path] = LOG_DIR / "execution_audit.log"

# --------------------------------------------------------------------------- #
# Environment-backed settings (secrets & wiring only)
# --------------------------------------------------------------------------- #


class Settings(BaseSettings):
    """Deployment-specific values. Read from ``.env`` then the process env."""

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    alpaca_api_key: str = Field(default="", description="Alpaca PAPER API key id")
    alpaca_secret_key: str = Field(default="", description="Alpaca PAPER API secret")
    webhook_shared_secret: str = Field(
        default="", description="Shared secret required in the x-webhook-secret header"
    )
    webhook_url: str = Field(
        default="http://localhost:8000/webhook/signal",
        description="Where the orchestrator POSTs validated signals",
    )
    watchlist: str = Field(
        default="AAPL,MSFT,NVDA",
        description="Comma-separated tickers the orchestrator evaluates each cycle",
    )
    anthropic_api_key: str = Field(default="", description="Claude API key (orchestrator only)")
    brightdata_api_token: str = Field(default="", description="Bright Data API token (orchestrator only)")
    brightdata_serp_zone: str = Field(
        default="serp_api", description="Name of the SERP API zone in the Bright Data dashboard"
    )

    @property
    def watchlist_tickers(self) -> list[str]:
        return [t.strip().upper() for t in self.watchlist.split(",") if t.strip()]


_settings: Settings | None = None


def get_settings() -> Settings:
    """Lazily construct the settings singleton so importing modules is side-effect free."""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
