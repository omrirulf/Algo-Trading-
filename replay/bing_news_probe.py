#!/usr/bin/env python3
"""Would Bing News answer where Google refuses? Production's request against Bing's RSS feed, for the same names.

    python replay/bing_news_probe.py [--count 20] [--no-bright-data]

Production's news fetch (``orchestrator/news.py``) asks Google News through
Bright Data from a US exit, once more after 10 seconds when the answer is an
empty 200. Since 23 Sep 2026 a share of those answers have been "redirect
location was rejected": Google answers the search with a redirect (its
consent or regional page) and the Unlocker refuses to follow it. The share
rose through October (1 name a day in the middle of the month, 4 to 5 a day
in its last week, 7 on 2 Nov) and the owner asked on 4 Nov 2026 whether Bing
would do instead.

Bing News publishes the same search as an RSS feed, with no consent page:
``https://www.bing.com/news/search?q=...&format=rss``. For each of the first
``count`` watchlist names this asks, back to back:

* **google, Bright Data** -- production's exact request (its zone, its URL
  with ``brd_json=1``, its US exit), judged the way production judges it;
* **bing rss, direct** -- the feed fetched from this machine, no Bright Data,
  no time window;
* **bing rss, direct, 24h** -- the same with Bing's past-24-hours filter;
* **bing rss, Bright Data, 24h** -- the filtered feed through production's
  Bright Data zone, in case Bing blocks the runner's address one day.

It prints for every ask the status, the bytes, how many headlines the parser
found, the newest and oldest story's age in hours, the seconds, and the
vendor's own headers on a refusal; then each arm's share of names with news,
and how many of Google's headlines Bing also carried. Read-only beyond the
asks it pays for (two Bright Data requests a name, a few cents in all): it
prints, writes nothing, trades nothing, holds no broker key, asks no model.
The token goes only to api.brightdata.com and never into the output.
Production changes only by the owner's decision.
"""

from __future__ import annotations

import argparse
import os
import re
import statistics
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Callable, Optional
from urllib.parse import urlencode
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from config.instruments import is_fund  # noqa: E402
from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from orchestrator import news  # noqa: E402

BING_NEWS_URL = "https://www.bing.com/news/search"
#: Bing's "past 24 hours" filter, as its own news page sends it.
BING_LAST_24H = 'interval="7"'
REQUEST_TIMEOUT_SECONDS = news.REQUEST_TIMEOUT_SECONDS
#: A browser's name: Bing answers an empty client name with a block page.
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

Fetch = Callable[[str, str, dict, Optional[dict]], Any]


def http_fetch(method: str, url: str, headers: dict, body: Optional[dict] = None) -> Any:
    with httpx.Client(timeout=REQUEST_TIMEOUT_SECONDS, follow_redirects=True) as client:
        return client.request(method, url, headers=headers, json=body)


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


# --------------------------------------------------------------------------- #
# Bing's feed
# --------------------------------------------------------------------------- #


def bing_news_url(ticker: str, last_24h: bool = False) -> str:
    """Bing News RSS for one ticker, with production's qualifier ("stock", or "ETF" for a fund)."""
    qualifier = "ETF" if is_fund(ticker) else "stock"
    params: dict[str, Any] = {"q": f"{ticker} {qualifier}", "format": "rss", "setlang": "en-US", "cc": "US"}
    if last_24h:
        params["qft"] = BING_LAST_24H
    return f"{BING_NEWS_URL}?{urlencode(params)}"


def _text(element: Optional[ElementTree.Element]) -> str:
    return (element.text or "").strip() if element is not None else ""


def _child(item: ElementTree.Element, local: str) -> Optional[ElementTree.Element]:
    """A child by its local name, whatever namespace the feed put it in (Bing's carries the query)."""
    for child in item:
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == local:
            return child
    return None


def _age_hours(published: str, now: Optional[datetime] = None) -> Optional[float]:
    try:
        stamp = parsedate_to_datetime(published)
    except (TypeError, ValueError, IndexError):
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    now = now or datetime.now(timezone.utc)
    return max(0.0, (now - stamp).total_seconds() / 3600.0)


@dataclass(frozen=True)
class Story:
    headline: news.Headline
    age_hours: Optional[float]


def parse_bing_rss(text: str, limit: int = news.MAX_HEADLINES, now: Optional[datetime] = None) -> list[Story]:
    """The feed's items as production's ``Headline`` records (title, snippet, source, when, url), newest first.

    Deduplicated by title, as production's parser does. Raises
    ``news.NewsFetchError`` on anything that is not an RSS document (a block
    page, an empty body), so the probe judges it the way production would.
    """
    stripped = (text or "").strip()
    if not stripped:
        raise news.NewsFetchError("Bing returned an empty body")
    if not stripped.startswith("<"):
        raise news.NewsFetchError(f"Bing returned something that is not XML (starts {stripped[:30]!r})")
    try:
        root = ElementTree.fromstring(stripped)
    except ElementTree.ParseError as exc:
        raise news.NewsFetchError(f"Bing returned XML the parser refused: {exc}") from exc
    items = root.findall(".//item")
    if root.tag.lower() != "rss" and not items:
        raise news.NewsFetchError(f"Bing returned <{root.tag}>, not an RSS feed")
    out: list[Story] = []
    seen: set[str] = set()
    for item in items:
        title = _text(_child(item, "title"))
        if not title or title.lower() in seen:
            continue
        seen.add(title.lower())
        published = _text(_child(item, "pubDate"))
        age = _age_hours(published, now)
        when = f"{age:.0f}h ago" if age is not None else published
        snippet = re.sub(r"\s+", " ", _text(_child(item, "description")))
        out.append(Story(news.Headline(title=title, snippet=snippet, source=_text(_child(item, "Source")),
                                       when=when, url=_text(_child(item, "link"))), age))
        if len(out) >= limit:
            break
    return out


# --------------------------------------------------------------------------- #
# The arms and the asks
# --------------------------------------------------------------------------- #

GOOGLE = "google, Bright Data"
BING_DIRECT = "bing rss, direct"
BING_DIRECT_24H = "bing rss, direct, 24h"
BING_BRIGHT_DATA_24H = "bing rss, Bright Data, 24h"


@dataclass(frozen=True)
class Arm:
    label: str
    #: ``google`` is production's request; ``bing`` the feed.
    engine: str
    via_bright_data: bool
    last_24h: bool = False


def arms_for(bright_data: bool) -> list[Arm]:
    out: list[Arm] = []
    if bright_data:
        out.append(Arm(GOOGLE, "google", True))
    out += [Arm(BING_DIRECT, "bing", False), Arm(BING_DIRECT_24H, "bing", False, True)]
    if bright_data:
        out.append(Arm(BING_BRIGHT_DATA_24H, "bing", True, True))
    return out


@dataclass
class Ask:
    arm: str
    ticker: str
    status: Optional[int] = None
    size: int = 0
    items: int = 0
    titles: tuple[str, ...] = ()
    newest_hours: Optional[float] = None
    oldest_hours: Optional[float] = None
    refused: str = ""
    headers: str = ""
    seconds: float = 0.0
    error: str = ""

    @property
    def outcome(self) -> str:
        if self.error:
            return "error"
        if self.status != 200:
            return f"HTTP {self.status}"
        if self.refused:
            return "refused"
        return "news" if self.items else "no items"


def ask(fetch: Fetch, token: str, zone: str, arm: Arm, ticker: str, now: Optional[datetime] = None) -> Ask:
    """One search for ``ticker`` through ``arm``, judged the way production judges it."""
    result = Ask(arm.label, ticker)
    if arm.engine == "google":
        target = news.build_news_search_url(ticker)
    else:
        target = bing_news_url(ticker, arm.last_24h)
    clock = time.monotonic()
    try:
        if arm.via_bright_data:
            body = {"zone": zone, "url": target, "format": "raw", "country": news.BRD_COUNTRY}
            response = fetch("POST", news.BRIGHTDATA_REQUEST_URL, _auth(token), body)
        else:
            response = fetch("GET", target, {"User-Agent": USER_AGENT, "Accept": "application/rss+xml, text/xml"}, None)
    except httpx.HTTPError as exc:
        result.error = type(exc).__name__
        result.seconds = time.monotonic() - clock
        return result
    result.seconds = time.monotonic() - clock
    result.status = getattr(response, "status_code", None)
    text = getattr(response, "text", "") or ""
    result.size = len(text)
    if arm.via_bright_data:
        result.headers = news.brd_headers(response)
    if result.status != 200:
        return result
    try:
        if arm.engine == "google":
            headlines = news.parse_news_items(text)
            ages: list[float] = []
        else:
            stories = parse_bing_rss(text, now=now)
            headlines = [s.headline for s in stories]
            ages = [s.age_hours for s in stories if s.age_hours is not None]
    except news.NewsFetchError as exc:
        result.refused = str(exc)[:60]
        if not result.size:
            result.refused = "empty body"
        return result
    result.items = len(headlines)
    result.titles = tuple(h.title for h in headlines)
    if ages:
        result.newest_hours, result.oldest_hours = min(ages), max(ages)
    return result


def probe(fetch: Fetch, token: str, zone: str, arms: list[Arm], tickers: list[str],
          now: Optional[datetime] = None) -> list[Ask]:
    out: list[Ask] = []
    for ticker in tickers:
        for arm in arms:
            out.append(ask(fetch, token, zone, arm, ticker, now))
    return out


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


def _words(title: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", title.lower()) if len(w) > 2}


def shared_titles(google: tuple[str, ...], bing: tuple[str, ...]) -> int:
    """Google headlines that Bing also carried: the same story, allowing the outlets' different wording."""
    count = 0
    for g in google:
        mine = _words(g)
        if not mine:
            continue
        if any(len(mine & _words(b)) >= max(3, int(0.6 * len(mine))) for b in bing):
            count += 1
    return count


def line_for(a: Ask) -> str:
    ages = ""
    if a.newest_hours is not None:
        ages = f"newest {a.newest_hours:4.0f}h oldest {a.oldest_hours:5.0f}h"
    extra = a.error or (f"[{a.headers}]" if a.headers else "")
    return (f"{a.ticker:<6} {a.arm:<28} {a.outcome:<9} status {a.status if a.status is not None else '-':>4} "
            f"{a.size:7d} bytes {a.items:3d} items {a.seconds:6.1f}s {ages} {a.refused} {extra}".rstrip())


def summary(asks: list[Ask], arms: list[Arm]) -> str:
    lines = []
    for arm in arms:
        mine = [a for a in asks if a.arm == arm.label]
        if not mine:
            continue
        n = len(mine)
        with_news = [a for a in mine if a.outcome == "news"]
        refused = sum(1 for a in mine if a.outcome == "refused")
        errors = sum(1 for a in mine if a.outcome.startswith("HTTP") or a.outcome == "error")
        none = sum(1 for a in mine if a.outcome == "no items")
        median_s = statistics.median(a.seconds for a in mine)
        items = statistics.median(a.items for a in with_news) if with_news else 0
        newest = [a.newest_hours for a in with_news if a.newest_hours is not None]
        oldest = [a.oldest_hours for a in with_news if a.oldest_hours is not None]
        ages = (f", newest story median {statistics.median(newest):.0f}h, oldest median {statistics.median(oldest):.0f}h"
                if newest else "")
        lines.append(f"{arm.label}: {n} asks, news for {len(with_news)} ({len(with_news) / n:.0%}), no items {none}, "
                     f"refused {refused}, HTTP/transport errors {errors}, median {items:.0f} headlines, "
                     f"median {median_s:.1f}s{ages}")
    google = {a.ticker: a for a in asks if a.arm == GOOGLE and a.outcome == "news"}
    for arm in arms:
        if arm.engine != "bing":
            continue
        pairs = [(google[a.ticker], a) for a in asks if a.arm == arm.label and a.outcome == "news" and a.ticker in google]
        if pairs:
            shared = sum(shared_titles(g.titles, b.titles) for g, b in pairs)
            total = sum(len(g.titles) for g, _ in pairs)
            lines.append(f"{arm.label} against google: {len(pairs)} names with news on both; "
                         f"{shared} of Google's {total} headlines also on Bing ({shared / total:.0%})"
                         if total else f"{arm.label} against google: nothing to compare")
    rescued = [a.ticker for a in asks if a.arm == GOOGLE and a.outcome != "news"
               and any(b.arm == BING_DIRECT_24H and b.ticker == a.ticker and b.outcome == "news" for b in asks)]
    if any(a.arm == GOOGLE for a in asks):
        lines.append(f"names Google did not answer that Bing (direct, 24h) did: {len(rescued)}"
                     + (f" ({', '.join(rescued)})" if rescued else ""))
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None, fetch: Fetch = http_fetch) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--count", type=int, default=20, help="watchlist names to ask, from the front of the list")
    parser.add_argument("--no-bright-data", action="store_true",
                        help="ask only Bing directly: no token needed, nothing billed")
    args = parser.parse_args(argv)

    token = "" if args.no_bright_data else news.resolve_token(os.environ.get("BRIGHTDATA_API_TOKEN", ""))
    zone = news.resolve_zone(os.environ.get("BRIGHTDATA_SERP_ZONE", "")) or ""
    bright_data = bool(token and zone)
    if not args.no_bright_data and not bright_data:
        print("no Bright Data token or zone: only Bing's feed is asked, directly")
    arms = arms_for(bright_data)
    tickers = list(DEFAULT_WATCHLIST[:max(0, args.count)])
    print(f"{len(tickers)} names x {len(arms)} arm(s), back to back"
          + (f"; production's zone {zone}" if bright_data else "") + ": " + "; ".join(a.label for a in arms))
    asks = probe(fetch, token, zone, arms, tickers)
    for a in asks:
        print(line_for(a))
    print()
    print(summary(asks, arms))
    return 0


if __name__ == "__main__":
    sys.exit(main())
