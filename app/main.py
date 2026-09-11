"""FastAPI entry point exposing the single ``POST /webhook/signal`` endpoint.

Request validation is done by FastAPI/pydantic against ``LLMSignal``. Because
that model forbids extra fields, a payload carrying ``quantity``, ``price``
or any other order parameter is answered with HTTP 422 and never reaches
``ExecutionEngine``.
"""

from __future__ import annotations

import hmac
import logging
from functools import lru_cache
from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, status

from app.execution_engine import ExecutionEngine
from app.schemas import ExecutionResult, LLMSignal
from config.settings import get_settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

app = FastAPI(
    title="Deterministic Execution Engine",
    description="Accepts LLM sentiment signals; owns all sizing, stops and execution.",
    version="1.0.0",
)


@lru_cache(maxsize=1)
def get_engine() -> ExecutionEngine:
    """Build the production engine lazily (first request), so importing the
    app for tests never touches Alpaca or yfinance."""
    from app.broker_client import AlpacaPaperBroker
    from app.market_data import YFinanceMarketData

    return ExecutionEngine(broker=AlpacaPaperBroker(), market_data=YFinanceMarketData())


def require_webhook_secret(
    x_webhook_secret: Annotated[str | None, Header()] = None,
) -> None:
    expected = get_settings().webhook_shared_secret
    if not expected:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="WEBHOOK_SHARED_SECRET is not configured on the server",
        )
    if x_webhook_secret is None or not hmac.compare_digest(x_webhook_secret, expected):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid webhook secret")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/webhook/signal",
    response_model=ExecutionResult,
    dependencies=[Depends(require_webhook_secret)],
)
def receive_signal(
    signal: LLMSignal,
    engine: Annotated[ExecutionEngine, Depends(get_engine)],
) -> ExecutionResult:
    return engine.execute(signal)
