#!/usr/bin/env python3
"""Would a SERP API zone give the news fetch fewer empty answers than the Web Unlocker zone? Two zones, the same asks.

    python replay/serp_zone_probe.py [--zone-b serp_news_probe] [--create] [--count 20]

Production's news fetch (``orchestrator/news.py``) sends its Google News
searches through the Web Unlocker zone ``cli_unlocker``, and since 23 Sep
2026 a share of the answers have been a 200 with an empty body (6 Oct: 44 of
80 first answers; 15 Oct: 60, and 53 of the second asks were empty again).
Bright Data serves the same searches through a SERP API zone too, opened
free of charge and billed per request. The owner (16 Oct 2026) allowed one
to be opened through the account API and expects no difference; this
measures instead of assuming.

For each of the first ``count`` watchlist names it sends production's exact
request -- the same URL with ``brd_json=1``, the same ``format: raw`` --
once through each zone, back to back, and prints for every ask the status,
the bytes, whether the parser found news and how many items, Bright Data's
own headers and the seconds; then each zone's share of empty answers.
``--create`` opens zone B through the account API when it does not exist
yet (``POST /zone``) and prints the API's status and words, so a refused
shape is corrected from what the API said rather than guessed.

The token goes only to api.brightdata.com and never into the output.
Read-only beyond the asks it pays for (about forty, a few cents): it
prints, writes nothing, trades nothing, holds no broker key. Production's
zone does not change here; that is the owner's decision, made by setting
the repository variable ``BRIGHTDATA_SERP_ZONE``.
"""

from __future__ import annotations

import argparse
import os
import statistics
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from config.watchlist import DEFAULT_WATCHLIST  # noqa: E402
from orchestrator import news  # noqa: E402

ZONE_API = "https://api.brightdata.com/zone"
ACTIVE_ZONES_API = "https://api.brightdata.com/zone/get_active_zones"
DEFAULT_ZONE_B = "serp_news_probe"
DEFAULT_ZONE_A = "cli_unlocker"
REQUEST_TIMEOUT_SECONDS = news.REQUEST_TIMEOUT_SECONDS

#: ``(method, url, headers, json body or None) -> response``: the one seam a test replaces.
Fetch = Callable[[str, str, dict, Optional[dict]], Any]


def http_fetch(method: str, url: str, headers: dict, body: Optional[dict] = None) -> Any:
    with httpx.Client(timeout=REQUEST_TIMEOUT_SECONDS) as client:
        return client.request(method, url, headers=headers, json=body)


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def zone_a_from_env(explicit: str = "") -> str:
    """Production's zone: the SERP zone variable when set, else the CLI's unlocker zone, else ``cli_unlocker``."""
    return (explicit.strip() or os.environ.get("BRIGHTDATA_SERP_ZONE", "").strip()
            or os.environ.get(news.CLI_UNLOCKER_ENV_VAR, "").strip() or DEFAULT_ZONE_A)


# --------------------------------------------------------------------------- #
# The zone
# --------------------------------------------------------------------------- #


def zone_body(name: str) -> dict[str, Any]:
    """What the account API is asked for: a SERP API zone, pay per use.

    The SERP API is the Unlocker plan with ``serp`` on (Bright Data's CLI
    opens its zones the same way); nothing here chooses a bandwidth plan or
    an IP pool, so there is nothing to pay for until a request is sent.
    """
    return {"zone": {"name": name, "type": "unblocker"}, "plan": {"type": "unblocker", "serp": True}}


def zone_exists(fetch: Fetch, token: str, name: str) -> Optional[bool]:
    """True or False from the account's active zones; None when the list could not be read."""
    response = fetch("GET", ACTIVE_ZONES_API, _auth(token), None)
    if getattr(response, "status_code", None) != 200:
        return None
    try:
        zones = response.json()
    except ValueError:
        return None
    if not isinstance(zones, list):
        return None
    return name in {z.get("name") for z in zones if isinstance(z, dict)}


def create_zone(fetch: Fetch, token: str, name: str) -> tuple[Optional[int], str]:
    """Open zone ``name``; the API's status and its first words (never the token)."""
    response = fetch("POST", ZONE_API, _auth(token), zone_body(name))
    status = getattr(response, "status_code", None)
    text = getattr(response, "text", "") or ""
    return status, text[:300].replace(token, "***") if token else text[:300]


# --------------------------------------------------------------------------- #
# The asks
# --------------------------------------------------------------------------- #


@dataclass
class Ask:
    """One search through one zone."""

    zone: str
    ticker: str
    status: Optional[int] = None
    size: int = 0
    empty: bool = False
    items: int = 0
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
        if self.empty:
            return "empty body"
        if self.refused:
            return "refused"
        return "news" if self.items else "no items"


def ask(fetch: Fetch, token: str, zone: str, ticker: str) -> Ask:
    """Production's request for ``ticker`` through ``zone``, judged the way production judges it."""
    url = news.build_news_search_url(ticker)
    body = {"zone": zone, "url": url, "format": "raw"}
    result = Ask(zone, ticker)
    clock = time.monotonic()
    try:
        response = fetch("POST", news.BRIGHTDATA_REQUEST_URL, _auth(token), body)
    except httpx.HTTPError as exc:
        result.error = type(exc).__name__
        result.seconds = time.monotonic() - clock
        return result
    result.seconds = time.monotonic() - clock
    result.status = getattr(response, "status_code", None)
    text = getattr(response, "text", "") or ""
    result.size = len(text)
    result.empty = not text.strip()
    result.headers = news.brd_headers(response)
    if result.status == 200 and not result.empty:
        try:
            result.items = len(news.parse_news_items(text))
        except news.NewsFetchError as exc:
            result.refused = str(exc)[:60]
    return result


def probe(fetch: Fetch, token: str, zones: list[str], tickers: list[str]) -> list[Ask]:
    """Every ticker through every zone, back to back, in production's order."""
    out: list[Ask] = []
    for ticker in tickers:
        for zone in zones:
            out.append(ask(fetch, token, zone, ticker))
    return out


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


def line_for(a: Ask) -> str:
    extra = a.error or (f"[{a.headers}]" if a.headers else "")
    return (f"{a.ticker:<6} {a.zone:<18} {a.outcome:<10} status {a.status if a.status is not None else '-':>4} "
            f"{a.size:7d} bytes {a.items:3d} items {a.seconds:6.1f}s {a.refused} {extra}".rstrip())


def summary(asks: list[Ask], zones: list[str]) -> str:
    lines = []
    for zone in zones:
        mine = [a for a in asks if a.zone == zone]
        if not mine:
            continue
        n = len(mine)
        empty = sum(1 for a in mine if a.outcome == "empty body")
        with_news = sum(1 for a in mine if a.outcome == "news")
        refused = sum(1 for a in mine if a.outcome == "refused")
        errors = sum(1 for a in mine if a.outcome.startswith("HTTP") or a.outcome == "error")
        median = statistics.median(a.seconds for a in mine)
        lines.append(f"{zone}: {n} asks, news for {with_news} ({with_news / n:.0%}), empty body {empty} "
                     f"({empty / n:.0%}), refused {refused}, HTTP/transport errors {errors}, median {median:.1f}s")
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None, fetch: Fetch = http_fetch) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--zone-a", default="", help="production's zone (default: from the environment, else cli_unlocker)")
    parser.add_argument("--zone-b", default=DEFAULT_ZONE_B, help="the SERP API zone to compare")
    parser.add_argument("--create", action="store_true", help="open zone B through the account API if it does not exist")
    parser.add_argument("--count", type=int, default=20, help="watchlist names to ask, from the front of the list")
    args = parser.parse_args(argv)

    token = news.resolve_token(os.environ.get("BRIGHTDATA_API_TOKEN", ""))
    if not token:
        print("no Bright Data token: set BRIGHTDATA_API_TOKEN")
        return 1
    zone_a = zone_a_from_env(args.zone_a)
    zones = [zone_a]
    exists = zone_exists(fetch, token, args.zone_b)
    print(f"zone A (production): {zone_a}; zone B: {args.zone_b} "
          f"{'exists' if exists else 'does not exist' if exists is False else 'unknown (the zone list could not be read)'}")
    if exists is False and args.create:
        status, words = create_zone(fetch, token, args.zone_b)
        print(f"POST /zone -> HTTP {status}: {words}")
        exists = zone_exists(fetch, token, args.zone_b)
        print(f"zone B now {'exists' if exists else 'still missing' if exists is False else 'unknown'}")
    if exists:
        zones.append(args.zone_b)
    else:
        print("zone B is not asked; only production's zone is measured")
    tickers = list(DEFAULT_WATCHLIST[:max(0, args.count)])
    print(f"{len(tickers)} names x {len(zones)} zone(s), back to back, production's request each time")
    asks = probe(fetch, token, zones, tickers)
    for a in asks:
        print(line_for(a))
    print()
    print(summary(asks, zones))
    return 0


if __name__ == "__main__":
    sys.exit(main())
