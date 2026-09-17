"""The contract map names one market exactly, and the query asks for it exactly.

A substring is what broke this. ``upper(names) like '%GOLD%'`` matched three
markets, the CFTC returned all three ordered by date, and the parser read
consecutive rows as consecutive weeks -- so the "change on the week" was the
gap between two different gold contracts and the "52-week percentile" ranked
twenty real weeks of three mixed series. Nine of the nineteen mappings were
doing this. Nothing failed; the numbers just stopped meaning anything, which
is worse than a gap, because a gap is visible.

These tests pin the two halves of the fix -- full names in the map, an exact
query in the fetch -- so neither can quietly revert.
"""

from __future__ import annotations

import re
from urllib.parse import unquote

import httpx
import pytest

from orchestrator import positioning as pos


def test_every_mapping_names_a_full_market_not_a_fragment():
    """A real name carries its exchange: "GOLD - COMMODITY EXCHANGE INC.".

    "GOLD" on its own is the shape that matched three markets.
    """
    for ticker, (_, name) in sorted(pos.CONTRACTS.items()):
        assert " - " in name, f"{ticker}: {name!r} is a fragment, not a market name"
        assert name == name.strip(), f"{ticker}: {name!r} has stray outer spacing"


def test_no_mapping_is_a_prefix_of_another():
    """The interleaving test, stated directly on the map.

    Under exact matching this cannot happen at all; it is pinned so that a
    return to substring matching fails here rather than in a prompt.
    """
    names = sorted({name for _, name in pos.CONTRACTS.values()})
    for name in names:
        others = [n for n in names if n != name and name.upper() in n.upper()]
        assert not others, f"{name!r} is contained in {others!r}"


def test_two_tickers_may_share_one_contract():
    """IEF and TIP both read the 10-year note. That is deliberate, not a clash."""
    assert pos.CONTRACTS["IEF"][1] == pos.CONTRACTS["TIP"][1]


@pytest.mark.parametrize("ticker", sorted(pos.CONTRACTS))
def test_the_query_is_an_exact_match_for_every_mapping(ticker):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        return httpx.Response(200, json=[])

    pos.fetch_rows(ticker, client=httpx.Client(transport=httpx.MockTransport(handler)))
    asked = unquote(seen["url"])
    dataset, name = pos.CONTRACTS[ticker]
    assert dataset in asked
    assert f"upper(market_and_exchange_names) = '{name.upper()}'" in asked
    assert "like" not in asked
    assert "%" not in asked, "a wildcard is a substring match wearing an equals sign"


def test_a_name_with_an_apostrophe_cannot_end_the_query_early(monkeypatch):
    """No name carries one today. One that did would rewrite the query."""
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["url"] = str(request.url)
        return httpx.Response(200, json=[])

    monkeypatch.setitem(pos.CONTRACTS, "ZZZ", (pos.FINANCIAL, "O'HARE IDX - SOME EXCHANGE"))
    pos.fetch_rows("ZZZ", client=httpx.Client(transport=httpx.MockTransport(handler)))
    asked = unquote(seen["url"])
    assert "'O''HARE IDX - SOME EXCHANGE'" in asked
    # One opening quote, one closing quote, and the doubled pair between them.
    assert asked.count("'") == 4


def test_the_renamed_contracts_are_the_ones_that_report_today():
    """The five that read a series last updated in February 2022.

    Pinned by name because the old names still exist in the dataset: a
    revert would look like working code and read four-year-old positioning.
    """
    assert pos.CONTRACTS["TLT"][1] == "ULTRA UST BOND - CHICAGO BOARD OF TRADE"
    assert pos.CONTRACTS["IEF"][1] == "UST 10Y NOTE - CHICAGO BOARD OF TRADE"
    assert pos.CONTRACTS["SHY"][1] == "UST 2Y NOTE - CHICAGO BOARD OF TRADE"
    assert pos.CONTRACTS["UUP"][1] == "USD INDEX - ICE FUTURES U.S."
    for ticker, (_, name) in pos.CONTRACTS.items():
        assert "U.S. TREASURY" not in name, f"{ticker} is back on a pre-2022 name"


def test_the_map_keeps_the_spacing_the_dataset_uses():
    """"MSCI EAFE  - ICE FUTURES U.S." carries two spaces. Tidying it breaks it."""
    assert pos.CONTRACTS["VGK"][1] == "MSCI EAFE  - ICE FUTURES U.S."
    assert pos.CONTRACTS["CPER"][1] == "COPPER- #1 - COMMODITY EXCHANGE INC."


def test_the_printed_contract_is_the_market_that_was_read():
    """The prompt names the market, so a wrong mapping is visible in the output."""
    rows = [
        {"report_date_as_yyyy_mm_dd": f"2026-09-{day:02d}", "open_interest_all": "1000",
         "m_money_positions_long_all": "600", "m_money_positions_short_all": "400"}
        for day in range(8, 0, -1)
    ]
    snapshot = pos.build_snapshot("GLD", rows)
    assert snapshot is not None
    assert snapshot.contract == "GOLD - COMMODITY EXCHANGE INC."
    assert re.match(r"^Contract: GOLD - COMMODITY EXCHANGE INC\. \(positions as of ",
                    snapshot.as_lines()[0])
