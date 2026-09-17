"""Pydantic models that form the contract between the LLM and the risk engine.

``LLMSignal`` is the *only* thing the LLM is allowed to say. Its
``extra="forbid"`` config is the structural guardrail: any attempt to smuggle
``quantity``, ``price``, ``stop_price``, ``order_type`` etc. into the payload
fails validation (HTTP 422) before a single line of execution logic runs.

The per-dimension scores and ``key_factors`` are **inert**. They exist so that
a decision can be audited after the fact -- which input actually drove the
call, and were the confident calls the ones that paid? -- and nothing in
``execution_engine`` or ``risk_engine`` reads them. Only ``bias`` and
``conviction`` reach the decision path, and a CI invariant check enforces that.
Widening what the LLM may say is only safe while the extra words stay inert.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, field_validator

#: A single driver of the call: one short, standalone, factual phrase.
KeyFactor = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=1, max_length=200)
]

MAX_KEY_FACTORS = 6

_SCORE_SCALE = (
    "in [-1.0, 1.0], where -1.0 is maximally bearish, 0.0 is neutral and +1.0 is "
    "maximally bullish; null when the data for it was unavailable"
)


class Bias(str, Enum):
    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    NEUTRAL = "NEUTRAL"


class LLMSignal(BaseModel):
    """The complete, closed set of fields an LLM may emit."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    ticker: str = Field(
        ...,
        min_length=1,
        max_length=10,
        pattern=r"^[A-Za-z][A-Za-z0-9.\-]{0,9}$",
        description="Exchange ticker symbol, e.g. AAPL or BRK.B",
    )
    bias: Bias
    conviction: float = Field(..., ge=0.0, le=1.0)
    rationale: str = Field(..., min_length=1, max_length=2000)

    # --- Transparency only. Never read by the risk engine. --- #
    news_score: Optional[float] = Field(
        None, ge=-1.0, le=1.0, description=f"Read on the recent news {_SCORE_SCALE}"
    )
    technical_score: Optional[float] = Field(
        None, ge=-1.0, le=1.0, description=f"Read on trend, momentum and volatility {_SCORE_SCALE}"
    )
    fundamental_score: Optional[float] = Field(
        None, ge=-1.0, le=1.0, description=f"Read on valuation, growth and balance sheet {_SCORE_SCALE}"
    )
    analyst_score: Optional[float] = Field(
        None,
        ge=-1.0,
        le=1.0,
        description=f"Read on analyst consensus, targets and ownership {_SCORE_SCALE}",
    )
    insider_score: Optional[float] = Field(
        None,
        ge=-1.0,
        le=1.0,
        description=f"Read on insider buying and selling {_SCORE_SCALE}",
    )
    key_factors: list[KeyFactor] = Field(
        default_factory=list,
        max_length=MAX_KEY_FACTORS,
        description=(
            "The specific facts that drove this call, each a short standalone phrase "
            "citing the datum rather than restating the conclusion"
        ),
    )

    @field_validator("ticker")
    @classmethod
    def _upper(cls, v: str) -> str:
        return v.upper()


class ExecutionStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    ERROR = "ERROR"


class ExecutionResult(BaseModel):
    """What the risk engine decided and (if accepted) what it submitted."""

    status: ExecutionStatus
    ticker: str
    bias: Bias
    conviction: float
    reason: str
    quantity: Optional[int] = None
    side: Optional[str] = None
    entry_price: Optional[float] = None
    stop_price: Optional[float] = None
    atr: Optional[float] = None
    order_id: Optional[str] = None
    #: Account equity the decision was sized against, once the engine has
    #: read it. ``None`` for a signal refused before the account was
    #: consulted (NEUTRAL, closed market, conviction floor). Recorded so the
    #: audit log says what the book was worth at every decision, not only
    #: what was traded -- the number a return has to be measured against.
    equity: Optional[float] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
