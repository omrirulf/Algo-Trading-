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

Two at a time, four tries (the owner's decision of 6 Oct 2026). Bright Data
throttled the news check of 5 Oct 2026 (an empty body with its 200, or "auto-
throttled") while it asked several names at once. So the universe, whose
calls run four names at a time, lets at most two of them search the news at
once (``NEWS_AT_ONCE``), and a search that fails is asked again, up to four
times in all (``TRIES``), a minute apart (``TRY_PAUSE_SECONDS``, outside the
two-at-a-time limit). One try is one ``fetch``: production's provider, whose
own one retry after an empty body or a broken connection is unchanged. A
missing key or zone is not tried again: it is the same every time.
"Two at a time" is read as the news searches: only they are two at a time;
the model calls stay four names at a time, because the whole name two at a
time (251 names x ~196 s / 2) would take about 7 hours, past
``RUN_BUDGET_SECONDS`` (240 min) and GitHub's 6-hour job limit.
``news_step`` asks every name that way and nothing else -- no model, no
journal -- to see how many get no answer (the owner asked for one full run in
the week of 14 Dec 2026).
"""

from __future__ import annotations

import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Final, Iterable, Optional
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


#: At most this many universe names search the news at once: the owner's "two at a time" (6 Oct 2026),
#: applied to the news searches only (the model calls stay four at a time; see the module docstring).
NEWS_AT_ONCE: Final[int] = 2
#: A name's search is asked up to this many times in all (the owner: "up to four tries per name").
TRIES: Final[int] = 4
#: The pause between two tries of one name (the check of 5 Oct 2026 waited a minute between rounds).
TRY_PAUSE_SECONDS: Final[float] = 60.0
#: The provider's own words for a missing key or zone: the same on every try, so never tried again.
NOT_RETRIED: Final[tuple[str, ...]] = ("No Bright Data credentials", "No Bright Data zone")

_AT_ONCE = threading.BoundedSemaphore(NEWS_AT_ONCE)


def fetch_with_tries(ticker: str, *, tries: int = TRIES, pause: float = TRY_PAUSE_SECONDS,
                     sleep: Optional[Callable[[float], None]] = None) -> list[Headline]:
    """``fetch``, with at most ``NEWS_AT_ONCE`` names searching at once, a failed search asked up to ``tries`` times.

    Raises ``NewsFetchError`` after the last try, saying how many there were.
    """
    sleep = time.sleep if sleep is None else sleep
    failure: Optional[NewsFetchError] = None
    for attempt in range(1, tries + 1):
        with _AT_ONCE:
            try:
                return fetch(ticker)
            except NewsFetchError as exc:
                failure = exc
        if str(failure).startswith(NOT_RETRIED):
            raise failure
        if attempt < tries:
            log.warning("%s: news search failed (try %d of %d): %s", ticker, attempt, tries, failure)
            sleep(pause)
    raise NewsFetchError(f"asked {tries} times: {failure}") from failure


def news_step(tickers: Iterable[str], workers: int, *, tries: int = TRIES, pause: float = TRY_PAUSE_SECONDS,
              sleep: Optional[Callable[[float], None]] = None) -> dict:
    """Every name's news search as the universe makes it, ``workers`` names at a time, and nothing else.

    No model, no journal, no file: each name's headline count, or the error
    of its last try. What the owner asked to know: how many got no answer.
    """
    names = list(tickers)
    started = time.monotonic()

    def ask(ticker: str) -> tuple[str, Optional[int], Optional[str]]:
        try:
            return ticker, len(fetch_with_tries(ticker, tries=tries, pause=pause, sleep=sleep)), None
        except NewsFetchError as exc:
            return ticker, None, str(exc)[:200]

    with ThreadPoolExecutor(max_workers=max(1, min(workers, len(names) or 1))) as pool:
        found = list(pool.map(ask, names))
    no_answer = [t for t, count, _ in found if count is None]
    return {
        "names": len(names),
        "answered": len(names) - len(no_answer),
        "with_headlines": sum(1 for _, count, _ in found if count),
        "no_headline": sum(1 for _, count, _ in found if count == 0),
        "no_answer": no_answer,
        "errors": {t: error for t, _, error in found if error},
        "workers": workers, "news_at_once": NEWS_AT_ONCE, "tries": tries,
        "minutes": round((time.monotonic() - started) / 60, 1),
    }


def build_context(ticker: str) -> TickerContext:
    """``heartbeat.build_context`` with the universe's search: never raises for want of news."""
    try:
        headlines = fetch_with_tries(ticker)
    except NewsFetchError as exc:
        log.warning("%s: news unavailable, continuing on the other sections (%s)", ticker, exc)
        return context.gather(
            ticker, [], news_gap=f"{context.NEWS_GAP_PREFIX}: {exc}",
        )
    return context.gather(ticker, headlines)


__all__ = ["DEFAULT_ZONE", "NEWS_AT_ONCE", "TRIES", "TRY_PAUSE_SECONDS", "UniverseNewsProvider", "build_context",
           "fetch", "fetch_with_tries", "news_step", "search_url"]
