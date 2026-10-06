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
* When the list was chosen, the news search asked for ``"<ticker> stock"``
  (production's query, ``orchestrator/news.py``), so no ticker whose letters
  are the usual name of something bigger in market news. Dow Inc. ("DOW
  stock" finds the Dow Jones index) and ASE Technology ("ASX stock" finds the
  Australian exchange) were replaced by Martin Marietta and UMC. A news check
  on 3 Oct 2026 showed that this query also finds other things for short
  tickers (SO, C, D, T, ED, NOW, V, ICE, O, F, MET, EW), so on the owner's
  decision of the same day the universe has its own query, company name plus
  ticker (``"Southern Company SO stock"``: ``COMPANIES`` and ``news_query``,
  used by ``orchestrator/universe_news.py``); production's query is
  unchanged. Those names were kept. A name whose headlines are still under
  30% relevant with the new query (``analysis/news_relevance.py``) may be
  replaced by the card's rule (2), never for its returns.
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
$1.50 a day on the two together (approved by the owner on 3 Oct 2026), a
phone alert when the day's cost passes $1.20, and another when the cap stops
a run (``orchestrator/universe.py``).

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
#: the run before the end of the list every day. Approved by the owner on
#: 3 Oct 2026.
DAILY_COST_CAP_USD: Final[float] = 1.50

#: The day's cost at which the owner's phone is told, before the cap (the
#: owner's decision of 3 Oct 2026: "add a phone alert at $1.20 a day"). Only an
#: alert: the run goes on to the cap.
DAILY_COST_WARN_USD: Final[float] = 1.20

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

#: Each name's company name, for the universe's own news search and the
#: relevance check (the owner's decision of 3 Oct 2026). The first entry is
#: the name the search asks for, as ``"<name> <ticker> stock"``
#: (``news_query``); every entry is a name a headline may call the company
#: (``match_names``). Written down before the first weekday check, and frozen
#: with the list. The first entry is never the bare ticker: on 5 Oct 2026 the
#: first check found 18 names whose first entry was (``"UPS stock"``, ``"SQM
#: stock"``), which is production's query, not the owner's; their full
#: company names were put first (``"United Parcel Service UPS stock"``).
COMPANIES: Final[dict[str, tuple[str, ...]]] = {
    # Energy
    "BKR": ("Baker Hughes",), "CNQ": ("Canadian Natural Resources", "Canadian Natural"),
    "COP": ("ConocoPhillips",), "CVX": ("Chevron",), "ENB": ("Enbridge",), "EOG": ("EOG Resources",),
    "FANG": ("Diamondback Energy", "Diamondback"), "HAL": ("Halliburton",), "KMI": ("Kinder Morgan",),
    "MPC": ("Marathon Petroleum",), "OKE": ("ONEOK", "Oneok"), "OXY": ("Occidental Petroleum", "Occidental"),
    "PSX": ("Phillips 66",), "SLB": ("Schlumberger", "SLB"), "VLO": ("Valero",),
    "WMB": ("Williams Companies", "Williams Cos"),
    # Materials
    "ALB": ("Albemarle",), "APD": ("Air Products",), "CRH": ("CRH plc", "CRH"), "DD": ("DuPont",), "ECL": ("Ecolab",),
    "FCX": ("Freeport-McMoRan", "Freeport McMoRan"), "LIN": ("Linde",),
    "MLM": ("Martin Marietta",), "NEM": ("Newmont",), "NTR": ("Nutrien",), "NUE": ("Nucor",),
    "PPG": ("PPG Industries", "PPG"), "SHW": ("Sherwin-Williams", "Sherwin Williams"),
    "VMC": ("Vulcan Materials",),
    # Industrials
    "ADP": ("Automatic Data Processing", "ADP"), "BA": ("Boeing",), "CMI": ("Cummins",), "CSX": ("CSX Corporation", "CSX"),
    "DE": ("Deere", "John Deere"), "EMR": ("Emerson Electric", "Emerson"), "ETN": ("Eaton",),
    "GD": ("General Dynamics",), "GE": ("GE Aerospace", "General Electric"),
    "ITW": ("Illinois Tool Works",), "JCI": ("Johnson Controls",), "LHX": ("L3Harris",),
    "LMT": ("Lockheed Martin", "Lockheed"), "MMM": ("3M",), "NOC": ("Northrop Grumman", "Northrop"),
    "PH": ("Parker Hannifin", "Parker-Hannifin"), "RSG": ("Republic Services",),
    "RTX": ("RTX Corporation", "RTX", "Raytheon"), "TT": ("Trane Technologies", "Trane"), "UNP": ("Union Pacific",),
    "UPS": ("United Parcel Service", "UPS"), "WM": ("Waste Management",),
    # Consumer discretionary
    "ABNB": ("Airbnb",), "AMZN": ("Amazon",), "AZO": ("AutoZone",),
    "BKNG": ("Booking Holdings", "Booking.com"), "CMG": ("Chipotle",), "F": ("Ford Motor", "Ford"),
    "GM": ("General Motors",), "HD": ("Home Depot",), "HLT": ("Hilton",), "LOW": ("Lowe's", "Lowe’s"),
    "MAR": ("Marriott",), "MCD": ("McDonald's", "McDonald’s"), "NKE": ("Nike",),
    "ORLY": ("O'Reilly Automotive", "O'Reilly", "O’Reilly"), "ROST": ("Ross Stores",), "SBUX": ("Starbucks",),
    "TJX": ("TJX Companies", "TJX"), "TSLA": ("Tesla",), "YUM": ("Yum! Brands", "Yum Brands"),
    # Consumer staples
    "ADM": ("Archer-Daniels-Midland", "Archer Daniels Midland", "ADM"),
    "CL": ("Colgate-Palmolive", "Colgate"), "COST": ("Costco",), "GIS": ("General Mills",),
    "HSY": ("Hershey",), "KMB": ("Kimberly-Clark", "Kimberly Clark"), "KO": ("Coca-Cola", "Coca Cola"),
    "KR": ("Kroger",), "MDLZ": ("Mondelez",), "MNST": ("Monster Beverage",), "MO": ("Altria",),
    "PEP": ("PepsiCo",), "PM": ("Philip Morris International", "Philip Morris"), "SYY": ("Sysco",),
    "TGT": ("Target", "Target Corp", "Target Corporation", "Target's", "Target’s"),
    "WMT": ("Walmart",),
    # Health care
    "ABBV": ("AbbVie",), "ABT": ("Abbott Laboratories", "Abbott"), "AMGN": ("Amgen",),
    "BMY": ("Bristol-Myers Squibb", "Bristol Myers"), "BSX": ("Boston Scientific",), "CI": ("Cigna",),
    "CVS": ("CVS Health", "CVS"), "DHR": ("Danaher",), "ELV": ("Elevance Health", "Elevance"),
    "EW": ("Edwards Lifesciences",), "GILD": ("Gilead Sciences", "Gilead"), "HCA": ("HCA Healthcare", "HCA"),
    "IDXX": ("IDEXX Laboratories", "IDEXX", "Idexx"), "ISRG": ("Intuitive Surgical",), "MRK": ("Merck",),
    "PFE": ("Pfizer",), "REGN": ("Regeneron",), "SYK": ("Stryker",),
    "TMO": ("Thermo Fisher Scientific", "Thermo Fisher"), "UNH": ("UnitedHealth",),
    "VRTX": ("Vertex Pharmaceuticals", "Vertex"), "ZTS": ("Zoetis",),
    # Financials
    "AIG": ("American International Group", "AIG"), "AXP": ("American Express", "Amex"),
    "BAC": ("Bank of America", "BofA"), "BLK": ("BlackRock",), "BX": ("Blackstone",),
    "C": ("Citigroup", "Citi"), "CB": ("Chubb",), "CME": ("CME Group", "CME"), "COF": ("Capital One",),
    "GS": ("Goldman Sachs", "Goldman"), "ICE": ("Intercontinental Exchange",), "MA": ("Mastercard",),
    "MCO": ("Moody's", "Moody’s"), "MET": ("MetLife",), "MS": ("Morgan Stanley",),
    "PGR": ("Progressive", "Progressive Corp", "Progressive Corporation", "Progressive Insurance",
            "Progressive's", "Progressive’s"),
    "PNC": ("PNC Financial", "PNC"), "PYPL": ("PayPal", "Paypal"), "SCHW": ("Charles Schwab", "Schwab"),
    "STT": ("State Street",), "TRV": ("Travelers",), "USB": ("U.S. Bancorp", "US Bancorp"),
    "V": ("Visa",), "WFC": ("Wells Fargo",),
    # Information technology
    "AAPL": ("Apple",), "ACN": ("Accenture",), "ADBE": ("Adobe",), "ADI": ("Analog Devices",),
    "AMAT": ("Applied Materials",), "AMD": ("Advanced Micro Devices", "AMD"), "ANET": ("Arista Networks", "Arista"),
    "AVGO": ("Broadcom",), "CDNS": ("Cadence Design Systems", "Cadence Design", "Cadence"),
    "CRM": ("Salesforce",), "CSCO": ("Cisco",), "IBM": ("International Business Machines", "IBM"), "INTC": ("Intel",), "INTU": ("Intuit",),
    "KLAC": ("KLA",), "LRCX": ("Lam Research",), "MU": ("Micron Technology", "Micron"),
    "NOW": ("ServiceNow",), "ORCL": ("Oracle",), "PANW": ("Palo Alto Networks",), "QCOM": ("Qualcomm",),
    "SNPS": ("Synopsys",), "TXN": ("Texas Instruments",),
    # Communication services
    "CHTR": ("Charter Communications", "Charter"), "CMCSA": ("Comcast",), "DIS": ("Walt Disney", "Disney"),
    "FOXA": ("Fox Corporation", "Fox Corp"), "LYV": ("Live Nation",), "META": ("Meta Platforms", "Meta"),
    "NFLX": ("Netflix",), "OMC": ("Omnicom",), "SPOT": ("Spotify",), "T": ("AT&T",),
    "TMUS": ("T-Mobile",), "TTWO": ("Take-Two Interactive", "Take-Two"), "VZ": ("Verizon",),
    # Utilities
    "AEP": ("American Electric Power", "AEP"), "CEG": ("Constellation Energy",),
    "D": ("Dominion Energy",), "DUK": ("Duke Energy",), "ED": ("Consolidated Edison", "Con Edison", "ConEd"),
    "EXC": ("Exelon",), "NEE": ("NextEra Energy", "NextEra"),
    "PEG": ("Public Service Enterprise Group", "PSEG"), "SO": ("Southern Company", "Southern Co"),
    "SRE": ("Sempra",), "VST": ("Vistra",), "XEL": ("Xcel Energy", "Xcel"),
    # Real estate
    "AMT": ("American Tower",), "CBRE": ("CBRE Group", "CBRE"), "CCI": ("Crown Castle",),
    "DLR": ("Digital Realty",), "EQIX": ("Equinix",), "IRM": ("Iron Mountain",), "O": ("Realty Income",),
    "PLD": ("Prologis",), "PSA": ("Public Storage",), "SPG": ("Simon Property Group", "Simon Property"),
    "VICI": ("VICI Properties", "VICI"), "WELL": ("Welltower",),
    # ADR: Europe
    "AZN": ("AstraZeneca",), "BBVA": ("Banco Bilbao Vizcaya Argentaria", "BBVA"), "BP": ("BP plc", "BP"), "BTI": ("British American Tobacco",),
    "DEO": ("Diageo",), "GSK": ("GSK plc", "GSK"), "HSBC": ("HSBC Holdings", "HSBC"), "ING": ("ING Groep", "ING"), "NVS": ("Novartis",),
    "RIO": ("Rio Tinto",), "SAN": ("Banco Santander", "Santander"), "SAP": ("SAP SE", "SAP"), "SHEL": ("Shell",),
    "SNY": ("Sanofi",), "TTE": ("TotalEnergies",), "UBS": ("UBS Group", "UBS"), "UL": ("Unilever",),
    # ADR: Japan
    "HMC": ("Honda",), "IX": ("ORIX", "Orix"), "MFG": ("Mizuho",), "MUFG": ("Mitsubishi UFJ", "MUFG"),
    "NMR": ("Nomura",), "SMFG": ("Sumitomo Mitsui",), "SONY": ("Sony",), "TAK": ("Takeda",),
    # ADR: China and Hong Kong
    "BABA": ("Alibaba",), "BEKE": ("KE Holdings", "Beike"), "BIDU": ("Baidu",), "JD": ("JD.com",),
    "NTES": ("NetEase",), "PDD": ("PDD Holdings", "Pinduoduo", "Temu"), "TCOM": ("Trip.com",),
    "ZTO": ("ZTO Express",),
    # ADR: India
    "IBN": ("ICICI Bank", "ICICI"), "INFY": ("Infosys",), "MMYT": ("MakeMyTrip",),
    "RDY": ("Dr. Reddy's", "Dr Reddy's", "Dr. Reddy’s", "Dr Reddy’s"), "WIT": ("Wipro",),
    # ADR: Latin America
    "ABEV": ("Ambev",), "AMX": ("America Movil", "América Móvil"), "BAP": ("Credicorp",),
    "FMX": ("FEMSA", "Fomento Economico Mexicano"), "ITUB": ("Itau Unibanco", "Itaú Unibanco", "Itaú", "Itau"),
    "NU": ("Nu Holdings", "Nubank"), "PBR": ("Petrobras",), "SQM": ("Sociedad Quimica y Minera", "SQM"),
    "VALE": ("Vale",),
    # ADR: Israel
    "CHKP": ("Check Point Software", "Check Point"), "ICL": ("ICL Group", "ICL"), "MNDY": ("monday.com", "Monday.com"),
    "NICE": ("NICE Ltd", "NICE"), "WIX": ("Wix.com", "Wix"),
    # ADR: Korea and Taiwan
    "KB": ("KB Financial",), "PKX": ("POSCO",), "SHG": ("Shinhan Financial", "Shinhan"),
    "TSM": ("TSMC", "Taiwan Semiconductor"), "UMC": ("United Microelectronics", "UMC"),
    # ADR: Australia
    "BHP": ("BHP Group", "BHP"),
}

#: Names whose search name is also a common word in market news ("price
#: target", "progressive policies"): searched for by that name, but a headline
#: counts as theirs only by a longer form (or the ticker). Stricter, never
#: looser.
SEARCH_NAME_NOT_MATCHED: Final[frozenset[str]] = frozenset({"TGT", "PGR"})


#: The names a replacement may come from (card rule (2), Amendment 2026-10-06), as ticker -> (block,
#: company names; the first is the search name). A candidate is asked by the news check (``ONLY_NAMES``
#: in ``.github/workflows/universe-news-check.yml``) and by the verify job before it can join the list,
#: and it is never part of the list: the scorer asks ``TICKERS`` only. Empty until a name needs
#: replacing; chosen as the card says, never by price, return or score.
CANDIDATES: Final[dict[str, tuple[str, tuple[str, ...]]]] = {}


def company_names(ticker: str) -> tuple[str, ...]:
    """A name's company names: from the list, or from the candidates."""
    return COMPANIES[ticker] if ticker in COMPANIES else CANDIDATES[ticker][1]


def news_query(ticker: str) -> str:
    """The universe's news search: company name plus ticker (``"Southern Company SO stock"``).

    Only the shadow universe uses it (``orchestrator/universe_news.py``);
    production still asks for ``"<ticker> stock"``. When the name is the
    ticker itself (``"BP"``), it is said once. A candidate is searched the
    same way.
    """
    name = company_names(ticker)[0]
    return f"{ticker} stock" if name == ticker else f"{name} {ticker} stock"


def match_names(ticker: str) -> tuple[str, ...]:
    """The names a headline may call the company, for the relevance check."""
    names = company_names(ticker)
    return names[1:] if ticker in SEARCH_NAME_NOT_MATCHED else names


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
    "COMPANIES",
    "DAILY_COST_CAP_USD",
    "DAILY_COST_WARN_USD",
    "ESTIMATED_DAILY_COST_USD",
    "ESTIMATED_DAILY_MODEL_COST_USD",
    "ESTIMATED_DAILY_NEWS_COST_USD",
    "GICS_SECTORS",
    "JOURNAL_DIR",
    "NEWS_USD_PER_REQUEST",
    "REGISTRATION",
    "REPLACED",
    "SEARCH_NAME_NOT_MATCHED",
    "SECTORS",
    "SELECTED_ON",
    "SHADOW_UNIVERSE_ENABLED",
    "START",
    "TICKERS",
    "markdown_table",
    "match_names",
    "news_query",
]
