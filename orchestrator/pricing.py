"""What a call actually cost, from the token counts the API reports.

Cost was an estimate in this project until now -- a guess at output length
multiplied by a list price. The guess drove a real decision (how many tickers
to watch), which is the wrong way round. Everything here works from
``response.usage``, so the number in the journal is measured.

Prices are list prices per million tokens, current as of 2026-06. They are a
constant rather than a lookup because a silent price change should show up as
a diff, and because there is no pricing endpoint to ask.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final, Optional
from config import settings as cfg

#: A cache read bills at roughly a tenth of the input rate, a cache write at
#: about 1.25x. Documented multipliers rather than separately published
#: per-model rates, so treat a cache-heavy estimate as approximate.
CACHE_READ_MULTIPLIER: Final[float] = 0.1
CACHE_WRITE_MULTIPLIER: Final[float] = 1.25


@dataclass(frozen=True)
class Price:
    """List price per million tokens."""

    input_per_mtok: float
    output_per_mtok: float

    @property
    def cache_read_per_mtok(self) -> float:
        return self.input_per_mtok * CACHE_READ_MULTIPLIER

    @property
    def cache_write_per_mtok(self) -> float:
        return self.input_per_mtok * CACHE_WRITE_MULTIPLIER


#: Only the models this project would plausibly run. An unknown model costs
#: ``None`` rather than zero -- see ``cost_usd``.
PRICES: Final[dict[str, Price]] = {
    "claude-opus-5": Price(5.00, 25.00),
    "claude-sonnet-5": Price(2.00, 10.00),
    "claude-haiku-4-5": Price(1.00, 5.00),
}


@dataclass(frozen=True)
class Usage:
    """Token counts for one call, as the API reported them."""

    model: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_input_tokens: int = 0
    cache_creation_input_tokens: int = 0

    def as_dict(self) -> dict:
        return {
            "model": self.model,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "cache_read_input_tokens": self.cache_read_input_tokens,
            "cache_creation_input_tokens": self.cache_creation_input_tokens,
            "cost_usd": self.cost_usd,
        }

    @property
    def cost_usd(self) -> Optional[float]:
        return cost_usd(self)

    @property
    def output_share(self) -> Optional[float]:
        """Output's share of the bill.

        The cost guide's round-0 diagnostic: an output-heavy workload is one
        where lowering effort is the strongest lever, because thinking tokens
        bill at the output rate. Reported rather than assumed.
        """
        cost = self.cost_usd
        if not cost:
            return None
        price = PRICES.get(self.model)
        if price is None:
            return None
        return (self.output_tokens * price.output_per_mtok / 1e6) / cost


def cost_usd(usage: Usage) -> Optional[float]:
    """Dollars for one call, or ``None`` when the model's price is unknown.

    ``None`` rather than 0.0 on an unknown model: a zero would quietly read as
    "this was free" and would sum into a total that understates the bill.
    """
    price = PRICES.get(usage.model)
    if price is None:
        return None
    return (
        usage.input_tokens * price.input_per_mtok
        + usage.output_tokens * price.output_per_mtok
        + usage.cache_read_input_tokens * price.cache_read_per_mtok
        + usage.cache_creation_input_tokens * price.cache_write_per_mtok
    ) / 1e6


def usage_from_response(response: object, model: str = "") -> Usage:
    """Pull token counts off an SDK response, tolerating a missing field.

    Never raises: a usage block that has moved or gained a field must not take
    down the cycle that produced a perfectly good signal.
    """
    raw = getattr(response, "usage", None)
    if raw is None:
        return Usage(model=model)

    def count(name: str) -> int:
        value = getattr(raw, name, 0)
        return int(value) if isinstance(value, (int, float)) else 0

    return Usage(
        model=getattr(response, "model", "") or model,
        input_tokens=count("input_tokens"),
        output_tokens=count("output_tokens"),
        cache_read_input_tokens=count("cache_read_input_tokens"),
        cache_creation_input_tokens=count("cache_creation_input_tokens"),
    )


def monthly_usd(
    per_call_usd: float, tickers: int, cycles_per_day: int = cfg.CYCLES_PER_TRADING_DAY, trading_days: int = 21
) -> float:
    """Scale one measured call up to a monthly bill."""
    return per_call_usd * tickers * cycles_per_day * trading_days


__all__ = [
    "CACHE_READ_MULTIPLIER",
    "CACHE_WRITE_MULTIPLIER",
    "PRICES",
    "Price",
    "Usage",
    "cost_usd",
    "usage_from_response",
    "monthly_usd",
]
