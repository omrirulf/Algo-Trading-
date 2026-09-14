"""What gets traded is version-controlled, and the zone fallback actually fires.

The second half of this file exists because of a real bug: BRIGHTDATA_SERP_ZONE
defaulted to "serp_api", which is non-empty, so the Web Unlocker fallback could
never be reached. Anyone who had only run `brightdata login` would have sent a
zone name their account did not have, and the first live cycle would have
failed on every ticker.
"""

from __future__ import annotations

import pytest

from config import instruments as inst
from config import watchlist as wl
from config.settings import Settings
from orchestrator import news, pricing


# --- the list itself ------------------------------------------------------


def test_the_default_watchlist_is_the_curated_one():
    assert Settings(_env_file=None).watchlist_tickers == list(wl.DEFAULT_WATCHLIST)


def test_no_duplicate_tickers():
    """A duplicate would silently double that ticker's cost every cycle."""
    assert len(set(wl.DEFAULT_WATCHLIST)) == len(wl.DEFAULT_WATCHLIST)


def test_every_bucket_is_represented():
    for name, bucket in wl.BUCKETS.items():
        assert bucket, f"{name} is empty"
        assert set(bucket) <= set(wl.DEFAULT_WATCHLIST), f"{name} is not in the default"


def test_the_buckets_account_for_the_whole_list():
    from_buckets = [t for bucket in wl.BUCKETS.values() for t in bucket]
    assert sorted(from_buckets) == sorted(wl.DEFAULT_WATCHLIST)


def test_it_is_not_three_correlated_megacaps_any_more():
    """The starting default was AAPL, MSFT, NVDA -- closer to one bet than three."""
    assert len(wl.DEFAULT_WATCHLIST) > 3
    assert len(wl.BUCKETS) >= 4


def test_every_sleeve_and_asset_class_is_reachable():
    """The reason the list exists: breadth that single US tech names cannot give."""
    for bucket in ("Financials", "Energy", "Fund: International equity",
                   "Fund: Duration", "Fund: Precious metals", "Fund: Agriculture"):
        assert bucket in wl.BUCKETS


def test_no_single_sector_dominates_the_single_name_sleeve():
    """The previous list was 37% technology and called its ADRs diversification.

    ASML, TSM, SAP and INFY are global technology cyclicals: they fall with US
    technology in a drawdown, whatever exchange they list on. A sector cap is
    the check that actually bites; a country cap is not.
    """
    largest = max(len(b) for b in inst.SINGLE_NAME_SECTORS.values())
    assert largest / len(inst.SINGLE_NAMES) <= 0.25


def test_the_index_sleeve_reaches_what_single_names_cannot():
    """Cap tiers and non-equity asset classes have no affordable single-name route."""
    assert "IWM" in inst.FUNDS   # small caps
    assert "VNQ" in inst.FUNDS   # REITs
    assert "TLT" in inst.FUNDS   # duration -- the only non-equity risk here
    # The goods themselves, not the companies that mine and drill them.
    for commodity in ("GLD", "SLV", "CPER", "USO", "CORN", "JO"):
        assert commodity in inst.COMMODITY_FUNDS


def test_tickers_look_like_tickers():
    """A stray lowercase or whitespace entry would be fetched as-is."""
    for ticker in wl.DEFAULT_WATCHLIST:
        assert ticker == ticker.strip().upper()
        assert 1 <= len(ticker) <= 5
        assert ticker.isalpha()


def test_an_explicit_watchlist_still_overrides():
    assert Settings(watchlist="AAPL, msft ", _env_file=None).watchlist_tickers == ["AAPL", "MSFT"]


# --- cost is a function of list length ------------------------------------


def test_cost_scales_with_the_number_of_tickers():
    """Breadth is the main cost lever, so it should be visible."""
    one = wl.estimated_monthly_cost_usd(1)
    ten = wl.estimated_monthly_cost_usd(10)
    assert ten == pytest.approx(one * 10)
    assert one > 0


def test_the_default_list_has_an_estimable_cost():
    assert wl.estimated_monthly_cost_usd(len(wl.DEFAULT_WATCHLIST)) > 0


# --- the zone fallback that used to be dead code --------------------------


def test_the_serp_zone_no_longer_defaults_to_a_name(monkeypatch):
    """The regression this file was written for.

    While BRIGHTDATA_SERP_ZONE defaulted to "serp_api", resolve_zone always
    returned it and the unlocker fallback was unreachable.
    """
    assert Settings(_env_file=None).brightdata_serp_zone == ""


def test_default_settings_resolve_to_the_cli_zone(monkeypatch):
    settings = Settings(_env_file=None)
    resolved = news.resolve_zone(settings.brightdata_serp_zone, settings.brightdata_unlocker_zone)
    assert resolved == "cli_unlocker"


def test_an_explicit_serp_zone_still_wins():
    settings = Settings(brightdata_serp_zone="my_serp", _env_file=None)
    resolved = news.resolve_zone(settings.brightdata_serp_zone, settings.brightdata_unlocker_zone)
    assert resolved == "my_serp"


def test_the_cli_env_var_beats_the_configured_default(monkeypatch):
    monkeypatch.setenv(news.CLI_UNLOCKER_ENV_VAR, "from_env")
    assert news.resolve_zone("", "cli_unlocker") == "from_env"


def test_no_zone_at_all_resolves_to_empty(monkeypatch):
    assert news.resolve_zone("", "") == ""


def test_a_provider_with_no_zone_anywhere_still_errors(monkeypatch):
    with pytest.raises(news.NewsFetchError) as excinfo:
        news.BrightDataNewsProvider("tok", "", unlocker_zone="")
    assert "BRIGHTDATA_SERP_ZONE" in str(excinfo.value)


def test_the_estimate_is_derived_from_the_price_table_not_hard_coded():
    """A price change should move the estimate without a second edit.

    The figure used to be a single magic float, which meant a repriced model
    left the sizing table quietly wrong. Pinning the derivation here is what
    stops it from drifting back.
    """
    price = pricing.PRICES["claude-opus-5"]
    expected = (
        wl.ESTIMATED_INPUT_TOKENS * price.input_per_mtok
        + wl.ASSUMED_OUTPUT_TOKENS * price.output_per_mtok
    ) / 1e6
    assert wl.COST_PER_TICKER_PER_CYCLE_USD == pytest.approx(expected)


def test_output_tokens_dominate_the_estimate():
    """The reason effort is a bigger lever than list length.

    If this ever flips, the advice in docs/cost.mdx and docs/watchlist.mdx --
    turn effort down before trimming tickers -- stops being true.
    """
    price = pricing.PRICES["claude-opus-5"]
    input_cost = wl.ESTIMATED_INPUT_TOKENS * price.input_per_mtok
    output_cost = wl.ASSUMED_OUTPUT_TOKENS * price.output_per_mtok
    assert output_cost > input_cost * 2
