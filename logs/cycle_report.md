# Daily report

**22 Oct 2026, 19:09 Israel time (16:09 UTC)** · 80 names checked · 0 traded · 0 with a problem

**Answers with no explanation:** 10 of 66 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 4 | 12 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Gold (GLD) · Commodity | **Sold part.** Sold 3 of 10 shares at +1.10R, 7 still held. Stop-loss raised 387.99 → 383.47. |
| ASML (ASML) · Company | **Stop raised.** At +0.33R, following the price. Stop-loss raised 1750.24 → 1714.37. |
| Eli Lilly (LLY) · Company | **Stop raised.** At +2.57R, following the price. Stop-loss raised 1224.49 → 1233.74. |
| Nvidia (NVDA) · Company | **Stop raised.** At +0.21R, following the price. Stop-loss raised 228.84 → 226.55. |
| Israel (EIS) · Sector or country | **Holding.** -0.69R, holding 57 shares. Stop-loss 118.59. |
| United Kingdom (EWU) · Sector or country | **Holding.** +1.50R, holding 104 shares. Stop-loss 47.23. |
| HDFC Bank (HDB) · Company | **Holding.** -0.25R, holding 60 shares. Stop-loss 21.65. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** -0.22R, holding 158 shares. Stop-loss 76.66. |
| Defence and aerospace (ITA) · Sector or country | **Holding.** -0.87R, holding 33 shares. Stop-loss 201.78. |
| JPMorgan Chase (JPM) · Company | **Holding.** -0.04R, holding 15 shares. Stop-loss 321.20. |
| Microsoft (MSFT) · Company | **Holding.** -0.40R, holding 9 shares. Stop-loss 509.74. |
| Royal Bank of Canada (RY) · Company | **Holding.** +0.79R, holding 17 shares. Stop-loss 194.88. |
| US materials and chemicals (XLB) · Sector or country | **Holding.** -0.01R, holding 138 shares. Stop-loss 49.68. |
| Exxon Mobil (XOM) · Company | **Holding.** +1.97R, holding 9 shares. Stop-loss 170.88. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “Buy”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Secured USD 235M three‑year contract (news)
- Four consecutive earnings beats (earnings record)
- Price above 20‑day and 50‑day SMA, MACD positive (technical)
- Analyst mean price target +8.2% above current price (analyst view)
- Trailing P/E 55.8 indicates premium valuation (fundamentals)

<details><summary><b>News</b> — score +0.70</summary>

- [Elbit Systems (ESLT) Gains Over 20% in 2026 as Aerospace Weakness Tests Its Premium Valuation](https://finance.yahoo.com/markets/stocks/articles/elbit-systems-eslt-gains-over-171717711.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Elbit Systems Ltd. (NASDAQ:ESLT) has delivered solid returns in 2026, supported by robust demand for its advanced technologies. The stock is already up more...
- [(ESLT) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/9/ESLT_Price_Dynamics_and_Execution-Aware_Positioning_102226011002_1792645802.html)  
  <sub>Stock Traders Daily, 14 hours ago</sub>  
  Key findings for Elbit Systems Ltd. (NASDAQ: ESLT). Strong Sentiment Across All Horizons Supports Overweight Bias; A mid-channel oscillation pattern is in...
- [ESLT stock pre-market at EUR 657.25: defense systems provider](https://www.ad-hoc-news.de/boerse/news/vorboerse/eslt-stock-pre-market-at-eur-657-25-defense-systems-provider/70390141)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  Elbit Systems supplies defense, homeland security and commercial aerospace solutions. At Lang & Schwarz the stock trades pre-market at EUR 657.25 on October...
- [Elbit Systems secures USD 235 million deal: Elbit Systems stock is valued at USD 34.8 billion](https://www.ad-hoc-news.de/boerse/news/corporate-news/elbit-systems-secures-usd-235-million-deal-elbit-systems-stock-is-valued-at-usd-34-8-billion/70392651)  
  <sub>AD HOC NEWS, 6 hours ago</sub>  
  A USD 235.00 million contract runs for three years. The USD 2287.10 million quarter and USD 32.00 billion backlog frame Elbit Systems stock.
- [Cathie Wood Adds Netflix After Earnings Selloff, Ark Keeps Selling Palantir Stock](https://www.tradingview.com/news/benzinga:92f36d4c4094b:0-cathie-wood-adds-netflix-after-earnings-selloff-ark-keeps-selling-palantir-stock/)  
  <sub>TradingView, 12 hours ago</sub>  
  On Wednesday, Cathie Wood-led Ark Invest purchased shares of Netflix Inc. NASDAQ:NFLX, while continuing to trim its position in Palantir Technologies Inc.
- [Cathie Wood’s ARK sells Shopify stock, buys Scribe Therapeutics](https://www.investing.com/news/company-news/cathie-woods-ark-sells-shopify-stock-buys-scribe-therapeutics-93CH-4964448)  
  <sub>Investing.com, 14 hours ago</sub>  
  Cathie Wood's ARK ETF published their daily trades for Wednesday, October 21st, 2026, showcasing a mix of strategic buys and sells across various sectors.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 741.21 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 705.73 (+5.0%), 50d 723.17 (+2.5%), 200d 782.93 (-5.3%); 50d below 200d
Momentum: RSI(14) 57.3 | MACD 4.912 vs signal -3.879 (histogram 8.791)
Returns: 1d -0.2% | 5d -0.1% | 1m -0.2% | 3m -9.6%
52-week range: 454.95 - 1,014.33 (now 51.2% of the way up)
Volatility: ATR(14) 18.77 (2.5% of price) | annualised 20d 40.6%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.74B
Valuation: trailing P/E 55.77 | forward P/E 39.82 | P/B 7.86 | PEG n/a
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
Price target: mean 802.17 (+8.2% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-10-05 Jefferies: main, Hold -> Hold
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 27.6%
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

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Strong earnings beat and raised FY27 guidance drive a bullish view despite overbought technicals and slightly bearish analyst price target.

**Main reasons it gave:**
- Q1 earnings beat (+5.82% EPS surprise) and raised FY27 guidance
- RSI 74.7 indicates overbought condition, suggesting short‑term pullback risk
- Analyst mean price target $162.13 is ~2.3% below current price, indicating slight bearish sentiment
- Strong profitability: ROE 30.3% and operating margin 22.1%

<details><summary><b>News</b> — score +0.90</summary>

- [Procter & Gamble earnings beat as sales rise 4%, boosted by laundry and home products](https://www.cnbc.com/2026/10/22/procter-gamble-pg-q1-2027-earnings.html)  
  <sub>CNBC, 3 hours ago</sub>  
  Procter & Gamble topped Wall Street's estimates for its quarterly earnings and revenue.
- [PG Stock Climbs to $158.59 Ahead of Procter & Gamble Q1 Earnings](https://www.fxleaders.com/news/2026/10/22/procter-gamble-stock-forecast/)  
  <sub>FXLeaders, 2 hours ago</sub>  
  Procter & Gamble (NYSE: PG) is trading at $158.59 in the pre-market hours, rising +1.12% for the day. The stock declined 1.56% yesterday.
- [ETFs Are Net Sellers of Procter & Gamble (PG) on Tuesday](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-procter-gamble-110309005.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. ETF activity left The Procter & Gamble Company (PG) with a net outflow of $61.8 million on Tuesday, as 17 ETFs...
- [Procter & Gamble (NYSE:PG) Reaffirms FY27 Outlook as Core EPS Beat and Volume Growth Offset Sales Miss](https://www.chartmill.com/news/PG/Chartmill-56636-Procter-Gamble-NYSEPG-Reaffirms-FY27-Outlook-as-Core-EPS-Beat-and-Volume-Growth-Offset-Sales-Miss)  
  <sub>ChartMill, 2 hours ago</sub>  
  P&G beat Q1 profit estimates, sales fell just short, reaffirmed FY27 outlook, and shares rose premarket as volume growth offset commodity pressure.
- [Why Procter & Gamble Stock Is Heading for Its Biggest Gain Since 2020](https://www.barrons.com/articles/procter-gamble-earnings-stock-price-21cd2df6)  
  <sub>Barron's, 56 minutes ago</sub>  
  Procter & Gamble rises after reporting solid organic growth in its product categories and raising guidance thanks to a recent acquisition.
- [Procter & Gamble (PG) Reports Strong Q3 Results, Reinforcing Div](https://www.gurufocus.com/news/9136349/procter-gamble-pg-reports-strong-q3-results-reinforcing-dividend-appeal)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 22, 2026, Procter & Gamble Co (NYSE: PG) announced better-than-expected third-quarter earnings with a non-GAAP EPS of $2.00, beating estimates by...
- [Why Is Procter & Gamble Stock Gaining Thursday? - Procter & Gamble (NYSE:PG)](https://www.benzinga.com/markets/earnings/26/10/62527709/tide-and-gillette-maker-procter-gambles-sales-machine-keeps-humming-despite-inflation-pressure)  
  <sub>Benzinga, 58 minutes ago</sub>  
  Procter & Gamble (NYSE: PG) stock jumps after Q1 earnings & revenue beat estimates. Full fiscal 2027 sales outlook raised.
- [Procter & Gamble Co Stock (PG) Moved Up by 5.19% on Oct 22: A Full Analysis](https://www.tradingkey.com/news/market-movers/262232615-market-movers-pg-20261022)  
  <sub>TradingKey, 32 minutes ago</sub>  
  First-quarter net sales rose four percent year-over-year to $23.28 billion.Adjusted core earnings per share reached $2.00, beating analyst estimates.
- [Procter & Gamble (PG) Q1 Earnings and Revenues Beat Estimates](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-q1-earnings-111502516.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  P&G (PG) delivered earnings and revenue surprises of +5.82% and +2.51%, respectively, for the quarter ended September 2026. Do the numbers hold clues to...
- [Procter & Gamble (PG) Reports Q1 Volume-Driven Growth Amid Risin](https://www.gurufocus.com/news/9136713/procter-gamble-pg-reports-q1-volumedriven-growth-amid-rising-costs-and-china-challenges)  
  <sub>GuruFocus, 1 hour ago</sub>  
  On October 22, 2026, Procter & Gamble Co (NYSE: PG) disclosed that its first-quarter growth was primarily fueled by increased volume across multiple global...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 165.90 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 152.03 (+9.1%), 50d 148.04 (+12.1%), 200d 148.40 (+11.8%); 50d below 200d
Momentum: RSI(14) 74.7 | MACD 3.836 vs signal 2.633 (histogram 1.203)
Returns: 1d +5.8% | 5d +5.6% | 1m +12.6% | 3m +12.5%
52-week range: 138.04 - 167.20 (now 95.5% of the way up)
Volatility: ATR(14) 3.04 (1.8% of price) | annualised 20d 27.0%
Volume: 0.95x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 385.33B
Valuation: trailing P/E 25.06 | forward P/E 22.44 | P/B 7.23 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.1% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 in line
  2027-03-31 beat by 3% | 2026-06-30 in line | 2026-03-31 in line | 2025-06-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

```text
Consensus: buy (mean 2.16 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 8 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 162.13 (-2.3% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-10-20 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Citigroup: main, Buy -> Buy
  - 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - 2026-10-06 RBC Capital: main, Outperform -> Outperform
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 156,293 shares in 42 transaction(s) | sold 48,751 shares in 16
Net: +107,542 shares (+5.3% of insider holdings) | insiders hold 2,138,478 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(40 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Fundamentals and analyst consensus are strongly bullish, while technicals are moderately bearish and earnings record is mixed. No insider buying activity. Overall net bullish view with moderate conviction.

**Main reasons it gave:**
- Fundamentals: profit margin 54.8%, operating margin 34%, ROE 48.7%, revenue growth 24.2% YoY
- Analyst consensus strong buy with mean price target $429.13 (+31% upside)
- Technical: price below 20d/50d/200d SMAs, RSI 35.1, MACD negative, volume 0.29x 20‑day average
- Earnings record: 2 beats, 2 misses; recent quarter missed by 4%
- Insider activity: no insider purchases in last 180 days

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 327.15 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 344.42 (-5.0%), 50d 343.52 (-4.8%), 200d 341.34 (-4.2%); 50d above 200d
Momentum: RSI(14) 35.1 | MACD -2.067 vs signal 0.025 (histogram -2.093)
Returns: 1d -2.3% | 5d -6.3% | 1m -3.2% | 3m +2.3%
52-week range: 251.69 - 402.62 (now 50.0% of the way up)
Volatility: ATR(14) 8.61 (2.6% of price) | annualised 20d 19.4%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.00T
Valuation: trailing P/E 16.42 | forward P/E 21.32 | P/B 6.43 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.21 | short interest 1.4% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.13 (+31.2% vs last close), range 340.00 - 500.00
Recent rating changes:
  - 2026-10-22 Citizens: main, Market Outperform -> Market Outperform
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Keybanc: main, Overweight -> Overweight
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-10-14 UBS: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
Institutional ownership: 81.1%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 195,313,088 shares
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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data HTTP 502: <html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
</body>
</html>


### Novo Nordisk (NVO) · Company — BULLISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The recent CagriSema trial showing 25% weight loss in women provides a material, ticker‑specific catalyst that pushes the outlook bullish. Fundamentals are cheap (trailing P/E 9.69) and the company generates strong cash flow, supporting the upside. Technicals are mixed – price near 52‑week low with thin volume and a longer‑term downtrend – which tempers the view, and the earnings record (2 misses out of 4) adds downside risk. Analyst consensus is neutral but the mean price target implies ~14% upside. Overall, the net effect is modestly bullish, warranting a BUY signal with moderate conviction.

**Main reasons it gave:**
- CagriSema trial shows 25% weight loss in women (news)
- Trailing P/E 9.69 indicates cheap valuation (fundamentals)
- Price near 52‑week low with low volume (technical)
- Recent earnings miss of 6% (earnings record)

<details><summary><b>News</b> — score +0.45</summary>

- [Bristol Myers Squibb vs. Novo Nordisk: Stable Scale vs. GLP-1 Volatility](https://www.theglobeandmail.com/investing/markets/stocks/NVO-N/pressreleases/8315309/bristol-myers-squibb-vs-novo-nordisk-stable-scale-vs-glp-1-volatility/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [NVO261030P00034000 interactive stock chart | NVO Oct 2026 34.000 put stock](https://uk.finance.yahoo.com/chart/NVO261030P00034000)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Novo Nordisk (NVO), Why Is Fresh Attention Building Now?](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-nvo/novo-nordisk/news/novo-nordisk-nvo-why-is-fresh-attention-building-now)  
  <sub>Simply Wall Street, 10 hours ago</sub>  
  OpenAI's acquisition of biotech software startup Orchestra Bio has pulled Novo Nordisk (NYSE:NVO) into the spotlight again, since the drugmaker already uses...
- [When the Price of (NVO) Talks, People Listen (NVO:CA)](https://news.stocktradersdaily.com/canada/when-the-price-of-nvo-talks,-people-listen_20261021_8df478)  
  <sub>Stock Traders Daily, 15 hours ago</sub>  
  My Stocks · Stock Signals · Sentiment Table · Macroeconomics · Raw Data · Evitar Corte · Home. Proprietary Signals for NVO:CA. Proprietary Signals for NVO:...
- [RBC Capital Remains a Buy on Eli Lilly & Co (LLY)](https://www.theglobeandmail.com/investing/markets/stocks/LLY-N/pressreleases/8300031/rbc-capital-remains-a-buy-on-eli-lilly-co-lly/)  
  <sub>The Globe and Mail, 13 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [Novo's CagriSema shows 25% weight loss in women, sparking hope for stock recovery.](https://pluang.com/en/news-feed/di-mana-saham-novo-10-tahun-ke-depan)  
  <sub>Pluang, 19 hours ago</sub>  
  Novo's drug CagriSema has demonstrated a significant 25% weight loss effect in women, a promising result that could boost the company's prospects.
- [Where Will Novo Stock Be in 10 Years?](https://www.theglobeandmail.com/investing/markets/markets-news/Motley%20Fool/8289111/where-will-novo-stock-be-in-10-years/)  
  <sub>The Globe and Mail, 19 hours ago</sub>  
  Novo(NYSE: NVO), a Denmark-based pharmaceutical leader, has made important breakthroughs over the past decade. The company initially benefited from its...
- [Biotech Stocks To Watch And Pharma Industry News](https://www.investors.com/news/technology/biotech-and-pharma-industry-and-stock-news-merk-bristol-myers-amgn-gilead/)  
  <sub>Investor's Business Daily, 22 hours ago</sub>  
  Bookmark this page for the latest news and stock analysis for Eli Lilly (LLY), Novo Nordisk (NVO), Merck (MRK), Johnson & Johnson (JNJ), Pfizer (PFE) and...
- [Novo Nordisk (NYSE: NVO) CagriSema Shows 25% Weight Loss In Women As Investors Eye Stock Recovery](https://www.foreignpolicyjournal.com/2026/10/21/novo-nordisk-nyse-nvo-cagrisema-shows-25-weight-loss-in-women-as-investors-eye-stock-recovery/)  
  <sub>Foreign Policy Journal, 21 hours ago</sub>  
  Novo Nordisk (NYSE: NVO) has reported that a 2.4 milligram dose of CagriSema was associated with an average weight loss of 25% after 68 weeks in 2309 women.
- [CoreWeave (CRWV) vs. Nebius (NBIS): Which AI Infrastructure Stock Offers More Upside?](https://www.tipranks.com/news/coreweave-crwv-vs-nebius-nbis-which-ai-infrastructure-stock-offers-more-upside)  
  <sub>TipRanks, 23 hours ago</sub>  
  CoreWeave ($CRWV) and Nebius ($NBIS) stocks both offer upside, but one stock offers greater upside than the other. The demand for artificial intelligence...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 39.62 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 38.39 (+3.2%), 50d 42.07 (-5.8%), 200d 44.78 (-11.5%); 50d below 200d
Momentum: RSI(14) 49.5 | MACD -0.729 vs signal -1.158 (histogram 0.429)
Returns: 1d +1.4% | 5d +1.0% | 1m +3.8% | 3m -18.8%
52-week range: 35.29 - 63.98 (now 15.1% of the way up)
Volatility: ATR(14) 0.86 (2.2% of price) | annualised 20d 20.0%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 174.85B
Valuation: trailing P/E 9.69 | forward P/E 11.62 | P/B 5.31 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.35</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.11 (+13.8% vs last close), range 39.76 - 61.80
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

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

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: positive news on record backlog and strong earnings record versus bearish technicals and high leverage; analyst view bullish but insider activity neutral. Overall contradictory inputs lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Record order backlog driven by data-center power demand (positive news)
- Technical downtrend: price below 20d, 50d, 200d SMAs, RSI 28.7, low volume (bearish technicals)
- Four consecutive earnings beats (strong earnings record)
- High debt/equity ratio of 232.8% (fundamental risk)

<details><summary><b>News</b> — score +0.15</summary>

- [How Big Could Caterpillar Stock's Next Fall Be?](https://finance.yahoo.com/markets/stocks/articles/big-could-caterpillar-stocks-next-171337582.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Caterpillar (CAT) stock lost 18.4% over the three months to October 20,...
- [Caterpillar Inc Stock (CAT) Moved Down by 3.96% on Oct 22: What Investors Need To Know](https://www.tradingkey.com/news/market-movers/262232614-market-movers-cat-20261022)  
  <sub>TradingKey, 30 minutes ago</sub>  
  Macroeconomic concerns and falling factory surveys drove downside volatility for Caterpillar stock.Regulatory scrutiny and lowered analyst price targets...
- [CAT 261023 585.00P (CAT261023P585000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/CAT261023P585000-US)  
  <sub>Moomoo, 8 hours ago</sub>  
  Track real-time CAT 261023 585.00P (CAT261023P585000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Caterpillar (CAT) Laps the Stock Market: Here's Why](https://au.finance.yahoo.com/news/caterpillar-cat-laps-stock-market-204503640.html)  
  <sub>Yahoo Finance Australia, 18 hours ago</sub>  
  The latest trading day saw Caterpillar (CAT) settling at $740.21, representing a +2.06% change from its previous close.
- [Caterpillar (NYSE:CAT) stock rises as power-equipment demand lifts backlog today](https://kalkinemedia.com/us/stocks/industrial/caterpillar-nysecat-stock-rises-as-power-equipment-demand-lifts-backlog-today)  
  <sub>Kalkine Media, 5 hours ago</sub>  
  Caterpillar (NYSE:CAT) stock drew attention as a record order backlog, lifted by data-center power demand, framed its approaching quarterly results amid...
- [Will Caterpillar (CAT) Beat Estimates Again in Its Next Earnings Report?](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-beat-estimates-again-151003761.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  If you are looking for a stock that has a solid history of beating earnings estimates and is in a good position to maintain the trend in its next quarterly...
- [Caterpillar stock: Caterpillar schedules October 29 results for Caterpillar stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/caterpillar-stock-caterpillar-schedules-october-29-results-for-caterpillar-stock/70386080)  
  <sub>AD HOC NEWS, 23 hours ago</sub>  
  Caterpillar reports USD 20.54 billion revenue, up 23.70 percent year over year. Caterpillar stock costs EUR 652.00 on October 21, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 700.07 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 787.58 (-11.1%), 50d 803.01 (-12.8%), 200d 808.14 (-13.4%); 50d below 200d
Momentum: RSI(14) 28.7 | MACD -26.492 vs signal -17.221 (histogram -9.271)
Returns: 1d -5.4% | 5d -4.8% | 1m -13.8% | 3m -21.2%
52-week range: 513.91 - 1,064.90 (now 33.8% of the way up)
Volatility: ATR(14) 27.45 (3.9% of price) | annualised 20d 37.9%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 321.80B
Valuation: trailing P/E 30.14 | forward P/E 21.48 | P/B 16.59 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 2.00 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 15 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 945.76 (+35.1% vs last close), range 575.00 - 1,155.00
Recent rating changes:
  - 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - 2026-10-12 Citigroup: main, Buy -> Buy
  - 2026-10-05 Truist Securities: main, Buy -> Buy
  - 2026-09-10 Freedom Broker: up, Hold -> Buy
  - 2026-08-11 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-08-06 DA Davidson: main, Neutral -> Neutral
Institutional ownership: 73.5%
Largest holders: Blackrock Inc. (8.3%), State Street Corporation (7.5%), Vanguard Capital Management LLC (6.5%), State Farm Mutual Automobile Insurance Co (3.2%), Vanguard Portfolio Management LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The data are mixed and lack a clear catalyst. News is generic, technicals show mixed signals with low volume, fundamentals are mixed with high debt and earnings decline, earnings record is weak, while analyst consensus is bullish and insiders have made small purchases. The contradictions lead to a neutral stance with low conviction.

**Main reasons it gave:**
- No material company-specific news; only generic price/option data and a small institutional sell (Robeco trimmed 1.3%)
- Technical indicators mixed: bullish MACD but low volume (0.15x 20‑day avg) and recent price decline
- Earnings record shows 1 beat and 3 misses in the last 4 quarters
- Fundamentals show high debt/equity (168.6%) and earnings decline (-10.9% YoY) despite strong revenue growth (+49.8%)

<details><summary><b>News</b> — score -0.20</summary>

- [MercadoLibre, Inc. (MELI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  MercadoLibre, Inc. (MELI) · 0.86% · 1.89% · 0.04% · -7.91% · -13.41% · 17.11% · 8,331.27%. Key Events. Baseline. Advanced Chart. Loading chart...
- [MercadoLibre, Inc. $MELI Stock Sold by Robeco Institutional Asset Management B.V.](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-stock-sold-by-robeco-institutional-asset-management-bv-2026-10-22/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Robeco Institutional Asset Management B.V. trimmed its holdings in MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 1.3% in the 3rd quarter, according to...
- [MELI 261023 1905.00C (MELI261023C1905000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/MELI261023C1905000-US)  
  <sub>Moomoo, 22 hours ago</sub>  
  Track real-time MELI 261023 1905.00C (MELI261023C1905000) stock options chain data and pricing information and news on moomoo App for your options trading...
- [MELI Nov 2026 1805.000 put (MELI261113P01805000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/MELI261113P01805000/chart/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  OPR - Delayed Quote • USD. MELI Nov 2026 1805.000 put (MELI261113P01805000). 50.22 0.00 (0.00%). As of October 12 at 1:56:33 p.m. EDT. Market Open. Tools.
- [MELI Sep 2027 1080.000 put (MELI270917P01080000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI270917P01080000/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest MELI Sep 2027 1080.000 put (MELI270917P01080000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI281215C02360000 Interactive Stock Chart | MELI Dec 2028 2360.000 call Stock](https://finance.yahoo.com/chart/MELI281215C02360000)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Nov 2026 1940.000 call (MELI261106C01940000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI261106C01940000/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Find the latest MELI Nov 2026 1940.000 call (MELI261106C01940000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Oct 2026 1685.000 put (MELI261023P01685000) interactive stock chart](https://au.finance.yahoo.com/quote/MELI261023P01685000/chart/)  
  <sub>Yahoo Finance Australia, 6 hours ago</sub>  
  Interactive chart for MELI Oct 2026 1685.000 put (MELI261023P01685000) – analyse all of the data with a huge range of indicators.
- [MELI Oct 2026 1750.000 call (MELI261023C01750000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261023C01750000/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest MELI Oct 2026 1750.000 call (MELI261023C01750000) stock quote, history, news and other vital information to help you with your stock trading...
- [MELI Oct 2026 1660.000 call (MELI261030C01660000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261030C01660000/)  
  <sub>Yahoo Finance UK, 16 hours ago</sub>  
  Find the latest MELI Oct 2026 1660.000 call (MELI261030C01660000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 1,815.30 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 1,816.30 (-0.1%), 50d 1,859.50 (-2.4%), 200d 1,826.92 (-0.6%); 50d above 200d
Momentum: RSI(14) 46.7 | MACD 3.418 vs signal 0.633 (histogram 2.785)
Returns: 1d -2.1% | 5d -2.2% | 1m +0.9% | 3m +0.8%
52-week range: 1,546.81 - 2,360.76 (now 33.0% of the way up)
Volatility: ATR(14) 54.26 (3.0% of price) | annualised 20d 41.2%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 92.03B
Valuation: trailing P/E 49.37 | forward P/E 32.28 | P/B 11.75 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.8% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 16 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 2,273.86 (+25.3% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-13 Citigroup: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
Institutional ownership: 80.0%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Contradictory signals: technicals show negative momentum, fundamentals are weak (high leverage, high trailing P/E), while analyst consensus is bullish and earnings record is mostly positive but includes a recent large miss. No news catalyst. Net tilt is slight bullish, but contradictions and lack of catalyst lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Technical momentum negative (MACD below signal, RSI neutral)
- High leverage (debt/equity 217.8%)
- Analyst consensus strong buy with 19% price target
- Recent earnings miss (June 30) with 92% shortfall

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 39.88 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 40.15 (-0.7%), 50d 38.62 (+3.2%), 200d 34.34 (+16.1%); 50d above 200d
Momentum: RSI(14) 50.7 | MACD 0.665 vs signal 0.791 (histogram -0.126)
Returns: 1d -1.8% | 5d -3.0% | 1m +2.2% | 3m +29.4%
52-week range: 18.95 - 41.50 (now 92.8% of the way up)
Volatility: ATR(14) 1.12 (2.8% of price) | annualised 20d 24.9%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 46.51B
Valuation: trailing P/E 66.47 | forward P/E 12.92 | P/B 5.99 | PEG n/a
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.6% of float
Next earnings: 2026-11-03
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-06-30 missed by 92% | 2026-03-31 beat by 9% | 2025-12-31 beat by 39% | 2025-09-30 beat by 17%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 47.58 (+19.3% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-15 Barclays: main, Overweight -> Overweight
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
Institutional ownership: 27.0%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

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
  - 2026-08-03 HUGHES ERIC A (Officer): 25,578 shares, 892.05K
(13 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed news: a sizable recall of ~105,800 US Toyota vehicles (negative) versus strong demand indicated by a 35‑day inventory supply (positive). Technicals show modest upside but thin volume. Fundamentals are cheap yet leveraged with negative free cash flow, while analyst sentiment is bullish with a sizable price‑target upside. Four consecutive earnings beats reinforce earnings strength. Contradictory signals lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Recall of ~105,800 US Toyota vehicles (negative catalyst)
- Toyota inventory at 35‑day supply, indicating strong demand
- Trailing P/E 8.67 and forward P/E 12.51 suggest undervaluation
- Four consecutive earnings beats (44%, 12%, 27%, 24% beats)
- Analyst mean price target $234.08 (+18.6% upside)

<details><summary><b>News</b> — score -0.40</summary>

- [Tesla: My First Buy Rating Ever, Thanks To SpaceX (Rating Upgrade) (NASDAQ:TSLA)](https://seekingalpha.com/article/4956354-tesla-my-first-buy-rating-ever-thanks-to-spacex-rating-upgrade)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Tesla, Inc. faces margin pressure, weak delivery growth, and rising CapEx for FSD and AI. Click for this TSLA earnings update.
- [Greene Concepts Partners with Mission Springs Water Foundation to Support Faith-Driven Clean Water Mission](https://finance.yahoo.com/small-business/articles/greene-concepts-partners-mission-springs-114500434.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Full truckloads of customized 500 mL artesian spring water will support Mission Springs' mission to provide clean drinking water, compassion and hope to...
- [Toyota to recall about 105,800 US vehicles over fire risk, NHTSA says By Reuters](https://www.investing.com/news/stock-market-news/toyota-to-recall-about-105800-us-vehicles-over-fire-risknhtsa-says-4961860)  
  <sub>Investing.com, 7 hours ago</sub>  
  Oct 21 (Reuters) - Toyota is recalling 105,794 vehicles in the US over a potential fuel leak that could raise the risk of fire if it reaches an ignition...
- [Rockets, Robots and a $135 Billion AI Bar Tab](https://www.fxtm.com/en/analysis/market-analysis/rockets-robots-and-a-135billion-ai-bar-tab/)  
  <sub>FXTM, 4 hours ago</sub>  
  SpaceX's AI division earned more than its rockets did. It made up over half of quarterly revenue. Meta had a record quarter, then spent more cash than it...
- [A new research facility has its occupancy permit; American Fusion expects to move in by Nov. 1.](https://www.stocktitan.net/news/AMFN/american-fusion-tm-advances-texatron-tm-commercialization-with-four-rgzf745gw672.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  A North Texas property deal could close by end-October 2026, subject to customary conditions; the company is also negotiating several investment-banking...
- [BYD, Chery expand EU foothold as car registrations climb for eighth straight month (EUR:USD:)](https://seekingalpha.com/news/4655682-byd-chery-expand-eu-foothold-as-car-registrations-climb-for-eighth-straight-month)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  EU car registrations rose 5.7% YTD 2026 as EV share hit 22.7% and Tesla, BYD, Chery gained.
- [(QMAX) Pivots Trading Plans and Risk Controls (QMAX:CA)](https://news.stocktradersdaily.com/canada/qmax-pivots-trading-plans-and-risk-controls_20261022_1a35fd)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Pivot Points for Hamilton Technology YIELD MAXIMIZER TM ETF QMAX that help investors see where to buy and sell QMAX_.
- [Banks can now offer Greenlight money lessons to kids through their apps](https://www.stocktitan.net/news/JKHY/greenlight-collaborates-with-jack-henry-to-bring-its-leading-family-w7gv0gnaf7zt.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Jack Henry's ecosystem includes over 1000 fintechs and offers products to more than 7200 financial institutions; Greenlight partners with over 230.
- [Toyota cars are selling out fast with only 35 d...](https://pluang.com/en/news-feed/toyota-laris-manis-mobil-terjual-cepat)  
  <sub>Pluang, 19 hours ago</sub>  
  Toyota is experiencing a surge in demand, with only a 35-day supply of inventory, the lowest among all car brands in the US. Popular models like the RAV4...
- [Sensex Today Tanks 660 Points | Nifty Below 22,600 | Maruti Suzuki & Tata Steel Top Losers](https://www.equitymaster.com/indian-share-markets/10/22/2026/Sensex-Today-Tanks-660-Points--Nifty-Below-22600--Maruti-Suzuki--Tata-Steel-Top-Losers?utm_source=homepage&utm_medium=website&utm_campaign=Content&utm_content=TM)  
  <sub>Equitymaster, 10 hours ago</sub>  
  Indian share markets are trading lower with Sensex trading 660 points lower, and Nifty is trading 252 points lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 197.36 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 188.43 (+4.7%), 50d 191.29 (+3.2%), 200d 199.50 (-1.1%); 50d below 200d
Momentum: RSI(14) 62.8 | MACD 1.537 vs signal 0.125 (histogram 1.412)
Returns: 1d +1.3% | 5d +2.8% | 1m +3.7% | 3m +11.2%
52-week range: 166.50 - 248.29 (now 37.7% of the way up)
Volatility: ATR(14) 3.07 (1.6% of price) | annualised 20d 20.1%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 232.45B
Valuation: trailing P/E 8.67 | forward P/E 12.51 | P/B 15.86 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
```

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+18.6% vs last close), range 230.00 - 239.31
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

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML Vs. Taiwan Semiconductor: Who Can More Fully Satisfy AI Demand?](https://finance.yahoo.com/technology/ai/articles/asml-vs-taiwan-semiconductor-more-124509753.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Both ASML and TSMC say AI demand outstrips everything they can build, but each company is betting on a different strategy to close that gap.
- [ASML Has Incredible News for Nvidia Stock and Micron Stock Investors](https://www.fool.com/investing/2026/10/21/asml-has-incredible-news-for-nvidia-stock-and-micron-stock-investors/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  ASML management's recent comments indicate that the AI infrastructure build-out won't be slowing down.
- [ASML Holding NV Stock (ASML) Opened Down by 3.46% on Oct 22: Key Drivers Unveiled](https://www.tradingkey.com/news/market-movers/262232548-market-movers-asml-20261022)  
  <sub>TradingKey, 54 minutes ago</sub>  
  ASML faced intraday pressure from profit-taking in high-valuation semiconductor stocks.The MACD indicates a sell signal while the Williams %R shows oversold...
- [Besi says ASML is not hybrid bonding rival as AI demand drives orders](https://www.aol.com/articles/besis-quarterly-orders-beat-expectations-051208000.html)  
  <sub>AOL.com, 8 hours ago</sub>  
  By Nathan Vifflin Oct 22 (Reuters) - BE Semiconductor Industries on Thursday beat market expectations for third-quarter orders on strong AI data-centre...
- [10 ETFs Add to ASML (ASML) Holdings on Oct. 20](https://finance.yahoo.com/markets/stocks/articles/10-etfs-add-asml-asml-110139955.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs bought $87.1 million of ASML shares in Tuesday's session.
- [ASML Nov 2026 1605.000 call (ASML261127C01605000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML261127C01605000/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest ASML Nov 2026 1605.000 call (ASML261127C01605000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Nov 2026 1785.000 put (ASML261113P01785000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/ASML261113P01785000/chart/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Interactive Chart for ASML Nov 2026 1785.000 put (ASML261113P01785000), analyze all the data with a huge range of indicators.
- [ASML Nov 2026 2010.000 call (ASML261113C02010000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/ASML261113C02010000/chart/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Interactive Chart for ASML Nov 2026 2010.000 call (ASML261113C02010000), analyze all the data with a huge range of indicators.
- [ASML Nov 2026 1790.000 put (ASML261113P01790000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML261113P01790000/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest ASML Nov 2026 1790.000 put (ASML261113P01790000) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Nov 2026 1120.000 put (ASML261127P01120000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML261127P01120000/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest ASML Nov 2026 1120.000 put (ASML261127P01120000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,602.31 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 1,743.01 (-8.1%), 50d 1,729.09 (-7.3%), 200d 1,586.48 (+1.0%); 50d above 200d
Momentum: RSI(14) 36.8 | MACD -28.362 vs signal -10.421 (histogram -17.941)
Returns: 1d -4.4% | 5d -3.3% | 1m -8.2% | 3m -8.8%
52-week range: 966.57 - 1,989.44 (now 62.2% of the way up)
Volatility: ATR(14) 54.72 (3.4% of price) | annualised 20d 34.0%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 617.56B
Valuation: trailing P/E 39.43 | forward P/E 25.52 | P/B 1,376.84 | PEG 1.58
Profitability: profit margin 34.1% | operating margin 44.4% | ROE 65.6%
Growth (YoY): revenue +55.2% | earnings +135.9%
Balance sheet: debt/equity 8.9% | free cash flow 10.37B
Risk: beta 1.30 | short interest 0.4% of float
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
Price target: mean 2,142.22 (+33.7% vs last close), range 866.34 - 2,845.87
Recent rating changes:
  - 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-16 Wells Fargo: main, Overweight -> Overweight
  - 2026-07-16 RBC Capital: main, Outperform -> Outperform
  - 2026-07-14 RBC Capital: main, Outperform -> Outperform
  - 2026-07-06 Bernstein: main, Outperform -> Outperform
Institutional ownership: 20.3%
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

### HDFC Bank (HDB) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Dividend alert! Last day to buy HDB Financial, Tech Mahindra, LTM among 10 stocks for dividend rewards](https://m.economictimes.com/markets/stocks/news/dividend-alert-last-day-to-buy-hdb-financial-tech-mahindra-ltm-among-10-stocks-for-dividend-rewards/articleshow/135105472.cms)  
  <sub>The Economic Times, 12 hours ago</sub>  
  Under Sebi's T+1 settlement cycle, investors need to purchase a company's shares at least one trading day before the record date to ensure the shares are...
- [Tech Mahindra, HDB Financial Services, IRFC, Oberoi Realty dividend record date on Oct 23: Last day to buy for payout](https://upstox.com/news/market-news/stocks/tech-mahindra-hdb-financial-services-irfc-oberoi-realty-dividend-record-date-on-oct-23-last-day-to-buy-for-payout/article-202220/)  
  <sub>Upstox, 7 hours ago</sub>  
  360 ONE WAM, Artemis Electricals and Projects, Bhansali Engineering Polymers, Garuda Construction and Engineering, ICICI Lombard General Insurance Company,...
- [Forum: Take a balanced approach to HDB corridor clutter](https://www.straitstimes.com/opinion/forum/forum-take-a-balanced-approach-to-hdb-corridor-clutter)  
  <sub>The Straits Times, 5 hours ago</sub>  
  I refer to the letter “Clamp down on residents blocking common corridors with items” (Oct 21). While I share the writer's concerns about fire safety,...
- [HDB stock pre-market: Indian bank at EUR 20.05 before the open](https://www.ad-hoc-news.de/boerse/news/vorboerse/hdb-stock-pre-market-indian-bank-at-eur-20-05-before-the-open/70391182)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  HDFC Bank provides banking and financial services to individual and corporate clients in India. At Lang & Schwarz the stock trades pre-market at EUR 20.05...
- [HDB Financial Services ESOP Allotment: 1,21,300 Shares Issued](https://www.kalkine.co.in/article/announcements/hdb-financial-services-nsehdbfs-what-does-the-esop-allotment-of-121300-shares-mean)  
  <sub>Kalkine India, 3 hours ago</sub>  
  HDB Financial Services (NSE:HDBFS) allotted 1,21300 equity shares under its ESOP schemes on 22 Oct 2026, raising paid-up capital.
- [Investment funds experienced net outflows of VND 31.7 trillion, and the pressure has not eased.](https://www.vietnam.vn/en/quy-dau-tu-rut-rong-31-700-ty-dong-ap-luc-chua-ha-nhiet)  
  <sub>Vietnam.vn, 11 hours ago</sub>  
  Capital continued to flow out of investment funds, bringing the total net outflow for the first nine months of 2026 to nearly VND 31700 billion,...
- [Five Consecutive Losses Push HDB Financial Services Ltd to a New 52-Week Low](https://www.marketsmojo.com/news/stocks-in-action/hdb-financial-services-ltd-falls-to-52-week-low-amid-market-pressure-4233921)  
  <sub>MarketsMojo, 9 hours ago</sub>  
  For the fifth straight session, HDB Financial Services Ltd closed lower, breaching its 52-week low at Rs 501.75 on 22 Oct 2026, marking a significant...
- [HDFC Bank reports Q2 profit growth as leadership change nears for HDFC Bank stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdfc-bank-reports-q2-profit-growth-as-leadership-change-nears-for-hdfc-bank-stock/70391737)  
  <sub>AD HOC NEWS, 7 hours ago</sub>  
  HDFC Bank reported INR 195.10 billion profit in Q2 FY27. HDFC Bank stock traded at EUR 20.10 on October 22, 2026.
- [Jio, Hyundai, NSE and more: Which of India’s biggest IPOs in recent times delivered the best listing gains?](https://www.theweek.in/news/biz-tech/2026/10/21/jio-hyundai-nse-and-more-which-of-indias-biggest-ipos-in-recent-times-delivered-the-best-listing-gains.amp.html)  
  <sub>The Week, 23 hours ago</sub>  
  The ₹30213-crore initial public offering of Jio Platforms hit full subscription by 11 am, barely 1.5 hours after the opening bell, on the day the...
- [Fractal Analytics among 4 stocks showing RSI trending up](https://m.economictimes.com/markets/stocks/news/fractal-analytics-among-4-stocks-showing-rsi-trending-up/slideshow/135105933.cms)  
  <sub>The Economic Times, 11 hours ago</sub>  
  On October 21, four Nifty500 stocks that gained over 3% were highlighted in the RSI Trending Up scan, based on data from StockEdge.An RSI Trending Up signal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.50 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 22.66 (-0.7%), 50d 22.87 (-1.6%), 200d 26.15 (-14.0%); 50d below 200d
Momentum: RSI(14) 46.4 | MACD 0.007 vs signal -0.030 (histogram 0.037)
Returns: 1d -0.8% | 5d -4.4% | 1m -1.3% | 3m -3.2%
52-week range: 21.84 - 37.18 (now 4.3% of the way up)
Volatility: ATR(14) 0.56 (2.5% of price) | annualised 20d 29.4%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 115.61B
Valuation: trailing P/E 14.51 | forward P/E 16.28 | P/B 8.99 | PEG n/a
Profitability: profit margin 26.5% | operating margin 38.5% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2027-01-16
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.30 (+34.7% vs last close), range 26.20 - 33.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 0 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Big U.S. banks are detecting unauthorized AI agents - report (JPM:NYSE)](https://seekingalpha.com/news/4655856-big-u-s-banks-are-detecting-unauthorized-ai-agents-report)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Several major U.S. banks, such as Bank of America (BAC), JPMorgan Chase (JPM), and Citigroup (C), are restricting third-party AI agent access after...
- [JPM Nov 2026 375.000 call (JPM261127C00375000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/JPM261127C00375000/chart/)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Interactive Chart for JPM Nov 2026 375.000 call (JPM261127C00375000), analyze all the data with a huge range of indicators.
- [J.P. Morgan’s new cohort includes veteran and military spouse businesses averaging $8.6 million in revenue.](https://www.stocktitan.net/news/JPM/j-p-morgan-commercial-banking-and-syracuse-university-s-d-aniello-4aer7pbchuge.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  CEOcircle is a yearlong peer-accountability program; more than 250 leaders have participated since 2021, and cohort companies employ over 2300 people.
- [JPMorgan Chase & Co. $JPM Stock Holdings Lowered by RWQ Financial Management Services Inc.](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-holdings-lowered-by-rwq-financial-management-services-inc-2026-10-22/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  RWQ Financial Management Services Inc. lessened its holdings in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 40.0% during the 3rd quarter,...
- [JPM261023C00425000 Interactive Stock Chart | JPM Oct 2026 425.000 call Stock](https://finance.yahoo.com/chart/JPM261023C00425000)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [JPM sees Corning posting strong revenue on AI demand](https://www.tradingview.com/news/seekingalpha:988117a91094b:0-jpm-sees-corning-posting-strong-revenue-on-ai-demand/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Best Stocks To Buy Now For UK Investors In 2026](https://www.forbes.com/advisor/uk/investing/best-stocks-to-buy-now/)  
  <sub>Forbes, 20 hours ago</sub>  
  Whether you're a complete beginner or a highly-experienced investor, the same question applies – what are the best stocks to invest in for 2026 and beyond?
- [5,483 JPMorgan Chase & Co. $JPM Shares Acquired by Prairie Advisory LLC](https://www.marketbeat.com/instant-alerts/filing-5483-jpmorgan-chase-co-jpm-shares-acquired-by-prairie-advisory-llc-2026-10-22/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Prairie Advisory LLC grew its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 100.3% during the third quarter, according to its most...
- [JPM Oct 2026 322.500 put (JPM261023P00322500) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/JPM261023P00322500/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  Find the latest JPM Oct 2026 322.500 put (JPM261023P00322500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Prosus stock: J.P. Morgan maintains EUR 71.00 target for Prosus stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/prosus-stock-j-p-morgan-maintains-eur-71-00-target-for-prosus-stock/70394221)  
  <sub>AD HOC NEWS, 17 minutes ago</sub>  
  Prosus grew ecosystem revenue 12.00 percent in fiscal 2026. Prosus stock costs EUR 34.05 on October 22, 2026, down 1.53 percent versus Xetra close.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 333.79 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 334.13 (-0.1%), 50d 345.98 (-3.5%), 200d 322.47 (+3.5%); 50d above 200d
Momentum: RSI(14) 43.5 | MACD -2.769 vs signal -3.652 (histogram 0.883)
Returns: 1d -0.4% | 5d -0.5% | 1m -1.1% | 3m -5.5%
52-week range: 282.84 - 365.18 (now 61.9% of the way up)
Volatility: ATR(14) 6.34 (1.9% of price) | annualised 20d 14.6%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 886.40B
Valuation: trailing P/E 14.00 | forward P/E 13.07 | P/B 2.52 | PEG 1.57
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
Consensus: buy (mean 2.04 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 10 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 372.57 (+11.6% vs last close), range 312.00 - 425.00
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

- [LLY Stock Hits All-Time High After Goldman Sachs Raises Price Target Ahead Of Q3 Earnings](https://stocktwits.com/news-articles/markets/equity/lly-stock-hits-new-record-eli-lilly-valuation-pushes-past-berkshire-hathaway-ahead-of-q3-earnings/cZxAGvFRBHP)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Eli Lilly and Company (LLY) shares climbed to a record high in midday trade on Tuesday, pushing its market capitalization above Berkshire Hathaway's (BRK.
- [Eli Lilly stock may move 6.6% on Oct. 29 earnings release](https://www.investing.com/news/stock-market-news/eli-lilly-stock-may-move-66-on-oct-29-earnings-release-93CH-4966657)  
  <sub>Investing.com, 23 minutes ago</sub>  
  Investing.com -- Eli Lilly & Co. (NYSE:LLY) stock may move 6.6% when the company reports earnings on Oct. 29 before the market opens, according to options...
- [Lilly's new Virginia plant will create 650 jobs and about 1,800 construction jobs](https://www.stocktitan.net/news/LLY/lilly-breaks-ground-in-richmond-to-expand-american-manufacturing-of-1q4i14u4eqc8.html)  
  <sub>Stock Titan, 12 minutes ago</sub>  
  Eli Lilly and Company (LLY) broke ground on a $5 billion manufacturing facility in Goochland County, just west of Richmond, Virginia.
- [Eli Lilly (LLY) Grew Revenue 48% While Prices Fell, Can Volume Keep Winning?](https://finance.yahoo.com/healthcare/articles/eli-lilly-lly-grew-revenue-173137270.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Eli Lilly (NYSE:LLY) reports third-quarter results in about a week, and the split between volume and price matters more than the headline total.
- [LLY Stock Drops 1.01%, Golden Cross: Full Details](https://journalarta.com/en/2026/10/22/lly-stock-drops-1-01-golden-cross-formed-in-focus/)  
  <sub>JournalArta, 6 hours ago</sub>  
  On October 21, 2026: price 1270.75 USD, trend uptrend, RSI 66.1, support 1142.85, resistance 1283.66. technical analysis of lly stock.
- [RBC Capital Remains a Buy on Eli Lilly & Co (LLY)](https://www.theglobeandmail.com/investing/markets/stocks/LLY-N/pressreleases/8300031/rbc-capital-remains-a-buy-on-eli-lilly-co-lly/)  
  <sub>The Globe and Mail, 13 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [If You Invested $100 In Eli Lilly Stock 20 Years Ago, You Would Have This Much Today](https://www.benzinga.com/news/26/10/62512329/if-you-invested-100-eli-lilly-stock-20-years-ago-you-would-have-much-today)  
  <sub>Benzinga, 18 hours ago</sub>  
  Eli Lilly (NYSE:LLY) has outperformed the market over the past 20 years by 7.86% on an annualized basis producing an average annual return of 16.86%.
- [Eli Lilly (LLY) Could Be 14% Below Fair Value On Fresh Research And Omvoh Data](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-could-be-14-below-fair-value-on-fresh-research)  
  <sub>Simply Wall Street, 7 hours ago</sub>  
  Eli Lilly (LLY) just inked a research deal with Metis TechBio focused on lipid nanoparticle delivery and followed it with fresh Omvoh data in pediatric...
- [LLY Maintains by Leerink Partners -- Price Target Raised to $131](https://www.gurufocus.com/news/9134789/lly-maintains-by-leerink-partners-price-target-raised-to-1316)  
  <sub>GuruFocus, 19 hours ago</sub>  
  Eli Lilly Analyst Rating Update - %B %d, %Y On %B %d, %Y, Eli Lilly (LLY) received a maintained rating with a revised price target from Leerink Partners.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,306.69 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 1,200.44 (+8.9%), 50d 1,185.32 (+10.2%), 200d 1,084.11 (+20.5%); 50d above 200d
Momentum: RSI(14) 70.7 | MACD 30.134 vs signal 16.916 (histogram 13.218)
Returns: 1d +2.8% | 5d +4.4% | 1m +13.5% | 3m +9.3%
52-week range: 812.43 - 1,306.69 (now 100.0% of the way up)
Volatility: ATR(14) 36.47 (2.8% of price) | annualised 20d 29.1%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.17T
Valuation: trailing P/E 43.86 | forward P/E 27.67 | P/B 34.38 | PEG 1.14
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
Price target: mean 1,331.55 (+1.9% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-08 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-07 Morgan Stanley: main, Overweight -> Overweight
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
Institutional ownership: 85.3%
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

- [Microsoft (MSFT) Stock May Be 22% Undervalued After Maia 300 Unveiling](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-stock-may-22-042528043.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  Microsoft is back near the top of the market leaderboard. With the stock at about US$532.95, the key question for investors is whether that price can be...
- [How much MSFT stock does Microsoft CEO Satya Nadella actually own?](https://www.thestreet.com/personalities/how-much-msft-stock-does-microsoft-ceo-satya-nadella-actually-own)  
  <sub>TheStreet, 34 minutes ago</sub>  
  Satya Nadella transformed Microsoft into a Cloud and AI powerhouse. But compared with his predecessors, his stake in the company is surprisingly small.
- [MSFT 261021 530.00C (MSFT261021C530000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/MSFT261021C530000-US)  
  <sub>Moomoo, 9 hours ago</sub>  
  Track real-time MSFT 261021 530.00C (MSFT261021C530000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Microsoft Corporation (MSFT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MSFT/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Valuation Measures · Market Cap. 3.72T · Enterprise Value. 3.70T · Trailing P/E. 27.74 · Forward P/E. 25.13 · PEG Ratio (5yr expected). 1.62 · Price/Sales (ttm).
- [MSFT Stock Gets A Thumbs Up From Barclays – Firm Expects Quarter To Start Showing ‘More Differentiation’ In Software](https://stocktwits.com/news-articles/markets/equity/msft-stock-gets-a-thumbs-up-from-barclays-firm-expects-quarter-to-start-showing-more-differentiation-in-software/cZxBllTRBY4)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Microsoft is scheduled to report fiscal Q1 2027 results after the closing bell on Oct. 28, with analysts estimating earnings of $4.72 per share on revenue...
- [ETFs Are Net Sellers of Microsoft (MSFT) on Tuesday](https://finance.yahoo.com/markets/stocks/articles/etfs-net-sellers-microsoft-msft-110210080.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. Microsoft (MSFT) recorded $278.0 million in net ETF selling in Tuesday's session, even though more funds traded...
- [MSFT Oct 2026 450.000 call (MSFT261023C00450000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MSFT261023C00450000/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest MSFT Oct 2026 450.000 call (MSFT261023C00450000) stock quote, history, news and other vital information to help you with your stock trading...
- [MSFT 261021 520.00P (MSFT261021P520000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/MSFT261021P520000-US)  
  <sub>Moomoo, 12 hours ago</sub>  
  Track real-time MSFT 261021 520.00P (MSFT261021P520000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [MSFT Oct 2026 547.500 put (MSFT261019P00547500) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MSFT261019P00547500/)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Find the latest MSFT Oct 2026 547.500 put (MSFT261019P00547500) stock quote, history, news and other vital information to help you with your stock trading...
- [MSFT Oct 2026 495.000 put (MSFT261019P00495000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MSFT261019P00495000/)  
  <sub>Yahoo Finance UK, 6 hours ago</sub>  
  Find the latest MSFT Oct 2026 495.000 put (MSFT261019P00495000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 523.02 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 526.38 (-0.6%), 50d 507.91 (+3.0%), 200d 436.32 (+19.9%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD 8.274 vs signal 10.058 (histogram -1.784)
Returns: 1d -1.9% | 5d -3.0% | 1m +4.5% | 3m +37.0%
52-week range: 352.83 - 543.45 (now 89.3% of the way up)
Volatility: ATR(14) 11.22 (2.1% of price) | annualised 20d 22.9%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.88T
Valuation: trailing P/E 29.14 | forward P/E 22.06 | P/B 8.78 | PEG 1.62
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
  2026-06-30 beat by 10% | 2026-03-31 beat by 3% | 2025-06-30 beat by 6% | 2025-03-31 beat by 5%
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
Price target: mean 601.73 (+15.0% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-21 Guggenheim: reit, Buy -> Buy
  - 2026-10-20 BMO Capital: main, Outperform -> Outperform
  - 2026-10-19 Bernstein: main, Outperform -> Outperform
  - 2026-10-16 StoneX: main, Buy -> Buy
  - 2026-10-15 UBS: main, Buy -> Buy
  - 2026-10-15 Citigroup: main, Buy -> Buy
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

- [NVIDIA Corporation (NVDA) Remains a Key AI Growth Driver Despite Benchmark Headwinds](https://finance.yahoo.com/technology/ai/articles/nvidia-corporation-nvda-remains-key-142520422.html)  
  <sub>Yahoo Finance, 16 minutes ago</sub>  
  Polen Capital, an investment management company, released its “Polen Focus Growth Strategy” Q3 2026 investor letter. A copy of the letter can be downloaded...
- [Nvidia Stock Falls in a Case of Bad Timing Over Another Potential AI Investment](https://www.barrons.com/articles/nvidia-stock-ai-investment-7f0d45b5)  
  <sub>Barron's, 5 hours ago</sub>  
  stock was falling on Thursday alongside many others in the chip and AI space as the market continues to worry about the sustainability of spending on AI.
- [NVDA Stock’s 7-Day Losing Streak Sets Up Make-Or-Break AI Earnings Test: Retail Expects Yet Another Beat](https://stocktwits.com/news-articles/markets/equity/nvda-stock-s-7-day-losing-streak-sets-up-make-or-break-ai-earnings-test-retail-expects-yet-another-beat/cZYke4BRJFM)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Earnings per share is expected to come in at $0.82, compared to $0.53 in Q4 of 2025, implying an expectation of a rise of nearly 57%.
- [Market Decline: Nvidia (NVDA), Intel (INTC), and AMD (AMD) Stocks Drop](https://www.gurufocus.com/news/9136143/market-decline-nvidia-nvda-intel-intc-and-amd-amd-stocks-drop)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On October 22, 2026, recent earnings reports from major tech companies such as Tesla, Lam Research, and IBM have disappointed investors,...
- [Nvidia's Huang says scarce capital is holding back neocloud growth (NVDA:NASDAQ)](https://seekingalpha.com/news/4655787-nvidias-huang-says-scarce-capital-is-holding-back-neocloud-growth)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Nvidia (NVDA) CEO Jensen Huang said demand for specialized AI cloud providers is "off the charts," but limited access to capital is holding back their...
- [Wall Street Didn’t Expect This AI Stock to Become This Important](https://247wallst.com/investing/2026/10/22/wall-street-didnt-expect-this-ai-stock-to-become-this-important/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  NVIDIA (NVDA) earns a BUY rating with a $258 price target, roughly 21% upside, backed by six straight earnings beats and Q3 guidance of $108 billion.
- [NVDA 261023 190.00C (NVDA261023C190000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/NVDA261023C190000-US)  
  <sub>Moomoo, 11 hours ago</sub>  
  Track real-time NVDA 261023 190.00C (NVDA261023C190000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Missed NVIDIA's Rally? Here Is What Holders Saw](https://finance.yahoo.com/markets/stocks/articles/missed-nvidias-rally-holders-saw-031413419.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  If you only checked headlines this year, NVIDIA looked unstoppable as AI demand drove record data center revenue and fatter margins. For NVIDIA shareholders...
- [ARK Is Buying The AI Dip: Cathie Wood Adds NVDA Across Five Funds, Buys NET, AVGO Stocks Too](https://stocktwits.com/news-articles/markets/equity/cathie-woods-ark-invest-adds-nvda-net-stocks-spacex-merger-rumors/cZoZMKORJQJ)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Cathie Wood Bought The NVDA Dip Across Five Funds – Here's What Else ARK Bought And Sold · ARK Invest bought Nvidia across five funds on Monday after NVDA stock...
- [Nvidia continues impressive path at GTC Berlin, BNP Paribas says (NVDA:NASDAQ)](https://seekingalpha.com/news/4655976-nvidia-continues-impressive-path-at-gtc-berlin-bnp-paribas-says)  
  <sub>Seeking Alpha, 5 minutes ago</sub>  
  Nvidia (NVDA) held its GTC Berlin event earlier this week, and investment firm BNP Paribas walked away from the conference impressed at the size and speed...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 214.21 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 226.35 (-5.4%), 50d 222.81 (-3.9%), 200d 203.57 (+5.2%); 50d above 200d
Momentum: RSI(14) 40.6 | MACD -1.841 vs signal 0.072 (histogram -1.914)
Returns: 1d -3.5% | 5d -1.4% | 1m -5.0% | 3m +3.6%
52-week range: 165.17 - 239.24 (now 66.2% of the way up)
Volatility: ATR(14) 6.05 (2.8% of price) | annualised 20d 27.8%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.17T
Valuation: trailing P/E 27.08 | forward P/E 13.46 | P/B 22.59 | PEG 0.48
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
Earnings record, last 4 quarters: 4 beats
  2026-09-30 beat by 4% | 2026-09-30 beat by 4% | 2026-06-30 beat by 4% | 2026-06-30 beat by 4%
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
Consensus: strong_buy (mean 1.29 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 49 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.72 (+53.5% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-10-22 Needham: reit, Buy -> Buy
  - 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-09-29 Rosenblatt: main, Buy -> Buy
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
Institutional ownership: 71.4%
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

- [RY Nov 2026 185.000 put (RY261120P00185000) interactive stock chart](https://uk.finance.yahoo.com/quote/RY261120P00185000/chart/)  
  <sub>Yahoo Finance UK, 12 hours ago</sub>  
  Interactive chart for RY Nov 2026 185.000 put (RY261120P00185000) – analyse all of the data with a huge range of indicators.
- [Why Super Micro Computer Stock Popped Today](https://www.theglobeandmail.com/investing/markets/markets-news/motley/8288928/why-super-micro-computer-stock-popped-today/)  
  <sub>The Globe and Mail, 19 hours ago</sub>  
  Shares of Super Micro Computer (NASDAQ:SMCI) leaped on Wednesday after the server maker announced preliminary financial results.
- [RY Nov 2026 190.000 put (RY261120P00190000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/RY261120P00190000/chart/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Interactive Chart for RY Nov 2026 190.000 put (RY261120P00190000), analyze all the data with a huge range of indicators.
- [Royal Bank Of Canada $RY Stake Trimmed by Guardian Partners Inc.](https://www.marketbeat.com/instant-alerts/filing-royal-bank-of-canada-ry-stake-trimmed-by-guardian-partners-inc-2026-10-21/)  
  <sub>MarketBeat, 21 hours ago</sub>  
  Guardian Partners Inc. trimmed its position in shares of Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 4.6% in the 3rd quarter, according to the...
- [Robinhood (HOOD) stock is up, what you need to know](https://www.theglobeandmail.com/investing/markets/stocks/HOOD/pressreleases/8284556/robinhood-hood-stock-is-up-what-you-need-to-know/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Shares of financial services company Robinhood (NASDAQ:HOOD) jumped 3.9% in the afternoon session after Rosenblatt Securities initiated coverage on the...
- [Royal Bank of Canada stock pre-market at EUR 178.86: Canadian bank](https://www.ad-hoc-news.de/boerse/news/vorboerse/royal-bank-of-canada-stock-pre-market-at-eur-178-86-canadian-bank/70390491)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  The Canadian bank provides banking, wealth management, capital markets, insurance and investor services. At Lang & Schwarz the stock trades pre-market at...
- [Royal Bank of Canada (TSX:RY): Trending With Financial Readers?](https://kalkinemedia.com/ca/stocks/financial/royal-bank-of-canada-tsxry-trending-with-financial-readers)  
  <sub>Kalkine Media, 18 hours ago</sub>  
  Search Momentum Canada-market analysis of Royal Bank of Canada in financial stocks, linking the latest news with the next signals to watch.
- [Stock Market Midday, Oct. 21: Tech Gains Lift Nasdaq as SpaceX Soars](https://www.theglobeandmail.com/investing/markets/stocks/NFLX/pressreleases/8284368/stock-market-midday-oct-21-tech-gains-lift-nasdaq-as-spacex-soars/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Detailed price information for Netflix Inc (NFLX-Q) from The Globe and Mail including charting and trades.
- [Royal Bank of Canada (TSX:RY): Is Execution The Key?](https://kalkinemedia.com/ca/stocks/dividend/royal-bank-of-canada-tsxry-is-execution-the-key)  
  <sub>Kalkine Media, 18 hours ago</sub>  
  Execution Watch Canada-market analysis of Royal Bank of Canada in dividend stocks, linking the latest news with the next signals to watch.
- [Royal Bank of Canada stock: Fourth-quarter results set for December 3, 2026](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-fourth-quarter-results-set-for-december-3-2026/70385654)  
  <sub>AD HOC NEWS, 24 hours ago</sub>  
  RBC earned CAD 6.00 billion in third-quarter 2026, up 11.00 percent. Royal Bank of Canada stock costs EUR 179.13 at Lang & Schwarz on October 21, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 200.41 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 196.43 (+2.0%), 50d 202.56 (-1.1%), 200d 188.18 (+6.5%); 50d above 200d
Momentum: RSI(14) 53.7 | MACD -0.908 vs signal -2.111 (histogram 1.203)
Returns: 1d -0.8% | 5d +1.9% | 1m +0.5% | 3m -4.1%
52-week range: 145.41 - 217.87 (now 75.9% of the way up)
Volatility: ATR(14) 2.95 (1.5% of price) | annualised 20d 17.4%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 277.46B
Valuation: trailing P/E 17.52 | forward P/E 15.74 | P/B 2.91 | PEG 2.26
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
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2025-12-31 beat by 6%
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
Price target: mean 212.53 (+6.0% vs last close), range 185.49 - 233.75
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.4%
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

- [Should You Forget ExxonMobil and Buy Cameco Stock Instead?](https://finance.yahoo.com/markets/stocks/articles/forget-exxonmobil-buy-cameco-stock-110500261.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Energy stocks are getting more attention lately, and for good reason. Electricity demand is booming. On top of that, the ongoing conflict in Iran has put...
- [XOM vs. BP: Which Integrated Energy Giant Has the Edge?](https://www.zacks.com/stock/news/3013018/xom-vs-bp-which-integrated-energy-giant-has-the-edge)  
  <sub>Zacks Investment Research, 32 minutes ago</sub>  
  ExxonMobil outpaces BP in stock gains and balance sheet strength, but BP's lower valuation makes the choice between these oil giants worth a closer look.
- [Why Did XOM, CVX, MPC Stocks Surge To 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-xom-cvx-mpc-stocks-surge-to-52-week-highs-today/cZxq1SXRBua)  
  <sub>Stocktwits, 17 hours ago</sub>  
  XOM stock clocked an annual high of $179.30 on Monday during trading hours, before closing about 0.4% down. CVX stock surged to a 52-week high of $225.67,...
- [ExxonMobil Corporation $XOM Stock Purchased by Integrated Advisors Network LLC](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-stock-purchased-by-integrated-advisors-network-llc-2026-10-22/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Integrated Advisors Network LLC increased its stake in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 37.1% in the 3rd quarter, according to...
- [Fund Update: New $10.3M $XOM stock position opened by AXXCESS WEALTH MANAGEMENT, LLC](https://www.quiverquant.com/news/Fund+Update%3A+New+%2410.3M+%24XOM+stock+position+opened+by+AXXCESS+WEALTH+MANAGEMENT%2C+LLC)  
  <sub>Quiver Quantitative, 17 hours ago</sub>  
  AXXCESS WEALTH MANAGEMENT, LLC has opened a new $10.3M position in $XOM, per a new SEC 13F filing. T.
- [ExxonMobil stock hits all-time high at 180.26 USD By Investing.com](https://uk.investing.com/news/stock-market-news/exxonmobil-stock-hits-alltime-high-at-18026-usd-93CH-4925863)  
  <sub>Investing.com UK, 1 hour ago</sub>  
  ExxonMobil Holdings Corporation's stock reached an all-time high of 180.26 USD, marking a significant milestone for the energy giant. Over the past year,...
- [Is Exxon Mobil's Next Big Thing Already Here?](https://finance.yahoo.com/energy/articles/exxon-mobils-next-big-thing-004809263.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. Exxon Mobil (XOM) stock returned 63.1% over the past year, compared with...
- [ExxonMobil Corporation $XOM Stock: Nisa Investment Advisors LLC Reduces Stake](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-stock-nisa-investment-advisors-llc-reduces-stake-2026-10-22/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Nisa Investment Advisors LLC lowered its position in ExxonMobil Corporation (NYSE:XOM - Free Report) by 4.1% in the 3rd quarter, according to the company in...
- [EQT Gears Up to Report Q3 Earnings: What's in Store for the Stock?](https://finance.yahoo.com/markets/stocks/articles/eqt-gears-report-q3-earnings-113800446.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  EQT Corporation EQT is set to release third-quarter 2026 results on Oct. 27, after market close. The Zacks Consensus Estimate for earnings is pegged at 38...
- [Analysts Have Conflicting Sentiments on These Energy Companies: Antero Midstream (AM), Exxon Mobil (XOM) and Crescent Energy Company Class A (CRGY)](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/8320784/analysts-have-conflicting-sentiments-on-these-energy-companies-antero-midstream-am-exxon-mobil-xom-and-crescent-energy-company-class-a-crgy/)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Analysts have been eager to weigh in on the Energy sector with new ratings on Antero Midstream (AM), Exxon Mobil (XOM) and Crescent Energy Company Class A...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 176.03 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 169.61 (+3.8%), 50d 165.25 (+6.5%), 200d 152.82 (+15.2%); 50d above 200d
Momentum: RSI(14) 64.2 | MACD 4.226 vs signal 3.522 (histogram 0.704)
Returns: 1d -1.2% | 5d +0.8% | 1m +9.2% | 3m +12.2%
52-week range: 113.68 - 178.98 (now 95.5% of the way up)
Volatility: ATR(14) 3.68 (2.1% of price) | annualised 20d 18.3%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 723.82B
Valuation: trailing P/E 22.66 | forward P/E 14.34 | P/B 2.79 | PEG 1.38
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
Price target: mean 179.41 (+1.9% vs last close), range 142.00 - 206.00
Recent rating changes:
  - 2026-10-19 Barclays: main, Overweight -> Overweight
  - 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
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

## Whole-market funds

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral: no material macro surprise, flat fund flows, mixed technicals, and fundamentals are modestly positive but not decisive.

**Main reasons it gave:**
- Flat fund flows (0% change week/month)
- Technical indicators: price below 20‑day and 50‑day SMA, RSI 37.5, no decisive break
- Macro: upward sloping yield curve, VIX up, no policy surprise
- Wheat futures fell to 14‑week lows on Ukraine peace efforts
- Fund basics: 3.2% yield, 13.2% annual return over 3 years, 47% cash allocation

<details><summary><b>News</b> — score +0.00</summary>

- [U.S. wheat futures sink to 14-week lows on Ukraine peace efforts (WEAT:NYSEARCA)](https://seekingalpha.com/news/4655648-u-s-wheat-futures-sink-to-14-week-lows-on-ukraine-peace-efforts)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  CBOT wheat futures fell to 14-week lows following news that US special envoy Steve Witkoff met with Russia's President Putin in St. Petersburg to discuss a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.93 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 28.30 (-1.3%), 50d 28.51 (-2.0%), 200d 27.32 (+2.3%); 50d above 200d
Momentum: RSI(14) 37.5 | MACD -0.109 vs signal -0.071 (histogram -0.039)
Returns: 1d -0.7% | 5d -1.2% | 1m -2.2% | 3m -1.1%
52-week range: 25.44 - 29.49 (now 61.6% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.3%
Volume: 1.55x the 20-day average
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
Three-year record: +13.2% a year | beta to the market 0.35
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 27.60M | fund size: 771.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Given the lack of a macro catalyst, neutral technicals, flat fund flows, and mixed fundamental signals, a neutral stance is appropriate.

**Main reasons it gave:**
- No policy or rate surprise; macro data in line with expectations
- Technical indicators bullish but low volume, no decisive break
- Fund flows flat, indicating no net demand shift
- Fundamental signals mixed: oil inventory draw bullish vs EIA price outlook bearish, net neutral

<details><summary><b>News</b> — score +0.00</summary>

- [Is Sticky Inflation Here to Stay? ETF Areas to Watch](https://www.tradingview.com/news/zacks:000337bb8094b:0-is-sticky-inflation-here-to-stay-etf-areas-to-watch/)  
  <sub>TradingView, 4 hours ago</sub>  
  Inflation does not usually hit your wallet all at once. Instead, it gradually eats into your monthly budget. For much of 2026, rising gasoline prices,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.49 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 32.98 (+1.6%), 50d 32.30 (+3.7%), 200d 28.91 (+15.9%); 50d above 200d
Momentum: RSI(14) 60.2 | MACD 0.380 vs signal 0.378 (histogram 0.002)
Returns: 1d -0.0% | 5d +0.6% | 1m +1.9% | 3m +11.3%
52-week range: 22.36 - 33.74 (now 97.8% of the way up)
Volatility: ATR(14) 0.46 (1.4% of price) | annualised 20d 14.1%
Volume: 0.23x the 20-day average
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
Three-year record: +15.1% a year | beta to the market 1.05
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
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 111.40M | fund size: 3.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals show downtrend but no decisive break, fundamentals are solid, while recent outflows signal bearish demand.

**Main reasons it gave:**
- 1‑month outflows of -11.3% (-$1.65B) indicating bearish demand
- Price at 91.57 below 50‑day SMA (92.96) and 200‑day SMA (95.09), downtrend
- US Treasury yields slipped modestly (10‑yr -0.07%) and VIX rose 2.8 points, no policy surprise
- Fund yield 5.4% and three‑year record +10% annualized, solid fundamentals

<details><summary><b>News</b> — score +0.00</summary>

- [(EMB) Risk Channels and Responsive Allocation](https://news.stocktradersdaily.com/news_release/23/EMB_Risk_Channels_and_Responsive_Allocation_102126110802_1792638482.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Price-action only: Ishares J.p. Morgan Usd Emerging Markets Bond Etf (EMB) movements set the tone for institutional models. (EMB) Risk Channels and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.57 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 91.12 (+0.5%), 50d 92.96 (-1.5%), 200d 95.09 (-3.7%); 50d below 200d
Momentum: RSI(14) 46.7 | MACD -0.408 vs signal -0.584 (histogram 0.176)
Returns: 1d +0.1% | 5d -0.3% | 1m -1.2% | 3m -3.2%
52-week range: 90.14 - 97.74 (now 18.8% of the way up)
Volatility: ATR(14) 0.50 (0.6% of price) | annualised 20d 6.3%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.5%, BB 25.3%, B 19.5%, A 17.7% | US government debt 88.0%
Three-year record: +10.0% a year | beta to the market 1.10
Cost and size: expense ratio 0.39% | net assets 12.93B
What it is made of: Bonds 99.1%, Cash 0.9%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.7%
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
Share count change: 1 week: -0.2% (-29.02M) over 7d | 1 month: -11.3% (-1.65B) over 30d
Shares outstanding: 141.89M | fund size: 12.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, stable fundamentals, slight reduction in net short but still net short.

**Main reasons it gave:**
- Net short on 10Y note decreased by 0.6% (POSITIONING)
- Fund basics unchanged: AA credit quality, 4.1% yield (FUND BASICS)
- Technicals show price above 20‑day SMA, RSI 60, no decisive break (TECHNICALS)
- Macro: yields down 0.07% this week, no rate surprise (MACRO)

<details><summary><b>News</b> — score +0.00</summary>

- [Gabelli Series K Preferred: Duration Pain Creates An Opportunity (NYSE:GDV.PR.K)](https://seekingalpha.com/article/4956182-gabelli-series-k-preferred-duration-pain-creates-an-opportunity?source=generic_rss)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Gabelli Dividend & Income Trust Series K Preferred remains attractive despite a -4% YTD total return and heightened rate sensitivity. GDV.PR.
- [Daily ETF Flows: SOXX On Top](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-soxx-top)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 20, 2026.
- [The Government Spends About $5.5 Billion a Day More Than It Takes In. The Debt Has Doubled in 10 Years. Jaime Dimon This the Situation Could Get Much Worse.](https://247wallst.com/investing/2026/10/21/the-government-spends-about-5-5-billion-a-day-more-than-it-takes-in-the-debt-has-doubled-in-10-years-jaime-dimon-this-the-situation-could-get-much-worse/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Washington borrows over a trillion dollars a year just to pay interest on what it already owes, and two of Wall Street's most powerful executives are...
- [Form 424B3 GOLDMAN SACHS GROUP INC](https://www.streetinsider.com/SEC+Filings/Form+424B3+GOLDMAN+SACHS+GROUP+INC/27217232.html)  
  <sub>StreetInsider, 18 hours ago</sub>  
  October 2026 BlackRock® Dynamic Factor Index Supplement Addendum to the BlackRock® Dynamic Factor Index Supplement, the Prospectus Supplement and the...
- [Opus Genetics Secures FDA Approval For Eye Drops – Set To Receive Milestone Payment](https://stocktwits.com/news-articles/markets/equity/opus-genetics-secures-fda-approval-for-reading-vision-eye-drops-viatris-holds-us-commercial-rights/cZxKBzoRBsx)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Ryzumvi contains phentolamine ophthalmic solution 0.75%, which reduces pupil size to improve near vision without affecting longer-distance vision.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.92 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 89.68 (+1.4%), 50d 91.11 (-0.2%), 200d 94.01 (-3.3%); 50d below 200d
Momentum: RSI(14) 60.1 | MACD -0.135 vs signal -0.383 (histogram 0.248)
Returns: 1d +0.8% | 5d +0.6% | 1m +0.8% | 3m -2.3%
52-week range: 88.92 - 97.99 (now 22.0% of the way up)
Volatility: ATR(14) 0.50 (0.6% of price) | annualised 20d 5.1%
Volume: 0.31x the 20-day average
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
Three-year record: +4.1% a year | beta to the market 1.16
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 37.9% of open interest (5,819,512 contracts)
Change on the week: -0.6% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 146.00M | fund size: 13.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 2% of fund, weighted price target +19.2% above current price
- CFTC positioning: net short 20.6% of open interest, short position increased 4.2% week over week
- Technicals: price below 20‑day SMA (-0.9%) and 50‑day SMA (-4.1%), RSI 42.1, recent down returns
- Macro: Fed rate unchanged, yields down slightly, VIX up 2.8 points, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [How to Buy iShares Russell 2000 ETF (IWM)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-iwm-etf/)  
  <sub>The Motley Fool, 11 hours ago</sub>  
  The iShares Russell 2000 ETF has a 0.19% expense ratio. In other words, if you invested $10,000 in the fund, $19 would go toward fees, while the remaining...
- [iShares Russell 2000 (IWM) Buys $3.6 Million More MiniMed on Oct. 20](https://finance.yahoo.com/markets/stocks/articles/ishares-russell-2000-iwm-buys-110456374.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  The ETF added $153.2 million in gross trades Tuesday, netting $8.2 million, with 1868 positions raised and 35 trimmed.
- [Webull to Introduce Extended-Hours Options Trading, Expanding Access Beyond the Regular Market Session](https://www.tradingview.com/news/prnewswire:5e0da1e8a24f2:0-webull-to-introduce-extended-hours-options-trading-expanding-access-beyond-the-regular-market-session/)  
  <sub>TradingView, 2 hours ago</sub>  
  New trading hours will enable Webull users to trade select stock and ETF options around earnings announcements and other market-moving events during pre-...
- [How Might Stock, Bond, And Oil Markets React To The Fed's Rate Decision](https://seekingalpha.com/article/4956068-how-might-stock-bond-and-oil-markets-react-fed-rate-decision)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The Fed's October 2026 rate decision is expected to keep rates steady, with markets now seeing only a 15% chance of a hike. Read the full analysis here.
- [Inside CAYN: The Next Calamos Autocallable ETF](https://www.etftrends.com/alternatives-content-hub/cayn-calamos-autocallable-etf/)  
  <sub>ETF Trends, 21 hours ago</sub>  
  Calamos is adding a new autocallable ETF to its lineup, and this fund uses a 'least-of' strategy to tackle autocallable income.
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...
- [IWM 261021 284.00C (IWM261021C284000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/IWM261021C284000-US?global_content=%7B%22promote_id%22%3A11927,%22sub_promote_id%22%3A51%7D)  
  <sub>Moomoo, 12 hours ago</sub>  
  iShares Russell 2000 ETF (IWM) News. Options Whale Alert: $2.41M Bearish Long Put Opened on $IWM. $IWM closed up 0.25% at $276.48.
- [Webull launches extended-hours options trading for U.S. customers](https://www.streetinsider.com/Corporate+News/Webull+launches+extended-hours+options+trading+for+U.S.+customers/27220131.html)  
  <sub>StreetInsider, 2 hours ago</sub>  
  Webull (NASDAQ: BULL) has introduced extended-hours trading for select single-stock and ETF options, allowing eligible U.S. customers to trade outside the...
- [FNDA: Small Caps Have Fallen, But Earnings Expectations Are Still Too High (NYSEARCA:FNDA)](https://seekingalpha.com/article/4956352-fnda-small-caps-fallen-earnings-expectations-still-too-high)  
  <sub>Seeking Alpha, 60 minutes ago</sub>  
  Schwab Fundamental U.S. Small Company ETF is downgraded to Hold due to declining EPS growth and price momentum. Read more on FNDA ETF here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 275.05 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 277.42 (-0.9%), 50d 286.94 (-4.1%), 200d 278.12 (-1.1%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD -3.428 vs signal -3.745 (histogram 0.317)
Returns: 1d -0.5% | 5d -0.0% | 1m -2.4% | 3m -5.5%
52-week range: 229.11 - 305.09 (now 60.5% of the way up)
Volatility: ATR(14) 3.70 (1.3% of price) | annualised 20d 14.7%
Volume: 0.34x the 20-day average
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
Three-year record: +19.7% a year | beta to the market 1.27
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.86 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.2% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-21 Truist Securities: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 20.6% of open interest (444,784 contracts)
Change on the week: +4.2% of open interest
Crowding: 22% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 281.05M | fund size: 77.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material catalyst in news, technicals, macro, or flows; fund fundamentals unchanged.

**Main reasons it gave:**
- No news found in past 24 hours
- Technicals: price below 50‑day and 200‑day SMA, no decisive break on volume
- Fund flows flat over 1‑month, indicating no net demand
- Macro: Treasury yields unchanged, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 103.94 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 102.65 (+1.3%), 50d 104.32 (-0.4%), 200d 107.88 (-3.6%); 50d below 200d
Momentum: RSI(14) 57.4 | MACD -0.223 vs signal -0.483 (histogram 0.259)
Returns: 1d +0.7% | 5d +0.4% | 1m +0.1% | 3m -2.2%
52-week range: 101.83 - 112.92 (now 19.1% of the way up)
Volatility: ATR(14) 0.63 (0.6% of price) | annualised 20d 5.7%
Volume: 0.36x the 20-day average
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
Three-year record: +6.2% a year | beta to the market 1.35
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 293.50M | fund size: 30.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise (rates unchanged, inflation near expectations)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs; RSI 59, MACD positive but no decisive breakout
- Analyst coverage thin (1.4% weight) with slight bearish price target (-6.6%)
- CFTC positioning net short 21.2% with small increase (+0.3%)

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) Sells $0.7 Million of Moderna on Tuesday](https://finance.yahoo.com/markets/stocks/articles/invesco-p-500-equal-weight-110449305.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. Invesco S&P 500 Equal Weight ETF (RSP) was alone in selling on Tuesday, Oct. 20, with no ETFs buying.
- [Here Are 5 ETFs Retirees Use to Get Paid Without Leaning on the Magnificent Seven](https://247wallst.com/investing/etf/2026/10/21/here-are-5-etfs-retirees-use-to-get-paid-without-leaning-on-the-magnificent-seven/)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  Most broad index funds quietly hand enormous weight to the same seven companies, which means retirees collecting dividends may be more exposed to big tech...
- [AI Stocks Could Crash in 2027: 3 Ways to Protect Your Money](https://beincrypto.com/ai-bubble-crash-2027-protect-portfolio/)  
  <sub>BeInCrypto, 5 hours ago</sub>  
  If the AI bubble bursts in 2027 and the stock market crashes, how should investors prepare? What is the best way to stay safe while still increasing your...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 216.33 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 212.30 (+1.9%), 50d 215.44 (+0.4%), 200d 207.16 (+4.4%); 50d above 200d
Momentum: RSI(14) 59.1 | MACD 0.489 vs signal -0.264 (histogram 0.753)
Returns: 1d -0.1% | 5d +0.6% | 1m +2.4% | 3m +1.3%
52-week range: 182.18 - 222.77 (now 84.1% of the way up)
Volatility: ATR(14) 1.92 (0.9% of price) | annualised 20d 9.7%
Volume: 0.58x the 20-day average
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
Three-year record: +18.2% a year | beta to the market 0.84
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

<details><summary><b>What analysts and big funds say</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.15</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.6% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-21 TD Cowen: main, Hold -> Hold
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-19 Canaccord Genuity: main, Hold -> Hold
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 21.2% of open interest (1,931,607 contracts)
Change on the week: +0.3% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 155.55M | fund size: 33.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals are flat, positioning shows a slight reduction in net short pressure, and fund flows are flat.

**Main reasons it gave:**
- Positioning: net short on 2‑yr note fell 2% of OI this week, reducing bearish pressure
- Technical: price just above 20‑day SMA, MACD line above signal, RSI 59.4 (neutral momentum)
- Macro: Treasury yields slipped ~0.07% across the curve this week, no policy surprise
- Fund flows: share count unchanged over past month, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [The Government Spends About $5.5 Billion a Day More Than It Takes In. The Debt Has Doubled in 10 Years. Jaime Dimon This the Situation Could Get Much Worse.](https://247wallst.com/investing/2026/10/21/the-government-spends-about-5-5-billion-a-day-more-than-it-takes-in-the-debt-has-doubled-in-10-years-jaime-dimon-this-the-situation-could-get-much-worse/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Washington borrows over a trillion dollars a year just to pay interest on what it already owes, and two of Wall Street's most powerful executives are...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.45 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 81.21 (+0.3%), 50d 81.48 (-0.0%), 200d 82.15 (-0.9%); 50d below 200d
Momentum: RSI(14) 59.4 | MACD -0.018 vs signal -0.066 (histogram 0.047)
Returns: 1d +0.2% | 5d +0.2% | 1m +0.4% | 3m -0.5%
52-week range: 81.05 - 83.18 (now 18.7% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.3%
Volume: 0.26x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 30.0% of open interest (4,554,153 contracts)
Change on the week: -2.0% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 209.30M | fund size: 17.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, modest technical bullishness offset by bearish positioning, solid fundamentals.

**Main reasons it gave:**
- Fed target unchanged at 4.00% (no policy surprise)
- Large speculators net short 37.9% of open interest (bearish positioning)
- Price above 20‑day and 50‑day SMA but below 200‑day SMA (mixed trend)
- Fund yield 4.7% with AA credit quality (solid fundamentals)

<details><summary><b>News</b> — score +0.00</summary>

- [Tax-Busting Trades Fuel Rush for Muni ETFs After Fall Selloff](https://www.bloomberg.com/news/articles/2026-10-21/tax-busting-trades-fuel-rush-for-muni-etfs-after-fall-selloff?srnd=homepage-americas)  
  <sub>Bloomberg.com, 22 hours ago</sub>  
  Owners of municipal bonds usually aren't happy to see their holdings go into the red, but this year, they're taking full advantage of negative returns in...
- [VOO vs. VOOG: One Vanguard ETF Offers 27% Upside, but Comes with Higher Risk](https://www.tipranks.com/news/voo-vs-voog-one-vanguard-etf-offers-27-upside-but-comes-with-higher-risk)  
  <sub>TipRanks, 51 minutes ago</sub>  
  Vanguard SP 500 ETF ($VOO) and Vanguard SP 500 Growth ETF ($VOOG) both track the SP 500 ($SPX) in different ways. According to TipRanks' ETF Analyst ...
- [AI Spending Now Reaches Chip Manufacturers: The Pictet AI & Automation ETF (PBOT) After One Year](https://www.tipranks.com/news/ai-spending-now-reaches-chip-manufacturers-the-pictet-ai-automation-etf-pbot-after-one-year)  
  <sub>TipRanks, 4 hours ago</sub>  
  Global sales of semiconductor manufacturing equipment are forecast to reach a record $165.9 billion in 2026, up 23.2% from a year earlier, according to SEMI...
- [‘It’s definitely a bubble’: Paul Musson warns AI investors on ‘Zero Sum’](https://invezz.com/pk/news/2026/10/21/its-definitely-a-bubble-paul-musson-warns-ai-investors-on-zero-sum/)  
  <sub>Invezz, 22 hours ago</sub>  
  The US national debt has climbed to $40 trillion, but the bigger question is what decades of borrowing, low interest rates, and rising asset prices have...
- [Bitcoin Rally Meets ETF Chill: BITO Sees Outflows as BTC Technicals Flash ‘Strong Buy’](https://www.tipranks.com/news/cryptocurrencies/bitcoin-rally-meets-etf-chill-bito-sees-outflows-as-btc-technicals-flash-strong-buy)  
  <sub>TipRanks, 7 hours ago</sub>  
  Bitcoin ETF investors tap the brakes as ProShares Bitcoin Strategy ETF (BITO) posts fresh outflows. The fund saw $3.30 million exit on October 16, 2026,...
- [3 ETFs with More Than 14% Upside Potential, According to the AI Analyst](https://www.tipranks.com/news/3-etfs-with-more-than-14-upside-potential-according-to-the-ai-analyst)  
  <sub>TipRanks, 18 hours ago</sub>  
  TipRanks' ETFAIAnalyst expects Vanguard Mega Cap Growth ETF ($MGK), iShares Nasdaq 100 ETF ($IQQ), and First Trust Expanded Technology ETF ($XPND) to de...
- [3 Best Dividend ETFs with Yields Above 10%](https://www.tipranks.com/news/3-best-dividend-etfs-with-yields-above-10)  
  <sub>TipRanks, 24 hours ago</sub>  
  Dividend ETFs are popular with investors seeking income, but some offer higher yields than others. According to TipRanks' High Dividend Yield ETFs tool,...
- [3 Best Vanguard ETFs with 25%+ Upside](https://www.tipranks.com/news/3-best-vanguard-etfs-with-25-upside)  
  <sub>TipRanks, 23 hours ago</sub>  
  Vanguard ETFs are popular for long-term investing, and a few funds now stand out for their growth potential. Based on TipRanks' Best Vanguard ETFs tool,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 106.01 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 104.67 (+1.3%), 50d 105.78 (+0.2%), 200d 108.97 (-2.7%); 50d below 200d
Momentum: RSI(14) 63.1 | MACD 0.009 vs signal -0.242 (histogram 0.251)
Returns: 1d +0.4% | 5d +0.7% | 1m +1.1% | 3m -1.4%
52-week range: 103.98 - 112.20 (now 24.7% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 3.6%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 100.0%
Three-year record: +4.3% a year | beta to the market 0.71
Cost and size: expense ratio 0.18% | net assets 14.23B
What it is made of: Bonds 100.0%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 37.9% of open interest (5,819,512 contracts)
Change on the week: -0.6% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 177.70M | fund size: 18.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro news and technicals provide mixed signals, and positioning shows modest bearish bias.

**Main reasons it gave:**
- AI stock anxiety sparked bond buying, 10‑yr Treasury yield down 0.07% this week
- Weak jobs report cooled rate‑hike expectations, Treasury yields fell across the curve
- CFTC data shows large speculators net short 29.8% of open interest, up 0.4% week‑over‑week
- Price above 20‑day (78.65) and 50‑day (80.57) SMAs but below 200‑day SMA (84.81), with volume at 0.32× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [AI doubts drive bond rally as Meta, IBM flash warning signs (TLT:NASDAQ)](https://seekingalpha.com/news/4655965-ai-doubts-spark-bond-rally-as-meta-ibm-flash-warning-signs)  
  <sub>Seeking Alpha, 26 minutes ago</sub>  
  AI stock anxiety sparks bond buying as Treasury yields fall.
- [TLT 261021 90.00C (TLT261021C90000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021C90000-US)  
  <sub>Moomoo, 11 hours ago</sub>  
  Track real-time TLT 261021 90.00C (TLT261021C90000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [How to Buy iShares Russell 2000 ETF (IWM)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-iwm-etf/)  
  <sub>The Motley Fool, 11 hours ago</sub>  
  The iShares Russell 2000 ETF (IWM +0.25%) is a top exchange-traded fund (ETF) for investors seeking broad exposure to small-cap stocks. The ETF tracks the...
- [S&P 500, Nasdaq, Dow End Week Higher As Weak Jobs Report Cools Rate Hike Bets — NVDA, BA, SPCX, RIVN, APLD In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-end-week-higher-as-weak-jobs-report-cools-rate-hike-bets-nvda-ba-spcx-rivn-apld-in-focus/cZDjq3URBKF)  
  <sub>Stocktwits, 14 hours ago</sub>  
  U.S. stock indices ended higher on Friday as employment data showed the economy added fewer jobs than expected, easing fears of an October rate hike.
- [The Government Spends About $5.5 Billion a Day More Than It Takes In. The Debt Has Doubled in 10 Years. Jaime Dimon This the Situation Could Get Much Worse.](https://247wallst.com/investing/2026/10/21/the-government-spends-about-5-5-billion-a-day-more-than-it-takes-in-the-debt-has-doubled-in-10-years-jaime-dimon-this-the-situation-could-get-much-worse/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Washington borrows over a trillion dollars a year just to pay interest on what it already owes, and two of Wall Street's most powerful executives are...
- [TLT 261021 74.00C (TLT261021C74000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021C74000-US)  
  <sub>Moomoo, 21 hours ago</sub>  
  Track real-time TLT 261021 74.00C (TLT261021C74000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [TLT 261021 77.50P (TLT261021P77500) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021P77500-US)  
  <sub>Moomoo, 21 hours ago</sub>  
  Track real-time TLT 261021 77.50P (TLT261021P77500) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [TLT 261021 95.00P (TLT261021P95000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021P95000-US?search_track_info=)  
  <sub>Moomoo, 23 hours ago</sub>  
  Track real-time TLT 261021 95.00P (TLT261021P95000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [TLT 261021 93.00C (TLT261021C93000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/TLT261021C93000-US?chain_id=Name1K9-3FXPhg.1kgajc0)  
  <sub>Moomoo, 23 hours ago</sub>  
  Track real-time TLT 261021 93.00C (TLT261021C93000) stock options chain data and pricing information and news on moomoo App for your options trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.25 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 78.65 (+3.3%), 50d 80.57 (+0.8%), 200d 84.81 (-4.2%); 50d below 200d
Momentum: RSI(14) 63.8 | MACD -0.022 vs signal -0.485 (histogram 0.463)
Returns: 1d +1.3% | 5d +1.6% | 1m +1.0% | 3m -2.4%
52-week range: 77.11 - 92.06 (now 27.7% of the way up)
Volatility: ATR(14) 0.83 (1.0% of price) | annualised 20d 10.1%
Volume: 0.32x the 20-day average
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
Three-year record: +3.0% a year | beta to the market 2.31
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 29.8% of open interest (2,397,995 contracts)
Change on the week: +0.4% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 109.70M | fund size: 8.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, modest bullish positioning, strong inflows but no decisive technical breakout.

**Main reasons it gave:**
- Dollar index down 0.13% on the week, indicating slight USD weakness
- Large speculators net long 4% of open interest, up 2.3% week, showing modest bullish positioning
- Fund share count up 41.7% over the month, indicating strong inflows
- Price above 20‑, 50‑ and 200‑day SMAs but volume only 0.29× 20‑day average, lacking strong momentum

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.96 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 28.93 (+0.1%), 50d 28.47 (+1.7%), 200d 27.87 (+3.9%); 50d above 200d
Momentum: RSI(14) 57.9 | MACD 0.136 vs signal 0.170 (histogram -0.034)
Returns: 1d +0.1% | 5d -0.1% | 1m +1.1% | 3m +1.3%
52-week range: 26.47 - 29.13 (now 93.6% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.2%
Volume: 0.29x the 20-day average
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
Three-year record: +3.7% a year | beta to the market -11.39
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 4.0% of open interest (51,816 contracts)
Change on the week: +2.3% of open interest
Crowding: 85% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.8% (3.26M) over 7d | 1 month: +41.7% (127.07M) over 30d
Shares outstanding: 14.91M | fund size: 431.87M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to modest bullish analyst view offset by thin coverage, slight bullish shift in positioning, but technicals show downtrend and no macro surprise.

**Main reasons it gave:**
- Analyst coverage thin (12.1% of fund) with modest buy bias (+18.8% price target)
- CFTC positioning net short 0.3% of OI, short positions fell -0.4% week
- Technical trend below 20d, 50d, 200d SMAs, low volume, no decisive break
- Macro: yields down slightly, VIX up, no policy or data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [GSK’s Hepatitis B Drug Was Approved Days Early, But The Harder Question Is Whether the Cure Lasts](https://www.moomoo.com/community/feed/gsk-s-hepatitis-b-drug-was-approved-days-early-but-117479932428294)  
  <sub>Moomoo, 22 hours ago</sub>  
  A chance to stop treatment” is the headline, but the numbers behind it show how narrow that chance still is. The FDA approved GSK's Hibsago, chemical...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 86.62 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 86.69 (-0.1%), 50d 89.18 (-2.9%), 200d 87.82 (-1.4%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD -0.548 vs signal -0.793 (histogram 0.245)
Returns: 1d -1.1% | 5d -0.7% | 1m -1.6% | 3m -2.0%
52-week range: 77.90 - 93.19 (now 57.0% of the way up)
Volatility: ATR(14) 0.91 (1.1% of price) | annualised 20d 13.2%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.6% | hold 32.4% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.8% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, SHEL.L, NOVN.SW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 0.3% of open interest (480,891 contracts)
Change on the week: -0.4% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 282.09M | fund size: 24.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro catalyst, technicals show oversold conditions but no decisive break, analyst coverage is thin despite bullish ratings, and positioning shows a slight bearish shift.

**Main reasons it gave:**
- No macro surprise: yields down 0.07% on 10‑year, inflation 3.7% near target
- Technical oversold RSI 29.7 but price below 20‑day, 50‑day, and 200‑day SMAs, no decisive break
- Analyst coverage thin: only 23.5% of fund weight, despite 100% buy rating and +50% price target
- Positioning net long 2.8% of open interest, down 1.5% week‑over‑week

<details><summary><b>News</b> — score +0.00</summary>

- [Cheapest international stock ETFs in 2026, compared](https://qz.com/cheapest-international-stock-etfs)  
  <sub>qz.com, 21 hours ago</sub>  
  These index funds track developed and emerging markets at some of the lowest annual costs available today.
- [ETFs Investing in Sany Heavy Industry Co., Ltd. Class H Stocks](https://www.tradingview.com/symbols/HKEX-6031/etfs/)  
  <sub>TradingView, 6 hours ago</sub>  
  Explore funds investing in 6031 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 56.83 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 59.19 (-4.0%), 50d 59.89 (-5.1%), 200d 58.31 (-2.5%); 50d above 200d
Momentum: RSI(14) 29.7 | MACD -0.608 vs signal -0.373 (histogram -0.235)
Returns: 1d -2.3% | 5d -3.3% | 1m -5.5% | 3m -1.7%
52-week range: 52.42 - 61.44 (now 48.9% of the way up)
Volatility: ATR(14) 0.67 (1.2% of price) | annualised 20d 15.2%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 16.13 | P/B 2.13 | P/S 1.85 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +18.7% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 164.66B
What it is made of: Stocks 95.8%, Cash 4.0%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 15.7%, Tencent Holdings Ltd 2.8%, Alibaba Group Holding Ltd Ordinary Shares 2.1%, MediaTek Inc 1.9%, Delta Electronics Inc 0.9%
Sector mix: Technology 33.8%, Financial services 19.5%, Consumer cyclical 9.3%, Industrials 7.5%
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
Rolled up from the 5 largest holdings, 23.5% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +50.4% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 2.8% of open interest (1,042,945 contracts)
Change on the week: -1.5% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 1.42B | fund size: 80.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [HINC ETF Holdings List — NASDAQ:HINC](https://www.tradingview.com/symbols/NASDAQ-HINC/holdings/)  
  <sub>TradingView, 2 hours ago</sub>  
  Explore Hartford High Yield ETF holdings with weight, market value, and other helpful data to make more informed decisions for HINC trading.
- [Daily ETF Flows: SOXX On Top](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-soxx-top)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 20, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 76.97 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 77.12 (-0.2%), 50d 78.33 (-1.7%), 200d 79.63 (-3.3%); 50d below 200d
Momentum: RSI(14) 36.6 | MACD -0.392 vs signal -0.446 (histogram 0.054)
Returns: 1d -0.0% | 5d -0.2% | 1m -1.4% | 3m -2.8%
52-week range: 76.81 - 81.28 (now 3.7% of the way up)
Volatility: ATR(14) 0.29 (0.4% of price) | annualised 20d 3.8%
Volume: 0.21x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 195.60M | fund size: 15.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, no decisive technical break, and mixed flow and analyst signals.

**Main reasons it gave:**
- US Treasury yields unchanged (3‑month -0.05% week) and inflation 3.7% near expectations – no macro surprise
- Technical indicators: price below 20‑day/50‑day/200‑day SMAs, RSI 34.7, but low volume and no decisive break
- Fund flows: net outflow of -6.7% over the past 30 days indicating bearish sentiment
- Analyst view: 100% buy rating (mean 1.66) with +35.4% price target for top holdings covering 49.4% of the fund

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 84.79 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 87.36 (-2.9%), 50d 91.20 (-7.0%), 200d 92.31 (-8.2%); 50d below 200d
Momentum: RSI(14) 34.7 | MACD -1.306 vs signal -1.298 (histogram -0.007)
Returns: 1d -3.0% | 5d -3.5% | 1m -6.9% | 3m -9.0%
52-week range: 70.58 - 102.94 (now 43.9% of the way up)
Volatility: ATR(14) 1.77 (2.1% of price) | annualised 20d 29.7%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.4% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-13 Citigroup: main, Neutral -> Neutral
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-09-01 JP Morgan: main, Neutral -> Neutral
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
Direction: money going out (1 month)
Share count change: 1 week: +2.0% (13.69M) over 7d | 1 month: -6.7% (-49.91M) over 30d
Shares outstanding: 8.23M | fund size: 697.46M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, mixed technicals, modest analyst optimism, and recent outflows offset fundamentals

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with +3.6% price target
- Fund flows: 1% net outflows in the past month
- Technicals: MACD bullish cross but price below 20‑day SMA and low volume
- Fundamentals: Low P/E (13.2) and strong 3‑year annualized return (+39.8%)

<details><summary><b>News</b> — score +0.00</summary>

- [Price-Driven Insight from (EPOL) for Rule-Based Strategy](https://news.stocktradersdaily.com/news_release/21/Price-Driven_Insight_from_EPOL_for_Rule-Based_Strategy_102226121602_1792642562.html)  
  <sub>Stock Traders Daily, 15 hours ago</sub>  
  Key findings for Ishares Msci Poland Etf (NASDAQ: EPOL). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias; Support is being tested.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 44.03 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 44.10 (-0.2%), 50d 44.40 (-0.8%), 200d 40.14 (+9.7%); 50d above 200d
Momentum: RSI(14) 48.4 | MACD 0.023 vs signal -0.023 (histogram 0.047)
Returns: 1d -2.3% | 5d -0.9% | 1m -1.2% | 3m +7.6%
52-week range: 32.56 - 45.76 (now 86.9% of the way up)
Volatility: ATR(14) 0.69 (1.6% of price) | annualised 20d 21.0%
Volume: 0.23x the 20-day average
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
Three-year record: +39.8% a year | beta to the market 0.64
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.6% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
Recent rating changes among them: none reported
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
Share count change: 1 week: -0.7% (-5.59M) over 7d | 1 month: -1.0% (-8.75M) over 30d
Shares outstanding: 18.89M | fund size: 831.59M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, modest bearish analyst view, and technicals are mixed without decisive break.

**Main reasons it gave:**
- Analyst view: 40.5% sell, weighted price target -6% (bearish)
- Fund flows flat: 0% change over 1 week and 1 month
- Technicals: price above 20‑day SMA (+1.4%), MACD positive, but volume 0.41× 20‑day average
- Macro: no surprise data; yields down modestly, VIX up 2.8 points

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.97 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 28.58 (+1.4%), 50d 29.17 (-0.7%), 200d 28.80 (+0.6%); 50d above 200d
Momentum: RSI(14) 52.8 | MACD 0.006 vs signal -0.106 (histogram 0.112)
Returns: 1d -0.9% | 5d +0.6% | 1m +2.2% | 3m +0.9%
52-week range: 24.95 - 30.43 (now 73.4% of the way up)
Volatility: ATR(14) 0.32 (1.1% of price) | annualised 20d 11.7%
Volume: 0.41x the 20-day average
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
Three-year record: +16.1% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.30</summary>

```text
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.0% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 63.60M | fund size: 1.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, modest analyst optimism, technicals lack decisive breakout.

**Main reasons it gave:**
- Fund flows flat: 0% change week and month
- Technicals: price above 20‑day (+2%) and 50‑day (+0.2%) SMAs, near 52‑week high, low volume, RSI 55, no decisive breakout
- Analyst coverage: 79.8% buy rating, weighted price target +3.3% above current
- Macro: No surprise in US Treasury yields or data; Canada’s C$8.7B steel/auto support plan is sector‑specific, not a broad catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [How Ishares Msci Canada Etf (EWC) Affects Rotational Strategy Timing](https://news.stocktradersdaily.com/news_release/139/How_Ishares_Msci_Canada_Etf_EWC_Affects_Rotational_Strategy_Timing_102226020802_1792649282.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares Msci Canada Etf (NYSE: EWC). Strong Sentiment Across All Horizons Supports Overweight Bias; A mid-channel oscillation pattern is in...
- [Canada to invest billions in tariff-hit steel and auto sectors](https://seekingalpha.com/news/4655705-canada-to-invest-billions-in-tariff-hit-steel-and-auto-sectors)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Canada's Prime Minister Mark Carney and Ontario Premier Doug Ford announced an C$8.7B ($6.2B) support plan for the steel and auto sectors, which have been...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.66 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 59.44 (+2.0%), 50d 60.53 (+0.2%), 200d 58.12 (+4.4%); 50d above 200d
Momentum: RSI(14) 55.4 | MACD 0.187 vs signal -0.099 (histogram 0.286)
Returns: 1d -1.1% | 5d +0.5% | 1m +1.7% | 3m +2.7%
52-week range: 49.72 - 62.64 (now 84.7% of the way up)
Volatility: ATR(14) 0.71 (1.2% of price) | annualised 20d 15.2%
Volume: 0.42x the 20-day average
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
Three-year record: +25.6% a year | beta to the market 0.80
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
Ratings by weight: buy 79.8% | hold 20.2% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.3% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-16 RBC Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 94.80M | fund size: 5.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, weak technicals, flat fund flows, and analyst coverage limited to a minority of the fund.

**Main reasons it gave:**
- US Treasury yields unchanged (3‑month 4.03%, 5‑year 4.83%, 10‑year 5.02%) and no Fed policy surprise
- EWD price below 20‑day SMA (50.57), 50‑day SMA (51.75) and 200‑day SMA (51.49); RSI 41.8 indicating weak momentum
- Fund flows flat (share count change +0.0% week, +0.0% month) indicating no net demand
- Analyst coverage of top holdings (28.9% of fund) shows 81.7% buy rating and +15.2% price target, but limited to a minority of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Technical Reactions to EWD Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/141/Technical_Reactions_to_EWD_Trends_in_Macro_Strategies_102226021002_1792649402.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Price-action only: Ishares Msci Sweden Etf (EWD) movements set the tone for institutional models. Technical Reactions to EWD Trends in Macro Strategies.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 50.08 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 50.57 (-1.0%), 50d 51.75 (-3.2%), 200d 51.49 (-2.7%); 50d above 200d
Momentum: RSI(14) 41.8 | MACD -0.203 vs signal -0.280 (histogram 0.077)
Returns: 1d -1.9% | 5d -2.0% | 1m -2.4% | 3m -0.6%
52-week range: 45.38 - 54.72 (now 50.3% of the way up)
Volatility: ATR(14) 0.70 (1.4% of price) | annualised 20d 15.2%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.64 | P/B 2.82 | P/S 2.83 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +21.1% a year | beta to the market 1.25
Cost and size: expense ratio 0.51% | net assets 947.21M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Spotify Technology SA 9.7%, Investor AB Class B 9.6%, Atlas Copco AB Class A 7.1%, Volvo AB Class B 6.8%, Sandvik AB 5.3%
Sector mix: Industrials 46.3%, Financial services 25.6%, Communication services 13.5%, Technology 6.1%
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
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.2% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-20 Rosenblatt: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 7.65M | fund size: 383.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no material macro surprise, technicals are indecisive, flows flat, and analyst view is bullish but limited in coverage.

**Main reasons it gave:**
- Analyst consensus: 78.7% buy, weighted price target +20.5% (covers 45.4% of fund weight)
- Fund flows flat over the past week and month (0% change), indicating no net demand shift
- Technical indicators: price just above 20‑day SMA but below 50‑day and 200‑day SMAs, RSI 46.2, low volume, no decisive breakout
- Macro data unchanged: yields slightly down, VIX up modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [(EWG) Risk Channels and Responsive Allocation](https://news.stocktradersdaily.com/news_release/149/EWG_Risk_Channels_and_Responsive_Allocation_102226021201_1792649521.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Price-action only: Ishares Msci Germany Etf (EWG) movements set the tone for institutional models. (EWG) Risk Channels and Responsive Allocation.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.37 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 41.34 (+0.1%), 50d 42.59 (-2.9%), 200d 42.29 (-2.2%); 50d above 200d
Momentum: RSI(14) 46.2 | MACD -0.284 vs signal -0.397 (histogram 0.113)
Returns: 1d -0.8% | 5d -0.4% | 1m -1.2% | 3m +0.6%
52-week range: 38.08 - 44.59 (now 50.5% of the way up)
Volatility: ATR(14) 0.49 (1.2% of price) | annualised 20d 14.4%
Volume: 0.17x the 20-day average
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
Three-year record: +20.4% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.94 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 79.50M | fund size: 3.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, bullish analyst view limited to 53% of holdings, flat fund flows.

**Main reasons it gave:**
- Inflation 3.7% near Fed target, no policy surprise
- RSI 31.6 oversold but volume 0.2x 20‑day avg, low conviction
- Analyst coverage 53% of fund, 100% buy rating, price target +24.8% above current
- Fund flows flat (0% change week/month), no net positioning

<details><summary><b>News</b> — score +0.00</summary>

- [Discipline and Rules-Based Execution in EWI Response](https://news.stocktradersdaily.com/news_release/150/Discipline_and_Rules-Based_Execution_in_EWI_Response_102226021402_1792649642.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares Msci Italy Etf (NYSE: EWI). Divergent Sentiment Across All Horizons Suggests Choppy Conditions; No clear price positioning signal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 54.97 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 57.10 (-3.7%), 50d 59.92 (-8.3%), 200d 58.13 (-5.4%); 50d above 200d
Momentum: RSI(14) 31.6 | MACD -1.242 vs signal -1.233 (histogram -0.008)
Returns: 1d -2.4% | 5d -2.7% | 1m -8.4% | 3m -8.6%
52-week range: 50.66 - 63.35 (now 33.9% of the way up)
Volatility: ATR(14) 0.84 (1.5% of price) | annualised 20d 19.3%
Volume: 0.20x the 20-day average
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
Three-year record: +28.0% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 8.55M | fund size: 469.95M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technicals: price below 20‑day (96.93) and 50‑day (96.80) SMA, RSI 38.7, MACD negative
- CFTC positioning: net short 2.4% of open interest, up 5.8% week‑over‑week
- Analyst view: thin coverage (17% weight) all buy, price target +27.7% above current price
- Macro: VIX up 2.8 points, yields slightly down, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [(EWJ) and the Role of Price-Sensitive Allocations](https://news.stocktradersdaily.com/news_release/151/EWJ_and_the_Role_of_Price-Sensitive_Allocations_102226021601_1792649761.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares Msci Japan Etf (NYSE: EWJ). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias; A mid-channel oscillation...
- [Asian markets slide as U.S. futures retreat and Gulf tensions weigh on sentiment](https://seekingalpha.com/news/4655680-asian-markets-slide-as-us-futures-retreat-and-gulf-tensions-weigh-on-sentiment)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Asian stock market update: indexes slide on AI spending fears, Gulf tensions and surging oil.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 94.43 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 96.93 (-2.6%), 50d 96.80 (-2.4%), 200d 91.48 (+3.2%); 50d above 200d
Momentum: RSI(14) 38.7 | MACD -0.531 vs signal -0.172 (histogram -0.359)
Returns: 1d -1.3% | 5d -1.0% | 1m -2.7% | 3m +3.5%
52-week range: 79.49 - 99.32 (now 75.3% of the way up)
Volatility: ATR(14) 1.27 (1.3% of price) | annualised 20d 15.2%
Volume: 0.20x the 20-day average
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
Three-year record: +21.5% a year | beta to the market 0.83
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.7% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 2.4% of open interest (23,701 contracts)
Change on the week: +5.8% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 227.85M | fund size: 21.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, modest analyst buy bias, technicals overbought but low volume, not a decisive break.

**Main reasons it gave:**
- Fund flows flat (0% change week/month) indicating no net demand shift
- No macro surprise: US Treasury yields unchanged, VIX modestly higher, no policy shift
- Analyst coverage modest (48.2% of fund) with slight buy bias (mean rating 2.40, price target +3.5%)
- Technical indicators show overbought RSI (70.1) and bullish MACD but low volume (0.26x 20‑day average), not a decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Behavioral Patterns of EWL and Institutional Flows](https://news.stocktradersdaily.com/news_release/9/Behavioral_Patterns_of_EWL_and_Institutional_Flows_102226022201_1792650121.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares Msci Switzerland Etf (NYSE: EWL). If Near and Mid-Term Strong Sentiment Holds, It Could Extend to Long Term; Support is being...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.44 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 60.55 (+4.8%), 50d 61.56 (+3.0%), 200d 61.69 (+2.8%); 50d below 200d
Momentum: RSI(14) 70.1 | MACD 0.503 vs signal -0.014 (histogram 0.518)
Returns: 1d +0.4% | 5d +2.3% | 1m +5.1% | 3m +2.2%
52-week range: 55.06 - 65.08 (now 83.6% of the way up)
Volatility: ATR(14) 0.65 (1.0% of price) | annualised 20d 13.7%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.08 | P/B 4.13 | P/S 2.67 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +16.4% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.67B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.9%, Novartis AG Registered Shares 12.4%, Nestle SA 11.0%, UBS Group AG Registered Shares 6.4%, ABB Ltd 4.6%
Sector mix: Healthcare 38.0%, Financial services 19.6%, Consumer defensive 13.1%, Industrials 12.3%
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
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 28.62M | fund size: 1.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technical indicators bearish but no decisive break, flat fund flows, strong analyst view limited to <50% of fund weight.

**Main reasons it gave:**
- US inflation 3.7% and unemployment 4.2% in line with expectations, no macro surprise
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 35.1 and MACD below signal, indicating bearish momentum
- Fund flows flat over the past month, share count unchanged
- Analyst coverage of top holdings 100% buy with +48.9% price target, covering 46.7% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 64.01 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 66.44 (-3.6%), 50d 67.68 (-5.4%), 200d 64.91 (-1.4%); 50d above 200d
Momentum: RSI(14) 35.1 | MACD -0.836 vs signal -0.665 (histogram -0.171)
Returns: 1d -2.4% | 5d -1.7% | 1m -4.8% | 3m -3.7%
52-week range: 55.33 - 71.61 (now 53.3% of the way up)
Volatility: ATR(14) 0.96 (1.5% of price) | annualised 20d 17.8%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.85 | P/B 2.55 | P/S 1.87 | 3y earnings growth n/a
Yield: 4.2%
Three-year record: +24.8% a year | beta to the market 1.09
Cost and size: expense ratio 0.50% | net assets 710.44M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: ASML Holding NV 23.6%, ING Groep NV 9.1%, Nebius Group NV Shs Class-A- 4.9%, Prosus NV Ordinary Shares - Class N 4.6%, ASM International NV 4.4%
Sector mix: Technology 33.4%, Financial services 21.5%, Consumer defensive 10.4%, Industrials 9.6%
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

<details><summary><b>What analysts and big funds say</b> — score +0.71</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.71</summary>

```text
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +48.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 5.55M | fund size: 355.28M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, modest bullish analyst view, slight bearish technicals.

**Main reasons it gave:**
- Flat fund flows (0% change in share count over 1 week and 1 month) indicating no net demand
- No macro surprise: Treasury yields unchanged, inflation 3.7% in line with expectations, VIX modestly up but not extreme
- Technical indicators slightly bearish (price below 20‑day and 50‑day SMA, RSI 38.2) but no decisive break
- Analyst view modestly bullish (price target +10.4% and 51.5% buy rating) but not enough to outweigh neutral stance

<details><summary><b>News</b> — score +0.00</summary>

- [Liquidity Mapping Around (EWP) Price Events](https://news.stocktradersdaily.com/news_release/12/Liquidity_Mapping_Around_EWP_Price_Events_102226022802_1792650482.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Price-action only: Ishares Msci Spain Etf (EWP) movements set the tone for institutional models. Liquidity Mapping Around (EWP) Price Events.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 57.39 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 58.52 (-1.9%), 50d 60.60 (-5.3%), 200d 57.89 (-0.9%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.779 vs signal -0.824 (histogram 0.045)
Returns: 1d -1.7% | 5d -1.7% | 1m -4.9% | 3m -3.9%
52-week range: 49.34 - 63.23 (now 58.0% of the way up)
Volatility: ATR(14) 0.83 (1.4% of price) | annualised 20d 16.7%
Volume: 0.06x the 20-day average
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
Three-year record: +34.1% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 55.8% of the fund by weight
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.30 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 37.35M | fund size: 2.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong analyst bullishness is offset by flat fund flows, short‑term technical weakness, modestly lower yields, higher VIX and high valuation metrics.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings with weighted price target +43.5% above current prices
- Fund flows flat over the past week and month, indicating no net inflows or outflows
- Technical indicators: price below 20‑day and 50‑day SMAs, RSI 35.5, low volume, suggesting short‑term weakness
- Macro backdrop: yields down modestly, VIX up to 19.3, no policy surprise, and high fund valuation (P/E 28.15) adds downside risk

<details><summary><b>News</b> — score +0.00</summary>

- [Price-Driven Insight from (EWT) for Rule-Based Strategy](https://news.stocktradersdaily.com/news_release/16/Price-Driven_Insight_from_EWT_for_Rule-Based_Strategy_102226023402_1792650842.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares Msci Taiwan Etf (NYSE: EWT). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; A mid-channel oscillation...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 104.35 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 112.33 (-7.1%), 50d 110.23 (-5.3%), 200d 92.15 (+13.2%); 50d above 200d
Momentum: RSI(14) 35.5 | MACD -1.125 vs signal 0.074 (histogram -1.198)
Returns: 1d -4.3% | 5d -4.4% | 1m -7.2% | 3m +6.5%
52-week range: 60.03 - 118.00 (now 76.5% of the way up)
Volatility: ATR(14) 2.47 (2.4% of price) | annualised 20d 27.6%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +43.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 85.00M | fund size: 8.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break; positive analyst view and fundamentals are offset by flat flows and mixed technicals.

**Main reasons it gave:**
- Flat fund flows (0% change week/month) indicating no net demand
- Analyst view: 90.9% buy rating, weighted price target +7.4% above current price
- Technical: price above 20‑day SMA (+1.7%) but below 50‑day (-0.4%) and 200‑day (-2.5%) SMA; MACD positive but low volume
- Macro unchanged: yields up modestly, VIX up 2.8 points, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [(EWW) Price Dynamics and Execution-Aware Positioning](https://news.stocktradersdaily.com/news_release/22/EWW_Price_Dynamics_and_Execution-Aware_Positioning_102226024202_1792651322.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Ishares Msci Mexico Etf (NYSE: EWW). Strong Sentiment Across All Horizons Supports Overweight Bias; A mid-channel oscillation pattern is in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 74.12 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 72.91 (+1.7%), 50d 74.43 (-0.4%), 200d 76.05 (-2.5%); 50d below 200d
Momentum: RSI(14) 51.8 | MACD 0.247 vs signal -0.179 (histogram 0.426)
Returns: 1d -1.9% | 5d +0.3% | 1m +1.0% | 3m -1.8%
52-week range: 65.37 - 81.23 (now 55.2% of the way up)
Volatility: ATR(14) 1.25 (1.7% of price) | annualised 20d 19.4%
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
Three-year record: +16.4% a year | beta to the market 1.07
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
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 18.90M | fund size: 1.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, neutral analyst view, and technicals lack a decisive break despite being bearish.

**Main reasons it gave:**
- Analyst view provides no rating or price target (neutral)
- Fund flows flat (0% change) indicating no net demand
- Technical indicators show price below SMAs and RSI 32.7, but low volume suggests no decisive break
- Macro data unchanged (inflation 3.7% vs Fed target 4%, VIX modestly higher) and no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Understanding Momentum Shifts in (EWY)](https://news.stocktradersdaily.com/news_release/23/Understanding_Momentum_Shifts_in_EWY_102226024402_1792651442.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Key findings for Ishares Msci South Korea Etf (NYSE: EWY). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 149.91 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 172.71 (-13.2%), 50d 177.86 (-15.7%), 200d 161.20 (-7.0%); 50d above 200d
Momentum: RSI(14) 32.7 | MACD -7.990 vs signal -5.231 (histogram -2.759)
Returns: 1d -4.4% | 5d -4.0% | 1m -19.3% | 3m -8.0%
52-week range: 88.53 - 219.20 (now 47.0% of the way up)
Volatility: ATR(14) 6.36 (4.2% of price) | annualised 20d 42.8%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.79 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +42.8% a year | beta to the market 2.48
Cost and size: expense ratio 0.59% | net assets 26.21B
What it is made of: Stocks 96.8%, Cash 3.2%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.8%, SK Square 3.1%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 1.9%
Sector mix: Technology 56.9%, Industrials 16.4%, Financial services 10.9%, Consumer cyclical 4.5%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 75.60M | fund size: 11.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or policy shift; technicals show an uptrend but low volume and a slightly negative MACD histogram; fund flows are flat, indicating no new demand; analyst coverage is bullish (+22.4% price target) but only covers 39.9% of the fund, so it does not outweigh the neutral macro and technical backdrop.

**Main reasons it gave:**
- No macro surprise: yields down slightly, Fed target unchanged, no policy shift
- Technicals: price above 20‑, 50‑ and 200‑day SMAs but low volume and MACD histogram negative
- Fund flows flat over 1‑week and 1‑month, indicating no new demand
- Analyst coverage bullish (100% buy, +22.4% price target) but only covers 39.9% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Form 4 iShares MSCI Brazil ETF For: 22 October By Investing.com](https://uk.investing.com/news/stock-market-news/form-4-ishares-msci-brazil-etf-for-22-october-93CH-4924796)  
  <sub>Investing.com UK, 5 hours ago</sub>  
  Filed Pursuant to Rule 424(b)(2). Registration No. 333-277211. October 19, 2026. PRICING SUPPLEMENT. (To Prospectus dated February 21, 2024,.
- [Trading Systems Reacting to (EWZ) Volatility](https://news.stocktradersdaily.com/news_release/24/Trading_Systems_Reacting_to_EWZ_Volatility_102226024602_1792651562.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Ishares Msci Brazil Etf (EWZ) movements set the tone for institutional models. Trading Systems Reacting to (EWZ) Volatility.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.70 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 40.90 (+1.9%), 50d 38.28 (+8.9%), 200d 37.14 (+12.3%); 50d above 200d
Momentum: RSI(14) 57.2 | MACD 1.243 vs signal 1.358 (histogram -0.114)
Returns: 1d -1.9% | 5d +0.3% | 1m +11.6% | 3m +16.7%
52-week range: 30.03 - 43.54 (now 86.4% of the way up)
Volatility: ATR(14) 0.99 (2.4% of price) | annualised 20d 50.4%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.73 | P/B 1.84 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.9%
Three-year record: +19.6% a year | beta to the market 0.83
Cost and size: expense ratio 0.59% | net assets 8.64B
What it is made of: Stocks 97.5%, Cash 2.0%, Preferred 0.5%
Largest holdings: Vale SA 8.9%, Itau Unibanco Holding SA Participating Preferred 8.4%, Nu Holdings Ltd Ordinary Shares Class A 8.1%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.5%, Petroleo Brasileiro SA Petrobras 7.0%
Sector mix: Financial services 34.4%, Energy 18.1%, Basic materials 13.0%, Utilities 12.8%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.4% above the current prices
Holdings read: VALE3.SA, ITUB4, NU, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-10-20 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 200.55M | fund size: 8.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a mix of bullish analyst coverage (+36.9% price target, 100% buy) and solid fundamentals (low P/E, high yield, strong three‑year record), but technicals indicate a downtrend (price below 20‑, 50‑, 200‑day SMAs, RSI 43) and fund flows are flat, while macro data show no surprise. Overall, no clear macro catalyst or decisive technical break justifies a directional tilt.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +36.9% price target for top holdings
- Technical trend: price below 20‑, 50‑, 200‑day SMAs, RSI 43 indicating downtrend
- Fund flows: flat share count change (0% week/month) indicating no net demand
- Macro: modest yield declines and VIX rise, no major data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Trading the Move, Not the Narrative: (EZA) Edition](https://news.stocktradersdaily.com/news_release/81/Trading_the_Move,_Not_the_Narrative:_EZA_Edition_102226030402_1792652642.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Ishares Msci South Africa Etf (EZA) movements set the tone for institutional models. Trading the Move, Not the Narrative: (EZA) Edition.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 63.74 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 64.11 (-0.6%), 50d 67.42 (-5.5%), 200d 68.80 (-7.4%); 50d below 200d
Momentum: RSI(14) 43.0 | MACD -0.653 vs signal -0.928 (histogram 0.275)
Returns: 1d -2.4% | 5d -2.0% | 1m -4.1% | 3m +4.4%
52-week range: 60.43 - 81.60 (now 15.6% of the way up)
Volatility: ATR(14) 1.24 (1.9% of price) | annualised 20d 24.0%
Volume: 1.46x the 20-day average
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
Three-year record: +27.7% a year | beta to the market 1.07
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.9% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 7.90M | fund size: 503.51M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; mixed technical, flow, analyst and fundamental signals lead to a neutral stance.

**Main reasons it gave:**
- No macro surprise: Treasury yields unchanged, inflation 3.7% below Fed target
- Technical downtrend: price below 20d, 50d, and 200d SMAs, RSI 37.2
- Fund flows: net outflow of -4.6% over the past month
- Analyst view: 100% buy rating on top holdings with +22% price target

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  VanEck Gold Miners ETF (GDX) · 3.98% · -8.16% · -6.74% · -0.14% · 19.14% · 164.96% · 137.46%. Key Events. Baseline. Advanced Chart. Loading...
- [RAAX Update: Ride the Trend](https://www.vaneck.com/us/en/blogs/natural-resources/raax-update-ride-the-trend/)  
  <sub>VanEck, 21 hours ago</sub>  
  Stay invested in AI and the physical buildout behind it, tune out bubble noise, and remain diversified.
- [ETFs Investing in SSR Mining Inc Stocks](https://www.tradingview.com/symbols/SWB-ZSV/etfs/)  
  <sub>TradingView, 19 hours ago</sub>  
  Explore funds investing in ZSV in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [VanEck UCITS ETFs Plc - Net Asset Value(s)](https://uk.finance.yahoo.com/news/vaneck-ucits-etfs-plc-net-060000303.html)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Fund Name. NAV Date. Ticker Symbol. ISIN. Shares in Issue. Net Asset Value. NAV per Share. VanEck Emerging Markets High Yield Bond UCITS ETF. 2026-10-21.
- [Russian gold reserves fall to lowest since 2019 after drawdown for 10 straight months (GLD:NYSEARCA)](https://seekingalpha.com/news/4655636-russian-gold-reserves-fall-to-lowest-since-2019-after-drawdown-for-10-straight-months)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  The Bank of Russia sold 200K troy oz of gold in September, equivalent to 6.2 metric tons, lowering Russia's sovereign gold holdings to 72.8M troy oz,...
- [iShares Gold Trust (IAU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IAU/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest iShares Gold Trust (IAU) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Gfi Etf Unit Trust - Gf Hkex Tech & Us Tech 100 Index Etf (3599.HK) latest stock news and headlines](https://uk.finance.yahoo.com/quote/3599.HK/news/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Gfi Etf Unit Trust - Gf Hkex Tech & Us Tech 100 Index Etf (3599.HK). 14.150 -0.050 (-0.35%). At close: 13 October at 15:39:47 GMT+8...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 82.16 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 87.23 (-5.8%), 50d 93.03 (-11.7%), 200d 91.00 (-9.7%); 50d above 200d
Momentum: RSI(14) 37.2 | MACD -1.958 vs signal -1.773 (histogram -0.185)
Returns: 1d -5.3% | 5d -5.6% | 1m -12.2% | 3m +9.2%
52-week range: 68.28 - 115.84 (now 29.2% of the way up)
Volatility: ATR(14) 3.00 (3.7% of price) | annualised 20d 40.5%
Volume: 0.53x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 13.93 | P/B 3.18 | P/S 4.54 | 3y earnings growth n/a
Yield: 0.7%
Three-year record: +44.6% a year | beta to the market 0.81
Cost and size: expense ratio 0.51% | net assets 26.25B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Newmont Corp 11.1%, Agnico Eagle Mines Ltd 11.0%, Barrick Mining Corp 7.9%, Wheaton Precious Metals Corp 5.5%, Franco-Nevada Corp 5.2%
Sector mix: Basic materials 100.0%
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
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.0% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-20 Citigroup: main, Buy -> Buy
  - AEM.TO: 2026-10-21 JP Morgan: main, Neutral -> Neutral
  - ABX.TO: 2026-10-21 JP Morgan: main, Overweight -> Overweight
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.6% (639.77M) over 7d | 1 month: -4.6% (-1.20B) over 30d
Shares outstanding: 304.69M | fund size: 25.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields fell slightly across the curve with no surprise
- MACD histogram negative despite price above 20d/50d/200d SMAs
- Fund flows flat over the past month, indicating no net demand
- Analyst coverage of top holdings (42.9% of fund) is 100% buy with +21.5% price target

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Expanded Tech-Software Sector ETF (IGV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance Singapore, 7 hours ago</sub>  
  iShares Expanded Tech-Software Sector ETF (IGV) · 1.09% · 1.58% · 25.54% · 1.71% · -5.38% · 24.82% · 972.12%. Key events. Baseline. Advanced chart.
- [iShares Expanded Tech-Software Sector ETF (IGV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  iShares Expanded Tech-Software Sector ETF (IGV) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM to 4...
- [Winning AI Trade Stalls While Investors Bet On Victims Instead](https://www.investors.com/etfs-and-funds/etfs/ai-trade-stalls-while-investors-bet-on-victims-instead/)  
  <sub>Investor's Business Daily, 4 hours ago</sub>  
  Investors have settled on the idea chipmakers will profit the most from AI — while crushing software firms. But the theory is breaking apart.
- [Palantir Rises 4% as Software Stocks Rally; ServiceNow Gains 3%, Salesforce Holds Flat](https://247wallst.com/investing/2026/10/21/palantir-rises-4-as-software-stocks-rally-servicenow-gains-3-salesforce-holds-flat/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Palantir is pulling away from its software peers as buyers chase AI platform names, but a steep valuation and an undisclosed federal partnership deal leave...
- [SpaceX Jumps 10%, Nasdaq 100 Rises as AI Trade Returns: Stock Market Today](https://www.tradingview.com/news/benzinga:b1cccd956094b:0-spacex-jumps-10-nasdaq-100-rises-as-ai-trade-returns-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  Shares of Space Exploration Technologies Corp. NASDAQ:SPCX jumped 10% on Wednesday after a third quarter that blew past forecasts, reviving the artificial...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 108.82 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 108.36 (+0.4%), 50d 106.22 (+2.5%), 200d 93.80 (+16.0%); 50d above 200d
Momentum: RSI(14) 53.2 | MACD 0.637 vs signal 1.007 (histogram -0.370)
Returns: 1d +0.0% | 5d -0.7% | 1m +0.7% | 3m +23.7%
52-week range: 74.67 - 117.08 (now 80.5% of the way up)
Volatility: ATR(14) 2.72 (2.5% of price) | annualised 20d 28.5%
Volume: 0.33x the 20-day average
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
Three-year record: +16.4% a year | beta to the market 1.22
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.5% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
  - PLTR: 2026-10-15 Mizuho: main, Outperform -> Outperform
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - MSFT: 2026-10-21 Guggenheim: reit, Buy -> Buy
  - ORCL: 2026-10-22 Cantor Fitzgerald: reit, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 12.50M | fund size: 1.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; mixed evidence from analyst view, outflows, and fundamentals.

**Main reasons it gave:**
- Analyst coverage thin (23.7% of fund) but all buy with +29.8% price target
- Share count fell -12.6% over past month, indicating outflows
- Price below 50‑day and 200‑day SMA, near 52‑week low
- No macro surprise: yields down slightly, VIX up modestly
- Fund valuations moderate (P/E 21.36) and low beta (0.62)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.14 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 46.91 (+0.5%), 50d 48.19 (-2.2%), 200d 49.37 (-4.5%); 50d below 200d
Momentum: RSI(14) 47.3 | MACD -0.178 vs signal -0.346 (histogram 0.168)
Returns: 1d -0.3% | 5d -1.7% | 1m -1.9% | 3m -1.8%
52-week range: 45.42 - 55.29 (now 17.4% of the way up)
Volatility: ATR(14) 0.50 (1.1% of price) | annualised 20d 15.8%
Volume: 0.44x the 20-day average
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
Three-year record: +3.1% a year | beta to the market 0.62
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.8% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.60</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -2.7% (-157.56M) over 7d | 1 month: -12.6% (-831.83M) over 30d
Shares outstanding: 122.29M | fund size: 5.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat flows, technicals not decisive, analyst view bullish but limited coverage, fundamentals moderate.

**Main reasons it gave:**
- Flat fund flows: share count unchanged over week and month
- Technicals: price just above 20‑day SMA, RSI 55.9, low volume
- Macro data unchanged: yields down slightly, VIX up modestly, no policy surprise
- Analyst coverage 51.6% of fund, 100% buy rating with +25.6% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.56 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 79.76 (+2.2%), 50d 82.22 (-0.8%), 200d 81.59 (-0.0%); 50d above 200d
Momentum: RSI(14) 55.9 | MACD -0.363 vs signal -0.682 (histogram 0.319)
Returns: 1d +2.0% | 5d +0.8% | 1m +2.3% | 3m -7.3%
52-week range: 68.14 - 90.01 (now 61.3% of the way up)
Volatility: ATR(14) 1.28 (1.6% of price) | annualised 20d 14.8%
Volume: 0.59x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 18.90 | P/B 3.94 | P/S 1.34 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +13.5% a year | beta to the market 1.32
Cost and size: expense ratio 0.37% | net assets 1.88B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Union Pacific Corp 17.4%, Uber Technologies Inc 15.1%, CSX Corp 9.3%, Delta Air Lines Inc 4.9%, United Airlines Holdings Inc 4.8%
Sector mix: Industrials 84.1%, Technology 15.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.6% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-07 Citigroup: main, Buy -> Buy
  - UBER: 2026-10-16 Guggenheim: reit, Buy -> Buy
  - CSX: 2026-10-22 TD Cowen: main, Buy -> Buy
  - DAL: 2026-10-12 UBS: main, Buy -> Buy
  - UAL: 2026-10-22 Susquehanna: main, Positive -> Positive
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 2.80M | fund size: 228.35M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: modest bullish fundamentals and analyst view are offset by net outflows and only modest technical upside.

**Main reasons it gave:**
- Fund flows show net outflows: -1.6% week, -4.2% month
- Analyst coverage thin (5.7% of fund) but bullish: 74.8% buy, +10.9% price target
- Technical indicators modestly positive: price above 20‑day SMA, MACD above signal, 1‑day +1.4% gain
- Fundamentals: low P/E 12.02, low P/B 1.21, 3‑year annual return +25.1% per year

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the Invesco KBW Bank ETF (KBWB)?](https://finance.yahoo.com/markets/stocks/articles/invest-invesco-kbw-bank-etf-092002007.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Designed to provide broad exposure to the Financials - Banking segment of the equity market, the Invesco KBW Bank ETF (KBWB) is a passively managed exchange...
- [Should You Invest in the iShares U.S. Regional Banks ETF (IAT)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-regional-banks-092002140.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Financials - Regional Banks segment of the equity market? You should consider the iShares U.S. Regional Banks ETF (IAT),...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 71.64 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 69.95 (+2.4%), 50d 72.45 (-1.1%), 200d 70.82 (+1.2%); 50d above 200d
Momentum: RSI(14) 55.3 | MACD -0.520 vs signal -0.893 (histogram 0.373)
Returns: 1d +1.4% | 5d +2.7% | 1m +1.8% | 3m -5.4%
52-week range: 58.63 - 77.93 (now 67.4% of the way up)
Volatility: ATR(14) 1.28 (1.8% of price) | annualised 20d 17.2%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +25.1% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
Sector mix: Financial services 100.0%
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
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 74.8% | hold 25.2% | sell 0.0% (mean 1.94 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.9% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-22 TD Cowen: main, Buy -> Buy
  - HWC: 2026-10-21 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EWBC: 2026-10-21 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.6% (-60.65M) over 7d | 1 month: -4.2% (-166.67M) over 30d
Shares outstanding: 52.81M | fund size: 3.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: geopolitical tension (Iran war, Houthi attacks) adds downside risk, but technicals show oversold conditions (RSI 17.2, price at 52‑week low) and analyst coverage is strongly bullish (90.3% buy, +24.2% price target). Fund flows show modest weekly inflow (+3.1% share count), while fundamentals are moderate (P/E 14.08, low 3‑yr return). No policy or data surprise, nor decisive technical break, so maintain a neutral stance.

**Main reasons it gave:**
- Geopolitical tension: Iran war and Houthi attacks in Saudi Arabia
- Technical oversold: RSI 17.2 and price at 52‑week low
- Analyst coverage: 90.3% buy rating, price target +24.2% above price
- Fund flows: +3.1% share count increase in past week

<details><summary><b>News</b> — score +0.00</summary>

- [Saudi Arabia Forced to Rethink Investment Strategy Because of Iran War](https://www.barrons.com/articles/iran-war-saudi-arabia-uae-changing-investments-8c7dc8a5)  
  <sub>Barron's, 4 hours ago</sub>  
  Reshma Kapadia here, filling in for Sabrina Escobar. The strange dynamic between the U.S., Russia and Ukraine is getting even stranger.
- [US Warns Citizens of Escalating Attacks in Saudi Arabia](https://ng.headtopics.com/news/us-warns-citizens-of-escalating-attacks-in-saudi-arabia-89057532)  
  <sub>Head Topics, 18 hours ago</sub>  
  The United States has issued a security alert warning its citizens in Saudi Arabia to exercise extreme caution due to ongoing Houthi attacks on civilian...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.68 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 35.82 (-6.0%), 50d 37.22 (-9.5%), 200d 38.05 (-11.5%); 50d below 200d
Momentum: RSI(14) 17.2 | MACD -0.792 vs signal -0.634 (histogram -0.158)
Returns: 1d -2.5% | 5d -4.2% | 1m -9.4% | 3m -9.1%
52-week range: 33.68 - 41.03 (now 0.0% of the way up)
Volatility: ATR(14) 0.37 (1.1% of price) | annualised 20d 14.7%
Volume: 0.67x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.08 | P/B 1.70 | P/S 2.84 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +0.8% a year | beta to the market 0.19
Cost and size: expense ratio 0.75% | net assets 588.43M
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.5%, Saudi National Bank 8.6%, Saudi Telecom Co 6.1%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 42.2%, Energy 12.5%, Basic materials 12.4%, Communication services 9.0%
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
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.2% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: +3.1% (17.25M) over 7d | 1 month: -0.3% (-1.92M) over 30d
Shares outstanding: 16.96M | fund size: 571.30M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: mixed signals with no material macro surprise or decisive technical break. Bullish fundamentals and analyst coverage are offset by downtrend technicals and recent net outflows.

**Main reasons it gave:**
- Technical downtrend: price below 20‑day, 50‑day and 200‑day SMAs, low volume
- RSI at 27.2 indicating oversold but no decisive breakout
- Fund flows: net outflows of -1.6% over the past month
- Analyst view: 100% buy rating but only covers 32.3% of the fund
- Fund fundamentals: low valuation multiples (P/E 11.39, P/B 1.33) suggest cheapness

<details><summary><b>News</b> — score +0.00</summary>

- [How to Buy BYD Stock (BYDDF) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-byd-stock/)  
  <sub>The Motley Fool, 45 minutes ago</sub>  
  BYD (OTC:BYDD.F) is one of the world's largest electric vehicle (EV) makers. The Chinese company is more than an EV maker, as its diversified business also...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 48.91 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 51.61 (-5.2%), 50d 53.15 (-8.0%), 200d 56.14 (-12.9%); 50d below 200d
Momentum: RSI(14) 27.2 | MACD -0.833 vs signal -0.636 (histogram -0.196)
Returns: 1d -2.3% | 5d -5.4% | 1m -8.0% | 3m -8.3%
52-week range: 48.91 - 65.59 (now 0.0% of the way up)
Volatility: ATR(14) 0.72 (1.5% of price) | annualised 20d 17.9%
Volume: 0.46x the 20-day average
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
Three-year record: +10.4% a year | beta to the market 0.45
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +71.1% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
Recent rating changes among them: none reported
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
Share count change: 1 week: +2.2% (122.17M) over 7d | 1 month: -1.6% (-90.92M) over 30d
Shares outstanding: 117.17M | fund size: 5.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral: strong analyst bullishness is offset by flat fund flows, oversold technicals without a decisive breakout, and a neutral macro backdrop with no policy surprise.

**Main reasons it gave:**
- Analyst coverage of top holdings is 100% buy with a +51.7% price target (strong bullish bias)
- Fund flows are flat over the past week and month, indicating no net demand shift
- Technical indicators show oversold RSI (32.6) and negative MACD, but price remains below 20‑day SMA with low volume, no decisive breakout
- Macro data shows no policy surprise; yields slightly down, VIX modestly higher, inflation above target, indicating a neutral macro backdrop

<details><summary><b>News</b> — score +0.00</summary>

- [Semiconductor Stocks May Face An Explosive Move This Week (NASDAQ:SMH)](https://seekingalpha.com/article/4955914-semiconductor-stocks-may-face-an-explosive-move-this-week)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  The VanEck Semiconductor ETF sits at critical technical support, with upcoming Bank of Korea rate decisions likely to drive the next major SMH move.
- [S&P 500, Nasdaq End Higher As Chipmakers Rally, While Dow Posts Best First Half In Five Years — LUNR, AMZN, PLTR, XYZ, AVAV In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-end-higher-as-chipmakers-rally-while-dow-posts-best-first-half-in-five-years-lunr-amzn-pltr-xyz-avav-in-focus/cZ1QvpOR70p)  
  <sub>Stocktwits, 15 hours ago</sub>  
  U.S. stock indices ended higher on Tuesday, tracking gains in chipmaker stocks, while the Dow Jones ended its best first half in five years.
- [SMH 261023 420.00P (SMH261023P420000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/SMH261023P420000-US)  
  <sub>Moomoo, 22 hours ago</sub>  
  Today's paper-trading experience reminded me that a good investment decision involves more than buying at an attractive price. My SMH position currently...
- [S&P 500, Nasdaq Gain, Powered By Meta, Tesla Stock — SPCX, META, TSLA, SKYD, IBM In Focus](https://www.tradingview.com/news/stocktwits:fb56da102094b:0-s-p-500-nasdaq-gain-powered-by-meta-tesla-stock-spcx-meta-tsla-skyd-ibm-in-focus/)  
  <sub>TradingView, 16 hours ago</sub>  
  U.S. stock indices ended higher on Wednesday, with robust results from Meta and Tesla helping aid investor confidence in technology shares.The S&P 500 ended...
- [Chip Stocks Have Pulled Back—Here's How 3 Semiconductor ETFs Stack Up for Investors](https://www.marketbeat.com/articles/chip-stocks-have-pulled-backheres-how-3-semiconductor-etfs-stack-up-for-investors/)  
  <sub>MarketBeat, 22 hours ago</sub>  
  Semiconductor stocks have pulled back amid rate concerns and AI buildout worries. SMH, SOXX, and XSD offer differing ETF approaches to gaining exposure as...
- [The Earnings Twist In The AI Chip Bubble Debate](https://www.benzinga.com/opinion/26/10/62507341/the-earnings-twist-in-the-ai-chip-bubble-debate)  
  <sub>Benzinga, 23 hours ago</sub>  
  Picture a ski resort that has sold out every winter for the past three years, with this season fully booked too. Then a long-range forecast calls for a warm...
- [Bank of Korea rate decision may trigger major m...](https://pluang.com/en/news-feed/pergerakan-ekspansif-saham-semikonduktor-minggu-ini)  
  <sub>Pluang, 24 hours ago</sub>  
  The VanEck Semiconductor ETF (SMH) is at a critical technical support level, with the upcoming Bank of Korea rate decision expected to influence its next...
- [iShares Expanded Tech-Software Sector ETF (IGV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest iShares Expanded Tech-Software Sector ETF (IGV) stock quote, history, news and other vital information to help you with your stock trading...
- [Daily ETF Flows: SOXX On Top](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-soxx-top)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 20, 2026.
- [Nasdaq 100 Sees Best Day In Nearly A Month As AI Rout Cools — AMZN, BE, CRWV, AAPL, PLTR In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-100-sees-best-day-in-nearly-a-month-as-ai-rout-cools-amzn-be-crwv-aapl-pltr-in-focus/cZxo2SbRBu5)  
  <sub>Stocktwits, 14 hours ago</sub>  
  The S&P 500 ended Monday 0.4% higher, the Nasdaq 100 added 1.2%, and the Dow Jones Industrial Average slipped 0.1%. CoreWeave extended last week's weakness,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 527.79 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 589.74 (-10.5%), 50d 576.42 (-8.4%), 200d 514.75 (+2.5%); 50d above 200d
Momentum: RSI(14) 32.6 | MACD -11.566 vs signal -2.792 (histogram -8.774)
Returns: 1d -5.2% | 5d -5.6% | 1m -12.2% | 3m -6.0%
52-week range: 325.10 - 668.91 (now 59.0% of the way up)
Volatility: ATR(14) 17.39 (3.3% of price) | annualised 20d 32.3%
Volume: 0.57x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Technology
What it holds: P/E 32.50 | P/B 11.65 | P/S 13.32 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +57.4% a year | beta to the market 2.00
Cost and size: expense ratio 0.35% | net assets 74.88B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 19.3%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.3%, Advanced Micro Devices Inc 5.5%, Broadcom Inc 5.3%, Micron Technology Inc 4.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +51.7% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - TSM: 2026-10-16 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-22 Tigress Financial: init, ? -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 11.67M | fund size: 6.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals are bearish (price below SMAs, low RSI), macro is slightly negative (higher yields, inflation above target, VIX up), analyst view is bullish but only covers 43% of the fund, and fund flows are flat, indicating no net demand.

**Main reasons it gave:**
- Analyst view covers 43.2% of fund with 100% buy rating and +34.4% price target
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 26.4, MACD negative
- Macro: Treasury yields up slightly, inflation 3.7% above target, VIX up 2.8 points
- Fund flows flat (0% change week/month), indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 31.11 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 33.77 (-7.9%), 50d 37.13 (-16.2%), 200d 39.20 (-20.6%); 50d below 200d
Momentum: RSI(14) 26.4 | MACD -1.464 vs signal -1.358 (histogram -0.106)
Returns: 1d -3.3% | 5d -7.3% | 1m -17.0% | 3m -20.6%
52-week range: 31.11 - 43.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.68 (2.2% of price) | annualised 20d 26.3%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.69 | P/B 1.02 | P/S 0.63 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +0.5% a year | beta to the market 0.61
Cost and size: expense ratio 0.59% | net assets 163.33M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.4%, Tupras-Turkiye Petrol Rafineleri AS 10.6%, Bim Birlesik Magazalar AS 10.4%, Akbank TAS 6.1%, Turk Hava Yollari AO 4.8%
Sector mix: Industrials 29.2%, Financial services 16.1%, Consumer defensive 13.9%, Basic materials 11.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 15.65M | fund size: 486.87M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields fell slightly this week (10‑yr -0.07%) – no policy surprise
- Fund flows flat: share count unchanged (+0.0% week, +0.0% month)
- Analyst coverage of top holdings (40.5% weight) shows 100% buy rating and +18.9% price target
- Technical indicators: price near 52‑week low (36.2% up from low), RSI 51.4, MACD above signal, but volume 0.22× 20‑day average
- Fund fundamentals: high P/E 28.36, yield 3.8%, three‑year return +12.8% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 92.05 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 90.54 (+1.7%), 50d 93.82 (-1.9%), 200d 94.50 (-2.6%); 50d below 200d
Momentum: RSI(14) 51.4 | MACD -0.466 vs signal -0.906 (histogram 0.440)
Returns: 1d +0.6% | 5d +0.7% | 1m +0.7% | 3m -8.7%
52-week range: 87.00 - 100.95 (now 36.2% of the way up)
Volatility: ATR(14) 1.25 (1.4% of price) | annualised 20d 14.3%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.36 | P/B 2.42 | P/S 4.59 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +12.8% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
Sector mix: Real estate 99.5%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.9% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2026-10-19 Wells Fargo: main, Overweight -> Overweight
  - PLD: 2026-10-21 Raymond James: up, Market Perform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 35d
Shares outstanding: 370.18M | fund size: 34.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals mixed, modest bearish flow pressure, thin analyst coverage.

**Main reasons it gave:**
- US Treasury yields down modestly across curve, no rate surprise
- Technical indicators mixed: price just above 20‑day SMA, below 50‑day SMA, RSI 48.8
- Fund flows show 7.1% outflow over month, indicating bearish sentiment but no macro catalyst
- Analyst coverage thin (9.2% of fund) with modest bullish tilt

<details><summary><b>News</b> — score +0.00</summary>

- [Biotech Giants vs. Emerging Innovators: Which ETF Is the Better Buy?](https://www.fool.com/coverage/etfs/2026/10/22/biotech-giants-vs-emerging-innovators-which-etf-is-the-better-buy/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  The VanEck Biotech ETF (BBH +0.68%) offers a concentrated play on industry giants, while the State Street SPDR S&P Biotech ETF (XBI -0.30%) provides broad...
- [Big Pharma vs. Breakthrough Biotech: Which ETF Has More Upside for Investors?](https://finance.yahoo.com/healthcare/articles/big-pharma-vs-breakthrough-biotech-092002507.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  The Invesco Pharmaceuticals ETF (NYSEMKT:PJP) offers a lower-volatility approach to healthcare than the Invesco Biotechnology & Genome ETF (NYSEMKT:PBE),...
- [I’m Bottom Fishing This Data Center Play the Right Way](https://pro.thestreet.com/trade-ideas/im-bottom-fishing-this-data-center-play-the-right-way)  
  <sub>TheStreet Pro, 24 hours ago</sub>  
  SpaceX has confirmed the strong need for data centers with power supplies.
- [Arbutus Biopharma says FDA lifts AB-101 clinical hold](https://mugglehead.com/arbutus-biopharma-ab-101-fda-clinical-hold-lifted/)  
  <sub>Mugglehead Investment Magazine, 2 hours ago</sub>  
  Arbutus says the FDA lifted the AB-101 clinical hold after a Phase 1 study. Further United States development remains under evaluation.
- [Michael Burry Says His Puts Give Him 'Far More Upside' In A Crash As He Pulls His AI Bubble Timeline Forward](https://stocktwits.com/news-articles/markets/equity/michael-burry-puts-far-more-upside-crash-pulls-ai-bubble-timeline-forward/cZMnDzGRBWH)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Fresh research accelerated Burry's bearish AI timeline from an earlier 2028 base case, prompting a shift toward more leveraged positions.
- [iShares Biotechnology ETF (IBB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IBB/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest iShares Biotechnology ETF (IBB) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 152.13 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 152.03 (+0.1%), 50d 157.43 (-3.4%), 200d 140.76 (+8.1%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD -1.817 vs signal -2.219 (histogram 0.402)
Returns: 1d -0.4% | 5d +1.6% | 1m -2.0% | 3m +1.1%
52-week range: 107.32 - 169.55 (now 72.0% of the way up)
Volatility: ATR(14) 4.32 (2.8% of price) | annualised 20d 31.9%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +32.1% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -7.5% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-21 TD Cowen: main, Hold -> Hold
  - NTRA: 2026-10-19 Canaccord Genuity: main, Buy -> Buy
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-21 Barclays: main, Equal-Weight -> Equal-Weight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -1.1% (-118.51M) over 7d | 1 month: -7.1% (-783.41M) over 30d
Shares outstanding: 67.62M | fund size: 10.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no macro surprise, technicals mixed, and modest bullish analyst and flow signals offset by moderate fundamentals.

**Main reasons it gave:**
- Macro unchanged: inflation 3.7% vs Fed target 4.0%, no surprise
- Technical trend mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA
- Analyst view thin (17% coverage) despite 100% buy rating and +16.8% price target
- Fund flows net inflow over month (+7.6% shares, $103M) offset by recent weekly outflow (-2.3%)

<details><summary><b>News</b> — score +0.00</summary>

- [ProShares UltraPro QQQ (TQQQ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TQQQ/)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Find the latest ProShares UltraPro QQQ (TQQQ) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Green Brick Partners tops homebuilder stocks as sector faces rising costs, high inventory (ITB:BATS)](https://seekingalpha.com/news/4655395-green-brick-partners-tops-homebuilder-stocks-as-sector-faces-rising-costs-high-inventory)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  U.S. homebuilder stocks face mounting headwinds from elevated housing inventories, rising mortgage rates and higher construction costs, raising questions...
- [Housing Is Weak, but Its Impact on the Business Cycle Is Muted](https://ng.investing.com/analysis/housing-is-weak-but-its-impact-on-the-business-cycle-is-muted-220180)  
  <sub>Investing.com Nigeria, 21 hours ago</sub>  
  Market Analysis by covering: State Street® SPDR® S&P® Homebuilders ETF. Read 's Market Analysis on Investing.com NG.
- [(XHB) Stock Market Analysis (XHB:CA)](https://news.stocktradersdaily.com/canada/xhb-stock-market-analysis_20261022_78c200)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Stock Market Analysis for iShares Canadian HYBrid Corporate Bond Index ETF (XHB) Highlighting Key Trading Opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 98.12 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 95.87 (+2.3%), 50d 99.60 (-1.5%), 200d 105.48 (-7.0%); 50d below 200d
Momentum: RSI(14) 53.9 | MACD -0.943 vs signal -1.445 (histogram 0.501)
Returns: 1d +2.6% | 5d +2.5% | 1m +1.1% | 3m -9.5%
52-week range: 92.84 - 121.36 (now 18.5% of the way up)
Volatility: ATR(14) 2.24 (2.3% of price) | annualised 20d 23.8%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 18.56 | P/B 2.09 | P/S 1.23 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +11.7% a year | beta to the market 1.48
Cost and size: expense ratio 0.35% | net assets 1.43B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: SharkNinja Inc 3.5%, Cavco Industries Inc 3.4%, Champion Homes Inc 3.4%, Johnson Controls International PLC Registered Shares 3.4%, Wayfair Inc Class A 3.4%
Sector mix: Consumer cyclical 63.4%, Industrials 31.7%, Basic materials 3.2%, Real estate 1.8%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.8% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-10-19 JP Morgan: main, Overweight -> Overweight
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - JCI: 2026-10-15 Mizuho: main, Neutral -> Neutral
  - W: 2026-10-20 Piper Sandler: main, Overweight -> Overweight
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
Share count change: 1 week: -2.3% (-33.64M) over 7d | 1 month: +7.6% (103.34M) over 30d
Shares outstanding: 14.87M | fund size: 1.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst coverage and positive fund flows suggest bullishness, but weak technicals and a slightly negative macro backdrop temper the outlook, leading to a neutral stance.

**Main reasons it gave:**
- Analyst coverage 90.6% buy with +25.2% price target
- Fund flows +1.1% share count increase over week and month
- Technicals: price below 20d/50d/200d SMAs, RSI 37.4, negative MACD
- Macro: yields up, VIX up, inflation 3.7% above target

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs tied to Meta Platforms feel the downward pressure](https://www.tradingview.com/news/seekingalpha:80d7cc3eb094b:0-etfs-tied-to-meta-platforms-feel-the-downward-pressure/)  
  <sub>TradingView, 60 minutes ago</sub>  
  Shares of Meta Platforms NASDAQ:META are under pressure Thursday morning after the large-scale technology firm posted its latest quarterly earnings report.
- [Spotify Jumps 10% as Premium Subscriber Growth Tops Forecasts; Sirius XM Stays Put](https://247wallst.com/investing/2026/10/22/spotify-jumps-10-as-premium-subscriber-growth-tops-forecasts-sirius-xm-stays-put/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  A third-quarter subscriber count that exceeded its own guidance has put Spotify Technology (NYSE:SPOT | SPOT Price Prediction) at the front of a soft media...
- [Skydance Rallies 10% as Shares Rebound After Warrant Selloff; Spotify Eases, Disney Holds Steady](https://247wallst.com/investing/2026/10/21/skydance-rallies-10-as-shares-rebound-after-warrant-selloff-spotify-eases-disney-holds-steady/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Skydance shares are staging a sharp recovery while the rest of the media sector slides, and the reason traces back to a warrant split that may not be done...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 107.48 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 110.89 (-3.1%), 50d 111.75 (-3.8%), 200d 113.34 (-5.2%); 50d below 200d
Momentum: RSI(14) 37.4 | MACD -0.730 vs signal -0.374 (histogram -0.356)
Returns: 1d -1.4% | 5d -4.4% | 1m -4.5% | 3m +1.1%
52-week range: 105.38 - 120.08 (now 14.3% of the way up)
Volatility: ATR(14) 1.70 (1.6% of price) | annualised 20d 16.0%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Communications
What it holds: P/E 16.28 | P/B 3.24 | P/S 2.42 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +19.7% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.53B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 22.2%, Alphabet Inc Class A 11.6%, Alphabet Inc Class C 9.3%, Warner Bros. Discovery Inc Ordinary Shares - Class A 4.9%, The Walt Disney Co 4.5%
Sector mix: Communication services 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.2% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-22 Scotiabank: main, Sector Perform -> Sector Perform
  - GOOGL: 2026-10-22 Citizens: main, Market Outperform -> Market Outperform
  - GOOG: 2026-10-15 JP Morgan: main, Overweight -> Overweight
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-16 Citigroup: main, Buy -> Buy
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
Share count change: 1 week: +1.1% (240.28M) over 7d | 1 month: +1.1% (228.96M) over 30d
Shares outstanding: 204.43M | fund size: 21.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical breakout, flat fund flows, mixed inventory picture, bearish EIA oil price outlook offset by strong analyst coverage.

**Main reasons it gave:**
- Analyst coverage of top holdings (58.2% weight) is 100% buy with a +2.3% price target
- Fund flows flat over the past month, indicating no net demand shift
- Energy inventories show crude and gasoline draws (bullish) but diesel and natural gas builds (bearish), net mixed
- EIA forecast projects oil prices falling ~14% over six months, bearish for the fund
- No macro surprise or decisive technical breakout observed; technicals show uptrend but low volume

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Energy Select Sector SPDR ETF (XLE) Bought: Exxon Leads on Tuesday](https://finance.yahoo.com/energy/articles/state-street-energy-select-sector-110437639.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Energy Select Sector SPDR ETF (XLE) added to every one of its 21 holdings on Tuesday, Oct. 20,...
- [Sector Update: Energy Stocks Advance Pre-Bell Thursday](https://ca.finance.yahoo.com/news/sector-energy-stocks-advance-pre-132555231.html)  
  <sub>Yahoo! Finance Canada, 1 hour ago</sub>  
  Energy stocks were advancing premarket Thursday, with the State Street Energy Select Sector SPDR ETF (XLE) 1.1% higher. The United States Oil Fund (USO) was...
- [Using Sector ETFs to Spot Changes in Market Leadership for AMEX:XLK by Capitalcom](https://www.tradingview.com/chart/XLK/F1eu6yvk-Using-Sector-ETFs-to-Spot-Changes-in-Market-Leadership/)  
  <sub>TradingView, 22 hours ago</sub>  
  If you have an interest in momentum trading, understanding the ebb and flow of sector leadership is an important part of the process. Sector ETFs offer an...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 66.83 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 65.00 (+2.8%), 50d 64.16 (+4.2%), 200d 58.06 (+15.1%); 50d above 200d
Momentum: RSI(14) 58.5 | MACD 1.285 vs signal 1.053 (histogram 0.232)
Returns: 1d -1.9% | 5d +0.4% | 1m +7.2% | 3m +12.1%
52-week range: 43.60 - 68.24 (now 94.3% of the way up)
Volatility: ATR(14) 1.35 (2.0% of price) | annualised 20d 20.8%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.51 | P/B 2.47 | P/S 1.70 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +18.3% a year | beta to the market -0.03
Cost and size: expense ratio 0.08% | net assets 39.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.0%, Chevron Corp 18.1%, ConocoPhillips 6.7%, Valero Energy Corp 4.7%, Marathon Petroleum Corp 4.7%
Sector mix: Energy 100.0%
```

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
  Natural gas: 3,567.0 billion cubic feet, +67.0 on the week (a build), 83% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.3% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-19 Barclays: main, Overweight -> Overweight
  - CVX: 2026-10-15 Morgan Stanley: main, Overweight -> Overweight
  - COP: 2026-10-20 Susquehanna: main, Positive -> Positive
  - VLO: 2026-10-22 TD Cowen: main, Hold -> Hold
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 186.42M | fund size: 12.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, modest technical bullishness with low volume, strong analyst coverage limited to <50% of fund, flat fund flows.

**Main reasons it gave:**
- Macro data: yields down slightly, inflation 3.7% in line with expectations, no surprise
- Technicals: price above 20‑day, 50‑day, and 200‑day SMAs; MACD positive; RSI 60.3; volume 0.32× 20‑day average
- Analyst coverage: 42.7% of fund weight, 100% buy, price target +8.2% above current
- Fund flows: flat share count, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Fin Select SPDR (XLF) Sells $37.5 Million of Berkshire on Oct. 20](https://finance.yahoo.com/markets/stocks/articles/state-street-fin-select-spdr-110409310.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Financial Select Sector SPDR ETF (XLF) sold $292.3 million of stock and bought nothing in Tuesday's...
- [State Street Joins the Uncapped Sector ETF Race](https://www.etf.com/sections/features/state-street-joins-uncapped-sector-etf-race)  
  <sub>ETF.com, 10 hours ago</sub>  
  The issuer behind the world's first sector ETFs is now offering versions that give the biggest stocks their full weight.
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...
- [Webull to Introduce Extended-Hours Options Trading, Expanding Access Beyond the Regular Market Session](https://www.tradingview.com/news/prnewswire:5e0da1e8a24f2:0-webull-to-introduce-extended-hours-options-trading-expanding-access-beyond-the-regular-market-session/)  
  <sub>TradingView, 2 hours ago</sub>  
  New trading hours will enable Webull users to trade select stock and ETF options around earnings announcements and other market-moving events during pre-...
- [Using Sector ETFs to Spot Changes in Market Leadership for AMEX:XLK by Capitalcom](https://www.tradingview.com/chart/XLK/F1eu6yvk-Using-Sector-ETFs-to-Spot-Changes-in-Market-Leadership/)  
  <sub>TradingView, 22 hours ago</sub>  
  If you have an interest in momentum trading, understanding the ebb and flow of sector leadership is an important part of the process. Sector ETFs offer an...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 56.25 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 54.61 (+3.0%), 50d 56.12 (+0.2%), 200d 53.69 (+4.8%); 50d above 200d
Momentum: RSI(14) 60.3 | MACD 0.025 vs signal -0.288 (histogram 0.313)
Returns: 1d +0.4% | 5d +1.8% | 1m +3.1% | 3m -0.1%
52-week range: 47.81 - 58.56 (now 78.5% of the way up)
Volatility: ATR(14) 0.70 (1.2% of price) | annualised 20d 11.9%
Volume: 0.32x the 20-day average
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
Three-year record: +21.9% a year | beta to the market 0.75
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.2% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - JPM: 2026-10-15 Citigroup: main, Neutral -> Neutral
  - V: 2026-10-12 Baird: main, Outperform -> Outperform
  - MA: 2026-10-09 Baird: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 883.44M | fund size: 49.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall call; analyst view bullish but limited coverage, flat fund flows, modest technical weakness, high valuation, and no macro surprise.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top 5 holdings (25.7% weight) with +31% price target
- Fund flows: flat share count (0% change) over 1 week and 1 month
- Technicals: price below 20d, 50d, 200d SMAs; RSI 37; low volume (0.55x 20‑day avg)
- Fundamentals: high valuation multiples (P/E 27.43, P/B 6.56) despite strong 3‑year performance
- Macro: no surprise in rates or data; yields up slightly, VIX up, inflation above target

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Industrial SPDR (XLI) Bought: Caterpillar Leads on Tuesday](https://finance.yahoo.com/markets/stocks/articles/state-street-industrial-spdr-xli-110425016.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Industrial Select Sector SPDR ETF (XLI) extended a broad buying streak on Tuesday, Oct. 20,...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Jobless Claims Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131512646.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.9% and the actively tr.
- [Using Sector ETFs to Spot Changes in Market Leadership for AMEX:XLK by Capitalcom](https://www.tradingview.com/chart/XLK/F1eu6yvk-Using-Sector-ETFs-to-Spot-Changes-in-Market-Leadership/)  
  <sub>TradingView, 22 hours ago</sub>  
  If you have an interest in momentum trading, understanding the ebb and flow of sector leadership is an important part of the process. Sector ETFs offer an...
- [Cyclicals Top Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62499965/cyclicals-top-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions alongside Technology.
- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest State Street Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock...
- [iShares North American Tech-Software ETF (IGV) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Find the latest iShares North American Tech-Software ETF (IGV) stock quote, history, news and other vital information to help you with your stock trading...
- [State Street Joins the Uncapped Sector ETF Race](https://finance.yahoo.com/news/state-street-joins-uncapped-sector-083216877.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  The issuer behind the world's first sector ETFs is now offering versions that give the biggest stocks their full weight.
- [What State Street Technology SPDR (XLK) Sold: NVIDIA Leads on Oct. 20](https://finance.yahoo.com/markets/stocks/articles/state-street-technology-spdr-xlk-110445014.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) posted a net outflow of $185.4 million in Tuesday's session,...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 165.33 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 168.44 (-1.8%), 50d 172.63 (-4.2%), 200d 173.13 (-4.5%); 50d below 200d
Momentum: RSI(14) 37.0 | MACD -1.491 vs signal -1.528 (histogram 0.036)
Returns: 1d -1.8% | 5d -1.5% | 1m -2.8% | 3m -9.5%
52-week range: 147.83 - 186.51 (now 45.2% of the way up)
Volatility: ATR(14) 2.55 (1.5% of price) | annualised 20d 14.8%
Volume: 0.55x the 20-day average
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
Three-year record: +20.8% a year | beta to the market 1.01
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
Weighted price target: +31.0% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-14 Oppenheimer: main, Outperform -> Outperform
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - GEV: 2026-10-14 Susquehanna: main, Positive -> Positive
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 136.63M | fund size: 22.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, technical momentum weak, fund flows flat, analyst view bullish but limited coverage, high valuations offset by strong growth.

**Main reasons it gave:**
- No macro surprise: yields down modestly, inflation 3.7% within expectations
- Technical momentum weak: RSI 36.5, MACD negative, volume 0.38x 20‑day avg
- Fund flows flat: share count unchanged over week and month
- Analyst view bullish (100% buy) covering 49.5% of fund with +27.4% price target
- Fund basics show high valuations (P/E 32.04) despite strong 3‑year growth record

<details><summary><b>News</b> — score +0.00</summary>

- [What State Street Technology SPDR (XLK) Sold: NVIDIA Leads on Oct. 20](https://finance.yahoo.com/markets/stocks/articles/state-street-technology-spdr-xlk-110445014.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) posted a net outflow of $185.4 million in Tuesday's session,...
- [State Street Joins the Uncapped Sector ETF Race](https://www.etf.com/sections/features/state-street-joins-uncapped-sector-etf-race)  
  <sub>ETF.com, 10 hours ago</sub>  
  The issuer behind the world's first sector ETFs is now offering versions that give the biggest stocks their full weight.
- [The Technology Select Sector SPDR® Fund (XLK) Stock Price | Quotes & News](https://www.moomoo.com/stock/XLK-US?chain_id=Name1K9-3FXPhg.1ldj9j0&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FTECL-US%22%7D)  
  <sub>Moomoo, 8 hours ago</sub>  
  Track the latest The Technology Select Sector SPDR® Fund (XLK) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF...
- [Using Sector ETFs to Spot Changes in Market Leadership for AMEX:XLK by Capitalcom](https://www.tradingview.com/chart/XLK/F1eu6yvk-Using-Sector-ETFs-to-Spot-Changes-in-Market-Leadership/)  
  <sub>TradingView, 22 hours ago</sub>  
  If you have an interest in momentum trading, understanding the ebb and flow of sector leadership is an important part of the process. Sector ETFs offer an...
- [Gfi Etf Unit Trust - Gf Hkex Tech & Us Tech 100 Index Etf (3599.HK) latest stock news and headlines](https://uk.finance.yahoo.com/quote/3599.HK/news/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Gfi Etf Unit Trust - Gf Hkex Tech & Us Tech 100 Index Etf (3599.HK). 14.150 -0.050 (-0.35%). At close: 13 October at 15:39:47 GMT+8...
- [Cyclicals Top Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62499965/cyclicals-top-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions alongside Technology.
- [Alphabet Slips 2% Despite NASDAQ Rally as Pichai Says Google Cloud Is Giving Up Revenue for AI Capacity; Amazon Dips, Microsoft Holds Steady](https://247wallst.com/investing/2026/10/21/alphabet-slips-2-despite-nasdaq-rally-as-pichai-says-google-cloud-is-giving-up-revenue-for-ai-capacity-amazon-dips-microsoft-holds-steady/?tpid=1685628&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Shares of Alphabet (NASDAQ:GOOGL | GOOGL Price Prediction) are sliding even while the NASADQ 100 is up 1% on Wednesday morning. The market is digesting an...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...
- [JPMorgan-Asia Pacific Eq.Fund A (JP5N.MU) latest stock news and headlines](https://au.finance.yahoo.com/quote/JP5N.MU/news/)  
  <sub>Yahoo Finance Australia, 11 hours ago</sub>  
  JPMorgan-Asia Pacific Eq.Fund A (JP5N.MU). 221.66 -2.64 (-1.18%). As of 8:07:01 am GMT+2. Market open. Related ETF news...
- [LRCX Stock Sinks As Analysts Trim Targets, See Supply Constraints – But Longer-Term Bull Case Remains](https://www.tradingview.com/news/stocktwits:0e64ae180094b:0-lrcx-stock-sinks-as-analysts-trim-targets-see-supply-constraints-but-longer-term-bull-case-remains/)  
  <sub>TradingView, 2 hours ago</sub>  
  Lam Research Corp. (LRCX) shares tumbled more than 8% in Thursday's premarket trading as multiple firms lowered their price targets following the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 182.49 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 193.89 (-5.9%), 50d 189.80 (-3.8%), 200d 168.32 (+8.4%); 50d above 200d
Momentum: RSI(14) 36.5 | MACD -1.508 vs signal 0.345 (histogram -1.853)
Returns: 1d -3.2% | 5d -3.5% | 1m -6.6% | 3m +3.8%
52-week range: 127.50 - 202.00 (now 73.8% of the way up)
Volatility: ATR(14) 3.90 (2.1% of price) | annualised 20d 23.4%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 32.04 | P/B 11.88 | P/S 9.26 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +32.1% a year | beta to the market 1.45
Cost and size: expense ratio 0.08% | net assets 127.30B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 15.5%, Apple Inc 13.6%, Microsoft Corp 10.7%, Advanced Micro Devices Inc 5.1%, Broadcom Inc 4.7%
Sector mix: Technology 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.4% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - AAPL: 2026-10-20 MoffettNathanson: main, Neutral -> Neutral
  - MSFT: 2026-10-21 Guggenheim: reit, Buy -> Buy
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-22 Tigress Financial: init, ? -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 35d
Shares outstanding: 272.06M | fund size: 49.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, modest analyst optimism, technicals near top but overbought with low volume, flat fund flows.

**Main reasons it gave:**
- Macro data in line with expectations: inflation 3.7%, unemployment 4.2%, no rate surprise
- Analyst consensus 100% buy with modest +3.4% price target, indicating limited upside
- Technical indicators show strong uptrend but RSI 71.7 (overbought) and low volume, no decisive break
- Fund flows flat over the past week and month, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Jobless Claims Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131512646.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.9% and the actively tr.
- [Undervalued consumer staples stocks to watch as Q3 earnings season unfolds (XLP:NYSEARCA)](https://seekingalpha.com/news/4655813-undervalued-consumer-staples-stocks-to-watch-as-q3-earnings-season-unfolds)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  As the third-quarter 2026 earnings season unfolds, investors are assessing valuations across the U.S. consumer staples sector, which includes food producers...
- [Centene, Harmony Biosciences lead list of undervalued healthcare stocks (XLV:NYSEARCA)](https://seekingalpha.com/news/4655950-centene-harmony-biosciences-lead-list-of-undervalued-healthcare-stocks)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Q3 2026 healthcare stock valuations: discover 7 undervalued picks led by Centene and Harmony Biosciences, plus key quant ratings investors should review.
- [Sector Update: Consumer Stocks Decline Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-decline-afternoon-194451591.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were lower late Wednesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.8% and the State Street...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-165705593.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Consumer stocks were mixed Wednesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) shedding 0.5% and the State Street...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...
- [State Street Joins the Uncapped Sector ETF Race](https://www.etf.com/sections/features/state-street-joins-uncapped-sector-etf-race)  
  <sub>ETF.com, 10 hours ago</sub>  
  The issuer behind the world's first sector ETFs is now offering versions that give the biggest stocks their full weight.
- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest State Street Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock...
- [State Street Health Care SPDR (XLV) Buys $19.9 Million More Lilly on Tuesday](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110502233.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) reported $125.8 million in ETF activity on Tuesday, Oct. 20,...
- [P&G beats estimates - but $1.4 billion cost squeeze clouds celebration](https://invezz.com/au/news/2026/10/22/pandampg-beats-estimates-but-dollar14b-cost-squeeze-clouds-celebration/)  
  <sub>Invezz, 2 hours ago</sub>  
  Procter & Gamble PG delivered better-than-expected earnings for its fiscal Q1, offering investors evidence that demand for its household staples can...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 88.93 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 83.95 (+5.9%), 50d 84.31 (+5.5%), 200d 84.21 (+5.6%); 50d above 200d
Momentum: RSI(14) 71.7 | MACD 1.272 vs signal 0.610 (histogram 0.662)
Returns: 1d +2.1% | 5d +2.6% | 1m +7.9% | 3m +5.7%
52-week range: 75.60 - 90.01 (now 92.5% of the way up)
Volatility: ATR(14) 1.16 (1.3% of price) | annualised 20d 15.7%
Volume: 0.59x the 20-day average
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
Three-year record: +12.3% a year | beta to the market 0.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.4% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-20 Evercore ISI Group: main, Outperform -> Outperform
  - COST: 2026-10-21 CICC: init, ? -> Outperform
  - PG: 2026-10-20 RBC Capital: reit, Outperform -> Outperform
  - KO: 2026-10-16 Barclays: main, Overweight -> Overweight
  - PM: 2026-10-22 Needham: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 210.17M | fund size: 18.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, technicals show price below 200‑day SMA with low volume, analyst coverage is bullish but limited to ~40% of the fund, and utilities have been trailing in recent market performance.

**Main reasons it gave:**
- Fund flows flat: share count unchanged over 1 week and 1 month
- Technical price below 200‑day SMA, low volume, RSI neutral
- Analyst coverage bullish (+14.4% price target) but only 39.5% of fund weight
- Macro: no rate or data surprise; yields stable, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  State Street Utilities Select Sector SPDR ETF (XLU) · 0.67% · 3.30% · -6.56% · -1.62% · -7.30% · 25.54% · 177.69%. Key Events. Baseline.
- [Cyclicals Top Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62499965/cyclicals-top-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions alongside Technology.
- [Triple Sputter - TalkMarkets](https://t.co/f2d5Xo1fb9)  
  <sub>Howl.link, 15 hours ago</sub>  
  This rapid 'triple sputter' indicates that market optimism is fleeting, signaling potential exhaustion in the current rally.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 42.34 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 40.94 (+3.4%), 50d 41.89 (+1.1%), 200d 44.29 (-4.4%); 50d below 200d
Momentum: RSI(14) 59.6 | MACD 0.157 vs signal -0.072 (histogram 0.229)
Returns: 1d +0.8% | 5d +1.7% | 1m +6.5% | 3m -8.5%
52-week range: 39.25 - 47.73 (now 36.4% of the way up)
Volatility: ATR(14) 0.63 (1.5% of price) | annualised 20d 15.8%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Utilities
What it holds: P/E 17.86 | P/B 2.04 | P/S 2.49 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +16.4% a year | beta to the market 0.40
Cost and size: expense ratio 0.08% | net assets 21.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: NextEra Energy Inc 12.7%, Southern Co 7.7%, Duke Energy Corp 7.2%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.2%
Sector mix: Utilities 100.0%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-21 Bernstein: reit, Outperform -> Outperform
  - SO: 2026-10-22 HSBC: init, ? -> Buy
  - DUK: 2026-10-22 HSBC: init, ? -> Hold
  - CEG: 2026-10-22 HSBC: init, ? -> Buy
  - AEP: 2026-10-22 HSBC: init, ? -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 163.27M | fund size: 6.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bullish analyst view offset by overbought technicals, flat fund flows, and a neutral macro backdrop.

**Main reasons it gave:**
- Analyst view: 44.3% coverage, 100% buy, +4% price target
- Technicals: RSI 70.1 (overbought) and low volume (0.37x 20‑day avg)
- Fund flows: flat share count, no net creation/redemption
- Macro: yields down slightly, VIX up modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Using Sector ETFs to Spot Changes in Market Leadership for AMEX:XLK by Capitalcom](https://www.tradingview.com/chart/XLK/F1eu6yvk-Using-Sector-ETFs-to-Spot-Changes-in-Market-Leadership/)  
  <sub>TradingView, 22 hours ago</sub>  
  If you have an interest in momentum trading, understanding the ebb and flow of sector leadership is an important part of the process. Sector ETFs offer an...
- [State Street Health Care SPDR (XLV) Buys $19.9 Million More Lilly on Tuesday](https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110502233.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Health Care Select Sector SPDR ETF (XLV) reported $125.8 million in ETF activity on Tuesday, Oct. 20,...
- [State Street Joins the Uncapped Sector ETF Race](https://www.etf.com/sections/features/state-street-joins-uncapped-sector-etf-race)  
  <sub>ETF.com, 10 hours ago</sub>  
  The issuer behind the world's first sector ETFs is now offering versions that give the biggest stocks their full weight.
- [Centene, Harmony Biosciences lead list of undervalued healthcare stocks (XLV:NYSEARCA)](https://seekingalpha.com/news/4655950-centene-harmony-biosciences-lead-list-of-undervalued-healthcare-stocks)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Q3 2026 healthcare stock valuations: discover 7 undervalued picks led by Centene and Harmony Biosciences, plus key quant ratings investors should review.
- [Biotech Giants vs. Emerging Innovators: Which ETF Is the Better Buy?](https://finance.yahoo.com/healthcare/articles/biotech-giants-vs-emerging-innovators-095002548.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The VanEck Biotech ETF (NASDAQ:BBH) offers a concentrated play on industry giants, while the State Street SPDR S&P Biotech ETF (NYSEMKT:XBI) provides broad...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 181.41 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 172.05 (+5.4%), 50d 170.90 (+6.1%), 200d 157.97 (+14.8%); 50d above 200d
Momentum: RSI(14) 70.1 | MACD 2.798 vs signal 1.645 (histogram 1.153)
Returns: 1d +1.4% | 5d +2.4% | 1m +7.5% | 3m +11.6%
52-week range: 142.84 - 181.41 (now 100.0% of the way up)
Volatility: ATR(14) 2.81 (1.5% of price) | annualised 20d 18.7%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +13.9% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
Sector mix: Healthcare 100.0%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.0% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-10-21 Barclays: main, Overweight -> Overweight
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-22 Mizuho: main, Outperform -> Outperform
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 197.42M | fund size: 35.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to lack of macro surprise, mixed technicals, flat fund flows, and stable fundamentals despite bullish analyst coverage.

**Main reasons it gave:**
- Treasury yields down 0.05‑0.10% across the curve, no rate surprise
- VIX up to 19.27, elevated volatility
- Price above 20‑day SMA (+3.0%) and 50‑day SMA (+1.4%) but below 200‑day SMA, low volume (0.33× avg)
- Fund flows flat: share count unchanged over 1 week and 1 month
- Analyst view: 100% buy, weighted price target +19.2% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Discretionary (XLY) Adds Amazon and Tesla on Oct. 20](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-xly-110452560.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) extended its run of one-sided ETF activity in...
- [Brinker, Yum China lead restaurant stocks Quant ratings as dining frequency falls (XLY:NYSEARCA)](https://seekingalpha.com/news/4655911-brinker-yum-china-lead-restaurant-stocks-quant-ratings-as-dining-frequency-falls)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Americans are dining out less frequently, with the share of people who said they or their family ate at a restaurant at least once a week falling to 39% in...
- [Tesla’s post-earnings puts 553 ETFs in the spotlight](https://www.tradingview.com/news/seekingalpha:6016f5277094b:0-tesla-s-post-earnings-puts-553-etfs-in-the-spotlight/)  
  <sub>TradingView, 50 minutes ago</sub>  
  Post-earnings trading in Tesla NASDAQ:TSLA shares has intensified the focus on exchange traded funds that carry heavy allocations to the electric-vehicle...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Thursday Amid Jobless Claims Data Release](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-131512646.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.9% and the actively tr.
- [How Might Stock, Bond, And Oil Markets React To The Fed's Rate Decision](https://seekingalpha.com/article/4956068-how-might-stock-bond-and-oil-markets-react-fed-rate-decision)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The Fed's October 2026 rate decision is expected to keep rates steady, with markets now seeing only a 15% chance of a hike. Read the full analysis here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 115.19 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 111.86 (+3.0%), 50d 113.55 (+1.4%), 200d 115.80 (-0.5%); 50d below 200d
Momentum: RSI(14) 60.8 | MACD 0.640 vs signal 0.018 (histogram 0.621)
Returns: 1d -0.3% | 5d +1.6% | 1m +4.1% | 3m +5.3%
52-week range: 105.66 - 124.52 (now 50.5% of the way up)
Volatility: ATR(14) 1.55 (1.3% of price) | annualised 20d 13.5%
Volume: 0.33x the 20-day average
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
Three-year record: +16.0% a year | beta to the market 1.18
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.2% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-19 Morgan Stanley: main, Overweight -> Overweight
  - TSLA: 2026-10-22 JP Morgan: main, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-10-20 Citigroup: main, Buy -> Buy
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 120.25M | fund size: 13.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Price-Driven Insight from (EIS) for Rule-Based Strategy](https://news.stocktradersdaily.com/news_release/8/Price-Driven_Insight_from_EIS_for_Rule-Based_Strategy_102126104402_1792637042.html)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Key findings for Ishares Msci Israel Etf (NYSE: EIS). Near-Term Strong Sentiment Could Influence Mid-Term Neutrality Toward Long-Term Positive Bias...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 119.79 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 120.14 (-0.3%), 50d 122.35 (-2.1%), 200d 123.15 (-2.7%); 50d below 200d
Momentum: RSI(14) 46.5 | MACD -0.672 vs signal -0.937 (histogram 0.265)
Returns: 1d -1.9% | 5d -0.3% | 1m -4.0% | 3m +0.2%
52-week range: 98.34 - 137.69 (now 54.5% of the way up)
Volatility: ATR(14) 1.80 (1.5% of price) | annualised 20d 16.8%
Volume: 0.51x the 20-day average
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
Three-year record: +39.3% a year | beta to the market 1.09
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
Weighted price target: +22.0% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-15 Barclays: main, Overweight -> Overweight
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 2.55M | fund size: 305.48M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [How (EWU) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/20/How_EWU_Movements_Inform_Risk_Allocation_Models_102226023802_1792651082.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Key findings for Ishares Msci United Kingdom Etf (NYSE: EWU). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.63 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 46.89 (+1.6%), 50d 47.66 (-0.1%), 200d 46.89 (+1.6%); 50d above 200d
Momentum: RSI(14) 55.0 | MACD 0.060 vs signal -0.120 (histogram 0.179)
Returns: 1d -0.1% | 5d -0.3% | 1m +1.1% | 3m +0.8%
52-week range: 41.34 - 49.39 (now 78.1% of the way up)
Volatility: ATR(14) 0.48 (1.0% of price) | annualised 20d 12.7%
Volume: 0.19x the 20-day average
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
Three-year record: +20.3% a year | beta to the market 0.71
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
Ratings by weight: buy 59.1% | hold 40.9% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.7% above the current prices
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
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 67.80M | fund size: 3.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares Aerospace ETF vs Tema Space Innovators ETF](https://www.theglobeandmail.com/investing/markets/stocks/BA-N/pressreleases/8296367/ishares-aerospace-etf-vs-tema-space-innovators-etf/)  
  <sub>The Globe and Mail, 16 hours ago</sub>  
  iShares U.S. Aerospace & Defense ETF offers a significantly lower expense ratio of 0.37% compared to 0.75% for Tema Space Innovators ETF.
- [Lockheed Martin Rises 9% as Record Backlog Lifts Outlook; RTX Gains 2%, Northrop Grumman Advances 3%](https://247wallst.com/investing/2026/10/22/lockheed-martin-rises-9-as-record-backlog-lifts-outlook-rtx-gains-2-northrop-grumman-advances-3/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Lockheed Martin (NYSE:LMT | LMT Price Prediction) stock rose 9% to $602.75 on Thursday after the company reported third-quarter results that topped...
- [​AHIC ETF Explained: Holdings, Yield and Credit Risks](https://www.ebc.com/forex/ahic-etf-holdings-yield-credit-risks)  
  <sub>EBC Financial Group, 10 hours ago</sub>  
  Explore AHIC ETF holdings, its 7.05% portfolio yield to maturity, BB/B credit exposure, short-duration risks, fees and early trading liquidity.
- [Lockheed Martin posts earnings beat, but Quant rating keeps it outside top five defense stocks (ITA:BATS)](https://seekingalpha.com/news/4655854-lockheed-martin-posts-earnings-beat-but-quant-rating-keeps-it-outside-top-five-defense-stocks)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  guvendemir/E+ via Getty Images. Lockheed Martin (LMT) ranked seventh among the top 10 U.S. aerospace and defense stocks by Seeking Alpha's Quant Ratings,...
- [iShares U.S. Medical Devices ETF (IHI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IHI/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest iShares U.S. Medical Devices ETF (IHI) stock quote, history, news and other vital information to help you with your stock trading and...
- [U.S. orders evacuation of some embassy staff in Saudi Arabia (update) (ITA:BATS)](https://seekingalpha.com/news/4655461-u-s-readies-evacuation-of-some-embassy-staff-across-gulf-region-report)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Updated at 3:40 p.m. ET: Adds statement from U.S. State Department Spokesperson Tommy Pigott. The U.S. State Department has issued an ordered departure for...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 202.82 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 206.93 (-2.0%), 50d 219.53 (-7.6%), 200d 229.68 (-11.7%); 50d below 200d
Momentum: RSI(14) 33.1 | MACD -3.650 vs signal -4.345 (histogram 0.695)
Returns: 1d -1.4% | 5d -2.0% | 1m -5.2% | 3m -15.5%
52-week range: 198.23 - 253.22 (now 8.3% of the way up)
Volatility: ATR(14) 3.85 (1.9% of price) | annualised 20d 15.7%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 31.87 | P/B 5.88 | P/S 2.95 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +25.4% a year | beta to the market 0.98
Cost and size: expense ratio 0.37% | net assets 12.14B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: GE Aerospace 21.0%, RTX Corp 16.2%, Boeing Co 7.5%, Howmet Aerospace Inc 4.6%, Lockheed Martin Corp 4.6%
Sector mix: Industrials 100.0%
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
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.5% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-19 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - HWM: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - LMT: 2026-10-15 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: +0.0% (2.46M) over 7d | 1 month: -7.6% (-979.85M) over 30d
Shares outstanding: 58.89M | fund size: 11.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [State Street Consumer Discretionary (XLY) Adds Amazon and Tesla on Oct. 20](https://finance.yahoo.com/markets/stocks/articles/state-street-consumer-discretionary-xly-110452560.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Consumer Discretionary Select Sector SPDR ETF (XLY) extended its run of one-sided ETF activity in...
- [Cyclicals Top Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62499965/cyclicals-top-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with cyclical sectors holding two of the top three positions alongside Technology.
- [State Street Utilities Select Sector SPDR ETF (XLU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLU/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest State Street Utilities Select Sector SPDR ETF (XLU) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.17 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 49.82 (+2.7%), 50d 51.02 (+0.3%), 200d 50.96 (+0.4%); 50d above 200d
Momentum: RSI(14) 59.6 | MACD 0.134 vs signal -0.171 (histogram 0.304)
Returns: 1d -0.3% | 5d +1.2% | 1m +1.8% | 3m -0.2%
52-week range: 42.23 - 53.67 (now 78.1% of the way up)
Volatility: ATR(14) 0.69 (1.3% of price) | annualised 20d 12.0%
Volume: 0.29x the 20-day average
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
Three-year record: +12.9% a year | beta to the market 0.85
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.6% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - NEM: 2026-10-20 Citigroup: main, Buy -> Buy
  - FCX: 2026-10-19 Barclays: main, Overweight -> Overweight
  - ECL: 2026-10-05 UBS: main, Buy -> Buy
  - SHW: 2026-10-13 Barclays: init, ? -> Equal-Weight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 71.92M | fund size: 3.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, crowded long with minimal change, heavy roll cost, and recent outflows suggest mixed signals; overall no clear catalyst for a directional bet.

**Main reasons it gave:**
- CFTC large speculators net long 22% of open interest, 100% percentile crowding
- Fund outflows of -17.8% over the past month
- Cost of holding -8.1% annual, indicating heavy roll cost
- No macro surprise: yields down modestly, VIX up 2.8 points, no policy shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 12.14 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 11.99 (+1.3%), 50d 11.57 (+4.9%), 200d 10.16 (+19.5%); 50d above 200d
Momentum: RSI(14) 57.8 | MACD 0.250 vs signal 0.272 (histogram -0.022)
Returns: 1d -0.9% | 5d -2.6% | 1m +6.8% | 3m +25.0%
52-week range: 9.02 - 12.47 (now 90.4% of the way up)
Volatility: ATR(14) 0.19 (1.6% of price) | annualised 20d 22.4%
Volume: 0.41x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +25.0%, commodity +37.2%, gap -12.2% | 6 months: fund +30.0%, commodity +49.0%, gap -19.1% | 12 months: fund +24.9%, commodity +33.0%, gap -8.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 22.0% of open interest (1,179,144 contracts)
Change on the week: +0.2% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +0.1% (31.60K) over 7d | 1 month: -17.8% (-11.38M) over 30d
Shares outstanding: 4.32M | fund size: 52.50M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to lack of a material macro catalyst; bearish signals from positioning change, heavy roll cost, and outflows are offset by modest magnitude and no decisive technical break.

**Main reasons it gave:**
- CFTC positioning: net long fell 4.4% week-over-week
- Cost of holding: -7.6% annual roll cost
- Technicals: RSI 28 (oversold) and price below 20‑day SMA
- Fund flows: 1‑month outflows of -13.2% share count

<details><summary><b>News</b> — score +0.00</summary>

- [Corn Extending Bounce to Thursday Morning](https://www.barchart.com/story/news/8318785/corn-extending-bounce-to-thursday-morning)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Corn prices are up 1 to 2 cents so far on Thursday AM trade. Futures were on the higher side of unchanged by Wednesday's close, as front months were up 1 ¼...
- [U.S. wheat futures sink to 14-week lows on Ukraine peace efforts (WEAT:NYSEARCA)](https://seekingalpha.com/news/4655648-u-s-wheat-futures-sink-to-14-week-lows-on-ukraine-peace-efforts)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  CBOT wheat futures fell to 14-week lows following news that US special envoy Steve Witkoff met with Russia's President Putin in St. Petersburg to discuss a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 17.80 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 18.69 (-4.8%), 50d 19.24 (-7.5%), 200d 18.18 (-2.1%); 50d above 200d
Momentum: RSI(14) 28.0 | MACD -0.403 vs signal -0.303 (histogram -0.100)
Returns: 1d -1.0% | 5d -3.0% | 1m -9.9% | 3m -2.7%
52-week range: 16.47 - 20.29 (now 34.8% of the way up)
Volatility: ATR(14) 0.28 (1.6% of price) | annualised 20d 16.6%
Volume: 0.30x the 20-day average
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
Cost of holding this fund instead of corn itself: -7.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -2.7%, commodity -0.9%, gap -1.8% | 6 months: fund -2.6%, commodity +1.0%, gap -3.6% | 12 months: fund +1.9%, commodity +9.6%, gap -7.6%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

```text
Corn rated good or excellent: 56% of the US crop (week 42 of 2026)
Direction over 3 weeks: steady, +2 points
A better crop means more supply, which reads bearish for the price, and a worse one bullish. The trend matters more than the level, and the market has already seen this: it is published on a schedule everyone trades.
```

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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 13.4% of open interest (1,845,260 contracts)
Change on the week: -4.4% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +3.4% (4.29M) over 7d | 1 month: -13.2% (-19.62M) over 30d
Shares outstanding: 7.27M | fund size: 129.46M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields unchanged (3‑month 4.03%, 10‑year 5.02%)
- RSI 38.3 and price below 20‑day SMA (38.56 vs 39.78)
- Share count down 4.0% over 1 month (outflows)
- Cost of holding -3.8% annual drag

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 38.56 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 39.78 (-3.1%), 50d 39.82 (-3.2%), 200d 37.81 (+2.0%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -0.148 vs signal -0.026 (histogram -0.122)
Returns: 1d -2.5% | 5d -2.3% | 1m -5.1% | 3m +0.5%
52-week range: 30.53 - 41.43 (now 73.6% of the way up)
Volatility: ATR(14) 0.58 (1.5% of price) | annualised 20d 17.5%
Volume: 0.94x the 20-day average
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
Cost of holding this fund instead of copper itself: -3.8% a year -- a steady drag
Measured: 3 months: fund +0.5%, commodity +1.5%, gap -0.9% | 6 months: fund +4.3%, commodity +5.5%, gap -1.2% | 12 months: fund +26.2%, commodity +30.1%, gap -3.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 19.5% of open interest (313,832 contracts)
Change on the week: -0.7% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.1% (14.03M) over 7d | 1 month: -4.0% (-28.69M) over 30d
Shares outstanding: 17.96M | fund size: 692.56M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance – no macro surprise, technicals bearish but no decisive break, modest fundamental drag, flat flows, and crowded short positioning not decisive.

**Main reasons it gave:**
- US Treasury yields down slightly week‑on‑week, no macro surprise
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 33.8, no decisive break
- Positioning: net long 5.2% of OI, short side crowded (8% percentile) and net long decreased 2% week
- Cost of holding: -2.8% annual drag for long positions
- Fund flows flat, no net creation/redemption

<details><summary><b>News</b> — score +0.00</summary>

- [A Recession Is Coming Eventually, and History Says There's a Major Silver Lining for Investors](https://www.fool.com/investing/2026/10/22/a-recession-is-coming-eventually-and-history-says/)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  The last serious recession started in 2008. We might be overdue for another one. Are you ready?
- [First Majestic Silver Corp. (AG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/AG/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest First Majestic Silver Corp. (AG) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Silver ETFs dip nearly 3% as rate hike fears overshadow safe-haven appeal](https://www.business-standard.com/markets/news/silver-etfs-dip-nearly-3-as-rate-hike-fears-overshadow-safe-haven-appeal-126102200681_1.html)  
  <sub>Business Standard, 6 hours ago</sub>  
  Silver exchange-traded funds (ETFs) were under selling pressure on Thursday, October 22, 2026, tracking a fall in precious metals prices.
- [Silver Prices Are Falling: 3 ETFs to Watch](https://www.equitymaster.com/detail.asp?date=10/22/2026&story=7&title=Silver-Prices-Are-Falling-3-ETFs-to-Watch&utm_source=homepage&utm_medium=website&utm_campaign=top-articles&utm_content=link)  
  <sub>Equitymaster, 3 hours ago</sub>  
  Silver is about half its January peak, and nine silver ETFs show 3-year returns within 0.6 points of each other. Here are 3 that stand out from the lot.
- [Russian gold reserves fall to lowest since 2019 after drawdown for 10 straight months (GLD:NYSEARCA)](https://seekingalpha.com/news/4655636-russian-gold-reserves-fall-to-lowest-since-2019-after-drawdown-for-10-straight-months)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  The Bank of Russia sold 200K troy oz of gold in September, equivalent to 6.2 metric tons, lowering Russia's sovereign gold holdings to 72.8M troy oz,...
- [First Majestic Silver Corp. (AG.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/AG.TO/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest First Majestic Silver Corp. (AG.TO) stock quote, history, news and other vital information to help you with your stock trading and...
- [PC Jeweller Slips; Vodafone Idea, Tata Tele, Yes Bank In Focus](https://hdfcsky.com/news/gold-and-silver-etfs-fall-again-as-it-funds-give-back-gains-bank-etfs-hold-up)  
  <sub>HDFC Sky, 6 hours ago</sub>  
  Mumbai, Oct 22: Gold and silver exchange-traded funds (ETFs) lost ground for a second straight session on Thursday, with all 26 gold funds and all 19 silver...
- [Silver/AUD (XAGAUD) Is down 2.12% on Oct 22: What Is Driving the Move?](https://www.tradingkey.com/news/market-movers/262231210-market-movers-xagaud-20261022)  
  <sub>TradingKey, 13 hours ago</sub>  
  Stronger dollar dynamics and elevated Treasury yields drove silver liquidation.Softening industrial activity and ETF redemptions increased market supply...
- [Why silver is trending with investors in 2026](https://www.usatoday.com/story/money/money-management/investing/why-investors-are-buying-silver-in-2026/90084445007/)  
  <sub>USA Today, 19 hours ago</sub>  
  Industrial demand, supply shortages and lower entry costs are keeping silver in focus. Here's what investors should know before buying.
- [China's Silver Imports Buck the Trend as Oil and Yields Call the Tune](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/china-s-silver-imports-buck-the-trend-as-oil-and-yields-call-the-tune/70393726)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  Chinese silver imports rose sharply in September while exports fell 23.7% to 309.77 tonnes, as oil prices and US yields kept pressure on the metal.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 49.79 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 53.63 (-7.2%), 50d 57.19 (-12.9%), 200d 65.06 (-23.5%); 50d below 200d
Momentum: RSI(14) 33.8 | MACD -1.717 vs signal -1.509 (histogram -0.208)
Returns: 1d -4.7% | 5d -4.1% | 1m -14.4% | 3m -5.3%
52-week range: 42.40 - 105.60 (now 11.7% of the way up)
Volatility: ATR(14) 1.53 (3.1% of price) | annualised 20d 39.7%
Volume: 0.73x the 20-day average
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
Cost of holding this fund instead of silver itself: -2.8% a year -- a steady drag
Measured: 3 months: fund -5.3%, commodity -5.7%, gap +0.4% | 6 months: fund -27.2%, commodity -26.7%, gap -0.5% | 12 months: fund +13.7%, commodity +16.5%, gap -2.8%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 5.2% of open interest (108,433 contracts)
Change on the week: -2.0% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 341.45M | fund size: 17.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- CFTC large speculators net long 23.3% with +0.3% weekly change (crowded long)
- Fund flows positive: share count +2.7% week, +1.3% month
- Cost of holding -1.4% annual drag (negative for long)
- Technicals: RSI 39.5, MACD below signal, price below 20-day SMA (mixed bearish signals)
- No macro surprise: yields down slightly, no policy shift

<details><summary><b>News</b> — score +0.00</summary>

- [U.S. wheat futures sink to 14-week lows on Ukraine peace efforts (WEAT:NYSEARCA)](https://seekingalpha.com/news/4655648-u-s-wheat-futures-sink-to-14-week-lows-on-ukraine-peace-efforts)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  CBOT wheat futures fell to 14-week lows following news that US special envoy Steve Witkoff met with Russia's President Putin in St. Petersburg to discuss a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 26.73 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 27.24 (-1.9%), 50d 27.18 (-1.7%), 200d 24.98 (+7.0%); 50d above 200d
Momentum: RSI(14) 39.5 | MACD -0.161 vs signal -0.047 (histogram -0.115)
Returns: 1d +0.5% | 5d -0.8% | 1m -4.5% | 3m +1.7%
52-week range: 21.71 - 28.14 (now 78.1% of the way up)
Volatility: ATR(14) 0.27 (1.0% of price) | annualised 20d 10.9%
Volume: 0.58x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.00</summary>

```text
Cost of holding this fund instead of soybeans itself: -1.4% a year -- a steady drag
Measured: 3 months: fund +1.7%, commodity +1.4%, gap +0.3% | 6 months: fund +9.4%, commodity +9.1%, gap +0.3% | 12 months: fund +21.4%, commodity +22.8%, gap -1.4%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 23.3% of open interest (1,072,235 contracts)
Change on the week: +0.3% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +2.7% (1.20M) over 7d | 1 month: +1.3% (565.75K) over 30d
Shares outstanding: 1.70M | fund size: 45.35M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Net short position increased by 0.7% of open interest (small bearish bias)
- Natural gas inventories built 77 BCF, 87th percentile (bearish)
- Cost of holding -4.8% annual drag (bearish for long)
- EIA price outlook mixed: price up to $4.01 in 3 months then down to $2.59 in 6 months (neutral)
- No macro surprise or decisive technical break (neutral overall)

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.05 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 10.68 (-6.0%), 50d 10.49 (-4.2%), 200d 11.25 (-10.7%); 50d below 200d
Momentum: RSI(14) 40.5 | MACD -0.050 vs signal 0.065 (histogram -0.115)
Returns: 1d +0.8% | 5d -9.4% | 1m -7.6% | 3m -4.8%
52-week range: 9.63 - 16.90 (now 5.7% of the way up)
Volatility: ATR(14) 0.37 (3.6% of price) | annualised 20d 41.8%
Volume: 0.28x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -4.8% a year -- a steady drag
Measured: 3 months: fund -4.8%, commodity -1.7%, gap -3.1% | 6 months: fund -4.5%, commodity +8.0%, gap -12.5% | 12 months: fund -23.6%, commodity -18.8%, gap -4.8%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.07</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.07</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 7.3% of open interest (1,741,163 contracts)
Change on the week: +0.7% of open interest
Crowding: 12% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.07</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 12.08M | fund size: 121.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no material macro surprise, policy shift, or decisive technical breakout observed. Scores reflect slight bearish tilt from positioning and fundamentals but overall call remains neutral.

**Main reasons it gave:**
- Energy inventories draw of 3.1 million barrels (bullish)
- EIA price outlook forecasts WTI $100 now falling to $86 in 6 months (bearish)
- CFTC speculators net long decreased by 0.7% of OI (bearish)
- Technicals show price above 20d, 50d, 200d SMA with positive momentum (bullish)

<details><summary><b>News</b> — score +0.00</summary>

- [Sector Update: Energy Stocks Advance Pre-Bell Thursday](https://ca.finance.yahoo.com/news/sector-energy-stocks-advance-pre-132555231.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Energy stocks were advancing premarket Thursday, with the State Street Energy Select Sector SPDR ETF (XLE) 1.1% higher. The United States Oil Fund (USO) was...
- [Trump administration taps heating oil reserve in bid to lower prices as election looms](https://seekingalpha.com/news/4655649-trump-administration-taps-heating-oil-reserve-in-bid-to-lower-prices-as-election-looms)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  The US Department of Energy said it will loan up to 315M barrels of heating oil stockpiled in Maine, Massachusetts, and Connecticut in an effort to bring...
- [SpaceX's Strong AI Computing Returns And Hidden Risk - United States Oil Fund (ARCA:USO), State Street SP](https://www.benzinga.com/opinion/26/10/62501333/spacex-strong-ai-computing-returns-and-hidden-risk)  
  <sub>Benzinga, 24 hours ago</sub>  
  AI Trade Character Is Changing Please click here for an enlarged chart of Space Exploration Technologies Corp (NASDAQ:SPCX). Note the following: This...
- [Why Did NKE, OPEN, NCLH Stocks Slump To 52-Week Lows Today?](https://stocktwits.com/news-articles/markets/equity/why-did-nke-open-nclh-stocks-slump-to-52-week-lows-today/cZtXPSMRJ6C)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Shares of Nike, Opendoor Technologies, and Norwegian Cruise Line fell to 52-week lows amid negative company catalysts and overall macroeconomic and sectoral...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...
- [U.S. orders evacuation of some embassy staff in Saudi Arabia (update) (ITA:BATS)](https://seekingalpha.com/news/4655461-u-s-readies-evacuation-of-some-embassy-staff-across-gulf-region-report)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Updated at 3:40 p.m. ET: Adds statement from U.S. State Department Spokesperson Tommy Pigott. The U.S. State Department has issued an ordered departure for...
- [USO Plays The Path; Bulls Break Higher On Strong Oil Prices - TalkMarkets](https://t.co/BsTBIJc3o7)  
  <sub>Howl.link, 14 hours ago</sub>  
  United States Oil Fund has broken higher toward the $180 level, extending a major bullish cycle driven by surging crude oil prices.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 160.83 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 151.61 (+6.1%), 50d 145.55 (+10.5%), 200d 121.09 (+32.8%); 50d above 200d
Momentum: RSI(14) 64.5 | MACD 4.263 vs signal 3.414 (histogram 0.849)
Returns: 1d +0.6% | 5d +2.2% | 1m +8.1% | 3m +17.7%
52-week range: 66.17 - 161.86 (now 98.9% of the way up)
Volatility: ATR(14) 4.85 (3.0% of price) | annualised 20d 32.0%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 205.3 million barrels, -3.0 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 104.3 million barrels, +1.7 on the week (a build), 25% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 2.1% of open interest (1,900,179 contracts)
Change on the week: -0.7% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 34d
Shares outstanding: 119.10M | fund size: 19.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- CFTC: net short 6.4% of open interest, change -0.6% (week)
- Cost of holding: -11.2% annual roll cost (heavy, tailwinds short)
- Macro: no policy or data surprise; yields stable, inflation 3.7% vs target 4.0%
- Technicals: price below 20d/50d/200d SMAs, RSI 25.1, volume 0.45x average

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat Holding on the Lower Side of Unchanged to Start Thursday](https://www.barchart.com/story/news/8318809/wheat-holding-on-the-lower-side-of-unchanged-to-start-thursday)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Wheat is trading with just modest losses on Thursday morning, following midweek losses. The wheat complex saw Wednesday weakness across the three markets,...
- [U.S. wheat futures sink to 14-week lows on Ukraine peace efforts (WEAT:NYSEARCA)](https://seekingalpha.com/news/4655648-u-s-wheat-futures-sink-to-14-week-lows-on-ukraine-peace-efforts)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  CBOT wheat futures fell to 14-week lows following news that US special envoy Steve Witkoff met with Russia's President Putin in St. Petersburg to discuss a...
- [Wheat Falls on Wednesday with Black Sea News](https://www.barchart.com/story/news/8293544/wheat-falls-on-wednesday-with-black-sea-news)  
  <sub>Barchart.com, 18 hours ago</sub>  
  The wheat complex saw Wednesday weakness across the three markets, pressured by Black Sea news. Chicago SRW contracts fell 7 ½ to 16 ½ cents at the close.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 22.82 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 24.45 (-6.7%), 50d 25.51 (-10.6%), 200d 23.47 (-2.8%); 50d above 200d
Momentum: RSI(14) 25.1 | MACD -0.626 vs signal -0.466 (histogram -0.160)
Returns: 1d -1.2% | 5d -6.0% | 1m -11.1% | 3m -9.5%
52-week range: 19.88 - 28.00 (now 36.2% of the way up)
Volatility: ATR(14) 0.47 (2.1% of price) | annualised 20d 17.9%
Volume: 0.45x the 20-day average
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
Cost of holding this fund instead of wheat itself: -11.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -9.5%, commodity -8.2%, gap -1.3% | 6 months: fund -2.5%, commodity +1.9%, gap -4.4% | 12 months: fund +13.3%, commodity +24.4%, gap -11.2%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-13, published the following Friday)
Large speculators: net short 6.4% of open interest (506,774 contracts)
Change on the week: -0.6% of open interest
Crowding: 58% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +3.8% (10.00M) over 7d | 1 month: -13.8% (-44.15M) over 30d
Shares outstanding: 12.07M | fund size: 275.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Webull to Introduce Extended-Hours Options Trading, Expanding Access Beyond the Regular Market Session](https://www.tradingview.com/news/prnewswire:5e0da1e8a24f2:0-webull-to-introduce-extended-hours-options-trading-expanding-access-beyond-the-regular-market-session/)  
  <sub>TradingView, 2 hours ago</sub>  
  New trading hours will enable Webull users to trade select stock and ETF options around earnings announcements and other market-moving events during pre-...
- [Webull introduces extended trading hours after Intercontinental Exchange, Cboe (BULL:NASDAQ)](https://seekingalpha.com/news/4655952-webull-introduces-extended-trading-hours-after-intercontinental-exchange-cboe)  
  <sub>Seeking Alpha, 57 minutes ago</sub>  
  Webull (BULL) on Thursday announced the launch of extended-hours trading for select single-stock and exchange-traded fund options.
- [Webull launches extended-hours options trading for U.S. customers](https://www.streetinsider.com/Corporate+News/Webull+launches+extended-hours+options+trading+for+U.S.+customers/27220131.html)  
  <sub>StreetInsider, 2 hours ago</sub>  
  Webull (NASDAQ: BULL) has introduced extended-hours trading for select single-stock and ETF options, allowing eligible U.S. customers to trade outside the...
- [iShares Gold Trust (IAU) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IAU/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest iShares Gold Trust (IAU) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Jim Cramer Names Bitcoin and Ethereum as Established Cryptocurrencies](https://logos-pres.md/en/news/jim-cramer-named-the-top-2-cryptocurrencies-for-investors/)  
  <sub>logos-pres.md, 8 hours ago</sub>  
  The CNBC host prefers gold to hedge a portfolio but favors Bitcoin and Ethereum over low-quality tokens, warning investors about speculative crypto assets.
- [GLD NTA 21-10-2026 $3.82946](https://www.businessdesk.co.nz/nzx-announcements/gld-etf-units/482213/)  
  <sub>BusinessDesk, 18 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 21-10-2026 $3.82946. Financial updates and company disclosures on BusinessDesk.
- [Russian gold reserves fall to lowest since 2019 after drawdown for 10 straight months (GLD:NYSEARCA)](https://seekingalpha.com/news/4655636-russian-gold-reserves-fall-to-lowest-since-2019-after-drawdown-for-10-straight-months)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  The Bank of Russia sold 200K troy oz of gold in September, equivalent to 6.2 metric tons, lowering Russia's sovereign gold holdings to 72.8M troy oz,...
- [Exchange-Traded Funds Higher as US Equities Rise After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171218843.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1.3%. US equity indexes rose as a...
- [Day 508: Rate Hike + Trump 2.0 Day 639](https://www.moomoo.com/community/feed/day-508-rate-hike-trump-2-0-day-639-117485067894790)  
  <sub>Moomoo, 38 minutes ago</sub>  
  Market Recap | Thursday, October 22, 2026 The Beat That Bought a Bill Yesterday's poll asked how the market would greet Meta. The answer came b...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.03% (-0.05 on the week) | 5-year 4.83% (-0.07 on the week) | 10-year 5.02% (-0.07 on the week) | 30-year 5.33% (-0.10 on the week)
Yield curve, 10-year minus 3-month: +0.98 points -- upward sloping (normal)
US dollar index: 101.87 (-0.13 on the week)
Volatility (VIX): 19.27 (+2.8 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.79% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 371.48 (bar of 2026-10-22), from 502 daily bars
Trend: vs 20d SMA 380.56 (-2.4%), 50d 395.20 (-6.0%), 200d 414.43 (-10.4%); 50d below 200d
Momentum: RSI(14) 37.3 | MACD -4.473 vs signal -4.418 (histogram -0.054)
Returns: 1d -2.0% | 5d -2.9% | 1m -5.4% | 3m -0.1%
52-week range: 362.32 - 495.90 (now 6.9% of the way up)
Volatility: ATR(14) 5.74 (1.5% of price) | annualised 20d 21.2%
Volume: 0.57x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.8% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -0.1%, commodity +0.2%, gap -0.3% | 6 months: fund -13.8%, commodity -13.7%, gap -0.1% | 12 months: fund -1.5%, commodity -0.8%, gap -0.8%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-10-13, published the following Friday)
Large speculators: net long 27.0% of open interest (396,345 contracts)
Change on the week: -1.0% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 30d
Shares outstanding: 260.30M | fund size: 96.70B
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

