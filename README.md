# Hybrid LLM/Deterministic Trading System

[![CI](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml/badge.svg)](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml)

Qualitative LLM analysis is fully decoupled from trade execution. The LLM can
only ever emit a closed set of fields — a direction, a confidence, and its
reasoning — and only `bias` and `conviction` are ever acted on. A FastAPI
webhook validates that shape (rejecting anything else with a 422), and a
pure-Python risk engine does 100% of the sizing, stop-loss, and Alpaca
paper-trade execution.

Each daily cycle gives the model five kinds of context per ticker — recent
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
│   ├── risk_engine.py         # position sizing (per-instrument caps) + ATR stops
│   ├── market_data.py         # yfinance-based ATR / price fetch
│   ├── broker_client.py       # Alpaca paper trading client (only module with keys)
│   ├── execution_engine.py    # orchestrates validate -> size -> stop -> submit
│   └── logger.py              # structured JSON audit log
├── orchestrator/
│   ├── heartbeat.py           # daily job: gather context -> call LLM -> POST signal
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
├── store/                     # queryable index over the logs; writes only its own db
│   ├── schema.py              # the DDL, in one place
│   ├── database.py            # connect_rw / connect_ro (the read-only boundary)
│   ├── loader.py              # idempotent JSONL -> rows; keeps each line verbatim
│   ├── build_db.py            # CLI: python store/build_db.py
│   └── query.py               # CLI: python store/query.py daily
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
│   ├── test_store_loader.py       # idempotence, tolerance, file/db agreement
│   ├── test_store_database.py     # proves the scorer's connection cannot write
│   ├── test_store_query.py        # every canned query parses against the schema
│   ├── test_store_build_db.py     # the build CLI, including --rebuild
│   └── test_llm.py            # schema derivation + every LLM failure mode
└── logs/
    ├── execution_audit.log    # what the engine did      (generated at runtime)
    ├── signal_journal.log     # what the model saw       (generated at runtime)
    └── trading.db             # index over both  (derived; gitignored, rebuildable)
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
told to leave that dimension `null` rather than guess. News is the deliberate
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

**A learned blend of the five scores runs beside the model, in shadow.**
`orchestrator/blend.py` reads `logs/blend_weights.json` once per cycle and
writes a `blend` record on every full-model journal line: the composite, which
dimensions had a score, the weights actually applied and the level they came
from (ticker, instrument kind, global, or equal weights while nothing has been
learned). `BLEND_MODE` is pinned to `shadow` by a CI invariant, so the
composite is recorded next to realised returns and cannot touch a trade until
the walk-forward report has shown it should. The arithmetic lives in
`analysis/blend.py`; the weights file is written by a separate trainer.

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

`.github/workflows/heartbeat.yml` runs one cycle per trading day, shortly after the US open
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

# What a 2x ATR stop and the position caps actually do, over two years of real bars.
python backtest/run_backtest.py AAPL

# Do the three sleeves behave differently under the risk engine?
# Each is replayed under its own cap. Needs no credentials.
python backtest/compare_sleeves.py

# Does every watchlist ticker still exist and trade? ETNs get called and small
# funds delist; a dead symbol fails its ticker every cycle, silently.
python backtest/verify_tickers.py

# What a cycle actually costs, and whether a cheaper model would behave the same.
python replay/compare_models.py --dry-run
python replay/compare_models.py --limit 20
```

[Replay](docs/replay.mdx) is honest because the context was captured live;
a backtest of the *strategy* would not be, since fundamentals and analyst
ratings are current-snapshot only and a SERP query cannot be time-travelled.
[The risk-engine backtest](docs/backtest.mdx) sidesteps that by testing only
the deterministic half -- and reports that its own returns are not an edge.

The backtest needs no credentials and no live cycles, so it is the one piece
of evidence available before the first cycle ever runs.

Cost is measured rather than estimated: every call records its own token counts
in the journal, and [Cost](docs/cost.mdx) compares model and effort settings on
identical recorded context. Output is ~84% of the bill at this prompt shape, so
`EFFORT` moves more money than the model tier does -- and a stronger model
thinking less can undercut a weaker model thinking more.

## Query the archive

The two log files are the record. They are good at being a record and poor at
being asked questions, so `store/` indexes them into SQLite:

```bash
python store/build_db.py           # load both logs (idempotent; run it after a cycle)
python store/query.py daily        # signals, bias split, conviction and cost per day
python store/query.py rejections   # which guardrail bites, and at what conviction
python store/query.py trades       # signals that became real orders, with size and stop
python store/query.py --sql "SELECT ..."
```

**The database is derived, not authoritative.** The JSON-lines files stay the
system of record; `--rebuild` throws the index away and reloads from them in
seconds. That is what makes it safe to add to a system that trades — a corrupt
index costs a rebuild, never a cycle and never a record.

Two things follow. Every row keeps its source line verbatim, so a field nobody
columnised is a query away rather than a migration away:

```sql
SELECT ticker, ROUND(AVG(json_extract(raw, '$.context.technicals.rsi14')), 1) AS mean_rsi
FROM signals GROUP BY ticker;
```

And loading is keyed on a content hash of each line, so re-loading a journal
that grew by one line inserts one row.

The `decisions` view joins each signal to the order it became, on the order id
the journal already records. Nothing here can trade or edit the logs: four CI
invariants hold `store/` to writing its own database, and every SQLite
connection opened from `analysis/` uses the read-only URI. See
[`docs/database.mdx`](docs/database.mdx).

### Push it somewhere that isn't git

```bash
python store/push_remote.py --print-schema   # run once in the Supabase SQL editor
python store/push_remote.py                  # send what the remote is missing
python store/push_remote.py --all            # backfill everything
```

Set `SUPABASE_URL` and `SUPABASE_SERVICE_KEY` to switch it on; leave them unset
and the push says there is no remote and exits 0. The heartbeat runs it as a
step **after** the journal is committed — so a failed push cannot cost a
signal, and the next one catches up on its own, because rows are keyed on the
same content hash and conflicts are ignored on arrival.

Two CI invariants keep it out of the trading path: `orchestrator/` may not
import `store/` (checked by walking the AST), and the Supabase key has exactly
one reader, `store/remote.py`.

The remote tables run with row-level security **on and no policies**, so the
publishable key can do nothing at all — not even read. The service-role key
bypasses RLS and belongs in a GitHub Actions secret. The `decisions` view is
`security_invoker`, without which it would read straight through that RLS.

## Score the signals

```bash
python analysis/score_journal.py              # text report
python analysis/score_journal.py --json       # same figures, machine-readable
python analysis/score_journal.py --db --since 2026-10-01   # from the index
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
| The learned blend cannot influence a trade | `BLEND_MODE` is pinned to `shadow`; CI greps the execution path and the dispatcher for the blend's output and checks that only the journal reads it |
| Enriched context can't reach for a credential | CI greps `context.py` / `technicals.py` / `fundamentals.py` / `analysts.py` for settings and key reads |
| The scorer cannot trade | CI greps `analysis/` for any order path or file write — it grades past decisions and must never be able to make one |
| Prompt injection has a bounded blast radius | Headlines and firm names are third-party text. The system prompt marks the whole context block untrusted, and even a successful injection can only move `bias`/`conviction` — still subject to the conviction floor, the per-instrument cap, the group and sleeve limits, the gross exposure cap, and a mandatory stop |
| Max 5% per single name, 12% per broad fund, 7% per focused (one-sector or one-country) fund, 4% per single-commodity fund | `risk_engine.calculate_position_size()` (checked twice: pre- and post-rounding). The cap comes from `config/instruments.py` via `max_position_pct_for()` — never from the signal, which has no field that could carry an instrument kind. A commodity fund is capped *below* a stock: "fund" does no diversification work when it holds one commodity |
| Max 25% per exposure group | `risk_engine.exposure_group_headroom()` — what stops a diversified watchlist producing a one-bet book. Spans every sleeve, so XOM plus `XLE` plus two energy funds is one energy bet made four times |
| Funds are the core: 70% vs 25% for single names | `risk_engine.sleeve_headroom()` — a deliberate statement that a stock-picking edge is unproven here |
| Max 95% of equity deployed in total | `risk_engine.check_gross_exposure_limit()` — the 5% buffer |
| A winner is sold down in thirds and its stop walked up | `app/position_manager.py` — at +1R sell ⅓ and move the stop to breakeven; at +3R sell ⅓ and move it to +1R; the last third runs. The stop only tightens, and exits go through the broker's close-only endpoint, so nothing here can open a position |
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
2. Conviction below `MIN_CONVICTION` (0.30) → `REJECTED`, before any network I/O.
3. Fetch equity and open positions from Alpaca.
4. New ticker and already at `MAX_OPEN_POSITIONS` → `REJECTED`.
5. Open position in the opposite direction → `REJECTED`.
6. Fetch latest close and 14-day ATR; ATR below `MIN_ATR_PCT_OF_PRICE` → `REJECTED`.
7. Stop = entry ∓ `ATR_STOP_MULTIPLIER` × ATR (long / short).
8. Size = floor((cap × equity − existing exposure) / price), bounded by the tightest of the group, sleeve and gross limits; 0 shares → `REJECTED`. The cap is 5% for a single name, 12% for a broad fund, 7% for a one-sector or one-country fund and 4% for a single-commodity fund, resolved from the ticker.
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
  the way there still scores as a win. The join it needs now exists — the
  `decisions` view carries the size, entry and stop the engine chose — but
  `analysis/returns.py` does not yet walk a filled trade forward bar by bar to
  ask whether the stop was hit first.
- Git still carries the journal. The remote push exists, but the heartbeat
  still commits the JSON-lines files, because they remain the record and the
  runner is discarded. Once the remote has run long enough to be trusted, the
  commit step can rotate or stop — that is the change that actually stops git
  growing, and a remote you have never restored from is not yet a backup.
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
