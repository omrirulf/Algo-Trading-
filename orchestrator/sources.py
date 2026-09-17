"""The one place on the context side where a credential is read.

A guardrail in CI holds every module under ``orchestrator/`` to reading no
credentials, with a short allowlist for the ones that must. The reason is
specific and worth restating: these modules handle untrusted third-party data
and assemble the text sent to a language model, and the signal journal they
feed is **committed to the repository every cycle**. A key that reached a
snapshot would reach a prompt and then a public git history.

Four free sources need a key -- EIA, USDA, FRED and Finnhub -- and rather than
letting four modules each read the environment, all four fetches live here and
the parsing modules stay what their siblings are: pure functions over payloads
handed to them. That trades four files to audit for one.

The rules this file keeps, and the tests that hold it to them:

* **A key goes into a request and nowhere else.** Never into a return value,
  never into a log line, never into an exception message that is logged. Error
  bodies from these APIs echo the query string back, so only exception *types*
  are ever recorded.
* **Nothing here formats or persists.** No rendering helpers, no file
  writes. It fetches, and what it returns is raw -- turning a payload into
  prompt text is the parsing modules' job, and a guardrail greps this file to
  keep it that way.
* **No key is a state, not a failure.** Every function returns empty, and the
  caller omits the section. A key is a way to see more; the system works
  without any of them, and that is checked.
"""

from __future__ import annotations

import logging
import os
from typing import Any, Optional

log = logging.getLogger(__name__)

REQUEST_TIMEOUT_SECONDS = 30.0
USDA_TIMEOUT_SECONDS = 45.0

#: Every name a key may be stored under, most-expected first. Several per
#: source because a key saved under a name nothing reads is a silent no-op --
#: silent precisely because an absent key is legitimate everywhere here -- and
#: silence is the one failure mode this system cannot see.
KEY_ENV_VARS = {
    "eia": ("EIA_API_KEY", "EIA_KEY", "EIA_TOKEN"),
    "usda": ("USDA_NASS_KEY", "USDA_API_KEY", "NASS_API_KEY", "USDA_KEY", "NASS_KEY"),
    "fred": ("FRED_API_KEY", "FRED_KEY", "FRED_TOKEN"),
    "finnhub": ("FINNHUB_API_KEY", "FINNHUB_KEY", "FINNHUB_TOKEN"),
}

FRED_URL = "https://api.stlouisfed.org/fred/series/observations"
EIA_URL = "https://api.eia.gov/v2"
USDA_URL = "https://quickstats.nass.usda.gov/api/api_GET/"
FINNHUB_URL = "https://finnhub.io/api/v1/stock/earnings"


def api_key(source: str) -> Optional[str]:
    """The key for one source, or ``None`` when none is configured."""
    for name in KEY_ENV_VARS.get(source, ()):
        value = (os.environ.get(name) or "").strip()
        if value:
            return value
    return None


def configured() -> dict[str, bool]:
    """Which sources have a key. Booleans only -- never the keys themselves."""
    return {source: api_key(source) is not None for source in KEY_ENV_VARS}


def _client(client: Any, timeout: float):
    """``(client, owned)`` -- an injected client is never closed by us."""
    if client is not None:
        return client, False
    import httpx

    return httpx.Client(timeout=timeout), True


def _json(client: Any, url: str, params: dict, what: str) -> Any:
    """One request. Returns ``None`` on any failure, and never says why in
    detail: these APIs echo the query string, key included, into error bodies.
    """
    try:
        response = client.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as exc:  # noqa: BLE001 - the type is all that is safe to log
        log.warning("%s unavailable: %s", what, type(exc).__name__)
        return None


def fetch_fred_releases(client: Any = None) -> dict[str, Any]:
    """Raw observations per series label. Empty without a key."""
    from orchestrator import fred

    key = api_key("fred")
    if not key:
        return {}
    client, owned = _client(client, REQUEST_TIMEOUT_SECONDS)
    out: dict[str, Any] = {}
    try:
        for series_id, label, units, _ in fred.SERIES:
            payload = _json(client, FRED_URL, {
                "series_id": series_id, "api_key": key, "file_type": "json",
                "units": units, "sort_order": "desc", "limit": "6",
            }, f"FRED {series_id}")
            if payload is not None:
                out[label] = payload
    finally:
        if owned:
            client.close()
    return out


def fetch_energy_payloads(ticker: str, client: Any = None) -> dict[str, Any]:
    """Raw EIA rows per series label, for the tickers they bear on."""
    from orchestrator import energy

    wanted = energy.series_for(ticker)
    key = api_key("eia")
    if not wanted or not key:
        return {}
    client, owned = _client(client, REQUEST_TIMEOUT_SECONDS)
    out: dict[str, Any] = {}
    try:
        for label in wanted:
            route, series_id, _, _ = energy.SERIES[label]
            payload = _json(client, f"{EIA_URL}/{route}/data/", {
                "api_key": key, "frequency": "weekly", "data[0]": "value",
                "facets[series][]": series_id,
                "sort[0][column]": "period", "sort[0][direction]": "desc",
                "length": str(energy.HISTORY_WEEKS + 1),
            }, f"EIA {series_id}")
            if payload is not None:
                out[label] = payload
    finally:
        if owned:
            client.close()
    return out


def fetch_outlook_payloads(ticker: str, client: Any = None) -> dict[str, Any]:
    """Raw EIA Short-Term Energy Outlook rows per series label, for the
    tickers they bear on. Same key as the inventories; empty without it."""
    from orchestrator import outlook

    wanted = outlook.series_for(ticker)
    key = api_key("eia")
    if not wanted or not key:
        return {}
    client, owned = _client(client, REQUEST_TIMEOUT_SECONDS)
    out: dict[str, Any] = {}
    try:
        for label in wanted:
            series_id, _, _ = outlook.SERIES[label]
            payload = _json(client, f"{EIA_URL}/{outlook.ROUTE}/data/", {
                "api_key": key, "frequency": "monthly", "data[0]": "value",
                "facets[seriesId][]": series_id,
                "sort[0][column]": "period", "sort[0][direction]": "desc",
                "length": str(outlook.ROW_LIMIT),
            }, f"EIA STEO {series_id}")
            if payload is not None:
                out[label] = payload
    finally:
        if owned:
            client.close()
    return out


def fetch_crop_rows(ticker: str, year: int, client: Any = None) -> list:
    """Raw USDA national condition rows for one crop and season."""
    from orchestrator import crops

    mapping = crops.commodity_for(ticker)
    key = api_key("usda")
    if mapping is None or not key:
        return []
    commodity, _ = mapping
    client, owned = _client(client, USDA_TIMEOUT_SECONDS)
    try:
        payload = _json(client, USDA_URL, {
            "key": key, "commodity_desc": commodity,
            "statisticcat_desc": "CONDITION", "agg_level_desc": "NATIONAL",
            "year": str(year), "format": "JSON",
        }, f"USDA {commodity} {year}")
    finally:
        if owned:
            client.close()
    rows = payload.get("data") if isinstance(payload, dict) else None
    return rows if isinstance(rows, list) else []


def fetch_earnings_rows(ticker: str, client: Any = None) -> list:
    """Raw quarterly surprise rows for one company, newest first."""
    key = api_key("finnhub")
    if not key:
        return []
    client, owned = _client(client, REQUEST_TIMEOUT_SECONDS)
    try:
        payload = _json(client, FINNHUB_URL, {"symbol": ticker, "token": key},
                        f"Finnhub earnings {ticker}")
    finally:
        if owned:
            client.close()
    return payload if isinstance(payload, list) else []


__all__ = [
    "api_key",
    "configured",
    "fetch_crop_rows",
    "fetch_earnings_rows",
    "fetch_energy_payloads",
    "fetch_fred_releases",
    "fetch_outlook_payloads",
    "KEY_ENV_VARS",
]
