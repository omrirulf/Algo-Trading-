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
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from datetime import date, timedelta
from urllib.parse import urlencode

from config.instruments import is_fund

import httpx

log = logging.getLogger(__name__)

BRIGHTDATA_REQUEST_URL = "https://api.brightdata.com/request"

#: Where a relative result link is relative *to*. Google's news results often
#: carry their own redirect stub (``/goto?url=...``) rather than the
#: publisher's URL, and the parser hands it back with no origin -- which makes
#: it a dead link anywhere outside a google.com page. The first live cycle
#: stored 100 of 176 links in that shape.
GOOGLE_ORIGIN = "https://www.google.com"

#: Google ``tbs=qdr:`` window. ``d`` = past 24 hours, which suits a daily job.
NEWS_LOOKBACK = "d"
MAX_HEADLINES = 10
REQUEST_TIMEOUT_SECONDS = 60.0
#: One more try after a transport failure (a read timeout, a dropped
#: connection), after this pause. On 17 Sep two names lost their day to a
#: single timed-out read. An HTTP error is never retried: a 401 or a 429
#: says the same thing twice.
RETRY_PAUSE_SECONDS = 2.0

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


def _date_window(on: date) -> str:
    """Google's custom date range: the day before the signal through the day.

    ``cdr:1`` switches the ``tbs`` parameter from a rolling window to explicit
    bounds, in US month/day/year. Two days rather than one because a story
    filed late the previous evening is what the market opened on, and
    because a single day of an old index is often empty. Nothing dated after
    ``on`` can match, which is the whole point.
    """
    start = on - timedelta(days=1)
    return f"cdr:1,cd_min:{start.month}/{start.day}/{start.year},cd_max:{on.month}/{on.day}/{on.year}"


def build_news_search_url(ticker: str, on: Optional[date] = None) -> str:
    """Google News URL for one ticker.

    The qualifier differs by instrument because the query is what decides
    whether the headlines are about the right thing. ``"SPY stock"`` drags in
    single-stock coverage that mentions the index in passing; ``"SPY ETF"``
    returns the fund and macro commentary, which is the only frame an index
    signal can honestly be built on.

    ``on`` asks for stories as of a past date instead of the past 24 hours --
    the historical replay's way of rebuilding what the model would have seen.
    """
    qualifier = "ETF" if is_fund(ticker) else "stock"
    params = {
        "q": f"{ticker} {qualifier}",
        "tbm": "nws",
        "tbs": _date_window(on) if on is not None else f"qdr:{NEWS_LOOKBACK}",
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


@dataclass(frozen=True)
class Headline:
    """One news result, including the link the prompt line leaves out.

    ``as_line()`` is what the model is shown, and it is deliberately
    byte-identical to the string this module has always produced. The prompt
    is the input every replay and sanity baseline was measured against, so
    carrying a new field into the journal must not change one character of
    it -- and the model is never handed a URL it cannot open anyway.

    ``url`` exists for the reader: a person reviewing a signal afterwards
    needs to be able to open the story the model scored, and a headline with
    no source to check is an assertion rather than evidence.
    """

    title: str
    snippet: str = ""
    source: str = ""
    when: str = ""
    url: str = ""

    def as_line(self) -> str:
        """The prompt line: ``title — snippet (source, when)``."""
        line = self.title
        if self.snippet:
            line += f" — {self.snippet}"
        meta = ", ".join(x for x in (self.source, self.when) if x)
        if meta:
            line += f" ({meta})"
        return line

    def as_dict(self) -> dict[str, str]:
        """Plain JSON-serialisable form, for the signal journal."""
        return {
            "title": self.title,
            "snippet": self.snippet,
            "source": self.source,
            "when": self.when,
            "url": self.url,
        }


def absolute_url(url: str) -> str:
    """Give a result link an origin, so it is clickable away from google.com.

    Google's redirect stub carries an encrypted payload -- decoding it locally
    yields no readable URL -- so the publisher's address cannot be recovered
    without a round trip per headline, which a 35-ticker cycle cannot afford.
    Pointing the link back at Google's own resolver is the honest fix: one
    click still lands on the story, and the journal stops recording links that
    go nowhere.
    """
    url = (url or "").strip()
    if not url or url.startswith(("http://", "https://")):
        return url
    if url.startswith("//"):  # protocol-relative
        return "https:" + url
    if url.startswith("/"):
        return GOOGLE_ORIGIN + url
    return f"{GOOGLE_ORIGIN}/{url}"


def parse_news_items(payload: Any, limit: int = MAX_HEADLINES) -> list[Headline]:
    """Turn a Bright Data parsed-Google payload into ``Headline`` records.

    Deduplicated by title, because the same story syndicated across three
    outlets is one piece of evidence, not three.
    """
    data = _unwrap(payload)
    items: list[Any] = []
    for key in _RESULT_KEYS:
        value = data.get(key)
        if isinstance(value, list) and value:
            items = value
            break

    out: list[Headline] = []
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            continue
        title = _first(item, "title")
        if not title or title.lower() in seen:
            continue
        seen.add(title.lower())
        out.append(
            Headline(
                title=title,
                snippet=_first(item, "description", "snippet"),
                source=_first(item, "source", "source_name", "display_link"),
                when=_first(item, "date", "time", "published", "age"),
                url=absolute_url(_first(item, "link", "url", "source_link")),
            )
        )
        if len(out) >= limit:
            break
    return out


def parse_news_results(payload: Any, limit: int = MAX_HEADLINES) -> list[str]:
    """The same results as ``parse_news_items``, rendered as prompt lines."""
    return [h.as_line() for h in parse_news_items(payload, limit)]


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


def resolve_zone(serp_zone: str = "", unlocker_zone: str = "") -> str:
    """The zone to send requests through: the SERP zone, else the unlocker one.

    Mirrors Bright Data's own CLI so a machine set up for it needs nothing
    extra here. Returns "" when neither is configured, which the provider
    turns into a NewsFetchError naming both.

    ``unlocker_zone`` falls back to the environment so the CLI's own variable
    keeps working, then to the configured default. The SERP zone must be
    genuinely unset for the fallback to fire -- which is why it no longer
    defaults to a zone name.
    """
    explicit = serp_zone.strip()
    if explicit:
        return explicit
    from_env = os.environ.get(CLI_UNLOCKER_ENV_VAR, "").strip()
    return from_env or unlocker_zone.strip()


def resolve_token(api_token: str = "") -> Optional[str]:
    """Settings first, then the CLI's own env var, then its stored login.

    Stripped, because a token pasted into a secrets form with a trailing
    newline is sent as ``Bearer abc...\n`` and refused as invalid -- and the
    401 gives no hint that the value was one character away from right. The
    first live exercise of this path failed on exactly a 401.
    """
    return (api_token or "").strip() or os.environ.get(CLI_ENV_VAR, "").strip() or token_from_cli()


class BrightDataNewsProvider:
    def __init__(
        self,
        api_token: str,
        zone: str,
        client: httpx.Client | None = None,
        unlocker_zone: str = "",
    ) -> None:
        token = resolve_token(api_token)
        if not token:
            raise NewsFetchError(
                "No Bright Data credentials found: set BRIGHTDATA_API_TOKEN, "
                "or run `brightdata login`"
            )
        resolved_zone = resolve_zone(zone, unlocker_zone)
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

    def _post_with_one_retry(self, body: dict[str, Any]) -> httpx.Response:
        try:
            return self._post(body)
        except httpx.TransportError as exc:
            log.warning("Bright Data transport error (%s); retrying once", type(exc).__name__)
            time.sleep(RETRY_PAUSE_SECONDS)
            return self._post(body)

    def fetch_items(self, ticker: str) -> list[Headline]:
        """Headlines from the past 24 hours, with their links -- the live path."""
        return self._fetch_items(build_news_search_url(ticker))

    def fetch(self, ticker: str) -> list[str]:
        """The same headlines as prompt lines, for callers that want only text."""
        return [h.as_line() for h in self.fetch_items(ticker)]

    def fetch_on(self, ticker: str, day: date) -> list[str]:
        """Headlines as of a past date -- the historical replay's path.

        Same request, same parser, same zone; only the date window differs.
        What comes back is what Google still indexes for that day, which is
        sparser than the day's real coverage and biased towards stories that
        lasted. The caller counts empty results rather than hiding them.
        """
        return [h.as_line() for h in self._fetch_items(build_news_search_url(ticker, on=day))]

    def _fetch_items(self, url: str) -> list[Headline]:
        body = {"zone": self._zone, "url": url, "format": "raw"}
        try:
            resp = self._post_with_one_retry(body)
        except httpx.HTTPError as exc:
            raise NewsFetchError(f"Bright Data unreachable: {exc}") from exc
        if resp.status_code != 200:
            raise NewsFetchError(f"Bright Data HTTP {resp.status_code}: {resp.text[:300]}")
        return parse_news_items(resp.text)
