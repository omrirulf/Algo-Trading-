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

#: The same cap for an index fund, which is a different kind of bet. A broad
#: fund is already hundreds of positions, so holding one at the single-name
#: cap buys 5% of equity exposure and leaves the account in cash -- the
#: diversification argument for indices and a 5% cap cancel each other out.
#: Sized against volatility rather than picked for roundness. Risk per trade
#: is roughly ``cap / volatility``, so a cap N times larger on an instrument
#: only M times quieter multiplies the risk the stop carries by N/M. A first
#: pass at 20% measured ~1.9x the planned risk per trade of a single name --
#: bigger, not safer. 12% keeps it near parity while still buying enough
#: exposure for an index position to matter.
#:
#: Above the single-name cap because a broad fund's tail is truncated in a way
#: a company's is not: an index does not go to zero on a fraud.
#:
#: MEASURED, 2026-09-14, 3mo of real bars via backtest/verify_tickers.py:
#: median daily volatility was 2.26% for a single name and 0.88% for a broad
#: fund -- a ratio of 2.57x, so a broad-fund cap up to ~12.8% carries no more
#: risk per trade than 5% on a stock. 12% is 2.40x, inside that and slightly
#: conservative. This number started as a guess and is now checked.
MAX_BROAD_FUND_PCT: Final[float] = 0.12

#: A fund tracking ONE commodity gets the tightest cap of the three, below
#: even a single name. "Fund" does no diversification work here -- coffee is
#: one thing -- and three risks pile on top that no equity carries: roll decay
#: in contango (USO being the notorious case), issuer credit risk on the ETNs,
#: and thin volume that makes a stop fill badly.
#:
#: Sizing these like a broad fund because both are technically ETFs would
#: repeat, in a subtler place, the error of picking a cap by label rather than
#: by risk.
#:
#: MEASURED, 2026-09-14: median daily volatility 1.58%, which is 0.70x a single
#: name -- so volatility *alone* would justify ~7%, and 4% is deliberately
#: below what the arithmetic allows. Three reasons to stay there:
#:
#: - The median hides the spread. USO measured 3.29% and SLV 2.62%, both above
#:   the median single name. A cap set on the median would be far too loose
#:   for the volatile end of the sleeve.
#: - Daily volatility does not see roll decay. A futures-backed fund can bleed
#:   value with spot flat, and no standard-deviation figure captures that.
#: - It does not see issuer risk either. The coffee ETN on this list stopped
#:   resolving between being added and first being verified, which is what
#:   that risk looks like when it arrives.
MAX_COMMODITY_FUND_PCT: Final[float] = 0.04

#: Ceiling on any one exposure group (``instruments.EXPOSURE_GROUPS``).
#:
#: A diversified watchlist does not produce a diversified portfolio. Nothing
#: previously stopped the engine opening MSFT, NVDA, TSM, ASML and GOOGL on
#: the same morning: five positions, one bet, and every per-ticker cap
#: satisfied. This is the check that bites, and it spans both sleeves -- XOM
#: plus an oil fund plus a gas fund is one energy bet made three times.
MAX_EXPOSURE_GROUP_PCT: Final[float] = 0.25

#: Sleeve budgets. Funds are the core holding and single names the satellite,
#: which is a deliberate statement about where the confidence is: a broad fund
#: is diversified by construction, while a stock-picking edge is unproven here
#: and this budget declines to assume one.
#:
#: They sum to MAX_GROSS_EXPOSURE_PCT, so the gross cap binds only when a
#: sleeve is under-used rather than being a fourth independent limit.
MAX_SINGLE_NAME_SLEEVE_PCT: Final[float] = 0.25
MAX_FUND_SLEEVE_PCT: Final[float] = 0.70

#: Ceiling on total deployed capital across every open position. Its job is to
#: stop the per-ticker caps multiplying out into leverage -- nothing else.
#:
#: It sat at 60% for one revision, which meant a permanent 40% cash floor. That
#: was wrong for an investment account and hard to defend: cash yields close to
#: nothing while equities are the reason the account exists, so a standing 40%
#: allocation to it is a large, silent drag chosen by no one. The risk work it
#: looked like it was doing is already done, and done better, by limits that
#: target the actual hazards: MAX_EXPOSURE_GROUP_PCT bounds concentration,
#: the per-kind caps bound single-position risk, and every position carries a
#: stop.
#:
#: In a *paper* account the argument is stronger still: there is no capital at
#: risk, so holding back only produces less information about how the strategy
#: behaves at full size.
#:
#: 95% rather than 100% is operational, not prudential. An order needs buying
#: power to be accepted, and a market order can fill above the quote -- a book
#: at exactly 100% would start rejecting its own orders.
MAX_GROSS_EXPOSURE_PCT: Final[float] = 0.95

#: Signals with conviction below this are rejected before any market data is
#: fetched.
MIN_CONVICTION: Final[float] = 0.60

#: Maximum number of distinct tickers that may be held at once.
#:
#: Raised from 10 with the cash floor. The per-position caps are small by
#: design -- 12% for a broad fund, 4% for a single commodity -- so reaching a
#: fully-invested book *requires* many positions: roughly eight funds and five
#: names. At 10 this limit would have silently capped the account near 60%
#: again through the back door, which is the sort of interaction that is
#: invisible until someone reads two constants together.
MAX_OPEN_POSITIONS: Final[int] = 20

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

#: Orchestrator-side record of the context each signal was produced from, for
#: judging signal quality after the fact. Separate from the execution audit:
#: that one records what the engine did, this one records what the model saw.
SIGNAL_JOURNAL_PATH: Final[Path] = LOG_DIR / "signal_journal.log"

#: Queryable index over both logs above, built by ``store/build_db.py``.
#:
#: Derived data, and gitignored for that reason: the JSON-lines files are the
#: system of record, this is a rebuild away from them, and committing a binary
#: that changes every cycle would bloat the repository for nothing.
DATABASE_PATH: Final[Path] = LOG_DIR / "trading.db"

from config.watchlist import default_watchlist_csv

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
    execution_mode: str = Field(
        default="direct",
        description=(
            "How signals reach the engine: 'direct' (in-process, no webhook) "
            "or 'webhook' (POST to a separately running app)"
        ),
    )
    webhook_url: str = Field(
        default="http://localhost:8000/webhook/signal",
        description="Where the orchestrator POSTs validated signals",
    )
    watchlist: str = Field(
        default_factory=default_watchlist_csv,
        description=(
            "Comma-separated tickers evaluated each cycle. Defaults to the "
            "curated list in config/watchlist.py, which is version-controlled "
            "so a change to what gets traded shows up in a diff"
        ),
    )
    anthropic_api_key: str = Field(default="", description="Claude API key (orchestrator only)")
    brightdata_api_token: str = Field(default="", description="Bright Data API token (orchestrator only)")
    brightdata_serp_zone: str = Field(
        default="",
        description=(
            "Name of your Bright Data SERP API zone. Deliberately empty by "
            "default: it used to default to 'serp_api', which meant the "
            "unlocker-zone fallback below could never fire and anyone who had "
            "only run `brightdata login` sent a zone name their account did "
            "not have"
        ),
    )
    brightdata_unlocker_zone: str = Field(
        default="cli_unlocker",
        description=(
            "Web Unlocker zone, used when no SERP zone exists. Defaults to the "
            "zone `brightdata login` creates, so the CLI path needs no config"
        ),
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
