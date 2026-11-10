"""Recent news for a ticker via Bright Data's SERP API (Google News).

Request shape (from Bright Data's own SDK and MCP server): POST
``https://api.brightdata.com/request`` with a Bearer token and a JSON body of
``{zone, url, format: "raw", country: "us"}``. Appending ``brd_json=1`` to a
Google URL makes Bright Data return the parsed result set as JSON instead of
HTML; ``country`` is the exit the request leaves from (``BRD_COUNTRY``).

The token can come from ``BRIGHTDATA_API_TOKEN``, from the ``BRIGHTDATA_API_KEY``
env var the official CLI reads, or from the key ``brightdata login`` stores
after its OAuth flow -- in that order. Reading the CLI's file is best-effort:
its format is not documented, so the lookup tries several field names and
treats anything it cannot make sense of as "not configured this way".

When Google's answer is unusable after the retries below (a second refused
200, an HTTP error, a transport failure after its retry), the live path asks
Bing News for the same name: its RSS feed of the past 24 hours, directly
first (no token, a fraction of a second) and through Bright Data if the
direct ask fails, kept to the headlines that name the ticker or the company
(``relevant_headlines``). The owner's decision of 4 Nov 2026 after the probe
of the same day (``replay/bing_news_probe.py``), logged in the
pre-registration's Amendments table; the Google request, its parser and the
model's prompt are unchanged, and the journal says when a name's headlines
came this way (``NewsAnswer.fallback``).

This module has no credentials other than the Bright Data token and never
talks to the broker or the execution engine.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sys
import threading
import time
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Iterable, Optional
from datetime import date, datetime, timedelta, timezone
from urllib.parse import urlencode
from xml.etree import ElementTree

from config.instruments import DISPLAY_NAMES, NEWS_THEMES, is_fund

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
#: One more try after a 200 the parser refused (an empty body, a block page),
#: after this longer pause. The empty 200s come from the vendor's side in
#: bursts (6 Oct 2026: 44 of 80 first answers; 15 Oct: 60, and 53 of the
#: second asks two seconds later were empty again), so the second ask waits
#: long enough for a burst to pass. The owner's decision of 16 Oct 2026.
EMPTY_RETRY_PAUSE_SECONDS = 10.0
#: Bright Data's own headers on an answer: the target's status code and the
#: reason it gives when it refuses. Written into the warning and into the
#: error a second refused 200 leaves in the journal, so the record says what
#: the vendor said and not only that the body was empty (the owner's
#: decision of 16 Oct 2026). Never a credential: these are status headers.
BRD_HEADERS = ("x-brd-status-code", "x-brd-err-code", "x-brd-err-msg", "x-brd-error", "x-luminati-error")
#: The exit country of the request (``"country": "us"`` in the body). Google
#: answers a search from a non-US exit with a redirect (its consent or
#: regional page) that the Unlocker refuses: ``x-brd-status-code 502;
#: x-brd-error redirect location was rejected`` was every empty 200 the
#: probe of 16 Oct 2026 read (``replay/serp_zone_probe.py``), and those
#: empties cost 22 names their news on 6 Oct and 55 on 15 Oct. The same
#: request from a US exit came back empty 2 times of 20 against 5 of 20
#: without it. The owner's decision of 17 Oct 2026; the search URL, the
#: zone and the parser are unchanged.
BRD_COUNTRY = "us"

#: Keys under which Bright Data's Google parser may put result items. ``news``
#: is the news-tab list; ``organic`` is the fallback if the zone returns a
#: regular SERP for the same query.
_RESULT_KEYS = ("news", "top_stories", "organic")

#: Bing News publishes the same search as an RSS feed, with no consent page.
#: The fallback when Google's answer is unusable after the retries above: the
#: owner's decision of 4 Nov 2026, after the probe of the same day
#: (``replay/bing_news_probe.py``, 30 names, two runs). Production's request
#: answered 24 of 30 names each run (4 "redirect location was rejected", 2
#: empty, different names each run); the feed answered all 30, directly from
#: the runner in 0.2 s and through Bright Data in 1.8 s, against 5 s for the
#: Google request. The feed is asked directly first and through Bright Data
#: only if that fails (one connection error in 60 direct asks that day).
BING_NEWS_URL = "https://www.bing.com/news/search"
#: Bing's own "past 24 hours" filter, as its news page sends it: Google's
#: ``qdr:d`` window. Without it the feed's newest story was a day old at the
#: median and its oldest more than a year.
BING_LAST_24H = 'interval="7"'
#: A browser's name: Bing answers an empty client name with a block page.
BING_USER_AGENT = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/129.0 Safari/537.36")
#: The direct ask's budget. The one direct ask that failed on 4 Nov hung
#: for 29 s before its connection error; the Bright Data route waits behind.
BING_DIRECT_TIMEOUT_SECONDS = 20.0
#: The guard on the feed. With the filter on, its answer for a thin fund was
#: mostly about other things (for DBA on 4 Nov: a country music festival, a
#: town's pool bond, a Senate race; one title in five named the fund across
#: the 14 funds, against three in four for the 16 companies), so a headline
#: is kept only when its title or snippet names the ticker or, for a
#: company, a word of its display name -- or, since 10 Nov 2026, for a fund
#: one of the words a story about what it holds would use
#: (``config.instruments.NEWS_THEMES``): on 9 and 10 Nov the ticker alone
#: left 11 and then 14 funds without news while the feed had stories for
#: most of them. Words shorter than this, and these generic ones, name no
#: company on their own.
NAME_WORD_MIN_LENGTH = 4
GENERIC_NAME_WORDS = frozenset({
    "bank", "systems", "canada", "pharmaceutical", "pharmaceuticals", "royal", "company", "group",
    "holdings", "corp", "corporation", "inc", "the", "and", "of",
})


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


def brd_headers(response: Any) -> str:
    """Bright Data's own headers on ``response``, as one string; empty when it sent none.

    ``x-brd-status-code 502; x-brd-err-msg ...`` -- the vendor's account of a
    200 that carried nothing, read from the HTTP answer itself (with
    ``format: raw`` the body is the target's, the headers are Bright Data's).
    """
    headers = getattr(response, "headers", None) or {}
    said = [f"{name} {headers.get(name)}" for name in BRD_HEADERS if headers.get(name)]
    return "; ".join(said)


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
        if not stripped:
            # 18 Sep 2026: TM lost its day to this, and the message it left in
            # the journal was "Expecting value: line 1 column 1 (char 0)" --
            # json's way of saying the string was empty, which reads like a
            # parser bug rather than an empty 200 from the vendor. Say what
            # actually arrived.
            raise NewsFetchError(
                "Bright Data returned an empty body with its 200; nothing to parse"
            )
        try:
            payload = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise NewsFetchError(
                f"Bright Data response is not JSON ({len(stripped)} bytes, "
                f"starts {stripped[:40]!r}): {exc}"
            ) from exc
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


# --------------------------------------------------------------------------- #
# Bing's feed: the fallback (the owner's decision of 4 Nov 2026)
# --------------------------------------------------------------------------- #


def build_bing_news_url(ticker: str, last_24h: bool = True) -> str:
    """Bing News RSS for ``ticker``, with the Google search's qualifier ("stock", or "ETF" for a fund).

    The live path always asks with the past-24-hours filter; the probe can
    ask without it, to measure the difference.
    """
    qualifier = "ETF" if is_fund(ticker) else "stock"
    params: dict[str, Any] = {"q": f"{ticker} {qualifier}", "format": "rss", "setlang": "en-US", "cc": "US"}
    if last_24h:
        params["qft"] = BING_LAST_24H
    return f"{BING_NEWS_URL}?{urlencode(params)}"


def _feed_text(element: Optional[ElementTree.Element]) -> str:
    return (element.text or "").strip() if element is not None else ""


def _feed_child(item: ElementTree.Element, local: str) -> Optional[ElementTree.Element]:
    """A child by its local name, whatever namespace the feed put it in (Bing's carries the query)."""
    for child in item:
        if child.tag.rsplit("}", 1)[-1] == local:
            return child
    return None


def _age_hours(published: str, now: Optional[datetime] = None) -> Optional[float]:
    try:
        stamp = parsedate_to_datetime(published)
    except (TypeError, ValueError, IndexError):
        return None
    if stamp.tzinfo is None:
        stamp = stamp.replace(tzinfo=timezone.utc)
    return max(0.0, ((now or datetime.now(timezone.utc)) - stamp).total_seconds() / 3600.0)


@dataclass(frozen=True)
class BingStory:
    """One feed item as a ``Headline``, with the story's age for whoever measures the feed."""

    headline: Headline
    age_hours: Optional[float]


def parse_bing_rss(text: str, limit: int = MAX_HEADLINES, now: Optional[datetime] = None) -> list[BingStory]:
    """The feed's items as ``Headline`` records (title, snippet, source, when, url), newest first.

    Deduplicated by title, as ``parse_news_items`` is. Raises
    ``NewsFetchError`` on anything that is not an RSS document (a block page,
    an empty body), so the fallback judges it the way the Google path judges
    its answers.
    """
    stripped = (text or "").strip()
    if not stripped:
        raise NewsFetchError("Bing returned an empty body")
    if not stripped.startswith("<"):
        raise NewsFetchError(f"Bing returned something that is not XML (starts {stripped[:30]!r})")
    try:
        root = ElementTree.fromstring(stripped)
    except ElementTree.ParseError as exc:
        raise NewsFetchError(f"Bing returned XML the parser refused: {exc}") from exc
    items = root.findall(".//item")
    if root.tag.lower() != "rss" and not items:
        raise NewsFetchError(f"Bing returned <{root.tag}>, not an RSS feed")
    out: list[BingStory] = []
    seen: set[str] = set()
    for item in items:
        title = _feed_text(_feed_child(item, "title"))
        if not title or title.lower() in seen:
            continue
        seen.add(title.lower())
        published = _feed_text(_feed_child(item, "pubDate"))
        age = _age_hours(published, now)
        when = f"{age:.0f}h ago" if age is not None else published
        snippet = re.sub(r"\s+", " ", _feed_text(_feed_child(item, "description")))
        out.append(BingStory(Headline(title=title, snippet=snippet, source=_feed_text(_feed_child(item, "Source")),
                                      when=when, url=_feed_text(_feed_child(item, "link"))), age))
        if len(out) >= limit:
            break
    return out


def name_words(ticker: str) -> tuple[str, ...]:
    """The words a headline about the name would carry.

    The ticker; for a company the distinctive words of its name; for a fund
    the words a story about what it holds would use (``NEWS_THEMES``: a
    fund's display name describes it, "Commodities basket", and names
    nothing a headline would say).
    """
    words: list[str] = [ticker]
    if is_fund(ticker):
        words.extend(NEWS_THEMES.get(ticker, ()))
    else:
        name = DISPLAY_NAMES.get(ticker, "")
        for word in re.findall(r"[A-Za-z][A-Za-z'-]*", name):
            clean = word.strip("'-")
            if len(clean) >= NAME_WORD_MIN_LENGTH and clean.lower() not in GENERIC_NAME_WORDS:
                words.append(clean)
        if len(name.split()) > 1:
            words.append(name)
    return tuple(dict.fromkeys(words))


def _names(text: str, word: str, exact: bool) -> bool:
    """Whether ``text`` carries ``word`` as a whole word: the ticker as written (and not as the start of PG&E), a name in any case."""
    tail = r"(?![A-Za-z0-9&])" if exact else r"(?![A-Za-z0-9])"
    pattern = rf"(?<![A-Za-z0-9]){re.escape(word)}{tail}"
    return re.search(pattern, text, 0 if exact else re.IGNORECASE) is not None


def relevant_headlines(ticker: str, headlines: Iterable[Headline]) -> list[Headline]:
    """The headlines whose title or snippet name the ticker or, for a company, a word of its name."""
    words = name_words(ticker)
    kept: list[Headline] = []
    for headline in headlines:
        text = f"{headline.title} {headline.snippet}"
        if _names(text, ticker, True) or any(_names(text, word, False) for word in words[1:]):
            kept.append(headline)
    return kept


@dataclass(frozen=True)
class NewsAnswer:
    """What the live path hands the cycle: the headlines, and a note when they are not Google's."""

    headlines: list[Headline]
    #: Empty when Google answered. Otherwise why Bing's feed was asked, which
    #: route answered and how many of its headlines named the name: the
    #: journal's record of the fallback (``context.news_note``).
    fallback: str = ""


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


#: Requests sent to Bright Data by each thread, for a caller that pays per
#: request: the shadow universe charges every one to its daily cost cap
#: (``orchestrator/universe.py``). Counted when sent, whatever comes back, so
#: the count never understates what may be billed. Production reads nothing
#: here; the requests themselves are unchanged.
_SENT = threading.local()


def requests_sent() -> int:
    """How many requests the calling thread has sent to Bright Data so far."""
    return getattr(_SENT, "count", 0)


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
        _SENT.count = requests_sent() + 1
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

    def fetch_answer(self, ticker: str) -> NewsAnswer:
        """Headlines from the past 24 hours, with their links -- the live path.

        Google's, through Bright Data, with the retries of ``_fetch_items``;
        when its answer is unusable even so, Bing's feed kept to the
        headlines that name the name (``_bing_fallback``), and the answer
        says so. Raises ``NewsFetchError`` when neither gives the name a
        headline, with both reasons, so the cycle records a gap as before.
        """
        try:
            return NewsAnswer(self._fetch_items(build_news_search_url(ticker)))
        except NewsFetchError as google:
            return self._bing_fallback(ticker, google)

    def fetch_items(self, ticker: str) -> list[Headline]:
        """The live path's headlines, with their links, for callers that keep no note."""
        return self.fetch_answer(ticker).headlines

    def fetch(self, ticker: str) -> list[str]:
        """The same headlines as prompt lines, for callers that want only text."""
        return [h.as_line() for h in self.fetch_items(ticker)]

    def _get(self, url: str) -> httpx.Response:
        """A plain GET, not through Bright Data: nothing billed, nothing counted, no token sent."""
        headers = {"User-Agent": BING_USER_AGENT, "Accept": "application/rss+xml, text/xml"}
        if self._client is not None:
            return self._client.get(url, headers=headers)
        with httpx.Client(timeout=BING_DIRECT_TIMEOUT_SECONDS, follow_redirects=True) as client:
            return client.get(url, headers=headers)

    def _bing_stories(self, route: str, url: str) -> list[BingStory]:
        """The feed by one route. Raises ``NewsFetchError`` (with Bright Data's headers on its route) or ``httpx.HTTPError``."""
        if route == "direct":
            resp = self._get(url)
        else:
            resp = self._post_with_one_retry({"zone": self._zone, "url": url, "format": "raw", "country": BRD_COUNTRY})
        said = brd_headers(resp) if route != "direct" else ""
        if resp.status_code != 200:
            raise NewsFetchError(f"HTTP {resp.status_code}" + (f" (Bright Data said: {said})" if said else ""))
        try:
            return parse_bing_rss(resp.text)
        except NewsFetchError as exc:
            if said:
                raise NewsFetchError(f"{exc} (Bright Data said: {said})") from exc
            raise

    def _bing_fallback(self, ticker: str, google: NewsFetchError) -> NewsAnswer:
        """Bing's past-24-hours feed for ``ticker``, directly then through Bright Data, kept to the name.

        A name with at least one headline left is judged on those, and the
        answer's note says so. A name with none left raises, like before the
        fallback: the prompt says "unavailable this cycle" and the journal
        keeps a gap naming Google's reason and the feed's count.
        """
        url = build_bing_news_url(ticker)
        failures: list[str] = []
        for route in ("direct", "Bright Data"):
            try:
                stories = self._bing_stories(route, url)
            except httpx.HTTPError as exc:
                failures.append(f"{route}: {type(exc).__name__}")
                continue
            except NewsFetchError as exc:
                failures.append(f"{route}: {exc}")
                continue
            kept = relevant_headlines(ticker, [story.headline for story in stories])
            if not kept:
                raise NewsFetchError(f"{google} (Bing's feed, {route}: {len(stories)} headline(s), "
                                     f"none naming {ticker})") from google
            note = (f"news from Bing's feed ({route}) after Google: {google}; "
                    f"{len(kept)} of {len(stories)} headline(s) name {ticker}")
            log.warning("%s: %s", ticker, note)
            return NewsAnswer(kept, note)
        raise NewsFetchError(f"{google} (Bing's feed also failed: {'; '.join(failures)})") from google

    def fetch_on(self, ticker: str, day: date) -> list[str]:
        """Headlines as of a past date -- the historical replay's path.

        Same request, same parser, same zone; only the date window differs.
        What comes back is what Google still indexes for that day, which is
        sparser than the day's real coverage and biased towards stories that
        lasted. The caller counts empty results rather than hiding them. No
        Bing fallback here: the feed has no window for a past day.
        """
        return [h.as_line() for h in self._fetch_items(build_news_search_url(ticker, on=day))]

    def _fetch_items(self, url: str) -> list[Headline]:
        body = {"zone": self._zone, "url": url, "format": "raw", "country": BRD_COUNTRY}
        try:
            resp = self._post_with_one_retry(body)
        except httpx.HTTPError as exc:
            raise NewsFetchError(f"Bright Data unreachable: {exc}") from exc
        if resp.status_code != 200:
            raise NewsFetchError(f"Bright Data HTTP {resp.status_code}: {resp.text[:300]}")
        try:
            return parse_news_items(resp.text)
        except NewsFetchError as exc:
            first_refusal = exc
        # A 200 the parser refuses is an interstitial, a block page or an
        # upstream error wrapped in a 200, and on 18 Sep one cost TM its
        # day. Once more, after the longer pause; a second one is real, and
        # it carries whatever Bright Data's own headers said about it.
        said = brd_headers(resp)
        log.warning("Bright Data answered 200 with something the parser refused (%s)%s; "
                    "retrying once after %.0f s",
                    str(first_refusal)[:80], f" [{said}]" if said else "", EMPTY_RETRY_PAUSE_SECONDS)
        time.sleep(EMPTY_RETRY_PAUSE_SECONDS)
        try:
            resp = self._post(body)
        except httpx.HTTPError as exc:
            raise NewsFetchError(f"Bright Data unreachable: {exc}") from exc
        if resp.status_code != 200:
            raise NewsFetchError(f"Bright Data HTTP {resp.status_code}: {resp.text[:300]}")
        try:
            return parse_news_items(resp.text)
        except NewsFetchError as exc:
            said = brd_headers(resp)
            if not said:
                raise
            raise NewsFetchError(f"{exc} (Bright Data said: {said})") from exc
