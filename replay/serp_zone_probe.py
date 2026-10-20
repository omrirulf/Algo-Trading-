#!/usr/bin/env python3
"""Would a SERP API zone, or a US exit, give the news fetch fewer empty answers? The same asks, several ways.

    python replay/serp_zone_probe.py [--zone-b serp_news_probe] [--create] [--country us] [--count 20]
    python replay/serp_zone_probe.py --delete-zone serp_news_probe

Production's news fetch (``orchestrator/news.py``) sends its Google News
searches through the Web Unlocker zone ``cli_unlocker``, and since 23 Sep
2026 a share of the answers have been a 200 with an empty body (6 Oct: 44 of
80 first answers; 15 Oct: 60, and 53 of the second asks were empty again).
The first probe (16 Oct 2026) read Bright Data's own headers on those: every
empty 200 said ``x-brd-status-code 502; x-brd-error redirect location was
rejected`` -- Google answered the search with a redirect and the Unlocker
refused to follow it. A SERP API zone, opened the same day, showed the same
(6 of 20 empty against 4 of 20), so the zone is not the lever; the exit
country may be, since the redirect is likely Google's consent or regional
page for a non-US exit.

For each of the first ``count`` watchlist names this sends production's
exact request -- the same URL with ``brd_json=1``, the same ``format:
raw`` -- once through each arm, back to back: production's zone as it is,
production's zone with ``country`` set when ``--country`` is given, and
the same for zone B when it exists. It prints for every ask the status,
the bytes, whether the parser found news and how many items, Bright Data's
own headers and the seconds; then each arm's share of empty answers.

``--create`` opens zone B through the account API when it does not exist
(``POST /zone``, free to open, billed per request); ``--delete-zone``
removes a zone (``DELETE /zone``) and does nothing else. The account API's
answers are printed as their status and a few named fields only, never
whole: the create answer carries the zone's password. The token goes only
to api.brightdata.com and never into the output. Read-only beyond the
asks it pays for (a few cents): it prints, writes nothing, trades nothing,
holds no broker key. Production changes only by the owner's decision: the
repository variable ``BRIGHTDATA_SERP_ZONE`` for the zone, a code change
for the exit country.
"""

from __future__ import annotations

import argparse
import os
import statistics
import sys
import time
from dataclasses import dataclass, field
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
#: The only fields of an account API answer that are printed. A zone's
#: answer also carries its password; that is never shown.
SHOWN_FIELDS = ("created", "type", "product", "serp", "ips_type", "vips_type")

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


def shown(payload: Any) -> str:
    """The few named fields of an account API answer, as ``name=value``; nothing else of it."""
    found: list[str] = []

    def walk(node: Any, depth: int = 0) -> None:
        if not isinstance(node, dict) or depth > 3:
            return
        for key, value in node.items():
            if key in SHOWN_FIELDS and isinstance(value, (str, int, float, bool)):
                pair = f"{key}={value}"
                if pair not in found:
                    found.append(pair)
            elif isinstance(value, dict):
                walk(value, depth + 1)
    walk(payload)
    return ", ".join(found)


def api_words(response: Any) -> str:
    """``HTTP <status>`` and the shown fields of the answer, or its first words when it is not JSON."""
    status = getattr(response, "status_code", None)
    try:
        payload = response.json()
    except (ValueError, AttributeError):
        payload = None
    if isinstance(payload, dict):
        fields = shown(payload)
        return f"HTTP {status}" + (f": {fields}" if fields else "")
    text = str(getattr(response, "text", "") or "")[:120]
    return f"HTTP {status}: {text}" if text else f"HTTP {status}"


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


def create_zone(fetch: Fetch, token: str, name: str) -> str:
    """Open zone ``name``; the API's status and its shown fields (never the password, never the token)."""
    return api_words(fetch("POST", ZONE_API, _auth(token), zone_body(name)))


def delete_zone(fetch: Fetch, token: str, name: str) -> str:
    """Remove zone ``name``; the API's status and words."""
    return api_words(fetch("DELETE", ZONE_API, _auth(token), {"zone": name}))


# --------------------------------------------------------------------------- #
# The asks
# --------------------------------------------------------------------------- #


@dataclass
class Arm:
    """One way of asking: a zone, and what is added to production's body."""

    label: str
    zone: str
    extra: dict[str, Any] = field(default_factory=dict)


def arms_for(zone_a: str, zone_b: Optional[str], country: str) -> list[Arm]:
    """Production's zone first, each zone plain and then with the exit country when one is given."""
    out = [Arm(zone_a, zone_a)]
    if country:
        out.append(Arm(f"{zone_a}, {country} exit", zone_a, {"country": country}))
    if zone_b:
        out.append(Arm(zone_b, zone_b))
        if country:
            out.append(Arm(f"{zone_b}, {country} exit", zone_b, {"country": country}))
    return out


@dataclass
class Ask:
    """One search through one arm."""

    arm: str
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


def ask(fetch: Fetch, token: str, arm: Arm, ticker: str) -> Ask:
    """Production's request for ``ticker`` through ``arm``, judged the way production judges it."""
    url = news.build_news_search_url(ticker)
    body = {"zone": arm.zone, "url": url, "format": "raw", **arm.extra}
    result = Ask(arm.label, ticker)
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


def probe(fetch: Fetch, token: str, arms: list[Arm], tickers: list[str]) -> list[Ask]:
    """Every ticker through every arm, back to back, in production's order."""
    out: list[Ask] = []
    for ticker in tickers:
        for arm in arms:
            out.append(ask(fetch, token, arm, ticker))
    return out


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


def line_for(a: Ask) -> str:
    extra = a.error or (f"[{a.headers}]" if a.headers else "")
    return (f"{a.ticker:<6} {a.arm:<24} {a.outcome:<10} status {a.status if a.status is not None else '-':>4} "
            f"{a.size:7d} bytes {a.items:3d} items {a.seconds:6.1f}s {a.refused} {extra}".rstrip())


def summary(asks: list[Ask], arms: list[Arm]) -> str:
    lines = []
    for arm in arms:
        mine = [a for a in asks if a.arm == arm.label]
        if not mine:
            continue
        n = len(mine)
        empty = sum(1 for a in mine if a.outcome == "empty body")
        with_news = sum(1 for a in mine if a.outcome == "news")
        refused = sum(1 for a in mine if a.outcome == "refused")
        errors = sum(1 for a in mine if a.outcome.startswith("HTTP") or a.outcome == "error")
        median = statistics.median(a.seconds for a in mine)
        lines.append(f"{arm.label}: {n} asks, news for {with_news} ({with_news / n:.0%}), empty body {empty} "
                     f"({empty / n:.0%}), refused {refused}, HTTP/transport errors {errors}, median {median:.1f}s")
    return "\n".join(lines)


def main(argv: Optional[list[str]] = None, fetch: Fetch = http_fetch) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--zone-a", default="", help="production's zone (default: from the environment, else cli_unlocker)")
    parser.add_argument("--zone-b", default=DEFAULT_ZONE_B, help="the SERP API zone to compare; blank for none")
    parser.add_argument("--create", action="store_true", help="open zone B through the account API if it does not exist")
    parser.add_argument("--country", default="", help="also ask each zone from this exit country, e.g. us")
    parser.add_argument("--count", type=int, default=20, help="watchlist names to ask, from the front of the list")
    parser.add_argument("--delete-zone", default="", metavar="NAME", help="remove this zone and do nothing else")
    args = parser.parse_args(argv)

    token = news.resolve_token(os.environ.get("BRIGHTDATA_API_TOKEN", ""))
    if not token:
        print("no Bright Data token: set BRIGHTDATA_API_TOKEN")
        return 1
    if args.delete_zone:
        print(f"DELETE /zone {args.delete_zone} -> {delete_zone(fetch, token, args.delete_zone)}")
        gone = zone_exists(fetch, token, args.delete_zone)
        print(f"zone {args.delete_zone} now {'gone' if gone is False else 'still listed' if gone else 'unknown'}")
        return 0 if gone is False else 1
    zone_a = zone_a_from_env(args.zone_a)
    zone_b: Optional[str] = args.zone_b.strip() or None
    if zone_b:
        exists = zone_exists(fetch, token, zone_b)
        print(f"zone A (production): {zone_a}; zone B: {zone_b} "
              f"{'exists' if exists else 'does not exist' if exists is False else 'unknown (the zone list could not be read)'}")
        if exists is False and args.create:
            print(f"POST /zone -> {create_zone(fetch, token, zone_b)}")
            exists = zone_exists(fetch, token, zone_b)
            print(f"zone B now {'exists' if exists else 'still missing' if exists is False else 'unknown'}")
        if not exists:
            print("zone B is not asked; only production's zone is measured")
            zone_b = None
    else:
        print(f"zone A (production): {zone_a}; no zone B")
    arms = arms_for(zone_a, zone_b, args.country.strip())
    tickers = list(DEFAULT_WATCHLIST[:max(0, args.count)])
    print(f"{len(tickers)} names x {len(arms)} arm(s), back to back, production's request each time: "
          + "; ".join(a.label for a in arms))
    asks = probe(fetch, token, arms, tickers)
    for a in asks:
        print(line_for(a))
    print()
    print(summary(asks, arms))
    return 0


if __name__ == "__main__":
    sys.exit(main())
