"""The SERP zone probe (replay/serp_zone_probe.py, the owner's decision of 16 Oct 2026).

Two zones, production's request, the vendor's own words on a refusal. These
pin what it sends, how it judges an answer, and that the workflow holds only
the news fetch's credentials.
"""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest
import yaml

from orchestrator import news
from replay import serp_zone_probe as probe

ROOT = Path(__file__).resolve().parent.parent
NEWS = {"news": [{"title": "Microsoft reveals a chip", "source": "Reuters", "link": "https://example.test/a",
                  "date": "2 hours ago", "description": "d"}]}


class Response:
    def __init__(self, status: int, text: str = "", headers: dict | None = None, payload=None):
        self.status_code = status
        self.text = text if payload is None else json.dumps(payload)
        self.headers = httpx.Headers(headers or {})
        self._payload = payload

    def json(self):
        if self._payload is None:
            return json.loads(self.text)
        return self._payload


def test_the_zone_body_opens_a_serp_zone_that_costs_nothing_until_used():
    body = probe.zone_body("serp_news_probe")
    assert body == {"zone": {"name": "serp_news_probe", "type": "unblocker"}, "plan": {"type": "unblocker", "serp": True}}


def test_zone_exists_reads_the_active_zones():
    def fetch(method, url, headers, body):
        assert method == "GET" and url == probe.ACTIVE_ZONES_API and headers["Authorization"] == "Bearer tok"
        return Response(200, payload=[{"name": "cli_unlocker"}, {"name": "serp_news_probe"}])
    assert probe.zone_exists(fetch, "tok", "serp_news_probe") is True
    assert probe.zone_exists(fetch, "tok", "other") is False
    assert probe.zone_exists(lambda *a: Response(401, text="denied"), "tok", "x") is None


def test_create_zone_reports_the_apis_words_and_never_the_token():
    sent = {}

    def fetch(method, url, headers, body):
        sent.update(method=method, url=url, body=body)
        return Response(400, text="bad plan for token secret-tok")
    status, words = probe.create_zone(fetch, "secret-tok", "serp_news_probe")
    assert sent["method"] == "POST" and sent["url"] == probe.ZONE_API and sent["body"] == probe.zone_body("serp_news_probe")
    assert status == 400 and "secret-tok" not in words and "***" in words


def test_an_ask_is_productions_request_and_is_judged_like_production():
    sent = []

    def fetch(method, url, headers, body):
        sent.append((method, url, body))
        return Response(200, payload=NEWS)
    result = probe.ask(fetch, "tok", "cli_unlocker", "MSFT")
    assert sent[0][0] == "POST" and sent[0][1] == news.BRIGHTDATA_REQUEST_URL
    assert sent[0][2] == {"zone": "cli_unlocker", "url": news.build_news_search_url("MSFT"), "format": "raw"}
    assert result.outcome == "news" and result.items == 1 and result.status == 200


def test_an_empty_two_hundred_shows_bright_datas_headers():
    fetch = lambda *a: Response(200, text="", headers={"x-brd-status-code": "502"})  # noqa: E731
    result = probe.ask(fetch, "tok", "serp_news_probe", "NVDA")
    assert result.outcome == "empty body" and result.headers == "x-brd-status-code 502"
    assert "[x-brd-status-code 502]" in probe.line_for(result)


def test_a_block_page_is_refused_and_a_transport_error_is_an_error():
    refused = probe.ask(lambda *a: Response(200, text="<html>blocked</html>"), "tok", "z", "ASML")
    assert refused.outcome == "refused" and refused.refused

    def boom(*a):
        raise httpx.ReadTimeout("timed out")
    assert probe.ask(boom, "tok", "z", "ASML").outcome == "error"


def test_the_summary_counts_each_zone():
    asks = [
        probe.Ask("a", "MSFT", status=200, size=100, items=3, seconds=4.0),
        probe.Ask("a", "NVDA", status=200, size=0, empty=True, seconds=20.0),
        probe.Ask("b", "MSFT", status=200, size=100, items=2, seconds=3.0),
        probe.Ask("b", "NVDA", status=200, size=90, items=1, seconds=5.0),
    ]
    text = probe.summary(asks, ["a", "b"])
    assert "a: 2 asks, news for 1 (50%), empty body 1 (50%), refused 0, HTTP/transport errors 0, median 12.0s" in text
    assert "b: 2 asks, news for 2 (100%), empty body 0 (0%), refused 0, HTTP/transport errors 0, median 4.0s" in text


def test_zone_a_is_productions_resolution(monkeypatch):
    monkeypatch.delenv("BRIGHTDATA_SERP_ZONE", raising=False)
    monkeypatch.delenv(news.CLI_UNLOCKER_ENV_VAR, raising=False)
    assert probe.zone_a_from_env() == "cli_unlocker"
    monkeypatch.setenv("BRIGHTDATA_SERP_ZONE", "my_serp")
    assert probe.zone_a_from_env() == "my_serp"
    assert probe.zone_a_from_env("explicit") == "explicit"


def test_main_measures_only_production_when_zone_b_cannot_be_opened(monkeypatch, capsys):
    monkeypatch.setenv("BRIGHTDATA_API_TOKEN", "tok")
    monkeypatch.delenv("BRIGHTDATA_SERP_ZONE", raising=False)
    calls = []

    def fetch(method, url, headers, body):
        calls.append((method, url))
        if url == probe.ACTIVE_ZONES_API:
            return Response(200, payload=[{"name": "cli_unlocker"}])
        if url == probe.ZONE_API:
            return Response(400, text="no")
        return Response(200, payload=NEWS)
    assert probe.main(["--create", "--count", "2"], fetch=fetch) == 0
    out = capsys.readouterr().out
    assert "POST /zone -> HTTP 400: no" in out and "zone B is not asked" in out
    assert sum(1 for m, u in calls if u == news.BRIGHTDATA_REQUEST_URL) == 2       # two names, one zone
    assert "cli_unlocker: 2 asks, news for 2 (100%)" in out


def test_the_workflow_holds_only_the_news_fetchs_credentials():
    wf = yaml.safe_load((ROOT / ".github/workflows/serp-zone-probe.yml").read_text(encoding="utf-8"))
    assert wf["permissions"] == {"contents": "read"}
    env = next(s for s in wf["jobs"]["probe"]["steps"] if s.get("name") == "Ask both zones")["env"]
    assert set(k for k in env if "KEY" in k or "TOKEN" in k) == {"BRIGHTDATA_API_TOKEN"}
    triggers = wf.get("on") or wf.get(True)
    assert "replay/serp_zone_probe.py" in triggers["pull_request"]["paths"]
