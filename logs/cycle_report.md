# Daily report

**15 Oct 2026, 19:17 Israel time (16:17 UTC)** · 80 names checked · 5 traded · 5 with a problem

**Answers with no explanation:** 13 of 63 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 7 | 8 | 1 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 1 | 37 | 3 |
| Commodities | 9 | 0 | 8 | 1 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| United Kingdom (EWU) · Sector or country | **Sold part.** Sold 51 of 155 shares at +1.70R, 104 still held. Stop-loss raised 45.88 → 46.84. |
| Eli Lilly (LLY) · Company | **Sold part.** Sold 1 of 4 shares at +1.87R, 3 still held. Stop-loss raised 1136.43 → 1191.16. |
| Argentina (ARGT) · Sector or country | **Holding.** -0.37R, holding 80 shares. Stop-loss 86.01. |
| Poland (EPOL) · Sector or country | **Holding.** +0.53R, holding 164 shares. Stop-loss 43.03. |
| Brazil (EWZ) · Sector or country | **Holding.** -0.34R, holding 165 shares. Stop-loss 41.48. |
| Gold (GLD) · Commodity | **Holding.** +0.49R, holding 10 shares. Stop-loss 387.99. |
| Alphabet (Google) (GOOGL) · Company | **Holding.** -0.14R, holding 14 shares. Stop-loss 338.49. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** -0.09R, holding 158 shares. Stop-loss 76.66. |
| Microsoft (MSFT) · Company | **Holding.** +2.08R, holding 7 shares. Stop-loss 525.70. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** +0.91R, holding 86 shares. Stop-loss 39.51. |
| US dollar (UUP) · Index fund | **Holding.** +2.79R, holding 142 shares. Stop-loss 28.96. |
| Exxon Mobil (XOM) · Company | **Holding.** +1.81R, holding 9 shares. Stop-loss 168.38. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Novo Nordisk (NVO) · Company — BULLISH, confidence 0.70

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> EU approval of oral Wegovy provides a clear, material catalyst that lifted the stock 3% in the last day. Technicals show short‑term upside (price +3.1% 1‑day, RSI 45.3, MACD histogram positive) despite a longer‑term downtrend. Fundamentals are solid with low valuation (P/E 9.6) and high profitability (ROE 59.8%). Earnings record is mixed (1 beat, 2 misses) and analyst consensus is neutral (hold) with a +16% price‑target upside. No insider buying activity, so neutral on insider side. Overall, the positive news outweighs the neutral/negative signals, leading to a BUY recommendation with moderate‑high conviction.

**Main reasons it gave:**
- EU approval of oral Wegovy pill (Stocktwits, 19h ago) lifted price 3%
- Short‑term technicals positive: 1‑day return +3.1%, RSI 45.3, MACD histogram +0.364
- Strong fundamentals: low P/E 9.6, profit margin 35.3%, ROE 59.8%
- Analyst consensus hold with mean price target 45.72 (+16% upside)

<details><summary><b>News</b> — score +0.80</summary>

- [NVO Stock Jumps 3% As EU Approves Oral Wegovy Pill — Retail Notes LLY Is ‘Clearly Behind’ Its Danish Counterpart](https://stocktwits.com/news-articles/markets/equity/nvo-stock-jumps-3-as-eu-approves-oral-wegovy-pill-retail-notes-lly-is-clearly-behind-its-danish-counterpart/cZZPaw9R7r9)  
  <sub>Stocktwits, 19 hours ago</sub>  
  NVO Stock Jumps 3% As EU Approves Oral Wegovy Pill — Retail Notes LLY Is 'Clearly Behind' Its Danish Counterpart. Oral Wegovy is now cleared in all EU member...
- [NVO Nov 2026 38.000 put (NVO261113P00038000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO261113P00038000/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest NVO Nov 2026 38.000 put (NVO261113P00038000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Novo Nordisk (NVO) Could Be 63% Undervalued Following Its Share Buyback](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nvo-could-63-201751092.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Novo Nordisk (NVO) triggered fresh attention after launching a DKK 15b share repurchase programme, committing up to DKK 11.2b to B shares through early 2027...
- [Novo Nordisk (NVO) Could Be 57% Undervalued As Buyback Puts Fair Value In Focus](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-nvo/novo-nordisk/news/novo-nordisk-nvo-could-be-57-undervalued-as-buyback-puts-fai)  
  <sub>Simply Wall Street, 19 hours ago</sub>  
  Share repurchase move puts Novo Nordisk in focus Novo Nordisk (NVO) is back on investors radar after launching a share repurchase programme of up to DKK 15b...
- [BIOA, GLUE Stocks Clock Worst Day In Years— What’s The NVO Connection?](https://stocktwits.com/news-articles/markets/equity/bioa-glue-stocks-clock-worst-day-in-years-what-s-the-nvo-connection/cZN4NtDRJ5G)  
  <sub>Stocktwits, 20 hours ago</sub>  
  Citi noted BIOA's greater-than-60% drop and agreed the data is a negative for BioAge's heart-disease thesis, yet argued the size of the move “seems overdone”...
- [NVO Nov 2026 38.000 put (NVO261113P00038000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/NVO261113P00038000/chart/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Interactive Chart for NVO Nov 2026 38.000 put (NVO261113P00038000), analyze all the data with a huge range of indicators.
- [Novo Nordisk’s Biggest Growth Engine Could Become Its Biggest Risk, Morgan Stanley Warns](https://stocktwits.com/news-articles/markets/equity/nvo-stock-why-morgan-stanley-is-bearish-on-novo-nordisk-despite-its-weight-loss-drug-opportunity/cZtXhhNRBGl)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Morgan Stanley downgraded Novo to 'Underweight' from 'Equal Weight' while keeping its $40 price target, a 7% downside from current levels.
- [NVO Nov 2026 39.000 put (NVO261106P00039000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/NVO261106P00039000/)  
  <sub>Yahoo Finance UK, 14 hours ago</sub>  
  Find the latest NVO Nov 2026 39.000 put (NVO261106P00039000) stock quote, history, news and other vital information to help you with your stock trading and...
- [NVO Oct 2026 41.500 call (NVO261016C00041500) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/NVO261016C00041500/chart/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Interactive Chart for NVO Oct 2026 41.500 call (NVO261016C00041500), analyze all the data with a huge range of indicators.
- [Is Novo Nordisk (NYSE:NVO) A Long Term Value Opportunity Now?](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nyse-nvo-long-161806261.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Novo Nordisk has seen a steep reset in its share price over the past few years, which puts a spotlight on whether the current market value still lines up...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 39.29 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 38.59 (+1.8%), 50d 42.85 (-8.3%), 200d 45.13 (-12.9%); 50d below 200d
Momentum: RSI(14) 45.3 | MACD -1.287 vs signal -1.651 (histogram 0.364)
Returns: 1d +3.1% | 5d +2.9% | 1m -5.8% | 3m -21.9%
52-week range: 35.29 - 63.98 (now 14.0% of the way up)
Volatility: ATR(14) 0.95 (2.4% of price) | annualised 20d 35.1%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 173.41B
Valuation: trailing P/E 9.61 | forward P/E 11.53 | P/B 5.27 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.72 (+16.4% vs last close), range 39.85 - 61.95
Recent rating changes:
  - 2026-10-12 BMO Capital: main, Market Perform -> Market Perform
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
Institutional ownership: 9.9%
Largest holders: Dodge & Cox Inc. (0.6%), LOOMIS SAYLES & CO L P (0.5%), Franklin Resources, Inc. (0.4%), Price (T.Rowe) Associates Inc (0.3%), Morgan Stanley (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

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

### Procter & Gamble (PG) · Company — BEARISH, confidence 0.68

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Negative earnings preview dominates, reinforced by overbought technicals and declining YoY earnings growth; analyst view remains modestly bullish but insufficient to offset downside.

**Main reasons it gave:**
- Earnings preview expects Q1 earnings decline and likely miss
- RSI 73.8 indicates overbought conditions
- YoY earnings growth -15.5% shows declining profitability

<details><summary><b>News</b> — score -0.80</summary>

- [Earnings Preview: Procter & Gamble (PG) Q1 Earnings Expected to Decline](https://finance.yahoo.com/markets/stocks/articles/earnings-preview-procter-gamble-pg-130011444.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  P&G (PG) doesn't possess the right combination of the two key ingredients for a likely earnings beat in its upcoming report. Get prepared with the key...
- [Procter & Gamble (PG) director Joseph Jimenez holds 38,968 shares directly after a 1,438-share award.](https://www.stocktitan.net/sec-filings/PG/form-4-procter-gamble-co-insider-trading-activity-bf5ad966bb25.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Procter & Gamble (PG) director Joseph Jimenez acquired 1,438 shares of common stock on October 13, 2026, through an award of restricted stock units.
- [These Stocks Break Out As Investors Play Defense. But Watch This.](https://www.investors.com/news/bj-stock-pg-stock-consumer-stocks-rally-investors-play-defense/)  
  <sub>Investor's Business Daily, 19 hours ago</sub>  
  Consumer defensive giants and minnows shone after a hot inflation report spurred a broader selloff. BJ's stock and PG stock broke out.
- [Procter & Gamble (PG) Projected to Post Quarterly Earnings on Thursday](https://www.marketbeat.com/instant-alerts/upcoming-procter-gamble-pg-projected-to-post-quarterly-earnings-on-thursday-2026-10-15/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Procter & Gamble (NYSE:PG) will be releasing its Q1 2027 earnings before the market opens on Thursday, October 22. (View Earnings Report at...
- [Discover which dow jones stocks are making waves on Wednesday.](https://www.chartmill.com/news/WMT/Chartmill-56226-Discover-which-dow-jones-stocks-are-making-waves-on-Wednesday)  
  <sub>ChartMill, 20 hours ago</sub>  
  Uncover the latest developments among dow jones stocks in today's session. Stay tuned to the dow jones index's top gainers and losers on Wednesday.
- [ETFs Are Net Sellers of Procter & Gamble (PG) on Tuesday](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-procter-gamble-110235890.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs sold a net $56.1 million of Procter & Gamble on Oct. 13, with 19 buying and 17 selling.
- [Director Christopher J. Kempczinski receives 1,438 stock units from Procter & Gamble (PG).](https://www.stocktitan.net/sec-filings/PG/form-4-procter-gamble-co-insider-trading-activity-d56532d5467a.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Procter & Gamble director Christopher J. Kempczinski received an award of 1,438 restricted stock units on October 13, 2026. The report lists 13,372 shares...
- [PG Dec 2026 185.000 put (PG261218P00185000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/PG261218P00185000/chart/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Interactive Chart for PG Dec 2026 185.000 put (PG261218P00185000), analyze all the data with a huge range of indicators.
- [A director receives 1,438 stock units at Procter & Gamble (PG), bringing his direct position to 7,768 shares.](https://www.stocktitan.net/sec-filings/PG/form-4-procter-gamble-co-insider-trading-activity-61cdce5265fc.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Rajesh Subramaniam's October 13, 2026 award falls under the 2025 incentive plan; his reported position includes stock-unit dividend equivalents.
- [After acquiring 1,438 stock units, Procter & Gamble (PG) director Portman holds 6,685 common shares.](https://www.stocktitan.net/sec-filings/PG/form-4-procter-gamble-co-insider-trading-activity-b15861c23987.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Procter & Gamble (PG) director Robert Jones Portman acquired 1,438 restricted stock units on October 13, 2026. The award was reported as a direct...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 158.40 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 148.83 (+6.4%), 50d 146.65 (+8.0%), 200d 147.96 (+7.1%); 50d below 200d
Momentum: RSI(14) 73.8 | MACD 2.431 vs signal 1.277 (histogram 1.154)
Returns: 1d +1.2% | 5d +5.2% | 1m +7.7% | 3m +5.6%
52-week range: 138.04 - 167.20 (now 69.8% of the way up)
Volatility: ATR(14) 2.57 (1.6% of price) | annualised 20d 18.9%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 367.92B
Valuation: trailing P/E 23.40 | forward P/E 21.42 | P/B 6.90 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.1% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.16 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 8 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 161.65 (+2.1% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-10-14 Citigroup: main, Buy -> Buy
  - 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - 2026-10-06 RBC Capital: main, Outperform -> Outperform
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
  - 2026-07-30 HSBC: down, Buy -> Hold
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

```text
Last 180 days: bought 151,979 shares in 39 transaction(s) | sold 48,751 shares in 16
Net: +103,228 shares (+5.1% of insider holdings) | insiders hold 2,138,478 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(37 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — BULLISH, confidence 0.65

**Result:** ACCEPTED · 17 shares · submitted buy 17 RY @ ~195.64, stop 189.64

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Insider buys: 200k shares on 2026-09-29, 2026-09-28, 2026-09-25, 2026-09-24
- Analyst target: mean $210.84, +7.5% vs $196.08
- Technical: price above 200‑day SMA (+4.6%) and MACD histogram positive
- Fundamentals: forward P/E 15.56, ROE 16.2%, revenue growth 8.9% YoY

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 196.08 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 197.23 (-0.6%), 50d 203.77 (-3.8%), 200d 187.48 (+4.6%); 50d above 200d
Momentum: RSI(14) 44.8 | MACD -3.011 vs signal -3.201 (histogram 0.190)
Returns: 1d +1.2% | 5d +2.9% | 1m -3.1% | 3m -9.0%
52-week range: 145.31 - 217.87 (now 70.0% of the way up)
Volatility: ATR(14) 2.99 (1.5% of price) | annualised 20d 17.7%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 271.46B
Valuation: trailing P/E 17.22 | forward P/E 15.56 | P/B 2.88 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.91 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
```

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

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 210.84 (+7.5% vs last close), range 183.64 - 232.72
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- 5%+ price jump on above‑average volume (NEWS)
- RSI 59.1 and positive MACD histogram indicating modest momentum (TECHNICALS)
- Four consecutive earnings beats (EARNINGS RECORD)
- Analyst price target 8.6% above last close (ANALYST & INSTITUTIONAL VIEW)
- Revenue growth +15.9% YoY and earnings growth +34.2% YoY (FUNDAMENTALS)

<details><summary><b>News</b> — score +0.30</summary>

- [Strength Seen in Elbit (ESLT): Can Its 5.1% Jump Turn into More Strength?](https://finance.yahoo.com/markets/stocks/articles/strength-seen-elbit-eslt-5-092000198.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Elbit (ESLT) witnessed a jump in share price last session on above-average trading volume. The latest trend in earnings estimate revisions for the stock...
- [A Look at Elbit Systems Ltd (ESLT) After 5.0% Gain -- GF Value $386.44 vs Price $701.38](https://www.gurufocus.com/news/9124221/a-look-at-elbit-systems-ltd-eslt-after-50-gain-gf-value-38644-vs-price-70138)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On October 14, 2026, Elbit Systems Ltd (ESLT) shares rose by 5.0%, bringing the current price to $701.38. Over the past year, the stock has shown a...
- [Elbit Systems (NASDAQ:ESLT) Shares Gap Up - Time to Buy?](https://www.marketbeat.com/instant-alerts/price-elbit-systems-nasdaq-eslt-shares-gap-up-time-to-buy-2026-10-14/)  
  <sub>MarketBeat, 24 hours ago</sub>  
  Shares of Elbit Systems Ltd. (NASDAQ:ESLT - Get Free Report) gapped up prior to trading on Wednesday. The stock had previously closed at $667.67,...
- [Elbit Stocks Rise 4.3% as Sweden Expansion Faces a Backlog Delivery Test](https://www.tradingview.com/news/gurufocus:641f8d1eb094b:0-elbit-stocks-rise-4-3-as-sweden-expansion-faces-a-backlog-delivery-test/)  
  <sub>TradingView, 19 hours ago</sub>  
  Elbit Systems, the defense-electronics and autonomous-systems supplier NASDAQ:ESLT, advanced to $696.45, up approximately 4.3%, around 12:56 p.m. ET on...
- [Elbit Systems builds Swedish laser center as Elbit Systems stock trades at EUR 646.00](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-builds-swedish-laser-center-as-elbit-systems-stock-trades-at-eur-646-00/70326903)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  ESLT, IL0010811243. Elbit Systems builds Swedish laser center as Elbit Systems stock trades at EUR 646.00. Published on 10/15/2026 at 10:15 | Editorial...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 738.10 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 704.45 (+4.8%), 50d 730.59 (+1.0%), 200d 779.28 (-5.3%); 50d below 200d
Momentum: RSI(14) 59.1 | MACD -11.922 vs signal -15.495 (histogram 3.572)
Returns: 1d +5.2% | 5d +11.0% | 1m -0.0% | 3m -0.5%
52-week range: 454.95 - 1,014.33 (now 50.6% of the way up)
Volatility: ATR(14) 20.44 (2.8% of price) | annualised 20d 38.8%
Volume: 0.76x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.59B
Valuation: trailing P/E 52.87 | forward P/E 40.20 | P/B 7.83 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 801.33 (+8.6% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 23.0%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.0%), Altshuler Shaham Ltd (1.0%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### HDFC Bank (HDB) · Company — BULLISH, confidence 0.55

**Result:** ACCEPTED · 4 shares · submitted buy 4 HDB @ ~23.56, stop 22.48

**In the model's own words:**

> Moderately bullish technicals, solid analyst consensus with a large price‑target upside, recent earnings beats, and neutral fundamentals support a BUY view despite thin volume and lack of a fresh catalyst.

**Main reasons it gave:**
- Price above 20‑day (+3.5%) and 50‑day (+2.5%) SMA, indicating short‑term uptrend
- Analyst consensus buy with mean price target $30.52 (+29.9% upside)
- Recent earnings beats (61% and 10%) and 2 in‑line quarters
- RSI 58.2 and MACD histogram positive, showing bullish momentum

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.40</summary>

```text
Last close 23.49 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 22.70 (+3.5%), 50d 22.91 (+2.5%), 200d 26.46 (-11.2%); 50d below 200d
Momentum: RSI(14) 58.2 | MACD -0.062 vs signal -0.168 (histogram 0.105)
Returns: 1d +3.8% | 5d +6.7% | 1m +5.0% | 3m -11.0%
52-week range: 21.84 - 37.18 (now 10.8% of the way up)
Volatility: ATR(14) 0.53 (2.3% of price) | annualised 20d 29.4%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 120.73B
Valuation: trailing P/E 15.25 | forward P/E 16.89 | P/B 9.47 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2026-10-17
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.52 (+29.9% vs last close), range 26.10 - 35.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 13.7%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), Schroder Investment Management Group (0.4%), JPMORGAN CHASE & CO (0.4%), Bank of America Corporation (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### ASML (ASML) · Company — BEARISH, confidence 0.48

**Result:** ACCEPTED · 3 shares · submitted sell 3 ASML @ ~1641.11, stop 1750.37

**In the model's own words:**

> The Q3 earnings beat was offset by a revenue miss and capacity constraints, causing a 5‑7% sell‑off and bearish technical indicators (RSI 35.9, negative MACD, price below short‑term SMAs). However, the company’s fundamentals remain strong (high margins, ROE, forward P/E ~26) and analysts maintain a strong‑buy consensus with a +32% price target. No insider buying activity was observed. The mixed signals lead to a bearish short‑term outlook with moderate conviction.

**Main reasons it gave:**
- Q3 earnings beat but revenue miss led to 5-7% stock decline
- RSI 35.9 and MACD negative show bearish technical momentum
- High profitability (30.1% margin, 53.9% ROE) and forward P/E 26.19 indicate strong fundamentals
- Analyst consensus strong buy with mean price target +32% above last close
- Earnings record: 3 beats, 1 miss in last 4 quarters

<details><summary><b>News</b> — score -0.40</summary>

- [ASML Holding N.V. (ASML) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  ASML Holding N.V. (ASML) · -8.59% · -2.84% · 9.99% · 53.90% · 67.57% · 121.65% · 67,660.00%. Key Events. Baseline. Advanced Chart. Loading chart for...
- [Why is ASML stock sliding today?](https://www.investing.com/news/stock-market-news/why-is-asml-stock-sliding-today-93CH-4950763)  
  <sub>Investing.com, 6 hours ago</sub>  
  Investing.com -- ASML stock is sliding 5.5% today to trade at €1,443.8, following other AI-exposed stocks that also fell sharply, and tracking an overnight...
- [ASML Stock Falls Following a Slight Sales Miss in Q3](https://www.tikr.com/blog/asml-stock-falls-third-quarter-sales-miss)  
  <sub>TIKR.com, 2 hours ago</sub>  
  ASML stock slipped after a small Q3 sales miss, but profit beat and customers want to order tools for 2029 and 2030.
- [Should You Trade ASML Stock With Caution Despite Q3 Earnings Beat?](https://www.zacks.com/stock/news/3008666/should-you-trade-asml-stock-with-caution-despite-q3-earnings-beat)  
  <sub>Zacks Investment Research, 26 minutes ago</sub>  
  ASML's Q3 earnings beat and AI-driven demand signal growth, but revenue misses, capacity constraints and rising costs raise concerns about the stock's...
- [ASML vs. Applied Materials: Which Chip-Equipment Stock Is the Better Buy?](https://www.fool.com/investing/2026/10/15/asml-vs-applied-materials-which-chip-equipment-sto/)  
  <sub>The Motley Fool, 4 hours ago</sub>  
  Semiconductor manufacturers are expanding production capacity as fast as they can, and both stocks stand to benefit.
- [ASML Stock Is Falling After Earnings Point to Soaring AI Demand. Here's Why.](https://www.barrons.com/articles/asml-earnings-stock-price-d0973c5c)  
  <sub>Barron's, 23 hours ago</sub>  
  ASML's U.S.-listed stock was falling even after it raised its sales guidance and said it can't keep up with customer demand for lithography tools.
- [Chip-Gear Giant ASML Posts Mixed Q3 Results, Guides Up](https://www.investors.com/news/technology/asml-stock-q3-2026-earnings/)  
  <sub>Investor's Business Daily, 18 hours ago</sub>  
  Semiconductor equipment maker ASML (ASML) on Wednesday beat analyst estimates for earnings in the third quarter, but its sales were a tad light. ASML stock...
- [Why Is ASML Stock Falling Today?](https://stocktwits.com/news-articles/markets/equity/asml-stock-is-falling-today-china-connection/cZZxnU0R76j)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Shares of ASML Holding NV (ASML) fell over 7% in Monday's midday trade amid a report that a Chinese state-backed company has started manufacturing immersion...
- [ASML: Indiscriminate Selloff Doesn't Make Much Sense (NASDAQ:ASML)](https://seekingalpha.com/article/4954475-asml-indiscriminate-selloff-doesnt-make-much-sense)  
  <sub>Seeking Alpha, 49 minutes ago</sub>  
  ASML Holding N.V. is the predominant semiconductor bellwether on wafer fab equipment. It delivered robust Q3 results while projecting strong low-NA EUV...
- [ASML Posts Record Q3 2026 Results and Signals Capacity Strain Amid Surging AI Demand](https://www.theglobeandmail.com/investing/markets/stocks/ASML/pressreleases/7817200/asml-posts-record-q3-2026-results-and-signals-capacity-strain-amid-surging-ai-demand/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Detailed price information for ASML Holding NV (ASML-Q) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,624.27 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 1,761.74 (-7.8%), 50d 1,740.22 (-6.7%), 200d 1,574.20 (+3.2%); 50d above 200d
Momentum: RSI(14) 35.9 | MACD -6.971 vs signal 13.001 (histogram -19.972)
Returns: 1d -1.6% | 5d -8.2% | 1m +1.4% | 3m -7.1%
52-week range: 966.57 - 1,989.44 (now 64.3% of the way up)
Volatility: ATR(14) 54.41 (3.3% of price) | annualised 20d 32.8%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 623.88B
Valuation: trailing P/E 54.89 | forward P/E 26.19 | P/B 1,417.80 | PEG 1.58
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.30 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 17% | 2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 17 analysts)
Ratings: 6 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,153.25 (+32.6% vs last close), range 868.48 - 2,885.64
Recent rating changes:
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
  - 2026-06-22 B of A Securities: main, Buy -> Buy
Institutional ownership: 20.4%
Largest holders: FMR, LLC (1.4%), Fisher Asset Management, LLC (1.2%), Capital World Investors (1.0%), Invesco Ltd. (0.8%), State Farm Mutual Automobile Insurance Co (0.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 1,707,111 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish news (large stake reduction and target cut) outweighs modest bullish analyst consensus and neutral technicals; fundamentals are mixed with high valuation and leverage; insider buying is small. Net tilt slightly bearish, but not strong enough for high conviction.

**Main reasons it gave:**
- Strategy Asset Managers cut MELI stake by 26.6% (large sell)
- Citi lowered price target to $2,100 (downward revision)
- Analyst consensus is buy with mean target $2,270 (+23% upside)
- Technical indicators neutral: RSI 51, MACD positive, but volume 0.15x 20‑day average

<details><summary><b>News</b> — score -0.60</summary>

- [1,142 MercadoLibre, Inc. $MELI Shares Sold by Strategy Asset Managers LLC](https://www.marketbeat.com/instant-alerts/filing-1142-mercadolibre-inc-meli-shares-sold-by-strategy-asset-managers-llc-2026-10-15/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Strategy Asset Managers LLC lowered its position in MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 26.6% during the 3rd quarter, according to the company...
- [MELI Dec 2027 2540.000 call (MELI271217C02540000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI271217C02540000/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest MELI Dec 2027 2540.000 call (MELI271217C02540000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Momentum Gains: Full Details](https://journalarta.com/en/2026/10/15/meli-momentum-gains-stock-drops-1-97-october-14-2026/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 14, 2026: price 1839.11 USD, trend sideways, RSI 50.4, support 1685.12, resistance 1892.44. technical analysis of meli stock.
- [MercadoLibre (NASDAQ:MELI) Share Price, Forecast & Analysis](https://stocksdownunder.com/company/meli/)  
  <sub>Stocks Down Under, 23 hours ago</sub>  
  Explore MercadoLibre (NASDAQ:MELI) share price, stock analysis, financial performance, valuation and analyst price targets on Stocks Down Under.
- [Citi cut target to USD 2,100. MercadoLibre stock fell 1.13 percent](https://www.ad-hoc-news.de/boerse/news/corporate-news/citi-cut-target-to-usd-2-100-mercadolibre-stock-fell-1-13-percent/70326834)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  MELI, US58733R1023. Citi cut target to USD 2,100. MercadoLibre stock fell 1.13 percent. Published on 10/15/2026 at 10:11 | Editorial responsibility: Rafael...
- [MELI Oct 2026 2040.000 call (MELI261030C02040000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/MELI261030C02040000/chart/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Interactive Chart for MELI Oct 2026 2040.000 call (MELI261030C02040000), analyze all the data with a huge range of indicators.
- [MELI Oct 2026 1960.000 call (MELI261016C01960000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI261016C01960000/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest MELI Oct 2026 1960.000 call (MELI261016C01960000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Oct 2026 1670.000 put (MELI261016P01670000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261016P01670000/)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Find the latest MELI Oct 2026 1670.000 put (MELI261016P01670000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Oct 2026 2330.000 call (MELI261030C02330000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/MELI261030C02330000/chart/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  OPR - Delayed Quote • USD. MELI Oct 2026 2330.000 call (MELI261030C02330000). 4.3200 0.0000 (0.00%). As of September 15 at 11:51:15 a.m. EDT. Market Open.
- [Will MELI hold $1,770 support as ETF outflows add liquidity pressure?](https://tradersunion.com/news/stocks/show/3814106-mercadolibre-slides-2-84percent-to-usd1822/)  
  <sub>Traders Union, 20 hours ago</sub>  
  MercadoLibre trades at $1822 today, down 2.84%. Get the latest on MELI price action, technicals, and earnings performance.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 1,845.48 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 1,803.95 (+2.3%), 50d 1,859.67 (-0.8%), 200d 1,832.47 (+0.7%); 50d above 200d
Momentum: RSI(14) 51.3 | MACD 3.697 vs signal -7.907 (histogram 11.603)
Returns: 1d +0.3% | 5d -0.6% | 1m +0.3% | 3m +1.7%
52-week range: 1,546.81 - 2,360.76 (now 36.7% of the way up)
Volatility: ATR(14) 54.44 (2.9% of price) | annualised 20d 41.8%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 93.56B
Valuation: trailing P/E 50.19 | forward P/E 32.81 | P/B 11.94 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.8% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 16 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 2,270.01 (+23.0% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-13 Citigroup: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
Institutional ownership: 80.2%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

### Nvidia (NVDA) · Company — BEARISH, confidence 0.45

**Result:** ACCEPTED · 23 shares · submitted sell 23 NVDA @ ~216.92, stop 228.95

**In the model's own words:**

> The short‑term outlook is weighed down by negative news sentiment and bearish technical indicators, despite strong fundamentals and a solid earnings record. The net insider activity is neutral, and analyst consensus is already priced in. Overall, the balance of short‑term factors points to a modest probability of a near‑term downside move.

**Main reasons it gave:**
- Recent news shows ~2% price drop due to risk‑off sentiment and export‑control concerns
- RSI 39.6 and price below 20‑day/50‑day SMA indicate bearish technical momentum
- Strong fundamentals: profit margin 63.7%, forward P/E 13.6, revenue growth +105.9% YoY
- Earnings record: 3 beats and 1 in‑line over the last 4 quarters
- Insider sales of ~6.2M shares (weak evidence of bearish sentiment)

<details><summary><b>News</b> — score -0.30</summary>

- [Nvidia leads chip stocks lower as AI trade takes](https://finance.yahoo.com/markets/stocks/article/nvidia-stock-sinks-amid-concerns-over-ai-financing-134237567.html)  
  <sub>Yahoo Finance, 58 minutes ago</sub>  
  The sell-off in chip stocks deepened Thursday as hot inflation data collided with growing worries over debt-heavy balance sheets amid an AI infrastructure...
- [NVDA Stock Slips As Risk-Off Mood And Trump Sale Hit Sentiment](https://stockstotrade.com/news/nvidia-corporation-nvda-news-2026_10_15/)  
  <sub>StocksToTrade, 1 hour ago</sub>  
  NVIDIA Corporation faces heightened volatility as regulatory scrutiny on AI chips weighs on outlook, while stocks have been trading down by -2.04 percent.
- [NVDA Stock Slips As Momentum Traders Turn Cautious](https://www.timothysykes.com/news/nvidia-corporation-nvda-news-2026_10_15/)  
  <sub>Timothy Sykes, 1 hour ago</sub>  
  NVIDIA Corporation stocks have been trading down by -2.09 percent amid reports of tightening AI chip export controls to China. Key Takeaways Nvidia is down.
- [The Case For NVIDIA Stock Rests On One Thing](https://www.trefis.com/stock/nvda/articles/618865/the-case-for-nvidia-stock-rests-on-one-thing/2026-10-15)  
  <sub>Trefis, 59 minutes ago</sub>  
  NVIDIA (NVDA) has translated demand for its AI platform into rapid sales growth. NVIDIA can only sell the hardware its partners build, leaving the open risk...
- [History Says Nvidia Stock Usually Rises in the Fourth Quarter -- It Has in 20 of the Last 27](https://www.fool.com/investing/2026/10/14/history-says-nvidia-stock-usually-rises-in-the-fourth-quarter-it-has-in-20-of-the-last-27/)  
  <sub>The Motley Fool, 14 hours ago</sub>  
  Shares of Nvidia (NVDA -3.16%) hit another record on Tuesday, Oct. 6, closing at $239.24. If history's any guide, the October-to-December quarter has...
- [NVIDIA Corporation (NVDA) stock price, news, quote and history](https://au.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo Finance Australia, 8 hours ago</sub>  
  505,728.61% · Previous close 228.52 · Open 225.60 · Bid 209.79 x 100 · Ask 221.69 x 200 · Day's range 219.64 - 226.00 · 52-week range 164.27 - 243.37 · Volume...
- [NVIDIA Corporation $NVDA Stock Holdings Cut by SPX Gestao de Recursos Ltda](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-holdings-cut-by-spx-gestao-de-recursos-ltda-2026-10-15/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  SPX Gestao de Recursos Ltda trimmed its holdings in NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 57.2% in the 2nd quarter, according to its most recent...
- [Why Dan Ives Sees NVDA And Korea Memory Stocks Driving AI Demand](https://stocktwits.com/news-articles/markets/equity/why-dan-ives-sees-nvda-korean-memory-stocks-driving-ai-demand/cZm1YQ1R7ly)  
  <sub>Stocktwits, 4 hours ago</sub>  
  AMD Sits Second Behind NVDA In Stocktwits Retail Poll. A live Stocktwits retail poll shows AMD as the second-most popular long-term semiconductor pick among...
- [How Investors May Respond To NVIDIA (NVDA) Higher AI Funding Costs](https://simplywall.st/stocks/us/semiconductors/nasdaq-nvda/nvidia/news/how-investors-may-respond-to-nvidia-nvda-higher-ai-funding-c)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  NVIDIA faced fresh pressure as a sector wide selloff in semiconductor and AI stocks followed hotter than expected inflation data, which raised concerns...
- [NVIDIA Corporation $NVDA Stock: Rakuten Investment Management Inc. Boosts Stake](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-rakuten-investment-management-inc-boosts-stake-2026-10-15/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Rakuten Investment Management Inc. lifted its holdings in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 12.4% during the second quarter,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 216.49 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 228.55 (-5.3%), 50d 223.16 (-3.0%), 200d 202.83 (+6.7%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD 0.855 vs signal 2.759 (histogram -1.903)
Returns: 1d -2.2% | 5d -6.1% | 1m +1.2% | 3m +6.7%
52-week range: 165.17 - 239.24 (now 69.3% of the way up)
Volatility: ATR(14) 6.02 (2.8% of price) | annualised 20d 25.2%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Technology / Semiconductors | market cap 5.23T
Valuation: trailing P/E 28.26 | forward P/E 13.60 | P/B 22.82 | PEG 0.48
Profitability: profit margin 63.7% | operating margin 66.2% | ROE 117.2%
Growth (YoY): revenue +105.9% | earnings +127.8%
Balance sheet: debt/equity 17.0% | free cash flow 41.81B
Risk: beta 2.22 | short interest 1.3% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 in line
  2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-03-31 beat by 4% | 2025-12-31 in line
```

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: strong_buy (mean 1.29 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 49 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.72 (+51.8% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-09-29 Rosenblatt: main, Buy -> Buy
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
  - 2026-08-27 Citigroup: main, Buy -> Buy
Institutional ownership: 71.4%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.4%), FMR, LLC (4.3%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: negative news and technicals suggest downside pressure, while strong fundamentals, earnings record, and bullish analyst view support upside potential. Insider activity is neutral. The conflict leads to a neutral stance with moderate conviction.

**Main reasons it gave:**
- Negative news sentiment: multiple headlines reporting ~4% slide due to analyst target cuts and AI concerns
- Technical indicators show oversold RSI 29.7 and price below 20/50/200 SMA
- Strong earnings record: 4 consecutive beats with beats ranging 8-31%
- Fundamentals strong: high profit margin 14.5%, ROE 57%, revenue growth 24% YoY
- Insider activity neutral: net small buy of 41k shares but large CEO sale considered weak evidence

<details><summary><b>News</b> — score -0.70</summary>

- [Caterpillar releases results at 5:30 a.m. Central on Oct. 29; its call starts at 7:30.](https://www.stocktitan.net/news/CAT/caterpillar-inc-to-announce-third-quarter-2026-financial-results-on-j3lezkarddxn.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  The call with securities analysts and institutional investors is listen-only; the webcast is free, and a transcript and replay will be available afterward.
- [Why is Caterpillar stock sliding today?](https://www.investing.com/news/stock-market-news/why-is-caterpillar-stock-sliding-today-93CH-4952076)  
  <sub>Investing.com, 48 minutes ago</sub>  
  Investing.com -- Caterpillar stock is sliding nearly 4.8% in morning trading to reach $712.76, driven by a compounding wave of analyst target reductions and...
- [Caterpillar stock is down about 30% from its record on oil, rate and AI worries](https://qz.com/caterpillar-stock-record-high-oil-rates-ai-worries-101426)  
  <sub>Quartz, 19 hours ago</sub>  
  Caterpillar stock is up about 40% over the past year as investors await third-quarter earnings expected Oct. 28.
- [Caterpillar sinks 30% from record high amid AI selloff, inflation fears (CAT:NYSE)](https://seekingalpha.com/news/4653120-caterpillar-sinks-30-percent-from-record-high-amid-ai-selloff-inflation-fears)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Caterpillar (CAT) shares extended their decline Wednesday, falling 3.3% as a broader retreat in artificial intelligence-related stocks and concerns about...
- [CAT261030C01020000 Interactive Stock Chart | CAT Oct 2026 1020.000 call Stock](https://finance.yahoo.com/chart/CAT261030C01020000)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Caterpillar Inc Stock (CAT) Moved Down by 3.05% on Oct 14: What Signal Does It Send?](https://www.tradingkey.com/news/market-movers/262216769-market-movers-cat-20261014)  
  <sub>TradingKey, 21 hours ago</sub>  
  Caterpillar experienced downward volatility driven by analyst rating revisions and valuation metrics.Citi and Truist lowered price objectives due to...
- [Caterpillar Shares Eye 30% Slump as Oil Bites, AI Rally Stalls](https://www.bloomberg.com/news/articles/2026-10-14/caterpillar-shares-eye-30-slump-as-oil-bites-ai-rally-stalls)  
  <sub>Bloomberg.com, 21 hours ago</sub>  
  Caterpillar Inc. shares are on track to fall more than 30% from their record high as concerns about oil prices, bond yields and the future of the artificial...
- [Trending Stocks Today | Token Cat Shoots up 26.6% Post-Market](https://www.moomoo.com/news/post/1001217995/trending-stocks-today-token-cat-shoots-up-26-6-post)  
  <sub>Moomoo, 16 hours ago</sub>  
  October14th - US stocks trending post-market.Gainers: $Token Cat(TC.US)$ soars 26.6% to $1.66 with a turnover of $7.09 million. $Netcapital(NCPL.
- [Trust Cat Deeley to wear the £36 M&S skirt of the season - and shockingly, it's still in stock](https://www.hellomagazine.com/shopping/929177/cat-deeley-knitted-marks-and-spencer-skirt/)  
  <sub>HELLO! Magazine, 4 hours ago</sub>  
  This Morning's Cat Deeley's knitted skirt is a high street buy from Marks & Spencer's new in collection, with the 49-year-old wearing the M&S High Waisted...
- [Caterpillar Inc. to Announce Third-Quarter 2026 Financial Results on October 29](https://www.marketscreener.com/news/caterpillar-inc-to-announce-third-quarter-2026-financial-results-on-october-29-ce785dd3dd8eff26)  
  <sub>www.marketscreener.com, 3 hours ago</sub>  
  IRVING, Texas, Oct. 15, 2026 /PRNewswire/ -- Caterpillar Inc. (NYSE: CAT) will release third-quarter financial results at 5:30 a.m. CDT on Thursday,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 723.57 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 808.41 (-10.5%), 50d 815.04 (-11.2%), 200d 804.91 (-10.1%); 50d above 200d
Momentum: RSI(14) 29.7 | MACD -14.956 vs signal -5.267 (histogram -9.689)
Returns: 1d -3.4% | 5d -9.1% | 1m -7.6% | 3m -17.8%
52-week range: 513.91 - 1,064.90 (now 38.1% of the way up)
Volatility: ATR(14) 28.45 (3.9% of price) | annualised 20d 34.8%
Volume: 0.61x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 332.60B
Valuation: trailing P/E 32.14 | forward P/E 22.20 | P/B 17.15 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 14 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 951.11 (+31.4% vs last close), range 575.00 - 1,155.00
Recent rating changes:
  - 2026-10-12 Citigroup: main, Buy -> Buy
  - 2026-10-05 Truist Securities: main, Buy -> Buy
  - 2026-09-10 Freedom Broker: up, Hold -> Buy
  - 2026-08-11 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-08-06 DA Davidson: main, Neutral -> Neutral
  - 2026-08-06 Barclays: main, Equal-Weight -> Equal-Weight
Institutional ownership: 73.5%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.5%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 169,246 shares in 20 transaction(s) | sold 128,174 shares in 10
Net: +41,072 shares (+4.2% of insider holdings) | insiders hold 1,011,284 shares
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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: a material recall of ~31k RAV4 plug‑in hybrids provides a short‑term negative catalyst, while cheap valuation, strong earnings growth, four consecutive earnings beats and a bullish analyst consensus suggest longer‑term upside. Low trading volume adds technical caution, leading to a neutral stance with modest conviction.

**Main reasons it gave:**
- Recall of ~31,000 RAV4 plug‑in hybrids (negative news)
- Trailing P/E 8.48 indicates cheap valuation (positive fundamentals)
- Four consecutive earnings beats (positive earnings record)
- Analyst consensus of 2 strong buys, 2 buys with +21% price target (positive analyst view)
- Low trading volume (0.30× 20‑day average) suggests technical caution

<details><summary><b>News</b> — score -0.60</summary>

- [A new dental mixing tip delivers up to 60% more uses per product than earlier models.](https://www.stocktitan.net/news/MDMXF/medmix-launches-mixpac-tm-picco-mix-tm-to-advance-efficiency-and-2c2940fg8rbs.html)  
  <sub>Stock Titan, 8 hours ago</sub>  
  The tip also reduces dental material waste by 52% and has 12 mixing elements, versus 8 in previous models, with options for root canal and intra-oral use.
- [3 Asia Pacific Dividend Stocks Built For Rough Markets](https://finance.yahoo.com/markets/stocks/articles/3-asia-pacific-dividend-stocks-042745056.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  When headlines focus on slower Asian growth, higher bond yields and the risk of an energy shock from the Middle East, it is easy to assume every stock is in...
- [(HMAX) Stock Evaluation Report (HMAX:CA)](https://news.stocktradersdaily.com/canada/hmax-stock-evaluation-report_20261014_43bf7a)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Stock Evaluation Report for Hamilton Canadian Financials YIELD MAXIMIZER TM ETF (HMAX) Including Buy/Sell Signals.
- [REG - Fusion Antibodies - Result of AGM](https://www.tradingview.com/news/reuters.com,2026-10-15:newsml_RSO1632Za:0-reg-fusion-antibodies-result-of-agm/)  
  <sub>TradingView, 2 hours ago</sub>  
  RNS Number : 1632Z Fusion Antibodies PLC 15 October 2026 Fusion Antibodies plc("Fusion" or the "Company")Result of AGMFusion Antibodies plc (AIM: FAB),...
- [JetBlue’s first-class cabin starts flying Dec. 8 from Boston to Fort Lauderdale.](https://www.stocktitan.net/news/JBLU/jet-blue-s-blue-first-tm-new-domestic-first-class-now-on-okncbqafjwi7.html)  
  <sub>Stock Titan, 39 minutes ago</sub>  
  Introductory one-way fares start at $249 on select flights; seats offer up to seven inches more legroom than JetBlue Main, with more routes to follow.
- [Qnity Announces Fourth Quarter 2026 Dividend on Common Stock](https://www.businesswire.com/news/home/20261014162488/en/Qnity-Announces-Fourth-Quarter-2026-Dividend-on-Common-Stock)  
  <sub>Business Wire, 18 hours ago</sub>  
  Qnity Electronics, Inc. (“Qnity”) (NYSE: Q), a premier technology solutions leader across the semiconductor value chain, announced that its Board of...
- [Toyota recalls nearly 31,000 RAV4 plug-in hybri...](https://pluang.com/en/news-feed/toyota-tarik-kembali-31000-rav4-plug-in-hybrid-karena-masalah-perangkat-lunak)  
  <sub>Pluang, 12 hours ago</sub>  
  Toyota is recalling 30978 units of its 2026 RAV4 Plug-in Hybrid due to a software defect that may cause the plug-in hybrid system to reduce power or shut...
- [PyroGenesis Completes Seven-System Drosrite(TM) Deployment at World's Largest Aluminum Complex](https://stockhouse.com/news/press-releases/2026/10/15/pyrogenesis-completes-seven-system-drosrite-tm-deployment-at-world-s-largest)  
  <sub>Stockhouse, 4 hours ago</sub>  
  Final four systems now operational, including PyroGenesis' first 10000-tonnes-per-year system, fulfilling original contract.
- [BioVie Inc. (BIVI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/BIVI/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest BioVie Inc. (BIVI) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [(HBND) Market Insights and Trading Signals (HBND:CA)](https://news.stocktradersdaily.com/canada/hbnd-market-insights-and-trading-signals_20261014_8988bc)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Market Insights Report for Hamilton U.S. Bond YIELD MAXIMIZER TM ETF (HBND) with Key Trading Signals.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 192.87 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 187.26 (+3.0%), 50d 190.65 (+1.2%), 200d 200.02 (-3.6%); 50d below 200d
Momentum: RSI(14) 58.1 | MACD -0.724 vs signal -1.467 (histogram 0.743)
Returns: 1d +2.3% | 5d +3.7% | 1m +0.3% | 3m +8.6%
52-week range: 166.50 - 248.29 (now 32.2% of the way up)
Volatility: ATR(14) 3.05 (1.6% of price) | annualised 20d 21.3%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 227.16B
Valuation: trailing P/E 8.48 | forward P/E 12.22 | P/B 15.51 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+21.4% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Alphabet Stock Can Soar 24%, JPMorgan Says. Why Google Can Defy AI Fears.](https://www.barrons.com/articles/google-alphabet-stock-ai-slump-1aa9c42e)  
  <sub>Barron's, 53 minutes ago</sub>  
  Megacap earnings are always a blockbuster event for the market—but there will be even more than usual riding on them this quarter.
- [Google DeepMind Chair Warns Rogue AI Agent Hacks Are Early Warning Shots](https://www.tikr.com/blog/alphabet-stock-deepmind-hassabis-ai-agent-hacks-warning)  
  <sub>TIKR.com, 2 hours ago</sub>  
  Alphabet stock in focus as DeepMind's Demis Hassabis says rogue AI agent hacks are early warning shots. Here's what it means for investors.
- [Prediction: AI Could Transform This Magnificent 7 Stock Over the Next 3 Years](https://247wallst.com/investing/2026/10/15/prediction-ai-could-transform-this-magnificent-7-stock-over-the-next-3-years/)  
  <sub>24/7 Wall St., 11 minutes ago</sub>  
  GOOG posted 24% revenue growth and 82% Cloud expansion, yet shares trade at $348, a full 44% below the $500 bull case target. Google's $514B cloud backlog,...
- [Alphabet (GOOGL) Falls More Steeply Than Broader Market: What Investors Need to Know](https://finance.yahoo.com/markets/stocks/articles/alphabet-googl-falls-more-steeply-204504949.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Alphabet (GOOGL) reached $347.64 at the closing of the latest trading day, reflecting a -1.74% change compared to its last close.
- [MU, SNDK, SKHY Stocks Jump: Google's AI Hunger, Elon Musk's Micron Shoutout Send Memory Bulls Charging](https://stocktwits.com/news-articles/markets/equity/mu-sndk-skhy-stocks-jump-google-s-ai-hunger-elon-musk-s-micron-shoutout-send-memory-bulls-charging/cZZn7enR7D6)  
  <sub>Stocktwits, 5 hours ago</sub>  
  MU, SNDK, SKHY: Retail's View On Memory Stocks. On Stocktwits, the retail sentiment was 'neutral' for MU and SNDK, and 'bearish' for SKHY and DRAM.
- [YouTube in talks with publishers over potential audiobook service (GOOG:NASDAQ)](https://seekingalpha.com/news/4653313-youtube-in-talks-with-publishers-over-potential-audiobook-service)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  YouTube, the video-streaming platform owned by Alphabet's Google (GOOG), has held discussions with publishers in recent months about developing an audiobook...
- [Discover which dow jones stocks are making waves on Wednesday.](https://www.chartmill.com/news/WMT/Chartmill-56226-Discover-which-dow-jones-stocks-are-making-waves-on-Wednesday)  
  <sub>ChartMill, 20 hours ago</sub>  
  Uncover the latest developments among dow jones stocks in today's session. Stay tuned to the dow jones index's top gainers and losers on Wednesday.
- [$Alphabet-A (GOOGL.US)$ As always](https://www.moomoo.com/community/feed/alphabet-a-googl-us-as-always-117442730721290)  
  <sub>Moomoo, 12 hours ago</sub>  
  Disclaimer: Community is offered by Moomoo Technologies Inc. and is for educational purposes only.Read more. Lol. 1. 945 Views. Report. Comments.
- [Google Just Started Paying SpaceX $920 Million a Month. Here's What That's Worth per Share.](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL-Q/pressreleases/7776751/google-just-started-paying-spacex-920-million-a-month-here-s-what-that-s-worth-per-share/)  
  <sub>The Globe and Mail, 8 hours ago</sub>  
  Google is renting compute from SpaceX for $920 million per month. The contract is 33 months, from October 2026 through June 2029, for a total value of about...
- [Prediction: Alphabet Will Soar After Oct. 28](https://www.fool.com/investing/2026/10/14/prediction-alphabet-will-soar-after-october-28/)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  An important event is coming up for Alphabet (GOOG -1.68%) (GOOGL -1.74%) investors: its third-quarter earnings. I think it has a great setup heading into...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 349.74 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 346.89 (+0.8%), 50d 344.93 (+1.4%), 200d 340.77 (+2.6%); 50d above 200d
Momentum: RSI(14) 53.3 | MACD 1.801 vs signal 1.218 (histogram 0.583)
Returns: 1d +0.6% | 5d +0.4% | 1m +2.0% | 3m +0.9%
52-week range: 250.46 - 402.62 (now 65.2% of the way up)
Volatility: ATR(14) 8.70 (2.5% of price) | annualised 20d 21.0%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.28T
Valuation: trailing P/E 17.86 | forward P/E 22.93 | P/B 6.87 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.21 | short interest 1.4% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
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
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 44 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 430.51 (+23.1% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-10-14 UBS: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-10-08 Needham: reit, Buy -> Buy
  - 2026-10-06 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
Institutional ownership: 81.0%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 195,190,800 shares
Distinct insiders: 0 buying, 0 selling
(2 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [JPMorgan Chase & Co. (JPM) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/JPM/)  
  <sub>Yahoo Finance Singapore, 6 hours ago</sub>  
  6,580.86% · Previous close 331.43 · Open 327.17 · Bid -- · Ask -- · Day's range 326.40 - 336.17 · 52-week range 279.10 - 366.50 · Volume 10,236,412 · Avg.
- [JPMorgan Chase & Co. $JPM Stock: Thurston Springer Miller Herd & Titak Inc. Lowers Stake](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-thurston-springer-miller-herd-titak-inc-lowers-stake-2026-10-15/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Thurston Springer Miller Herd & Titak Inc. reduced its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 80.1% in the third quarter,...
- [JPMorgan Chase (JPM) Stock Faces Rising Costs Despite Profit Strength](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/jpmorgan-chase-jpm-stock-faces-rising-costs-despite-profit-s)  
  <sub>Simply Wall Street, 13 hours ago</sub>  
  The market barely flinched. JPMorgan Chase shares edged about 1% higher into the print, even as the bank dropped a heavy Q3 earnings package that mixed...
- [JPMorgan Chase (JPM) Receives a New Rating from a Top Analyst](https://www.theglobeandmail.com/investing/markets/stocks/JPM-N/pressreleases/7832073/jpmorgan-chase-jpm-receives-a-new-rating-from-a-top-analyst/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPM, GS, MS Stocks Edge Higher After-Hours — Banks Lift Dividends And Announce Buybacks After Fed Stress Test](https://stocktwits.com/news-articles/markets/equity/jpm-gs-ms-stocks-edge-higher-after-hours-banks-lift-dividends-buybacks-fed-stress-test/cZKypH4R7Q3)  
  <sub>Stocktwits, 19 hours ago</sub>  
  JPM, GS, MS Stocks Edge Higher After-Hours — Banks Lift Dividends And Announce Buybacks After Fed Stress Test · JPM's Buyback And Dividend Boost · GS, MS Raise...
- [JPM, Phillip Securities Lowers Price Target to $370 Amid Earnings Adjustments](https://www.gurufocus.com/news/9124984/jpm-phillip-securities-lowers-price-target-to-370-amid-earnings-adjustments)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On October 15, 2026, Phillip Securities revised its price target for JPMorgan Chase (JPM) from $380 to $370 while maintaining an "Accumulate" rating.
- [JPMorgan Chase & Co. $JPM Stock Acquired by First Citizens Bank & Trust Co.](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-acquired-by-first-citizens-bank-trust-co-2026-10-15/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  First Citizens Bank & Trust Co. lifted its stake in shares of JPMorgan Chase & Co. (NYSE:JPM) by 18.7% in the 3rd quarter, according to its most recent...
- [TD Cowen Remains a Hold on JPMorgan Chase (JPM)](https://www.theglobeandmail.com/investing/markets/stocks/JPM/pressreleases/7867120/td-cowen-remains-a-hold-on-jpmorgan-chase-jpm/)  
  <sub>The Globe and Mail, 47 minutes ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPMorgan's Q3 Miss Is Noise, But Tread Carefully (NYSE:JPM)](https://seekingalpha.com/article/4954207-jpmorgan-q3-miss-is-noise-but-tread-carefully)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  JPMorgan Chase & Co. maintains strong fundamentals, but its P/B valuation premium leads to reaffirm a Hold rating. Read more on JPM stock here.
- [JPM Oct 2026 325.000 call (JPM261030C00325000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/JPM261030C00325000/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest JPM Oct 2026 325.000 call (JPM261030C00325000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 335.33 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 336.14 (-0.2%), 50d 348.45 (-3.8%), 200d 322.28 (+4.0%); 50d above 200d
Momentum: RSI(14) 44.1 | MACD -4.232 vs signal -4.909 (histogram 0.677)
Returns: 1d +0.0% | 5d +1.2% | 1m -3.9% | 3m -1.7%
52-week range: 282.84 - 365.18 (now 63.7% of the way up)
Volatility: ATR(14) 6.34 (1.9% of price) | annualised 20d 17.4%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 890.50B
Valuation: trailing P/E 13.90 | forward P/E 13.15 | P/B 2.53 | PEG 1.57
Profitability: profit margin 34.6% | operating margin 42.6% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 0.9% of float
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
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 9 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 372.35 (+11.0% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-10-14 Truist Securities: main, Hold -> Hold
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - 2026-10-14 Baird: main, Neutral -> Neutral
  - 2026-10-05 UBS: main, Buy -> Buy
Institutional ownership: 75.6%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 230,236 shares in 19
Net: -93,626 shares (-0.9% of insider holdings) | insiders hold 10,383,396 shares
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

- [Eli Lilly (LLY) Stock Looks Undervalued As Its 404% Run Continues](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-lly-stock-looks-211103429.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Eli Lilly's stock has become one of the most closely watched pharmaceuticals on the market, and at around US$1166 per share the question for investors is...
- [Here’s How Much You Would Have Made Owning Eli Lilly Stock In The Last 20 Years](https://www.benzinga.com/news/26/10/62384758/here-s-how-much-you-would-have-made-owning-eli-lilly-stock-last-20-years)  
  <sub>Benzinga, 26 minutes ago</sub>  
  Eli Lilly (NYSE:LLY) has outperformed the market over the past 20 years by 7.7% on an annualized basis producing an average annual return of 16.65%.
- [How Investors May Respond To Eli Lilly (LLY) Oral Weight Loss Rollout](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/how-investors-may-respond-to-eli-lilly-lly-oral-weight-loss)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Eli Lilly recently reported fresh clinical and regulatory progress across obesity, diabetes and oncology, including new TOGETHER-PsO biomarker data,...
- [Why Eli Lilly Became Wall Street’s Safe Haven on a Hot CPI Day](https://www.tikr.com/blog/why-eli-lilly-became-wall-streets-safe-haven-on-a-hot-cpi-day)  
  <sub>TIKR.com, 8 hours ago</sub>  
  Eli Lilly (LLY) stock rose roughly 4% on Wednesday, October 14, joining a broad rally in healthcare stocks. No major Lilly news drove it.
- [Dow Jones Futures Rise, But AI Sell-Off Continues On Anthropic News; Taiwan Semiconductor Earnings Strong](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-dell-amd-coreweave-ai-fears-anthropic-taiwan-semiconductor-due/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones futures rose slightly early Thursday while S&P 500 futures and especially Nasdaq futures fell on Anthropic revenue reports.
- [Eli Lilly (NYSE:LLY) Stock Surges Nearly 4% as Investors Rotate Out of Tech](https://stocksdownunder.com/eli-lilly-stock-rally-healthcare-tech-selloff/)  
  <sub>Stocks Down Under, 17 hours ago</sub>  
  Eli Lilly (LLY) stock jumped nearly 4% as healthcare shares rallied during a tech selloff. See what's driving the gains and what investors should watch...
- [LLY Stock Analysis: Explained](https://journalarta.com/en/2026/10/15/lly-stock-analysis-gains-3-62-testing-key-resistance/)  
  <sub>JournalArta, 6 hours ago</sub>  
  On October 14, 2026: price 1208.74 USD, trend sideways, RSI 60.5, support 1142.85, resistance 1208.74. technical analysis of lly stock.
- [Why is Eli Lilly stock rallying today?](https://www.investing.com/news/stock-market-news/why-is-eli-lilly-stock-rallying-today-93CH-4949655)  
  <sub>Investing.com, 24 hours ago</sub>  
  Investing.com -- Eli Lilly stock rose 3.3% in morning trading, reaching $1,205.24, as a confluence of pipeline developments and pre-earnings positioning...
- [LLY Stock Powers Higher As Obesity And Diabetes Pipeline Deepens](https://stockstotrade.com/news/eli-lilly-and-company-lly-news-2026_10_14/)  
  <sub>StocksToTrade, 22 hours ago</sub>  
  Eli Lilly and Company stocks have been trading up by 4.0 percent following strong demand signals for its obesity drugs. Key Takeaways For Active Traders...
- [Eli Lilly Rallies as Investors Revisit Obesity Pipeline and Bullish Price Targets](https://www.quiverquant.com/news/Eli+Lilly+Rallies+as+Investors+Revisit+Obesity+Pipeline+and+Bullish+Price+Targets)  
  <sub>Quiver Quantitative, 21 hours ago</sub>  
  Eli Lilly and Company (LLY) is up 3.9% today. Here is some analysis on what might have caused this p.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,263.44 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 1,174.15 (+7.6%), 50d 1,179.28 (+7.1%), 200d 1,079.08 (+17.1%); 50d above 200d
Momentum: RSI(14) 69.3 | MACD 11.550 vs signal 2.666 (histogram 8.884)
Returns: 1d +4.5% | 5d +8.0% | 1m +11.0% | 3m +7.2%
52-week range: 799.57 - 1,280.34 (now 96.5% of the way up)
Volatility: ATR(14) 36.10 (2.9% of price) | annualised 20d 28.3%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.13T
Valuation: trailing P/E 40.93 | forward P/E 26.61 | P/B 33.25 | PEG 1.14
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
Price target: mean 1,328.05 (+5.1% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-08 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-07 Morgan Stanley: main, Overweight -> Overweight
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
  - 2026-09-18 Guggenheim: main, Buy -> Buy
Institutional ownership: 85.3%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 1,479 shares in 28 transaction(s) | sold 308,215 shares in 8
Net: -306,736 shares (-18.0% of insider holdings) | insiders hold 1,390,517 shares
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 535.19 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 518.24 (+3.3%), 50d 504.86 (+6.0%), 200d 435.02 (+23.0%); 50d above 200d
Momentum: RSI(14) 63.2 | MACD 11.782 vs signal 10.789 (histogram 0.993)
Returns: 1d +0.3% | 5d +2.4% | 1m +9.2% | 3m +35.9%
52-week range: 352.83 - 543.45 (now 95.7% of the way up)
Volatility: ATR(14) 11.31 (2.1% of price) | annualised 20d 21.0%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.97T
Valuation: trailing P/E 30.36 | forward P/E 22.57 | P/B 8.98 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.10 | short interest 0.8% of float
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
Consensus: strong_buy (mean 1.34 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 13 strong buy, 40 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 594.52 (+11.1% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-15 TD Cowen: main, Buy -> Buy
  - 2026-10-13 Barclays: main, Overweight -> Overweight
  - 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-10-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-30 Piper Sandler: main, Overweight -> Overweight
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%), FMR, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 513,644 shares in 16 transaction(s) | sold 242,344 shares in 9
Net: +271,300 shares (+4.9% of insider holdings) | insiders hold 5,866,181 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
  - 2026-09-01 NADELLA SATYA (Chief Executive Officer): 86,525 shares, 43.39M
  - 2026-08-05 ALTHOFF JUDSON (Officer): 10,000 shares, 4.88M
  - 2026-08-04 NUMOTO TAKESHI (Officer): 4,810 shares, 2.39M
(15 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [What Investors Need To Know About The Israeli Elections](https://www.investors.com/news/israel-elections-netanyahu-stocks/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Israel's stock market is on a three-year bull run that is likely to continue. Here are the top stocks to watch ahead of the election.
- [TEVA Oct 2026 37.500 put (TEVA261016P00037500) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/TEVA261016P00037500/)  
  <sub>Yahoo Finance UK, 8 hours ago</sub>  
  Find the latest TEVA Oct 2026 37.500 put (TEVA261016P00037500) stock quote, history, news and other vital information to help you with your stock trading...
- [JPMorgan raises target for Teva stock to USD 50.00](https://www.ad-hoc-news.de/boerse/news/corporate-news/jpmorgan-raises-target-for-teva-stock-to-usd-50-00/70326391)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  Weltruza adds a once-monthly option in the United States after FDA approval on October 9, 2026. Teva stock enters its Q3 results date on November 3, 2026.
- [Here Are Thursday’s Top Wall Street Analyst Research Calls: AngloGold Ashanti, Bank of America, Cirrus Logic, Crocs, Diamondback Energy, Devon Energy, Netflix, PayPal, Spotify Technolgy , and More](https://247wallst.com/investing/2026/10/15/here-are-thursdays-top-wall-street-analyst-research-calls-anglogold-ashanti-bank-of-america-cirrus-logic-crocs-diamondback-energy-devon-energy-netflix-paypal-spotify-technolgy-and/?tpid=1681103&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Pre-Market Stock Futures: Futures are trading mixed, but the Nasdaq is down sharply Thursday morning as worries about AI overspending continue to emerge.
- [SPCX Stock Falls Ahead Of Share Unlock As Starlink Approaches New Milestone](https://stocktwits.com/news-articles/markets/equity/spcx-stock-falls-ahead-of-share-unlock-as-starlink-approaches-new-milestone/cZYdUSARJlw)  
  <sub>Stocktwits, 4 hours ago</sub>  
  SpaceX already has permission from the U.S. government to put between 15000 and 19000 of its Gen-1 and Gen-2 Starlink satellites into space.
- [SPHERA FUNDS MANAGEMENT LTD. Boosts Tenax Therapeutics Inc (TENX) Stake with 669,800-Share Purchase](https://www.gurufocus.com/news/9124918/sphera-funds-management-ltd-boosts-tenax-therapeutics-inc-tenx-stake-with-669800share-purchase)  
  <sub>GuruFocus, 6 hours ago</sub>  
  A Strategic Add Transaction in the Biotechnology Space On 2026-09-30, SPHERA FUNDS MANAGEMENT LTD. (Trades, Portfolio) executed an add transaction for Tenax...
- [Dr. Reddy's Laboratories (NYSE:RDY) Shares Cross Above Two Hundred Day Moving Average - Time to Sell?](https://www.marketbeat.com/instant-alerts/price-dr-reddys-laboratories-nyse-rdy-shares-cross-above-two-hundred-day-moving-average-time-to-sell-2026-10-15/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Dr. Reddy's Laboratories (NYSE:RDY) Stock Price Breaks Above Two Hundred Day Moving Average - Should You Sell?
- [Deckers Outdoor Corporation (DECK) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/DECK/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest Deckers Outdoor Corporation (DECK) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [WOLF Stock Drops 11% After Earnings Miss — Wolfspeed’s AI Growth Fails To Offset Negative Margins](https://stocktwits.com/news-articles/markets/equity/wolf-stock-drops-11-percent-after-earnings-miss-wolfspeed-ai-growth-fails-to-offset-negative-margins/cZYdwFjRJlM)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Shares of Wolfspeed Inc. (WOLF) fell around 11% in after-hours trading on Wednesday after the company reported earnings and revenue misses in its fiscal...
- [This biotech stock has a massive upside, Roth says](https://www.cantechletter.com/2026/10/this-biotech-stock-has-a-massive-upside-roth-says/)  
  <sub>Cantech Letter, 22 hours ago</sub>  
  Roth Capital Partners analyst Adam Walsh has reiterated his “Buy” rating and US$12.00 target on Equillium.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.44 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 39.85 (+4.0%), 50d 38.14 (+8.6%), 200d 34.10 (+21.5%); 50d above 200d
Momentum: RSI(14) 64.9 | MACD 0.880 vs signal 0.800 (histogram 0.080)
Returns: 1d +1.8% | 5d +5.6% | 1m +7.5% | 3m +29.4%
52-week range: 18.95 - 41.44 (now 100.0% of the way up)
Volatility: ATR(14) 1.19 (2.9% of price) | annualised 20d 28.8%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 48.33B
Valuation: trailing P/E 69.06 | forward P/E 13.44 | P/B 6.23 | PEG 0.71
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.6% of float
Next earnings: 2026-11-03
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39% | 2025-09-30 beat by 17%
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
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 47.58 (+14.8% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
Institutional ownership: 24.9%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.3% of insider holdings) | insiders hold 6,525,658 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-18 SAVAGE BRIAN (Officer): 7,342 shares, 285.21K
  - 2026-09-18 MIGNONE ROBERTO A. (Director): 367,600 shares, 14.36M
  - 2026-08-21 WEISS AMIR (Officer): 9,445 shares, 355.30K
  - 2026-08-03 HUGHES ERIC A (Officer): 25,578 shares, 892.05K
(13 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 175.01 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 165.36 (+5.8%), 50d 163.21 (+7.2%), 200d 151.43 (+15.6%); 50d above 200d
Momentum: RSI(14) 69.0 | MACD 3.372 vs signal 2.109 (histogram 1.264)
Returns: 1d -1.1% | 5d +3.9% | 1m +7.2% | 3m +18.8%
52-week range: 110.64 - 177.01 (now 97.0% of the way up)
Volatility: ATR(14) 3.48 (2.0% of price) | annualised 20d 20.4%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 719.63B
Valuation: trailing P/E 22.15 | forward P/E 15.08 | P/B 2.77 | PEG 1.38
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
Price target: mean 174.00 (-0.6% vs last close), range 142.00 - 200.00
Recent rating changes:
  - 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
  - 2026-08-17 Barclays: main, Overweight -> Overweight
  - 2026-08-07 TD Cowen: main, Buy -> Buy
Institutional ownership: 67.2%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.5%), State Street Corporation (5.0%), FMR, LLC (3.3%), Vanguard Portfolio Management LLC (2.8%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-194.8% of insider holdings) | insiders hold 3,371,767 shares
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
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

## Whole-market funds

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price 28.32 below 20‑day SMA (‑0.3%) and 50‑day SMA (‑0.5%)
- RSI 46.7 (neutral) and MACD slightly negative
- Flat fund flows (share count +0.0% over 1 week)
- No analyst ratings or price targets for holdings

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco DB Agriculture Fund (DBA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/DBA/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest Invesco DB Agriculture Fund (DBA) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.32 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 28.40 (-0.3%), 50d 28.47 (-0.5%), 200d 27.26 (+3.9%); 50d above 200d
Momentum: RSI(14) 46.7 | MACD -0.051 vs signal -0.036 (histogram -0.014)
Returns: 1d +0.2% | 5d -0.1% | 1m -1.8% | 3m +1.7%
52-week range: 25.44 - 29.49 (now 71.0% of the way up)
Volatility: ATR(14) 0.27 (0.9% of price) | annualised 20d 12.1%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +13.9% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.36B
What it is made of: Other 51.0%, Cash 47.0%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 42.3%, Invesco Short Term Treasury ETF 4.6%
Sector mix: Healthcare 16.8%, Industrials 15.2%, Financial services 13.7%, Consumer cyclical 11.8%
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 27.60M | fund size: 781.49M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crude oil inventories draw of -3.2 million barrels (bullish) vs natural gas build of +85 BCF (bearish)
- EIA forecasts falling crude (to $86 in 6 months) and gas (to $2.59 in 6 months) prices
- Fund flows flat: share count unchanged (+0.0% over 1 week)
- Technicals show price near 52‑week high with modest momentum, no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.28 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 32.78 (+1.5%), 50d 31.90 (+4.3%), 200d 28.64 (+16.2%); 50d above 200d
Momentum: RSI(14) 59.8 | MACD 0.354 vs signal 0.347 (histogram 0.007)
Returns: 1d -0.1% | 5d +1.1% | 1m +0.4% | 3m +14.8%
52-week range: 22.11 - 33.68 (now 96.5% of the way up)
Volatility: ATR(14) 0.46 (1.4% of price) | annualised 20d 15.1%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +15.4% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.92B
What it is made of: Other 50.4%, Cash 45.1%, Bonds 2.5%, Stocks 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.5%, Brent Crude Future Dec 26 9.7%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

```text
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 111.40M | fund size: 3.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields slipped modestly (10‑yr -0.17%, 30‑yr -0.21%) with no surprise
- Technicals: price below 50‑day SMA (-1.6%) and 200‑day SMA (-3.5%) with low volume (0.29× 20‑day avg)
- Fund flows: week‑long outflow of -0.9% shares (~$119 M) indicating slight net redemption
- Fund basics: yield 5.4%, three‑year return +9.5%/yr, credit quality mixed but 88% US government debt

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.85 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 91.57 (+0.3%), 50d 93.32 (-1.6%), 200d 95.21 (-3.5%); 50d below 200d
Momentum: RSI(14) 48.0 | MACD -0.625 vs signal -0.797 (histogram 0.173)
Returns: 1d +0.7% | 5d +1.0% | 1m -1.3% | 3m -3.9%
52-week range: 90.14 - 97.74 (now 22.4% of the way up)
Volatility: ATR(14) 0.53 (0.6% of price) | annualised 20d 7.5%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.9%, BB 25.2%, B 19.3%, A 17.6% | US government debt 88.0%
Three-year record: +9.5% a year | beta to the market 1.10
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.9% (-118.97M) over 7d
Shares outstanding: 142.21M | fund size: 13.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bullish shift in speculator positioning offset by mixed technicals and unchanged fundamentals.

**Main reasons it gave:**
- 10-year Treasury yield fell 0.17% on the week, boosting bond price gains
- Large speculators net short 37.3% of open interest, short position decreased 1.4% on the week
- IEF price above 20-day SMA (+0.9%) but below 50-day SMA (-0.9%), mixed trend
- Fund flows flat (share count unchanged), indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.54 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 89.74 (+0.9%), 50d 91.37 (-0.9%), 200d 94.16 (-3.9%); 50d below 200d
Momentum: RSI(14) 54.9 | MACD -0.464 vs signal -0.664 (histogram 0.199)
Returns: 1d +0.9% | 5d +1.2% | 1m -0.2% | 3m -3.5%
52-week range: 88.92 - 97.99 (now 17.8% of the way up)
Volatility: ATR(14) 0.51 (0.6% of price) | annualised 20d 6.7%
Volume: 0.44x the 20-day average
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
Three-year record: +3.1% a year | beta to the market 1.16
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 37.3% of open interest (5,742,990 contracts)
Change on the week: -1.4% of open interest
Crowding: 70% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 146.00M | fund size: 13.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no macro surprise, technical break not decisive, and mixed positioning signals.

**Main reasons it gave:**
- Price 273.81 below 20‑day SMA 279.93, 50‑day SMA 289.60, and 200‑day SMA 277.53
- RSI 34.5 (oversold) with low volume (0.48× 20‑day average)
- CFTC net short 24.8% of open interest, short crowding (8% percentile) and weekly increase of +2% OI
- Macro: Treasury yields up modestly, VIX up 2.0 points to 17.44, no Fed policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [History Says This ETF Could Turn $100 per Month Into $167,690 in 20 Years. Here's How.](https://finance.yahoo.com/markets/stocks/articles/history-says-etf-could-turn-002000533.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Most of the attention in the stock market goes to the largest companies: large-cap stocks, some of which are worth more than $1 trillion.
- [Broad Selling Breaks the Fragile Recovery as Small Caps Sink](https://www.chartmill.com/news/IWM/Chartmill-56241-market-breadth-2026-10-14-broad-selling-small-caps)  
  <sub>ChartMill, 6 hours ago</sub>  
  Wednesday's selloff pushed all three major ETFs below their short-term moving averages and drove several breadth measures to 20-session lows.
- [Small caps slide as Russell 2000 enters correction territory (IWM:NYSEARCA)](https://seekingalpha.com/news/4653255-small-caps-slide-as-russell-2000-enters-correction-territory)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The deepening tech selloff is making headlines, but subtle trouble elsewhere is brewing beneath the surface. The small-cap Russell 2000 Index (RTY) has...
- [iShares Russell 2000 ETF (IWM) Hits Lowest Price Since May, Trad](https://www.gurufocus.com/news/9123788/ishares-russell-2000-etf-iwm-hits-lowest-price-since-may-trading-below-key-moving-averages)  
  <sub>GuruFocus, 21 hours ago</sub>  
  On October 14, 2026, the iShares Russell 2000 ETF (ticker: IWM) declined to $271.45 per share, marking its lowest level since May 19.
- [Russell 2000 ETF breaks below major moving averages and tags a near 5-month low](https://seekingalpha.com/news/4653068-russell-2000-etf-breaks-below-major-moving-averages-and-tags-a-near-5-month-low)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The iShares Russell 2000 ETF (IWM), which tracks the Russell 2000 Index (RTY), last traded at $271.45 a share—its lowest level since May 19.
- [8 Of 11 Sectors Fall Wednesday As Defensives Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62359155/8-of-11-sectors-fall-wednesday-as-defensives-lead)  
  <sub>Benzinga, 23 hours ago</sub>  
  Three sectors are higher and eight are lower in Wednesday's regular session, with defensive sectors holding the top three positions.
- [Cboe to expand options trading hours for major stocks and ETFs](https://www.cnbc.com/amp/2026/10/15/cboe-stock-etf-options-extended-hours.html)  
  <sub>CNBC, 3 hours ago</sub>  
  Cboe will offer trading on 24 of the most actively traded companies and five ETFs between 7:30 a.m. and 9:25 a.m. ET and 4:00 p.m. to 4:15 p.m. ET.
- [iShares Russell 2000 Index Fund (IWM) Adds Crescent Energy and Moelis on Oct. 13](https://finance.yahoo.com/markets/stocks/articles/ishares-russell-2000-index-fund-110414587.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. iShares Russell 2000 Index Fund (IWM) reported a net $984.3 million in ETF activity on Tuesday, Oct. 13,...
- [Exchange-Traded Funds Lower as US Equities Drop After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-lower-us-170825191.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 1.7%.
- [Cboe plans to extend options trading hours for major stocks and ETFs - report (CBOE:BATS)](https://seekingalpha.com/news/4653363-cboe-plans-to-extend-options-trading-hours-for-major-stocks-and-etfs-report)  
  <sub>Seeking Alpha, 44 minutes ago</sub>  
  Cboe Global Markets (CBOE) and the Options Clearing Corp. have been cleared by regulators to offer trading on 24 of the most actively traded companies and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 273.81 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 279.93 (-2.2%), 50d 289.60 (-5.5%), 200d 277.53 (-1.3%); 50d above 200d
Momentum: RSI(14) 34.5 | MACD -3.936 vs signal -3.669 (histogram -0.266)
Returns: 1d +0.9% | 5d -1.4% | 1m -3.6% | 3m -6.9%
52-week range: 229.11 - 305.09 (now 58.8% of the way up)
Volatility: ATR(14) 3.61 (1.3% of price) | annualised 20d 13.1%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.35 | P/B 2.02 | P/S 1.25 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +18.9% a year | beta to the market 1.27
Cost and size: expense ratio 0.19% | net assets 78.04B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%, Twist Bioscience Corp 0.4%, Moog Inc Class A 0.4%, JFrog Ltd Ordinary Shares 0.4%, 10x Genomics Inc Ordinary Shares - Class A 0.4%
Sector mix: Healthcare 20.9%, Financial services 18.0%, Technology 14.5%, Industrials 13.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.1% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-14 UBS: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 24.8% of open interest (425,152 contracts)
Change on the week: +2.0% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 76.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (no net creations/redemptions) indicating no strong demand shift
- No macro surprise; yields fell modestly but market expects future rate hikes
- Technicals show price below 50‑day and 200‑day SMA with low volume, no decisive break
- Macro data (inflation 3.7%, unemployment 4.2%) within expectations, no material change

<details><summary><b>News</b> — score +0.00</summary>

- [LQD Sep 2027 104.000 put (LQD270917P00104000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/LQD270917P00104000/chart/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  OPR - Delayed Quote • USD. LQD Sep 2027 104.000 put (LQD270917P00104000). 4.7000 0.0000 (0.00%). As of September 28 at 3:25:24 p.m. EDT. Market Open. Tools.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.54 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 102.92 (+0.6%), 50d 104.61 (-1.0%), 200d 108.05 (-4.2%); 50d below 200d
Momentum: RSI(14) 52.4 | MACD -0.571 vs signal -0.771 (histogram 0.200)
Returns: 1d +0.9% | 5d +1.0% | 1m -0.9% | 3m -3.7%
52-week range: 101.83 - 112.92 (now 15.5% of the way up)
Volatility: ATR(14) 0.63 (0.6% of price) | annualised 20d 7.0%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Corporate Bond
Yield: 4.9%
Credit quality: A 46.6%, BBB 40.2%, AA 12.3%, AAA 1.0%
Three-year record: +5.0% a year | beta to the market 1.35
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 293.50M | fund size: 30.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest technical uptrend but no decisive break, thin analyst coverage with mixed price target, net short position slightly reduced, fundamentals unchanged.

**Main reasons it gave:**
- Technical: price above 20‑day SMA (+1.2%) and 200‑day SMA (+3.6%) but below 50‑day SMA (-0.9%); RSI 53.9, no decisive break
- Analyst coverage thin (1.4% of fund) with 78.5% buy rating but weighted price target -9.3% vs current price
- CFTC positioning: net short 21.5% of open interest, short reduced 1.8% week‑over‑week, low crowding (27th percentile)
- Fund basics unchanged: P/E 20.26, yield 1.5%, three‑year return 16.9%/yr, no significant shift
- Macro: Treasury yields fell modestly, VIX rose to 17.44, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 213.96 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 211.40 (+1.2%), 50d 215.90 (-0.9%), 200d 206.62 (+3.6%); 50d above 200d
Momentum: RSI(14) 53.9 | MACD -0.541 vs signal -1.150 (histogram 0.608)
Returns: 1d +0.9% | 5d +1.0% | 1m +0.8% | 3m +0.3%
52-week range: 182.18 - 222.77 (now 78.3% of the way up)
Volatility: ATR(14) 1.85 (0.9% of price) | annualised 20d 8.7%
Volume: 0.76x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Large Blend
What it holds: P/E 20.26 | P/B 2.97 | P/S 1.87 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +16.9% a year | beta to the market 0.84
Cost and size: expense ratio 0.20% | net assets 96.06B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.3%, Everpure Inc Class A 0.3%, Illumina Inc 0.3%, CrowdStrike Holdings Inc Class A 0.3%, Revvity Inc 0.3%
Sector mix: Technology 18.0%, Industrials 15.2%, Financial services 13.5%, Healthcare 12.6%
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
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -9.3% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-15 Goldman Sachs: main, Neutral -> Neutral
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-13 TD Cowen: main, Hold -> Hold
  - CRWD: 2026-10-14 Freedom Broker: main, Buy -> Buy
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 21.5% of open interest (1,932,227 contracts)
Change on the week: -1.8% of open interest
Crowding: 27% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 155.55M | fund size: 33.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bullish tilt from positioning and macro surprise, but no decisive catalyst.

**Main reasons it gave:**
- Inflation 3.7% came in hotter than expected, but Treasury yields fell (3‑month +0.03%, 5‑year -0.13%, 10‑year -0.17%) indicating a news failure
- CME FedWatch shows October rate hike odds dropped below 30%
- CFTC positioning: net short 28% of open interest, down 2.3% week‑over‑week, crowding at 97th percentile
- Technicals: price near 20‑day SMA, RSI 52.3, MACD near zero, no decisive trend break

<details><summary><b>News</b> — score +0.00</summary>

- [Does AI matter more than the Fed now to bond traders?](https://seekingalpha.com/news/4653411-does-ai-matter-more-than-the-fed-now-to-bond-traders)  
  <sub>Seeking Alpha, 6 minutes ago</sub>  
  Douglas Rissing. Bond traders now are shelving the central bank playbook, seemingly shrugging off scorching inflation prints to obsess instead over whether...
- [BTIG: U.S. Treasury yields fail to rise despite inflation exceeding expectations; “rates and Nasdaq falling in tandem” may emerge as the most painful trade](https://www.moomoo.com/news/post/1001240161/btig-us-treasury-yields-fail-to-rise-despite-inflation-exceeding)  
  <sub>Moomoo, 11 hours ago</sub>  
  U.S.investment bank BTIG said Wednesday that, following inflation data that came in higher than expected, the bond market has exhibited a classic 'news...
- [October rate hike odds retreat below 30%](https://seekingalpha.com/news/4653437-october-rate-hike-odds-retreat-below-30)  
  <sub>Seeking Alpha, 21 minutes ago</sub>  
  Market pricing for Federal Reserve policy has shifted sharply in the past day, according to the CME FedWatch tool.
- [Bond market 'news failure' signals pain trade ahead - BTIG (TLT:NASDAQ)](https://seekingalpha.com/news/4653099-bond-market-news-failure-signals-pain-trade-ahead-btig)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  A "news failure" in the bond market following hotter-than-expected inflation data confirms that Treasury yields (SHY) (TLT) (IEF) have reached a tactical...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.32 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 81.18 (+0.2%), 50d 81.54 (-0.3%), 200d 82.19 (-1.1%); 50d below 200d
Momentum: RSI(14) 52.3 | MACD -0.081 vs signal -0.121 (histogram 0.040)
Returns: 1d +0.2% | 5d +0.2% | 1m +0.1% | 3m -0.8%
52-week range: 81.05 - 83.18 (now 12.9% of the way up)
Volatility: ATR(14) 0.12 (0.1% of price) | annualised 20d 1.6%
Volume: 0.22x the 20-day average
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
Three-year record: +3.9% a year | beta to the market 0.24
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 28.0% of open interest (4,485,811 contracts)
Change on the week: -2.3% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 209.30M | fund size: 17.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals lack decisive break, positioning and flows neutral.

**Main reasons it gave:**
- Treasury yields slipped modestly this week (10‑yr -0.17%, 5‑yr -0.13%) with no macro surprise
- Technicals show price just above 20‑day SMA, below 50‑day SMA, RSI 56.8, low volume, no decisive break
- CFTC positioning: net short 37.3% of open interest, weekly change -1.4%, indicating no strong directional bias
- Fund flows flat over the past week, share count unchanged, suggesting no new demand for exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 105.47 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 104.57 (+0.9%), 50d 105.92 (-0.4%), 200d 109.08 (-3.3%); 50d below 200d
Momentum: RSI(14) 56.8 | MACD -0.332 vs signal -0.532 (histogram 0.200)
Returns: 1d +0.6% | 5d +0.9% | 1m +0.1% | 3m -2.6%
52-week range: 103.98 - 112.20 (now 18.1% of the way up)
Volatility: ATR(14) 0.42 (0.4% of price) | annualised 20d 5.2%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.7%
Credit quality: AA 99.9% | US government debt 100.0%
Three-year record: +3.7% a year | beta to the market 0.71
Cost and size: expense ratio 0.18% | net assets 14.23B
What it is made of: Bonds 100.0%
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

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 37.3% of open interest (5,742,990 contracts)
Change on the week: -1.4% of open interest
Crowding: 70% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 177.70M | fund size: 18.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bearish pressure from speculators is offset by stable fundamentals and no clear macro or technical catalyst.

**Main reasons it gave:**
- Large speculators net short 30.2% of open interest, up 2.1% week‑over‑week
- Fund yield 5.0% aligns with 10‑year Treasury yield 5.06%, credit quality AA
- Price above 20‑day SMA (+1.9%) but below 50‑day SMA (‑0.5%), RSI 58.6, no decisive break
- 10‑year Treasury yield fell 0.17% this week, VIX up 2.0 points, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.37 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 78.84 (+1.9%), 50d 80.79 (-0.5%), 200d 84.99 (-5.4%); 50d below 200d
Momentum: RSI(14) 58.6 | MACD -0.662 vs signal -0.978 (histogram 0.316)
Returns: 1d +1.9% | 5d +3.2% | 1m -0.6% | 3m -4.9%
52-week range: 77.11 - 92.06 (now 21.8% of the way up)
Volatility: ATR(14) 0.83 (1.0% of price) | annualised 20d 12.5%
Volume: 0.77x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Long Government
Yield: 5.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +0.5% a year | beta to the market 2.31
Cost and size: expense ratio 0.15% | net assets 46.23B
What it is made of: Bonds 99.6%, Cash 0.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 30.2% of open interest (2,404,377 contracts)
Change on the week: +2.1% of open interest
Crowding: 85% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 109.70M | fund size: 8.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, no decisive technical break, thin analyst coverage, and weak positioning.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve, no policy surprise
- Technicals: price below 20‑day SMA, low volume, no decisive breakout
- CFTC positioning: net long 0.1% of OI, down 2.2% week‑over‑week
- Analyst coverage thin (11.4% of fund) despite bullish rating

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Repsol SA Stocks](https://www.tradingview.com/symbols/BX-REPEUR/etfs/)  
  <sub>TradingView, 6 hours ago</sub>  
  Explore funds investing in REPEUR in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Trading the Move, Not the Narrative: (VGK) Edition](https://news.stocktradersdaily.com/news_release/35/Trading_the_Move,_Not_the_Narrative:_VGK_Edition_101426075001_1792021802.html)  
  <sub>Stock Traders Daily, 19 hours ago</sub>  
  Price-action only: Vanguard Ftse Europe Etf (VGK) movements set the tone for institutional models. Trading the Move, Not the Narrative: (VGK) Edition.
- [Why Did QQQ (NASDAQ:QQQ), SPY (NYSEARCA:SPY), IWM (NYSEARCA:IWM) and VGK (NYSEARCA:VGK) Move Differently on October 14?](https://kalkine.ca/news/general-news/why-did-qqq-nasdaqqqq-spy-nysearcaspy-iwm-nysearcaiwm-and-vgk-nysearcavgk-move-differently-on-october-14)  
  <sub>kalkine.ca, 2 hours ago</sub>  
  Why Did QQQ (NASDAQ:QQQ), SPY (NYSEARCA:SPY), IWM (NYSEARCA:IWM) and VGK (NYSEARCA:VGK) Move Differently on October 14?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.87 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 87.07 (-0.2%), 50d 89.69 (-3.1%), 200d 87.76 (-1.0%); 50d above 200d
Momentum: RSI(14) 45.2 | MACD -0.987 vs signal -1.089 (histogram 0.101)
Returns: 1d +1.0% | 5d +1.7% | 1m -2.0% | 3m -1.9%
52-week range: 77.90 - 93.19 (now 58.7% of the way up)
Volatility: ATR(14) 0.89 (1.0% of price) | annualised 20d 13.9%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +18.1% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 37.17B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.0%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.7%, Shell PLC 1.6%
Sector mix: Financial services 25.3%, Industrials 19.8%, Healthcare 12.1%, Technology 9.0%
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
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.8% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 0.1% of open interest (493,234 contracts)
Change on the week: -2.2% of open interest
Crowding: 72% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 282.09M | fund size: 24.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage thin (22.2% of fund) but 100% buy rating with +43.7% price target
- CFTC speculators net long 4.3% of open interest, up 1.2% week‑over‑week, crowding at 60th percentile
- RSI 39.4 (near oversold) and price below 20‑day/50‑day SMA, volume 0.30× 20‑day average
- Macro: No policy or rate surprise; Treasury yields modestly changed, dollar down 0.16, VIX up modestly, inflation 3.7%

<details><summary><b>News</b> — score +0.00</summary>

- [Trading the Move, Not the Narrative: (VWO) Edition](https://news.stocktradersdaily.com/news_release/1/Trading_the_Move,_Not_the_Narrative:_VWO_Edition_101426105402_1792032842.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Price-action only: Vanguard Ftse Emerging Markets Etf (VWO) movements set the tone for institutional models. Trading the Move, Not the Narrative: (VWO)...
- [ETFs Investing in YTL Corp Bhd. Stocks](https://www.tradingview.com/symbols/OTC-YTLCF/etfs/)  
  <sub>TradingView, 16 hours ago</sub>  
  Explore funds investing in YTLCF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.57 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 59.82 (-2.1%), 50d 60.13 (-2.6%), 200d 58.23 (+0.6%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -0.257 vs signal -0.143 (histogram -0.114)
Returns: 1d -0.6% | 5d -0.9% | 1m -1.0% | 3m +1.3%
52-week range: 52.42 - 61.44 (now 68.2% of the way up)
Volatility: ATR(14) 0.64 (1.1% of price) | annualised 20d 15.4%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 15.91 | P/B 2.13 | P/S 1.86 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +18.5% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 164.66B
What it is made of: Stocks 95.3%, Cash 4.6%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 14.7%, Tencent Holdings Ltd 2.9%, Alibaba Group Holding Ltd Ordinary Shares 2.2%, MediaTek Inc 1.5%, Delta Electronics Inc 0.9%
Sector mix: Technology 31.8%, Financial services 20.2%, Consumer cyclical 9.9%, Basic materials 7.9%
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
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +43.7% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 4.3% of open interest (1,059,025 contracts)
Change on the week: +1.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 83.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Fed cornered by sticky CPI; Pantheon Macro sees another hike before year-end](https://seekingalpha.com/news/4653421-fed-cornered-by-sticky-cpi-pantheon-macro-sees-another-hike-before-year-end)  
  <sub>Seeking Alpha, 46 minutes ago</sub>  
  September's consumer price data has left the Federal Reserve with limited room to pause, Pantheon Macroeconomics noted.
- [U.S. ETF Express | Direxion Daily Semiconductor Bear 3x Shares ETF Was the Top Gainer, Rising 13.63%](https://www.moomoo.com/news/post/1001216599/us-etf-express-direxion-daily-semiconductor-bear-3x-shares-etf)  
  <sub>Moomoo, 17 hours ago</sub>  
  TopGainers/Losers1107 U.S. ETFs rose and 5040 fell today.The top gainer was $Direxion Daily Semiconductor Bear 3x Shares ETF(SOXS.US)$, climbing 13.63% to...
- [Nasdaq falls 1.2% as AI sell-off deepens on inflation and Fed rate fears](https://invezz.com/uk/news/2026/10/15/nasdaq-falls-12percent-as-ai-sell-off-deepens-on-inflation-and-fed-rate-fears/)  
  <sub>Invezz, 1 hour ago</sub>  
  Wall Street opened lower on Thursday as persistent inflation concerns and growing doubts over artificial intelligence spending weighed on technology shares.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.02 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 77.48 (-0.6%), 50d 78.59 (-2.0%), 200d 79.73 (-3.4%); 50d below 200d
Momentum: RSI(14) 33.3 | MACD -0.469 vs signal -0.495 (histogram 0.026)
Returns: 1d +0.3% | 5d -0.2% | 1m -1.8% | 3m -3.3%
52-week range: 76.81 - 81.28 (now 4.7% of the way up)
Volatility: ATR(14) 0.31 (0.4% of price) | annualised 20d 4.2%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: High Yield Bond
Yield: 6.1%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +8.2% a year | beta to the market 0.70
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 195.60M | fund size: 15.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.00 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 28.83 (+0.6%), 50d 28.39 (+2.2%), 200d 27.83 (+4.2%); 50d above 200d
Momentum: RSI(14) 62.2 | MACD 0.204 vs signal 0.202 (histogram 0.002)
Returns: 1d -0.4% | 5d +0.1% | 1m +2.1% | 3m +2.4%
52-week range: 26.47 - 29.13 (now 95.3% of the way up)
Volatility: ATR(14) 0.13 (0.4% of price) | annualised 20d 5.1%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +3.7% a year | beta to the market -11.39
Cost and size: expense ratio 0.75% | net assets 431.14M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 49.4%
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
Rolled up from the 1 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 1.7% of open interest (51,095 contracts)
Change on the week: +0.9% of open interest
Crowding: 80% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.5% (-2.07M) over 7d
Shares outstanding: 14.80M | fund size: 429.29M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

## Sector and country funds

### US media and communication (XLC) · Sector or country — BULLISH, confidence 0.40

**Result:** ACCEPTED · 60 shares · submitted buy 60 XLC @ ~112.12, stop 108.76

**In the model's own words:**

> Analyst consensus is strongly bullish (90.6% buy, +15% price target), fundamentals are solid (P/E 16.28, 3‑year return +20.1% per year), technicals show price above short‑term SMAs with neutral momentum, and macro conditions are stable with falling yields and no policy surprise. Fund flows are flat, providing no contrary signal.

**Main reasons it gave:**
- Analyst consensus 90.6% buy with +15% price target
- Fund fundamentals: P/E 16.28 and 3‑year return +20.1% per year
- Technicals: price above 20‑day and 50‑day SMAs, RSI 51, MACD near zero
- Macro: Treasury yields down, curve normal, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 112.03 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 111.80 (+0.2%), 50d 111.91 (+0.1%), 200d 113.54 (-1.3%); 50d below 200d
Momentum: RSI(14) 51.1 | MACD -0.157 vs signal -0.158 (histogram 0.001)
Returns: 1d +1.1% | 5d -0.0% | 1m -0.9% | 3m +1.2%
52-week range: 105.38 - 120.08 (now 45.2% of the way up)
Volatility: ATR(14) 1.68 (1.5% of price) | annualised 20d 20.3%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Communications
What it holds: P/E 16.28 | P/B 3.24 | P/S 2.42 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +20.1% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.53B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.2%, Alphabet Inc Class A 11.6%, Alphabet Inc Class C 9.3%, Warner Bros. Discovery Inc Ordinary Shares - Class A 4.9%, The Walt Disney Co 4.5%
Sector mix: Communication services 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.0% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-13 Pivotal Research: main, Buy -> Buy
  - GOOGL: 2026-10-14 UBS: main, Neutral -> Neutral
  - GOOG: 2026-10-14 UBS: main, Neutral -> Neutral
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-09 Needham: reit, Buy -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.2% (37.13M) over 7d
Shares outstanding: 202.20M | fund size: 22.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst view is the primary driver of a modest bearish tilt, while technicals, flows and fundamentals are neutral.

**Main reasons it gave:**
- Analyst view: 40.5% sell rating, mean rating 3.41, weighted price target -6.1% below current price
- Technicals: price above 20‑day SMA but below 50‑day SMA, MACD just above signal, low volume (0.24× 20‑day avg)
- Fund flows: flat share count over the week, indicating no net demand
- Macro: no surprise data; yields modestly down, VIX elevated but unchanged – no macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.76 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 28.51 (+0.9%), 50d 29.28 (-1.8%), 200d 28.74 (+0.1%); 50d above 200d
Momentum: RSI(14) 50.3 | MACD -0.156 vs signal -0.239 (histogram 0.083)
Returns: 1d +0.8% | 5d +1.9% | 1m +0.9% | 3m +0.0%
52-week range: 24.95 - 30.43 (now 69.5% of the way up)
Volatility: ATR(14) 0.33 (1.1% of price) | annualised 20d 15.0%
Volume: 0.24x the 20-day average
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
Three-year record: +14.6% a year | beta to the market 0.98
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
Weighted price target: -6.1% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 63.60M | fund size: 1.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view: 61% buy, price target +4.4% above current (modest bullish bias)
- Fund flows flat: share count unchanged (+0.0% week)
- Technical indicators neutral: price above 20‑day SMA but below 50‑day SMA, RSI 52, low volume
- Macro environment unchanged: no rate surprise, yields modestly down, VIX up modestly

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.83 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 59.26 (+1.0%), 50d 60.58 (-1.2%), 200d 57.95 (+3.2%); 50d above 200d
Momentum: RSI(14) 52.0 | MACD -0.292 vs signal -0.458 (histogram 0.165)
Returns: 1d +1.0% | 5d +2.6% | 1m -0.1% | 3m +0.6%
52-week range: 49.72 - 62.64 (now 78.3% of the way up)
Volatility: ATR(14) 0.69 (1.1% of price) | annualised 20d 14.7%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.94 | P/B 2.75 | P/S 2.69 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +24.1% a year | beta to the market 0.80
Cost and size: expense ratio 0.50% | net assets 7.02B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.5%, Shopify Inc Registered Shs -A- Subord Vtg 6.0%, Bank of Montreal 3.8%, Bank of Nova Scotia 3.7%
Sector mix: Financial services 39.9%, Energy 17.3%, Basic materials 15.2%, Technology 9.3%
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
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.4% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-14 Baird: main, Outperform -> Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 94.80M | fund size: 5.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals lack decisive break on volume, flows flat, analyst view modestly bullish but limited coverage, fundamentals solid but not decisive.

**Main reasons it gave:**
- Analyst coverage 28.9% of fund with 81.7% buy rating and +12.6% price target
- Fund flows flat: share count unchanged (+0.0% over 1 week)
- Technical: price 0.1% above 20‑day SMA but 2.3% below 50‑day SMA; volume 0.05× 20‑day average
- Macro: US 10‑yr yield down 0.17% on week, inflation 3.7% above target, VIX elevated at 17.44

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 50.77 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 50.71 (+0.1%), 50d 51.97 (-2.3%), 200d 51.46 (-1.3%); 50d above 200d
Momentum: RSI(14) 47.9 | MACD -0.343 vs signal -0.460 (histogram 0.117)
Returns: 1d +0.3% | 5d +1.3% | 1m -0.5% | 3m +1.4%
52-week range: 45.38 - 54.72 (now 57.7% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 16.0%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.64 | P/B 2.82 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +19.2% a year | beta to the market 1.25
Cost and size: expense ratio 0.51% | net assets 947.21M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Spotify Technology SA 9.7%, Investor AB Class B 9.6%, Atlas Copco AB Class A 7.1%, Volvo AB Class B 6.8%, Sandvik AB 5.3%
Sector mix: Industrials 46.3%, Financial services 25.6%, Communication services 13.5%, Technology 6.1%
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
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.6% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-15 StoneX: down, Buy -> Hold
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 7.65M | fund size: 388.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, bearish technicals, and limited analyst coverage.

**Main reasons it gave:**
- Flat fund flows (0% change in share count) indicating no net demand
- Price below 20‑day, 50‑day and 200‑day SMAs, indicating a bearish technical trend
- Analyst coverage bullish (+18.4% price target) but only covers 45.4% of holdings
- No macro surprise; yields stable and VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 41.26 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 41.53 (-0.6%), 50d 42.82 (-3.6%), 200d 42.33 (-2.5%); 50d above 200d
Momentum: RSI(14) 43.3 | MACD -0.491 vs signal -0.520 (histogram 0.029)
Returns: 1d +0.8% | 5d +1.5% | 1m -2.7% | 3m +0.3%
52-week range: 38.08 - 44.59 (now 48.9% of the way up)
Volatility: ATR(14) 0.47 (1.1% of price) | annualised 20d 14.6%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +19.5% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 79.50M | fund size: 3.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals not decisive, flat fund flows, but analyst view bullish and fundamentals solid.

**Main reasons it gave:**
- Analyst view: 100% buy rating, +21% price target for top holdings
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs, RSI 31.7 (oversold), low volume
- Macro: no policy or rate surprise, yields stable, VIX modestly elevated
- Fund flows: flat share count, no net inflows/outflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 56.18 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 58.23 (-3.5%), 50d 60.65 (-7.4%), 200d 58.11 (-3.3%); 50d above 200d
Momentum: RSI(14) 31.7 | MACD -1.332 vs signal -1.207 (histogram -0.125)
Returns: 1d +0.1% | 5d +0.2% | 1m -7.3% | 3m -6.8%
52-week range: 50.47 - 63.35 (now 44.3% of the way up)
Volatility: ATR(14) 0.77 (1.4% of price) | annualised 20d 18.8%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.42 | P/B 1.77 | P/S 1.50 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +27.8% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.17B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: UniCredit SpA 18.0%, Intesa Sanpaolo 15.0%, Enel SpA 10.6%, Eni SpA 4.7%, Prysmian SpA 4.7%
Sector mix: Financial services 54.1%, Utilities 16.5%, Industrials 12.0%, Consumer cyclical 8.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.0% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 8.55M | fund size: 480.34M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Inflation 3.7% near Fed target, no macro surprise
- Price 94.81 below 20-day SMA 97.45 and 50-day SMA 96.92, but no decisive technical break
- RSI 39.3, MACD negative, volume 0.32x 20-day average
- CFTC: net short 8.2% of OI, short positions fell 6.9% on week
- Analyst coverage 17% of fund, 100% buy, +23.5% price target (thin coverage)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 94.81 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 97.45 (-2.7%), 50d 96.92 (-2.2%), 200d 91.15 (+4.0%); 50d above 200d
Momentum: RSI(14) 39.3 | MACD -0.075 vs signal 0.303 (histogram -0.378)
Returns: 1d -1.1% | 5d -2.6% | 1m -2.3% | 3m +4.8%
52-week range: 79.49 - 99.32 (now 77.3% of the way up)
Volatility: ATR(14) 1.29 (1.4% of price) | annualised 20d 17.4%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.27 | P/B 1.98 | P/S 1.37 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +21.3% a year | beta to the market 0.83
Cost and size: expense ratio 0.49% | net assets 23.53B
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.7%, Toyota Motor Corp 3.3%, Tokyo Electron Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 3.0%, Advantest Corp 3.0%
Sector mix: Industrials 22.8%, Technology 22.0%, Financial services 19.3%, Consumer cyclical 11.1%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.5% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 8.2% of open interest (20,996 contracts)
Change on the week: -6.9% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 227.85M | fund size: 21.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, modest technical bullishness with low volume, and only modest analyst optimism.

**Main reasons it gave:**
- Flat fund flows (0% share count change over 1 week) indicating no net demand
- Technicals: price above 20‑, 50‑, 200‑day SMAs and RSI 61.8, but low volume (0.28× 20‑day average) and no decisive break
- Macro data shows no surprise; yields modestly changed, VIX 17.44, Fed target unchanged
- Analyst coverage of 48.2% of fund with 64.8% buy rating and price target +4.8% above current price

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 61.78 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 59.98 (+3.0%), 50d 61.69 (+0.2%), 200d 61.62 (+0.3%); 50d above 200d
Momentum: RSI(14) 61.8 | MACD -0.304 vs signal -0.604 (histogram 0.300)
Returns: 1d +2.1% | 5d +4.3% | 1m +2.9% | 3m -2.2%
52-week range: 55.06 - 65.08 (now 67.1% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 13.7%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.08 | P/B 4.13 | P/S 2.67 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +12.9% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.67B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.9%, Novartis AG Registered Shares 12.4%, Nestle SA 11.0%, UBS Group AG Registered Shares 6.4%, ABB Ltd 4.6%
Sector mix: Healthcare 38.0%, Financial services 19.6%, Consumer defensive 13.1%, Industrials 12.3%
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
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.8% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 28.62M | fund size: 1.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data HTTP 500: {"status_code":500,"error":"Proxy request failed","error_code":"unknown_proxy_error","details":"connect ECONNREFUSED 157.230.219.198:44445"}

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst consensus and solid fundamentals offset by weak technicals, flat fund flows and no macro surprise.

**Main reasons it gave:**
- Analyst consensus 100% buy with weighted price target +44.5% above current price
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 33.8 (oversold); MACD negative
- Fund flows flat: share count unchanged (0% change) over the week
- Macro data in line with expectations: inflation 3.7%, unemployment 4.2%, yields slightly down, VIX elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 64.37 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 67.10 (-4.1%), 50d 68.11 (-5.5%), 200d 64.75 (-0.6%); 50d above 200d
Momentum: RSI(14) 33.8 | MACD -0.713 vs signal -0.430 (histogram -0.283)
Returns: 1d -0.9% | 5d -2.7% | 1m -2.8% | 3m -3.7%
52-week range: 55.33 - 71.61 (now 55.5% of the way up)
Volatility: ATR(14) 0.93 (1.4% of price) | annualised 20d 18.2%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.85 | P/B 2.55 | P/S 1.87 | 3y earnings growth n/a
Yield: 4.2%
Three-year record: +24.3% a year | beta to the market 1.09
Cost and size: expense ratio 0.50% | net assets 710.44M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: ASML Holding NV 23.6%, ING Groep NV 9.1%, Nebius Group NV Shs Class-A- 4.9%, Prosus NV Ordinary Shares - Class N 4.6%, ASM International NV 4.4%
Sector mix: Technology 33.4%, Financial services 21.5%, Consumer defensive 10.4%, Industrials 9.6%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +44.5% above the current prices
Holdings read: ASML.AS, INGA.AS, NBIS, PRX.AS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-10-08 Rosenblatt: init, ? -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 5.55M | fund size: 357.25M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: analyst coverage is slightly bullish (51.5% buy, 48.5% hold) with a modest +6.6% price target; fundamentals are decent (P/E 15.94, yield 2.8%, strong 3‑yr record); technicals are weak (RSI 38.1, MACD below signal, price below 20‑day/50‑day SMAs); fund flows are flat (share count +0.0%); macro data are stable with no surprise. No material macro catalyst or decisive technical break is present, so the overall stance remains neutral.

**Main reasons it gave:**
- Technical indicators (RSI 38.1, MACD below signal) show weak momentum and price below 20‑day and 50‑day SMAs
- Fund flows flat (share count change +0.0% over 7 days) indicate no net demand
- Analyst view mixed (51.5% buy, 48.5% hold) with modest price target +6.6% suggests limited upside
- Macro data stable (inflation 3.7% near target, yields unchanged, VIX 17.44) with no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.08 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 59.27 (-2.0%), 50d 61.06 (-4.9%), 200d 57.80 (+0.5%); 50d above 200d
Momentum: RSI(14) 38.1 | MACD -0.909 vs signal -0.861 (histogram -0.048)
Returns: 1d +0.3% | 5d +0.3% | 1m -4.5% | 3m -1.8%
52-week range: 48.95 - 63.23 (now 64.0% of the way up)
Volatility: ATR(14) 0.77 (1.3% of price) | annualised 20d 17.1%
Volume: 0.03x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.94 | P/B 2.15 | P/S 1.78 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +33.7% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 2.38B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.3%, Iberdrola SA 12.8%, Repsol SA 5.0%, CaixaBank SA 4.5%
Sector mix: Financial services 45.6%, Utilities 20.7%, Industrials 14.1%, Technology 5.5%
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
Rolled up from the 5 largest holdings, 55.8% of the fund by weight
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.26 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.6% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 37.35M | fund size: 2.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, technicals lack decisive breakout, and analyst bullishness is limited to a minority of the fund.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% week)
- Macro unchanged: Treasury yields modestly down, inflation 3.7% (no surprise)
- Technical momentum weak: price below 20‑day SMA, RSI 39.6, low volume
- Analyst view bullish but covers only 39% of fund (buy rating 100% of covered weight)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 108.11 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 113.97 (-5.1%), 50d 109.87 (-1.6%), 200d 91.09 (+18.7%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD 0.598 vs signal 1.540 (histogram -0.942)
Returns: 1d -2.6% | 5d -4.6% | 1m -0.3% | 3m +11.1%
52-week range: 60.03 - 118.00 (now 82.9% of the way up)
Volatility: ATR(14) 2.32 (2.2% of price) | annualised 20d 27.0%
Volume: 0.54x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Greater China Region
What it holds: P/E 28.15 | P/B 4.48 | P/S 2.64 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +44.8% a year | beta to the market 1.26
Cost and size: expense ratio 0.59% | net assets 12.34B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 21.9%, MediaTek Inc 7.2%, Delta Electronics Inc 3.9%, Hon Hai Precision Industry Co Ltd 3.2%, ASE Technology Holding Co Ltd 3.0%
Sector mix: Technology 74.2%, Financial services 14.3%, Basic materials 3.8%, Industrials 2.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.83</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.83</summary>

```text
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +38.9% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 85.00M | fund size: 9.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, and modest bullish analyst view not enough to shift direction.

**Main reasons it gave:**
- Fund flows flat: share count unchanged over the week (0.0% change)
- Analyst ratings for top holdings overwhelmingly buy (90.9%) with price target +9.7% above current prices
- Technical indicators mixed: price above 20‑day SMA (+1.2%) but below 50‑day and 200‑day SMAs, low volume (0.34× 20‑day average)
- Macro data unchanged: yields modestly moved, no policy surprise, inflation 3.7% and unemployment 4.2% within expectations

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 73.36 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 72.48 (+1.2%), 50d 74.59 (-1.7%), 200d 75.92 (-3.4%); 50d below 200d
Momentum: RSI(14) 51.0 | MACD -0.507 vs signal -0.798 (histogram 0.291)
Returns: 1d +0.9% | 5d +2.6% | 1m +0.6% | 3m -2.3%
52-week range: 65.07 - 81.23 (now 51.3% of the way up)
Volatility: ATR(14) 1.26 (1.7% of price) | annualised 20d 19.0%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +14.1% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.16 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.7% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 18.90M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, flat fund flows and no analyst consensus. Fundamentals are modestly positive but offset by high beta and a downtrend.

**Main reasons it gave:**
- Technicals: price below 20‑day SMA and RSI 29.8 (oversold) with low volume
- Fund flows flat (0% change) indicating neutral demand
- Analyst view provides no ratings or price targets (no consensus)
- Macro: modest yield declines, VIX up modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 153.62 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 180.75 (-15.0%), 50d 179.18 (-14.3%), 200d 159.90 (-3.9%); 50d above 200d
Momentum: RSI(14) 29.8 | MACD -4.800 vs signal -1.091 (histogram -3.709)
Returns: 1d -3.9% | 5d -12.9% | 1m -12.5% | 3m -5.5%
52-week range: 85.17 - 219.20 (now 51.1% of the way up)
Volatility: ATR(14) 6.34 (4.1% of price) | annualised 20d 42.3%
Volume: 0.92x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.79 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +45.0% a year | beta to the market 2.48
Cost and size: expense ratio 0.59% | net assets 26.21B
What it is made of: Stocks 96.8%, Cash 3.2%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.8%, SK Square 3.1%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 1.9%
Sector mix: Technology 56.9%, Industrials 16.4%, Financial services 10.9%, Consumer cyclical 4.5%
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 75.60M | fund size: 11.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, no decisive technical break, and flat fund flows; analyst view is bullish but not enough to outweigh neutral macro/technical backdrop.

**Main reasons it gave:**
- Treasury yields changed modestly, no policy surprise
- Price below 50‑day and 200‑day SMAs, trend still bearish
- Fund flows flat, no net inflows or outflows
- Analyst coverage bullish (+32% target) but not supported by macro/technical

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 64.71 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 64.79 (-0.1%), 50d 67.79 (-4.5%), 200d 68.93 (-6.1%); 50d below 200d
Momentum: RSI(14) 46.9 | MACD -1.183 vs signal -1.320 (histogram 0.137)
Returns: 1d +2.3% | 5d +3.3% | 1m -4.2% | 3m +3.8%
52-week range: 60.43 - 81.60 (now 20.2% of the way up)
Volatility: ATR(14) 1.24 (1.9% of price) | annualised 20d 25.5%
Volume: 0.15x the 20-day average
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
Three-year record: +25.4% a year | beta to the market 1.07
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.2% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-10-15 Goldman Sachs: init, ? -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 7.90M | fund size: 511.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view and fundamentals versus bearish technicals and modest outflows, with no macro surprise.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +19.9% price target for top holdings
- Fund flows: -1.1% share count over 7 days (outflows of $284.34M)
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 41.6 (neutral to slightly oversold)
- Macro: yields fell modestly, dollar down 0.16, VIX up 2.0 (no major surprise)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 85.46 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 89.38 (-4.4%), 50d 93.33 (-8.4%), 200d 91.04 (-6.1%); 50d above 200d
Momentum: RSI(14) 41.6 | MACD -2.089 vs signal -1.720 (histogram -0.370)
Returns: 1d +2.5% | 5d -1.5% | 1m -7.9% | 3m +19.8%
52-week range: 68.28 - 115.84 (now 36.1% of the way up)
Volatility: ATR(14) 2.91 (3.4% of price) | annualised 20d 39.0%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 13.93 | P/B 3.18 | P/S 4.54 | 3y earnings growth n/a
Yield: 0.7%
Three-year record: +46.1% a year | beta to the market 0.81
Cost and size: expense ratio 0.51% | net assets 26.25B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Newmont Corp 11.1%, Agnico Eagle Mines Ltd 11.0%, Barrick Mining Corp 7.9%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.2%
Sector mix: Basic materials 100.0%
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
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.63 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.9% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-10-08 UBS: main, Neutral -> Neutral
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.1% (-284.34M) over 7d
Shares outstanding: 296.90M | fund size: 25.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, mixed technicals, flat fund flows, and a strong but limited analyst view.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +18.4% price target for 42.9% of fund weight
- Fund flows flat over past week (share count unchanged), indicating no net demand shift
- Fund fundamentals: high valuation multiples (P/E 31.87) but strong 3‑year record (+16.7% annual) and tech sector exposure
- Technicals: price above 50‑day and 200‑day SMA, below 20‑day SMA, MACD slightly bearish, low volume
- Macro: yields modestly down, VIX modestly higher, inflation 3.7% and unemployment 4.2% in line with expectations, no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 107.83 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 108.20 (-0.3%), 50d 105.77 (+2.0%), 200d 93.73 (+15.0%); 50d above 200d
Momentum: RSI(14) 50.9 | MACD 1.407 vs signal 1.620 (histogram -0.214)
Returns: 1d +0.2% | 5d -1.6% | 1m +2.7% | 3m +16.2%
52-week range: 74.67 - 117.08 (now 78.2% of the way up)
Volatility: ATR(14) 2.49 (2.3% of price) | annualised 20d 23.0%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Technology
What it holds: P/E 31.87 | P/B 7.50 | P/S 8.53 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +16.7% a year | beta to the market 1.22
Cost and size: expense ratio 0.38% | net assets 13.91B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Palo Alto Networks Inc 9.7%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, CrowdStrike Holdings Inc Class A 8.9%, Microsoft Corp 8.5%, Oracle Corp 6.9%
Sector mix: Technology 93.2%, Communication services 4.2%, Financial services 2.2%, Consumer cyclical 0.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-13 Wells Fargo: main, Overweight -> Overweight
  - PLTR: 2026-10-09 Barclays: init, ? -> Overweight
  - CRWD: 2026-10-14 Freedom Broker: main, Buy -> Buy
  - MSFT: 2026-10-15 TD Cowen: main, Buy -> Buy
  - ORCL: 2026-10-02 Citizens: reit, Market Outperform -> Market Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 12.50M | fund size: 1.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technicals show price above 20‑day SMA but below 50‑day and 200‑day SMA
- Analyst coverage of top holdings is bullish (+28.7% target) but only covers 23.7% of fund
- Fund flows flat with a modest 0.4% share count increase over the week
- US Treasury yields slipped modestly with no policy surprise; VIX rose to 17.44 indicating elevated volatility

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.78 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 47.06 (+1.5%), 50d 48.46 (-1.4%), 200d 49.53 (-3.5%); 50d below 200d
Momentum: RSI(14) 53.9 | MACD -0.436 vs signal -0.608 (histogram 0.172)
Returns: 1d +1.6% | 5d +4.9% | 1m +0.7% | 3m -2.3%
52-week range: 45.42 - 55.29 (now 23.9% of the way up)
Volatility: ATR(14) 0.53 (1.1% of price) | annualised 20d 15.3%
Volume: 0.90x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: India Equity
What it holds: P/E 21.36 | P/B 2.96 | P/S 2.56 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.3% a year | beta to the market 0.62
Cost and size: expense ratio 0.61% | net assets 5.83B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: HDFC Bank Ltd 6.4%, ICICI Bank Ltd 5.6%, Reliance Industries Ltd 5.4%, Bharti Airtel Ltd 3.9%, Infosys Ltd 2.4%
Sector mix: Financial services 29.7%, Consumer cyclical 12.3%, Industrials 10.2%, Basic materials 8.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.7% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.4% (25.16M) over 7d
Shares outstanding: 125.64M | fund size: 6.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals not decisive, flat fund flows, analyst view bullish but limited coverage.

**Main reasons it gave:**
- Analyst coverage of top holdings is 100% buy with a +28.8% price target, covering 53.9% of the fund
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs and RSI 31.6 (oversold) with low volume, no decisive break
- Fund flows are flat, share count up only 0.4% over the week
- Macro data shows modest yield declines and no surprise in inflation or unemployment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 204.62 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 208.76 (-2.0%), 50d 223.96 (-8.6%), 200d 230.06 (-11.1%); 50d below 200d
Momentum: RSI(14) 31.6 | MACD -5.018 vs signal -5.542 (histogram 0.524)
Returns: 1d +0.2% | 5d -0.1% | 1m -4.9% | 3m -11.3%
52-week range: 198.23 - 253.22 (now 11.6% of the way up)
Volatility: ATR(14) 3.48 (1.7% of price) | annualised 20d 14.2%
Volume: 0.27x the 20-day average
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
Three-year record: +24.2% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.8% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-10-15 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-10-12 Bernstein: main, Outperform -> Outperform
  - HWM: 2026-10-09 TD Cowen: main, Buy -> Buy
  - LMT: 2026-10-14 Bernstein: main, Market Perform -> Market Perform
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
Direction: flat (1 week)
Share count change: 1 week: +0.4% (43.31M) over 7d
Shares outstanding: 58.88M | fund size: 12.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall call; analyst view is bullish but offset by flat fund flows, mixed technicals, and unchanged macro environment.

**Main reasons it gave:**
- Analyst view: 100% buy rating, price target +27.4% above current
- Fund flows flat (share count unchanged over 1 week)
- Technical: price below 50‑day and 200‑day SMA, RSI 45.5, MACD histogram positive
- Macro: yields down slightly, no policy surprise, VIX up modestly

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.04 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 79.63 (+0.5%), 50d 82.87 (-3.4%), 200d 81.47 (-1.8%); 50d above 200d
Momentum: RSI(14) 45.5 | MACD -0.753 vs signal -1.030 (histogram 0.277)
Returns: 1d +0.7% | 5d +0.1% | 1m -0.1% | 3m -10.3%
52-week range: 68.14 - 90.01 (now 54.4% of the way up)
Volatility: ATR(14) 1.06 (1.3% of price) | annualised 20d 11.7%
Volume: 0.09x the 20-day average
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
Three-year record: +13.0% a year | beta to the market 1.32
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.4% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-07 Citigroup: main, Buy -> Buy
  - UBER: 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - CSX: 2026-10-07 Citigroup: main, Neutral -> Neutral
  - DAL: 2026-10-12 UBS: main, Buy -> Buy
  - UAL: 2026-10-07 Susquehanna: main, Positive -> Positive
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 2.80M | fund size: 224.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical breakout, and only modest positive signals (inflows, low valuations, thin analyst coverage) that do not justify a directional tilt.

**Main reasons it gave:**
- Fund flows: +1.3% share count increase over 1 week (moderate inflow)
- Analyst coverage thin (5.7% of fund) with modest bullish rating (+13.3% price target)
- Fundamentals: low P/E 12.0 and P/B 1.21 indicate relative cheapness
- Technicals: price below 20‑day SMA, RSI 42.4, low volume, no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

- [Bank of America shares slip over 5% as $1.2 billion fine hits Q3 profits](https://invezz.com/nz/news/2026/10/14/bank-of-america-shares-slip-over-5percent-as-dollar12-billion-fine-hits-q3-profits/)  
  <sub>Invezz, 20 hours ago</sub>  
  Bank of America shares fall over 5% in premarket trading after missing Wall Street earnings estimates. Regulatory penalty of $1.3 billion contributed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 69.65 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 70.21 (-0.8%), 50d 73.07 (-4.7%), 200d 70.71 (-1.5%); 50d above 200d
Momentum: RSI(14) 42.4 | MACD -1.123 vs signal -1.174 (histogram 0.051)
Returns: 1d +1.6% | 5d +0.1% | 1m -4.2% | 3m -9.2%
52-week range: 58.14 - 77.93 (now 58.2% of the way up)
Volatility: ATR(14) 1.25 (1.8% of price) | annualised 20d 15.8%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +22.8% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
Sector mix: Financial services 100.0%
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
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.3% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-09 RBC Capital: main, Sector Perform -> Sector Perform
  - HWC: 2026-10-05 Barclays: main, Overweight -> Overweight
  - EWBC: 2026-10-14 Cantor Fitzgerald: main, Overweight -> Overweight
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.3% (46.74M) over 7d
Shares outstanding: 53.66M | fund size: 3.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, bearish technicals, modest bullish fundamentals and slight inflow.

**Main reasons it gave:**
- Technical: price below 20d, 50d, 200d SMAs; RSI 41.1
- Analyst view: 100% buy rating on top holdings, +57.7% price target
- Fund flows: share count up 0.5% over the week (flat direction)
- Fund basics: low valuation (P/E 11.39) and 2.1% dividend yield
- Macro: no policy or data surprise; yields modestly down, VIX up modestly

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 51.56 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 52.37 (-1.6%), 50d 53.71 (-4.0%), 200d 56.42 (-8.6%); 50d below 200d
Momentum: RSI(14) 41.1 | MACD -0.528 vs signal -0.544 (histogram 0.016)
Returns: 1d +0.2% | 5d +0.4% | 1m -1.4% | 3m -2.6%
52-week range: 50.48 - 65.59 (now 7.1% of the way up)
Volatility: ATR(14) 0.64 (1.2% of price) | annualised 20d 18.3%
Volume: 0.79x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.39 | P/B 1.33 | P/S 1.31 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +9.2% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 5.99B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.8%, Alibaba Group Holding Ltd Ordinary Shares 9.3%, China Construction Bank Corp Class H 4.3%, Industrial And Commercial Bank Of China Ltd Class H 2.6%, Xiaomi Corp Class B 2.2%
Sector mix: Consumer cyclical 22.5%, Financial services 21.0%, Communication services 18.1%, Technology 11.6%
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
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +57.7% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Direction: flat (1 week)
Share count change: 1 week: +0.5% (29.18M) over 7d
Shares outstanding: 114.67M | fund size: 5.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, mixed technicals, and high valuations offset strong analyst bullishness.

**Main reasons it gave:**
- No macro surprise: Treasury yields modestly down, inflation 3.7% near target, no policy shift
- Fund flows flat: share count unchanged, indicating no net demand
- Technical indicators mixed: price below 20‑day and 50‑day SMAs, RSI 34.3, MACD below signal, but above 200‑day SMA
- Analyst consensus strongly bullish (100% buy, +47% price target) but lacking macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 550.92 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 602.31 (-8.5%), 50d 579.51 (-4.9%), 200d 510.42 (+7.9%); 50d above 200d
Momentum: RSI(14) 34.3 | MACD 0.433 vs signal 8.429 (histogram -7.996)
Returns: 1d -2.4% | 5d -9.3% | 1m +1.0% | 3m -1.0%
52-week range: 325.10 - 668.91 (now 65.7% of the way up)
Volatility: ATR(14) 16.29 (3.0% of price) | annualised 20d 30.9%
Volume: 0.90x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 32.50 | P/B 11.65 | P/S 13.32 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +59.0% a year | beta to the market 2.00
Cost and size: expense ratio 0.35% | net assets 74.88B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 19.3%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.3%, Advanced Micro Devices Inc 5.5%, Broadcom Inc 5.3%, Micron Technology Inc 4.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +47.1% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-10-15 Needham: main, Buy -> Buy
  - AMD: 2026-10-06 Citigroup: main, Buy -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-13 Rosenblatt: main, Buy -> Buy
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 11.67M | fund size: 6.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong bullish analyst view (+25.8% price target) offset by bearish technicals (price below 20‑, 50‑, 200‑day SMAs; RSI 31.4) and neutral fund flows; macro backdrop shows elevated VIX and rising yields, suggesting no clear directional catalyst.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +25.8% price target (covers 43.2% of fund)
- Technical indicators: price below 20‑, 50‑, 200‑day SMAs; RSI 31.4 (oversold)
- Fund flows: flat share count change (0.0% over 7 days)
- Macro: upward‑sloping yield curve; VIX elevated at 17.44

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 33.48 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 35.08 (-4.6%), 50d 37.81 (-11.4%), 200d 39.28 (-14.8%); 50d below 200d
Momentum: RSI(14) 31.4 | MACD -1.265 vs signal -1.267 (histogram 0.002)
Returns: 1d -0.5% | 5d -1.3% | 1m -7.5% | 3m -14.0%
52-week range: 31.90 - 43.74 (now 13.3% of the way up)
Volatility: ATR(14) 0.60 (1.8% of price) | annualised 20d 20.9%
Volume: 0.20x the 20-day average
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
Three-year record: -0.9% a year | beta to the market 0.61
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.8% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 15.65M | fund size: 523.96M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view and fund flows, strong fundamentals, but technicals show price below short‑term averages and modest bearish momentum; macro environment is neutral with no surprise data.

**Main reasons it gave:**
- Analyst view: 61.1% buy, weighted price target +7.6% above current price
- Fund flows: share count +3.1% week, indicating net inflows
- Technicals: price 2.5% below 20‑day SMA, RSI 43.1, MACD negative, volume 0.42× 20‑day avg
- Macro: 10‑year yield down 0.17% week, VIX up to 17.44 (elevated volatility)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 150.00 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 153.92 (-2.5%), 50d 158.17 (-5.2%), 200d 140.05 (+7.1%); 50d above 200d
Momentum: RSI(14) 43.1 | MACD -2.581 vs signal -2.028 (histogram -0.553)
Returns: 1d +2.2% | 5d +0.5% | 1m -2.7% | 3m -2.8%
52-week range: 107.32 - 169.55 (now 68.6% of the way up)
Volatility: ATR(14) 4.22 (2.8% of price) | annualised 20d 30.0%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +28.5% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.40</summary>

_Not available today._

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

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -7.6% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-15 Goldman Sachs: main, Neutral -> Neutral
  - NTRA: 2026-10-14 JP Morgan: main, Overweight -> Overweight
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-13 Guggenheim: main, Neutral -> Neutral
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.1% (307.93M) over 7d
Shares outstanding: 68.40M | fund size: 10.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest positive analyst and flow signals are offset by weak technicals and no macro surprise.

**Main reasons it gave:**
- Fund flows positive: share count +2.4% over 7 days
- Analyst coverage thin (17% weight) but all buy with +18.4% price target
- Technical indicators below 20d, 50d, 200d SMAs; RSI 43.9, MACD slightly negative
- Macro data: yields down modestly, VIX up, no major surprise in inflation or unemployment

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 95.35 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 96.23 (-0.9%), 50d 100.95 (-5.5%), 200d 105.70 (-9.8%); 50d below 200d
Momentum: RSI(14) 43.9 | MACD -1.721 vs signal -1.791 (histogram 0.070)
Returns: 1d +2.7% | 5d -0.3% | 1m -1.5% | 3m -11.9%
52-week range: 92.84 - 121.36 (now 8.8% of the way up)
Volatility: ATR(14) 2.19 (2.3% of price) | annualised 20d 22.8%
Volume: 0.83x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 18.56 | P/B 2.09 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +9.4% a year | beta to the market 1.48
Cost and size: expense ratio 0.35% | net assets 1.43B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SharkNinja Inc 3.5%, Cavco Industries Inc 3.4%, Champion Homes Inc 3.4%, Johnson Controls International PLC Registered Shares 3.4%, Wayfair Inc Class A 3.4%
Sector mix: Consumer cyclical 63.4%, Industrials 31.7%, Basic materials 3.2%, Real estate 1.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-08-07 TD Cowen: main, Buy -> Buy
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-09-30 Oppenheimer: init, ? -> Perform
  - JCI: 2026-10-15 Mizuho: main, Neutral -> Neutral
  - W: 2026-10-08 Baird: main, Neutral -> Neutral
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
Direction: money coming in (1 week)
Share count change: 1 week: +2.4% (33.76M) over 7d
Shares outstanding: 15.21M | fund size: 1.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, mixed technicals, flat fund flows, and limited analyst coverage.

**Main reasons it gave:**
- Analyst view: 100% buy rating covering 34.1% of fund, price target +13.6% above current
- Fund flows: flat share count change (0% over 1 week)
- Technicals: price below 50‑day SMA, MACD above signal, low volume
- Macro: modest yield declines, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 50.47 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 49.54 (+1.9%), 50d 51.19 (-1.4%), 200d 50.84 (-0.7%); 50d above 200d
Momentum: RSI(14) 54.4 | MACD -0.349 vs signal -0.547 (histogram 0.198)
Returns: 1d +1.6% | 5d +2.4% | 1m +0.2% | 3m -0.1%
52-week range: 42.23 - 53.67 (now 72.0% of the way up)
Volatility: ATR(14) 0.71 (1.4% of price) | annualised 20d 14.8%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Natural Resources
What it holds: P/E 22.69 | P/B 2.70 | P/S 1.78 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +10.7% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 7.78B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Linde PLC 12.2%, Newmont Corp 6.8%, Freeport-McMoRan Inc 5.6%, Ecolab Inc 4.7%, Sherwin-Williams Co 4.7%
Sector mix: Basic materials 83.2%, Consumer cyclical 16.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 34.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.6% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-13 Barclays: init, ? -> Overweight
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - FCX: 2026-10-08 UBS: main, Buy -> Buy
  - ECL: 2026-10-05 UBS: main, Buy -> Buy
  - SHW: 2026-10-13 Barclays: init, ? -> Equal-Weight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 71.92M | fund size: 3.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage and technicals versus bearish price outlook and inventory trends; flat fund flows indicate no net demand shift.

**Main reasons it gave:**
- EIA price outlook: WTI to fall 14% over six months
- Energy inventories: crude draw, gas build (net bearish)
- Analyst coverage: 100% buy rating on top holdings
- Technicals: price above 20d/50d/200d SMAs, RSI 64, MACD positive

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Energy Select Sector SPDR (XLE) Adds XOM and CVX on Oct. 13](https://finance.yahoo.com/energy/articles/state-street-energy-select-sector-110527039.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Energy Select Sector SPDR ETF (XLE) recorded a net $124.2 million in ETF activity on Tuesday,...
- [Energy’s 50% sprint ranks among the fastest since 1990 (XLE:NYSEARCA)](https://seekingalpha.com/news/4653264-energys-50-sprint-ranks-among-the-fastest-since-1990)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  The energy sector reached a 50% gain this year in 196 trading days through Wednesday, marking the fifth-fastest rally to that threshold among all sectors...
- [New State Street Sector ETFs Give Biggest Stocks Full Weight](https://etfdb.com/sector-investing-content-hub/new-state-street-market-sector-spdr-etfs/)  
  <sub>ETF Database, 18 hours ago</sub>  
  State Street's four Market Sector SPDR ETFs give the biggest tech, energy and consumer stocks more weight than its Select Sector funds do.
- [GS Finance Corp. Launches Auto-Callable Jump Securities Linked to XLE, XLU, XLV ETFs Maturing in 2032](https://kalkinemedia.com/us/news/announcements/gs-finance-corp-launches-auto-callable-jump-securities-linked-to-xle-xlu-xlv-etfs-maturing-in-2032)  
  <sub>Kalkine Media, 5 hours ago</sub>  
  The filing states these securities are unsecured notes issued under GS Finance Corp.'s Medium-Term Notes, Series F program, fully and unconditionally...
- [Sector Update: Energy Stocks Advance Pre-Bell Thursday](https://ca.finance.yahoo.com/news/sector-energy-stocks-advance-pre-132137510.html)  
  <sub>Yahoo! Finance Canada, 1 hour ago</sub>  
  Energy stocks were advancing pre-bell Thursday, with the State Street Energy Select Sector SPDR ETF (XLE) 0.2% higher. The United States Oil Fund (USO) was...
- [Exchange-Traded Funds Lower as US Equities Drop After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-lower-us-170825191.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 1.7%.
- [Energy Stocks Aren't Running Out Of Gas](https://www.investors.com/etfs-and-funds/etfs/energy-stocks-arent-running-out-of-gas/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Investors keep waiting for the S&P 500 energy stock rally to sputter. But it's only picking up more power.
- [State Street Investment Management Launches Four New S&P 500 Market Sector ETFs](https://pulse2.com/state-street-investment-management-launches-four-new-sp-500-market-sector-etfs/)  
  <sub>Pulse 2.0, 18 hours ago</sub>  
  State Street Investment Management has launched four new State Street S&P 500 Market Sector SPDR ETFs, expanding the sector ETF franchise the firm pioneered...
- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Thursday Amid Economic Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131605386.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Sector Update: Energy Stocks Rise Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-rise-afternoon-200334873.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks were higher late Wednesday afternoon, with the NYSE Energy Sector Index rising 0.3% and the State Street Energy Select Sector SPDR ETF (XLE)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.50</summary>

```text
Last close 66.68 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 63.73 (+4.6%), 50d 63.34 (+5.3%), 200d 57.50 (+16.0%); 50d above 200d
Momentum: RSI(14) 64.1 | MACD 1.009 vs signal 0.568 (histogram 0.441)
Returns: 1d -1.4% | 5d +2.2% | 1m +4.1% | 3m +15.6%
52-week range: 42.64 - 67.63 (now 96.2% of the way up)
Volatility: ATR(14) 1.26 (1.9% of price) | annualised 20d 21.1%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.60</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.51 | P/B 2.47 | P/S 1.70 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +18.1% a year | beta to the market -0.03
Cost and size: expense ratio 0.08% | net assets 39.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.0%, Chevron Corp 18.1%, ConocoPhillips 6.7%, Valero Energy Corp 4.7%, Marathon Petroleum Corp 4.7%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.60</summary>

```text
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +0.0% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - CVX: 2026-10-12 TD Cowen: main, Hold -> Hold
  - COP: 2026-10-07 Jefferies: main, Buy -> Buy
  - VLO: 2026-10-14 Wells Fargo: main, Overweight -> Overweight
  - MPC: 2026-10-14 Wells Fargo: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 186.42M | fund size: 12.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack a decisive break, flows flat, and fundamentals unchanged despite bullish analyst coverage.

**Main reasons it gave:**
- No macro surprise: yields unchanged, no policy shift
- Technicals: price above 20‑day SMA, MACD above signal, but below 50‑day SMA and low volume
- Fund flows flat: 0% share count change over the week
- Analyst view: 100% buy on top holdings with +9.4% price target
- Mixed news: banks report strong loan growth but sector index fell and Bank of America stock down

<details><summary><b>News</b> — score +0.00</summary>

- [Financial Select Sector SPDR (XLF) Sells Berkshire and JPMorgan on Oct. 13](https://finance.yahoo.com/markets/stocks/articles/financial-select-sector-spdr-xlf-110428095.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. In a one-sided ETF activity on Tuesday, Oct. 13, State Street Financial Select Sector SPDR ETF (XLF) was the only...
- [Cboe to expand options trading hours for major stocks and ETFs](https://www.cnbc.com/amp/2026/10/15/cboe-stock-etf-options-extended-hours.html)  
  <sub>CNBC, 3 hours ago</sub>  
  Cboe will offer trading on 24 of the most actively traded companies and five ETFs between 7:30 a.m. and 9:25 a.m. ET and 4:00 p.m. to 4:15 p.m. ET.
- [Banks Want To Lend: The New Constraint Of This Earnings Season (NYSEARCA:XLF)](https://seekingalpha.com/article/4954424-banks-want-to-lend-the-new-constraint-of-this-earnings-season)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Major US banks like JPMorgan, Bank of America, and Wells Fargo report strong credit quality and robust double-digit business loan growth despite high rates.
- [$100B Anthropic IPO Could Boost Wall Street Banks: ETFs to Watch - State Street Financial Select Sector S](https://www.benzinga.com/etfs/sector-etfs/26/10/62370149/potential-100-billion-anthropic-ipo-could-boost-wall-street-banks-which-etfs-stand-to-benefit)  
  <sub>Benzinga, 18 hours ago</sub>  
  A $100 billion Anthropic IPO could generate $700 million in bank fees. Find out which financial ETFs could benefit from a Wall Street IPO revival.
- [Webcast: Beyond Cash: Unlocking More Potential Income with Short Duration Bonds | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/17/beyond-cash-unlocking-more-income-potential-with-short-duration-bonds?topic=real-estate)  
  <sub>Advisor Perspectives, 19 hours ago</sub>  
  Short duration bond strategies may offer opportunities for investors seeking income while managing interest rate sensitivity. Join Peter Brown, CFA®,...
- [QUICK SPARK: Bank of America Stock Eyes Worst Day Since Trump’s Tariffs Shock](https://www.tradingview.com/news/benzinga:4fb1159b4094b:0-quick-spark-bank-of-america-stock-eyes-worst-day-since-trump-s-tariffs-shock/)  
  <sub>TradingView, 24 hours ago</sub>  
  Bank of America Corp. NYSE:BAC stock is heading for its worst day since the April 2025 tariff selloff.Shares fell 7.5% to $49.93 by Wednesday midday,...
- [Sector Update: Financial](https://finance.yahoo.com/markets/stocks/articles/sector-financial-192948554.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Financial stocks were lower in late Wednesday afternoon trading, with the NYSE Financial Index falli.
- [Berkshire Stock Notches 10 Straight Gains, First Since 2018 - State Street Financial Select Sector SPDR E](https://www.benzinga.com/markets/equities/26/10/62366355/berkshire-hathaway-stock-10-day-winning-streak)  
  <sub>Benzinga, 20 hours ago</sub>  
  Berkshire Hathaway has risen 10 sessions in a row, its first such streak since January 2018 and the first under CEO Greg Abel.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 54.85 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 54.44 (+0.7%), 50d 56.31 (-2.6%), 200d 53.68 (+2.2%); 50d above 200d
Momentum: RSI(14) 47.7 | MACD -0.445 vs signal -0.639 (histogram 0.194)
Returns: 1d +0.6% | 5d +1.1% | 1m -1.9% | 3m -2.5%
52-week range: 47.81 - 58.56 (now 65.4% of the way up)
Volatility: ATR(14) 0.68 (1.2% of price) | annualised 20d 11.9%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Financial
What it holds: P/E 15.21 | P/B 2.25 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +20.0% a year | beta to the market 0.75
Cost and size: expense ratio 0.08% | net assets 50.97B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.3%, JPMorgan Chase & Co 11.7%, Visa Inc Class A 8.1%, Mastercard Inc Class A 5.9%, Bank of America Corp 4.7%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.2%
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
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.4% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - JPM: 2026-10-14 Truist Securities: main, Hold -> Hold
  - V: 2026-10-12 Baird: main, Outperform -> Outperform
  - MA: 2026-10-09 Baird: main, Outperform -> Outperform
  - BAC: 2026-10-15 Barclays: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 883.44M | fund size: 48.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed fundamentals, weak technicals

**Main reasons it gave:**
- Analyst coverage 25.7% of fund, all buy with +26% price target
- Fund flows flat, no net creations or redemptions
- Fund fundamentals show high valuations (P/E 27.43, P/B 6.56) and low yield 1.1%
- Technical indicators below SMAs, low volume, RSI 36.5 indicating slight oversold

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 166.27 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 169.06 (-1.6%), 50d 174.42 (-4.7%), 200d 172.91 (-3.8%); 50d above 200d
Momentum: RSI(14) 36.5 | MACD -1.601 vs signal -1.696 (histogram 0.095)
Returns: 1d -0.5% | 5d -1.3% | 1m -1.4% | 3m -7.3%
52-week range: 147.83 - 186.51 (now 47.7% of the way up)
Volatility: ATR(14) 2.40 (1.4% of price) | annualised 20d 13.1%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 27.43 | P/B 6.56 | P/S 2.92 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +20.0% a year | beta to the market 1.01
Cost and size: expense ratio 0.08% | net assets 29.83B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Caterpillar Inc 7.0%, GE Aerospace 6.1%, GE Vernova Inc 4.8%, RTX Corp 4.7%, Deere & Co 3.2%
Sector mix: Industrials 93.4%, Technology 6.1%, Basic materials 0.3%, Consumer cyclical 0.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.0% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-12 Citigroup: main, Buy -> Buy
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - GEV: 2026-10-14 Susquehanna: main, Positive -> Positive
  - RTX: 2026-10-15 Bernstein: main, Market Perform -> Market Perform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 136.63M | fund size: 22.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst bullishness (+24% price target) is offset by short‑term technical weakness, flat fund flows, high valuation and elevated macro risk.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +24% price target
- Technicals: price below 20‑day SMA, negative MACD, RSI 38.6
- Fund flows flat (0% change), indicating no net demand
- Macro: yields modestly higher, VIX elevated at 17.44, indicating higher risk

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 187.46 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 196.04 (-4.4%), 50d 189.94 (-1.3%), 200d 167.31 (+12.0%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD 1.262 vs signal 2.678 (histogram -1.416)
Returns: 1d -1.6% | 5d -5.2% | 1m +1.9% | 3m +6.8%
52-week range: 127.50 - 202.00 (now 80.5% of the way up)
Volatility: ATR(14) 3.41 (1.8% of price) | annualised 20d 20.0%
Volume: 0.93x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Technology
What it holds: P/E 32.04 | P/B 11.88 | P/S 9.26 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +33.4% a year | beta to the market 1.45
Cost and size: expense ratio 0.08% | net assets 127.30B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 15.5%, Apple Inc 13.6%, Microsoft Corp 10.7%, Advanced Micro Devices Inc 5.1%, Broadcom Inc 4.7%
Sector mix: Technology 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.0% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - MSFT: 2026-10-15 TD Cowen: main, Buy -> Buy
  - AMD: 2026-10-06 Citigroup: main, Buy -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 272.06M | fund size: 51.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro unchanged, technicals bullish but with overbought RSI and low volume, flat fund flows, and moderate fundamentals. Analyst view is bullish but not enough to outweigh neutral macro and flow signals.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 41.8% of fund, weighted price target +4.3% above current
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs; RSI 71.5 (overbought); volume 0.77× 20‑day average
- Fund flows: share count unchanged (+0.0% over 7 days), indicating neutral demand
- Macro: 10‑year yield down 0.17% on week, VIX up 2.0 points to 17.44 (elevated but stable)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.55 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 82.64 (+5.9%), 50d 84.06 (+4.2%), 200d 83.96 (+4.3%); 50d above 200d
Momentum: RSI(14) 71.5 | MACD 0.462 vs signal -0.255 (histogram 0.717)
Returns: 1d +1.7% | 5d +5.0% | 1m +5.1% | 3m +2.8%
52-week range: 75.60 - 90.01 (now 82.9% of the way up)
Volatility: ATR(14) 1.15 (1.3% of price) | annualised 20d 16.6%
Volume: 0.77x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 23.91 | P/B 4.44 | P/S 1.29 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +11.0% a year | beta to the market 0.48
Cost and size: expense ratio 0.08% | net assets 13.45B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 10.5%, Costco Wholesale Corp 9.2%, Procter & Gamble Co 7.7%, Coca-Cola Co 7.6%, Philip Morris International Inc 6.8%
Sector mix: Consumer defensive 98.5%, Consumer cyclical 1.5%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.3% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-15 Deutsche Bank: up, Hold -> Buy
  - COST: 2026-10-09 RBC Capital: reit, Sector Perform -> Sector Perform
  - PG: 2026-10-14 Citigroup: main, Buy -> Buy
  - KO: 2026-10-14 Citigroup: main, Buy -> Buy
  - PM: 2026-09-23 UBS: main, Neutral -> Neutral
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 210.17M | fund size: 18.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, flat fund flows, and solid but unchanged fundamentals.

**Main reasons it gave:**
- Flat fund flows (0.0% share count change) indicating neutral demand
- Technical indicators mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA, low volume
- Macro environment unchanged: modest yield declines, no policy surprise, VIX at 17.44
- Analyst consensus bullish (80.6% buy, +16.8% price target) but not enough to outweigh neutral macro/technical
- Fund fundamentals stable (P/E 17.86, yield 3.1%, low beta) with no new catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.63 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 40.52 (+2.7%), 50d 42.04 (-1.0%), 200d 44.31 (-6.0%); 50d below 200d
Momentum: RSI(14) 54.8 | MACD -0.079 vs signal -0.391 (histogram 0.312)
Returns: 1d -0.2% | 5d +1.4% | 1m +0.8% | 3m -7.8%
52-week range: 39.25 - 47.73 (now 28.1% of the way up)
Volatility: ATR(14) 0.64 (1.5% of price) | annualised 20d 16.8%
Volume: 0.41x the 20-day average
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
Three-year record: +15.6% a year | beta to the market 0.40
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.8% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-14 Morgan Stanley: main, Overweight -> Overweight
  - SO: 2026-10-13 JP Morgan: main, Neutral -> Neutral
  - DUK: 2026-10-13 JP Morgan: main, Neutral -> Neutral
  - CEG: 2026-10-06 Bernstein: reit, Outperform -> Outperform
  - AEP: 2026-10-13 Keybanc: up, Sector Weight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 163.27M | fund size: 6.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data HTTP 500: {"status_code":500,"error":"Proxy request failed","error_code":"unknown_proxy_error","details":"connect ECONNREFUSED 68.183.147.31:44445"}

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bullish but low volume, analyst view bullish but limited coverage, flows flat, fundamentals mixed.

**Main reasons it gave:**
- Analyst coverage: 44.3% of fund weighted, 100% buy rating, price target +6.1% above current
- Fund flows: flat share count change (+0.0% over 1 week)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 68.6, but volume only 0.53× 20‑day average
- Sector momentum: defensive sectors leading, healthcare up late afternoon
- Macro: no policy or data surprise, yields modestly down, VIX 17.44 (moderate volatility)

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo Finance UK, 13 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 3.05% · 3.70% · 16.89% · 12.38% · 22.21% · 36.61% · 601.10%. Key events. Baseline. Advanced chart.
- [New Earnings Show the Healthcare Sector Has a Pulse](https://www.etftrends.com/sector-investing-content-hub/new-earnings-show-healthcare-sector-pulse/)  
  <sub>ETF Trends, 3 hours ago</sub>  
  The new earnings reports from UnitedHealth Group and Johnson & Johnson prove why the health care sector warrants targeted exposure.
- [State Street Health Care SPDR (XLV) Sells Medtronic and Eli Lilly on Oct. 13](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110541059.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. ETF activity on Tuesday showed State Street Health Care Select Sector SPDR ETF (XLV) as the sole seller among the...
- [GS Finance Corp. Launches Auto-Callable Jump Securities Linked to XLE, XLU, XLV ETFs Maturing in 2032](https://kalkinemedia.com/us/news/announcements/gs-finance-corp-launches-auto-callable-jump-securities-linked-to-xle-xlu-xlv-etfs-maturing-in-2032)  
  <sub>Kalkine Media, 5 hours ago</sub>  
  The filing states these securities are unsecured notes issued under GS Finance Corp.'s Medium-Term Notes, Series F program, fully and unconditionally...
- [8 Of 11 Sectors Fall Wednesday As Defensives Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62359155/8-of-11-sectors-fall-wednesday-as-defensives-lead?utm_source=googlefinance)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Wednesday's regular session, with defensive sectors holding the top three positions.
- [Goldman Sachs USD Investment Grade Corporate Bond Active UCITS ETF Class USD (Dist) (GIGU.DE) risk](https://uk.finance.yahoo.com/quote/GIGU.DE/risk/)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  View historical risk statistics for Goldman Sachs USD Investment Grade Corporate Bond Active UCITS ETF Class USD (Dist) (GIGU.DE).
- [Stocktwits Pharma Pulse: JNJ Earnings, Cancer Updates And Two FDA Target Dates — The Week’s Biotech Watchlist](https://stocktwits.com/news-articles/markets/equity/stocktwits-pharma-pulse-jnj-earnings-cancer-updates-fda-target-dates-week-biotech-watchlist/cZx4H9CRBFa)  
  <sub>Stocktwits, 7 hours ago</sub>  
  JNJ reports third-quarter results on Tuesday, and Koyfin analysts expect modest revenue growth and lower earnings.
- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Thursday Amid Economic Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131605386.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Sector Update: Healthcare Stocks Gain Late Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-gain-afternoon-195615429.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Healthcare stocks were higher late Wednesday afternoon, with the NYSE Healthcare Index and the State Street Health Care Select Sector SPDR ETF (XLV) each...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 178.00 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 169.76 (+4.9%), 50d 169.77 (+4.8%), 200d 157.41 (+13.1%); 50d above 200d
Momentum: RSI(14) 68.6 | MACD 1.223 vs signal 0.387 (histogram 0.836)
Returns: 1d +2.3% | 5d +5.9% | 1m +6.1% | 3m +10.5%
52-week range: 142.32 - 178.00 (now 100.0% of the way up)
Volatility: ATR(14) 2.86 (1.6% of price) | annualised 20d 17.2%
Volume: 0.53x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +11.1% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
Sector mix: Healthcare 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.1% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - JNJ: 2026-10-14 Leerink Partners: main, Outperform -> Outperform
  - ABBV: 2026-10-13 RBC Capital: reit, Outperform -> Outperform
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-15 TD Cowen: reit, Hold -> Hold
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 197.42M | fund size: 35.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view is strongly bullish but covers only ~54% of the fund; fund flows are flat; technicals show mixed signals with price above short‑term SMA but below longer‑term SMAs and low volume; macro data show modest yield declines and higher volatility but no surprise events; fundamentals are solid but not a catalyst.

**Main reasons it gave:**
- Analyst view: 100% buy on top holdings (54.4% weight) with +22% price target
- Fund flows: flat share count (+0.0% change) over past week
- Technical: price above 20‑day SMA (+1.6%) but below 50‑day (-1.1%) and 200‑day (-2.7%) SMAs, low volume (0.30x avg)
- Macro: yields down modestly, VIX up to 17.44, no surprise data releases
- Fundamentals: P/E 24, yield 0.9%, three‑year return +13.2%/yr, beta 1.18

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 112.76 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 111.00 (+1.6%), 50d 113.97 (-1.1%), 200d 115.93 (-2.7%); 50d below 200d
Momentum: RSI(14) 53.8 | MACD -0.267 vs signal -0.711 (histogram 0.444)
Returns: 1d +1.1% | 5d +0.9% | 1m +2.3% | 3m -2.3%
52-week range: 105.66 - 124.52 (now 37.6% of the way up)
Volatility: ATR(14) 1.37 (1.2% of price) | annualised 20d 12.5%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.00 | P/B 5.56 | P/S 2.32 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +13.2% a year | beta to the market 1.18
Cost and size: expense ratio 0.08% | net assets 21.27B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 23.4%, Tesla Inc 17.7%, The Home Depot Inc 5.0%, McDonald's Corp 4.2%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.7%, Technology 1.3%
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
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.0% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-12 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-10-15 GLJ Research: reit, Sell -> Sell
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-10-08 Bernstein: main, Market Perform -> Market Perform
  - TJX: 2026-08-26 Jefferies: down, Buy -> Hold
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 120.25M | fund size: 13.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Argentina (ARGT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 87.10 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 88.52 (-1.6%), 50d 91.75 (-5.1%), 200d 92.45 (-5.8%); 50d below 200d
Momentum: RSI(14) 40.3 | MACD -1.337 vs signal -1.471 (histogram 0.134)
Returns: 1d +0.1% | 5d -1.3% | 1m -6.7% | 3m -5.4%
52-week range: 70.49 - 102.94 (now 51.2% of the way up)
Volatility: ATR(14) 1.74 (2.0% of price) | annualised 20d 28.8%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.92 | P/B 1.57 | P/S 1.21 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +31.5% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 718.85M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 21.7%, YPF SA ADR 10.4%, Vista Energy SAB de CV ADR 7.0%, Grupo Financiero Galicia SA ADR 5.7%, Pampa Energia SA ADR 4.7%
Sector mix: Consumer cyclical 27.8%, Energy 21.2%, Financial services 14.2%, Basic materials 11.8%
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
Rolled up from the 5 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.6% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-13 Citigroup: main, Neutral -> Neutral
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-09-01 JP Morgan: main, Neutral -> Neutral
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
Direction: flat (1 week)
Share count change: 1 week: +0.4% (2.90M) over 7d
Shares outstanding: 8.06M | fund size: 702.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Israel (EIS) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 118.95 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 121.31 (-1.9%), 50d 122.50 (-2.9%), 200d 122.95 (-3.3%); 50d below 200d
Momentum: RSI(14) 43.2 | MACD -1.419 vs signal -1.104 (histogram -0.315)
Returns: 1d +0.8% | 5d +1.1% | 1m -3.5% | 3m -0.8%
52-week range: 97.88 - 137.69 (now 52.9% of the way up)
Volatility: ATR(14) 1.72 (1.4% of price) | annualised 20d 17.5%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +36.3% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.4% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - TSEM.TA: 2026-09-25 Mizuho: init, ? -> Outperform
  - ESLT.TA: 2026-10-05 Jefferies: main, Hold -> Hold
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 2.55M | fund size: 303.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 44.24 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 44.24 (+0.0%), 50d 44.38 (-0.3%), 200d 39.93 (+10.8%); 50d above 200d
Momentum: RSI(14) 50.8 | MACD -0.087 vs signal -0.085 (histogram -0.002)
Returns: 1d +0.5% | 5d +1.8% | 1m +0.2% | 3m +9.6%
52-week range: 32.56 - 45.76 (now 88.5% of the way up)
Volatility: ATR(14) 0.63 (1.4% of price) | annualised 20d 21.7%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.22 | P/B 2.06 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +42.1% a year | beta to the market 0.64
Cost and size: expense ratio 0.59% | net assets 833.96M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: PKO Bank Polski SA 16.2%, Orlen SA 12.7%, Bank Polska Kasa Opieki SA 7.4%, Powszechny Zaklad Ubezpieczen SA 6.0%, Allegro.EU SA Ordinary Shares 4.9%
Sector mix: Financial services 46.9%, Energy 13.3%, Consumer cyclical 13.2%, Basic materials 6.2%
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
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.7% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
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
Direction: money going out (1 week)
Share count change: 1 week: -0.7% (-5.67M) over 7d
Shares outstanding: 19.01M | fund size: 841.17M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.78 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 46.82 (+2.0%), 50d 47.73 (+0.1%), 200d 46.81 (+2.1%); 50d above 200d
Momentum: RSI(14) 59.2 | MACD -0.214 vs signal -0.364 (histogram 0.150)
Returns: 1d +1.8% | 5d +3.3% | 1m +0.7% | 3m +1.8%
52-week range: 41.34 - 49.39 (now 79.9% of the way up)
Volatility: ATR(14) 0.49 (1.0% of price) | annualised 20d 13.4%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.50 | P/B 2.22 | P/S 1.46 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +18.4% a year | beta to the market 0.71
Cost and size: expense ratio 0.50% | net assets 3.67B
What it is made of: Stocks 98.6%, Other 1.1%, Cash 0.4%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 8.9%, AstraZeneca PLC 8.0%, Rolls-Royce Holdings PLC 5.2%, Unilever PLC 4.3%
Sector mix: Financial services 26.1%, Consumer defensive 14.1%, Industrials 13.3%, Healthcare 13.0%
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
Rolled up from the 5 largest holdings, 37.4% of the fund by weight
Ratings by weight: buy 59.1% | hold 40.9% | sell 0.0% (mean 2.16 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
Holdings read: HSBA.L, SHEL.L, AZN.L, RR.L, ULVR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 67.80M | fund size: 3.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 42.42 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 39.81 (+6.6%), 50d 37.56 (+12.9%), 200d 36.89 (+15.0%); 50d above 200d
Momentum: RSI(14) 66.7 | MACD 1.638 vs signal 1.373 (histogram 0.265)
Returns: 1d -0.4% | 5d -0.4% | 1m +13.2% | 3m +20.4%
52-week range: 29.24 - 43.54 (now 92.1% of the way up)
Volatility: ATR(14) 1.03 (2.4% of price) | annualised 20d 49.6%
Volume: 0.32x the 20-day average
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
Three-year record: +19.1% a year | beta to the market 0.83
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.2% above the current prices
Holdings read: VALE3.SA, ITUB4, NU, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-10-06 JP Morgan: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 200.55M | fund size: 8.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Saudi Arabia (KSA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 35.12 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 36.46 (-3.6%), 50d 37.53 (-6.4%), 200d 38.10 (-7.8%); 50d below 200d
Momentum: RSI(14) 26.2 | MACD -0.602 vs signal -0.491 (histogram -0.111)
Returns: 1d -0.1% | 5d -2.7% | 1m -5.7% | 3m -4.5%
52-week range: 35.12 - 41.03 (now 0.0% of the way up)
Volatility: ATR(14) 0.33 (0.9% of price) | annualised 20d 12.7%
Volume: 0.39x the 20-day average
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
Three-year record: +2.2% a year | beta to the market 0.19
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
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
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
Direction: money coming in (1 week)
Share count change: 1 week: +2.2% (12.39M) over 7d
Shares outstanding: 16.45M | fund size: 577.82M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US real estate (VNQ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.50 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 90.77 (+0.8%), 50d 94.40 (-3.1%), 200d 94.43 (-3.1%); 50d below 200d
Momentum: RSI(14) 48.1 | MACD -1.061 vs signal -1.445 (histogram 0.384)
Returns: 1d +1.3% | 5d +2.4% | 1m -2.1% | 3m -8.5%
52-week range: 87.00 - 100.95 (now 32.3% of the way up)
Volatility: ATR(14) 1.23 (1.3% of price) | annualised 20d 15.1%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +10.8% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.1%, Cash 0.7%, Other 0.2%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 8.7%, Prologis Inc 6.9%, Equinix Inc 5.5%, American Tower Corp 4.3%
Sector mix: Real estate 99.4%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.9% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-10-13 Barclays: main, Equal-Weight -> Equal-Weight
  - PLD: 2026-10-13 Scotiabank: up, Sector Perform -> Sector Outperform
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-09-30 Barclays: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 370.18M | fund size: 33.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields stable, no policy change
- Crowded long: net long 21.8% of OI, 100% percentile, weekly increase +1.9% OI
- Outflows: share count down 1.2% over 7 days
- Heavy cost of holding: -9.8% annual roll cost
- Technicals: price at 52‑week high, RSI 69.3, low volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 12.44 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 11.73 (+6.1%), 50d 11.41 (+9.1%), 200d 10.10 (+23.2%); 50d above 200d
Momentum: RSI(14) 69.3 | MACD 0.316 vs signal 0.259 (histogram 0.057)
Returns: 1d +0.9% | 5d +3.8% | 1m +9.2% | 3m +27.7%
52-week range: 9.02 - 12.44 (now 100.0% of the way up)
Volatility: ATR(14) 0.21 (1.7% of price) | annualised 20d 21.4%
Volume: 0.26x the 20-day average
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
Cost of holding this fund instead of sugar itself: -9.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +27.7%, commodity +42.3%, gap -14.6% | 6 months: fund +34.1%, commodity +54.5%, gap -20.5% | 12 months: fund +23.2%, commodity +32.9%, gap -9.8%
A commodity fund holds futures, not sugar, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 21.8% of open interest (1,158,944 contracts)
Change on the week: +1.9% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.2% (-630.06K) over 7d
Shares outstanding: 4.32M | fund size: 53.77M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed fundamentals (heavy cost of holding vs stable crop condition) lead to a neutral view.

**Main reasons it gave:**
- Macro: yields and inflation in line with expectations (no surprise)
- Technical: price below 20‑day SMA, RSI 33.8, low volume, no decisive break
- Cost of holding: -9.6% annual drag for long positions
- Crop condition: 56% good/excellent, steady over 3 weeks (slight decline in condition)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 18.40 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 19.17 (-4.0%), 50d 19.21 (-4.2%), 200d 18.17 (+1.2%); 50d above 200d
Momentum: RSI(14) 33.8 | MACD -0.278 vs signal -0.162 (histogram -0.117)
Returns: 1d -0.1% | 5d -3.0% | 1m -7.9% | 3m +3.5%
52-week range: 16.47 - 20.29 (now 50.5% of the way up)
Volatility: ATR(14) 0.30 (1.6% of price) | annualised 20d 20.3%
Volume: 0.12x the 20-day average
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
Cost of holding this fund instead of corn itself: -9.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +3.5%, commodity +7.9%, gap -4.4% | 6 months: fund +2.4%, commodity +7.0%, gap -4.6% | 12 months: fund +6.6%, commodity +16.2%, gap -9.6%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 41 of 2026)
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 17.7% of open interest (1,859,993 contracts)
Change on the week: -2.8% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.1% (2.69M) over 7d
Shares outstanding: 7.03M | fund size: 129.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals slightly bearish but no decisive break; positioning net long decreased; fund outflows; cost of holding negative drag.

**Main reasons it gave:**
- Positioning net long fell 5.8% week over week
- Fund flows: share count down 1.6% (outflows) over the week
- Technical indicators: price below 20‑day SMA, RSI 45.5, MACD histogram negative
- Cost of holding: -3.9% annual drag versus copper

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 39.41 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 40.11 (-1.7%), 50d 39.90 (-1.2%), 200d 37.72 (+4.5%); 50d above 200d
Momentum: RSI(14) 45.5 | MACD 0.022 vs signal 0.066 (histogram -0.043)
Returns: 1d -0.6% | 5d -0.1% | 1m +2.1% | 3m +3.9%
52-week range: 30.53 - 41.43 (now 81.5% of the way up)
Volatility: ATR(14) 0.59 (1.5% of price) | annualised 20d 19.5%
Volume: 1.13x the 20-day average
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

```text
Cost of holding this fund instead of copper itself: -3.9% a year -- a steady drag
Measured: 3 months: fund +3.9%, commodity +5.4%, gap -1.4% | 6 months: fund +6.7%, commodity +8.0%, gap -1.4% | 12 months: fund +27.7%, commodity +31.6%, gap -3.9%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 20.1% of open interest (304,033 contracts)
Change on the week: -5.8% of open interest
Crowding: 23% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.6% (-11.52M) over 7d
Shares outstanding: 17.60M | fund size: 693.59M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals bearish but no decisive break, positioning unchanged, flat fund flows, moderate negative cost of holding.

**Main reasons it gave:**
- Positioning unchanged: net long 7.2% of open interest, 0% weekly change
- Technical trend bearish (price below 20-day, 50-day, 200-day SMAs) with no decisive break
- Macro data stable: yields modestly down, no policy surprise
- Cost of holding -3.4% annual drag (moderate negative fundamental)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 51.57 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 55.56 (-7.2%), 50d 57.84 (-10.8%), 200d 65.49 (-21.3%); 50d below 200d
Momentum: RSI(14) 36.9 | MACD -1.608 vs signal -1.206 (histogram -0.402)
Returns: 1d +2.7% | 5d -3.5% | 1m -9.6% | 3m +1.6%
52-week range: 42.40 - 105.60 (now 14.5% of the way up)
Volatility: ATR(14) 1.61 (3.1% of price) | annualised 20d 39.4%
Volume: 0.51x the 20-day average
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

```text
Cost of holding this fund instead of silver itself: -3.4% a year -- a steady drag
Measured: 3 months: fund +1.6%, commodity +2.0%, gap -0.5% | 6 months: fund -27.6%, commodity -27.3%, gap -0.3% | 12 months: fund +10.2%, commodity +13.6%, gap -3.4%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 7.2% of open interest (105,130 contracts)
Change on the week: +0.0% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 341.45M | fund size: 17.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields slipped modestly, inflation 3.7% in line with expectations, no policy shift
- Technical indicators mixed: price above 200‑day SMA but below 20‑day SMA, RSI 44.7, MACD histogram negative
- Crowded long position: 23% net long, 92nd percentile, weekly increase only +0.4%
- Fund outflows: share count down 0.6% over the past week
- Crop condition deteriorating slightly (good/excellent down 1 point over 3 weeks) indicating tighter supply

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.13 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 27.55 (-1.5%), 50d 27.02 (+0.4%), 200d 24.86 (+9.1%); 50d above 200d
Momentum: RSI(14) 44.7 | MACD 0.015 vs signal 0.108 (histogram -0.093)
Returns: 1d -0.2% | 5d -0.9% | 1m -3.0% | 3m +6.4%
52-week range: 21.59 - 28.14 (now 84.6% of the way up)
Volatility: ATR(14) 0.31 (1.1% of price) | annualised 20d 12.5%
Volume: 0.07x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.7% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +6.4%, commodity +5.7%, gap +0.7% | 6 months: fund +11.1%, commodity +9.4%, gap +1.6% | 12 months: fund +25.8%, commodity +26.5%, gap -0.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 23.0% of open interest (1,121,298 contracts)
Change on the week: +0.4% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.6% (-269.23K) over 7d
Shares outstanding: 1.65M | fund size: 44.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish fundamentals (EIA price forecast down 14% in six months) offset by modest bullish inventory draw and slight bearish shift in speculator positioning; technicals remain bullish but on low volume and no macro surprise.

**Main reasons it gave:**
- EIA forecast WTI price $100 now, down to $86 in 6 months, indicating bearish outlook
- Crude oil inventories draw of 3.2 million barrels (week ending 2026-10-02) suggests bullish supply pressure
- CFTC large speculators net long decreased by 1.4% of open interest, indicating slight bearish shift
- Technical trend shows price above 20‑day, 50‑day, 200‑day SMAs with positive momentum but low volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 155.73 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 148.74 (+4.7%), 50d 141.79 (+9.8%), 200d 118.79 (+31.1%); 50d above 200d
Momentum: RSI(14) 61.4 | MACD 2.480 vs signal 2.198 (histogram 0.282)
Returns: 1d +1.4% | 5d +5.5% | 1m -0.3% | 3m +25.6%
52-week range: 66.17 - 161.86 (now 93.6% of the way up)
Volatility: ATR(14) 4.63 (3.0% of price) | annualised 20d 37.6%
Volume: 0.41x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

```text
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 2.8% of open interest (1,889,422 contracts)
Change on the week: -1.4% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 119.10M | fund size: 18.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Positioning net short 5.8% of OI, short positions fell 1.2% week‑over‑week
- Technical trend below 20‑day and 50‑day SMAs, RSI 40.6, MACD slightly negative
- Fund flows positive: share count +2.6% over 7 days
- Cost of holding -14% annual, heavy roll cost

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 24.50 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 25.06 (-2.2%), 50d 25.56 (-4.2%), 200d 23.39 (+4.8%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -0.387 vs signal -0.318 (histogram -0.069)
Returns: 1d +0.4% | 5d -1.1% | 1m -7.7% | 3m -3.0%
52-week range: 19.88 - 28.00 (now 56.9% of the way up)
Volatility: ATR(14) 0.48 (1.9% of price) | annualised 20d 19.1%
Volume: 0.18x the 20-day average
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

```text
Cost of holding this fund instead of wheat itself: -14.0% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -3.0%, commodity -0.9%, gap -2.1% | 6 months: fund +7.5%, commodity +13.1%, gap -5.6% | 12 months: fund +21.3%, commodity +35.3%, gap -14.0%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 5.8% of open interest (497,181 contracts)
Change on the week: -1.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.6% (7.19M) over 7d
Shares outstanding: 11.63M | fund size: 284.96M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 381.07 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 385.20 (-1.1%), 50d 397.30 (-4.1%), 200d 415.05 (-8.2%); 50d below 200d
Momentum: RSI(14) 44.5 | MACD -4.720 vs signal -4.828 (histogram 0.108)
Returns: 1d +1.3% | 5d +0.6% | 1m -2.7% | 3m +3.4%
52-week range: 362.32 - 495.90 (now 14.0% of the way up)
Volatility: ATR(14) 6.17 (1.6% of price) | annualised 20d 20.9%
Volume: 0.32x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.3% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +3.4%, commodity +4.0%, gap -0.5% | 6 months: fund -13.4%, commodity -13.1%, gap -0.3% | 12 months: fund +0.1%, commodity +0.4%, gap -0.3%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 28.0% of open interest (396,109 contracts)
Change on the week: -1.6% of open interest
Crowding: 53% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 260.30M | fund size: 99.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.08% (+0.03 on the week) | 5-year 4.87% (-0.13 on the week) | 10-year 5.06% (-0.17 on the week) | 30-year 5.40% (-0.21 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.98 (-0.16 on the week)
Volatility (VIX): 17.44 (+2.0 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 199k (2026-10-10)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 11.16 (bar of 2026-10-15), from 502 daily bars
Trend: vs 20d SMA 10.80 (+3.3%), 50d 10.45 (+6.8%), 200d 11.29 (-1.2%); 50d below 200d
Momentum: RSI(14) 57.3 | MACD 0.188 vs signal 0.136 (histogram 0.052)
Returns: 1d -0.5% | 5d +3.2% | 1m +7.7% | 3m +6.2%
52-week range: 9.63 - 16.90 (now 21.0% of the way up)
Volatility: ATR(14) 0.37 (3.3% of price) | annualised 20d 47.1%
Volume: 0.24x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -14.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +6.2%, commodity +12.6%, gap -6.4% | 6 months: fund +3.5%, commodity +23.8%, gap -20.3% | 12 months: fund -6.6%, commodity +8.2%, gap -14.8%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 8.0% of open interest (1,815,990 contracts)
Change on the week: -0.5% of open interest
Crowding: 3% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 12.08M | fund size: 134.87M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

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

