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
the 251 names on a weekday (`.github/workflows/universe-news-check.yml`, about $0.40) and reports the share per
name, the names under 30% and the overall share. A name still under 30% may be replaced by the card's rule (2),
never for its returns, and each replacement is recorded with its reason.

The first run is on the first weekday, Monday 5 Oct 2026. Its results are added here.

## 2. The race's 80 names (a description only)

Run once on 2026-10-03 over the news the model read on every answered line from 2026-09-23 (the full model's
first day) to 2026-10-02: 2563 headlines (`python -m analysis.news_relevance`). **Nothing in production changes
because of it.** A fund's "company name" is its brand as headlines write it (for example "Energy Select
Sector" for XLE, "SPDR Gold" for GLD); a headline about the fund's asset or sector that does not name the fund
does not count. Production asks for "<ticker> ETF" for a fund and "<ticker> stock" for a single name.

| Group | Names | Headlines | Relevant | Share | Names under 30% |
| --- | ---: | ---: | ---: | ---: | ---: |
| Single names | 16 | 1071 | 812 | 76% | 0 |
| Funds | 64 | 1492 | 337 | 23% | 45 |
| **All** | **80** | **2563** | **1149** | **45%** | **45** |

What it shows, as a description: the 16 single names' news is mostly about them (from 46% for TM to 99%).
Most funds' news is about the market, the sector or other funds, and rarely names the fund; three funds (EWU,
EWW, CANE) had no headline at all on these days. Whether that matters for a fund's score is not tested here.

**Overall: 45% relevant** (1149 of 2563 headlines, 80 names).

**Under 30% (or no headline): 45 name(s)**: RSP (27%), VGK (6%), VWO (29%), SHY (2%), IEF (17%), TIP (1%), LQD (25%), HYG (28%), DBC (0%), UUP (20%), XLF (25%), KRE (14%), XBI (26%), XLK (28%), XLC (20%), SMH (20%), XLI (4%), ITA (12%), IYT (22%), XLY (13%), XLU (18%), XLB (10%), VNQ (28%), GDX (27%), EWJ (13%), EIS (25%), EWU (n/a), EWL (0%), EWN (0%), EWP (25%), EWD (0%), EWC (20%), EWA (25%), MCHI (0%), EWY (10%), EWT (9%), EWW (n/a), TUR (25%), EZA (0%), SLV (5%), UNG (20%), CORN (0%), WEAT (0%), SOYB (0%), CANE (n/a)

| Name | Headlines | Relevant | Share | By name alone |
| --- | ---: | ---: | ---: | ---: |
| MSFT | 48 | 45 | 94% | 83% |
| NVDA | 78 | 77 | 99% | 86% |
| ASML | 77 | 53 | 69% | 69% |
| GOOGL | 78 | 77 | 99% | 86% |
| JPM | 79 | 73 | 92% | 77% |
| RY | 69 | 53 | 77% | 68% |
| HDB | 58 | 38 | 66% | 59% |
| LLY | 79 | 72 | 91% | 84% |
| NVO | 80 | 59 | 74% | 54% |
| TEVA | 61 | 43 | 70% | 70% |
| CAT | 78 | 43 | 55% | 47% |
| ESLT | 17 | 9 | 53% | 41% |
| TM | 69 | 32 | 46% | 38% |
| MELI | 43 | 34 | 79% | 58% |
| PG | 79 | 43 | 54% | 47% |
| XOM | 78 | 61 | 78% | 67% |
| RSP | 41 | 11 | 27% | 22% |
| IWM | 41 | 16 | 39% | 22% |
| VGK | 17 | 1 | 6% | 0% |
| VWO | 21 | 6 | 29% | 24% |
| SHY | 43 | 1 | 2% | 2% |
| IEF | 29 | 5 | 17% | 14% |
| TLT | 77 | 27 | 35% | 18% |
| TIP | 80 | 1 | 1% | 0% |
| LQD | 16 | 4 | 25% | 12% |
| HYG | 29 | 8 | 28% | 14% |
| EMB | 5 | 3 | 60% | 20% |
| DBC | 2 | 0 | 0% | 0% |
| DBA | 6 | 3 | 50% | 50% |
| UUP | 5 | 1 | 20% | 20% |
| XLE | 47 | 19 | 40% | 21% |
| XLF | 53 | 13 | 25% | 15% |
| KRE | 7 | 1 | 14% | 0% |
| XLV | 56 | 18 | 32% | 21% |
| XBI | 46 | 12 | 26% | 15% |
| XLK | 39 | 11 | 28% | 21% |
| XLC | 25 | 5 | 20% | 8% |
| SMH | 64 | 13 | 20% | 11% |
| IGV | 31 | 11 | 35% | 13% |
| XLI | 67 | 3 | 4% | 0% |
| ITA | 42 | 5 | 12% | 5% |
| IYT | 9 | 2 | 22% | 0% |
| XLY | 46 | 6 | 13% | 2% |
| XLP | 62 | 23 | 37% | 29% |
| XLU | 28 | 5 | 18% | 4% |
| XLB | 30 | 3 | 10% | 3% |
| VNQ | 29 | 8 | 28% | 14% |
| XHB | 10 | 3 | 30% | 10% |
| GDX | 37 | 10 | 27% | 19% |
| EWJ | 15 | 2 | 13% | 0% |
| EIS | 4 | 1 | 25% | 0% |
| EWU | 0 | 0 | n/a | n/a |
| EWG | 2 | 2 | 100% | 0% |
| EWL | 1 | 0 | 0% | 0% |
| EWN | 1 | 0 | 0% | 0% |
| EWI | 5 | 3 | 60% | 20% |
| EWP | 4 | 1 | 25% | 0% |
| EWD | 2 | 0 | 0% | 0% |
| EWC | 5 | 1 | 20% | 0% |
| EWA | 8 | 2 | 25% | 12% |
| MCHI | 18 | 0 | 0% | 0% |
| INDA | 5 | 3 | 60% | 20% |
| EWY | 31 | 3 | 10% | 3% |
| EWT | 11 | 1 | 9% | 0% |
| EWZ | 5 | 2 | 40% | 0% |
| EWW | 0 | 0 | n/a | n/a |
| KSA | 5 | 2 | 40% | 0% |
| TUR | 8 | 2 | 25% | 12% |
| EZA | 1 | 0 | 0% | 0% |
| EPOL | 2 | 1 | 50% | 0% |
| ARGT | 2 | 1 | 50% | 0% |
| GLD | 72 | 25 | 35% | 18% |
| SLV | 63 | 3 | 5% | 2% |
| CPER | 5 | 2 | 40% | 0% |
| USO | 66 | 21 | 32% | 8% |
| UNG | 5 | 1 | 20% | 0% |
| CORN | 2 | 0 | 0% | 0% |
| WEAT | 2 | 0 | 0% | 0% |
| SOYB | 2 | 0 | 0% | 0% |
| CANE | 0 | 0 | n/a | n/a |
