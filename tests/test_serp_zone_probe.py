"""The SERP zone probe (replay/serp_zone_probe.py, the owner's decision of 16 Oct 2026).

Several arms, production's request, the vendor's own words on a refusal, and
the account API's answers shown by a few named fields only: the first run
printed the new zone's password, which an answer to ``POST /zone`` carries.
These pin what it sends, how it judges an answer, what it shows of the
account API, and that the workflow holds only the news fetch's credentials.
"""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import yaml

from orchestrator import news
from replay import serp_zone_probe as probe

ROOT = Path(__file__).resolve().parent.parent
NEWS = {"news": [{"title": "Microsoft reveals a chip", "source": "Reuters", "link": "https://example.test/a",
                  "date": "2 hours ago", "description": "d"}]}
CREATED = {"zone": {"created": "2026-10-16T19:52:26.819Z", "password": ["d6554hqradj6"], "ips": "any",
                    "plan": {"type": "unblocker", "serp": 1, "vips_type": "shared", "product": "serp"}},
           "plan": {"type": "unblocker", "serp": 1}}


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


# --------------------------------------------------------------------------- #
# The account API
# --------------------------------------------------------------------------- #


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


def test_the_create_answer_is_shown_by_a_few_fields_and_never_its_password():
    """16 Oct 2026: the first run printed the API's whole answer, password included."""
    sent = {}

    def fetch(method, url, headers, body):
        sent.update(method=method, url=url, body=body)
        return Response(200, payload=CREATED)
    words = probe.create_zone(fetch, "secret-tok", "serp_news_probe")
    assert sent["method"] == "POST" and sent["url"] == probe.ZONE_API and sent["body"] == probe.zone_body("serp_news_probe")
    assert words == "HTTP 200: created=2026-10-16T19:52:26.819Z, type=unblocker, serp=1, vips_type=shared, product=serp"
    assert "d6554hqradj6" not in words and "password" not in words and "secret-tok" not in words


def test_a_refused_create_shows_the_apis_first_words():
    words = probe.create_zone(lambda *a: Response(400, text="bad plan, token secret-tok"), "secret-tok", "z")
    assert words.startswith("HTTP 400: bad plan")


def test_delete_zone_asks_the_account_api_to_remove_it():
    sent = {}

    def fetch(method, url, headers, body):
        sent.update(method=method, url=url, body=body)
        return Response(200, text="")
    assert probe.delete_zone(fetch, "tok", "serp_news_probe") == "HTTP 200"
    assert sent == {"method": "DELETE", "url": probe.ZONE_API, "body": {"zone": "serp_news_probe"}}


# --------------------------------------------------------------------------- #
# The asks
# --------------------------------------------------------------------------- #


def test_the_arms_are_each_zone_plain_and_with_the_exit_country():
    arms = probe.arms_for("cli_unlocker", "serp_news_probe", "us")
    assert [(a.label, a.zone, a.extra) for a in arms] == [
        ("cli_unlocker", "cli_unlocker", {}),
        ("cli_unlocker, us exit", "cli_unlocker", {"country": "us"}),
        ("serp_news_probe", "serp_news_probe", {}),
        ("serp_news_probe, us exit", "serp_news_probe", {"country": "us"}),
    ]
    assert [a.label for a in probe.arms_for("cli_unlocker", None, "")] == ["cli_unlocker"]


def test_an_ask_is_productions_request_plus_the_arms_extra_and_is_judged_like_production():
    sent = []

    def fetch(method, url, headers, body):
        sent.append((method, url, body))
        return Response(200, payload=NEWS)
    arm = probe.Arm("cli_unlocker, us exit", "cli_unlocker", {"country": "us"})
    result = probe.ask(fetch, "tok", arm, "MSFT")
    assert sent[0][0] == "POST" and sent[0][1] == news.BRIGHTDATA_REQUEST_URL
    assert sent[0][2] == {"zone": "cli_unlocker", "url": news.build_news_search_url("MSFT"), "format": "raw",
                          "country": "us"}
    assert result.outcome == "news" and result.items == 1 and result.status == 200 and result.arm == arm.label


def test_an_empty_two_hundred_shows_bright_datas_headers():
    fetch = lambda *a: Response(200, text="", headers={"x-brd-status-code": "502",  # noqa: E731
                                                       "x-brd-error": "redirect location was rejected"})
    result = probe.ask(fetch, "tok", probe.Arm("z", "z"), "NVDA")
    assert result.outcome == "empty body"
    assert result.headers == "x-brd-status-code 502; x-brd-error redirect location was rejected"
    assert "[x-brd-status-code 502; x-brd-error redirect location was rejected]" in probe.line_for(result)


def test_a_block_page_is_refused_and_a_transport_error_is_an_error():
    refused = probe.ask(lambda *a: Response(200, text="<html>blocked</html>"), "tok", probe.Arm("z", "z"), "ASML")
    assert refused.outcome == "refused" and refused.refused

    def boom(*a):
        raise httpx.ReadTimeout("timed out")
    assert probe.ask(boom, "tok", probe.Arm("z", "z"), "ASML").outcome == "error"


def test_the_summary_counts_each_arm():
    arms = [probe.Arm("a", "a"), probe.Arm("b", "b")]
    asks = [
        probe.Ask("a", "MSFT", status=200, size=100, items=3, seconds=4.0),
        probe.Ask("a", "NVDA", status=200, size=0, empty=True, seconds=20.0),
        probe.Ask("b", "MSFT", status=200, size=100, items=2, seconds=3.0),
        probe.Ask("b", "NVDA", status=200, size=90, items=1, seconds=5.0),
    ]
    text = probe.summary(asks, arms)
    assert "a: 2 asks, news for 1 (50%), empty body 1 (50%), refused 0, HTTP/transport errors 0, median 12.0s" in text
    assert "b: 2 asks, news for 2 (100%), empty body 0 (0%), refused 0, HTTP/transport errors 0, median 4.0s" in text


def test_zone_a_is_productions_resolution(monkeypatch):
    monkeypatch.delenv("BRIGHTDATA_SERP_ZONE", raising=False)
    monkeypatch.delenv(news.CLI_UNLOCKER_ENV_VAR, raising=False)
    assert probe.zone_a_from_env() == "cli_unlocker"
    monkeypatch.setenv("BRIGHTDATA_SERP_ZONE", "my_serp")
    assert probe.zone_a_from_env() == "my_serp"
    assert probe.zone_a_from_env("explicit") == "explicit"


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #


def test_main_measures_only_production_when_zone_b_cannot_be_opened(monkeypatch, capsys):
    monkeypatch.setenv("BRIGHTDATA_API_TOKEN", "tok")
    monkeypatch.delenv("BRIGHTDATA_SERP_ZONE", raising=False)
    calls = []

    def fetch(method, url, headers, body):
        calls.append((method, url, body))
        if url == probe.ACTIVE_ZONES_API:
            return Response(200, payload=[{"name": "cli_unlocker"}])
        if url == probe.ZONE_API:
            return Response(400, text="no")
        return Response(200, payload=NEWS)
    assert probe.main(["--create", "--count", "2"], fetch=fetch) == 0
    out = capsys.readouterr().out
    assert "POST /zone -> HTTP 400: no" in out and "zone B is not asked" in out
    assert sum(1 for m, u, b in calls if u == news.BRIGHTDATA_REQUEST_URL) == 2       # two names, one arm
    assert "cli_unlocker: 2 asks, news for 2 (100%)" in out


def test_main_with_a_country_asks_each_zone_twice(monkeypatch, capsys):
    monkeypatch.setenv("BRIGHTDATA_API_TOKEN", "tok")
    monkeypatch.delenv("BRIGHTDATA_SERP_ZONE", raising=False)
    bodies = []

    def fetch(method, url, headers, body):
        if url == probe.ACTIVE_ZONES_API:
            return Response(200, payload=[{"name": "cli_unlocker"}, {"name": "serp_news_probe"}])
        bodies.append(body)
        return Response(200, payload=NEWS)
    assert probe.main(["--country", "us", "--count", "3"], fetch=fetch) == 0
    assert len(bodies) == 12                                    # 3 names x 4 arms
    assert sum(1 for b in bodies if b.get("country") == "us") == 6
    assert "4 arm(s)" in capsys.readouterr().out


def test_main_delete_zone_removes_it_and_does_nothing_else(monkeypatch, capsys):
    monkeypatch.setenv("BRIGHTDATA_API_TOKEN", "tok")
    calls = []

    def fetch(method, url, headers, body):
        calls.append((method, url))
        if method == "DELETE":
            return Response(200, text="")
        return Response(200, payload=[{"name": "cli_unlocker"}])
    assert probe.main(["--delete-zone", "serp_news_probe"], fetch=fetch) == 0
    assert calls == [("DELETE", probe.ZONE_API), ("GET", probe.ACTIVE_ZONES_API)]
    assert "now gone" in capsys.readouterr().out


def test_the_workflow_holds_only_the_news_fetchs_credentials():
    wf = yaml.safe_load((ROOT / ".github/workflows/serp-zone-probe.yml").read_text(encoding="utf-8"))
    assert wf["permissions"] == {"contents": "read"}
    env = next(s for s in wf["jobs"]["probe"]["steps"] if s.get("name") == "Ask both zones")["env"]
    assert set(k for k in env if "KEY" in k or "TOKEN" in k) == {"BRIGHTDATA_API_TOKEN"}
    triggers = wf.get("on") or wf.get(True)
    assert "replay/serp_zone_probe.py" in triggers["pull_request"]["paths"]
