"""The Bing news probe (replay/bing_news_probe.py, the owner's question of 4 Nov 2026).

Production's request on one arm and Bing's RSS feed on the others, judged the
way production judges an answer; the feed read into production's own
``Headline`` shape; the summary's arithmetic; and the workflow holding only
the news fetch's credentials.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import httpx
import yaml

from orchestrator import news
from replay import bing_news_probe as probe

ROOT = Path(__file__).resolve().parent.parent
NOW = datetime(2026, 11, 4, 20, 0, tzinfo=timezone.utc)
RSS = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:News="https://www.bing.com/news/search?q=TEVA+stock&amp;format=rss">
<channel><title>TEVA stock - Bing News</title>
<item><title>Teva raises its outlook after a strong quarter</title>
<link>https://www.bing.com/news/apiclick.aspx?ref=FexRss&amp;aid=&amp;url=https%3a%2f%2fexample.test%2fteva</link>
<description>The drugmaker lifted its full-year guidance.</description>
<pubDate>Wed, 04 Nov 2026 17:30:00 GMT</pubDate>
<News:Source>Reuters</News:Source></item>
<item><title>Teva raises its outlook after a strong quarter</title><link>https://example.test/dup</link>
<description>syndicated</description><pubDate>Wed, 04 Nov 2026 16:00:00 GMT</pubDate><News:Source>Other</News:Source></item>
<item><title>Generic drug prices fall again</title><link>https://example.test/generics</link>
<description>A   second   story.</description><pubDate>Tue, 03 Nov 2026 20:00:00 GMT</pubDate><News:Source>Bloomberg</News:Source></item>
</channel></rss>"""
GOOGLE = {"news": [{"title": "Teva raises outlook after strong quarter", "source": "Reuters", "link": "https://g/1",
                    "date": "2 hours ago", "description": "d"},
                   {"title": "Analysts weigh in on Teva", "source": "Barron's", "link": "https://g/2", "date": "5 hours ago"}]}


class Response:
    def __init__(self, status: int, text: str = "", headers: dict | None = None, payload=None):
        self.status_code = status
        self.text = text if payload is None else json.dumps(payload)
        self.headers = httpx.Headers(headers or {})


def test_the_bing_url_carries_productions_qualifier_and_the_24h_filter():
    assert probe.bing_news_url("TEVA") == ("https://www.bing.com/news/search?q=TEVA+stock&format=rss&setlang=en-US&cc=US")
    assert "q=GLD+ETF" in probe.bing_news_url("GLD") and "ETF" in news.build_news_search_url("GLD")
    assert probe.bing_news_url("TEVA", last_24h=True).endswith("&qft=interval%3D%227%22")


def test_the_feed_is_read_into_productions_headline_shape_newest_first_without_duplicates():
    stories = probe.parse_bing_rss(RSS, now=NOW)
    assert [s.headline.title for s in stories] == ["Teva raises its outlook after a strong quarter",
                                                   "Generic drug prices fall again"]
    first = stories[0].headline
    assert isinstance(first, news.Headline)
    assert first.source == "Reuters" and first.when == "2h ago" and first.snippet == "The drugmaker lifted its full-year guidance."
    assert first.url.startswith("https://www.bing.com/news/apiclick.aspx")
    assert first.as_line() == ("Teva raises its outlook after a strong quarter — The drugmaker lifted its full-year "
                               "guidance. (Reuters, 2h ago)")
    assert stories[1].headline.snippet == "A second story." and stories[1].age_hours == 24.0


def test_what_is_not_a_feed_is_refused_the_way_production_refuses_an_answer():
    for text in ("", "   ", "<html><body>blocked</body></html>", "{\"not\": \"xml\"}", "<rss><channel><item><title"):
        try:
            probe.parse_bing_rss(text, now=NOW)
        except news.NewsFetchError:
            continue
        raise AssertionError(f"accepted {text!r}")


def test_each_arm_sends_what_it_says_and_the_token_goes_only_to_bright_data():
    sent = []

    def fetch(method, url, headers, body):
        sent.append((method, url, headers, body))
        if url == news.BRIGHTDATA_REQUEST_URL:
            if "google.com" in body["url"]:
                return Response(200, payload=GOOGLE)
            return Response(200, text=RSS, headers={"x-brd-status-code": "200"})
        return Response(200, text=RSS)

    arms = probe.arms_for(bright_data=True)
    assert [a.label for a in arms] == [probe.GOOGLE, probe.BING_DIRECT, probe.BING_DIRECT_24H, probe.BING_BRIGHT_DATA_24H]
    asks = probe.probe(fetch, "secret-tok", "cli_unlocker", arms, ["TEVA"], now=NOW)
    assert [a.outcome for a in asks] == ["news"] * 4 and [a.items for a in asks] == [2, 2, 2, 2]
    google_body = sent[0][3]
    assert sent[0][1] == news.BRIGHTDATA_REQUEST_URL and google_body["zone"] == "cli_unlocker"
    assert google_body["url"] == news.build_news_search_url("TEVA") and google_body["country"] == news.BRD_COUNTRY
    assert sent[1][0] == "GET" and sent[1][1] == probe.bing_news_url("TEVA") and sent[1][3] is None
    assert "Authorization" not in sent[1][2] and "Authorization" not in sent[2][2]
    assert sent[2][1] == probe.bing_news_url("TEVA", last_24h=True)
    assert sent[3][3] == {"zone": "cli_unlocker", "url": probe.bing_news_url("TEVA", last_24h=True), "format": "raw",
                          "country": news.BRD_COUNTRY}
    assert asks[0].titles == ("Teva raises outlook after strong quarter", "Analysts weigh in on Teva")
    assert asks[2].newest_hours == 2.5 and asks[2].oldest_hours == 24.0


def test_a_refusal_an_error_and_a_block_page_are_judged_like_production():
    def fetch(method, url, headers, body):
        if body and "google.com" in body["url"]:
            return Response(200, text="", headers={"x-brd-status-code": "502", "x-brd-error": "redirect location was rejected"})
        if body:
            raise httpx.ReadTimeout("slow")
        return Response(200, text="<html>blocked</html>") if "qft" in url else Response(429, text="later")

    asks = probe.probe(fetch, "tok", "z", probe.arms_for(True), ["NVO"])
    google, direct, direct_24h, via = asks
    assert google.outcome == "refused" and google.refused == "empty body"
    assert google.headers == "x-brd-status-code 502; x-brd-error redirect location was rejected"
    assert direct.outcome == "HTTP 429" and direct_24h.outcome == "refused" and via.outcome == "error"
    assert via.error == "ReadTimeout"
    assert "redirect location was rejected" in probe.line_for(google) and "ReadTimeout" in probe.line_for(via)


def test_the_summary_counts_names_with_news_shared_headlines_and_rescues():
    arms = probe.arms_for(True)
    asks = [
        probe.Ask(probe.GOOGLE, "TEVA", 200, 1000, 2, ("Teva raises outlook after strong quarter", "Analysts weigh in on Teva"), seconds=4.0),
        probe.Ask(probe.BING_DIRECT, "TEVA", 200, 1000, 2, ("Teva raises its outlook after a strong quarter", "Generic drug prices fall"), 2.0, 24.0, seconds=1.0),
        probe.Ask(probe.BING_DIRECT_24H, "TEVA", 200, 1000, 1, ("Teva raises its outlook after a strong quarter",), 2.0, 2.0, seconds=1.0),
        probe.Ask(probe.BING_BRIGHT_DATA_24H, "TEVA", 200, 1000, 1, ("Teva raises its outlook after a strong quarter",), 2.0, 2.0, seconds=3.0),
        probe.Ask(probe.GOOGLE, "NVO", 200, 0, refused="empty body", headers="x-brd-status-code 502", seconds=3.0),
        probe.Ask(probe.BING_DIRECT, "NVO", 200, 900, 3, ("Novo cuts guidance", "b", "c"), 1.0, 20.0, seconds=1.0),
        probe.Ask(probe.BING_DIRECT_24H, "NVO", 200, 900, 1, ("Novo cuts guidance",), 1.0, 1.0, seconds=1.0),
        probe.Ask(probe.BING_BRIGHT_DATA_24H, "NVO", error="ReadTimeout", seconds=60.0),
    ]
    text = probe.summary(asks, arms)
    assert "google, Bright Data: 2 asks, news for 1 (50%), no items 0, refused 1, HTTP/transport errors 0" in text
    assert "bing rss, direct, 24h: 2 asks, news for 2 (100%)" in text and "newest story median 2h" in text
    assert "bing rss, Bright Data, 24h: 2 asks, news for 1 (50%), no items 0, refused 0, HTTP/transport errors 1" in text
    assert "bing rss, direct against google: 1 names with news on both; 1 of Google's 2 headlines also on Bing (50%)" in text
    assert "names Google did not answer that Bing (direct, 24h) did: 1 (NVO)" in text


def test_shared_titles_allows_the_outlets_different_wording_but_not_a_different_story():
    assert probe.shared_titles(("Teva raises outlook after strong quarter",), ("Teva raises its outlook after a strong quarter",)) == 1
    assert probe.shared_titles(("Teva raises outlook after strong quarter",), ("Generic drug prices fall again",)) == 0


def test_without_a_token_only_bings_feed_is_asked_and_nothing_is_billed(monkeypatch, capsys):
    monkeypatch.delenv("BRIGHTDATA_API_TOKEN", raising=False)
    monkeypatch.setattr(news, "resolve_token", lambda explicit="": "")
    sent = []

    def fetch(method, url, headers, body):
        sent.append(url)
        return Response(200, text=RSS)

    assert probe.main(["--count", "2", "--no-bright-data"], fetch=fetch) == 0
    out = capsys.readouterr().out
    assert all("bing.com" in url for url in sent) and len(sent) == 4
    assert "2 names x 2 arm(s)" in out and "secret" not in out and news.BRIGHTDATA_REQUEST_URL not in out


def test_the_workflow_holds_only_the_news_fetchs_credentials_and_changes_nothing():
    text = (ROOT / ".github" / "workflows" / "bing-news-probe.yml").read_text()
    flow = yaml.safe_load(text)
    assert flow["permissions"] == {"contents": "read"}
    job = flow["jobs"]["probe"]
    env = next(step for step in job["steps"] if step.get("name", "").startswith("Ask Google and Bing"))["env"]
    assert env["BRIGHTDATA_API_TOKEN"] == "${{ secrets.BRIGHTDATA_API_TOKEN }}"
    assert [k for k, v in env.items() if "secrets." in str(v)] == ["BRIGHTDATA_API_TOKEN"]
    assert "ALPACA" not in text and "ANTHROPIC" not in text and "NTFY" not in text
    assert "--no-bright-data" in text                                 # a pull request asks Bing only
