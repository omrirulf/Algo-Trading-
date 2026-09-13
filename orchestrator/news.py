"""Recent news for a ticker via Bright Data's SERP API (Google News).

Request shape (from Bright Data's own SDK and MCP server): POST
``https://api.brightdata.com/request`` with a Bearer token and a JSON body of
``{zone, url, format: "raw"}``. Appending ``brd_json=1`` to a Google URL makes
Bright Data return the parsed result set as JSON instead of HTML.

The token can come from ``BRIGHTDATA_API_TOKEN``, from the ``BRIGHTDATA_API_KEY``
env var the official CLI reads, or from the key ``brightdata login`` stores
after its OAuth flow -- in that order. Reading the CLI's file is best-effort:
its format is not documented, so the lookup tries several field names and
treats anything it cannot make sense of as "not configured this way".

This module has no credentials other than the Bright Data token and never
talks to the broker or the execution engine.
"""

from __future__ import annotations

import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlencode

import httpx

log = logging.getLogger(__name__)

BRIGHTDATA_REQUEST_URL = "https://api.brightdata.com/request"

#: Google ``tbs=qdr:`` window. ``d`` = past 24 hours, which suits an hourly job.
NEWS_LOOKBACK = "d"
MAX_HEADLINES = 10
REQUEST_TIMEOUT_SECONDS = 60.0

#: Keys under which Bright Data's Google parser may put result items. ``news``
#: is the news-tab list; ``organic`` is the fallback if the zone returns a
#: regular SERP for the same query.
_RESULT_KEYS = ("news", "top_stories", "organic")


#: Env var the official Bright Data CLI reads as an override. Ours is
#: ``BRIGHTDATA_API_TOKEN``; accepting theirs too means a shell already set up
#: for the CLI needs no second variable for the same secret.
CLI_ENV_VAR = "BRIGHTDATA_API_KEY"

#: The zone env var Bright Data's own CLI falls back to when no SERP zone is
#: configured. Their ``search`` command resolves BRIGHTDATA_SERP_ZONE first and
#: then BRIGHTDATA_UNLOCKER_ZONE (brightdata/cli, src/commands/search.ts), and
#: its ``init`` offers the unlocker zone as the SERP default with "yes"
#: preselected. A Web Unlocker zone therefore serves ``brd_json=1`` search
#: URLs -- which is what makes `brightdata login` alone enough, since it
#: provisions ``cli_unlocker`` and no SERP zone.
CLI_UNLOCKER_ENV_VAR = "BRIGHTDATA_UNLOCKER_ZONE"

#: Where ``brightdata login`` stores the key it obtains over OAuth.
CLI_CONFIG_DIRNAME = "brightdata-cli"
CLI_CREDENTIALS_FILENAME = "credentials.json"

#: Field names to look for inside that file. The format is not documented, so
#: several plausible spellings are tried rather than betting on one. Anything
#: unrecognised is treated as "no credential here", never as an error.
CLI_CREDENTIAL_FIELDS = ("api_key", "apiKey", "api_token", "apiToken", "token", "key")

#: How deep to search the JSON for one of those fields. The file may well be
#: flat, but a wrapper like ``{"default": {...}}`` costs nothing to survive.
CLI_CREDENTIAL_MAX_DEPTH = 3


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
                "Bright Data returned HTML, not parsed JSON; check that the zone "
                "can serve search results (a SERP API or Web Unlocker zone) and "
                "that brd_json=1 is on the URL"
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


# --------------------------------------------------------------------------- #
# Credential resolution
# --------------------------------------------------------------------------- #


def cli_credential_paths() -> list[Path]:
    """Where the Bright Data CLI may have stored its key, per platform."""
    home = Path.home()
    if sys.platform == "darwin":
        roots = [home / "Library" / "Application Support"]
    elif os.name == "nt":
        appdata = os.environ.get("APPDATA")
        roots = [Path(appdata)] if appdata else []
    else:
        xdg = os.environ.get("XDG_CONFIG_HOME")
        roots = [Path(xdg)] if xdg else [home / ".config"]
    return [root / CLI_CONFIG_DIRNAME / CLI_CREDENTIALS_FILENAME for root in roots]


def _find_credential(node: Any, depth: int = 0) -> Optional[str]:
    """First credential-shaped string found in a decoded credentials file."""
    if depth > CLI_CREDENTIAL_MAX_DEPTH or not isinstance(node, dict):
        return None
    for field in CLI_CREDENTIAL_FIELDS:
        value = node.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    for value in node.values():
        found = _find_credential(value, depth + 1)
        if found:
            return found
    return None


def token_from_cli() -> Optional[str]:
    """Read the key left behind by ``brightdata login``, if there is one.

    Best-effort by design: the CLI's credential file format is not documented,
    so a missing file, bad JSON, a shape this does not recognise, or a
    permissions error all mean "not configured this way" -- never an error of
    its own. The caller still reports a clear failure if nothing turns up
    anywhere.
    """
    for path in cli_credential_paths():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        token = _find_credential(payload)
        if token:
            # Never log the value itself.
            log.info("using Bright Data credentials from %s", path)
            return token
    return None


def resolve_zone(serp_zone: str = "") -> str:
    """The zone to send requests through: the SERP zone, else the unlocker one.

    Mirrors Bright Data's own CLI so a machine set up for it needs nothing
    extra here. Returns "" when neither is configured, which the provider
    turns into a NewsFetchError naming both.
    """
    return (
        serp_zone.strip()
        or os.environ.get(CLI_UNLOCKER_ENV_VAR, "").strip()
    )


def resolve_token(api_token: str = "") -> Optional[str]:
    """Settings first, then the CLI's own env var, then its stored login."""
    return api_token or os.environ.get(CLI_ENV_VAR, "").strip() or token_from_cli()


class BrightDataNewsProvider:
    def __init__(self, api_token: str, zone: str, client: httpx.Client | None = None) -> None:
        token = resolve_token(api_token)
        if not token:
            raise NewsFetchError(
                "No Bright Data credentials found: set BRIGHTDATA_API_TOKEN, "
                "or run `brightdata login`"
            )
        resolved_zone = resolve_zone(zone)
        if not resolved_zone:
            raise NewsFetchError(
                "No Bright Data zone configured: set BRIGHTDATA_SERP_ZONE, or "
                f"{CLI_UNLOCKER_ENV_VAR} if you are using the zone "
                "`brightdata login` created (cli_unlocker)"
            )
        self._token = token
        self._zone = resolved_zone
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
