# Daily report

**27 Oct 2026, 17:55 Israel time (15:55 UTC)** · 80 names checked · 3 traded · 0 with a problem

**Answers with no explanation:** 13 of 68 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 5 | 11 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 2 | 39 | 0 |
| Commodities | 9 | 1 | 8 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Royal Bank of Canada (RY) · Company | **Sold part.** Sold 5 of 17 shares at +1.06R, 12 still held. Stop-loss raised 195.67 → 196.13. |
| Israel (EIS) · Sector or country | **Stop raised.** At +0.60R, following the price. Stop-loss raised 118.59 → 120.47. |
| US company bonds, riskier (HYG) · Index fund | **Stop raised.** At +0.37R, following the price. Stop-loss raised 76.70 → 76.76. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.12R, following the price. Stop-loss raised 323.17 → 323.76. |
| Microsoft (MSFT) · Company | **Stop raised.** At +0.04R, following the price. Stop-loss raised 509.74 → 511.25. |
| US materials and chemicals (XLB) · Sector or country | **Stop raised.** At +0.33R, following the price. Stop-loss raised 50.09 → 50.13. |
| ASML (ASML) · Company | **Holding.** +0.23R, holding 3 shares. Stop-loss 1684.98. |
| Brazil (EWZ) · Sector or country | **Holding.** -0.29R, holding 210 shares. Stop-loss 36.81. |
| Gold (GLD) · Commodity | **Holding.** +1.16R, holding 7 shares. Stop-loss 378.03. |
| Eli Lilly (LLY) · Company | **Holding.** +2.25R, holding 3 shares. Stop-loss 1233.74. |
| Nvidia (NVDA) · Company | **Holding.** -0.00R, holding 23 shares. Stop-loss 225.68. |
| Exxon Mobil (XOM) · Company | **Holding.** +2.72R, holding 9 shares. Stop-loss 174.71. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### HDFC Bank (HDB) · Company — NEUTRAL, confidence 0.62

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The stock is at a fresh 52‑week low with weak technicals (price below 20‑day, 50‑day, 200‑day SMAs; RSI 37.5; MACD negative) and a high valuation (P/B 8.55). Analyst consensus remains bullish (buy) with a +41% price target, but no insider buying activity is present. Overall, bearish news and technical signals outweigh the bullish analyst view, leading to a neutral stance with moderate conviction.

**Main reasons it gave:**
- HDFC Bank hit a fresh 52‑week low at $21.71 (news)
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 37.5; MACD negative (technical)
- Trailing P/E 13.86, forward P/E 15.55, P/B 8.55 indicating high valuation (fundamentals)
- Consensus buy with mean price target $30.30 (+41% upside) (analyst view)

<details><summary><b>News</b> — score -0.70</summary>

- [HDFC Bank Falls to a Fresh 52-Week Low at $21.71](https://247wallst.com/cards/hdfc-bank-just-marked-a-new-52-week-low-at-21-71-0-6-unde-hdb-price-extreme-01m5x9qdbvrr6vhxw06pec0c57)  
  <sub>24/7 Wall St., 13 hours ago</sub>  
  HDFC Bank just marked a new 52-week low at $21.71, 0.6% under the prior floor set on September 10. The $111.7 billion lender has spent the past year...
- [VN-Index down slightly due to lingering selling pressure](https://vietnamnews.vn/economy/1802993/vn-index-down-slightly-due-to-lingering-selling-pressure.html)  
  <sub>vietnamnews.vn, 5 hours ago</sub>  
  Selling pressure across several banking stocks offset gains in selected large-cap and steel shares.
- [HDFC Bank (NYSE:HDB) Reaches New 52-Week Low - Time to Sell?](https://www.marketbeat.com/instant-alerts/price-hdfc-bank-nyse-hdb-reaches-new-52-week-low-time-to-sell-2026-10-26/)  
  <sub>MarketBeat, 21 hours ago</sub>  
  HDFC Bank Limited (NYSE:HDB - Get Free Report)'s stock price hit a new 52-week low during trading on Monday. The stock traded as low as $21.66 and last...
- [Stock market on October 27th: Energy stocks and other stocks under pressure, VN-Index loses nearly 2 points.](https://www.vietnam.vn/en/chung-khoan-ngay-27-10-co-phieu-nang-luong-chung-khoan-chiu-ap-luc-vn-index-mat-gan-2-diem)  
  <sub>Vietnam.vn, 2 hours ago</sub>  
  On October 27th, the Vietnamese stock market traded predominantly in the red, with the energy sector falling 1.41%, securities down 0.85%, and banking down...
- [HDB stock pre-market at EUR 19.55: Indian bank before Xetra open](https://www.ad-hoc-news.de/boerse/news/vorboerse/hdb-stock-pre-market-at-eur-19-55-indian-bank-before-xetra-open/70417924)  
  <sub>ad-hoc-news.de, 8 hours ago</sub>  
  HDFC Bank serves individuals, businesses and institutions through banking services. At Lang & Schwarz the stock trades pre-market at EUR 19.55 on October 27...
- [Jio IPO: Can India’s biggest-ever issue buck the trend of muted listing gains among mega IPOs?](https://m.economictimes.com/markets/ipos/fpos/jio-ipo-can-indias-biggest-ever-issue-buck-the-trend-of-muted-listing-gains-among-mega-ipos/articleshow/135224855.cms)  
  <sub>The Economic Times, 10 hours ago</sub>  
  Jio Platforms is gearing up for a groundbreaking debut on October 28, following a remarkable Rs 30188 crore IPO. Historical insights indicate a varied...
- [HDFC Bank stock hits a 52-week low despite Q2 profit growth](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdfc-bank-stock-hits-a-52-week-low-despite-q2-profit-growth/70418506)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  HDFC Bank stock traded at EUR 19.55 on October 27, 2026. Q2 profit rose 4.70 percent to INR 195.10 billion, while NYSE shares hit USD 21.66.
- [Jio IPO brings a smaller payday for bankers than other large offers](https://m.economictimes.com/markets/stocks/news/jio-ipo-brings-a-smaller-payday-for-bankers-than-other-large-offers/amp_articleshow/135222126.cms)  
  <sub>The Economic Times, 14 hours ago</sub>  
  In a landmark move, Jio Platforms, supported by Mukesh Ambani, successfully secured ₹30213 crore, marking the largest IPO in Indias history.
- [HDFC Bank Announces Leadership Transition: Anup Bagchi Takes Charge as MD & CEO Following Tenure Completion of Sashidhar Jagdishan](https://www.equitybulls.com/news/377767/hdfc-bank-announces-leadership-transition-anup-bagchi-takes-charge-as-md-ceo-fol)  
  <sub>EquityBulls, 10 hours ago</sub>  
  HDFC Bank Limited has announced the change in its Managing Director and Chief Executive Officer (MD & CEO).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 21.49 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 22.52 (-4.6%), 50d 22.78 (-5.7%), 200d 25.98 (-17.3%); 50d below 200d
Momentum: RSI(14) 37.5 | MACD -0.205 vs signal -0.085 (histogram -0.120)
Returns: 1d -1.0% | 5d -6.8% | 1m -4.1% | 3m -10.6%
52-week range: 21.49 - 37.13 (now 0.0% of the way up)
Volatility: ATR(14) 0.53 (2.5% of price) | annualised 20d 28.8%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 110.49B
Valuation: trailing P/E 13.86 | forward P/E 15.55 | P/B 8.55 | PEG n/a
Profitability: profit margin 26.5% | operating margin 38.5% | ROE 11.0%
Growth (YoY): revenue +80.8% | earnings +21.3%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2027-01-16
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.30 (+41.0% vs last close), range 26.20 - 33.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

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

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Positive Q1 earnings beat and analyst consensus buy with upside price target, supported by technicals above key moving averages and a net insider purchase. Fundamentals are solid but growth is modest and valuation appears stretched (high PEG), tempering conviction. Overall view is a modest bullish stance.

**Main reasons it gave:**
- Q1 earnings beat by 3% (2026-09-30)
- Analyst consensus buy, mean rating 2.08, price target +8.9% vs last close
- Price above 20d, 50d, 200d SMAs; MACD positive (3.679 vs 3.193)
- Forward P/E 21.5, PEG 4.14 (high) indicating modest growth vs valuation
- Insider net purchase of 99,030 shares (+4.8% of holdings)

<details><summary><b>News</b> — score +0.50</summary>

- [The Procter & Gamble Company (PG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  The Procter & Gamble Company (PG) · 1.41% · 9.36% · 7.92% · 11.59% · 4.87% · 11.95% · 11,147.12%. Key Events. Baseline. Advanced Chart. Loading chart for...
- [Procter & Gamble (PG) Stock May Be 23% Undervalued As Q1 Beat Lifts Outlook](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-stock-may-080558444.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Procter & Gamble has delivered steady gains in recent years, so the question now is whether the current share price lines up with the cash flows investors...
- [Up 16% This Year, How Long Can Procter & Gamble Continue Outperforming the S&P 500?](https://www.fool.com/investing/2026/10/27/up-16-this-year-how-long-can-procter-gamble-contin/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Defensive consumer staples stocks are back in the limelight, with the sector on pace for its best monthly showing in 28 years. Count Procter & Gamble (PG...
- [How Bad Would Higher Oil Prices Be For Procter & Gamble Stock?](https://www.trefis.com/stock/pg/articles/620505/how-bad-would-higher-oil-prices-be-for-procter-gamble-stock/2026-10-26)  
  <sub>Trefis, 19 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. With oil staying expensive, Procter & Gamble (PG) holders want to know what...
- [Is Trending Stock Procter & Gamble Company (The) (PG) a Buy Now?](https://finance.yahoo.com/markets/stocks/articles/trending-stock-procter-gamble-company-120003097.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Zacks.com users have recently been watching P&G (PG) quite a bit. Thus, it is worth knowing the facts that could determine the stock's prospects.
- [PG Maintains Equal-Weight Rating -- Price Target Raised to $165](https://www.gurufocus.com/news/9142639/pg-maintains-equalweight-rating-price-target-raised-to-165)  
  <sub>GuruFocus, 21 hours ago</sub>  
  Procter & Gamble Analyst Rating Update - October 2023 On October 23, 2023, Barclays maintained an Equal-Weight rating on Procter & Gamble (PG).
- [After exercising options at $78.52 per share, Procter & Gamble (PG) CEO sells shares.](https://www.stocktitan.net/sec-filings/PG/form-4-procter-gamble-co-insider-trading-activity-c13f11885e0a.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Shailesh Jejurikar exercised 35000 options and sold shares at an average $163.0871 on October 23, 2026. No Rule 10b5-1 plan was reported.
- [Procter & Gamble (NYSE:PG) Stock: Insider Shailesh Jejurikar Sells 35,000 Shares](https://www.google.com/goto?url=CAESxAEB6zswFba4q-nK96OThq5heOEBLS_bPIjtHxgFnKV-sZm--gd1Yg1oTiKYkPD-JoWaSgjUfpcutHFMqwgoHgZBOa15vhLoH4_3JRijkGkT7GTMye_6GpFa8nxNsNuKbSe5IoszsQh0wrXaiRBRzLu-IXsr4mswtYLSaU8Su94Hi8SC-FAdbYgUmiz8k7jLWghdklc_7xuZKTMQCRwKtJGS_XdROPoRSu-27JVckTDwhAZM2FOoTuXrfz84B_wFA90fpbCd)  
  <sub>MarketBeat, 17 hours ago</sub>  
  Procter & Gamble Company (The) (NYSE:PG - Get Free Report) CEO Shailesh Jejurikar sold 35000 shares of the business's stock in a transaction that occurred...
- [Procter & Gamble Insiders Sold Shares Worth Over $1.3M](https://www.tradingview.com/news/tradingview:2ad7f8bb8439b:0-procter-gamble-insiders-sold-shares-worth-over-1-3m/)  
  <sub>TradingView, 23 hours ago</sub>  
  Gama Paul, an officer serving as CEO- Health Care, sold 4331 shares of Procter & Gamble common stock at $161.27 per share for a total of $698460.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 159.20 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 153.85 (+3.5%), 50d 149.00 (+6.8%), 200d 148.69 (+7.1%); 50d above 200d
Momentum: RSI(14) 59.8 | MACD 3.679 vs signal 3.193 (histogram 0.486)
Returns: 1d -0.5% | 5d -0.1% | 1m +6.8% | 3m +9.0%
52-week range: 138.04 - 167.20 (now 72.5% of the way up)
Volatility: ATR(14) 3.03 (1.9% of price) | annualised 20d 28.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 368.98B
Valuation: trailing P/E 23.98 | forward P/E 21.51 | P/B 6.79 | PEG 4.14
Profitability: profit margin 18.2% | operating margin 27.1% | ROE 29.6%
Growth (YoY): revenue +4.0% | earnings +0.8%
Balance sheet: debt/equity 70.3% | free cash flow 12.66B
Risk: beta 0.38 | short interest 1.1% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 191,293 shares in 43 transaction(s) | sold 92,263 shares in 19
Net: +99,030 shares (+4.8% of insider holdings) | insiders hold 2,155,538 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-23 PURUSHOTHAMAN BALAJI (Officer): 4,181 shares, 671.93K
  - 2026-10-23 GAMA PAUL (Officer): 4,331 shares, 698.46K
  - 2026-10-23 JEJURIKAR SHAILESH (Chief Executive Officer): 35,000 shares, 5.71M
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
(41 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “Buy”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Acquisition of BXCL501, a dexmedetomidine sublingual film under FDA review (Yahoo Finance, 3h ago)
- Analyst consensus strong buy; mean price target +17% above current price (Analyst view)
- Forward P/E 13.13 and PEG 0.71 suggest undervaluation relative to growth (Fundamentals)
- Volume 0.33x 20‑day average indicates thin trading (Technical)

<details><summary><b>News</b> — score +0.30</summary>

- [Teva Acquires Worldwide Rights to BXCL501, Further Expanding Innovative Neuroscience Pipeline](https://www.google.com/goto?url=CAESngEB6zswFdts-6BbDETEylKJAiTKW2VaBwZsCb1YpLm1OzZRsFDfn4EZmN5aDHyX-jH0sjUuUkAqlglsaZDPpuFPBOfsalptsHYeRqlbq0YkdNyv0zRNKeLg1XL1wWKp8-6LVo31gVaZKpNyhsSvLvuQPgfeudv1gOFR4rm241xtoKTmxBELrWm9EAvMxlgOjj3RBmdc0H-MDLYVSAddJA)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  BXCL501, a dexmedetomidine sublingual film, is under FDA review for first-ever at-home use for the acute treatment of agitation associated with...
- [Teva's Austedo-Led Turnaround Faces A Margin Test As Generics Drag On Third-Quarter Results](https://www.google.com/goto?url=CAEStAEB6zswFdIbR9N36B7BrVEMUbWnvoH9NW3iOz9p6mAxMgslFT81oOYD61wbKlWk6CPNJDlbNoEMrI2Xjdq-8S72JAwldYNG4Wz3n8ACLuTwHPbhaU1kUmkNIK0PDc4-UBOLJFI856QwpNLKusBT8kAsjNopR530eWgtJUHyQi5-ZxCwpfoD6zxVCqq7O79Lb-5mt2Tys2lkyRDgMCd6PlURvCXNq9z15l3B62XLw9SsvITBHo8)  
  <sub>Finviz, 16 hours ago</sub>  
  Stock screener for investors and traders, financial visualizations.
- [Teva Pharmaceutical Industries (TEVA) Expected to Release Quarterly Earnings on Tuesday](https://www.marketbeat.com/instant-alerts/upcoming-teva-pharmaceutical-industries-teva-expected-to-release-quarterly-earnings-on-tuesday-2026-10-27/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Teva Pharmaceutical Industries (NYSE:TEVA) will be releasing its Q3 2026 earnings before the market opens on Tuesday, November 3. (View Earnings Report at...
- [AUPH Stock Rallies 6% After-Hours — Here’s Why](https://stocktwits.com/news-articles/markets/equity/auph-stock-rallies-6-after-hours-here-s-why/cZYdw3NRJlt)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Under the deal, Teva agreed that two of Aurinia's key U.S. patents, expiring in December 2037, are valid, enforceable, and would be infringed by its generic...
- [Teva reports 44-week duvakitug data for Teva stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/teva-reports-44-week-duvakitug-data-for-teva-stock/70418401)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  Duvakitug retained 58 percent remission at Week 44. Teva stock enters November 3 results after USD 4.14 billion second-quarter revenue.
- [Bausch Health Companies Inc. (BHC) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/BHC/)  
  <sub>Yahoo Finance Singapore, 11 hours ago</sub>  
  Find the latest Bausch Health Companies Inc. (BHC) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Israel stocks higher at close of trade; TA 35 up 1.99%](https://www.investing.com/news/stock-market-news/israel-stocks-higher-at-close-of-trade-ta-35-up-199-4973267)  
  <sub>Investing.com, 22 hours ago</sub>  
  Investing.com – Israel stocks were higher after the close on Monday, as gains in the Real Estate, Oil & Gas and Insurance sectors led shares higher.
- [Mon: TASE jumps ahead of elections](https://en.globes.co.il/en/article-mon-tase-jumps-ahead-of-elections-1001560919)  
  <sub>Globes - Israel Business News, 20 hours ago</sub>  
  The Tel Aviv Stock Exchange rose strongly today. The Tel Aviv 35 Index rose 1.99% to 4,206.35 points, the Tel Aviv 125 Index rose 1.81% to 4,108.05 points;...
- [Netlist Bags Federal Circuit Win After Court Rejects Micron’s Patent Challenge](https://stocktwits.com/news-articles/markets/equity/netlist-bags-federal-circuit-win-rejects-micron-patent-challenge/cZRNkluR4xw)  
  <sub>Stocktwits, 14 hours ago</sub>  
  The U.S. Court of Appeals for the Federal Circuit upheld the validity of the patents in an opinion on Friday, saying Micron failed to prove unpatentability...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 40.54 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 40.27 (+0.7%), 50d 38.83 (+4.4%), 200d 34.45 (+17.7%); 50d above 200d
Momentum: RSI(14) 55.4 | MACD 0.455 vs signal 0.644 (histogram -0.189)
Returns: 1d +1.5% | 5d -0.7% | 1m +4.3% | 3m +16.8%
52-week range: 19.61 - 41.50 (now 95.6% of the way up)
Volatility: ATR(14) 1.11 (2.7% of price) | annualised 20d 22.9%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 47.29B
Valuation: trailing P/E 67.58 | forward P/E 13.13 | P/B 6.09 | PEG 0.71
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.82 | short interest 2.6% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: strong_buy (mean 1.46 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 4 strong buy, 8 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 47.58 (+17.4% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-15 Barclays: main, Overweight -> Overweight
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
Institutional ownership: 27.3%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

> The company shows strong fundamentals and analyst support, a recent dividend hike, and a solid earnings beat record, while technicals are bearish and insider activity is neutral. Overall the bullish factors outweigh the bearish technicals, leading to a moderate‑conviction BUY signal.

**Main reasons it gave:**
- Sixth consecutive 8% dividend hike signals confidence
- Technical indicators show price below 20/50/200‑day SMAs and low volume (bearish)
- Revenue up 24% YoY, earnings up 68% YoY, ROE 57% indicates strong fundamentals
- Consensus buy with mean price target +31% above current price
- Four straight earnings beats suggest continued outperformance

<details><summary><b>News</b> — score +0.20</summary>

- [Toromont Industries Ltd. (TIH.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TIH.TO/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest Toromont Industries Ltd. (TIH.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Caterpillar vs. Deere: Which Heavy Equipment Dividend Is Growing Faster?](https://247wallst.com/investing/2026/10/27/caterpillar-vs-deere-which-heavy-equipment-dividend-is-growing-faster/?tpid=1689353&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Caterpillar made its sixth consecutive 8% dividend hike to $1.63 per quarter while Deere has held its payout flat for two years.
- [Red Cat Holdings: The Risk/Reward Has Shifted In Investors' Favor (NASDAQ:RCAT)](https://seekingalpha.com/article/4957900-red-cat-holdings-the-riskreward-has-shifted-in-investors-favor)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Red Cat stock has plunged, but revenue growth, drone market expansion, and a low valuation may offer upside. Click for more on RCAT stock.
- [Analysts Have Conflicting Sentiments on These Industrial Goods Companies: Caterpillar (CAT) and Comfort Systems (FIX)](https://www.theglobeandmail.com/investing/markets/stocks/CAT/pressreleases/8470282/analysts-have-conflicting-sentiments-on-these-industrial-goods-companies-caterpillar-cat-and-comfort-systems-fix/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Detailed price information for Caterpillar Inc (CAT-N) from The Globe and Mail including charting and trades.
- [CAT|Caterpillar Inc|Price:692.130|Chg%:+6.760](https://www.tradingkey.com/markets/stocks/cat)  
  <sub>TradingKey, 7 hours ago</sub>  
  Macroeconomic concerns and falling factory surveys drove downside volatility for Caterpillar stock. • Regulatory scrutiny and lowered analyst price targets...
- [CAT Stock Gains 0.75%, RSI Oversold In Focus: Explained](https://journalarta.com/en/2026/10/27/cat-stock-gains-0-75-rsi-oversold-in-focus/)  
  <sub>JournalArta, 6 hours ago</sub>  
  On October 26, 2026: price 692.13 USD, trend downtrend, RSI 28.8, support 687.00, resistance 863.44. technical analysis of cat stock. CAT Stock Gains...
- [Why Are Nasdaq Futures Falling Premarket? SPCX, SNDK, SOUN, IONQ, FIG Stocks Are In Focus](https://stocktwits.com/news-articles/markets/equity/why-nasdaq-futures-falling-premarket-jobless-claims-spcx-sndk-soun-ionq-fig-stocks-in-focus/cZoJAYjRJ7T)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Retail traders appear to be dialing back optimism. On Stocktwits, sentiment is now 'neutral' on SPY and QQQ.
- [CAT Oct 2026 930.000 put (CAT261030P00930000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/CAT261030P00930000/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest CAT Oct 2026 930.000 put (CAT261030P00930000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Analysts’ Top Industrial Goods Picks: Caterpillar (CAT), Comfort Systems (FIX)](https://www.google.com/goto?url=CAES2gEB6zswFU9s62NXo-dhTg0rS-lqT_aFv86v1Fb1bYJv2mlqE-zwTQc6qjnzzAcVB7LKUuokHNpr-uGcGaTac1p6otcQkT8txFysgUEsTrKuAy6BJLzl1_EhSBEhPQ-AjeVI1Z06UJNKlU7HZdWI4gYqzmOYr6IxSyeHbQi7VW5ipEMAgeuw_OAGUgFwarklr-Ig5raT35BBilPoJ-cbFK8oQyuMAosAy-5JSB77U-zjJ_PsEBAa_9GivhlXyiG8mgKb5ZWsihfScB-DubOMarzBi5ibE4WuGUBaxw)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Generac Holdings Inc (GNRC-N) from The Globe and Mail including charting and trades.
- [Caterpillar (CAT) Taps Derrick York As Denise Johnson Sets Early 2027 Retirement](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-taps-derrick-york-210639423.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Caterpillar (NYSE: CAT) said group president of Resource Industries Denise Johnson plans to retire in early 2027. The company named Derrick York,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 705.96 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 768.63 (-8.2%), 50d 792.93 (-11.0%), 200d 809.48 (-12.8%); 50d below 200d
Momentum: RSI(14) 33.9 | MACD -31.283 vs signal -23.822 (histogram -7.461)
Returns: 1d +2.0% | 5d -2.7% | 1m -13.9% | 3m -9.8%
52-week range: 524.47 - 1,064.90 (now 33.6% of the way up)
Volatility: ATR(14) 25.84 (3.7% of price) | annualised 20d 37.4%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 324.51B
Valuation: trailing P/E 30.39 | forward P/E 21.66 | P/B 16.73 | PEG 1.20
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 2.00 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 15 buy, 12 hold, 1 sell, 0 strong sell
Price target: mean 926.91 (+31.3% vs last close), range 575.00 - 1,150.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — NEUTRAL, confidence 0.55

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Slightly bearish tilt from technical downtrend and weak fundamentals outweighs neutral news and analyst consensus.

**Main reasons it gave:**
- Judge denied NVO's bid to halt Eli Lilly's weight‑loss ads (sales impact deemed negligible)
- Share buyback programme announced, total DKK 11.2 bn (positive shareholder return)
- Technicals: price below 50‑day and 200‑day SMAs, volume 0.13× 20‑day average (bearish positioning)
- Fundamentals: revenue growth +2.1% YoY, earnings down –20.6% YoY, 2 of last 4 earnings missed (weak earnings performance)
- Analyst consensus: hold with mean price target +15% but recent downgrades (mixed outlook)

<details><summary><b>News</b> — score +0.00</summary>

- [Novo Nordisk A/S (NOVO-B.CO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NOVO-B.CO/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest Novo Nordisk A/S (NOVO-B.CO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Buy, Sell or Hold LLY Stock? Key Factors to Watch Ahead of Q3 Earnings](https://www.tradingview.com/news/zacks:201d6915a094b:0-buy-sell-or-hold-lly-stock-key-factors-to-watch-ahead-of-q3-earnings/)  
  <sub>TradingView, 3 hours ago</sub>  
  Eli Lilly and Company LLY will report its third-quarter 2026 earnings on Oct. 29, before market open. The Zacks Consensus Estimate for sales and earnings is...
- [Omnicom Group: Stock Rallied On Strong Growth, Still A Bargain At A 8x P/E (NYSE:OMC)](https://seekingalpha.com/article/4957484-omnicom-stock-rallied-on-strong-growth-still-bargain-at-8x-pe)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Omnicom remains a buy: 8x forward earnings, 3.9% yield, strong cash flow, AI growth drivers, and attractive upside for patient investors.
- [Eli Lilly defeats Novo Nordisk attempt to halt weight-loss drug ads (LLY:NYSE)](https://seekingalpha.com/news/4657660-eli-lilly-defeats-novo-nordisk-attempt-to-halt-weight-loss-drug-ads)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  A US judge on Monday denied Novo Nordisk's (NVO) bid to halt Eli Lilly's (LLY) weight-loss drug advertisements, which the Danish pharmaceutical company...
- [Treasury shares total 1.2% of capital as Novo Nordisk (NVO) buybacks reach DKK 11.2B.](https://www.google.com/goto?url=CAESqgEB6zswFSoTOdYijk5IrdvJhLRFGpJvl15vB5g6a7lXaMnB7ClrXJKSkCk_H37wpz8WhhX-lHBX8c28gkfV9KrUTyuwtZnBeaP0Uauut-drshu8r0hwuR0FI78ZnrYMnmXFHG5zdPjUdaI6eTh6y5JafqjFMfP6eK_7YEjyDIJMjs9LiwaX-gg0ZFHoUckqCnbKzsffiu5nANqAu-mtyWlrvdPiABHO_3SnpQ)  
  <sub>Stock Titan, 22 hours ago</sub>  
  Purchases averaged DKK 277.78 per B share since February 4, 2026. The programme launched May 6 runs through February 1, 2027, capped at DKK 11.2B.
- [Buy the Dip: 4 Stocks the Market Marked Down Too Far Ahead of Big Catalysts](https://www.marketbeat.com/articles/buy-the-dip-4-stocks-the-market-marked-down-too-far-ahead-of-big-catalysts/)  
  <sub>MarketBeat, 23 hours ago</sub>  
  MercadoLibre, Novo Nordisk, Tyler Technologies and Summit Therapeutics trade below recent highs, yet each has earnings or catalysts that could shift...
- [Novo Nordisk A/S - share repurchase programme](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-share-repurchase-programme-155700648.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Bagsværd, Denmark, 26 October 2026 – On 6 May 2026, Novo Nordisk initiated a share repurchase programme in accordance with Article 5 of Regulation No...
- [Zacks Investment Research](https://www.globes.co.il/en/zarticle.aspx?id=3015020)  
  <sub>גלובס, 21 hours ago</sub>  
  VKTX is likely to report Q3 results Oct. 28 as investors await updates on VK2735's oral and injectable obesity programs and 2027 data readouts.
- [Which Pharmaceutical ETF Is the Better Buy: iShares’ Domestic IHE or VanEck’s Global PPH?](https://www.fool.com/coverage/etfs/2026/10/26/which-pharmaceutical-etf-is-the-better-buy-ishares-domestic-ihe-or-vaneck-s-global-pph/)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  IHE has outperformed recently by concentrating in U.S. drugmakers. PPH offers global reach and a higher dividend for investors willing to trade some of that...
- [Novo Nordisk Loses Court Bid Against Eli Lilly’s Weight-Loss Drug Ads — Judge Says Sales Impact Was Negligible](https://www.tradingview.com/news/benzinga:b21b7c8d5094b:0-novo-nordisk-loses-court-bid-against-eli-lilly-s-weight-loss-drug-ads-judge-says-sales-impact-was-negligible/)  
  <sub>TradingView, 4 hours ago</sub>  
  Eli Lilly NYSE:LLY can continue running advertisements for its weight-loss medicines after a federal judge rejected Novo Nordisk A/S' NYSE:NVO request for a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 38.94 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 38.45 (+1.3%), 50d 41.65 (-6.5%), 200d 44.50 (-12.5%); 50d below 200d
Momentum: RSI(14) 44.9 | MACD -0.559 vs signal -0.889 (histogram 0.330)
Returns: 1d -0.5% | 5d -1.0% | 1m +0.6% | 3m -24.5%
52-week range: 35.29 - 63.98 (now 12.7% of the way up)
Volatility: ATR(14) 0.82 (2.1% of price) | annualised 20d 19.7%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 171.82B
Valuation: trailing P/E 9.52 | forward P/E 11.32 | P/B 5.19 | PEG 4.37
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 44.92 (+15.4% vs last close), range 39.59 - 61.55
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

### Toyota (TM) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst consensus: 2 strong buy, 2 buy; price target +18.6% vs last close
- Four consecutive earnings beats (44%, 12%, 27%, 24%)
- Trailing P/E 8.67 (cheap) and earnings growth +86.9% YoY
- Technicals: price below 200‑day SMA and volume 0.09× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

- [Zacks Industry Outlook Highlights Toyota Motor, Honda Motor and Polestar Automotive](https://finance.yahoo.com/markets/stocks/articles/zacks-industry-outlook-highlights-toyota-123800642.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Chicago, IL – October 27, 2026 – Today, Zacks Equity Research discusses Toyota Motor TM, Honda Motor HMC and Polestar Automotive PSNY.
- [Autoliv Stock After Q3 Earnings: Buy, Hold or Sell the Stock?](https://www.tradingview.com/news/zacks:b96a09795094b:0-autoliv-stock-after-q3-earnings-buy-hold-or-sell-the-stock/)  
  <sub>TradingView, 2 hours ago</sub>  
  Autoliv, Inc. ALV is benefiting from increasing safety content per vehicle, strong product launches, expanding business with Chinese automakers and India,...
- [Toyota Motor Corporation (NYSE:TM) Stock Now Rated "Buy" by Sell-Side Brokerages](https://www.marketbeat.com/instant-alerts/consensus-toyota-motor-corporation-nyse-tm-stock-now-rated-buy-by-sell-side-brokerages-2026-10-27/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Shares of Toyota Motor Corporation (NYSE:TM - Get Free Report) have earned an average recommendation of "Buy" from the seven analysts that are presently...
- [The Zacks Analyst Blog Highlights Ford, General Motors and Toyota](https://finance.yahoo.com/markets/stocks/articles/zacks-analyst-blog-highlights-ford-120600470.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Chicago, IL – October 27, 2026 – Zacks.com announces the list of stocks featured in the Analyst Blog. Every day the Zacks Equity Research analysts discuss...
- [AI processors can sit idle waiting for data. SOAR AI's new U.S. patent aims to reduce that waste.](https://www.stocktitan.net/news/SOAR/soar-ai-granted-u-s-patent-covering-neural-sync-tm-ai-infrastructure-hxv75slearhy.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  The 20-claim patent covers forecasting GPU availability and coordinating data movement; SOAR AI sees potential future licensing and product opportunities.
- [Toyota Motor Corporation $TM Stock Bought by Evergreen Capital Management LLC](https://www.marketbeat.com/instant-alerts/filing-toyota-motor-corporation-tm-stock-bought-by-evergreen-capital-management-llc-2026-10-27/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Evergreen Capital Management LLC increased its holdings in Toyota Motor Corporation (NYSE:TM - Free Report) by 91.9% in the third quarter, according to the...
- [VersaBank Receives Final Regulatory Approval to Complete Reorganization](https://www.theglobeandmail.com/investing/markets/markets-news/Newsfile/8471607/versabank-receives-final-regulatory-approval-to-complete-reorganization/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Reorganization Will Support Significant Growth Opportunities and Contribute to Enhanced Shareholder Value, Including Broader Investor Awareness and...
- [(UMAX) Trading Performance and Risk Management (UMAX:CA)](https://news.stocktradersdaily.com/canada/umax-trading-performance-and-risk-management_20261027_249c63)  
  <sub>Stock Traders Daily, 6 hours ago</sub>  
  Trading Performance Report for Hamilton Utilities YIELD MAXIMIZER TM ETF (UMAX) with Risk Management Strategies.
- [Gentex Stock After Q3 Earnings: Buy, Hold or Sell the Stock?](https://www.zacks.com/stock/news/3014730/gentex-stock-after-q3-earnings-buy-hold-or-sell-the-stock)  
  <sub>Zacks Investment Research, 23 hours ago</sub>  
  GNTX's advanced automotive technologies and new programs fuel growth, but rising material costs, margin pressure and China weakness cloud its outlook.
- [Can GM Stock Balance Strong Q3 Earnings With Its 365M-Ton Emissions Challenge?](https://carboncredits.com/can-gm-stock-balance-strong-q3-earnings-with-its-365m-ton-emissions-challenge/)  
  <sub>CarbonCredits.com, 22 hours ago</sub>  
  General Motors (GM stock) reported stronger Q3 2026 earnings as China sales topped 358000 vehicles and new energy vehicles reached a record share,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 197.39 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 189.79 (+4.0%), 50d 191.76 (+2.9%), 200d 199.21 (-0.9%); 50d below 200d
Momentum: RSI(14) 61.3 | MACD 2.230 vs signal 1.088 (histogram 1.142)
Returns: 1d -0.1% | 5d +0.4% | 1m +4.8% | 3m +2.4%
52-week range: 166.50 - 248.29 (now 37.8% of the way up)
Volatility: ATR(14) 2.95 (1.5% of price) | annualised 20d 18.9%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 232.48B
Valuation: trailing P/E 8.67 | forward P/E 12.51 | P/B 15.85 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
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

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Trailing P/E 16.04 and PEG 1.11 indicate cheap valuation
- Profit margin 54.8% and ROE 48.7% reflect strong profitability
- Analyst consensus strong buy; mean price target $429 (+34% vs current price)
- Technical indicators: price 6% below 20d/50d/200d SMAs, RSI 32.9, volume 0.34x 20‑day avg
- Earnings record: 2 beats, 2 misses (recent misses) adds caution

<details><summary><b>News</b> — score -0.10</summary>

- [Down 7.6% in 4 Weeks, Here's Why You Should You Buy the Dip in Alphabet (GOOGL)](https://finance.yahoo.com/markets/stocks/articles/down-7-6-4-weeks-123502520.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Alphabet (GOOGL) has been beaten down lately with too much selling pressure. While the stock has lost 7.6% over the past four weeks, there is light at the...
- [Alphabet Earnings Dilemma: Organic Traffic Slowdown Meets Unstoppable CapEx (NASDAQ:GOOG)](https://seekingalpha.com/article/4957623-alphabet-earnings-dilemma-organic-traffic-slowdown-meets-unstoppable-capex)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Why Alphabet Inc. faces a near-term downside despite long-term strength. Click for this GOOG earnings preview and see why I am downgrading the stock.
- [GOOGL Stock Inches Up Premarket: Retail Traders Are Buying The Dip After CapEx-Fueled Selloff](https://stocktwits.com/news-articles/markets/equity/googl-stock-inches-up-premarket-retail-traders-are-buying-the-dip-after-cap-ex-fueled-selloff/cZZYAMLR7yW)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The move came as a relief for the stock which has fallen sharply over the last two months.
- [Alphabet Stock: 3 Reasons Why GOOGL Is a Buy Ahead of Q3 Results](https://www.barchart.com/story/news/8456108/alphabet-stock-3-reasons-why-googl-is-a-buy-ahead-of-q3-results)  
  <sub>Barchart.com, 23 hours ago</sub>  
  Alphabet is expected to deliver solid growth in Q3, driven by the resilience of its core advertising business and continued growth in Google Cloud.
- [Alphabet Reports Soon: How Has The Stock Reacted To Past Earnings?](https://www.trefis.com/stock/googl/articles/620714/alphabet-reports-soon-how-has-the-stock-reacted-to-past-earnings/2026-10-27)  
  <sub>Trefis, 6 hours ago</sub>  
  Alphabet (NASDAQ:GOOGL) is scheduled to report its earnings on Wednesday, October 28, 2026. The company has a market value of about $3.85 trillion.
- [GOOGL 261030 292.50C (GOOGL261030C292500) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GOOGL261030C292500-US?chain_id=Name1K9-3FXPhg.1ld0hff&global_content=%7B%22promote_id%22%3A%2214282%22,%22sub_promote_id%22%3A%2255%22,%22f%22%3A%22www.moomoo.com%2Fca%2Fhant%2Flearn%2Fdetail-best-stock-trading-platform-in-canada-117852-250268031%22%7D)  
  <sub>Moomoo, 10 hours ago</sub>  
  Track real-time GOOGL 261030 292.50C (GOOGL261030C292500) stock options chain data and pricing information and news on moomoo App for your options trading...
- [Alphabet Must Show This on Oct. 28 or the Stock Could Stall](https://www.fool.com/investing/2026/10/26/alphabet-must-show-this-on-oct-28-or-the-stock-cou/)  
  <sub>The Motley Fool, 13 hours ago</sub>  
  Alphabet (NASDAQ: GOOG) (GOOGL -1.06%) reports third-quarter results on Wednesday, Oct. 28, and most of the attention will focus on the usual places.
- ['We're Trading Them Like Baseball Cards': Mark Cuban Warns ‘Everything’s a Meme Stock’ as AAPL, GOOGL and MU Fuel Market Bubble Fears](https://www.tradingview.com/news/benzinga:5519b09bb094b:0-we-re-trading-them-like-baseball-cards-mark-cuban-warns-everything-s-a-meme-stock-as-aapl-googl-and-mu-fuel-market-bubble-fears/)  
  <sub>TradingView, 6 hours ago</sub>  
  Entrepreneur Mark Cuban stated that technology companies like Apple Inc. NASDAQ:AAPL and Google parent Alphabet Inc. NASDAQ:GOOG NASDAQ:GOOGL are currently...
- [Google GOOG Stock Heads to $300 as Infrastructure Costs Rise Ahead of Alphabet Earnings](https://www.fxleaders.com/news/2026/10/26/google-goog-stock-heads-to-300-as-infrastructure-costs-rise-ahead-of-alphabet-earnings/)  
  <sub>FXLeaders, 11 hours ago</sub>  
  Alphabet GOOGL stock fell below $320 as investors reduced technology exposure ahead of October 28 earnings, weighing the potential of Google Cloud and...
- [Will Alphabet Stock Surge After Oct. 28?](https://finance.yahoo.com/markets/stocks/articles/alphabet-stock-surge-oct-28-222500307.html)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Alphabet (NASDAQ: GOOG)(NASDAQ: GOOGL) reports Q3 2026 earnings after the market closes on Oct. 28. Wall Street analysts have an average revenue estimate of...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 319.63 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 340.72 (-6.2%), 50d 341.87 (-6.5%), 200d 341.23 (-6.3%); 50d above 200d
Momentum: RSI(14) 32.9 | MACD -5.997 vs signal -2.526 (histogram -3.471)
Returns: 1d +0.9% | 5d -6.1% | 1m -6.7% | 3m -5.1%
52-week range: 267.47 - 402.62 (now 38.6% of the way up)
Volatility: ATR(14) 7.97 (2.5% of price) | annualised 20d 21.5%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 3.91T
Valuation: trailing P/E 16.04 | forward P/E 20.81 | P/B 6.28 | PEG 1.11
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
Price target: mean 429.12 (+34.3% vs last close), range 340.00 - 500.00
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

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The recent sharp price drop (7‑11%) due to election concerns provides a material negative catalyst, reinforced by bearish technicals (price below key SMAs, RSI 38.2, negative MACD) and a mixed fundamentals picture (high leverage, earnings decline). Analyst consensus remains bullish but is already priced, and insider buying is minimal. Overall the signals tilt bearish, but the mixed context yields moderate conviction.

**Main reasons it gave:**
- Shares fell 7‑11% on election overreaction, prompting analyst defense (NEWS)
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.2, negative MACD (TECHNICALS)
- High debt/equity 168.6% and earnings down 10.9% YoY (FUNDAMENTALS)
- Earnings record: 1 beat, 3 misses, recent beat only 4% (EARNINGS)

<details><summary><b>News</b> — score -0.40</summary>

- [MercadoLibre, Inc. (MELI) Stock Forecasts](https://finance.yahoo.com/research/reports/MS_0P00009FL7_AnalystReport_1793093102000)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Analysts say buy the dip in MercadoLibre due to election overreaction (MELI:NASDAQ)](https://seekingalpha.com/news/4657799-analysts-says-buy-the-dip-in-mercadolibre-due-to-election-overreaction)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  MercadoLibre (MELI) pushed higher in early trading on Tuesday as analysts defended the stock after its sharp decline on Monday.
- [MercadoLibre (MELI) Gains 2.9% Premarket After Analyst Buy Recom](https://www.gurufocus.com/news/9144484/mercadolibre-meli-gains-29-premarket-after-analyst-buy-recommendations)  
  <sub>GuruFocus, 14 minutes ago</sub>  
  On October 27, 2026, MercadoLibre Inc (MELI) shares rose 2.9% in premarket trading to $1716.26 following renewed analyst buy calls amid a recent sharp price...
- [BTIG reiterates MercadoLibre stock rating ahead of earnings](https://www.investing.com/news/analyst-ratings/btig-reiterates-mercadolibre-stock-rating-ahead-of-earnings-93CH-4974820)  
  <sub>Investing.com, 4 hours ago</sub>  
  Investing.com - BTIG reiterated a Buy rating and $2,150 price target on MercadoLibre (NASDAQ:MELI) shares ahead of the company's third-quarter earnings...
- [Cathie Wood’s ARK Scoops Up 2 Brazilian Stocks Amid Selloff On Lula’s Win; Michael Burry Sees ‘Opportunity’ In One](https://www.tradingview.com/news/stocktwits:90e3e76ff094b:0-cathie-wood-s-ark-scoops-up-2-brazilian-stocks-amid-selloff-on-lula-s-win-michael-burry-sees-opportunity-in-one/)  
  <sub>TradingView, 10 hours ago</sub>  
  On Monday, ARK Invest purchased 76,636 NU shares worth via the ARK Blockchain & Fintech Innovation ETF. The asset management firm also purchased 723 MELI...
- [What Sent MercadoLibre Stock Lower?](https://finance.yahoo.com/markets/stocks/articles/sent-mercadolibre-stock-lower-102628216.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  For questions about this article or underlying research, email help@trefis.com. MercadoLibre (MELI) shares fell 7.8% on Monday, October 26, 2026,...
- [MercadoLibre, Inc. $MELI Stock Sold by Apollon Wealth Management LLC](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-stock-sold-by-apollon-wealth-management-llc-2026-10-27/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Apollon Wealth Management LLC trimmed its position in shares of MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 18.8% in the third quarter, according to...
- [MELI Testing Support Level: Stock Drops 7.81% (October 26, 2026)](https://journalarta.com/en/2026/10/27/meli-testing-support-level-stock-drops-7-81-october-26-2026/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 26, 2026: price 1668.72 USD, trend sideways, RSI 32.6, support 1668.72, resistance 1892.44. technical analysis of meli stock.
- [Why MercadoLibre (MELI) shares are plunging today](https://www.barchart.com/story/news/8455719/why-mercadolibre-meli-shares-are-plunging-today)  
  <sub>Barchart.com, 24 hours ago</sub>  
  Shares of latin American e-commerce and fintech company MercadoLibre (NASDAQ:MELI) fell 11.3% in the morning session after Brazilian President Luiz Inácio...
- [MercadoLibre (Dinari Tokenized Stock) (MELI) Price Prediction for 2026 to 2031](https://www.bybit.com/en/price-prediction/mercadolibre-dinari-tokenized-stock/)  
  <sub>Bybit, 20 hours ago</sub>  
  Based on current prediction models, MELI is estimated to reach approximately $2,028 by 2030. Compared to its current price of $1,669, this suggests potential...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,710.41 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 1,816.75 (-5.9%), 50d 1,854.27 (-7.8%), 200d 1,820.31 (-6.0%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -19.725 vs signal -5.390 (histogram -14.334)
Returns: 1d +2.5% | 5d -9.0% | 1m -0.1% | 3m -8.2%
52-week range: 1,546.81 - 2,360.76 (now 20.1% of the way up)
Volatility: ATR(14) 66.12 (3.9% of price) | annualised 20d 50.1%
Volume: 0.55x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 86.71B
Valuation: trailing P/E 46.52 | forward P/E 30.41 | P/B 11.07 | PEG 0.99
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.8% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: buy (mean 1.58 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 16 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,273.86 (+32.9% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-27 BTIG: reit, Buy -> Buy
  - 2026-10-13 Citigroup: main, Neutral -> Neutral
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
Institutional ownership: 80.1%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material news catalyst in the past 24 h; technicals show slight bullish momentum but low volume; fundamentals indicate high valuation and negative free cash flow; strong earnings record but next earnings is a month away, limiting near‑term catalyst impact.

**Main reasons it gave:**
- No material news catalyst in past 24h
- Technical indicators show slight bullish momentum but low volume
- Fundamentals indicate high valuation and negative free cash flow
- Strong earnings record but next earnings is a month away

<details><summary><b>News</b> — score +0.15</summary>

- [Elbit Systems Ltd. (ESLT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ESLT/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  19,349.00% · Previous close 735.34 · Open 752.61 · Bid 844.57 x 100 · Ask 690.28 x 200 · Day's range 752.61 - 778.55 · 52-week range 453.00 - 1,016.06 · Volume...
- [ESLT stock pre-market at EUR 697.50: defense systems provider](https://www.ad-hoc-news.de/boerse/news/vorboerse/eslt-stock-pre-market-at-eur-697-50-defense-systems-provider/70417875)  
  <sub>ad-hoc-news.de, 8 hours ago</sub>  
  Elbit Systems supplies defense, homeland-security and aerospace solutions. At Lang & Schwarz the stock trades pre-market at EUR 697.50 on October 27, 2026.
- [Elbit Systems: A 28% Pullback, But Valuation Still Demands Exceptional Execution (ESLT)](https://seekingalpha.com/article/4957815-elbit-systems-pullback-but-valuation-demands-exceptional-execution)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Elbit Systems is growing its manufacturing capacity, adjusting its footprint for increasingly nationalist procurement policies. See why I rate ESLT stock a...
- [3 Drone Technology Stocks Poised to Benefit From Rising Adoption](https://www.tradingview.com/news/zacks:12ceb8760094b:0-3-drone-technology-stocks-poised-to-benefit-from-rising-adoption/)  
  <sub>TradingView, 2 hours ago</sub>  
  An updated edition of the Sept. 2, 2026 article.The drone technology industry is gaining significant traction as unmanned aerial systems (UAS) increasingly...
- [A Look at Elbit Systems Ltd (ESLT) After 5.8% Gain -- GF Value $388.35 vs Price $777.96](https://www.google.com/goto?url=CAESrgEB6zswFX60f47w1Vo1sgbJCP7NYJRKrHW0K4fPiaAz4PteJYrWlLvR6stxx0RT77j80vCB8SvopW8DQHzkrsheOXQibeWP2ZYimeBBhP93-0oc0uvOCTiid8QYB7nKUONYhEK6Gli0YCqzAcSklz7y4-PuEGCsmhvAMprgTnO-cxEkQOAtv8GH3WMXiuoxlK03F6kTjEMDrEDm6crx68IWaLgk4NHU6J0FBXp9oCM)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On October 26, 2026, Elbit Systems Ltd (ESLT) shares rose 5.8% to $777.96, continuing a strong performance with a year-to-date increase of 35.2%.
- [GEV, D, CMS, AEP And PWR To Report Earnings This Week – A Look At What Investors Are Watching](https://stocktwits.com/news-articles/markets/equity/gev-d-cms-aep-pwr-to-report-earnings-this-week-a-look-at-what-investors-are-watching/cZUdCq6RByk)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Investors will look for the impact of AI-driven electricity demand as power and utility companies face a crucial earnings week.
- [Harel Insurance Investments & Financial Services Ltd. Adds Elbit](https://www.gurufocus.com/news/9143578/harel-insurance-investments-financial-services-ltd-adds-elbit-systems-ltd-eslt-shares-look-100-overvalued-on-gf-value)  
  <sub>GuruFocus, 11 hours ago</sub>  
  A Major Institutional Add in Israeli Defense Electronics Harel Insurance Investments & Financial Services Ltd. (Trades, Portfolio) disclosed on 2026-10-27 a...
- [3 Defence Stocks With Long Term Backlogs For Portfolio Defense](https://simplywall.st/stocks/il/capital-goods/tase-eslt/elbit-systems-shares/news/3-defence-stocks-with-long-term-backlogs-for-portfolio-defen)  
  <sub>Simply Wall Street, 14 hours ago</sub>  
  Geopolitics is back on every market screen as the US-Iran conflict keeps flaring and investors reassess what “risk” really means for portfolios.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 770.00 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 712.87 (+8.0%), 50d 721.95 (+6.7%), 200d 784.28 (-1.8%); 50d below 200d
Momentum: RSI(14) 62.4 | MACD 11.463 vs signal 2.521 (histogram 8.941)
Returns: 1d -1.0% | 5d +3.4% | 1m +9.3% | 3m +0.1%
52-week range: 454.95 - 1,014.33 (now 56.3% of the way up)
Volatility: ATR(14) 21.31 (2.8% of price) | annualised 20d 42.7%
Volume: 0.54x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 36.09B
Valuation: trailing P/E 57.94 | forward P/E 41.37 | P/B 8.17 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 802.17 (+4.2% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

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

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML Holding N.V. (ASML) Gains on Strong EUV Demand and Higher Guidance](https://www.google.com/goto?url=CAESkQEB6zswFdYweY9jZBHmdqvT-NUlYtQ9-OeILGmS9TZJxgBHslhKzpul7k5o7ryBS0o0wt51TYOJhi148psl8h3hfqs43wZdYjN4mlbMF_Jxc-drEOnIet0WxALDCgamWUSsgOR5LaSbmp0Hrlmwt8oLkxbjrCi4bWHZcbDiqKxHTJzA_WVktaxBDol4hyZURWaS)  
  <sub>Yahoo Finance, 32 minutes ago</sub>  
  Antipodes Partners published its third-quarter 2026 investor letter for “Antipodes Global Fund.” The letter can be downloaded here.
- [ASML: Creating Its Own Bottleneck (NASDAQ:ASML)](https://seekingalpha.com/article/4957642-asml-creating-its-own-bottleneck)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  ASML reported record Q3 sales and demand visibility through 2028, but supply remains the bottleneck, not customer interest. Despite a record quarter,...
- [ASML's Impact on Dutch Economy Grows, Stock Market Value Reaches €547 Billion](https://www.gurufocus.com/news/9143522/asmls-impact-on-dutch-economy-grows-stock-market-value-reaches-547-billion)  
  <sub>GuruFocus, 13 hours ago</sub>  
  On October 26, 2026, economists from ING released a report indicating that ASML (ASML), a leading chip equipment manufacturer, could contribute as much as...
- [Why ASML's Q3 2026 Results Dropped The Stock Price (NASDAQ:ASML)](https://seekingalpha.com/article/4957584-why-asml-q3-2026-results-dropped-the-stock-price)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  ASML Holding N.V. posted strong Q3 2026 results, with sales and net income growth outpacing prior trends. Read more on ASML stock here.
- [ASML Holding (ENXTAM:ASML) Could Be 24% Undervalued After Raised Guidance And Q3 Beat](https://simplywall.st/stocks/nl/semiconductors/ams-asml/asml-holding-shares/news/asml-holding-enxtamasml-could-be-24-undervalued-after-raised)  
  <sub>Simply Wall Street, 14 hours ago</sub>  
  ASML Holding (ENXTAM:ASML) is back in focus after third quarter 2026 results showed higher revenue and net income year over year, alongside raised guidance,...
- [ASML Nov 2026 940.000 put (ASML261120P00940000) interactive stock chart](https://uk.finance.yahoo.com/quote/ASML261120P00940000/chart/)  
  <sub>Yahoo Finance UK, 20 hours ago</sub>  
  Interactive chart for ASML Nov 2026 940.000 put (ASML261120P00940000) – analyse all of the data with a huge range of indicators.
- [ASML posts record Q3 sales but supply limits gr...](https://pluang.com/en/news-feed/asml-menciptakan-bottleneck-sendiri)  
  <sub>Pluang, 16 hours ago</sub>  
  ASML reported record sales in Q3 and strong demand visibility through 2028, but supply constraints remain a key challenge. Despite this strong performance,...
- [ASML Oct 2026 1672.500 call (ASML261030C01672500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML261030C01672500/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest ASML Oct 2026 1672.500 call (ASML261030C01672500) stock quote, history, news and other vital information to help you with your stock trading...
- [ASML Keeps Buying Back Stock Daily as Musk Flags Pulled-Forward Terafab Tool Deliveries](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/asml-keeps-buying-back-stock-daily-as-musk-flags-pulled-forward-terafab/70416044)  
  <sub>ad-hoc-news.de, 22 hours ago</sub>  
  ASML disclosed daily buybacks under its January 28 programme, while Musk said suppliers brought forward Terafab deliveries; Q3 sales rose 55.2%.
- [Top Japanese Chip Stocks to Watch Going Into Q3 Earnings, According to Bernstein](https://finance.yahoo.com/technology/articles/top-japanese-chip-stocks-watch-080039434.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Investing.com-- Bernstein outlined its top picks among Japanese semiconductor stocks going into the September-quarter earnings season, with positioning...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,616.66 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 1,712.40 (-5.6%), 50d 1,712.34 (-5.6%), 200d 1,591.69 (+1.6%); 50d above 200d
Momentum: RSI(14) 41.6 | MACD -39.888 vs signal -24.916 (histogram -14.971)
Returns: 1d +1.6% | 5d -0.9% | 1m -8.7% | 3m +4.3%
52-week range: 966.57 - 1,989.44 (now 63.6% of the way up)
Volatility: ATR(14) 52.87 (3.3% of price) | annualised 20d 36.1%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 623.09B
Valuation: trailing P/E 39.78 | forward P/E 25.73 | P/B 1,388.14 | PEG 0.89
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
Price target: mean 2,138.92 (+32.3% vs last close), range 862.76 - 2,834.13
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

### JPMorgan Chase (JPM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [JPMorgan's CEO just sent a memo to anyone watching the U.S. economy](https://finance.yahoo.com/economy/articles/jpmorgans-ceo-just-sent-memo-010300953.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  JPMorgan Chase recently delivered another big quarter. The bank earned $15.3 billion, or $5.57 a share, in the third quarter, though the results fell short...
- [JPMorgan Chase: A Fortress Built For Uncertain Times (NYSE:JPM)](https://seekingalpha.com/article/4957813-jpmorgan-chase-a-fortress-built-for-uncertain-times)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  JPMorgan Chase's ROTCE reached 24% for the first nine months of FY26, with a CET1 ratio of 13.9%, well above regulatory requirements. See why JPM stock is a...
- [JPMorgan Chase Says That Bitcoin Will Outperform Stocks, Bonds, and Gold Over the Next 10 Years. Here's Why It Might Be Right](https://www.fool.com/investing/2026/10/27/jpmorgan-chase-says-that-bitcoin-will-outperform-s/)  
  <sub>The Motley Fool, 4 hours ago</sub>  
  Per a new report, the asset management arm of JPMorgan Chase (JPM +0.74%) has a base case in which Bitcoin (BTC -1.07%) beats domestic stocks, bonds,...
- [JPMorgan's Asset Growth in Asia Pacific Reaches $400 Billion](https://www.gurufocus.com/news/9144010/jpmorgans-asset-growth-in-asia-pacific-reaches-400-billion)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On October 27, 2026, JPMorgan Asset Management announced a significant increase in its assets under management in the Asia Pacific region,...
- [JPMorgan Chase & Co. $JPM Stock: Sepio Capital LP Cuts Position](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-sepio-capital-lp-cuts-position-2026-10-27/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Sepio Capital LP lowered its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 59.3% in the third quarter, according to the company in...
- [Will JPMorgan's Nigeria Expansion Bolster Its Growth Prospects?](https://www.theglobeandmail.com/investing/markets/stocks/JPM-N/pressreleases/8457524/will-jpmorgan-s-nigeria-expansion-bolster-its-growth-prospects/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  JPMorgan Chase & Co.JPM is advancing its expansion plans in Nigeria after the Central Bank of Nigeria (CBN) granted approval-in-principle to establish...
- [JPM Oct 2026 312.500 call (JPM261030C00312500) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/JPM261030C00312500/)  
  <sub>Yahoo Finance Singapore, 7 hours ago</sub>  
  Find the latest JPM Oct 2026 312.500 call (JPM261030C00312500) stock quote, history, news and other vital information to help you with your stock trading...
- [JPMorgan Chase (NYSE:JPM) Share Price, Forecast & Analysis](https://stocksdownunder.com/company/jpmorgan-chase/)  
  <sub>Stocks Down Under, 18 hours ago</sub>  
  Explore JPMorgan Chase (NYSE:JPM) share price, stock analysis, financial performance, valuation and analyst price targets on Stocks Down Under.
- [Goldman and Morgan Stanley stocks rise after scoring plum roles in Anthropic IPO (GS:NYSE)](https://seekingalpha.com/news/4657478-goldman-and-morgan-stanley-stocks-rise-after-scoring-plum-roles-in-anthropic-ipo)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Goldman Sachs Group (GS) stock climbed 2.2%, and Morgan Stanley (MS) stock gained 2.6% in Monday trading after they won two key roles in the Anthropic (ANT)...
- [JPMorgan Chase & Co. $JPM Stock Acquired by Brookstone Capital Management](https://www.google.com/goto?url=CAESvgEB6zswFZpT2F4mr_FIQNkK051ZYMJS_kqa3itnllcDKs19TQ7VMl3NgxrVrQt6ugZGvjZeAz7KLGN-vGpm1AQhYQXXlGOZ4ko1RYV58_6OtK2kzmPaEVVEHxX3wTP1qbF6MxTzwgUMzgSqWPXmCPUKLDvCaoOVUPv6LS-45ZFbxuaHFdE8ZrX0nd0npQNOVUX8iGsDxtx-voqcHlPzgGouJ4XT70vjIb8blY85NMbW4lsyymBgtR1Pumg35YzU)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Brookstone Capital Management boosted its holdings in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 12.1% during the 3rd quarter, according to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 335.71 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 333.61 (+0.6%), 50d 344.33 (-2.5%), 200d 322.56 (+4.1%); 50d above 200d
Momentum: RSI(14) 47.7 | MACD -2.248 vs signal -3.041 (histogram 0.792)
Returns: 1d +0.5% | 5d +0.1% | 1m -0.3% | 3m -2.6%
52-week range: 282.84 - 365.18 (now 64.2% of the way up)
Volatility: ATR(14) 6.04 (1.8% of price) | annualised 20d 13.4%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 891.51B
Valuation: trailing P/E 14.08 | forward P/E 13.15 | P/B 2.54 | PEG 1.42
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
Price target: mean 372.26 (+10.9% vs last close), range 312.00 - 425.00
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

- [Buy, Sell or Hold LLY Stock? Key Factors to Watch Ahead of Q3 Earnings](https://ca.finance.yahoo.com/news/buy-sell-hold-lly-stock-115300408.html)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Eli Lilly and Company LLY will report its third-quarter 2026 earnings on Oct. 29, before market open. The Zacks Consensus Estimate for sales and earnings is...
- [Eli Lilly (LLY) Stock May Be 26% Below Fair Value On Richmond Plant Buildout](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-stock-may-be-26-below-fair-value-on-richmond-p)  
  <sub>Simply Wall Street, 3 hours ago</sub>  
  Eli Lilly has delivered a powerful run over the past few years, and with the stock recently closing at US$1279.14, the key issue for investors is how well...
- [Eli Lilly defeats Novo Nordisk attempt to halt weight-loss drug ads (LLY:NYSE)](https://seekingalpha.com/news/4657660-eli-lilly-defeats-novo-nordisk-attempt-to-halt-weight-loss-drug-ads)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  A US judge on Monday denied Novo Nordisk's (NVO) bid to halt Eli Lilly's (LLY) weight-loss drug advertisements, which the Danish pharmaceutical company...
- [Dear Eli Lilly Stock Fans, Mark October 29 on Your Calendar](https://www.barchart.com/story/news/8458544/dear-eli-lilly-stock-fans-mark-october-29-on-your-calendar)  
  <sub>Barchart.com, 21 hours ago</sub>  
  Eli Lilly (LLY) is making billions from the weight-loss boom. But it's no longer simply fighting for a bigger slice of the weight-loss drug market.
- [LLY vs. MRK: Which Stock Offers the More Compelling Investment Case?](https://www.theglobeandmail.com/investing/markets/stocks/MRK/pressreleases/8455370/lly-vs-mrk-which-stock-offers-the-more-compelling-investment-case/)  
  <sub>The Globe and Mail, 24 hours ago</sub>  
  Detailed price information for Merck & Company (MRK-N) from The Globe and Mail including charting and trades.
- [LLY Oct 2026 1350.000 call (LLY261030C01350000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/LLY261030C01350000/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest LLY Oct 2026 1350.000 call (LLY261030C01350000) stock quote, history, news and other vital information to help you with your stock trading...
- [Eli Lilly (LLY) Earnings: Is the Profit Turning Into Cash?](https://finchannel.com/eli-lilly-lly-earnings-is-the-profit-turning-into-cash/139495/american-business-trends/stock-prices/2026/10/)  
  <sub>finchannel, 20 hours ago</sub>  
  Increasingly, yes. In the first half of 2026 Eli Lilly turned 74% of its net income into free cash flow, against 18% in the same six months a year earlier.
- [FUBO CEO Teases November Strategy Reveal After Strong North America Subscriber Growth In Q3](https://stocktwits.com/news-articles/markets/equity/fubo-ceo-teases-november-strategy-reveal-after-strong-north-america-subscriber-growth-in-q3/cZo4AyQRJIo)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Alisa Bowen, who succeeded co-founder David Gandler as CEO last month, said her confidence in FuboTV's differentiation and growth prospects has “only...
- [Eli Lilly declares $1.73 fourth-quarter dividend](https://grafa.com/en/news/united-states/eli-lilly-fourth-quarter-2026-dividend-173-per-share)  
  <sub>grafa.com, 18 hours ago</sub>  
  Eli Lilly declared a fourth-quarter 2026 cash dividend of $1.73 per share on its outstanding common stock. The dividend is payable December 10, 2026,...
- [Don't Miss This Week's 5 Most Important Earnings Charts](https://www.tradingview.com/news/zacks:07a468a17094b:0-don-t-miss-this-week-s-5-most-important-earnings-charts/)  
  <sub>TradingView, 17 hours ago</sub>  
  Earnings season picks up steam this week with hundreds of S&P 500 companies reporting earnings including several of the Magnificent 7 stocks like Alphabet,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,288.25 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 1,214.84 (+6.0%), 50d 1,190.69 (+8.2%), 200d 1,087.03 (+18.5%); 50d above 200d
Momentum: RSI(14) 64.4 | MACD 32.271 vs signal 24.084 (histogram 8.188)
Returns: 1d +0.7% | 5d +0.4% | 1m +8.7% | 3m +6.5%
52-week range: 813.53 - 1,306.69 (now 96.3% of the way up)
Volatility: ATR(14) 36.33 (2.8% of price) | annualised 20d 31.0%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.15T
Valuation: trailing P/E 43.24 | forward P/E 27.19 | P/B 33.90 | PEG 1.23
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
Price target: mean 1,333.72 (+3.5% vs last close), range 930.00 - 1,600.00
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

- [Microsoft offers voluntary buyout to 60,000 employees](https://finance.yahoo.com/technology/article/microsoft-offers-voluntary-buyout-to-60000-employees-160011034.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Microsoft (MSFT) announced it was offering voluntary buyouts to roughly 60000 employees on Monday as it looks to reshape its organization for the AI era.
- [Microsoft's Stock May Fall Sharply Following Quarterly Results (NASDAQ:MSFT)](https://seekingalpha.com/article/4957544-microsofts-stock-may-fall-sharply-following-quarterly-results)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Microsoft Corporation must deliver a significant earnings and guidance beat to sustain its bullish momentum near all-time highs. Read more on MSFT stock...
- [Microsoft Is Paying Workers to Leave So It Can Pay for AI](https://247wallst.com/investing/2026/10/27/microsoft-is-paying-workers-to-leave-so-it-can-pay-for-ai/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Microsoft just offered buyouts to roughly a quarter of its entire workforce, and the announcement never once mentions AI or cost cutting.
- [Microsoft Layoffs 2026? 60,000 Staff Offered Buyouts](https://www.indmoney.com/blog/us-stocks/microsoft-layoffs-60000-employee-buyouts)  
  <sub>INDmoney, 5 hours ago</sub>  
  Microsoft offered buyouts to 60000 eligible employees, not 60000 layoffs. Here's why, how much it could save and what it means for MSFT stock.
- [Morgan Stanley Sticks to Its Buy Rating for Microsoft (MSFT)](https://www.theglobeandmail.com/investing/markets/stocks/MSFT-Q/pressreleases/8470272/morgan-stanley-sticks-to-its-buy-rating-for-microsoft-msft/)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Microsoft Stock Price Forecast: MSFT Rebounds Over 50% From June Low, Earnings Beat May Push It Toward Record $555 High](https://www.tradingkey.com/analysis/stocks/us-stocks/262242360-microsoft-stock-forecast-msft-poised-challenge-555-all-time-high-tradingkey)  
  <sub>TradingKey, 1 hour ago</sub>  
  TradingKey - Microsoft (MSFT) will report its first-quarter fiscal 2027 earnings after the market close on October 28, Eastern Time. As its stock price...
- [Microsoft Stock News (Oct 27, 2026): MSFT Rises 1.5% to $532.60](https://www.heygotrade.com/en/news/microsoft-msft-stock-news-october-27-2026/)  
  <sub>Gotrade, 11 hours ago</sub>  
  Microsoft (MSFT) rose 1.54% to $532.60 on Oct. 26, 2026, beating the Nasdaq as Anthropic's IPO filing lifted AI stocks and Microsoft offered buyouts.
- [Oppenheimer Revamps Microsoft Stock Price Target For 2027](https://www.tradingview.com/news/gurufocus:0a0baedcc094b:0-oppenheimer-revamps-microsoft-stock-price-target-for-2027/)  
  <sub>TradingView, 2 hours ago</sub>  
  Oppenheimer raised its price target on Microsoft NASDAQ:MSFT to $625 from $570 while keeping an Outperform rating, citing continued enterprise demand and...
- [Microsoft (MSFT) Q3 earnings report preview: what to look for](https://finance.yahoo.com/markets/stocks/articles/microsoft-msft-q3-earnings-report-085447584.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Technology giant Microsoft (NASDAQ:MSFT) will be announcing earnings results this Wednesday after market close. Here's what you need to know.
- [Microsoft earnings: Options traders bet on $555 calls while stacking $460 puts (MSFT:NASDAQ)](https://seekingalpha.com/news/4657895-microsoft-earnings-options-traders-bet-on-555-calls-while-stacking-460-puts)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Options pricing implies Microsoft Corp. (MSFT) is primed for a $28 share-price swing when it reports fiscal first-quarter results after Wednesday market...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 532.77 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 529.06 (+0.7%), 50d 510.22 (+4.4%), 200d 437.05 (+21.9%); 50d above 200d
Momentum: RSI(14) 57.3 | MACD 6.740 vs signal 8.511 (histogram -1.770)
Returns: 1d +0.0% | 5d +0.2% | 1m +4.6% | 3m +36.4%
52-week range: 352.83 - 543.45 (now 94.4% of the way up)
Volatility: ATR(14) 10.89 (2.0% of price) | annualised 20d 19.6%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.96T
Valuation: trailing P/E 29.22 | forward P/E 22.49 | P/B 8.94 | PEG 1.73
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
Consensus: strong_buy (mean 1.33 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 13 strong buy, 41 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 605.12 (+13.6% vs last close), range 440.00 - 870.00
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 216.93 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 224.38 (-3.3%), 50d 222.14 (-2.3%), 200d 203.98 (+6.4%); 50d above 200d
Momentum: RSI(14) 45.2 | MACD -2.679 vs signal -1.290 (histogram -1.389)
Returns: 1d +0.4% | 5d +0.2% | 1m -5.2% | 3m +14.2%
52-week range: 165.17 - 239.24 (now 69.9% of the way up)
Volatility: ATR(14) 5.89 (2.7% of price) | annualised 20d 30.1%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.24T
Valuation: trailing P/E 27.43 | forward P/E 13.63 | P/B 22.88 | PEG 0.26
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
Price target: mean 328.95 (+51.6% vs last close), range 180.00 - 515.00
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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Royal Bank of Canada (RY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 201.98 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 196.66 (+2.7%), 50d 201.75 (+0.1%), 200d 188.68 (+7.0%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD 0.145 vs signal -1.113 (histogram 1.258)
Returns: 1d -0.2% | 5d +1.5% | 1m +0.5% | 3m -2.2%
52-week range: 145.41 - 217.87 (now 78.1% of the way up)
Volatility: ATR(14) 2.94 (1.5% of price) | annualised 20d 16.6%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 279.63B
Valuation: trailing P/E 17.66 | forward P/E 15.84 | P/B 2.93 | PEG 1.89
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
Price target: mean 212.48 (+5.2% vs last close), range 185.45 - 233.70
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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Exxon Mobil (XOM) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ExxonMobil's Q3 Earnings on Deck: Should You Bet on the Stock?](https://finance.yahoo.com/markets/stocks/articles/exxonmobils-q3-earnings-deck-bet-124800753.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  ExxonMobil Holdings Corporation XOM is set to report third-quarter 2026 results on Oct. 30, before the opening bell. The Zacks Consensus Estimate for...
- [Fund Update: New $175.5M $XOM stock position opened by STATE OF MICHIGAN RETIREMENT SYSTEM](https://www.quiverquant.com/news/Fund+Update%3A+New+%24175.5M+%24XOM+stock+position+opened+by+STATE+OF+MICHIGAN+RETIREMENT+SYSTEM)  
  <sub>Quiver Quantitative, 2 hours ago</sub>  
  STATE OF MICHIGAN RETIREMENT SYSTEM has opened a new $175.5M position in $XOM, per a new SEC 13F filing. This disclosure reflects the funds' holdings for...
- [28 ETFs Add to ExxonMobil (XOM) Holdings on Friday](https://finance.yahoo.com/markets/stocks/articles/28-etfs-add-exxonmobil-xom-110141533.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ETFs bought a net $54.3 million of ExxonMobil stock, with 28 buyers against 15 sellers.
- [ExxonMobil Corporation $XOM Stock Sold by Middleton & Co. Inc. MA](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-stock-sold-by-middleton-co-inc-ma-2026-10-27/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Middleton & Co. Inc. MA lowered its stake in ExxonMobil Corporation (NYSE:XOM - Free Report) by 5.6% in the 3rd quarter, according to the company in its...
- [ExxonMobil (NYSE:XOM) Share Price, Forecast & Analysis](https://stocksdownunder.com/company/exxonmobil/)  
  <sub>Stocks Down Under, 14 hours ago</sub>  
  Explore ExxonMobil (NYSE:XOM) share price, stock analysis, financial performance, valuation and analyst price targets on Stocks Down Under.
- [How Investors Are Reacting To ExxonMobil Stock As Earnings Near](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/how-investors-are-reacting-to-exxonmobil-stock-as-earnings-n)  
  <sub>Simply Wall Street, 15 hours ago</sub>  
  Persian Gulf exports have already moved above pre conflict levels, while ExxonMobil heads into an earnings week supported by higher Brent crude and strong...
- [ExxonMobil Corporation $XOM Stock: Citizens Financial Group Inc. RI Raises Holdings](https://www.marketbeat.com/instant-alerts/filing-exxonmobil-corporation-xom-stock-citizens-financial-group-inc-ri-raises-holdings-2026-10-27/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Citizens Financial Group Inc. RI boosted its position in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 591.6% during the 3rd quarter,...
- [XOM Oct 2026 167.500 call (XOM261030C00167500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XOM261030C00167500/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  Find the latest XOM Oct 2026 167.500 call (XOM261030C00167500) stock quote, history, news and other vital information to help you with your stock trading...
- [9,251 ExxonMobil Corporation $XOM Shares Purchased by Simplicity Wealth LLC](https://www.marketbeat.com/instant-alerts/filing-9251-exxonmobil-corporation-xom-shares-purchased-by-simplicity-wealth-llc-2026-10-27/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Simplicity Wealth LLC lifted its holdings in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) by 10.2% during the third quarter, according to its...
- [12,995 Shares in ExxonMobil Corporation $XOM Bought by Norris Perne & French LLP MI](https://www.marketbeat.com/instant-alerts/filing-12995-shares-in-exxonmobil-corporation-xom-bought-by-norris-perne-french-llp-mi-2026-10-27/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Norris Perne & French LLP MI acquired a new stake in shares of ExxonMobil Corporation (NYSE:XOM - Free Report) in the third quarter, according to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 182.23 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 172.99 (+5.3%), 50d 166.69 (+9.3%), 200d 153.75 (+18.5%); 50d above 200d
Momentum: RSI(14) 70.4 | MACD 5.136 vs signal 4.277 (histogram 0.859)
Returns: 1d -1.3% | 5d +2.5% | 1m +12.1% | 3m +16.3%
52-week range: 113.68 - 184.54 (now 96.7% of the way up)
Volatility: ATR(14) 3.77 (2.1% of price) | annualised 20d 18.9%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 749.29B
Valuation: trailing P/E 23.45 | forward P/E 14.93 | P/B 2.89 | PEG 1.50
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
Price target: mean 179.41 (-1.5% vs last close), range 142.00 - 206.00
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

> Neutral overall; no material macro surprise, flat fund flows, technicals oversold but no decisive break, and analyst view lacks rating data.

**Main reasons it gave:**
- Soybean futures slide after Brazil's currency drop, but fund's 47% cash weighting limits impact
- No macro surprise: yields down modestly, inflation near target, no policy shift
- Flat fund flows: no net creations or redemptions in the past week or month
- Technical indicators oversold (RSI 27.9) but no decisive break on volume
- Analyst view provides no rating data, offering no directional bias

<details><summary><b>News</b> — score +0.00</summary>

- [U.S. soybean futures slide alongside Brazilian real (SOYB:NYSEARCA)](https://seekingalpha.com/news/4657632-u-s-soybean-futures-slide-alongside-brazilian-real)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  CBOT soybeans fell to two-month lows following President Lula's surprise election win that sent the Brazil's currency sliding nearly 8%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.42 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 28.19 (-2.7%), 50d 28.50 (-3.8%), 200d 27.34 (+0.3%); 50d above 200d
Momentum: RSI(14) 27.9 | MACD -0.207 vs signal -0.121 (histogram -0.086)
Returns: 1d -0.6% | 5d -2.6% | 1m -2.9% | 3m -0.2%
52-week range: 25.44 - 29.49 (now 49.0% of the way up)
Volatility: ATR(14) 0.24 (0.9% of price) | annualised 20d 9.5%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +12.7% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.36B
What it is made of: Other 51.0%, Cash 47.0%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 42.3%, Invesco Short Term Treasury ETF 4.6%
Sector mix: Healthcare 16.8%, Industrials 15.2%, Financial services 13.7%, Consumer cyclical 11.8%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 27.60M | fund size: 756.93M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- EIA forecast: WTI crude price to drop 14% over six months (bearish)
- US dollar index up 0.44% on the week (bearish for commodities)
- Flat fund flows (0% change) indicating no new demand
- Crude oil inventories draw of -3.1 million barrels (15th percentile) (bullish but limited exposure)

<details><summary><b>News</b> — score +0.00</summary>

- [Commodities Are Back as DBC, PDBC Break to 52-Week Highs](https://etfdb.com/innovative-etfs-content-hub/dbc-pdbc-break-52-week-highs/)  
  <sub>ETF Database, 24 hours ago</sub>  
  With crude oil rising and AI infrastructure driving raw material demand, broad commodities ETFs offer advisors a strategic portfolio hedge.
- [Retirees Facing 3.7% Inflation May Find Relief in These 4 ETFs](https://financebuzz.com/news/best-etfs-retirees-beat-inflation)  
  <sub>FinanceBuzz, 5 hours ago</sub>  
  September's CPI hit 3.7% for the seventh straight month above 3.3%, and four ETFs spanning TIPS, commodities, staples, and dividends each address a gap.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.63 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 33.20 (+1.3%), 50d 32.53 (+3.4%), 200d 29.08 (+15.7%); 50d above 200d
Momentum: RSI(14) 58.4 | MACD 0.393 vs signal 0.392 (histogram 0.001)
Returns: 1d -0.4% | 5d +0.2% | 1m +3.5% | 3m +14.3%
52-week range: 22.36 - 34.10 (now 96.0% of the way up)
Volatility: ATR(14) 0.45 (1.4% of price) | annualised 20d 12.7%
Volume: 0.06x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +15.9% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.92B
What it is made of: Other 50.4%, Cash 45.1%, Bonds 2.5%, Stocks 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.5%, Brent Crude Future Dec 26 9.7%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 111.40M | fund size: 3.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most macro and technical indicators are unchanged; no policy surprise or decisive technical break. Outflows suggest some bearish pressure, but fundamentals remain modestly positive, leaving the overall view neutral.

**Main reasons it gave:**
- Outflows of -11.9% over the past month indicate bearish investor sentiment
- Price below 50‑day and 200‑day SMA, indicating a downtrend
- Yield of 5.4% offers modest premium over US Treasury yields
- Macro data stable with no surprise rate changes

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.67 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 91.14 (+0.6%), 50d 92.76 (-1.2%), 200d 95.02 (-3.5%); 50d below 200d
Momentum: RSI(14) 48.4 | MACD -0.267 vs signal -0.443 (histogram 0.175)
Returns: 1d +0.2% | 5d +0.5% | 1m +0.4% | 3m -3.1%
52-week range: 90.14 - 97.74 (now 20.1% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 5.8%
Volume: 0.19x the 20-day average
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
Three-year record: +10.0% a year | beta to the market 1.10
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: -0.0% (-1.92M) over 7d | 1 month: -11.9% (-1.76B) over 31d
Shares outstanding: 141.25M | fund size: 12.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals modestly bullish, positioning modestly bearish, fundamentals neutral‑slightly bullish; net effect near neutral.

**Main reasons it gave:**
- 10-year Treasury yield fell 12 bps this week (MACRO)
- CFTC data shows net short 35.9% of open interest, up 2% week-over-week (POSITIONING)
- Fund yield 4.1% with AA credit quality and low expense ratio (FUND BASICS)
- Price 91.08 above 20-day SMA 89.91 and 50-day SMA 90.99, RSI 60.6, MACD positive (TECHNICALS)

<details><summary><b>News</b> — score +0.00</summary>

- [FLOT: An Investment Grade ETF Outperforming In 2026 (Rating Upgrade)](https://seekingalpha.com/article/4957785-flot-investment-grade-etf-outperforming-2026-rating-upgrade)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  iShares Floating Rate Bond ETF stands out in 2026, outperforming other investment grade fixed income due to its floating rate structure.
- [Citi's Nathan Sheets Warns Markets Could Misread The Fed — Sees Fiscal, AI Financing Worries Pushing Up Treasury Yields](https://stocktwits.com/news-articles/markets/equity/citi-s-nathan-sheets-warns-markets-could-misread-the-fed-sees-fiscal-ai-financing-worries-pushing-up-treasury-yields/cZxqU0dRBuU)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Citi Global Chief Economist Nathan Sheets warned Tuesday that markets could misinterpret the Federal Reserve's policy intentions as Chair Kevin Warsh seeks...
- [Nasdaq 100 and 10-Year yield drop together as correlation turns positive](https://seekingalpha.com/news/4657890-nasdaq-100-and-10-year-yield-drop-together-as-correlation-turns-positive)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The Nasdaq 100 (NDX) and the U.S. 10-year Treasury yield (US10Y) have begun declining in tandem. Learn more information here.
- [SPARTAN WEEKLY #018: Gold Selloff, Bitcoin and Fed Outlook](https://www.onebullex.com/blog/spartan-weekly-018-gold-bitcoin-fed-outlook)  
  <sub>OneBullEx, 11 hours ago</sub>  
  The ten-year fell 19 basis points on Thursday. Gold fell 2.2% the same day. That should not happen. A falling yield is gold's oxygen; this week it got the...
- [Inflation is no longer just a supply story, Apollo’s Slok says](https://seekingalpha.com/news/4657912-inflation-is-no-longer-just-a-supply-story-apollo-s-slok-says)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The Federal Reserve faces a more complex inflation challenge as demand pressures reassert themselves alongside lingering supply effects, according to Apollo...
- [CROX Stock Jumps 20% After Q4 Beat – CEO Highlights Buybacks And Global Growth Runway](https://stocktwits.com/news-articles/markets/equity/crox-stock-jumps-after-q4-beat-ceo-highlights-buybacks-and-global-growth-runway/cZRTpt9R4rn)  
  <sub>Stocktwits, 14 hours ago</sub>  
  In the fourth-quarter earnings call, Rees highlighted the company's ability to simultaneously strengthen its balance sheet and return cash to shareholders.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.08 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 89.91 (+1.3%), 50d 90.99 (+0.1%), 200d 93.94 (-3.0%); 50d below 200d
Momentum: RSI(14) 60.6 | MACD 0.088 vs signal -0.174 (histogram 0.262)
Returns: 1d -0.0% | 5d +0.9% | 1m +1.7% | 3m -2.2%
52-week range: 88.92 - 97.99 (now 23.8% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 5.3%
Volume: 0.55x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Long Government
Yield: 4.1%
Credit quality: AA 100.0% | US government debt 99.7%
Three-year record: +4.2% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.56B
What it is made of: Bonds 99.7%, Cash 0.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 35.9% of open interest (5,868,295 contracts)
Change on the week: +2.0% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 146.00M | fund size: 13.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage thin (2% weight) but all buy with +11.1% price target
- CFTC speculators net short 11.4% of open interest, short position increased 9.2% week over week
- Fund fundamentals: P/E 16.35, 3‑year record +20% annual, expense ratio 0.19%
- Technicals mixed: price above 20‑day SMA (+0.5%) but below 50‑day SMA (-2.4%), MACD histogram positive, low volume
- Macro unchanged: yields down slightly, VIX up 0.6, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Should iShares Russell Top 200 Value ETF (IWX) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/ishares-russell-top-200-value-092002515.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Designed to provide broad exposure to the Large Cap Value segment of the US equity market, the iShares Russell Top 200 Value ETF (IWX) is a passively...
- [IWM 261007 277.00P (IWM261007P277000) Stock Options Chain | Quotes & News](https://www.moomoo.com/stock/IWM261007P277000-US)  
  <sub>Moomoo, 12 hours ago</sub>  
  Track real-time IWM 261007 277.00P (IWM261007P277000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [Investors Buy the Dip in Chip ETFs as Inflows Top $44B](https://www.etf.com/sections/weekly-etf-flows/investors-buy-dip-chip-etfs-inflows-top-44b)  
  <sub>ETF.com, 18 hours ago</sub>  
  Investors put $44.1 billion to work in US-listed ETFs during the week ending Friday, Oct. 23. That brought year-to-date inflows to $1.69 trillion.
- [Oppenheimer's top 50 small- and mid-cap Buy list (IWM:NYSEARCA)](https://www.google.com/goto?url=CAESkAEB6zswFYbSUifR3stI9-9dmlzLcSE2bv-YWgj5cE7Ezlkyq7EVcIMab007mUWPEICQu1oxskdZ0BnyxoLwG-tp921sCKhPxxxi2Nnhi2w0yTpdhsgWjhQCmgT6LZa8hEQj6aTJF6I8VSURFPIWrZ3nzMyoyWEv6luw8EyCbj23QlNBblJgxkODimj3u4-b9yE)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Oppenheimer technical analyst Ari Wald has updated the firm's list of 50 top small- (IWM) and mid-cap (MDY) Buy ideas, spanning stocks across energy,...
- [Nasdaq 100 Rallies on Chip Rebound; Brazil ETF Sinks 21%: Stock Market Today](https://www.tradingview.com/news/benzinga:1a9c72503094b:0-nasdaq-100-rallies-on-chip-rebound-brazil-etf-sinks-21-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  The Nasdaq 100 rallied 1.2% on Monday as chipmakers rebounded and investors piled back into AI hardware.The S&P 500 rose 0.8% to 7681, up 58 points.
- [Exchange-Traded Funds Higher as US Equities Advance After Midday](https://www.google.com/goto?url=CAESmwEB6zswFZrZqmTu20tpVtB0rEpJLKwcnfV9JATev39S0Wwp_OjzWk0dResidcBpJi9vZmrC6YNOJnKhJe0mB9XG7sX_MVPDYgarX6-AHIQdO8H1XAyPdqJ1-TZZ1dKLXsh3Dzo-mCey3SOHQOoPM-8NweOS8fo5M-Z1ZYVDuIKpb9lFFC8jrurzmxRJHulbSwfhir6ZJ0EQTcmlbg)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1%. US equity indexes rose as big...
- [The Russell 2000 Is the Chart to Watch. Here’s Why.](https://pro.thestreet.com/market-commentary/the-russell-2000-is-the-chart-to-watch-heres-why)  
  <sub>RealMoney Pro, 5 hours ago</sub>  
  I've mentioned the equal-weight S&P as an important indicator before. But now, I'm watching the Russell 2000 because it might have even better guidance for...
- [Form 4 iShares Russell 2000 ETF For: 26 October By Investing.com](https://uk.investing.com/news/stock-market-news/form-4-ishares-russell-2000-etf-for-26-october-93CH-4932153)  
  <sub>Investing.com UK, 22 hours ago</sub>  
  This pricing supplement, which is not complete and may be changed, relates to an effective Registration Statement under the Securities Act of 1933.
- [IWM 261023 160.00C (IWM261023C160000) Stock Options Chain | Quotes & News](https://www.google.com/goto?url=CAESmgIB6zswFW61RzZ9MyyTYLlfX1r9wX6ZiEOPPJJCJj8wW2xGCCdkN8sQ_l18xWLeR3cCKs4iG5rwWGpLHhIsXn7rKeiHUm9AHA1TKVpvmNSVTe7Jv4lN1Uu-3lhx2nHPHlr62fxI4O2zS0I2cd00_po6B6ANfDtAYcRZ4KT0fAfgQSM-49AlTl1QLclDwD5-5euKrAg1bm6SjSqRpwMjNyV4fBqAzAB97zdYH7ioxhnQUBcjUyYSAnbOcyKO62Tm2ok-bljKyfo7BP0CPxRE6NwCj-mvHSYMrLRFXMSyPE02wo-Rak9evKAK21tn82WNmSj0PFJke5maMDHtsKlUxAaDduhWB7WCOphSAqvzgiCljgnuWvyTXeGr1jo)  
  <sub>Moomoo, 12 hours ago</sub>  
  Track real-time IWM 261023 160.00C (IWM261023C160000) stock options chain data and pricing information and news on moomoo App for your options trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 278.43 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 277.01 (+0.5%), 50d 285.34 (-2.4%), 200d 278.42 (+0.0%); 50d above 200d
Momentum: RSI(14) 48.6 | MACD -2.390 vs signal -3.221 (histogram 0.831)
Returns: 1d +0.5% | 5d +1.0% | 1m -0.6% | 3m -3.5%
52-week range: 229.11 - 305.09 (now 64.9% of the way up)
Volatility: ATR(14) 3.49 (1.3% of price) | annualised 20d 14.7%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.35 | P/B 2.02 | P/S 1.25 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +20.0% a year | beta to the market 1.27
Cost and size: expense ratio 0.19% | net assets 78.04B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%, Twist Bioscience Corp 0.4%, Moog Inc Class A 0.4%, JFrog Ltd Ordinary Shares 0.4%, 10x Genomics Inc Ordinary Shares - Class A 0.4%
Sector mix: Healthcare 20.9%, Financial services 18.0%, Technology 14.5%, Industrials 13.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.89 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.1% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-10-21 Truist Securities: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 11.4% of open interest (466,789 contracts)
Change on the week: +9.2% of open interest
Crowding: 73% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 281.05M | fund size: 78.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields down slightly, normal upward curve
- Technical indicators show slight bullish momentum (RSI 58, MACD positive) but no decisive break
- Fund flows flat, no net inflow or outflow
- Fund fundamentals stable: yield 4.9%, high credit quality, no change

<details><summary><b>News</b> — score +0.00</summary>

- [FLOT: An Investment Grade ETF Outperforming In 2026 (Rating Upgrade)](https://seekingalpha.com/article/4957785-flot-investment-grade-etf-outperforming-2026-rating-upgrade)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  iShares Floating Rate Bond ETF stands out in 2026, outperforming other investment grade fixed income due to its floating rate structure.
- [AI Is Pushing Corporate Bond Sales to an All-Time Record](https://finance.yahoo.com/markets/stocks/articles/ai-pushing-corporate-bond-sales-124720846.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  US investment-grade bond sales hit a record $1.76 trillion, topping the 2020 pandemic peak, with LQD closing at $104.02 despite the flood of new supply.
- [Oracle Bonds Are Sliding as AI Debt Worries Grow. At 62, She Discovers the "Safe" Side of Her 401(k) Can Lose Money Too](https://247wallst.com/personal-finance/2026/10/27/oracle-bonds-are-sliding-as-ai-debt-worries-grow-at-62-she-discovers-the-safe-side-of-her-401k-can-lose-money-too/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Oracle's investment-grade bonds now carry a 263 basis point spread over Treasuries, wider than the average BB-rated junk bond, as AI debt fears grow.
- [IG: Your Guide To The Principal Investment Grade Corporate ETF](https://www.google.com/goto?url=CAESnAEB6zswFc-VqV02Jjm7keZZIkKeLe0WlWSSbXB9hUeeuUr8KfQ5RmfAQ400rekCok2MuDQ2BwH6vUjEh8_x2l96R4B7d6ZjN3kqJjh1ak7vyShG-qeYXJArS_G0MpxucVAiw6uiYn5XUxMJQxauLugZyhG-0xVVjQnckI6jt3_E_SJBQFd5PWNX5bGZQPIYz8KxMy7cLKttA5PDc4c)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Review Principal's IG corporate bond ETF: active duration tweaks, BBB-heavy portfolio, yield vs 7-year Treasuries, returns, and best tax placement—read now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 104.18 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 102.87 (+1.3%), 50d 104.20 (-0.0%), 200d 107.78 (-3.3%); 50d below 200d
Momentum: RSI(14) 58.2 | MACD 0.010 vs signal -0.268 (histogram 0.278)
Returns: 1d +0.1% | 5d +0.9% | 1m +1.7% | 3m -1.9%
52-week range: 101.83 - 112.92 (now 21.1% of the way up)
Volatility: ATR(14) 0.61 (0.6% of price) | annualised 20d 5.8%
Volume: 0.20x the 20-day average
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
Three-year record: +6.1% a year | beta to the market 1.35
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 293.50M | fund size: 30.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, technicals lack a decisive breakout, and mixed signals from analysts (modest bullish) and positioning (slight bearish) offset each other.

**Main reasons it gave:**
- Recent news: RSP on track for best outperformance vs. weighted S&P 500 since 2009 → positive sentiment
- Analyst coverage thin (1.4% weight) with 58.3% buy and price target ~+8.7% above current price → modest bullish bias
- CFTC shows net short 19.2% of open interest, up 2% week‑over‑week → slight bearish pressure
- Macro: Treasury yields down modestly, VIX up modestly, no policy surprise → neutral macro backdrop
- Technicals: price above 20‑, 50‑, 200‑day SMAs, RSI 57.5, MACD positive but no decisive breakout → neutral technicals

<details><summary><b>News</b> — score +0.00</summary>

- [S&P 500 Equal Weight on track for best weighted index outperformance since 2009](https://www.tradingview.com/news/seekingalpha:d8ff08a2a094b:0-s-p-500-equal-weight-on-track-for-best-weighted-index-outperformance-since-2009/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 equal-weight index AMEX:RSP is on track for its largest outperformance vs. the weighted S&P 500 (SP500) since April 2009.The equal-weight index...
- [Understanding The Vanguard FTSE All-World UCITS ETF (VWRA), And Why Many Investors Choose This Cult-Classic ETF To Build Their Portfolio](https://dollarsandsense.sg/understanding-the-vanguard-ftse-all-world-ucits-etf-vwra-and-why-many-investors-choose-this-cult-classic-etf-to-build-their-portfolio/)  
  <sub>DollarsAndSense.sg, 6 hours ago</sub>  
  VWRA or S&P 500 ETFs like CSPX and VUAA? Here's how VWRA compares on diversification, cost, risk, and long-term investing.
- [The Size of the Benefit Is Finally Public. For Small Cell Lung Cancer, It’s Big, and So Is the Bill.](https://www.moomoo.com/community/feed/the-size-of-the-benefit-is-finally-public-for-small-117508265410566)  
  <sub>Moomoo, 22 hours ago</sub>  
  When AstraZeneca and Amgen first announced this lung cancer win, the size of the benefit had not been published. Now it has, and the details deserve a...
- [Why Investing in S&P 500 Index Funds Is a Whole Lot Riskier These Days](https://www.aol.com/articles/why-investing-p-500-index-190501000.html)  
  <sub>AOL.com, 20 hours ago</sub>  
  The S&P 500 gives investors access to the top stocks on U.S. markets, including Nvidia and other big tech giants. It has been a terrific index to track not...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 216.71 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 213.40 (+1.5%), 50d 215.16 (+0.7%), 200d 207.47 (+4.4%); 50d above 200d
Momentum: RSI(14) 57.5 | MACD 0.956 vs signal 0.312 (histogram 0.643)
Returns: 1d -0.3% | 5d +0.4% | 1m +3.3% | 3m +0.5%
52-week range: 182.18 - 222.77 (now 85.1% of the way up)
Volatility: ATR(14) 1.96 (0.9% of price) | annualised 20d 10.1%
Volume: 0.24x the 20-day average
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
Three-year record: +18.6% a year | beta to the market 0.84
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 58.3% | hold 41.7% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -8.7% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-27 William Blair: down, Outperform -> Market Perform
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-19 Canaccord Genuity: main, Hold -> Hold
  - CRWD: 2026-10-22 Mizuho: main, Outperform -> Outperform
  - RVTY: 2026-10-13 TD Cowen: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 19.2% of open interest (1,935,470 contracts)
Change on the week: +2.0% of open interest
Crowding: 62% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 155.55M | fund size: 33.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall view: modest bearish insider positioning, stable fundamentals, mixed macro and technical signals.

**Main reasons it gave:**
- Net short 28.4% of open interest with a +1.7% increase (crowded short) in POSITIONING
- 10‑year Treasury yield fell 12 bps this week, supporting bond prices
- RSI 58 and MACD positive indicate slight bullish momentum, but price remains below 200‑day SMA
- Fund fundamentals stable: AA credit quality, 3‑year return +4.1%/yr, low beta 0.24

<details><summary><b>News</b> — score +0.00</summary>

- [Nasdaq 100 and 10-Year yield drop together as correlation turns positive](https://seekingalpha.com/news/4657890-nasdaq-100-and-10-year-yield-drop-together-as-correlation-turns-positive)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The Nasdaq 100 (NDX) and the U.S. 10-year Treasury yield (US10Y) have begun declining in tandem. Learn more information here.
- [Israel Discount Bank of New York's iShares 1-3 Year Treasury Bond ETF(SHY) Holding History](https://www.gurufocus.com/guru-portfolio/Israel%20Discount%20Bank%20of%20New%20York/SHY)  
  <sub>GuruFocus, 19 hours ago</sub>  
  iShares 1-3 Year Treasury Bond ETF(SHY) Buys and Sells Made by Israel Discount Bank of New York. Latest and Historical Data and Chart.
- [Inflation is no longer just a supply story, Apollo’s Slok says](https://seekingalpha.com/news/4657912-inflation-is-no-longer-just-a-supply-story-apollo-s-slok-says)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The Federal Reserve faces a more complex inflation challenge as demand pressures reassert themselves alongside lingering supply effects, according to Apollo...
- [SPARTAN WEEKLY #018: Gold Selloff, Bitcoin and Fed Outlook](https://www.onebullex.com/blog/spartan-weekly-018-gold-bitcoin-fed-outlook)  
  <sub>OneBullEx, 11 hours ago</sub>  
  The ten-year fell 19 basis points on Thursday. Gold fell 2.2% the same day. That should not happen. A falling yield is gold's oxygen; this week it got the...
- [The Bank of Japan's "hawkish pause" is only awaiting official confirmation, as market focus has already shifted to monetary policy signals for December.](https://news.futunn.com/en/post/1002356172/the-bank-of-japan-s-hawkish-pause-is-only-awaiting)  
  <sub>富途牛牛, 13 hours ago</sub>  
  Zhitong Finance APP has learned that this week can be described as "Super Central Bank Week"—the U.S., Japanese, and European central banks will hold...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.46 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 81.26 (+0.2%), 50d 81.45 (+0.0%), 200d 82.13 (-0.8%); 50d below 200d
Momentum: RSI(14) 58.1 | MACD 0.024 vs signal -0.025 (histogram 0.049)
Returns: 1d -0.0% | 5d +0.2% | 1m +0.4% | 3m -0.6%
52-week range: 81.05 - 83.18 (now 19.2% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.4%
Volume: 0.17x the 20-day average
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
Three-year record: +4.1% a year | beta to the market 0.24
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 28.4% of open interest (4,533,571 contracts)
Change on the week: +1.7% of open interest
Crowding: 93% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 209.30M | fund size: 17.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest technical upside with low volume, large speculators net short 35.9% (bearish) but fundamentals solid.

**Main reasons it gave:**
- Large speculators net short 35.9% of open interest, up 2% week‑over‑week (bearish positioning)
- Price above 20‑day and 50‑day SMAs but below 200‑day SMA, low volume (weak momentum)
- Yields slipped modestly, inflation unchanged, Fed policy unchanged (no macro surprise)
- Fund fundamentals solid: 4.7% yield, AA credit quality, 0.18% expense ratio (positive fundamentals)
- Recent article comparing TIPS to dividend stocks highlights continued demand for inflation protection (neutral sentiment)

<details><summary><b>News</b> — score +0.00</summary>

- [TIPS or Dividend Stocks? How Retirees Can Keep Up With Inflation](https://247wallst.com/investing/2026/10/26/tips-or-dividend-stocks-how-retirees-can-keep-up-with-inflation/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Two very different tools promise to shield retirement income from rising prices, but each carries a trap the other avoids. Knowing which trap you can live...
- [3 Dividend ETFs with Double-Digit Yields and 20%+ Upside](https://www.tipranks.com/news/3-dividend-etfs-with-double-digit-yields-and-20-upside)  
  <sub>TipRanks, 8 minutes ago</sub>  
  Dividend ETFs remain popular with investors looking for income, but some funds stand out. Using TipRanks' High Dividend Yield ETFs tool, we identified three...
- [Morgan Stanley’s Solana ETF Draws Fresh Cash Even as Short-Term Signals Flash Sell](https://www.tipranks.com/news/cryptocurrencies/morgan-stanleys-solana-etf-draws-fresh-cash-even-as-short-term-signals-flash-sell)  
  <sub>TipRanks, 7 hours ago</sub>  
  Morgan Stanley's crypto ambitions took another step forward this week as the Morgan Stanley Solana Trust ETF, MSOL, logged fresh inflows.
- [Meta Stock Sell-Off Looks Like an Overreaction](https://www.tipranks.com/news/meta-stock-sell-off-looks-like-an-overreaction)  
  <sub>TipRanks, 2 hours ago</sub>  
  Meta Platforms ($META) stock's recent sell-off looks like an overreaction, given the company's strong revenue growth and ability to fund its heavy...
- [Largest borrow rate increases among liquid names](https://www.tipranks.com/news/the-fly/largest-borrow-rate-increases-among-liquid-names-thefly-news-167)  
  <sub>TipRanks, 2 hours ago</sub>  
  Latest data shows the largest indicative borrow rate increases among liquid option names include: ASP Isotopes Inc (ASPI) 6.52% +1.75, GRANITESHARES 2X LONG...
- [GOOGL vs. MSFT: Which Big Tech Stock Has More Upside Ahead of Earnings, According to Analysts?](https://www.tipranks.com/news/googl-vs-msft-which-big-tech-stock-has-more-upside-ahead-of-earnings-according-to-analysts)  
  <sub>TipRanks, 3 hours ago</sub>  
  Big Tech Giants Alphabet ($GOOGL) and Microsoft ($MSFT) will report quarterly earnings on October 28, with investors watching their AI growth.
- [General Motors Stock (GM) Rises on Plan to Switch Listing — Why This Matters](https://www.tipranks.com/news/general-motors-stock-gm-rises-on-plan-to-move-listing-from-nyse-to-nasdaq-why-this-matters)  
  <sub>TipRanks, 3 hours ago</sub>  
  General Motors shares ($GM) rose more than 3% to about $80 early Tuesday after the U.S. auto giant announced plans to move its listing to the Nasdaq Global...
- [Bitcoin ETF’s Big Backstep: Hedgeye’s HBIT Sees Quarter of Assets Walk Out](https://www.tipranks.com/news/cryptocurrencies/bitcoin-etfs-big-backstep-hedgeyes-hbit-sees-quarter-of-assets-walk-out)  
  <sub>TipRanks, 11 hours ago</sub>  
  Bitcoin ETF's Big Backstep: Hedgeye's HBIT Sees Quarter of Assets Walk Out The Hedgeye Hedged Bitcoin ETF, HBIT, recorded a sharp outflow of $1033020 on...
- [TSMC’s AI Chip Packaging Prices Could Jump 20%](https://www.tipranks.com/news/tsmcs-ai-chip-packaging-prices-could-jump-20)  
  <sub>TipRanks, 6 hours ago</sub>  
  Taiwan Semiconductor Manufacturing (TSMC) ($TSM) is reportedly preparing to raise prices for its CoWoS advanced chip packaging services by up to 20%,...
- [ETF State of the Union: Record Inflows, Active ETFs & What's Next | State Street's Matthew Bartolini](https://www.tipranks.com/video/etf-state-of-the-union-record-inflows-active-etfs-whats-next-state-streets-matthew-bartolini)  
  <sub>TipRanks, 22 hours ago</sub>  
  ETFs are on track for a record-breaking year. In this interview, Matthew Bartolini, Global Head of Research Strategists at State Street Investment...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 106.26 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 105.00 (+1.2%), 50d 105.75 (+0.5%), 200d 108.92 (-2.4%); 50d below 200d
Momentum: RSI(14) 64.3 | MACD 0.220 vs signal -0.035 (histogram 0.255)
Returns: 1d -0.0% | 5d +0.7% | 1m +2.1% | 3m -1.4%
52-week range: 103.98 - 112.03 (now 28.3% of the way up)
Volatility: ATR(14) 0.38 (0.4% of price) | annualised 20d 3.7%
Volume: 0.08x the 20-day average
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
Three-year record: +4.5% a year | beta to the market 0.71
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 35.9% of open interest (5,868,295 contracts)
Change on the week: +2.0% of open interest
Crowding: 82% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 177.70M | fund size: 18.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, modest technical bullishness but not decisive, slight reduction in net short positions but still a sizable short bias, flat fund flows.

**Main reasons it gave:**
- Fed expected to hold rates; no policy surprise this week
- 10‑year Treasury yield fell 12 bps this week, modestly supportive of bond prices
- CFTC data shows net short 34 % of open interest, down 4.2 % week‑over‑week, indicating slight bullish shift but still bearish bias
- Technical indicators (RSI 63.5, MACD positive) show modest bullish momentum but price remains below 200‑day SMA

<details><summary><b>News</b> — score +0.00</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT)](https://www.google.com/goto?url=CAESkgEB6zswFXbm3UN2VF65nNAQt4iadHqgrvbiypDb0Am-jBRwX7_uhRS7uuXqfk7RnNK4BSJltpw3e33pT-HmsnDVDyp8i2O5a6Kx7gEaMB_eBYhvS1M8QkKpmmcl0LEIrN_b3U5s5pU_GIdj2nE5J2I3tPk85UAxJULfCtsHxzpPmc7PnB-DlWONmyA1sUnXo-Fmog)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  View the basic TLT option chain and compare options of iShares 20+ Year Treasury Bond ETF on Yahoo Finance.
- [Two Yields, One Fund: Why Your ETF’s Yield Depends on Which Number You Read](https://www.google.com/goto?url=CAESswEB6zswFZ8knKN3st6iOjYDW-2C_S22_J1fbmrcyY-wgOUdJjF9xFykL5fS0oCaBK0HmAOQJPGoWspuWd_E2eZBzcfSJgTSwOZO5f5p7vZEvFmimKTYPLutSQCn-zRs625EZn9t4cvv47GFT1DW24xUAlmc5RNHv-mUk1Eq9IE09L6ozcbi_8uvu9bpr7JItdu35oAMdUNsGXriqrYZGpKxUdLXI-XZ_Y4PLh2BLdDaQEpjIw)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  DGRW shows a 2.06% distribution yield versus a 1.19% SEC yield on the same day because it annualizes one large quarter-end payment. TLT's SEC yield of 5.30%...
- [Morgan Stanley's Michael Gapen Says Fed Is Not ‘Out Of The Water’ Even With A Hold Decision: ‘Economy Can Handle 75-100 Bps In Total Hikes’](https://www.google.com/goto?url=CAES_wEB6zswFdnDPL6oQvAvM1VBwB4nWG7OJo24y2hjxQo4eP3PpodwafL6DKdWnW8JZ2ajdQwC3KrDUke6fsZmWCNBBJOteD9XYcSzvadwNVjPAMw3tGvU9FPciGvspBjncphHbRrjwRzovoFyUmsKe03wLCwzGEBqgbNzYmz0rfMpcnf4ARPJzKMeGLamDV30ZidHDt-0DFucSevZll8OwqjYnPm0uUSp8QCkCrv_vpoZZJN79YPLZhpRelUxHM9-Y7AiLLCJ4jfAFWWcx6yu5nOvin9XQb0IdsB7wEolWEVDrs5tAo-LKFW4LWMUtsR6vc9FNhEEMp5f7Uiq6tm6Q5M)  
  <sub>TradingView, 8 hours ago</sub>  
  The Federal Reserve is set to meet for its October policy decision on Tuesday, with markets overwhelmingly expecting the central bank to hold rates steady...
- [Citi's Nathan Sheets Warns Markets Could Misread The Fed — Sees Fiscal, AI Financing Worries Pushing Up Treasury Yields](https://www.google.com/goto?url=CAES8AEB6zswFZwNGAXYAGOC1e2Yt0e8heVCqaJzimF-6shawDlx_tpbHbPfETzEUzoOdqgEerPPPe-gKvhsOH2M7PiPK3xmRqX-GwZjjvKiKxJOSKad3iniyaAMUxUXh_yMj7UeYhaweDCUvaYFDHBfQXH5OpeOm0OkQKj_w7uUHWkGuyNJIsA_6CngwGe_jMW1EEkZVa9jRz-uiIN2Ib42Edgg5aOEOANUhUtDldPnorgU6NoXjbcaarMksWAcpsf2JjJbZoUY0H4eyHXms7A3vHcPpgB77AMJGj0XcpeZ9e3t_zBIPcNKT9KO3U7B5ydisdI)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Citi Global Chief Economist Nathan Sheets warned Tuesday that markets could misinterpret the Federal Reserve's policy intentions as Chair Kevin Warsh seeks...
- [ETF yields vary by calculation method; use 30-d...](https://www.google.com/goto?url=CAESqgEB6zswFVC5QMon3z6LpNogMaM3TWtmu_9JrThsn4y3QzDVHpaLYBW0k0NCmU-6zxrW7d26pNshKC4ERRlBz8OH-1srhMa8h7UhrIgI0F9UYEYo9SJBG8AYBDklNLD5nFb-_M36bRdB9X5AdtszyhJnS-hLfpT--Toqza9C-LGTizHMNCgKWVKZWFDaGU0ckQr4v0Mg1uJh7ukKAxouAZh9xLie5cvAVpiRkQ)  
  <sub>Pluang, 4 hours ago</sub>  
  The same ETF can show different yield numbers on the same day due to varying calculation methods. Distribution yield reflects the latest payout annualized,...
- [Dow, S&P 500, Nasdaq Futures Climb As Tech Stocks Get A Boost From Anthropic IPO Listing: SOFI, BB, PYPL, CLS In Focus](https://www.google.com/goto?url=CAES4AEB6zswFTHzLZF0SCANF8aCxgQ4r3fRDK4krUBq_lTLWNIIj5HpkzGEmy0HUGNzshZ9EFGej0UeWNrJcMnYrtHFBXLL6HHNazcgrtFhw5Hlc14sxRWv3hLSIausvunIXir8NXh0VEpxRauVx5A4RbtGTtMoy7QDLBqGj7fMpryJvwxwsBFhTgBaZm4kyIw_JXMiXGhYNy5XCRFGrAGbGPhL1VbGGwxDV4x0OXSfG_kcAT77YbdzOCEcI6J1PffuZ98LcFlVPRMx4JoFDBGUchvPtYu-mPi7HFOdnJD_bUkXcw)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures traded higher in the overnight session late Monday as Wall Street kicked off the week on a winning note, bolstered by Anthropic's Nasdaq...
- [S&P 500, Nasdaq Futures Pull Back After Trump Wants 'Couple Days To Think' About Iran Ceasefire Deal: ASTS, DELL, BB, SMCI In Focus](https://www.google.com/goto?url=CAES2wEB6zswFbiNW1BH0l5hGTplwJzyByKHwxCFL2i2V5LeG22phuHy8dKmFYmTdxEX3b7cRkreOjOKmiLzvlpIGNZmzuzxbH3DpJ-IWrlJfz-qBH_X__wZQlPNV2yMnomJDer4D3YM-z7x3cMIFP5ojHrzPdwDi9loTnoF1GL_7o0u9WbKYm9f-LnEdlj1Wpq5OgFm30NaLakPowFbvsPj3eeaKi2HCkQk18NuM8m90tkb1ed6HDXzmL7NmPYI5LaiiFYG04NaxgmrCF0cAO3yetnvikfXgpE7Y8hbVwg)  
  <sub>Stocktwits, 15 hours ago</sub>  
  According to a report from Axios, the U.S. and Iran have reached a tentative deal to extend the ceasefire between the two nations by 60 days and are on...
- [Nasdaq 100 and 10-Year yield drop together as correlation turns positive](https://www.google.com/goto?url=CAESqQEB6zswFdt7KAKEEMax2qaQaxFb4IEeZCnhL_ZiaA8qLl5vieTq0gDVXlc3HOMxV0xcn29oqFQJJQ9M5SA6zCE9amRS3u2rMhLbBVs0fhv9ZUllMa_ytA7GAAZ3C5Fu9Mlj7yRQBT9qfhg-RMhSUoHcDrb0CbLoqWzNjF0tE5-2mAL3Lj6MtdqG63wnxvF4EVKXu5ND-DhYiKTwsQ2WRD4yDV30NWBaHIJ7)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  The Nasdaq 100 (NDX) and the U.S. 10-year Treasury yield (US10Y) have begun declining in tandem. Learn more information here.
- [TIOmarkets Expands ETF Offering with 25 New Funds](https://www.google.com/goto?url=CAESfgHrOzAVZez0FYFU4QDbr8UzOxM7Db4B9QP7a4QO6GKLhc2Hv5zUl4pOtF5qLKHzi8McFDTPT2tESaeRHmj2EQFuPbQBmfw9QZB1C4FK84KcXAZ5C-7E9tlsqQGr6a6Z7XMkxM6uFf751_vzHmDopzvTSBNMBl255CZdu_bl-w)  
  <sub>LeapRate, 4 hours ago</sub>  
  TIOmarkets expands its offering with 25 new ETFs covering US stocks, global markets, technology, bonds and precious metals. Discover the new instruments.
- [You Check the Portfolio Every Morning at 6 A.M. and It Sets the Mood for the Day. These 3 ETFs Let You Stop Looking](https://247wallst.com/investing/etf/2026/10/27/you-check-the-portfolio-every-morning-at-6-a-m-and-it-sets-the-mood-for-the-day-these-3-etfs-let-you-stop-looking/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  That quick glance at your brokerage app before breakfast is doing something to your retirement that has nothing to do with the numbers on the screen.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 81.59 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 79.09 (+3.2%), 50d 80.55 (+1.3%), 200d 84.72 (-3.7%); 50d below 200d
Momentum: RSI(14) 63.5 | MACD 0.372 vs signal -0.106 (histogram 0.477)
Returns: 1d -0.1% | 5d +1.8% | 1m +3.8% | 3m -1.5%
52-week range: 77.11 - 92.02 (now 30.0% of the way up)
Volatility: ATR(14) 0.78 (1.0% of price) | annualised 20d 10.6%
Volume: 0.09x the 20-day average
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
Three-year record: +3.1% a year | beta to the market 2.31
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net short 34.0% of open interest (2,364,949 contracts)
Change on the week: -4.2% of open interest
Crowding: 45% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 109.70M | fund size: 8.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US dollar index up 0.44% on the week, no policy or inflation surprise
- Price near 52‑week high with RSI 62.6, MACD histogram negative, and volume 0.08× 20‑day average
- CFTC net long 6.4% of open interest, up 2.4% week, crowding 85% percentile – modest bullish bias but not decisive
- Fund flows: 1‑month share count +42.8% indicating inflows, 1‑week change flat
- Analyst coverage 49.4% of fund with no ratings or price targets

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 29.08 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 28.98 (+0.4%), 50d 28.52 (+2.0%), 200d 27.90 (+4.2%); 50d above 200d
Momentum: RSI(14) 62.6 | MACD 0.121 vs signal 0.146 (histogram -0.025)
Returns: 1d +0.2% | 5d +0.6% | 1m +1.3% | 3m +2.3%
52-week range: 26.47 - 29.13 (now 98.1% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 5.1%
Volume: 0.08x the 20-day average
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
Three-year record: +3.9% a year | beta to the market -11.39
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 6.4% of open interest (49,382 contracts)
Change on the week: +2.4% of open interest
Crowding: 85% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -0.0% (-149.64K) over 7d | 1 month: +42.8% (129.77M) over 31d
Shares outstanding: 14.89M | fund size: 433.07M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, thin analyst coverage, modest positioning shift, flat fund flows, mixed technicals.

**Main reasons it gave:**
- Treasury yields fell modestly (3‑month -0.04% to 4.04%) and VIX rose 0.6 to 17.94 – no macro surprise
- Analyst coverage thin (12.1% of fund) despite 67.6% buy rating and +19.2% price target
- CFTC positioning: net short 1.5% of open interest, decreasing by 1.2% week‑over‑week
- Fund flows flat: share count unchanged over the past month
- Technicals mixed: price 0.5% above 20‑day SMA but 2.2% below 50‑day SMA, RSI 47.4 (neutral)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.89 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 86.44 (+0.5%), 50d 88.84 (-2.2%), 200d 87.84 (-1.1%); 50d above 200d
Momentum: RSI(14) 47.4 | MACD -0.467 vs signal -0.650 (histogram 0.183)
Returns: 1d +0.4% | 5d -0.3% | 1m -1.7% | 3m -2.2%
52-week range: 77.90 - 93.19 (now 58.8% of the way up)
Volatility: ATR(14) 0.88 (1.0% of price) | annualised 20d 13.0%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.26 | P/B 2.24 | P/S 1.59 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +19.1% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 37.17B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.5%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Shell PLC 1.8%, Novartis AG Registered Shares 1.7%
Sector mix: Financial services 25.4%, Industrials 19.5%, Healthcare 12.1%, Technology 9.4%
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
Rolled up from the 5 largest holdings, 12.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.6% | hold 32.4% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 282.09M | fund size: 24.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields unchanged; yield curve remains upward sloping
- RSI 30.7 indicates oversold but price below 20‑day, 50‑day, 200‑day SMAs; volume 0.23× 20‑day average
- Analyst coverage thin (23.5% of fund) with 100% buy rating and +50% price target
- CFTC net long 2.1% of open interest, down 0.7% week‑over‑week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 56.71 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 58.72 (-3.4%), 50d 59.68 (-5.0%), 200d 58.33 (-2.8%); 50d above 200d
Momentum: RSI(14) 30.7 | MACD -0.833 vs signal -0.573 (histogram -0.260)
Returns: 1d +0.4% | 5d -2.6% | 1m -5.0% | 3m -0.4%
52-week range: 52.42 - 61.44 (now 47.6% of the way up)
Volatility: ATR(14) 0.64 (1.1% of price) | annualised 20d 15.0%
Volume: 0.23x the 20-day average
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
Three-year record: +17.8% a year | beta to the market 0.75
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
Weighted price target: +50.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 1.42B | fund size: 80.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Oracle Bonds Are Sliding as AI Debt Worries Grow. At 62, She Discovers the "Safe" Side of Her 401(k) Can Lose Money Too](https://247wallst.com/personal-finance/2026/10/27/oracle-bonds-are-sliding-as-ai-debt-worries-grow-at-62-she-discovers-the-safe-side-of-her-401k-can-lose-money-too/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Oracle's investment-grade bonds now carry a 263 basis point spread over Treasuries, wider than the average BB-rated junk bond, as AI debt fears grow.
- [TIOmarkets Expands ETF Offering with 25 New Funds](https://www.leaprate.com/retail-fx-cfd/tiomarkets-adds-25-new-etfs/)  
  <sub>LeapRate, 4 hours ago</sub>  
  TIOmarkets expands its offering with 25 new ETFs covering US stocks, global markets, technology, bonds and precious metals. Discover the new instruments.
- [Twenty-one options underlyings where premium stood out on 23 October](https://www.home.saxo/content/articles/options/twenty-one-options-markets-where-premium-stood-out-on-23-october-26102026)  
  <sub>Saxo, 18 hours ago</sub>  
  Twenty-one US and euro-zone option markets, ranked by how dear their options were against their own one-year range at the 23 October close.
- [U.S. ETF Express | Tradr 2X Long LITE Daily ETF Was the Top Gainer, Rising 16.41%](https://www.moomoo.com/news/post/1002395076/us-etf-express-tradr-2x-long-lite-daily-etf-was)  
  <sub>Moomoo, 17 hours ago</sub>  
  TopGainers/Losers4571 U.S. ETFs rose and 1558 fell today.The top gainer was $Tradr 2X Long LITE Daily ETF(LITX.US)$, climbing 16.41% to close at $22.35.
- [Nasdaq futures up 160 points: 5 things to know before Wall Street opens](https://invezz.com/nz/news/2026/10/26/nasdaq-futures-up-160-points-5-things-to-know-before-wall-street-opens/)  
  <sub>Invezz, 24 hours ago</sub>  
  US stock futures were in the green on Monday, with all three indexes seeming set to begin the week on a high at the opening bell.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.36 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 77.07 (+0.4%), 50d 78.19 (-1.1%), 200d 79.58 (-2.8%); 50d below 200d
Momentum: RSI(14) 48.1 | MACD -0.273 vs signal -0.379 (histogram 0.105)
Returns: 1d +0.2% | 5d +0.7% | 1m -0.2% | 3m -2.4%
52-week range: 76.81 - 81.28 (now 12.2% of the way up)
Volatility: ATR(14) 0.29 (0.4% of price) | annualised 20d 3.7%
Volume: 0.18x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 195.60M | fund size: 15.13B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Gold mining companies (GDX) · Sector or country — BULLISH, confidence 0.40

**Result:** ACCEPTED · 84 shares · submitted buy 84 GDX @ ~82.94, stop 77.13

**In the model's own words:**

> Analyst view: 100% buy rating covering 40.8% of fund, mean rating 1.71 (strong buy) and +22.5% price target; Fund flows: share count rose 9.3% in the past week (≈2.30B shares), indicating strong inflows; Fund basics: P/E 13.93, three‑year annualized return +41.6%, low expense ratio 0.51%

**Main reasons it gave:**
- Analyst view: 100% buy rating covering 40.8% of fund, mean rating 1.71 (strong buy) and +22.5% price target
- Fund flows: share count rose 9.3% in the past week (≈2.30B shares), indicating strong inflows
- Fund basics: P/E 13.93, three‑year annualized return +41.6%, low expense ratio 0.51%

<details><summary><b>News</b> — score +0.00</summary>

- [why gold miners fall even after record profits](https://www.kitco.com/opinion/2026-10-27/why-gold-miners-fall-even-after-record-profits)  
  <sub>Kitco, 2 hours ago</sub>  
  Newmont, the world's largest gold miner, reported record third-quarter adjusted net income on Thursday. On Friday, its shares fell 4.6 percent,...
- [Reevaluating The Leveraged JNUG ETF As Gold Consolidates Near The 2026 Low (NYSEARCA:JNUG)](https://seekingalpha.com/article/4957579-reevaluating-the-leveraged-jnug-etf-as-gold-consolidates-near-the-2026-low)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Direxion Daily Junior Gold Miners Idx Bull 2X ETF is a high-risk short-term trading tool for gold rallies. Click for this JNUG update.
- [Stockspot flags AI risks as ETF investors chase global shares and income](https://www.moneymanagement.com.au/stockspot-flags-ai-risks-as-etf-investors-chase-global-shares-and-income/)  
  <sub>Money Management, 12 hours ago</sub>  
  Stockspot's latest report has revealed where ETF investors are finding returns, while warning that chasing hot themes can leave portfolios exposed and...
- [GDXJ Stock Price, Quote & News](https://www.syfe.com/stocks/us/gdxj)  
  <sub>Syfe, 21 hours ago</sub>  
  Overview. VanEck Junior Gold Miners ETF (GDXJ) is trading at US$100.38, up 1.04% today as of Oct 26, 14:05 EDT. Over the past 52 weeks, GDXJ has traded between...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 82.14 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 85.88 (-4.4%), 50d 92.49 (-11.2%), 200d 90.84 (-9.6%); 50d above 200d
Momentum: RSI(14) 39.5 | MACD -2.538 vs signal -2.121 (histogram -0.416)
Returns: 1d +1.4% | 5d -4.6% | 1m -6.5% | 3m +11.6%
52-week range: 68.28 - 115.84 (now 29.1% of the way up)
Volatility: ATR(14) 2.85 (3.5% of price) | annualised 20d 37.9%
Volume: 0.22x the 20-day average
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
Three-year record: +41.6% a year | beta to the market 0.81
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 40.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.5% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - AEM.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - ABX.TO: 2026-10-22 Freedom Broker: down, Buy -> Hold
  - WPM.TO: 2026-10-08 UBS: main, Buy -> Buy
  - FNV.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +9.3% (2.30B) over 7d | 1 month: +0.5% (139.76M) over 31d
Shares outstanding: 327.53M | fund size: 26.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — BULLISH, confidence 0.40

**Result:** ACCEPTED · 39 shares · submitted buy 39 XLV @ ~179.20, stop 173.68

**In the model's own words:**

> The fund shows a moderately bullish outlook: strong analyst coverage with a 100% buy rating and a +5.5% price target on 44.3% of holdings; solid fundamentals with a 3‑year annualized return of +14% and a low expense ratio; technicals indicating the price is above its 20‑day, 50‑day and 200‑day SMAs with RSI 64 and a bullish MACD; and flat fund flows suggesting no net outflow pressure. No macro surprise or policy shift is present to alter the view.

**Main reasons it gave:**
- Analyst view: 100% buy rating covering 44.3% of fund, weighted price target +5.5% above current price
- Fund basics: 3‑year annualized return +14% per year and low expense ratio 0.08%
- Technicals: Price above 20‑day, 50‑day and 200‑day SMAs; RSI 64 and MACD bullish
- Fund flows: flat share count over past month, indicating no net outflow

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the State Street Health Care Select Sector SPDR ETF ETF (XLV)?](https://ca.finance.yahoo.com/news/invest-state-street-health-care-092002587.html)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Sector ETF report for XLV.
- [Which Healthcare ETF Is the Better Buy: Fidelity’s FHLC or State Street’s XLV?](https://www.fool.com/coverage/etfs/2026/10/26/which-healthcare-etf-is-the-better-buy-fidelity-s-fhlc-or-state-street-s-xlv/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  XLV concentrates on 61 large-cap S&P 500 names, while FHLC casts a wider net with 365 holdings across mid and small caps. Both charge 0.08% annually.
- [Healthcare stocks with strong revenue growth and attractive valuations (XLV:NYSEARCA)](https://seekingalpha.com/news/4657740-healthcare-stocks-with-strong-revenue-growth-and-attractive-valuations)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Healthcare stocks with strong year-over-year revenue growth and attractive valuations may draw attention as investors assess pharmaceutical demand,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.50</summary>

```text
Last close 179.42 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 173.31 (+3.5%), 50d 171.60 (+4.6%), 200d 158.29 (+13.4%); 50d above 200d
Momentum: RSI(14) 64.2 | MACD 2.934 vs signal 2.265 (histogram 0.669)
Returns: 1d +0.1% | 5d -0.2% | 1m +4.8% | 3m +7.9%
52-week range: 142.84 - 181.30 (now 95.1% of the way up)
Volatility: ATR(14) 2.75 (1.5% of price) | annualised 20d 19.3%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +14.0% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
Sector mix: Healthcare 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.5% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-21 Leerink Partners: main, Outperform -> Outperform
  - JNJ: 2026-10-16 Wells Fargo: main, Overweight -> Overweight
  - ABBV: 2026-10-23 Goldman Sachs: main, Neutral -> Neutral
  - MRK: 2026-10-26 Barclays: main, Overweight -> Overweight
  - UNH: 2026-10-27 Wells Fargo: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 197.42M | fund size: 35.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish technicals and fund outflows versus bullish analyst consensus and neutral fundamentals; no macro surprise.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs with negative MACD, indicating bearish technical momentum
- Net outflow of -7.8% over the past month, showing bearish investor sentiment
- Analyst consensus 100% buy with a weighted price target +38.1% above current price
- No macro surprise; yields slightly down but stable, no policy shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 83.52 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 87.02 (-4.0%), 50d 90.82 (-8.0%), 200d 92.18 (-9.4%); 50d below 200d
Momentum: RSI(14) 35.4 | MACD -1.610 vs signal -1.363 (histogram -0.247)
Returns: 1d +0.9% | 5d -4.2% | 1m -3.4% | 3m -10.2%
52-week range: 82.77 - 102.94 (now 3.7% of the way up)
Volatility: ATR(14) 2.13 (2.6% of price) | annualised 20d 33.1%
Volume: 0.37x the 20-day average
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
Three-year record: +32.5% a year | beta to the market 0.45
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 49.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +38.1% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-27 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-10-13 UBS: main, Neutral -> Neutral
  - PAM: 2026-09-01 JP Morgan: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.1% (7.49M) over 7d | 1 month: -7.8% (-57.82M) over 31d
Shares outstanding: 8.24M | fund size: 688.12M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals are neutral, modest inflows and modest analyst bullishness, fundamentals are solid but not extraordinary.

**Main reasons it gave:**
- Treasury yields fell modestly across the curve, no policy surprise
- RSI 50.2 and MACD -0.063 indicate neutral technical momentum
- Weekly share count rose 2.7% (≈$970M), modest inflow but not decisive
- Analyst coverage shows 73% buy rating with mean rating 2.21 (modest bullish bias)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 44.17 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 43.98 (+0.4%), 50d 44.38 (-0.5%), 200d 40.26 (+9.7%); 50d above 200d
Momentum: RSI(14) 50.2 | MACD -0.063 vs signal -0.040 (histogram -0.022)
Returns: 1d +1.3% | 5d -0.1% | 1m -1.1% | 3m +6.3%
52-week range: 32.56 - 45.76 (now 88.0% of the way up)
Volatility: ATR(14) 0.67 (1.5% of price) | annualised 20d 21.5%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.22 | P/B 2.06 | P/S 1.40 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +38.9% a year | beta to the market 0.64
Cost and size: expense ratio 0.59% | net assets 833.96M
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: PKO Bank Polski SA 16.2%, Orlen SA 12.7%, Bank Polska Kasa Opieki SA 7.4%, Powszechny Zaklad Ubezpieczen SA 6.0%, Allegro.EU SA Ordinary Shares 4.9%
Sector mix: Financial services 46.9%, Energy 13.3%, Consumer cyclical 13.2%, Basic materials 6.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.1% of the fund by weight
Ratings by weight: buy 73.1% | hold 26.9% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.1% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, ALE.WA
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
Share count change: 1 week: +2.7% (21.97M) over 7d | 1 month: +0.8% (6.59M) over 31d
Shares outstanding: 19.18M | fund size: 847.28M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bearish analyst view offset by solid fundamentals, flat fund flows, and modestly bullish technicals.

**Main reasons it gave:**
- Analyst rating mean 3.41 (sell bias)
- Weighted price target -8.1% below current price
- Fund flows flat (0% change week/month)
- Technical price above 20‑day, 50‑day, 200‑day SMAs with positive MACD

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 29.44 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 28.71 (+2.6%), 50d 29.14 (+1.0%), 200d 28.85 (+2.1%); 50d above 200d
Momentum: RSI(14) 60.6 | MACD 0.090 vs signal -0.024 (histogram 0.114)
Returns: 1d +0.9% | 5d +1.0% | 1m +3.3% | 3m +1.2%
52-week range: 24.95 - 30.43 (now 82.0% of the way up)
Volatility: ATR(14) 0.30 (1.0% of price) | annualised 20d 11.9%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.31 | P/B 2.65 | P/S 3.31 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +16.0% a year | beta to the market 0.98
Cost and size: expense ratio 0.50% | net assets 1.21B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: BHP Group Ltd 15.4%, Commonwealth Bank of Australia 12.6%, National Australia Bank Ltd 6.1%, Westpac Banking Corp 6.0%, ANZ Group Holdings Ltd 5.8%
Sector mix: Financial services 42.0%, Basic materials 25.4%, Consumer cyclical 6.5%, Healthcare 5.6%
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

<details><summary><b>What analysts and big funds say</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.30</summary>

```text
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -8.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 63.60M | fund size: 1.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, tentative policy news, flat fund flows, and modest technicals.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand
- Price above 20‑day, 50‑day, and 200‑day SMAs but volume at 0.2× 20‑day average
- Macro data (inflation 3.7%, Fed target unchanged) shows no surprise
- US‑Canada tariff talks are tentative, not a confirmed policy change

<details><summary><b>News</b> — score +0.00</summary>

- [US, Canada in talks to ease steel and auto tariffs: report (EWC:NYSEARCA)](https://seekingalpha.com/news/4657653-us-canada-in-talks-to-ease-steel-and-auto-tariffs-report)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  The United States ​and Canada are working on a deal to ease US tariffs on Canadian steel and autos, as the two governments try to repair relations that...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.87 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 59.70 (+2.0%), 50d 60.46 (+0.7%), 200d 58.22 (+4.6%); 50d above 200d
Momentum: RSI(14) 56.8 | MACD 0.283 vs signal 0.080 (histogram 0.203)
Returns: 1d +0.0% | 5d +0.0% | 1m +3.0% | 3m +2.7%
52-week range: 49.72 - 62.64 (now 86.3% of the way up)
Volatility: ATR(14) 0.67 (1.1% of price) | annualised 20d 14.5%
Volume: 0.20x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 79.8% | hold 20.2% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 94.80M | fund size: 5.77B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; analyst view bullish but limited coverage, fundamentals modestly positive, flows flat.

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings, weighted price target +15.5% above current price
- Fund flows: share count unchanged (flat) over past week and month
- Technicals: price above 20‑day SMA and MACD above signal, but volume at 0.09× 20‑day average
- Macro: yields down modestly, no policy surprise; VIX at 17.9 indicating moderate volatility
- Fundamentals: moderate valuation (P/E 14.6), 3.6% yield, three‑year record +20.8% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 51.09 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 50.53 (+1.1%), 50d 51.63 (-1.0%), 200d 51.49 (-0.8%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD -0.151 vs signal -0.229 (histogram 0.078)
Returns: 1d +1.0% | 5d +0.0% | 1m +0.3% | 3m -0.3%
52-week range: 45.38 - 54.72 (now 61.1% of the way up)
Volatility: ATR(14) 0.66 (1.3% of price) | annualised 20d 13.9%
Volume: 0.09x the 20-day average
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
Three-year record: +20.8% a year | beta to the market 1.25
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 7.65M | fund size: 390.84M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, flat flows, and bullish analyst view not enough to shift direction.

**Main reasons it gave:**
- Inflation 3.7% and rates unchanged; no macro surprise
- Price 41.47 above 20‑day SMA (41.20) but below 50‑day (42.42) and 200‑day (42.26) SMAs
- Flat fund flows: share count unchanged (+0.0% week, +0.0% month)
- Analyst ratings 78.7% buy with +20.4% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.47 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 41.20 (+0.6%), 50d 42.42 (-2.2%), 200d 42.26 (-1.9%); 50d above 200d
Momentum: RSI(14) 48.5 | MACD -0.247 vs signal -0.336 (histogram 0.089)
Returns: 1d +0.5% | 5d +0.1% | 1m -1.6% | 3m -1.1%
52-week range: 38.08 - 44.59 (now 52.0% of the way up)
Volatility: ATR(14) 0.49 (1.2% of price) | annualised 20d 14.7%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +19.8% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.96 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 79.50M | fund size: 3.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst view is strongly bullish (100% buy, +22.3% price target) but fund flows are flat and technicals show price below short‑term averages with modest momentum, leading to a neutral overall stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating, price target +22.3% above current price
- Fund flows: flat share count (0% change over 1 week and 1 month)
- Fund basics: P/E 14.42, yield 3.2%, three‑year record +27% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 55.87 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 56.42 (-1.0%), 50d 59.45 (-6.0%), 200d 58.13 (-3.9%); 50d above 200d
Momentum: RSI(14) 39.8 | MACD -1.144 vs signal -1.216 (histogram 0.072)
Returns: 1d +0.8% | 5d -0.2% | 1m -6.9% | 3m -7.0%
52-week range: 50.70 - 63.35 (now 40.9% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 19.6%
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
Three-year record: +27.0% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 8.55M | fund size: 477.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; fundamentals are solid but no new catalyst, technicals are mixed, analyst coverage is thin, and positioning shows only modest bullish bias.

**Main reasons it gave:**
- No macro surprise: yields modestly down, dollar slightly up, VIX unchanged
- Technicals mixed: price above 200‑day SMA but below 20‑day/50‑day SMAs, RSI 43.8, MACD negative, low volume
- Analyst coverage thin (17% of fund) despite 100% buy rating and +27.4% price target
- Speculators net long only 2.3% of open interest, modest weekly increase (+4.7%) and low crowding (28th percentile)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 95.06 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 96.54 (-1.5%), 50d 96.57 (-1.6%), 200d 91.65 (+3.7%); 50d above 200d
Momentum: RSI(14) 43.8 | MACD -0.680 vs signal -0.415 (histogram -0.265)
Returns: 1d +0.8% | 5d -0.4% | 1m -1.8% | 3m +6.4%
52-week range: 79.49 - 99.32 (now 78.5% of the way up)
Volatility: ATR(14) 1.19 (1.3% of price) | annualised 20d 12.5%
Volume: 0.09x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Japan Stock
What it holds: P/E 15.27 | P/B 1.98 | P/S 1.37 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +21.0% a year | beta to the market 0.83
Cost and size: expense ratio 0.49% | net assets 23.53B
What it is made of: Stocks 99.1%, Cash 0.9%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.7%, Toyota Motor Corp 3.3%, Tokyo Electron Ltd 3.1%, Sumitomo Mitsui Financial Group Inc 3.0%, Advantest Corp 3.0%
Sector mix: Industrials 22.8%, Technology 22.0%, Financial services 19.3%, Consumer cyclical 11.1%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.4% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 227.85M | fund size: 21.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, modest analyst bullishness but limited coverage, technicals bullish but low volume.

**Main reasons it gave:**
- No macro data surprise; inflation 3.7% in line with expectations
- Fund flows flat (share count unchanged) indicating neutral demand
- Analyst coverage: 64.8% buy, weighted price target +3.6% above current
- Technicals: price above 20‑, 50‑, 200‑day SMAs but 20‑day volume at 0.10× average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.30 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 60.97 (+3.8%), 50d 61.56 (+2.8%), 200d 61.73 (+2.5%); 50d below 200d
Momentum: RSI(14) 65.2 | MACD 0.673 vs signal 0.304 (histogram 0.369)
Returns: 1d +0.6% | 5d +0.4% | 1m +4.8% | 3m +0.8%
52-week range: 55.06 - 65.08 (now 82.2% of the way up)
Volatility: ATR(14) 0.63 (1.0% of price) | annualised 20d 14.1%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.08 | P/B 4.13 | P/S 2.67 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +16.5% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.67B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.9%, Novartis AG Registered Shares 12.4%, Nestle SA 11.0%, UBS Group AG Registered Shares 6.4%, ABB Ltd 4.6%
Sector mix: Healthcare 38.0%, Financial services 19.6%, Consumer defensive 13.1%, Industrials 12.3%
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
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 28.62M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, bearish technicals with low volume, strong analyst rating but limited coverage, moderate fundamentals.

**Main reasons it gave:**
- Technical indicators show price below 20d, 50d, and 200d SMAs, RSI 38.9, MACD negative (bearish)
- Fund flows are flat with 0% share count change over the past week and month (neutral demand)
- Analyst coverage of top holdings (46.7% weight) rates 100% buy with +45.8% price target (bullish but limited coverage)
- Macro data shows no surprise; yields up slightly, dollar stronger, inflation 3.7% (no material catalyst)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 64.35 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 65.81 (-2.2%), 50d 67.24 (-4.3%), 200d 64.98 (-1.0%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.929 vs signal -0.792 (histogram -0.137)
Returns: 1d +0.7% | 5d -1.0% | 1m -5.5% | 3m -0.3%
52-week range: 55.33 - 71.61 (now 55.4% of the way up)
Volatility: ATR(14) 0.91 (1.4% of price) | annualised 20d 17.2%
Volume: 0.01x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.85 | P/B 2.55 | P/S 1.87 | 3y earnings growth n/a
Yield: 4.2%
Three-year record: +23.6% a year | beta to the market 1.09
Cost and size: expense ratio 0.50% | net assets 710.44M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: ASML Holding NV 23.6%, ING Groep NV 9.1%, Nebius Group NV Shs Class-A- 4.9%, Prosus NV Ordinary Shares - Class N 4.6%, ASM International NV 4.4%
Sector mix: Technology 33.4%, Financial services 21.5%, Consumer defensive 10.4%, Industrials 9.6%
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
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +45.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 5.55M | fund size: 357.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, moderate analyst optimism, technicals lack decisive break.

**Main reasons it gave:**
- Analyst consensus: 51.5% buy, 48.5% hold, weighted price target +10.7% (moderate bullishness)
- Fund flows flat over 1 week and 1 month (no net inflow/outflow)
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs, low volume, RSI 40.4, MACD slightly bullish but no decisive break
- Macro: no surprise in rates or data; yields slightly down but still high, VIX moderate

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.56 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 58.05 (-0.8%), 50d 60.29 (-4.5%), 200d 57.93 (-0.6%); 50d above 200d
Momentum: RSI(14) 40.4 | MACD -0.751 vs signal -0.794 (histogram 0.043)
Returns: 1d +0.6% | 5d -0.9% | 1m -5.1% | 3m -3.1%
52-week range: 49.37 - 63.23 (now 59.1% of the way up)
Volatility: ATR(14) 0.77 (1.3% of price) | annualised 20d 16.0%
Volume: 0.04x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 55.8% of the fund by weight
Ratings by weight: buy 51.5% | hold 48.5% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 37.35M | fund size: 2.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral – no macro surprise, mixed technicals, flat fund flows, and analyst bullishness limited to ~40% of the fund.

**Main reasons it gave:**
- No macro surprise: yields down modestly, curve normal, inflation and unemployment in line with expectations
- Technical indicators mixed: price below 20‑day and 50‑day SMA, RSI 43.4, MACD negative, low volume
- Fund flows flat: share count unchanged over week and month
- Analyst view bullish (+43.9% price target) but covers only 39.1% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 107.00 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 111.03 (-3.6%), 50d 110.13 (-2.8%), 200d 92.75 (+15.4%); 50d above 200d
Momentum: RSI(14) 43.4 | MACD -1.558 vs signal -0.712 (histogram -0.847)
Returns: 1d +1.3% | 5d -0.3% | 1m -6.3% | 3m +19.7%
52-week range: 60.03 - 118.00 (now 81.0% of the way up)
Volatility: ATR(14) 2.34 (2.2% of price) | annualised 20d 28.7%
Volume: 0.23x the 20-day average
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
Three-year record: +42.5% a year | beta to the market 1.26
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
Weighted price target: +43.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 85.00M | fund size: 9.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or policy shift; technicals mixed with no decisive break; fund flows flat; analyst coverage limited and only modestly bullish.

**Main reasons it gave:**
- No macro surprise: yields down modestly, Fed policy unchanged
- Technical indicators mixed: price above 20‑day and 200‑day SMA but below 50‑day SMA, RSI 49.3, low volume
- Fund flows flat: share count unchanged over week and month
- Analyst coverage limited to 37.4% of fund, with 59.1% buy rating and +16.6% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.26 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 46.95 (+0.6%), 50d 47.62 (-0.8%), 200d 46.93 (+0.7%); 50d above 200d
Momentum: RSI(14) 49.3 | MACD 0.079 vs signal -0.017 (histogram 0.096)
Returns: 1d -0.7% | 5d -1.1% | 1m -0.0% | 3m -1.3%
52-week range: 41.34 - 49.39 (now 73.5% of the way up)
Volatility: ATR(14) 0.48 (1.0% of price) | annualised 20d 12.8%
Volume: 0.08x the 20-day average
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
Three-year record: +20.1% a year | beta to the market 0.71
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
Ratings by weight: buy 59.1% | hold 40.9% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 67.80M | fund size: 3.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, mixed technicals, and bullish analyst view not enough to shift direction.

**Main reasons it gave:**
- Flat fund flows (0% share count change over 1 week and 1 month)
- Technicals: price above 20‑day (73.36) and 50‑day (74.46) SMAs but below 200‑day SMA (76.13), low volume (0.20× 20‑day avg)
- Analyst view: 90.9% buy rating, weighted price target +6.7% above current
- Macro unchanged: yields down slightly, no data surprise (inflation 3.7%, unemployment 4.2%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 75.25 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 73.36 (+2.6%), 50d 74.46 (+1.1%), 200d 76.13 (-1.1%); 50d below 200d
Momentum: RSI(14) 57.9 | MACD 0.459 vs signal 0.124 (histogram 0.335)
Returns: 1d -0.1% | 5d -0.3% | 1m +4.0% | 3m -0.4%
52-week range: 65.65 - 81.23 (now 61.6% of the way up)
Volatility: ATR(14) 1.23 (1.6% of price) | annualised 20d 16.9%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +16.2% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
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
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 18.90M | fund size: 1.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: fundamentals are modestly positive but technicals are weak, macro shows no surprise, and fund flows are flat.

**Main reasons it gave:**
- Share count unchanged (+0.0% week, +0.0% month)
- Price 156.38 below 20d SMA 167.79, 50d SMA 176.18, 200d SMA 161.89
- RSI 40.3 indicating slight bearish momentum
- Treasury yields stable (10-year 4.99% down 0.12% week) and Fed target unchanged at 4.00%

<details><summary><b>News</b> — score +0.00</summary>

- [EWY Jan 2029 250.000 call (EWY290119C00250000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/EWY290119C00250000/chart/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Interactive Chart for EWY Jan 2029 250.000 call (EWY290119C00250000), analyze all the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 156.38 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 167.79 (-6.8%), 50d 176.18 (-11.2%), 200d 161.89 (-3.4%); 50d above 200d
Momentum: RSI(14) 40.3 | MACD -7.892 vs signal -6.654 (histogram -1.239)
Returns: 1d +2.4% | 5d +1.5% | 1m -14.8% | 3m +8.4%
52-week range: 88.53 - 219.20 (now 51.9% of the way up)
Volatility: ATR(14) 5.94 (3.8% of price) | annualised 20d 43.3%
Volume: 0.23x the 20-day average
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
Three-year record: +41.7% a year | beta to the market 2.48
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 75.60M | fund size: 11.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, and technicals show no decisive break despite bullish analyst view and solid fundamentals.

**Main reasons it gave:**
- Fund flows flat: 0.0% share count change over 1 week and 1 month
- Macro unchanged: Treasury yields down modestly, no policy surprise, normal upward yield curve
- Technical indicators neutral: RSI 44.9, MACD near zero, volume 0.11x 20‑day average
- Analyst view bullish: 100% buy rating, +34.2% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 63.90 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 63.85 (+0.1%), 50d 67.17 (-4.9%), 200d 68.69 (-7.0%); 50d below 200d
Momentum: RSI(14) 44.9 | MACD -0.692 vs signal -0.818 (histogram 0.127)
Returns: 1d +0.6% | 5d -2.4% | 1m -0.9% | 3m +2.9%
52-week range: 60.43 - 81.60 (now 16.4% of the way up)
Volatility: ATR(14) 1.16 (1.8% of price) | annualised 20d 21.4%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.44 | P/B 2.00 | P/S 1.73 | 3y earnings growth n/a
Yield: 7.9%
Three-year record: +25.9% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 473.79M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 12.7%, Gold Fields Ltd 8.7%, Naspers Ltd Class N 8.4%, Firstrand Ltd 7.4%, Standard Bank Group Ltd 6.2%
Sector mix: Basic materials 39.1%, Financial services 34.4%, Consumer cyclical 12.8%, Communication services 6.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 7.90M | fund size: 504.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a strong analyst consensus (100% buy, mean rating 1.65) and a bullish technical trend (price above 20‑, 50‑, and 200‑day SMAs, RSI 58.5, MACD positive). However, fund flows are flat, indicating no net demand, and the fund’s fundamentals are mixed – high valuations (P/E 31.9, P/B 7.5) temper the bullish view. Macro conditions are neutral with no surprise data. Overall, the bullish and bearish signals offset, leading to a neutral directional call.

**Main reasons it gave:**
- Analyst consensus: 100% buy, mean rating 1.65 (strong buy)
- Technical trend: price above 20‑, 50‑, 200‑day SMAs; RSI 58.5; MACD positive
- Fund flows: flat share count, no net creations/redemptions
- Fundamentals: high valuations (P/E 31.9, P/B 7.5) suggest caution
- Short interest ratio low (1‑4), indicating strong positive sentiment

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Expanded Tech-Software Sector ETF (IGV) Short Interest & Short Float | Updated Oct 2026](https://www.marketbeat.com/stocks/BATS/IGV/short-interest/)  
  <sub>MarketBeat, 10 hours ago</sub>  
  A short interest ratio ranging between 1 and 4 generally indicates strong positive sentiment about a stock and a lack of short sellers. A short interest ratio...
- [iShares Expanded Tech-Software (IGV) Sells $9.1 Million of Palantir on Friday](https://www.google.com/goto?url=CAESngEB6zswFVjij3SCDaroNSu48b6sPcQI4j6qb6yYGktHqCcfHvouInBfF2KH5fS6zoWUuWvGV31duJz7HyqAgaKhulzCPIJ2kDRv9mjWvQA1F0zojVS7kZG3bsmEk9V1lewFqtL4wIk1C0moDYweh6qwgV5suUE3yASS2i-YmtC8LeE7hc74uG7xhUmLqZ-LzNs3V7H-c0sf4Y4L0TYDnQ)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. iShares Expanded Tech-Software Sector ETF (IGV) recorded a net outflow of $99.5 million in Friday's session,...
- [Form 4 iShares Expanded Tech-Software Sector ETF For: 26 October](https://ca.investing.com/news/stock-market-news/form-4-ishares-expanded-techsoftware-sector-etf-for-26-october-93CH-4903805)  
  <sub>Investing.com Canada, 19 hours ago</sub>  
  The information in this preliminary pricing supplement is not complete and may be changed. This preliminary pricing supplement and the accompanying product...
- [Closing Bell Movers: Celestica jumps 17% on earnings beat](https://www.tipranks.com/news/the-fly/closing-bell-movers-celestica-jumps-17-on-earnings-beat-thefly-news)  
  <sub>TipRanks, 15 hours ago</sub>  
  Nasdaq Composite and S&P 500 bounced after two consecutive losing sessions, as the S-1 pre-IPO filing by Anthropic revived investor optimism in the AI trade...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.50</summary>

```text
Last close 111.41 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 109.19 (+2.0%), 50d 106.64 (+4.5%), 200d 93.89 (+18.7%); 50d above 200d
Momentum: RSI(14) 58.5 | MACD 1.064 vs signal 0.977 (histogram 0.087)
Returns: 1d +0.0% | 5d +4.2% | 1m +5.7% | 3m +20.6%
52-week range: 74.67 - 117.08 (now 86.6% of the way up)
Volatility: ATR(14) 2.63 (2.4% of price) | annualised 20d 28.6%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 31.87 | P/B 7.50 | P/S 8.53 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +17.7% a year | beta to the market 1.22
Cost and size: expense ratio 0.38% | net assets 13.91B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Palo Alto Networks Inc 9.7%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, CrowdStrike Holdings Inc Class A 8.9%, Microsoft Corp 8.5%, Oracle Corp 6.9%
Sector mix: Technology 93.2%, Communication services 4.2%, Financial services 2.2%, Consumer cyclical 0.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-15 Citigroup: main, Buy -> Buy
  - PLTR: 2026-10-23 Piper Sandler: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 12.50M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- 1‑month net outflows of -10.1% indicate bearish flow but no macro catalyst
- Price below 50‑day and 200‑day SMA, with 50‑day SMA below 200‑day SMA
- Analyst consensus 100% buy covers only 23.7% of fund weight
- No macro surprise in inflation, unemployment, or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 46.81 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 46.82 (-0.0%), 50d 48.01 (-2.5%), 200d 49.26 (-5.0%); 50d below 200d
Momentum: RSI(14) 45.5 | MACD -0.237 vs signal -0.287 (histogram 0.050)
Returns: 1d +0.5% | 5d -2.0% | 1m -0.6% | 3m -4.8%
52-week range: 45.42 - 54.83 (now 14.8% of the way up)
Volatility: ATR(14) 0.51 (1.1% of price) | annualised 20d 16.2%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: India Equity
What it holds: P/E 21.36 | P/B 2.96 | P/S 2.56 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.4% a year | beta to the market 0.62
Cost and size: expense ratio 0.61% | net assets 5.83B
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: HDFC Bank Ltd 6.4%, ICICI Bank Ltd 5.6%, Reliance Industries Ltd 5.4%, Bharti Airtel Ltd 3.9%, Infosys Ltd 2.4%
Sector mix: Financial services 29.7%, Consumer cyclical 12.3%, Industrials 10.2%, Basic materials 8.5%
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
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.7% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.9% (165.91M) over 7d | 1 month: -10.1% (-657.79M) over 31d
Shares outstanding: 125.57M | fund size: 5.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, bearish technicals, modest outflow, but strong analyst bullishness balances to a neutral view.

**Main reasons it gave:**
- Fund flows: -5.9% net outflow over month (money leaving the fund)
- Technical trend: price below 20‑day, 50‑day, and 200‑day SMAs, RSI 41.2 (downtrend)
- Macro: yields unchanged, no policy surprise (normal upward slope, VIX 17.94)
- Analyst view: 100% buy rating, weighted price target +30.5% above current price

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 204.98 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 206.11 (-0.5%), 50d 216.77 (-5.4%), 200d 229.33 (-10.6%); 50d below 200d
Momentum: RSI(14) 41.2 | MACD -3.086 vs signal -3.807 (histogram 0.721)
Returns: 1d -1.1% | 5d -0.6% | 1m -2.0% | 3m -13.2%
52-week range: 198.23 - 253.22 (now 12.3% of the way up)
Volatility: ATR(14) 4.06 (2.0% of price) | annualised 20d 16.8%
Volume: 0.25x the 20-day average
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
Three-year record: +24.6% a year | beta to the market 0.98
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.5% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-10-21 UBS: main, Buy -> Buy
  - RTX: 2026-10-21 UBS: main, Neutral -> Neutral
  - BA: 2026-10-19 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - HWM: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - LMT: 2026-10-26 JP Morgan: main, Neutral -> Neutral
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
Share count change: 1 week: +3.4% (401.87M) over 7d | 1 month: -5.9% (-764.28M) over 31d
Shares outstanding: 59.99M | fund size: 12.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, flat fund flows, modest technicals, and limited analyst coverage

**Main reasons it gave:**
- Flat fund flows (share count unchanged over week and month)
- Macro data in line with expectations (inflation 3.7%, unemployment 4.2%)
- Technical indicators modestly bullish but low volume and no decisive break (RSI 52.3, MACD above signal, volume 0.11x 20‑day avg)
- Analyst coverage bullish (+27% price target) but only covers ~52% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the iShares U.S. Industrials ETF (IYJ)?](https://finance.yahoo.com/markets/stocks/articles/invest-ishares-u-industrials-etf-092001257.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the iShares U.S. Industrials ETF (IYJ),...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.01 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 79.98 (+1.3%), 50d 81.80 (-1.0%), 200d 81.63 (-0.8%); 50d above 200d
Momentum: RSI(14) 52.3 | MACD -0.172 vs signal -0.460 (histogram 0.289)
Returns: 1d +0.4% | 5d +1.4% | 1m +2.5% | 3m -5.5%
52-week range: 68.14 - 90.01 (now 58.8% of the way up)
Volatility: ATR(14) 1.31 (1.6% of price) | annualised 20d 17.6%
Volume: 0.11x the 20-day average
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
Three-year record: +14.2% a year | beta to the market 1.32
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 2.80M | fund size: 226.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: modest bullish analyst view (thin coverage), solid fundamentals, but strong outflows indicate bearish pressure; macro and technicals are neutral.

**Main reasons it gave:**
- Fund flows: -9.8% share count over past month (outflows)
- Analyst coverage: 59.8% buy, price target +10.7% for 5.7% of fund (thin coverage)
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs but volume 0.2× 20‑day average
- Macro: yields down slightly, inflation 3.7% and unemployment 4.2% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [Anthropic's IPO could set off forced buying by index funds. SpaceX shows how that played out.](https://finance.yahoo.com/markets/article/anthropics-ipo-could-set-off-forced-buying-by-index-funds-spacex-shows-how-that-played-out-161356189.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  SpaceX joined the Nasdaq-100 faster than any company in history. Then its stock fell 15% in its first week there. Anthropic could be next.
- [Brazil Implodes -21%. Cybersecurity Breaks Out. The Market Doesn't Care About Either.](https://www.barchart.com/story/news/8459285/brazil-implodes-21-cybersecurity-breaks-out-the-market-doesn-t-care-about-either)  
  <sub>Barchart.com, 20 hours ago</sub>  
  ETF Market Strategist & Derivatives Trader | CMT | Author, Physical Over Digital Alpha | Featured Author, Barchart | 500+ Institutional Subscribers.
- [Daily ETF Flows: GLD Loses Assets](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-gld-loses-003806670.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SOXL · Direxion Daily Semiconductor Bull 3X ETF. 1,604.29.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 72.47 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 70.27 (+3.1%), 50d 72.16 (+0.4%), 200d 70.90 (+2.2%); 50d above 200d
Momentum: RSI(14) 58.5 | MACD 0.057 vs signal -0.483 (histogram 0.540)
Returns: 1d -0.4% | 5d +2.6% | 1m +2.7% | 3m -4.9%
52-week range: 58.63 - 77.93 (now 71.7% of the way up)
Volatility: ATR(14) 1.25 (1.7% of price) | annualised 20d 17.3%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 12.02 | P/B 1.21 | P/S 3.59 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +26.3% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: United Bankshares Inc 1.1%, First Interstate BancSystem Inc 1.1%, Old National Bancorp 1.1%, Hancock Whitney Corp 1.1%, East West Bancorp Inc 1.1%
Sector mix: Financial services 100.0%
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
Rolled up from the 5 largest holdings, 5.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-22 TD Cowen: main, Buy -> Buy
  - HWC: 2026-10-21 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - EWBC: 2026-10-22 Citigroup: main, Buy -> Buy
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
Share count change: 1 week: -3.6% (-140.21M) over 7d | 1 month: -9.8% (-403.66M) over 31d
Shares outstanding: 51.43M | fund size: 3.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst coverage and fund inflows are offset by bearish technicals and modestly weak fundamentals, with no macro surprise.

**Main reasons it gave:**
- Analyst coverage: 90.3% buy rating and +20.7% price target for top holdings (44.6% of fund)
- Fund inflows: share count up 4.4% week-over-week indicating demand
- Technical downtrend: price below 20d, 50d, 200d SMAs, RSI 37.1, MACD negative
- Macro environment stable: no policy surprise, yields slightly down, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 34.67 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 35.42 (-2.1%), 50d 37.00 (-6.3%), 200d 38.02 (-8.8%); 50d below 200d
Momentum: RSI(14) 37.1 | MACD -0.808 vs signal -0.733 (histogram -0.076)
Returns: 1d +2.0% | 5d -0.3% | 1m -6.2% | 3m -4.6%
52-week range: 33.69 - 41.03 (now 13.4% of the way up)
Volatility: ATR(14) 0.39 (1.1% of price) | annualised 20d 16.8%
Volume: 1.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.08 | P/B 1.70 | P/S 2.84 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +0.5% a year | beta to the market 0.19
Cost and size: expense ratio 0.75% | net assets 588.43M
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.5%, Saudi National Bank 8.6%, Saudi Telecom Co 6.1%, Saudi Arabian Mining Co 4.3%
Sector mix: Financial services 42.2%, Energy 12.5%, Basic materials 12.4%, Communication services 9.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.7% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +4.4% (25.24M) over 7d | 1 month: +1.8% (10.53M) over 31d
Shares outstanding: 17.42M | fund size: 604.10M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bearish, but analyst view bullish (limited coverage) and modest inflows keep the overall stance neutral.

**Main reasons it gave:**
- No macro catalyst: Fed target unchanged, yields stable, no policy surprise
- Technical indicators bearish: price below 20d, 50d, 200d SMAs; RSI 28.2; MACD negative; low volume
- Analyst view strongly bullish (100% buy, +70.7% price target) but covers only 32.3% of fund
- Fund flows positive (+4.3% weekly share count increase) indicating modest demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 48.96 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 51.11 (-4.2%), 50d 52.81 (-7.3%), 200d 55.95 (-12.5%); 50d below 200d
Momentum: RSI(14) 28.2 | MACD -1.030 vs signal -0.806 (histogram -0.223)
Returns: 1d -0.3% | 5d -3.9% | 1m -6.8% | 3m -11.1%
52-week range: 48.96 - 65.59 (now 0.0% of the way up)
Volatility: ATR(14) 0.64 (1.3% of price) | annualised 20d 17.7%
Volume: 0.18x the 20-day average
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
Three-year record: +8.7% a year | beta to the market 0.45
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +70.7% above the current prices
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
Share count change: 1 week: +4.3% (245.33M) over 7d | 1 month: +2.8% (160.28M) over 31d
Shares outstanding: 121.92M | fund size: 5.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, high valuations, and bullish analyst view limited to 44.3% of the fund.

**Main reasons it gave:**
- Macro: yields down modestly, no policy surprise
- Fund flows: flat share count (0% change week/month)
- Technical: price above 200‑day SMA but below 20‑day SMA, RSI 43.6, low volume
- Analyst view: 100% buy, +46% price target, covering 44.3% of fund
- Fundamentals: high valuation multiples (P/E 32.5, P/B 11.65)

<details><summary><b>News</b> — score +0.00</summary>

- [Investors Buy the Dip in Chip ETFs as Inflows Top $44B](https://www.etf.com/sections/weekly-etf-flows/investors-buy-dip-chip-etfs-inflows-top-44b)  
  <sub>ETF.com, 18 hours ago</sub>  
  Investors put $44.1 billion to work in US-listed ETFs during the week ending Friday, Oct. 23. That brought year-to-date inflows to $1.69 trillion.
- [Xtrackers MSCI World UCITS ETF 1C (XWR.SI) risk](https://www.google.com/goto?url=CAESagHrOzAVPXNbXT8ctOCzzVASHfFSmrwA6uh9MYEhSsEYeCAKvxdJyySYuARqCRgqja6NY7ZhmptyohhzNKyjeLhOuzJ4nduv0Hnfx71mqr-RK-NrVSQvBstjhbH110GIqKwMnFap__Ci3nk)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Xtrackers MSCI World UCITS ETF 1C (XWR.SI). 204.79 +0.51 (+0.25%). At close: 17:04:57 GMT+8. Risk data is currently unavailable for XWR.SI.
- [5 ETFs That Outperform the S&P 500 | Financial Advisors](https://www.google.com/goto?url=CAESkAEB6zswFfqitKRBzQcxFdDoVb6dXwbd5K9B8qAcBcWXBhxKMuLh5Pj-gTKBmcLmVjxOINz_cAfbp7MwlNiWftGHEhniI2g1gd_Ck_RH5XbvGrsm5hmfvprYGwQ8zqhsipMxqZHXjlBgsm5YxpKmVz58Zz3aSScGiJw2RxXGYYb-QVnnnyjzZhfFie2VG6yW-Ls)  
  <sub>U.S. News - Money, 20 hours ago</sub>  
  They have each beaten the index at times, but the reason to own them is diversification, not returns.
- [If This Sector Breaks, ‘So Does the Market’: Jay Woods Says This Chart is 'Most Important in the World'](https://www.google.com/goto?url=CAES2AEB6zswFV5BR9eLoGPaToVW4YPzmECa1AVySfFMx1PutyXQvAzJW-Vm4NbUQt5o1t0mqFLErAXlLjoQAbvMGsvH9bNLg7KAEPmwMg5WD0rgJ2OS4FTTtxuOwlmTNyIMrer0Tnvi1B2Apgm5EyyG8plEpA0TsYKH73Z9wFTHbpO0QQ019qTo-Gg1FiKQjAB4MEM6cC71VjBnLeEFr22wKRRhnQp5BKQri_uW28FeZNYCletZV80iMZ2BC9h1grm-MWp4rf11ZETPeuPnviWZx90m1YmhNIHbN8Q)  
  <sub>TradingView, 19 hours ago</sub>  
  In a big earnings week, one sector may stand out more than others, according to market expert Jay Woods.While the semiconductor sector doesn't have as many...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 551.18 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 579.84 (-4.9%), 50d 573.31 (-3.9%), 200d 517.06 (+6.6%); 50d above 200d
Momentum: RSI(14) 43.6 | MACD -13.543 vs signal -8.240 (histogram -5.303)
Returns: 1d +1.8% | 5d +0.9% | 1m -8.1% | 3m +9.3%
52-week range: 325.10 - 668.91 (now 65.8% of the way up)
Volatility: ATR(14) 17.08 (3.1% of price) | annualised 20d 36.2%
Volume: 0.24x the 20-day average
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
Three-year record: +55.3% a year | beta to the market 2.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +46.0% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - TSM: 2026-10-16 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-27 DA Davidson: up, Neutral -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 11.67M | fund size: 6.43B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bearish, analyst view bullish but limited, flows flat, fundamentals mixed – overall neutral.

**Main reasons it gave:**
- RSI 25.6, price below 20‑day/50‑day/200‑day SMAs, MACD negative
- US Treasury yields unchanged, no policy surprise
- Share count unchanged (0% change) over week and month
- Analyst coverage 43.2% of fund, weighted price target +35.8% above current price
- Fund P/E 11.69, 3‑year earnings -2.4% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 30.70 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 33.05 (-7.1%), 50d 36.61 (-16.1%), 200d 39.11 (-21.5%); 50d below 200d
Momentum: RSI(14) 25.6 | MACD -1.584 vs signal -1.460 (histogram -0.125)
Returns: 1d -0.4% | 5d -5.8% | 1m -13.4% | 3m -19.7%
52-week range: 30.70 - 43.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.66 (2.1% of price) | annualised 20d 25.4%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 11.69 | P/B 1.02 | P/S 0.63 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: -2.4% a year | beta to the market 0.61
Cost and size: expense ratio 0.59% | net assets 163.33M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.4%, Tupras-Turkiye Petrol Rafineleri AS 10.6%, Bim Birlesik Magazalar AS 10.4%, Akbank TAS 6.1%, Turk Hava Yollari AO 4.8%
Sector mix: Industrials 29.2%, Financial services 16.1%, Consumer defensive 13.9%, Basic materials 11.4%
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

<details><summary><b>What analysts and big funds say</b> — score +0.68</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.68</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 15.65M | fund size: 480.46M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals, but analyst consensus strongly bullish and fundamentals solid; overall view remains neutral.

**Main reasons it gave:**
- Analyst consensus: 100% buy, price target +17.9% above current price
- Fund flows flat: 0% change in share count over week and month
- Technicals: price above 20‑day SMA but below 50‑day and 200‑day SMA, RSI 53.8
- Macro: no rate or data surprise; yields down modestly, curve normal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 92.72 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 90.89 (+2.0%), 50d 93.50 (-0.8%), 200d 94.56 (-1.9%); 50d below 200d
Momentum: RSI(14) 53.8 | MACD -0.049 vs signal -0.526 (histogram 0.477)
Returns: 1d -0.5% | 5d +0.5% | 1m +2.4% | 3m -7.9%
52-week range: 87.00 - 100.95 (now 41.0% of the way up)
Volatility: ATR(14) 1.25 (1.3% of price) | annualised 20d 14.9%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Real Estate
What it holds: P/E 28.36 | P/B 2.42 | P/S 4.59 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +13.3% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 9.1%, Prologis Inc 6.9%, Equinix Inc 5.7%, American Tower Corp 4.3%
Sector mix: Real estate 99.5%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 40.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 370.18M | fund size: 34.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, mixed technicals, modest outflows offset by cheap fundamentals and a neutral analyst view.

**Main reasons it gave:**
- Share count down 3.6% in the past week (outflows)
- Analyst coverage of top holdings (9.2% weight) shows 61.1% buy, 38.9% hold, weighted price target -6.2% vs current price
- Fundamentals: P/B 0.21, P/S 0.12, 3-year annualized return +32% (cheap and strong growth)
- Macro: Treasury yields up slightly, VIX at 17.94, no major data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Biotech IPOs raise $7.5B as sector’s performance rally flattens](https://www.google.com/goto?url=CAESmgEB6zswFaXn5knMWXPLKdAHvyarqEmIj5PLa4gleiO72TE0VffmHJmtE4pkkE5vi7JNCzw9IuMb866L--5ohFzTpKa8dU2dg3g5QZ3tFK86e-dtxehS-gxLyVh4ujOT7YJ-WPugVZFB8e3KeR9NAUCWyHBLObE5DnCq-zE1swRK1ZObn7_m8uJSRF6uVOvkIwI3-zX1XEg_Gu5q)  
  <sub>BioSpace, 24 hours ago</sub>  
  While biopharma financing exit activity has remained strong through the third quarter, public-market performance for the same period was muted,...
- [Which Healthcare ETF Is the Better Buy: Fidelity’s FHLC or State Street’s XLV?](https://www.google.com/goto?url=CAESmgEB6zswFRc0zNEN27CkiMpC85CKl6JEcTmr71e8kYl0Zx55q_cMUoMPFR68y9RIzRJESl4N4VWKQpA6OjtLv_6DXJemZIePrz07zHeVQwrnngOujMCSizy_ZbVbgCloIBVtZIhkZtcwymzULbPNmgjBriGBOce_K49YF5VcAvCSJYmABb0p8EykntY2wOSiEJYMvlIgH29nf3e_)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  While Fidelity MSCI Health Care Index ETF (NYSEMKT:FHLC) provides broad-spectrum coverage of the U.S. healthcare market, State Street Health Care Select...
- [The Size of the Benefit Is Finally Public. For Small Cell Lung Cancer, It’s Big, and So Is the Bill.](https://www.google.com/goto?url=CAESpAEB6zswFRucSEOIbt9lOHvJqqNaiPxK21T2KTGT0dJdWoBZQxh1LANar1qYMdxI-RII6v5vlpn-kkPaIDEhB3iREhU1sb2A4Qj0zOGTGVG7E92yt0PkmBymWHDvgmjfYTr-OL3esi4yb_zflPsesN6iQ35DQ85mrSMI38frjkUv2Wc_x7yJMdktBDvF5YNeXlUYwLHg55VhA2QAvGHMbc94Z_kaeQ)  
  <sub>Moomoo, 22 hours ago</sub>  
  When AstraZeneca and Amgen first announced this lung cancer win, the size of the benefit had not been published. Now it has, and the details deserve a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 153.64 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 151.26 (+1.6%), 50d 157.01 (-2.1%), 200d 141.15 (+8.8%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD -1.345 vs signal -1.917 (histogram 0.572)
Returns: 1d +2.1% | 5d +0.3% | 1m -1.9% | 3m +3.9%
52-week range: 108.04 - 169.55 (now 74.1% of the way up)
Volatility: ATR(14) 4.26 (2.8% of price) | annualised 20d 33.0%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +32.0% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.2% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-27 William Blair: down, Outperform -> Market Perform
  - NTRA: 2026-10-19 Canaccord Genuity: main, Buy -> Buy
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-23 Oppenheimer: main, Outperform -> Outperform
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
Share count change: 1 week: -3.6% (-395.50M) over 7d | 1 month: -5.5% (-615.11M) over 31d
Shares outstanding: 69.23M | fund size: 10.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals mixed, analyst coverage thin despite bullish ratings, modest net inflow but limited conviction, fundamentals unchanged.

**Main reasons it gave:**
- No macro surprise: yields down slightly, Fed target unchanged, no policy shock
- Technical indicators mixed: price above 20‑day SMA but below 50‑day and 200‑day SMA, RSI neutral, low volume
- Analyst coverage thin (17% weight) despite 100% buy rating and +16% price target
- Fund flows show modest net inflow (+6% month) but recent weekly outflow, indicating limited conviction

<details><summary><b>News</b> — score +0.00</summary>

- [Triple Plays Striking Out? - TalkMarkets](https://t.co/6VjbdnM02S)  
  <sub>Howl.Link, 19 hours ago</sub>  
  Pexels. An earnings triple play is a stock that reports quarterly earnings results and 1) beats analyst EPS estimates, 2) beats analyst sales estimates,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 97.77 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 96.00 (+1.8%), 50d 98.97 (-1.2%), 200d 105.34 (-7.2%); 50d below 200d
Momentum: RSI(14) 52.1 | MACD -0.299 vs signal -0.936 (histogram 0.636)
Returns: 1d -0.2% | 5d +1.6% | 1m +0.5% | 3m -6.6%
52-week range: 92.84 - 121.36 (now 17.3% of the way up)
Volatility: ATR(14) 2.21 (2.3% of price) | annualised 20d 25.0%
Volume: 0.25x the 20-day average
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
Three-year record: +12.4% a year | beta to the market 1.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.4% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-10-19 JP Morgan: main, Overweight -> Overweight
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - JCI: 2026-10-15 Mizuho: main, Neutral -> Neutral
  - W: 2026-10-23 RBC Capital: main, Sector Perform -> Sector Perform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.25</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: -3.5% (-51.33M) over 7d | 1 month: +6.0% (80.68M) over 31d
Shares outstanding: 14.54M | fund size: 1.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst buy coverage and positive fund inflows versus negative sector news and a downtrend in technicals. No macro surprise or decisive technical break, so overall call remains neutral.

**Main reasons it gave:**
- Analyst coverage: 90.6% buy, weighted price target +29.7% above current
- Fund flows: share count up 7.1% over past month, indicating net inflows
- Technicals: price below 20d, 50d, 200d SMAs, RSI 29.3 (oversold) with low volume
- News: telecom stocks decline, XLC hits lowest point since June 2025

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  State Street Communication Services Select Sector SPDR ETF (XLC) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS,...
- [Telecom Stocks Decline as XLC Hits Lowest Point Since June 2025](https://www.google.com/goto?url=CAESoQEB6zswFfc0PfrkVtD0mfPTSQ1jYq4ca92L11cEF70K5pmvfAdNNO59EwLcfltEZ9TurOKDCqJAkF4qd5QT1ZaST78gDHnUQ2rmqimSy8mIsoVoCgRrfDRkrd8j18Ndjkxu_TVg_vRONE0lTGS9Q3uN3l1ydoNdB9y4ZFVwOT9j2Jk52iIEdIvBwwKo6Ge6roCR51lq12doNMj6UDHTqBvQfw)  
  <sub>GuruFocus, 18 hours ago</sub>  
  On October 26, 2026, telecommunication stocks faced a significant downturn, with the SPDR Communication Services Sector ETF (XLC) hitting its lowest point...
- [Energy’s Back, Baby!](https://www.google.com/goto?url=CAESbwHrOzAVAw8mL_qNVPm8doGFs7DOD7Udb0zzh1rqkA6aOz12Soki-tZ1l9sMvxV4LXGY2_kUCjICWoQYmS1Z8zflvqT9MP8rYI4MgLh-qecp2XiI2RbMv4Ma4HTkdxGG5iIuB3I0w464HB5ClyFeMA)  
  <sub>Money & Markets, 22 hours ago</sub>  
  AI may dominate the headlines, but energy stocks are surging in 2026. And my system suggests the rally could have plenty of fuel left...
- [ValuEngine Weekly Market Commentary](https://seekingalpha.com/article/4957756-valuengine-weekly-market-commentary)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  U.S. equity markets remained mixed this week, with weakness in growth-oriented sectors offset by continued strength in value, defensive, and energy-related...
- [Skydance Sinks 6% Despite Citi Buy Call and Elon Musk's Reported $1B Investment; Roku and Disney Dip](https://www.google.com/goto?url=CAESyAEB6zswFfvKXi_wsYSw6mSLmgTu8S2FcgBiUOwoxnwiMhF_o-yO-o3TyDWyIDahKEqqcUT1liLLkaRa9mWF_jKPLiBDOjvBC6arzMxjXHQukFlpAT-Slnm5blvNEaJboHPNlP8qvXPsjtfMAbSmWnmdF0vUQaZkVWY4XfNHj8MTFF-VsPeLIAqgZWr4dm2_zMM8SkRJJ-CzHRbPd2TLnKxgaUzIxyDyIsD5CP0HXmRYSqwLk9Qj5iXpg_LJgyvJ3Z9BwENgtdcq-g)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  A Citi Buy rating and a reported billion-dollar investment from Elon Musk arrived at the same time, yet Skydance shares kept falling.
- [Netflix Drops 4% as Engagement Worries Outweigh Earnings Beat; Disney and Spotify Slip](https://www.google.com/goto?url=CAESvAEB6zswFVd1AHtLZqz_dQv4eHv5D8987niuPPg2gE3CTCilBsQib9InB5YrjTnBJ-5P2yRM6vwzOEU8bu-KGHQ4jy4fxDWk7yPbpNxd8CF8xz40nx_jS1ERX5jrtI2xKL5NJWyXg-fvtxgV4XeAmcqwMcgEp1oQexYjTi6G9ZN7p6Sa0g4hFxKMHtR23ofSjrGsJ1UvWrAb2_v1so7cMD_3cFrPjSW0aBbF_hI2I0XQ38uD0SLjtwv-_O3bmw)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Netflix beat earnings but Wall Street is selling anyway, and the reason behind the selloff is rattling the entire streaming sector.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 103.74 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 109.76 (-5.5%), 50d 111.28 (-6.8%), 200d 113.14 (-8.3%); 50d below 200d
Momentum: RSI(14) 29.3 | MACD -1.714 vs signal -0.898 (histogram -0.815)
Returns: 1d -0.1% | 5d -5.9% | 1m -6.7% | 3m -5.3%
52-week range: 103.74 - 120.08 (now 0.0% of the way up)
Volatility: ATR(14) 1.69 (1.6% of price) | annualised 20d 16.6%
Volume: 0.30x the 20-day average
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
Three-year record: +17.8% a year | beta to the market 0.85
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.7% above the current prices
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
Share count change: 1 week: +4.5% (959.02M) over 7d | 1 month: +7.1% (1.47B) over 31d
Shares outstanding: 213.47M | fund size: 22.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US Treasury yields unchanged (3‑month 4.04%, 10‑year 4.99%) – no macro surprise
- Technicals show price above 20‑, 50‑, 200‑day SMAs, RSI 63.3, MACD positive, but volume only 0.32× 20‑day avg – bullish trend without decisive break
- EIA forecast WTI $100 now, $86 in 6 months – price outlook predicts falling oil prices
- Crude inventories draw -3.1 MMbbl (15th percentile) and gasoline draw -3.0 MMbbl (8th percentile) – modest bullish supply‑demand signal, offset by diesel and natural‑gas builds

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Energy SPDR (XLE) Buys $49.2 Million More Exxon on Friday](https://finance.yahoo.com/energy/articles/state-street-energy-spdr-xle-110511889.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Energy Select Sector SPDR ETF (XLE) recorded net buying of $204.5 million on Friday,...
- [Crude Oil Weekly Outlook: Brent Tests September Highs, WTI Tops $100, and XLE Reclaims 18-Year Resistance](https://www.stonex.com/en-gb/news-and-analysis/crude-oil-weekly-outlook-brent-tests-september-highs-wti-tops-100-and-xle-reclaims-18-year-resistance/)  
  <sub>StoneX, 10 hours ago</sub>  
  Brent crude is testing its September highs, WTI has moved back towards the psychological 100 level, and the energy sector ETF (XLE) has reclaimed its 18...
- [Should You Invest in the Vanguard Energy Index Fund ETF Shares (VDE)?](https://www.google.com/goto?url=CAESnQEB6zswFRBscuQYg31uatlxEgKARzg6QnP7lidfmTs21qFKAr7WWmavgv5itsG_p7QvPytYZ6ZICmgRkX-P4NYZnjKNqsDlxjk6TpsIPlHdvYIUkzJ4aMIUV4wY7DTuOdr_idzn5ajoBYR2GAGIVrSRJRWT3ENDmgLU3XDuxkGQnLjtHeXgGGUtRgKS9SePxESQjmu-57_0sPSnKDks)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  If you're interested in broad exposure to the Energy - Broad segment of the equity market, look no further than the Vanguard Energy Index Fund ETF Shares...
- [28 ETFs Add to ExxonMobil (XOM) Holdings on Friday](https://www.google.com/goto?url=CAES_QEB6zswFTrjt6G2IvsiOQw0NqBilkGRSN0i5i5aJvkhryxDxk6vxAuXVhcxQick6BydMJclJEuZYpsBPg-c1VnL2oGkXxfs3pf2sKMzhgrJb1Z0fPOsCRln_4M6L7Yt0rDaaGoaO232hGAZZwIvOUzqE3OqPPilMvh8br0lqUNAcmwH2DKBrO1uRBii0cegdI8Uv4i_9dqQu0uyJRKpqMiVRm_Pqy_D8usCTwxIMoJLBrlpcMupbM9GXOvr4MG1q42yRgKBkcgpmoTji1zbo_nOgVSvRYDsOoETgP_Knny0rx0caow_trfeeQXWNZQqDFPqojVXI_8Ox8JXRYnv)  
  <sub>GuruFocus, 4 hours ago</sub>  
  XLE led the move, as ETF activity produced a net $54.3 million of buying in ExxonMobil (XOM) in Friday's session. Twenty-eight ETFs added shares while 15...
- [AI’s Unlikely Ally: How Energy Powers the Digital Revolution](https://www.google.com/goto?url=CAESnQEB6zswFQ2SRyXASWDYlQWRmMLzgN8C8STUxAeO31t6B0p20o7Vs2q7gTPqXEqvxUgao-RbZEDRfVuQF-knqU7yB6vA2q-1pZSRWcVuVO3N8xNXLNi-B8u77eBJ86v8EgpijufvC1YbdeMs8O1nnIV01YP4ErUrZxqWRgX_nIyWsSt0gOpHU3RKnb5dK8yIhs3XEA-iHqnf6KllkCnK)  
  <sub>ETF Database, 22 hours ago</sub>  
  Many investors are fixated on tech and AI ETFs, and for good reason, given how potent AI hype and its subsequent buildout have turned out to be.
- [XLE 261026 70.00C (XLE261026C70000) Stock Options Chain | Quotes & News](https://www.google.com/goto?url=CAESxQIB6zswFZ_Dd_YGLSwyFncgVK6skuc-OqLr6BRKhe6WjOf_5rDLD0zXfoAzEv9DZRB7y8JDOiHsFhtDOLszK5PDzYSYdYwukM00KIxHBA6dOQdegLEEwhP_ocfwepPRtlAXZFw721z5lcCLd2AP_r4eq_dDhu_OgJULSeYVciXR7q9f9nl91Ka6G7srWyv43XWqAlp_KEWjjGdNSO3E7xx2UKG6pWbA8xHzamkfwJDdbc-t6LKxyS1FbwRtrtbiYZ8ve2Ukm7WPpw6YBMULIH9zGKswJTMsXRQhW7YQGf-5wCHVsFoni1Lx2SNTFMeHayFfW1UnyRzBlUszqcng-7mPlNbC2hhrFIUyGNCek4GDS-IFmF45T1-14jgxRj8Jofn3We9-ajO2HKtGSwTDJYJJcLhi-VqWi4ytCRO76H4pDLAZz1S9)  
  <sub>Moomoo, 17 hours ago</sub>  
  Track real-time XLE 261026 70.00C (XLE261026C70000) stock options chain data and pricing information and news on moomoo App for your options trading and...
- [iShares Global Energy ETF offers broad energy s...](https://pluang.com/en/news-feed/ixc-saya-suka-momentum-sektor-energi)  
  <sub>Pluang, 7 hours ago</sub>  
  The iShares Global Energy ETF (IXC) provides passive, diversified exposure to global energy stocks, benefiting from sustained high oil prices.
- [How Midstream/MLPs Diversify Equity & Income Portfolios](https://www.google.com/goto?url=CAESrQEB6zswFW5rwOr_QK6m4kolxnt7udImqaCUjSbpE4K3We5CFHdqVpshC_Il0gYa3WfhObsnQ08BIYh5kDP2Yj22nEgf9nnL7qirrBUDczyZaZf_hx09NfPE0LVhDwnia4p6RSp7a0L8POsT0rzfCIcxpgEdqp3_5TkejGZdN75T7CjSmuyfTj_mdor0cjAAjf2AULj7hPNAu6vKGL8jF35moy15vBz_TIneHM7Yqw)  
  <sub>ETF Trends, 4 hours ago</sub>  
  VettaFi discusses how midstream/MLPs can provide diversification benefits in a broad equity portfolio or income portfolio.
- [Energy’s Back, Baby!](https://moneyandmarkets.com/energys-back-baby-2/amp/)  
  <sub>Money & Markets, 22 hours ago</sub>  
  AI may dominate the headlines, but energy stocks are surging in 2026. And my system suggests the rally could have plenty of fuel left...
- [Ten energy stocks with strong revenue growth and attractive valuations (XLE:NYSEARCA)](https://www.google.com/goto?url=CAESpwEB6zswFakOhv0_epg-l70rrPKhK-jmpDgb23P1liCJI7ND3YKg5ZQKY9f18CYHfJUHeyuZVT2W-n9mEIvZEyqYhGD1LQLRTW37rHU8A3J5UvAK19ZncQzOtLyYaDB3rONKv8lRojH7UP7Lv34aemQgjFPcJp7rrGIhRCuERV4GZiz9E6avCHlAhhRbi5R0Ng9vcpWtHO0YsUP274mIP5JHAe6zX1A_Eg)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Energy stocks with strong revenue growth and attractive valuations could draw attention as investors weigh the outlook for oil and gas demand,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 68.62 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 66.13 (+3.8%), 50d 64.61 (+6.2%), 200d 58.41 (+17.5%); 50d above 200d
Momentum: RSI(14) 63.3 | MACD 1.516 vs signal 1.281 (histogram 0.235)
Returns: 1d -1.5% | 5d +1.0% | 1m +10.5% | 3m +17.0%
52-week range: 43.60 - 69.64 (now 96.1% of the way up)
Volatility: ATR(14) 1.40 (2.0% of price) | annualised 20d 21.0%
Volume: 0.32x the 20-day average
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
Three-year record: +19.7% a year | beta to the market -0.03
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
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 91.9% | hold 8.1% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +0.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 186.42M | fund size: 12.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technicals, and bullish analyst view limited to 42.7% coverage.

**Main reasons it gave:**
- Flat fund flows (0% change week/month) indicating no net demand
- Macro data unchanged: yields down slightly, normal upward sloping curve, no surprise
- Technical indicators mixed: RSI 54.1 (neutral), MACD positive but low volume (0.14x avg)
- Analyst view bullish (100% buy, +9.1% price target) but covers only 42.7% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Financial SPDR (XLF) Sells Berkshire and JPMorgan on Friday](https://finance.yahoo.com/markets/stocks/articles/state-street-financial-spdr-xlf-110454792.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Financial Select Sector SPDR ETF (XLF) was the only ETF selling in Friday's session, with no ETFs...
- [PayPal Slips 3% Ahead of Earnings Despite Truist Target Raise; Klarna and Affirm Retreat](https://247wallst.com/investing/2026/10/26/paypal-slips-3-ahead-of-earnings-despite-truist-target-raise-klarna-and-affirm-retreat/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Truist just raised its price target on PayPal stock while shares tumble ahead of earnings, and the disconnect between analyst optimism and trader caution...
- [Financial stocks with strong revenue growth and attractive valuations (XLF:NYSEARCA)](https://seekingalpha.com/news/4657869-financial-stocks-with-strong-revenue-growth-and-attractive-valuations)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Financial stocks with strong year-over-year revenue growth and attractive valuations may draw attention as investors assess interest-rate expectations,...
- [Sector Update: Financial Stocks Mixed Late Afternoon](https://ca.finance.yahoo.com/news/sector-financial-stocks-mixed-afternoon-195403842.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Financial stocks were mixed in late Monday afternoon trading, with the NYSE Financial Index fraction.
- [Visa Analyst Sees AI Agents Strengthening its Digital Payments Business](https://www.tradingview.com/news/benzinga:af2896a3a094b:0)  
  <sub>TradingView, 20 hours ago</sub>  
  Visa Inc. NYSE:V is scheduled to report fiscal fourth quarter 2026 earnings on Oct. 27, with analysts expecting EPS of $3.44 versus $2.98 a year earlier and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 55.83 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 54.87 (+1.8%), 50d 56.00 (-0.3%), 200d 53.69 (+4.0%); 50d above 200d
Momentum: RSI(14) 54.1 | MACD 0.150 vs signal -0.080 (histogram 0.230)
Returns: 1d -0.3% | 5d +0.2% | 1m +3.0% | 3m -1.5%
52-week range: 47.81 - 58.56 (now 74.7% of the way up)
Volatility: ATR(14) 0.69 (1.2% of price) | annualised 20d 12.4%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Financial
What it holds: P/E 15.21 | P/B 2.25 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +22.3% a year | beta to the market 0.75
Cost and size: expense ratio 0.08% | net assets 50.97B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.3%, JPMorgan Chase & Co 11.7%, Visa Inc Class A 8.1%, Mastercard Inc Class A 5.9%, Bank of America Corp 4.7%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.2%
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
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.1% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-10-22 UBS: main, Buy -> Buy
  - JPM: 2026-10-15 Citigroup: main, Neutral -> Neutral
  - V: 2026-10-26 Susquehanna: main, Positive -> Positive
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 883.44M | fund size: 49.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view bullish but limited coverage, flat fund flows, no macro surprise, technicals slightly bearish.

**Main reasons it gave:**
- Fund flows flat: 0.0% change in share count over 1 week and 1 month
- No macro surprise: Treasury yields down slightly, inflation 3.7% in line with expectations, Fed target unchanged
- Technical indicators show price below 20d, 50d, 200d SMAs and RSI 43.9, indicating slight bearish momentum
- Analyst coverage limited to 25.7% of fund weight, rating 100% buy with +26.6% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Tuesday as Investors Assess Corporate Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-131350822.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively trad.
- [Should You Invest in the iShares U.S. Industrials ETF (IYJ)?](https://www.google.com/goto?url=CAESnAEB6zswFcIdsaFLBCvmDR_Tky5lF8oyaFzmvoNLpLaImftvsED-TzRphJZsdLF9SyRcdYMDLIw6M-VzIcRXkNEDGZatelZ7pTxvDzmuZcR6YmJoGj6lIfDH0iVrNDbok7kpPedks-9Ef_GZyfckcWuMIFeUJr--03Peesd0YXw8v60mmtUsKYj9aLIzZVje9srz8_iz-SC1NzowLek)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Looking for broad exposure to the Industrials - Broad segment of the equity market? You should consider the iShares U.S. Industrials ETF (IYJ),...
- [ValuEngine Weekly Market Commentary](https://seekingalpha.com/article/4957756-valuengine-weekly-market-commentary)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  U.S. equity markets remained mixed this week, with weakness in growth-oriented sectors offset by continued strength in value, defensive, and energy-related...
- [Growth Leads Sectors In Monday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62593015/growth-leads-sectors-in-monday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Seven sectors are higher and four are lower in Monday's regular session, with growth sectors holding two of the top three positions alongside Industrials.
- [Undervalued industrial stocks with strong year-over-year revenue growth (XLI:NYSEARCA)](https://seekingalpha.com/news/4657438-undervalued-industrial-stocks-with-strong-year-over-year-revenue-growth)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Discover 11 industrial stocks with strong revenue growth and attractive valuations as investors assess infrastructure and shipping trends—see the list now.
- [State Street Technology SPDR (XLK) Sells NVIDIA and Apple on Oct. 23](https://finance.yahoo.com/markets/stocks/articles/state-street-technology-spdr-xlk-110519514.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) extended its run of one-sided ETF activity in Friday's...
- [Finally, Factories Are Hiring Again](https://seekingalpha.com/article/4957536-finally-factories-are-hiring-again)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Advanced manufacturing jobs are rebounding in the U.S., boosting utilities and industrials as power demand surges. Read the full analysis here.
- [Exchange-Traded Funds Higher as US Equities Advance After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171302344.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1%. US equity indexes rose as big...
- [What to Expect From Ferguson Enterprises’ Next Quarterly Earnings Report](https://www.barchart.com/story/news/8476881/what-to-expect-from-ferguson-enterprises-next-quarterly-earnings-report)  
  <sub>Barchart.com, 1 hour ago</sub>  
  Ferguson Enterprises is scheduled to report its Q3 results next month, with Wall Street expecting diluted EPS to increase at a double-digit rate year over...
- [Energy’s Back, Baby!](https://moneyandmarkets.com/energys-back-baby-2/)  
  <sub>Money & Markets, 20 hours ago</sub>  
  AI may dominate the headlines, but energy stocks are surging in 2026. And my system suggests the rally could have plenty of fuel left...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 166.94 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 168.01 (-0.6%), 50d 171.46 (-2.6%), 200d 173.23 (-3.6%); 50d below 200d
Momentum: RSI(14) 43.9 | MACD -1.383 vs signal -1.478 (histogram 0.095)
Returns: 1d -0.0% | 5d +0.1% | 1m -1.1% | 3m -5.5%
52-week range: 147.83 - 186.51 (now 49.4% of the way up)
Volatility: ATR(14) 2.52 (1.5% of price) | annualised 20d 14.6%
Volume: 0.22x the 20-day average
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
Three-year record: +20.4% a year | beta to the market 1.01
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.6% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2026-10-26 UBS: main, Neutral -> Neutral
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 136.63M | fund size: 22.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise; technicals mixed; flat fund flows; bond‑market risk warning for tech; analyst view bullish but limited coverage

**Main reasons it gave:**
- No macro surprise: yields down slightly, normal upward sloping curve
- Technical indicators mixed: price above 200‑day SMA but below 20‑day/50‑day SMAs, RSI 47.4, MACD negative
- Fund flows flat: share count unchanged over week and month
- Bond market risk warning for tech stocks could pressure XLK
- Analyst ratings bullish (100% buy) with +24.7% price target, but coverage only 49.5% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Technology SPDR (XLK) Sells NVIDIA and Apple on Oct. 23](https://www.google.com/goto?url=CAESnAEB6zswFVdNI9H_GgAL1JCsF1HtlEvnr75TQVCeeR6_beOUnb8uHUPRU1vlWv7dX_DGmYADxuwgeml8ocbpDvdDz57hiJeqOsb9KPS5Q7oETteRbKVdhikmI5_3Hh9bV-H3maFlX8pHhiLXDoiWo4KZ-6tP3YzIGt2LDWNSJbCKpOp1RYTZdpL4HiPC6_SuXYaoEUykIXOyDWKzdYY)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  This article first appeared on GuruFocus. State Street Technology Select Sector SPDR ETF (XLK) extended its run of one-sided ETF activity in Friday's...
- [Should You Invest in the Vanguard Information Technology Index Fund ETF Shares (VGT)?](https://finance.yahoo.com/markets/stocks/articles/invest-vanguard-information-technology-index-092002004.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  If you're interested in broad exposure to the Technology - Broad segment of the equity market, look no further than the Vanguard Information Technology...
- [Energy’s Back, Baby!](https://moneyandmarkets.com/energys-back-baby-2/amp/)  
  <sub>Money & Markets, 22 hours ago</sub>  
  AI may dominate the headlines, but energy stocks are surging in 2026. And my system suggests the rally could have plenty of fuel left...
- [Exchange-Traded Funds Higher as US Equities Advance After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171302344.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1%. US equity indexes rose as big...
- [Sector Update: Tech Stocks Gain Monday Afternoon](https://ca.finance.yahoo.com/news/sector-tech-stocks-gain-monday-175241264.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Tech stocks were higher Monday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) rising 1.7% and the State Street SPDR S&P...
- [Growth Leads Sectors In Monday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62593015/growth-leads-sectors-in-monday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Seven sectors are higher and four are lower in Monday's regular session, with growth sectors holding two of the top three positions alongside Industrials.
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Tuesday as Investors Assess Corporate Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-131350822.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively trad.
- [Sector Update: Tech](https://finance.yahoo.com/markets/stocks/articles/sector-tech-165030034.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Tech stocks were higher Monday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) rising 1.6% and the State Street SPDR S&P...
- [Bond Market Sends Warning to Tech Stocks as Credit Risk Hits Highest Level Since 2022](https://www.tipranks.com/news/bond-market-sends-warning-to-tech-stocks-as-credit-risk-hits-highest-level-since-2022)  
  <sub>TipRanks, 24 hours ago</sub>  
  Technology stocks could face more selling pressure as investors in the bond market become increasingly worried about the cost of AI development.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 188.38 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 192.51 (-2.1%), 50d 189.53 (-0.6%), 200d 168.93 (+11.5%); 50d above 200d
Momentum: RSI(14) 47.4 | MACD -1.775 vs signal -0.733 (histogram -1.042)
Returns: 1d +1.1% | 5d +1.6% | 1m -3.2% | 3m +13.1%
52-week range: 127.50 - 202.00 (now 81.7% of the way up)
Volatility: ATR(14) 3.76 (2.0% of price) | annualised 20d 24.7%
Volume: 0.22x the 20-day average
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
Three-year record: +31.5% a year | beta to the market 1.45
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.58 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.7% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-22 Needham: reit, Buy -> Buy
  - AAPL: 2026-10-20 MoffettNathanson: main, Neutral -> Neutral
  - MSFT: 2026-10-26 Oppenheimer: main, Outperform -> Outperform
  - AMD: 2026-10-21 Susquehanna: main, Positive -> Positive
  - AVGO: 2026-10-27 DA Davidson: up, Neutral -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 272.06M | fund size: 51.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show an uptrend but low volume and recent small declines, fund flows flat, analyst view bullish but limited coverage, fundamentals stable and defensive.

**Main reasons it gave:**
- US Treasury yields fell modestly across the curve with no surprise data releases
- XLP price above 20‑day, 50‑day and 200‑day SMAs, but volume is only 27% of 20‑day average
- Fund flows flat over the past week and month, indicating neutral investor demand
- Analyst coverage 100% buy with a +6.1% price target, covering 41.8% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Tuesday as Investors Assess Corporate Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-131350822.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively trad.
- [ETFs Are Net Sellers of Walmart (WMT) on Oct. 23](https://www.gurufocus.com/news/9144099/etfs-are-net-sellers-of-walmart-wmt-on-oct-23?utm_source=yahoo_finance&utm_medium=syndication&utm_campaign=headlines&r=caf6fe0e0db70d936033da5461e60141)  
  <sub>GuruFocus, 4 hours ago</sub>  
  XLP drove the largest move, cutting its Walmart (WMT) position by $58.2 million in ETF activity last Friday. The day's net flow was a sale of $32.7 million,...
- [Which Healthcare ETF Is the Better Buy: Fidelity’s FHLC or State Street’s XLV?](https://www.fool.com/coverage/etfs/2026/10/26/which-healthcare-etf-is-the-better-buy-fidelity-s-fhlc-or-state-street-s-xlv/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  XLV concentrates on 61 large-cap S&P 500 names, while FHLC casts a wider net with 365 holdings across mid and small caps. Both charge 0.08% annually.
- [Exchange-Traded Funds Higher as US Equities Advance After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171302344.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1%. US equity indexes rose as big...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-193359439.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.6% and the State Street...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 87.41 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 84.88 (+3.0%), 50d 84.47 (+3.5%), 200d 84.36 (+3.6%); 50d above 200d
Momentum: RSI(14) 59.3 | MACD 1.370 vs signal 1.005 (histogram 0.366)
Returns: 1d -0.6% | 5d -0.4% | 1m +6.2% | 3m +0.1%
52-week range: 75.60 - 90.01 (now 82.0% of the way up)
Volatility: ATR(14) 1.24 (1.4% of price) | annualised 20d 20.1%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 23.91 | P/B 4.44 | P/S 1.29 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +12.5% a year | beta to the market 0.48
Cost and size: expense ratio 0.08% | net assets 13.45B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 10.5%, Costco Wholesale Corp 9.2%, Procter & Gamble Co 7.7%, Coca-Cola Co 7.6%, Philip Morris International Inc 6.8%
Sector mix: Consumer defensive 98.5%, Consumer cyclical 1.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.1% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-10-20 Evercore ISI Group: main, Outperform -> Outperform
  - COST: 2026-10-21 CICC: init, ? -> Outperform
  - PG: 2026-10-26 Barclays: main, Equal-Weight -> Equal-Weight
  - KO: 2026-10-26 Piper Sandler: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 210.17M | fund size: 18.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, and solid but not catalyst‑driven fundamentals.

**Main reasons it gave:**
- Analyst view: 80.6% buy rating and +13.2% price target
- Fund flows flat: no net inflow or outflow in the past week/month
- Technicals: price below 200‑day SMA but above 20‑day/50‑day SMAs, RSI 60.9, MACD positive
- Macro: yields slightly down, no surprise data releases; VIX modestly elevated
- Fundamentals: solid 3.1% yield and strong 3‑year record, but no new catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [FUTY: Fidelity’s MSCI Utilities ETF Holds The Entire U.S. Utilities Sector (NYSEARCA:FUTY)](https://seekingalpha.com/article/4957513-futy-fidelitys-msci-utilities-etf-holds-entire-us-utilities-sector)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Explore Fidelity MSCI Utilities Index ETF performance, holdings, dividends, and long-term returns to see if this utilities fund fits your portfolio.
- [Form 4 iShares Russell 2000 ETF For: 26 October By Investing.com](https://ng.investing.com/news/stock-market-news/form-4-ishares-russell-2000-etf-for-26-october-93CH-2757990)  
  <sub>Investing.com Nigeria, 22 hours ago</sub>  
  This pricing supplement, which is not complete and may be changed, relates to an effective Registration Statement under the Securities Act of 1933.
- [ValuEngine Weekly Market Commentary](https://seekingalpha.com/article/4957756-valuengine-weekly-market-commentary)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  U.S. equity markets remained mixed this week, with weakness in growth-oriented sectors offset by continued strength in value, defensive, and energy-related...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 42.68 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 41.43 (+3.0%), 50d 41.80 (+2.1%), 200d 44.30 (-3.7%); 50d below 200d
Momentum: RSI(14) 60.9 | MACD 0.326 vs signal 0.111 (histogram 0.214)
Returns: 1d +0.3% | 5d +1.9% | 1m +8.7% | 3m -5.0%
52-week range: 39.25 - 47.73 (now 40.4% of the way up)
Volatility: ATR(14) 0.60 (1.4% of price) | annualised 20d 16.8%
Volume: 0.10x the 20-day average
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
Three-year record: +17.4% a year | beta to the market 0.40
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.00 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.2% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-23 Barclays: main, Equal-Weight -> Equal-Weight
  - SO: 2026-10-22 HSBC: init, ? -> Buy
  - DUK: 2026-10-22 HSBC: init, ? -> Hold
  - CEG: 2026-10-27 Barclays: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 163.27M | fund size: 6.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technicals, bullish analyst view limited to 54% coverage, fundamentals moderate.

**Main reasons it gave:**
- Yields down modestly across curve, Fed target unchanged
- Fund flows flat: share count unchanged week‑over‑week
- Price above 20‑day and 50‑day SMAs but below 200‑day SMA
- Analyst coverage 54% of fund, 100% buy rating, +19% price target

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Tuesday as Investors Assess Corporate Earnings](https://www.google.com/goto?url=CAESnwEB6zswFY6jpPzmgNGO6zRA2L-0fnOAccOtada8We0XWH2cKCEwUyQJX5HFeYqUGR753L0S6IzS_emGZO4e5tbRS7sfLqt_M2xeOP7myR4hjkKz-NeH1BmWFA3abQm5OW5tEI1WaKbwoREY2-THv29_WaPv6iuEK2NHadgblJcbM1Z3fhBFUch0rOK-Ay9T57i8mWZfoFVv7CQ7Hig1Pnc)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.4% and the actively trad.
- [Consumer discretionary stocks with strong revenue growth and attractive valuations (XLY:NYSEARCA)](https://seekingalpha.com/news/4657445-consumer-discretionary-stocks-with-strong-revenue-growth-and-attractive-valuations)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Consumer discretionary stocks with strong year-over-year revenue growth and attractive valuations may draw attention as investors assess consumer spending...
- [Sector Update: Consumer](https://www.google.com/goto?url=CAESiwEB6zswFQLUxkS4sGifehZOfCXK7d8J8BaDH6i07avgQ-80mGSs39-8CcPsGKMa0CO-dBLgn4tRIVLNndssMLa32AYnrtRZV40Z03KReLhiYh1SOS7HLDKlS2IVHl1uKkJ4XbVqVWZRpW-iakE8OJK0hozwGmtYZT8rL4XSy2yD-kUuPfcnb8SMU7V4)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.6% and the State Street...
- [Exchange-Traded Funds Higher as US Equities Advance After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-us-171302344.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1%. US equity indexes rose as big...
- [Sector Update: Consumer Stocks Mixed in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-175953994.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.7% and the State Street...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-195311236.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.6% and the State Street...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 114.74 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 112.52 (+2.0%), 50d 113.32 (+1.3%), 200d 115.67 (-0.8%); 50d below 200d
Momentum: RSI(14) 57.0 | MACD 0.628 vs signal 0.296 (histogram 0.332)
Returns: 1d +0.4% | 5d -0.7% | 1m +5.3% | 3m +2.8%
52-week range: 105.66 - 124.52 (now 48.1% of the way up)
Volatility: ATR(14) 1.57 (1.4% of price) | annualised 20d 14.3%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.00 | P/B 5.56 | P/S 2.32 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +15.1% a year | beta to the market 1.18
Cost and size: expense ratio 0.08% | net assets 21.27B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 23.4%, Tesla Inc 17.7%, The Home Depot Inc 5.0%, McDonald's Corp 4.2%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.7%, Technology 1.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 120.25M | fund size: 13.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 124.36 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 120.18 (+3.5%), 50d 122.25 (+1.7%), 200d 123.22 (+0.9%); 50d below 200d
Momentum: RSI(14) 59.9 | MACD -0.073 vs signal -0.638 (histogram 0.565)
Returns: 1d +1.8% | 5d +2.8% | 1m +2.5% | 3m +7.4%
52-week range: 99.40 - 137.69 (now 65.2% of the way up)
Volatility: ATR(14) 1.89 (1.5% of price) | annualised 20d 18.4%
Volume: 1.82x the 20-day average
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
Three-year record: +39.8% a year | beta to the market 1.09
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
Weighted price target: +20.5% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 2.55M | fund size: 317.12M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Why Brazil’s Stocks and Funds Like the iShares MSCI Brazil ETF Are Crashing Today](https://finance.yahoo.com/markets/stocks/articles/why-brazil-stocks-funds-ishares-164801956.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  The pro-capitalism Presidential candidate expected to win Sunday's election was defeated by the incumbent, potentially setting the stage for...
- [Brazil ETF Plunges Nearly 20% After Lula’s Surprise Win](https://www.etf.com/sections/features/brazil-etf-plunges-nearly-20-after-lulas-surprise-win)  
  <sub>ETF.com, 15 hours ago</sub>  
  EWZ suffered its second-worst day on record as investors who bet on a Bolsonaro victory were caught off guard.
- [Brazil Stocks Dive As President Lula Wins Re-Election](https://www.investors.com/news/brazil-stocks-dive-as-president-lula-wins-re-election/)  
  <sub>Investor's Business Daily, 18 hours ago</sub>  
  Brazil stocks are diving as President Luiz Inácio Lula da Silva narrowly won re-election Sunday vs. Flávio Bolsonaro.
- [EWZ Trading Volume Put at About $10 Billion](https://www.tokenpost.com/news/investing/41522)  
  <sub>TOKENPOST, 13 hours ago</sub>  
  The figure concerns the iShares MSCI Brazil ETF, which offers exposure to Brazilian equities. Hyperliquid's EWZ-linked perpetual contract is a separate...
- [Brazilian Equities: Thoughts On The Post-Election Bloodbath (NYSEARCA:EWZ)](https://seekingalpha.com/article/4957567-brazilian-equities-thoughts-on-the-post-election-bloodbath)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Brazil stocks sank after Lula's re-election, pressuring EWZ and EWZS amid debt, deficits, and high rates. Read the full analysis here.
- [Nasdaq 100 Rallies on Chip Rebound; Brazil ETF Sinks 21%: Stock Market Today](https://www.benzinga.com/markets/equities/26/10/62598326/nasdaq-100-chip-rebound-brazil-etf-ewz-stock-market-today)  
  <sub>Benzinga, 22 hours ago</sub>  
  The Nasdaq 100 gains 1.2% as chipmakers rebound and Tesla jumps on an upgrade, while Brazil's EWZ sinks 21.7% after Lula's win. Yields ease.
- [NU Stock Suffers Worst Day On Record In Brazil Market Rout – Monness Crespi Initiates Coverage With ‘Buy’ Rating](https://www.tradingview.com/news/stocktwits:aef0714b5094b:0-nu-stock-suffers-worst-day-on-record-in-brazil-market-rout-monness-crespi-initiates-coverage-with-buy-rating/)  
  <sub>TradingView, 22 hours ago</sub>  
  Nu Holdings (NU) shares plummeted on Monday amid a broad sell-off in Brazilian stocks after President Luiz Inácio Lula da Silva won a fourth term,...
- [Brazil’s Stock Market Crashes After Lula’s Upset Victory](https://decrypt.co/381828/brazil-stock-market-crashes-lula-upset-victory)  
  <sub>Decrypt, 23 hours ago</sub>  
  Brazil's stock market lost more than $200 billion in value at Monday's open, and the iShares MSCI Brazil ETF (EWZ) fell as much as 26% after Lula beat...
- [EWZS: Brazilian Small-Caps Crash 35% Monday, The Reaction Is Overdone](https://seekingalpha.com/article/4957851-ewzs-brazilian-small-caps-crash-35-percent-monday-the-reaction-is-overdone)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Brazil small-cap stocks plunged after the election, but valuations look compelling. Read here for an analysis of iShares MSCI Brazil Small-Cap ETF (EWZS).
- [Exchange-Traded Funds Higher as US Equities Advance After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171302344.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1%. US equity indexes rose as big...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 34.49 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 41.00 (-15.9%), 50d 38.47 (-10.3%), 200d 37.20 (-7.3%); 50d above 200d
Momentum: RSI(14) 31.5 | MACD -0.039 vs signal 0.924 (histogram -0.964)
Returns: 1d +1.0% | 5d -19.7% | 1m -4.7% | 3m -2.7%
52-week range: 30.77 - 43.54 (now 29.2% of the way up)
Volatility: ATR(14) 1.68 (4.9% of price) | annualised 20d 88.6%
Volume: 0.65x the 20-day average
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
Three-year record: +19.4% a year | beta to the market 0.83
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
Weighted price target: +34.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 200.55M | fund size: 6.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [These three materials stocks combine revenue growth with attractive valuations (XLB:NYSEARCA)](https://seekingalpha.com/news/4657426-these-three-materials-stocks-combine-revenue-growth-with-attractive-valuations)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Materials stocks with strong year-over-year revenue growth and attractive valuations may draw attention as investors assess commodity-price movements,...
- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest State Street Communication Services Select Sector SPDR ETF (XLC) stock quote, history, news and other vital information to help you with...
- [Growth Leads Sectors In Monday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/10/62593015/growth-leads-sectors-in-monday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Seven sectors are higher and four are lower in Monday's regular session, with growth sectors holding two of the top three positions alongside Industrials.
- [ValuEngine Weekly Market Commentary](https://seekingalpha.com/article/4957756-valuengine-weekly-market-commentary)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  U.S. equity markets remained mixed this week, with weakness in growth-oriented sectors offset by continued strength in value, defensive, and energy-related...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.47 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 50.13 (+2.7%), 50d 50.98 (+1.0%), 200d 51.02 (+0.9%); 50d below 200d
Momentum: RSI(14) 61.0 | MACD 0.292 vs signal 0.045 (histogram 0.247)
Returns: 1d +0.2% | 5d +0.5% | 1m +4.1% | 3m -0.5%
52-week range: 42.23 - 53.67 (now 80.8% of the way up)
Volatility: ATR(14) 0.68 (1.3% of price) | annualised 20d 11.6%
Volume: 0.48x the 20-day average
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
Three-year record: +13.4% a year | beta to the market 0.85
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: LIN, NEM, FCX, ECL, SHW
Recent rating changes among them:
  - LIN: 2026-10-15 RBC Capital: main, Outperform -> Outperform
  - NEM: 2026-10-22 Freedom Broker: down, Buy -> Hold
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 71.92M | fund size: 3.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Corn (CORN) · Commodity — BEARISH, confidence 0.40

**Result:** ACCEPTED · 229 shares · submitted sell 229 CORN @ ~17.50, stop 18.02

**In the model's own words:** no explanation. It wrote only “Bearish”, so the main reasons below are all it gave.

**Main reasons it gave:**
- USDA surprise corn yield increase (supply boost)
- Technical RSI 24.6 (oversold) and MACD negative
- Positioning net long down 4.4% week, indicating reduced bullish sentiment
- Cost of holding -7.4% annual, heavy roll cost

<details><summary><b>News</b> — score -0.20</summary>

- [Corn Closing in on Unchanged at Midday](https://www.barchart.com/story/news/8458461/corn-closing-in-on-unchanged-at-midday)  
  <sub>Barchart.com, 22 hours ago</sub>  
  Corn futures are off their overnight lows, with contracts holding onto fractional losses at midday on Monday. The CmdtyView national average Cash Corn price...
- [U.S. soybean futures slide alongside Brazilian real (SOYB:NYSEARCA)](https://seekingalpha.com/news/4657632-u-s-soybean-futures-slide-alongside-brazilian-real)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  CBOT soybeans fell to two-month lows following President Lula's surprise election win that sent the Brazil's currency sliding nearly 8%.
- [Nobody Had This on Their Bingo Card: USDA Yield Surprise, Brazil’s Election, and Fund Liquidation in Corn and Beans](https://www.barchart.com/story/news/8461573/nobody-had-this-on-their-bingo-card-usda-yield-surprise-brazils-election-and-fund-liquidation-in-corn-and-beans)  
  <sub>Barchart.com, 18 hours ago</sub>  
  USDA's surprise corn yield increase and Brazil's election results have pushed grains into liquidation mode. Blue Line Futures' Jason Gehler breaks down...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 17.53 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 18.39 (-4.7%), 50d 19.20 (-8.7%), 200d 18.18 (-3.6%); 50d above 200d
Momentum: RSI(14) 24.6 | MACD -0.453 vs signal -0.370 (histogram -0.083)
Returns: 1d -0.6% | 5d -1.9% | 1m -10.2% | 3m -1.7%
52-week range: 16.47 - 20.29 (now 27.7% of the way up)
Volatility: ATR(14) 0.26 (1.5% of price) | annualised 20d 16.3%
Volume: 0.40x the 20-day average
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

```text
Cost of holding this fund instead of corn itself: -7.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -1.7%, commodity +0.7%, gap -2.4% | 6 months: fund -6.6%, commodity -2.8%, gap -3.8% | 12 months: fund -0.5%, commodity +6.9%, gap -7.4%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 9.0% of open interest (1,835,658 contracts)
Change on the week: -4.4% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +2.9% (3.65M) over 7d | 1 month: -11.7% (-17.04M) over 31d
Shares outstanding: 7.37M | fund size: 129.12M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed signals from positioning, flows, and cost of holding lead to a neutral stance.

**Main reasons it gave:**
- Crowded long position (98th percentile) with net long 21.9% of OI and slight weekly reduction (-0.2%)
- Heavy cost of holding (-7.8% annual) indicating roll cost tailwind for short
- Fund outflows over past month (-14.5%) indicating demand decline
- Price below 20‑day (12.05) and 50‑day (11.62) SMAs, RSI 39.8, negative MACD, low volume (0.15× 20‑day avg) suggesting short‑term bearish momentum

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.45 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 12.05 (-5.0%), 50d 11.62 (-1.5%), 200d 10.19 (+12.4%); 50d above 200d
Momentum: RSI(14) 39.8 | MACD 0.095 vs signal 0.211 (histogram -0.116)
Returns: 1d -0.2% | 5d -6.6% | 1m +2.0% | 3m +19.9%
52-week range: 9.02 - 12.47 (now 70.4% of the way up)
Volatility: ATR(14) 0.23 (2.0% of price) | annualised 20d 31.0%
Volume: 0.15x the 20-day average
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
Cost of holding this fund instead of sugar itself: -7.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +19.9%, commodity +32.1%, gap -12.2% | 6 months: fund +19.8%, commodity +35.7%, gap -15.9% | 12 months: fund +20.1%, commodity +27.9%, gap -7.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 21.9% of open interest (1,210,639 contracts)
Change on the week: -0.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.8% (875.76K) over 7d | 1 month: -14.5% (-8.50M) over 31d
Shares outstanding: 4.38M | fund size: 50.16M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals mixed, cost of holding negative, positioning ambiguous, net outflows.

**Main reasons it gave:**
- Macro: yields down slightly, Fed target unchanged, no surprise data
- Technical: price above 20‑day, 50‑day and 200‑day SMAs but RSI 52.7, MACD negative, volume low
- Cost of holding: -3.6% annual drag on long exposure
- Positioning: net long fell 4.9% of OI, short crowding at 2% percentile, recent outflows, no clear directional bias

<details><summary><b>News</b> — score +0.00</summary>

- [Calamos Russell 2000 ETF (CPRY) Touches New 52-Week High](https://finance.yahoo.com/markets/options/articles/calamos-russell-2000-etf-cpry-122000699.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Calamos Russell 2000 Structured Alt Protection ETF - January CPRY is probably on the radar for investors seeking momentum. The fund just hit a 52-week high...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.97 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 39.69 (+0.7%), 50d 39.79 (+0.4%), 200d 37.86 (+5.6%); 50d above 200d
Momentum: RSI(14) 52.7 | MACD -0.126 vs signal -0.091 (histogram -0.035)
Returns: 1d +1.5% | 5d +0.5% | 1m +0.7% | 3m +4.2%
52-week range: 30.53 - 41.43 (now 86.6% of the way up)
Volatility: ATR(14) 0.59 (1.5% of price) | annualised 20d 18.3%
Volume: 0.27x the 20-day average
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
Cost of holding this fund instead of copper itself: -3.6% a year -- a steady drag
Measured: 3 months: fund +4.2%, commodity +5.7%, gap -1.4% | 6 months: fund +10.3%, commodity +12.1%, gap -1.8% | 12 months: fund +26.5%, commodity +30.1%, gap -3.6%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.35</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 14.6% of open interest (327,119 contracts)
Change on the week: -4.9% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: money going out (1 month)
Share count change: 1 week: +1.0% (7.02M) over 7d | 1 month: -1.6% (-12.12M) over 31d
Shares outstanding: 18.22M | fund size: 728.32M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break on volume, and positioning shows a modestly crowded short but no strong directional catalyst. Cost of holding is near zero, providing no clear bias.

**Main reasons it gave:**
- CFTC positioning: net long 3.1% of OI, weekly -2.1% change, crowded short (2% percentile)
- Technicals: price 49.08 below 20d SMA 52.51, 50d SMA 56.58, 200d SMA 64.73; RSI 33.4 (oversold)
- Macro: Treasury yields down modestly, inflation 3.7% (no surprise), no policy shock
- Cost of holding: -0.7% annual cost, gap near zero (fund performance close to commodity)

<details><summary><b>News</b> — score +0.00</summary>

- [Get Paid to Wait on a Silver Resurgence](https://etfdb.com/monthly-income-content-hub/get-paid-wait-silver-resurgence/)  
  <sub>ETF Database, 41 minutes ago</sub>  
  The YTD loss in silver sported by the largest ETF by physical holdings of silver is more than triple that of its gold counterpart.
- [Silver Is Down 17% in a Month. Here's My Prediction for What's Ahead for the Precious Metal.](https://finance.yahoo.com/markets/commodities/articles/silver-down-17-month-heres-181500009.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Over the past month, silver's spot price has declined 17% to about $54 per troy ounce. Let's see what caused that pullback -- and whether it will head...
- [SILJ: Underlying Conditions In Silver Don't Look Too Conducive For This Product To Flourish](https://seekingalpha.com/article/4957755-silj-underlying-conditions-in-silver-dont-look-too-conducive-for-this-product-to-flourish)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  The Amplify Junior Silver Miners ETF is a $3B ETF tracking junior silver miners, emphasizing early-stage and pre-production entities with low market-cap...
- [₹10,000 SIP in gold and silver ETFs 5 years ago: How much are they worth?](https://m.rediff.com/amp/getahead/report/personalfinance-10000-sip-in-gold-and-silver-etfs-5-years-ago-how-much-are-they-worth/20261027.htm)  
  <sub>Rediff, 12 hours ago</sub>  
  Both gold and silver investments have proved profitable in the last few years; however, there has been a marked difference in their behaviour.
- [Silver ETFs Slide Up to 2.75%; Gold, Bank, IT Also Weak](https://hdfcsky.com/news/gold-and-silver-etfs-slide-again-as-defence-funds-rebound-october-27-2026)  
  <sub>HDFC Sky, 5 hours ago</sub>  
  All 19 silver ETFs fell 1.62–2.75% and all 26 gold ETFs declined. Defence ETFs rebounded, PSU bank funds rose, while IT ETFs slipped.
- [Gold, Silver ETFs sink up to 53% from 52-week highs; Silver at 11-month low](https://www.business-standard.com/markets/news/gold-etfs-silver-etfs-under-pressure-sink-up-to-53-from-52-week-highs-silver-hits-11-month-low-126102700687_1.html)  
  <sub>Business Standard, 7 hours ago</sub>  
  Gold Exchange Traded Funds (ETFs) and Silver ETFs traded on a negative note, down up to 2 per cent on Tuesday tracking losses in international Gold and...
- [Diwali investment: Invesco launches silver ETF, FoF; ICICI Prudential opens BSE Power ETF NFO](https://www.businesstoday.in/mutual-funds/story/diwali-investment-invesco-launches-silver-etf-fof-icici-prudential-opens-bse-power-etf-nfo-563964-2026-10-27)  
  <sub>Business Today, 5 hours ago</sub>  
  The new fund offers (NFOs) for Invesco India Silver ETF and Invesco India Silver ETF Fund of Fund (FoF) will remain open from October 27 to November 9.
- [Dhanteras 2026: From Jewellery To ETFs, Ways To Invest In Gold And Silver](https://www.ndtvprofit.com/personal-finance/dhanteras-2026-from-jewellery-to-etfs-ways-to-invest-in-gold-and-silver-12240664)  
  <sub>NDTV Profit, 12 hours ago</sub>  
  From gold jewellery and coins to ETFs and digital gold, here are a few ways to invest in gold this Dhanteras, along with options to invest in silver.
- [Invesco MF introduces India Silver ETF Fund of Fund](https://www.investmentguruindia.com/newsdetail/invesco-mf-introduces-india-silver-etf-fund-of-fund190632)  
  <sub>Investment Guru India, 4 hours ago</sub>  
  Invesco Mutual Fund has launched Invesco India Silver ETF Fund of Fund, an open-ended Fund of Fund scheme investing in units of Invesco India Silver ETF.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 49.08 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 52.51 (-6.5%), 50d 56.58 (-13.3%), 200d 64.73 (-24.2%); 50d below 200d
Momentum: RSI(14) 33.4 | MACD -2.052 vs signal -1.756 (histogram -0.297)
Returns: 1d +0.9% | 5d -5.8% | 1m -10.7% | 3m -5.2%
52-week range: 42.40 - 105.60 (now 10.6% of the way up)
Volatility: ATR(14) 1.47 (3.0% of price) | annualised 20d 36.6%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.05</summary>

```text
Cost of holding this fund instead of silver itself: -0.7% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund -5.2%, commodity -6.2%, gap +1.0% | 6 months: fund -25.9%, commodity -25.8%, gap -0.0% | 12 months: fund +11.6%, commodity +12.2%, gap -0.7%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.45</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 3.1% of open interest (113,992 contracts)
Change on the week: -2.1% of open interest
Crowding: 2% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.45</summary>

```text
Direction: flat (1 month)
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 341.45M | fund size: 16.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed, positioning slightly bearish but not decisive, crop condition slightly bullish, cost of holding a modest drag.

**Main reasons it gave:**
- CFTC positioning net long 20.2% of OI, down 3.1% week-over-week
- Crop condition rating down 1 point over 3 weeks (worsening supply outlook)
- Cost of holding drag -1.3% per year (negative carry for long positions)
- Technicals: price below 20‑day SMA (27.09) and 50‑day SMA (27.25), RSI 35.9, MACD negative

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 26.47 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 27.09 (-2.3%), 50d 27.25 (-2.8%), 200d 25.04 (+5.7%); 50d above 200d
Momentum: RSI(14) 35.9 | MACD -0.217 vs signal -0.122 (histogram -0.095)
Returns: 1d +0.1% | 5d -0.8% | 1m -3.2% | 3m +5.0%
52-week range: 21.71 - 28.14 (now 74.1% of the way up)
Volatility: ATR(14) 0.28 (1.1% of price) | annualised 20d 10.1%
Volume: 0.06x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.3% a year -- a steady drag
Measured: 3 months: fund +5.0%, commodity +6.4%, gap -1.4% | 6 months: fund +7.3%, commodity +6.8%, gap +0.4% | 12 months: fund +19.0%, commodity +20.3%, gap -1.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-10-20, published the following Friday)
Large speculators: net long 20.2% of open interest (1,093,612 contracts)
Change on the week: -3.1% of open interest
Crowding: 70% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 month)
Share count change: 1 week: +0.6% (283.19K) over 7d | 1 month: +2.4% (1.04M) over 31d
Shares outstanding: 1.70M | fund size: 44.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse (Bright Data said: x-brd-status-code 502; x-brd-error redirect location was rejected)

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Cost of holding fund -18.1% annual (heavy roll cost)
- US natural gas inventories built +77 bcf, 87% percentile (high supply)
- EIA forecast $3.15 for Oct 2026 vs current $9.44 (price expected to fall)
- No macro surprise; yields unchanged, Fed target unchanged
- Technicals: price below 20d/50d/200d SMAs, RSI 33, low volume (no decisive break)

<details><summary><b>News</b> — score +0.00</summary>

- [UNG Oct 2026 10.500 call (UNG261028C00010500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/UNG261028C00010500/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest UNG Oct 2026 10.500 call (UNG261028C00010500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Brazil Implodes -21%. Cybersecurity Breaks Out. The Market Doesn't Care About Either.](https://www.barchart.com/story/news/8459285/brazil-implodes-21-cybersecurity-breaks-out-the-market-doesn-t-care-about-either)  
  <sub>Barchart.com, 21 hours ago</sub>  
  ETF Market Strategist & Derivatives Trader | CMT | Author, Physical Over Digital Alpha | Featured Author, Barchart | 500+ Institutional Subscribers.
- [Exchange-Traded Funds Higher as US Equities Advance After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-higher-us-171302344.html)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 1%. US equity indexes rose as big...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 9.44 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 10.49 (-10.0%), 50d 10.46 (-9.7%), 200d 11.22 (-15.8%); 50d below 200d
Momentum: RSI(14) 33.0 | MACD -0.241 vs signal -0.064 (histogram -0.178)
Returns: 1d -1.2% | 5d -10.0% | 1m -12.5% | 3m -4.9%
52-week range: 9.44 - 16.90 (now 0.0% of the way up)
Volatility: ATR(14) 0.36 (3.8% of price) | annualised 20d 38.1%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.80</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.80</summary>

```text
Cost of holding this fund instead of natural gas itself: -18.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -4.9%, commodity +10.2%, gap -15.1% | 6 months: fund -8.6%, commodity +17.4%, gap -25.9% | 12 months: fund -27.2%, commodity -9.1%, gap -18.1%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.80</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Natural gas: 3,644.0 billion cubic feet, +77.0 on the week (a build), 87% percentile over 52 weeks -- high for the time of year
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.80</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 12.08M | fund size: 114.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price 164.06, +33.9% above 200‑day SMA (strong uptrend)
- Crude inventories draw of 3.1 M bbl (15th percentile) indicating bullish supply balance
- EIA forecast WTI $86 in 6 months, bearish price outlook
- CFTC net long down 0.2% week‑over‑week, slight bearish shift in positioning

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 164.06 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 154.60 (+6.1%), 50d 147.94 (+10.9%), 200d 122.55 (+33.9%); 50d above 200d
Momentum: RSI(14) 62.6 | MACD 5.294 vs signal 4.329 (histogram 0.965)
Returns: 1d -1.3% | 5d +2.1% | 1m +9.4% | 3m +26.9%
52-week range: 66.17 - 169.53 (now 94.7% of the way up)
Volatility: ATR(14) 4.93 (3.0% of price) | annualised 20d 29.4%
Volume: 0.35x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

```text
US inventories, week ending 2026-10-16 (published the following Wednesday)
  Crude oil: 412.5 million barrels, -3.1 on the week (a draw), 15% percentile over 52 weeks
  Petrol: 205.3 million barrels, -3.0 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 104.3 million barrels, +1.7 on the week (a build), 25% percentile over 52 weeks
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 119.10M | fund size: 19.54B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data HTTP 502: <html>
<head><title>502 Bad Gateway</title></head>
<body>
<center><h1>502 Bad Gateway</h1></center>
</body>
</html>


### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, heavy carry cost, net outflows, and modest reduction in net short positions lead to a neutral stance.

**Main reasons it gave:**
- Macro: yields down modestly, inflation 3.7% (in line with expectations)
- Technical: price 22.5 below 20‑day SMA 24.07 and 50‑day SMA 25.38; RSI 22.9 oversold
- Cost of holding: -10.7% annual, heavy carry cost for longs
- Fund flows: share count down 11.6% over past month (net outflows)
- Positioning: large speculators net short 10.1% of OI, short positions fell 3.6% of OI this week

<details><summary><b>News</b> — score +0.00</summary>

- [U.S. soybean futures slide alongside Brazilian real (SOYB:NYSEARCA)](https://seekingalpha.com/news/4657632-u-s-soybean-futures-slide-alongside-brazilian-real)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  CBOT soybeans fell to two-month lows following President Lula's surprise election win that sent the Brazil's currency sliding nearly 8%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 22.50 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 24.07 (-6.5%), 50d 25.38 (-11.3%), 200d 23.51 (-4.3%); 50d above 200d
Momentum: RSI(14) 22.9 | MACD -0.751 vs signal -0.589 (histogram -0.162)
Returns: 1d -0.2% | 5d -4.4% | 1m -9.9% | 3m -8.1%
52-week range: 19.88 - 28.00 (now 32.3% of the way up)
Volatility: ATR(14) 0.42 (1.9% of price) | annualised 20d 17.0%
Volume: 0.16x the 20-day average
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
Cost of holding this fund instead of wheat itself: -10.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -8.1%, commodity -6.8%, gap -1.4% | 6 months: fund -9.0%, commodity -5.1%, gap -3.9% | 12 months: fund +9.5%, commodity +20.2%, gap -10.7%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

_Not available today._

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
Share count change: 1 week: +5.4% (14.46M) over 7d | 1 month: -11.6% (-36.76M) over 31d
Shares outstanding: 12.47M | fund size: 280.56M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Daily ETF Flows: GLD Loses Assets](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-gld-loses-assets)  
  <sub>ETF.com, 18 hours ago</sub>  
  Here are the daily ETF fund flows for October 25, 2026.
- [GLD 261023 368.00C (GLD261023C368000) Stock Options Chain | Quotes & News](https://www.moomoo.com/options/GLD261023C368000-US)  
  <sub>Moomoo, 10 hours ago</sub>  
  SPDR Gold ETF (GLD) News. Peter Schiff Says Republicans Touting 'No Tax' on Tips Must 'Accept Responsibility for Higher Inflation': 'That Was the Trade-Off'.
- [Gold futures turn higher as crude oil prices pull back (GLD:NYSEARCA)](https://seekingalpha.com/news/4657607-gold-futures-turn-higher-as-crude-oil-prices-pull-back)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Gold futures rose to start the week, supported by softer oil prices, following last week's steep losses that dragged down prices to three-month lows.
- [GLD Oct 2026 369.000 call (GLD261028C00369000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GLD261028C00369000/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest GLD Oct 2026 369.000 call (GLD261028C00369000) stock quote, history, news and other vital information to help you with your stock trading...
- [GLD NTA 23-10-2026 $3.75038](https://www.businessdesk.co.nz/nzx-announcements/gld-etf-units/482428/)  
  <sub>BusinessDesk, 12 hours ago</sub>  
  View the full NZX announcement for Smart Gold ETF (GLD): GLD NTA 23-10-2026 $3.75038. Financial updates and company disclosures on BusinessDesk.
- [Gold Price Crashed 25%, But Investors are Still Buying](https://beincrypto.com/gold-price-falls-etfs-rally-investors-keep-buying/)  
  <sub>BeInCrypto, 14 hours ago</sub>  
  Gold fell 25% since the Iran war began, yet gold ETF holdings hit a record. See who is buying, who is selling, and why.
- [Make money doing the work you believe in](https://substack.com/@quantifiedstrategies/note/c-371431954)  
  <sub>Substack, 6 hours ago</sub>  
  In this article, we examine a short-term strategy for the gold ETF GLD. Each trade lasts three trading days, and the backtest spends just 7.36% of its time...
- [GLD Oct 2026 422.000 put (GLD261026P00422000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GLD261026P00422000/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest GLD Oct 2026 422.000 put (GLD261026P00422000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Gold And Silver Hammered Again - But Buyers Aren't Giving Up](https://seekingalpha.com/article/4957560-gold-silver-hammered-again-buyers-arent-giving-up)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Gold and silver are attempting to regain their footing after another brutal week. Gold plunged roughly 4%, finishing just above $4000 an ounce in its...
- [GLD Oct 2026 290.000 put (GLD261026P00290000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GLD261026P00290000/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest GLD Oct 2026 290.000 put (GLD261026P00290000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.04% (-0.04 on the week) | 5-year 4.84% (-0.10 on the week) | 10-year 4.99% (-0.12 on the week) | 30-year 5.31% (-0.12 on the week)
Yield curve, 10-year minus 3-month: +0.95 points -- upward sloping (normal)
US dollar index: 102.17 (+0.44 on the week)
Volatility (VIX): 17.94 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 194k (2026-10-17)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.69% vs Fed target 3.75-4.00% -- the bond market prices about 3 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 371.29 (bar of 2026-10-27), from 501 daily bars
Trend: vs 20d SMA 378.01 (-1.8%), 50d 393.15 (-5.6%), 200d 413.77 (-10.3%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -5.585 vs signal -4.984 (histogram -0.601)
Returns: 1d +0.9% | 5d -1.7% | 1m -1.8% | 3m +0.1%
52-week range: 362.32 - 495.90 (now 6.7% of the way up)
Volatility: ATR(14) 5.55 (1.5% of price) | annualised 20d 17.0%
Volume: 0.23x the 20-day average
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
Cost of holding this fund instead of gold itself: 0.2% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +0.1%, commodity +0.7%, gap -0.6% | 6 months: fund -12.0%, commodity -11.8%, gap -0.2% | 12 months: fund -1.7%, commodity -1.8%, gap +0.2%
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
Share count change: 1 week: +0.0% (0.00) over 7d | 1 month: +0.0% (0.00) over 31d
Shares outstanding: 260.30M | fund size: 96.65B
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

