#!/usr/bin/env python3
"""One recorded context, with its articles fetched: what the model reads, and what it says.

    python replay/article_probe.py --dry-run
    python replay/article_probe.py --no-model
    python replay/article_probe.py --ticker NVO --day 2026-09-28
    python replay/article_probe.py --build-scraper
    python replay/article_probe.py --collector c_...        # build on (or use) a collector that exists
    python replay/article_probe.py --scraper-trigger 'https://api.brightdata.com/dca/trigger?collector=c_...'

The news block is a headline and Google's ~150-character snippet per result.
This asks, on one example, what changes when the model also gets the start of
each article: how many words that adds, how much of it is the story rather
than the page around it, and what the model then says and spends. It is a
feel for the idea before anything is built, not a test of it.

Where the text comes from
-------------------------
Two sources, side by side when both are asked for:

* **The Web Unlocker**, through the zone the news fetch already uses, with one
  generic article extractor (trafilatura) cutting the story out of the page.
  Every site goes through the same path.
* **A Scraper Studio scraper** for one site (``--site``). ``--build-scraper``
  has Scraper Studio's AI build one on the spot, from one of this line's
  article links, through the same API calls Bright Data's own CLI makes -- no
  dashboard, nothing to copy by hand -- and the report prints its trigger URL
  so a later run can reuse it with ``--scraper-trigger``. ``--collector``
  builds on a collector that exists instead of creating another. Its records are
  read whatever the fields were named: ``body`` if there is one, else the
  longest text. Bright Data's library of ready-made scrapers is looked up
  too, and any named for the site are listed.

Both are cut to the same number of words (``--words``) before the model sees
them, so a difference between the two is a difference in *which* words, not
in how many.

What the model is asked
-----------------------
The production call, unchanged -- the same system prompt, model, effort and
schema as ``orchestrator.heartbeat.call_llm`` -- on the same context rendered
several ways, each asked ``--repeats`` times:

* ``headlines``: the prompt exactly as recorded;
* ``unlocker``: every result that yielded an article gets its opening words,
  indented under its own headline;
* ``unlocker-named``: the same, but only the stories that name the company --
  asked when some do not, because a result about another company is noise
  that no parser removes;
* ``unlocker+scraper``: the Unlocker's text, plus the scraper's for the pages
  the Unlocker could not read -- the design a scraper would really be used
  in, asked when the scraper filled at least one;
* ``unlocker-site`` / ``scraper-site``: only the chosen site's results get
  them, from each source in turn, and only the results both sources read --
  so the pair differs in nothing but where the words came from.

What it cannot say
------------------
One context and a handful of calls show what the model reads and what it
costs. They cannot show that it trades better: that takes the saved-text test
at a checkpoint, over many contexts, scored against prices. The pages are
also fetched when this runs, not when the line was written, so a story edited
since then is read as it is now.

Same guarantees as the rest of replay/: it reads the journal, fetches pages,
asks the model and prints. No broker keys, no journal write, no order path.
"""

from __future__ import annotations

import argparse
import html as html_lib
import json
import logging
import re
import sys
import time
import textwrap
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, replace
from pathlib import Path
from statistics import mean
from typing import Any, Callable, Optional
from urllib.parse import urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

from config import journal_files  # noqa: E402
from config import settings as cfg  # noqa: E402
from config.instruments import is_fund, name_for  # noqa: E402
from orchestrator import news  # noqa: E402
from orchestrator.context import TickerContext  # noqa: E402
from orchestrator.heartbeat import build_user_prompt, parse_signal, system_prompt_for  # noqa: E402
from orchestrator.llm import Completion  # noqa: E402
from replay import runner  # noqa: E402
from replay.runner import ReplayEntry  # noqa: E402

log = logging.getLogger("article_probe")

DEFAULT_SITE = "finance.yahoo.com"
#: About a minute of reading, and enough for the lede and the numbers under it.
DEFAULT_WORDS = 300
DEFAULT_REPEATS = 2
#: Without --ticker or --day, the most recent single-stock line with at least
#: this many article links on the site, so the scraper has something to read.
MIN_SITE_LINKS = 2

#: One page through the Unlocker. Slow sites take tens of seconds.
UNLOCKER_TIMEOUT_SECONDS = 90.0
FETCH_WORKERS = 4
MODEL_WORKERS = 4

#: The scraper runs as a job: triggered, then collected once it is done.
SCRAPER_DEADLINE_SECONDS = 600.0
SCRAPER_POLL_SECONDS = 10.0

#: The only host the Bright Data token is ever sent to. A scraper trigger URL
#: comes from a person, so it is checked rather than trusted.
BRIGHTDATA_API = "https://api.brightdata.com/"

#: How a result's link is treated.
ARTICLE = "article"
GOOGLE_REDIRECT = "google redirect"
NOT_AN_ARTICLE = "not an article"
NO_LINK = "no link"

#: Pages with nothing to read: quotes, charts, symbol pages, filings, videos.
NOT_ARTICLE_PATH = re.compile(r"/(?:quote|chart|symbols?|sec-filings|rankings)/|/videos?/", re.I)

#: A paragraph that is the page talking about itself rather than the story.
#: Crude on purpose, and reported as such: it counts words, it does not judge.
BOILERPLATE = re.compile(
    r"\b(?:sign up|subscribe|subscription|newsletter|log in|sign in|free trial|"
    r"create a free account|unlock|premium|cookie|advertisement|sponsored|"
    r"read more|click here|related (?:stories|articles|news)|recommended (?:stories|for you)|"
    r"story continues|view comments|see also|most popular|trending now|"
    r"all rights reserved|terms of (?:use|service)|privacy policy|copyright|"
    r"disclosure|has (?:no )?positions? in|this article was (?:originally )?published|"
    r"not investment advice|for informational purposes)\b",
    re.I,
)

#: Short text plus one of these on the page reads like a teaser, not a story.
PAYWALL = re.compile(
    r"subscribe to (?:read|continue)|to continue reading|subscribers? only|"
    r"premium (?:article|content|subscribers?)|sign in to (?:read|continue)|"
    r"register to (?:read|continue)|paywall",
    re.I,
)
PAYWALL_MAX_WORDS = 150

#: First words of a company name too common to count as naming it.
GENERIC_NAME_WORDS = frozenset({"royal", "bank", "first", "general", "united", "american", "the"})

#: Fields a scraper record's article text is looked for under, in order.
TEXT_FIELDS = (
    "body", "text", "content", "article_body", "article_text", "article",
    "paragraphs", "markdown",
)
#: Fields that are never the article text, however long they are.
META_FIELDS = frozenset({
    "url", "input", "input_url", "title", "headline", "author", "authors", "date",
    "published", "published_at", "date_published", "timestamp", "error", "error_code",
    "warning", "warning_code", "image", "images", "tags", "source", "domain",
})
#: Status values that mean "not ready yet" on either of Bright Data's job APIs.
PENDING = frozenset({"running", "building", "collecting", "starting", "pending", "queued", "in_progress"})

VARIANTS = ("headlines", "unlocker", "unlocker-named", "unlocker+scraper", "unlocker-site", "scraper-site")


# --------------------------------------------------------------------------- #
# Which line, and which of its links
# --------------------------------------------------------------------------- #


def host_of(url: str) -> str:
    host = urlsplit(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def on_site(url: str, site: str) -> bool:
    """Is ``url`` on ``site`` or one of its regional editions (``uk.``, ``ca.``, ...)?"""
    host, site = host_of(url), site.lower().removeprefix("www.")
    return bool(host) and (host == site or host.endswith("." + site))


def classify(url: str) -> str:
    """What a result's link is: an article, Google's redirect stub, or nothing to read."""
    if not url:
        return NO_LINK
    parts = urlsplit(url)
    if parts.netloc.lower().endswith("google.com") and parts.path.startswith(("/goto", "/url")):
        return GOOGLE_REDIRECT
    if NOT_ARTICLE_PATH.search(parts.path):
        return NOT_AN_ARTICLE
    return ARTICLE


def result_links(context: TickerContext) -> list[tuple[int, str, str]]:
    """``(index, source name, absolute url)`` for each result, in prompt order.

    The index is the headline's position, which is also its source's: the
    journal writes both lists from the same records in the same order.
    """
    return [
        (i, str(item.get("source") or ""), news.absolute_url(str(item.get("url") or "")))
        for i, item in enumerate(context.sources)
    ]


def site_indexes(context: TickerContext, site: str) -> list[int]:
    """The results on ``site`` that point at an article."""
    return [i for i, _, url in result_links(context) if classify(url) == ARTICLE and on_site(url, site)]


def usable(entry: ReplayEntry) -> bool:
    """A single stock whose headlines and sources line up one to one."""
    context = entry.context
    return (
        context is not None
        and not is_fund(entry.ticker)
        and bool(context.sources)
        and len(context.sources) == len(context.headlines)
    )


def pick(
    entries: list[ReplayEntry], site: str, ticker: Optional[str] = None,
    day: Optional[str] = None, min_site_links: int = MIN_SITE_LINKS,
) -> Optional[ReplayEntry]:
    """The line to probe: the most recent that fits.

    With neither ``ticker`` nor ``day`` named, the line must carry at least
    ``min_site_links`` articles on the site, or the scraper would have nothing
    to read. A line picked by name is taken as it is, and the report says how
    many site links it has.
    """
    wanted = (ticker or "").strip().upper()
    chosen = None
    for entry in entries:
        if not usable(entry):
            continue
        if wanted and entry.ticker != wanted:
            continue
        if day and not str(entry.ts_utc or "").startswith(day):
            continue
        if not wanted and not day and len(site_indexes(entry.context, site)) < min_site_links:
            continue
        chosen = entry
    return chosen


# --------------------------------------------------------------------------- #
# Fetching through the Unlocker
# --------------------------------------------------------------------------- #


class Http:
    """The two calls this probe makes, as the seam a test replaces."""

    def __init__(self, timeout: float = UNLOCKER_TIMEOUT_SECONDS) -> None:
        self._timeout = timeout

    def post(self, url: str, body: Any, headers: dict[str, str]) -> Any:
        with httpx.Client(timeout=self._timeout) as client:
            return client.post(url, json=body, headers=headers)

    def get(self, url: str, headers: dict[str, str]) -> Any:
        with httpx.Client(timeout=self._timeout) as client:
            return client.get(url, headers=headers)


def _auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


@dataclass
class Page:
    """One result, as far as the Unlocker and the extractor got with it."""

    index: int
    source: str
    url: str
    kind: str
    final_url: str = ""
    status: Optional[int] = None
    page_bytes: int = 0
    requests: int = 0
    seconds: float = 0.0
    error: str = ""
    html: str = field(default="", repr=False)
    text: str = ""
    title: str = ""
    date: str = ""
    lede: Optional["Lede"] = None
    paywall: bool = False
    mentions: Optional[bool] = None

    @property
    def fetched(self) -> bool:
        return self.kind in (ARTICLE, GOOGLE_REDIRECT)


_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
_META_REFRESH = re.compile(
    r"""<meta[^>]+http-equiv=["']?refresh["']?[^>]*content=["'][^"']*?url=['"]?([^"'>\s]+)""", re.I
)
_JS_LOCATION = re.compile(
    r"""location(?:\.href)?\s*(?:=|\.replace\(|\.assign\()\s*["'](https?://[^"']+)["']""", re.I
)
_HREF = re.compile(r"""<a[^>]+href=["'](https?://[^"']+)["']""", re.I)


def _looks_like_google(page: str) -> bool:
    title = _TITLE.search(page[:20000])
    heading = (title.group(1) if title else "").lower()
    return "google" in heading or "redirect notice" in page[:20000].lower()


def redirect_target(page: str) -> Optional[str]:
    """Where Google's redirect page sends the reader, if this is one.

    ``None`` when the page is not Google's -- the Unlocker already followed
    the redirect and this is the story itself -- or when no destination can
    be read off it.
    """
    if not page or not _looks_like_google(page):
        return None
    for pattern in (_META_REFRESH, _JS_LOCATION, _HREF):
        for match in pattern.finditer(page):
            target = html_lib.unescape(match.group(1))
            if target.startswith("http") and not host_of(target).endswith("google.com"):
                return target
    return None


def brief(body: str, limit: int = 200) -> str:
    """An error body on one line: tags stripped, whitespace folded.

    A gateway's error page is HTML, and its newlines broke the report's table
    on the first real run.
    """
    return " ".join(re.sub(r"<[^>]+>", " ", body or "").split())[:limit]


#: Where Bright Data says why a request failed, when it does: the news fetch
#: reads the first two, Bright Data's CLI the second and third.
BRD_ERROR_HEADERS = ("x-brd-err-msg", "x-brd-error", "x-luminati-error", "x-brd-err-code")


def brd_reason(response: Any) -> str:
    """Bright Data's own words for a failure, from its headers; empty when it gave none."""
    headers = getattr(response, "headers", None) or {}
    said = [str(headers.get(name)) for name in BRD_ERROR_HEADERS if headers.get(name)]
    return "; ".join(dict.fromkeys(said))


def _unlock(http: Http, token: str, zone: str, url: str) -> tuple[int, str, str]:
    """``(status, body, error)`` for one page through the Unlocker."""
    response = http.post(news.BRIGHTDATA_REQUEST_URL, {"zone": zone, "url": url, "format": "raw"},
                         _auth(token))
    status = int(response.status_code)
    body = response.text or ""
    if status != 200:
        reason = brd_reason(response) or brief(body)
        return status, "", f"HTTP {status} {reason}".strip()
    return status, body, ""


def fetch_page(http: Http, token: str, zone: str, index: int, source: str, url: str) -> Page:
    """One result's page, following Google's redirect stub once if that is what it is. Never raises."""
    page = Page(index=index, source=source, url=url, kind=classify(url))
    if not page.fetched:
        return page
    started = time.monotonic()
    try:
        page.status, page.html, page.error = _unlock(http, token, zone, url)
        page.requests = 1
        page.final_url = url
        if page.kind == GOOGLE_REDIRECT and page.html:
            target = redirect_target(page.html)
            if target:
                page.final_url = target
                page.status, page.html, page.error = _unlock(http, token, zone, target)
                page.requests = 2
            elif _looks_like_google(page.html):
                page.error = "Google's redirect page, and no destination could be read off it"
                page.html = ""
    except httpx.HTTPError as exc:
        page.error = f"{type(exc).__name__}: {exc}"[:200]
        page.html = ""
    page.page_bytes = len(page.html.encode("utf-8"))
    page.seconds = time.monotonic() - started
    return page


def fetch_all(http: Http, token: str, zone: str, context: TickerContext,
              workers: int = FETCH_WORKERS) -> list[Page]:
    links = result_links(context)
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        return list(pool.map(lambda link: fetch_page(http, token, zone, *link), links))


# --------------------------------------------------------------------------- #
# From a page to the words the model would read
# --------------------------------------------------------------------------- #


#: ``(html, url) -> (text, title, date)``. trafilatura unless a test says otherwise.
Extractor = Callable[[str, str], tuple[str, str, str]]


def trafilatura_extract(page: str, url: str) -> tuple[str, str, str]:
    """The story cut out of the page: text, title and date, empty when there is none.

    Imported here rather than at the top so the rest of the probe, and the
    suite, need nothing that production does not already install.
    """
    import trafilatura

    document = trafilatura.bare_extraction(
        page, url=url or None, include_comments=False, include_tables=False, with_metadata=True,
    )
    if document is None:
        return "", "", ""
    found = document.as_dict() if hasattr(document, "as_dict") else dict(document)
    return str(found.get("text") or ""), str(found.get("title") or ""), str(found.get("date") or "")


def paragraphs(text: str, title: str = "") -> list[str]:
    """The text's paragraphs, whitespace folded, repeats dropped.

    A first paragraph that only repeats the title is dropped too: the
    headline is already in the prompt, one line above.
    """
    out: list[str] = []
    seen: set[str] = set()
    heading = " ".join(title.split()).lower()
    for raw in text.splitlines():
        paragraph = " ".join(raw.split())
        key = paragraph.lower()
        if not paragraph or key in seen:
            continue
        if not out and heading and key == heading:
            continue
        seen.add(key)
        out.append(paragraph)
    return out


@dataclass(frozen=True)
class Lede:
    """The opening words of one article, as the model would get them."""

    text: str
    words: int
    #: Of ``words``, how many sit in paragraphs that look like page furniture.
    boilerplate_words: int
    #: The whole article's length, before the cut.
    article_words: int

    @property
    def boilerplate_share(self) -> float:
        return self.boilerplate_words / self.words if self.words else 0.0


def lede_of(parts: list[str], limit: int) -> Optional[Lede]:
    """The first ``limit`` words, paragraph by paragraph. ``None`` for an empty article."""
    kept: list[str] = []
    count = boiler = 0
    for paragraph in parts:
        room = limit - count
        if room <= 0:
            break
        words = paragraph.split()
        piece = words[:room]
        kept.append(" ".join(piece) + (" …" if len(words) > room else ""))
        count += len(piece)
        if BOILERPLATE.search(paragraph):
            boiler += len(piece)
    if not count:
        return None
    total = sum(len(p.split()) for p in parts)
    return Lede(text=" ".join(kept), words=count, boilerplate_words=boiler, article_words=total)


def company_terms(ticker: str) -> tuple[str, list[str]]:
    """The symbol, and the name words that count as naming the company."""
    name = name_for(ticker)
    base = re.sub(r"\(.*?\)", "", name).strip()
    names = [n for n in [base, *re.findall(r"\((.*?)\)", name)] if n]
    words = base.split()
    for word in (words[0] if words else "", words[-1] if len(words) > 1 else ""):
        if len(word) >= 4 and word.lower() not in GENERIC_NAME_WORDS:
            names.append(word)
    return ticker.upper(), names


def mentions_company(text: str, ticker: str) -> bool:
    """Does the text name the company at all? A crude check, reported as one."""
    symbol, names = company_terms(ticker)
    if re.search(rf"(?<![A-Za-z]){re.escape(symbol)}(?![A-Za-z])", text):
        return True
    return any(re.search(rf"\b{re.escape(n)}\b", text, re.I) for n in names)


def paywall_suspected(text: str, page: str) -> bool:
    return len(text.split()) < PAYWALL_MAX_WORDS and bool(PAYWALL.search(page or text))


def read_page(page: Page, ticker: str, words: int, extract: Extractor) -> Page:
    """Fill in what the page says. Never raises: a page the extractor chokes on is empty."""
    if not page.html:
        return page
    try:
        page.text, page.title, page.date = extract(page.html, page.final_url or page.url)
    except Exception as exc:  # noqa: BLE001 - one bad page must not end the probe
        page.error = page.error or f"extraction failed: {type(exc).__name__}: {exc}"[:200]
        return page
    page.lede = lede_of(paragraphs(page.text, page.title), words)
    page.paywall = paywall_suspected(page.text, page.html)
    page.mentions = mentions_company(page.text, ticker) if page.text else None
    return page


# --------------------------------------------------------------------------- #
# The Scraper Studio scraper
# --------------------------------------------------------------------------- #


@dataclass
class ScraperRun:
    """What one trigger of the scraper returned, and how it got there."""

    trigger: str = ""
    records: list = field(default_factory=list)
    log: list = field(default_factory=list)
    error: str = ""
    seconds: float = 0.0
    requests: int = 0


def _payload(response: Any) -> Any:
    """The body as JSON -- a document or newline-delimited records -- or ``None``."""
    try:
        return response.json()
    except ValueError:
        pass
    records = []
    for line in (response.text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except ValueError:
            return None
    return records or None


def _poll_url(payload: dict) -> Optional[str]:
    """Where a triggered job's results are collected, on whichever API started it."""
    if payload.get("snapshot_id"):
        return f"{BRIGHTDATA_API}datasets/v3/snapshot/{payload['snapshot_id']}?format=json"
    if payload.get("collection_id"):
        return f"{BRIGHTDATA_API}dca/dataset?id={payload['collection_id']}"
    if payload.get("response_id"):
        return f"{BRIGHTDATA_API}dca/get_result?response_id={payload['response_id']}"
    return None


def _pending(status: int, payload: Any, text: str = "") -> bool:
    """Is a job's answer "not ready yet" rather than a result or a failure?

    As Bright Data's own CLI reads its collector API (@brightdata/cli,
    commands/scraper.js, ``classify_result`` / ``classify_dataset``): a 202,
    any other non-2xx while the job settles, an empty or ``null`` body, a
    ``{"pending": true}`` and a ``{"status": "building"}`` all mean wait. The
    deadline, not the status, is what ends a job that never finishes.
    """
    if not 200 <= status < 300 or status == 202:
        return True
    if payload is None and (text or "").strip() in ("", "null"):
        return True
    return isinstance(payload, dict) and (
        payload.get("pending") is True or str(payload.get("status", "")).lower() in PENDING
    )


def _is_record(payload: Any) -> bool:
    """One article record: says which page it is, and carries text from it."""
    return isinstance(payload, dict) and bool(record_url(payload)) and bool(record_text(payload)[1])


def _job_summary(payload: Any) -> str:
    """A collector job's log (``GET /dca/log/{id}``) on one line: how many pages went
    in, how many records came out, how many failed. Keys come in either casing."""
    if not isinstance(payload, dict):
        return "no log"

    def get(key: str) -> Any:
        return payload.get(key, payload.get(key.capitalize()))

    parts = [str(get("status") or "?")]
    parts += [f"{get(key)} {label}" for key, label in (("inputs", "input(s)"), ("lines", "record(s)"),
                                                          ("fails", "failed")) if get(key) is not None]
    if get("success_rate") is not None:
        parts.append(f"success rate {get('success_rate')}")
    errors = get("errors") or get("error")
    if errors:
        parts.append(f"errors: {brief(json.dumps(errors, default=str), 160)}")
    return ", ".join(parts)


def run_scraper(
    http: Http, token: str, trigger: str, urls: list[str], *,
    deadline: float = SCRAPER_DEADLINE_SECONDS, poll: float = SCRAPER_POLL_SECONDS,
    sleep: Callable[[float], None] = time.sleep, clock: Callable[[], float] = time.monotonic,
) -> ScraperRun:
    """Trigger the scraper on ``urls`` and collect what it returns. Never raises.

    Scraper Studio's dashboard shows the trigger URL for a scraper; both of
    Bright Data's job APIs are understood here, because which one a given
    scraper uses is the dashboard's to say: a ``snapshot_id`` is collected
    from the datasets API, a ``collection_id`` or ``response_id`` from the
    older collector API, and a list is the records themselves. Anything else
    is reported verbatim rather than guessed at.

    The realtime trigger (``/dca/trigger_immediate``) takes one page per
    request, as Bright Data's CLI sends it; the batch trigger takes them all
    at once. A batch job that brings back no article text has its job log
    read, so the report says whether the pages failed or were read and
    yielded nothing.
    """
    run = ScraperRun(trigger=trigger)
    if not trigger.startswith(BRIGHTDATA_API):
        run.error = (f"refusing to send the Bright Data token to {host_of(trigger) or trigger!r}: "
                     f"the scraper trigger must be a {BRIGHTDATA_API} URL")
        return run
    started = clock()
    realtime = urlsplit(trigger).path.rstrip("/").endswith("/dca/trigger_immediate")
    bodies: list[Any] = [{"url": u} for u in urls] if realtime else [[{"url": u} for u in urls]]
    try:
        for body in bodies:
            records, error, job = _one_job(http, token, trigger, body, run, started,
                                           deadline=deadline, poll=poll, sleep=sleep, clock=clock)
            run.records += records
            if error:
                run.error = f"{body['url']}: {error}" if realtime else error
                if not realtime or clock() - started > deadline:
                    return run
            if job and not any(record_text(r)[1] for r in records if isinstance(r, dict)):
                response = http.get(f"{BRIGHTDATA_API}dca/log/{job}", _auth(token))
                run.requests += 1
                run.log.append(f"job log: {_job_summary(_payload(response))}"
                               if int(response.status_code) < 300
                               else f"job log: HTTP {response.status_code} {brief(response.text, 120)}")
        return run
    except httpx.HTTPError as exc:
        run.error = f"{type(exc).__name__}: {exc}"[:200]
        return run
    finally:
        run.seconds = clock() - started


def _one_job(
    http: Http, token: str, trigger: str, body: Any, run: ScraperRun, started: float, *,
    deadline: float, poll: float, sleep: Callable[[float], None], clock: Callable[[], float],
) -> tuple[list, str, str]:
    """``(records, error, collection id)`` for one trigger request and its results."""
    response = http.post(trigger, body, _auth(token))
    run.requests += 1
    payload = _payload(response)
    run.log.append(f"trigger: HTTP {response.status_code}")
    if int(response.status_code) >= 400:
        return [], f"trigger refused: HTTP {response.status_code} {brief(response.text)}", ""
    if isinstance(payload, list):
        return payload, "", ""
    if not isinstance(payload, dict):
        return [], f"trigger answered with something that is not JSON: {(response.text or '')[:200]!r}", ""
    target = _poll_url(payload)
    if target is None:
        if _is_record(payload):
            return [payload], "", ""
        return [], f"unrecognised trigger response: {json.dumps(payload)[:300]}", ""
    job = str(payload.get("collection_id") or "") if not payload.get("snapshot_id") else ""
    run.log.append(f"collecting from {target.replace(BRIGHTDATA_API, '/')}")
    last = ""
    while True:
        if clock() - started > deadline:
            return [], (f"the scraper's results were not ready after {deadline:.0f}s"
                        + (f" (last answer: {last})" if last else "")), job
        sleep(poll)
        response = http.get(target, _auth(token))
        run.requests += 1
        payload = _payload(response)
        status = int(response.status_code)
        if status == 200 and isinstance(payload, list):
            return payload, "", job
        if status == 200 and _is_record(payload):
            return [payload], "", job
        if _pending(status, payload, response.text or ""):
            last = f"HTTP {status} {brief(response.text, 120)}".strip()
            continue
        return [], f"collecting failed: HTTP {status} {brief(response.text)}", job


# --------------------------------------------------------------------------- #
# Building the scraper through Scraper Studio's own API
# --------------------------------------------------------------------------- #

#: What Scraper Studio's AI is asked to build. The field names are the ones
#: ``record_text`` looks for first, so its answer needs no guessing.
SCRAPER_DESCRIPTION = (
    "A news article page. Return one record per URL with these fields: url (the page URL), "
    "title (the headline), published_at (the publication date and time, ISO 8601), author "
    "(the byline, if any) and body (the article's own text, paragraph by paragraph, in "
    "order). Leave out navigation, ads, related or recommended stories, comments, sign-up "
    "or subscription prompts, share buttons and disclaimers."
)

#: A build is Bright Data's AI writing and testing a scraper; the CLI waits
#: ten minutes for one. The whole build, retries included, fits this.
SCRAPER_BUILD_DEADLINE_SECONDS = 900.0
SCRAPER_BUILD_POLL_SECONDS = 10.0
#: The AI takes a few builds at a time per account and answers 429 beyond
#: that; the CLI waits 30s, doubling to at most 240s, four times over.
SCRAPER_BUILD_RETRIES = 4
SCRAPER_BUILD_RETRY_BASE_SECONDS = 30.0
SCRAPER_BUILD_RETRY_MAX_SECONDS = 240.0
TRANSIENT_STATUSES = frozenset({429, 500, 502, 503, 504})
#: Example pages the AI builds from. The API takes a list, but Bright Data's
#: CLI always sends one, and the first build -- sent two -- was refused.
SCRAPER_BUILD_EXAMPLES = 1
#: A collector id, as the collector API hands one out.
COLLECTOR_ID = re.compile(r"c_[a-z0-9]+")

#: Where the built scraper's own results would be pushed. The collector API
#: wants a delivery target at creation; this is the CLI's default, and the
#: probe never reads from it -- it collects each job's results by polling.
SCRAPER_DELIVERY = {
    "type": "webhook",
    "endpoint": "https://example.com/webhook",
    "filename": {"template": "data", "extension": "json"},
}


@dataclass
class ScraperBuild:
    """A scraper Scraper Studio's AI built for the probe, or how far it got."""

    site: str = ""
    collector_id: str = ""
    name: str = ""
    status: str = ""
    steps: list = field(default_factory=list)
    log: list = field(default_factory=list)
    error: str = ""
    seconds: float = 0.0
    requests: int = 0

    @property
    def trigger(self) -> str:
        """The batch trigger URL for the finished scraper; empty until it is done."""
        if self.status != "done" or not self.collector_id:
            return ""
        return f"{BRIGHTDATA_API}dca/trigger?collector={self.collector_id}"


def build_scraper(
    http: Http, token: str, site: str, urls: list[str], description: str = SCRAPER_DESCRIPTION, *,
    name: str = "", collector: str = "", deadline: float = SCRAPER_BUILD_DEADLINE_SECONDS,
    poll: float = SCRAPER_BUILD_POLL_SECONDS, sleep: Callable[[float], None] = time.sleep,
    clock: Callable[[], float] = time.monotonic,
) -> ScraperBuild:
    """Have Scraper Studio's AI build a scraper for ``site`` from example pages. Never raises.

    The three calls Bright Data's own CLI makes for ``bdata scraper create``
    (@brightdata/cli, commands/scraper.js): create an empty collector, ask the
    AI to build its template from the example URLs and a description of the
    fields wanted, and poll the build until it is done. No dashboard, and no
    URL for anyone to copy: the finished scraper's trigger is its id.

    The collector stays in the account's Scraper Studio, where it can be
    inspected, reused by id, or deleted by hand -- Bright Data documents no
    API to delete one, as the CLI notes. So this runs only when asked for,
    and ``collector`` builds on one that exists instead of creating another:
    one a failed build left behind is finished rather than joined by a
    second, and one already built is used as it is.
    """
    build = ScraperBuild(site=site, name=name or f"article-probe {site} {time.strftime('%Y-%m-%d %H:%M', time.gmtime())}")
    started = clock()
    headers = _auth(token)

    def said(response: Any) -> str:
        """A refused call as the log and the report show it, Bright Data's headers included."""
        reason = brd_reason(response)
        return f"HTTP {response.status_code} {brief(response.text)}{f' [{reason}]' if reason else ''}".strip()

    def post_retrying(url: str, body: Any) -> Any:
        """POST, waiting out the AI's parallel-build cap and brief server errors.

        A server error that says the same thing twice is an answer, not a
        hiccup: the first build spent seven minutes being told the same thing
        five times.
        """
        last = ""
        for attempt in range(SCRAPER_BUILD_RETRIES + 1):
            response = http.post(url, body, headers)
            build.requests += 1
            status = int(response.status_code)
            if status not in TRANSIENT_STATUSES or attempt == SCRAPER_BUILD_RETRIES:
                return response
            this = said(response)
            if status != 429 and this == last:
                return response
            last = this
            wait = min(SCRAPER_BUILD_RETRY_BASE_SECONDS * 2 ** attempt, SCRAPER_BUILD_RETRY_MAX_SECONDS)
            if clock() - started + wait > deadline:
                return response
            build.log.append(f"{this} from {url.replace(BRIGHTDATA_API, '/')}; waiting {wait:.0f}s")
            sleep(wait)
        return response  # pragma: no cover - the loop always returns

    try:
        if collector:
            if not COLLECTOR_ID.fullmatch(collector):
                build.error = f"{collector!r} is not a collector id (c_ and letters or digits)"
                return build
            build.collector_id, build.name = collector, name
            base = f"{BRIGHTDATA_API}dca/collectors/{collector}/automate_template"
            response = http.get(f"{base}/progress", headers)
            build.requests += 1
            payload = _payload(response)
            before = ""
            if int(response.status_code) < 300 and isinstance(payload, dict):
                before = str(payload.get("status") or "").lower()
                build.steps = list(payload.get("completed_steps") or [])
                found = f"{before or 'no status'} at step {payload.get('step') or '?'}"
            else:
                found = said(response)
            build.log.append(f"collector {collector} reused; its last build: {found}")
            if before == "done":
                build.status = "done"
                build.log.append("already built, so used as it is")
                return build
            if before == "pending_answer":
                build.status = before
                build.error = ("the AI build is waiting for an answer in Scraper Studio's web UI "
                               f"(https://brightdata.com/cp/scrapers/{collector})")
                return build
        else:
            response = post_retrying(f"{BRIGHTDATA_API}dca/collector",
                                     {"name": build.name, "deliver": SCRAPER_DELIVERY})
            payload = _payload(response)
            if int(response.status_code) >= 300 or not isinstance(payload, dict) or not payload.get("id"):
                build.error = f"creating the collector failed: {said(response)}"
                return build
            build.collector_id = str(payload["id"])
            build.name = str(payload.get("name") or build.name)
            build.log.append(f"collector {build.collector_id} created")
            base = f"{BRIGHTDATA_API}dca/collectors/{build.collector_id}/automate_template"

        response = post_retrying(base, {"description": description, "urls": list(urls)})
        if int(response.status_code) >= 300:
            build.error = f"starting the AI build failed: {said(response)}"
            return build
        build.log.append(f"AI build started from {len(urls)} example page(s): " + ", ".join(urls))

        last = ""
        while True:
            if clock() - started > deadline:
                build.error = (f"the AI build was not done after {deadline:.0f}s"
                               + (f" (last: {last})" if last else ""))
                return build
            sleep(poll)
            response = http.get(f"{base}/progress", headers)
            build.requests += 1
            payload = _payload(response)
            if not isinstance(payload, dict) or int(response.status_code) >= 300:
                last = said(response)[:160]
                continue
            build.status = str(payload.get("status") or "").lower()
            build.steps = list(payload.get("completed_steps") or build.steps)
            last = f"{build.status or '?'} at step {payload.get('step') or '?'}"
            if build.status == "done":
                build.log.append(f"AI build done after {len(build.steps)} step(s)")
                return build
            if build.status in ("failed", "error", "cancelled"):
                detail = payload.get("error") or payload.get("message") or payload.get("reason")
                build.error = (f"the AI build ended with status {build.status!r} at step "
                               f"{payload.get('step') or '?'}" + (f": {brief(str(detail))}" if detail else ""))
                return build
            if build.status == "pending_answer":
                build.error = ("the AI build is waiting for an answer in Scraper Studio's web UI "
                               f"(https://brightdata.com/cp/scrapers/{build.collector_id})")
                return build
    except httpx.HTTPError as exc:
        build.error = f"{type(exc).__name__}: {exc}"[:200]
        return build
    finally:
        build.seconds = clock() - started


def brand_of(site: str) -> str:
    """``finance.yahoo.com`` -> ``yahoo``: the word a library scraper's name would carry."""
    labels = [part for part in site.lower().removeprefix("www.").split(".") if part]
    return labels[-2] if len(labels) >= 2 else (labels[0] if labels else "")


def library_matches(http: Http, token: str, site: str) -> tuple[list[dict], int, str]:
    """``(matches, scrapers seen, error)``: ready-made scrapers whose name carries the site's brand.

    Bright Data's library of ready-made scrapers is listed by the datasets
    API. A name match is only a lead -- the one Bright Data's CLI knows for
    Yahoo returns company data, not articles -- so the report shows what
    matched and the build decides nothing from it. Never raises.
    """
    brand = brand_of(site)
    try:
        response = http.get(f"{BRIGHTDATA_API}datasets/list", _auth(token))
    except httpx.HTTPError as exc:
        return [], 0, f"{type(exc).__name__}: {exc}"[:200]
    payload = _payload(response)
    if int(response.status_code) != 200 or not isinstance(payload, list):
        return [], 0, f"the library listing answered HTTP {response.status_code} {brief(response.text, 120)}".strip()
    items = [item for item in payload if isinstance(item, dict)]
    found = [{"id": str(item.get("id") or ""), "name": str(item.get("name") or "")}
             for item in items if brand and brand in str(item.get("name") or "").lower()]
    return found, len(items), ""


def record_text(record: dict) -> tuple[str, str]:
    """``(field, text)``: the article text in one scraper record, whatever it was called.

    A named text field if there is one, else the longest string that is not
    plainly metadata. A list of strings (paragraphs) is joined one per line.
    """
    if not isinstance(record, dict):
        return "", ""

    def as_text(value: Any) -> str:
        if isinstance(value, str):
            return value.strip()
        if isinstance(value, list) and all(isinstance(v, str) for v in value):
            return "\n".join(v.strip() for v in value if v.strip())
        return ""

    for name in TEXT_FIELDS:
        text = as_text(record.get(name))
        if text:
            return name, text
    candidates = [(len(as_text(v)), k, as_text(v)) for k, v in record.items() if k not in META_FIELDS]
    candidates = [c for c in candidates if c[0]]
    if not candidates:
        return "", ""
    _, name, text = max(candidates)
    return name, text


def _normal(url: str) -> str:
    parts = urlsplit(url.split("#")[0])
    host = parts.netloc.lower().removeprefix("www.")
    return f"{host}{parts.path.rstrip('/')}{'?' + parts.query if parts.query else ''}"


def record_url(record: Any) -> str:
    if not isinstance(record, dict):
        return ""
    source = record.get("input") if isinstance(record.get("input"), dict) else {}
    return str(record.get("url") or source.get("url") or record.get("input_url") or "")


def align(records: list, urls: list[str]) -> dict[str, dict]:
    """Each requested URL's record, matched by URL, or by order when none carry one."""
    by_url = {_normal(record_url(r)): r for r in records if record_url(r)}
    matched = {u: by_url[_normal(u)] for u in urls if _normal(u) in by_url}
    if not matched and not by_url and len(records) == len(urls):
        matched = dict(zip(urls, records))
    return matched


@dataclass
class Scraped:
    """One site result, as the scraper returned it."""

    index: int
    url: str
    field: str = ""
    text: str = ""
    lede: Optional[Lede] = None
    error: str = ""
    #: Share of the scraper's words found in the Unlocker's text, and the
    #: reverse: near 1.0 both ways means the two read the same story.
    in_unlocker: Optional[float] = None
    unlocker_in: Optional[float] = None


def shingles(text: str, size: int = 5) -> set[tuple[str, ...]]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {tuple(words[i:i + size]) for i in range(max(0, len(words) - size + 1))}


def contained(part: str, whole: str) -> Optional[float]:
    """The share of ``part``'s five-word runs that also appear in ``whole``."""
    mine = shingles(part)
    if not mine:
        return None
    return len(mine & shingles(whole)) / len(mine)


def read_scraped(run: ScraperRun, pages: list[Page], indexes: list[int], words: int) -> list[Scraped]:
    by_index = {p.index: p for p in pages}
    urls = [by_index[i].url for i in indexes]
    matched = align(run.records, urls)
    out = []
    for i in indexes:
        page = by_index[i]
        record = matched.get(page.url)
        item = Scraped(index=i, url=page.url)
        if record is None:
            item.error = run.error or "no record came back for this URL"
        elif not isinstance(record, dict):
            item.error = f"the record is not an object: {str(record)[:100]!r}"
        elif record.get("error") and not record_text(record)[1]:
            item.error = str(record.get("error"))[:200]
        else:
            item.field, item.text = record_text(record)
            title = str(record.get("title") or record.get("headline") or "")
            item.lede = lede_of(paragraphs(item.text, title), words)
            if page.text and item.text:
                item.in_unlocker = contained(item.text, page.text)
                item.unlocker_in = contained(page.text, item.text)
        out.append(item)
    return out


# --------------------------------------------------------------------------- #
# The prompts, and the model
# --------------------------------------------------------------------------- #


def with_ledes(context: TickerContext, ledes: dict[int, str]) -> TickerContext:
    """The same context, with article text indented under the headlines it belongs to.

    Rendered by the real ``as_prompt()``, so everything outside the NEWS
    block is byte for byte what production sent.
    """
    lines = list(context.headlines)
    for index, text in ledes.items():
        lines[index] = f"{lines[index]}\n  Article: {text}"
    return replace(context, headlines=lines)


def build_variants(context: TickerContext, pages: list[Page], scraped: list[Scraped]) -> dict[str, TickerContext]:
    """Each prompt the model will be asked, in report order.

    ``unlocker-named`` gives text only to the stories that name the company.
    The first real run found the noise was not page furniture but whole
    articles about other companies -- four of eight on a Novo Nordisk line --
    so this is the prompt that asks whether leaving those out is cheaper and
    reads differently. Only asked when it would differ from ``unlocker``.
    """
    unlocker = {p.index: p.lede.text for p in pages if p.lede}
    variants = {"headlines": context}
    if unlocker:
        variants["unlocker"] = with_ledes(context, unlocker)
    named = {p.index: p.lede.text for p in pages if p.lede and p.mentions}
    if named and named != unlocker:
        variants["unlocker-named"] = with_ledes(context, named)
    # The design a scraper would actually be used in: the Unlocker everywhere,
    # the scraper filling the pages the Unlocker could not read. Asked only
    # when the scraper filled at least one.
    filled = {s.index: s.lede.text for s in scraped if s.lede and s.index not in unlocker}
    if filled:
        variants["unlocker+scraper"] = with_ledes(context, {**unlocker, **filled})
    both = {s.index: s.lede.text for s in scraped if s.lede and s.index in unlocker}
    if both:
        variants["unlocker-site"] = with_ledes(context, {i: unlocker[i] for i in both})
        variants["scraper-site"] = with_ledes(context, both)
    return variants


#: ``(system prompt, user prompt) -> Completion``: the production call, or a fake.
Complete = Callable[[str, str], Completion]


def production_complete() -> Complete:
    """The call the cycle makes, unchanged: ``heartbeat.call_llm``."""
    from orchestrator.heartbeat import SIGNAL_JSON_SCHEMA, call_llm

    return lambda system, user: call_llm(system, user, SIGNAL_JSON_SCHEMA)


@dataclass(frozen=True)
class Call:
    variant: str
    repeat: int
    signal: Any = None
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: Optional[float] = None
    seconds: float = 0.0
    error: str = ""


def ask(complete: Complete, system: str, ticker: str, variant: str, repeat: int,
        context: TickerContext) -> Call:
    """One answer to one prompt. Never raises: a failure is a row in the report."""
    started = time.monotonic()
    try:
        completion = complete(system, build_user_prompt(context))
    except Exception as exc:  # noqa: BLE001 - a failed call is a finding, not a crash
        return Call(variant, repeat, error=f"{type(exc).__name__}: {exc}"[:300],
                    seconds=time.monotonic() - started)
    usage = completion.usage
    measured = dict(
        input_tokens=usage.input_tokens, output_tokens=usage.output_tokens,
        cost_usd=usage.cost_usd, seconds=time.monotonic() - started,
    )
    try:
        signal = parse_signal(completion.text)
    except ValueError as exc:
        return Call(variant, repeat, error=f"invalid output: {exc}"[:300], **measured)
    if signal.ticker != ticker:
        return Call(variant, repeat, error=f"answered for {signal.ticker}", **measured)
    return Call(variant, repeat, signal=signal, **measured)


def ask_all(complete: Complete, system: str, ticker: str, variants: dict[str, TickerContext],
            repeats: int, workers: int = MODEL_WORKERS) -> list[Call]:
    """Every prompt ``repeats`` times, interleaved so a bad minute at the provider hits all of them alike."""
    jobs = [(name, r) for r in range(repeats) for name in variants]
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        return list(pool.map(
            lambda job: ask(complete, system, ticker, job[0], job[1], variants[job[0]]), jobs
        ))


# --------------------------------------------------------------------------- #
# The report
# --------------------------------------------------------------------------- #


@dataclass
class Probe:
    entry: ReplayEntry
    site: str
    words: int
    repeats: int
    model: str = ""
    effort: Optional[str] = None
    pages: list = field(default_factory=list)
    #: Ready-made scrapers named for the site, looked up whenever a scraper is used.
    library: Optional[tuple] = None
    build: Optional[ScraperBuild] = None
    scraper: Optional[ScraperRun] = None
    scraped: list = field(default_factory=list)
    variants: dict = field(default_factory=dict)
    calls: list = field(default_factory=list)


def _fmt_int(n: Optional[float]) -> str:
    return "-" if n is None else f"{n:,.0f}"


def _fmt_share(x: Optional[float]) -> str:
    return "-" if x is None else f"{x:.0%}"


def _note(page: Page) -> str:
    if page.kind in (NOT_AN_ARTICLE, NO_LINK):
        return f"skipped: {page.kind}"
    if page.error:
        return page.error[:60]
    if not page.lede:
        return "no article text found on the page"
    notes = []
    if page.paywall:
        notes.append("short: paywall or teaser?")
    if page.final_url and page.final_url != page.url:
        notes.append(f"via Google to {host_of(page.final_url)}")
    return "; ".join(notes)


def variant_rows(probe: Probe) -> list[dict]:
    rows = []
    for name, context in probe.variants.items():
        answered = [c for c in probe.calls if c.variant == name and c.signal is not None]
        priced = [c.cost_usd for c in answered if c.cost_usd is not None]
        rows.append({
            "variant": name,
            "prompt_words": len(build_user_prompt(context).split()),
            "asked": sum(1 for c in probe.calls if c.variant == name),
            "answered": len(answered),
            "input_tokens": mean(c.input_tokens for c in answered) if answered else None,
            "output_tokens": mean(c.output_tokens for c in answered) if answered else None,
            "cost_usd": mean(priced) if priced else None,
            "answers": [
                f"{c.signal.bias.value} {c.signal.conviction:.2f} news {c.signal.news_score:+.2f}"
                if c.signal is not None and c.signal.news_score is not None
                else (f"{c.signal.bias.value} {c.signal.conviction:.2f}" if c.signal is not None
                      else f"failed: {c.error[:40]}")
                for c in probe.calls if c.variant == name
            ],
        })
    return rows


def render(probe: Probe) -> str:
    entry, context = probe.entry, probe.entry.context
    rule = "-" * 78
    site_count = len(site_indexes(context, probe.site))
    out = [
        "ARTICLE PROBE: one recorded context, with its articles fetched",
        "=" * 78,
        f"Context       : {entry.ticker} ({name_for(entry.ticker)}), journalled {str(entry.ts_utc)[:16]}Z, "
        f"{len(context.headlines)} results, {site_count} article(s) on {probe.site}",
        f"Words kept    : the first {probe.words} of each article, for both sources",
    ]
    if probe.variants and probe.calls:
        out.append(f"Model         : {probe.model} at {probe.effort or 'default effort'}; system prompt, "
                   f"schema and effort as production; each prompt asked {probe.repeats}x")
    out += ["", "WHAT THE UNLOCKER GOT (generic extraction)", rule,
            f"{'#':>2}  {'source':<18} {'page KB':>8} {'article':>8} {'sent':>5} {'boiler':>6} {'names it':>8}  note"]
    for page in probe.pages:
        lede = page.lede
        out.append(
            f"{page.index + 1:>2}  {page.source[:18]:<18} "
            f"{(_fmt_int(page.page_bytes / 1024) if page.page_bytes else '-'):>8} "
            f"{_fmt_int(lede.article_words if lede else None):>8} {_fmt_int(lede.words if lede else None):>5} "
            f"{_fmt_share(lede.boilerplate_share if lede else None):>6} "
            f"{('-' if page.mentions is None else 'yes' if page.mentions else 'NO'):>8}  {_note(page)}"
        )
    requests = sum(p.requests for p in probe.pages)
    via_google = sum(1 for p in probe.pages if p.requests == 2)
    skipped = sum(1 for p in probe.pages if not p.fetched)
    read = [p for p in probe.pages if p.lede]
    failed = sum(1 for p in probe.pages if p.fetched and not p.lede)
    wall = max((p.seconds for p in probe.pages), default=0.0)
    out.append(
        f"Unlocker: {requests} request(s) ({via_google} through a Google redirect), {skipped} skipped, "
        f"{len(read)} article(s) read, {failed} without text; slowest page {wall:.0f}s"
    )
    out.append(
        f"Article text for the model: {sum(p.lede.words for p in read):,} words over {len(read)} result(s); "
        f"{sum(1 for p in read if p.mentions is False)} of them never name the company"
    )

    out += ["", f"SCRAPER STUDIO ({probe.site})", rule]
    if probe.library is not None:
        found, seen, error = probe.library
        if error:
            out.append(f"library: not listed ({error})")
        elif found:
            out.append(f"library: {len(found)} of {seen} ready-made scrapers are named for "
                       f"{brand_of(probe.site)!r}: " + "; ".join(f"{m['name']} ({m['id']})" for m in found[:5]))
        else:
            out.append(f"library: none of {seen} ready-made scrapers is named for {brand_of(probe.site)!r}")
    build = probe.build
    if build is not None:
        head = f"built by Scraper Studio's AI: {build.collector_id or 'no collector'}"
        if build.name:
            head += f" ({build.name})"
        out.append(f"{head}, {build.status or 'not started'}, {len(build.steps)} step(s), "
                   f"{build.requests} request(s), {build.seconds:.0f}s")
        out += [f"  {line}" for line in build.log]
        if build.error:
            out.append(f"build error: {build.error}")
        if build.trigger:
            out.append(f"reuse it: scraper_trigger={build.trigger}")
    if probe.scraper is None:
        if build is None:
            out.append("not asked: no scraper trigger URL was given, and no build was asked for")
    else:
        run = probe.scraper
        out.append(f"{len(run.records)} record(s), {run.requests} request(s), {run.seconds:.0f}s"
                   + (f"; {'; '.join(run.log)}" if run.log else ""))
        if run.error:
            out.append(f"error: {run.error}")
        out.append(f"{'#':>2}  {'field':<10} {'article':>8} {'sent':>5} {'boiler':>6} "
                   f"{'its words in unlocker text':>27} {'unlocker words in its':>22}")
        for item in probe.scraped:
            lede = item.lede
            if item.error and not lede:
                out.append(f"{item.index + 1:>2}  failed: {item.error[:70]}")
                continue
            out.append(
                f"{item.index + 1:>2}  {item.field[:10]:<10} {_fmt_int(lede.article_words if lede else None):>8} "
                f"{_fmt_int(lede.words if lede else None):>5} "
                f"{_fmt_share(lede.boilerplate_share if lede else None):>6} "
                f"{_fmt_share(item.in_unlocker):>27} {_fmt_share(item.unlocker_in):>22}"
            )

    out += ["", "WHAT THE MODEL READ AND SAID", rule]
    if not probe.calls:
        out.append("not asked (--no-model); prompt sizes only:")
    out.append(f"{'prompt':<14} {'words':>6} {'input tok':>10} {'output tok':>11} {'cost/call':>10}  answers")
    for row in variant_rows(probe):
        cost = "-" if row["cost_usd"] is None else f"${row['cost_usd']:.4f}"
        out.append(
            f"{row['variant']:<14} {row['prompt_words']:>6,} {_fmt_int(row['input_tokens']):>10} "
            f"{_fmt_int(row['output_tokens']):>11} {cost:>10}  " + " | ".join(row["answers"])
        )
    if probe.calls:
        out.append("tokens and cost are the mean over the answered calls; output tokens include reasoning")
        out += ["", "RATIONALES (the first answer to each prompt)", rule]
        for name in probe.variants:
            first = next((c for c in probe.calls if c.variant == name and c.signal is not None), None)
            text = first.signal.rationale if first else "(no answer)"
            out.append(f"[{name}]")
            out += textwrap.wrap(text, width=96, initial_indent="  ", subsequent_indent="  ")

    out += ["", "LIMITS", rule, *textwrap.wrap(
        "One context and a few calls: this shows what the model reads and what it costs, not whether "
        "it trades better -- that needs many contexts scored against prices. Pages are fetched now, "
        "not when the line was written. 'boiler' and 'names it' are crude text matches, and a "
        "Google redirect or a paywall can leave a result with no text at all.", width=78)]
    return "\n".join(out)


def as_json(probe: Probe) -> dict:
    entry = probe.entry
    return {
        "probe": "article",
        "ticker": entry.ticker,
        "ts_utc": entry.ts_utc,
        "site": probe.site,
        "words": probe.words,
        "repeats": probe.repeats,
        "model": probe.model,
        "effort": probe.effort,
        "pages": [
            {
                "index": p.index, "source": p.source, "url": p.url, "kind": p.kind,
                "final_url": p.final_url, "status": p.status, "page_bytes": p.page_bytes,
                "requests": p.requests, "seconds": round(p.seconds, 1), "error": p.error,
                "title": p.title, "date": p.date, "paywall_suspected": p.paywall,
                "names_the_company": p.mentions,
                "article_words": p.lede.article_words if p.lede else None,
                "lede_words": p.lede.words if p.lede else None,
                "boilerplate_words": p.lede.boilerplate_words if p.lede else None,
                "lede": p.lede.text if p.lede else None,
                "article_text": p.text,
            }
            for p in probe.pages
        ],
        "library": None if probe.library is None else {
            "matches": probe.library[0], "scrapers_seen": probe.library[1], "error": probe.library[2],
        },
        "build": None if probe.build is None else {
            "collector_id": probe.build.collector_id, "name": probe.build.name,
            "status": probe.build.status, "steps": probe.build.steps, "log": probe.build.log,
            "error": probe.build.error, "seconds": round(probe.build.seconds, 1),
            "requests": probe.build.requests, "trigger": probe.build.trigger,
        },
        "scraper": None if probe.scraper is None else {
            "trigger": probe.scraper.trigger, "error": probe.scraper.error,
            "log": probe.scraper.log, "seconds": round(probe.scraper.seconds, 1),
            "requests": probe.scraper.requests,
            "records": [json.dumps(r, ensure_ascii=False, default=str)[:20000] for r in probe.scraper.records],
            "results": [
                {
                    "index": s.index, "url": s.url, "field": s.field, "error": s.error,
                    "article_words": s.lede.article_words if s.lede else None,
                    "lede_words": s.lede.words if s.lede else None,
                    "boilerplate_words": s.lede.boilerplate_words if s.lede else None,
                    "in_unlocker": s.in_unlocker, "unlocker_in": s.unlocker_in,
                    "lede": s.lede.text if s.lede else None,
                }
                for s in probe.scraped
            ],
        },
        "variants": variant_rows(probe),
        "prompts": {name: build_user_prompt(ctx) for name, ctx in probe.variants.items()},
        "calls": [
            {
                "variant": c.variant, "repeat": c.repeat, "error": c.error,
                "input_tokens": c.input_tokens, "output_tokens": c.output_tokens,
                "cost_usd": c.cost_usd, "seconds": round(c.seconds, 1),
                "signal": c.signal.model_dump(mode="json") if c.signal is not None else None,
            }
            for c in probe.calls
        ],
    }


# --------------------------------------------------------------------------- #
# Putting it together
# --------------------------------------------------------------------------- #


def examples(pages: list[Page], indexes: list[int], count: int = SCRAPER_BUILD_EXAMPLES) -> list[str]:
    """The site's pages the AI builds from: ones the Unlocker read first, since a page
    that loads is one the AI can learn from, then the rest in their order."""
    site_pages = [p for p in pages if p.index in indexes]
    ordered = [p for p in site_pages if p.lede] + [p for p in site_pages if not p.lede]
    return [p.url for p in ordered][:max(1, count)]


def run(
    entry: ReplayEntry, *, site: str, words: int, repeats: int, http: Http, token: str, zone: str,
    extract: Extractor = trafilatura_extract, complete: Optional[Complete] = None,
    scraper_trigger: str = "", model: str = "", effort: Optional[str] = None,
    fetch_workers: int = FETCH_WORKERS, model_workers: int = MODEL_WORKERS,
    scraper_kwargs: Optional[dict] = None, build: bool = False,
    scraper_description: str = SCRAPER_DESCRIPTION, build_kwargs: Optional[dict] = None,
    collector: str = "",
) -> Probe:
    """Fetch, read, optionally build and run a scraper, optionally ask. Never raises for a bad page or call.

    ``build`` has Scraper Studio's AI build a scraper for the site from one of
    its article links on this line -- ``collector``, when given, is built on
    rather than a new one created -- then runs it on all of them. A trigger
    URL, when one is given, wins: a scraper that exists is reused, never
    rebuilt.
    """
    probe = Probe(entry=entry, site=site, words=words, repeats=repeats, model=model, effort=effort)
    probe.pages = [read_page(p, entry.ticker, words, extract)
                   for p in fetch_all(http, token, zone, entry.context, fetch_workers)]
    indexes = site_indexes(entry.context, site)
    urls = [p.url for p in probe.pages if p.index in indexes]
    if (build or scraper_trigger) and urls:
        probe.library = library_matches(http, token, site)
    if build and not scraper_trigger and urls:
        probe.build = build_scraper(http, token, site, examples(probe.pages, indexes), scraper_description,
                                    collector=collector, **(build_kwargs or {}))
        scraper_trigger = probe.build.trigger
    if scraper_trigger:
        probe.scraper = run_scraper(http, token, scraper_trigger, urls, **(scraper_kwargs or {}))
        probe.scraped = read_scraped(probe.scraper, probe.pages, indexes, words)
    probe.variants = build_variants(entry.context, probe.pages, probe.scraped)
    if complete is not None:
        system = system_prompt_for(entry.ticker, entry.context)
        probe.calls = ask_all(complete, system, entry.ticker, probe.variants, repeats, model_workers)
    return probe


def plan(entry: ReplayEntry, site: str) -> str:
    """What a real run would fetch, for --dry-run: no network, no credentials."""
    lines = [f"{entry.ticker} ({name_for(entry.ticker)}), journalled {entry.ts_utc}", ""]
    site_set = set(site_indexes(entry.context, site))
    for index, source, url in result_links(entry.context):
        kind = classify(url)
        mark = f"  <- {site}" if index in site_set else ""
        lines.append(f"{index + 1:>2}. [{kind}] {source}: {url[:90]}{mark}")
    fetched = sum(1 for _, _, url in result_links(entry.context) if classify(url) in (ARTICLE, GOOGLE_REDIRECT))
    lines += ["", f"a real run fetches {fetched} page(s) through the Unlocker "
                  f"(one more for each Google redirect) and hands {len(site_set)} to the scraper"]
    return "\n".join(lines)


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch one recorded context's articles and ask the model with them.")
    parser.add_argument("--journal", type=Path, default=cfg.SIGNAL_JOURNAL_PATH)
    parser.add_argument("--site", default=DEFAULT_SITE,
                        help="the site the scraper covers, and the one a line is picked for (default %(default)s)")
    parser.add_argument("--ticker", default="", help="probe this single stock's line instead of the default pick")
    parser.add_argument("--day", default="", help="YYYY-MM-DD: probe a line journalled that day")
    parser.add_argument("--min-site-links", type=int, default=MIN_SITE_LINKS)
    parser.add_argument("--words", type=int, default=DEFAULT_WORDS,
                        help="words of each article the model gets (default %(default)s)")
    parser.add_argument("--repeats", type=int, default=DEFAULT_REPEATS,
                        help="times each prompt is asked (default %(default)s)")
    parser.add_argument("--scraper-trigger", default="",
                        help="reuse this scraper: its trigger URL, e.g. "
                             "https://api.brightdata.com/dca/trigger?collector=c_...")
    parser.add_argument("--build-scraper", action="store_true",
                        help="have Scraper Studio's AI build a scraper for --site from this line's "
                             "article links, then run it; ignored when --scraper-trigger is given")
    parser.add_argument("--collector", default="",
                        help="build on this existing collector (c_...) instead of creating one -- a "
                             "failed build's leftover is finished, a built one used as it is; implies "
                             "--build-scraper")
    parser.add_argument("--scraper-description", default=SCRAPER_DESCRIPTION,
                        help="what the built scraper should return, for Scraper Studio's AI")
    parser.add_argument("--concurrency", type=int, default=MODEL_WORKERS, help="model calls in flight at once")
    parser.add_argument("--no-model", action="store_true", help="fetch and measure only; ask no model")
    parser.add_argument("--dry-run", action="store_true", help="show the line and what would be fetched, then stop")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="print everything read and said to stdout as JSON; the report goes to stderr")
    return parser.parse_args(argv)


def main(argv: Optional[list[str]] = None) -> int:
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr, format="%(levelname)s %(name)s: %(message)s")
    args = parse_args(argv)
    say = (lambda text: print(text, file=sys.stderr)) if args.as_json else print

    entries = list(runner.load_entries(list(journal_files.iter_lines(args.journal))))
    entry = pick(entries, args.site, args.ticker or None, args.day or None, args.min_site_links)
    if entry is None:
        say(f"no single-stock line fits (site {args.site}, ticker {args.ticker or 'any'}, "
            f"day {args.day or 'any'}, at least {args.min_site_links} site articles when neither is named)")
        return 1
    if args.dry_run:
        say(plan(entry, args.site))
        return 0

    from config.settings import get_settings
    from orchestrator import llm

    settings = get_settings()
    token = news.resolve_token(settings.brightdata_api_token)
    zone = news.resolve_zone(settings.brightdata_serp_zone, settings.brightdata_unlocker_zone)
    if not token or not zone:
        say("no Bright Data token or zone: set BRIGHTDATA_API_TOKEN (and the zone the news fetch uses)")
        return 2
    complete = None
    if not args.no_model:
        if llm.MODEL_BASE_URL and not settings.full_model_api_key:
            say("FULL_MODEL_API_KEY is empty, so the model cannot be asked; rerun with --no-model to fetch only")
            return 2
        complete = production_complete()

    probe = run(
        entry, site=args.site, words=args.words, repeats=max(1, args.repeats), http=Http(),
        token=token, zone=zone, complete=complete, scraper_trigger=args.scraper_trigger.strip(),
        model=llm.configured_model(), effort=llm.configured_effort(),
        model_workers=max(1, args.concurrency), build=args.build_scraper or bool(args.collector.strip()),
        scraper_description=args.scraper_description.strip() or SCRAPER_DESCRIPTION,
        collector=args.collector.strip(),
    )
    say(render(probe))
    if args.as_json:
        print(json.dumps(as_json(probe), ensure_ascii=False, indent=1))

    if not any(p.lede for p in probe.pages):
        return 1
    if complete is not None and not any(c.signal is not None for c in probe.calls):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
