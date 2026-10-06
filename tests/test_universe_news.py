"""The shadow universe's own news query (the owner's decision of 3 Oct 2026): company name plus ticker.

Production's query and code stay as they were; the universe's search goes through production's provider
with only the ``q`` changed, and reads no credential itself.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from analysis.news_relevance import Matcher
from config import shadow_universe as su
from orchestrator import context, news, universe_news
from tests.test_news import PARSED_NEWS

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "orchestrator" / "universe_news.py"

#: The owner's list of 3 Oct 2026: kept, with the query fixed instead.
SHORT_TICKERS = ("SO", "C", "D", "T", "ED", "NOW", "V", "ICE", "O", "F", "MET", "EW")


# --------------------------------------------------------------------------- #
# The names and the query
# --------------------------------------------------------------------------- #


def test_every_name_of_the_list_has_a_company_name_and_no_other_name_has_one():
    assert set(su.COMPANIES) == set(su.TICKERS) and len(su.COMPANIES) == len(su.TICKERS) == 251
    for ticker, names in su.COMPANIES.items():
        assert names and all(isinstance(n, str) and n.strip() == n and n for n in names), ticker
        assert len(set(names)) == len(names), ticker


def test_the_query_is_company_name_plus_ticker():
    assert su.news_query("SO") == "Southern Company SO stock"   # the owner's example
    assert su.news_query("C") == "Citigroup C stock"
    assert su.news_query("STT") == "State Street STT stock"
    assert su.news_query("BP") == "BP plc BP stock"
    assert su.news_query("UPS") == "United Parcel Service UPS stock"
    for ticker in su.TICKERS:
        query = su.news_query(ticker)
        assert query.endswith(f"{ticker} stock") and query.count(f" {ticker} stock") <= 1, ticker
        assert query.startswith(su.COMPANIES[ticker][0]), ticker


def test_no_search_name_is_the_bare_ticker():
    """5 Oct 2026: 18 names searched as "<ticker> stock" (production's query); now all by their company name."""
    assert [t for t in su.TICKERS if su.COMPANIES[t][0] == t] == []
    for ticker in ("UPS", "SQM", "BHP", "BP", "HSBC", "IBM", "NICE", "SLB"):
        assert ticker in su.match_names(ticker), "the short form still counts as the company"


def test_the_short_tickers_are_kept_and_searched_by_their_company_name():
    for ticker in SHORT_TICKERS:
        assert ticker in su.TICKERS, ticker
        name = su.COMPANIES[ticker][0]
        assert name != ticker and len(name) > len(ticker), ticker


def test_a_search_name_that_is_a_common_word_does_not_count_as_the_company_by_itself():
    assert su.SEARCH_NAME_NOT_MATCHED == {"TGT", "PGR"}
    assert "Target" not in su.match_names("TGT") and "Target Corp" in su.match_names("TGT")
    assert "Progressive" not in su.match_names("PGR")
    assert not Matcher("TGT", su.match_names("TGT")).relevant("Analyst raises Price Target on Nike")
    for ticker in set(su.TICKERS) - su.SEARCH_NAME_NOT_MATCHED:
        assert su.match_names(ticker) == su.COMPANIES[ticker]


def test_every_company_name_counts_as_its_company():
    for ticker in su.TICKERS:
        matcher = Matcher(ticker, su.match_names(ticker))
        for name in su.match_names(ticker):
            assert matcher.named(f"{name} reports quarterly results"), (ticker, name)


# --------------------------------------------------------------------------- #
# The search
# --------------------------------------------------------------------------- #


def test_the_url_is_production_s_with_only_the_query_changed():
    for ticker in ("SO", "BP", "TGT", "MNDY"):
        ours = parse_qs(urlparse(universe_news.search_url(ticker)).query)
        production = parse_qs(urlparse(news.build_news_search_url(ticker)).query)
        assert ours.pop("q") == [su.news_query(ticker)]
        assert production.pop("q") == [f"{ticker} stock"]
        assert ours == production
        assert urlparse(universe_news.search_url(ticker)).netloc == "www.google.com"


def test_production_s_query_is_unchanged():
    assert parse_qs(urlparse(news.build_news_search_url("SO")).query)["q"] == ["SO stock"]
    assert news.BrightDataNewsProvider.fetch_items is not universe_news.UniverseNewsProvider.fetch_items
    assert issubclass(universe_news.UniverseNewsProvider, news.BrightDataNewsProvider)


def _mock_bright_data(monkeypatch) -> dict:
    captured: dict = {"bodies": []}
    real_client = httpx.Client

    def handler(request: httpx.Request) -> httpx.Response:
        captured["auth"] = request.headers["authorization"]
        captured["bodies"].append(json.loads(request.content))
        return httpx.Response(200, text=json.dumps(PARSED_NEWS))

    monkeypatch.setattr(news.httpx, "Client", lambda **_kw: real_client(transport=httpx.MockTransport(handler)))
    return captured


def test_fetch_uses_the_key_and_zone_from_bright_data_s_own_variables(monkeypatch):
    captured = _mock_bright_data(monkeypatch)
    monkeypatch.setenv(news.CLI_ENV_VAR, "tok-universe")
    monkeypatch.setenv(news.CLI_UNLOCKER_ENV_VAR, "the_cycle_zone")
    before = news.requests_sent()
    items = universe_news.fetch("SO")
    assert [h.title for h in items] == ["Apple beats on earnings", "iPhone demand cools"]
    assert captured["auth"] == "Bearer tok-universe"
    assert captured["bodies"] == [{"zone": "the_cycle_zone", "url": universe_news.search_url("SO"), "format": "raw"}]
    assert news.requests_sent() - before == 1   # the cap's count, as for production's search


def test_fetch_falls_back_to_the_login_zone(monkeypatch):
    captured = _mock_bright_data(monkeypatch)
    monkeypatch.setenv(news.CLI_ENV_VAR, "tok")
    universe_news.fetch("C")
    assert captured["bodies"][0]["zone"] == universe_news.DEFAULT_ZONE == "cli_unlocker"


def test_fetch_without_a_key_is_a_news_error_not_a_crash(monkeypatch):
    monkeypatch.setattr(news, "token_from_cli", lambda: None)
    with pytest.raises(news.NewsFetchError):
        universe_news.fetch("SO")


def test_build_context_turns_a_failed_search_into_a_news_gap(monkeypatch):
    calls = []

    def gather(ticker, headlines, **kwargs):
        calls.append((ticker, headlines, kwargs))
        return context.TickerContext(ticker=ticker)

    monkeypatch.setattr(context, "gather", gather)

    def broken(_ticker):
        raise news.NewsFetchError("Bright Data HTTP 502")

    monkeypatch.setattr(universe_news, "fetch", broken)
    universe_news.build_context("SO")
    assert calls[-1][:2] == ("SO", []) and calls[-1][2]["news_gap"].startswith(context.NEWS_GAP_PREFIX)

    found = [news.Headline(title="Southern Company raises its outlook")]
    monkeypatch.setattr(universe_news, "fetch", lambda _ticker: found)
    universe_news.build_context("SO")
    assert calls[-1] == ("SO", found, {})


def test_the_module_reads_no_credential():
    """The CI guardrail "Market context carries no credentials", run here on this file."""
    credential = re.compile(r"(get_settings|os\.environ|getenv|\bsettings\.|\.[A-Za-z_]*(secret|api_key|_token|password)\b)")
    assert not [line for line in SOURCE.read_text(encoding="utf-8").splitlines() if credential.search(line)]
