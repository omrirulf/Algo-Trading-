# Hybrid LLM/Deterministic Trading System

[![CI](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml/badge.svg)](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml)

Qualitative LLM analysis is fully decoupled from trade execution. The LLM can
only ever emit a closed set of fields — a direction, a confidence, and its
reasoning — and only `bias` and `conviction` are ever acted on. A FastAPI
webhook validates that shape (rejecting anything else with a 422), and a
pure-Python risk engine does 100% of the sizing, stop-loss, and Alpaca
paper-trade execution.

Each hourly cycle gives the model five kinds of context per ticker — recent
news, technicals, fundamentals, the analyst/institutional view, and insider
buying and selling — and records all of it alongside the resulting signal so
the signals can be graded later.

**Full documentation:** **[algotrade.mintlify.site](https://algotrade.mintlify.site/)**
— built from the [`docs/`](docs/) directory, auto-deployed on every push to
`main`. For a local preview instead, run `cd docs && npx mintlify dev`, or
read the `.mdx` files directly on GitHub starting from
[`docs/index.mdx`](docs/index.mdx).

## Directory structure

```
algo-trading-system/
├── requirements.txt
├── pytest.ini
├── .github/workflows/ci.yml   # tests on 3.11/3.12 + guardrail invariant checks
├── .env.example              # copy to .env and fill in
├── config/
│   └── settings.py           # all guardrail constants (single source of truth)
├── app/
│   ├── main.py                # FastAPI app + /webhook/signal endpoint
│   ├── schemas.py             # LLMSignal (extra="forbid") + ExecutionResult
│   ├── risk_engine.py         # position sizing (5% cap) + ATR stop-loss math
│   ├── market_data.py         # yfinance-based ATR / price fetch
│   ├── broker_client.py       # Alpaca paper trading client (only module with keys)
│   ├── execution_engine.py    # orchestrates validate -> size -> stop -> submit
│   └── logger.py              # structured JSON audit log
├── orchestrator/
│   ├── heartbeat.py           # hourly job: gather context -> call LLM -> POST signal
│   ├── news.py                # Bright Data SERP API (Google News) headline fetch
│   ├── context.py             # the only module that touches yfinance; prompt assembly
│   ├── technicals.py          # SMA/RSI/MACD/returns/52w/vol (pure, no network)
│   ├── fundamentals.py        # valuation, margins, growth, balance sheet (pure)
│   ├── analysts.py            # consensus, targets, rating changes, ownership (pure)
│   ├── insiders.py            # Form 4 buys/sells; grants excluded (pure)
│   ├── formatting.py          # number formatting; missing values render as "n/a"
│   ├── journal.py             # per-cycle record of context + signal + outcome
│   └── llm.py                 # Claude call, constrained by the signal schema
├── analysis/                  # offline scoring; read-only, no broker path
│   ├── reader.py              # parse the signal journal (pure)
│   ├── returns.py             # join signals to realised returns; entry-timing rules
│   ├── metrics.py             # rank correlations, buckets, drift (pure)
│   ├── report.py              # text report; owns the "too few to conclude" threshold
│   └── score_journal.py       # CLI: python analysis/score_journal.py
├── tests/
│   ├── conftest.py            # FakeBroker / FakeMarketData; no network in tests
│   ├── test_risk_engine.py    # proves the 5% cap and ATR stop math hold
│   ├── test_schemas.py        # proves the LLM cannot smuggle qty/price fields
│   ├── test_market_data.py    # Wilder ATR against a reference implementation
│   ├── test_execution_engine.py  # full decision path + the new fields are inert
│   ├── test_webhook.py        # auth + 422 at the HTTP layer
│   ├── test_heartbeat.py      # orchestrator can only send the closed shape
│   ├── test_news.py           # Bright Data request shape + response parsing
│   ├── test_technicals.py     # indicators vs independent reference implementations
│   ├── test_fundamentals.py   # info parsing + every earnings-date shape
│   ├── test_analysts.py       # consensus / ratings / holders parsing
│   ├── test_insiders.py       # proves a grant is never counted as insider buying
│   ├── test_context.py        # assembly and every degradation path
│   ├── test_journal.py        # the journal records context, signal and failures
│   ├── test_analysis_returns.py   # proves an entry price can never predate its signal
│   ├── test_analysis_metrics.py   # rank correlation vs hand-computed values
│   ├── test_analysis_reader.py    # journal parsing, including truncated lines
│   ├── test_analysis_scoring.py   # scorer end to end + report honesty
│   └── test_llm.py            # schema derivation + every LLM failure mode
└── logs/
    ├── execution_audit.log    # what the engine did      (generated at runtime)
    └── signal_journal.log     # what the model saw       (generated at runtime)
```

## Setup

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # fill in your Alpaca paper keys + a random webhook secret
```

### Broker (Alpaca paper)

Copy a **paper** key pair from the
[Alpaca paper dashboard](https://app.alpaca.markets/paper/dashboard/overview)
into `ALPACA_API_KEY` / `ALPACA_SECRET_KEY`.

**Or use the CLI instead of copying keys.** The official
[Alpaca CLI](https://github.com/alpacahq/cli) authenticates over OAuth and
stores a profile in `~/.config/alpaca/profiles/` at `0600`:

```bash
alpaca profile login    # browser OAuth; paper by default
# leave ALPACA_API_KEY / ALPACA_SECRET_KEY blank in .env
```

Credentials resolve as an **atomic bundle** — a key from one source is never
paired with a secret from another — in the order `ALPACA_API_KEY` +
`ALPACA_SECRET_KEY` → the profile's OAuth `access_token` → the profile's
stored `api_key` + `secret_key`. Setting only one half of the env pair is an
error rather than a silent fallthrough. `ALPACA_PROFILE` picks the profile;
`ALPACA_CONFIG_DIR` moves the directory.

> **A profile marked `live_trade: true` is refused, not used.** This system is
> paper-only, and borrowing a live bundle would point real money at a strategy
> whose entire safety argument is that it cannot reach a live endpoint. The
> refusal names the profile and the ways out, rather than reporting "no
> credentials found" on a machine that plainly has some. It is belt-and-braces
> anyway: `paper=True` is hard-coded, and the SDK pins its base URL to the
> paper endpoint from that flag alone. CI checks for both.

<sub>Unlike the Bright Data lookup, this one is **verified against the CLI's
source** (`alpacahq/cli`, `internal/config/config.go`), not guessed: YAML at
`<config dir>/profiles/<name>.yaml`, fields `api_key`, `secret_key`,
`access_token`, `scopes`, `live_trade`, and a config directory of
`$ALPACA_CONFIG_DIR` or `~/.config/alpaca` on every platform.</sub>

### News feed (Bright Data)

The orchestrator pulls the last 24 hours of Google News headlines for each
watchlist ticker through [Bright Data's SERP API](https://brightdata.com/products/serp-api).

```bash
brightdata login                               # browser OAuth; --device if headless
export BRIGHTDATA_UNLOCKER_ZONE=cli_unlocker   # the zone the login just created
```

That is the whole setup — **no dashboard visit required.** `brightdata login`
provisions a `cli_unlocker` zone rather than a SERP API zone, but Bright Data's
own CLI sends search queries through an unlocker zone by preference: its
`search` command resolves `BRIGHTDATA_SERP_ZONE` and then falls back to
`BRIGHTDATA_UNLOCKER_ZONE`, and its `init` offers the unlocker zone as the SERP
default with *yes* preselected. `orchestrator/news.py` mirrors that resolution.

<sub>Read from the CLI's source, not confirmed against a live call — Bright
Data's API was unreachable from the environment this was built in. If your
account refuses search on an unlocker zone, the symptom is a `NewsFetchError`
about HTML instead of JSON; create a **SERP API** zone in the dashboard and set
`BRIGHTDATA_SERP_ZONE`. Nothing else changes.</sub>

The dashboard route, if you prefer it: create a zone of type **SERP API**
(default name `serp_api`, else set `BRIGHTDATA_SERP_ZONE`) and copy a token
from *Account settings -> API tokens* into `BRIGHTDATA_API_TOKEN`.

**Or use the CLI instead of copying a token.** The official
[Bright Data CLI](https://github.com/brightdata/cli) authenticates over OAuth
and stores a key locally:

```bash
brightdata login        # browser OAuth; use --device on a headless machine
# leave BRIGHTDATA_API_TOKEN blank in .env
```

The token is resolved in order: `BRIGHTDATA_API_TOKEN` → `BRIGHTDATA_API_KEY`
(the variable the CLI itself reads, so one secret serves both) → the key
`brightdata login` stored on disk.

<sub>Reading the CLI's credential file is **best-effort**: its format isn't
documented, so the lookup tries several field names and treats anything it
can't parse as "not configured this way" rather than failing. If it guesses
wrong on your machine, set `BRIGHTDATA_API_TOKEN` explicitly.</sub>

Each cycle sends one request per ticker, so the default three-ticker
watchlist costs 72 SERP requests a day. Bright Data's own free tier /
pay-as-you-go pricing covers that comfortably; check your zone's usage page
after the first day. If no token is resolvable the cycle logs
`No Bright Data credentials found: set BRIGHTDATA_API_TOKEN, or run
brightdata login` for each ticker and sends nothing.

### Market context (yfinance — no API key)

Headlines alone say that something happened, not whether it landed on a cheap
business or an expensive one, on an uptrend or a breakdown, or on a name the
street already loves. Before building the prompt, `orchestrator/context.py`
adds four more dimensions, all from yfinance, which is unauthenticated — **no
new key, no new per-request cost:**

| Source | What goes into the prompt |
|---|---|
| `technicals.py` | 20/50/200-day SMAs and distance from each, Wilder RSI(14), MACD(12/26/9), 1d/5d/1m/3m returns, 52-week range position, ATR(14) as % of price, annualised 20-day vol, volume vs its 20-day average |
| `fundamentals.py` | Sector, market cap, trailing/forward P/E, P/B, PEG, profit and operating margins, ROE, YoY revenue and earnings growth, debt/equity, free cash flow, beta, short interest, next earnings date |
| `analysts.py` | Consensus rating and 1-to-5 mean, full rating breakdown, mean/high/low price targets and implied upside, recent upgrades and downgrades by firm, institutional ownership and largest holders |
| `insiders.py` | Six-month insider buy/sell rollup, net shares, distinct buyers vs sellers, and recent open-market purchases and sales by name and role |

Insider data is the one source where the naive reading is usually wrong, so
it gets special handling: **buys and sells are not symmetric.** An insider
buying on the open market is spending their own money on a view; a sale is
weak evidence, since insiders sell on schedules, for tax on vesting shares,
and to diversify. Stock grants and option exercises are excluded entirely —
counting compensation as "insider buying" would make the dimension noise. The
prompt states all of this, and `orchestrator/insiders.py` reports the
exclusions rather than hiding them.

The ATR comes from `app.market_data.calculate_atr` — the same function the
risk engine will use to place the stop, not a second implementation that could
drift from it.

**Failures degrade rather than propagate.** Every source is fetched
independently; a failure records a named gap in the prompt and the model is
told to score that dimension `0.0` rather than guess. News is the deliberate
exception: if Bright Data is down the ticker is skipped entirely, because
trading on technicals alone would quietly be a different strategy.

Slow-moving data (fundamentals, ratings, ownership, insider filings) is cached
for six hours per ticker; price history is refetched every cycle.

### Analyst (Claude)

Put an API key from [the Anthropic Console](https://console.anthropic.com)
in `ANTHROPIC_API_KEY`. The orchestrator sends each ticker's assembled context
to `claude-opus-5` and gets back one signal per ticker.

**Or use the CLI instead of a key.** If you run `ant auth login` (the
[Anthropic CLI](https://console.anthropic.com)) on the machine that runs the
heartbeat, `ANTHROPIC_API_KEY` can be left blank — the SDK falls back to that
login's profile, then to `ANTHROPIC_AUTH_TOKEN`, then to Workload Identity
Federation. This is a good fit for running the heartbeat locally under your
own login; an unattended deployment (a server, a container) should still use
an explicit key, since a CLI login profile is tied to one person's session.
Leaving the key blank never fails silently: if nothing is resolvable when a
cycle runs, that ticker logs `No Claude credentials found: set
ANTHROPIC_API_KEY, or run ant auth login` and is skipped, the same as any
other `LLMError`.

The system prompt weights the five inputs differently — news is fast and
noisy, technicals are about timing rather than business quality, fundamentals
rarely change a view within an hour, and the analyst view is a prior already
in the price unless it just moved. It is also explicit about the failure mode
that richer context introduces:

> More context does not mean more conviction. Conviction is earned when
> independent dimensions agree, and it must fall when they conflict.

Alongside `bias`, `conviction` and `rationale`, the model reports a score in
`[-1, 1]` for each of the five dimensions plus up to six `key_factors`. These
are **inert**: they are journalled for later evaluation and nothing in the
execution or risk engine reads them. A CI invariant check enforces that.

The call is constrained at generation time: `orchestrator/llm.py` derives a
JSON schema from `LLMSignal` and passes it as `output_config.format`, so the
model physically cannot emit a `quantity` field to be rejected later. Value
bounds (conviction in [0, 1], the ticker pattern, the 2000-character
rationale cap) are deliberately *not* sent to the model and are enforced by
`LLMSignal` on the way back instead — the schema the model sees stays inside
what constrained decoding accepts, and the tight bounds stay where they are
actually checked.

Model and thinking effort are code constants at the top of
`orchestrator/llm.py` (`MODEL`, `EFFORT`), not environment variables, so
changing which model trades your account is a visible code change. A refusal,
a truncated response, a non-JSON response, or an API error all raise
`LLMError`, which is logged and skips that ticker for the cycle.

**Refusal fallback.** If a safety classifier declines a request, the API
re-runs it on another model within the same call and marks the switch with a
`fallback` content block. The request asks for `fallbacks="default"`, which
routes by refusal category, so there is no model list in the repo to go
stale. Two consequences worth knowing:

- The answer is read from *after* the last switch point. A model that
  declines mid-turn can leave partial text behind, and that text is not the
  signal.
- If the fallback beta is not enabled on your account, the first call of each
  provider is rejected and retried immediately without it, with a warning in
  the log. You lose the rescue, not the cycle.

## Run

One process, no webhook — `EXECUTION_MODE` defaults to `direct`:

```bash
python -m orchestrator.heartbeat --once   # one cycle, then exit
python -m orchestrator.heartbeat          # schedule every HEARTBEAT_INTERVAL_MINUTES
```

A cycle exits immediately when Alpaca's clock says the market is shut, so
running it off-hours costs nothing.

<details>
<summary>Two-process mode, if you want the engine on a different machine</summary>

```bash
# Terminal 1: the deterministic execution engine
uvicorn app.main:app --reload --port 8000

# Terminal 2: the orchestrator
EXECUTION_MODE=webhook python -m orchestrator.heartbeat
```

Only this mode reads `WEBHOOK_SHARED_SECRET`. The trade-off either way is in
[Deployment](docs/deployment.mdx): direct mode is simpler and needs no secret,
but the orchestrator process then holds the Alpaca credentials.
</details>

## Run it on a schedule, without a server

`.github/workflows/heartbeat.yml` runs a cycle hourly through US market hours
and commits the journal back, so there is nothing to host and the logs are
readable from the GitHub mobile app. Add four Actions *secrets* —
`ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ANTHROPIC_API_KEY`,
`BRIGHTDATA_API_TOKEN` — then run it once by hand from the Actions tab as a
smoke test. No variables to set: the watchlist is in `config/watchlist.py` and
the Bright Data zone defaults to the one `brightdata login` creates. Full setup
and caveats in [Deployment](docs/deployment.mdx).

<sub>A runner is a fresh container every run, with no home directory and no
browser, so the CLI logins cannot help there — secrets are the only way to
authenticate on Actions. The CLI logins are for running the heartbeat on a
machine you control.</sub>

## Iterate without waiting

The scorer needs ~20 signals before it says anything. Two tools close faster
loops in the meantime:

```bash
# Change the prompt, see how the model would have answered context it was
# already shown. --dry-run costs nothing.
python replay/replay_journal.py --dry-run --limit 3
python replay/replay_journal.py --system-prompt v2.txt --limit 20

# What a 2x ATR stop and a 5% cap actually do, over two years of real bars.
python backtest/run_backtest.py AAPL
```

[Replay](docs/replay.mdx) is honest because the context was captured live;
a backtest of the *strategy* would not be, since fundamentals and analyst
ratings are current-snapshot only and a SERP query cannot be time-travelled.
[The risk-engine backtest](docs/backtest.mdx) sidesteps that by testing only
the deterministic half -- and reports that its own returns are not an edge.

The backtest needs no credentials and no live cycles, so it is the one piece
of evidence available before the first cycle ever runs.

## Score the signals

```bash
python analysis/score_journal.py              # text report
python analysis/score_journal.py --json       # same figures, machine-readable
```

Joins every journalled signal to the return that actually followed and reports
whether conviction predicted the outcome, whether the 0.60 floor filtered the
*right* signals, which of the five dimension scores carried any information,
whether conviction fell when dimensions disagreed (the prompt demands it), and
whether conviction is drifting upward over time.

Two properties matter more than the numbers:

- **It cannot enter at a price that predates the signal.** A signal fired after
  the close is never scored against that day's close — that is the one bug that
  would make the report flatter the strategy and be believed. `--entry` selects
  the rule; the default reads the signal's UTC timestamp to decide.
- **It reports sample sizes and refuses to overclaim.** Anything under 20
  observations is marked `too few`. Two weeks in, the honest output is a
  coverage table and a row of `too few`.

Returns are close-to-close and ignore the stop-loss, slippage and commission:
this measures the *signal*, not the strategy's P&L. The agreement check needs no
price data at all, so it works from the first cycle.

## Test the guardrails directly

```bash
pytest tests/ -v
```

Or hit the webhook by hand:

```bash
curl -X POST http://localhost:8000/webhook/signal \
  -H "Content-Type: application/json" \
  -H "x-webhook-secret: <your WEBHOOK_SHARED_SECRET>" \
  -d '{"ticker": "AAPL", "bias": "BULLISH", "conviction": 0.75, "rationale": "Strong earnings beat"}'
```

Try adding `"quantity": 500` to that payload — it will be rejected with a
422 before any execution logic runs.

## Where each guardrail is enforced

| Guardrail | Enforced in |
|---|---|
| LLM cannot set qty/price/order params | `schemas.py` (`extra="forbid"`) — structural, not a convention |
| Scores and `key_factors` cannot influence a trade | Only `bias` and `conviction` are read by `execution_engine.py`; CI greps the execution path for the transparency fields |
| Enriched context can't reach for a credential | CI greps `context.py` / `technicals.py` / `fundamentals.py` / `analysts.py` for settings and key reads |
| The scorer cannot trade | CI greps `analysis/` for any order path or file write — it grades past decisions and must never be able to make one |
| Prompt injection has a bounded blast radius | Headlines and firm names are third-party text. The system prompt marks the whole context block untrusted, and even a successful injection can only move `bias`/`conviction` — still subject to the conviction floor, the 5% cap, and a mandatory stop |
| Max 5% of equity per ticker | `risk_engine.calculate_position_size()` (checked twice: pre- and post-rounding; existing exposure in the ticker counts toward the cap) |
| Mandatory stop-loss on every order | `broker_client.submit_bracket_order()` — no code path submits without `StopLossRequest` (Alpaca OTO: market entry + attached stop) |
| Stop distance from real volatility | `market_data.calculate_atr()` (Wilder ATR from yfinance OHLC), rejected if ATR is degenerate |
| Conviction floor | `risk_engine.check_conviction_threshold()` |
| Max concurrent positions | `risk_engine.check_position_count_limit()` |
| No flipping via a fresh entry | `execution_engine.py` rejects a signal opposing an open position in the same ticker |
| Guardrails can't be loosened by `.env` | `config/settings.py` — thresholds are `Final` constants, not env vars |
| API keys never touch LLM-adjacent code | Only `broker_client.py` imports the Alpaca SDK / reads the keys |
| Full audit trail | `logger.py` → `logs/execution_audit.log`, every accept/reject/error logged as JSON |

## Decision path

`POST /webhook/signal` → shared-secret check (401) → `LLMSignal` validation
(422) → `ExecutionEngine.execute()`:

1. `NEUTRAL` bias → `REJECTED` (nothing to do).
2. Conviction below `MIN_CONVICTION` → `REJECTED`, before any network I/O.
3. Fetch equity and open positions from Alpaca.
4. New ticker and already at `MAX_OPEN_POSITIONS` → `REJECTED`.
5. Open position in the opposite direction → `REJECTED`.
6. Fetch latest close and 14-day ATR; ATR below `MIN_ATR_PCT_OF_PRICE` → `REJECTED`.
7. Stop = entry ∓ `ATR_STOP_MULTIPLIER` × ATR (long / short).
8. Size = floor((5% × equity − existing exposure) / price); 0 shares → `REJECTED`.
9. Submit market entry with attached stop → `ACCEPTED`.

Any broker / market-data failure produces an `ERROR` result rather than an
exception, and every outcome is written to the audit log.

## Continuous integration

`.github/workflows/ci.yml` runs on every pull request against `main`, and
on pushes to `main` itself:

- **tests** — installs the pinned requirements and runs the full suite on
  Python 3.11 and 3.12, with no credentials and no network, then checks that
  `app.main` imports and builds its OpenAPI schema without any Alpaca keys.
- **guardrail invariants** — greps that enforce the architecture claims in the
  table above, so they cannot rot silently:
  the Alpaca SDK is imported only by `broker_client.py`; the API keys are read
  only there; `paper=True` is still a hard-coded literal; the risk thresholds
  are still `Final` constants and `config/settings.py` never reads the
  environment directly; the LLM's transparency fields never appear in the
  execution path; the market-context modules read no credentials; and no
  `.env` is tracked in git.

Each invariant check was verified to fail when its invariant is broken, so a
green run means something.

## Notes / next steps for production

- Swap the webhook's shared-secret header for HMAC request signing.
- `orchestrator/news.py` searches Google News for `"<TICKER> stock"`. For
  tickers whose symbol is a common word, or to include the company name,
  adjust `build_news_search_url()`.
- The journal is recorded *and* scored, but nothing acts on the result. If
  `score_journal.py` says a dimension carries no information, or that the
  conviction floor is filtering the wrong way, changing the prompt or the
  threshold is still a manual decision — as it should be, until there are
  months rather than weeks of data behind it.
- Scoring measures the signal, not the strategy. Close-to-close returns ignore
  the stop-loss, so a signal that was right about direction but stopped out on
  the way there still scores as a win. Joining the scorer to
  `logs/execution_audit.log` would close that gap.
- Insider transactions (Form 4 buying and selling) are the obvious next
  context source. yfinance exposes some of it, but a dedicated provider is
  more reliable — that one would need a new API key.
- `context.py` fetches each ticker's sources serially. With a longer watchlist
  that becomes the slowest part of a cycle; the fetches are independent and
  could run concurrently.
- Consider persisting `ExecutionResult` rows to a database in addition to
  the log file, for querying trade history.
- `TradingClient(..., paper=True)` is hard-coded in `broker_client.py` —
  removing that safety requires an explicit code change, not an env flag,
  so a misconfigured `.env` can't accidentally go live.
- The engine does not currently close or reduce positions; the attached
  stop is the only exit. Add an explicit exit path before relying on
  `BEARISH` signals to unwind longs.
