"""Hourly job: fetch news -> ask the LLM for a signal -> POST it to the engine.

This process knows nothing about position sizing, stops, or the broker. It
has no Alpaca keys. All it can do is send ``{ticker, bias, conviction,
rationale}`` to the webhook, and the webhook will 422 anything else.

Two integration points are left as stubs (``fetch_news`` and ``call_llm``)
because they depend on which providers you use. When wiring ``call_llm``,
use your LLM provider's structured-output / tool-use mode with
``SIGNAL_JSON_SCHEMA`` so the model is constrained at generation time.
"""

from __future__ import annotations

import json
import logging
import sys
from pathlib import Path

# Allow ``python orchestrator/heartbeat.py`` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402
from apscheduler.schedulers.blocking import BlockingScheduler  # noqa: E402
from pydantic import ValidationError  # noqa: E402

from app.schemas import LLMSignal  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.settings import get_settings  # noqa: E402

log = logging.getLogger("heartbeat")

#: JSON schema the LLM must conform to. Derived from the same pydantic model
#: the webhook validates against, so the two can never drift apart.
SIGNAL_JSON_SCHEMA: dict = LLMSignal.model_json_schema()

SYSTEM_PROMPT = (
    "You are a sell-side equity analyst. Given recent news about a ticker, "
    "output ONLY a JSON object matching the provided schema with fields "
    "ticker, bias (BULLISH|BEARISH|NEUTRAL), conviction (0.0-1.0) and a short "
    "rationale. Do not include any other fields. You do not decide position "
    "size, price, or order type; a separate risk system does."
)


# --------------------------------------------------------------------------- #
# Provider stubs
# --------------------------------------------------------------------------- #


def fetch_news(ticker: str) -> list[str]:
    """Return recent headlines / snippets for ``ticker``.

    Wire this to your news provider (e.g. an RSS feed, NewsAPI, Alpaca News).
    """
    raise NotImplementedError("fetch_news(): connect a news provider")


def call_llm(system_prompt: str, user_prompt: str, json_schema: dict) -> str:
    """Return the LLM's raw JSON string for the given prompts.

    Use your provider's structured-output / tool-use mode and pass
    ``json_schema`` so the response is constrained to the signal shape.
    """
    raise NotImplementedError("call_llm(): connect an LLM provider")


# --------------------------------------------------------------------------- #
# Pipeline
# --------------------------------------------------------------------------- #


def build_user_prompt(ticker: str, headlines: list[str]) -> str:
    joined = "\n".join(f"- {h}" for h in headlines) or "- (no recent news)"
    return f"Ticker: {ticker}\nRecent news:\n{joined}\n\nRespond with the JSON signal."


def parse_signal(raw_json: str) -> LLMSignal:
    """Parse and validate the LLM output locally before sending it anywhere.

    The webhook re-validates on receipt; this is defence in depth and gives
    a clearer error message at the source.
    """
    return LLMSignal.model_validate(json.loads(raw_json))


def post_signal(signal: LLMSignal, client: httpx.Client | None = None) -> httpx.Response:
    settings = get_settings()
    headers = {"x-webhook-secret": settings.webhook_shared_secret}
    body = signal.model_dump(mode="json")
    if client is None:
        with httpx.Client(timeout=30.0) as c:
            return c.post(settings.webhook_url, json=body, headers=headers)
    return client.post(settings.webhook_url, json=body, headers=headers)


def process_ticker(ticker: str) -> None:
    try:
        headlines = fetch_news(ticker)
        raw = call_llm(SYSTEM_PROMPT, build_user_prompt(ticker, headlines), SIGNAL_JSON_SCHEMA)
        signal = parse_signal(raw)
    except NotImplementedError as exc:
        log.error("%s: %s", ticker, exc)
        return
    except (json.JSONDecodeError, ValidationError) as exc:
        log.error("%s: LLM output rejected before sending: %s", ticker, exc)
        return
    except Exception:  # noqa: BLE001
        log.exception("%s: failed to produce a signal", ticker)
        return

    if signal.ticker != ticker:
        log.error("%s: LLM answered for %s instead; dropping", ticker, signal.ticker)
        return

    try:
        resp = post_signal(signal)
    except httpx.HTTPError as exc:
        log.error("%s: webhook unreachable: %s", ticker, exc)
        return
    log.info("%s -> HTTP %s %s", ticker, resp.status_code, resp.text[:300])


def run_cycle() -> None:
    tickers = get_settings().watchlist_tickers
    log.info("heartbeat cycle start: %s", tickers)
    for ticker in tickers:
        process_ticker(ticker)
    log.info("heartbeat cycle end")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    scheduler = BlockingScheduler()
    scheduler.add_job(
        run_cycle,
        "interval",
        minutes=cfg.HEARTBEAT_INTERVAL_MINUTES,
        id="heartbeat",
        max_instances=1,
        coalesce=True,
    )
    log.info("running first cycle now, then every %d minutes", cfg.HEARTBEAT_INTERVAL_MINUTES)
    run_cycle()
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        log.info("heartbeat stopped")


if __name__ == "__main__":
    main()
