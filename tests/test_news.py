"""Bright Data news provider: request shape, response parsing, failure modes."""

from __future__ import annotations

import json
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from orchestrator import heartbeat as hb
from orchestrator import news
from config.settings import Settings

PARSED_NEWS = {
    "general": {"search_engine": "google", "query": "AAPL stock", "results_cnt": 3},
    "news": [
        {"title": "Apple beats on earnings", "description": "Revenue up 8%", "source": "Reuters", "date": "2 hours ago", "link": "https://x/1"},
        {"title": "Apple beats on earnings", "description": "duplicate headline", "source": "Copycat", "link": "https://x/2"},
        {"title": "iPhone demand cools", "snippet": "Analysts trim targets", "source_name": "Bloomberg", "time": "5 hours ago"},
        {"title": "   ", "description": "blank title must be skipped"},
        "not-a-dict",
    ],
}


def test_search_url_targets_google_news_with_parsing_enabled():
    url = urlparse(news.build_news_search_url("AAPL"))
    q = parse_qs(url.query)
    assert url.netloc == "www.google.com"
    assert q["q"] == ["AAPL stock"]
    assert q["tbm"] == ["nws"]
    assert q["brd_json"] == ["1"]
    assert q["tbs"] == [f"qdr:{news.NEWS_LOOKBACK}"]


def test_parse_dedupes_and_formats_headlines():
    lines = news.parse_news_results(PARSED_NEWS)
    assert lines == [
        "Apple beats on earnings — Revenue up 8% (Reuters, 2 hours ago)",
        "iPhone demand cools — Analysts trim targets (Bloomberg, 5 hours ago)",
    ]


def test_parse_accepts_json_string_and_wrapped_body():
    as_string = json.dumps(PARSED_NEWS)
    assert news.parse_news_results(as_string) == news.parse_news_results(PARSED_NEWS)
    wrapped = {"status_code": 200, "headers": {}, "body": as_string}
    assert news.parse_news_results(wrapped) == news.parse_news_results(PARSED_NEWS)


def test_parse_falls_back_to_organic_results():
    payload = {"organic": [{"title": "Fallback", "description": "d", "display_link": "example.com"}]}
    assert news.parse_news_results(payload) == ["Fallback — d (example.com)"]


def test_parse_respects_limit_and_empty_payload():
    many = {"news": [{"title": f"h{i}"} for i in range(25)]}
    assert len(news.parse_news_results(many)) == news.MAX_HEADLINES
    assert news.parse_news_results({"general": {}}) == []
    assert news.parse_news_results({"news": []}) == []


@pytest.mark.parametrize(
    "payload",
    [
        "<html><body>captcha</body></html>",
        "not json at all",
        {"status_code": 200, "headers": {}, "body": "<!DOCTYPE html><html></html>"},
        {"status_code": 403, "headers": {"x-brd-err-msg": "zone not found"}, "body": ""},
        ["a", "list"],
    ],
)
def test_parse_rejects_html_and_error_wrappers(payload):
    with pytest.raises(news.NewsFetchError):
        news.parse_news_results(payload)


def test_provider_requires_token_and_zone():
    with pytest.raises(news.NewsFetchError):
        news.BrightDataNewsProvider("", "serp_api")
    with pytest.raises(news.NewsFetchError):
        news.BrightDataNewsProvider("tok", "")


def test_provider_posts_expected_request_and_returns_headlines():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = str(request.url)
        captured["headers"] = dict(request.headers)
        captured["body"] = json.loads(request.content)
        return httpx.Response(200, text=json.dumps(PARSED_NEWS))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok-123", "my_zone", client=client)
        lines = provider.fetch("AAPL")

    assert captured["url"] == news.BRIGHTDATA_REQUEST_URL
    assert captured["headers"]["authorization"] == "Bearer tok-123"
    assert captured["body"]["zone"] == "my_zone"
    assert captured["body"]["format"] == "raw"
    assert captured["body"]["url"] == news.build_news_search_url("AAPL")
    assert set(captured["body"]) == {"zone", "url", "format"}
    assert len(lines) == 2 and lines[0].startswith("Apple beats on earnings")


@pytest.mark.parametrize("status", [401, 403, 429, 500])
def test_provider_raises_on_http_error(status):
    handler = lambda request: httpx.Response(status, text="denied")  # noqa: E731
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with pytest.raises(news.NewsFetchError) as exc:
            provider.fetch("AAPL")
    assert str(status) in str(exc.value)


def test_provider_raises_on_transport_error():
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("boom")

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with pytest.raises(news.NewsFetchError):
            provider.fetch("AAPL")


def test_heartbeat_fetch_news_uses_settings(monkeypatch):
    seen = {}

    class FakeProvider:
        def __init__(self, token, zone, client=None):
            seen["token"], seen["zone"] = token, zone

        def fetch(self, ticker):
            seen["ticker"] = ticker
            return ["headline"]

    monkeypatch.setattr(hb, "BrightDataNewsProvider", FakeProvider)
    monkeypatch.setattr(
        hb, "get_settings",
        lambda: Settings(brightdata_api_token="t", brightdata_serp_zone="z", _env_file=None),
    )
    assert hb.fetch_news("MSFT") == ["headline"]
    assert seen == {"token": "t", "zone": "z", "ticker": "MSFT"}


def test_news_module_has_no_broker_or_engine_imports():
    src = (news.__file__ and open(news.__file__).read()) or ""
    assert "alpaca" not in src.lower()
    assert "from app" not in src and "import app" not in src
