# Daily report

**28 Oct 2026, 18:01 Israel time (16:01 UTC)** · 80 names checked · 0 traded · 3 with a problem

**Answers with no explanation:** 10 of 63 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 6 | 10 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 38 | 3 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Corn (CORN) · Commodity | **Stop raised.** At +0.04R, following the price. Stop-loss raised 18.02 → 17.97. |
| Brazil (EWZ) · Sector or country | **Stop raised.** At -0.01R, following the price. Stop-loss raised 36.81 → 36.67. |
| US company bonds, riskier (HYG) · Index fund | **Stop raised.** At +0.79R, following the price. Stop-loss raised 76.76 → 77.03. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.23R, following the price. Stop-loss raised 323.76 → 325.57. |
| Royal Bank of Canada (RY) · Company | **Stop raised.** At +1.09R, following the price. Stop-loss raised 196.13 → 196.58. |
| US materials and chemicals (XLB) · Sector or country | **Stop raised.** At +0.39R, following the price. Stop-loss raised 50.13 → 50.20. |
| US health care (XLV) · Sector or country | **Stop raised.** At +0.30R, following the price. Stop-loss raised 173.68 → 175.22. |
| ASML (ASML) · Company | **Holding.** -0.08R, holding 3 shares. Stop-loss 1684.98. |
| Gold mining companies (GDX) · Sector or country | **Holding.** -0.13R, holding 84 shares. Stop-loss 77.13. |
| Gold (GLD) · Commodity | **Holding.** +1.22R, holding 7 shares. Stop-loss 378.03. |
| Eli Lilly (LLY) · Company | **Holding.** +2.38R, holding 3 shares. Stop-loss 1233.74. |
| Microsoft (MSFT) · Company | **Holding.** -0.12R, holding 9 shares. Stop-loss 511.25. |
| Nvidia (NVDA) · Company | **Holding.** -0.06R, holding 23 shares. Stop-loss 225.68. |
| Exxon Mobil (XOM) · Company | **Holding.** +2.68R, holding 9 shares. Stop-loss 174.71. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Novo Nordisk (NVO) · Company — BEARISH, confidence 0.85

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Negative competitor trial news, bearish technicals, weak earnings record, and recent analyst downgrades outweigh strong profitability and low valuation.

**Main reasons it gave:**
- Eli Lilly's retatrutide outperformed Novo's Ozempic in head-to-head Phase 3 trial
- NVO price below 50‑day and 200‑day SMA with low volume
- Revenue growth +2.1% YoY but earnings down 20.6% YoY
- Earnings record: 2 misses, 1 beat, 1 in line over last 4 quarters
- Analyst consensus hold with recent downgrades from Morgan Stanley and Goldman Sachs

<details><summary><b>News</b> — score -0.70</summary>

- [Novo Nordisk (NVO) Stock Declines While Market Improves: Some Information for Investors](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nvo-stock-declines-204503176.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Novo Nordisk (NVO) closed the most recent trading day at $38.70, moving -1.11% from the previous trading session. The stock fell short of the S&P 500,...
- [LLY Vs NVO: Lilly’s Retatrutide Beats Novo’s Ozempic In Head-To-Head Trial — Retatrutide More Than Doubles Weight Loss](https://stocktwits.com/news-articles/markets/equity/lly-nvo-retatrutide-beats-ozempic-in-head-to-head-trial/cZU9h53R9GR)  
  <sub>Stocktwits, 2 hours ago</sub>  
  Retatrutide helped patients with type 2 diabetes lose an average of 44 to 47 pounds over 80 weeks, compared with about 21 pounds for Ozempic.
- [Lilly's retatrutide beats Ozempic in Phase 3 trial (LLY:NYSE)](https://seekingalpha.com/news/4658788-lillys-retatrutide-beats-ozempic-phase-3-trial)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Eli Lilly (LLY) says next-gen weight loss drug, retatrutide beat Ozempic on weight loss and A1C reduction in a head-to-head Phase 3 trial for diabetes.
- [Can Novo Nordisk (NYSE:NVO) Support A Reasonable Price On Earnings?](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-nvo/novo-nordisk/news/can-novo-nordisk-nysenvo-support-a-reasonable-price-on-earni/amp)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  Novo Nordisk has been in the spotlight for its obesity treatments, yet the share price slide over the past few years raises a basic question for holders and...
- [Amgen vs. Novo Nordisk: Which Healthcare Giant's Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/27/amgen-vs-novo-nordisk-which-healthcare-giant-s-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  Amgen's 9.9% revenue growth outpaces Novo Nordisk, but a 33.1% net margin and lower valuation multiples tell a different profitability story.
- [Novo Nordisk Vs. Eli Lilly Q3 Preview: I'd (Now) Buy Both, But Lilly Is My Top Pick (NVO)](https://seekingalpha.com/article/4958217-novo-nordisk-vs-eli-lilly-q3-preview-id-now-buy-both-but-lilly-is-my-top-pick)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Eli Lilly and Company has decisively outpaced Novo Nordisk A/S in the GLP-1/obesity/T2D market, now commanding a $1.21T valuation. NVO's share price has...
- [NVO Sep 2027 20.000 put (NVO270917P00020000) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/NVO270917P00020000/)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>  
  Find the latest NVO Sep 2027 20.000 put (NVO270917P00020000) stock quote, history, news and other vital information to help you with your stock trading and...
- [GE Vernova To Acquire Trench Group For $9B, Raises 2026 Guidance After Q3 Revenue Beat — What Investors Need To Know](https://stocktwits.com/news-articles/markets/equity/ge-vernova-to-acquire-trench-group-for-9-b-raises-2026-guidance-after-q3-revenue-beat-what-investors-need-to-know/cZU9hqqR9Gc)  
  <sub>Stocktwits, 11 hours ago</sub>  
  GE Vernova (GEV) is in focus on Wednesday after announcing a $9 billion agreement to acquire Trench Group from Triton Partners and raising its 2026...
- [NVO261030C00038500 interactive stock chart | NVO Oct 2026 38.500 call stock - Yahoo Finance](https://sg.finance.yahoo.com/chart/NVO261030C00038500)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Tibooburra Project Update: RC drilling to commence as Novo forms unincorporated Joint Venture with Manhattan Gold](https://markets.businessinsider.com/news/stocks/tibooburra-project-update-rc-drilling-to-commence-as-novo-forms-unincorporated-joint-venture-with-manhattan-gold-1036672877)  
  <sub>markets.businessinsider.com, 18 hours ago</sub>  
  HIGHLIGHTS Novo has now received all regulatory and land holder approvals required to commence a ~2700 m RC program at Tibooburra, NSW, with dril...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 38.51 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 38.47 (+0.1%), 50d 41.51 (-7.2%), 200d 44.39 (-13.2%); 50d below 200d
Momentum: RSI(14) 42.1 | MACD -0.567 vs signal -0.828 (histogram 0.261)
Returns: 1d -0.4% | 5d -1.4% | 1m +0.5% | 3m -25.4%
52-week range: 35.29 - 63.98 (now 11.2% of the way up)
Volatility: ATR(14) 0.80 (2.1% of price) | annualised 20d 19.8%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 169.88B
Valuation: trailing P/E 9.42 | forward P/E 11.20 | P/B 5.13 | PEG 4.37
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.2% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score -0.10</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 44.85 (+16.4% vs last close), range 39.53 - 61.45
Recent rating changes:
  - 2026-10-12 BMO Capital: main, Market Perform -> Market Perform
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
Institutional ownership: 9.8%
Largest holders: Dodge & Cox Inc. (0.6%), LOOMIS SAYLES & CO L P (0.5%), Franklin Resources, Inc. (0.4%), Price (T.Rowe) Associates Inc (0.3%), Morgan Stanley (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 132,841 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — BULLISH, confidence 0.68

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The acquisition of BioXcel's BXCL501 provides a material, ticker‑specific catalyst, reinforced by a strong analyst consensus (mean price target +18% vs current price) and a solid earnings record (3 beats, 1 miss). Fundamentals are mixed (high forward P/E suggests cheap valuation but debt is high) and technicals show slight bearish momentum (MACD below signal, low volume), tempering conviction but not overturning the bullish case.

**Main reasons it gave:**
- Teva announced acquisition of BioXcel's BXCL501, under FDA review for at‑home agitation use
- Analyst consensus strong buy with mean price target 18% above current price
- Earnings record shows 3 beats and 1 miss, recent beats of 9%, 39%, and 17%
- Forward P/E 13.04 suggests cheap valuation relative to earnings expectations
- Technical indicators show slight bearish momentum (MACD below signal, low volume)

<details><summary><b>News</b> — score +0.45</summary>

- [Teva Pharmaceutical Industries Limited (TEVA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) · -0.57% · 3.88% · 27.74% · 29.41% · 104.20% · 362.66% · 4,356.83%. Key Events. Baseline. Advanced Chart. Loading...
- [Teva Pharmaceutical Industries Limited (TEVA) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/TEVA/)  
  <sub>Yahoo Finance Singapore, 14 hours ago</sub>  
  Teva Pharmaceutical Industries Limited (TEVA) · -0.57% · 3.88% · 27.74% · 29.41% · 104.20% · 362.66% · 4,356.83%. Key events. Baseline. Advanced chart. Loading...
- [Roundup: Teva Acquires BXCL501 for $57.5 Million Upfront, Rumi Therapeutics Enters Option Agreement for Fragile X PDE2 Inhibitor From Enthorin](https://www.pharmexec.com/view/teva-acquires-bxcl501-bioxcel-rumi-therapeutics-option-enthorin-fragile-x-pde2-inhibitor)  
  <sub>Pharmaceutical Executive, 23 hours ago</sub>  
  Teva acquires BioXcel's BXCL501, under FDA review for at-home agitation use; Rumi Therapeutics gains an option on Enthorin's Fragile X PDE2 inhibitor.
- [US estrogen supply crunch widens as women seek alternatives to scarce patches By Reuters](https://www.investing.com/news/stock-market-news/us-estrogen-supply-crunch-widens-as-women-seek-alternatives-to-scarce-patches-4978221)  
  <sub>Investing.com, 4 hours ago</sub>  
  By Mrinalika Roy. Oct 28 (Reuters) - Women in the US struggling to find hormone replacement treatments to manage menopause symptoms are facing shortages...
- [Samsung Biologics Epix: Solid Similar Performance… On Track for Leap to 'World-Class' Status](https://www.mt.co.kr/en/thebio/2026/10/28/2026102816024799659)  
  <sub>머니투데이, 7 hours ago</sub>  
  (Initial Report) Q3 Revenue 442.2 Billion Won, Operating Profit 132.6 Billion Won Solidifying Growth Through Expanded Global Product Sales
- [Teva Pharmaceutical Industries (TEVA) Stock Forecasts](https://finance.yahoo.com/research/reports/MS_0P0000JFMH_AnalystReport_1793116529000)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Sanofi (SAN.PA) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/SAN.PA/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest Sanofi (SAN.PA) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Sector Update: Healthcare Stocks Decline Tuesday Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-decline-tuesday-175850788.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Healthcare stocks were lower Tuesday afternoon, with the NYSE Healthcare Index and the State Street Health Care Select Sector SPDR ETF (XLV) each down about...
- [TEVA Oct 2026 44.500 call (TEVA261030C00044500) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/TEVA261030C00044500/)  
  <sub>Yahoo Finance Singapore, 11 hours ago</sub>  
  Find the latest TEVA Oct 2026 44.500 call (TEVA261030C00044500) stock quote, history, news and other vital information to help you with your stock trading...
- [TEVA Oct 2026 33.000 call (TEVA261030C00033000) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/TEVA261030C00033000/)  
  <sub>Yahoo Finance Singapore, 13 hours ago</sub>  
  Find the latest TEVA Oct 2026 33.000 call (TEVA261030C00033000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 40.28 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 40.30 (-0.0%), 50d 38.91 (+3.5%), 200d 34.49 (+16.8%); 50d above 200d
Momentum: RSI(14) 53.4 | MACD 0.406 vs signal 0.595 (histogram -0.188)
Returns: 1d -0.3% | 5d -0.8% | 1m +1.2% | 3m +13.8%
52-week range: 19.78 - 41.50 (now 94.4% of the way up)
Volatility: ATR(14) 1.10 (2.7% of price) | annualised 20d 22.5%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.98B
Valuation: trailing P/E 67.13 | forward P/E 13.04 | P/B 6.05 | PEG 0.71
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.4% of float
Next earnings: 2026-11-03
```

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39% | 2025-09-30 beat by 17%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.75</summary>

```text
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 47.58 (+18.1% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-15 Barclays: main, Overweight -> Overweight
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
Institutional ownership: 29.2%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.75</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.3% of insider holdings) | insiders hold 6,525,658 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-18 SAVAGE BRIAN (Officer): 7,342 shares, 285.21K
  - 2026-09-18 MIGNONE ROBERTO A. (Director): 367,600 shares, 14.36M
  - 2026-08-21 WEISS AMIR (Officer): 9,445 shares, 355.30K
  - 2026-08-03 JOVER PLACID (Officer): 12,827 shares, 447.35K
(13 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The company shows strong earnings momentum (4 straight beats) and positive news on order backlog and raised earnings expectations, supported by recent ETF buying and solid fundamentals (high growth, high ROE). Technicals are bearish (price below SMAs, low volume) and insider activity is slightly negative (more sellers than buyers), but the bullish fundamentals and earnings record outweigh the technical and insider signals, leading to an overall bullish view with moderate conviction.

**Main reasons it gave:**
- Four consecutive earnings beats (8%–31% above consensus)
- Order backlog highlighted in news, indicating revenue visibility
- ETF net buying of $18.5M on Oct 26
- Strong fundamentals: 24% YoY revenue growth, 68% YoY earnings growth, ROE 57%

<details><summary><b>News</b> — score +0.30</summary>

- [Caterpillar earnings: what to look for from CAT](https://finance.yahoo.com/markets/stocks/articles/caterpillar-earnings-look-cat-091834278.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Construction equipment company Caterpillar (NYSE:CAT) will be announcing earnings results this Thursday before market open. Here's what to expect.
- [Red Cat: Interesting Acquisition, But Execution Remains The Focus (NASDAQ:RCAT)](https://seekingalpha.com/article/4958541-red-cat-interesting-acquisition-but-execution-remains-the-focus)  
  <sub>Seeking Alpha, 19 minutes ago</sub>  
  Red Cat's Steyr Motors deal could boost defense manufacturing and revenue, but cash burn and order visibility pose risks. Click for more on RCAT stock.
- [How To Earn $500 A Month From Caterpillar Stock Ahead Of Q3 Earnings](https://www.benzinga.com/trading-ideas/dividends/26/10/62650102/how-to-earn-500-a-month-from-caterpillar-stock-ahead-of-q3-earnings)  
  <sub>Benzinga, 3 hours ago</sub>  
  Caterpillar has an annual dividend yield of 0.91%, with a quarterly dividend of $1.63 per share. To earn $500 monthly, here's what you do.
- [Drone Stocks Rally as High-Beta Small Caps Lead: Red Cat Jumps 10%, Ondas Climbs 8%, AeroVironment Ticks Up](https://247wallst.com/investing/2026/10/27/drone-stocks-rally-as-high-beta-small-caps-lead-red-cat-jumps-10-ondas-climbs-8-aerovironment-ticks-up/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Small-cap drone names are surging while the sector's established defense player barely budges, and the gap between them reveals exactly where traders are...
- [ETFs Bought $18.5 Million of Caterpillar (CAT) on Oct. 26](https://finance.yahoo.com/markets/stocks/articles/etfs-bought-18-5-million-110130598.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. In Monday's session, 22 ETFs were buying Caterpillar (CAT) shares versus 15 selling, for net ETF buying of $18.5...
- [Caterpillar Inc (CAT) Shares Surge 3.1% -- What GF Score of 91 T](https://www.gurufocus.com/news/9145619/caterpillar-inc-cat-shares-surge-31-what-gf-score-of-91-tells-investors)  
  <sub>GuruFocus, 16 hours ago</sub>  
  On October 27, 2026, Caterpillar Inc (CAT) shares rose 3.1% today, closing at $713.31. The stock has experienced a 52-week trading range of $521.43 to...
- [Caterpillar Inc Stock (CAT) Moved Up by 3.02% on Oct 27: Key Drivers Unveiled](https://www.tradingkey.com/news/market-movers/262242974-market-movers-cat-20261027)  
  <sub>TradingKey, 19 hours ago</sub>  
  Caterpillar shares advanced with high volatility ahead of third-quarter earnings.Record order backlog supports revenue visibility across multiple operating...
- [Red Cat xStock Price | RCATx Price Today, Live Chart, USD converter, Market Capitalization](https://cryptorank.io/price/red-cat-tokenized-stock-xstock)  
  <sub>CryptoRank, 6 hours ago</sub>  
  Red Cat xStock is a tokenized stock issued by Backed as part of the xStocks ecosystem. The token is backed 1:1 by the corresponding underlying stock,...
- [Caterpillar (CAT) CEO gets 23 stock-linked units, payable in cash on retirement or separation from service.](https://www.stocktitan.net/sec-filings/CAT/form-4-caterpillar-inc-insider-trading-activity-83f41d286cf4.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Caterpillar Inc. (CAT) CEO Joseph E. Creed acquired 23 Phantom Stock Units on October 26, 2026, as an award. The reported total included 12 units credited...
- [Caterpillar (CAT) Could Be 23% Undervalued After Raised Earnings Views](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/caterpillar-cat-could-be-23-undervalued-after-raised-earning)  
  <sub>Simply Wall Street, 12 hours ago</sub>  
  Wall Street's reset on earnings expectations has pushed Caterpillar (CAT) into focus, as investors weigh higher profit forecasts against fresh manufacturing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 709.22 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 763.92 (-7.2%), 50d 790.45 (-10.3%), 200d 809.91 (-12.4%); 50d below 200d
Momentum: RSI(14) 35.5 | MACD -30.196 vs signal -25.003 (histogram -5.193)
Returns: 1d -0.6% | 5d -4.2% | 1m -14.2% | 3m -12.3%
52-week range: 524.47 - 1,064.90 (now 34.2% of the way up)
Volatility: ATR(14) 26.25 (3.7% of price) | annualised 20d 38.4%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 326.01B
Valuation: trailing P/E 30.53 | forward P/E 21.77 | P/B 16.81 | PEG 1.20
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.00 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 15 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 926.91 (+30.7% vs last close), range 575.00 - 1,150.00
Recent rating changes:
  - 2026-10-26 UBS: main, Neutral -> Neutral
  - 2026-10-26 Wells Fargo: main, Overweight -> Overweight
  - 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - 2026-10-12 Citigroup: main, Buy -> Buy
  - 2026-10-05 Truist Securities: main, Buy -> Buy
  - 2026-09-10 Freedom Broker: up, Hold -> Buy
Institutional ownership: 73.5%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.5%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

```text
Last 180 days: bought 169,246 shares in 20 transaction(s) | sold 128,174 shares in 10
Net: +41,072 shares (+4.2% of insider holdings) | insiders hold 1,006,687 shares
Distinct insiders: 1 buying, 8 selling
Open-market purchases — insiders spending their own money:
  - 2026-05-04 MACLENNAN DAVID W (Director): 250 shares, 219.21K
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-28 CREED JOSEPH E (Chief Executive Officer): 32,401 shares, 26.21M
  - 2026-05-14 JOHNSON DENISE C. (Officer): 12,605 shares, 11.44M
  - 2026-05-13 SCHAUPP WILLIAM E (Officer): 360 shares, 326.16K
  - 2026-05-13 JOHNSON DENISE C. (Officer): 6,196 shares, 5.64M
(19 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

_Not available today._

</details>

### HDFC Bank (HDB) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The appointment of a new CEO provides a material catalyst, while technicals are bearish, but strong analyst consensus and solid fundamentals tilt the view toward a modest upside.

**Main reasons it gave:**
- New CEO Anup Bagchi appointed, indicating leadership transition
- Technical indicators show price below 20‑day, 50‑day, 200‑day SMAs and RSI 38.9 (bearish momentum)
- Analyst consensus is buy with mean price target $30.30 (+40.7% upside)
- Fundamentals: trailing P/E 13.89 and revenue growth +80.8% YoY

<details><summary><b>News</b> — score +0.00</summary>

- [A new CEO takes charge at HDFC Bank (HDB) after Sashidhar Jagdishan completes his tenure.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-480f55482027.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  HDFC Bank Limited (HDB) reported that Sashidhar Jagdishan vacated the office of Managing Director and Chief Executive Officer at the close of business on...
- [VN-Index ticks up as banking stocks support market](https://vietnamnews.vn/economy/1803085/vn-index-ticks-up-as-banking-stocks-support-market.html)  
  <sub>vietnamnews.vn, 4 hours ago</sub>  
  Banking stocks provided the main support for the benchmark, although gains were not evenly distributed across the sector.
- [TCB shares attract strong foreign investment.](https://www.vietnam.vn/en/co-phieu-tcb-hut-manh-dong-tien-ngoai)  
  <sub>Vietnam.vn, 9 hours ago</sub>  
  During the morning trading session on October 28th, foreign investors continued to heavily invest in TCB shares.
- [CONSTRUCTION STOCKS: UOB KH Sees Buying Opportunities After 2026 Sell-Down](https://nextinsight.net/story-archive-mainmenu-60/949-2026/16941-construction-stocks-uob-kh-sees-buying-opportunities-after-2026-sell-down)  
  <sub>NextInsight, 17 hours ago</sub>  
  Many Singapore construction-related stocks have come under pressure in 2026, especially after strong gains in 2025. UOB Kay Hian says the sell-down looks...
- [Jio IPO listing: How LIC, Reliance Power, NSE, LG, Hyundai, Paytm fared on debut day](https://www.businesstoday.in/markets/stocks/story/jio-ipo-listing-how-lic-reliance-power-nse-lg-hyundai-paytm-fared-on-debut-days-564131-2026-10-28)  
  <sub>Business Today, 12 hours ago</sub>  
  Among past big IPOs, LG Electronics India Ltd delivered the highest listing-day return of 48.24 per cent, data compiled by Bloomberg suggested.
- [Anup Bagchi takes charge as CEO. HDFC Bank stock costs EUR 19.35](https://www.ad-hoc-news.de/boerse/news/corporate-news/anup-bagchi-takes-charge-as-ceo-hdfc-bank-stock-costs-eur-19-35/70421116)  
  <sub>ad-hoc-news.de, 24 hours ago</sub>  
  Anup Bagchi takes charge on October 27, 2026 after Q2 profit rose 4.70 percent. HDFC Bank stock costs EUR 19.35 on October 27, 2026 in Germany.
- [S’porean father joins migrant workers for lunch at HDB void deck, gets to know them personally](https://mustsharenews.com/singaporean-migrant-workers-lunch/amp/)  
  <sub>Must Share News, 13 hours ago</sub>

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 21.53 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 22.48 (-4.2%), 50d 22.75 (-5.3%), 200d 25.92 (-16.9%); 50d below 200d
Momentum: RSI(14) 38.9 | MACD -0.265 vs signal -0.122 (histogram -0.143)
Returns: 1d +0.8% | 5d -5.0% | 1m -4.9% | 3m -10.8%
52-week range: 21.36 - 37.13 (now 1.1% of the way up)
Volatility: ATR(14) 0.52 (2.4% of price) | annualised 20d 29.0%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 110.74B
Valuation: trailing P/E 13.89 | forward P/E 15.59 | P/B 8.57 | PEG n/a
Profitability: profit margin 26.5% | operating margin 38.5% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.8% of float
Next earnings: 2027-01-16
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.30 (+40.7% vs last close), range 26.20 - 33.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 13.8%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), Schroder Investment Management Group (0.4%), JPMORGAN CHASE & CO (0.4%), Bank of America Corporation (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 0 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Mixed but overall positive: recent earnings lift shares 5.6%, RBC reaffirmed Outperform rating, insiders net bought ~5% of holdings, price remains above key moving averages with modest momentum. Fundamentals are solid but valuation is high, and analyst consensus is already priced in, tempering conviction.

**Main reasons it gave:**
- Shares rose 5.6% after latest quarter results (Trefis)
- RBC reaffirmed "outperform" rating with $166 price target (MarketBeat)
- Insiders net bought 99,030 shares (+4.8% of holdings) (Insider Activity)
- Price above 20‑day, 50‑day, 200‑day SMAs; RSI 59.7, MACD positive (Technical)
- Habitat Care realignment raises profit‑transparency concerns (Globe and Mail)

<details><summary><b>News</b> — score +0.15</summary>

- [What Did Procter & Gamble’s Latest Quarter Change For Its Stock?](https://www.trefis.com/stock/pg/articles/620996/what-did-procter-gambles-latest-quarter-change-for-its-stock/2026-10-28)  
  <sub>Trefis, 7 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com.Shares of Procter & Gamble (PG) rose 5.6% on October 22, 2026,...
- [PG Nov 2026 155.000 call (PG261127C00155000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261127C00155000/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest PG Nov 2026 155.000 call (PG261127C00155000) stock quote, history, news and other vital information to help you with your stock trading and...
- [P&G’s Habitat Care Realignment Raises Questions on Segment Comparability and Profit Transparency](https://www.theglobeandmail.com/investing/markets/stocks/PG/pressreleases/8492904/pgs-habitat-care-realignment-raises-questions-on-segment-comparability-and-profit-transparency/)  
  <sub>The Globe and Mail, 9 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.
- [PG Electroplast Beats Q2 Estimates Despite Margin Pressure; Shares Rally 6%](https://www.tradingview.com/news/moodys:912c08c2675f5:0-pg-electroplast-beats-q2-estimates-despite-margin-pressure-shares-rally-6/)  
  <sub>TradingView, 3 hours ago</sub>  
  The EBITDA margin expands to 7.4 per cent from 6.8 per cent in the corresponding quarter last year, beating analysts' expectations of 5.6 per centShares of...
- [Procter & Gamble (NYSE:PG) Stock Keeps "Outperform" Rating at Royal Bank Of Canada](https://www.marketbeat.com/instant-alerts/analyst-procter-gambles-pg-outperform-rating-reiterated-at-royal-bank-of-canada-2026-10-20/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Royal Bank Of Canada reiterated an "outperform" rating and issued a $166.00 price target on shares of Procter & Gamble in a research note on Tuesday.
- [Here's How Many Shares of Procter & Gamble It Would Take to Fund an Annual $3,000 Vacation From Dividends](https://finance.yahoo.com/markets/stocks/articles/heres-many-shares-procter-gamble-014400957.html)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  If you're planning a $3,000 annual vacation and want to pay for it with dividends from Procter & Gamble (NYSE: PG) shares, you'll have to put in a...
- [CDs or Dividend Stocks: Which Pays Retirees Better Right Now?](https://247wallst.com/investing/2026/10/27/cds-or-dividend-stocks-which-pays-retirees-better-right-now/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Johnson & Johnson, Procter & Gamble, and Coca-Cola all beat the national CD average on yield, but the real comparison has nothing to do with today's rate...
- [One Unsettled Question Sits Under Procter & Gamble Stock](https://www.trefis.com/stock/pg/articles/620786/one-unsettled-question-sits-under-procter-gamble-stock/2026-10-27)  
  <sub>Trefis, 22 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Procter & Gamble (PG) kept its forecast for fiscal 2027 earnings unchanged...
- [The View | Chef Ayesha Nurdjaja shares Mediterranean-inspired recipes from her new cookbook](https://abc.com/video/0d6c5542-7734-4508-bfe0-a5fc8073541f/playlist/pl551344809)  
  <sub>ABC Network, 14 hours ago</sub>  
  Watch The View: The chef behind New York City restaurants Shuka and Shukette joins 'The View' to share how her roots influenced her dishes featured in...
- [Procter & Gamble CEO Shailesh Jejurikar sells $5.7M in shares By Investing.com](https://za.investing.com/news/stock-market-news/procter--gamble-ceo-shailesh-jejurikar-sells-57m-in-shares-93CH-4526883)  
  <sub>Investing.com South Africa, 19 hours ago</sub>  
  Shailesh Jejurikar, Chairman, President and CEO of Procter & Gamble Co. (NYSE:PG), sold shares of the company's common stock on October 23, 2026,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 159.15 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 154.54 (+3.0%), 50d 149.31 (+6.6%), 200d 148.77 (+7.0%); 50d above 200d
Momentum: RSI(14) 59.7 | MACD 3.516 vs signal 3.258 (histogram 0.258)
Returns: 1d -0.1% | 5d +1.5% | 1m +7.3% | 3m +10.6%
52-week range: 138.04 - 167.20 (now 72.4% of the way up)
Volatility: ATR(14) 2.95 (1.9% of price) | annualised 20d 27.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 368.88B
Valuation: trailing P/E 23.97 | forward P/E 21.50 | P/B 6.79 | PEG 4.11
Profitability: profit margin 18.2% | operating margin 27.1% | ROE 29.6%
Growth (YoY): revenue +4.0% | earnings +0.8%
Balance sheet: debt/equity 70.3% | free cash flow 12.66B
Risk: beta 0.38 | short interest 0.9% of float
Next earnings: 2027-01-21
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 in line
  2026-09-30 beat by 3% | 2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: buy (mean 2.08 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 9 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 173.30 (+8.9% vs last close), range 143.00 - 190.00
Recent rating changes:
  - 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-10-26 Piper Sandler: main, Neutral -> Neutral
  - 2026-10-23 Freedom Broker: up, Hold -> Buy
  - 2026-10-23 UBS: main, Buy -> Buy
  - 2026-10-23 Citigroup: main, Buy -> Buy
  - 2026-10-23 BNP Paribas: main, Outperform -> Outperform
Institutional ownership: 71.9%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

```text
Last 180 days: bought 191,293 shares in 43 transaction(s) | sold 92,263 shares in 19
Net: +99,030 shares (+4.8% of insider holdings) | insiders hold 2,132,360 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-23 PURUSHOTHAMAN BALAJI (Officer): 4,181 shares, 671.93K
  - 2026-10-23 GAMA PAUL (Officer): 4,331 shares, 698.46K
  - 2026-10-23 JEJURIKAR SHAILESH (Chief Executive Officer): 35,000 shares, 5.71M
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
(41 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

_Not available today._

</details>

### Toyota (TM) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Toyota showcased Crown Signia GT-S Concept at SEMA (new product showcase)
- Price above 20‑day and 50‑day SMA, MACD positive (technical slight bullish)
- Trailing P/E 8.51 and forward P/E 12.27 indicate cheap valuation
- Analyst price target 20.9% above current price (upside potential)
- Four consecutive earnings beats (strong earnings record)

<details><summary><b>News</b> — score +0.10</summary>

- [Toyota's SUV concept sits nearly five inches lower than the stock model](https://www.stocktitan.net/news/TM/toyota-reimagines-crown-signia-as-gt-s-performance-concept-for-5nvhpoxmvn0w.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Toyota (TM) showcased the Crown Signia GT-S Concept, a modified grand touring prototype, at the 2026 SEMA show. Built by Toyota Motorsports Garage from the...
- [The Zacks Analyst Blog Highlights Alphabet, ExxonMobil, Toyota, Waterstone Financial and AXIL Brands](https://finance.yahoo.com/markets/stocks/articles/zacks-analyst-blog-highlights-alphabet-073900537.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Chicago, IL – October 28, 2026 – Zacks.com announces the list of stocks featured in the Analyst Blog. Every day the Zacks Equity Research analysts discuss...
- [Form 4 TOYOTA MOTOR CORP/: Takefumi Shiga (Operating Officer) For: 23 October](https://uk.investing.com/news/stock-market-news/form-4-toyota-motor-corp-takefumi-shiga-operating-officer-for-23-october-93CH-4937337)  
  <sub>Investing.com UK, 3 hours ago</sub>  
  FORM 4, UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549. STATEMENT OF CHANGES IN BENEFICIAL OWNERSHIP
- [LASE Introduces Quantum Bullet(TM) Anti-Drone Platform at I/ITSEC Conference in November 2026](https://finance.yahoo.com/technology/articles/lase-introduces-quantum-bullet-tm-123100314.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Modular Directed-Energy Platform Designed for Easily Deployable Defense Against Group 1 and Group 2 Drone ThreatsORLANDO, FL / ACCESS Newswire / October 28,...
- [Which Small-Cap Value ETF Is the Better Buy: iShares’ ISCV or State Street’s SLYV?](https://www.fool.com/coverage/etfs/2026/10/27/which-small-cap-value-etf-is-the-better-buy-ishares-iscv-or-state-street-s-slyv/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  The case for ISCV is lower fees and broader diversification. The case for SLYV is that it only owns companies that are actually making money.
- [PayPal's Q3 Earnings Beat Estimates on Venmo Growth, TPV Rises](https://www.tradingview.com/news/zacks:7704d57d0094b:0-paypal-s-q3-earnings-beat-estimates-on-venmo-growth-tpv-rises/)  
  <sub>TradingView, 22 hours ago</sub>  
  PayPal Holdings, Inc. PYPL reported third-quarter 2026 non-GAAP earnings per share (EPS) of $1.45, beating the Zacks Consensus Estimate of $1.31 by 10.7%.
- [General Motors Rises 5% on Nasdaq Listing Move and Index Eligibility; Tesla Gains 3%, Ford Edges Higher](https://247wallst.com/investing/2026/10/27/general-motors-rises-5-on-nasdaq-listing-move-and-index-eligibility-tesla-gains-3-ford-edges-higher/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  General Motors is abandoning its historic home on the New York Stock Exchange for a move that has nothing to do with cars and everything to do with which...
- [Toyota unveils Crown Signia GT-S Concept blendi...](https://pluang.com/en/news-feed/toyota-merevolusi-crown-signia-gt-s-konsep-performa-untuk-sema)  
  <sub>Pluang, 1 hour ago</sub>  
  Toyota showcased the Crown Signia GT-S Concept at the 2026 SEMA show, transforming the 2026 Crown Signia into a sleek grand touring vehicle that combines...
- [(AMAX) Market Insights and Trading Signals (AMAX:CA)](https://news.stocktradersdaily.com/canada/amax-market-insights-and-trading-signals_20261028_a1868e)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Market Insights Report for Hamilton Gold Producer YIELD MAXIMIZER TM ETF (AMAX) with Key Trading Signals.
- [A packaging finish can cut CO₂ emissions by up to 26% vs. conventional matte lacquer, without ink or foil.](https://www.stocktitan.net/news/MDMXF/medmix-reaches-10-million-parts-milestone-with-sustainable-shadow-vb7meo420372.html)  
  <sub>Stock Titan, 7 hours ago</sub>  
  Orders for a further 2 million parts are already placed, while 43 different bottles and caps are in production at medmix sites in Germany,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 193.59 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 190.28 (+1.7%), 50d 191.86 (+0.9%), 200d 199.06 (-2.7%); 50d below 200d
Momentum: RSI(14) 53.1 | MACD 1.963 vs signal 1.252 (histogram 0.710)
Returns: 1d -1.5% | 5d -0.7% | 1m +3.7% | 3m +1.1%
52-week range: 166.50 - 248.29 (now 33.1% of the way up)
Volatility: ATR(14) 2.99 (1.5% of price) | annualised 20d 18.5%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 228.01B
Valuation: trailing P/E 8.51 | forward P/E 12.27 | P/B 15.55 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+20.9% vs last close), range 230.00 - 239.31
Recent rating changes:
  - 2025-11-07 Freedom Broker: down, Buy -> Hold
  - 2025-02-04 Macquarie: up, Neutral -> Outperform
  - 2024-06-14 Erste Group: down, Buy -> Hold
  - 2023-07-11 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2022-10-06 UBS: down, Buy -> Neutral
  - 2022-07-07 Jefferies: main, ? -> Hold
Institutional ownership: 2.2%
Largest holders: Fisher Asset Management, LLC (0.5%), Morgan Stanley (0.2%), FMR, LLC (0.1%), Goldman Sachs Group Inc (0.1%), Northern Trust Corporation (0.1%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 757,877 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to mixed technical signals, high valuation, strong earnings record, and no catalyst.

**Main reasons it gave:**
- Technical: price above 20‑day and 50‑day SMA but below 200‑day SMA, low volume (0.29× avg)
- Valuation: high trailing P/E 58.3 and forward P/E 41.6, indicating expensive stock
- Earnings: four consecutive beats (+10% to +21%) showing strong earnings momentum
- Analyst consensus: Hold with modest +3.5% price target, no recent upgrades

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 774.80 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 718.51 (+7.8%), 50d 721.93 (+7.3%), 200d 784.67 (-1.3%); 50d below 200d
Momentum: RSI(14) 62.0 | MACD 14.651 vs signal 5.203 (histogram 9.449)
Returns: 1d -1.9% | 5d +4.3% | 1m +10.2% | 3m -1.4%
52-week range: 454.95 - 1,014.33 (now 57.2% of the way up)
Volatility: ATR(14) 21.49 (2.8% of price) | annualised 20d 41.4%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 36.31B
Valuation: trailing P/E 58.30 | forward P/E 41.63 | P/B 8.22 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 802.17 (+3.5% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 27.8%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.0%), Altshuler Shaham Ltd (1.0%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 19,278,816 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Alphabet (Google) (GOOGL) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong fundamentals and bullish analyst consensus are offset by bearish technicals and mixed news, leading to a neutral view with modest conviction.

**Main reasons it gave:**
- Technical indicators: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 37.4 (bearish)
- News includes lawsuit and concerns about AI spending limiting gains (negative)
- Strong fundamentals: profit margin 54.8%, ROE 48.7%, low debt/equity 18.9% (bullish)
- Analyst consensus strong buy with mean price target +32.8% vs last close (bullish)

<details><summary><b>News</b> — score -0.30</summary>

- [Google to report Q3 results as investors focus on AI growth, weigh Meta Muse AI risk](https://finance.yahoo.com/technology/article/google-to-report-q3-results-as-investors-focus-on-ai-growth-weigh-meta-muse-ai-risk-191624324.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>
- [Google Earnings: Cloud Is Booming, But Can Search Deliver Amid AI Shift?](https://www.investors.com/news/technology/google-stock-google-earnings-capex-cloud-search-business/)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Google stock faces a Q3 earnings test amid renewed investor worries over the core internet search advertising business.
- [Google Stock Earnings Preview Q3 2026: What to Expect for GOOGL Stock](https://www.indmoney.com/blog/us-stocks/google-stock-q3-earnings-preview-googl)  
  <sub>INDmoney, 7 hours ago</sub>  
  Google Q3 2026 earnings are due October 28. See revenue and EPS forecasts, Cloud growth, AI spending and what investors should watch for GOOGL stock.
- [Alphabet stock rises as OpenAI plans to buy Google’s TPUs](https://finance.yahoo.com/technology/ai/articles/alphabet-stock-rises-openai-plans-133455553.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>
- [Meta- and Google-backed Jio Platforms’ shares soar over 21% on trading debut after record IPO](https://www.cnbc.com/2026/10/28/jio-ipo-india-listing-.html)  
  <sub>CNBC, 10 hours ago</sub>  
  Jio had offered 270 million shares in the IPO priced at 1119 rupees apiece, raising 302 billion rupees ($3.2 billion) in the country's largest-ever IPO.
- [Stock Market Today: S&P 500, Dow Jones Futures Trade Mixed Ahead of Federal Reserve Interest Rate Decision — SKHY, STX, V, GOOGL in Focus](https://www.tradingview.com/news/benzinga:c16c2c109094b:0-stock-market-today-s-p-500-dow-jones-futures-trade-mixed-ahead-of-federal-reserve-interest-rate-decision-skhy-stx-v-googl-in-focus/)  
  <sub>TradingView, 5 hours ago</sub>  
  U.S. stock futures were mixed on Wednesday, as the Dow Jones, S&P 500, and Nasdaq 100 index futures moved in different directions, following Tuesday's...
- [Google (GOOGL) Q3 2026 Earnings: Why a Beat May Not Lift Shares](https://www.ebc.com/forex/google-googl-q3-2026-earnings-preview)  
  <sub>EBC Financial Group, 5 hours ago</sub>  
  Google Q3 2026 earnings preview: See GOOGL revenue and EPS forecasts, Cloud margins, Search risks and why $200B in spending could limit stock gains.
- [$GOOG and $GOOGL Stock Market Alert: Alphabet Sued for](https://www.globenewswire.com/news-release/2026/10/28/3389972/0/en/goog-and-googl-stock-market-alert-alphabet-sued-for-securities-fraud-after-ai-issues-lead-to-4-stock-drop-contact-bfa-law-if-you-lost-money.html)  
  <sub>GlobeNewswire, 4 hours ago</sub>  
  Alphabet Sued for Securities Fraud after AI Issues Lead to 4% Stock Drop – Contact BFA Law if You Lost Money...
- [Alphabet Stock Breaks Down Ahead of Q3 Earnings: Could GOOGL Fall 30%?](https://www.mitrade.com/au/insights/stock-analysis/us-stocks/beincrypto-GOOG-202610281020)  
  <sub>Mitrade, 10 hours ago</sub>  
  Alphabet (GOOGL) stock trades below its 200-day moving average by the widest margin in 17 months, Barchart data show. AI spending fears pushed shares near...
- [Alphabet Shares Rise Over 1% Pre-Market Ahead of Earnings as OpenAI TPU Plan Draws Focus](https://www.tradingkey.com/analysis/stocks/us-stocks/262246812-ahead-of-alphabet-earnings-share-premarket-openai-planned-tpu-googl-tradingkey)  
  <sub>TradingKey, 3 hours ago</sub>  
  TradingKey - Shares of Google parent company Alphabet (GOOGL) rose over 1% in pre-market trading. The market is focusing on news that OpenAI may purchase...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 323.65 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 339.75 (-4.7%), 50d 341.48 (-5.2%), 200d 341.19 (-5.1%); 50d above 200d
Momentum: RSI(14) 37.4 | MACD -6.183 vs signal -3.245 (histogram -2.938)
Returns: 1d +1.0% | 5d -3.3% | 1m -5.1% | 3m -3.0%
52-week range: 267.47 - 402.62 (now 41.6% of the way up)
Volatility: ATR(14) 8.07 (2.5% of price) | annualised 20d 21.8%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.96T
Valuation: trailing P/E 16.24 | forward P/E 21.07 | P/B 6.36 | PEG 1.11
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.21 | short interest 1.3% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.80</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 42 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.68 (+32.8% vs last close), range 340.00 - 500.00
Recent rating changes:
  - 2026-10-22 Citizens: main, Market Outperform -> Market Outperform
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Keybanc: main, Overweight -> Overweight
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-10-14 UBS: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
Institutional ownership: 81.0%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 195,435,392 shares
Distinct insiders: 0 buying, 0 selling
(3 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst upgrade and insider buys versus bearish technicals, high valuation/debt, and weak earnings record. No material catalyst, so neutral stance with low conviction.

**Main reasons it gave:**
- Citigroup upgraded to Buy with price target +36% (analyst view bullish)
- Technical indicators: price below 20d/50d/200d SMAs, RSI 33.2, low volume (technical bearish)
- High debt/equity 168.6% and forward P/E 29.8 (fundamentals bearish)
- Earnings record: 1 beat, 3 misses (earnings bearish)

<details><summary><b>News</b> — score +0.20</summary>

- [MercadoLibre Stock: Brazil Panicked, I’m Buying (NASDAQ:MELI)](https://seekingalpha.com/article/4958388-mercadolibre-brazil-panicked-im-buying)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  MercadoLibre remains a strong buy after a sell-off driven by Brazilian politics, with fundamentals intact. Read more on MELI stock here.
- [MercadoLibre, Inc. (MELI) Stock Forecasts](https://ca.finance.yahoo.com/research/reports/MS_0P00009FL7_AnalystReport_1793054765000)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [DoorDash vs. MercadoLibre: Which Consumer Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/28/doordash-vs-mercadolibre-which-consumer-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  MercadoLibre trades at a significant valuation discount while generating more than four times DoorDash's free cash flow, raising a key question about growth...
- [Will Brazil Election Risk Change MercadoLibre Stock Narrative](https://simplywall.st/stocks/us/retail/nasdaq-meli/mercadolibre/news/will-brazil-election-risk-change-mercadolibre-stock-narrativ)  
  <sub>Simply Wall St, 1 hour ago</sub>  
  MercadoLibre has come under pressure after Brazil's surprise re-election of President Luiz Inácio Lula da Silva, raising questions about how potential...
- [MELI Upgraded by Citigroup -- Price Target Lowered to $2050](https://www.gurufocus.com/news/9145602/meli-upgraded-by-citigroup-price-target-lowered-to-2050)  
  <sub>GuruFocus, 15 hours ago</sub>  
  MercadoLibre (MELI) Analyst Rating Update - October 13, 2026 On October 13, 2026, Citigroup analyst Joao Pedro Soares upgraded MercadoLibre (MELI) to a Buy...
- [MercadoLibre (MELI) Set to Release Quarterly Earnings on Wednesday](https://www.marketbeat.com/instant-alerts/upcoming-mercadolibre-meli-set-to-release-quarterly-earnings-on-wednesday-2026-10-28/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  MercadoLibre (NASDAQ:MELI) will be releasing its Q3 2026 earnings after the market closes on Wednesday, November 4. (View Earnings Report at...
- [MercadoLibre Cratered by 20% Last Year: Two Wall Street Pros Agree It's Going to Rise 50% Soon](https://247wallst.com/investing/2026/10/27/mercadolibre-cratered-by-20-last-year-two-wall-street-pros-agree-its-going-to-rise-50-soon/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  MercadoLibre posted record revenue while its stock cratered, and two Wall Street firms now see a path to 50% gains from here.
- [MELI Sep 2027 1380.000 call (MELI270917C01380000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI270917C01380000/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest MELI Sep 2027 1380.000 call (MELI270917C01380000) stock quote, history, news and other vital information to help you with your stock trading...
- [MercadoLibre drops 8% post-Lula win but stays a strong buy with solid growth and risks ahead.](https://pluang.com/en/news-feed/saham-mercadolibre-brazil-panik-saya-beli-nasdaq-meli)  
  <sub>Pluang, 4 hours ago</sub>  
  MercadoLibre's stock fell nearly 8% following Lula da Silva's surprise election win in Brazil, reflecting political uncertainty. Despite this, the company...
- [MELI Sep 2027 2070.000 put (MELI270917P02070000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI270917P02070000/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest MELI Sep 2027 2070.000 put (MELI270917P02070000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 1,667.00 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 1,812.18 (-8.0%), 50d 1,851.43 (-10.0%), 200d 1,817.75 (-8.3%); 50d above 200d
Momentum: RSI(14) 33.2 | MACD -30.472 vs signal -10.788 (histogram -19.684)
Returns: 1d -0.8% | 5d -10.1% | 1m -3.4% | 3m -11.6%
52-week range: 1,546.81 - 2,360.76 (now 14.8% of the way up)
Volatility: ATR(14) 63.54 (3.8% of price) | annualised 20d 49.3%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 84.51B
Valuation: trailing P/E 45.34 | forward P/E 29.79 | P/B 10.79 | PEG 0.91
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 2.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 17 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 2,271.93 (+36.3% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-27 Citigroup: up, Neutral -> Buy
  - 2026-10-27 BTIG: reit, Buy -> Buy
  - 2026-10-13 Citigroup: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
Institutional ownership: 80.1%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,529,511 shares
Distinct insiders: 2 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-06-11 MELAMUD MARCELO (Officer): 124 shares, 200.00K
  - 2026-05-22 AGUZIN ALEJANDRO NICOLAS (Director): 600 shares, 993.56K
(4 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,650.27 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 1,705.28 (-3.2%), 50d 1,709.66 (-3.5%), 200d 1,593.63 (+3.6%); 50d above 200d
Momentum: RSI(14) 45.9 | MACD -35.266 vs signal -26.745 (histogram -8.521)
Returns: 1d +0.9% | 5d -1.6% | 1m -10.0% | 3m -0.1%
52-week range: 966.57 - 1,989.44 (now 66.8% of the way up)
Volatility: ATR(14) 52.65 (3.2% of price) | annualised 20d 37.5%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 636.06B
Valuation: trailing P/E 40.61 | forward P/E 26.27 | P/B 1,417.05 | PEG 0.85
Profitability: profit margin 34.1% | operating margin 44.4% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.30 | short interest 0.3% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 17% | 2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 7 strong buy, 31 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 2,135.11 (+29.4% vs last close), range 861.23 - 2,829.08
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 20.4%
Largest holders: FMR, LLC (1.4%), Fisher Asset Management, LLC (1.2%), Capital World Investors (1.0%), Invesco Ltd. (0.8%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 1,702,666 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### JPMorgan Chase (JPM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [JPM puts ArcelorMittal on Positive Catalyst Watch on steel price gains](https://finance.yahoo.com/markets/stocks/articles/jpm-puts-arcelormittal-positive-catalyst-113359294.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Onvesting.com -- J.P. Morgan placed steelmaker ArcelorMittal on its short-term "Positive Catalyst Watch" on Wednesday ahead of third-quarter results on Nov.
- [JPMorgan Chase (NYSE:JPM) Share Price, Forecast & Analysis](https://stocksdownunder.com/company/jpmorgan-chase/)  
  <sub>Stocks Down Under, 4 hours ago</sub>  
  Explore JPMorgan Chase (NYSE:JPM) share price, stock analysis, financial performance, valuation and analyst price targets on Stocks Down Under.
- [JPM Stock Gains 0.52%, Testing Key: Full Details](https://journalarta.com/en/2026/10/28/jpm-stock-gains-0-52-testing-key-resistance-in-focus/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 27, 2026: price 335.79 USD, trend sideways, RSI 47.6, support 329.58, resistance 339.72. technical analysis of jpm stock. JPM Stock Gains — full…
- [JPMorgan to lead Anthropic's U.S. retail IPO offering - report (ANT:Pending)](https://seekingalpha.com/news/4658624-jpmorgan-to-lead-anthropics-us-retail-ipo-offering---report)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  Anthropic (ANT) has tapped JPMorgan Chase (JPM) to lead U.S. share sales to individual investors in its potentially record-setting initial public offering,...
- [3 Dow Jones stocks with questionable fundamentals](https://www.theglobeandmail.com/investing/markets/stocks/JPM/pressreleases/8494423/3-dow-jones-stocks-with-questionable-fundamentals/)  
  <sub>The Globe and Mail, 10 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPMorgan’s 2027 earnings calls run into January 2028.](https://www.stocktitan.net/news/JPM/jp-morgan-chase-updates-2027-earnings-release-date-6d2o05tl434y.html)  
  <sub>Stock Titan, 18 hours ago</sub>  
  10/27/2026 - 01:21 PM PDT. NEW YORK --(BUSINESS WIRE)-- JPMorgan Chase & Co. (NYSE: JPM) (“JPMorganChase” or the “Firm”) plans to host conference calls to...
- [6,567 JPMorgan Chase & Co. $JPM Shares Sold by OLD Second National Bank of Aurora](https://www.marketbeat.com/instant-alerts/filing-6567-jpmorgan-chase-co-jpm-shares-sold-by-old-second-national-bank-of-aurora-2026-10-28/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  OLD Second National Bank of Aurora lowered its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 18.5% in the third quarter, according to the...
- [JPM Oct 2026 367.500 call (JPM261030C00367500) stock historical prices and data](https://uk.finance.yahoo.com/quote/JPM261030C00367500/history/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Discover historical prices for JPM261030C00367500 stock on Yahoo Finance. View daily, weekly or monthly formats back to when JPM Oct 2026 367.500 call stock...
- [JPMorgan Chase & Co. $JPM Shares Sold by Sterling Capital Management LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-sold-by-sterling-capital-management-llc-2026-10-28/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Sterling Capital Management LLC trimmed its position in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 17.4% in the 3rd quarter, according to the company...
- [Where Did JPMorgan Chase (NYSE:JPM) Find Strength in the Third Quarter?](https://kalkinemedia.com/us/stocks/financial/where-did-jpmorgan-chase-nysejpm-find-strength-in-the-third-quarter)  
  <sub>Kalkine Media, 8 hours ago</sub>  
  JPMorgan Chase reported third-quarter net earnings of about , or five dollars and fifty-seven cents per diluted share, according to its regulatory filing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 337.33 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 333.94 (+1.0%), 50d 343.81 (-1.9%), 200d 322.63 (+4.6%); 50d above 200d
Momentum: RSI(14) 50.1 | MACD -1.876 vs signal -2.807 (histogram 0.931)
Returns: 1d +0.5% | 5d +0.6% | 1m +0.7% | 3m -3.9%
52-week range: 282.84 - 365.18 (now 66.2% of the way up)
Volatility: ATR(14) 5.81 (1.7% of price) | annualised 20d 12.6%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 895.81B
Valuation: trailing P/E 14.15 | forward P/E 13.21 | P/B 2.55 | PEG 1.42
Profitability: profit margin 34.6% | operating margin 42.6% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 1.0% of float
Next earnings: 2027-01-14
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 missed by 7% | 2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

```text
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 10 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 372.26 (+10.4% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-10-15 Citigroup: main, Neutral -> Neutral
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - 2026-10-14 Baird: main, Neutral -> Neutral
Institutional ownership: 75.6%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 49,845 shares in 11
Net: +86,765 shares (+0.8% of insider holdings) | insiders hold 10,356,840 shares
Distinct insiders: 0 buying, 9 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(7 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Eli Lilly (LLY) reports earnings tomorrow: what to expect](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-lly-reports-earnings-094234283.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Global pharmaceutical company Eli Lilly (NYSE:LLY) will be reporting earnings this Thursday before market hours. Here's what you need to know.
- [LLY 261030 1290.00P (LLY261030P1290000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/LLY261030P1290000-US)  
  <sub>Moomoo, 6 hours ago</sub>  
  Track real-time LLY 261030 1290.00P (LLY261030P1290000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [LLY Vs NVO: Lilly’s Retatrutide Beats Novo’s Ozempic In Head-To-Head Trial — Retatrutide More Than Doubles Weight Loss](https://stocktwits.com/news-articles/markets/equity/lly-nvo-retatrutide-beats-ozempic-in-head-to-head-trial/cZU9h53R9GR)  
  <sub>Stocktwits, 2 hours ago</sub>  
  Retatrutide helped patients with type 2 diabetes lose an average of 44 to 47 pounds over 80 weeks, compared with about 21 pounds for Ozempic.
- [Lilly's retatrutide beats Ozempic in Phase 3 trial (LLY:NYSE)](https://seekingalpha.com/news/4658788-lillys-retatrutide-beats-ozempic-phase-3-trial)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Eli Lilly (LLY) says next-gen weight loss drug, retatrutide beat Ozempic on weight loss and A1C reduction in a head-to-head Phase 3 trial for diabetes.
- [Strong Results, Guidance Boost Eli Lilly Shares Ahead of Earnings](https://www.fxempire.com/forecasts/article/strong-results-guidance-boost-eli-lilly-shares-ahead-of-earnings-1640975)  
  <sub>FXEmpire, 3 hours ago</sub>  
  Shares of Eli Lilly and Company (LLY) rise 19899% since Big Money bought big in 1990.
- [Eli Lilly's Retatrutide Outperforms Ozempic in Weight Loss Trial, LLY Stock Shows 19.5% Undervaluation](https://www.gurufocus.com/news/9147340/eli-lillys-retatrutide-outperforms-ozempic-in-weight-loss-trial-lly-stock-shows-195-undervaluation)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 28, 2026, Eli Lilly and Co (NYSE: LLY) announced that its novel weight loss drug, retatrutide, demonstrated superior efficacy compared to Novo...
- [If Eli Lilly Stock Looks Expensive, You Need To Read This](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-stock-looks-expensive-092501265.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Eli Lilly (LLY) shares closed at $1,281.91 on October 27, 2026,...
- [Top Wall Street Forecasters Revamp Eli Lilly Expectations Ahead Of Q3 Earnings](https://www.benzinga.com/analyst-stock-ratings/price-target/26/10/62645956/top-wall-street-forecasters-revamp-eli-lilly-expectations-ahead-of-q3-earnings)  
  <sub>Benzinga, 5 hours ago</sub>  
  Eli Lilly and Company (NYSE:LLY) will release its third quarter earnings report before the opening bell on Thursday, Oct. 29.
- [Eli Lilly (LLY) Keeps Obesity Ads Live As Court Rules And AI Program Launches](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-keeps-obesity-ads-live-as-court-rules-and-ai-p/amp)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  Eli Lilly (NYSE: LLY) kept its obesity drug ads running after a U.S. federal court rejected Novo Nordisk's request for an injunction.
- [Here’s How Much Eli Lilly Stock Is Expected to Move After Earnings](https://finance.yahoo.com/markets/stocks/articles/much-eli-lilly-stock-expected-100000415.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Eli Lilly is set to report earnings Thursday morning, with traders expecting a move that could send the stock to a fresh high.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,295.72 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 1,221.45 (+6.1%), 50d 1,191.96 (+8.7%), 200d 1,088.08 (+19.1%); 50d above 200d
Momentum: RSI(14) 65.5 | MACD 32.779 vs signal 25.742 (histogram 7.037)
Returns: 1d +1.1% | 5d +2.0% | 1m +9.4% | 3m +12.2%
52-week range: 813.53 - 1,306.69 (now 97.8% of the way up)
Volatility: ATR(14) 36.29 (2.8% of price) | annualised 20d 29.3%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.16T
Valuation: trailing P/E 43.50 | forward P/E 27.34 | P/B 34.10 | PEG 1.23
Profitability: profit margin 33.5% | operating margin 54.2% | ROE 102.3%
Growth (YoY): revenue +47.7% | earnings +26.2%
Balance sheet: debt/equity 162.1% | free cash flow 11.07B
Risk: beta 0.45 | short interest 0.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 38% | 2026-03-31 beat by 27% | 2025-12-31 beat by 12% | 2025-09-30 beat by 22%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

```text
Consensus: buy (mean 1.61 on a 1=strong buy to 5=strong sell scale, 30 analysts)
Ratings: 6 strong buy, 20 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,333.72 (+2.9% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-08 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-07 Morgan Stanley: main, Overweight -> Overweight
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
Institutional ownership: 85.4%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 1,467 shares in 28 transaction(s) | sold 308,215 shares in 8
Net: -306,748 shares (-18.0% of insider holdings) | insiders hold 1,390,517 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
  - 2026-06-10 YUFFA ILYA (Officer): 2,500 shares, 2.88M
(28 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Microsoft to report Q1 earnings with Wall Street looking for further Azure growth](https://finance.yahoo.com/technology/article/microsoft-to-report-q1-earnings-with-wall-street-looking-for-further-azure-growth-160835128.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Microsoft (MSFT) will report its first quarter earnings after the bell on Wednesday, providing the market with a better view of demand for AI apps and...
- [Microsoft (NASDAQ:MSFT): Strong Growth Paired With a High-Quality Technical Setup](https://www.chartmill.com/news/MSFT/Chartmill-57007-Microsoft-NASDAQMSFT-Strong-Growth-Paired-With-a-High-Quality-Technical-Setup)  
  <sub>ChartMill, 2 hours ago</sub>  
  Microsoft pairs double-digit growth with strong profitability and positive technical trends, offering a consolidation breakout setup for growth investors.
- [Microsoft Earnings Preview: Polymarket Doubts a July-Size Surge - Microsoft (NASDAQ:MSFT)](https://www.benzinga.com/markets/earnings/26/10/62643954/microsoft-earnings-preview-polymarket-traders-say-july-size-jump-unlikely)  
  <sub>Benzinga, 8 hours ago</sub>  
  Microsoft Corp.'s (NASDAQ:MSFT) shares ended the week of its fourth-quarter earnings report in July nearly 22% higher, but Polymarket traders are not...
- [4 stocks to watch on Wednesday: MSFT, BSX, V, and SKHY (SPX:)](https://seekingalpha.com/news/4658832-4-stocks-to-watch-on-wednesday-msft-bsx-v-and-skhy)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock index futures were mixed on Wednesday as traders awaited the Federal Reserve's policy decision, while investors looked forward to the earnings from...
- [MSFT Dips Premarket Ahead Of Q1 Report: Analysts Expect Azure Acceleration As Management Faces Questions On Massive Employee Buyout](https://stocktwits.com/news-articles/markets/equity/msft-dips-premarket-ahead-of-q1-report-analysts-expect-azure-acceleration-as-management-faces-questions-on-massive-employee-buyout-offer/cZU9BLXRB6F)  
  <sub>Stocktwits, 6 hours ago</sub>  
  Investors will focus on the performance of Microsoft's Azure cloud unit and any updates around its spending plan.
- [Microsoft Stock Breaks $513 as Azure and Copilot Growth Support MSFT](https://www.tradingkey.com/analysis/stocks/us-stocks/262141656-microsoft-stock-azure-copilot-msft-breakout-513-tradingkey)  
  <sub>TradingKey, 3 hours ago</sub>  
  Microsoft Stock Breaks $513 as Azure and Copilot Growth Support MSFT ... Microsoft enters September with strong momentum, driven by 43% Azure growth, surging...
- [Futures Mixed as Fed, MSFT, GOOGL Report Oct. 28 [2026]](https://tech-insider.org/futures-mixed-fed-microsoft-alphabet-earnings-oct-28-2026/)  
  <sub>https://tech-insider.org/, 11 hours ago</sub>  
  Stock futures are mixed as the Fed decision and Microsoft and Google earnings land. See what these 3 events mean for the S&P 500, Nasdaq and Dow.
- [MSFT 261023 540.00P (MSFT261023P540000) Stock Community & Discussion](https://www.moomoo.com/options/MSFT261023P540000-US/community)  
  <sub>Moomoo, 16 hours ago</sub>  
  Find the latest MSFT 261023 540.00P (MSFT261023P540000)stock discussion in moomoo's forum, a popular stock community. Get stock reviews, comments and...
- [ETFs Are Net Sellers of Microsoft (MSFT) on Monday](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-microsoft-msft-110214286.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs sold a net $272.5 million of Microsoft stock in Monday's session.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 529.48 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 529.82 (-0.1%), 50d 511.15 (+3.6%), 200d 437.31 (+21.1%); 50d above 200d
Momentum: RSI(14) 54.9 | MACD 6.142 vs signal 8.019 (histogram -1.877)
Returns: 1d -0.3% | 5d -0.7% | 1m +4.0% | 3m +17.4%
52-week range: 352.83 - 543.45 (now 92.7% of the way up)
Volatility: ATR(14) 10.63 (2.0% of price) | annualised 20d 19.6%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.93T
Valuation: trailing P/E 29.50 | forward P/E 22.35 | P/B 8.89 | PEG 1.73
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.10 | short interest 0.9% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-12-31 beat by 3% | 2025-09-30 beat by 10%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

```text
Consensus: strong_buy (mean 1.33 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 13 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 605.12 (+14.3% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-26 Oppenheimer: main, Outperform -> Outperform
  - 2026-10-26 Truist Securities: reit, Buy -> Buy
  - 2026-10-26 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-10-21 Guggenheim: reit, Buy -> Buy
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Bernstein: main, Outperform -> Outperform
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%), FMR, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 513,644 shares in 16 transaction(s) | sold 249,649 shares in 10
Net: +263,995 shares (+4.7% of insider holdings) | insiders hold 5,866,181 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-13 HOOD AMY E (Chief Financial Officer): 7,305 shares, 3.98M
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
  - 2026-09-01 NADELLA SATYA (Chief Executive Officer): 86,525 shares, 43.39M
  - 2026-08-05 ALTHOFF JUDSON (Officer): 10,000 shares, 4.88M
(15 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://au.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo Finance Australia, 5 hours ago</sub>  
  498,048.58% · Previous close 216.00 · Open 218.30 · Bid 210.00 x 100 · Ask 216.28 x 200 · Day's range 215.53 - 219.19 · 52-week range 164.27 - 243.37 · Volume...
- [Nvidia Stock May Actually Raise Its 70% Growth Guide In November (NASDAQ:NVDA)](https://seekingalpha.com/article/4958511-nvidia-may-actually-raise-its-70-percent-growth-guide-in-november)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Nvidia Corporation keeps a Strong Buy as supply constraints ease and AI demand surges. Click for this NVDA stock update.
- [5 Stocks Poised to Win Big as SpaceX Ramps Up AI Infrastructure](https://www.fool.com/investing/2026/10/28/5-stocks-poised-to-win-big-as-spacex-ramps-up-ai-i/)  
  <sub>The Motley Fool, 4 hours ago</sub>  
  Space Exploration Technologies (SPCX +1.14%) just upped the ante in the artificial intelligence (AI) infrastructure race, planning to increase its computing...
- [Nvidia Stock Faces a Test From Its Biggest AI Chip Rival](https://www.barrons.com/articles/nvidia-stock-price-ai-chip-competition-b81f00a2)  
  <sub>Barron's, 4 hours ago</sub>  
  Nvidia shares were up 0.8% at $219.62 in premarket trading Wednesday. The chip maker has dropped back from the record highs of more than $240 it recorded...
- [Fund Update: 145,295 NVIDIA (NVDA) shares added to Donor Advised Charitable Giving, Inc. portfolio](https://www.quiverquant.com/news/Fund+Update%3A+145%2C295+NVIDIA+%28NVDA%29+shares+added+to+Donor+Advised+Charitable+Giving%2C+Inc.+portfolio)  
  <sub>Quiver Quantitative, 40 minutes ago</sub>  
  Donor Advised Charitable Giving, Inc. has added 145295 shares of $NVDA to their portfolio, per a ne.
- [SpaceX Ramps Up AI Compute Expansion: Four US Stocks Stand to Benefit](https://nai500.com/blog/2026/10/spacex-ramps-up-ai-compute-expansion-four-us-stocks-stand-to-benefit/)  
  <sub>NAI500, 3 hours ago</sub>  
  SpaceX is raising stakes in the global artificial‑intelligence infrastructure race, planning to lift its computing capacity by roughly 10 gigawatts next...
- [Prediction: $10,000 Invested in Nvidia Will Be Worth This Much by Late 2029 -- If the AI Spending Boom Continues](https://www.theglobeandmail.com/investing/markets/stocks/NVDA-Q/pressreleases/8499576/prediction-10-000-invested-in-nvidia-will-be-worth-this-much-by-late-2029-if-the-ai-spending-boom-continues/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.
- [NVIDIA Corporation $NVDA Stock Holdings Decreased by Legacy Private Trust Co.](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-holdings-decreased-by-legacy-private-trust-co-2026-10-28/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Legacy Private Trust Co. reduced its stake in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 1.9% in the third quarter, according to its most...
- [Nvidia: Brace For The Worst (NASDAQ:NVDA)](https://seekingalpha.com/article/4958219-nvidia-brace-for-the-worst)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Nvidia Corporation faces AI demand risks, rising memory costs, and margin pressure as customers strain cash flow. Click for this NVDA stock update.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 217.76 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 223.90 (-2.7%), 50d 222.12 (-2.0%), 200d 204.15 (+6.7%); 50d above 200d
Momentum: RSI(14) 46.1 | MACD -2.484 vs signal -1.516 (histogram -0.968)
Returns: 1d -0.1% | 5d -1.9% | 1m -4.2% | 3m +11.7%
52-week range: 165.17 - 239.24 (now 71.0% of the way up)
Volatility: ATR(14) 5.71 (2.6% of price) | annualised 20d 30.2%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.26T
Valuation: trailing P/E 27.53 | forward P/E 13.68 | P/B 22.96 | PEG 0.26
Profitability: profit margin 63.7% | operating margin 66.2% | ROE 117.2%
Growth (YoY): revenue +105.9% | earnings +127.8%
Balance sheet: debt/equity 17.0% | free cash flow 41.81B
Risk: beta 2.22 | short interest 1.3% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-03-31 beat by 4% | 2025-12-31 in line
```

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

```text
Consensus: strong_buy (mean 1.29 on a 1=strong buy to 5=strong sell scale, 58 analysts)
Ratings: 10 strong buy, 49 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.95 (+51.1% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-10-22 Needham: reit, Buy -> Buy
  - 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-09-29 Rosenblatt: main, Buy -> Buy
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
Institutional ownership: 71.5%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), FMR, LLC (4.3%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,613,243 shares in 18 transaction(s) | sold 6,198,325 shares in 9
Net: -3,585,082 shares (-0.4% of insider holdings) | insiders hold 965,687,040 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-21 TETER TIMOTHY S (General Counsel): 30,460 shares, 6.79M
  - 2026-09-18 STEVENS MARK A (Director): 1,366,000 shares, 300.15M
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
(18 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Meta Stock Analysis: Buy or Sell? (My Final Verdict)](https://www.theglobeandmail.com/investing/markets/stocks/META-Q/pressreleases/8499023/meta-stock-analysis-buy-or-sell-my-final-verdict/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Before you buy stock in Meta Platforms, consider this: Missed Nvidia in 2009? This Rare Signal Is Flashing Again.In 2009, a "Double Down" signal flashed for...
- [Royal Bank of Canada stock rises Tuesday, still underperforms market](https://www.marketwatch.com/data-news/royal-bank-of-canada-stock-rises-tuesday-still-underperforms-market-87d4c4df-a75c13e52a2b)  
  <sub>MarketWatch, 18 hours ago</sub>  
  inched 0.42% higher to C$285.46 Tuesday, in what proved to be an all-around favorable trading session for the Canadian market, with the S&P/TSX Composite...
- [Anthropic Delivers Massive News to Stock Market Investors](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL/pressreleases/8492067/anthropic-delivers-massive-news-to-stock-market-investors/)  
  <sub>The Globe and Mail, 11 hours ago</sub>  
  Before you buy stock in Amazon, consider this: Missed AI's "Act 1"? Act 2 Could Be 15x Bigger. Most investors think they missed the AI boat because they...
- [MarketBeat cites USD 225.00 target for Royal Bank of Canada stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/marketbeat-cites-usd-225-00-target-for-royal-bank-of-canada-stock/70421847)  
  <sub>ad-hoc-news.de, 22 hours ago</sub>  
  RBC declared a CAD 1.76 dividend payable November 24, 2026. Royal Bank of Canada stock costs EUR 181.95 on October 27, 2026 after the Xetra close.
- [Why SoFi Stock Popped Today](https://www.theglobeandmail.com/investing/markets/markets-news/motley/8490960/why-sofi-stock-popped-today/)  
  <sub>The Globe and Mail, 12 hours ago</sub>  
  Shares of SoFi Technologies (NASDAQ:SOFI) rose more than 13% on Tuesday after the digital financial services provider issued an optimistic growth forecast.
- [Charm Care Completes Restricted Stock Compensation Transaction](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/8493287/charm-care-completes-restricted-stock-compensation-transaction/)  
  <sub>The Globe and Mail, 8 hours ago</sub>  
  Charm Care Corporation ( (JP:6062) ) has shared an update. Charm Care Corporation has completed payment procedures for the disposal of 10,400 shares of its...
- [RBC Says SpaceX Stock Has 50% Upside. S&P Global Just Warned About Its Hidden AI Debt. Here's Who I Think Is Right.](https://www.theglobeandmail.com/investing/markets/stocks/RY-N/pressreleases/8490238/rbc-says-spacex-stock-has-50-upside-sp-global-just-warned-about-its-hidden-ai-debt-here-s-who-i-think-is-right/)  
  <sub>The Globe and Mail, 14 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.
- [Stock Market Today, Oct. 27: CoreWeave Surges on Denmark Data Center Launch](https://www.theglobeandmail.com/investing/markets/stocks/CRWV/pressreleases/8487523/stock-market-today-oct-27-coreweave-surges-on-denmark-data-center-launch/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  CoreWeave(NASDAQ:CRWV), a specialized AI cloud computing provider, closed at $59.57, up 7.94%. The stock surged after it switched on new compute capacity at...
- [Air Canada (AC:CA) ATB Cormark Cuts Target on Stock](https://www.theglobeandmail.com/investing/markets/stocks/AC-T/pressreleases/8492214/air-canada-acca-atb-cormark-cuts-target-on-stock/)  
  <sub>The Globe and Mail, 10 hours ago</sub>  
  ATB Cormark maintained its Outperform rating while lowering its price target to $43.00 from $45.00, representing a 4.4% reduction.
- [If You'd Invested $10,000 in Apple Stock 10 Years Ago, Here's How Much You'd Have Today](https://www.theglobeandmail.com/investing/markets/stocks/NFLX-Q/pressreleases/8501929/if-you-d-invested-10-000-in-apple-stock-10-years-ago-here-s-how-much-you-d-have-today/)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Creating a diversified portfolio of excellent stocks benefits investors in so many ways. One of them is access to a variety of growth opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 202.29 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 196.99 (+2.7%), 50d 201.55 (+0.4%), 200d 188.85 (+7.1%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 0.423 vs signal -0.792 (histogram 1.215)
Returns: 1d -0.4% | 5d +0.1% | 1m +1.2% | 3m -3.7%
52-week range: 145.41 - 217.87 (now 78.5% of the way up)
Volatility: ATR(14) 2.81 (1.4% of price) | annualised 20d 15.4%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 280.06B
Valuation: trailing P/E 17.68 | forward P/E 15.86 | P/B 2.94 | PEG 1.89
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.91 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 212.21 (+4.9% vs last close), range 185.22 - 233.41
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.5%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.4%), Vanguard Capital Management LLC (3.1%), FIL LTD (1.7%), TD Asset Management, Inc (1.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 373,796 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-09-29 Royal Bank of Canada (Issuer): 200,000 shares, 39.94M
  - 2026-09-28 Royal Bank of Canada (Issuer): 200,000 shares, 40.29M
  - 2026-09-25 Royal Bank of Canada (Issuer): 200,000 shares, 40.24M
  - 2026-09-24 Royal Bank of Canada (Issuer): 200,000 shares, 39.86M
(101 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Exxon Mobil (XOM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Energy Select Sector SPDR (XLE) Buys $26.1 Million More XOM on Monday](https://finance.yahoo.com/energy/articles/state-street-energy-select-sector-110503197.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  The fund added $107.9 million across all 21 of its positions, led by a $26.1 million increase in Exxon Mobil.
- [Fund Update: New $17.4M $XOM Stock Position Opened by Empirical Financial Services, LLC D.b.a. Empirical Wealth Management](https://www.moomoo.com/news/post/1002577817/fund-update-new-17-4m-xom-stock-position-opened-by)  
  <sub>Moomoo, 11 hours ago</sub>  
  EmpiricalFinancial Services, LLC d.b.a. Empirical Wealth Management has opened a new $17.4M position in $XOM, per a new SEC 13F filing.
- [Why Did XOM, BTE, VTRS Jump To 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-xom-bte-vtrs-jump-to-52-week-highs-today/cZU9GwsRB6I)  
  <sub>Stocktwits, 12 hours ago</sub>  
  XOM stock jumped to a 52-week high during regular trading hours before closing 2.5% lower as oil prices continued to edge higher. BTE stock also rose to a...
- [AI Power Stocks Fell 7% to 13% in a Week While Exxon and Chevron Just Hit Record Highs. Here's Which Side I'd Rather Own.](https://www.fool.com/investing/2026/10/27/ai-power-stocks-fell-7-to-13-in-a-week-while-exxon/)  
  <sub>The Motley Fool, 11 hours ago</sub>  
  Stocks like Oklo are high-risk, and the opportunity may not pan out, but Exxon and Chevron are built to survive hard times.
- [EXXONMOBIL HOLDINGS CORPORATION COMMON STOCK - Pete Sessions Congressional Trade on Oct. 14, 2026](https://www.quiverquant.com/congresstrading/trade/House-S000250-477)  
  <sub>Quiver Quantitative, 1 hour ago</sub>  
  See details for Pete Sessions' trade of XOM - EXXONMOBIL HOLDINGS CORPORATION COMMON STOCK on Oct. 14, 2026.
- [US-Russia Talks Could Open Door for ExxonMobil (XOM) in Russian Oil Sector Amid Peace Negotiations](https://www.gurufocus.com/news/9145868/usrussia-talks-could-open-door-for-exxonmobil-xom-in-russian-oil-sector-amid-peace-negotiations)  
  <sub>GuruFocus, 14 hours ago</sub>  
  On October 27, 2026, discussions between the U.S. and Russia surfaced around the potential re-entry of major American energy companies, including ExxonMobil...
- [ExxonMobil's Q3 Earnings on Deck: Should You Bet on the Stock?](https://www.theglobeandmail.com/investing/markets/stocks/XOM/pressreleases/8479008/exxonmobils-q3-earnings-on-deck-should-you-bet-on-the-stock/)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  ExxonMobil Holdings Corporation XOM is set to report third-quarter 2026 results on Oct. 30, before the opening bell. The Zacks Consensus Estimate for...
- [ExxonMobil (XOM) Wins $12 Billion Kazakhstan Case And Finds Oil In Guyana](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/exxonmobil-xom-wins-12-billion-kazakhstan-case-and-finds-oil)  
  <sub>Simply Wall Street, 4 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) secured dismissal of Kazakhstan's US$12b Kashagan oil field claim in a recent court ruling. The government of Kazakhstan had...
- [BlackRock reports a passive stake above 5% in ExxonMobil Holdings (XOM).](https://www.stocktitan.net/sec-filings/XOM/schedule-13g-exxon-mobil-holdings-corp-passive-investment-disclosure--2075d0d7c7c8.html)  
  <sub>Stock Titan, 17 hours ago</sub>  
  ExxonMobil Holdings Corp (XOM) had a report of 297,486,444 shares beneficially owned by BlackRock, Inc., equal to 7.2% of the common stock, as of September...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 181.40 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 173.81 (+4.4%), 50d 166.96 (+8.7%), 200d 154.03 (+17.8%); 50d above 200d
Momentum: RSI(14) 66.5 | MACD 4.889 vs signal 4.370 (histogram 0.519)
Returns: 1d +0.8% | 5d +1.9% | 1m +12.4% | 3m +15.6%
52-week range: 113.68 - 184.54 (now 95.6% of the way up)
Volatility: ATR(14) 3.80 (2.1% of price) | annualised 20d 20.9%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 745.92B
Valuation: trailing P/E 23.35 | forward P/E 14.86 | P/B 2.88 | PEG 1.50
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.21 | short interest 1.1% of float
Next earnings: 2026-10-30
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 beat by 14% | 2025-12-31 in line | 2025-09-30 beat by 2%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

```text
Consensus: buy (mean 2.40 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 6 buy, 16 hold, 0 sell, 0 strong sell
Price target: mean 179.41 (-1.1% vs last close), range 142.00 - 206.00
Recent rating changes:
  - 2026-10-19 Barclays: main, Overweight -> Overweight
  - 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 67.0%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.5%), State Street Corporation (5.0%), FMR, LLC (3.3%), Vanguard Portfolio Management LLC (2.8%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-194.9% of insider holdings) | insiders hold 3,371,767 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

## Whole-market funds

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, no analyst rating, and bearish technicals without decisive volume.

**Main reasons it gave:**
- Technical momentum bearish (RSI 24.9, MACD negative) with low volume (0.18x 20‑day average)
- Fund flows flat over the past week and month (share count unchanged)
- No macro surprise: yields unchanged, inflation 3.7% in line, Fed target unchanged
- Analyst view provides no rating, indicating a neutral outlook

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 27.22 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 28.15 (-3.3%), 50d 28.49 (-4.5%), 200d 27.35 (-0.5%); 50d above 200d
Momentum: RSI(14) 24.9 | MACD -0.254 vs signal -0.148 (histogram -0.106)
Returns: 1d -0.7% | 5d -3.2% | 1m -3.7% | 3m -1.0%
52-week range: 25.44 - 29.49 (now 43.8% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.7%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +12.5% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.36B
What it is made of: Other 51.0%, Cash 47.0%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 42.3%, Invesco Short Term Treasury ETF 4.6%
Sector mix: Healthcare 16.8%, Industrials 15.2%, Financial services 13.7%, Consumer cyclical 11.8%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 2 largest holdings, 46.9% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, TBLL
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 27.60M | fund size: 751.13M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Given the lack of macro surprises, flat fund flows, mixed fundamental signals from inventories and price outlook, and technicals showing a bullish trend but low volume near a 52‑week high, there is no clear directional catalyst, so the appropriate call is NEUTRAL.

**Main reasons it gave:**
- No macro surprise in rates or inflation data
- Technical trend bullish but price near 52‑week high and low volume
- Energy inventories draw bullish but EIA price outlook bearish, net neutral
- Fund flows flat, indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.90 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 33.28 (+1.9%), 50d 32.60 (+4.0%), 200d 29.13 (+16.4%); 50d above 200d
Momentum: RSI(14) 61.5 | MACD 0.392 vs signal 0.392 (histogram 0.000)
Returns: 1d +0.9% | 5d +1.2% | 1m +5.9% | 3m +15.6%
52-week range: 22.36 - 34.10 (now 98.3% of the way up)
Volatility: ATR(14) 0.45 (1.3% of price) | annualised 20d 12.7%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +16.1% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.92B
What it is made of: Other 50.4%, Cash 45.1%, Bonds 2.5%, Stocks 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.5%, Brent Crude Future Dec 26 9.7%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 4 largest holdings, 59.1% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, BRNG6, TBLL, WINZ26
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 111.40M | fund size: 3.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or policy shift this week; mixed technicals with price near 52‑week low and low volume; significant outflows of -11.8% share count over the past month indicating negative sentiment.

**Main reasons it gave:**
- No macro surprise or policy shift this week (yields down slightly, Fed target unchanged)
- Price near 52‑week low (22.8% up from low) with mixed technicals: RSI 51, MACD above signal, low volume
- Large outflows: -11.8% share count over past month indicating negative sentiment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.88 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 91.20 (+0.7%), 50d 92.71 (-0.9%), 200d 95.00 (-3.3%); 50d below 200d
Momentum: RSI(14) 51.0 | MACD -0.201 vs signal -0.391 (histogram 0.190)
Returns: 1d -0.0% | 5d +0.5% | 1m +0.7% | 3m -3.1%
52-week range: 90.14 - 97.74 (now 22.8% of the way up)
Volatility: ATR(14) 0.46 (0.5% of price) | annualised 20d 5.6%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.5%, BB 25.3%, B 19.5%, A 17.7% | US government debt 88.0%
Three-year record: +9.8% a year | beta to the market 1.10
Cost and size: expense ratio 0.39% | net assets 12.93B
What it is made of: Bonds 99.1%, Cash 0.9%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.7%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.2% (-29.82M) over 7d | 1 month: -11.8% (-1.74B) over 32d
Shares outstanding: 141.47M | fund size: 13.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, modest bearish positioning but mixed technicals and stable fundamentals.

**Main reasons it gave:**
- Fed likely to hold rates steady – no policy surprise
- 10-year Treasury yield fell 13 bps this week, supporting bond prices
- CFTC positioning shows net short 35.9% of OI, up 2% week‑over‑week – slight bearish tilt
- Technical indicators mixed: price above 20‑day SMA but below 50‑day SMA, MACD bullish, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Daily ETF Flows: Over $1B Flows Into JCPB](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-over-1b-flows-jcpb)  
  <sub>ETF.com, 21 hours ago</sub>  
  Here are the daily ETF fund flows for October 26, 2026.
- [FPE: Better Than Preferred Stock Index Funds, But Inflation Is A Real Risk (NYSEARCA:FPE)](https://seekingalpha.com/article/4958329-fpe-better-than-preferred-stock-index-funds-but-inflation-is-a-real-risk)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  The First Trust Preferred Securities and Income ETF offers a 6.40% yield, outperforming passive preferred stock ETFs over the past decade.
- [Fund Files: Fidelity PM to exit, come off $33bn fund; VanEck launches all-in-one ETF](https://citywire.com/pro-buyer/news/fund-files-fidelity-pm-to-exit-come-off-33bn-fund-vaneck-launches-all-in-one-etf/a2502022)  
  <sub>Citywire, 20 hours ago</sub>  
  Twitter Facebook Linkedin WhatsApp print. Twitter Facebook Linkedin WhatsApp print. Get the latest news in your inbox. See all newsletters.
- [Fed Likely To Hold Rates Steady, Says Wolfe Research’s Roth — Analysts See Inflation Risks Keeping December Hike In Play](https://www.google.com/goto?url=CAES8QEB6zswFTJs2SRa8ZfHlXrlmetHIx_y5Qf5VmceF1lzaVEJx_v1aZOq7Q_QhjpEuh5CxYcLEgGvo4zxI-tLlaw-VEUuaXkJ8KNhz4kAgo1nRHMUWdiOqg1wD2Fh1QWE2Y7reO48NF8ZbmHFrICbL0pt_vf4o0lGwpxOLS-_O5pr8qPf5XgA1unAJJba3CEonY20fKFiLB3YxImgBkPB2BF3aUmQ4ETGD2ngDwlO75QajE2Q9NmpQ4SjJnpBYfyVV757zG7tpRXTj131Q85JLboYcYiaO36HAzw3_MDWDqLWUiMnbENLpzE592CsEyHjpVjD)  
  <sub>Stocktwits, 3 hours ago</sub>  
  The Federal Reserve is 'overwhelmingly likely' to leave interest rates unchanged on Wednesday, according to Wolfe Research Chief Economist Stephanie Roth,...
- [BHK: A CEF Upgrade As Risk Factors Exhaust (NYSE:BHK)](https://seekingalpha.com/article/4958336-bhk-a-cef-upgrade-as-risk-factors-exhaust?source=feed_all_articles)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  BlackRock Core Bond Trust is now rated 'Hold' after a period of negative performance driven by higher rates and wider credit spreads.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.89 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 89.99 (+1.0%), 50d 90.95 (-0.1%), 200d 93.91 (-3.2%); 50d below 200d
Momentum: RSI(14) 56.9 | MACD 0.112 vs signal -0.117 (histogram 0.229)
Returns: 1d -0.2% | 5d +0.7% | 1m +1.6% | 3m -2.5%
52-week range: 88.92 - 97.99 (now 21.7% of the way up)
Volatility: ATR(14) 0.45 (0.5% of price) | annualised 20d 5.3%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Long Government
Yield: 4.1%
Credit quality: AA 100.0% | US government debt 99.7%
Three-year record: +4.2% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.56B
What it is made of: Bonds 99.7%, Cash 0.3%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 35.9% of open interest (5,868,295 contracts)
Change on the week: +2.0% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 146.00M | fund size: 13.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Treasury yields fell modestly across the curve (10‑yr -0.13% week)
- CFTC speculators net short 11.4% of open interest, up 9.2% week‑over‑week
- Analyst coverage thin (2% of fund) but 100% buy rating with +5% price target
- Technicals neutral: price above 20‑day SMA (+1.1%), MACD bullish, volume 0.18× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [Should iShares Russell Mid-Cap ETF (IWR) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/ishares-russell-mid-cap-etf-092001015.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Launched on July 17, 2001, the iShares Russell Mid-Cap ETF (IWR) is a passively managed exchange traded fund designed to provide a broad exposure to the Mid...
- [IWM 261020 279.00C (IWM261020C279000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/IWM261020C279000-US)  
  <sub>Moomoo, 6 hours ago</sub>  
  Track real-time IWM 261020 279.00C (IWM261020C279000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Wall Street’s Structured-Note Strategies Are Moving Into ETFs. Learn What “Least-Of” Means First](https://247wallst.com/investing/etf/2026/10/27/wall-streets-structured-note-strategies-are-moving-into-etfs-learn-what-least-of-means-first/)  
  <sub>24/7 Wall St., 13 hours ago</sub>  
  Wall Street has long used worst-of structured notes to pay investors for a very specific risk, and now that same mechanism is in ETF form.
- [How to Buy SPDR S&P 500 ETF Trust (SPY)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-spy-etf/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  The SPDR S&P 500 ETF Trust, or SPY ETF, is the oldest ETF in the U.S. Learn how to invest in this S&P 500 index fund.
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171324281.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose,...
- [When the Pension Already Covers the Bills at 63, These 3 ETFs Give the Portfolio a Real Job](https://247wallst.com/investing/etf/2026/10/27/when-the-pension-already-covers-the-bills-at-63-these-3-etfs-give-the-portfolio-a-real-job/)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  A pension that covers the bills sounds like the finish line, but it leaves a pile of savings without a clear purpose. Three funds can fix that, and the way...
- [October 27th borrow fees are telling two very different](https://www.kucoin.com/news/insight/GME/6ae15415bbcb52000744d0f6)  
  <sub>KuCoin, 13 hours ago</sub>  
  October 27th borrow fees are telling two very different stories. $GMEU: 23.26%. $GME: 0.41%. Shorting the 2× leveraged GameStop ETF costs roughly 5.
- [AI Funding Worries Ease and Buyers Show Up](https://pro.thestreet.com/market-commentary/ai-funding-worries-ease-and-buyers-show-up)  
  <sub>RealMoney Pro, 18 hours ago</sub>  
  Meta's offering and Anthropic's IPO filing answered questions about where the money will come from.
- [Nasdaq 100 Climbs on Chip Rally, Boeing Sinks 10%: Stock Market Today](https://www.tradingview.com/news/benzinga:5b9bee4bd094b:0-nasdaq-100-climbs-on-chip-rally-boeing-sinks-10-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Chipmakers powered a broad rebound on Wall Street at midday Tuesday, lifting the Nasdaq 100 1.5% as fresh money for the artificial intelligence buildout...
- [Alaska gas prices tomorrow](https://www.coinbase.com/en-de/predictions/event/KXAAAGASDAK-26OCT28)  
  <sub>Coinbase, 5 hours ago</sub>  
  The following are prohibited from trading this contract: Persons who are employed by any of the Source Agencies are not permitted to trade on the Contract.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 280.17 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 277.21 (+1.1%), 50d 284.97 (-1.7%), 200d 278.52 (+0.6%); 50d above 200d
Momentum: RSI(14) 51.8 | MACD -1.814 vs signal -2.917 (histogram 1.103)
Returns: 1d -0.0% | 5d +1.3% | 1m +0.4% | 3m -4.2%
52-week range: 229.11 - 305.09 (now 67.2% of the way up)
Volatility: ATR(14) 3.46 (1.2% of price) | annualised 20d 15.1%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.35 | P/B 2.02 | P/S 1.25 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +20.4% a year | beta to the market 1.27
Cost and size: expense ratio 0.19% | net assets 78.04B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%, Twist Bioscience Corp 0.4%, Moog Inc Class A 0.4%, JFrog Ltd Ordinary Shares 0.4%, 10x Genomics Inc Ordinary Shares - Class A 0.4%
Sector mix: Healthcare 20.9%, Financial services 18.0%, Technology 14.5%, Industrials 13.3%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.89 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.0% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-28 Oppenheimer: main, Outperform -> Outperform
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 11.4% of open interest (466,789 contracts)
Change on the week: +9.2% of open interest
Crowding: 73% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 281.05M | fund size: 78.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, policy shift, or decisive technical break; fund flows flat and fundamentals unchanged.

**Main reasons it gave:**
- 10‑year Treasury yield down 13 bps this week
- LQD price 1.2% above 20‑day SMA, at 50‑day SMA
- Fund flows flat over past month (0% net change)
- Credit composition: 46.7% A, 40.5% BBB

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 104.19 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 102.97 (+1.2%), 50d 104.17 (+0.0%), 200d 107.75 (-3.3%); 50d below 200d
Momentum: RSI(14) 57.8 | MACD 0.072 vs signal -0.198 (histogram 0.270)
Returns: 1d -0.1% | 5d +0.9% | 1m +1.7% | 3m -2.1%
52-week range: 101.83 - 112.92 (now 21.3% of the way up)
Volatility: ATR(14) 0.60 (0.6% of price) | annualised 20d 5.8%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Corporate Bond
Yield: 4.9%
Credit quality: A 46.7%, BBB 40.5%, AA 11.9%, AAA 0.9%
Three-year record: +6.0% a year | beta to the market 1.35
Cost and size: expense ratio 0.14% | net assets 28.27B
What it is made of: Bonds 98.7%, Cash 1.3%, Convertible 0.0%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 293.50M | fund size: 30.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error response body was rejected)

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals not decisive, insider positioning net short, analyst view thin but modestly bullish, fundamentals solid but no catalyst.

**Main reasons it gave:**
- CFTC positioning shows net short 19.2% of open interest, with a +2% increase in net short this week
- Technicals: price above 20‑day, 50‑day, and 200‑day SMAs but volume only 0.28× the 20‑day average
- Analyst coverage thin (1.4% of fund) with 58.3% buy rating, indicating modest bullish bias
- Macro: yields down slightly, VIX up modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Is Invesco S&P 500 Equal Weight Financials ETF (RSPF) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-equal-weight-092002578.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The Invesco S&P 500 Equal Weight Financials ETF (RSPF) made its debut on 11/01/2006, and is a smart beta exchange traded fund that provides broad exposure...
- [Stocks Without AI Are Beating the S&P 500 by 6 Points This Month](https://247wallst.com/investing/2026/10/28/stocks-without-ai-are-beating-the-sp-500-by-6-points-this-month/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Something unusual happened in October: the parts of the market farthest from AI surged while megacap tech stalled, and now a record-breaking gap is sitting...
- [Kevin O'Leary Warns Investors Could Get 'Slaughtered' by Ignoring Diversification, Shares His 5% Stock and 20% Sector Rule](https://www.tradingview.com/news/benzinga:0ec12ddb4094b:0-kevin-o-leary-warns-investors-could-get-slaughtered-by-ignoring-diversification-shares-his-5-stock-and-20-sector-rule/)  
  <sub>TradingView, 7 hours ago</sub>  
  Investor Kevin O'Leary urged investors to limit their exposure to individual stocks and sectors, saying diversification helped shape his returns after...
- [Oct. 27 Has Historically Marked the Stock Market’s Autumn Bottom](https://247wallst.com/investing/2026/10/28/oct-27-has-historically-marked-the-stock-markets-autumn-bottom/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Jim Reid found October 27 historically marks the S&P 500's autumn low, and SPY gained 0.57% as small caps surged over 1%. RSP hedges megacap concentration...
- [Jeff Bezos Says Retirees Should Buy the S&P 500 Instead of AI Stocks — but That Could Be Riskier Than You Think](https://247wallst.com/investing/2026/10/28/jeff-bezos-says-retirees-should-buy-the-sp-500-instead-of-ai-stocks-but-that-could-be-riskier-than-you-think/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Bezos advises retirees to "buy the S&P 500" rather than individual AI stocks, warning that bubbles destroy wealth even when the underlying technology...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 217.16 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 213.90 (+1.5%), 50d 215.13 (+0.9%), 200d 207.57 (+4.6%); 50d above 200d
Momentum: RSI(14) 58.9 | MACD 1.075 vs signal 0.475 (histogram 0.599)
Returns: 1d -0.2% | 5d +0.2% | 1m +3.7% | 3m +0.8%
52-week range: 182.18 - 222.77 (now 86.2% of the way up)
Volatility: ATR(14) 1.90 (0.9% of price) | annualised 20d 9.5%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Large Blend
What it holds: P/E 20.26 | P/B 2.97 | P/S 1.87 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +19.0% a year | beta to the market 0.84
Cost and size: expense ratio 0.20% | net assets 96.06B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.3%, Everpure Inc Class A 0.3%, Illumina Inc 0.3%, CrowdStrike Holdings Inc Class A 0.3%, Revvity Inc 0.3%
Sector mix: Technology 18.0%, Industrials 15.2%, Financial services 13.5%, Healthcare 12.6%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 58.3% | hold 41.7% | sell 0.0% (mean 2.22 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -12.8% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-27 William Blair: down, Outperform -> Market Perform
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-19 Canaccord Genuity: main, Hold -> Hold
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 19.2% of open interest (1,935,470 contracts)
Change on the week: +2.0% of open interest
Crowding: 62% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 155.55M | fund size: 33.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest yield decline, mixed technicals, slight bearish positioning, stable fundamentals.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve this week (e.g., 10-year down 13 bps)
- Positioning shows a modest increase in net short on 2‑year notes (+1.7% OI) with high crowding (93% percentile)
- Technical indicators are mixed: price above 20‑day SMA but below 200‑day SMA, MACD positive but no decisive break
- Fund basics unchanged: short‑government fund with AA credit quality, 3.6% yield and stable expense ratio

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard's All-World ETF Stays Within Reach of Its Peak as Tech Earnings and the Fed Take Centre Sta](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-s-all-world-etf-stays-within-reach-of-its-peak-as-tech-earnings-and-the-fed-take-centre/70425306)  
  <sub>ad-hoc-news.de, 3 hours ago</sub>  
  Vanguard's FTSE All-World ETF drew EUR 641.8M in the week of 19-23 October, the top-selling ETP in Europe, as AI stocks lifted global indexes.
- [U.S.-aligned countries slash Treasury purchases, led by Asia - report](https://seekingalpha.com/news/4658638-us-aligned-countries-slash-treasury-purchases)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Treasury purchases by countries most aligned with the US are down over 60%. Read more.
- [Vanguard's All-World ETF Pulls In €641.8 Million as AI Listing Revives Global Risk Appetite](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-s-all-world-etf-pulls-in-641-8-million-as-ai-listing-revives-global-risk-appetite/70422638)  
  <sub>ad-hoc-news.de, 21 hours ago</sub>  
  Vanguard FTSE All-World ETF rose 0.9% to €171.80 as Anthropic's listing plans lifted risk sentiment; the fund drew €641.8 million in weekly inflows.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.41 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 81.27 (+0.2%), 50d 81.44 (-0.0%), 200d 82.12 (-0.9%); 50d below 200d
Momentum: RSI(14) 54.1 | MACD 0.025 vs signal -0.015 (histogram 0.040)
Returns: 1d -0.1% | 5d +0.1% | 1m +0.3% | 3m -0.7%
52-week range: 81.05 - 83.18 (now 16.7% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.4%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.5%
Three-year record: +4.0% a year | beta to the market 0.24
Cost and size: expense ratio 0.15% | net assets 26.28B
What it is made of: Bonds 99.5%, Cash 0.5%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 28.4% of open interest (4,533,571 contracts)
Change on the week: +1.7% of open interest
Crowding: 93% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 209.30M | fund size: 17.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, modest technicals, slight bearish positioning, solid fundamentals.

**Main reasons it gave:**
- Large speculators net short 35.9% of open interest, up 2% week over week (positioning)
- Fund basics: 4.7% yield, AA credit quality, 100% US government bonds (fundamental)
- US Treasury yields fell slightly across curve; no policy surprise (macro)
- Price above 20‑day SMA, MACD positive, but volume 0.09× 20‑day average (technical)

<details><summary><b>News</b> — score +0.00</summary>

- [A historically awful 5-year TIPS matured Oct. 15. How did it do as an investment?](https://tipswatch.com/2026/10/28/a-historically-awful-5-year-tips-matured-oct-15-how-did-it-do-as-an-investment/)  
  <sub>tipswatch.com, 3 hours ago</sub>  
  David Enna, Tipswatch.com On October 21, 2021, the Treasury offered $19 billion in a new 5-year Treasury Inflation-Protected Security, CUSIP 91282CDC2,...
- [Taiwan's MediaTek Rebounds After Falling Below NT$4,000; Finance Writer Flags 2 ETFs With Over 100% One-Year Returns](https://finance.biggo.com/news/8bb0d72a-18e5-425a-be06-244daefa316f)  
  <sub>BigGo Finance, 11 hours ago</sub>  
  MediaTek shares have fallen sharply from their September 22 intraday high of NT$5480, closing at NT$3960 on October 27—a decline of more than 27% in…
- [Markets.com](https://www.markets.com/ae/quote/tip-h_v)  
  <sub>Markets.com, 22 hours ago</sub>  
  BTC to AED Forecast 2026–2030: Can Bitcoin Hold AED 300,000 as ETF Flows Turn Volatile? Explore the BTC to AED forecast for 2026–2030, including AED 300,000...
- [SPDR S&P 500 ETF Trust: Pivot points](https://www.tipranks.com/news/the-fly/spdr-sp-500-etf-trust-pivot-points-thefly-news-174)  
  <sub>TipRanks, 2 hours ago</sub>  
  The following are the pivot points for the SPDR S&P 500 ETF Trust (SPY). Pivot High: $773.36, Pivot Low: $767.43. These were calculated using the DeMark...
- [Apple’s $2,000 iPhone Duo Faces ‘Crackgate’ Days after Launch](https://www.tipranks.com/news/apples-2000-iphone-duo-faces-crackgate-days-after-launch)  
  <sub>TipRanks, 41 minutes ago</sub>  
  Apple Inc. ($AAPL) is facing an awkward start to its foldable iPhone era. Just days after the $2000 iPhone Duo went on sale, customers began reporting...
- [IBM, USTA announce five-year renewal of partnership](https://www.tipranks.com/news/the-fly/ibm-usta-announce-five-year-renewal-of-partnership-thefly-news)  
  <sub>TipRanks, 40 minutes ago</sub>  
  The USTA and IBM (IBM) announced a five-year renewal of their partnership that will see IBM serve as the Official AI and Cloud Partner of the US Open...
- [Apple’s iPhone Duo Sales ‘Look Promising’ Despite Cracked Screen Problem, Analyst Says Ahead of Q4 Earnings](https://www.tipranks.com/news/apples-iphone-duo-sales-look-promising-despite-cracked-screen-problem-analyst-says-ahead-of-q4-earnings)  
  <sub>TipRanks, 5 hours ago</sub>  
  Over the weekend, iPhone buyers took to social media to complain about cracked screens after purchasing Apple's ($AAPL) new foldable iPhone Duo.
- [OpenAI Turns to Google AI Chips to Diversify Beyond Nvidia](https://www.tipranks.com/news/openai-turns-to-google-ai-chips-to-diversify-beyond-nvidia)  
  <sub>TipRanks, 6 hours ago</sub>  
  OpenAI plans to buy AI chips from Google ($GOOGL), according to The Information, citing a person familiar with the matter. The deal could give OpenAI...
- [Investors Dial Up Yield on Ether: Covered Call ETF YETH Attracts Fresh Cash Despite Short-Term Sell Signal](https://www.tipranks.com/news/cryptocurrencies/investors-dial-up-yield-on-ether-covered-call-etf-yeth-attracts-fresh-cash-despite-short-term-sell-signal)  
  <sub>TipRanks, 14 hours ago</sub>  
  Roundhill Ether Covered Call Strategy ETF saw a fresh burst of investor interest as it logged a $997205 inflow on October 22, 2026, lifting assets under...
- [3 ETFs That Could Outperform, According to AI Analyst](https://www.tipranks.com/news/3-etfs-that-could-outperform-according-to-ai-analyst)  
  <sub>TipRanks, 18 hours ago</sub>  
  Exchange-traded funds (ETFs) remain a convenient way to tap into the long-term growth potential of major American businesses. Notably, three funds stand out...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 106.14 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 105.10 (+1.0%), 50d 105.73 (+0.4%), 200d 108.90 (-2.5%); 50d below 200d
Momentum: RSI(14) 61.7 | MACD 0.246 vs signal 0.022 (histogram 0.224)
Returns: 1d -0.2% | 5d +0.6% | 1m +2.0% | 3m -1.5%
52-week range: 103.98 - 112.03 (now 26.8% of the way up)
Volatility: ATR(14) 0.37 (0.4% of price) | annualised 20d 3.8%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 100.0%
Three-year record: +4.5% a year | beta to the market 0.71
Cost and size: expense ratio 0.18% | net assets 14.23B
What it is made of: Bonds 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 35.9% of open interest (5,868,295 contracts)
Change on the week: +2.0% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 177.70M | fund size: 18.86B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fed expected to hold rates steady (no policy surprise)
- Large speculators net short 34% of open interest, but net short fell 4.2% week‑over‑week (slight bullish shift)
- Technicals: price above 20‑day SMA, RSI 61.9, MACD positive, but volume only 0.11× 20‑day average (weak momentum)
- Fund basics: 5% yield, AA credit quality, low expense ratio 0.15%

<details><summary><b>News</b> — score +0.00</summary>

- [What Is TLT ETF? Price, Yield and How the Fund Works](https://www.vtmarkets.com/discover/what-is-tlt-etf/)  
  <sub>VT Markets, 4 hours ago</sub>  
  What is TLT ETF? It is the iShares 20+ Year Treasury Bond ETF, a fund that holds long-dated US government bonds. Learn how its price reacts to the 20 year...
- [TLT 261028 92.00C (TLT261028C92000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261028C92000-US)  
  <sub>Moomoo, 13 hours ago</sub>  
  Track real-time TLT 261028 92.00C (TLT261028C92000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Time to Extend Bond ETF Duration?](https://etfdb.com/fixed-income-content-hub/time-extend-bond-etf-duration/)  
  <sub>ETF Database, 23 hours ago</sub>  
  Bond markets are flashing levels not seen in close to two decades. The 10-year Treasury yield is hovering around 5%.
- [Fed Likely To Hold Rates Steady, Says Wolfe Research’s Roth — Analysts See Inflation Risks Keeping December Hike In Play](https://www.tradingview.com/news/stocktwits:fce9d8a19094b:0-fed-likely-to-hold-rates-steady-says-wolfe-research-s-roth-analysts-see-inflation-risks-keeping-december-hike-in-play/)  
  <sub>TradingView, 3 hours ago</sub>  
  The Federal Reserve is 'overwhelmingly likely' to leave interest rates unchanged on Wednesday, according to Wolfe Research Chief Economist Stephanie Roth,...
- [This Gold ETF Sees Best Day In Nearly Four Years As Treasury Yields Drop On Bessent's Bond Buyback Move](https://stocktwits.com/news-articles/markets/equity/treasury-yields-drop-on-bessent-s-bond-buyback-move/cZYdoGARJlj)  
  <sub>Stocktwits, 14 hours ago</sub>  
  The U.S. Treasury's plan to double its long-term bond buybacks pulled yields lower, sending spot gold up by $100 and triggering a massive surge in...
- [What Is Driving the 10-Year Yield 4.995% for TLT (NASDAQ:TLT) Holders, and What Might the Market Be Missing?](https://kalkine.com.au/news/general-news/what-is-driving-the-10-year-yield-4995-for-tlt-nasdaqtlt-holders-and-what-might-the-market-be-missing)  
  <sub>Kalkine, 4 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [FOMC is expected to hold on Wednesday, but it's likely not done with rate hikes (TLT:NASDAQ)](https://seekingalpha.com/news/4657973-fomc-is-expected-to-hold-on-wednesday-but-its-likely-not-done-with-rate-hikes)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  The Federal Open Market Committee is widely expected to hold the federal funds rate target range at 3.75%-4.00% when it issues its rate decision on...
- [TLT 261028 64.00P (TLT261028P64000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261028P64000-US)  
  <sub>Moomoo, 18 hours ago</sub>  
  Track real-time TLT 261028 64.00P (TLT261028P64000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Ellsworth Growth and Income Fund Preferred offe...](https://pluang.com/en/news-feed/peluang-yield-saham-preferred-ecf-dan-perbandingan-etf-obligasi-treasury-tlt)  
  <sub>Pluang, 20 hours ago</sub>  
  The Ellsworth Growth and Income Fund Preferred (ECF-A) currently trades below par, presenting a yield-to-worst of nearly 7.2%. Its slower recovery compared...
- [This 7% Preferred From ECF Lagging The Rally In Treasuries (NYSE:ECF)](https://seekingalpha.com/article/4958127-this-7-percent-preferred-from-ecf-lagging-the-rally-in-treasuries)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Ellsworth Growth and Income Fund Preferred offers a 7.2% yield-to-worst and upside potential as spreads narrow. Click to see if now is the entry point.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.44 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 79.28 (+2.7%), 50d 80.55 (+1.1%), 200d 84.69 (-3.8%); 50d below 200d
Momentum: RSI(14) 61.9 | MACD 0.430 vs signal 0.002 (histogram 0.428)
Returns: 1d -0.2% | 5d +1.5% | 1m +4.1% | 3m -1.6%
52-week range: 77.11 - 92.02 (now 29.1% of the way up)
Volatility: ATR(14) 0.76 (0.9% of price) | annualised 20d 10.3%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Long Government
Yield: 5.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +3.1% a year | beta to the market 2.31
Cost and size: expense ratio 0.15% | net assets 46.23B
What it is made of: Bonds 99.6%, Cash 0.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 34.0% of open interest (2,364,949 contracts)
Change on the week: -4.2% of open interest
Crowding: 45% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 109.70M | fund size: 8.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical breakout, modest bullish positioning but mixed fund flows; overall view remains neutral.

**Main reasons it gave:**
- US Treasury yields slipped modestly across the curve this week (3‑month -0.03, 10‑year -0.13) – no rate surprise
- UUP price at 52‑week high (29.14) with low volume (0.10x 20‑day avg) – no decisive breakout
- CFTC speculators net long 6.4% of open interest, up 2.4% OI this week – modest bullish positioning
- Fund inflows +42.5% over the past month, but slight weekly outflow (-0.1%) – mixed demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.14 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 29.00 (+0.5%), 50d 28.54 (+2.1%), 200d 27.91 (+4.4%); 50d above 200d
Momentum: RSI(14) 64.7 | MACD 0.128 vs signal 0.143 (histogram -0.015)
Returns: 1d +0.1% | 5d +0.8% | 1m +1.4% | 3m +3.6%
52-week range: 26.47 - 29.14 (now 100.0% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 5.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +3.6% a year | beta to the market -11.39
Cost and size: expense ratio 0.75% | net assets 431.14M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 1 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 6.4% of open interest (49,382 contracts)
Change on the week: +2.4% of open interest
Crowding: 85% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.1% (-298.98K) over 7d | 1 month: +42.5% (129.30M) over 32d
Shares outstanding: 14.87M | fund size: 433.22M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields down modestly, no rate surprise
- Technical: price below 50‑day SMA, RSI 48 (neutral)
- Positioning: net short 1.5% fell 1.2% week‑over‑week, crowding normal

<details><summary><b>News</b> — score +0.00</summary>

- [5 Best International Stocks to Buy in 2026](https://www.fool.com/investing/stock-market/types-of-stocks/international-stocks/)  
  <sub>The Motley Fool, 24 hours ago</sub>  
  This is a guide to international stocks and what they offer investors. Learn how to track foreign markets and see our top stocks to watch on the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.97 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 86.46 (+0.6%), 50d 88.75 (-2.0%), 200d 87.84 (-1.0%); 50d above 200d
Momentum: RSI(14) 48.0 | MACD -0.405 vs signal -0.600 (histogram 0.194)
Returns: 1d -0.1% | 5d -0.7% | 1m -1.0% | 3m -4.4%
52-week range: 77.90 - 93.19 (now 59.4% of the way up)
Volatility: ATR(14) 0.84 (1.0% of price) | annualised 20d 12.4%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.26 | P/B 2.24 | P/S 1.59 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +19.6% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 37.17B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.5%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Shell PLC 1.8%, Novartis AG Registered Shares 1.7%
Sector mix: Financial services 25.4%, Industrials 19.5%, Healthcare 12.1%, Technology 9.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.6% | hold 32.4% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.5% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 1.5% of open interest (493,553 contracts)
Change on the week: -1.2% of open interest
Crowding: 42% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 282.09M | fund size: 24.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals lack decisive break, analyst coverage thin, positioning slightly less long, flows flat.

**Main reasons it gave:**
- Analyst coverage of top holdings (23.5% weight) is 100% buy with +47.9% price target
- CFTC positioning shows net long 2.1% of open interest, down 0.7% week over week
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs; RSI 31.8 (oversold); volume 0.17× 20‑day average
- Macro: yields modestly down, dollar up 0.61% on week, VIX up 0.7 to 17.34 – no policy surprise
- Fund flows flat over the past month, share count unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [Beyond Brazil’s Turmoil, Emerging Market ETF Opportunity Persists](https://etfdb.com/equity-etf-content-hub/emerging-market-etf-opportunity-persists/)  
  <sub>ETF Database, 1 hour ago</sub>  
  Emerging market equity ETFs came into sharp focus this week, as we were reminded that volatility in the region is often part of the ride.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 56.77 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 58.60 (-3.1%), 50d 59.62 (-4.8%), 200d 58.33 (-2.7%); 50d above 200d
Momentum: RSI(14) 31.8 | MACD -0.847 vs signal -0.626 (histogram -0.221)
Returns: 1d -0.1% | 5d -2.4% | 1m -4.8% | 3m -2.4%
52-week range: 52.42 - 61.44 (now 48.2% of the way up)
Volatility: ATR(14) 0.62 (1.1% of price) | annualised 20d 15.1%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +17.7% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 164.66B
What it is made of: Stocks 95.8%, Cash 4.0%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.7%, Tencent Holdings Ltd 2.8%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.9%, Delta Electronics Inc 0.9%
Sector mix: Technology 33.8%, Financial services 19.5%, Consumer cyclical 9.3%, Industrials 7.5%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +47.9% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 2.1% of open interest (1,051,211 contracts)
Change on the week: -0.7% of open interest
Crowding: 27% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 1.42B | fund size: 80.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Wednesday's big stock stories: What’s likely to move the market in the next trading session](https://www.cnbc.com/2026/10/27/wednesdays-big-stock-stories-whats-likely-to-move-the-market.html)  
  <sub>CNBC, 15 hours ago</sub>  
  ... and Financial News, Stock Quotes, and Market Data and Analysis. Market Data Terms of Use and Disclaimers. Data also provided by Reuters logo.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.64 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 77.10 (+0.7%), 50d 78.15 (-0.7%), 200d 79.56 (-2.4%); 50d below 200d
Momentum: RSI(14) 54.5 | MACD -0.198 vs signal -0.339 (histogram 0.142)
Returns: 1d +0.0% | 5d +0.9% | 1m +0.4% | 3m -2.3%
52-week range: 76.81 - 81.20 (now 18.8% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 4.0%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: High Yield Bond
Yield: 6.1%
Credit quality: BB 58.3%, B 32.6%, Below B 7.9%, BBB 0.7%
Three-year record: +8.4% a year | beta to the market 0.70
Cost and size: expense ratio 0.49% | net assets 16.78B
What it is made of: Bonds 99.5%, Cash 0.3%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 195.60M | fund size: 15.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as macro data shows no surprise, technicals are bearish but not decisive, analyst view is strongly bullish, while fund flows show slight net outflow. The mix of signals leads to a neutral stance.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs, RSI 31, low volume
- Analyst consensus 100% buy on top holdings, weighted price target +41% above current
- Net outflow of -3% over the past month (fund flows)
- Macro data unchanged: yields stable, inflation 3.7%, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 81.98 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 86.78 (-5.5%), 50d 90.66 (-9.6%), 200d 92.12 (-11.0%); 50d below 200d
Momentum: RSI(14) 31.0 | MACD -1.866 vs signal -1.471 (histogram -0.395)
Returns: 1d -1.2% | 5d -6.2% | 1m -4.8% | 3m -14.7%
52-week range: 81.98 - 102.94 (now 0.0% of the way up)
Volatility: ATR(14) 2.07 (2.5% of price) | annualised 20d 33.1%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.92 | P/B 1.57 | P/S 1.21 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +29.8% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 718.85M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 21.7%, YPF SA ADR 10.4%, Vista Energy SAB de CV ADR 7.0%, Grupo Financiero Galicia SA ADR 5.7%, Pampa Energia SA ADR 4.7%
Sector mix: Consumer cyclical 27.8%, Energy 21.2%, Financial services 14.2%, Basic materials 11.8%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.0% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-27 Citigroup: up, Neutral -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-09-01 JP Morgan: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +5.0% (33.92M) over 7d | 1 month: -3.0% (-21.82M) over 32d
Shares outstanding: 8.67M | fund size: 710.36M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals, limited analyst coverage, no clear catalyst.

**Main reasons it gave:**
- Analyst view: 100% buy, +23.8% price target, covering 37.6% of fund
- Fund flows flat: share count unchanged (+0.0% week, +0.0% month)
- Technical: price below 20d/50d/200d SMAs, RSI 42.3, MACD above signal but recent price declines
- Macro: yields down modestly, no rate surprise; inflation 3.7% below Fed target 4.0%
- VIX at 17.34, modestly elevated but no spike

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 117.60 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 120.00 (-2.0%), 50d 122.16 (-3.7%), 200d 123.22 (-4.6%); 50d below 200d
Momentum: RSI(14) 42.3 | MACD -0.344 vs signal -0.580 (histogram 0.236)
Returns: 1d -5.4% | 5d -3.7% | 1m -3.2% | 3m -1.2%
52-week range: 99.40 - 137.69 (now 47.5% of the way up)
Volatility: ATR(14) 2.28 (1.9% of price) | annualised 20d 27.0%
Volume: 1.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +41.6% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.8% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-15 Barclays: main, Overweight -> Overweight
  - TSEM.TA: 2026-09-25 Mizuho: init, ? -> Outperform
  - ESLT.TA: 2026-10-05 Jefferies: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 2.55M | fund size: 299.88M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, modest fund inflows, analyst view modestly bullish but not decisive, technicals lack a clear break.

**Main reasons it gave:**
- No macro surprise: yields up modestly, inflation 3.7% near target, Fed unchanged
- Fund flows flat to modestly positive (+1% week), indicating limited new demand
- Analyst coverage shows 73% buy rating but only +2.2% price target, modest bullishness
- Technicals show price near 52‑week high but RSI neutral (48.4) and MACD slightly negative, low volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.95 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 43.96 (-0.0%), 50d 44.38 (-1.0%), 200d 40.29 (+9.1%); 50d above 200d
Momentum: RSI(14) 48.4 | MACD -0.071 vs signal -0.047 (histogram -0.024)
Returns: 1d -0.4% | 5d -2.5% | 1m -0.6% | 3m +2.8%
52-week range: 32.56 - 45.76 (now 86.3% of the way up)
Volatility: ATR(14) 0.64 (1.5% of price) | annualised 20d 21.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.22 | P/B 2.06 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +37.2% a year | beta to the market 0.64
Cost and size: expense ratio 0.59% | net assets 833.96M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: PKO Bank Polski SA 16.2%, Orlen SA 12.7%, Bank Polska Kasa Opieki SA 7.4%, Powszechny Zaklad Ubezpieczen SA 6.0%, Allegro.EU SA Ordinary Shares 4.9%
Sector mix: Financial services 46.9%, Energy 13.3%, Consumer cyclical 13.2%, Basic materials 6.2%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 73.1% | hold 26.9% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.2% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +1.0% (8.45M) over 7d | 1 month: +0.4% (3.04M) over 32d
Shares outstanding: 19.10M | fund size: 839.45M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: analyst coverage of top holdings is bearish (40.5% sell, price target -8.3%), technicals are modestly bullish but with very low volume, Australian inflation came in slightly above forecast (4.3% vs 4.2%) which is a minor surprise, and fund flows are flat. No clear macro catalyst or decisive technical break is present, so the overall stance remains neutral.

**Main reasons it gave:**
- Australian inflation 4.3% in Sep, 0.1% above forecast (small surprise)
- Analyst coverage of top holdings: 40.5% sell, weighted price target -8.3% (bearish bias)
- Technicals: price above 20d, 50d, 200d SMAs, RSI 59.4, but volume 0.14x 20‑day average (weak conviction)
- Fund flows flat over past week/month (no net inflow/outflow)

<details><summary><b>News</b> — score +0.00</summary>

- [Australia inflation rises to 4.3% in September, exceeding forecasts and RBA target](https://www.tradingview.com/news/seekingalpha:d5a761a45094b:0-australia-inflation-rises-to-4-3-in-september-exceeding-forecasts-and-rba-target/)  
  <sub>TradingView, 10 hours ago</sub>  
  Australia's annual inflation rate accelerated to 4.3% in September 2026 from 4.0% in August, topping market expectations of 4.2% and reaching its highest...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.41 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 28.76 (+2.2%), 50d 29.14 (+0.9%), 200d 28.86 (+1.9%); 50d above 200d
Momentum: RSI(14) 59.4 | MACD 0.118 vs signal 0.005 (histogram 0.113)
Returns: 1d -0.3% | 5d +0.6% | 1m +3.6% | 3m -1.4%
52-week range: 24.95 - 30.43 (now 81.3% of the way up)
Volatility: ATR(14) 0.29 (1.0% of price) | annualised 20d 12.0%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.31 | P/B 2.65 | P/S 3.31 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +16.2% a year | beta to the market 0.98
Cost and size: expense ratio 0.50% | net assets 1.21B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: BHP Group Ltd 15.4%, Commonwealth Bank of Australia 12.6%, National Australia Bank Ltd 6.1%, Westpac Banking Corp 6.0%, ANZ Group Holdings Ltd 5.8%
Sector mix: Financial services 42.0%, Basic materials 25.4%, Consumer cyclical 6.5%, Healthcare 5.6%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -8.3% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 63.60M | fund size: 1.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals lack decisive break, flows flat, analyst view modestly bullish but not enough to shift stance.

**Main reasons it gave:**
- Bank of Canada raised policy rate to 2.5% (policy change, not a surprise)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs but volume only 0.12× 20‑day average (no decisive break)
- Fund flows flat over past week and month (no net inflow/outflow)
- Analyst coverage: 79.8% buy, price target +3.1% (moderate bullish but insufficient to shift overall view)

<details><summary><b>News</b> — score +0.00</summary>

- [Bank of Canada raises policy rate to 2.5%, warns further hikes may be needed (CAD:USD:)](https://seekingalpha.com/news/4658651-bank-of-canada-raises-policy-rate-by-25-basis-points)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Bank of Canada rate decision: see how inflation, trade risks, and policy signals could shape markets and what it means for investors now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.96 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 59.84 (+1.9%), 50d 60.45 (+0.8%), 200d 58.25 (+4.7%); 50d above 200d
Momentum: RSI(14) 57.2 | MACD 0.314 vs signal 0.129 (histogram 0.185)
Returns: 1d -0.1% | 5d -0.6% | 1m +3.4% | 3m +2.0%
52-week range: 49.72 - 62.64 (now 87.0% of the way up)
Volatility: ATR(14) 0.64 (1.1% of price) | annualised 20d 13.9%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.94 | P/B 2.75 | P/S 2.69 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +26.5% a year | beta to the market 0.80
Cost and size: expense ratio 0.50% | net assets 7.02B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.5%, Shopify Inc Registered Shs -A- Subord Vtg 6.0%, Bank of Montreal 3.8%, Bank of Nova Scotia 3.7%
Sector mix: Financial services 39.9%, Energy 17.3%, Basic materials 15.2%, Technology 9.3%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 79.8% | hold 20.2% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.1% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-23 Oppenheimer: main, Outperform -> Outperform
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 94.80M | fund size: 5.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, flat fund flows; analyst view is bullish but limited coverage; fundamentals are solid but not decisive.

**Main reasons it gave:**
- Analyst coverage: 100% buy rating on top holdings, weighted price target +15.6% above current price
- Fund flows: share count flat over the past week and month, indicating no net demand
- Technical indicators: price below 50‑day and 200‑day SMA, low volume, RSI 52.2 (neutral), MACD slightly bullish
- Macro data: yields down modestly, no surprise inflation or employment data, normal upward‑sloping yield curve
- Fundamentals: P/E 14.64, dividend yield 3.6%, 3‑year annual return +21.6% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.15 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 50.60 (+1.1%), 50d 51.61 (-0.9%), 200d 51.50 (-0.7%); 50d above 200d
Momentum: RSI(14) 52.2 | MACD -0.100 vs signal -0.201 (histogram 0.101)
Returns: 1d -0.2% | 5d +0.2% | 1m +1.1% | 3m -2.6%
52-week range: 45.38 - 54.72 (now 61.8% of the way up)
Volatility: ATR(14) 0.64 (1.3% of price) | annualised 20d 13.4%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.64 | P/B 2.82 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +21.6% a year | beta to the market 1.25
Cost and size: expense ratio 0.51% | net assets 947.21M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Spotify Technology SA 9.7%, Investor AB Class B 9.6%, Atlas Copco AB Class A 7.1%, Volvo AB Class B 6.8%, Sandvik AB 5.3%
Sector mix: Industrials 46.3%, Financial services 25.6%, Communication services 13.5%, Technology 6.1%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-23 Morgan Stanley: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 7.65M | fund size: 391.30M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technicals, and bullish analyst view not strong enough to shift the call.

**Main reasons it gave:**
- Analyst ratings: 78.7% buy, weighted price target +19.5% above current price
- Fund flows flat over the past month, indicating no net demand shift
- Technical MACD line above signal but RSI near 50, low volume and recent negative returns
- Macro data unchanged: yields slightly down, no policy surprise, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.56 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 41.22 (+0.8%), 50d 42.38 (-1.9%), 200d 42.25 (-1.6%); 50d above 200d
Momentum: RSI(14) 49.6 | MACD -0.206 vs signal -0.309 (histogram 0.103)
Returns: 1d +0.1% | 5d -0.3% | 1m -0.8% | 3m -3.1%
52-week range: 38.08 - 44.59 (now 53.5% of the way up)
Volatility: ATR(14) 0.48 (1.1% of price) | annualised 20d 13.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +20.9% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.96 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.5% above the current prices
Holdings read: SIE.DE, SAP.DE, ALV.DE, ENR.DE, DTE.DE
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 79.50M | fund size: 3.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals show price below key moving averages with low volume, analyst view is bullish but limited to 53% coverage, and fund flows are flat.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 39.8; volume 0.04× 20‑day average – no bullish break
- Analyst coverage (53% of fund) rates all holdings as Buy with a +22.1% price target – bullish view but limited coverage
- Fund flows flat over the past month; share count unchanged – no net demand
- Macro: US Treasury yields down slightly, no surprise; VIX 17.34 and dollar up 0.61% – no material macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 55.87 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 56.27 (-0.7%), 50d 59.31 (-5.8%), 200d 58.14 (-3.9%); 50d above 200d
Momentum: RSI(14) 39.8 | MACD -1.070 vs signal -1.187 (histogram 0.116)
Returns: 1d +0.0% | 5d -0.8% | 1m -6.2% | 3m -9.4%
52-week range: 50.70 - 63.35 (now 40.9% of the way up)
Volatility: ATR(14) 0.76 (1.4% of price) | annualised 20d 19.2%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.42 | P/B 1.77 | P/S 1.50 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +27.9% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.17B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: UniCredit SpA 18.0%, Intesa Sanpaolo 15.0%, Enel SpA 10.6%, Eni SpA 4.7%, Prysmian SpA 4.7%
Sector mix: Financial services 54.1%, Utilities 16.5%, Industrials 12.0%, Consumer cyclical 8.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.1% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, PRY.MI
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 8.55M | fund size: 477.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals lack a decisive bullish break, modest bullish analyst and positioning signals are offset by thin coverage and modest fundamentals.

**Main reasons it gave:**
- Japan inflation accelerating, reviving BOJ rate‑hike bets (no policy change yet)
- Technicals: price below 20‑day and 50‑day SMAs, RSI 40.4, low volume (no decisive bullish break)
- Analyst view: 100% buy on 5 largest holdings, weighted price target +26.4% (thin coverage 17% of fund)
- Positioning: net long 2.3% of open interest, up 4.7% week‑over‑week (modest bullish crowding)

<details><summary><b>News</b> — score +0.00</summary>

- [Japan Inflation Accelerates: ETFs to Watch Amid Rate Uncertainty](https://www.zacks.com/stock/news/3016214/japan-inflation-accelerates-etfs-to-watch-amid-rate-uncertainty)  
  <sub>Zacks Investment Research, 24 hours ago</sub>  
  Japan's rising inflation has revived BOJ rate-hike bets. Discover how Japanese equity, currency-hedged and yen ETFs could respond to likely policy...
- [AI stocks have rattled U.S. and emerging markets. Japan and Europe could help investors diversify](https://www.cnbc.com/2026/10/27/ai-stocks-japan-europe-diversification.html)  
  <sub>CNBC, 21 hours ago</sub>  
  Turbulence in the tech sector underscores the importance of a more diversified portfolio.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 94.28 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 96.39 (-2.2%), 50d 96.55 (-2.4%), 200d 91.69 (+2.8%); 50d above 200d
Momentum: RSI(14) 40.4 | MACD -0.709 vs signal -0.471 (histogram -0.238)
Returns: 1d -1.0% | 5d -1.5% | 1m -2.3% | 3m +1.1%
52-week range: 79.49 - 99.32 (now 74.6% of the way up)
Volatility: ATR(14) 1.20 (1.3% of price) | annualised 20d 12.5%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.27 | P/B 1.98 | P/S 1.37 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +21.5% a year | beta to the market 0.83
Cost and size: expense ratio 0.49% | net assets 23.53B
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.7%, Toyota Motor Corp 3.3%, Tokyo Electron Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 3.0%, Advantest Corp 3.0%
Sector mix: Industrials 22.8%, Technology 22.0%, Financial services 19.3%, Consumer cyclical 11.1%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.4% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 2.3% of open interest (25,143 contracts)
Change on the week: +4.7% of open interest
Crowding: 28% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 227.85M | fund size: 21.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, modest analyst bullishness, mixed technicals, solid fundamentals but no decisive catalyst.

**Main reasons it gave:**
- Analyst coverage shows 64.8% buy rating for 48.2% of fund weight and price target +3.7% above current price
- Fund flows flat over the past week and month, indicating no net demand
- Technicals show price above 20‑, 50‑ and 200‑day SMAs with RSI 62 and positive MACD, but volume is low and no decisive break
- Macro environment unchanged: yields fell modestly, no surprise data, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 63.06 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 61.17 (+3.1%), 50d 61.56 (+2.4%), 200d 61.74 (+2.1%); 50d below 200d
Momentum: RSI(14) 62.1 | MACD 0.691 vs signal 0.383 (histogram 0.309)
Returns: 1d -0.5% | 5d -0.2% | 1m +5.2% | 3m -1.3%
52-week range: 55.06 - 65.08 (now 79.8% of the way up)
Volatility: ATR(14) 0.63 (1.0% of price) | annualised 20d 13.1%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.08 | P/B 4.13 | P/S 2.67 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +16.6% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.67B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.9%, Novartis AG Registered Shares 12.4%, Nestle SA 11.0%, UBS Group AG Registered Shares 6.4%, ABB Ltd 4.6%
Sector mix: Healthcare 38.0%, Financial services 19.6%, Consumer defensive 13.1%, Industrials 12.3%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.7% above the current prices
Holdings read: ROP.SW, NOVN.SW, NESN.SW, UBSG.SW, ABBN.SW
Recent rating changes among them:
  - UBSG.SW: 2026-04-20 Barclays: up, Underweight -> Equal-Weight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 28.62M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro catalyst, technicals show no decisive break, and fund flows are flat despite bullish analyst coverage.

**Main reasons it gave:**
- No macro news or data surprise reported
- RSI 45.1 and MACD -0.795 vs signal -0.783 indicate neutral momentum
- Price below 20‑day (65.72) and 50‑day (67.15) SMAs, slight above 200‑day (65.00) SMA
- Fund flows flat: 0.0% share count change over 1 week and 1 month

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 65.19 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 65.72 (-0.8%), 50d 67.15 (-2.9%), 200d 65.00 (+0.3%); 50d above 200d
Momentum: RSI(14) 45.1 | MACD -0.795 vs signal -0.783 (histogram -0.012)
Returns: 1d +0.2% | 5d -0.6% | 1m -4.9% | 3m -3.3%
52-week range: 55.33 - 71.61 (now 60.6% of the way up)
Volatility: ATR(14) 0.91 (1.4% of price) | annualised 20d 18.2%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.85 | P/B 2.55 | P/S 1.87 | 3y earnings growth n/a
Yield: 4.2%
Three-year record: +23.8% a year | beta to the market 1.09
Cost and size: expense ratio 0.50% | net assets 710.44M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: ASML Holding NV 23.6%, ING Groep NV 9.1%, Nebius Group NV Shs Class-A- 4.9%, Prosus NV Ordinary Shares - Class N 4.6%, ASM International NV 4.4%
Sector mix: Technology 33.4%, Financial services 21.5%, Consumer defensive 10.4%, Industrials 9.6%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.71</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.71</summary>

```text
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +42.5% above the current prices
Holdings read: ASML.AS, INGA.AS, NBIS, PRX.AS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-10-21 Piper Sandler: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 5.55M | fund size: 361.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bullish analyst view is offset by flat fund flows, unchanged macro backdrop, and no decisive technical break.

**Main reasons it gave:**
- Flat fund flows: 0% share count change over week and month
- No macro surprise: Treasury yields down modestly, no policy shift
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs, low volume, RSI 35.8 (oversold)
- Analyst view: 51.5% buy rating, weighted price target +13.3% above current price

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.70 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 57.93 (-2.1%), 50d 60.18 (-5.8%), 200d 57.94 (-2.1%); 50d above 200d
Momentum: RSI(14) 35.8 | MACD -0.782 vs signal -0.790 (histogram 0.008)
Returns: 1d -1.7% | 5d -2.9% | 1m -5.6% | 3m -7.7%
52-week range: 49.37 - 63.23 (now 52.9% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 16.5%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.94 | P/B 2.15 | P/S 1.78 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +33.8% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 2.38B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.3%, Iberdrola SA 12.8%, Repsol SA 5.0%, CaixaBank SA 4.5%
Sector mix: Financial services 45.6%, Utilities 20.7%, Industrials 14.1%, Technology 5.5%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 55.8% of the fund by weight
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.3% above the current prices
Holdings read: SAN.MC, BBVA.MC, IBE.MC, REP.MC, CABK.MC
Recent rating changes among them:
  - SAN.MC: 2023-11-08 JP Morgan: main, Neutral -> Neutral
  - REP.MC: 2020-01-29 RBC Capital: up, Underperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 37.35M | fund size: 2.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals, strong analyst rating but not enough to outweigh other neutral factors.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +40% price target
- Fund flows flat (0% change in share count over 1 week and 1 month)
- Technical: price below 20‑day and 50‑day SMA, negative MACD, RSI 45.8
- Macro: no rate or data surprise; yields up slightly, upward sloping curve

<details><summary><b>News</b> — score +0.00</summary>

- [AI stocks have rattled U.S. and emerging markets. Japan and Europe could help investors diversify](https://www.cnbc.com/2026/10/27/ai-stocks-japan-europe-diversification.html)  
  <sub>CNBC, 21 hours ago</sub>  
  Turbulence in the tech sector underscores the importance of a more diversified portfolio.
- [Investors in the Brazilian ETF Fund $EWZ have made $0 over the last 21 years. 👀 https://t.co/eGmELP2C0y](https://www.kucoin.com/news/insight/EWZ/6ae18948bbcb52000744d678)  
  <sub>KuCoin, 9 hours ago</sub>  
  Investors in the Brazilian ETF Fund $EWZ have made $0 over the last 21 years. https://t.co/eGmELP2C0y.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 107.92 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 110.80 (-2.6%), 50d 110.20 (-2.1%), 200d 92.96 (+16.1%); 50d above 200d
Momentum: RSI(14) 45.8 | MACD -1.439 vs signal -0.854 (histogram -0.585)
Returns: 1d +0.6% | 5d -1.0% | 1m -5.4% | 3m +14.8%
52-week range: 60.03 - 118.00 (now 82.6% of the way up)
Volatility: ATR(14) 2.29 (2.1% of price) | annualised 20d 28.9%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Greater China Region
What it holds: P/E 28.15 | P/B 4.48 | P/S 2.64 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +43.5% a year | beta to the market 1.26
Cost and size: expense ratio 0.59% | net assets 12.34B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 21.9%, MediaTek Inc 7.2%, Delta Electronics Inc 3.9%, Hon Hai Precision Industry Co Ltd 3.2%, ASE Technology Holding Co Ltd 3.0%
Sector mix: Technology 74.2%, Financial services 14.3%, Basic materials 3.8%, Industrials 2.8%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.1% above the current prices
Holdings read: 2330.TW, 2454.TW, 2308.TW, 2317.TW, 3711.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 85.00M | fund size: 9.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technicals, modest analyst optimism limited to ~37% coverage.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over week and month
- US Treasury yields down modestly (10‑yr -0.13% week) with no policy surprise
- Price above 20‑day SMA (+0.4%) but below 50‑day SMA (-0.9%); volume 0.13x 20‑day average
- Analyst coverage 37.4% of fund, 59% buy rating, price target +16.5% above current price

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.17 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 46.98 (+0.4%), 50d 47.60 (-0.9%), 200d 46.94 (+0.5%); 50d above 200d
Momentum: RSI(14) 48.3 | MACD 0.052 vs signal -0.004 (histogram 0.056)
Returns: 1d -0.0% | 5d -1.1% | 1m +0.7% | 3m -3.1%
52-week range: 41.34 - 49.39 (now 72.4% of the way up)
Volatility: ATR(14) 0.45 (1.0% of price) | annualised 20d 12.6%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.50 | P/B 2.22 | P/S 1.46 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +20.6% a year | beta to the market 0.71
Cost and size: expense ratio 0.50% | net assets 3.67B
What it is made of: Stocks 98.6%, Other 1.1%, Cash 0.4%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 8.9%, AstraZeneca PLC 8.0%, Rolls-Royce Holdings PLC 5.2%, Unilever PLC 4.3%
Sector mix: Financial services 26.1%, Consumer defensive 14.1%, Industrials 13.3%, Healthcare 13.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 37.4% of the fund by weight
Ratings by weight: buy 59.1% | hold 40.9% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
Holdings read: HSBA.L, SHEL.L, AZN.L, RR.L, ULVR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 67.80M | fund size: 3.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals mixed, analyst view bullish but not decisive, flows flat.

**Main reasons it gave:**
- No macro surprise: Treasury yields down slightly, no rate shock
- Technical indicators mixed: price below 50‑day and 200‑day SMA, RSI 49.7, MACD positive but low volume
- Analyst coverage 47.8% of fund, 90.9% buy and +8.2% price target, but not enough to shift stance
- Fund flows flat: share count unchanged over week and month

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 74.06 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 73.49 (+0.8%), 50d 74.45 (-0.5%), 200d 76.14 (-2.7%); 50d below 200d
Momentum: RSI(14) 49.7 | MACD 0.366 vs signal 0.169 (histogram 0.197)
Returns: 1d -1.3% | 5d -2.0% | 1m +2.8% | 3m -4.0%
52-week range: 65.65 - 81.23 (now 54.0% of the way up)
Volatility: ATR(14) 1.24 (1.7% of price) | annualised 20d 17.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +15.4% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.2% above the current prices
Holdings read: GMEXICOB.MX, GFNORTEO.MX, FEMSAUBD.MX, AMXB.MX, WALMEX.MX
Recent rating changes among them:
  - GMEXICOB.MX: 2018-11-12 Citigroup: down, Buy -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 18.90M | fund size: 1.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; fundamentals modestly bullish, but macro and technicals offer no clear catalyst and fund flows are flat.

**Main reasons it gave:**
- US inflation 3.7% above target, market expects 3 quarter-point hikes
- EWY price below 20‑day (166.89) and 50‑day (176.07) SMA, RSI 47.2, no decisive break
- Fund flows flat over past week and month
- Fund fundamentals: low P/E 10.41, high beta 2.48, tech sector 56.9% weight

<details><summary><b>News</b> — score +0.00</summary>

- [EWY: The Memory Cushion That Gives Back More Than It Protects (NYSEARCA:EWY)](https://seekingalpha.com/article/4957860-ewy-the-memory-cushion-that-gives-back-more-than-it-protects?source=generic_rss)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  I view iShares MSCI South Korea ETF through a memory lens, given its concentration in SK hynix and Samsung Electronics. EWY provides a middle-ground memory...
- [iShares MSCI South Korea ETF rated Hold due to limited diversification and uncertain memory chip outlook](https://pluang.com/en/news-feed/ewy-memory-cushion-hold-rating-etf-korea-selatan-sk-hynix-samsung)  
  <sub>Pluang, 23 hours ago</sub>  
  The iShares MSCI South Korea ETF (EWY), heavily concentrated in SK hynix and Samsung Electronics, is viewed mainly through its exposure to memory chip...
- [EWY 261030 153.00P (EWY261030P153000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/EWY261030P153000-US?chain_id=Name1K9-3FXPhg.1kvsu80&global_content=%7B%22promote_id%22%3A13764,%22sub_promote_id%22%3A64,%22f%22%3A%22www.moomoo.com%2Fhans%2Fcommunity%2Fprofile%2F104734695%2Fpost%2Fall%22%7D)  
  <sub>Moomoo, 18 hours ago</sub>  
  Track real-time EWY 261030 153.00P (EWY261030P153000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [KORU: South Korea's Daily Returns, Amplified By A Factor Of 3x (NYSEARCA:KORU)](https://seekingalpha.com/article/4952305-koru-south-koreas-daily-returns-amplified-by-factor-of-3x)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  The Direxion Daily MSCI South Korea Bull 3x ETF carries an F risk grade due to volatility, high churn, concentration, and compounding risk.
- [News by CNBC TV18 on TradingView, 2026-10-28 — cnbctv:2ee8dcd5e094b:0](https://www.tradingview.com/news/cnbctv:2ee8dcd5e094b:0/)  
  <sub>TradingView, 14 hours ago</sub>  
  Investors wary of concentration risk in their portfolios following the latest rout in the artificial intelligence trade could take a look at developed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 163.56 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 166.89 (-2.0%), 50d 176.07 (-7.1%), 200d 162.17 (+0.9%); 50d above 200d
Momentum: RSI(14) 47.2 | MACD -6.850 vs signal -6.679 (histogram -0.171)
Returns: 1d +3.9% | 5d +4.3% | 1m -12.6% | 3m +1.5%
52-week range: 88.53 - 219.20 (now 57.4% of the way up)
Volatility: ATR(14) 6.15 (3.8% of price) | annualised 20d 46.7%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.79 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +43.8% a year | beta to the market 2.48
Cost and size: expense ratio 0.59% | net assets 26.21B
What it is made of: Stocks 96.8%, Cash 3.2%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.8%, SK Square 3.1%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 1.9%
Sector mix: Technology 56.9%, Industrials 16.4%, Financial services 10.9%, Consumer cyclical 4.5%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 5 largest holdings, 54.3% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: 000660.KQ, 005930.KQ, 402340.KQ, 009150.KQ, 105560.KQ
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 75.60M | fund size: 12.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals show a downtrend but no decisive break, macro environment is risk‑off, analyst view is bullish on a subset of holdings, and fund flows are flat.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (downtrend)
- US dollar index up 0.61% on the week; VIX elevated at 17.34 (risk‑off sentiment)
- Analyst coverage of top holdings (43.4% weight) all buy with +33% price target
- Fund flows flat over past week and month (no net demand)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 63.65 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 63.84 (-0.3%), 50d 67.11 (-5.1%), 200d 68.64 (-7.3%); 50d below 200d
Momentum: RSI(14) 43.8 | MACD -0.673 vs signal -0.788 (histogram 0.115)
Returns: 1d -0.6% | 5d -2.6% | 1m -1.9% | 3m -0.7%
52-week range: 60.43 - 81.60 (now 15.2% of the way up)
Volatility: ATR(14) 1.12 (1.8% of price) | annualised 20d 21.1%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.44 | P/B 2.00 | P/S 1.73 | 3y earnings growth n/a
Yield: 7.9%
Three-year record: +26.5% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 473.79M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 12.7%, Gold Fields Ltd 8.7%, Naspers Ltd Class N 8.4%, Firstrand Ltd 7.4%, Standard Bank Group Ltd 6.2%
Sector mix: Basic materials 39.1%, Financial services 34.4%, Consumer cyclical 12.8%, Communication services 6.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.2% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-10-22 Freedom Broker: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 7.90M | fund size: 502.84M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, no decisive technical break, and flat fund flows. Analyst view is bullish but limited to 42.9% coverage; fundamentals are mixed with high valuations but strong past performance.

**Main reasons it gave:**
- Analyst coverage: 100% buy on 42.9% of fund, price target +15.6% above current
- Fund flows: flat share count (0% change) over 1 week and 1 month
- Technical trend: price above 20‑day, 50‑day and 200‑day SMAs, RSI 58, MACD positive but low volume
- Macro: yields down slightly, VIX modestly up, no major data surprise
- Fund basics: high valuation (P/E 31.87) with strong 3‑year return (+19.1% per year)

<details><summary><b>News</b> — score +0.00</summary>

- [The 9 Months That Flipped the AI Agent Fear: Cybersecurity Stocks Surge 120%](https://finance.biggo.com/news/31c81bda-4b0c-4b2b-8ecc-3cc032542181)  
  <sub>BigGo Finance, 4 hours ago</sub>  
  The arrival of the AI agent Claude Cowork fueled fears that the software business model was under threat, sending the IGV ETF down 25% in the first…
- [BlackBerry Rises 5% as CEO Pitches QNX for Robots and Physical AI; Mobileye and Aptiv Edge Higher](https://247wallst.com/investing/2026/10/27/blackberry-rises-5-as-ceo-pitches-qnx-for-robots-and-physical-ai-mobileye-and-aptiv-edge-higher/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  BlackBerry's CEO just told CNBC that QNX has a future beyond cars, and investors sent shares surging well past what the broader software market could match.
- [Form 4 iShares Biotechnology ETF For: 27 October By Investing.com](https://in.investing.com/news/stock-market-news/form-4-ishares-biotechnology-etf-for-27-october-93CH-5658043)  
  <sub>Investing.com India, 18 hours ago</sub>  
  Pricing Supplement dated October 23, 2026. (To the Prospectus dated May 15, 2025, the Prospectus Supplement dated May 15, 2025
- [Exploring Software ETFs: Undervalued Opportunities Amid AI Decline](https://www.rswebsols.com/news/exploring-software-etfs-undervalued-opportunities-in-the-midst-of-the-ai-market-decline/)  
  <sub>RS Web Solutions, 23 hours ago</sub>  
  Discover undervalued software ETFs poised for growth despite the AI market decline. Explore key investment opportunities before the next big surge.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 111.48 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 109.46 (+1.8%), 50d 106.83 (+4.3%), 200d 93.92 (+18.7%); 50d above 200d
Momentum: RSI(14) 58.3 | MACD 1.177 vs signal 1.022 (histogram 0.155)
Returns: 1d -0.3% | 5d +2.4% | 1m +5.9% | 3m +19.5%
52-week range: 74.67 - 116.72 (now 87.5% of the way up)
Volatility: ATR(14) 2.52 (2.3% of price) | annualised 20d 28.5%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 31.87 | P/B 7.50 | P/S 8.53 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +19.1% a year | beta to the market 1.22
Cost and size: expense ratio 0.38% | net assets 13.91B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Palo Alto Networks Inc 9.7%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, CrowdStrike Holdings Inc Class A 8.9%, Microsoft Corp 8.5%, Oracle Corp 6.9%
Sector mix: Technology 93.2%, Communication services 4.2%, Financial services 2.2%, Consumer cyclical 0.3%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
  - PLTR: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - MSFT: 2026-10-26 Oppenheimer: main, Outperform -> Outperform
  - ORCL: 2026-10-26 Wells Fargo: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 12.50M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, modest analyst view on a thin slice, bearish fund outflows, slightly bearish technicals, and modestly weak fundamentals.

**Main reasons it gave:**
- 1-month fund outflows of -10.5% (net redemptions)
- Analyst coverage thin (23.7% of fund) with all-buy rating and +31.4% price target
- Technical indicators below 20‑day, 50‑day, 200‑day SMAs; RSI 44.4, MACD negative
- Macro: yields up modestly, dollar stronger (+0.61% week), VIX elevated (17.34) – no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.71 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 46.82 (-0.2%), 50d 47.95 (-2.6%), 200d 49.23 (-5.1%); 50d below 200d
Momentum: RSI(14) 44.4 | MACD -0.248 vs signal -0.280 (histogram 0.033)
Returns: 1d -0.1% | 5d -1.2% | 1m -0.5% | 3m -6.0%
52-week range: 45.42 - 54.83 (now 13.7% of the way up)
Volatility: ATR(14) 0.49 (1.0% of price) | annualised 20d 16.0%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: India Equity
What it holds: P/E 21.36 | P/B 2.96 | P/S 2.56 | 3y earnings growth n/a
Yield: n/a
Three-year record: +3.2% a year | beta to the market 0.62
Cost and size: expense ratio 0.61% | net assets 5.83B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: HDFC Bank Ltd 6.4%, ICICI Bank Ltd 5.6%, Reliance Industries Ltd 5.4%, Bharti Airtel Ltd 3.9%, Infosys Ltd 2.4%
Sector mix: Financial services 29.7%, Consumer cyclical 12.3%, Industrials 10.2%, Basic materials 8.5%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.4% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.45</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.5% (85.91M) over 7d | 1 month: -10.5% (-683.60M) over 32d
Shares outstanding: 124.98M | fund size: 5.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view offset by bearish fund outflows and slightly negative technicals, with no macro catalyst.

**Main reasons it gave:**
- Analyst view: 100% buy rating with weighted price target +29.3% above current
- Fund flows: -8% net outflow over past month
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 42.7 indicating slight bearish momentum
- Macro: yields up modestly, no policy surprise, VIX 17.34 indicating neutral environment

<details><summary><b>News</b> — score +0.00</summary>

- [IYT vs XTN ETF: Why UPS Has More Weight in One Transportation Fund](https://www.ebc.com/forex/iyt-vs-xtn-etf-holdings-fees-ups-exposure)  
  <sub>EBC Financial Group, 7 hours ago</sub>  
  Compare IYT vs XTN ETF holdings, fees and UPS exposure, and see how their different index weighting methods shape transportation portfolios.
- [Defense Stocks Wrap Up October 27, 2026](https://www.investorideas.com/CO/VWAV/news/2026/10271-defense-stocks-wrap-up-october-27-2026.asp)  
  <sub>Investorideas.com, 17 hours ago</sub>  
  Indian defense stocks rally on DAC approvals while US defense stocks soften on Boeing's 10.74% drop after Q3 results; VisionWave (Nasdaq: VWAV) trades down...
- [Boeing Drops 9% as Commercial Jet Losses Overshadow Positive Cash Flow; GE Aerospace Ticks Up, RTX Holds Steady](https://247wallst.com/investing/2026/10/27/boeing-drops-9-as-commercial-jet-losses-overshadow-positive-cash-flow-ge-aerospace-ticks-up-rtx-holds-steady/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Boeing's latest quarterly report handed investors a surprise that a record backlog and positive cash flow could not paper over, and the commercial jet...
- [General Electric (GE) Sees $17.2 Million in Net ETF Buying on Oct. 26](https://finance.yahoo.com/markets/stocks/articles/general-electric-ge-sees-17-110151303.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs bought $17.2 million of General Electric stock, with 26 funds adding shares against 10 trimming.
- [Where Cramer stands on two beaten-down aerospace stocks — and the one to buy](https://www.cnbc.com/amp/2026/10/27/cramer-ge-aerospace-boeing-stock-selloff.html)  
  <sub>CNBC, 16 hours ago</sub>  
  CNBC's Jim Cramer likes this beaten-down aerospace stock after a post-earnings pullback.
- [Axon Enterprise Stock Climbs 11% On A 6-Day Winning Streak](https://www.trefis.com/stock/axon/articles/620950/axon-enterprise-stock-climbs-11-on-a-6-day-winning-streak/2026-10-28)  
  <sub>Trefis, 7 hours ago</sub>  
  Axon Enterprise (AXON) stock has risen for 6 consecutive trading days, gaining 11.2% over that stretch. That added about $3.4 billion to the company's...
- [Iran war said to cost U.S. military more than $47B](https://seekingalpha.com/news/4658639-iran-war-costs-rise-to-more-than-47b)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Reuters reports the U.S.-Iran war has already cost over $47B, far above Pentagon estimates.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 205.91 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 206.11 (-0.1%), 50d 215.87 (-4.6%), 200d 229.18 (-10.2%); 50d below 200d
Momentum: RSI(14) 42.7 | MACD -2.782 vs signal -3.587 (histogram 0.804)
Returns: 1d -0.2% | 5d +0.1% | 1m -1.6% | 3m -13.5%
52-week range: 198.23 - 253.22 (now 14.0% of the way up)
Volatility: ATR(14) 3.86 (1.9% of price) | annualised 20d 16.1%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 31.87 | P/B 5.88 | P/S 2.95 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +25.1% a year | beta to the market 0.98
Cost and size: expense ratio 0.37% | net assets 12.14B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 21.0%, RTX Corp 16.2%, Boeing Co 7.5%, Howmet Aerospace Inc 4.6%, Lockheed Martin Corp 4.6%
Sector mix: Industrials 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.3% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-28 Wells Fargo: main, Overweight -> Overweight
  - HWM: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - LMT: 2026-10-26 JP Morgan: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.3% (33.98M) over 7d | 1 month: -8.0% (-1.05B) over 32d
Shares outstanding: 58.60M | fund size: 12.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage is offset by flat fund flows, stable macro and no decisive technical break.

**Main reasons it gave:**
- Analyst consensus: 100% buy, weighted price target +26.9% for top holdings covering 51.6% of fund
- Fund flows flat: 0% share count change over 1 week and 1 month
- Technical indicators: price above 20‑day SMA, MACD line above signal, but volume only 0.26× 20‑day average
- Macro environment stable: yields down modestly, no policy or data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [IYT vs XTN ETF: Why UPS Has More Weight in One Transportation Fund](https://www.ebc.com/forex/iyt-vs-xtn-etf-holdings-fees-ups-exposure)  
  <sub>EBC Financial Group, 7 hours ago</sub>  
  Compare IYT vs XTN ETF holdings, fees and UPS exposure, and see how their different index weighting methods shape transportation portfolios.
- [UPS Rises 5% as Q3 Beat Lifts Full-Year Outlook; FedEx Inches Higher](https://247wallst.com/investing/2026/10/27/ups-rises-5-as-q3-beat-lifts-full-year-outlook-fedex-inches-higher/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  UPS just handed investors a beat-and-raise quarter heading into the holiday peak, but a profit stumble in one key segment and months of headwinds from its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.67 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 80.15 (+0.7%), 50d 81.72 (-1.3%), 200d 81.65 (-1.2%); 50d above 200d
Momentum: RSI(14) 50.0 | MACD -0.066 vs signal -0.367 (histogram 0.301)
Returns: 1d -1.8% | 5d +0.9% | 1m +1.5% | 3m -5.0%
52-week range: 68.14 - 90.01 (now 57.3% of the way up)
Volatility: ATR(14) 1.42 (1.8% of price) | annualised 20d 19.3%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 18.90 | P/B 3.94 | P/S 1.34 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +16.0% a year | beta to the market 1.32
Cost and size: expense ratio 0.37% | net assets 1.88B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Union Pacific Corp 17.4%, Uber Technologies Inc 15.1%, CSX Corp 9.3%, Delta Air Lines Inc 4.9%, United Airlines Holdings Inc 4.8%
Sector mix: Industrials 84.1%, Technology 15.9%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.9% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-27 Susquehanna: main, Positive -> Positive
  - UBER: 2026-10-16 Guggenheim: reit, Buy -> Buy
  - CSX: 2026-10-27 Susquehanna: main, Positive -> Positive
  - DAL: 2026-10-12 UBS: main, Buy -> Buy
  - UAL: 2026-10-22 BMO Capital: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 2.80M | fund size: 225.88M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, no decisive technical break, and mixed signals from flows, analyst view, and fundamentals.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 27.9 (downtrend, no decisive break)
- Weekly share count up 3.6% (206.6 M) indicating modest inflow
- Analyst consensus 100% buy on top holdings (32.3% of fund) with +68.9% price target
- Fund fundamentals: low P/E 11.39, dividend yield 2.1% (cheap valuation)
- US macro unchanged: yields down slightly, dollar up 0.61%, no data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [MCHI 261120 48.00P (MCHI261120P48000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/MCHI261120P48000-US?chain_id=Name1K9-3FXPhg.1ldvqc0&global_content=%7B%22promote_id%22%3A%2211927%22,%22sub_promote_id%22%3A%2282%22,%22f%22%3A%22www.moomoo.com%2Fau%2Fhans%2Flearn%2Fdetail-moomoo-vs-cmc-118001-250653083%22%7D)  
  <sub>Moomoo, 11 hours ago</sub>  
  Will China A-shares see big moves as we near Trump-Xi Summit? New ChinaA50 warrants now available! The iShares FTSE China A50 ETF (2823 HK) is a Hong...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 48.90 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 50.95 (-4.0%), 50d 52.70 (-7.2%), 200d 55.87 (-12.5%); 50d below 200d
Momentum: RSI(14) 27.9 | MACD -1.051 vs signal -0.854 (histogram -0.198)
Returns: 1d -0.4% | 5d -2.3% | 1m -6.1% | 3m -11.9%
52-week range: 48.90 - 65.49 (now 0.0% of the way up)
Volatility: ATR(14) 0.61 (1.3% of price) | annualised 20d 17.6%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.39 | P/B 1.33 | P/S 1.31 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +8.3% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 5.99B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.8%, Alibaba Group Holding Ltd Ordinary Shares 9.3%, China Construction Bank Corp Class H 4.3%, Industrial And Commercial Bank Of China Ltd Class H 2.6%, Xiaomi Corp Class B 2.2%
Sector mix: Consumer cyclical 22.5%, Financial services 21.0%, Communication services 18.1%, Technology 11.6%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +68.9% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +3.6% (206.63M) over 7d | 1 month: +2.4% (137.00M) over 32d
Shares outstanding: 121.45M | fund size: 5.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, mixed technicals, and a bullish analyst view that only covers less than half the fund.

**Main reasons it gave:**
- Flat fund flows (0% change over 1 week and 1 month)
- No macro surprise: yields fell slightly, inflation 3.7% in line with expectations
- Technical indicators mixed: price below 20‑day and 50‑day SMA, RSI 48.2, MACD negative
- Analyst view bullish (100% buy, +44% price target) but covers only 44.3% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (Dinari Tokenized ETF) (SMH) Price Prediction for 2026 to 2031](https://www.bybit.com/en/price-prediction/vaneck-semiconductor-etf-dinari-tokenized-etf/)  
  <sub>Bybit, 18 hours ago</sub>  
  SMH Price Prediction 2027. Forecast data for 2027 places VanEck Semiconductor ETF (Dinari Tokenized ETF)'s expected price at approximately $590.75. Historically...
- [VanEck Semiconductor ETF Options Spot-On: On October 27th, 251.18K Contracts Were Traded, With 2 Million Open Interest](https://news.futunn.com/en/post/1002475948/vaneck-semiconductor-etf-options-spot-on-on-october-27th-251)  
  <sub>富途牛牛, 15 hours ago</sub>  
  OnOctober 27th ET, $VanEck Semiconductor ETF(SMH.US)$ had active options trading, with a total trading volume of 251.18K options for the day,...
- [Anthropic’s $750B Compute Ambition Puts SOXX, SMH and AI Infrastructure ETFs in Focus](https://www.tradingview.com/news/benzinga:64ebbbd43094b:0-anthropic-s-750b-compute-ambition-puts-soxx-smh-and-ai-infrastructure-etfs-in-focus/)  
  <sub>TradingView, 22 hours ago</sub>  
  Anthropic reported $16.3 billion in revenue for the first half of 2026. That's up from $1.1 billion a year earlier, according to its preliminary IPO filing.
- [Musk's Neocloud Warning Makes SOXX A Better Buy Than Nvidia, And SMH (NASDAQ:SOXX)](https://seekingalpha.com/article/4958075-musks-neocloud-warning-makes-soxx-a-better-buy-than-nvidia-and-smh)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Nvidia faces neocloud risk as AI cloud debt surges. Discover why NVDA is now a Hold and why SOXX may be the better semiconductor ETF to buy now.
- [My Paper Trading Journey Day 15](https://www.moomoo.com/community/feed/my-paper-trading-journey-day-15-117513909239814)  
  <sub>Moomoo, 22 hours ago</sub>  
  Today I added the Roundhill Memory ETF (DRAM) to my paper-trading portfolio at US$50.425 per share. I already hold SMH, a semiconductor ETF, so I'm i...
- [Q4 2026 Outlook: The Bond Squeeze](https://www.vaneck.com/us/en/blogs/investment-outlook/jan-van-eck-q4-2026-outlook-the-bond-squeeze/)  
  <sub>VanEck, 20 hours ago</sub>  
  The AI trade continues to evolve, but is intact. Rising bond yields are appealing, but because of this are putting downward pressure on other parts of your...
- [S&P 500, Nasdaq Jump On Chipmaker Strength As Investors Eye October Fed Decision — ORCL, HOOD, JBLU, RIVN, SMCI In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-jump-on-chipmaker-strength-as-investors-eye-october-fed-decision/cZUe8u8RB6G)  
  <sub>Stocktwits, 15 hours ago</sub>  
  U.S. stock indices ended higher on Tuesday for the second consecutive session, driven by strong gains in chipmaker stocks as investors await the Federal...
- [Semiconductor stocks in focus after SK Hynix results; Micron, Nvidia top Quant list (SMH:NASDAQ)](https://seekingalpha.com/news/4658784-semiconductor-stocks-in-focus-after-sk-hynix-results-micron-nvidia-top-quant-list)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Memory and AI-related stocks moved higher in premarket trading Wednesday after SK Hynix (SKHY) reported record quarterly profit that beat estimates and...
- [Dow, S&P 500, Nasdaq Futures Mixed Ahead Of Key Tech Results, Fed Rate Decision: SKHY, HOOD, BA, ENPH In Focus](https://www.tradingview.com/news/stocktwits:78f7c11ef094b:0-dow-s-p-500-nasdaq-futures-mixed-ahead-of-key-tech-results-fed-rate-decision-skhy-hood-ba-enph-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures were mixed overnight late Tuesday as Wall Street gears up for key technology results and the much-anticipated Federal Reserve policy...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 563.86 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 577.92 (-2.4%), 50d 573.33 (-1.7%), 200d 517.96 (+8.9%); 50d above 200d
Momentum: RSI(14) 48.2 | MACD -11.410 vs signal -8.787 (histogram -2.623)
Returns: 1d +1.1% | 5d +1.3% | 1m -7.1% | 3m +4.6%
52-week range: 325.10 - 668.91 (now 69.4% of the way up)
Volatility: ATR(14) 16.88 (3.0% of price) | annualised 20d 37.7%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Technology
What it holds: P/E 32.50 | P/B 11.65 | P/S 13.32 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +58.6% a year | beta to the market 2.00
Cost and size: expense ratio 0.35% | net assets 74.88B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 19.3%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.3%, Advanced Micro Devices Inc 5.5%, Broadcom Inc 5.3%, Micron Technology Inc 4.9%
Sector mix: Technology 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +44.0% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - TSM: 2026-10-16 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-28 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
  - MU: 2026-10-22 Rosenblatt: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 11.67M | fund size: 6.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +34.9% price target (bullish)
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs, RSI 25.7 (oversold) but very low volume and no decisive break
- Fund flows flat over the past week and month, indicating neutral demand
- Macro: no surprise in yields, inflation, or policy; normal upward‑sloping yield curve

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 30.71 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 32.91 (-6.7%), 50d 36.43 (-15.7%), 200d 39.08 (-21.4%); 50d below 200d
Momentum: RSI(14) 25.7 | MACD -1.570 vs signal -1.480 (histogram -0.090)
Returns: 1d -0.4% | 5d -4.5% | 1m -11.6% | 3m -18.6%
52-week range: 30.71 - 43.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.62 (2.0% of price) | annualised 20d 24.2%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.69 | P/B 1.02 | P/S 0.63 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: -1.8% a year | beta to the market 0.61
Cost and size: expense ratio 0.59% | net assets 163.33M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.4%, Tupras-Turkiye Petrol Rafineleri AS 10.6%, Bim Birlesik Magazalar AS 10.4%, Akbank TAS 6.1%, Turk Hava Yollari AO 4.8%
Sector mix: Industrials 29.2%, Financial services 16.1%, Consumer defensive 13.9%, Basic materials 11.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.9% above the current prices
Holdings read: ASELS.IS, TUPRS.IS, BIMAS.IS, AKBNK.IS, THYAO.IS
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 15.65M | fund size: 480.61M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage of top holdings is 100% buy with +19.7% price target but only covers 40.5% of fund
- Fund flows flat over the past week and month, indicating no net demand
- Fundamentals show high valuation (P/E 28.36) and yield 3.8% below 10‑year Treasury yield, suggesting limited upside
- Technical indicators show price below 50‑day and 200‑day SMAs, RSI near 50, and no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

- [3 Underrated Vanguard ETFs with 15%+ Upside Potential](https://www.tipranks.com/news/3-underrated-vanguard-etfs-with-15-upside-potential)  
  <sub>TipRanks, 24 hours ago</sub>  
  Vanguard ETFs are often known for their low costs and long-term stability, but not all of them get the attention they deserve. Some lesser-known Vanguard...
- [New home sales fell 0.6% month-over-month in September](https://www.tipranks.com/news/the-fly/new-home-sales-fell-0-6-month-over-month-in-september-thefly-news)  
  <sub>TipRanks, 23 hours ago</sub>  
  New single-family home sales in the U.S. fell 0.6% month-over-month to a seasonally adjusted annual rate of 676000 in September, down from a revised...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.52 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 90.97 (+0.6%), 50d 93.37 (-2.0%), 200d 94.57 (-3.2%); 50d below 200d
Momentum: RSI(14) 47.6 | MACD -0.100 vs signal -0.445 (histogram 0.345)
Returns: 1d -0.9% | 5d +0.0% | 1m +1.1% | 3m -8.0%
52-week range: 87.00 - 100.95 (now 32.4% of the way up)
Volatility: ATR(14) 1.27 (1.4% of price) | annualised 20d 15.1%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.36 | P/B 2.42 | P/S 4.59 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +13.1% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
Sector mix: Real estate 99.5%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.7% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-10-19 Wells Fargo: main, Overweight -> Overweight
  - PLD: 2026-10-26 Truist Securities: main, Buy -> Buy
  - EQIX: 2026-10-21 CIBC: init, ? -> Outperformer
  - AMT: 2026-10-20 Bernstein: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 370.18M | fund size: 33.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, modest positive analyst view on a thin slice, net inflow over the month but weekly outflow, fundamentals are moderate.

**Main reasons it gave:**
- Analyst view: 100% buy rating for top 5 holdings (17% weight) with +15.5% price target
- Fund flows: net inflow of 6.5% over past month (87.48M) indicating demand
- Macro: yields up slightly, upward sloping curve, no surprise in inflation or policy
- Technical: price above 20‑day SMA but below 50‑day SMA, RSI 54.3 (neutral), MACD near zero

<details><summary><b>News</b> — score +0.00</summary>

- [(XHB) Technical Pivots with Risk Controls (XHB:CA)](https://news.stocktradersdaily.com/canada/xhb-technical-pivots-with-risk-controls_20261028_80d51c)  
  <sub>Stock Traders Daily, 6 hours ago</sub>  
  Technical analysis for iShares Canadian HYBrid Corporate Bond Index ETF XHB including support levels resistance levels and stop losses for XHB.
- [Alphabet And Meta Sink Communication Services 10.8%: Oversold? - TalkMarkets](https://t.co/Rr4Rc30Exw)  
  <sub>Howl.Link, 20 hours ago</sub>  
  Communication Services plunged 10.8% in October, hitting deeply oversold territory as Alphabet and Meta falter.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 98.66 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 96.20 (+2.6%), 50d 98.85 (-0.2%), 200d 105.27 (-6.3%); 50d below 200d
Momentum: RSI(14) 54.3 | MACD -0.040 vs signal -0.739 (histogram 0.699)
Returns: 1d -0.5% | 5d +3.2% | 1m +1.7% | 3m -5.6%
52-week range: 92.84 - 121.36 (now 20.4% of the way up)
Volatility: ATR(14) 2.19 (2.2% of price) | annualised 20d 25.1%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 18.56 | P/B 2.09 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +12.8% a year | beta to the market 1.48
Cost and size: expense ratio 0.35% | net assets 1.43B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SharkNinja Inc 3.5%, Cavco Industries Inc 3.4%, Champion Homes Inc 3.4%, Johnson Controls International PLC Registered Shares 3.4%, Wayfair Inc Class A 3.4%
Sector mix: Consumer cyclical 63.4%, Industrials 31.7%, Basic materials 3.2%, Real estate 1.8%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.5% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-10-28 Piper Sandler: main, Overweight -> Overweight
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - JCI: 2026-10-28 Wells Fargo: main, Overweight -> Overweight
  - W: 2026-10-23 RBC Capital: main, Sector Perform -> Sector Perform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -3.9% (-58.12M) over 7d | 1 month: +6.5% (87.48M) over 32d
Shares outstanding: 14.60M | fund size: 1.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst coverage and inflows are offset by bearish technicals and a stable macro backdrop with no surprise catalyst.

**Main reasons it gave:**
- RSI 27.6 indicating oversold condition and price below 20d/50d/200d SMAs
- Weekly share count up 6.1% (1.27B) showing net inflows
- Analyst coverage 90.6% buy with weighted price target +30.3% above current price
- Macro environment stable: yields up modestly, no rate surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Why Meta Is a Good Bet Despite Huge AI Spending: ETFs in Focus](https://www.tradingview.com/news/zacks:1c22cee87094b:0-why-meta-is-a-good-bet-despite-huge-ai-spending-etfs-in-focus/)  
  <sub>TradingView, 4 hours ago</sub>  
  Meta Platforms META is leaving no stone unturned in its efforts to raise funds for its AI ambitions. The company intends to raise up to $95 billion to...
- [Cathie Wood's ARK Loads Up 38,110 Meta Shares Across 3 ETFs Despite Mounting AI Spending Concerns](https://stocktwits.com/news-articles/markets/equity/cathie-wood-s-ark-loads-up-38-110-meta-shares-across-3-et-fs-despite-mounting-ai-spending-concerns/cZxyX6URBxa)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Cathie Wood's ARK Invest loaded up on Meta Platforms (META) shares on Thursday, purchasing 38110 shares across three exchange-traded funds (ETFs) as the...
- [Walt Disney Earnings Preview: What to Expect](https://www.barchart.com/story/news/8498221/walt-disney-earnings-preview-what-to-expect)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Walt Disney will announce its fourth-quarter earnings next month, and analysts expect its EPS to rise over 50%.
- [Reddit Stock Extends A 5-Day Losing Streak To A 12% Loss](https://www.google.com/goto?url=CAESrwEB6zswFfeQP2GJ-NEM-abY_yonyLnXllrH1pS7SuWXc2SMRdidkMn38tGilxLyayMMNqA2C3MdtTfLUHHGGLA84cUXZ3yAZWKojPZhrbPqH-MLIBUXZNXl9xqQMcRnTgTXDTYYFtCmFOOeewGFOg0WpRTmVxN172qE-2fhTfNNglqoCLuQiTWyD4luFI3D9s8hfzhz4s1IHzNkgKjFveahKWxIkcEfRUn2aL-BwJBw)  
  <sub>Trefis, 7 hours ago</sub>  
  Reddit (RDDT) stock has fallen for 5 consecutive trading days, losing 12.3% over that stretch. That erased about $3.7 billion from the company's market...
- [ACHP vs SOXX ETF: Holdings, Fees and Asia Exposure](https://www.ebc.com/forex/achp-vs-soxx-etf-holdings-fees-asia-exposure)  
  <sub>EBC Financial Group, 8 hours ago</sub>  
  Compare ACHP vs SOXX ETF holdings, fees and Asian chip exposure. See how TSMC, SK Hynix, portfolio concentration and trading costs affect risks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 102.85 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 109.35 (-5.9%), 50d 111.12 (-7.5%), 200d 113.07 (-9.0%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -1.998 vs signal -1.120 (histogram -0.878)
Returns: 1d -0.7% | 5d -5.6% | 1m -7.7% | 3m -3.5%
52-week range: 102.85 - 120.08 (now 0.0% of the way up)
Volatility: ATR(14) 1.66 (1.6% of price) | annualised 20d 16.6%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Communications
What it holds: P/E 16.28 | P/B 3.24 | P/S 2.42 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +19.3% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.53B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.2%, Alphabet Inc Class A 11.6%, Alphabet Inc Class C 9.3%, Warner Bros. Discovery Inc Ordinary Shares - Class A 4.9%, The Walt Disney Co 4.5%
Sector mix: Communication services 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.3% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-22 UBS: main, Buy -> Buy
  - GOOGL: 2026-10-22 Citizens: main, Market Outperform -> Market Outperform
  - GOOG: 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +6.1% (1.27B) over 7d | 1 month: +8.8% (1.81B) over 32d
Shares outstanding: 216.94M | fund size: 22.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, mixed inventory signals, modest analyst bullishness, price outlook bearish but likely priced in, flat fund flows

**Main reasons it gave:**
- No macro surprise: yields down modestly, Fed target unchanged
- Energy inventories mixed: crude draw (bullish) vs diesel/gas build (bearish)
- Analyst coverage 91.9% buy, weighted price target +1.3% above current
- EIA forecast of falling oil prices (WTI $100→$86) but market likely priced in
- Fund flows flat, no net inflow/outflow

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Energy Select Sector SPDR ETF (XLE) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLE/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  State Street Energy Select Sector SPDR ETF (XLE) · 0.35% · 9.95% · 20.15% · 52.56% · 54.53% · 137.50% · 485.18%. Key events. Baseline. Advanced chart. Loading...
- [Crude Oil Weekly Outlook: Brent Tests September Highs, WTI Tops $100, and XLE Reclaims 18-Year Resistance](https://www.stonex.com/en-gb/news-and-analysis/crude-oil-weekly-outlook-brent-tests-september-highs-wti-tops-100-and-xle-reclaims-18-year-resistance/)  
  <sub>StoneX, 3 hours ago</sub>  
  Brent crude is testing its September highs, WTI has moved back towards the psychological 100 level, and the energy sector ETF (XLE) has reclaimed its 18...
- [State Street Energy Select Sector SPDR (XLE) Buys $26.1 Million More XOM on Monday](https://finance.yahoo.com/energy/articles/state-street-energy-select-sector-110503197.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Energy Select Sector SPDR ETF (XLE) reported $107.9 million in gross ETF activity on Monday, Oct. 26,...
- [AI’s Unlikely Ally: How Energy Powers the Digital Revolution - VettaFi - Commentaries](https://www.advisorperspectives.com/commentaries/2026/10/28/energy-powers-digital-revolution)  
  <sub>Advisor Perspectives, 3 hours ago</sub>  
  Many investors are fixated on tech and AI ETFs, and for good reason, given how potent AI hype and its subsequent buildout have turned out to be.
- [Oil Hits Six-Month High And The Impact Could Be Felt In Many Aspects Of The Economy (SPY)](https://seekingalpha.com/article/4958099-oil-hits-six-month-and-impact-could-be-felt-in-many-aspects-of-economy)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Brent crude oil surged to a six-month high. Read why energy producers and XLE ETF are positioned to outperform if oil prices remain high.
- [How Midstream/MLPs Diversify Equity & Income Portfolios](https://etfdb.com/energy-infrastructure-content-hub/midstream-mlps-diversify-equity-income-portfolios/)  
  <sub>ETF Database, 24 hours ago</sub>  
  VettaFi discusses how midstream/MLPs can provide diversification benefits in a broad equity portfolio or income portfolio.
- [Royal Caribbean Surges 8% as Earnings Beat Lifts Full-Year Outlook; Norwegian Climbs 3%, Carnival Edges Higher](https://247wallst.com/investing/2026/10/27/royal-caribbean-surges-8-as-earnings-beat-lifts-full-year-outlook-norwegian-climbs-3-carnival-edges-higher/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Royal Caribbean surged 8% after Q3 EPS of $6.57 beat estimates and management raised full-year guidance, while Norwegian trailed with a 3% gain.
- [These energy stocks are trading in overbought territory as earnings season heats up (XLE:NYSEARCA)](https://seekingalpha.com/news/4658894-these-energy-stocks-are-trading-in-overbought-territory-as-earnings-season-heats-up)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Energy stocks are in focus as third-quarter earnings season gets underway, with investors weighing whether recent price momentum across the sector can be...
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Ahead of US Fed Rate Announcement](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-125522610.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 68.40 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 66.46 (+2.9%), 50d 64.70 (+5.7%), 200d 58.51 (+16.9%); 50d above 200d
Momentum: RSI(14) 61.6 | MACD 1.435 vs signal 1.306 (histogram 0.129)
Returns: 1d +0.3% | 5d +0.4% | 1m +11.2% | 3m +16.0%
52-week range: 43.60 - 69.64 (now 95.3% of the way up)
Volatility: ATR(14) 1.37 (2.0% of price) | annualised 20d 21.7%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.51 | P/B 2.47 | P/S 1.70 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +20.9% a year | beta to the market -0.03
Cost and size: expense ratio 0.08% | net assets 39.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.0%, Chevron Corp 18.1%, ConocoPhillips 6.7%, Valero Energy Corp 4.7%, Marathon Petroleum Corp 4.7%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 205.3 million barrels, -3.0 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 104.3 million barrels, +1.7 on the week (a build), 25% percentile over 52 weeks
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 91.9% | hold 8.1% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.3% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-19 Barclays: main, Overweight -> Overweight
  - CVX: 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - COP: 2026-10-20 Susquehanna: main, Positive -> Positive
  - VLO: 2026-10-23 Freedom Broker: down, Hold -> Sell
  - MPC: 2026-10-22 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 186.42M | fund size: 12.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view bullish but limited coverage, flat fund flows, modest technicals, no macro surprise, fundamentals solid but not decisive.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 42.7% of fund, weighted price target +8.8% above current price
- Fund flows flat: 0% share count change over 1 week and 1 month, indicating no net demand
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs with modest momentum but low volume and no decisive break
- Macro: Treasury yields fell slightly, no rate surprise, VIX at 17.34 (moderate), financial sector neutral
- Fundamentals: P/E 15.2, 3‑year return +22.4% per year, yield 1.6%, low expense ratio 0.08%

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Financial Select SPDR (XLF) Bought: Berkshire Leads on Oct. 26](https://finance.yahoo.com/markets/stocks/articles/state-street-financial-select-spdr-110428274.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Financial Select Sector SPDR ETF (XLF) extended its run of across-the-board additions, boosting all...
- [ETFs Bought $17.8 Million of Mastercard (MA) on Oct. 26](https://www.gurufocus.com/news/9146804/etfs-bought-178-million-of-mastercard-ma-on-oct-26)  
  <sub>GuruFocus, 4 hours ago</sub>  
  XLF led ETF activity in Mastercard (MA) on Monday, as 27 ETFs bought shares and 13 sold, producing a net inflow of $17.8 million.
- [Webcast: Beyond Traditional Income: Exploring Autocallable and High Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/16/beyond-traditional-income-exploring-autocallable-and-high-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  As investors seek new sources of income beyond traditional fixed income, derivative-based strategies offer different ways to seek income from equity markets...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171324281.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose,...
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Ahead of US Fed Rate Announcement](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-equity-125522610.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [Daily ETF Flows: Over $1B Flows Into JCPB](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-over-1b-213901655.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Here are the daily ETF fund flows for October 26, 2026.
- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...
- [Sector Update: Financial](https://finance.yahoo.com/markets/stocks/articles/sector-financial-173844202.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Financial stocks were slightly lower in Tuesday afternoon trading, with the NYSE Financial Index dec.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.01 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 55.00 (+1.8%), 50d 55.96 (+0.1%), 200d 53.70 (+4.3%); 50d above 200d
Momentum: RSI(14) 55.7 | MACD 0.176 vs signal -0.028 (histogram 0.204)
Returns: 1d +0.2% | 5d -0.1% | 1m +3.7% | 3m -1.7%
52-week range: 47.81 - 58.56 (now 76.2% of the way up)
Volatility: ATR(14) 0.66 (1.2% of price) | annualised 20d 11.4%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Financial
What it holds: P/E 15.21 | P/B 2.25 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +22.4% a year | beta to the market 0.75
Cost and size: expense ratio 0.08% | net assets 50.97B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.3%, JPMorgan Chase & Co 11.7%, Visa Inc Class A 8.1%, Mastercard Inc Class A 5.9%, Bank of America Corp 4.7%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.2%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.8% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-10-22 UBS: main, Buy -> Buy
  - JPM: 2026-10-15 Citigroup: main, Neutral -> Neutral
  - V: 2026-10-28 Piper Sandler: main, Overweight -> Overweight
  - MA: 2026-10-23 Truist Securities: main, Buy -> Buy
  - BAC: 2026-10-15 Citigroup: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 883.44M | fund size: 49.48B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat (0% net change over past month)
- Analyst coverage of top holdings (25.7% weight) all buy with +26.7% price target
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 46.2; MACD negative
- Macro: Treasury yields down modestly, no rate surprise; VIX up modestly, no major data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Industrial Select SPDR (XLI) Bought: Caterpillar Leads on Oct. 26](https://finance.yahoo.com/markets/stocks/articles/state-street-industrial-select-spdr-110459405.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Industrial Select Sector SPDR ETF (XLI) reported $108.5 million in gross ETF activity on Monday,...
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Ahead of US Fed Rate Announcement](https://www.google.com/goto?url=CAESnwEB6zswFYytM1iMY_f84lL4QsdgyIC1h0s3gGitixIZ4VPdcLqUf50cikpPIz72ylFQb2aonVWypMcqXeUt4WmdYmhVnH74Br_3QkC30uo8KepzUgdvPOcgu5nforZ2duMNLlpPV9OWHtLLrXsauf9sU_VUKJcJjtkcvq7ghDRuho28vDLY98t7bVBu7sMmrTw2t7iK2j25iEHpJc-pj80)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [If You Invested $100 In State Street Technology Select Sector SPDR ETF Stock 20 Years Ago, You Would Have](https://www.benzinga.com/news/26/10/62637093/if-you-invested-100-state-street-technology-select-sector-spdr-etf-stock-20-years-ago-you-would-have)  
  <sub>Benzinga, 19 hours ago</sub>  
  State Street Technology Select Sector SPDR ETF (NYSE:XLK) has outperformed the market over the past 20 years by 6.1% on an annualized basis producing an...
- [State Street Energy Select Sector SPDR ETF (XLE) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLE/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  Find the latest State Street Energy Select Sector SPDR ETF (XLE) stock quote, history, news and other vital information to help you with your stock trading...
- [Growth Leads Sectors In Tuesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62623952/growth-leads-sectors-in-tuesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Seven sectors are higher and four are lower in Tuesday's regular session, with growth and cyclical sectors split across the top three positions.
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171324281.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose,...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [Webcast: Beyond Traditional Income: Exploring Autocallable and High Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/16/beyond-traditional-income-exploring-autocallable-and-high-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  As investors seek new sources of income beyond traditional fixed income, derivative-based strategies offer different ways to seek income from equity markets...
- [General Electric (GE) Sees $17.2 Million in Net ETF Buying on Oc](https://www.gurufocus.com/news/9146806/general-electric-ge-sees-172-million-in-net-etf-buying-on-oct-26)  
  <sub>GuruFocus, 4 hours ago</sub>  
  In Monday's session, 26 ETFs were buying General Electric (GE) shares versus 10 selling, for net buying of $17.2 million by dollar value.
- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 167.61 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 168.09 (-0.3%), 50d 171.16 (-2.1%), 200d 173.25 (-3.3%); 50d below 200d
Momentum: RSI(14) 46.2 | MACD -1.193 vs signal -1.408 (histogram 0.215)
Returns: 1d -0.2% | 5d -0.4% | 1m -0.9% | 3m -6.0%
52-week range: 147.83 - 186.51 (now 51.1% of the way up)
Volatility: ATR(14) 2.47 (1.5% of price) | annualised 20d 14.0%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 27.43 | P/B 6.56 | P/S 2.92 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +21.4% a year | beta to the market 1.01
Cost and size: expense ratio 0.08% | net assets 29.83B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Caterpillar Inc 7.0%, GE Aerospace 6.1%, GE Vernova Inc 4.8%, RTX Corp 4.7%, Deere & Co 3.2%
Sector mix: Industrials 93.4%, Technology 6.1%, Basic materials 0.3%, Consumer cyclical 0.2%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.7% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-26 UBS: main, Neutral -> Neutral
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - GEV: 2026-10-28 Bernstein: reit, Outperform -> Outperform
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - DE: 2026-10-08 JP Morgan: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 136.63M | fund size: 22.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view (100% buy, +24.3% price target) is offset by flat fund flows, unchanged macro backdrop, and mixed technicals (negative MACD, RSI near 50, low volume). No policy surprise or decisive technical break.

**Main reasons it gave:**
- Fund flows flat: 0% change in share count over 1 week and 1 month
- Macro data unchanged: yields down slightly, no policy surprise
- Technical indicators mixed: MACD negative, RSI near 50, low volume
- Analyst view bullish but covers only 49.5% of fund, rating 100% buy, price target +24.3% above current

<details><summary><b>News</b> — score +0.00</summary>

- [If You Invested $100 In State Street Technology Select Sector SPDR ETF Stock 20 Years Ago, You Would Have](https://www.benzinga.com/news/26/10/62637093/if-you-invested-100-state-street-technology-select-sector-spdr-etf-stock-20-years-ago-you-would-have)  
  <sub>Benzinga, 19 hours ago</sub>  
  State Street Technology Select Sector SPDR ETF (NYSE:XLK) has outperformed the market over the past 20 years by 6.1% on an annualized basis producing an...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171324281.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose,...
- [Sector Update: Tech Stocks Gain Late Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-gain-afternoon-195045333.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Tech stocks were higher late Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) rising 1.7% and the State Street SPDR S&P...
- [Sector Update: Tech Stocks Gain Tuesday Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-gain-tuesday-175540101.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Tech stocks were higher Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) rising 1.7% and the State Street SPDR S&P...
- [Growth Leads Sectors In Tuesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62623952/growth-leads-sectors-in-tuesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Seven sectors are higher and four are lower in Tuesday's regular session, with growth and cyclical sectors split across the top three positions.
- [Sector Update: Tech](https://finance.yahoo.com/markets/stocks/articles/sector-tech-192934886.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Tech stocks were higher late Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) rising 1.7% and the State Street SPDR S&P...
- [Exploring Software ETFs: Undervalued Opportunities Amid AI Decline](https://www.rswebsols.com/news/exploring-software-etfs-undervalued-opportunities-in-the-midst-of-the-ai-market-decline/)  
  <sub>RS Web Solutions, 23 hours ago</sub>  
  Discover undervalued software ETFs poised for growth despite the AI market decline. Explore key investment opportunities before the next big surge.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 189.89 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 192.27 (-1.2%), 50d 189.64 (+0.1%), 200d 169.15 (+12.3%); 50d above 200d
Momentum: RSI(14) 49.7 | MACD -1.440 vs signal -0.860 (histogram -0.580)
Returns: 1d +0.2% | 5d +0.7% | 1m -2.4% | 3m +8.1%
52-week range: 127.50 - 202.00 (now 83.7% of the way up)
Volatility: ATR(14) 3.70 (1.9% of price) | annualised 20d 25.1%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 32.04 | P/B 11.88 | P/S 9.26 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +33.3% a year | beta to the market 1.45
Cost and size: expense ratio 0.08% | net assets 127.30B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 15.5%, Apple Inc 13.6%, Microsoft Corp 10.7%, Advanced Micro Devices Inc 5.1%, Broadcom Inc 4.7%
Sector mix: Technology 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.3% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - AAPL: 2026-10-20 MoffettNathanson: main, Neutral -> Neutral
  - MSFT: 2026-10-26 Oppenheimer: main, Outperform -> Outperform
  - AMD: 2026-10-28 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-27 Rosenblatt: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 272.06M | fund size: 51.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, modest technical uptrend with low volume, and strong analyst coverage of top holdings but limited to ~42% of the fund. Overall view remains neutral.

**Main reasons it gave:**
- US Treasury yields slipped modestly across the curve, no policy surprise
- Fund flows flat with 0% share count change over the week
- Technicals show price above 20‑day, 50‑day and 200‑day SMAs but low volume and no decisive breakout
- Analyst coverage of top holdings is 100% buy with a +6.9% price target, covering 41.8% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Staples Select Sector SPDR ETF (XLP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  State Street Consumer Staples Select Sector SPDR ETF (XLP) · -0.68% · 6.20% · 5.84% · 12.19% · 10.01% · 22.63% · 236.81%. Key Events. Baseline. Advanced...
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Ahead of US Fed Rate Announcement](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-125522610.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · -0.36% · 4.97% · 24.90% · 15.75% · 22.42% · 36.33% · 622.14%. Key events. Baseline. Advanced...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-192624407.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) falling 0.9% and the State Street...
- [Webcast: Beyond Traditional Income: Exploring Autocallable and High Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/16/beyond-traditional-income-exploring-autocallable-and-high-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  As investors seek new sources of income beyond traditional fixed income, derivative-based strategies offer different ways to seek income from equity markets...
- [Sector Update: Consumer Stocks Mixed in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-175833031.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) falling 0.9% and the State Street Consumer...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171324281.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose,...
- [What State Street Health Care SPDR (XLV) Bought: Eli Lilly Leads on Oct. 26](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110410745.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) extended its buying streak, adding $340.5 million in ETF...
- [Why Coca-Cola ETFs Are Good Bets After Q3 Earnings Beat](https://finance.yahoo.com/markets/stocks/articles/why-coca-cola-etfs-good-120000658.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Coca-Cola beats Q3 earnings estimates and raises its outlook for the third straight quarter. Explore ETFs offering exposure to the beverage giant.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.95 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 85.18 (+2.1%), 50d 84.49 (+2.9%), 200d 84.39 (+3.0%); 50d above 200d
Momentum: RSI(14) 56.9 | MACD 1.259 vs signal 1.052 (histogram 0.207)
Returns: 1d -0.2% | 5d -0.2% | 1m +6.2% | 3m +1.7%
52-week range: 75.60 - 90.01 (now 78.8% of the way up)
Volatility: ATR(14) 1.22 (1.4% of price) | annualised 20d 19.2%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 23.91 | P/B 4.44 | P/S 1.29 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +12.2% a year | beta to the market 0.48
Cost and size: expense ratio 0.08% | net assets 13.45B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 10.5%, Costco Wholesale Corp 9.2%, Procter & Gamble Co 7.7%, Coca-Cola Co 7.6%, Philip Morris International Inc 6.8%
Sector mix: Consumer defensive 98.5%, Consumer cyclical 1.5%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.9% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-20 Evercore ISI Group: main, Outperform -> Outperform
  - COST: 2026-10-21 CICC: init, ? -> Outperform
  - PG: 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - KO: 2026-10-28 Wells Fargo: main, Overweight -> Overweight
  - PM: 2026-10-26 Argus Research: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 210.17M | fund size: 18.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral; no macro surprise, mixed technicals, flat fund flows, modest fundamentals, bullish analyst view not enough to shift direction.

**Main reasons it gave:**
- Analyst coverage: 80.6% buy, weighted price target +13.3% above current price
- Fund flows flat: 0% change in share count over week and month
- Fundamentals: moderate valuation (P/E 17.86) and 3.1% yield, low beta (0.40)
- Technicals: price above 20‑day and 50‑day SMA but below 200‑day SMA; RSI 61.2, MACD positive
- Macro: yields down slightly, upward‑sloping curve, VIX 17.34 (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [Webcast: Beyond Traditional Income: Exploring Autocallable and High Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/16/beyond-traditional-income-exploring-autocallable-and-high-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  As investors seek new sources of income beyond traditional fixed income, derivative-based strategies offer different ways to seek income from equity markets...
- [State Street Energy Select Sector SPDR ETF (XLE) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLE/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  Find the latest State Street Energy Select Sector SPDR ETF (XLE) stock quote, history, news and other vital information to help you with your stock trading...
- [Growth Leads Sectors In Tuesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62623952/growth-leads-sectors-in-tuesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Seven sectors are higher and four are lower in Tuesday's regular session, with growth and cyclical sectors split across the top three positions.
- [State Street Consumer Staples Select Sector SPDR ETF (XLP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest State Street Consumer Staples Select Sector SPDR ETF (XLP) stock quote, history, news and other vital information to help you with your...
- [Vistra's Quarterly Earnings Preview: What You Need to Know](https://finance.yahoo.com/markets/stocks/articles/vistras-quarterly-earnings-preview-know-161625410.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  With a market cap of $64.8 billion, Vistra Corp. (VST) is an integrated electricity retailer and power generation company, serving customers, businesses,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.78 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 41.61 (+2.8%), 50d 41.78 (+2.4%), 200d 44.30 (-3.4%); 50d below 200d
Momentum: RSI(14) 61.2 | MACD 0.369 vs signal 0.165 (histogram 0.204)
Returns: 1d -0.2% | 5d +1.8% | 1m +7.7% | 3m -4.2%
52-week range: 39.25 - 47.73 (now 41.6% of the way up)
Volatility: ATR(14) 0.60 (1.4% of price) | annualised 20d 16.5%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Utilities
What it holds: P/E 17.86 | P/B 2.04 | P/S 2.49 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +15.8% a year | beta to the market 0.40
Cost and size: expense ratio 0.08% | net assets 21.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: NextEra Energy Inc 12.7%, Southern Co 7.7%, Duke Energy Corp 7.2%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.2%
Sector mix: Utilities 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.3% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-23 Barclays: main, Equal-Weight -> Equal-Weight
  - SO: 2026-10-22 HSBC: init, ? -> Buy
  - DUK: 2026-10-22 HSBC: init, ? -> Hold
  - CEG: 2026-10-27 TD Cowen: main, Buy -> Buy
  - AEP: 2026-10-22 Jefferies: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 163.27M | fund size: 6.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro data: inflation 3.7% and unemployment 4.2% on 2026-09-01, no surprise relative to expectations
- Technical: price 114.92 below 200‑day SMA 115.63, low volume (0.27x 20‑day avg), no decisive break
- Fund flows: 1‑week share count change +0.0%, indicating flat net demand
- Analyst view: 100% buy rating, weighted price target +19.1% above current price, but not enough to outweigh neutral macro/technical

<details><summary><b>News</b> — score +0.00</summary>

- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-172852611.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.9% and the State Street...
- [General Motors Rises 5% on Nasdaq Listing Move and Index Eligibility; Tesla Gains 3%, Ford Edges Higher](https://247wallst.com/investing/2026/10/27/general-motors-rises-5-on-nasdaq-listing-move-and-index-eligibility-tesla-gains-3-ford-edges-higher/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  General Motors is abandoning its historic home on the New York Stock Exchange for a move that has nothing to do with cars and everything to do with which...
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Ahead of US Fed Rate Announcement](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-125522610.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.2% and the actively trad.
- [Sector Update: Consumer Stocks Mixed in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-175833031.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) falling 0.9% and the State Street Consumer...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171324281.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose,...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-194612946.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) falling 1% and the State Street...
- [XLY Nov 2026 111.000 call (XLY261113C00111000) interactive stock chart – Yahoo Finance](https://sg.finance.yahoo.com/quote/XLY261113C00111000/chart/)  
  <sub>Yahoo Finance Singapore, 10 hours ago</sub>  
  Interactive chart for XLY Nov 2026 111.000 call (XLY261113C00111000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 114.92 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 112.86 (+1.8%), 50d 113.30 (+1.4%), 200d 115.63 (-0.6%); 50d below 200d
Momentum: RSI(14) 56.9 | MACD 0.720 vs signal 0.390 (histogram 0.330)
Returns: 1d -0.5% | 5d -0.5% | 1m +5.3% | 3m +2.3%
52-week range: 105.66 - 124.52 (now 49.1% of the way up)
Volatility: ATR(14) 1.57 (1.4% of price) | annualised 20d 14.7%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.00 | P/B 5.56 | P/S 2.32 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +16.5% a year | beta to the market 1.18
Cost and size: expense ratio 0.08% | net assets 21.27B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 23.4%, Tesla Inc 17.7%, The Home Depot Inc 5.0%, McDonald's Corp 4.2%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.7%, Technology 1.3%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.1% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-26 UBS: main, Buy -> Buy
  - TSLA: 2026-10-26 Barclays: up, Equal-Weight -> Overweight
  - HD: 2026-10-26 Stifel: main, Hold -> Hold
  - MCD: 2026-10-26 BTIG: reit, Buy -> Buy
  - TJX: 2026-10-27 B of A Securities: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 120.25M | fund size: 13.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Brazil ETF took in $4.09B in 3 weeks as a bet on one candidate — then it cratered nearly 20% in just one day](https://finance.yahoo.com/markets/stocks/articles/brazil-etf-took-4-09b-125000186.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The iShares MSCI Brazil ETF (NYSE:EWZ) was one of the hottest trades ahead of Brazil's presidential election, as investors bet on a victory for...
- [Beyond Brazil’s Turmoil, Emerging Market ETF Opportunity Persists](https://www.etftrends.com/equity-etf-content-hub/beyond-brazil-turmoil-emerging-market-etf-opportunity-persists/)  
  <sub>ETF Trends, 4 hours ago</sub>  
  Emerging market equity ETFs came into sharp focus this week, as we were reminded that volatility in the region is often part of the ride.
- [Investors in the Brazilian ETF Fund $EWZ have made $0 over the last 21 years. 👀 https://t.co/eGmELP2C0y](https://www.kucoin.com/news/insight/EWZ/6ae18948bbcb52000744d678)  
  <sub>KuCoin, 9 hours ago</sub>  
  Investors in the Brazilian ETF Fund $EWZ have made $0 over the last 21 years. https://t.co/eGmELP2C0y.
- [Brazil ETFs stabilize after historic sell-off as the Lula trade unwinds](https://citywire.com/americas/news/brazil-etfs-stabilize-after-historic-sell-off-as-the-lula-trade-unwinds/a2502030)  
  <sub>Citywire, 12 hours ago</sub>  
  Brazil ETFs plunged after Lula's victory, then partially rebounded on October 27.
- [Pyth Amplifies $218 Million Turnover Claim Tied to BlackRock’s Brazil ETF](https://www.tokenpost.com/news/investing/41948)  
  <sub>TOKENPOST, 20 hours ago</sub>  
  Pyth Network amplified a $218 million turnover figure for perpetual futures tied to BlackRock's Brazil ETF (EWZ); the derivatives-market figure does not...
- [$218M turnover reported in perpetual futures li...](https://pluang.com/en/news-feed/pyth-perkuat-klaim-perputaran-218-juta-blackrock-etf-brazil-ewz)  
  <sub>Pluang, 20 hours ago</sub>  
  Pyth Network reported a $218 million turnover in perpetual futures contracts tied to BlackRock's Brazil ETF (EWZ). This figure reflects trading activity in...
- [Evening Report | A historic plunge](https://www.profarmer.com/pro-farmer-max/evening-report/evening-report-historic-plunge)  
  <sub>Pro Farmer, 16 hours ago</sub>  
  Check our advice monitor at ProFarmer.com for our marketing plan. On Monday, Brazilian equities recorded one of their worst single-day declines in decades...
- [Outflank The Fed: Buy These, Not That (NYSEARCA:EWZ)](https://seekingalpha.com/instablog/71188-chris-lau/6354687-outflank-the-fed-buy-these-not-that)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  DIY Service Reminder: Read the FOMC Rate decision before Wed. at 2 p.m.. Amid the >10 daily stock price alerts at DIY Investing sent to subscribers in a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 33.41 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 40.80 (-18.1%), 50d 38.46 (-13.1%), 200d 37.20 (-10.2%); 50d above 200d
Momentum: RSI(14) 28.9 | MACD -0.561 vs signal 0.625 (histogram -1.185)
Returns: 1d -2.6% | 5d -21.4% | 1m -8.4% | 3m -8.5%
52-week range: 30.92 - 43.54 (now 19.7% of the way up)
Volatility: ATR(14) 1.63 (4.9% of price) | annualised 20d 88.5%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.73 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.9%
Three-year record: +10.1% a year | beta to the market 0.83
Cost and size: expense ratio 0.59% | net assets 8.64B
What it is made of: Stocks 97.5%, Cash 2.0%, Preferred 0.5%
Largest holdings: Vale SA 8.9%, Itau Unibanco Holding SA Participating Preferred 8.4%, Nu Holdings Ltd Ordinary Shares Class A 8.1%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.5%, Petroleo Brasileiro SA Petrobras 7.0%
Sector mix: Financial services 34.4%, Energy 18.1%, Basic materials 13.0%, Utilities 12.8%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +37.4% above the current prices
Holdings read: VALE3.SA, ITUB4, NU, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-10-20 UBS: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 200.55M | fund size: 6.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Q4 2026 Outlook: The Bond Squeeze](https://www.vaneck.com/us/en/blogs/investment-outlook/jan-van-eck-q4-2026-outlook-the-bond-squeeze/)  
  <sub>VanEck, 20 hours ago</sub>  
  The AI trade continues to evolve, but is intact. Rising bond yields are appealing, but because of this are putting downward pressure on other parts of your...
- [GDXJ 261030 132.00C (GDXJ261030C132000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GDXJ261030C132000-US?chain_id=Name1K9-3FXPhg.1ld05s0&global_content=%7B%22promote_id%22%3A14282,%22sub_promote_id%22%3A29,%22f%22%3A%22www.moomoo.com%2Fca%2Fhant%2Flearn%2Finvesting-gold-with-etfs%22%7D)  
  <sub>Moomoo, 22 hours ago</sub>  
  Track real-time GDXJ 261030 132.00C (GDXJ261030C132000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Elliott Wave view: GDX rally expected in at least three waves [Video] | FXStreet](https://twaslnews1.twaslnews.com/6713155/)  
  <sub>شبكة تواصل الإخبارية, 11 hours ago</sub>  
  The short-term Elliott Wave outlook for Gold Miners ETF (GDX) suggests the corrective cycle from the August 26 high has already ended as a seven-swing.
- [Webcast: Beyond Traditional Income: Exploring Autocallable and High Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/16/beyond-traditional-income-exploring-autocallable-and-high-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  As investors seek new sources of income beyond traditional fixed income, derivative-based strategies offer different ways to seek income from equity markets...
- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.globenewswire.com/news-release/2026/10/28/3389994/0/en/yieldmax-etfs-announces-weekly-distributions-for-group-2-etfs.html)  
  <sub>GlobeNewswire, 4 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Oct. 28, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for the YieldMax® Group 2 weekly pay ETFs...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 82.12 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 85.65 (-4.1%), 50d 92.37 (-11.1%), 200d 90.78 (-9.5%); 50d above 200d
Momentum: RSI(14) 40.1 | MACD -2.462 vs signal -2.176 (histogram -0.286)
Returns: 1d -1.3% | 5d -5.3% | 1m -7.8% | 3m +7.0%
52-week range: 68.28 - 115.84 (now 29.1% of the way up)
Volatility: ATR(14) 2.80 (3.4% of price) | annualised 20d 38.9%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 13.93 | P/B 3.18 | P/S 4.54 | 3y earnings growth n/a
Yield: 0.7%
Three-year record: +43.3% a year | beta to the market 0.81
Cost and size: expense ratio 0.51% | net assets 26.25B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Newmont Corp 11.1%, Agnico Eagle Mines Ltd 11.0%, Barrick Mining Corp 7.9%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.2%
Sector mix: Basic materials 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

```text
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.2% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - AEM.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - ABX.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +7.0% (1.73B) over 7d | 1 month: -0.5% (-135.92M) over 32d
Shares outstanding: 324.17M | fund size: 26.62B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Form 4 Invesco KBW Bank ETF For: 27 October By Investing.com](https://uk.investing.com/news/stock-market-news/form-4-invesco-kbw-bank-etf-for-27-october-93CH-4935312)  
  <sub>Investing.com UK, 19 hours ago</sub>  
  Pricing Supplement dated October 23, 2026. (To the Prospectus dated May 15, 2025, the Prospectus Supplement dated May 15, 2025

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 71.98 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 70.40 (+2.2%), 50d 72.06 (-0.1%), 200d 70.93 (+1.5%); 50d above 200d
Momentum: RSI(14) 54.9 | MACD 0.122 vs signal -0.361 (histogram 0.483)
Returns: 1d -0.8% | 5d +1.9% | 1m +3.1% | 3m -5.2%
52-week range: 58.63 - 77.93 (now 69.2% of the way up)
Volatility: ATR(14) 1.22 (1.7% of price) | annualised 20d 17.4%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +25.7% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
Sector mix: Financial services 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

```text
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.5% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-22 TD Cowen: main, Buy -> Buy
  - HWC: 2026-10-21 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EWBC: 2026-10-22 Citigroup: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -4.7% (-181.77M) over 7d | 1 month: -10.0% (-410.76M) over 32d
Shares outstanding: 51.29M | fund size: 3.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: the streamed answer ran past the 480s ceiling (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares MSCI Saudi Arabia ETF Shs Unsponsored Brazilian Depositary Receipt Repr 0.25 Sh](https://www.tradingview.com/symbols/BMFBOVESPA-BKSA39/financials-estimates/)  
  <sub>TradingView, 11 hours ago</sub>  
  See how iShares MSCI Saudi Arabia ETF Shs Unsponsored Brazilian Depositary Receipt Repr 0.25 Sh performed against analyst expectations and compare actual...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 34.67 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 35.33 (-1.9%), 50d 36.93 (-6.1%), 200d 38.00 (-8.8%); 50d below 200d
Momentum: RSI(14) 37.1 | MACD -0.761 vs signal -0.739 (histogram -0.022)
Returns: 1d +0.1% | 5d +0.3% | 1m -4.8% | 3m -6.1%
52-week range: 33.69 - 41.03 (now 13.4% of the way up)
Volatility: ATR(14) 0.37 (1.1% of price) | annualised 20d 16.6%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.08 | P/B 1.70 | P/S 2.84 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +0.4% a year | beta to the market 0.19
Cost and size: expense ratio 0.75% | net assets 588.43M
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.5%, Saudi National Bank 8.6%, Saudi Telecom Co 6.1%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 42.2%, Energy 12.5%, Basic materials 12.4%, Communication services 9.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

```text
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.9% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +3.7% (21.61M) over 7d | 1 month: +1.0% (6.13M) over 32d
Shares outstanding: 17.29M | fund size: 599.61M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  State Street SPDR S&P Biotech ETF (XBI) · 1.04% · -0.12% · 16.39% · 26.99% · 38.76% · 26.69% · 838.42%. Key Events. Baseline. Advanced Chart. Loading...
- [ETFs That You May Consider Amid a Strengthening Biotech Outlook](https://www.zacks.com/stock/news/3017389/etfs-that-you-may-consider-amid-a-strengthening-biotech-outlook)  
  <sub>Zacks Investment Research, 12 minutes ago</sub>  
  Drug innovation, AI and rising M&A activity are boosting biotech optimism. Discover ETFs offering exposure to the sector.
- [XBI 261030 90.00P (XBI261030P90000) Stock Community & Discussion](https://www.moomoo.com/options/XBI261030P90000-US/community)  
  <sub>Moomoo, 20 hours ago</sub>  
  When AstraZeneca and Amgen first announced this lung cancer win, the size of the benefit had not been published. Now it has, and the details deserve a close...
- [AI Funding Worries Ease and Buyers Show Up](https://pro.thestreet.com/market-commentary/ai-funding-worries-ease-and-buyers-show-up)  
  <sub>RealMoney Pro, 18 hours ago</sub>  
  Meta's offering and Anthropic's IPO filing answered questions about where the money will come from.
- [Form 4 iShares Biotechnology ETF For: 27 October By Investing.com](https://in.investing.com/news/stock-market-news/form-4-ishares-biotechnology-etf-for-27-october-93CH-5658043)  
  <sub>Investing.com India, 18 hours ago</sub>  
  Pricing Supplement dated October 23, 2026. (To the Prospectus dated May 15, 2025, the Prospectus Supplement dated May 15, 2025

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 156.52 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 151.26 (+3.5%), 50d 156.97 (-0.3%), 200d 141.32 (+10.8%); 50d above 200d
Momentum: RSI(14) 55.7 | MACD -0.741 vs signal -1.666 (histogram 0.926)
Returns: 1d +1.1% | 5d +2.4% | 1m -0.2% | 3m +3.3%
52-week range: 108.04 - 169.55 (now 78.8% of the way up)
Volatility: ATR(14) 4.32 (2.8% of price) | annualised 20d 34.0%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +31.8% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -12.1% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-27 William Blair: down, Outperform -> Market Perform
  - NTRA: 2026-10-27 BTIG: main, Buy -> Buy
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-23 Oppenheimer: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.8% (-197.67M) over 7d | 1 month: -6.1% (-693.94M) over 32d
Shares outstanding: 68.80M | fund size: 10.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Ten overbought materials stocks to watch during Q3 earnings season (XLB:NYSEARCA)](https://seekingalpha.com/news/4658901-ten-overbought-materials-stocks-to-watch-during-q3-earnings-season)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Materials stocks are in focus as third-quarter earnings season gets underway, with investors assessing whether recent price momentum across the sector can...
- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [General Motors Rises 5% on Nasdaq Listing Move and Index Eligibility; Tesla Gains 3%, Ford Edges Higher](https://247wallst.com/investing/2026/10/27/general-motors-rises-5-on-nasdaq-listing-move-and-index-eligibility-tesla-gains-3-ford-edges-higher/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  General Motors is abandoning its historic home on the New York Stock Exchange for a move that has nothing to do with cars and everything to do with which...
- [Webcast: Beyond Traditional Income: Exploring Autocallable and High Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/16/beyond-traditional-income-exploring-autocallable-and-high-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  As investors seek new sources of income beyond traditional fixed income, derivative-based strategies offer different ways to seek income from equity markets...
- [Growth Leads Sectors In Tuesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62623952/growth-leads-sectors-in-tuesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Seven sectors are higher and four are lower in Tuesday's regular session, with growth and cyclical sectors split across the top three positions.
- [State Street Consumer Staples Select Sector SPDR ETF (XLP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest State Street Consumer Staples Select Sector SPDR ETF (XLP) stock quote, history, news and other vital information to help you with your...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-172852611.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.9% and the State Street...
- [XLY Nov 2026 110.000 call (XLY261120C00110000) interactive stock chart – Yahoo Finance](https://sg.finance.yahoo.com/quote/XLY261120C00110000/chart/)  
  <sub>Yahoo Finance Singapore, 10 hours ago</sub>  
  Interactive chart for XLY Nov 2026 110.000 call (XLY261120C00110000) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.47 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 50.29 (+2.4%), 50d 50.98 (+1.0%), 200d 51.03 (+0.9%); 50d below 200d
Momentum: RSI(14) 59.3 | MACD 0.334 vs signal 0.107 (histogram 0.228)
Returns: 1d -0.6% | 5d +0.3% | 1m +4.8% | 3m -0.3%
52-week range: 42.23 - 53.67 (now 80.8% of the way up)
Volatility: ATR(14) 0.68 (1.3% of price) | annualised 20d 11.5%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Natural Resources
What it holds: P/E 22.69 | P/B 2.70 | P/S 1.78 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +13.2% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 7.78B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Linde PLC 12.2%, Newmont Corp 6.8%, Freeport-McMoRan Inc 5.6%, Ecolab Inc 4.7%, Sherwin-Williams Co 4.7%
Sector mix: Basic materials 83.2%, Consumer cyclical 16.8%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

```text
Rolled up from the 5 largest holdings, 34.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.7% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - NEM: 2026-10-27 Scotiabank: main, Sector Outperform -> Sector Outperform
  - FCX: 2026-10-28 Wells Fargo: main, Overweight -> Overweight
  - ECL: 2026-10-05 UBS: main, Buy -> Buy
  - SHW: 2026-10-28 Guggenheim: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 71.92M | fund size: 3.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 180.85 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 173.92 (+4.0%), 50d 171.82 (+5.3%), 200d 158.40 (+14.2%); 50d above 200d
Momentum: RSI(14) 66.6 | MACD 3.008 vs signal 2.411 (histogram 0.597)
Returns: 1d +0.9% | 5d +1.1% | 1m +5.9% | 3m +10.6%
52-week range: 142.84 - 181.30 (now 98.8% of the way up)
Volatility: ATR(14) 2.83 (1.6% of price) | annualised 20d 18.5%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +14.6% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
Sector mix: Healthcare 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.8% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-10-23 Goldman Sachs: main, Neutral -> Neutral
  - MRK: 2026-10-26 Barclays: main, Overweight -> Overweight
  - UNH: 2026-10-27 Wells Fargo: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 197.42M | fund size: 35.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields down slightly, dollar up, no policy surprise
- Technical: price near 52‑week high, RSI neutral, MACD negative, low volume
- Positioning: net long 21.9% of OI, 98th percentile crowding, slight weekly decrease
- Cost of holding: -8.5% annual roll cost, heavy drag on longs

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.66 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 12.07 (-3.4%), 50d 11.63 (+0.2%), 200d 10.20 (+14.3%); 50d above 200d
Momentum: RSI(14) 45.4 | MACD 0.069 vs signal 0.184 (histogram -0.115)
Returns: 1d +1.1% | 5d -4.8% | 1m +2.6% | 3m +22.4%
52-week range: 9.02 - 12.47 (now 76.5% of the way up)
Volatility: ATR(14) 0.22 (1.9% of price) | annualised 20d 31.0%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.40</summary>

```text
Cost of holding this fund instead of sugar itself: -8.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +22.4%, commodity +34.0%, gap -11.7% | 6 months: fund +17.7%, commodity +31.7%, gap -14.1% | 12 months: fund +25.2%, commodity +33.7%, gap -8.5%
A commodity fund holds futures, not sugar, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 21.9% of open interest (1,210,639 contracts)
Change on the week: -0.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +6.6% (3.33M) over 7d | 1 month: -9.8% (-5.83M) over 32d
Shares outstanding: 4.62M | fund size: 53.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral call; no material macro surprise, technicals are near‑neutral, and behavioural data shows modest bearish tilt but not decisive.

**Main reasons it gave:**
- Positioning: net long decreased 4.9% week‑over‑week
- Cost of holding: -4.1% annual drag
- Fund flows: net outflows of 2.2% over 1 month
- Technical: price 0.8% above 20‑day SMA, RSI 53 (neutral)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 40.02 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 39.70 (+0.8%), 50d 39.81 (+0.5%), 200d 37.88 (+5.7%); 50d above 200d
Momentum: RSI(14) 53.1 | MACD -0.074 vs signal -0.086 (histogram 0.013)
Returns: 1d -0.1% | 5d +1.2% | 1m +0.2% | 3m +1.7%
52-week range: 30.53 - 41.43 (now 87.1% of the way up)
Volatility: ATR(14) 0.57 (1.4% of price) | annualised 20d 18.5%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.10</summary>

```text
Cost of holding this fund instead of copper itself: -4.1% a year -- a steady drag
Measured: 3 months: fund +1.7%, commodity +3.3%, gap -1.6% | 6 months: fund +11.3%, commodity +13.3%, gap -2.0% | 12 months: fund +25.5%, commodity +29.5%, gap -4.1%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 14.6% of open interest (327,119 contracts)
Change on the week: -4.9% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.5% (3.27M) over 7d | 1 month: -2.2% (-16.12M) over 32d
Shares outstanding: 18.12M | fund size: 725.34M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, modest bearish technicals but low volume, slight bearish positioning change, and a small cost‑of‑holding drag. Overall evidence does not justify a directional call.

**Main reasons it gave:**
- Fed policy unchanged, no rate surprise
- Positioning net long down 2.1% week over week
- Technical indicators bearish (RSI 31.8, price below 20‑day SMA) but low volume
- Cost of holding -1.1% annual drag
- Fund flows flat, no net creations/redemptions

<details><summary><b>News</b> — score +0.00</summary>

- [Gold and Silver - actionable measurements](https://www.barchart.com/story/news/8500238/gold-and-silver-actionable-measurements)  
  <sub>Barchart.com, 2 hours ago</sub>  
  Spot gold is trading modestly lower this morning, Wednesday, October 28, 2026, as attention turns to today's Federal Reserve policy decision.
- [SPDR Gold Shares vs. iShares Silver Trust: Looking for an Inflation Hedge? One Could Have the Edge](https://www.fool.com/coverage/etfs/2026/10/28/spdr-gold-shares-vs-ishares-silver-trust-looking-for-an-inflation-hedge-one-could-have-the-edge/)  
  <sub>The Motley Fool, 6 hours ago</sub>  
  Gold and silver have long attracted investors seeking protection against economic uncertainty, but these two popular ETFs offer different opportunities for...
- [Silver prices crash over 26% in 6 months but gain 14% in a year: How silver ETFs fare on 1-, 3- and 5-year returns?](https://www.livemint.com/money/personal-finance/silver-prices-crash-over-26-in-6-months-but-gain-14-in-a-year-how-silver-etfs-fare-on-1-3-and-5-year-returns-11793170700708.html)  
  <sub>Livemint, 7 hours ago</sub>  
  Silver prices have corrected sharply, dragging silver ETFs into the red over six months. However, Tata Silver ETF led one-year returns at 32.41%,...
- [Silver slips 17% in a month: Should investors buy the dip or stay cautious? | Financial Investment](https://www.business-standard.com/finance/investment/silver-price-correction-outlook-investment-strategy-mcx-etf-126102801137_1.html)  
  <sub>Business Standard, 5 hours ago</sub>  
  Higher US real yields, a stronger dollar, weak investment demand and industrial concerns have pressured silver, though experts remain cautiously positive...
- [A Closer Look at Gold Miners & the Leverage Advantage](https://www.etftrends.com/gold-silver-investing-content-hub/closer-look-gold-miners-leverage-advantage/)  
  <sub>ETF Trends, 22 hours ago</sub>  
  Gold is often viewed as a defensive investment, but miners can harness operating leverage to chase stronger gains amid bull markets.
- [Invesco MF launches silver ETF and FoF](https://cafemutual.com/news/nfo/39160-invesco-mf-launches-silver-etf-and-fof)  
  <sub>Cafemutual, 13 hours ago</sub>  
  Invesco Mutual Fund has launched Invesco India Silver ETF and Invesco India Silver ETF Fund of Fund (FoF), the company said in a press release.
- [Silver rate has fallen 50% from its record-high January rate; should you buy now or wait?](https://m.economictimes.com/wealth/invest/silver-rate-price-has-fallen-50-from-its-record-high-january-2026-peak-should-you-invest-now-or-wait/articleshow/135242661.cms)  
  <sub>The Economic Times, 12 hours ago</sub>  
  Silver prices have witnessed a sharp decline in the Multi Commodity Exchange, resulting in considerable losses for investors. Experts believe that a price...
- [Silver Price Today In The UK: October 27, 2026](https://www.forbes.com/advisor/uk/investing/silver-price/)  
  <sub>Forbes, 19 hours ago</sub>  
  Capital at risk. The value of your investments can go up and down, and you may get back less than you invest. Key Takeaways. • The price of silver today,...
- [Silver Rate Today In Meerut Live, Latest Silver Price](https://www.ndtvprofit.com/silver-rates/today-silver-price-in-meerut)  
  <sub>NDTV Profit, 8 hours ago</sub>  
  Track the silver rates today in Meerut with live updates. Check the latest silver prices, daily movements, historical trends, news and key market insights...
- [Gold, silver prices slip ahead of US Fed decision, Israel election results](https://www.business-standard.com/markets/commodities/gold-silver-prices-slip-ahead-of-us-fed-decision-israel-election-results-126102800383_1.html)  
  <sub>Business Standard, 10 hours ago</sub>  
  The Federal Reserve is widely expected to leave interest rates unchanged. However, traders will closely watch for signals on the possibility of a rate...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 48.38 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 52.20 (-7.3%), 50d 56.40 (-14.2%), 200d 64.58 (-25.1%); 50d below 200d
Momentum: RSI(14) 31.8 | MACD -2.102 vs signal -1.824 (histogram -0.278)
Returns: 1d -1.6% | 5d -7.4% | 1m -12.8% | 3m -9.6%
52-week range: 42.70 - 105.60 (now 9.0% of the way up)
Volatility: ATR(14) 1.43 (3.0% of price) | annualised 20d 36.6%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.10</summary>

```text
Cost of holding this fund instead of silver itself: -1.1% a year -- a steady drag
Measured: 3 months: fund -9.6%, commodity -8.8%, gap -0.8% | 6 months: fund -25.4%, commodity -25.1%, gap -0.3% | 12 months: fund +14.1%, commodity +15.2%, gap -1.1%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 3.1% of open interest (113,992 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 341.45M | fund size: 16.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: technicals bearish, macro bearish, positioning net‑long but weakening, fund inflows bullish, crop condition slightly bullish. No clear catalyst, so neutral stance.

**Main reasons it gave:**
- Technical: price below 20‑day and 50‑day SMA, RSI 32.3, low volume
- Macro: dollar up 0.61% week and yields up, indicating bearish pressure
- Positioning: large speculators net long 20.2% but down 3.1% week, weakening bullish sentiment
- Fund flows: share count up 1.3% week, 3.5% month, indicating demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 26.25 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 27.01 (-2.8%), 50d 27.25 (-3.7%), 200d 25.06 (+4.7%); 50d above 200d
Momentum: RSI(14) 32.3 | MACD -0.259 vs signal -0.152 (histogram -0.107)
Returns: 1d -0.1% | 5d -1.3% | 1m -4.9% | 3m +4.2%
52-week range: 21.71 - 28.14 (now 70.6% of the way up)
Volatility: ATR(14) 0.28 (1.1% of price) | annualised 20d 10.2%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

```text
Cost of holding this fund instead of soybeans itself: -0.5% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +4.2%, commodity +5.6%, gap -1.3% | 6 months: fund +6.0%, commodity +5.1%, gap +0.9% | 12 months: fund +15.9%, commodity +16.4%, gap -0.5%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

```text
Soybeans rated good or excellent: 57% of the US crop (week 41 of 2026)
Direction over 3 weeks: steady, -1 points
A better crop means more supply, which reads bearish for the price, and a worse one bullish. The trend matters more than the level, and the market has already seen this: it is published on a schedule everyone trades.
```

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 20.2% of open interest (1,093,612 contracts)
Change on the week: -3.1% of open interest
Crowding: 70% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +1.3% (593.92K) over 7d | 1 month: +3.5% (1.51M) over 32d
Shares outstanding: 1.71M | fund size: 45.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day and 200‑day SMAs (bearish trend)
- Energy inventories: 77 BCF build, 87th percentile (bearish)
- EIA outlook: price forecast down ~18% over 6 months (bearish)
- Cost of holding: -14.3% annual roll cost (tailwind for short)
- Positioning: net short 9.2% OI, short reduced by 1.9% (bullish bias)

<details><summary><b>News</b> — score +0.00</summary>

- [Hedge funds build most bearish bet on U.S. natural gas in over 6 years (UNG:NYSEARCA)](https://seekingalpha.com/news/4657963-hedge-funds-build-most-bearish-bet-on-u-s-natural-gas-in-over-6-years)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  Natural gas traders hold their biggest net short in 6 years as El Niño threatens winter demand.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 9.58 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 10.46 (-8.4%), 50d 10.46 (-8.4%), 200d 11.21 (-14.6%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -0.256 vs signal -0.100 (histogram -0.156)
Returns: 1d -0.6% | 5d -3.9% | 1m -7.4% | 3m -4.3%
52-week range: 9.56 - 16.90 (now 0.3% of the way up)
Volatility: ATR(14) 0.35 (3.6% of price) | annualised 20d 38.2%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.50</summary>

```text
Cost of holding this fund instead of natural gas itself: -14.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -4.3%, commodity +10.6%, gap -14.9% | 6 months: fund -5.6%, commodity +15.3%, gap -20.9% | 12 months: fund -25.7%, commodity -11.4%, gap -14.3%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 9.2% of open interest (1,710,685 contracts)
Change on the week: -1.9% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 12.08M | fund size: 115.77M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no policy surprise, mixed fundamentals (inventory draw bullish vs EIA price outlook bearish), technicals strong but low volume, positioning slightly less net‑long.

**Main reasons it gave:**
- Fed likely to hold rates steady (no policy surprise)
- WTI crude inventories draw 3.1M barrels (bullish) vs EIA price outlook forecasting $100→$86 in 6 months (bearish)
- Technical uptrend above 20d/50d/200d SMAs but low volume (no decisive break)
- Positioning net long 2% of OI with slight weekly reduction (-0.2%) (neutral)

<details><summary><b>News</b> — score +0.00</summary>

- [Fed Likely To Hold Rates Steady, Says Wolfe Research’s Roth — Analysts See Inflation Risks Keeping December Hike In Play](https://www.tradingview.com/news/stocktwits:fce9d8a19094b:0-fed-likely-to-hold-rates-steady-says-wolfe-research-s-roth-analysts-see-inflation-risks-keeping-december-hike-in-play/)  
  <sub>TradingView, 4 hours ago</sub>  
  The Federal Reserve is 'overwhelmingly likely' to leave interest rates unchanged on Wednesday, according to Wolfe Research Chief Economist Stephanie Roth,...
- [U.S. crude stockpiles fell 2M barrels last week, API says (USO:NYSEARCA)](https://seekingalpha.com/news/4658525-u-s-crude-stockpiles-fell-2m-barrels-last-week-api-says)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  The American Petroleum Institute reportedly shows a draw of 2.03M barrels of oil in US commercial stockpiles for the week ending October 23.
- [Trump Says Iran Wants a Deal as 1 Million Barrels of Venezuelan Oil Arrive in Texas Ahead of Midterms: 'I](https://www.benzinga.com/news/politics/26/10/62644224/trump-says-iran-wants-a-deal-as-1-million-barrels-of-venezuelan-oil-arrive-in-texas-ahead-of-midterms-its-a-question-of-when-do-i-want-to-end-it)  
  <sub>Benzinga, 7 hours ago</sub>  
  Trump says Iran wants a deal but Washington controls the timing of any agreements; touts Venezuelan oil gains.
- [Rubio Calls Trump's Russia Diesel Deal 'Very Wise' Amid Soaring Prices — Russian Deputy PM Says Ready To Supply 'As Much As Our Partners Want'](https://stocktwits.com/news-articles/markets/equity/rubio-trump-russia-diesel-deal-very-wise/cZUcvvMRBU8)  
  <sub>Stocktwits, 12 hours ago</sub>  
  According to a report by German news outlet N-TV, Rubio said the move reflects the broader economic impact of conflicts disrupting energy markets.
- [Trump administration discussing Russian deals with U.S. oil firms in Ukraine peace talks - FT](https://seekingalpha.com/news/4658549-trump-administration-discussing-russian-deals-with-us-oil-firms-in-ukraine-peace-talks---ft)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  The US and Russia are discussing a potential return by big American energy companies to the Russian oil market as part of wider talks to end the war in...
- [AI's Biggest Constraint Could Be Capital Availability—Anthropic, Meta And SpaceX Put Markets To The Test](https://www.benzinga.com/opinion/26/10/62632804/ai-biggest-constraint-could-be-capital-availability-anthropic-meta-and-spacex-put-markets-to-the-test)  
  <sub>Benzinga, 20 hours ago</sub>  
  AI Financing Deluge Please click here for an enlarged chart of Direxion Daily Semiconductor Bull 3X ETF (NYSE:SOXL). Note the following: Semiconductors...
- [GPT-6.1 Terra llega a la mitad de precio y con más uso de PC](https://observatorioblockchain.com/inteligencia-artificial/gpt-6-1-terra-mitad-precio-uso-pc/)  
  <sub>Observatorio Blockchain, 8 hours ago</sub>  
  GPT-6.1 Terra cobra 1 dólar por millón de tokens de entrada y 5 de salida, la mitad que GPT-6.1 Sol, y usa el ordenador a la altura de GPT-6 Astra.
- [Intercambio internacional fortalece capacidades de Chile para avanzar en transparencia climática](https://mma.gob.cl/intercambio-internacional-fortalece-capacidades-de-chile-para-avanzar-en-transparencia-climatica/)  
  <sub>MMA – Ministerio del Medio Ambiente, 21 hours ago</sub>  
  Equipos técnicos de los proyectos CBIT-2 y BTR-2 “Transparencia Climática en Acción”, liderados por el Ministerio del Medio Ambiente y apoyados técnicamente...
- [PIMCO 1-5 Year US TIPS Index Exchange-Traded Fund Shs Unsponsored Brazilian Depositary Receipt Repr 0.2 Sh](https://es.tradingview.com/symbols/BMFBOVESPA-BSTP39/financials-estimates/?category=cash_flow)  
  <sub>TradingView, 22 hours ago</sub>  
  Analice los datos financieros publicados y las estimaciones de los analistas en la cuenta de resultados, el balance de situación, el estado de flujos de...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 167.67 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 155.69 (+7.7%), 50d 148.68 (+12.8%), 200d 123.03 (+36.3%); 50d above 200d
Momentum: RSI(14) 65.9 | MACD 5.472 vs signal 4.556 (histogram 0.916)
Returns: 1d +2.3% | 5d +4.9% | 1m +17.0% | 3m +31.5%
52-week range: 66.17 - 169.53 (now 98.2% of the way up)
Volatility: ATR(14) 4.94 (2.9% of price) | annualised 20d 29.9%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 205.3 million barrels, -3.0 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 104.3 million barrels, +1.7 on the week (a build), 25% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 2.0% of open interest (1,835,144 contracts)
Change on the week: -0.2% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 119.10M | fund size: 19.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show bearish trend but no decisive break, positioning shows a modest bullish shift, heavy cost of holding is a tailwind for shorts, and fund flows indicate net outflows. Mixed signals lead to a neutral stance.

**Main reasons it gave:**
- Technical trend: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 20.4 indicating oversold momentum
- Positioning: large speculators net short 10.1% of OI, net short decreased by 3.6% OI this week (bullish shift)
- Cost of holding: -8.8% annual cost, heavy carry tailwind for short positions
- Fund flows: net outflows over past month (-10.7% share count), indicating bearish sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat Pushes Losses to Tuesday](https://www.barchart.com/story/news/8488355/wheat-pushes-losses-to-tuesday)  
  <sub>Barchart.com, 17 hours ago</sub>  
  The wheat complex is falling lower across the three markets on Tuesday. Chicago SRW contracts were 1 to 7 cents in the red at the close.
- [Wheat Facing Losses on Tuesday](https://www.barchart.com/story/news/8482125/wheat-facing-losses-on-tuesday)  
  <sub>Barchart.com, 22 hours ago</sub>  
  The wheat complex is falling lower across the three markets on Tuesday. Chicago SRW contracts are 2 to 3 cents in the red. KC HRW futures are 7 to 8 cents...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 22.10 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 23.94 (-7.7%), 50d 25.33 (-12.7%), 200d 23.51 (-6.0%); 50d above 200d
Momentum: RSI(14) 20.4 | MACD -0.810 vs signal -0.635 (histogram -0.175)
Returns: 1d -1.1% | 5d -4.3% | 1m -11.8% | 3m -10.2%
52-week range: 19.88 - 28.00 (now 27.3% of the way up)
Volatility: ATR(14) 0.44 (2.0% of price) | annualised 20d 16.3%
Volume: 1.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.30</summary>

```text
Cost of holding this fund instead of wheat itself: -8.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -10.2%, commodity -9.8%, gap -0.4% | 6 months: fund -10.2%, commodity -6.8%, gap -3.4% | 12 months: fund +5.0%, commodity +13.8%, gap -8.8%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 10.1% of open interest (516,379 contracts)
Change on the week: -3.6% of open interest
Crowding: 53% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +5.8% (15.34M) over 7d | 1 month: -10.7% (-33.22M) over 32d
Shares outstanding: 12.60M | fund size: 278.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [How To Invest In Commodities As Corn And Wheat Prices Shift](https://www.forbes.com/sites/investor-hub/article/how-to-invest-in-agricultural-commodities-as-corn-wheat-prices-shift/)  
  <sub>Forbes, 4 hours ago</sub>  
  As corn and wheat prices shift, learn how to invest in agricultural commodities through ETFs, futures and top agribusiness stocks to hedge against...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 17.52 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 18.31 (-4.3%), 50d 19.18 (-8.6%), 200d 18.18 (-3.6%); 50d above 200d
Momentum: RSI(14) 26.6 | MACD -0.465 vs signal -0.390 (histogram -0.075)
Returns: 1d +0.5% | 5d -2.5% | 1m -10.1% | 3m -1.3%
52-week range: 16.47 - 20.29 (now 27.5% of the way up)
Volatility: ATR(14) 0.25 (1.4% of price) | annualised 20d 15.3%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

```text
Cost of holding this fund instead of corn itself: -7.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -1.3%, commodity +1.4%, gap -2.7% | 6 months: fund -7.0%, commodity -3.1%, gap -3.9% | 12 months: fund -1.9%, commodity +5.4%, gap -7.4%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 43 of 2026)
Direction over 3 weeks: steady, 0 points
A better crop means more supply, which reads bearish for the price, and a worse one bullish. The trend matters more than the level, and the market has already seen this: it is published on a schedule everyone trades.
```

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 9.0% of open interest (1,835,658 contracts)
Change on the week: -4.4% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.3% (2.85M) over 7d | 1 month: -11.4% (-16.68M) over 32d
Shares outstanding: 7.39M | fund size: 129.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Gold, Bonds, Or Both? 55 Years Of Data Suggest About 20% In Gold (NYSEARCA:GLD)](https://seekingalpha.com/article/4958420-gold-bonds-or-both-55-years-of-data-suggest-about-20-percent-in-gold)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Over 1971–2025, a 20–30% gold allocation alongside U.S. equities improved risk-adjusted returns at no cost in returns. Treasuries reduced volatility, but at...
- [GLD 261027 388.00C (GLD261027C388000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GLD261027C388000-US?chain_id=Name1K9-3FXPhg.1ldanc0&global_content=%7B%22promote_id%22%3A13643,%22sub_promote_id%22%3A47,%22f%22%3A%22www.moomoo.com%2Fsg%2Flearn%2Fdetail-top-financial-institutions-117766-251071039%22%7D)  
  <sub>Moomoo, 12 hours ago</sub>  
  Stock Market · Options Market · Futures Market · ETF Market · Forex Market. Technical Tools. Stock Screener · Heat Map · Earnings Calendar...
- [This Gold ETF Sees Best Day In Nearly Four Years As Treasury Yields Drop On Bessent's Bond Buyback Move](https://stocktwits.com/news-articles/markets/equity/treasury-yields-drop-on-bessent-s-bond-buyback-move/cZYdoGARJlj)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The U.S. Treasury's plan to double its long-term bond buybacks pulled yields lower, sending spot gold up by $100 and triggering a massive surge in...
- [GLD 261027 364.00C (GLD261027C364000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GLD261027C364000-US)  
  <sub>Moomoo, 12 hours ago</sub>  
  SPDR Gold ETF (GLD) News. As gold prices return to the $4,000 level, JPMorgan states that the allocation value of gold has become more prominent following...
- [GLD NTA 27-10-2026 $3.73256](https://www.businessdesk.co.nz/nzx-announcements/gld-etf-units/482512)  
  <sub>BusinessDesk, 16 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 27-10-2026 $3.73256. Financial updates and company disclosures on BusinessDesk.
- [eToro USA @etorous: "Anthropic Proposed IPO Sparks Tech..."](https://www.etoro.com/posts/68d14a20-d227-11f1-8080-80005a89758f)  
  <sub>eToro, 22 hours ago</sub>  
  Anthropic Proposed IPO Sparks Tech Rebound Daily Breakdown from Bret Kenwell @Bretman, etoro's Investment and Options Analyst Tuesday, October 27,...
- [Buy SLV: Unsustainable Global Debt And Rising Contagion Risks (NYSEARCA:SLV)](https://seekingalpha.com/article/4958348-buy-slv-unsustainable-global-debt-and-rising-contagion-risks)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  SLV has returned to levels where it once again represents an attractive setup for a higher bullish trade. Read more on the SLV ETF here.
- [Gold needs to build a floor or face further losses, Standard Chartered’s Cooper says (GLD:NYSEARCA)](https://seekingalpha.com/news/4658471-gold-needs-to-build-floor-or-face-further-losses-standard-chartereds-cooper-says)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Gold prices needs to hold support near current levels, or the market could be exposed to a much deeper correction, Standard Chartered Global Head of...
- [GLD 261027 361.00C (GLD261027C361000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GLD261027C361000-US)  
  <sub>Moomoo, 20 hours ago</sub>  
  SPDR Gold ETF (GLD) News. 'Another Golden Asteroid Story': Why Lab-Made Gold Won't Crash Bullion. "Any sufficiently advanced technology is indistinguishable...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.03 on the week) | 5-year 4.88% (-0.10 on the week) | 10-year 5.02% (-0.13 on the week) | 30-year 5.32% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.99 points -- upward sloping (normal)
US dollar index: 102.39 (+0.61 on the week)
Volatility (VIX): 17.34 (+0.7 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.68% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 370.33 (bar of 2026-10-28), from 502 daily bars
Trend: vs 20d SMA 377.53 (-1.9%), 50d 392.60 (-5.7%), 200d 413.52 (-10.4%); 50d below 200d
Momentum: RSI(14) 39.5 | MACD -5.482 vs signal -5.071 (histogram -0.411)
Returns: 1d -0.5% | 5d -2.3% | 1m -3.3% | 3m -1.8%
52-week range: 362.32 - 495.90 (now 6.0% of the way up)
Volatility: ATR(14) 5.39 (1.5% of price) | annualised 20d 17.3%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

```text
Cost of holding this fund instead of gold itself: 0.0% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -1.8%, commodity -1.1%, gap -0.7% | 6 months: fund -11.3%, commodity -11.1%, gap -0.2% | 12 months: fund +0.9%, commodity +0.9%, gap +0.0%
A commodity fund holds futures, not gold, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 25.9% of open interest (402,279 contracts)
Change on the week: -1.1% of open interest
Crowding: 42% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 32d
Shares outstanding: 260.30M | fund size: 96.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Word list

Terms that appear above and have no simpler word:

- **Confidence** — How sure the model is, from 0.00 to 1.00. A trade needs 0.30 or more.
- **R** — The amount one trade risked when it was opened: the distance from the entry price to the stop-loss. +1R means the trade has earned that amount back; +3R means three times it.
- **Score** — How good or bad one kind of evidence looks, from -1.00 (bad) to +1.00 (good).
- **Moving average (SMA)** — The average price over the last N days. A price above it usually means an up trend.
- **RSI** — A 0-100 meter of how fast the price has moved lately. Over 70 means a lot of buying, under 30 a lot of selling.
- **MACD** — Compares a short and a long average to show whether a trend is getting stronger or weaker.
- **P/E** — Price divided by yearly profit per share. A high number means the share is expensive next to today's profit.
- **ATR** — The normal size of one day's price move. The system uses it to place the stop-loss.
- **Stop-loss** — An order that closes the position if the price moves too far the wrong way.
- **Insider** — A director or senior manager of the company. They have to report their own trades.
- **Index fund** — One fund that holds many shares at once, so it follows a whole market instead of one company.
- **Sector or country fund** — A fund that holds many companies, but all of them in one industry or one country. Safer than one company, riskier than a whole-market fund.
- **Positioning** — How much the big professional traders are betting on a commodity or bond, from the weekly US regulator report. High numbers mean the bet is crowded, which cuts both ways.
- **Fund flows** — Money going into or out of a fund. When more people want a fund, new shares are created; when they leave, shares are destroyed. So a rising share count means real money came in. It has already happened -- it is not a forecast.
- **Roll-up** — A fund does not get analyst ratings, but the companies it holds do. A roll-up adds those ratings up, weighted by how much of each company the fund owns. The "coverage" number says how much of the fund that actually covers.
- **Beta** — How hard a fund swings compared with the whole market. Beta 1.0 moves with the market, 2.0 swings twice as hard, 0.5 half as hard.
- **Yield curve** — The gap between what the government pays to borrow for three months and for ten years. Normally ten years costs more. When it costs less -- an "inverted" curve -- markets are expecting a slowdown.
- **VIX** — How nervous the market is about the next month. Under 15 is calm, over 25 is stressed.
- **Build and draw** — A build means more oil or gas went into storage than came out last week, so there is more supply around — usually bad for the price. A draw is the opposite.
- **Good or excellent** — The share of a US crop that government inspectors rate as healthy. A healthier crop means more grain, which usually pushes the price down.
- **Beat and miss** — A company beat if it earned more than analysts forecast, and missed if it earned less.
- **Cost of holding** — A commodity fund does not own the gold or the oil. It owns contracts that expire every month and must be replaced, and the replacement often costs more. That difference comes out of the fund's price every month, even when the commodity itself does not move. Funds that hold real metal in a vault avoid almost all of it.

