# Hybrid LLM/Deterministic Trading System

[![CI](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml/badge.svg)](https://github.com/omrirulf/Algo-Trading-/actions/workflows/ci.yml)

Qualitative LLM analysis is fully decoupled from trade execution. The LLM
can only ever emit `{ticker, bias, conviction, rationale}`; a FastAPI
webhook validates that shape (rejecting anything else with a 422), and a
pure-Python risk engine does 100% of the sizing, stop-loss, and Alpaca
paper-trade execution.

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
│   ├── heartbeat.py           # hourly job: fetch news -> call LLM -> POST signal
│   ├── news.py                # Bright Data SERP API (Google News) headline fetch
│   └── llm.py                 # Claude call, constrained by the signal schema
├── tests/
│   ├── conftest.py            # FakeBroker / FakeMarketData; no network in tests
│   ├── test_risk_engine.py    # proves the 5% cap and ATR stop math hold
│   ├── test_schemas.py        # proves the LLM cannot smuggle qty/price fields
│   ├── test_market_data.py    # Wilder ATR against a reference implementation
│   ├── test_execution_engine.py  # full decision path with fakes
│   ├── test_webhook.py        # auth + 422 at the HTTP layer
│   ├── test_heartbeat.py      # orchestrator can only send the closed shape
│   ├── test_news.py           # Bright Data request shape + response parsing
│   └── test_llm.py            # schema derivation + every LLM failure mode
└── logs/
    └── execution_audit.log    # generated at runtime
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

### Analyst (Claude)

Put an API key from [the Anthropic Console](https://console.anthropic.com)
in `ANTHROPIC_API_KEY`. The orchestrator sends each ticker's headlines to
`claude-opus-5` and gets back one `{ticker, bias, conviction, rationale}`
object per ticker.

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
  environment directly; and no `.env` is tracked in git.

Each invariant check was verified to fail when its invariant is broken, so a
green run means something.

## Notes / next steps for production

- Swap the webhook's shared-secret header for HMAC request signing.
- `orchestrator/news.py` searches Google News for `"<TICKER> stock"`. For
  tickers whose symbol is a common word, or to include the company name,
  adjust `build_news_search_url()`.
- Nothing measures whether the signals are any good. Before trusting the
  conviction numbers, log a few weeks of paper decisions and check whether
  high-conviction calls actually outperformed low-conviction ones.
- The prompt asks the model to calibrate conviction, but nothing enforces
  that. If it drifts toward always answering 0.9, the conviction floor stops
  filtering anything.
- Consider persisting `ExecutionResult` rows to a database in addition to
  the log file, for querying trade history.
- `TradingClient(..., paper=True)` is hard-coded in `broker_client.py` —
  removing that safety requires an explicit code change, not an env flag,
  so a misconfigured `.env` can't accidentally go live.
- The engine does not currently close or reduce positions; the attached
  stop is the only exit. Add an explicit exit path before relying on
  `BEARISH` signals to unwind longs.
