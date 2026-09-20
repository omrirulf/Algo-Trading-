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
from typing import Final, NamedTuple

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

#: A fund holding many companies, all in ONE sector or ONE country.
#:
#: The cap that makes it safe to widen the watchlist past a couple of index
#: funds. A sector or country fund is diversified against a single company
#: failing and against nothing else -- XLE is twenty-three ways of being long
#: the oil price, and a Brazil fund is one currency, one central bank and one
#: election. Sizing it like a fund that spans the world would repeat, one
#: level up, the error the commodity cap exists to avoid: reading the cap off
#: the word "fund" rather than off the risk.
#:
#: Above the single-name cap because a sector cannot go to zero on a fraud;
#: below the broad-fund cap because one sector is one bet.
#:
#: MEASURED, 2026-09-15, by the `market checks` workflow over the new sleeve.
#: Two measurements disagreed, and the tighter one wins -- which is the same
#: call MAX_COMMODITY_FUND_PCT already makes:
#:
#: - Median daily volatility, 3mo of real bars: 1.16% for a focused fund
#:   against 2.25% for a single name, a ratio of 1.9x. Volatility *alone*
#:   would justify about 9.7%.
#: - Realised risk per trade, 2 years and 3,977 mechanical trades through the
#:   actual ATR stop and sizing math (backtest/compare_sleeves.py): a focused
#:   fund at 8% carried 0.28% of the account per trade against 0.25% for a
#:   single name at 5% -- *above* parity, which is exactly what the
#:   broad-fund cap was tuned down to avoid. Its worst trade was -1.09%
#:   against the single name's -0.97%.
#:
#: 7% is where the second measurement puts parity (8% x 0.25/0.28 = 7.1%).
#: The median volatility figure is the loose bound and the stop is what
#: actually decides what a position can lose, so the stop wins.
MAX_FOCUSED_FUND_PCT: Final[float] = 0.07

#: A fund tracking ONE commodity gets the tightest cap of the four, below
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

#: Per-group exceptions to MAX_EXPOSURE_GROUP_PCT. Each carries the number
#: that set it, measured on daily closes 2007-01-03 to 2026-09-18 (80 tickers,
#: yfinance, closes.csv SHA-256 f3a98414...5c3c).
#:
#: Duration: 30%. It holds LQD as well as the four Treasury maturities (see
#: ``instruments.EXPOSURE_GROUPS``).
#:
#: The number is set by how much the bucket can *lose*, not by how tightly its
#: members move together. They do move together -- that is why they are one
#: group -- but a cap is a loss budget, and correlation alone does not say how
#: large the loss is.
#:
#: Size it on the worst fill the caps actually *permit*, not on the basket
#: average. This cap counts market value, so it is blind to the fact that TLT
#: is roughly ten times as volatile as SHY -- $30 of each is the same number
#: to it, and in 2022 one fell 31.2% and the other 3.9%. What stops that being
#: a hole is the 12% per-position cap: 30% cannot be filled with TLT alone, it
#: needs three funds. The worst reachable fill is TLT 12% + LQD 12% + IEF 6%,
#: which on calendar-2022 returns loses **6.8% of the account** (peak to
#: trough, somewhat more). The basket average -- an 18.9% fall, 5.7% of the
#: account -- is the number an evenly-spread book gets, not the ceiling.
#:
#: One equity group at 25% still risks more: real estate fell 64% in the 2008
#: crisis, which is 16% of the account. A tighter number here would be buying
#: less protection than the equity groups already give away, while forbidding
#: the one asset that usually rallies when they fall.
#:
#: Read against what this replaces rather than against the general cap: 25% of
#: Treasuries plus 25% of LQD through Credit was really a 50% ceiling on one
#: rate view. 30% is a tightening of that.
EXPOSURE_GROUP_CAP_OVERRIDES: Final[dict[str, float]] = {
    "Duration": 0.30,
}

#: Ceiling on *net* stock-market risk, across every equity group at once.
#:
#: The groups bound one sector or region each. They do not bound the thing
#: those sectors share: on 20 years of weekly returns the 62 stock and
#: stock-like tickers move together at 0.52 on average, rising to 0.72 in the
#: 2008 crisis and 0.81 in the 2020 crash. Spread across eleven groups, that
#: one bet could fill the whole 95% gross cap while every group cap was
#: satisfied. This is the limit on it.
#:
#: Counted in beta-weighted dollars: each position's market value times its
#: beta to the US market (``instruments.EQUITY_RISK_BETAS``), so a staples
#: fund at beta 0.54 uses about half the room of a dollar of NVDA at 1.57.
#: Longs add and shorts subtract -- inside this bucket only. Stocks fell
#: together in every crash measured, so a short stock fund does offset a long
#: one; government paper rallied while stocks fell in 2022, so nothing outside
#: the bucket nets against it. The group, sleeve and gross caps stay sign-blind.
#:
#: The bucket is whatever ``EQUITY_RISK_BETAS`` lists, which is not the same
#: as whatever is called a stock: ``HYG`` (0.45) and ``EMB`` (0.34) are in it,
#: because credit sells off with equities and counting it at a haircut is
#: nearer the truth than counting it at zero. The Treasury maturities, the
#: commodities and ``UUP`` are absent, so they can neither consume this room
#: nor free any.
#:
#: What 60% would have meant, as a share of the account, for a book at the
#: limit: about 25% lost in the 2008 crisis, 22% in the 2020 crash, 15% in
#: 2022. With nothing but the gross cap the same book could have lost about
#: 39%, 35% and 24%.
#:
#: Known gap, measured and partly closed: this limit and Duration's ceiling
#: are separate budgets, and they are not independent.
#: ``analysis.correlations.risk_axis`` measures the raw correlation between
#: the two baskets and finds the sign *changes* -- five of six drawdowns
#: negative (bonds rallied as stocks fell), 2022 positive, the last year
#: +0.55. So a long stock book held with a short duration leg is one bet
#: made twice in a flight to quality, and a hedge in a rates shock, and no
#: static rule is right in both. Nothing here nets the two; the docstring
#: there says why.
#:
#: Two of the leaks an independent review found are closed. LQD now also
#: counts here (0.36, its crisis-only equity beta -- see
#: ``instruments.EQUITY_RISK_BETAS``), on top of being a full Duration
#: member, because it is a rate instrument on a quiet day and fell like a
#: stock in March 2020. HYG and EMB's own rate duration, which neither this
#: cap nor Credit's used to see, now also charges Duration -- see
#: ``instruments.DURATION_RATE_WEIGHT`` and
#: ``risk_engine._group_market_value``.
#:
#: Still open: whether the two sleeves should share one joint limit rather
#: than two independent ones. ``analysis.correlations.joint_stress_loss``
#: measures what today's actual book would lose if each named crisis
#: replayed, against a 15% threshold -- but only as a report, not a live
#: cap. Turning it into one needs a decision this repository has not made
#: yet: whether it gates new orders, like the group caps, or trims what is
#: already open, like Duration's -- see
#: ``correlations.JOINT_STRESS_LIMIT_PCT``.
MAX_EQUITY_RISK_PCT: Final[float] = 0.60

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
#:
#: Was 0.60. Three live cycles produced some 120 signals and zero trades: the
#: model's directional calls landed between 0.30 and 0.58, and the floor sat
#: above every one of them. A floor nobody has measured is a guess, and a
#: guess that stops every trade produces no data with which to replace it.
#:
#: 0.30 is where the model starts taking a side at all, so everything sided
#: now trades and the journal records the conviction on each one. That is the
#: experiment: let realised returns, bucketed by conviction, say where the
#: floor belongs, instead of this constant saying it. Lowering it makes no
#: single trade larger -- size comes from the cap and the stop, never from
#: conviction -- and costs no extra API spend, because the model is called
#: either way. What it buys is the only thing a paper account is for. A floor
#: set from data can be raised back; the risk engine, the ladder below and
#: the stop had never once run in live conditions, and would have stayed
#: untested at 0.60 for as long as the model kept answering under it.
MIN_CONVICTION: Final[float] = 0.30


class LadderRung(NamedTuple):
    """One rung of the profit ladder, measured in R.

    R is the distance from the entry to the initial stop -- what the trade
    would lose if it were stopped out. Measuring in R rather than in percent
    makes one rule fit a 30%-volatility chip fund and a 0.5%-volatility bond
    fund alike: each rung is "the trade has earned N times what it risked".
    """

    take_at_r: float      #: unrealised gain, in R, at which the rung triggers
    take_fraction: float  #: share of the ORIGINAL position closed at this rung
    stop_to_r: float      #: where the stop moves afterwards, in R from entry


#: How a winning position is unwound, and how its stop follows it up.
#:
#: Rung 1, at +1R: close a third and move the stop to the entry. The trade has
#: earned back what it risked, so a third of it is banked and the rest can no
#: longer lose. Rung 2, at +3R: close another third and move the stop to +1R,
#: so the remainder is guaranteed a profit. The final third has no rung -- it
#: runs on that stop until the market takes it out.
#:
#: Three properties the position manager enforces around this table:
#:
#: - The stop only ever tightens. A rung can raise it; nothing lowers it.
#: - The fractions sum to less than one, so a runner always exists.
#: - A rung reached by a gap is not skipped: a position that opens at +3.5R
#:   takes both rungs in the same cycle, in order.
#:
#: A position too small to split (fewer than three shares) takes no tranche
#: and is managed by its stop alone; the ratchet still applies.
#:
#: The rungs are floors, not the whole story: every cycle the position manager
#: also trails the stop up to ``price - ATR_STOP_MULTIPLIER x ATR`` where that
#: is tighter, so the runner does not ride a long move back down to +1R. The
#: stop is the only exit, and it only ever moves in the money's favour.
PROFIT_LADDER: Final[tuple[LadderRung, ...]] = (
    LadderRung(take_at_r=1.0, take_fraction=1 / 3, stop_to_r=0.0),
    LadderRung(take_at_r=3.0, take_fraction=1 / 3, stop_to_r=1.0),
)

#: Maximum number of distinct tickers that may be held at once.
#:
#: Raised from 10 with the cash floor, and from 20 with the profit ladder.
#: The per-position caps are small by design -- 12% for a broad fund, 4% for
#: a single commodity -- so reaching a fully-invested book *requires* many
#: positions, and at 10 this limit silently capped the account near 60%
#: through the back door.
#:
#: 20 was enough for a book of full-size positions: at an average cap of
#: about 7% across the watchlist, MAX_GROSS_EXPOSURE_PCT fills at 13 or so,
#: and the count never bound. The ladder changes that. A winner at +3R is
#: down to a third of its size but still holds a slot, so twenty trimmed
#: runners would sit at ~30% of the account with the other 65% in cash and
#: no room to open anything -- the count blocking exactly the redeployment
#: the ladder exists to free. A slot limit's remaining job is to stop the
#: book fragmenting into dust, and 40 -- half the watchlist -- does that
#: while leaving a trimmed book room to grow.
#:
#: Diversity is not this constant's job and never was. It comes from the
#: limits that target concentration directly: MAX_EXPOSURE_GROUP_PCT across
#: every exposure group, the sleeve budgets, and the per-kind caps. More
#: slots can only make the book wider; they cannot make it more concentrated.
MAX_OPEN_POSITIONS: Final[int] = 40

#: Skip the model entirely on a ticker already in the book.
#:
#: Stage zero of the funnel, and the only free one: a held name is asked
#: nothing, by either model. What that gives up is the top-up -- the engine
#: sizes a fresh signal on a held name as an addition to the existing
#: exposure -- and the flip block, which rejects a signal opposite to the side
#: held. Neither is load-bearing. A position that has gone wrong is closed by
#: its stop, and one that has gone right is trimmed up the ladder by
#: ``PositionManager``; both run every cycle, on arithmetic, for nothing. So
#: the daily re-read of a held name bought an averaging-in decision at full
#: model price, on the one part of the book that is already being managed.
#:
#: The cost is real and the direction is deliberate: the watchlist is 80 names
#: against MAX_OPEN_POSITIONS of 40, so a cycle's model spend should go to the
#: names that could still become positions, not the ones that already are.
#: Turn this off to restore the old behaviour -- every ticker reviewed, held
#: or not -- and note that it degrades to that on its own if the open book
#: cannot be read.
SKIP_HELD_TICKERS: Final[bool] = True

#: Ask the Message Batches API instead of calling the model directly.
#:
#: Half price for the same request, and the cycle is the ideal shape for it:
#: eighty independent prompts, none of which needs an answer in the same
#: second. What it costs is immediacy -- a batch is allowed up to 24 hours,
#: though a small one usually finishes in minutes -- and immediacy is the one
#: thing a trading cycle cannot simply give up. Two things buy it back.
#:
#: The cycle starts before the market opens, so the waiting happens in hours
#: the strategy was not trading in anyway. And a batch that has not finished by
#: BATCH_DEADLINE_SECONDS is abandoned for live calls, ticker by ticker, so the
#: worst a slow batch can do is cost what today's cycle already costs. It can
#: never cost a session.
#:
#: The catch worth stating: the market-open gate no longer guards the front of
#: the cycle, because pre-market it would refuse every run. A weekend or a
#: listed NYSE holiday is caught for free instead, by
#: ``config.market_calendar.is_trading_day`` -- checked before anything is
#: fetched, so those days cost nothing rather than a wasted batch. What that
#: calendar cannot see -- a half day, or an unscheduled closure -- still
#: reaches the engine's own gate, which refuses the orders either way.
USE_BATCH_API: Final[bool] = True

#: How long to wait on ONE batch before giving up on it and paying full price.
#:
#: Applied twice in a cycle -- once for the screen, once for whatever it
#: escalates -- because the two stages are submitted one after the other, not
#: together. The job's own timeout has to cover both waits in full, on top of
#: gathering context for eighty tickers first; see the comment on
#: ``timeout-minutes`` in ``heartbeat.yml``, which is sized against exactly
#: this arithmetic. Too long here and the job is killed mid-wait, which loses
#: the answers *and* the fallback -- the batch is still finished and still
#: paid for, and only its id could get them back.
BATCH_DEADLINE_SECONDS: Final[int] = 35 * 60

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

#: Orchestrator cadence. One cycle per trading day: the slow inputs change
#: daily at most, so an hourly loop was seven near-identical calls per ticker
#: at seven times the cost. The order-idempotency window is derived from this,
#: so at daily cadence the same ticker and side cannot be re-entered twice in
#: one UTC day -- which is the intended meaning of a daily signal.
HEARTBEAT_INTERVAL_MINUTES: Final[int] = 24 * 60

#: How many cycles the cost projections assume per trading day. Derived from
#: the interval so the two cannot disagree: 6.5 market hours at an hourly
#: interval was 7; at a daily interval it is 1.
CYCLES_PER_TRADING_DAY: Final[int] = max(1, round(390 / HEARTBEAT_INTERVAL_MINUTES))

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

#: The one thing this project has to remember for itself. Nowhere free
#: publishes a share-count series for an ETF, so the cycle records today's
#: count for every fund and the series accumulates here, one line per fund per
#: cycle. Committed back with the journal, because a runner is discarded and
#: an uncommitted reading is a lost day of history.
FUND_SIZE_LOG_PATH: Final[Path] = LOG_DIR / "fund_size.log"

#: Queryable index over both logs above, built by ``store/build_db.py``.
#:
#: Derived data, and gitignored for that reason: the JSON-lines files are the
#: system of record, this is a rebuild away from them, and committing a binary
#: that changes every cycle would bloat the repository for nothing.
DATABASE_PATH: Final[Path] = LOG_DIR / "trading.db"

# --------------------------------------------------------------------------- #
# Learned blend of the dimension scores
# --------------------------------------------------------------------------- #

#: How the learned blend of the five dimension scores takes part in a cycle.
#: ``shadow``: the composite is computed and journalled beside the model's own
#: answer, and nothing reads it. This is the only value the constant may take
#: until the walk-forward report has said, on realised returns, that the
#: composite beats the model's own conviction -- a CI invariant pins it here,
#: and the modes that let the composite touch a trade arrive with that report.
BLEND_MODE: Final[str] = "shadow"

#: Where the trainer writes the fitted weights and the heartbeat reads them.
#: Read once per cycle. A missing or unreadable file is equal weights, with
#: the reason journalled on every line of that cycle.
BLEND_WEIGHTS_PATH: Final[Path] = LOG_DIR / "blend_weights.json"

#: Days after which a weights file is still applied but flagged stale in the
#: journal. Two weeks: the trainer is meant to run nightly, so a fortnight
#: without a refit is a broken job, not a quiet market.
BLEND_STALE_AFTER_DAYS: Final[int] = 14

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
    screening_base_url: str = Field(
        default="",
        description=(
            "OpenAI-compatible endpoint to run the screening stage against, "
            "e.g. http://10.0.0.5:11434/v1 for Ollama. Blank -- the default -- "
            "screens with Claude Haiku as before. It cannot be a model on the "
            "GitHub-hosted runner: no GPU, and the disk is discarded between "
            "runs, so this has to point at a self-hosted runner or a machine "
            "on the network. A screen this endpoint fails to answer falls "
            "through to the full model, so the worst case is the cycle's cost, "
            "never a bad trade"
        ),
    )
    screening_model: str = Field(
        default="",
        description=(
            "Model name to ask that endpoint for, e.g. 'qwen2.5:14b'. Required "
            "when screening_base_url is set; ignored otherwise"
        ),
    )
    screening_api_key: str = Field(
        default="",
        description=(
            "Bearer token for screening_base_url, if it wants one. A local "
            "endpoint usually does not, and blank sends no header at all"
        ),
    )
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
    supabase_url: str = Field(
        default="",
        description=(
            "Supabase project URL, e.g. https://abc.supabase.co. Blank keeps "
            "the archive local: the remote push is skipped, not failed"
        ),
    )
    supabase_service_key: str = Field(
        default="",
        description=(
            "Supabase service-role key, used only by store/remote.py to push "
            "the archive. It bypasses row-level security, which is what lets "
            "the tables keep RLS on with no policies -- so the publishable "
            "key can do nothing at all. Never put this in client code"
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
