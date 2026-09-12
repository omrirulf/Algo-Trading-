"""Recent news for a ticker via Bright Data's SERP API (Google News).

Request shape (from Bright Data's own SDK and MCP server): POST
``https://api.brightdata.com/request`` with a Bearer token and a JSON body of
``{zone, url, format: "raw"}``. Appending ``brd_json=1`` to a Google URL makes
Bright Data return the parsed result set as JSON instead of HTML.

This module has no credentials other than the Bright Data token and never
talks to the broker or the execution engine.
"""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlencode

import httpx

BRIGHTDATA_REQUEST_URL = "https://api.brightdata.com/request"

#: Google ``tbs=qdr:`` window. ``d`` = past 24 hours, which suits an hourly job.
NEWS_LOOKBACK = "d"
MAX_HEADLINES = 10
REQUEST_TIMEOUT_SECONDS = 60.0

#: Keys under which Bright Data's Google parser may put result items. ``news``
#: is the news-tab list; ``organic`` is the fallback if the zone returns a
#: regular SERP for the same query.
_RESULT_KEYS = ("news", "top_stories", "organic")


class NewsFetchError(Exception):
    """Bright Data was unreachable, rejected the request, or returned no JSON."""


def build_news_search_url(ticker: str) -> str:
    params = {
        "q": f"{ticker} stock",
        "tbm": "nws",
        "tbs": f"qdr:{NEWS_LOOKBACK}",
        "num": MAX_HEADLINES,
        "hl": "en",
        "gl": "us",
        "brd_json": 1,
    }
    return f"https://www.google.com/search?{urlencode(params)}"


def _first(item: dict[str, Any], *keys: str) -> str:
    for key in keys:
        value = item.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def _unwrap(payload: Any) -> dict[str, Any]:
    """Accept the parsed JSON directly or Bright Data's {status_code, headers, body} wrapper."""
    if isinstance(payload, str):
        stripped = payload.strip()
        if stripped.startswith("<"):
            raise NewsFetchError(
                "Bright Data returned HTML, not parsed JSON; check that the zone is a "
                "SERP API zone and brd_json=1 is on the URL"
            )
        try:
            payload = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise NewsFetchError(f"Bright Data response is not JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise NewsFetchError(f"unexpected Bright Data response type: {type(payload).__name__}")
    if "body" in payload and "status_code" in payload:
        status = payload.get("status_code")
        if isinstance(status, int) and status >= 400:
            headers = payload.get("headers") if isinstance(payload.get("headers"), dict) else {}
            msg = headers.get("x-brd-err-msg") or headers.get("x-brd-error") or ""
            raise NewsFetchError(f"Bright Data target request failed: HTTP {status} {msg}".rstrip())
        return _unwrap(payload["body"])
    return payload


def parse_news_results(payload: Any, limit: int = MAX_HEADLINES) -> list[str]:
    """Turn a Bright Data parsed-Google payload into ``"title — snippet (source, when)"`` lines."""
    data = _unwrap(payload)
    items: list[Any] = []
    for key in _RESULT_KEYS:
        value = data.get(key)
        if isinstance(value, list) and value:
            items = value
            break

    lines: list[str] = []
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            continue
        title = _first(item, "title")
        if not title or title.lower() in seen:
            continue
        seen.add(title.lower())
        snippet = _first(item, "description", "snippet")
        source = _first(item, "source", "source_name", "display_link")
        when = _first(item, "date", "time", "published", "age")
        line = title
        if snippet:
            line += f" — {snippet}"
        meta = ", ".join(x for x in (source, when) if x)
        if meta:
            line += f" ({meta})"
        lines.append(line)
        if len(lines) >= limit:
            break
    return lines


class BrightDataNewsProvider:
    def __init__(self, api_token: str, zone: str, client: httpx.Client | None = None) -> None:
        if not api_token:
            raise NewsFetchError("BRIGHTDATA_API_TOKEN is not set")
        if not zone:
            raise NewsFetchError("BRIGHTDATA_SERP_ZONE is not set")
        self._token = api_token
        self._zone = zone
        self._client = client

    def _post(self, body: dict[str, Any]) -> httpx.Response:
        headers = {"Authorization": f"Bearer {self._token}", "Content-Type": "application/json"}
        if self._client is not None:
            return self._client.post(BRIGHTDATA_REQUEST_URL, json=body, headers=headers)
        with httpx.Client(timeout=REQUEST_TIMEOUT_SECONDS) as client:
            return client.post(BRIGHTDATA_REQUEST_URL, json=body, headers=headers)

    def fetch(self, ticker: str) -> list[str]:
        body = {"zone": self._zone, "url": build_news_search_url(ticker), "format": "raw"}
        try:
            resp = self._post(body)
        except httpx.HTTPError as exc:
            raise NewsFetchError(f"Bright Data unreachable: {exc}") from exc
        if resp.status_code != 200:
            raise NewsFetchError(f"Bright Data HTTP {resp.status_code}: {resp.text[:300]}")
        return parse_news_results(resp.text)
