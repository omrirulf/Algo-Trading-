"""Bright Data news provider: request shape, response parsing, failure modes."""

from __future__ import annotations

import json
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from orchestrator import heartbeat as hb
from orchestrator import news
from config.settings import Settings

#: Captured before conftest's autouse fixture replaces it, so the real path
#: logic can still be tested.
REAL_CLI_CREDENTIAL_PATHS = news.cli_credential_paths

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
    assert captured["body"]["country"] == news.BRD_COUNTRY == "us"
    assert set(captured["body"]) == {"zone", "url", "format", "country"}
    assert len(lines) == 2 and lines[0].startswith("Apple beats on earnings")


@pytest.mark.parametrize("status", [401, 403, 429, 500])
def test_provider_raises_on_http_error(status):
    handler = lambda request: httpx.Response(status, text="denied")  # noqa: E731
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with pytest.raises(news.NewsFetchError) as exc:
            provider.fetch("AAPL")
    assert str(status) in str(exc.value)


def test_provider_raises_on_transport_error(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        raise httpx.ConnectError("boom")

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with pytest.raises(news.NewsFetchError):
            provider.fetch("AAPL")
    # Google: one retry, then the error is real. Then the feed (5 Nov 2026):
    # once directly, and once more with its retry through Bright Data.
    assert len(calls) == 5


def test_a_timed_out_read_is_tried_once_more_and_the_second_answer_counts(monkeypatch):
    slept = []
    monkeypatch.setattr(news.time, "sleep", lambda s: slept.append(s))
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            raise httpx.ReadTimeout("The read operation timed out")
        return httpx.Response(200, text=json.dumps(PARSED_NEWS))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        lines = provider.fetch("IGV")
    assert len(calls) == 2 and len(lines) == 2
    assert slept == [news.RETRY_PAUSE_SECONDS]


def test_a_block_page_with_status_200_is_tried_once_more(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(200, text="<html><body>Just a moment...</body></html>")
        return httpx.Response(200, text=json.dumps(PARSED_NEWS))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        lines = provider.fetch("TM")
    assert len(calls) == 2 and len(lines) == 2


def test_a_second_block_page_is_the_real_answer(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    calls = []
    handler = lambda request: (calls.append(1), httpx.Response(200, text="<html>blocked</html>"))[1]  # noqa: E731
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with pytest.raises(news.NewsFetchError) as exc:
            provider.fetch("TM")
    # Google twice; then the feed's two routes (5 Nov 2026), refused the same way.
    assert len(calls) == 4 and "JSON" in str(exc.value) and "Bing's feed also failed" in str(exc.value)


def test_an_http_error_is_never_retried(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: pytest.fail("slept on an HTTP error"))
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(429, text="slow down")

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with pytest.raises(news.NewsFetchError):
            provider.fetch("AAPL")
    assert len(calls) == 3                       # Google once, then the feed's two routes once each


def test_heartbeat_fetch_news_uses_settings(monkeypatch):
    seen = {}

    class FakeProvider:
        def __init__(self, token, zone, client=None, unlocker_zone=""):
            seen["token"], seen["zone"] = token, zone
            seen["unlocker_zone"] = unlocker_zone

        def fetch_answer(self, ticker):
            seen["ticker"] = ticker
            return news.NewsAnswer([news.Headline(title="headline")])

    monkeypatch.setattr(hb, "BrightDataNewsProvider", FakeProvider)
    monkeypatch.setattr(
        hb, "get_settings",
        lambda: Settings(brightdata_api_token="t", brightdata_serp_zone="z", _env_file=None),
    )
    # The cycle takes structured records so the journal can carry links, and
    # since 5 Nov 2026 the answer that says where they came from; the line
    # the model sees is unchanged.
    answer = hb.fetch_news("MSFT")
    assert [h.as_line() for h in answer.headlines] == ["headline"] and answer.fallback == ""
    assert seen == {
        "token": "t", "zone": "z", "ticker": "MSFT", "unlocker_zone": "cli_unlocker",
    }


# --------------------------------------------------------------------------- #
# Credential resolution: settings -> CLI env var -> `brightdata login` file
# --------------------------------------------------------------------------- #


def write_credentials(tmp_path, payload) -> None:
    path = tmp_path / "credentials.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def test_settings_token_wins_over_everything(monkeypatch, tmp_path):
    monkeypatch.setenv(news.CLI_ENV_VAR, "from-env")
    path = write_credentials(tmp_path, {"api_key": "from-cli"})
    monkeypatch.setattr(news, "cli_credential_paths", lambda: [path])

    assert news.resolve_token("from-settings") == "from-settings"


def test_cli_env_var_is_accepted_so_one_secret_serves_both(monkeypatch, tmp_path):
    """A shell already set up for the CLI shouldn't need a second variable."""
    monkeypatch.setenv(news.CLI_ENV_VAR, "from-env")
    path = write_credentials(tmp_path, {"api_key": "from-cli"})
    monkeypatch.setattr(news, "cli_credential_paths", lambda: [path])

    assert news.resolve_token("") == "from-env"


def test_the_cli_login_file_is_the_last_resort(monkeypatch, tmp_path):
    path = write_credentials(tmp_path, {"api_key": "from-cli"})
    monkeypatch.setattr(news, "cli_credential_paths", lambda: [path])

    assert news.resolve_token("") == "from-cli"


@pytest.mark.parametrize(
    "payload",
    [
        {"api_key": "k"},
        {"apiKey": "k"},
        {"api_token": "k"},
        {"apiToken": "k"},
        {"token": "k"},
        {"key": "k"},
        {"default": {"api_key": "k"}},
        {"accounts": {"default": {"token": "k"}}},
    ],
)
def test_credential_field_name_is_not_guessed_at_once(monkeypatch, tmp_path, payload):
    """The file format isn't documented, so several shapes are tolerated."""
    monkeypatch.setattr(news, "cli_credential_paths", lambda: [write_credentials(tmp_path, payload)])
    assert news.token_from_cli() == "k"


@pytest.mark.parametrize(
    "content",
    ["not json at all", "[]", "null", '{"unrelated": "value"}', '{"api_key": ""}', '{"api_key": 42}'],
)
def test_an_unreadable_or_unrecognised_file_is_not_an_error(monkeypatch, tmp_path, content):
    """Best-effort means a surprise in that file degrades, never raises."""
    path = tmp_path / "credentials.json"
    path.write_text(content, encoding="utf-8")
    monkeypatch.setattr(news, "cli_credential_paths", lambda: [path])

    assert news.token_from_cli() is None


def test_a_missing_file_is_not_an_error(monkeypatch, tmp_path):
    monkeypatch.setattr(news, "cli_credential_paths", lambda: [tmp_path / "nope.json"])
    assert news.token_from_cli() is None


def test_the_first_readable_path_wins(monkeypatch, tmp_path):
    second = write_credentials(tmp_path, {"api_key": "second"})
    monkeypatch.setattr(news, "cli_credential_paths", lambda: [tmp_path / "missing.json", second])
    assert news.token_from_cli() == "second"


def test_credential_paths_are_platform_specific(monkeypatch):
    # The autouse fixture neutralises path discovery for every other test, so
    # this one uses the reference captured at import time, before it was.
    monkeypatch.setenv("XDG_CONFIG_HOME", "/xdg")
    monkeypatch.setattr(news.sys, "platform", "linux")
    monkeypatch.setattr(news.os, "name", "posix")
    assert REAL_CLI_CREDENTIAL_PATHS() == [news.Path("/xdg/brightdata-cli/credentials.json")]

    monkeypatch.setattr(news.sys, "platform", "darwin")
    (mac,) = REAL_CLI_CREDENTIAL_PATHS()
    assert mac.parts[-3:] == ("Application Support", "brightdata-cli", "credentials.json")


def test_the_token_value_is_never_logged(monkeypatch, tmp_path, caplog):
    """A secret in the logs outlives the run that wrote it."""
    import logging

    caplog.set_level(logging.INFO)
    monkeypatch.setattr(
        news, "cli_credential_paths", lambda: [write_credentials(tmp_path, {"api_key": "s3cr3t"})]
    )

    assert news.token_from_cli() == "s3cr3t"
    assert "s3cr3t" not in caplog.text
    assert "credentials.json" in caplog.text  # the path is useful; the value is not


def test_no_credentials_anywhere_names_both_ways_to_fix_it():
    with pytest.raises(news.NewsFetchError) as exc:
        news.BrightDataNewsProvider(api_token="", zone="serp_api")

    assert "BRIGHTDATA_API_TOKEN" in str(exc.value)
    assert "brightdata login" in str(exc.value)


def test_a_cli_token_is_actually_used_for_the_request(monkeypatch, tmp_path):
    """Resolution is pointless if the resolved token doesn't reach the header."""
    monkeypatch.setattr(
        news, "cli_credential_paths", lambda: [write_credentials(tmp_path, {"api_key": "cli-tok"})]
    )
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["auth"] = request.headers.get("authorization")
        return httpx.Response(200, json=PARSED_NEWS)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        news.BrightDataNewsProvider("", "serp_api", client=client).fetch("AAPL")

    assert seen["auth"] == "Bearer cli-tok"


def test_news_module_has_no_broker_or_engine_imports():
    src = (news.__file__ and open(news.__file__).read()) or ""
    assert "alpaca" not in src.lower()
    assert "from app" not in src and "import app" not in src


# --- zone resolution: SERP zone, else the CLI's unlocker zone ---------------


def test_the_serp_zone_wins_when_both_are_set(monkeypatch):
    monkeypatch.setenv(news.CLI_UNLOCKER_ENV_VAR, "cli_unlocker")
    assert news.resolve_zone("serp_api") == "serp_api"


def test_the_unlocker_zone_is_used_when_no_serp_zone_is_set(monkeypatch):
    """`brightdata login` creates cli_unlocker and no SERP zone.

    Bright Data's own CLI resolves BRIGHTDATA_SERP_ZONE then
    BRIGHTDATA_UNLOCKER_ZONE for its `search` command, so an unlocker zone
    serves brd_json=1 search URLs. Mirroring that is what lets the login
    alone be enough.
    """
    monkeypatch.setenv(news.CLI_UNLOCKER_ENV_VAR, "cli_unlocker")
    assert news.resolve_zone("") == "cli_unlocker"


def test_no_zone_anywhere_resolves_to_empty(monkeypatch):
    assert news.resolve_zone("") == ""


def test_whitespace_is_not_a_zone(monkeypatch):
    monkeypatch.setenv(news.CLI_UNLOCKER_ENV_VAR, "   ")
    assert news.resolve_zone("   ") == ""


def test_the_unlocker_zone_reaches_the_request_body(monkeypatch):
    """The fallback has to arrive at Bright Data, not just resolve."""
    monkeypatch.setenv(news.CLI_UNLOCKER_ENV_VAR, "cli_unlocker")
    captured: dict = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["body"] = json.loads(request.content)
        return httpx.Response(200, json={"news": []})

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok-123", "", client=client)
        provider.fetch("AAPL")

    assert captured["body"]["zone"] == "cli_unlocker"


def test_missing_zone_error_names_both_variables(monkeypatch):
    with pytest.raises(news.NewsFetchError) as excinfo:
        news.BrightDataNewsProvider("tok-123", "")
    message = str(excinfo.value)
    assert "BRIGHTDATA_SERP_ZONE" in message
    assert news.CLI_UNLOCKER_ENV_VAR in message


def test_the_html_error_no_longer_claims_only_serp_zones_work():
    """The old wording sent people to the dashboard unnecessarily."""
    with pytest.raises(news.NewsFetchError) as excinfo:
        news.parse_news_results("<html><body>blocked</body></html>")
    assert "Web Unlocker" in str(excinfo.value)


def test_a_pasted_token_with_stray_whitespace_is_stripped(monkeypatch):
    """A trailing newline from a secrets form must not reach the Bearer header."""
    monkeypatch.delenv(news.CLI_ENV_VAR, raising=False)
    monkeypatch.setattr(news, "token_from_cli", lambda: None)
    assert news.resolve_token("  abc123\n") == "abc123"
    assert news.resolve_token("\n") is None


# --------------------------------------------------------------------------- #
# Structured headlines: the link the prompt line drops
# --------------------------------------------------------------------------- #


def test_items_carry_the_link():
    items = news.parse_news_items(PARSED_NEWS)
    assert items[0].url == "https://x/1"
    assert items[0].title == "Apple beats on earnings"
    assert items[0].source == "Reuters"


def test_the_prompt_line_is_unchanged_by_the_link():
    """Every replay and sanity baseline was measured against this exact string."""
    items = news.parse_news_items(PARSED_NEWS)
    assert [i.as_line() for i in items] == news.parse_news_results(PARSED_NEWS)
    assert items[0].as_line() == "Apple beats on earnings — Revenue up 8% (Reuters, 2 hours ago)"


def test_a_result_without_a_link_is_still_a_headline():
    items = news.parse_news_items({"news": [{"title": "No link here", "source": "Wire"}]})
    assert items[0].url == ""
    assert items[0].as_line() == "No link here (Wire)"


def test_items_are_json_serialisable_for_the_journal():
    import json as _json

    payload = _json.loads(_json.dumps([i.as_dict() for i in news.parse_news_items(PARSED_NEWS)]))
    assert payload[0]["url"] == "https://x/1"
    assert set(payload[0]) == {"title", "snippet", "source", "when", "url"}


def test_items_are_deduplicated_by_title_like_the_lines():
    items = news.parse_news_items(PARSED_NEWS)
    assert len(items) == len(news.parse_news_results(PARSED_NEWS))
    assert len({i.title.lower() for i in items}) == len(items)


# --------------------------------------------------------------------------- #
# A stored link has to survive leaving google.com
# --------------------------------------------------------------------------- #


def test_a_google_redirect_stub_gets_an_origin():
    """The first live cycle stored 100 of 176 links as bare `/goto?url=...`,
    which resolves against whatever page renders them -- so, nowhere."""
    assert news.absolute_url("/goto?url=CAESkQEB") == "https://www.google.com/goto?url=CAESkQEB"


@pytest.mark.parametrize("url", [
    "https://www.reuters.com/a",
    "http://example.com/b",
])
def test_an_absolute_link_is_left_alone(url):
    assert news.absolute_url(url) == url


def test_a_protocol_relative_link_gets_a_scheme_not_a_host():
    assert news.absolute_url("//cdn.example.com/a") == "https://cdn.example.com/a"


def test_a_bare_relative_link_gets_a_separator():
    assert news.absolute_url("articles/x") == "https://www.google.com/articles/x"


@pytest.mark.parametrize("url", ["", "   ", None])
def test_a_missing_link_stays_missing(url):
    assert news.absolute_url(url) == ""


def test_parsed_items_carry_links_that_can_be_opened():
    payload = {"news": [
        {"title": "Relative", "link": "/goto?url=BLOB"},
        {"title": "Absolute", "link": "https://www.reuters.com/x"},
    ]}
    items = news.parse_news_items(payload)
    assert items[0].url == "https://www.google.com/goto?url=BLOB"
    assert items[1].url == "https://www.reuters.com/x"
    assert all(h.url.startswith("https://") for h in items)


def test_the_prompt_line_never_shows_the_link():
    """Absolutising must not leak a URL into what the model reads."""
    items = news.parse_news_items({"news": [{"title": "T", "link": "/goto?url=BLOB"}]})
    assert "goto" not in items[0].as_line()
    assert items[0].as_line() == "T"


# --------------------------------------------------------------------------- #
# The 18 Sep 2026 message that read like a parser bug (issue #69)
# --------------------------------------------------------------------------- #


def test_an_empty_two_hundred_says_so_instead_of_blaming_the_parser():
    """What TM actually hit, and what its journal line should have said.

    json.loads("") raises "Expecting value: line 1 column 1 (char 0)", which
    reads like malformed JSON. The body was not malformed; there was no body.
    """
    with pytest.raises(news.NewsFetchError) as caught:
        news._unwrap("")
    assert "empty body" in str(caught.value)
    assert "Expecting value" not in str(caught.value)


def test_whitespace_only_counts_as_empty():
    with pytest.raises(news.NewsFetchError, match="empty body"):
        news._unwrap("   \n  ")


def test_genuinely_broken_json_still_shows_what_arrived():
    """A parse failure must hand the reader the evidence, not just the verdict."""
    with pytest.raises(news.NewsFetchError) as caught:
        news._unwrap("{'not': 'json'}")
    message = str(caught.value)
    assert "15 bytes" in message
    assert "not" in message


def test_html_keeps_its_own_clearer_message():
    """The one failure mode that already explained itself must not regress."""
    with pytest.raises(news.NewsFetchError, match="returned HTML"):
        news._unwrap("<!doctype html><html>blocked</html>")


def test_every_request_sent_is_counted_per_thread_for_a_caller_that_pays_per_request(monkeypatch):
    """The shadow universe charges each Bright Data request to its daily cap (the owner, 3 Oct 2026). The
    count includes the retry after a refused 200, and one thread's requests are not another's."""
    import threading

    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    answers = iter([httpx.Response(200, text=json.dumps(PARSED_NEWS)),
                    httpx.Response(200, text=""), httpx.Response(200, text=json.dumps(PARSED_NEWS))])
    with httpx.Client(transport=httpx.MockTransport(lambda request: next(answers))) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        before = news.requests_sent()
        provider.fetch("AAPL")
        assert news.requests_sent() - before == 1
        provider.fetch("KO")                           # an empty 200, then the retry
        assert news.requests_sent() - before == 3
    seen = []
    worker = threading.Thread(target=lambda: seen.append(news.requests_sent()))
    worker.start()
    worker.join()
    assert seen == [0]


# --------------------------------------------------------------------------- #
# The owner's decision of 16 Oct 2026: a longer pause before the second ask
# of a refused 200, and Bright Data's own headers in the record
# --------------------------------------------------------------------------- #


def test_the_second_ask_after_a_refused_two_hundred_waits_the_longer_pause(monkeypatch):
    """15 Oct 2026: 60 empty 200s, and 53 of the second asks two seconds later were empty again."""
    slept = []
    monkeypatch.setattr(news.time, "sleep", lambda s: slept.append(s))
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            return httpx.Response(200, text="")
        return httpx.Response(200, text=json.dumps(PARSED_NEWS))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        lines = provider.fetch("XLB")
    assert len(calls) == 2 and len(lines) == 2
    assert slept == [news.EMPTY_RETRY_PAUSE_SECONDS]
    assert news.EMPTY_RETRY_PAUSE_SECONDS == 10.0 > news.RETRY_PAUSE_SECONDS


def test_a_transport_error_keeps_the_short_pause(monkeypatch):
    slept = []
    monkeypatch.setattr(news.time, "sleep", lambda s: slept.append(s))
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        if len(calls) == 1:
            raise httpx.ReadTimeout("The read operation timed out")
        return httpx.Response(200, text=json.dumps(PARSED_NEWS))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        news.BrightDataNewsProvider("tok", "zone", client=client).fetch("XLB")
    assert slept == [news.RETRY_PAUSE_SECONDS]


def test_a_second_empty_two_hundred_carries_bright_datas_own_headers(monkeypatch, caplog):
    """What other users of the request API see: a 200, no body, and x-brd-status-code 502."""
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    headers = {"x-brd-status-code": "502", "x-brd-err-msg": "upstream timed out", "content-type": "text/html"}
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(1)
        return httpx.Response(200, text="", headers=headers)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with caplog.at_level("WARNING", logger=news.log.name):
            with pytest.raises(news.NewsFetchError) as caught:
                provider.fetch("KSA")
    message = str(caught.value)
    assert len(calls) == 4                       # Google twice, then the feed's two routes
    assert message.startswith("Bright Data returned an empty body with its 200; nothing to parse")
    assert "(Bright Data said: x-brd-status-code 502; x-brd-err-msg upstream timed out)" in message
    assert "content-type" not in message                  # only Bright Data's own headers
    assert "tok" not in message and "Bearer" not in message
    warning = [r.getMessage() for r in caplog.records if "parser refused" in r.getMessage()]
    assert len(warning) == 1
    assert "[x-brd-status-code 502; x-brd-err-msg upstream timed out]" in warning[0]
    assert "retrying once after 10 s" in warning[0]


def test_a_second_empty_two_hundred_without_headers_reads_as_before(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    handler = lambda request: httpx.Response(200, text="   ")  # noqa: E731
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        provider = news.BrightDataNewsProvider("tok", "zone", client=client)
        with pytest.raises(news.NewsFetchError) as caught:
            provider.fetch("KSA")
    assert str(caught.value) == ("Bright Data returned an empty body with its 200; nothing to parse "
                                 "(Bing's feed also failed: direct: Bing returned an empty body; "
                                 "Bright Data: Bing returned an empty body)")


def test_brd_headers_reads_only_the_vendors_headers():
    response = httpx.Response(200, text="", headers={"x-brd-status-code": "429", "date": "today", "x-brd-error": "auto-throttled"})
    assert news.brd_headers(response) == "x-brd-status-code 429; x-brd-error auto-throttled"
    assert news.brd_headers(httpx.Response(200, text="")) == ""
    assert news.brd_headers(object()) == ""


# --------------------------------------------------------------------------- #
# The owner's decision of 17 Oct 2026: the request exits from the US
# --------------------------------------------------------------------------- #


def test_every_ask_exits_from_the_us_the_second_one_too(monkeypatch):
    """16 Oct 2026: every empty 200 was the Unlocker refusing Google's redirect for a non-US exit, and
    the same request from a US exit was empty 2 times of 20 against 5 of 20. Both asks carry it."""
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    bodies = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(json.loads(request.content))
        return httpx.Response(200, text="" if len(bodies) == 1 else json.dumps(PARSED_NEWS))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        lines = news.BrightDataNewsProvider("tok", "zone", client=client).fetch("XLB")
    assert len(bodies) == 2 and len(lines) == 2
    assert [b["country"] for b in bodies] == ["us", "us"]
    assert bodies[0] == bodies[1]                          # the second ask is the same request
    assert news.BRD_COUNTRY == "us"


def test_the_historical_replay_exits_from_the_us_as_the_live_path_does():
    """Same request, same exit: a past day's news is fetched the way today's is."""
    from datetime import date

    bodies = []

    def handler(request: httpx.Request) -> httpx.Response:
        bodies.append(json.loads(request.content))
        return httpx.Response(200, text=json.dumps(PARSED_NEWS))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        news.BrightDataNewsProvider("tok", "zone", client=client).fetch_on("XLB", date(2026, 10, 1))
    assert bodies[0]["country"] == "us"
    assert bodies[0]["url"] == news.build_news_search_url("XLB", on=date(2026, 10, 1))


# --------------------------------------------------------------------------- #
# Bing's feed: the guarded fallback (the owner's decision of 4 Nov 2026)
# --------------------------------------------------------------------------- #

from datetime import date, datetime, timezone  # noqa: E402

from orchestrator import universe_news  # noqa: E402

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
REFUSED = {"x-brd-status-code": "502", "x-brd-error": "redirect location was rejected"}


def feed_transport(record, direct=None):
    """Google's answer an empty 200 with Bright Data's headers; the feed answers, directly (unless ``direct`` says otherwise) and through Bright Data."""
    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content) if request.content else None
        record.append((request.method, request.url.host, request.headers.get("Authorization"), body))
        if request.url.host == "api.brightdata.com":
            if "google.com" in body["url"]:
                return httpx.Response(200, text="", headers=REFUSED)
            return httpx.Response(200, text=RSS, headers={"x-brd-status-code": "200"})
        if callable(direct):
            return direct(request)
        return httpx.Response(200, text=RSS)
    return handler


def provider_with(handler, cls=news.BrightDataNewsProvider):
    return cls("tok", "zone", client=httpx.Client(transport=httpx.MockTransport(handler)))


def test_the_bing_url_carries_the_same_qualifier_as_the_google_search_and_the_24h_filter():
    assert news.build_bing_news_url("TEVA") == (
        "https://www.bing.com/news/search?q=TEVA+stock&format=rss&setlang=en-US&cc=US&qft=interval%3D%227%22")
    assert "q=GLD+ETF" in news.build_bing_news_url("GLD") and "ETF" in news.build_news_search_url("GLD")
    assert "qft" not in news.build_bing_news_url("TEVA", last_24h=False)


def test_the_feed_is_read_into_the_headline_shape_newest_first_without_duplicates():
    stories = news.parse_bing_rss(RSS, now=NOW)
    assert [s.headline.title for s in stories] == ["Teva raises its outlook after a strong quarter",
                                                   "Generic drug prices fall again"]
    first = stories[0].headline
    assert first.source == "Reuters" and first.when == "2h ago" and first.url.startswith("https://www.bing.com/news/apiclick")
    assert first.as_line() == ("Teva raises its outlook after a strong quarter — The drugmaker lifted its full-year "
                               "guidance. (Reuters, 2h ago)")
    assert stories[1].headline.snippet == "A second story." and stories[1].age_hours == 24.0
    assert len(news.parse_bing_rss(RSS, limit=1, now=NOW)) == 1


@pytest.mark.parametrize("text", ["", "   ", "<html><body>blocked</body></html>", "{\"not\": \"xml\"}", "<rss><channel><item><title"])
def test_what_is_not_a_feed_is_refused(text):
    with pytest.raises(news.NewsFetchError):
        news.parse_bing_rss(text, now=NOW)


def test_the_guard_keeps_the_ticker_or_the_companys_name_and_drops_the_rest():
    def kept(ticker, *titles):
        return [h.title for h in news.relevant_headlines(ticker, [news.Headline(t) for t in titles])]

    assert kept("TEVA", "Teva CEO explains why the drugmaker is growing", "Generic drug prices fall again",
                "$TEVA jumps after earnings") == ["Teva CEO explains why the drugmaker is growing", "$TEVA jumps after earnings"]
    # A fund is known by its ticker alone: its display name describes it.
    assert kept("DBA", "Malvern Country Music Gathering returns Nov. 6-7", "Bellevue residents approve $3 million pool bond",
                "DBA: A Well-Rounded Commodity ETF", "Agricultural ETFs rally") == ["DBA: A Well-Rounded Commodity ETF"]
    assert kept("DBC", "Vanguard S&P 500 ETF", "Top ETF Losers", "Notable ETF Outflow Detected - DBC") == ["Notable ETF Outflow Detected - DBC"]
    # The ticker as written: not a word that happens to spell it, and not the start of PG&E.
    assert kept("TIP", "A tip for investors", "Tips ETF (TIP) sees inflows") == ["Tips ETF (TIP) sees inflows"]
    assert kept("PG", "PG&E files its wildfire plan", "Procter & Gamble beats on sales", "Gamble's new campaign") == [
        "Procter & Gamble beats on sales", "Gamble's new campaign"]
    # Generic words of a name count only inside the whole name.
    assert kept("RY", "Royal Bank of Canada stock stays in focus", "Royal Caribbean sails higher", "Canada's banks report") == [
        "Royal Bank of Canada stock stays in focus"]
    assert kept("LLY", "Lilly's new drug clears a hurdle", "Eli who?") == ["Lilly's new drug clears a hurdle"]
    assert kept("GOOGL", "Google wins a cloud deal", "Alphabet shares climb") == ["Google wins a cloud deal", "Alphabet shares climb"]
    # The snippet counts too.
    assert kept("XOM") == []
    assert [h.title for h in news.relevant_headlines("XOM", [news.Headline("Oil majors report", snippet="Exxon beat")])] == ["Oil majors report"]
    assert news.name_words("RY") == ("RY", "Royal Bank of Canada") and news.name_words("DBA") == ("DBA",)


def test_a_second_refused_answer_from_google_takes_the_feed_directly_kept_to_the_name(monkeypatch, caplog):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    news._SENT.count = 0
    record = []
    provider = provider_with(feed_transport(record))
    with caplog.at_level("WARNING", logger=news.log.name):
        answer = provider.fetch_answer("TEVA")
    assert [h.title for h in answer.headlines] == ["Teva raises its outlook after a strong quarter"]   # the generic one is dropped
    assert answer.fallback.startswith("news from Bing's feed (direct) after Google: Bright Data returned an empty body")
    assert "redirect location was rejected" in answer.fallback and answer.fallback.endswith("1 of 2 headline(s) name TEVA")
    assert [(m, h) for m, h, _a, _b in record] == [("POST", "api.brightdata.com")] * 2 + [("GET", "www.bing.com")]
    assert record[2][2] is None and "tok" not in answer.fallback           # no token to Bing, none in the note
    assert news.requests_sent() == 2                                       # the direct ask is not a Bright Data request
    assert provider.fetch_items("TEVA")[0].title.startswith("Teva raises")   # the list-only path, the same way
    assert any("TEVA: news from Bing's feed (direct)" in r.getMessage() for r in caplog.records)


def test_the_direct_feed_failing_falls_to_bright_data_with_the_same_zone(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    record = []
    provider = provider_with(feed_transport(record, direct=lambda request: httpx.Response(429, text="later")))
    answer = provider.fetch_answer("TEVA")
    assert answer.fallback.startswith("news from Bing's feed (Bright Data) after Google")
    posts = [b for m, h, _a, b in record if m == "POST" and "bing.com" in b["url"]]
    assert posts == [{"zone": "zone", "url": news.build_bing_news_url("TEVA"), "format": "raw", "country": news.BRD_COUNTRY}]
    assert record[2][0] == "GET" and record[3][0] == "POST"


def test_a_direct_transport_error_also_falls_to_bright_data(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    record = []

    def boom(request):
        raise httpx.ConnectError("no route", request=request)

    answer = provider_with(feed_transport(record, direct=boom)).fetch_answer("TEVA")
    assert "(Bright Data)" in answer.fallback and len(answer.headlines) == 1


def test_both_feed_routes_failing_is_the_old_error_carrying_every_reason(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)

    def handler(request):
        if request.url.host == "api.brightdata.com":
            return httpx.Response(200, text="", headers=REFUSED)          # Google and the feed through Bright Data alike
        return httpx.Response(503, text="down")
    with pytest.raises(news.NewsFetchError) as caught:
        provider_with(handler).fetch_answer("TEVA")
    message = str(caught.value)
    assert message.startswith("Bright Data returned an empty body with its 200")
    assert "Bing's feed also failed: direct: HTTP 503; Bright Data: Bing returned an empty body (Bright Data said: x-brd-status-code 502" in message


def test_a_feed_with_no_headline_naming_the_name_is_unavailable_as_before(monkeypatch):
    """The owner's rule: if nothing is left, the name gets "no news", as today -- a gap, not a quiet day."""
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    record = []
    with pytest.raises(news.NewsFetchError) as caught:
        provider_with(feed_transport(record)).fetch_answer("DBA")      # the Teva feed names no DBA
    assert str(caught.value).endswith("(Bing's feed, direct: 2 headline(s), none naming DBA)")
    assert "redirect location was rejected" in str(caught.value)
    assert [m for m, *_ in record] == ["POST", "POST", "GET"]            # Bright Data's route is not asked for more of the same


def test_an_http_error_from_google_also_takes_the_fallback(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: pytest.fail("slept on an HTTP error"))
    record = []

    def handler(request):
        body = json.loads(request.content) if request.content else None
        record.append(request.method)
        if request.url.host == "api.brightdata.com" and "google.com" in body["url"]:
            return httpx.Response(500, text="upstream")
        return httpx.Response(200, text=RSS)
    answer = provider_with(handler).fetch_answer("TEVA")
    assert "after Google: Bright Data HTTP 500" in answer.fallback and record == ["POST", "GET"]


def test_the_historical_path_and_the_universe_query_have_no_fallback(monkeypatch):
    monkeypatch.setattr(news.time, "sleep", lambda s: None)
    record = []
    with pytest.raises(news.NewsFetchError):
        provider_with(feed_transport(record)).fetch_on("TEVA", date(2026, 9, 1))
    with pytest.raises(news.NewsFetchError):
        provider_with(feed_transport(record), cls=universe_news.UniverseNewsProvider).fetch_items("BKR")
    assert all(host == "api.brightdata.com" for _m, host, _a, _b in record)


def test_build_context_keeps_the_fallback_note_for_the_journal_and_takes_plain_lines_too(monkeypatch):
    seen = []
    monkeypatch.setattr(hb.context, "gather", lambda ticker, headlines, **kw: seen.append((ticker, list(headlines), kw)) or "ctx")
    note = "news from Bing's feed (direct) after Google: empty body; 1 of 2 headline(s) name TEVA"
    monkeypatch.setattr(hb, "fetch_news", lambda t: news.NewsAnswer([news.Headline("Teva raises")], note))
    assert hb.build_context("TEVA") == "ctx"
    monkeypatch.setattr(hb, "fetch_news", lambda t: ["plain line"])
    hb.build_context("MSFT")
    assert seen[0][0] == "TEVA" and seen[0][1][0].title == "Teva raises" and seen[0][2] == {"news_note": note}
    assert seen[1] == ("MSFT", ["plain line"], {"news_note": ""})
