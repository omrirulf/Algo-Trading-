# News relevance: is a headline about the name?

A code-only check, asked for by the owner on 2026-10-03. No model is asked.

**The rule, as the owner wrote it:** a headline counts as relevant if the company name, or the ticker as a whole
word, appears in the title or the first sentence. The code is `analysis/news_relevance.py`:

- The text is the title plus the snippet's first sentence (up to the first ". ", "! " or "? ").
- A name matches as whole words, as written or in capitals (`Nvidia` or `NVIDIA`). A company name is a proper
  noun, so "visa rules" is not Visa.
- The ticker matches as a whole word in capitals, with `$` allowed in front (`$NVDA`, `NYSE:T`). A hyphen or
  `&` joins it to the next word, so `T-Mobile` is not `T`. A one-letter ticker standing alone is weak evidence
  (`Class C`), so every table also shows the share that names the company by name alone.
- A name fails with under 30% relevant headlines, or with none.

It is used two ways.

## 1. The shadow stock universe (decides replacements under the card's rule (2))

The universe has its own news query, company name plus ticker ("Southern Company SO stock",
`config/shadow_universe.py`), and production's query is unchanged. The check asks that search once for each of
the 251 names on a weekday (`.github/workflows/universe-news-check.yml`) and reports the share per name, the
names under 30% and the overall share. A name still under 30% may be replaced by the card's rule (2), never for
its returns, and each replacement is recorded with its reason.

### The check of Monday 2026-10-05

Two runs on the same day, both with the universe's query and the code-only rule:

- **First run, all 251 names** (run 37345386044, 17:02-17:42 UTC). Bright Data throttled the requests all
  through the run: about one first request in two came back as an empty body with its 200, and 29 names had no
  answer even when asked twice. It also showed that 18 names had their ticker as their search name, so they were
  searched as "<ticker> stock" (production's query: "SQM stock" found square-metre property news), not as
  company name plus ticker. Their company names now lead (`"United Parcel Service UPS stock"`).
- **Recheck, 44 names** (run 37351217326, 17:49-17:59 UTC): the 29 with no answer and the 18 renamed (3 were
  both). Asked two at a time, a failed search up to four times. 43 answered; ZTO did not.

**Overall: 75% relevant** (1149 of 1537 headlines, 250 of 251 names; ZTO no answer). The
median name had 6 headlines.

**Under 30% or no headline: 19 names**: OKE (n/a, 0 of 0), APD (17%, 1 of 6), ECL (20%, 2 of 10), GD (20%, 1 of 5), BKNG (20%, 1 of 5), ORLY (25%, 1 of 4), HSY (29%, 2 of 7), INTU (25%, 2 of 8), FOXA (25%, 1 of 4), PEG (17%, 1 of 6), SO (25%, 1 of 4), GSK (29%, 2 of 7), NMR (n/a, 0 of 0), IBN (n/a, 0 of 0), AMX (0%, 0 of 1), CHKP (0%, 0 of 1), ICL (0%, 0 of 1), PKX (n/a, 0 of 0), SHG (n/a, 0 of 0).

**The replacements of 2026-10-02 and 2026-10-03, and the short tickers kept on 2026-10-03:** STT 80% (4 of 5),
IRM 100% (1 of 1), EW 62%, IDXX 100% (1 of 1), MET 71%, MLM 71%, UMC 78%; SO 25%, C 78%, D 75%, T 60%, ED
75%, NOW 44%, V 78%, ICE 70%, O 60%, F 60% (with "<ticker> stock" on 2026-10-03: SO, C, D and MET 0 of 10).

**No name is replaced on this day.** Rule (2) allows a replacement; it does not require one. Most names under
30% had 0 to 7 headlines, and their misses are mostly sector pages and market wraps (Google News filling a quiet
day), not another meaning of the letters; one more headline would move most of them over 30%. The owner decides.

Per name (the recheck's result for the 44 names it asked, the first run's for the others):

| Name | Block | Headlines | Relevant | Share | Run |
| --- | --- | ---: | ---: | ---: | --- |
| BKR | Energy | 7 | 5 | 71% | recheck |
| CNQ | Energy | 10 | 5 | 50% | first |
| COP | Energy | 6 | 5 | 83% | first |
| CVX | Energy | 10 | 10 | 100% | first |
| ENB | Energy | 9 | 7 | 78% | first |
| EOG | Energy | 4 | 3 | 75% | first |
| FANG | Energy | 3 | 1 | 33% | first |
| HAL | Energy | 6 | 2 | 33% | first |
| KMI | Energy | 3 | 2 | 67% | first |
| MPC | Energy | 4 | 4 | 100% | first |
| OKE | Energy | 0 | 0 | n/a | first |
| OXY | Energy | 7 | 5 | 71% | first |
| PSX | Energy | 10 | 8 | 80% | first |
| SLB | Energy | 1 | 1 | 100% | recheck |
| VLO | Energy | 6 | 4 | 67% | first |
| WMB | Energy | 4 | 3 | 75% | first |
| ALB | Materials | 3 | 2 | 67% | first |
| APD | Materials | 6 | 1 | 17% | first |
| CRH | Materials | 7 | 6 | 86% | recheck |
| DD | Materials | 3 | 3 | 100% | first |
| ECL | Materials | 10 | 2 | 20% | first |
| FCX | Materials | 8 | 7 | 88% | first |
| LIN | Materials | 4 | 4 | 100% | first |
| MLM | Materials | 7 | 5 | 71% | first |
| NEM | Materials | 7 | 6 | 86% | first |
| NTR | Materials | 8 | 8 | 100% | first |
| NUE | Materials | 5 | 5 | 100% | first |
| PPG | Materials | 5 | 2 | 40% | first |
| SHW | Materials | 4 | 4 | 100% | first |
| VMC | Materials | 8 | 7 | 88% | first |
| ADP | Industrials | 5 | 4 | 80% | first |
| BA | Industrials | 9 | 7 | 78% | first |
| CMI | Industrials | 6 | 6 | 100% | first |
| CSX | Industrials | 8 | 3 | 38% | recheck |
| DE | Industrials | 6 | 6 | 100% | first |
| EMR | Industrials | 5 | 2 | 40% | first |
| ETN | Industrials | 9 | 7 | 78% | first |
| GD | Industrials | 5 | 1 | 20% | first |
| GE | Industrials | 9 | 5 | 56% | first |
| ITW | Industrials | 8 | 4 | 50% | first |
| JCI | Industrials | 7 | 3 | 43% | first |
| LHX | Industrials | 4 | 4 | 100% | first |
| LMT | Industrials | 4 | 2 | 50% | first |
| MMM | Industrials | 3 | 3 | 100% | recheck |
| NOC | Industrials | 5 | 3 | 60% | first |
| PH | Industrials | 3 | 2 | 67% | first |
| RSG | Industrials | 5 | 4 | 80% | first |
| RTX | Industrials | 10 | 9 | 90% | recheck |
| TT | Industrials | 2 | 2 | 100% | first |
| UNP | Industrials | 6 | 5 | 83% | first |
| UPS | Industrials | 2 | 1 | 50% | recheck |
| WM | Industrials | 6 | 4 | 67% | first |
| ABNB | Consumer discretionary | 5 | 5 | 100% | first |
| AMZN | Consumer discretionary | 9 | 9 | 100% | first |
| AZO | Consumer discretionary | 3 | 2 | 67% | first |
| BKNG | Consumer discretionary | 5 | 1 | 20% | first |
| CMG | Consumer discretionary | 9 | 8 | 89% | first |
| F | Consumer discretionary | 10 | 6 | 60% | first |
| GM | Consumer discretionary | 10 | 7 | 70% | first |
| HD | Consumer discretionary | 9 | 4 | 44% | first |
| HLT | Consumer discretionary | 2 | 1 | 50% | first |
| LOW | Consumer discretionary | 7 | 3 | 43% | first |
| MAR | Consumer discretionary | 6 | 2 | 33% | first |
| MCD | Consumer discretionary | 10 | 9 | 90% | first |
| NKE | Consumer discretionary | 9 | 9 | 100% | first |
| ORLY | Consumer discretionary | 4 | 1 | 25% | first |
| ROST | Consumer discretionary | 5 | 2 | 40% | first |
| SBUX | Consumer discretionary | 10 | 8 | 80% | first |
| TJX | Consumer discretionary | 6 | 5 | 83% | recheck |
| TSLA | Consumer discretionary | 10 | 10 | 100% | first |
| YUM | Consumer discretionary | 2 | 2 | 100% | first |
| ADM | Consumer staples | 6 | 6 | 100% | first |
| CL | Consumer staples | 9 | 6 | 67% | first |
| COST | Consumer staples | 9 | 9 | 100% | first |
| GIS | Consumer staples | 6 | 6 | 100% | first |
| HSY | Consumer staples | 7 | 2 | 29% | first |
| KMB | Consumer staples | 7 | 6 | 86% | first |
| KO | Consumer staples | 10 | 10 | 100% | first |
| KR | Consumer staples | 4 | 4 | 100% | first |
| MDLZ | Consumer staples | 4 | 3 | 75% | first |
| MNST | Consumer staples | 7 | 3 | 43% | first |
| MO | Consumer staples | 3 | 2 | 67% | first |
| PEP | Consumer staples | 10 | 9 | 90% | first |
| PM | Consumer staples | 6 | 4 | 67% | first |
| SYY | Consumer staples | 4 | 2 | 50% | first |
| TGT | Consumer staples | 10 | 4 | 40% | first |
| WMT | Consumer staples | 9 | 9 | 100% | first |
| ABBV | Health care | 3 | 3 | 100% | first |
| ABT | Health care | 7 | 5 | 71% | recheck |
| AMGN | Health care | 5 | 4 | 80% | first |
| BMY | Health care | 7 | 6 | 86% | first |
| BSX | Health care | 5 | 3 | 60% | first |
| CI | Health care | 4 | 3 | 75% | first |
| CVS | Health care | 10 | 8 | 80% | first |
| DHR | Health care | 6 | 6 | 100% | first |
| ELV | Health care | 4 | 3 | 75% | first |
| EW | Health care | 8 | 5 | 62% | first |
| GILD | Health care | 5 | 4 | 80% | first |
| HCA | Health care | 6 | 2 | 33% | first |
| IDXX | Health care | 1 | 1 | 100% | first |
| ISRG | Health care | 6 | 3 | 50% | first |
| MRK | Health care | 10 | 10 | 100% | first |
| PFE | Health care | 5 | 5 | 100% | first |
| REGN | Health care | 3 | 3 | 100% | first |
| SYK | Health care | 5 | 5 | 100% | first |
| TMO | Health care | 8 | 7 | 88% | first |
| UNH | Health care | 9 | 9 | 100% | first |
| VRTX | Health care | 6 | 3 | 50% | first |
| ZTS | Health care | 2 | 1 | 50% | first |
| AIG | Financials | 4 | 2 | 50% | recheck |
| AXP | Financials | 8 | 8 | 100% | first |
| BAC | Financials | 7 | 4 | 57% | first |
| BLK | Financials | 5 | 5 | 100% | first |
| BX | Financials | 8 | 5 | 62% | first |
| C | Financials | 9 | 7 | 78% | first |
| CB | Financials | 7 | 7 | 100% | first |
| CME | Financials | 10 | 8 | 80% | recheck |
| COF | Financials | 8 | 3 | 38% | first |
| GS | Financials | 10 | 5 | 50% | recheck |
| ICE | Financials | 10 | 7 | 70% | first |
| MA | Financials | 10 | 9 | 90% | first |
| MCO | Financials | 3 | 2 | 67% | first |
| MET | Financials | 7 | 5 | 71% | first |
| MS | Financials | 10 | 9 | 90% | first |
| PGR | Financials | 6 | 5 | 83% | first |
| PNC | Financials | 10 | 3 | 30% | recheck |
| PYPL | Financials | 6 | 4 | 67% | first |
| SCHW | Financials | 6 | 5 | 83% | first |
| STT | Financials | 5 | 4 | 80% | first |
| TRV | Financials | 4 | 4 | 100% | first |
| USB | Financials | 4 | 3 | 75% | first |
| V | Financials | 9 | 7 | 78% | first |
| WFC | Financials | 7 | 7 | 100% | first |
| AAPL | Information technology | 10 | 10 | 100% | first |
| ACN | Information technology | 10 | 9 | 90% | first |
| ADBE | Information technology | 9 | 8 | 89% | first |
| ADI | Information technology | 5 | 4 | 80% | first |
| AMAT | Information technology | 6 | 5 | 83% | recheck |
| AMD | Information technology | 9 | 9 | 100% | recheck |
| ANET | Information technology | 6 | 6 | 100% | first |
| AVGO | Information technology | 9 | 8 | 89% | first |
| CDNS | Information technology | 9 | 4 | 44% | first |
| CRM | Information technology | 10 | 8 | 80% | first |
| CSCO | Information technology | 9 | 7 | 78% | first |
| IBM | Information technology | 3 | 3 | 100% | recheck |
| INTC | Information technology | 10 | 10 | 100% | first |
| INTU | Information technology | 8 | 2 | 25% | first |
| KLAC | Information technology | 8 | 4 | 50% | recheck |
| LRCX | Information technology | 6 | 6 | 100% | first |
| MU | Information technology | 10 | 9 | 90% | recheck |
| NOW | Information technology | 9 | 4 | 44% | first |
| ORCL | Information technology | 9 | 9 | 100% | first |
| PANW | Information technology | 8 | 4 | 50% | first |
| QCOM | Information technology | 10 | 10 | 100% | first |
| SNPS | Information technology | 8 | 8 | 100% | recheck |
| TXN | Information technology | 5 | 5 | 100% | first |
| CHTR | Communication services | 8 | 3 | 38% | first |
| CMCSA | Communication services | 8 | 6 | 75% | first |
| DIS | Communication services | 10 | 9 | 90% | first |
| FOXA | Communication services | 4 | 1 | 25% | first |
| LYV | Communication services | 2 | 1 | 50% | first |
| META | Communication services | 8 | 8 | 100% | recheck |
| NFLX | Communication services | 9 | 8 | 89% | first |
| OMC | Communication services | 1 | 1 | 100% | first |
| SPOT | Communication services | 10 | 8 | 80% | first |
| T | Communication services | 10 | 6 | 60% | first |
| TMUS | Communication services | 10 | 6 | 60% | recheck |
| TTWO | Communication services | 7 | 5 | 71% | first |
| VZ | Communication services | 9 | 6 | 67% | first |
| AEP | Utilities | 10 | 7 | 70% | first |
| CEG | Utilities | 6 | 6 | 100% | first |
| D | Utilities | 4 | 3 | 75% | first |
| DUK | Utilities | 7 | 7 | 100% | recheck |
| ED | Utilities | 4 | 3 | 75% | first |
| EXC | Utilities | 2 | 2 | 100% | first |
| NEE | Utilities | 10 | 3 | 30% | recheck |
| PEG | Utilities | 6 | 1 | 17% | first |
| SO | Utilities | 4 | 1 | 25% | first |
| SRE | Utilities | 2 | 2 | 100% | first |
| VST | Utilities | 10 | 10 | 100% | first |
| XEL | Utilities | 2 | 2 | 100% | first |
| AMT | Real estate | 4 | 3 | 75% | first |
| CBRE | Real estate | 6 | 6 | 100% | first |
| CCI | Real estate | 4 | 3 | 75% | first |
| DLR | Real estate | 5 | 3 | 60% | first |
| EQIX | Real estate | 2 | 2 | 100% | first |
| IRM | Real estate | 1 | 1 | 100% | first |
| O | Real estate | 10 | 6 | 60% | first |
| PLD | Real estate | 5 | 4 | 80% | first |
| PSA | Real estate | 2 | 1 | 50% | first |
| SPG | Real estate | 6 | 4 | 67% | first |
| VICI | Real estate | 6 | 6 | 100% | first |
| WELL | Real estate | 4 | 3 | 75% | first |
| AZN | ADR: Europe | 10 | 9 | 90% | first |
| BBVA | ADR: Europe | 6 | 2 | 33% | recheck |
| BP | ADR: Europe | 10 | 9 | 90% | recheck |
| BTI | ADR: Europe | 4 | 3 | 75% | first |
| DEO | ADR: Europe | 1 | 1 | 100% | first |
| GSK | ADR: Europe | 7 | 2 | 29% | recheck |
| HSBC | ADR: Europe | 10 | 8 | 80% | recheck |
| ING | ADR: Europe | 10 | 4 | 40% | first |
| NVS | ADR: Europe | 3 | 3 | 100% | first |
| RIO | ADR: Europe | 10 | 7 | 70% | first |
| SAN | ADR: Europe | 9 | 5 | 56% | first |
| SAP | ADR: Europe | 10 | 6 | 60% | recheck |
| SHEL | ADR: Europe | 10 | 7 | 70% | first |
| SNY | ADR: Europe | 3 | 2 | 67% | first |
| TTE | ADR: Europe | 9 | 4 | 44% | recheck |
| UBS | ADR: Europe | 9 | 9 | 100% | recheck |
| UL | ADR: Europe | 2 | 1 | 50% | first |
| HMC | ADR: Japan | 10 | 10 | 100% | first |
| IX | ADR: Japan | 2 | 2 | 100% | first |
| MFG | ADR: Japan | 1 | 1 | 100% | first |
| MUFG | ADR: Japan | 5 | 5 | 100% | recheck |
| NMR | ADR: Japan | 0 | 0 | n/a | recheck |
| SMFG | ADR: Japan | 3 | 3 | 100% | first |
| SONY | ADR: Japan | 7 | 6 | 86% | first |
| TAK | ADR: Japan | 1 | 1 | 100% | first |
| BABA | ADR: China and Hong Kong | 10 | 9 | 90% | first |
| BEKE | ADR: China and Hong Kong | 3 | 3 | 100% | first |
| BIDU | ADR: China and Hong Kong | 2 | 2 | 100% | first |
| JD | ADR: China and Hong Kong | 7 | 5 | 71% | first |
| NTES | ADR: China and Hong Kong | 2 | 2 | 100% | first |
| PDD | ADR: China and Hong Kong | 2 | 2 | 100% | first |
| TCOM | ADR: China and Hong Kong | 1 | 1 | 100% | first |
| ZTO | ADR: China and Hong Kong | — | — | n/a | recheck |
| IBN | ADR: India | 0 | 0 | n/a | recheck |
| INFY | ADR: India | 6 | 5 | 83% | first |
| MMYT | ADR: India | 1 | 1 | 100% | first |
| RDY | ADR: India | 3 | 3 | 100% | first |
| WIT | ADR: India | 2 | 2 | 100% | first |
| ABEV | ADR: Latin America | 7 | 7 | 100% | first |
| AMX | ADR: Latin America | 1 | 0 | 0% | first |
| BAP | ADR: Latin America | 2 | 2 | 100% | first |
| FMX | ADR: Latin America | 1 | 1 | 100% | first |
| ITUB | ADR: Latin America | 10 | 6 | 60% | recheck |
| NU | ADR: Latin America | 10 | 10 | 100% | first |
| PBR | ADR: Latin America | 10 | 10 | 100% | recheck |
| SQM | ADR: Latin America | 1 | 1 | 100% | recheck |
| VALE | ADR: Latin America | 10 | 3 | 30% | recheck |
| CHKP | ADR: Israel | 1 | 0 | 0% | recheck |
| ICL | ADR: Israel | 1 | 0 | 0% | first |
| MNDY | ADR: Israel | 2 | 1 | 50% | recheck |
| NICE | ADR: Israel | 6 | 5 | 83% | recheck |
| WIX | ADR: Israel | 4 | 4 | 100% | first |
| KB | ADR: Korea and Taiwan | 6 | 3 | 50% | recheck |
| PKX | ADR: Korea and Taiwan | 0 | 0 | n/a | first |
| SHG | ADR: Korea and Taiwan | 0 | 0 | n/a | recheck |
| TSM | ADR: Korea and Taiwan | 10 | 10 | 100% | first |
| UMC | ADR: Korea and Taiwan | 9 | 7 | 78% | first |
| BHP | ADR: Australia | 9 | 5 | 56% | recheck |

## 2. The race's 80 names (a description only)

Run once on 2026-10-03 over the race's journal from 2026-09-23 (the full model's first day) to 2026-10-02
(`python -m analysis.news_relevance`, with `--answered-only` for the first view). **Nothing in production changes
because of it.** A fund's "company name" is its brand as headlines write it (for example "Energy Select Sector"
for XLE, "SPDR Gold" for GLD); a headline about the fund's asset or sector that does not name the fund does not
count. Production asks for "<ticker> ETF" for a fund and "<ticker> stock" for a single name.

**On the lines the model answered** (the news it read; the race's rule: answered and not held):

| Group | Names | Headlines | Relevant | Share | Names under 30% or with none |
| --- | ---: | ---: | ---: | ---: | ---: |
| Single names | 16 | 310 | 229 | 74% | 5 |
| Funds | 64 | 969 | 224 | 23% | 44 |
| **All** | 80 | 1279 | 453 | 35% | 49 |

**On every journalled line** (held lines included: a held name's news is searched and journalled, but no model
is asked; this is the view first reported on 2026-10-03):

| Group | Names | Headlines | Relevant | Share | Names under 30% or with none |
| --- | ---: | ---: | ---: | ---: | ---: |
| Single names | 16 | 1071 | 812 | 76% | 0 |
| Funds | 64 | 1492 | 337 | 23% | 45 |
| **All** | 80 | 2563 | 1149 | 45% | 45 |

What it shows, as a description: the single names' news is mostly about them (74% on the lines the model
answered, 76% on every line). Five single names (MSFT, NVDA, LLY, NVO, TEVA) were held on every line of these
days, so they have no answered line; they count as "with none" in the first view. Most funds' news is about the
market, the sector or other funds, and rarely names the fund (23% in both views); three funds (EWU, EWW, CANE)
had no headline at all on these days. Whether that matters for a fund's score is not tested here.

Per name, on the lines the model answered:

**Overall: 35% relevant** (453 of 1279 headlines, 80 names).

**Under 30% (or no headline): 49 name(s)**: MSFT (n/a), NVDA (n/a), LLY (n/a), NVO (n/a), TEVA (n/a), RSP (n/a), VGK (0%), VWO (29%), SHY (0%), IEF (n/a), TLT (n/a), TIP (n/a), LQD (25%), EMB (n/a), DBC (0%), UUP (n/a), XLF (27%), XLC (22%), SMH (22%), IGV (24%), XLI (4%), ITA (13%), IYT (25%), XLY (n/a), XLU (18%), XLB (10%), VNQ (23%), GDX (26%), EWJ (14%), EWU (n/a), EWL (0%), EWN (0%), EWP (25%), EWD (0%), EWC (20%), EWA (25%), MCHI (0%), EWY (10%), EWT (n/a), EWW (n/a), TUR (25%), EZA (n/a), GLD (n/a), SLV (6%), USO (29%), CORN (0%), WEAT (0%), SOYB (0%), CANE (n/a)

| Name | Headlines | Relevant | Share | By name alone |
| --- | ---: | ---: | ---: | ---: |
| MSFT | 0 | 0 | n/a | n/a |
| NVDA | 0 | 0 | n/a | n/a |
| ASML | 10 | 5 | 50% | 50% |
| GOOGL | 69 | 69 | 100% | 87% |
| JPM | 30 | 28 | 93% | 83% |
| RY | 26 | 21 | 81% | 69% |
| HDB | 10 | 7 | 70% | 70% |
| LLY | 0 | 0 | n/a | n/a |
| NVO | 0 | 0 | n/a | n/a |
| TEVA | 0 | 0 | n/a | n/a |
| CAT | 10 | 3 | 30% | 30% |
| ESLT | 13 | 8 | 62% | 46% |
| TM | 59 | 28 | 47% | 41% |
| MELI | 43 | 34 | 79% | 58% |
| PG | 30 | 18 | 60% | 43% |
| XOM | 10 | 8 | 80% | 60% |
| RSP | 0 | 0 | n/a | n/a |
| IWM | 36 | 13 | 36% | 19% |
| VGK | 15 | 0 | 0% | 0% |
| VWO | 21 | 6 | 29% | 24% |
| SHY | 39 | 0 | 0% | 0% |
| IEF | 0 | 0 | n/a | n/a |
| TLT | 0 | 0 | n/a | n/a |
| TIP | 0 | 0 | n/a | n/a |
| LQD | 16 | 4 | 25% | 12% |
| HYG | 22 | 8 | 36% | 18% |
| EMB | 0 | 0 | n/a | n/a |
| DBC | 1 | 0 | 0% | 0% |
| DBA | 5 | 3 | 60% | 60% |
| UUP | 0 | 0 | n/a | n/a |
| XLE | 39 | 15 | 38% | 21% |
| XLF | 45 | 12 | 27% | 16% |
| KRE | 3 | 1 | 33% | 0% |
| XLV | 48 | 16 | 33% | 23% |
| XBI | 40 | 12 | 30% | 18% |
| XLK | 30 | 9 | 30% | 20% |
| XLC | 23 | 5 | 22% | 9% |
| SMH | 55 | 12 | 22% | 11% |
| IGV | 25 | 6 | 24% | 8% |
| XLI | 57 | 2 | 4% | 0% |
| ITA | 39 | 5 | 13% | 5% |
| IYT | 8 | 2 | 25% | 0% |
| XLY | 0 | 0 | n/a | n/a |
| XLP | 52 | 21 | 40% | 33% |
| XLU | 28 | 5 | 18% | 4% |
| XLB | 30 | 3 | 10% | 3% |
| VNQ | 26 | 6 | 23% | 12% |
| XHB | 9 | 3 | 33% | 11% |
| GDX | 35 | 9 | 26% | 17% |
| EWJ | 14 | 2 | 14% | 0% |
| EIS | 3 | 1 | 33% | 0% |
| EWU | 0 | 0 | n/a | n/a |
| EWG | 2 | 2 | 100% | 0% |
| EWL | 1 | 0 | 0% | 0% |
| EWN | 1 | 0 | 0% | 0% |
| EWI | 3 | 3 | 100% | 33% |
| EWP | 4 | 1 | 25% | 0% |
| EWD | 1 | 0 | 0% | 0% |
| EWC | 5 | 1 | 20% | 0% |
| EWA | 8 | 2 | 25% | 12% |
| MCHI | 13 | 0 | 0% | 0% |
| INDA | 2 | 2 | 100% | 50% |
| EWY | 29 | 3 | 10% | 3% |
| EWT | 0 | 0 | n/a | n/a |
| EWZ | 3 | 2 | 67% | 0% |
| EWW | 0 | 0 | n/a | n/a |
| KSA | 5 | 2 | 40% | 0% |
| TUR | 4 | 1 | 25% | 25% |
| EZA | 0 | 0 | n/a | n/a |
| EPOL | 2 | 1 | 50% | 0% |
| ARGT | 2 | 1 | 50% | 0% |
| GLD | 0 | 0 | n/a | n/a |
| SLV | 53 | 3 | 6% | 2% |
| CPER | 5 | 2 | 40% | 0% |
| USO | 56 | 16 | 29% | 4% |
| UNG | 3 | 1 | 33% | 0% |
| CORN | 1 | 0 | 0% | 0% |
| WEAT | 1 | 0 | 0% | 0% |
| SOYB | 1 | 0 | 0% | 0% |
| CANE | 0 | 0 | n/a | n/a |
