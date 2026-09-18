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
    assert len(calls) == 2                       # one retry, then the error is real


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
    assert len(calls) == 2 and "JSON" in str(exc.value)


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
    assert len(calls) == 1


def test_heartbeat_fetch_news_uses_settings(monkeypatch):
    seen = {}

    class FakeProvider:
        def __init__(self, token, zone, client=None, unlocker_zone=""):
            seen["token"], seen["zone"] = token, zone
            seen["unlocker_zone"] = unlocker_zone

        def fetch_items(self, ticker):
            seen["ticker"] = ticker
            return [news.Headline(title="headline")]

    monkeypatch.setattr(hb, "BrightDataNewsProvider", FakeProvider)
    monkeypatch.setattr(
        hb, "get_settings",
        lambda: Settings(brightdata_api_token="t", brightdata_serp_zone="z", _env_file=None),
    )
    # The cycle now takes structured records so the journal can carry links;
    # the line the model sees is unchanged.
    assert [h.as_line() for h in hb.fetch_news("MSFT")] == ["headline"]
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
