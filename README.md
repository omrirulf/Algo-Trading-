# Hybrid LLM/Deterministic Trading System

[![CI](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml/badge.svg)](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml)

Qualitative LLM analysis is fully decoupled from trade execution. The LLM can
only ever emit a closed set of fields — a direction, a confidence, and its
reasoning — and only `bias` and `conviction` are ever acted on. A FastAPI
webhook validates that shape (rejecting anything else with a 422), and a
pure-Python risk engine does 100% of the sizing, stop-loss, and Alpaca
paper-trade execution.

Each hourly cycle gives the model four kinds of context per ticker — recent
news, technicals, fundamentals, and the analyst/institutional view — and
records all of it alongside the resulting signal so the signals can be graded
later.

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
│   ├── formatting.py          # number formatting; missing values render as "n/a"
│   ├── journal.py             # per-cycle record of context + signal + outcome
│   └── llm.py                 # Claude call, constrained by the signal schema
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
│   ├── test_context.py        # assembly and every degradation path
│   ├── test_journal.py        # the journal records context, signal and failures
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

### News feed (Bright Data)

The orchestrator pulls the last 24 hours of Google News headlines for each
watchlist ticker through [Bright Data's SERP API](https://brightdata.com/products/serp-api).

1. In the Bright Data dashboard create a zone of type **SERP API** (the
   default name is `serp_api`; if you pick another, set `BRIGHTDATA_SERP_ZONE`).
2. Copy an API token from *Account settings -> API tokens* into
   `BRIGHTDATA_API_TOKEN`.

Each cycle sends one request per ticker, so the default three-ticker
watchlist costs 72 SERP requests a day. Bright Data's own free tier /
pay-as-you-go pricing covers that comfortably; check your zone's usage page
after the first day. If the token is missing the cycle logs an error for
each ticker and sends nothing.

### Market context (yfinance — no API key)

Headlines alone say that something happened, not whether it landed on a cheap
business or an expensive one, on an uptrend or a breakdown, or on a name the
street already loves. Before building the prompt, `orchestrator/context.py`
adds three more dimensions, all from yfinance, which is unauthenticated — **no
new key, no new per-request cost:**

| Source | What goes into the prompt |
|---|---|
| `technicals.py` | 20/50/200-day SMAs and distance from each, Wilder RSI(14), MACD(12/26/9), 1d/5d/1m/3m returns, 52-week range position, ATR(14) as % of price, annualised 20-day vol, volume vs its 20-day average |
| `fundamentals.py` | Sector, market cap, trailing/forward P/E, P/B, PEG, profit and operating margins, ROE, YoY revenue and earnings growth, debt/equity, free cash flow, beta, short interest, next earnings date |
| `analysts.py` | Consensus rating and 1-to-5 mean, full rating breakdown, mean/high/low price targets and implied upside, recent upgrades and downgrades by firm, institutional ownership and largest holders |

The ATR comes from `app.market_data.calculate_atr` — the same function the
risk engine will use to place the stop, not a second implementation that could
drift from it.

**Failures degrade rather than propagate.** Every source is fetched
independently; a failure records a named gap in the prompt and the model is
told to score that dimension `0.0` rather than guess. News is the deliberate
exception: if Bright Data is down the ticker is skipped entirely, because
trading on technicals alone would quietly be a different strategy.

Slow-moving data (fundamentals, ratings, ownership) is cached for six hours
per ticker; price history is refetched every cycle.

### Analyst (Claude)

Put an API key from [the Anthropic Console](https://console.anthropic.com)
in `ANTHROPIC_API_KEY`. The orchestrator sends each ticker's assembled context
to `claude-opus-5` and gets back one signal per ticker.

The system prompt weights the four inputs differently — news is fast and
noisy, technicals are about timing rather than business quality, fundamentals
rarely change a view within an hour, and the analyst view is a prior already
in the price unless it just moved. It is also explicit about the failure mode
that richer context introduces:

> More context does not mean more conviction. Conviction is earned when
> independent dimensions agree, and it must fall when they conflict.

Alongside `bias`, `conviction` and `rationale`, the model reports a score in
`[-1, 1]` for each of the four dimensions plus up to six `key_factors`. These
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

```bash
# Terminal 1: the deterministic execution engine
uvicorn app.main:app --reload --port 8000

# Terminal 2: the orchestrator
python orchestrator/heartbeat.py
```

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
- `logs/signal_journal.log` now records the full context behind every signal,
  but **nothing reads it back yet**. The next real step is a scoring script:
  join each journalled signal to the realised forward return and check whether
  high-conviction calls actually outperformed low-conviction ones, and which
  of the four dimension scores carries any information at all.
- The prompt asks the model to calibrate conviction and not to inflate it as
  context grows, but nothing enforces that. Watch the journalled conviction
  distribution: if it drifts toward always answering 0.9, the conviction floor
  stops filtering anything.
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
