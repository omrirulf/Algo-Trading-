"""The Unlocker check must ask the way Bright Data's tools ask, and send the token nowhere else."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from orchestrator import news
from replay import unlocker_check as uc

ROOT = Path(__file__).resolve().parents[1]
ARTICLE = "https://finance.yahoo.com/markets/stocks/articles/asml-asml-increases-despite-market-205005742.html"


class FakeResponse:
    def __init__(self, status=200, text="", headers=None, url=""):
        self.status_code = status
        self.text = text
        self.headers = headers or {}
        self.url = url

    def json(self):
        return json.loads(self.text)


def fake_fetch(calls):
    def fetch(method, url, headers, body):
        calls.append((method, url, headers, body))
        if body is None:
            return FakeResponse(200, "<html><title>ASML Increases</title><body>ASML rose on Monday.</body></html>",
                                {"server": "ATS"}, url="https://finance.yahoo.com/news/asml-asml-increases-despite-market-205005742.html")
        if body.get("format") == "json":
            return FakeResponse(200, json.dumps({"status_code": 502, "headers": {"server": "ATS"},
                                                 "body": "<html><title>502 Bad Gateway</title></html>"}))
        return FakeResponse(502, "<html><head><title>502 Bad Gateway</title></head><body><center><h1>502 Bad Gateway</h1></center></body></html>",
                            {"x-brd-err-code": "target_502"})
    return fetch


def test_the_token_goes_only_to_bright_data_and_the_control_carries_none():
    calls: list = []
    uc.run_all(fake_fetch(calls), "tok", "z", ARTICLE)
    direct = [c for c in calls if c[3] is None]
    unlocked = [c for c in calls if c[3] is not None]
    assert len(direct) == 1 and direct[0][1] == ARTICLE and "Authorization" not in direct[0][2]
    assert unlocked and all(url == news.BRIGHTDATA_REQUEST_URL for _, url, _, _ in unlocked)
    assert all(headers["Authorization"] == "Bearer tok" and body["zone"] == "z" for _, _, headers, body in unlocked)


def test_it_asks_the_ways_bright_data_s_own_tools_ask():
    bodies = [body for _, body in uc.variants(ARTICLE, "z") if body is not None]
    assert {"zone": "z", "url": ARTICLE, "format": "raw"} in bodies                              # the probe
    assert {"zone": "z", "url": ARTICLE, "format": "raw", "data_format": "markdown"} in bodies   # the MCP server
    assert {"zone": "z", "url": ARTICLE, "format": "json"} in bodies                             # the CLI's --format json
    assert {"zone": "z", "url": ARTICLE, "format": "raw", "country": "us"} in bodies             # the CLI's --country
    assert {"zone": "z", "url": "https://finance.yahoo.com/", "format": "raw"} in bodies


def test_yahoo_s_older_address_for_the_same_story():
    assert uc.news_path(ARTICLE) == "https://finance.yahoo.com/news/asml-asml-increases-despite-market-205005742.html"
    assert uc.news_path("https://finance.yahoo.com/healthcare/articles/lly-vs-nvo-102114784.html?.tsrc=rss") == \
        "https://finance.yahoo.com/news/lly-vs-nvo-102114784.html"
    assert uc.news_path("https://finance.yahoo.com/news/already-old-1.html") is None
    assert uc.news_path("https://www.cnbc.com/2026/09/29/articles/x.html") is None


def test_the_report_shows_what_each_way_got_headers_and_all():
    checks = uc.run_all(fake_fetch([]), "tok", "z", ARTICLE)
    text = uc.render(checks, ARTICLE, "z")
    assert "status: 200" in text and "final url: https://finance.yahoo.com/news/" in text
    assert "status: 502" in text and "x-brd-err-code: target_502" in text
    assert "bright data says: target_502" in text
    assert "the page itself answered: 502" in text
    assert "title: 502 Bad Gateway" in text and "body: 502 Bad Gateway" in text
    assert "tok" not in text.replace("token", "")


def test_a_network_error_is_one_line_not_the_end():
    def fetch(method, url, headers, body):
        import httpx
        raise httpx.ConnectError("boom")
    checks = uc.run_all(fetch, "tok", "z", ARTICLE)
    assert all(c.error.startswith("ConnectError") for c in checks)
    assert "error: ConnectError: boom" in uc.render(checks, ARTICLE, "z")


def test_the_workflow_holds_the_bright_data_keys_and_nothing_else():
    wf = yaml.safe_load((ROOT / ".github/workflows/unlocker-check.yml").read_text())
    step = next(s for s in wf["jobs"]["check"]["steps"] if s.get("name") == "Ask for the page every way")
    assert sorted(k for k, v in step["env"].items() if "secrets." in str(v)) == ["BRIGHTDATA_API_TOKEN"]
    assert "${{" not in step["run"]
    assert wf["permissions"] == {"contents": "read"}
    triggers = wf.get("on") or wf[True]
    assert sorted(triggers["pull_request"]["paths"]) == [".github/workflows/unlocker-check.yml", "replay/unlocker_check.py"]
    assert "github.repository" in wf["jobs"]["check"]["if"]
