"""Where the official forecaster says the price is going.

These pin the applicability (only the energy funds see it), the month
arithmetic (three and six months out, wrapping the year; next year's
average), the direction phrase, and the honest blanks: no "this month", no
month ahead, no key -- no block.
"""

from __future__ import annotations

from datetime import date

import pytest

from orchestrator import outlook

TODAY = date(2026, 9, 17)


def payload(values: dict[str, float]) -> dict:
    """EIA's payload shape: ``response.data`` rows with ``period`` and ``value``."""
    return {"response": {"data": [
        {"period": period, "value": value, "seriesId": "WTIPUUS"}
        for period, value in sorted(values.items(), reverse=True)
    ]}}


def wti(now=64.0, three=61.0, six=58.0, next_year=None):
    values = {"2026-08": 66.0, "2026-09": now, "2026-12": three, "2027-03": six}
    if next_year is not None:
        for month in range(1, 13):
            values[f"2027-{month:02d}"] = next_year
        values["2027-03"] = six
    return payload(values)


# --- who gets this section ----------------------------------------------------


@pytest.mark.parametrize("ticker,expected", [
    ("USO", ("wti", "brent")),
    ("UNG", ("henry_hub",)),
    ("XLE", ("wti", "henry_hub")),
    ("DBC", ("wti", "henry_hub")),
])
def test_an_energy_fund_is_asked_about_the_prices_it_tracks(ticker, expected):
    assert outlook.series_for(ticker) == expected


@pytest.mark.parametrize("ticker", ["GLD", "CORN", "TLT", "RSP", "EWZ", "MSFT", "NVDA", "XOM"])
def test_everything_else_is_asked_about_nothing(ticker):
    assert outlook.series_for(ticker) == ()
    assert outlook.build_snapshot(ticker, {"wti": wti()}, today=TODAY) is None


def test_the_coverage_matches_the_inventory_block():
    """The same funds see both EIA blocks: an oil fund is a bet on the price."""
    from orchestrator import energy

    assert set(outlook.COVERAGE) == set(energy.COVERAGE)


# --- the arithmetic -------------------------------------------------------------


def test_this_month_and_three_and_six_months_out_are_read():
    f = outlook.build_forecast("wti", wti(), today=TODAY)
    assert f.now == outlook.Point(0, "Sep 2026", 64.0)
    assert f.ahead == [outlook.Point(3, "Dec 2026", 61.0), outlook.Point(6, "Mar 2027", 58.0)]
    assert f.next_year is None  # only one 2027 month arrived


def test_the_horizons_wrap_the_year():
    assert outlook._add_months((2026, 9), 3) == (2026, 12)
    assert outlook._add_months((2026, 9), 6) == (2027, 3)
    assert outlook._add_months((2026, 12), 1) == (2027, 1)


def test_next_years_average_needs_at_least_half_the_year():
    f = outlook.build_forecast("wti", wti(next_year=55.0), today=TODAY)
    assert f.next_year is not None
    year, mean = f.next_year
    assert year == 2027 and abs(mean - (55.0 * 11 + 58.0) / 12) < 1e-9

    few = payload({"2026-09": 64.0, "2026-12": 61.0, "2027-01": 55.0, "2027-02": 55.0})
    assert outlook.build_forecast("wti", few, today=TODAY).next_year is None


def test_a_missing_horizon_is_left_out_not_invented():
    f = outlook.build_forecast("wti", payload({"2026-09": 64.0, "2026-12": 61.0}), today=TODAY)
    assert [p.months_ahead for p in f.ahead] == [3]
    assert f.six_month_change_pct is None and f.direction() == "no six-month figure"


# --- the honest blanks ------------------------------------------------------------


def test_no_figure_for_this_month_is_no_forecast():
    """A forecast that cannot say "from here" is not one."""
    stale = payload({"2026-07": 66.0, "2026-08": 65.0, "2026-12": 61.0})
    assert outlook.build_forecast("wti", stale, today=TODAY) is None


def test_nothing_ahead_of_this_month_is_no_forecast():
    history_only = payload({"2026-07": 66.0, "2026-08": 65.0, "2026-09": 64.0})
    assert outlook.build_forecast("wti", history_only, today=TODAY) is None


@pytest.mark.parametrize("bad", [None, {}, {"response": None}, {"response": {"data": "x"}},
                                 {"response": {"data": [{"period": "2026", "value": 1}]}},
                                 {"response": {"data": [{"period": "2026-09", "value": "n/a"}]}}])
def test_a_payload_of_the_wrong_shape_is_nothing_rather_than_a_crash(bad):
    assert outlook.build_forecast("wti", bad, today=TODAY) is None


def test_a_label_nobody_defined_is_nothing():
    assert outlook.build_forecast("uranium", wti(), today=TODAY) is None


def test_a_ticker_whose_series_all_failed_gets_no_block():
    assert outlook.build_snapshot("USO", {"wti": None, "brent": {}}, today=TODAY) is None
    assert outlook.build_snapshot("USO", None, today=TODAY) is None


# --- what the model reads ------------------------------------------------------------


def test_the_direction_phrase_is_from_the_six_month_point():
    falling = outlook.build_forecast("wti", wti(64.0, 61.0, 58.0), today=TODAY)
    assert falling.direction() == "seen to fall about 9% over six months"
    rising = outlook.build_forecast("wti", wti(64.0, 66.0, 70.0), today=TODAY)
    assert rising.direction() == "seen to rise about 9% over six months"
    flat = outlook.build_forecast("wti", wti(64.0, 64.5, 64.9), today=TODAY)
    assert flat.direction() == "seen roughly flat over six months"


def test_the_line_reads_in_dollars_with_the_months_named():
    snap = outlook.build_snapshot("USO", {"wti": wti(next_year=55.0)}, today=TODAY)
    lines = snap.as_lines()
    assert lines[0].startswith("EIA Short-Term Energy Outlook")
    assert lines[1] == (
        "  WTI crude ($/barrel): $64.00 this month (Sep 2026) -> $61.00 in 3 months (Dec 2026) "
        "-> $58.00 in 6 months (Mar 2027); 2027 average $55.25 -- seen to fall about 9% over six months"
    )
    assert "One agency's view" in lines[-1]


def test_gas_is_read_in_its_own_unit():
    gas = payload({"2026-09": 3.1, "2026-12": 3.9, "2027-03": 3.4})
    snap = outlook.build_snapshot("UNG", {"henry_hub": gas}, today=TODAY)
    assert "Henry Hub natural gas ($/million BTU): $3.10 this month" in snap.as_lines()[1]


def test_only_the_series_that_arrived_are_shown():
    snap = outlook.build_snapshot("USO", {"wti": wti(), "brent": None}, today=TODAY)
    assert [f.label for f in snap.forecasts] == ["wti"]


def test_the_journal_form_is_plain_data():
    d = outlook.build_snapshot("USO", {"wti": wti()}, today=TODAY).as_dict()
    assert d["ticker"] == "USO"
    assert d["forecasts"][0]["now"] == {"months_ahead": 0, "period": "Sep 2026", "value": 64.0}


# --- the fetch is keyed, and asks for the right thing ---------------------------------


def test_no_key_means_nothing_is_fetched(monkeypatch):
    from orchestrator import sources

    for name in sources.KEY_ENV_VARS["eia"]:
        monkeypatch.delenv(name, raising=False)

    class Boom:
        def get(self, *a, **k):
            raise AssertionError("must not be called without a key")

    assert sources.fetch_outlook_payloads("USO", client=Boom()) == {}


def test_a_ticker_with_no_coverage_costs_no_request_even_with_a_key(monkeypatch):
    from orchestrator import sources

    monkeypatch.setenv("EIA_API_KEY", "k")

    class Boom:
        def get(self, *a, **k):
            raise AssertionError("must not be called for GLD")

    assert sources.fetch_outlook_payloads("GLD", client=Boom()) == {}


def test_the_request_names_the_steo_route_and_series(monkeypatch):
    from orchestrator import sources

    monkeypatch.setenv("EIA_API_KEY", "secret-key")
    calls = []

    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {"response": {"data": []}}

    class Client:
        def get(self, url, params=None):
            calls.append((url, params))
            return Response()

    out = sources.fetch_outlook_payloads("XLE", client=Client())
    assert set(out) == {"wti", "henry_hub"}
    assert [u for u, _ in calls] == [f"{sources.EIA_URL}/steo/data/"] * 2
    assert [p["facets[seriesId][]"] for _, p in calls] == ["WTIPUUS", "NGHHUUS"]
    assert all(p["frequency"] == "monthly" and p["api_key"] == "secret-key" for _, p in calls)
    assert all(p["length"] == str(outlook.ROW_LIMIT) for _, p in calls)


def test_a_failed_request_is_logged_by_type_only_and_never_with_the_key(monkeypatch, caplog):
    from orchestrator import sources

    monkeypatch.setenv("EIA_API_KEY", "secret-key")

    class Client:
        def get(self, url, params=None):
            raise RuntimeError("400 https://api.eia.gov/v2/steo/data/?api_key=secret-key")

    assert sources.fetch_outlook_payloads("UNG", client=Client()) == {}
    assert "secret-key" not in caplog.text
    assert "RuntimeError" in caplog.text
