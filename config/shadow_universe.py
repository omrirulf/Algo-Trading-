"""The shadow stock universe: about 250 more names, scored every day, never traded.

Why it exists (the owner's instruction of 2 Oct 2026, item 5). The race and
the daily IC report can only judge the model on the 80 production names, and
80 names a day is a small sample for a rank test: a real but modest skill
needs many names on many days before it shows. So a second, larger list is
scored by the same model, with the same settings and the same prompt as
production, one call per name per trading day, and the IC report from item 4
reads those scores at 1 and 3 sessions, hidden until the checkpoints. Nothing
here is ever traded. It is shadow-only, like every arm and fund in this
project.

How the list was chosen (the selection rule, written down before any
result exists). Chosen on 2026-10-02, by hand, from well-known large and
mid-cap stocks listed in the US, spread over all 11 GICS sectors, plus a block
of large foreign companies that trade in New York. Rules:

* No ETF and no fund: one company per line.
* One share class per company (so no GOOG next to GOOGL, no BRK.B, no
  dotted class tickers at all).
* None of the 80 production names, and no other share class of one. The two
  universes are kept apart on purpose: the production names already have
  their own record, and a name in both lists would be counted twice. A test
  pins this against ``config.watchlist.DEFAULT_WATCHLIST``.
* Long-established names only. Names with a merger, a buy-out or a split
  announced for 2026-2027 were left out (for example Kenvue, Electronic Arts,
  Warner Bros. Discovery, Norfolk Southern, Honeywell, Kraft Heinz, Keurig Dr
  Pepper, Corteva, FedEx, Devon and Coterra), because a name that stops
  trading, or drops in price on a spin-off day, breaks a price-only return.
  After a review the same day, Johnson & Johnson (DePuy Synthes), Medtronic
  (MiniMed) and S&P Global (Mobility) were replaced by Edwards Lifesciences,
  IDEXX and MetLife for the same reason: each has a separation announced that
  may fall inside the scoring window.
* The news search asks for ``"<ticker> stock"`` (``orchestrator/news.py``,
  unchanged), so no ticker whose letters are the usual name of something
  bigger in market news. Dow Inc. ("DOW stock" finds the Dow Jones index) and
  ASE Technology ("ASX stock" finds the Australian exchange) were replaced by
  Martin Marietta and UMC.
* A name that does not resolve in the verify check is replaced. On 3 Oct 2026
  BNY Mellon (BK: no prices returned) and AvalonBay (AVB: fewer than two
  closes in three months) failed it in three runs while the other 249 names
  resolved, and were replaced by State Street and Iron Mountain. The card
  states the replacement rule.
* The ADR block holds large foreign companies bought in dollars on a US
  exchange. Most trade as ADRs; a few list their own shares directly (Check
  Point, Wix, monday.com, ICL, Nu, UBS). For this list they are the same
  thing. Canadian and Irish companies that list their common shares in New
  York sit in their GICS sector, not in the ADR block.

Checked before it counts. The list was written from knowledge in a sandbox
with no market data, exactly like the production watchlist was. Before the
registration date every name must be checked with ``backtest/verify_tickers.py``
(its ``check()``; it needs the network). The workflow
``.github/workflows/shadow-universe.yml`` has a by-hand ``verify`` run that
does exactly that and needs no key. A name that does not resolve is replaced
before registration, never after.

Frozen at registration. The list is published in the pre-registration card
on ``REGISTRATION`` (2026-12-22, the race's first checkpoint, where the IC
test is registered) and does not change afterwards: no name added, removed or
replaced, whatever it does. A name that is later bought out or delisted is
still asked every day (one call, about a quarter of a cent), but its lines
have no price to be measured against, so the IC report leaves them out.

Off until ``START``. ``SHADOW_UNIVERSE_ENABLED`` keeps the scorer off, the
same pattern as the screening flag; a test fails if the flag is on before the
date the pre-registration names. Cost: about $1.05 a day -- the model about
$0.65 (measured: the full model's 61 production calls in October 2026
averaged $0.0025 each) and the Bright Data news searches about $0.40 (about
270 requests at $1.50 per 1,000; about $102 a year) -- with a hard cap of
$1.50 a day on the two together and a phone alert when the cap stops a run
(``orchestrator/universe.py``).

Standard library only and no side effects, so any package may import it --
including the read-only report that reads these lines.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Final

#: The scorer's on/off switch. False until the pre-registration says the
#: universe is on; ``tests/test_shadow_universe.py`` fails if this is True
#: before the date the pre-registration names.
SHADOW_UNIVERSE_ENABLED: Final[bool] = False

#: The first UTC day the universe may be scored (the owner's instruction of
#: 2 Oct 2026). Must equal the date the pre-registration names.
START: Final[date] = date(2027, 1, 1)

#: The checkpoint at which the list is published in the pre-registration card
#: and frozen: the race's first planned look, where the IC test is registered.
REGISTRATION: Final[date] = date(2026, 12, 22)

#: The day the list below was chosen.
SELECTED_ON: Final[date] = date(2026, 10, 2)

#: Hard cap on the universe's cost in one UTC day, in dollars: the model and
#: the Bright Data news searches together (the owner's instruction of 3 Oct
#: 2026: "add it to the cost cap and the alert"). The scorer stops asking once
#: it is reached and the workflow alerts the owner's phone. $1 when it counted
#: the model only (2 Oct 2026); $1.50 since the news is counted too, because
#: the two together are expected at about $1.05 a day and a $1 cap would stop
#: the run before the end of the list every day. Proposed on 3 Oct 2026; the
#: owner confirms it before the pull request is merged.
DAILY_COST_CAP_USD: Final[float] = 1.50

#: What a full day's model calls are expected to cost, in dollars (about 250
#: calls at the measured $0.0025 each).
ESTIMATED_DAILY_MODEL_COST_USD: Final[float] = 0.65

#: Bright Data's price per request (pay as you go: $1.50 per 1,000 successful
#: requests, the same for the SERP API and the Web Unlocker since the price
#: list of 14 Jul 2026). Every request sent is charged to the cap, answered or
#: not, so the cap never counts less than may be billed.
NEWS_USD_PER_REQUEST: Final[float] = 0.0015

#: What a full day's news searches are expected to cost, in dollars: about
#: 270 requests (one per name, plus the retries production's journal shows,
#: plus re-runs for failed names) at ``NEWS_USD_PER_REQUEST``. About $102 a
#: year (252 trading days); $0.38 a day ($95 a year) with exactly one request
#: per name.
ESTIMATED_DAILY_NEWS_COST_USD: Final[float] = 0.40

#: What a full day is expected to cost, model and news, in dollars. For the
#: summary line only; the cap above is what stops a run.
ESTIMATED_DAILY_COST_USD: Final[float] = ESTIMATED_DAILY_MODEL_COST_USD + ESTIMATED_DAILY_NEWS_COST_USD

#: The repository root, worked out the same way ``config/settings.py`` does
#: it, so this module needs nothing outside the standard library.
_PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent

#: Where the universe's lines go: one file per UTC month (``2027-01.log``,
#: ...), exactly like the production journal (``config/journal_files.py``),
#: and never mixed into it. Mirrors ``SIGNAL_JOURNAL_PATH`` (``logs/journal``).
JOURNAL_DIR: Final[Path] = _PROJECT_ROOT / "logs" / "shadow_universe"

#: The 11 GICS sectors, in GICS code order (10 Energy ... 60 Real Estate).
GICS_SECTORS: Final[tuple[str, ...]] = (
    "Energy",
    "Materials",
    "Industrials",
    "Consumer discretionary",
    "Consumer staples",
    "Health care",
    "Financials",
    "Information technology",
    "Communication services",
    "Utilities",
    "Real estate",
)

#: How every label in the ADR block starts.
ADR_PREFIX: Final[str] = "ADR: "

#: The list, by block: the 11 GICS sectors, then the ADR block by region.
#: Alphabetical inside each block. Frozen at ``REGISTRATION``.
BLOCKS: Final[dict[str, tuple[str, ...]]] = {
    "Energy": (
        "BKR", "CNQ", "COP", "CVX", "ENB", "EOG", "FANG", "HAL",
        "KMI", "MPC", "OKE", "OXY", "PSX", "SLB", "VLO", "WMB",
    ),
    "Materials": (
        "ALB", "APD", "CRH", "DD", "ECL", "FCX", "LIN",
        "MLM", "NEM", "NTR", "NUE", "PPG", "SHW", "VMC",
    ),
    "Industrials": (
        "ADP", "BA", "CMI", "CSX", "DE", "EMR", "ETN", "GD", "GE", "ITW", "JCI",
        "LHX", "LMT", "MMM", "NOC", "PH", "RSG", "RTX", "TT", "UNP", "UPS", "WM",
    ),
    "Consumer discretionary": (
        "ABNB", "AMZN", "AZO", "BKNG", "CMG", "F", "GM", "HD", "HLT", "LOW",
        "MAR", "MCD", "NKE", "ORLY", "ROST", "SBUX", "TJX", "TSLA", "YUM",
    ),
    "Consumer staples": (
        "ADM", "CL", "COST", "GIS", "HSY", "KMB", "KO", "KR",
        "MDLZ", "MNST", "MO", "PEP", "PM", "SYY", "TGT", "WMT",
    ),
    "Health care": (
        "ABBV", "ABT", "AMGN", "BMY", "BSX", "CI", "CVS", "DHR", "ELV", "EW", "GILD",
        "HCA", "IDXX", "ISRG", "MRK", "PFE", "REGN", "SYK", "TMO", "UNH", "VRTX", "ZTS",
    ),
    "Financials": (
        "AIG", "AXP", "BAC", "BLK", "BX", "C", "CB", "CME", "COF", "GS", "ICE", "MA",
        "MCO", "MET", "MS", "PGR", "PNC", "PYPL", "SCHW", "STT", "TRV", "USB", "V", "WFC",
    ),
    "Information technology": (
        "AAPL", "ACN", "ADBE", "ADI", "AMAT", "AMD", "ANET", "AVGO", "CDNS", "CRM", "CSCO", "IBM",
        "INTC", "INTU", "KLAC", "LRCX", "MU", "NOW", "ORCL", "PANW", "QCOM", "SNPS", "TXN",
    ),
    "Communication services": (
        "CHTR", "CMCSA", "DIS", "FOXA", "LYV", "META", "NFLX",
        "OMC", "SPOT", "T", "TMUS", "TTWO", "VZ",
    ),
    "Utilities": (
        "AEP", "CEG", "D", "DUK", "ED", "EXC", "NEE", "PEG", "SO", "SRE", "VST", "XEL",
    ),
    "Real estate": (
        "AMT", "CBRE", "CCI", "DLR", "EQIX", "IRM", "O", "PLD", "PSA", "SPG", "VICI", "WELL",
    ),
    ADR_PREFIX + "Europe": (
        "AZN", "BBVA", "BP", "BTI", "DEO", "GSK", "HSBC", "ING", "NVS",
        "RIO", "SAN", "SAP", "SHEL", "SNY", "TTE", "UBS", "UL",
    ),
    ADR_PREFIX + "Japan": ("HMC", "IX", "MFG", "MUFG", "NMR", "SMFG", "SONY", "TAK"),
    ADR_PREFIX + "China and Hong Kong": ("BABA", "BEKE", "BIDU", "JD", "NTES", "PDD", "TCOM", "ZTO"),
    ADR_PREFIX + "India": ("IBN", "INFY", "MMYT", "RDY", "WIT"),
    ADR_PREFIX + "Latin America": ("ABEV", "AMX", "BAP", "FMX", "ITUB", "NU", "PBR", "SQM", "VALE"),
    ADR_PREFIX + "Israel": ("CHKP", "ICL", "MNDY", "NICE", "WIX"),
    ADR_PREFIX + "Korea and Taiwan": ("KB", "PKX", "SHG", "TSM", "UMC"),
    ADR_PREFIX + "Australia": ("BHP",),
}

#: The names replaced before registration, old -> (new, the card's rule: 1 a
#: separation or deal inside the window, 2 a news search that finds something
#: else, 3 not resolving in the verify check). For the record and the card;
#: the verify job reports whether the rule-3 names resolve again.
REPLACED: Final[dict[str, tuple[str, int]]] = {
    "JNJ": ("EW", 1), "MDT": ("IDXX", 1), "SPGI": ("MET", 1),
    "DOW": ("MLM", 2), "ASX": ("UMC", 2),
    "BK": ("STT", 3), "AVB": ("IRM", 3),
}

#: Every name, in block order then alphabetical: the order the scorer asks in.
TICKERS: Final[tuple[str, ...]] = tuple(t for names in BLOCKS.values() for t in names)

#: Ticker -> its block's label (a GICS sector, or ``ADR: <region>``), for the card.
SECTORS: Final[dict[str, str]] = {t: label for label, names in BLOCKS.items() for t in names}


def markdown_table() -> str:
    """The list as a Markdown table, one row per block, for the pre-registration card."""
    rows = [
        f"Shadow stock universe: {len(TICKERS)} names, chosen on {SELECTED_ON.isoformat()}, "
        f"frozen on {REGISTRATION.isoformat()}.",
        "",
        "| Sector | Names | Tickers |",
        "|---|---:|---|",
    ]
    rows += [f"| {label} | {len(names)} | {', '.join(names)} |" for label, names in BLOCKS.items()]
    rows.append(f"| **Total** | **{len(TICKERS)}** | |")
    return "\n".join(rows)


__all__ = [
    "ADR_PREFIX",
    "BLOCKS",
    "DAILY_COST_CAP_USD",
    "ESTIMATED_DAILY_COST_USD",
    "ESTIMATED_DAILY_MODEL_COST_USD",
    "ESTIMATED_DAILY_NEWS_COST_USD",
    "GICS_SECTORS",
    "JOURNAL_DIR",
    "NEWS_USD_PER_REQUEST",
    "REGISTRATION",
    "REPLACED",
    "SECTORS",
    "SELECTED_ON",
    "SHADOW_UNIVERSE_ENABLED",
    "START",
    "TICKERS",
    "markdown_table",
]
