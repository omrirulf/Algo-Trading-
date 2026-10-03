"""The shadow universe's own news search: company name plus ticker. Shadow only.

Why (the owner's decision of 3 Oct 2026). Production searches Google News for
``"<ticker> stock"`` (``orchestrator/news.py``). A news check that day showed
that for short tickers this finds other things: "SO stock", "C stock" and
"D stock" found no headline about Southern Company, Citigroup or Dominion.
The owner kept those names and had the query fixed instead, for the universe
only: ``"Southern Company SO stock"`` (``config.shadow_universe.news_query``).
Production's query, and every line of ``orchestrator/news.py``, is unchanged:
it feeds the main race.

The same request otherwise. The URL keeps every other parameter production
sends (Google News, the same look-back, the same number of results, US
English, parsed JSON), and the request goes through production's own
provider class -- the same zone, the same retries, the same parser, the same
per-thread request count the universe's cost cap reads. Only the ``q`` differs.

No credential is read here. The provider is built with empty arguments and
finds its key and zone itself, in ``orchestrator/news.py`` (Bright Data's own
environment variables, which the universe's workflow sets from the same
secret and zone production uses). A CI guardrail keeps credential reads out
of every orchestrator module but a few, and this is not one of them.

``build_context`` is ``heartbeat.build_context`` with this search in place
of production's: the same sections, and a failed search is the same explicit
news gap, never the name's whole day.
"""

from __future__ import annotations

import logging
from urllib.parse import urlencode

from config import shadow_universe as su
from orchestrator import context
from orchestrator.context import TickerContext
from orchestrator.news import (
    MAX_HEADLINES,
    NEWS_LOOKBACK,
    BrightDataNewsProvider,
    Headline,
    NewsFetchError,
)

log = logging.getLogger(__name__)

#: The zone ``brightdata login`` creates, when the workflow names none (the
#: same fallback as production's settings).
DEFAULT_ZONE = "cli_unlocker"


def search_url(ticker: str) -> str:
    """Google News URL for one universe name: production's parameters, the universe's query."""
    params = {
        "q": su.news_query(ticker),
        "tbm": "nws",
        "tbs": f"qdr:{NEWS_LOOKBACK}",
        "num": MAX_HEADLINES,
        "hl": "en",
        "gl": "us",
        "brd_json": 1,
    }
    return f"https://www.google.com/search?{urlencode(params)}"


class UniverseNewsProvider(BrightDataNewsProvider):
    """Production's provider, asking the universe's query."""

    def fetch_items(self, ticker: str) -> list[Headline]:
        return self._fetch_items(search_url(ticker))


def fetch(ticker: str) -> list[Headline]:
    """The past day's headlines for one universe name. Raises ``NewsFetchError`` like production."""
    return UniverseNewsProvider("", "", unlocker_zone=DEFAULT_ZONE).fetch_items(ticker)


def build_context(ticker: str) -> TickerContext:
    """``heartbeat.build_context`` with the universe's search: never raises for want of news."""
    try:
        headlines = fetch(ticker)
    except NewsFetchError as exc:
        log.warning("%s: news unavailable, continuing on the other sections (%s)", ticker, exc)
        return context.gather(
            ticker, [], news_gap=f"{context.NEWS_GAP_PREFIX}: {exc}",
        )
    return context.gather(ticker, headlines)


__all__ = ["DEFAULT_ZONE", "UniverseNewsProvider", "build_context", "fetch", "search_url"]
