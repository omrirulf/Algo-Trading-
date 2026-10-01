#!/usr/bin/env python3
"""Why can the Web Unlocker not read this page? One URL, asked every way Bright Data's own tools ask.

    python replay/unlocker_check.py --url https://finance.yahoo.com/markets/stocks/articles/...

The article probe and the article archive were refused with HTTP 502 on
every Yahoo Finance page they tried (29 Sep 2026), while the same pages open
in a browser. A 502 from Bright Data's request API says only that *something*
answered 502: the page itself, or the Unlocker giving up on it. This asks for
one page in each of the ways Bright Data's CLI and MCP server ask (raw; raw
as markdown; as JSON, which reports the target's status apart from the
API's; from a US exit), tries the same story under Yahoo's older ``/news/``
path and the site's front page, and fetches the page directly from this
machine as a control. For each it prints the status, every response header
and the first words of the body, so the answer is read rather than guessed.

The Bright Data token goes only to ``news.BRIGHTDATA_REQUEST_URL``; the
direct fetch carries no credential at all. Read-only: it fetches and prints.
No journal, no model, no broker key.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional
from urllib.parse import urlsplit, urlunsplit

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from orchestrator import news  # noqa: E402
from orchestrator.article_text import _auth, brd_reason, brief  # noqa: E402

#: The page the first refusals were seen on: ASML, from the 29 Sep cycle.
DEFAULT_URL = "https://finance.yahoo.com/markets/stocks/articles/asml-asml-increases-despite-market-205005742.html"
REQUEST_TIMEOUT_SECONDS = 60.0
#: What a browser sends; the direct fetch is a control, so it looks like one.
BROWSER_HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}
EXCERPT_CHARS = 300
_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)

#: ``(method, url, headers, json body or None) -> response``: the one seam a test replaces.
Fetch = Callable[[str, str, dict, Optional[dict]], Any]


def http_fetch(method: str, url: str, headers: dict, body: Optional[dict] = None) -> Any:
    with httpx.Client(timeout=REQUEST_TIMEOUT_SECONDS, follow_redirects=True) as client:
        return client.request(method, url, headers=headers, json=body)


def news_path(url: str) -> Optional[str]:
    """Yahoo's older address for the same story, when the given one is the newer kind.

    ``/markets/stocks/articles/<slug>.html`` and ``/healthcare/articles/<slug>.html``
    are the forms the news fetch sees now; ``/news/<slug>.html`` is the form
    Yahoo has served for years. The story id is in the slug, so both resolve.
    """
    parts = urlsplit(url)
    if not parts.netloc.lower().endswith("yahoo.com") or "/articles/" not in parts.path:
        return None
    slug = parts.path.split("/articles/", 1)[1]
    return urlunsplit((parts.scheme, parts.netloc, f"/news/{slug}", "", ""))


def variants(url: str, zone: str) -> list[tuple[str, Optional[dict]]]:
    """``(name, request body)`` in order; a body of None is the direct fetch."""
    front = urlunsplit((urlsplit(url).scheme, urlsplit(url).netloc, "/", "", ""))
    out: list[tuple[str, Optional[dict]]] = [
        ("direct from this machine, no Bright Data (control)", None),
        ("unlocker, raw (what the probe and the archive send)", {"zone": zone, "url": url, "format": "raw"}),
        ("unlocker, raw as markdown (what the MCP server sends)",
         {"zone": zone, "url": url, "format": "raw", "data_format": "markdown"}),
        ("unlocker, json (the target's status apart from the API's)", {"zone": zone, "url": url, "format": "json"}),
        ("unlocker, raw, US exit", {"zone": zone, "url": url, "format": "raw", "country": "us"}),
    ]
    alt = news_path(url)
    if alt:
        out.append(("unlocker, raw, the same story under /news/", {"zone": zone, "url": alt, "format": "raw"}))
    out.append(("unlocker, raw, the site's front page", {"zone": zone, "url": front, "format": "raw"}))
    return out


@dataclass
class Check:
    name: str
    request: Optional[dict]
    status: Optional[int] = None
    seconds: float = 0.0
    final_url: str = ""
    headers: dict = field(default_factory=dict)
    body_bytes: int = 0
    title: str = ""
    excerpt: str = ""
    reason: str = ""
    error: str = ""
    #: From the JSON form: what the page itself answered, as the API reports it.
    target_status: Optional[int] = None
    target_headers: dict = field(default_factory=dict)


def run_check(fetch: Fetch, token: str, name: str, request: Optional[dict], url: str) -> Check:
    """One way of asking; never raises."""
    check = Check(name=name, request=request)
    started = time.monotonic()
    try:
        if request is None:
            response = fetch("GET", url, dict(BROWSER_HEADERS), None)
        else:
            response = fetch("POST", news.BRIGHTDATA_REQUEST_URL, _auth(token), request)
    except httpx.HTTPError as exc:
        check.error = f"{type(exc).__name__}: {exc}"[:200]
        check.seconds = time.monotonic() - started
        return check
    check.seconds = time.monotonic() - started
    check.status = int(response.status_code)
    check.final_url = str(getattr(response, "url", "") or "")
    check.headers = {str(k): str(v)[:200] for k, v in dict(getattr(response, "headers", {}) or {}).items()}
    text = response.text or ""
    check.body_bytes = len(text.encode("utf-8"))
    check.reason = brd_reason(response)
    if request is not None and request.get("format") == "json":
        try:
            payload = response.json()
        except ValueError:
            payload = None
        if isinstance(payload, dict):
            if payload.get("status_code") is not None:
                check.target_status = int(payload["status_code"])
            check.target_headers = {str(k): str(v)[:200] for k, v in dict(payload.get("headers") or {}).items()}
            text = str(payload.get("body") or "")
    match = _TITLE.search(text[:20000])
    check.title = " ".join(match.group(1).split())[:120] if match else ""
    check.excerpt = brief(text, EXCERPT_CHARS)
    return check


def run_all(fetch: Fetch, token: str, zone: str, url: str) -> list[Check]:
    return [run_check(fetch, token, name, request, url) for name, request in variants(url, zone)]


def render(checks: list[Check], url: str, zone: str) -> str:
    out = [f"UNLOCKER CHECK: {url}", f"zone: {zone}", "=" * 78]
    for check in checks:
        out += ["", f"== {check.name}"]
        if check.request is not None:
            out.append("   request: " + json.dumps({k: v for k, v in check.request.items() if k != "zone"}))
        if check.error:
            out.append(f"   error: {check.error}")
            continue
        out.append(f"   status: {check.status}   {check.seconds:.1f}s   {check.body_bytes:,} bytes"
                   + (f"   final url: {check.final_url}" if check.final_url and check.final_url != url else ""))
        if check.reason:
            out.append(f"   bright data says: {check.reason}")
        if check.target_status is not None:
            out.append(f"   the page itself answered: {check.target_status}")
            for key, value in sorted(check.target_headers.items()):
                out.append(f"      {key}: {value}")
        for key, value in sorted(check.headers.items()):
            out.append(f"   {key}: {value}")
        if check.title:
            out.append(f"   title: {check.title}")
        out.append(f"   body: {check.excerpt or '(empty)'}")
    return "\n".join(out)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ask the Web Unlocker for one page every way Bright Data's tools do.")
    parser.add_argument("--url", default=DEFAULT_URL, help="the page (default: the ASML story of 29 Sep)")
    parser.add_argument("--zone", default="", help="the Unlocker zone (default: the one the news fetch uses)")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    args = parse_args(argv)
    from config.settings import get_settings

    settings = get_settings()
    token = news.resolve_token(settings.brightdata_api_token) or ""
    zone = args.zone.strip() or news.resolve_zone(settings.brightdata_serp_zone, settings.brightdata_unlocker_zone)
    if not token or not zone:
        print("no Bright Data token or zone: set BRIGHTDATA_API_TOKEN (and the zone the news fetch uses)")
        return 2
    print(render(run_all(http_fetch, token, zone, args.url.strip()), args.url.strip(), zone))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
