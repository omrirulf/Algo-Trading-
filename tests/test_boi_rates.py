"""The shekel rate table: the Bank of Israel's rate, the counted fallbacks, and the archive's copy.

The owner's instruction of 2 Oct 2026: the Bank of Israel's representative
rate on each day, another source only for a day the Bank did not publish,
every such day counted, and the table kept like the price table (its hash in
git, the table in the archive). No test here touches the network: every
answer is a canned CSV body handed to the parser or the fetcher.
"""

from __future__ import annotations

import ast
import json
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import httpx
import pytest

from analysis import boi_rates, price_tape
from analysis.boi_rates import BOI, CARRIED, ECB, DayRate, RateError, RateTable
from config import israel_tax
from store import scoring_prices

ROOT = Path(__file__).resolve().parent.parent
NOW = datetime(2026, 10, 2, 23, 0, tzinfo=timezone.utc)

BOI_HEADER = ("SERIES_CODE,FREQ,BASE_CURRENCY,COUNTER_CURRENCY,UNIT_MEASURE,DATA_TYPE,DATA_SOURCE,TIME_COLLECT,"
              "CONF_STATUS,PUB_WEBSITE,UNIT_MULT,COMMENTS,TIME_PERIOD,OBS_VALUE,RELEASE_STATUS")
ECB_HEADER = ("KEY,FREQ,CURRENCY,CURRENCY_DENOM,EXR_TYPE,EXR_SUFFIX,TIME_PERIOD,OBS_VALUE,OBS_STATUS,OBS_CONF,"
              "TITLE,TITLE_COMPL,UNIT,UNIT_MULT")


def boi_csv(rates: dict[date, object]) -> str:
    """A Bank of Israel SDMX answer, as the service writes it (a byte-order mark first)."""
    lines = [BOI_HEADER] + [f"RER_USD_ILS,D,USD,ILS,ILS,OF00,BOI_STATISTICS,V,F,Y,0,,{day.isoformat()},{rate},"
                            for day, rate in sorted(rates.items())]
    return "﻿" + "\r\n".join(lines) + "\r\n"


def ecb_csv(legs: dict[str, dict[date, object]]) -> str:
    """An ECB csvdata answer: one row per currency and day, a quoted title holding commas."""
    lines = [ECB_HEADER]
    for code, rates in legs.items():
        for day, rate in sorted(rates.items()):
            lines.append(f'EXR.D.{code}.EUR.SP00.A,D,{code},EUR,SP00,A,{day.isoformat()},{rate},A,F,'
                         f'{code}/Euro,"ECB reference exchange rate, {code}/Euro, 2:15 pm (C.E.T.)",{code},0')
    return "\n".join(lines) + "\n"


D = date
SEPTEMBER = {D(2026, 9, 7): 3.401, D(2026, 9, 8): 3.398, D(2026, 9, 9): 3.405, D(2026, 9, 10): 3.342,
             D(2026, 9, 11): 3.351, D(2026, 9, 14): 3.36, D(2026, 9, 15): 3.371, D(2026, 9, 16): 3.368,
             D(2026, 9, 17): 3.359, D(2026, 9, 18): 3.362, D(2026, 9, 22): 3.373, D(2026, 9, 23): 3.38}
# 2026-09-21 (Yom Kippur) is missing: the Bank did not publish.


def fixed(rates: dict[date, float]):
    """A fetcher that answers with ``rates`` and records what it was asked."""
    asked = []

    def fetch(start, end):
        asked.append((start, end))
        return dict(rates)

    fetch.asked = asked
    return fetch


def never(start, end):
    raise AssertionError(f"the fallback was asked ({start} to {end}) though no day was missing")


# --------------------------------------------------------------------------- #
# Parsing: by column name, loud on a changed format
# --------------------------------------------------------------------------- #


def test_the_bank_s_csv_is_read_by_column_name_and_kept_exactly():
    rates = boi_rates.parse_boi(boi_csv({D(2026, 9, 10): "3.342", D(2026, 9, 11): "3.3515"}))
    assert rates == {D(2026, 9, 10): 3.342, D(2026, 9, 11): 3.3515}
    assert all(type(v) is float for v in rates.values())
    # A day without a value is no rate that day, not an error.
    body = boi_csv({D(2026, 9, 10): "3.342", D(2026, 9, 11): ""})
    assert boi_rates.parse_boi(body) == {D(2026, 9, 10): 3.342}


def test_columns_are_found_in_any_case_and_order_with_date_and_value_second():
    assert boi_rates.parse_boi("date;value\n2026-09-10;3.342\n") == {D(2026, 9, 10): 3.342}
    assert boi_rates.parse_boi("obs_value,Time_Period\n3.342,2026-09-10T00:00:00\n") == {D(2026, 9, 10): 3.342}
    # TIME_PERIOD and OBS_VALUE come first when both names are there.
    body = "DATE,VALUE,TIME_PERIOD,OBS_VALUE\n2026-10-01,99,2026-09-10,3.342\n"
    assert boi_rates.parse_boi(body) == {D(2026, 9, 10): 3.342}


def test_the_ecb_rate_is_crossed_through_the_euro():
    body = ecb_csv({"ILS": {D(2026, 9, 21): "3.9762", D(2026, 9, 22): "3.98"},
                    "USD": {D(2026, 9, 21): "1.1832"},
                    "GBP": {D(2026, 9, 21): "0.8701"}})
    crossed = boi_rates.parse_ecb(body)
    # Only the day with both legs, and other currencies are skipped.
    assert crossed == {D(2026, 9, 21): 3.9762 / 1.1832}


@pytest.mark.parametrize("body", [
    "<!DOCTYPE html><html><body>The service has moved</body></html>",
    '{"error": "not found"}',
    "",
    "   \n",
    "TIME_PERIOD OBS_VALUE",                                        # one column: not CSV
    "SERIES_CODE,TIME_PERIOD,RATE\nRER_USD_ILS,2026-09-10,3.342\n",  # no value column
    "SERIES_CODE,PERIOD,OBS_VALUE\nRER_USD_ILS,2026-09-10,3.342\n",  # no date column
    "TIME_PERIOD,OBS_VALUE\n10/09/2026,3.342\n",                     # not an ISO date
    "TIME_PERIOD,OBS_VALUE\n2026-09,3.342\n",                        # a month, not a day
    "TIME_PERIOD,OBS_VALUE\n2026-02-30,3.342\n",                     # not a real day
    "TIME_PERIOD,OBS_VALUE\n2026-09-10,abc\n",                       # not a number
    "TIME_PERIOD,OBS_VALUE\n2026-09-10,-3.342\n",                    # not positive
    "TIME_PERIOD,OBS_VALUE\n2026-09-10,3,342\n",                     # a decimal comma moved the cells
    "TIME_PERIOD,OBS_VALUE\n2026-09-10,334.2\n",                     # per 100 dollars
    "TIME_PERIOD,OBS_VALUE\n2026-09-10,0.2992\n",                    # dollars per shekel
    "TIME_PERIOD,OBS_VALUE\n2026-09-10,3.342\n2026-09-10,3.35\n",    # two values for one day
    "SERIES_CODE,TIME_PERIOD,OBS_VALUE\nRER_USD_ILS\n",              # a short row
])
def test_a_changed_bank_format_raises_instead_of_giving_numbers(body):
    with pytest.raises(RateError):
        boi_rates.parse_boi(body)


@pytest.mark.parametrize("body", [
    "<html>maintenance</html>",
    "KEY,TIME_PERIOD,OBS_VALUE\nEXR.D.ILS.EUR.SP00.A,2026-09-21,3.97\n",                 # no CURRENCY column
    "CURRENCY,CURRENCY_DENOM,TIME_PERIOD,OBS_VALUE\nILS,USD,2026-09-21,3.36\n",          # not per euro
    "CURRENCY,TIME_PERIOD\nILS,2026-09-21\n",                                             # no value column
    "CURRENCY,TIME_PERIOD,OBS_VALUE\nILS,2026-09-21,39.7\nUSD,2026-09-21,1.18\n",       # a cross no rate can be
])
def test_a_changed_ecb_format_raises(body):
    with pytest.raises(RateError):
        boi_rates.parse_ecb(body)


def test_a_rate_error_is_a_value_error_so_the_funds_run_reads_it_as_no_table():
    assert issubclass(RateError, ValueError)


# --------------------------------------------------------------------------- #
# Fetching: the addresses, the retries, and 404
# --------------------------------------------------------------------------- #


def test_the_fetchers_ask_the_right_addresses_and_read_the_answers():
    asked = []

    def get(url):
        asked.append(url)
        return boi_csv(SEPTEMBER) if "boi.gov.il" in url else ecb_csv({"ILS": {D(2026, 9, 21): 4.0},
                                                                       "USD": {D(2026, 9, 21): 1.25}})

    assert boi_rates.fetch_boi(D(2026, 9, 1), D(2026, 9, 23), get=get) == SEPTEMBER
    assert boi_rates.fetch_ecb(D(2026, 9, 21), D(2026, 9, 21), get=get) == {D(2026, 9, 21): 4.0 / 1.25}
    assert asked == [
        "https://edge.boi.gov.il/FusionEdgeServer/sdmx/v2/data/dataflow/BOI.STATISTICS/EXR/1.0/RER_USD_ILS"
        "?startperiod=2026-09-01&endperiod=2026-09-23&format=csv",
        "https://data-api.ecb.europa.eu/service/data/EXR/D.ILS+USD.EUR.SP00.A"
        "?startPeriod=2026-09-21&endPeriod=2026-09-21&format=csvdata",
    ]


def test_a_404_is_no_data_from_the_ecb_but_an_error_from_the_bank():
    assert boi_rates.fetch_ecb(D(2026, 12, 25), D(2026, 12, 25), get=lambda url: None) == {}
    with pytest.raises(RateError, match="404"):
        boi_rates.fetch_boi(D(2026, 9, 1), D(2026, 9, 23), get=lambda url: None)


def _client(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler))


def test_a_busy_service_is_tried_three_times_with_a_pause():
    calls, pauses = [], []

    def handler(request):
        calls.append(request)
        if len(calls) == 1:
            raise httpx.ConnectError("down", request=request)
        return httpx.Response(503) if len(calls) == 2 else httpx.Response(200, text="TIME_PERIOD,OBS_VALUE\n")

    body = boi_rates.http_get("https://example.test/rates", client=_client(handler), pause=pauses.append)
    assert body == "TIME_PERIOD,OBS_VALUE\n" and len(calls) == 3
    assert pauses == [boi_rates.PAUSE_SECONDS, 2 * boi_rates.PAUSE_SECONDS]


def test_a_service_that_never_answers_raises_after_three_tries():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(502)

    with pytest.raises(RateError, match="HTTP 502"):
        boi_rates.http_get("https://example.test/rates", client=_client(handler), pause=lambda s: None)
    assert len(calls) == boi_rates.ATTEMPTS == 3


def test_a_refusal_is_final_and_404_means_no_data():
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(404 if "missing" in str(request.url) else 400)

    assert boi_rates.http_get("https://example.test/missing", client=_client(handler), pause=lambda s: None) is None
    with pytest.raises(RateError, match="HTTP 400"):
        boi_rates.http_get("https://example.test/bad", client=_client(handler), pause=lambda s: None)
    assert len(calls) == 2


def test_the_default_client_has_a_timeout_and_is_closed(monkeypatch):
    real, settings, clients = httpx.Client, [], []

    def client(**kwargs):
        settings.append(kwargs)
        clients.append(real(transport=httpx.MockTransport(lambda r: httpx.Response(200, text="ok")), **kwargs))
        return clients[-1]

    monkeypatch.setattr(httpx, "Client", client)
    assert boi_rates.http_get("https://example.test/rates") == "ok"
    (made,), (used,) = settings, clients
    assert made["timeout"] == boi_rates.TIMEOUT_SECONDS and made["follow_redirects"] is True
    assert used.is_closed


# --------------------------------------------------------------------------- #
# The table: the Bank's rate, else the ECB's, else carried -- every fallback counted
# --------------------------------------------------------------------------- #


def test_every_weekday_from_the_bank_needs_no_fallback():
    boi = fixed(SEPTEMBER)
    table = boi_rates.build(D(2026, 9, 10), D(2026, 9, 18), boi=boi, ecb=never)
    assert table.days == (D(2026, 9, 10), D(2026, 9, 11), D(2026, 9, 14), D(2026, 9, 15), D(2026, 9, 16),
                          D(2026, 9, 17), D(2026, 9, 18))
    assert table.counts() == {"boi": 7, "ecb": 0, "carried": 0} and table.fallback_days() == []
    assert table.as_dict() == {d: r for d, r in SEPTEMBER.items() if D(2026, 9, 10) <= d <= D(2026, 9, 18)}
    assert (table.first, table.last, len(table)) == (D(2026, 9, 10), D(2026, 9, 18), 7)
    # The Bank is read from before the start, so a first day can be carried.
    assert boi.asked == [(D(2026, 9, 10) - timedelta(days=boi_rates.LOOKBACK_DAYS), D(2026, 9, 18))]


def test_a_bank_holiday_is_filled_from_the_ecb_and_counted():
    ecb = fixed({D(2026, 9, 21): 3.9762 / 1.1832, D(2026, 9, 22): 9.0})
    table = boi_rates.build(D(2026, 9, 17), D(2026, 9, 23), boi=fixed(SEPTEMBER), ecb=ecb)
    assert table.source(D(2026, 9, 21)) == ECB and table.rate(D(2026, 9, 21)) == 3.9762 / 1.1832
    # The ECB only for the day the Bank did not publish; the Bank's rate wins on every other.
    assert table.source(D(2026, 9, 22)) == BOI and table.rate(D(2026, 9, 22)) == 3.373
    assert table.counts() == {"boi": 4, "ecb": 1, "carried": 0}
    assert table.fallback_days() == [(D(2026, 9, 21), "ecb")]
    assert ecb.asked == [(D(2026, 9, 21), D(2026, 9, 21))]


def test_a_day_missing_everywhere_carries_the_bank_s_latest_earlier_rate_and_is_counted():
    boi = {d: r for d, r in SEPTEMBER.items() if d not in (D(2026, 9, 10), D(2026, 9, 14), D(2026, 9, 15))}
    ecb = fixed({D(2026, 9, 14): 3.5})
    table = boi_rates.build(D(2026, 9, 10), D(2026, 9, 16), boi=fixed(boi), ecb=ecb)
    # The first day, from the Bank's rate before the start (read through the look-back).
    assert table.source(D(2026, 9, 10)) == CARRIED and table.rate(D(2026, 9, 10)) == SEPTEMBER[D(2026, 9, 9)]
    assert table.source(D(2026, 9, 14)) == ECB and table.rate(D(2026, 9, 14)) == 3.5
    # The Bank's latest earlier rate (Friday's), never the ECB day before it.
    assert table.source(D(2026, 9, 15)) == CARRIED and table.rate(D(2026, 9, 15)) == SEPTEMBER[D(2026, 9, 11)]
    assert table.counts() == {"boi": 2, "ecb": 1, "carried": 2}
    assert table.fallback_days() == [(D(2026, 9, 10), "carried"), (D(2026, 9, 14), "ecb"),
                                     (D(2026, 9, 15), "carried")]
    assert ecb.asked == [(D(2026, 9, 10), D(2026, 9, 15))]


def test_a_day_with_no_bank_rate_before_it_raises():
    later = {d: r for d, r in SEPTEMBER.items() if d >= D(2026, 9, 11)}
    with pytest.raises(RateError, match="no earlier Bank of Israel rate"):
        boi_rates.build(D(2026, 9, 10), D(2026, 9, 16), boi=fixed(later), ecb=fixed({}))
    # The ECB having the day is enough: nothing needs carrying.
    table = boi_rates.build(D(2026, 9, 10), D(2026, 9, 16), boi=fixed(later), ecb=fixed({D(2026, 9, 10): 3.3}))
    assert table.counts() == {"boi": 4, "ecb": 1, "carried": 0}


def test_a_range_with_no_weekday_or_backwards_raises():
    with pytest.raises(RateError):
        boi_rates.build(D(2026, 9, 12), D(2026, 9, 13), boi=fixed(SEPTEMBER), ecb=never)
    with pytest.raises(RateError):
        boi_rates.build(D(2026, 9, 18), D(2026, 9, 10), boi=fixed(SEPTEMBER), ecb=never)


def test_a_fetch_that_fails_fails_the_build():
    def down(start, end):
        raise RateError("could not fetch it (ConnectError)")

    with pytest.raises(RateError):
        boi_rates.build(D(2026, 9, 10), D(2026, 9, 18), boi=down, ecb=never)
    with pytest.raises(RateError):
        boi_rates.build(D(2026, 9, 17), D(2026, 9, 23), boi=fixed(SEPTEMBER), ecb=down)


def test_a_day_outside_the_table_or_a_weekend_has_no_rate():
    table = boi_rates.build(D(2026, 9, 10), D(2026, 9, 18), boi=fixed(SEPTEMBER), ecb=never)
    for day in (D(2026, 9, 9), D(2026, 9, 12), D(2026, 9, 21)):
        with pytest.raises(KeyError):
            table.rate(day)
        with pytest.raises(KeyError):
            table.source(day)
    # A timestamp on a table day reads that day.
    assert table.rate(datetime(2026, 9, 14, 20, 0, tzinfo=timezone.utc)) == SEPTEMBER[D(2026, 9, 14)]


@pytest.mark.parametrize("entries", [
    (),
    (DayRate(D(2026, 9, 10), 3.3, BOI), DayRate(D(2026, 9, 14), 3.3, BOI)),     # Friday is missing
    (DayRate(D(2026, 9, 12), 3.3, BOI),),                                         # a Saturday
    (DayRate(D(2026, 9, 10), 3.3, "yahoo"),),                                     # no such source
    (DayRate(D(2026, 9, 10), 330.0, BOI),),                                       # cannot be the rate
    (DayRate(D(2026, 9, 11), 3.3, BOI), DayRate(D(2026, 9, 10), 3.3, BOI)),     # out of order
])
def test_a_table_is_every_weekday_once_in_order_with_a_plausible_rate(entries):
    with pytest.raises(RateError):
        RateTable(entries)


# --------------------------------------------------------------------------- #
# The tape: the price table's shape, its hash, and the archive's copy
# --------------------------------------------------------------------------- #


def _table() -> RateTable:
    boi = {d: r for d, r in SEPTEMBER.items() if d != D(2026, 9, 15)}
    return boi_rates.build(D(2026, 9, 10), D(2026, 9, 23), boi=fixed(boi),
                           ecb=fixed({D(2026, 9, 21): 3.9762 / 1.1832}))


def test_the_tape_has_the_price_table_s_shape_and_hashes_its_rows():
    table = _table()
    tape = boi_rates.tape(table, NOW, table.last)
    assert list(tape) == ["kind", "v", "consumer", "source", "generated_at", "final_through", "prices_sha256",
                          "coverage", "rows"]
    assert (tape["kind"], tape["v"], tape["consumer"], tape["source"]) == (
        "scoring-prices", price_tape.TAPE_VERSION, "fx-rates", "bank-of-israel")
    assert tape["generated_at"] == NOW.isoformat() and tape["final_through"] == "2026-09-23"
    rows = tape["rows"]
    assert all(list(row) == list(price_tape.ROW_KEYS) for row in rows)
    assert rows == sorted(rows, key=lambda r: (r["instance"], r["ticker"], r["date"]))
    assert [r["instance"] for r in rows] == ["boi"] * 8 + ["carried"] + ["ecb"]
    assert {(r["instance"], r["ticker"]) for r in rows} == {
        ("boi", "USDILS"), ("carried", "USDILS.CARRIED"), ("ecb", "USDILS.ECB")}
    assert all(r["kind"] == "close" and r["open"] is r["high"] is r["low"] is r["dividends"] is None for r in rows)
    assert {r["date"]: r["close"] for r in rows} == {d.isoformat(): v for d, v in table.as_dict().items()}
    assert tape["prices_sha256"] == price_tape.digest(rows)
    assert tape["coverage"] == {
        "boi": {"kind": "close", "tickers": {"USDILS": {"first": "2026-09-10", "last": "2026-09-23", "bars": 8,
                                                        "fetched_at": NOW.isoformat()}}},
        "carried": {"kind": "close", "tickers": {"USDILS.CARRIED": {"first": "2026-09-15", "last": "2026-09-15",
                                                                    "bars": 1, "fetched_at": NOW.isoformat()}}},
        "ecb": {"kind": "close", "tickers": {"USDILS.ECB": {"first": "2026-09-21", "last": "2026-09-21",
                                                            "bars": 1, "fetched_at": NOW.isoformat()}}},
    }
    # Only the sources that gave a day are named.
    plain = boi_rates.tape(boi_rates.build(D(2026, 9, 10), D(2026, 9, 11), boi=fixed(SEPTEMBER), ecb=never),
                           NOW, D(2026, 9, 11))
    assert list(plain["coverage"]) == ["boi"]


def test_the_tape_round_trips_through_load_tape():
    table = _table()
    text = price_tape.dumps(boi_rates.tape(table, NOW, table.last))
    back = boi_rates.load_tape(text)
    assert back == table and back.as_dict() == table.as_dict()
    assert back.counts() == table.counts() == {"boi": 8, "ecb": 1, "carried": 1}
    assert back.fallback_days() == [(D(2026, 9, 15), "carried"), (D(2026, 9, 21), "ecb")]
    assert all(back.rate(d) == table.rate(d) for d in table.days)


def _rehash(tape: dict) -> str:
    tape["prices_sha256"] = price_tape.digest(tape["rows"])
    return json.dumps(tape)


@pytest.mark.parametrize("spoil", [
    lambda t: json.dumps({**t, "rows": [{**t["rows"][0], "close": t["rows"][0]["close"] + 0.001},
                                        *t["rows"][1:]]}),                         # a rate changed, hash kept
    lambda t: json.dumps({**t, "prices_sha256": "0" * 64}),                       # the hash changed
    lambda t: _rehash({**t, "consumer": "funds"}),                                 # not a rate table
    lambda t: _rehash({**t, "v": 2}),                                              # another version
    lambda t: _rehash({**t, "rows": t["rows"][:2] + t["rows"][3:]}),               # a day dropped: a gap
    lambda t: _rehash({**t, "rows": []}),                                          # no rows
    lambda t: _rehash({**t, "rows": [{**t["rows"][0], "ticker": "USDILS.ECB"}, *t["rows"][1:]]}),
    lambda t: _rehash({**t, "rows": [{**t["rows"][0], "open": 3.3}, *t["rows"][1:]]}),
    lambda t: _rehash({**t, "rows": [{**t["rows"][0], "close": "3.3"}, *t["rows"][1:]]}),
    lambda t: _rehash({**t, "rows": [{**t["rows"][0], "date": "2026-09-10T00:00"}, *t["rows"][1:]]}),
    lambda t: _rehash({**t, "rows": [{k: v for k, v in t["rows"][0].items() if k != "dividends"},
                                     *t["rows"][1:]]}),
    lambda t: "not json",
])
def test_load_tape_refuses_a_table_that_does_not_check(spoil):
    table = _table()
    with pytest.raises(RateError):
        boi_rates.load_tape(spoil(boi_rates.tape(table, NOW, table.last)))


def test_the_archive_takes_the_tape_and_can_rebuild_it():
    table = _table()
    tape = scoring_prices.load(price_tape.dumps(boi_rates.tape(table, NOW, table.last)))
    assert "fx-rates" in scoring_prices.CONSUMERS
    stored = scoring_prices.price_rows(tape, "18000000002")
    run = scoring_prices.run_row(tape, "18000000002")
    # Each day once (a carried day repeats a rate, but under its own ticker).
    assert len(stored) == len(tape["rows"]) == len(table)
    assert {r["source"] for r in stored} == {"bank-of-israel"} and {r["first_consumer"] for r in stored} == {"fx-rates"}
    assert run["consumer"] == "fx-rates" and run["rows"] == len(table)
    rebuilt = []
    for instance, part in run["coverage"].items():
        for ticker, span in part["tickers"].items():
            bars = sorted((r for r in stored if r["kind"] == part["kind"] and r["ticker"] == ticker
                           and span["first"] <= r["bar_date"] <= span["last"]), key=lambda r: r["bar_date"])
            assert len(bars) == span["bars"]
            rebuilt += [{"instance": instance, "kind": r["kind"], "ticker": ticker, "date": r["bar_date"],
                         "open": r["open"], "high": r["high"], "low": r["low"], "close": r["close"],
                         "dividends": r["dividends"]} for r in bars]
    rebuilt.sort(key=lambda r: (r["instance"], r["ticker"], r["date"]))
    assert price_tape.digest(rebuilt) == run["prices_sha256"] == tape["prices_sha256"]
    # And a spoiled one is refused there too.
    spoiled = boi_rates.tape(table, NOW, table.last)
    spoiled["rows"][2]["close"] += 0.01
    with pytest.raises(scoring_prices.TapeError):
        scoring_prices.load(json.dumps(spoiled))


# --------------------------------------------------------------------------- #
# The CLI: one line to commit, the table last, exit 1 on any failure
# --------------------------------------------------------------------------- #


@pytest.fixture
def services(monkeypatch):
    """Both services, answered with canned CSV at the one call every fetch makes."""
    asked = []

    def get(url):
        asked.append(url)
        if "boi.gov.il" in url:
            return boi_csv(SEPTEMBER)
        return ecb_csv({"ILS": {D(2026, 9, 21): "3.9762"}, "USD": {D(2026, 9, 21): "1.1832"}})

    monkeypatch.setattr(boi_rates, "http_get", get)
    monkeypatch.setattr(boi_rates, "_now", lambda: NOW)
    return asked


def test_the_cli_prints_one_line_and_the_table_last(services, capsys):
    assert boi_rates.main(["--start", "2026-09-10", "--end", "2026-09-23", "--with-table"]) == 0
    first, last = capsys.readouterr().out.splitlines()
    line, tape = json.loads(first), json.loads(last)
    assert list(line) == ["kind", "source", "fallback_source", "first", "last", "days", "counts",
                          "fallback_days", "rates_sha256", "generated_at"]
    assert line == {
        "kind": "fx-rates", "source": israel_tax.FX_SOURCE, "fallback_source": israel_tax.FX_FALLBACK_SOURCE,
        "first": "2026-09-10", "last": "2026-09-23", "days": 10, "counts": {"boi": 9, "ecb": 1, "carried": 0},
        "fallback_days": [["2026-09-21", "ecb"]], "rates_sha256": tape["prices_sha256"],
        "generated_at": NOW.isoformat(),
    }
    assert boi_rates.load_tape(last).rate(D(2026, 9, 21)) == 3.9762 / 1.1832
    assert scoring_prices.load(last)["consumer"] == "fx-rates"
    assert services[0].endswith("startperiod=2026-08-27&endperiod=2026-09-23&format=csv")
    assert "startPeriod=2026-09-21&endPeriod=2026-09-21" in services[1]


def test_the_cli_without_the_table_prints_one_line(services, capsys):
    assert boi_rates.main(["--start", "2026-09-10", "--end", "2026-09-18"]) == 0
    (line,) = capsys.readouterr().out.splitlines()
    assert json.loads(line)["counts"] == {"boi": 7, "ecb": 0, "carried": 0}
    assert len(services) == 1          # nothing missing: the ECB was not asked


def test_the_cli_exits_1_with_a_clear_message_on_any_failure(monkeypatch, capsys):
    def down(url):
        raise RateError(f"could not fetch {url} (ConnectError: down)")

    monkeypatch.setattr(boi_rates, "http_get", down)
    assert boi_rates.main(["--start", "2026-09-10", "--end", "2026-09-18", "--with-table"]) == 1
    out = capsys.readouterr()
    assert out.out == "" and "no rate table" in out.err and "ConnectError" in out.err

    monkeypatch.setattr(boi_rates, "http_get", lambda url: "<html>moved</html>")
    assert boi_rates.main(["--start", "2026-09-10", "--end", "2026-09-18"]) == 1
    out = capsys.readouterr()
    assert out.out == "" and "not CSV" in out.err

    assert boi_rates.main(["--start", "2026-09-18", "--end", "2026-09-10"]) == 1
    with pytest.raises(SystemExit) as stop:
        boi_rates.main(["--start", "18/09/2026", "--end", "2026-09-30"])
    assert stop.value.code == 2


# --------------------------------------------------------------------------- #
# The guardrails the module lives under
# --------------------------------------------------------------------------- #


def test_the_module_writes_nothing_and_reaches_no_archive():
    source = (ROOT / "analysis" / "boi_rates.py").read_text(encoding="utf-8")
    assert ".write_text(" not in source and ".write_bytes(" not in source and "open(" not in source
    imported = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            imported |= {alias.name for alias in node.names}
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module or "")
    assert not any(name == "store" or name.startswith("store.") for name in imported)
    assert not any(name.startswith(("os", "app", "orchestrator")) for name in imported)
