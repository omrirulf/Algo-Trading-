"""Pydantic models that form the contract between the LLM and the risk engine.

``LLMSignal`` is the *only* thing the LLM is allowed to say. Its
``extra="forbid"`` config is the structural guardrail: any attempt to smuggle
``quantity``, ``price``, ``stop_price``, ``order_type`` etc. into the payload
fails validation (HTTP 422) before a single line of execution logic runs.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


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
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
