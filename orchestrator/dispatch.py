"""How a validated signal reaches the execution engine.

Two modes, same guarantee. The boundary that keeps the model away from order
parameters is ``LLMSignal(extra="forbid")`` plus the engine owning all sizing
and stops -- that lives in the schema, not in the network hop. So dispatching
in-process preserves it exactly: a smuggled ``quantity`` is a pydantic
``ValidationError`` instead of an HTTP 422, rejected at the same point for the
same reason.

``direct`` runs the engine in this process. One process, no shared secret, no
port to expose -- which is what makes a scheduled job (GitHub Actions, cron)
a viable host.

``webhook`` POSTs to a separately running FastAPI app. Keep it when the engine
should live on a different machine from the LLM side: then the orchestrator
holds no broker credentials at all, and the shared secret is what stops
anything else on the network from submitting signals.

The trade-off in ``direct`` mode, stated plainly: the orchestrator process
holds Alpaca credentials, so "broker credentials never share a process with
LLM-adjacent code" weakens to "never share a *module*". CI still enforces the
module-level isolation. The practical exposure is unchanged -- the model's
output is a closed schema and cannot reach code execution -- but it is a real
difference, and it is why ``webhook`` remains supported rather than deleted.
"""

from __future__ import annotations

import logging
from typing import Any, Protocol

import httpx

from app.schemas import LLMSignal
from config.settings import get_settings

log = logging.getLogger(__name__)

DIRECT = "direct"
WEBHOOK = "webhook"
VALID_MODES = (DIRECT, WEBHOOK)


class Dispatcher(Protocol):
    """Delivers a signal to the engine and reports what it decided."""

    def dispatch(self, signal: LLMSignal) -> dict: ...

    def is_market_open(self) -> bool: ...

    def manage_positions(self) -> dict: ...


class DirectDispatcher:
    """Calls the execution engine in this process."""

    def __init__(self, engine: Any | None = None) -> None:
        self._engine = engine

    def _get_engine(self) -> Any:
        # Built on first use, not at construction: importing the orchestrator
        # must never require Alpaca credentials, the same way importing
        # ``app.main`` does not.
        if self._engine is None:
            from app.broker_client import AlpacaPaperBroker
            from app.execution_engine import ExecutionEngine
            from app.market_data import YFinanceMarketData

            self._engine = ExecutionEngine(
                broker=AlpacaPaperBroker(), market_data=YFinanceMarketData()
            )
        return self._engine

    def is_market_open(self) -> bool:
        return bool(self._get_engine().broker.is_market_open())

    def manage_positions(self) -> dict:
        # Same broker and feed the engine uses, so a tranche is priced off
        # the quote a new entry would be.
        from app.position_manager import PositionManager

        engine = self._get_engine()
        return PositionManager(engine.broker, engine.market_data).manage().as_dict()

    def dispatch(self, signal: LLMSignal) -> dict:
        result = self._get_engine().execute(signal)
        # Shaped like the webhook outcome so the journal records one format
        # regardless of how the signal was delivered -- otherwise the scorer
        # would have to learn two schemas for the same decision.
        return {
            "mode": DIRECT,
            "status": result.status.value,
            "reason": result.reason,
            "quantity": result.quantity,
            "order_id": result.order_id,
        }


class WebhookDispatcher:
    """POSTs to a separately running execution engine."""

    def __init__(self, client: httpx.Client | None = None) -> None:
        self._client = client

    def is_market_open(self) -> bool:
        # No broker here by design, so there is nothing authoritative to ask.
        # Returning True means the cycle proceeds and the engine's own
        # market-hours gate makes the call -- correct, just not free.
        return True

    def manage_positions(self) -> dict:
        settings = get_settings()
        headers = {"x-webhook-secret": settings.webhook_shared_secret}
        url = manage_url(settings.webhook_url)
        if self._client is None:
            with httpx.Client(timeout=60.0) as client:
                response = client.post(url, headers=headers)
        else:
            response = self._client.post(url, headers=headers)
        if response.status_code != 200:
            return {"error": f"HTTP {response.status_code}", "body": response.text[:500]}
        try:
            body = response.json()
        except ValueError:
            return {"error": "non-JSON body", "body": response.text[:500]}
        return body if isinstance(body, dict) else {"error": "unexpected body", "body": body}

    def dispatch(self, signal: LLMSignal) -> dict:
        settings = get_settings()
        headers = {"x-webhook-secret": settings.webhook_shared_secret}
        body = signal.model_dump(mode="json")
        if self._client is None:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(settings.webhook_url, json=body, headers=headers)
        else:
            response = self._client.post(settings.webhook_url, json=body, headers=headers)
        return _webhook_outcome(response)


def manage_url(signal_url: str) -> str:
    """The management endpoint, beside the signal one.

    ``.../webhook/signal`` -> ``.../webhook/positions/manage``. Derived rather
    than a second setting, so the two cannot point at different engines.
    """
    base = signal_url.rstrip("/")
    if base.endswith("/signal"):
        base = base[: -len("/signal")]
    return f"{base}/positions/manage"


def _webhook_outcome(response: httpx.Response) -> dict:
    """The engine's verdict, for the journal. Body may not be JSON on an error."""
    outcome: dict = {"mode": WEBHOOK, "http_status": response.status_code}
    try:
        body = response.json()
    except ValueError:
        outcome["body"] = response.text[:500]
        return outcome
    if isinstance(body, dict):
        outcome.update({key: body.get(key) for key in ("status", "reason", "quantity", "order_id")})
    else:
        outcome["body"] = body
    return outcome


def build_dispatcher(mode: str = "") -> Dispatcher:
    """The dispatcher named by ``EXECUTION_MODE``; direct unless told otherwise."""
    resolved = (mode or get_settings().execution_mode or DIRECT).strip().lower()
    if resolved not in VALID_MODES:
        raise ValueError(
            f"EXECUTION_MODE must be one of {', '.join(VALID_MODES)}, got {resolved!r}"
        )
    return DirectDispatcher() if resolved == DIRECT else WebhookDispatcher()


__all__ = [
    "manage_url",
    "DIRECT",
    "WEBHOOK",
    "VALID_MODES",
    "Dispatcher",
    "DirectDispatcher",
    "WebhookDispatcher",
    "build_dispatcher",
]
