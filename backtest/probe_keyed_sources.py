#!/usr/bin/env python3
"""Do the keyed data sources answer, and under which secret name?

    python backtest/probe_keyed_sources.py

Four sources need a key, all of them free. This asks each one whether the key
it was given works and what comes back, before anything is built on top of it
-- because the alternative is discovering the answer inside a live cycle.

It also reports *which* environment variable carried each key. The names were
suggested rather than dictated, so a key stored under a name nothing reads is
a silent no-op, and that is the single most likely way this goes wrong.

**No key value is ever printed, logged, or put in a URL that is printed.** The
output of this script is uploaded as a build artifact; it has to be safe to
read. Requests carry the key, the printed form never does.

Needs the open internet and the secrets, so it runs on a runner.
Read-only. No orders, no LLM, no trading.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx  # noqa: E402

#: Every name a key might plausibly have been stored under. The first that is
#: set wins. Generous on purpose: a key under an unread name is invisible.
CANDIDATES = {
    "EIA": ("EIA_API_KEY", "EIA_KEY", "EIA_TOKEN"),
    "USDA": ("USDA_NASS_KEY", "USDA_API_KEY", "NASS_API_KEY", "USDA_KEY", "NASS_KEY"),
    "FRED": ("FRED_API_KEY", "FRED_KEY", "FRED_TOKEN"),
    "FINNHUB": ("FINNHUB_API_KEY", "FINNHUB_KEY", "FINNHUB_TOKEN"),
}

TIMEOUT = 30.0


def key_for(source: str) -> tuple[Optional[str], Optional[str]]:
    """``(name, value)`` of the first candidate that is set and non-empty."""
    for name in CANDIDATES[source]:
        value = (os.environ.get(name) or "").strip()
        if value:
            return name, value
    return None, None


def _get(url: str, params: dict, label: str) -> Optional[Any]:
    """One request, reported by outcome rather than by exception."""
    try:
        response = httpx.get(url, params=params, timeout=TIMEOUT)
    except Exception as exc:  # noqa: BLE001 - a probe reports, it does not raise
        print(f"    {label}: request failed -- {type(exc).__name__}")
        return None
    if response.status_code != 200:
        # The body can echo the key back in an error message, so only the
        # status and a short scrubbed excerpt are shown.
        excerpt = " ".join(response.text.split())[:160]
        for _, value in (key_for(s) for s in CANDIDATES):
            if value and value in excerpt:
                excerpt = excerpt.replace(value, "<redacted>")
        print(f"    {label}: HTTP {response.status_code} -- {excerpt}")
        return None
    try:
        return response.json()
    except ValueError:
        print(f"    {label}: 200 but not JSON")
        return None


def probe_eia(key: str) -> None:
    """Weekly petroleum stocks. The route metadata validates the key and names
    the facets, which is what a fetcher has to get right."""
    payload = _get("https://api.eia.gov/v2/petroleum/stoc/wstk/",
                   {"api_key": key}, "route metadata")
    if payload:
        route = (payload.get("response") or {})
        facets = [f.get("id") for f in route.get("facets", [])]
        freqs = [f.get("id") for f in route.get("frequency", [])]
        print(f"    route ok: facets={facets} frequencies={freqs}")

    data = _get("https://api.eia.gov/v2/petroleum/stoc/wstk/data/", {
        "api_key": key, "frequency": "weekly", "data[0]": "value",
        "facets[series][]": "WCESTUS1",
        "sort[0][column]": "period", "sort[0][direction]": "desc", "length": "4",
    }, "crude stocks (WCESTUS1)")
    if data:
        rows = (data.get("response") or {}).get("data") or []
        print(f"    crude stocks: {len(rows)} rows")
        for row in rows[:3]:
            print(f"      {row.get('period')}  {row.get('value')} {row.get('units')}")

    gas = _get("https://api.eia.gov/v2/natural-gas/stor/wkly/data/", {
        "api_key": key, "frequency": "weekly", "data[0]": "value",
        "sort[0][column]": "period", "sort[0][direction]": "desc", "length": "3",
    }, "natural gas storage")
    if gas:
        rows = (gas.get("response") or {}).get("data") or []
        print(f"    gas storage: {len(rows)} rows")
        for row in rows[:2]:
            print(f"      {row.get('period')}  {row.get('value')} {row.get('units')}"
                  f"  [{row.get('series-description') or row.get('duoarea')}]")


def probe_usda(key: str) -> None:
    """Crop condition and stocks. `get_counts` is the cheap key check -- it
    returns one number rather than a megabyte of rows."""
    counts = _get("https://quickstats.nass.usda.gov/api/get_counts/", {
        "key": key, "commodity_desc": "CORN", "year": "2026",
        "statisticcat_desc": "CONDITION",
    }, "corn condition count")
    if counts:
        print(f"    corn condition rows available: {counts.get('count')}")

    rows = _get("https://quickstats.nass.usda.gov/api/api_GET/", {
        "key": key, "commodity_desc": "CORN", "year": "2026",
        "statisticcat_desc": "CONDITION", "agg_level_desc": "NATIONAL",
        "format": "JSON",
    }, "corn condition data")
    if rows:
        data = rows.get("data") or []
        print(f"    corn condition: {len(data)} rows")
        for row in data[:3]:
            print(f"      {row.get('reference_period_desc')} "
                  f"{row.get('unit_desc')} = {row.get('Value')}")


def probe_fred(key: str) -> None:
    """The monthly releases Yahoo's index symbols cannot give: prices, jobs."""
    for series, what in (("CPIAUCSL", "CPI"), ("UNRATE", "unemployment"),
                         ("ICSA", "jobless claims")):
        payload = _get("https://api.stlouisfed.org/fred/series/observations", {
            "series_id": series, "api_key": key, "file_type": "json",
            "sort_order": "desc", "limit": "3",
        }, f"{what} ({series})")
        if payload:
            obs = payload.get("observations") or []
            latest = ", ".join(f"{o.get('date')}={o.get('value')}" for o in obs[:3])
            print(f"    {what:<16} {latest}")


def probe_finnhub(key: str) -> None:
    """Earnings surprises, and whether the free tier covers a non-US name."""
    for symbol in ("MSFT", "ASML", "TEVA"):
        payload = _get("https://finnhub.io/api/v1/stock/earnings",
                       {"symbol": symbol, "token": key}, f"earnings {symbol}")
        if payload is None:
            continue
        if not isinstance(payload, list) or not payload:
            print(f"    {symbol:<6} no earnings rows returned")
            continue
        row = payload[0]
        print(f"    {symbol:<6} {row.get('period')}: actual {row.get('actual')} "
              f"vs estimate {row.get('estimate')} ({row.get('surprisePercent')}%)")


PROBES = {"EIA": probe_eia, "USDA": probe_usda, "FRED": probe_fred,
          "FINNHUB": probe_finnhub}


def main() -> int:
    missing = []
    for source, probe in PROBES.items():
        name, key = key_for(source)
        print(f"===== {source} =====")
        if not key:
            print(f"  NOT SET -- looked for: {', '.join(CANDIDATES[source])}")
            missing.append(source)
            print()
            continue
        print(f"  key found in {name} ({len(key)} characters)")
        probe(key)
        print()

    if missing:
        print(f"Missing keys: {', '.join(missing)}")
        print("A key stored under a name nothing reads is the same as no key.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
