"""The article probe must fetch the right pages, and change nothing but the article text.

The probe is a one-context look at what full article text would add to the
news block. Each of the things below is a way for it to produce a clean-looking
report about the wrong question: fetching a quote page as if it were a story,
sending the Bright Data token somewhere other than Bright Data, pairing a
scraper record with the wrong URL, or letting a prompt variant differ from
production in more than the article text it was meant to add.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest
import yaml

from app.schemas import Bias, LLMSignal
from config import settings as cfg
from orchestrator import heartbeat, llm, news
from orchestrator.context import TickerContext
from orchestrator.llm import Completion
from orchestrator.news import Headline
from orchestrator.pricing import Usage
from replay import article_probe as ap
from replay import runner

ROOT = Path(__file__).resolve().parents[1]

YAHOO_1 = "https://finance.yahoo.com/markets/stocks/articles/novo-buyback-135000341.html"
YAHOO_2 = "https://uk.finance.yahoo.com/news/novo-second-act-015519811.html"
STOCKTWITS = "https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982"
QUOTE = "https://finance.yahoo.com/quote/NVO/"
GOOGLE_STUB = "/goto?url=CAESmAEB6z"
PUBLISHER = "https://www.benzinga.com/news/26/09/61806602/novo-nordisk-cuts-guidance"

RESULTS = [
    ("Yahoo Finance", YAHOO_1, "Novo Nordisk A/S - share repurchase programme"),
    ("Stocktwits", STOCKTWITS, "VLO Stock Heads For Best Year Since 1982"),
    ("Yahoo Finance UK", YAHOO_2, "Can Novo Nordisk (NVO) Find a Second Act?"),
    ("Yahoo Finance", QUOTE, "Novo Nordisk A/S (NVO) Stock Price, News, Quote"),
    ("Benzinga", GOOGLE_STUB, "Novo Nordisk cuts its sales guidance"),
]

NOVO_TEXT = (
    "Novo Nordisk said on Monday it would buy back up to 5 billion kroner of shares.\n"
    "Sales of Wegovy rose 12% in the quarter, below the 15% analysts expected."
)
VALERO_TEXT = "Valero shares are heading for their best year since 1982, Michael Burry said."
BENZINGA_TEXT = "Novo Nordisk cut its full-year sales guidance to growth of 8% to 11%."


def context(ticker="NVO", results=RESULTS) -> TickerContext:
    items = [Headline(title=t, snippet="snippet", source=s, when="2 hours ago", url=u) for s, u, t in results]
    return TickerContext(ticker=ticker, headlines=[h.as_line() for h in items],
                         sources=[h.as_dict() for h in items])


def journal_line(ticker="NVO", results=RESULTS, ts="2026-09-28T14:42:00+00:00") -> str:
    return json.dumps({
        "ts_utc": ts, "ticker": ticker, "context": context(ticker, results).as_dict(),
        "signal": None, "outcome": None, "error": None,
    })


def entries(*lines: str) -> list:
    return list(runner.load_entries(list(lines)))


def signal(ticker="NVO", bias=Bias.NEUTRAL, conviction=0.2, news_score=0.1) -> LLMSignal:
    return LLMSignal(ticker=ticker, bias=bias, conviction=conviction,
                     rationale="Buyback is small; guidance cut matters more.", news_score=news_score)


class FakeResponse:
    _MISSING = object()

    def __init__(self, status=200, text="", headers=None, payload=_MISSING):
        self.status_code = status
        self.text = text if payload is self._MISSING else json.dumps(payload)
        self.headers = headers or {}
        self._payload = payload

    def json(self):
        if self._payload is not self._MISSING:
            return self._payload
        return json.loads(self.text)


class FakeHttp:
    """The Unlocker serves ``pages``; the scraper's trigger and polls answer in order."""

    def __init__(self, pages=None, trigger=None, polls=()):
        self.pages = pages or {}
        self.trigger = trigger
        self.polls = list(polls)
        self.posts: list = []
        self.gets: list = []

    def post(self, url, body, headers):
        self.posts.append((url, body, headers))
        if url == news.BRIGHTDATA_REQUEST_URL:
            status, page = self.pages.get(body["url"], (404, "gone"))
            return FakeResponse(status, page, headers={"x-brd-err-msg": "target said 404"} if status == 404 else {})
        return self.trigger

    def get(self, url, headers):
        self.gets.append((url, headers))
        if url == news.BRIGHTDATA_REQUEST_URL.replace("request", "datasets/list"):
            return FakeResponse(200, payload=[])   # an empty scraper library
        return self.polls.pop(0)


class RoutedHttp(FakeHttp):
    """Answers Bright Data's API by URL, longest prefix first; the Unlocker as FakeHttp does.

    Each route's answers are handed out in order, and the last one repeats.
    """

    def __init__(self, routes, pages=None):
        super().__init__(pages=pages or {})
        self.routes = {key: list(answers) for key, answers in routes.items()}

    def _answer(self, method, url):
        for (verb, prefix), answers in sorted(self.routes.items(), key=lambda kv: -len(kv[0][1])):
            if verb == method and url.startswith(prefix):
                return answers.pop(0) if len(answers) > 1 else answers[0]
        raise AssertionError(f"unexpected {method} {url}")

    def post(self, url, body, headers):
        if url == news.BRIGHTDATA_REQUEST_URL:
            return super().post(url, body, headers)
        self.posts.append((url, body, headers))
        return self._answer("POST", url)

    def get(self, url, headers):
        self.gets.append((url, headers))
        return self._answer("GET", url)


API = ap.BRIGHTDATA_API
CREATE = API + "dca/collector"
AUTOMATE = API + "dca/collectors/c_1/automate_template"
PROGRESS = AUTOMATE + "/progress"


def build_routes(create=None, automate=None, progress=None, **extra):
    routes = {
        ("POST", CREATE): create or [FakeResponse(200, payload={"id": "c_1", "name": "article-probe yahoo"})],
        ("POST", AUTOMATE): automate or [FakeResponse(200, payload={})],
        ("GET", PROGRESS): progress or [FakeResponse(200, payload={"status": "running", "step": "writing"}),
                                        FakeResponse(200, payload={"status": "done",
                                                                   "completed_steps": ["plan", "code", "test"]})],
    }
    routes.update(extra.get("more") or {})
    return routes


def plain_text(page: str, url: str) -> tuple[str, str, str]:
    """A fake extractor: the 'page' is already the article's text."""
    return page, "", ""


GOOGLE_NOTICE = (
    "<html><head><title>Redirect Notice</title></head><body>"
    f'<a href="https://www.google.com/">Google</a> The page you were on is trying to send you to '
    f'<a href="{PUBLISHER}">{PUBLISHER}</a></body></html>'
)

UNLOCKER_PAGES = {
    YAHOO_1: (200, NOVO_TEXT),
    STOCKTWITS: (200, VALERO_TEXT),
    YAHOO_2: (200, "Novo Nordisk faces a patent cliff.\nIts pipeline is thin."),
    news.absolute_url(GOOGLE_STUB): (200, GOOGLE_NOTICE),
    PUBLISHER: (200, BENZINGA_TEXT),
}


# --------------------------------------------------------------------------- #
# Which links are stories
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize("url, kind", [
    (YAHOO_1, ap.ARTICLE),
    (STOCKTWITS, ap.ARTICLE),
    (news.absolute_url(GOOGLE_STUB), ap.GOOGLE_REDIRECT),
    (QUOTE, ap.NOT_AN_ARTICLE),
    ("https://www.tradingview.com/symbols/BMV-HDB/N/etfs/", ap.NOT_AN_ARTICLE),
    ("https://www.stocktitan.net/sec-filings/BANR/form-4-banner-corp.html", ap.NOT_AN_ARTICLE),
    ("https://www.cnbc.com/video/2026/09/14/teva-ceo.html", ap.NOT_AN_ARTICLE),
    ("https://www.bloomberg.com/news/videos/2026-09-14/teva-ceo", ap.NOT_AN_ARTICLE),
    ("", ap.NO_LINK),
])
def test_a_link_is_classified_by_what_is_behind_it(url, kind):
    assert ap.classify(url) == kind


def test_a_site_includes_its_regional_editions_and_nothing_else():
    assert ap.on_site(YAHOO_1, "finance.yahoo.com")
    assert ap.on_site(YAHOO_2, "finance.yahoo.com")
    assert ap.on_site("https://www.stocktwits.com/x", "stocktwits.com")
    assert not ap.on_site(STOCKTWITS, "finance.yahoo.com")
    assert not ap.on_site("https://notfinance.yahoo.com.evil.test/x", "finance.yahoo.com")


def test_the_site_set_is_articles_on_the_site_only():
    """A quote page on the site is not something the scraper should read."""
    assert ap.site_indexes(context(), "finance.yahoo.com") == [0, 2]


def test_relative_google_stubs_are_given_an_origin_before_they_are_classified():
    links = ap.result_links(context())
    assert links[4][2] == news.GOOGLE_ORIGIN + GOOGLE_STUB
    assert ap.classify(links[4][2]) == ap.GOOGLE_REDIRECT


# --------------------------------------------------------------------------- #
# Which line
# --------------------------------------------------------------------------- #


def test_the_default_pick_is_the_latest_single_stock_with_enough_site_articles():
    one_yahoo = [RESULTS[0], RESULTS[1]]
    lines = entries(
        journal_line("NVO", ts="2026-09-25T15:00:00+00:00"),
        journal_line("LLY", results=one_yahoo, ts="2026-09-28T14:41:00+00:00"),
        journal_line("IWM", ts="2026-09-28T14:43:00+00:00"),
    )
    chosen = ap.pick(lines, "finance.yahoo.com")
    # LLY is later but has one site article; IWM is a fund.
    assert chosen.ticker == "NVO"
    assert chosen.ts_utc.startswith("2026-09-25")


def test_a_named_ticker_or_day_is_taken_whatever_its_site_links():
    one_yahoo = [RESULTS[0], RESULTS[1]]
    lines = entries(
        journal_line("NVO", ts="2026-09-25T15:00:00+00:00"),
        journal_line("LLY", results=one_yahoo, ts="2026-09-28T14:41:00+00:00"),
    )
    assert ap.pick(lines, "finance.yahoo.com", ticker="lly").ticker == "LLY"
    assert ap.pick(lines, "finance.yahoo.com", day="2026-09-28").ticker == "LLY"
    assert ap.pick(lines, "finance.yahoo.com", ticker="NVO", day="2026-09-28") is None


def test_a_fund_is_never_picked_even_by_name():
    assert ap.pick(entries(journal_line("IWM")), "finance.yahoo.com", ticker="IWM") is None


def test_a_line_whose_sources_do_not_line_up_with_its_headlines_is_skipped():
    record = json.loads(journal_line())
    record["context"]["sources"] = record["context"]["sources"][:-1]
    assert ap.pick(entries(json.dumps(record)), "finance.yahoo.com") is None


# --------------------------------------------------------------------------- #
# Fetching
# --------------------------------------------------------------------------- #


def test_a_page_is_one_unlocker_request_through_the_production_zone():
    http = FakeHttp(pages=UNLOCKER_PAGES)
    page = ap.fetch_page(http, "tok", "cli_unlocker", 0, "Yahoo Finance", YAHOO_1)
    assert page.requests == 1 and page.html == NOVO_TEXT and not page.error
    url, body, headers = http.posts[0]
    assert url == news.BRIGHTDATA_REQUEST_URL
    assert body == {"zone": "cli_unlocker", "url": YAHOO_1, "format": "raw"}
    assert headers["Authorization"] == "Bearer tok"


def test_google_s_redirect_page_is_followed_once_to_the_publisher():
    http = FakeHttp(pages=UNLOCKER_PAGES)
    stub = news.absolute_url(GOOGLE_STUB)
    page = ap.fetch_page(http, "tok", "z", 4, "Benzinga", stub)
    assert page.requests == 2
    assert page.final_url == PUBLISHER
    assert page.html == BENZINGA_TEXT
    assert [body["url"] for _, body, _ in http.posts] == [stub, PUBLISHER]


def test_a_redirect_the_unlocker_already_followed_is_not_followed_again():
    stub = news.absolute_url(GOOGLE_STUB)
    http = FakeHttp(pages={stub: (200, "<html><title>Novo cuts guidance</title>" + BENZINGA_TEXT)})
    page = ap.fetch_page(http, "tok", "z", 4, "Benzinga", stub)
    assert page.requests == 1 and page.html and not page.error


def test_a_google_page_with_no_destination_is_an_error_not_an_article():
    stub = news.absolute_url(GOOGLE_STUB)
    http = FakeHttp(pages={stub: (200, "<html><title>Google</title><p>Please enable JavaScript</p></html>")})
    page = ap.fetch_page(http, "tok", "z", 4, "Benzinga", stub)
    assert page.error and not page.html


def test_a_page_with_nothing_to_read_costs_no_request():
    http = FakeHttp(pages=UNLOCKER_PAGES)
    page = ap.fetch_page(http, "tok", "z", 3, "Yahoo Finance", QUOTE)
    assert page.kind == ap.NOT_AN_ARTICLE and page.requests == 0 and not http.posts


def test_a_refused_page_is_reported_with_bright_data_s_reason():
    page = ap.fetch_page(FakeHttp(pages={}), "tok", "z", 0, "Yahoo Finance", YAHOO_1)
    assert page.status == 404 and "target said 404" in page.error and not page.html


def test_a_transport_failure_is_a_row_not_a_crash():
    import httpx

    class Broken(FakeHttp):
        def post(self, url, body, headers):
            raise httpx.ReadTimeout("slow")

    page = ap.fetch_page(Broken(), "tok", "z", 0, "Yahoo Finance", YAHOO_1)
    assert "ReadTimeout" in page.error and not page.html


# --------------------------------------------------------------------------- #
# From a page to the model's words
# --------------------------------------------------------------------------- #


def test_the_lede_drops_the_repeated_title_and_repeats_and_stops_at_the_cap():
    text = "Novo shares slide\nFirst paragraph here.\nFirst paragraph here.\n" + " ".join(["word"] * 50)
    parts = ap.paragraphs(text, title="Novo shares slide")
    assert parts[0] == "First paragraph here."
    assert len(parts) == 2
    lede = ap.lede_of(parts, 10)
    assert lede.words == 10
    assert lede.text.endswith(" …")
    assert lede.article_words == 3 + 50


def test_boilerplate_is_counted_in_the_words_the_model_would_get():
    parts = ["Novo Nordisk cut its guidance.", "Sign up for our newsletter to read more."]
    lede = ap.lede_of(parts, 100)
    assert lede.boilerplate_words == len(parts[1].split())
    assert 0 < lede.boilerplate_share < 1


def test_an_empty_article_has_no_lede():
    assert ap.lede_of([], 300) is None


@pytest.mark.parametrize("ticker, text, expected", [
    ("NVO", NOVO_TEXT, True),
    ("NVO", VALERO_TEXT, False),
    ("NVO", "Shares of NVO fell.", True),
    ("NVO", "NVOX is a different company.", False),
    ("GOOGL", "Google's cloud unit grew.", True),
    ("LLY", "Lilly's pill beat Novo's.", True),
])
def test_a_crude_check_says_whether_the_story_names_the_company(ticker, text, expected):
    assert ap.mentions_company(text, ticker) is expected


def test_a_short_text_on_a_page_that_asks_for_a_subscription_reads_as_a_teaser():
    assert ap.paywall_suspected("Novo cut guidance.", "<div>Subscribe to continue reading</div>")
    assert not ap.paywall_suspected(" ".join(["word"] * 400), "<div>Subscribe to continue reading</div>")
    assert not ap.paywall_suspected("Novo cut guidance.", "<div>an ordinary page</div>")


def test_an_extractor_that_fails_costs_the_page_not_the_probe():
    def boom(page, url):
        raise RuntimeError("bad html")

    page = ap.Page(index=0, source="Yahoo", url=YAHOO_1, kind=ap.ARTICLE, html="<p>x</p>")
    ap.read_page(page, "NVO", 300, boom)
    assert "extraction failed" in page.error and page.lede is None


# --------------------------------------------------------------------------- #
# The Scraper Studio scraper
# --------------------------------------------------------------------------- #


def fast(**overrides):
    ticks = iter(range(0, 10_000, 5))
    return dict(sleep=lambda s: None, clock=lambda: next(ticks), **overrides)


def test_the_token_is_never_sent_anywhere_but_bright_data():
    http = FakeHttp()
    run = ap.run_scraper(http, "tok", "https://evil.example/dca/trigger?collector=c_1", [YAHOO_1], **fast())
    assert "refusing" in run.error
    assert not http.posts and not http.gets


def test_records_returned_at_once_are_taken_as_they_are():
    record = {"url": YAHOO_1, "body": NOVO_TEXT}
    http = FakeHttp(trigger=FakeResponse(200, payload=[record]))
    run = ap.run_scraper(http, "tok", ap.BRIGHTDATA_API + "datasets/v3/scrape?dataset_id=gd_1", [YAHOO_1], **fast())
    assert run.records == [record] and not run.error
    assert http.posts[0][1] == [{"url": YAHOO_1}]


def test_a_datasets_job_is_collected_from_its_snapshot_once_ready():
    record = {"url": YAHOO_1, "body": NOVO_TEXT}
    http = FakeHttp(
        trigger=FakeResponse(200, payload={"snapshot_id": "s_abc"}),
        polls=[FakeResponse(202, payload={"status": "running"}), FakeResponse(200, payload=[record])],
    )
    run = ap.run_scraper(http, "tok", ap.BRIGHTDATA_API + "datasets/v3/trigger?dataset_id=gd_1", [YAHOO_1], **fast())
    assert run.records == [record] and not run.error
    assert http.gets[0][0] == ap.BRIGHTDATA_API + "datasets/v3/snapshot/s_abc?format=json"
    assert run.requests == 3


def test_a_collector_job_is_collected_from_its_dataset_once_built():
    record = {"input": {"url": YAHOO_1}, "text": NOVO_TEXT}
    http = FakeHttp(
        trigger=FakeResponse(200, payload={"collection_id": "j_xyz"}),
        polls=[FakeResponse(200, payload={"status": "building"}), FakeResponse(200, payload=[record])],
    )
    run = ap.run_scraper(http, "tok", ap.BRIGHTDATA_API + "dca/trigger?collector=c_1&queue_next=1", [YAHOO_1],
                         **fast())
    assert run.records == [record]
    assert http.gets[0][0] == ap.BRIGHTDATA_API + "dca/dataset?id=j_xyz"


def test_a_realtime_collector_answers_with_one_record():
    record = {"url": YAHOO_1, "body": NOVO_TEXT}
    http = FakeHttp(
        trigger=FakeResponse(200, payload={"response_id": "z_1"}),
        polls=[FakeResponse(202, text="pending", payload={"status": "pending"}), FakeResponse(200, payload=record)],
    )
    run = ap.run_scraper(http, "tok", ap.BRIGHTDATA_API + "dca/trigger_immediate?collector=c_1", [YAHOO_1],
                         **fast())
    assert run.records == [record]


def test_newline_delimited_records_are_read_too():
    lines = "\n".join(json.dumps({"url": u, "body": "text"}) for u in (YAHOO_1, YAHOO_2))
    http = FakeHttp(trigger=FakeResponse(200, text=lines))
    run = ap.run_scraper(http, "tok", ap.BRIGHTDATA_API + "datasets/v3/scrape?dataset_id=gd_1",
                         [YAHOO_1, YAHOO_2], **fast())
    assert len(run.records) == 2


def test_a_refused_trigger_and_a_job_that_never_finishes_are_errors_not_hangs():
    refused = ap.run_scraper(FakeHttp(trigger=FakeResponse(401, text="bad token")), "tok",
                             ap.BRIGHTDATA_API + "dca/trigger?collector=c_1", [YAHOO_1], **fast())
    assert "HTTP 401" in refused.error

    forever = FakeHttp(trigger=FakeResponse(200, payload={"snapshot_id": "s_1"}),
                       polls=[FakeResponse(202, payload={"status": "running"})] * 500)
    slow = ap.run_scraper(forever, "tok", ap.BRIGHTDATA_API + "datasets/v3/trigger?dataset_id=gd_1", [YAHOO_1],
                          **fast(deadline=60))
    assert "not ready" in slow.error


def test_an_unrecognised_answer_is_reported_verbatim():
    http = FakeHttp(trigger=FakeResponse(200, payload={"something": "else"}))
    run = ap.run_scraper(http, "tok", ap.BRIGHTDATA_API + "dca/trigger?collector=c_1", [YAHOO_1], **fast())
    assert "unrecognised" in run.error and "something" in run.error


@pytest.mark.parametrize("record, expected", [
    ({"url": YAHOO_1, "title": "T", "body": "the body"}, ("body", "the body")),
    ({"url": YAHOO_1, "paragraphs": ["one", "two"]}, ("paragraphs", "one\ntwo")),
    ({"url": YAHOO_1, "title": "A long title that is not the article", "story": "the story itself, longer still"},
     ("story", "the story itself, longer still")),
    ({"url": YAHOO_1, "title": "only metadata"}, ("", "")),
])
def test_the_article_text_is_found_whatever_the_field_was_called(record, expected):
    assert ap.record_text(record) == expected


def test_records_are_matched_to_urls_by_url_then_by_order():
    records = [{"url": "https://www.finance.yahoo.com/markets/stocks/articles/novo-buyback-135000341.html/",
                "body": "a"}]
    assert ap.align(records, [YAHOO_1, YAHOO_2]) == {YAHOO_1: records[0]}
    unlabelled = [{"body": "a"}, {"body": "b"}]
    assert ap.align(unlabelled, [YAHOO_1, YAHOO_2]) == {YAHOO_1: unlabelled[0], YAHOO_2: unlabelled[1]}
    assert ap.align(unlabelled, [YAHOO_1]) == {}


def test_a_scraper_record_that_is_not_an_object_or_is_an_error_is_a_failed_row():
    pages = [ap.Page(index=0, source="Yahoo", url=YAHOO_1, kind=ap.ARTICLE, text=NOVO_TEXT),
             ap.Page(index=2, source="Yahoo", url=YAHOO_2, kind=ap.ARTICLE, text="x")]
    strings = ap.read_scraped(ap.ScraperRun(records=["just text", "more text"]), pages, [0, 2], 300)
    assert all("not an object" in s.error for s in strings)
    errors = ap.read_scraped(ap.ScraperRun(records=[{"url": YAHOO_1, "error": "blocked"}]), pages, [0, 2], 300)
    assert errors[0].error == "blocked" and errors[0].lede is None
    assert errors[1].error == "no record came back for this URL"


def test_the_same_story_from_both_sources_reads_as_the_same_text():
    assert ap.contained(NOVO_TEXT, NOVO_TEXT + "\nSign up for our newsletter.") == 1.0
    assert ap.contained(NOVO_TEXT, VALERO_TEXT) == 0.0
    assert ap.contained("too short", NOVO_TEXT) is None


@pytest.mark.parametrize("status, payload, text, pending", [
    (202, {"status": "running"}, "", True),
    (500, None, "oops", True),
    (404, None, "not yet", True),
    (200, None, "", True),
    (200, None, "null", True),
    (200, {"pending": True}, "", True),
    (200, {"status": "building"}, "", True),
    (200, {"status": "done"}, "", False),
    (200, {"url": YAHOO_1, "body": "text"}, "", False),
])
def test_not_ready_yet_is_read_the_way_bright_data_s_cli_reads_it(status, payload, text, pending):
    assert ap._pending(status, payload, text) is pending


# --------------------------------------------------------------------------- #
# Building the scraper through Scraper Studio's API
# --------------------------------------------------------------------------- #


def test_scraper_studio_s_ai_builds_the_scraper_with_the_cli_s_own_calls():
    http = RoutedHttp(build_routes())
    build = ap.build_scraper(http, "tok", "finance.yahoo.com", [YAHOO_1, YAHOO_2], **fast())
    assert build.status == "done" and build.collector_id == "c_1" and not build.error
    assert build.steps == ["plan", "code", "test"]
    assert build.trigger == API + "dca/trigger?collector=c_1"
    (create_url, create_body, headers), (automate_url, automate_body, _) = http.posts
    assert create_url == CREATE and create_body["deliver"] == ap.SCRAPER_DELIVERY and create_body["name"]
    assert headers["Authorization"] == "Bearer tok"
    assert automate_url == AUTOMATE
    assert automate_body == {"description": ap.SCRAPER_DESCRIPTION, "urls": [YAHOO_1, YAHOO_2]}
    assert [url for url, _ in http.gets] == [PROGRESS, PROGRESS]
    assert all(url.startswith(API) for url, *_ in http.posts + http.gets)


def test_the_ai_s_parallel_build_cap_is_waited_out_not_fatal():
    waits: list = []
    ticks = iter(range(0, 10_000, 5))
    http = RoutedHttp(build_routes(automate=[FakeResponse(429, text="cannot run more than 3 jobs in parallel"),
                                             FakeResponse(200, payload={})]))
    build = ap.build_scraper(http, "tok", "finance.yahoo.com", [YAHOO_1],
                             sleep=waits.append, clock=lambda: next(ticks))
    assert build.status == "done"
    assert waits[0] == ap.SCRAPER_BUILD_RETRY_BASE_SECONDS
    assert any("HTTP 429" in line for line in build.log)


@pytest.mark.parametrize("status, message", [
    ("failed", "ended with status 'failed'"),
    ("pending_answer", "waiting for an answer in Scraper Studio's web UI"),
])
def test_a_build_that_fails_or_waits_for_a_person_says_so_and_runs_nothing(status, message):
    http = RoutedHttp(build_routes(progress=[FakeResponse(200, payload={"status": status})]))
    build = ap.build_scraper(http, "tok", "finance.yahoo.com", [YAHOO_1], **fast())
    assert message in build.error and build.trigger == ""


def test_a_build_that_never_finishes_stops_at_its_deadline():
    http = RoutedHttp(build_routes(progress=[FakeResponse(200, payload={"status": "running", "step": "testing"})]))
    build = ap.build_scraper(http, "tok", "finance.yahoo.com", [YAHOO_1], **fast(deadline=60))
    assert "not done after 60s" in build.error and "running at step testing" in build.error
    assert build.trigger == ""


def test_a_refused_create_leaves_no_collector_behind_to_run():
    http = RoutedHttp(build_routes(create=[FakeResponse(401, text="invalid token")]))
    build = ap.build_scraper(http, "tok", "finance.yahoo.com", [YAHOO_1], **fast())
    assert "creating the collector failed: HTTP 401 invalid token" in build.error
    assert not build.collector_id and build.trigger == "" and len(http.posts) == 1


@pytest.mark.parametrize("site, brand", [
    ("finance.yahoo.com", "yahoo"), ("uk.finance.yahoo.com", "yahoo"),
    ("www.stocktwits.com", "stocktwits"), ("localhost", "localhost"),
])
def test_a_site_s_brand_is_the_name_a_library_scraper_would_carry(site, brand):
    assert ap.brand_of(site) == brand


def test_the_library_is_searched_for_scrapers_named_for_the_site():
    library = [{"id": "gd_lmrpz3vxmz972ghd7", "name": "Yahoo Finance business information"},
               {"id": "gd_lyptx9h74wtlvpnfu", "name": "Reuters news"}]
    http = RoutedHttp({("GET", API + "datasets/list"): [FakeResponse(200, payload=library)]})
    found, seen, error = ap.library_matches(http, "tok", "finance.yahoo.com")
    assert found == [library[0]] and seen == 2 and not error


def test_a_library_that_cannot_be_listed_is_reported_not_fatal():
    http = RoutedHttp({("GET", API + "datasets/list"): [FakeResponse(404, text="not found")]})
    found, seen, error = ap.library_matches(http, "tok", "finance.yahoo.com")
    assert found == [] and seen == 0 and "HTTP 404" in error


# --------------------------------------------------------------------------- #
# The prompts
# --------------------------------------------------------------------------- #


def test_the_headlines_prompt_is_the_recorded_one_byte_for_byte():
    entry = entries(journal_line())[0]
    variants = ap.build_variants(entry.context, [], [])
    assert list(variants) == ["headlines"]
    assert heartbeat.build_user_prompt(variants["headlines"]) == heartbeat.build_user_prompt(entry.context)


def test_article_text_lands_under_its_own_headline_and_nowhere_else():
    entry = entries(journal_line())[0]
    page = ap.Page(index=2, source="Yahoo", url=YAHOO_2, kind=ap.ARTICLE,
                   lede=ap.Lede(text="Novo faces a patent cliff.", words=5, boilerplate_words=0, article_words=5))
    variants = ap.build_variants(entry.context, [page], [])
    before = entry.context.as_prompt().splitlines()
    after = variants["unlocker"].as_prompt().splitlines()
    added = [line for line in after if line not in before]
    assert added == ["  Article: Novo faces a patent cliff."]
    assert after.index(added[0]) == after.index("- " + entry.context.headlines[2]) + 1


def test_the_named_only_prompt_gives_text_to_the_stories_about_the_company_and_no_others():
    entry = entries(journal_line())[0]

    def page(index, text, mentions):
        return ap.Page(index=index, source="s", url="u", kind=ap.ARTICLE, mentions=mentions,
                       lede=ap.Lede(text=text, words=len(text.split()), boilerplate_words=0, article_words=9))

    variants = ap.build_variants(entry.context, [page(0, "novo buyback words", True),
                                                 page(1, "valero record words", False)], [])
    assert list(variants) == ["headlines", "unlocker", "unlocker-named"]
    named = variants["unlocker-named"].as_prompt()
    assert "novo buyback words" in named and "valero record words" not in named
    # When every story names the company the prompt would repeat `unlocker`, so it is not asked.
    every = ap.build_variants(entry.context, [page(0, "novo buyback words", True)], [])
    assert list(every) == ["headlines", "unlocker"]


def test_the_scraper_fills_the_pages_the_unlocker_could_not_read():
    entry = entries(journal_line())[0]

    def lede(text):
        return ap.Lede(text=text, words=len(text.split()), boilerplate_words=0, article_words=9)

    pages = [ap.Page(index=0, source="Yahoo", url=YAHOO_1, kind=ap.ARTICLE, error="HTTP 502"),
             ap.Page(index=1, source="Stocktwits", url=STOCKTWITS, kind=ap.ARTICLE, lede=lede("valero words"))]
    scraped = [ap.Scraped(index=0, url=YAHOO_1, lede=lede("yahoo words from the scraper"))]
    variants = ap.build_variants(entry.context, pages, scraped)
    # No result was read by both, so there is no like-for-like pair -- only the fill.
    assert list(variants) == ["headlines", "unlocker", "unlocker+scraper"]
    combined = variants["unlocker+scraper"].as_prompt()
    assert "valero words" in combined and "yahoo words from the scraper" in combined
    assert "yahoo words" not in variants["unlocker"].as_prompt()


def test_an_html_error_page_becomes_one_readable_line():
    gateway = "<html>\n<head><title>502 Bad Gateway</title></head>\n<body><center>nginx</center></body></html>"
    assert ap.brief(gateway) == "502 Bad Gateway nginx"
    page = ap.fetch_page(FakeHttp(pages={YAHOO_1: (502, gateway)}), "tok", "z", 0, "Yahoo Finance", YAHOO_1)
    assert page.error == "HTTP 502 502 Bad Gateway nginx"


def test_the_two_site_prompts_differ_only_in_where_the_words_came_from():
    entry = entries(journal_line())[0]

    def lede(text):
        return ap.Lede(text=text, words=len(text.split()), boilerplate_words=0, article_words=9)

    pages = [ap.Page(index=0, source="Yahoo", url=YAHOO_1, kind=ap.ARTICLE, lede=lede("unlocker words zero")),
             ap.Page(index=1, source="Stocktwits", url=STOCKTWITS, kind=ap.ARTICLE, lede=lede("valero words")),
             ap.Page(index=2, source="Yahoo", url=YAHOO_2, kind=ap.ARTICLE, lede=None)]
    scraped = [ap.Scraped(index=0, url=YAHOO_1, lede=lede("scraper words zero")),
               ap.Scraped(index=2, url=YAHOO_2, lede=lede("only the scraper read this"))]
    variants = ap.build_variants(entry.context, pages, scraped)
    # The scraper also read page 2, which the Unlocker could not: that is the fill.
    assert list(variants) == ["headlines", "unlocker", "unlocker+scraper", "unlocker-site", "scraper-site"]
    site_u = variants["unlocker-site"].as_prompt()
    site_s = variants["scraper-site"].as_prompt()
    # Only the result both sources read is in either; the Stocktwits page is not a site page.
    assert "unlocker words zero" in site_u and "scraper words zero" in site_s
    assert "valero" not in site_u and "only the scraper" not in site_s
    assert site_u.replace("unlocker words zero", "scraper words zero") == site_s


# --------------------------------------------------------------------------- #
# The model
# --------------------------------------------------------------------------- #


def fake_complete(answer=None, seen=None):
    def complete(system, user):
        if seen is not None:
            seen.append((system, user))
        text = json.dumps((answer or signal()).model_dump(mode="json"))
        return Completion(text=text, usage=Usage(model=llm.MODEL, input_tokens=len(user) // 4, output_tokens=900))
    return complete


def test_each_prompt_is_asked_with_the_production_system_prompt_and_user_prompt():
    entry = entries(journal_line())[0]
    seen: list = []
    variants = {"headlines": entry.context}
    system = heartbeat.system_prompt_for(entry.ticker, entry.context)
    calls = ap.ask_all(fake_complete(seen=seen), system, entry.ticker, variants, repeats=2, workers=1)
    assert [(c.variant, c.repeat) for c in calls] == [("headlines", 0), ("headlines", 1)]
    assert all(s == heartbeat.SYSTEM_PROMPT for s, _ in seen)
    assert all(u == heartbeat.build_user_prompt(entry.context) for _, u in seen)
    assert calls[0].signal.bias == Bias.NEUTRAL
    assert calls[0].output_tokens == 900 and calls[0].cost_usd is not None


def test_the_probe_asks_through_the_cycle_s_own_call(monkeypatch):
    seen = []
    monkeypatch.setattr(heartbeat, "call_llm", lambda s, u, schema: seen.append(schema) or "ok")
    assert ap.production_complete()("system", "user") == "ok"
    assert seen == [heartbeat.SIGNAL_JSON_SCHEMA]


def test_a_failed_call_or_an_answer_about_another_ticker_is_a_row_not_a_crash():
    entry = entries(journal_line())[0]

    def broken(system, user):
        raise llm.LLMError("HTTP 429")

    failed = ap.ask(broken, "sys", "NVO", "headlines", 0, entry.context)
    assert failed.signal is None and "429" in failed.error

    wrong = ap.ask(fake_complete(signal(ticker="LLY")), "sys", "NVO", "headlines", 0, entry.context)
    assert wrong.signal is None and "LLY" in wrong.error

    def prose(system, user):
        return Completion(text="I think it is bullish", usage=Usage(model=llm.MODEL))

    garbled = ap.ask(prose, "sys", "NVO", "headlines", 0, entry.context)
    assert garbled.signal is None and "invalid output" in garbled.error


# --------------------------------------------------------------------------- #
# End to end, and the report
# --------------------------------------------------------------------------- #


def full_run(scraper_trigger="", scraper_http_kwargs=None):
    entry = entries(journal_line())[0]
    record_1 = {"url": YAHOO_1, "title": "Novo buyback", "body": NOVO_TEXT}
    record_2 = {"url": YAHOO_2, "body": "Novo Nordisk faces a patent cliff.\nIts pipeline is thin."}
    http = FakeHttp(pages=UNLOCKER_PAGES, **(scraper_http_kwargs or {
        "trigger": FakeResponse(200, payload=[record_1, record_2])}))
    probe = ap.run(
        entry, site="finance.yahoo.com", words=300, repeats=2, http=http, token="tok", zone="cli_unlocker",
        extract=plain_text, complete=fake_complete(), scraper_trigger=scraper_trigger,
        model=llm.MODEL, effort="high", fetch_workers=2, model_workers=2, scraper_kwargs=fast(),
    )
    return probe, http


def test_a_run_reads_every_story_and_skips_what_is_not_one():
    probe, http = full_run()
    by_index = {p.index: p for p in probe.pages}
    assert by_index[3].kind == ap.NOT_AN_ARTICLE and by_index[3].requests == 0
    assert by_index[4].final_url == PUBLISHER and by_index[4].lede is not None
    assert by_index[1].mentions is False          # the Valero story on a Novo line
    assert by_index[0].mentions is True
    # Four stories, one of them through Google: five Unlocker requests, no scraper.
    assert sum(p.requests for p in probe.pages) == 5
    # The Valero story never names Novo, so the named-only prompt is asked too.
    assert list(probe.variants) == ["headlines", "unlocker", "unlocker-named"]
    assert len(probe.calls) == 6


def test_a_run_with_a_scraper_compares_the_two_on_the_same_pages():
    probe, http = full_run(scraper_trigger=ap.BRIGHTDATA_API + "datasets/v3/scrape?dataset_id=gd_1")
    assert [s.index for s in probe.scraped] == [0, 2]
    assert all(s.in_unlocker == 1.0 and s.unlocker_in == 1.0 for s in probe.scraped)
    assert list(probe.variants) == ["headlines", "unlocker", "unlocker-named", "unlocker-site", "scraper-site"]
    assert len(probe.calls) == 10
    trigger_posts = [p for p in http.posts if p[0] != news.BRIGHTDATA_REQUEST_URL]
    assert trigger_posts[0][1] == [{"url": YAHOO_1}, {"url": YAHOO_2}]


def test_the_report_and_the_record_say_what_happened():
    probe, _ = full_run(scraper_trigger=ap.BRIGHTDATA_API + "datasets/v3/scrape?dataset_id=gd_1")
    report = ap.render(probe)
    for heading in ("WHAT THE UNLOCKER GOT", "SCRAPER STUDIO", "WHAT THE MODEL READ AND SAID",
                    "RATIONALES", "LIMITS"):
        assert heading in report
    assert "skipped: not an article" in report
    assert "via Google to benzinga.com" in report
    assert "1 of them never name the company" in report
    record = json.loads(json.dumps(ap.as_json(probe)))
    assert record["ticker"] == "NVO" and len(record["calls"]) == 10
    assert "  Article: " in record["prompts"]["unlocker"]
    assert "  Article: " not in record["prompts"]["headlines"]


def test_a_run_without_a_scraper_says_so():
    probe, _ = full_run()
    assert "not asked: no scraper trigger URL" in ap.render(probe)


YAHOO_RECORDS = [
    {"url": YAHOO_1, "title": "Novo buyback", "body": NOVO_TEXT},
    {"url": YAHOO_2, "body": "Novo Nordisk faces a patent cliff.\nIts pipeline is thin."},
]


def test_a_run_that_builds_its_scraper_runs_it_on_the_same_pages():
    http = RoutedHttp(build_routes(more={
        ("GET", API + "datasets/list"): [FakeResponse(200, payload=[])],
        ("POST", API + "dca/trigger?collector=c_1"): [FakeResponse(200, payload={"collection_id": "j_1"})],
        ("GET", API + "dca/dataset?id=j_1"): [FakeResponse(200, payload={"status": "building"}),
                                              FakeResponse(200, payload=YAHOO_RECORDS)],
    }), pages=UNLOCKER_PAGES)
    probe = ap.run(
        entries(journal_line())[0], site="finance.yahoo.com", words=300, repeats=1, http=http,
        token="tok", zone="z", extract=plain_text, complete=fake_complete(), build=True,
        fetch_workers=1, model_workers=1, scraper_kwargs=fast(), build_kwargs=fast(),
    )
    assert probe.build.trigger == API + "dca/trigger?collector=c_1"
    assert probe.scraper.trigger == probe.build.trigger and not probe.scraper.error
    assert [s.index for s in probe.scraped] == [0, 2]
    assert all(s.in_unlocker == 1.0 for s in probe.scraped)
    assert "scraper-site" in probe.variants
    # The scraper was asked for the site's two article links, and only those.
    trigger_body = next(body for url, body, _ in http.posts if url.startswith(API + "dca/trigger"))
    assert trigger_body == [{"url": YAHOO_1}, {"url": YAHOO_2}]
    report = ap.render(probe)
    assert "built by Scraper Studio's AI: c_1" in report
    assert "reuse it: scraper_trigger=" + API + "dca/trigger?collector=c_1" in report
    assert "library: none of 0 ready-made scrapers is named for 'yahoo'" in report
    record = json.loads(json.dumps(ap.as_json(probe)))
    assert record["build"]["collector_id"] == "c_1" and record["library"]["scrapers_seen"] == 0


def test_a_scraper_that_exists_is_reused_never_rebuilt():
    trigger = API + "dca/trigger?collector=c_9"
    http = RoutedHttp({
        ("GET", API + "datasets/list"): [FakeResponse(200, payload=[])],
        ("POST", trigger): [FakeResponse(200, payload=YAHOO_RECORDS)],
    }, pages=UNLOCKER_PAGES)
    probe = ap.run(
        entries(journal_line())[0], site="finance.yahoo.com", words=300, repeats=1, http=http,
        token="tok", zone="z", extract=plain_text, build=True, scraper_trigger=trigger,
        fetch_workers=1, scraper_kwargs=fast(),
    )
    assert probe.build is None
    assert not any(url == CREATE for url, *_ in http.posts)
    assert len(probe.scraped) == 2 and not probe.scraper.error


def test_a_failed_build_is_reported_and_the_rest_of_the_probe_still_runs():
    http = RoutedHttp(build_routes(create=[FakeResponse(403, text="forbidden")], more={
        ("GET", API + "datasets/list"): [FakeResponse(200, payload=[])],
    }), pages=UNLOCKER_PAGES)
    probe = ap.run(
        entries(journal_line())[0], site="finance.yahoo.com", words=300, repeats=1, http=http,
        token="tok", zone="z", extract=plain_text, complete=fake_complete(), build=True,
        fetch_workers=1, model_workers=1, build_kwargs=fast(),
    )
    assert probe.scraper is None and "HTTP 403" in probe.build.error
    assert "unlocker" in probe.variants and probe.calls
    assert "build error: creating the collector failed: HTTP 403 forbidden" in ap.render(probe)


# --------------------------------------------------------------------------- #
# The command line
# --------------------------------------------------------------------------- #


def test_a_dry_run_needs_no_network_and_no_credentials(tmp_path, capsys, monkeypatch):
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line() + "\n")
    monkeypatch.setattr(ap, "Http", lambda *a, **k: pytest.fail("a dry run must not build a client"))
    assert ap.main(["--journal", str(journal), "--dry-run"]) == 0
    out = capsys.readouterr().out
    assert "<- finance.yahoo.com" in out and "[not an article]" in out and "[google redirect]" in out


def test_no_token_stops_the_run_before_anything_is_fetched(tmp_path, capsys, monkeypatch):
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line() + "\n")
    monkeypatch.setattr(ap, "Http", lambda *a, **k: pytest.fail("nothing may be fetched without a token"))
    assert ap.main(["--journal", str(journal), "--no-model"]) == 2
    assert "BRIGHTDATA_API_TOKEN" in capsys.readouterr().out


def test_no_line_that_fits_is_a_clear_failure(tmp_path, capsys):
    journal = tmp_path / "journal.log"
    journal.write_text(journal_line("IWM") + "\n")
    assert ap.main(["--journal", str(journal), "--dry-run"]) == 1
    assert "no single-stock line fits" in capsys.readouterr().out


# --------------------------------------------------------------------------- #
# The workflow
# --------------------------------------------------------------------------- #


def _workflow() -> dict:
    return yaml.safe_load((ROOT / ".github/workflows/article-probe.yml").read_text())


def _probe_step() -> dict:
    steps = _workflow()["jobs"]["probe"]["steps"]
    return next(s for s in steps if s.get("name") == "Fetch one context's articles and ask the model with and without them")


def test_the_probe_workflow_is_read_only_about_trading():
    for step in _workflow()["jobs"]["probe"]["steps"]:
        for name in step.get("env") or {}:
            assert "ALPACA" not in name.upper(), name
            assert "WEBHOOK" not in name.upper(), name
            assert "SUPABASE" not in name.upper(), name


def test_the_probe_reads_pages_and_asks_the_model_the_way_the_cycle_does():
    """Same zone, same key chain: a probe of a different setup is a probe of nothing."""
    cycle = yaml.safe_load((ROOT / ".github/workflows/heartbeat.yml").read_text())
    cycle_env = next(s for s in cycle["jobs"]["cycle"]["steps"] if s.get("name") == "Run one cycle")["env"]
    env = _probe_step()["env"]
    for name in ("FULL_MODEL_API_KEY", "BRIGHTDATA_API_TOKEN", "BRIGHTDATA_SERP_ZONE"):
        assert env[name] == cycle_env[name], name


def test_the_probe_costs_money_so_it_runs_by_hand_or_on_its_own_pull_request_only():
    wf = _workflow()
    triggers = wf.get("on") or wf[True]
    assert set(triggers) == {"workflow_dispatch", "pull_request"}
    assert sorted(triggers["pull_request"]["paths"]) == [
        ".github/workflows/article-probe.yml", "replay/article_probe.py"]
    # A fork's pull request gets no secrets; the job must skip rather than fail there.
    assert "github.repository" in wf["jobs"]["probe"]["if"]


def test_inputs_reach_the_script_as_variables_never_as_shell_text():
    run = _probe_step()["run"]
    assert "${{" not in run
    assert '--scraper-trigger "$SCRAPER_TRIGGER"' in run


def test_a_scraper_is_built_only_when_someone_asks_for_one():
    """A build leaves a collector in the Bright Data account that no API can
    delete, so it never happens on a pull-request run or by default."""
    wf = _workflow()
    triggers = wf.get("on") or wf[True]
    build = triggers["workflow_dispatch"]["inputs"]["build_scraper"]
    assert build["type"] == "boolean" and build["default"] is False
    step = _probe_step()
    assert step["env"]["BUILD_SCRAPER"] == "${{ inputs.build_scraper }}"
    assert '[ "$BUILD_SCRAPER" = "true" ] && args+=(--build-scraper)' in step["run"]


def test_the_extractor_is_installed_for_the_probe_and_nowhere_else():
    runs = " ".join(s.get("run", "") for s in _workflow()["jobs"]["probe"]["steps"])
    assert "trafilatura==" in runs
    assert "trafilatura" not in (ROOT / "requirements.txt").read_text()


def test_the_probe_keeps_what_it_read_even_when_it_fails():
    steps = _workflow()["jobs"]["probe"]["steps"]
    upload = next(s for s in steps if s.get("uses", "").startswith("actions/upload-artifact"))
    assert upload.get("if") == "always()"
    assert "probe.json" in upload["with"]["path"]


def test_the_probe_can_outlast_every_wait_it_may_meet():
    """Derived from the constants, so raising one without the clock fails here."""
    pages = news.MAX_HEADLINES
    fetching = math.ceil(pages / ap.FETCH_WORKERS) * 2 * ap.UNLOCKER_TIMEOUT_SECONDS
    # The build's retries sleep inside its own deadline; its last request can run past it.
    building = ap.SCRAPER_BUILD_DEADLINE_SECONDS + 2 * ap.UNLOCKER_TIMEOUT_SECONDS
    scraping = ap.UNLOCKER_TIMEOUT_SECONDS + ap.SCRAPER_DEADLINE_SECONDS + ap.UNLOCKER_TIMEOUT_SECONDS
    calls = len(ap.VARIANTS) * ap.DEFAULT_REPEATS
    asking = math.ceil(calls / ap.MODEL_WORKERS) * (
        llm.FULL_MODEL_TIMEOUT_SECONDS + llm.TRANSPORT_RETRY_TIMEOUT_SECONDS)
    minutes = (fetching + building + scraping + asking) / 60
    assert _workflow()["jobs"]["probe"]["timeout-minutes"] >= minutes + 5, f"needs ~{minutes:.0f} min"


def test_the_default_journal_is_the_real_one():
    assert ap.parse_args([]).journal == cfg.SIGNAL_JOURNAL_PATH
