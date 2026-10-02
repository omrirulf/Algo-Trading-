"""An article behind a news result: fetched through the Web Unlocker, and cut out of its page.

The news block the model reads is a headline and Google's ~150-character
snippet per result. The pages behind those results are fetched here, through
the same Bright Data zone and request API the news fetch uses, and one
generic extractor (trafilatura) cuts the story out of each page, whatever
the site. Two callers share it:

* ``replay/article_probe.py`` -- one recorded context, fetched and handed to
  the model with and without the text, to see what it would add;
* ``store/articles.py`` -- the archive: after each cycle, the text of the
  articles that name the company, saved privately and never shown to the
  model, so a checkpoint can test whether it would have helped.

It only fetches and reads. The Bright Data key is passed in by the caller
and goes nowhere but Bright Data's request API (``news.BRIGHTDATA_REQUEST_URL``);
nothing here reads configuration, writes a file, or reaches the archive, and
the CI invariants on ``orchestrator/`` hold it to that.
"""

from __future__ import annotations

import html as html_lib
import re
import time
from dataclasses import dataclass, field
from typing import Any, Callable, NamedTuple, Optional
from urllib.parse import urlsplit

import httpx

from config.instruments import name_for
from orchestrator import news


#: One page through the Unlocker. Slow sites take tens of seconds.
UNLOCKER_TIMEOUT_SECONDS = 90.0


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


def host_of(url: str) -> str:
    host = urlsplit(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


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


class Http:
    """The two calls a fetch makes, as the seam a test replaces."""

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
    #: Which form of the request API the page came through: ``raw``, or
    #: ``json`` when the raw form met Bright Data's gateway failing.
    form: str = ""
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


class Answer(NamedTuple):
    """What one page fetch came back with."""

    status: int
    body: str
    error: str
    #: Requests it took: one, or two when the raw form failed and the json form was tried.
    requests: int = 1
    #: Which form of the request API answered: ``raw`` or ``json``.
    form: str = "raw"


#: Bright Data's own gateway failing looks like this: a bare "502 Bad Gateway"
#: page of a hundred-odd bytes with none of its error headers. A page's own
#: error answer is larger, and the Unlocker's own refusals carry a reason.
GATEWAY_PAGE_MAX_BYTES = 1024


def _unlock(http: Http, token: str, zone: str, url: str) -> Answer:
    """One page through the Unlocker: the raw form, then the json form when the gateway failed.

    The raw form is what the news fetch sends, and the page's own status
    comes back as the API's. On 1 Oct 2026 it answered 502 for each of the
    nine Yahoo Finance ``/.../articles/`` stories in that day's cycle -- a
    bare nginx "502 Bad Gateway" from Bright Data's own gateway, none of its
    error headers -- while the json form fetched the same page with status
    200, as did a direct fetch (``replay/unlocker_check.py``). Yahoo's
    responses carry a 29-35 KB header block; the raw form relays it to the
    caller and the json form carries it inside the body, and the raw
    failures fit a limit near 32 KB at the gateway (measured on 2 Oct, not
    confirmed by Bright Data). So a 5xx that carries no reason and no page
    is asked once more in the json form, which reports the page's own
    status apart from the API's. A refusal with a
    reason, a 4xx, or a page's own error answer is taken as it is.
    """
    response = http.post(news.BRIGHTDATA_REQUEST_URL, {"zone": zone, "url": url, "format": "raw"},
                         _auth(token))
    status = int(response.status_code)
    body = response.text or ""
    if status == 200:
        return Answer(status, body, "")
    reason = brd_reason(response)
    refusal = f"HTTP {status} {reason or brief(body)}".strip()
    if status < 500 or reason or len(body.encode("utf-8")) > GATEWAY_PAGE_MAX_BYTES:
        return Answer(status, "", refusal)
    return _unlock_json(http, token, zone, url, refusal)


def _unlock_json(http: Http, token: str, zone: str, url: str, refusal: str) -> Answer:
    """The same page in the json form: the API's status outside, the page's own inside."""
    response = http.post(news.BRIGHTDATA_REQUEST_URL, {"zone": zone, "url": url, "format": "json"},
                         _auth(token))
    status = int(response.status_code)
    if status != 200:
        reason = brd_reason(response) or brief(response.text or "")
        return Answer(status, "", f"{refusal} (raw); then HTTP {status} {reason} (json)".strip(), 2, "json")
    try:
        payload = response.json()
    except ValueError:
        payload = None
    if not isinstance(payload, dict) or not isinstance(payload.get("body"), str):
        return Answer(status, "", f"{refusal} (raw); then no page body (json)", 2, "json")
    page_status = int(payload.get("status_code") or 200)
    if page_status != 200:
        return Answer(page_status, "", f"{refusal} (raw); then the page answered HTTP {page_status} (json)",
                      2, "json")
    return Answer(200, payload["body"], "", 2, "json")


def fetch_page(http: Http, token: str, zone: str, index: int, source: str, url: str) -> Page:
    """One result's page, following Google's redirect stub once if that is what it is. Never raises."""
    page = Page(index=index, source=source, url=url, kind=classify(url))
    if not page.fetched:
        return page
    started = time.monotonic()
    try:
        answer = _unlock(http, token, zone, url)
        page.status, page.html, page.error = answer.status, answer.body, answer.error
        page.requests, page.form = answer.requests, answer.form
        page.final_url = url
        if page.kind == GOOGLE_REDIRECT and page.html:
            target = redirect_target(page.html)
            if target:
                page.final_url = target
                answer = _unlock(http, token, zone, target)
                page.status, page.html, page.error = answer.status, answer.body, answer.error
                page.requests += answer.requests
                page.form = answer.form
            elif _looks_like_google(page.html):
                page.error = "Google's redirect page, and no destination could be read off it"
                page.html = ""
    except httpx.HTTPError as exc:
        page.error = f"{type(exc).__name__}: {exc}"[:200]
        page.html = ""
    page.page_bytes = len(page.html.encode("utf-8"))
    page.seconds = time.monotonic() - started
    return page


#: ``(html, url) -> (text, title, date)``. trafilatura unless a test says otherwise.
Extractor = Callable[[str, str], tuple[str, str, str]]


def trafilatura_extract(page: str, url: str) -> tuple[str, str, str]:
    """The story cut out of the page: text, title and date, empty when there is none.

    Imported here rather than at the top so the rest of this module, and
    the suite, need nothing that the trading cycle does not already install.
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
    except Exception as exc:  # noqa: BLE001 - one bad page must not end the run
        page.error = page.error or f"extraction failed: {type(exc).__name__}: {exc}"[:200]
        return page
    page.lede = lede_of(paragraphs(page.text, page.title), words)
    page.paywall = paywall_suspected(page.text, page.html)
    page.mentions = mentions_company(page.text, ticker) if page.text else None
    return page
