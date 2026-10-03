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
