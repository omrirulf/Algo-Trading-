"""The one place on the context side where a credential is read.

A CI guardrail holds every module under ``orchestrator/`` to reading no
credentials, with a short allowlist. The reason is specific: those modules
assemble the text sent to a language model, and the signal journal they feed
is committed to the repository every cycle. A key that reached a snapshot
would reach a prompt and then a public git history.

Four free sources need a key, so rather than four modules each reading the
environment, all four fetches live in one. These hold that one file to the
three rules it claims: a key goes into a request and nowhere else; nothing
here formats or persists; and no key is a state rather than a failure.
"""

from __future__ import annotations

import inspect
import json
import logging

import pytest

from orchestrator import crops, earnings, energy, fred, sources

SOURCES = ("eia", "usda", "fred", "finnhub")


class FakeResponse:
    def __init__(self, payload, fail=False):
        self._payload = payload
        self._fail = fail

    def raise_for_status(self):
        if self._fail:
            raise RuntimeError("HTTP 401: invalid api_key=SECRETKEY123")

    def json(self):
        return self._payload


class FakeClient:
    """Records every call, so a test can inspect exactly what was sent."""

    def __init__(self, payload=None, fail=False):
        self.calls = []
        self._payload = payload if payload is not None else {}
        self._fail = fail
        self.closed = False

    def get(self, url, params=None):
        self.calls.append((url, dict(params or {})))
        return FakeResponse(self._payload, self._fail)

    def close(self):
        self.closed = True


@pytest.fixture
def no_keys(monkeypatch):
    for names in sources.KEY_ENV_VARS.values():
        for name in names:
            monkeypatch.delenv(name, raising=False)


# --- no key is a state, not a failure ----------------------------------------


def test_with_no_keys_nothing_is_fetched(no_keys):
    assert sources.fetch_fred_releases() == {}
    assert sources.fetch_energy_payloads("USO") == {}
    assert sources.fetch_crop_rows("CORN", 2026) == []
    assert sources.fetch_earnings_rows("MSFT") == []


def test_with_no_keys_configured_reports_all_four_as_absent(no_keys):
    assert sources.configured() == {s: False for s in SOURCES}


def test_configured_reports_booleans_and_never_the_keys(monkeypatch, no_keys):
    monkeypatch.setenv("FRED_API_KEY", "SECRETKEY123")
    report = sources.configured()
    assert report["fred"] is True and report["eia"] is False
    assert "SECRETKEY123" not in json.dumps(report)


@pytest.mark.parametrize("source", SOURCES)
def test_the_key_is_found_under_any_of_its_names(monkeypatch, no_keys, source):
    """A key saved under a name nothing reads is a silent no-op, and silence
    is the one failure mode this system cannot see."""
    for name in sources.KEY_ENV_VARS[source]:
        for other in sources.KEY_ENV_VARS[source]:
            monkeypatch.delenv(other, raising=False)
        monkeypatch.setenv(name, "  abc123  ")
        assert sources.api_key(source) == "abc123"


@pytest.mark.parametrize("source", SOURCES)
def test_an_empty_key_is_the_same_as_no_key(monkeypatch, no_keys, source):
    for name in sources.KEY_ENV_VARS[source]:
        monkeypatch.setenv(name, "   ")
    assert sources.api_key(source) is None


def test_an_unknown_source_has_no_key(no_keys):
    assert sources.api_key("bloomberg") is None


# --- the key goes into the request and nowhere else ---------------------------


def test_a_failure_never_records_the_body_that_echoes_the_key(monkeypatch, caplog):
    """These APIs put the query string, key included, into error messages.
    Only the exception type is ever logged."""
    monkeypatch.setenv("FRED_API_KEY", "SECRETKEY123")
    caplog.set_level(logging.DEBUG)
    assert sources.fetch_fred_releases(client=FakeClient(fail=True)) == {}
    assert "SECRETKEY123" not in caplog.text
    assert "RuntimeError" in caplog.text


def test_no_fetch_returns_the_key_in_what_it_hands_back(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "SECRETKEY123")
    rows = sources.fetch_earnings_rows("MSFT", client=FakeClient(
        [{"period": "2026-06-30", "actual": 1.0, "estimate": 0.9}]))
    assert "SECRETKEY123" not in json.dumps(rows)


def test_the_key_does_travel_in_the_request_because_that_is_the_point(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "SECRETKEY123")
    client = FakeClient([])
    sources.fetch_earnings_rows("MSFT", client=client)
    assert client.calls[0][1]["token"] == "SECRETKEY123"


def code_of(module) -> str:
    """A module's source with its own docstring removed.

    The docstrings here describe the rules; the checks below are about the
    code keeping them, and a rule quoted in prose must not satisfy its own
    test.
    """
    body = inspect.getsource(module)
    return body.split('"""', 2)[-1] if body.lstrip().startswith('"""') else body


def test_this_module_formats_nothing_and_writes_nothing():
    """It fetches. Rendering belongs to the parsing modules and persistence to
    the heartbeat, and keeping those apart is what makes one file auditable."""
    body = code_of(sources)
    for forbidden in ("as_lines", "as_prompt", ".write_text(", "open(", "journal"):
        assert forbidden not in body, forbidden


# --- a source is only asked for where it applies ------------------------------


@pytest.mark.parametrize("ticker", ["GLD", "CORN", "TLT", "RSP", "MSFT", "EWZ"])
def test_energy_is_never_fetched_for_a_ticker_with_no_energy_exposure(
    monkeypatch, ticker
):
    """Not merely unused -- never asked for, so an EIA outage cannot gap gold."""
    monkeypatch.setenv("EIA_API_KEY", "abc123")
    client = FakeClient()
    assert sources.fetch_energy_payloads(ticker, client=client) == {}
    assert client.calls == []


@pytest.mark.parametrize("ticker", ["GLD", "USO", "XLE", "MSFT"])
def test_crops_are_never_fetched_for_a_ticker_with_no_crop(monkeypatch, ticker):
    monkeypatch.setenv("USDA_NASS_KEY", "abc123")
    client = FakeClient()
    assert sources.fetch_crop_rows(ticker, 2026, client=client) == []
    assert client.calls == []


def test_an_energy_ticker_is_asked_only_about_its_own_series(monkeypatch):
    monkeypatch.setenv("EIA_API_KEY", "abc123")
    client = FakeClient({"response": {"data": []}})
    sources.fetch_energy_payloads("UNG", client=client)
    assert len(client.calls) == 1
    assert client.calls[0][1]["facets[series][]"] == energy.SERIES["natural_gas"][1]


# --- one failure never costs the rest -----------------------------------------


def test_one_fred_series_that_fails_does_not_cost_the_others(monkeypatch):
    monkeypatch.setenv("FRED_API_KEY", "abc123")

    class Picky(FakeClient):
        def get(self, url, params=None):
            self.calls.append((url, dict(params or {})))
            return FakeResponse({"observations": []},
                                fail=params["series_id"] == "UNRATE")

    out = sources.fetch_fred_releases(client=Picky())
    assert "unemployment" not in out
    assert len(out) == len(fred.SERIES) - 1


def test_one_eia_series_that_fails_does_not_cost_the_others(monkeypatch):
    monkeypatch.setenv("EIA_API_KEY", "abc123")

    class Picky(FakeClient):
        def get(self, url, params=None):
            self.calls.append((url, dict(params or {})))
            return FakeResponse({"response": {"data": []}},
                                fail=params["facets[series][]"] == "WGTSTUS1")

    assert set(sources.fetch_energy_payloads("USO", client=Picky())) == {
        "crude", "distillate"}


@pytest.mark.parametrize("fetch,args", [
    (sources.fetch_crop_rows, ("CORN", 2026)),
    (sources.fetch_earnings_rows, ("MSFT",)),
])
def test_a_failed_fetch_is_empty_rather_than_a_raised_error(monkeypatch, fetch, args):
    """An optional source must not be able to fail a cycle."""
    monkeypatch.setenv("USDA_NASS_KEY", "abc123")
    monkeypatch.setenv("FINNHUB_API_KEY", "abc123")
    assert fetch(*args, client=FakeClient(fail=True)) in ({}, [])


@pytest.mark.parametrize("junk", [None, 17, "nope", {"data": "nope"}, []])
def test_a_response_of_the_wrong_shape_is_empty_rather_than_a_crash(monkeypatch, junk):
    monkeypatch.setenv("USDA_NASS_KEY", "abc123")
    monkeypatch.setenv("FINNHUB_API_KEY", "abc123")
    assert sources.fetch_crop_rows("CORN", 2026, client=FakeClient(junk)) == []
    assert sources.fetch_earnings_rows("MSFT", client=FakeClient(junk)) == []


# --- an injected client is the caller's to close ------------------------------


def test_an_injected_client_is_not_closed(monkeypatch):
    monkeypatch.setenv("FINNHUB_API_KEY", "abc123")
    client = FakeClient([])
    sources.fetch_earnings_rows("MSFT", client=client)
    assert client.closed is False


# --- the parsing modules stayed pure ------------------------------------------


@pytest.mark.parametrize("module", [crops, earnings, energy, fred])
def test_no_parsing_module_reads_the_environment_or_the_network(module):
    """The guardrail in CI checks this by grep. This checks the same thing
    from the inside, so the reason survives a refactor of the grep."""
    body = code_of(module)
    for forbidden in ("os.environ", "getenv", "httpx", "api_key", "requests."):
        assert forbidden not in body, (module.__name__, forbidden)
