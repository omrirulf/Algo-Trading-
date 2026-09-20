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
#:
#: The two non-Claude rows are the documented screening endpoints. They are
#: here because a hosted API with a published price list is not the "someone
#: else's hardware" case ``OpenAICompatibleProvider`` leaves unpriced: we do
#: know what these cost, and without a row the whole screening stage prices as
#: ``None`` and drops out of the measured bill -- the same silent hole that
#: made the first 80-ticker cycle report $0.00 for 114 screening calls.
#:
#: A self-hosted endpoint still has no row, still costs ``None``, and that is
#: still the honest answer.
PRICES: Final[dict[str, Price]] = {
    "claude-opus-5": Price(5.00, 25.00),
    "claude-sonnet-5": Price(2.00, 10.00),
    "claude-haiku-4-5": Price(1.00, 5.00),
    # Screening endpoints. Verified 20 Sep 2026 against the providers' public
    # pricing; re-check before trusting a cost report months from now.
    #
    # A row is keyed by model name, but an open-weight model's price belongs to
    # whoever serves it: gpt-oss-20b is $0.03/$0.14 on DeepInfra and
    # $0.075/$0.30 on Groq, and the journal records only the name. The row
    # below is DeepInfra's, because Groq's paid tier is closed to new signups
    # ("Developer tier upgrades are temporarily unavailable"), which makes
    # DeepInfra the host this model is actually reachable through. Serving it
    # somewhere else makes this row wrong -- by a factor of about 2.4 for Groq
    # -- and nothing detects that, so change it when you change host.
    "gemini-3.5-flash-lite": Price(0.30, 2.50),
    "openai/gpt-oss-20b": Price(0.03, 0.14),
    # A full-model candidate rather than a screening one, so it is priced
    # here for the same reason: an unpriced row makes the stage it answers
    # vanish from the measured bill. Sources disagreed on 20 Sep 2026 --
    # $0.05/$0.45 and $0.04/$0.17 were both published for DeepInfra -- and
    # the dearer pair is used, because understating what a replacement costs
    # is the error that argues for making the swap.
    "openai/gpt-oss-120b": Price(0.05, 0.45),
}

#: The cache multipliers above are Anthropic's. Gemini's cache read happens to
#: be the same 0.1x, Groq's is 0.5x, and neither is exercised today: the
#: OpenAI-compatible path sends no ``cache_control`` and records no cache
#: token counts, so those fields are zero on every non-Claude row and the
#: multiplier never applies. Sending cache hints on that path would make this
#: comment wrong before it made the bill smaller.


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
        price = price_for(self.model)
        if price is None:
            return None
        return (self.output_tokens * price.output_per_mtok / 1e6) / cost


def price_for(model: str) -> Optional[Price]:
    """The price row for a model id, tolerating the API's dated form.

    ``MODEL`` and ``SCREENING_MODEL`` are configured as aliases
    (``claude-haiku-4-5``), but the API answers with the snapshot it actually
    ran (``claude-haiku-4-5-20251001``) and that is what the journal records.
    An exact-match lookup therefore priced **every screening call at
    ``None``** -- which, by the honest-``None`` rule below, silently dropped
    the entire first stage of the funnel out of the measured bill. The first
    80-ticker cycle recorded 114 screening calls and $0.00 for them.

    Matching is by longest alias prefix, so a dated snapshot prices as its
    family and a genuinely unknown model still returns ``None`` rather than
    borrowing a neighbour's price.
    """
    price = PRICES.get(model)
    if price is not None:
        return price
    candidates = [k for k in PRICES if model.startswith(f"{k}-")]
    if not candidates:
        return None
    return PRICES[max(candidates, key=len)]


def cost_usd(usage: Usage) -> Optional[float]:
    """Dollars for one call, or ``None`` when the model's price is unknown.

    ``None`` rather than 0.0 on an unknown model: a zero would quietly read as
    "this was free" and would sum into a total that understates the bill.
    """
    price = price_for(usage.model)
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


def cycles_per_trading_day() -> int:
    """The heartbeat's cadence, read at call time.

    A module-level ``from config import settings`` here forms a cycle --
    settings imports watchlist, which imports this module for PRICES -- that
    only fails when *this* module is imported first. Resolving lazily keeps
    the single source of truth without the import-order landmine.
    """
    from config import settings as cfg

    return cfg.CYCLES_PER_TRADING_DAY


def monthly_usd(
    per_call_usd: float,
    tickers: int,
    cycles_per_day: Optional[int] = None,
    trading_days: int = 21,
) -> float:
    """Scale one measured call up to a monthly bill."""
    if cycles_per_day is None:
        cycles_per_day = cycles_per_trading_day()
    return per_call_usd * tickers * cycles_per_day * trading_days


__all__ = [
    "CACHE_READ_MULTIPLIER",
    "CACHE_WRITE_MULTIPLIER",
    "PRICES",
    "Price",
    "Usage",
    "cost_usd",
    "price_for",
    "usage_from_response",
    "monthly_usd",
    "cycles_per_trading_day",
]
