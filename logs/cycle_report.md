# Daily report

**14 Oct 2026, 18:59 Israel time (15:59 UTC)** · 80 names checked · 0 traded · 0 with a problem

**Answers with no explanation:** 15 of 63 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 6 | 10 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Teva Pharmaceutical (TEVA) · Company | **Sold part.** Sold 42 of 128 shares at +1.10R, 86 still held. Stop-loss raised 38.87 → 39.51. |
| Gold (GLD) · Commodity | **Stop raised.** At +0.86R, following the price. Stop-loss raised 389.68 → 387.99. |
| Alphabet (Google) (GOOGL) · Company | **Stop raised.** At +0.13R, following the price. Stop-loss raised 338.01 → 338.49. |
| Eli Lilly (LLY) · Company | **Stop raised.** At +0.93R, following the price. Stop-loss raised 1130.70 → 1136.43. |
| US dollar (UUP) · Index fund | **Stop raised.** At +3.86R, following the price. Stop-loss raised 28.86 → 28.96. |
| Exxon Mobil (XOM) · Company | **Stop raised.** At +1.81R, following the price. Stop-loss raised 167.17 → 168.38. |
| Argentina (ARGT) · Sector or country | **Holding.** -0.34R, holding 80 shares. Stop-loss 86.01. |
| Poland (EPOL) · Sector or country | **Holding.** +0.30R, holding 164 shares. Stop-loss 43.03. |
| United Kingdom (EWU) · Sector or country | **Holding.** +0.57R, holding 155 shares. Stop-loss 45.88. |
| Brazil (EWZ) · Sector or country | **Holding.** -0.44R, holding 165 shares. Stop-loss 41.48. |
| Gold mining companies (GDX) · Sector or country | **Holding.** -0.58R, holding 82 shares. Stop-loss 82.88. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** -0.44R, holding 158 shares. Stop-loss 76.66. |
| US government bonds, 7-10 years (IEF) · Index fund | **Holding.** +2.52R, holding 40 shares. Stop-loss 89.85. |
| Microsoft (MSFT) · Company | **Holding.** +2.27R, holding 7 shares. Stop-loss 525.70. |
| Nvidia (NVDA) · Company | **Holding.** -0.58R, holding 22 shares. Stop-loss 218.74. |
| Novo Nordisk (NVO) · Company | **Holding.** +0.59R, holding 123 shares. Stop-loss 39.01. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +2.33R, holding 4 shares. Stop-loss 104.79. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### ASML (ASML) · Company — BULLISH, confidence 0.78

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BULLISH”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Q3 earnings beat and raised sales guidance, indicating strong AI demand (Barron's, 33 min ago)
- Customers expressing interest in orders for 2029-2030, signaling long‑term demand (CNBC, 9h ago)
- Strong fundamentals: profit margin 30.1%, ROE 53.9%, low debt/equity 9.1% (Fundamentals data)
- Analyst consensus strong buy with mean price target +21.5% above current price (Analyst view)

<details><summary><b>News</b> — score +0.60</summary>

- [ASML Stock Is Falling After Earnings Point to Soaring AI Demand. Here's Why.](https://www.barrons.com/articles/asml-earnings-stock-price-d0973c5c)  
  <sub>Barron's, 33 minutes ago</sub>  
  ASML stock was falling even after it raised its sales guidance and said it can't keep up with customer demand for lithography tools.
- [ASML: What We Think of the Stock After Earnings](https://global.morningstar.com/en-eu/stocks/asml-what-we-think-stock-after-earnings)  
  <sub>Morningstar, 1 hour ago</sub>  
  We maintain our fair value estimate for ASML stock as strong demand shifts attention to orders for 2029 and 2030.
- [ASML Stock Rises as Demand Outruns Its 2027 and 2028 Supply](https://finance.yahoo.com/markets/stocks/articles/asml-stock-rises-demand-outruns-122810044.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Chip-Gear Giant ASML Posts Mixed Q3 Results, Guides Up](https://www.investors.com/news/technology/asml-stock-q3-2026-earnings/)  
  <sub>Investor's Business Daily, 4 hours ago</sub>  
  Semiconductor equipment maker ASML (ASML) on Wednesday beat analyst estimates for earnings in the third quarter, but its sales were a tad light. ASML stock...
- [Here’s How Much ASML Stock Is Expected to Move After Earnings](https://www.investopedia.com/here-is-how-much-asml-stock-is-expected-to-move-after-earnings-12166433)  
  <sub>Investopedia, 18 hours ago</sub>  
  ASML Holding is set to report earnings Wednesday, with traders expect a sizable move from the semiconductor equipment maker's stock.
- [ASML says it's getting order interest through 2030 as profit smashes expectations](https://www.cnbc.com/2026/10/14/asml-3q-earnings-ai-demand-orders-capacity.html)  
  <sub>CNBC, 9 hours ago</sub>  
  ASML said some customers are "expressing an interest" in placing orders with the company in 2029 and 2030, giving investors a view into longer-term demand.
- [ASML's strong orders ease fears AI spending boom is running out of steam](https://www.reuters.com/business/asml-forecasts-q4-sales-above-expectations-ai-chip-demand-2026-10-14/)  
  <sub>Reuters, 10 hours ago</sub>  
  ASML said on Wednesday customers were already looking to place orders for its advanced chipmaking ‌tools for 2029 and 2030, easing concerns that the...
- [Why is ASML stock rallying today?](https://www.investing.com/news/stock-market-news/why-is-asml-stock-rallying-today-93CH-4948202)  
  <sub>Investing.com, 7 hours ago</sub>  
  Investing.com -- ASML Holding NV stock is up 1.9% today, reaching €1,538.6, after the Dutch semiconductor equipment giant published its third-quarter 2026...
- [ASML Stock Forecast: AI Demand Outruns Capacity Through 2028](https://www.tradingkey.com/analysis/stocks/us-stocks/262216029-asml-stock-forecast-ai-demand-capacity-q3-2026-tradingkey)  
  <sub>TradingKey, 3 hours ago</sub>  
  TradingKey - ASML's €11.66 billion Q3 sales and €44–45 billion annual outlook spotlight AI demand through 2028. Watch Q4 guidance and $1686 support.
- [ASML Raises Sales Forecast For A Third Time, But Q3 Revenue Miss Sends Stock Lower: Earnings Selloff Spreads To MU, SNDK, INTC](https://finance.yahoo.com/markets/stocks/articles/asml-raises-sales-forecast-third-061145434.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  ASML raised its 2026 revenue forecast. The company's third-quarter revenue narrowly missed analyst expectations, while earnings per share topped estimates.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 1,726.36 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 1,765.83 (-2.2%), 50d 1,742.83 (-0.9%), 200d 1,571.79 (+9.8%); 50d above 200d
Momentum: RSI(14) 46.0 | MACD 9.763 vs signal 19.212 (histogram -9.449)
Returns: 1d +0.5% | 5d -4.4% | 1m +8.5% | 3m -3.3%
52-week range: 966.57 - 1,989.44 (now 74.3% of the way up)
Volatility: ATR(14) 52.16 (3.0% of price) | annualised 20d 29.0%
Volume: 0.74x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 663.10B
Valuation: trailing P/E 56.03 | forward P/E 29.37 | P/B 1,512.48 | PEG 1.58
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.30 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.80</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 beat by 23% | 2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

```text
Consensus: strong_buy (mean 1.43 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 6 strong buy, 31 buy, 4 hold, 1 sell, 0 strong sell
Price target: mean 2,097.15 (+21.5% vs last close), range 860.84 - 2,840.83
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

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

### HDFC Bank (HDB) · Company — BULLISH, confidence 0.65

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Strong Q2 profit beat (+34% YoY) and bullish analyst consensus (+35% target upside) outweigh bearish technicals and high valuation; moderate‑high confidence to buy.

**Main reasons it gave:**
- Q2 net profit rose 34% YoY to Rs 780 cr on higher loan demand and lower provisions (Reuters, 3 h ago)
- Analyst consensus is buy with mean price target $30.52, implying ~35% upside (Analyst view)
- Revenue and earnings grew YoY 16.6% and 18.1% respectively (Fundamentals)
- Technicals show price below 20‑day, 50‑day, 200‑day SMAs and low volume, indicating short‑term weakness (Technical data)

<details><summary><b>News</b> — score +0.70</summary>

- [India's HDB Financial Services posts quarterly profit rise on loan demand, lower provisions](https://www.reuters.com/world/india/indias-hdb-financial-services-posts-quarterly-profit-rise-loan-demand-lower-2026-10-14/)  
  <sub>Reuters, 3 hours ago</sub>  
  Indian non-bank lender HDB Financial Services posted a 34.2% rise in second-quarter profit on ​Wednesday, supported by improved loan demand and ‌lower...
- [At 16:00 IST on October 17, HDFC Bank (HDB) will discuss quarter and half-year results.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-8e64517680df.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  Senior management will discuss unaudited standalone and consolidated results through September 30, 2026; audio will follow on the bank's website.
- [HDFC Bank Limited $HDB Shares Newly Purchased by Euro Pacific Asset Management LLC](https://www.marketbeat.com/instant-alerts/filing-hdfc-bank-limited-hdb-shares-newly-purchased-by-euro-pacific-asset-management-llc-2026-10-13/)  
  <sub>MarketBeat, 15 hours ago</sub>  
  Euro Pacific Asset Management LLC bought a new stake in HDFC Bank Limited (NYSE:HDB - Free Report) during the third quarter, according to the company in its...
- [HDFC Bank Limited Common Stock (HDB) Company Profile](https://pluang.com/en/asset/usstock/HDB/11402/about)  
  <sub>Pluang, 15 hours ago</sub>  
  Full profile of HDFC Bank Limited Common Stock (HDB): company history, business lines, management, and key facts before you invest.
- [HSBC cuts target for HDFC Bank stock to USD 26.10](https://www.ad-hoc-news.de/boerse/news/corporate-news/hsbc-cuts-target-for-hdfc-bank-stock-to-usd-26-10/70324475)  
  <sub>ad-hoc-news.de, 3 hours ago</sub>  
  HDB, US40415F1012. HSBC cuts target for HDFC Bank stock to USD 26.10. Published on 10/14/2026 at 14:07 | Editorial responsibility: Rafael Müller,...
- [HDB Financial Declares Interim Dividend Of Rs 2 Per Share; Check Record Date](https://www.ndtvprofit.com/markets/hdb-financial-declares-interim-dividend-of-rs-2-per-share-check-record-date-12184199)  
  <sub>NDTV Profit, 4 hours ago</sub>  
  HDB Financial Services Ltd., declared an interim dividend of Rs 2 per equity share, after announcing its financial results for the second quarter of fiscal...
- [Stocks To Watch For October 15: RIL, IDBI Bank, CSB Bank, Tata Tech, HDB Financial and more](https://www.cnbctv18.com/photos/market/stocks/stocks-to-watch-october-15-idbi-bank-tata-tech-hdb-financial-hyundai-motor-india-more-20011892.htm)  
  <sub>CNBC TV18, 2 hours ago</sub>  
  From Tata Tech, HDB Financial and Bajaj Consumer Care reporting their Q2 earnings to CCEA approving the strategic sale and restructuring of IDBI Bank,...
- [HDB Financial Q2 PAT climbs 34% to Rs 780 crore; stock slips 4%](https://www.businesstoday.in/markets/stocks/story/hdb-financial-q2-pat-climbs-34-to-rs-780-crore-stock-slips-4-561614-2026-10-14)  
  <sub>Business Today, 3 hours ago</sub>  
  Net interest income (NII) rose 15.6 per cent YoY to Rs 2534 crore in Q2 FY27 from Rs 2192 crore in Q2 FY26, the company said.
- [HDB Financial Services Q2 Results: Net profit jumps 34% YoY to Rs 780 crore, revenue up 10%](https://m.economictimes.com/markets/stocks/earnings/hdb-financial-services-q2-results-net-profit-jumps-34-yoy-to-rs-780-crore-revenue-up-10/articleshow/134939587.cms)  
  <sub>The Economic Times, 4 hours ago</sub>  
  HDB Financial Services on Wednesday reported a net profit of Rs 780 crore for the July-September quarter of financial year 2027, marking more than 34%...
- [Stocks to watch: Hyundai, Tata Elxsi, BHEL, HDB Fin, Adani Enterprises](https://www.business-standard.com/markets/news/stocks-to-watch-hyundai-tata-elxsi-bhel-hdb-fin-adani-enterprises-126101400117_1.html)  
  <sub>Business Standard, 12 hours ago</sub>  
  Stocks to watch Today: HDB Financial Services, Groww, BHEL, Tata Technologies, and Bajaj Consumer are among the companies that will report their Q2FY27...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 22.57 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 22.65 (-0.4%), 50d 22.92 (-1.5%), 200d 26.52 (-14.9%); 50d below 200d
Momentum: RSI(14) 48.7 | MACD -0.157 vs signal -0.195 (histogram 0.039)
Returns: 1d -0.9% | 5d +1.9% | 1m -0.1% | 3m -14.2%
52-week range: 21.84 - 37.18 (now 4.7% of the way up)
Volatility: ATR(14) 0.50 (2.2% of price) | annualised 20d 26.6%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 115.97B
Valuation: trailing P/E 14.56 | forward P/E 16.22 | P/B 9.15 | PEG n/a
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
Price target: mean 30.52 (+35.3% vs last close), range 26.10 - 35.00
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

### Elbit Systems (ESLT) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Positive, ticker‑specific news (European LWS production center and Morocco deliveries) outweighs modest technical weakness; strong earnings record and slight analyst upside support a bullish view, while high valuation and lack of insider buying temper conviction.

**Main reasons it gave:**
- Swedish subsidiary to build European laser warning systems production center (positive catalyst)
- Subsidiary plans March 2027 deliveries to Morocco (new contract)
- Four consecutive earnings beats (strong earnings record)
- Price below 20‑, 50‑, 200‑day SMAs and RSI 48.5 (technical weakness)

<details><summary><b>News</b> — score +0.70</summary>

- [Elbit Systems Ltd. (ESLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ESLT/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Elbit Systems Ltd. (ESLT) · -3.39% · -8.29% · -27.84% · 15.31% · 32.91% · 360.94% · 16,591.75%. Key Events. Baseline. Advanced Chart. Loading...
- [12 Industrials Stocks Moving In Wednesday's Pre-Market Session](https://www.benzinga.com/trading-ideas/movers/26/10/62350111/12-industrials-stocks-moving-wednesday-s-pre-market-session)  
  <sub>Benzinga, 3 hours ago</sub>  
  Gainers Youlife Group (NASDAQ:YOUL) shares moved upwards by 12.9% to $0.35 during Wednesday's pre-market session. The company's market cap stands at $28.4...
- [Elbit Systems Ltd. (ESLT) stock price, news, quote and history](https://au.finance.yahoo.com/quote/ESLT/)  
  <sub>Yahoo Finance Australia, 14 hours ago</sub>  
  Elbit Systems Ltd. (ESLT) · -0.22% · -8.29% · -28.60% · 15.31% · 28.90% · 356.53% · 16,591.75%. Key events. Baseline. Advanced chart. Loading...
- [Elbit Systems building European LWS production center](https://en.globes.co.il/en/article-elbit-systems-1001559528)  
  <sub>Globes - Israel Business News, 2 hours ago</sub>  
  Shares in the Israeli defense company jumped after the announcement that its Swedish subsidiary would build the facility for laser warning systems.
- [Bending Spoons, Liquidia, Verastem And Other Big Stocks Moving Higher On Wednesday](https://www.benzinga.com/trading-ideas/movers/26/10/62355551/bending-spoons-liquidia-verastem-and-other-big-stocks-moving-higher-on-wednesday)  
  <sub>Benzinga, 40 minutes ago</sub>  
  U.S. stocks mostly fell, but Bending Spoons surged 40% after Berkshire's $330M investment. Liquidia and Verastem also posted strong gains.
- [Elbit Systems subsidiary plans March 2027 Morocco deliveries: stock pre-market at EUR 596.00](https://www.ad-hoc-news.de/boerse/news/vorboerse/elbit-systems-subsidiary-plans-march-2027-morocco-deliveries-stock/70320728)  
  <sub>ad-hoc-news.de, 9 hours ago</sub>  
  ESLT, IL0010811243. Elbit Systems subsidiary plans March 2027 Morocco deliveries: stock pre-market at EUR 596.00. Published on 10/14/2026 at 07:58...
- [ESLT261120C00710000 Interactive Stock Chart | ESLT Nov 2026 710.000 call Stock](https://finance.yahoo.com/chart/ESLT261120C00710000)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Airbus SE (EADSF) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EADSF/)  
  <sub>Yahoo! Finance Canada, 14 hours ago</sub>  
  Find the latest Airbus SE (EADSF) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [ESLT Oct 2026 890.000 call (ESLT261016C00890000) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/ESLT261016C00890000/chart/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Interactive Chart for ESLT Oct 2026 890.000 call (ESLT261016C00890000), analyze all the data with a huge range of indicators.
- [Airbus SE (EADSY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EADSY/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest Airbus SE (EADSY) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 699.44 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 704.87 (-0.8%), 50d 733.07 (-4.6%), 200d 778.47 (-10.2%); 50d below 200d
Momentum: RSI(14) 48.5 | MACD -17.564 vs signal -16.419 (histogram -1.145)
Returns: 1d +4.8% | 5d +4.5% | 1m -4.4% | 3m -5.3%
52-week range: 454.95 - 1,014.33 (now 43.7% of the way up)
Volatility: ATR(14) 19.03 (2.7% of price) | annualised 20d 33.4%
Volume: 0.81x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.78B
Valuation: trailing P/E 52.63 | forward P/E 38.09 | P/B 7.42 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 801.33 (+14.6% vs last close), range 518.00 - 960.00
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

### Toyota (TM) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The company has a strong earnings beat record (four consecutive beats with large surprises) and a bullish analyst consensus (2 strong‑buy, 2 buy) with a mean price target ~24% above the current price. Valuation appears cheap (trailing P/E 8.28) despite high leverage and negative free cash flow, leading to a neutral fundamentals view. Technicals show mixed signals (price above 20‑day SMA but below 50‑ and 200‑day SMAs, low volume) giving a slight bearish tilt. A recent forecast cut by Erste Group to USD 21.91 is a negative news item but is a price‑target rehash and carries low weight. Overall, bullish factors outweigh bearish ones, supporting a BUY signal with moderate conviction.

**Main reasons it gave:**
- Four consecutive earnings beats (44%, 12%, 27%, 24%)
- Analyst consensus: 2 strong buy, 2 buy; mean price target +24% above current price
- Trailing P/E 8.28 indicates cheap valuation relative to earnings
- Erste Group forecast cut to USD 21.91 (negative news) considered but outweighed by other factors

<details><summary><b>News</b> — score -0.10</summary>

- [TM270617P00135000 Interactive Stock Chart | TM Jun 2027 135.000 put Stock](https://finance.yahoo.com/chart/TM270617P00135000)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [A TV ad tool has driven 6x more site visits and 3x more revenue than traditional TV targeting, on average, MNTN says.](https://www.stocktitan.net/news/MNTN/mntn-brings-tealium-first-party-data-into-mntn-matched-tm-to-advance-rhg2fww91hhv.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Tealium audiences refresh in real time, letting campaigns adjust whom to target or exclude across TV, search, social and email. The integration is available...
- [Meet Agility Robotics: A pure-play humanoid robot stock headed for Wall Street (CCXI:NASDAQ)](https://seekingalpha.com/news/4652725-meet-agility-robotics-a-pure-play-humanoid-robot-stock-headed-for-wall-street)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Agility Robotics is closer to going public after Churchill Capital Corp XI (CCXI) set November 2 as the date for the SPAC transaction to be voted on.
- [(LMAX) Technical Data (LMAX:CA)](https://news.stocktradersdaily.com/canada/lmax-technical-data_20261014_0e169f)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Changes to the Price of Hamilton Healthcare YIELD MAXIMIZER TM ETF LMAX Influence Investor Perception.
- [Gorilla Technology and Hoya Capital Interviews to Air Nationally on the RedChip Small Stocks, Big Money(TM) Show on CNBC and Bloomberg TV](https://www.elpasotimes.com/press-release/story/213878/gorilla-technology-and-hoya-capital-interviews-to-air-nationally-on-the-redchip-small-stocks-big-moneytm-show-on-cnbc-and-bloomberg-tv/)  
  <sub>El Paso Times, 20 hours ago</sub>  
  ORLANDO, FL / ACCESS Newswire / October 9, 2026 / RedChip Companies will air interviews with Gorilla Technology Group Inc. (NASDAQ:GRRR) and Hoya Capital on...
- [Ten drill holes are complete. Eskay Mining expects lab results in coming months.](https://www.stocktitan.net/news/ESKYF/eskay-mining-corp-announces-successful-completion-of-its-2026-dryym19qpui5.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  The work also included 45 days of mapping, 159 surface rock samples and 346 georeferenced photos; certified assays are expected from ALS in coming months.
- [Erste Group cut forecast for Toyota Motor stock to USD 21.91](https://www.ad-hoc-news.de/boerse/news/corporate-news/erste-group-cut-forecast-for-toyota-motor-stock-to-usd-21-91/70322440)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  TM, US8923313071. Erste Group cut forecast for Toyota Motor stock to USD 21.91. Published on 10/14/2026 at 10:29 | Editorial responsibility: Rafael Müller,...
- [(HBIL) Technical Data (HBIL:CA)](https://news.stocktradersdaily.com/canada/hbil-technical-data_20261013_8cf6dc)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Changes to the Price of Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF HBIL Influence Investor Perception.
- [Sensex Today Ends 252 Points Lower | Nifty Below 22,650 | LIC Housing Finance Down 5%](https://www.equitymaster.com/indian-share-markets/10/14/2026/Sensex-Today-Ends-252-Points-Lower--Nifty-Below-22650--LIC-Housing-Finance-Down-5?utm_source=homepage&utm_medium=website&utm_campaign=Content&utm_content=TM)  
  <sub>Equitymaster, 4 hours ago</sub>  
  The BSE Sensex ends 252 points lower, while Nifty ended 99 points lower, down at 22622.
- [Canada’s finance minister approved VersaBank’s restructuring; the bank still needs U.S. approval.](https://www.stocktitan.net/news/VBNK/versa-bank-receives-canadian-finance-minister-approval-for-ge71vb4u0rxk.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Versa Bancorp, a new Delaware corporation, would become the bank's direct parent; completion is targeted by October's end, pending Federal Reserve approval.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 188.39 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 187.30 (+0.6%), 50d 190.51 (-1.1%), 200d 200.13 (-5.9%); 50d below 200d
Momentum: RSI(14) 50.8 | MACD -1.339 vs signal -1.656 (histogram 0.317)
Returns: 1d -0.2% | 5d +3.0% | 1m -3.6% | 3m +4.8%
52-week range: 166.50 - 248.29 (now 26.8% of the way up)
Volatility: ATR(14) 2.93 (1.6% of price) | annualised 20d 19.9%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 221.89B
Valuation: trailing P/E 8.28 | forward P/E 11.94 | P/B 15.17 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.38 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
```

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

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+24.3% vs last close), range 230.00 - 239.31
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

### MercadoLibre (MELI) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Analyst consensus is strongly bullish with a mean price target 23.6% above the current price, and the company shows robust revenue growth and high ROE. Technicals show slight bullish momentum (positive MACD, price above 200‑day SMA) despite thin volume. News is mixed but leans positive with a Citi target cut that still leaves the target above price and recent institutional buying. However, earnings history (1 beat, 3 misses) and high leverage temper confidence, resulting in moderate conviction.

**Main reasons it gave:**
- Citi cut price target to $2,100 but target remains above current price
- Analyst consensus strongly bullish with mean target $2,270 (+23.6%)
- Revenue growth +49.8% YoY and ROE 27.5% indicate strong fundamentals
- Earnings record shows 1 beat and 3 misses, suggesting earnings miss risk

<details><summary><b>News</b> — score +0.20</summary>

- [Alibaba vs. MercadoLibre: Which Stock Is a Better Buy in 2026?](https://finance.yahoo.com/markets/stocks/articles/alibaba-vs-mercadolibre-stock-better-113303491.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Alibaba trades at a fraction of MercadoLibre's valuation, but the Latin American growth story carries very different risk and reward dynamics.
- [MercadoLibre, Inc. $MELI Shares Newly Bought by Verus Wealth Management LLC](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-shares-newly-bought-by-verus-wealth-management-llc-2026-10-13/)  
  <sub>MarketBeat, 14 hours ago</sub>  
  Verus Wealth Management LLC bought a new stake in shares of MercadoLibre, Inc. (NASDAQ:MELI - Free Report) in the third quarter, according to its most...
- [MELI Dec 2027 2720.000 call (MELI271217C02720000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI271217C02720000/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest MELI Dec 2027 2720.000 call (MELI271217C02720000) stock quote, history, news and other vital information to help you with your stock trading...
- [MercadoLibre Stock Rose 9% in October on Brazil’s Election. Time to Sell or Load Up?](https://www.tikr.com/blog/mercadolibre-stock-rose-9-in-october-on-brazils-election-time-to-sell-or-load-up)  
  <sub>TIKR.com, 21 hours ago</sub>  
  MercadoLibre gained 9.5% in October as Brazil's first-round vote set off a rally in Brazilian assets. The move came from a higher multiple,...
- [Citi cuts target for MercadoLibre stock to USD 2,100](https://www.ad-hoc-news.de/boerse/news/corporate-news/citi-cuts-target-for-mercadolibre-stock-to-usd-2-100/70323698)  
  <sub>ad-hoc-news.de, 4 hours ago</sub>  
  MELI, US58733R1023. Citi cuts target for MercadoLibre stock to USD 2,100. Published on 10/14/2026 at 12:37 | Editorial responsibility: Rafael Müller,...
- [MercadoLibre, Inc. $MELI Position Raised by Euro Pacific Asset Management LLC](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-position-raised-by-euro-pacific-asset-management-llc-2026-10-13/)  
  <sub>MarketBeat, 15 hours ago</sub>  
  Euro Pacific Asset Management LLC boosted its stake in MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 248.3% during the 3rd quarter, according to the...
- [MercadoLibre vs. Shopify: Which Consumer Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/13/mercadolibre-vs-shopify-which-consumer-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 20 hours ago</sub>  
  The e-commerce landscape is shifting as regional giants and global software leaders battle for market share. Deciding between MercadoLibre (MELI -0.87%) and...
- [Apple Watch Series 12 Vs Ultra 4: 7 Huge Upgrades You Need To Know! Meli Stock (XoO4Pp8y8W)](https://media.unisba.ac.id/6aa7c117/d0d8a0f6IJRBmte2YQI)  
  <sub>Unisba Media, 20 hours ago</sub>  
  Is Apple about to drop its biggest smartwatch upgrade in years? With the September event getting closer, massive leaks surrounding the Apple Watch Series 12...
- [MELI Oct 2026 1560.000 call (MELI261016C01560000) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/MELI261016C01560000/)  
  <sub>Yahoo Finance Singapore, 12 hours ago</sub>  
  Find the latest MELI Oct 2026 1560.000 call (MELI261016C01560000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 1,835.99 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 1,802.78 (+1.8%), 50d 1,861.15 (-1.4%), 200d 1,833.30 (+0.1%); 50d above 200d
Momentum: RSI(14) 50.1 | MACD 3.151 vs signal -10.857 (histogram 14.008)
Returns: 1d -2.1% | 5d -2.0% | 1m +0.4% | 3m -1.2%
52-week range: 1,546.81 - 2,360.76 (now 35.5% of the way up)
Volatility: ATR(14) 54.16 (2.9% of price) | annualised 20d 42.0%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 93.08B
Valuation: trailing P/E 49.93 | forward P/E 32.41 | P/B 11.88 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.8% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

```text
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 16 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 2,270.01 (+23.6% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Citi Research flags strong US sales growth and China diaper demand (positive research note)
- Charmin wider sheets product claims up to 50% less usage (product launch)
- Technical: price above SMAs, RSI 68.2, but thin volume (0.23x 20‑day avg)
- Fundamentals: high ROE (30.3%) but low revenue growth (+1.5%) and high PEG (3.79)
- Analyst consensus: buy with mean rating 2.16 and price target +4.3% above last close

<details><summary><b>News</b> — score +0.50</summary>

- [Charmin says wider sheets can help people use up to 50% less toilet paper](https://www.stocktitan.net/news/PG/think-your-toilet-paper-is-good-enough-charmin-thinks-you-and-your-qpxucmsvmo8e.html)  
  <sub>Stock Titan, 43 minutes ago</sub>  
  Its up-to-50% claim is versus a leading U.S. 1-ply bargain brand; the wider-sheet product is available at major retailers nationwide and online.
- [Procter & Gamble Company (The) (NYSE:PG) Stock Has Average Price Target of $161.70](https://www.marketbeat.com/instant-alerts/consensus-procter-gamble-company-the-nyse-pg-stock-has-average-price-target-of-16170-2026-10-14/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Procter & Gamble Company (The) (NYSE:PG - Get Free Report) has been assigned a consensus rating of "Moderate Buy" from the twenty-four ratings firms that...
- [4 stocks to watch on Wednesday:PG, MS, NFLX, and ASML (SPX:)](https://seekingalpha.com/news/4652889-4-stocks-to-watch-on-wednesdaypg-ms-nflx-and-asml)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock futures dip after CPI as traders track NFLX churn, PG catalyst watch, MS earnings, and ASML AI-driven demand outlook—get the key takeaways.
- [The Procter & Gamble Company (PG.SW) Interactive Stock Chart](https://ca.finance.yahoo.com/quote/PG.SW/chart/)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Interactive Chart for The Procter & Gamble Company (PG.SW), analyze all the data with a huge range of indicators.
- [Citi Research Flags Procter & Gamble (PG) for Strong U.S. Sales Growth and China Diaper Demand](https://www.gurufocus.com/news/9123111/citi-research-flags-procter-gamble-pg-for-strong-us-sales-growth-and-china-diaper-demand)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 14, 2026, Citi Research placed Procter & Gamble Co (NYSE: PG) on a positive 90-day watch, anticipating accelerating organic sales growth driven...
- [PG Stock Analysis: Drops 0.10%, Testing: What to Know](https://journalarta.com/en/2026/10/14/pg-stock-analysis-drops-0-10-testing-key-resistance/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 13, 2026: price 153.04 USD, trend uptrend, RSI 65.5, support 143.95, resistance 153.20. technical analysis of pg stock. PG Stock Analysis — full…
- [Procter & Gamble (PG) Unveils New Crest Toothpaste And Pampers Wipes Design](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/procter-gamble-pg-unveils-new-crest-toothpaste-and-pampers-w)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  Procter & Gamble (NYSE:PG) brand Crest has released a new Sensitivity Relief toothpaste aimed at people with sensitive teeth. Pampers has redesigned its...
- [Discover which dow jones stocks are making waves on Tuesday.](https://www.chartmill.com/news/DIS/Chartmill-56153-Discover-which-dow-jones-stocks-are-making-waves-on-Tuesday)  
  <sub>ChartMill, 22 hours ago</sub>  
  Curious about the dow jones stocks that are in motion on Tuesday? Join us as we explore the top movers within the dow jones index during today's session.
- [Procter & Gamble Company (The) (NYSE:PG) Shares Will Pay Quarterly Dividend of $1.09](https://www.marketbeat.com/instant-alerts/dividend-procter-gamble-company-the-nyse-pg-shares-will-pay-quarterly-dividend-of-109-2026-10-14/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Procter & Gamble Company (The) (NYSE:PG) declared a quarterly dividend on Tuesday, October 13th. Shareholders of record on Friday, October 23rd will be paid...
- [PG&E Corp. stock outperforms competitors on strong trading day](https://www.marketwatch.com/data-news/pg-e-corp-stock-outperforms-competitors-on-strong-trading-day-3412925e-6d58cdcfbb18?mod=goog_fin_scmw)  
  <sub>MarketWatch, 18 hours ago</sub>  
  rallied 1.29% to $13.33 Tuesday, on what proved to be an all-around rough trading session for the stock market, with the S&P 500 Index.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 154.57 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 148.19 (+4.3%), 50d 146.38 (+5.6%), 200d 147.88 (+4.5%); 50d below 200d
Momentum: RSI(14) 68.2 | MACD 1.785 vs signal 0.957 (histogram 0.828)
Returns: 1d +1.0% | 5d +4.6% | 1m +5.4% | 3m +2.0%
52-week range: 138.04 - 167.20 (now 56.7% of the way up)
Volatility: ATR(14) 2.43 (1.6% of price) | annualised 20d 17.4%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 359.29B
Valuation: trailing P/E 23.35 | forward P/E 20.90 | P/B 6.74 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.1% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 2.16 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 5 strong buy, 8 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 161.22 (+4.3% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - 2026-10-06 RBC Capital: main, Outperform -> Outperform
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
  - 2026-07-30 HSBC: down, Buy -> Hold
  - 2026-07-30 Citigroup: main, Buy -> Buy
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 140,475 shares in 31 transaction(s) | sold 48,751 shares in 16
Net: +91,724 shares (+4.5% of insider holdings) | insiders hold 2,138,478 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-10-05 WHALEY SUSAN STREET (Officer): 2,369 shares, 344.31K
  - 2026-10-05 GAMA PAUL (Officer): 2,225 shares, 323.38K
  - 2026-10-05 SCHULTEN ANDRE (Chief Financial Officer): 3,914 shares, 568.86K
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
(29 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: technicals and recent news are bearish, while fundamentals, earnings record, and analyst consensus are bullish. Near‑term price action appears more likely to stay flat or dip, but no strong catalyst justifies a clear directional bet.

**Main reasons it gave:**
- Negative news: regulatory uncertainty and analyst forecast cuts (Benzinga, 1 hour ago)
- Technical downtrend: price below 20‑day, 50‑day, 200‑day SMAs; RSI 35.8; MACD negative; volume 0.29× 20‑day average
- Strong earnings record: 4 consecutive beats, latest beat 31% (Q2 2026)
- Fundamentals: high growth (revenue +24%, earnings +68%) and strong profitability (ROE 57%) despite high leverage
- Analyst consensus bullish: mean rating 2.07 (Buy) and price target +25.6% vs last close

<details><summary><b>News</b> — score -0.40</summary>

- [Caterpillar (CAT) Stock May Be 13% Undervalued On FTC Inquiry](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-stock-may-13-091453569.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Caterpillar has pulled back in recent weeks after a long run, which puts a fresh spotlight on whether the current share price lines up with the cash the...
- [What's Going On With Caterpillar Stock Wednesday?](https://www.benzinga.com/trading-ideas/movers/26/10/62353386/whats-going-on-with-caterpillar-stock-wednesday)  
  <sub>Benzinga, 1 hour ago</sub>  
  Caterpillar Inc. (NYSE:CAT) stock traded lower in Wednesday's premarket session amid recent analyst forecast cuts, a premium valuation, and regulatory...
- [Caterpillar (CAT): A Cyclical Machine Maker Meets a Growth-Stock Valuation](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-cyclical-machine-maker-221938259.html)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  For most of its history, Caterpillar (NYSE:CAT) has traded like a cyclical machine maker, with profits that rise and fall with construction and mining.
- [Caterpillar Sinks 5% as Deere Edges Higher: Is the Data Center Power Premium Unwinding?](https://247wallst.com/investing/2026/10/13/caterpillar-sinks-5-as-deere-edges-higher-is-the-data-center-power-premium-unwinding/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Caterpillar built a hefty valuation on its data center power business, but a single afternoon of trading is stripping that premium away while rivals like...
- [Caterpillar Inc Stock (CAT) Moved Down by 4.19% on Oct 13: A Full Analysis](https://www.tradingkey.com/news/market-movers/262214369-market-movers-cat-20261013)  
  <sub>TradingKey, 23 hours ago</sub>  
  Caterpillar shares fell due to high Treasury yields, regulatory uncertainty, and analyst downgrades.The MACD indicates a sell signal, while the Williams %R...
- [Caterpillar (CAT) Bets $1 Billion On North Carolina As Its Valuation Story Builds](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/caterpillar-cat-bets-1-billion-on-north-carolina-as-its-valu)  
  <sub>Simply Wall Street, 24 hours ago</sub>  
  Caterpillar's North Carolina bet and what it means for investors Caterpillar (CAT) just committed about US$1b to expand compact equipment manufacturing in...
- [CAT Forecast — Price Target — Prediction for 2027](https://www.tradingview.com/symbols/MUN-CAT/forecast-price-target/)  
  <sub>TradingView, 21 hours ago</sub>  
  See Caterpillar Inc. DR price prediction for 2027 made by analysts and compare to the performance for the past 2 years to develop a better trading strategy.
- [What Could Derail Caterpillar Stock?](https://finance.yahoo.com/markets/stocks/articles/could-derail-caterpillar-stock-220519275.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Investors holding Caterpillar (CAT) stock are paying 33.9 times earnings, compared with 21.9 for the S&P 500. Sustaining that premium requires durable...
- [Is an Industrials Rotation Lifting Caterpillar (NYSE:CAT)?](https://kalkinemedia.com/us/stocks/industrial/is-an-industrials-rotation-lifting-caterpillar-nysecat)  
  <sub>Kalkine Media, 9 hours ago</sub>  
  The week opened with a familiar pattern in which money moved out of the highest-flying parts of the market and into sectors tied more directly to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 760.68 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 812.75 (-6.4%), 50d 818.22 (-7.0%), 200d 804.25 (-5.4%); 50d above 200d
Momentum: RSI(14) 35.8 | MACD -8.623 vs signal -2.659 (histogram -5.964)
Returns: 1d -1.6% | 5d -6.5% | 1m -2.9% | 3m -13.3%
52-week range: 513.91 - 1,064.90 (now 44.8% of the way up)
Volatility: ATR(14) 26.03 (3.4% of price) | annualised 20d 32.7%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 349.67B
Valuation: trailing P/E 32.75 | forward P/E 23.34 | P/B 18.03 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.58 | short interest 1.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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
Consensus: buy (mean 2.07 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 14 buy, 11 hold, 1 sell, 1 strong sell
Price target: mean 955.30 (+25.6% vs last close), range 575.00 - 1,155.00
Recent rating changes:
  - 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - 2024-10-14 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2024-10-09 Citigroup: main, Buy -> Buy
  - 2024-10-09 Truist Securities: main, Buy -> Buy
  - 2024-09-30 B of A Securities: main, Buy -> Buy
  - 2024-08-19 Evercore ISI Group: main, In-Line -> In-Line
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

### JPMorgan Chase (JPM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Contradictory inputs: earnings miss and mixed news pull down short‑term sentiment, while fundamentals, earnings record and analyst consensus stay bullish. Technicals also show slight weakness. Net result is no clear directional edge, so a neutral view with modest conviction.

**Main reasons it gave:**
- Q3 revenue and profit miss despite 8% YoY sales growth
- Raised full‑year net interest income outlook and Baird price target to $312
- Fundamentals: trailing P/E 13.97, ROE 18%, revenue growth +10.2% YoY
- Technical: price below 20‑day SMA, RSI 40.2, volume 0.34× 20‑day average
- Analyst consensus remains buy with mean price target $372.73 (+12% from last close)

<details><summary><b>News</b> — score -0.20</summary>

- [JPM Q3 Deep Dive: Consumer Banking and Investment Strength Offset Margin Pressures](https://finance.yahoo.com/markets/stocks/articles/jpm-q3-deep-dive-consumer-122007849.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Global financial services giant JPMorgan Chase (NYSE:JPM) missed Wall Street's revenue expectations in Q3 2026, but sales rose 8% year on year to $50.91...
- [JPMorgan Chase & Co. (NYSE:JPM) Stock Price Target Raised at Robert W. Baird](https://www.marketbeat.com/instant-alerts/analyst-jpmorgan-chase-co-nyse-jpm-stock-price-target-raised-at-robert-w-baird-2026-10-14/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Robert W. Baird boosted their price objective on JPMorgan Chase & Co. from $305.00 to $312.00 and gave the company a "neutral" rating in a report on...
- [JPMorgan Chase Raises Full-Year Net Interest Income Outlook Despite Missing Q3 Revenue Expectations](https://www.tikr.com/blog/jpmorgan-chase-stock-raises-net-interest-income-outlook-q3-2026)  
  <sub>TIKR.com, 6 hours ago</sub>  
  JPMorgan Chase missed Q3 profit estimates but raised its net interest income outlook. Here's what it means for JPMorgan Chase stock.
- [JPMorgan Chase Q3 2026: A Top-Tier Bank Whose Shares Already Reflect It (NYSE:JPM)](https://seekingalpha.com/article/4953988-jpmorgan-chase-q3-earnings-top-tier-bank-stock-reflect-it)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  JPMorgan Q3 2026: strong quarter but revenue/EPS miss and rich valuation.
- [JPMorgan Analysts Boost Their Forecasts After Q3 Results](http://www.benzinga.com/analyst-stock-ratings/price-target/26/10/62353255/jpmorgan-analysts-boost-their-forecasts-after-q3-results)  
  <sub>Benzinga, 1 hour ago</sub>  
  JPMorgan misses Q3 earnings and revenue estimates; shares dip 1.3% as analysts lift price targets and company forecasts 2027 NII growth.
- [JPMorgan posts rare profit miss as dealmaking, bond trading lose momentum](https://www.reuters.com/business/finance/jpmorgans-profit-rises-investment-banking-trading-strength-2026-10-13/)  
  <sub>Reuters, 22 hours ago</sub>  
  Oct 13 (Reuters) - JPMorgan Chase (JPM.N) , opens new tab fell short of quarterly profit estimates for the first time in nearly three years as market...
- [Why Did Banking Stocks GS, JPM, BAC Surge To 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-banking-stocks-gs-jpm-bac-surge-to-52-week-highs-today/cZZ2phOR7q6)  
  <sub>Stocktwits, 10 hours ago</sub>  
  GS stock led the climb among banking stocks, surging more than 9% after its record Q2 results triggered a buy-in. JPM stock rose 2.5% after its results surged...
- [JPMorgan Chase & Co (JPM) Stock Down 0.9% but Still Overvalued -- GF Score: 84/100](https://www.gurufocus.com/news/9122101/jpmorgan-chase-co-jpm-stock-down-09-but-still-overvalued-gf-score-84100)  
  <sub>GuruFocus, 14 hours ago</sub>  
  On October 13, 2026, JPMorgan Chase & Co (JPM) shares fell 0.9%, bringing the current price to $331.43. The stock has experienced a 52-week range of $279.10...
- [JPMorgan Chase & Co. $JPM Stock: Stone Summit Wealth LLC Reduces Holdings](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-stone-summit-wealth-llc-reduces-holdings-2026-10-14/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Stone Summit Wealth LLC reduced its stake in JPMorgan Chase & Co. (NYSE:JPM) by 12.0% in the 3rd quarter, according to the company in its most recent...
- [JPM Oct 2026 410.000 put (JPM261030P00410000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/JPM261030P00410000/)  
  <sub>Yahoo! Finance Canada, 3 hours ago</sub>  
  Find the latest JPM Oct 2026 410.000 put (JPM261030P00410000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 333.02 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 336.73 (-1.1%), 50d 348.88 (-4.5%), 200d 322.21 (+3.4%); 50d above 200d
Momentum: RSI(14) 40.2 | MACD -4.833 vs signal -5.114 (histogram 0.281)
Returns: 1d +0.5% | 5d +1.0% | 1m -5.5% | 3m -3.0%
52-week range: 282.84 - 365.18 (now 60.9% of the way up)
Volatility: ATR(14) 6.32 (1.9% of price) | annualised 20d 16.9%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 884.37B
Valuation: trailing P/E 13.97 | forward P/E 13.12 | P/B 2.52 | PEG 1.57
Profitability: profit margin 34.6% | operating margin 42.6% | ROE 18.0%
Growth (YoY): revenue +10.2% | earnings +9.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 0.9% of float
Next earnings: 2027-01-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 3 beats, 1 missed
  2026-09-30 missed by 3% | 2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3%
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
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 4 strong buy, 9 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 372.73 (+11.9% vs last close), range 312.00 - 425.00
Recent rating changes:
  - 2026-10-14 Barclays: main, Overweight -> Overweight
  - 2026-10-14 RBC Capital: reit, Outperform -> Outperform
  - 2026-10-14 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - 2026-10-14 Baird: main, Neutral -> Neutral
  - 2026-10-05 UBS: main, Buy -> Buy
  - 2026-09-28 HSBC: main, Hold -> Hold
Institutional ownership: 75.6%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: technicals are bearish while fundamentals, analyst view and insider buying are bullish; news lacks a material catalyst. The conflict leads to a neutral stance with low conviction.

**Main reasons it gave:**
- Technical indicators show price below 20‑day and 50‑day SMAs, low RSI (37) and very low volume (0.08× avg) – bearish
- Fundamentals display solid profitability (33.9% margin, 16.2% ROE) and reasonable valuation (P/E ~16) – bullish
- Insider purchases of 800 k shares in the last 180 days signal confidence – bullish
- News provides no material catalyst; bond issuance and modest price rise are generic – neutral

<details><summary><b>News</b> — score +0.00</summary>

- [Royal Bank of Canada (RY.TO) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RY.TO/)  
  <sub>Yahoo Finance UK, 17 hours ago</sub>  
  Royal Bank of Canada (RY.TO) · -0.12% · -2.79% · 16.00% · 18.49% · 37.80% · 115.47% · 4,045.79%. Key events. Baseline. Advanced chart.
- [RY Stock Price and Chart — TSX:RY](https://www.tradingview.com/symbols/TSX-RY/)  
  <sub>TradingView, 20 hours ago</sub>  
  The current price of RY is 277.25 CAD — it has increased by 1.27% in the past 24 hours. Watch Royal Bank of Canada stock price performance more closely on the...
- [Montrusco Bolton Investments Inc. Sells 33,648 Shares of Royal Bank Of Canada $RY](https://www.marketbeat.com/instant-alerts/filing-montrusco-bolton-investments-inc-sells-33648-shares-of-royal-bank-of-canada-ry-2026-10-13/)  
  <sub>MarketBeat, 15 hours ago</sub>  
  Montrusco Bolton Investments Inc. decreased its holdings in Royal Bank Of Canada (NYSE:RY - Free Report) (TSE:RY) by 13.3% in the 3rd quarter, according to...
- [Indigenous Bond Could Be A Game Changer For RBC Stock](https://simplywall.st/stocks/ca/banks/tsx-ry/royal-bank-of-canada-shares/news/indigenous-bond-could-be-a-game-changer-for-rbc-stock/amp)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  Royal Bank of Canada has issued a C$500 million four-year callable fixed-to-floating rate Indigenous Bond under its Sustainable Bond Framework to fund...
- [(RY) Movement as an Input in Quant Signal Sets](https://news.stocktradersdaily.com/news_release/12/RY_Movement_as_an_Input_in_Quant_Signal_Sets_101426012802_1791955682.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Key findings for Royal Bank Of Canada (NYSE: RY). Divergent Sentiment Across All Horizons Suggests Choppy Conditions; No clear price positioning signal...
- [Royal Bank of Canada stock rises Tuesday, outperforms market](https://www.marketwatch.com/data-news/royal-bank-of-canada-stock-rises-tuesday-outperforms-market-ab945305-52e0bb277470?mod=mw_quote_news)  
  <sub>MarketWatch, 18 hours ago</sub>  
  Trading volume of 4.8 M shares eclipsed its 50-day average volume of 2.9 M. Editor's Note: This story was auto-generated by Automated Insights,...
- [RBC issues CAD 500 million bond and Royal Bank of Canada stock reaches USD 270.5 billion value](https://www.ad-hoc-news.de/boerse/news/corporate-news/rbc-issues-cad-500-million-bond-and-royal-bank-of-canada-stock-reaches-usd/70323588)  
  <sub>ad-hoc-news.de, 4 hours ago</sub>  
  Indigenous loans support communities across Canada from October 13, 2026. Royal Bank of Canada stock costs EUR 174.62 on October 14, 2026.
- [Royal Bank of Canada Issues CA$500 Million Indigenous Bond](https://www.marketscreener.com/news/royal-bank-of-canada-issues-ca-500-million-indigenous-bond-ce785dd2dd8df320)  
  <sub>marketscreener.com, 5 hours ago</sub>  
  Royal Bank of Canada has issued a CA$500 million Indigenous bond, the bank said Tuesday. Proceeds from the issuance of four-year callable fixed-to-floating...
- [Big Banks Are Split on a Rate Hike: What That Means for Your 2027 Mortgage Renewal](https://www.theglobeandmail.com/investing/markets/stocks/RY/pressreleases/7443089/big-banks-are-split-on-a-rate-hike-what-that-means-for-your-2027-mortgage-renewal/)  
  <sub>The Globe and Mail, 19 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.
- [The Toronto-Dominion Bank (TD.TO) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/TD.TO/)  
  <sub>Yahoo Finance UK, 5 hours ago</sub>  
  Find the latest The Toronto-Dominion Bank (TD.TO) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 192.63 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 197.55 (-2.5%), 50d 204.05 (-5.6%), 200d 187.36 (+2.8%); 50d above 200d
Momentum: RSI(14) 37.0 | MACD -3.442 vs signal -3.268 (histogram -0.175)
Returns: 1d -1.0% | 5d +0.7% | 1m -5.7% | 3m -10.8%
52-week range: 145.31 - 217.87 (now 65.2% of the way up)
Volatility: ATR(14) 3.00 (1.6% of price) | annualised 20d 17.5%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 266.68B
Valuation: trailing P/E 16.84 | forward P/E 15.39 | P/B 2.84 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.91 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.30</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 207.01 (+7.5% vs last close), range 182.25 - 224.26
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.60</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.60</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [META, TTD, SNAP, GOOGL, BMBL, WDAY Stocks Get New UBS Targets Amid AI And Ad Shifts](https://finance.yahoo.com/media-advertising/articles/meta-ttd-snap-googl-bmbl-131144379.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  UBS raised its price targets on Meta, Snap, Alphabet and Bumble while cutting its targets on Trade Desk and Workday.
- [Alphabet Stock Climbs: What's Going On?](https://www.benzinga.com/trading-ideas/movers/26/10/62356146/alphabet-stock-climbs-whats-going-on)  
  <sub>Benzinga, 29 minutes ago</sub>  
  Alphabet shares are rising Wednesday. Google announced a program that opens its advanced AI models to scientists across Europe.
- [Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis](https://www.investors.com/news/technology/alphabet-googl-stock-quotes-company-news-google-stock-chart-analysis/)  
  <sub>Investor's Business Daily, 22 hours ago</sub>  
  Alphabet (GOOGL) Stock Quotes, Company News And Chart Analysis · IBD STAFF · Updated 12:58 PM ET 10/13/2026. (GOOGL). Chart Error...
- [Google’s Gemma AI Models Surpass 1 Billion Downloads As Developers Build over 100,000 Variants — GOOGL Stock Slips](https://stocktwits.com/news-articles/markets/equity/google-gemma-ai-models-surpass-1-billion-downloads-as-developers-build-over-100000-variants-googl-stock-slips/cZYIyAtRJZ8)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Alphabet Inc.'s (GOOGL) Google's Gemma family of open AI models has surpassed one billion downloads, with developers publishing more than 100000 model...
- [$GOOG, $GOOGL Investors: A Securities Fraud Class Action is](https://www.globenewswire.com/news-release/2026/10/14/3380572/0/en/goog-googl-investors-a-securities-fraud-class-action-is-pending-on-behalf-of-alphabet-investors-that-lost-money-after-4-stock-drop-contact-bfa-law-by-december-1-deadline.html)  
  <sub>GlobeNewswire, 4 hours ago</sub>  
  A Securities Fraud Class Action is Pending on behalf of Alphabet Investors that Lost Money after 4% Stock Drop – Contact BFA Law by December 1 Deadline...
- [Google](https://www.moomoo.com/community/feed/google-117438899486726?chain_id=Name1K9-3FXPhg.1lcurm0&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FGOOGL-US%2Fcommunity%22%7D)  
  <sub>Moomoo, 4 hours ago</sub>  
  Trading Analysis ​Alphabet-A (GOOGL) is currently trading at $356.83, moving above an average cost basis of $350.74 to generate an unrealized gain of...
- [Google DeepMind, Google Cloud to give European researchers access to AI models (GOOG:NASDAQ)](https://seekingalpha.com/news/4652811-google-deepmind-google-cloud-to-give-european-researchers-access-to-ai-models)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Google DeepMind & Google Cloud boost EU research with $3M compute credits and AI tools like AlphaFold 3 and WeatherNext for 200 scientists—learn more now.
- [Citizens reiterates Alphabet stock rating on YouTube engagement data](https://www.investing.com/news/analyst-ratings/citizens-reiterates-alphabet-stock-rating-on-youtube-engagement-data-93CH-4948474)  
  <sub>Investing.com, 5 hours ago</sub>  
  Investing.com - Citizens maintained its Market Outperform rating and $515.00 price target on Alphabet Inc. (NASDAQ:GOOGL) following an analysis of YouTube...
- [SpaceX Stock Could Soar by 73%, According to a Wall Street Analyst](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL-Q/pressreleases/7600716/spacex-stock-could-soar-by-73-according-to-a-wall-street-analyst/)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [Premarket Movers: DELL Slides After Barclays Downgrade, NOW And GOOGL Rise On Analyst Updates](https://finance.yahoo.com/markets/stocks/articles/premarket-movers-dell-slides-barclays-103025351.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  ServiceNow gets a boost from improving AI and federal-business checks, while UBS nudges its Alphabet target higher but sees no near-term catalyst.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 354.54 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 347.11 (+2.1%), 50d 345.33 (+2.7%), 200d 340.62 (+4.1%); 50d above 200d
Momentum: RSI(14) 58.9 | MACD 2.374 vs signal 1.182 (histogram 1.191)
Returns: 1d +0.2% | 5d +1.2% | 1m +2.8% | 3m +0.0%
52-week range: 245.45 - 402.62 (now 69.4% of the way up)
Volatility: ATR(14) 8.01 (2.3% of price) | annualised 20d 20.3%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.34T
Valuation: trailing P/E 17.79 | forward P/E 23.14 | P/B 6.97 | PEG 1.25
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
Price target: mean 430.42 (+21.4% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - 2026-10-08 Needham: reit, Buy -> Buy
  - 2026-10-06 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - 2026-09-17 Evercore ISI Group: main, Outperform -> Outperform
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

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [What Is Eli Lilly Stock's Biggest Opportunity?](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-stocks-biggest-opportunity-192423962.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Investors are currently valuing Eli Lilly (LLY) stock at a premium, with shares priced at 39.5 times earnings compared with 21.9 for the S&P 500.
- [LLY Stock Rides Trump Spotlight: President Touts Eli Lilly’s $3.5B Factory As Weight-Loss Pill Plans Go Global](https://stocktwits.com/news-articles/markets/equity/lly-trump-touts-factory-weight-loss-pill-plans-go-global/cZKUwnZR7OX)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Shares of Eli Lilly and Company (LLY) drew attention late Tuesday after U.S. President Donald Trump put the drugmaker's $3.5 billion Pennsylvania factory in the...
- [Eli Lilly and Company Earnings Preview: What to Expect](https://www.barchart.com/story/news/7576167/eli-lilly-and-company-earnings-preview-what-to-expect)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Eli Lilly and Company (LLY), based in Indianapolis, Indiana, with a market capitalization of approximately $1.1 trillion, is a global pharmaceutical company...
- [Eli Lilly, Arm among market cap stock movers on Wednesday](https://www.investing.com/news/stock-market-news/eli-lilly-arm-among-market-cap-stock-movers-on-wednesday-93CH-4949639)  
  <sub>Investing.com, 4 minutes ago</sub>  
  Wednesday's market has seen swings in various stocks based on news and other factors. Today, stocks like Eli Lilly (LLY) are rallying, while stocks like Arm...
- [29 ETFs Add to Lilly (Eli) & Co (LLY) on Oct. 12](https://www.gurufocus.com/news/9122725/29-etfs-add-to-lilly-eli-co-lly-on-oct-12)  
  <sub>GuruFocus, 2 hours ago</sub>  
  ETF activity on Monday saw a net $88.8 million flow into Eli Lilly (LLY), as 29 ETFs bought shares and 13 sold. The buying extended a five-day streak of net...
- [Eli Lilly (LLY) Gains 3.2% Intraday, Adding $35 Billion in Market Value](https://247wallst.com/cards/eli-lilly-lly-price-swing-01m4xcmrzpf3fq9r7qjmysnjc4)  
  <sub>24/7 Wall St., 21 minutes ago</sub>  
  A 3.2% intraday move to $1213.48 adds roughly $35 billion of market value to a trillion-dollar drugmaker in a single session. Moves that size are rare for a...
- [Eli Lilly (LLY) Psoriasis Data Tests Whether Its Valuation Story Still Has Room](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-psoriasis-data-tests-whether-its-valuation-sto)  
  <sub>Simply Wall Street, 9 hours ago</sub>  
  Eli Lilly (LLY) just put fresh clinical data on the table, showing that combining Taltz and Zepbound shifted more psoriasis and metabolic biomarkers than...
- [LLY|Eli Lilly and Co|Price:1166.510|Chg%:-16.110](https://www.tradingkey.com/markets/stocks/lly)  
  <sub>TradingKey, 10 hours ago</sub>  
  As of October 2024, Lilly has achieved the status of the most valuable drug company in the world, boasting a market capitalization of $842 billion, marking the...
- [NTAP,SCSC,TPC,NRGV,NEXT,CCEL,ATEX,LLY,OKLO,AROC | Stock Prices | Quote Comparison - Yahoo Finance](https://ca.finance.yahoo.com/quotes/NTAP,SCSC,TPC,NRGV,NEXT,CCEL,ATEX,LLY,OKLO,AROC/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  View and compare NTAP,SCSC,TPC,NRGV,NEXT,CCEL,ATEX,LLY,OKLO,AROC on Yahoo Finance.
- [A Look at Eli Lilly and Co (LLY) After 1.4% Decline -- GF Value $1575.10 vs Price $1166.51](https://www.gurufocus.com/news/9122098/a-look-at-eli-lilly-and-co-lly-after-14-decline-gf-value-157510-vs-price-116651)  
  <sub>GuruFocus, 14 hours ago</sub>  
  On October 13, 2026, Eli Lilly and Co (LLY) shares fell 1.4%, closing at $1166.51. The stock has fluctuated within a 52-week range of $783.85 to $1292.65,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,204.99 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 1,168.41 (+3.1%), 50d 1,177.33 (+2.3%), 200d 1,078.14 (+11.8%); 50d above 200d
Momentum: RSI(14) 59.7 | MACD 4.513 vs signal 0.385 (histogram 4.128)
Returns: 1d +3.3% | 5d +1.4% | 1m +6.1% | 3m +3.1%
52-week range: 799.57 - 1,280.34 (now 84.3% of the way up)
Volatility: ATR(14) 34.30 (2.8% of price) | annualised 20d 23.7%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.07T
Valuation: trailing P/E 40.45 | forward P/E 25.38 | P/B 31.71 | PEG 1.14
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
Consensus: buy (mean 1.63 on a 1=strong buy to 5=strong sell scale, 30 analysts)
Ratings: 6 strong buy, 20 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,328.05 (+10.2% vs last close), range 930.00 - 1,600.00
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

- [Microsoft (MSFT) Stock Seems Fairly Priced Despite Its 84% Five Year Run](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-msft-stock-seems-fairly-priced-despite-its-84-five)  
  <sub>Simply Wall Street, 48 minutes ago</sub>  
  Microsoft has ridden the AI buildout and cloud story to a share price of US$543.45, which puts the focus squarely on a simple question for investors: Are...
- [Microsoft Stock Reaches a Record High. How It Suddenly Became an AI Winner.](https://www.barrons.com/articles/microsoft-stock-price-record-high-d6d67bab)  
  <sub>Barron's, 18 hours ago</sub>  
  Wall Street firms believe Microsoft is well positioned to boost revenue through its Azure cloud platform and its Copilot artificial-intelligence tool.
- [Microsoft: Bears Are Making Noise About AI Spending, You Should Ignore It - Buy (NASDAQ:MSFT)](https://seekingalpha.com/article/4954057-microsoft-bears-are-making-noise-about-ai-spending-you-should-ignore-it-buy)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Microsoft (MSFT) continues to defy skeptics regarding its infrastructure investments, consistently proving critics wrong.
- [MSFT Stock Hits Highest Level This Year: Microsoft To Reportedly Hike Production Of AI Chips](https://stocktwits.com/news-articles/markets/equity/microsoft-to-reportedly-hike-production-of-ai-chips/cZojwJgRJO6)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Microsoft (MSFT) share price jumped 2% on Monday to its highest level in over nine months as it prepares a push in its AI silicon strategy by boosting...
- [MSFT Stock Gets A Thumbs Up From Barclays – Firm Expects Quarter To Start Showing ‘More Differentiation’ In Software](https://finance.yahoo.com/markets/stocks/articles/msft-stock-gets-thumbs-barclays-145159137.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  Microsoft is scheduled to report fiscal Q1 2027 results after the closing bell on Oct. 28, with analysts estimating earnings of $4.72 per share on revenue...
- [Microsoft (MSFT) Stock Quotes, Company News And Chart Analysis](https://www.investors.com/news/technology/microsoft-msft-stock-quotes-company-news-and-chart-analysis/)  
  <sub>Investor's Business Daily, 22 hours ago</sub>  
  Microsoft (MSFT) Stock Quotes, Company News And Chart Analysis · IBD STAFF · Updated 01:03 PM ET 10/13/2026. (MSFT). Chart Error...
- [Microsoft stock is on pace for its first record close in nearly a year](https://qz.com/microsoft-stock-record-high-ai-rally-101326)  
  <sub>Quartz, 21 hours ago</sub>  
  Microsoft $MSFT stock is closing in on its first record since October 2025, with shares climbing as high as $551.13 — a gain of 1.8% — during Tuesday...
- [Wall Street sets Microsoft stock price target for next 12 months](https://finbold.com/wall-street-sets-microsoft-stock-price-target-for-next-12-months-3/)  
  <sub>Finbold, 2 hours ago</sub>  
  The blue-chip technology giant Microsoft (NASDAQ: MSFT) appears poised to resume its rise – broken by the early 2026 stock market plummet – with its next...
- [How much MSFT stock does Microsoft founder Bill Gates actually own?](https://www.thestreet.com/personalities/how-much-msft-stock-does-microsoft-founder-bill-gates-own)  
  <sub>TheStreet, 18 hours ago</sub>  
  Bill Gates has spent decades giving away his Microsoft fortune; we examine how much MSFT stock he still owns in 2026.
- [RBC Capital Sticks to Its Buy Rating for Microsoft (MSFT)](https://www.theglobeandmail.com/investing/markets/stocks/MSFT-Q/pressreleases/7373552/rbc-capital-sticks-to-its-buy-rating-for-microsoft-msft/)  
  <sub>The Globe and Mail, 10 hours ago</sub>  
  In a report released yesterday, Matthew Hedberg from RBC Capital maintained a Buy rating on Microsoft. The company's shares closed yesterday at $541.15.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 538.65 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 516.62 (+4.3%), 50d 504.01 (+6.9%), 200d 434.81 (+23.9%); 50d above 200d
Momentum: RSI(14) 66.4 | MACD 12.438 vs signal 10.620 (histogram 1.817)
Returns: 1d -0.9% | 5d +1.7% | 1m +8.4% | 3m +34.3%
52-week range: 352.83 - 543.45 (now 97.5% of the way up)
Volatility: ATR(14) 11.13 (2.1% of price) | annualised 20d 20.3%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 4.00T
Valuation: trailing P/E 30.35 | forward P/E 22.75 | P/B 9.04 | PEG 1.62
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
Price target: mean 589.60 (+9.5% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-13 Barclays: main, Overweight -> Overweight
  - 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-10-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-30 Piper Sandler: main, Overweight -> Overweight
  - 2026-09-23 Stifel: up, Hold -> Buy
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

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Trump and Nancy Pelosi’s Top AI Stock Pick: NVIDIA (NVDA)](https://finance.yahoo.com/markets/stocks/articles/trump-nancy-pelosi-top-ai-133316297.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  NVIDIA (NASDAQ:NVDA) remains a top AI pick among US politicians. It is one of the four stocks in our list of President Trump and Nancy Pelosi Portfolio: Top...
- [Nvidia Stock News (Oct 14, 2026): NVDA Rises 1.0% to $228.52](https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-october-14-2026/)  
  <sub>Gotrade, 12 hours ago</sub>  
  Nvidia closed at $228.52 on Oct 13, up 0.97% as the Nasdaq slipped 0.15%. What moved NVDA, how chip peers traded and the key risks.
- [What's Going On With NVIDIA Stock Wednesday?](https://www.benzinga.com/markets/tech/26/10/62348372/whats-going-on-with-nvidia-stock-wednesday-6)  
  <sub>Benzinga, 4 hours ago</sub>  
  NVIDIA edges higher in premarket trading as technical levels hold. Key support, resistance, and stock analysis updated for NVDA.
- [NVDA Stock Eyes Worst First Half Since 2022: Retail Patience Wears Thin As Board Member Trims Stake For Third Time This Year](https://stocktwits.com/news-articles/markets/equity/nvda-stock-eyes-worst-first-half-since-2022-retail-patience-wears-thin-as-board-member-trims-stake-for-third-time-this-year/cZ1QIRnR7ie)  
  <sub>Stocktwits, 8 hours ago</sub>  
  NVDA Stock Eyes Worst First Half Since 2022: Retail Patience Wears Thin As Board Member Trims Stake For Third Time This Year. Nvidia shares are up a mere 4.7%...
- [NVIDIA will provide U.K. researchers $50 million in computing each year for AI safety and security.](https://www.stocktitan.net/news/NVDA/nvidia-commits-250-million-to-advance-uk-agentic-safety-and-security-vy3m6f6uixkf.html)  
  <sub>Stock Titan, 9 hours ago</sub>  
  NVIDIA (NVDA) committed $250 million in computing access to support U.K. research into the safety and security of AI agents. The five-year donation will...
- [NVIDIA Corporation $NVDA Stock: Light Street Capital Management LLC Reduces Position](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-light-street-capital-management-llc-reduces-position-2026-10-14/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Light Street Capital Management LLC lowered its holdings in NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 49.8% during the 2nd quarter, according to the...
- [Nvidia's Valuation Is Becoming Absurdly Cheap (NASDAQ:NVDA)](https://seekingalpha.com/article/4953587-nvidia-valuation-is-becoming-absurdly-cheap)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Nvidia Corporation is rated a Strong Buy, with robust EPS growth, a next-gen Vera Rubin chip ramp, and an undemanding 14.5x FY28 forward P/E. Click for...
- [Nvidia Splashes the Cash as It Takes AI Safety Case Global](https://www.barrons.com/articles/nvidia-stock-price-ai-safety-4ce04a01)  
  <sub>Barron's, 3 hours ago</sub>  
  Nvidia stock was wavering as it outlined investments in European AI start-ups and safety initiatives.
- [Nvidia in 5 Years: Where the Stock Could Be Headed](https://www.fool.com/investing/2026/10/13/nvidia-in-5-years-where-the-stock-could-be-headed/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  When investors talk about artificial intelligence (AI), Nvidia (NVDA +0.97%) might be the first business that comes to mind. There's a good reason for that.
- [AI Trade Rotation: Software and Cloud Stocks Outpace Chipmakers Ahead of Nvidia Earnings](https://www.chartmill.com/news/NVDA/Chartmill-56195-AI-Trade-Rotation-Software-and-Cloud-Stocks-Outpace-Chipmakers-Ahead-of-Nvidia-Earnings)  
  <sub>ChartMill, 3 hours ago</sub>  
  AI stocks are rotating, not retreating. Software and cloud names lead while chip giants cool. See key valuations, growth, and risks across Nvidia, Palantir,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 223.65 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 228.81 (-2.3%), 50d 223.26 (+0.2%), 200d 202.70 (+10.3%); 50d above 200d
Momentum: RSI(14) 46.3 | MACD 2.164 vs signal 3.272 (histogram -1.108)
Returns: 1d -2.1% | 5d -5.8% | 1m +5.4% | 3m +7.8%
52-week range: 165.17 - 239.24 (now 79.0% of the way up)
Volatility: ATR(14) 5.56 (2.5% of price) | annualised 20d 23.9%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.40T
Valuation: trailing P/E 28.27 | forward P/E 14.05 | P/B 23.58 | PEG 0.48
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
Consensus: strong_buy (mean 1.29 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 49 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.72 (+47.0% vs last close), range 180.00 - 515.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 2,452,825 shares in 17 transaction(s) | sold 6,198,325 shares in 9
Net: -3,745,500 shares (-0.4% of insider holdings) | insiders hold 965,687,040 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-21 TETER TIMOTHY S (General Counsel): 30,460 shares, 6.79M
  - 2026-09-18 STEVENS MARK A (Director): 1,366,000 shares, 300.15M
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
(17 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Why Is NVO Stock Falling Pre-Market Today?](https://stocktwits.com/news-articles/markets/equity/why-is-nvo-stock-falling-pre-market-today/cZRtZlKR4UC)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Novo Nordisk AS (NVO) shares fell more than 14% in Monday's pre-market trade after the company announced headline results from Redefine 4, an open-label phase 3...
- [Why Novo Nordisk (NVO) Dipped More Than Broader Market Today](https://finance.yahoo.com/markets/stocks/articles/why-novo-nordisk-nvo-dipped-204504519.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  In the latest trading session, Novo Nordisk (NVO) closed at $38.06, marking a -1.35% move from the previous day.
- [BIOA, GLUE Stocks Clock Worst Day In Years— What’s The NVO Connection?](https://stocktwits.com/news-articles/markets/equity/bioa-glue-stocks-clock-worst-day-in-years-what-s-the-nvo-connection/cZN4NtDRJ5G)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Citi noted BIOA's greater-than-60% drop and agreed the data is a negative for BioAge's heart-disease thesis, yet argued the size of the move “seems overdone”...
- [NVO Oct 2026 37.000 put (NVO261016P00037000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO261016P00037000/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest NVO Oct 2026 37.000 put (NVO261016P00037000) stock quote, history, news and other vital information to help you with your stock trading and...
- [NVO Stock Jumps 3% As EU Approves Oral Wegovy Pill — Retail Notes LLY Is ‘Clearly Behind’ Its Danish Counterpart](https://stocktwits.com/news-articles/markets/equity/nvo-stock-jumps-3-as-eu-approves-oral-wegovy-pill-retail-notes-lly-is-clearly-behind-its-danish-counterpart/cZZPaw9R7r9)  
  <sub>Stocktwits, 19 hours ago</sub>  
  NVO Stock Jumps 3% As EU Approves Oral Wegovy Pill — Retail Notes LLY Is 'Clearly Behind' Its Danish Counterpart. Oral Wegovy is now cleared in all EU member...
- [Novo Nordisk A/S (NVO) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/NVO/latest-news/)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  Novo Nordisk A/S (NVO).
- [NVO Stock Slumps After Late-Stage Trial Fails Primary Goal – Retail Says ‘Current Revenue Drivers’ Still Intact](https://stocktwits.com/news-articles/markets/equity/nvo-stock-slumps-after-late-stage-trial-fails-primary-goal-retail-says-current-revenue-drivers-still-intact/cZN4B0qRJPh)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Novo's Phase 3 trial showed that investigational drug Ziltivekimab did not reduce major adverse cardiovascular events compared with the placebo.
- [APP Stock Slumps After-Hours Despite Strong Q4 Earnings — Why Does Retail See This As A Buying Opportunity?](https://stocktwits.com/news-articles/markets/equity/app-stock-slumps-after-hours-despite-strong-q4-2025-earnings/cZb6sQ4R4AK)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Applovin posted 66% growth in Q4 revenue, clocking $1.66 billion in the quarter, and also posted EPS of $3.24, beating analyst expectations.
- [Will NVO avoid deeper losses as technical momentum remains weak?](https://tradersunion.com/news/stocks/show/3801151-novo-nordisk-slides-1-36percent-to/)  
  <sub>Traders Union, 7 hours ago</sub>  
  Highlights. Novo Nordisk repurchased 1,245,000 B shares between October 5 and 9, 2026, lifting the May to February buyback total to 23,090,000 shares valued...
- [Eli Lilly (NYSE: LLY), Novo Nordisk (NYSE: NVO), Intuitive Surgical (NASDAQ: ISRG), And Medtronic (NYSE: MDT) Stand Out As Long-Term Healthcare Plays](https://www.foreignpolicyjournal.com/2026/10/14/eli-lilly-nyse-lly-novo-nordisk-nyse-nvo-intuitive-surgical-nasdaq-isrg-and-medtronic-nyse-mdt-stand-out-as-long-term-healthcare-plays/)  
  <sub>Foreign Policy Journal, 5 hours ago</sub>  
  Growth investors and value hunters alike have reason to pay close attention to four healthcare stocks spanning two of the sector's most compelling niches.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.10 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 38.79 (-1.8%), 50d 42.96 (-11.3%), 200d 45.19 (-15.7%); 50d below 200d
Momentum: RSI(14) 35.4 | MACD -1.464 vs signal -1.742 (histogram 0.278)
Returns: 1d +0.1% | 5d -0.4% | 1m -10.4% | 3m -26.0%
52-week range: 35.29 - 63.98 (now 9.8% of the way up)
Volatility: ATR(14) 0.91 (2.4% of price) | annualised 20d 35.7%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 168.12B
Valuation: trailing P/E 9.31 | forward P/E 11.50 | P/B 5.08 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 1 beat, 1 in line, 2 missed
  2026-06-30 missed by 6% | 2026-03-31 beat by 23% | 2025-12-31 in line | 2025-09-30 missed by 7%
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
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 45.22 (+18.7% vs last close), range 39.50 - 61.40
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 132,841 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [First Tracks Biotherapeutics: Teva Validated The Pathway, ANB033 May Own The Receptor](https://seekingalpha.com/article/4954063-first-tracks-stock-biotherapeutics-teva-validated-pathway-anb033-may-own-receptor)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  First Tracks Biotherapeutics offers a differentiated CD122 antagonist, ANB033, showing promising Phase 1b data in celiac disease. Read why TRAX stock is a...
- [Barclays keeps Buy rating for Teva stock at USD 42.00](https://www.ad-hoc-news.de/boerse/news/corporate-news/barclays-keeps-buy-rating-for-teva-stock-at-usd-42-00/70323530)  
  <sub>ad-hoc-news.de, 4 hours ago</sub>  
  Second-quarter revenue was USD 4.14 billion. Teva stock last stood at USD 41.25 on October 13, 2026, up 0.19 percent versus its USD 41.17 prior close.
- [TEVA261009P00040000 Interactive Stock Chart | TEVA Oct 2026 40.000 put Stock](https://finance.yahoo.com/chart/TEVA261009P00040000)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MRNA Stock Sets New 52-Week High As Nasdaq-100 Reentry Meets NIH Cancer-Vaccine Push](https://stocktwits.com/news-articles/markets/equity/mrna-stock-sets-new-52-week-high-as-nasdaq-100-reentry-meets-nih-cancer-vaccine-push/cZxGGuoRBnj)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Moderna shares on Friday were driven by multiple catalysts, including a Nasdaq-100 entry, a New York Times report on a planned NIH-backed cancer-vaccine...
- [Scotiabank Sticks to Its Buy Rating for Teva (TEVA)](https://www.theglobeandmail.com/investing/markets/markets-news/Tipranks/7373540/scotiabank-sticks-to-its-buy-rating-for-teva-teva/)  
  <sub>The Globe and Mail, 10 hours ago</sub>  
  In a report released yesterday, Louise Chen from Scotiabank maintained a Buy rating on Teva, with a price target of $47.00. The company's shares closed...
- [This Biopharma Stock Offers Compelling Upside After a Pullback](https://www.barrons.com/articles/neurocrine-biopharma-stock-offers-compelling-upside-after-pullback-d3231dd3)  
  <sub>Barron's, 15 hours ago</sub>  
  stock has pulled back from its all-time high, creating an opportunity for investors to buy the commercial-stage biopharma ahead of its next phase of growth.
- [Teva Pharmaceutical Industries Ltd. Tokenized Stock (Reality) (RTEVA) Price Prediction for 2026 to 2031](https://www.bybit.com/en/price-prediction/teva-pharmaceutical-industries-ltd-rstock/)  
  <sub>Bybit, 20 hours ago</sub>  
  Discover how Teva Pharmaceutical Industries Ltd. Tokenized Stock (Reality) (RTEVA) may perform from 2026 to 2031 using historical trends and forecasts.
- [FDA Approves New Drug for HSV Lesions in Adults](https://www.drugtopics.com/view/fda-approves-new-drug-for-hsv-lesions-in-adults)  
  <sub>Drug Topics, 23 hours ago</sub>  
  The FDA approved pritelivir (Hovilpri) oral tablets for the treatment of mucocutaneous lesions from herpes simplex virus (HSV) infection in adults,...
- [Gastroparesis Drugs Market Forecast to 2035: Rising Diabetes Prevalence to Drive Growth](https://www.indexbox.io/blog/gastroparesis-drugs-market-forecast-to-2035-rising-diabetes-prevalence-to-drive-growth/)  
  <sub>IndexBox, 14 hours ago</sub>  
  The global gastroparesis drugs market is set to grow through 2035, driven by the increasing prevalence of diabetes and the launch of novel therapies.
- [Deckers Outdoor Corporation (DECK) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/DECK/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest Deckers Outdoor Corporation (DECK) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.84 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 39.79 (+5.1%), 50d 38.03 (+10.0%), 200d 34.06 (+22.9%); 50d above 200d
Momentum: RSI(14) 68.8 | MACD 0.926 vs signal 0.797 (histogram 0.129)
Returns: 1d +1.4% | 5d +6.8% | 1m +6.6% | 3m +29.9%
52-week range: 18.95 - 41.84 (now 100.0% of the way up)
Volatility: ATR(14) 1.16 (2.8% of price) | annualised 20d 28.4%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 48.80B
Valuation: trailing P/E 69.73 | forward P/E 13.53 | P/B 6.29 | PEG 0.71
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
Price target: mean 47.17 (+12.7% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
Institutional ownership: 24.6%
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

- [ExxonMobil (XOM): Can Its Chemical Recovery Survive a Smaller Cost Advantage?](https://finance.yahoo.com/energy/articles/exxonmobil-xom-chemical-recovery-survive-134628890.html)  
  <sub>Yahoo Finance, 57 minutes ago</sub>  
  ExxonMobil Holdings Corporation (NYSE:XOM) increased chemical earnings from $110 million in the first quarter to $1.13 billion in the second, even as sales...
- [Perpetual Ltd Sells 5,990 Shares of ExxonMobil Corporation $XOM](https://www.marketbeat.com/instant-alerts/filing-perpetual-ltd-sells-5990-shares-of-exxonmobil-corporation-xom-2026-10-14/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Perpetual Ltd cut its position in ExxonMobil Corporation (NYSE:XOM - Free Report) by 13.8% during the 3rd quarter, according to the company in its most...
- [XOM, CVX Stocks In Focus: Trump Criticizes Exxon And Chevron For Profiting From Iran-Driven Oil Price Surge — ‘They’re Making Too Much Money’](https://stocktwits.com/news-articles/markets/equity/xom-cvx-stocks-in-focus-trump-criticizes-exxon-chevron-for-profiting-from-iran-driven-oil-price-surge/cZoTFnxRJ3i)  
  <sub>Stocktwits, 15 hours ago</sub>  
  According to data from Fiscal AI, the company is expected to report quarterly revenue of $52.06 million, down from $239.24 in the corresponding quarter of 2025.
- [Fund Update: New $357.3M $XOM stock position opened by WEALTH ENHANCEMENT ADVISORY SERVICES, LLC](https://www.quiverquant.com/news/Fund+Update%3A+New+%24357.3M+%24XOM+stock+position+opened+by+WEALTH+ENHANCEMENT+ADVISORY+SERVICES%2C+LLC)  
  <sub>Quiver Quantitative, 24 hours ago</sub>  
  WEALTH ENHANCEMENT ADVISORY SERVICES, LLC has opened a new $357.3M position in $XOM, per a new SEC 13F filing. This disclosure reflects the funds' holdings...
- [Is ExxonMobil Holdings Corp (XOM) Overvalued After 1.1% Rally? G](https://www.gurufocus.com/news/9122103/is-exxonmobil-holdings-corp-xom-overvalued-after-11-rally-gf-value-says-overvalued)  
  <sub>GuruFocus, 14 hours ago</sub>  
  On October 13, 2026, ExxonMobil Holdings Corp (XOM) shares rose 1.1% to a current price of $174.08. The stock has performed well recently, with a 52-week...
- [XOM RSI Overbought: What to Know](https://journalarta.com/en/2026/10/14/xom-rsi-overbought-stock-gains-1-12-october-13-2026/)  
  <sub>JournalArta, 7 hours ago</sub>  
  On October 13, 2026: price 174.08 USD, trend uptrend, RSI 71.8, support 158.30, resistance 174.08. technical analysis of xom stock. XOM RSI Overbought...
- [Guyana weighs scaling back LNG plans as Exxon says more gas needed for its wells - Reuters](https://seekingalpha.com/news/4652726-guyana-weighs-scaling-back-lng-plans-as-exxon-says-more-gas-needed-for-its-wells-reuters)  
  <sub>Seeking Alpha, 14 hours ago</sub>  
  ExxonMobil (XOM) has told the Guyana government it needs more offshore gas than expected to maximize oil output, potentially leaving less for liquefied...
- [Will Elevated Crude Prices Enhance ExxonMobil's Cash Flows?](https://www.zacks.com/stock/news/3006177/will-elevated-crude-prices-enhance-exxonmobils-cash-flows)  
  <sub>Zacks Investment Research, 19 hours ago</sub>  
  XOM stands to benefit from oil prices above $90 per barrel, with low-cost production in the Permian and Guyana supporting its earnings and cash flow...
- [ExxonMobil (NYSE:XOM) Stock Jumps 1.2% - Still a Buy?](https://www.marketbeat.com/instant-alerts/price-exxonmobil-nyse-xom-stock-jumps-12-still-a-buy-2026-10-13/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  ExxonMobil (NYSE:XOM) Stock Price Up 1.2% - Here's What Happened.
- [Exxon Mobil (XOM) Stock Price Today, Live Chart, News](https://techgraph.co/stock-market/quote/xom/)  
  <sub>TechGraph, 22 hours ago</sub>  
  What is the 52-week range for XOM? The 52-week range for XOM is $97.00 to $126.00. Advertisement. Price quotes refresh periodically while this page...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 175.03 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 164.67 (+6.3%), 50d 162.71 (+7.6%), 200d 151.15 (+15.8%); 50d above 200d
Momentum: RSI(14) 72.7 | MACD 2.939 vs signal 1.761 (histogram 1.178)
Returns: 1d +0.5% | 5d +6.7% | 1m +3.4% | 3m +19.9%
52-week range: 110.64 - 175.03 (now 100.0% of the way up)
Volatility: ATR(14) 3.34 (1.9% of price) | annualised 20d 19.1%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 719.71B
Valuation: trailing P/E 22.53 | forward P/E 15.27 | P/B 2.77 | PEG 1.38
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
Price target: mean 173.64 (-0.8% vs last close), range 142.00 - 200.00
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

## Whole-market funds

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand shift
- No macro surprise: Treasury yields stable and inflation 3.7% near expectations
- Technical indicators mixed: price above 200‑day SMA but below 20‑day/50‑day SMAs, RSI 46.6, MACD slightly bearish
- Analyst view provides no rating or price target, implying neutral outlook

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.32 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 28.40 (-0.3%), 50d 28.46 (-0.5%), 200d 27.24 (+4.0%); 50d above 200d
Momentum: RSI(14) 46.6 | MACD -0.042 vs signal -0.032 (histogram -0.010)
Returns: 1d -0.4% | 5d -0.6% | 1m -1.9% | 3m +2.6%
52-week range: 25.44 - 29.49 (now 71.1% of the way up)
Volatility: ATR(14) 0.27 (1.0% of price) | annualised 20d 12.9%
Volume: 0.15x the 20-day average
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
Three-year record: +14.1% a year | beta to the market 0.35
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
Shares outstanding: 27.60M | fund size: 781.63M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise in recent data releases
- Fund flows flat (no net inflows/outflows)
- Technicals show strong uptrend but price near 52‑week high with low volume
- Energy inventories: oil draw (bullish) offset by gas build (bearish) and EIA price outlook predicts falling oil prices
- Dollar index up 0.57% this week, supporting a bearish bias for commodities

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.29 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 32.77 (+1.6%), 50d 31.80 (+4.7%), 200d 28.58 (+16.5%); 50d above 200d
Momentum: RSI(14) 60.0 | MACD 0.352 vs signal 0.345 (histogram 0.007)
Returns: 1d -0.6% | 5d +2.4% | 1m -1.1% | 3m +17.0%
52-week range: 22.10 - 33.68 (now 96.7% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 15.2%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +16.3% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.92B
What it is made of: Other 50.4%, Cash 45.1%, Bonds 2.5%, Stocks 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 41.5%, Brent Crude Future Dec 26 9.7%, Invesco Short Term Treasury ETF 5.8%, Mini Ibovespa Future Dec 26 2.0%
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 111.40M | fund size: 3.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Most dimensions are neutral: no macro surprise, technicals lack a decisive break on volume, fundamentals unchanged, and only modest outflows.

**Main reasons it gave:**
- Fund flows: -0.8% share count change (outflows) over the past week
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs, low volume (0.32× 20‑day avg) and no decisive break
- Macro: no policy or rate surprise; yields and inflation unchanged, upward‑sloping yield curve
- Fundamentals: stable yield 5.4% and credit mix, no material change in holdings

<details><summary><b>News</b> — score +0.00</summary>

- [EMB: I Still Don't See A Bullish Investment Case (NASDAQ:EMB)](https://seekingalpha.com/article/4953977-emb-i-still-dont-see-a-bullish-investment-case)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  The iShares JPMorgan USD Emerging Markets Bond ETF will continue to do what it always does - that is allow investors to diversify. Read more on EMB here.
- [iShares JPMorgan USD Emerging Markets Bond ETF (EMB) seen less attractive than developed markets now](https://pluang.com/en/news-feed/emb-tidak-ada-alasan-investasi-bullish)  
  <sub>Pluang, 8 hours ago</sub>  
  The article evaluates the iShares JPMorgan USD Emerging Markets Bond ETF (EMB) as an investment option, focusing on its market price, yield, and risk-return...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 91.06 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 91.65 (-0.6%), 50d 93.39 (-2.5%), 200d 95.24 (-4.4%); 50d below 200d
Momentum: RSI(14) 37.0 | MACD -0.740 vs signal -0.843 (histogram 0.103)
Returns: 1d -0.2% | 5d +0.3% | 1m -2.1% | 3m -4.7%
52-week range: 90.14 - 97.74 (now 12.0% of the way up)
Volatility: ATR(14) 0.51 (0.6% of price) | annualised 20d 7.5%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.4%
Credit quality: BBB 33.9%, BB 25.2%, B 19.3%, A 17.6% | US government debt 88.0%
Three-year record: +9.6% a year | beta to the market 1.10
Cost and size: expense ratio 0.39% | net assets 12.93B
What it is made of: Bonds 99.1%, Cash 0.9%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.7%
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

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.8% (-109.31M) over 7d
Shares outstanding: 142.28M | fund size: 12.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: inflation 3.7% in line with expectations
- Technical indicators: price below 20d, 50d, 200d SMAs, RSI 30.7, MACD negative
- CFTC positioning: net short 24.8% and short crowding increased 2% OI
- Analyst coverage thin: only 2% of fund weight, but 100% buy rating

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [The AI trade is cracking. Here's how to profit](https://www.cnbc.com/amp/2026/10/13/the-ai-trade-is-cracking-heres-how-to-profit.html)  
  <sub>CNBC, 22 hours ago</sub>  
  Despite the Magnificent Seven making record highs, the AI trade is showing signs of cracks. Concerns over OpenAI's revenue growth have hit neocloud stocks,...
- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [Chip Stocks Slide as South Korea's KOSPI Plunges, J&J Sinks 6%: Stock Market Today](https://www.tradingview.com/news/benzinga:46d40e769094b:0-chip-stocks-slide-as-south-korea-s-kospi-plunges-j-j-sinks-6-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks slipped by midday Tuesday as a chip-sector rout — sparked by a 5% plunge in South Korea's KOSPI — offset gains in banks and energy,...
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-lower-us-172017687.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.5%.
- [Split in the Market Widens as Bank Earnings Hit](https://realmoney.thestreet.com/market-commentary/split-in-the-market-widens-as-bank-earnings-hit)  
  <sub>RealMoney Pro, 18 hours ago</sub>  
  New lows topped 500 and more than 60% of stocks are below their 200-day averages, while the mega caps hit another record.
- [How to Buy Global X Defense Tech ETF (SHLD)](https://www.fool.com/investing/how-to-invest/etfs/how-to-invest-in-shld-etf/)  
  <sub>The Motley Fool, 15 hours ago</sub>  
  The Global X Defense Tech ETF (SHLD -0.82%) debuted in September 2023, entering an increasingly crowded market for defense-focused exchange-traded funds...
- [Here’s Why I’m Holding Off on Cheap Stocks Right Now](https://pro.thestreet.com/market-commentary/heres-why-im-holding-off-on-cheap-stocks-right-now)  
  <sub>RealMoney Pro, 23 hours ago</sub>  
  The banks reversed, breadth is poor and almost nothing is trending up. That's when buying “bargains” is most dangerous. Bank earnings received an initial...
- [Daily ETF Flows: RSP Gathers $565M](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-rsp-gathers-210004324.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SPYM · State Street SPDR Portfolio S&P 500 ETF. 1,818.62.
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 273.59 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 280.62 (-2.5%), 50d 290.16 (-5.7%), 200d 277.42 (-1.4%); 50d above 200d
Momentum: RSI(14) 30.7 | MACD -3.680 vs signal -3.567 (histogram -0.112)
Returns: 1d -1.1% | 5d -1.5% | 1m -4.1% | 3m -7.4%
52-week range: 229.11 - 305.09 (now 58.5% of the way up)
Volatility: ATR(14) 3.48 (1.3% of price) | annualised 20d 11.5%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Small Blend
What it holds: P/E 16.35 | P/B 2.02 | P/S 1.25 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +18.7% a year | beta to the market 1.27
Cost and size: expense ratio 0.19% | net assets 78.04B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 0.5%, Twist Bioscience Corp 0.4%, Moog Inc Class A 0.4%, JFrog Ltd Ordinary Shares 0.4%, 10x Genomics Inc Ordinary Shares - Class A 0.4%
Sector mix: Healthcare 20.9%, Financial services 18.0%, Technology 14.5%, Industrials 13.3%
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
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.5% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MOG-A: 2026-10-13 JP Morgan: main, Overweight -> Overweight
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - TXG: 2026-10-13 TD Cowen: main, Hold -> Hold
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 24.8% of open interest (425,152 contracts)
Change on the week: +2.0% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 76.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fed target unchanged and inflation/unemployment near expectations (no macro surprise)
- Fund flows flat with no net share creation or redemption
- Technical indicators show downtrend but no decisive break (price below SMAs, RSI 34.8)
- Yield curve remains upward sloping, market pricing modest rate hikes

<details><summary><b>News</b> — score +0.00</summary>

- [Is Inspire Corporate Bond ETF (IBD) a Strong ETF Right Now?](https://finance.yahoo.com/markets/options/articles/inspire-corporate-bond-etf-ibd-092001641.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Launched on 07/10/2017, the Inspire Corporate Bond ETF (IBD) is a smart beta exchange traded fund offering broad exposure to the Investment Grade Corporate...
- [Daily ETF Flows: RSP Gathers $565M](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-rsp-gathers-210004324.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SPYM · State Street SPDR Portfolio S&P 500 ETF. 1,818.62.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 102.36 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 102.98 (-0.6%), 50d 104.67 (-2.2%), 200d 108.09 (-5.3%); 50d below 200d
Momentum: RSI(14) 34.8 | MACD -0.721 vs signal -0.825 (histogram 0.104)
Returns: 1d -0.2% | 5d +0.3% | 1m -1.8% | 3m -4.8%
52-week range: 101.83 - 112.92 (now 4.8% of the way up)
Volatility: ATR(14) 0.58 (0.6% of price) | annualised 20d 6.6%
Volume: 0.27x the 20-day average
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
Three-year record: +5.2% a year | beta to the market 1.35
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 293.50M | fund size: 30.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals mixed, positioning not decisive, flows flat, analyst coverage thin

**Main reasons it gave:**
- Treasury yields stable: 3‑month +0.06, 10‑year -0.02; VIX 15.7, no macro surprise
- Technical: price above 200‑day SMA (206.51), MACD line (-0.79) above signal (-1.31), RSI 45.9, volume 0.39× 20‑day avg
- CFTC positioning: net short 21.5% of open interest, short decreased 1.8% week‑over‑week
- Fund flows: share count flat (+0.0% change) over the week
- Analyst view: thin coverage (1.4% of fund) with 78.5% buy rating, price target +13.6% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · 0.46% · -0.73% · 7.28% · 10.40% · 14.11% · 39.82% · 744.75%. Key Events. Baseline. Advanced Chart. Loading...
- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance UK, 7 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · 0.46% · -0.73% · 7.28% · 10.40% · 14.11% · 39.82% · 744.75%. Key events. Baseline. Advanced chart. Loading...
- [Wall Street’s ‘Last Men Standing’: The Mag 7 Are Propping Up the S&P 500, Then Why Are Your ETFs at Risk?](https://www.tradingview.com/news/benzinga:032ee8723094b:0-wall-street-s-last-men-standing-the-mag-7-are-propping-up-the-s-p-500-then-why-are-your-etfs-at-risk/)  
  <sub>TradingView, 2 hours ago</sub>  
  The S&P 500 has gained approximately 14% in 2026, yet more than 40% of its constituent stocks have declined this year, according to Reuters.
- [Daily ETF Flows: RSP Gathers $565M](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-rsp-gathers-565m)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 12, 2026.
- [Paul Tudor Jones Says He’ll Be Short Stocks All of 2027](https://247wallst.com/investing/2026/10/14/paul-tudor-jones-says-hell-be-short-stocks-all-of-2027/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  Paul Tudor Jones told live television he plans to short the stock market for an entire calendar year, and his reason has nothing to do with earnings or...
- [Technical Reactions to RSP Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/23/Technical_Reactions_to_RSP_Trends_in_Macro_Strategies_101426123202_1791952322.html)  
  <sub>Stock Traders Daily, 14 hours ago</sub>  
  Key findings for Invesco S&p 500 Equal Weight Etf (NYSE: RSP). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias...
- [Rotation Away From AI Lately](https://seekingalpha.com/article/4953995-rotation-away-from-ai-lately)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Summary. Large-cap index ETFs entered Tuesday trading in "overbought" territory, solidly above their 50 DMAs. Small caps and micro caps, however,...
- [Is Invesco S&P SmallCap 600 Pure Value ETF (RZV) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/invesco-p-smallcap-600-pure-092002796.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The Invesco S&P SmallCap 600 Pure Value ETF (RZV) was launched on 03/01/2006, and is a smart beta exchange traded fund designed to offer broad exposure to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 211.65 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 211.34 (+0.1%), 50d 216.01 (-2.0%), 200d 206.51 (+2.5%); 50d above 200d
Momentum: RSI(14) 45.9 | MACD -0.790 vs signal -1.309 (histogram 0.519)
Returns: 1d -0.8% | 5d +0.5% | 1m -1.1% | 3m -1.6%
52-week range: 182.18 - 222.77 (now 72.6% of the way up)
Volatility: ATR(14) 1.82 (0.9% of price) | annualised 20d 8.4%
Volume: 0.39x the 20-day average
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
Three-year record: +16.7% a year | beta to the market 0.84
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -13.6% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-07 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-13 TD Cowen: main, Hold -> Hold
  - CRWD: 2026-10-14 BTIG: main, Buy -> Buy
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 155.55M | fund size: 32.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, positioning shows slight bullish shift but still net short, fundamentals stable but yield below current short‑term rates.

**Main reasons it gave:**
- Oct rate hike probability rose to 49% after CPI data (no clear surprise)
- Price 81.10 below 20‑day, 50‑day, and 200‑day SMAs
- Net short 28% of OI, down 2.3% week‑over‑week; crowding 97th percentile
- Fund yield 3.6% vs 3‑month Treasury yield 4.10%

<details><summary><b>News</b> — score +0.00</summary>

- [Precision Trading with Ishares 1-3 Year Treasury Bond Etf (SHY) Risk Zones](https://news.stocktradersdaily.com/news_release/10/Precision_Trading_with_Ishares_1-3_Year_Treasury_Bond_Etf_SHY_Risk_Zones_101426050002_1791968402.html)  
  <sub>Stock Traders Daily, 10 hours ago</sub>  
  Key findings for Ishares 1-3 Year Treasury Bond Etf (NYSE: SHY). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach; A mid-channel oscillation...
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [October rate hike probability pops to 49%, now a coin flip chance after CPI data](https://seekingalpha.com/news/4652903-october-rate-hike-probability-pops-to-49-now-a-coin-flip-chance-after-cpi-data)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Federal Reserve rate-hike odds for October have surged to a near coin-flip following the latest consumer price index report. Learn more here.
- [Stocktwits Weekly Spread: What Shaped Treasury Yields And The Dollar This Week](https://stocktwits.com/news-articles/markets/equity/stocktwits-weekly-spread-what-shaped-treasury-yields-and-the-dollar-this-week/cZxTXunRBnZ)  
  <sub>Stocktwits, 16 hours ago</sub>  
  U.S. fixed-income and currency markets saw heightened volatility during the week ending Oct. 9, 2026, as a sustained surge in global crude oil prices...
- [European ETF review: iShares chases JP Morgan's top spot in active ETF space as assets surge](https://www.investmentweek.co.uk/opinion/4537248/european-etf-review-ishares-chases-jp-morgan-spot-active-etf-space-assets-surge)  
  <sub>Investment Week, 7 hours ago</sub>  
  Crossing €3trn in assets at the start of the year was a major milestone. By the end of September, assets stood just shy of €3.4trn, and growth shows no sign...
- [BlackRock shifts to buying Treasuries with yiel...](https://pluang.com/en/news-feed/blackrock-klaim-pasar-salah-paham-federal-reserve-dan-beli-treasury-yield-di)  
  <sub>Pluang, 24 hours ago</sub>  
  BlackRock Investment Institute reversed its underweight stance on U.S. Treasuries, upgrading short-term bonds to overweight and long-term bonds to neutral...
- [What Is Behind Strong ETF Flows For Vanguard (ASX:VAS)?](https://kalkinemedia.com/au/stocks/etf/what-is-behind-strong-etf-flows-for-vanguard-asxvas)  
  <sub>Kalkine Media, 13 hours ago</sub>  
  Monthly exchange traded fund inflows stayed strong in September, just shy of the record set in August; Australian equity funds had their best month since...
- [Divergence emerges on Wall Street: Which U.S. Treasuries to buy?](https://news.futunn.com/en/post/1001062885/divergence-emerges-on-wall-street-which-us-treasuries-to-buy)  
  <sub>富途牛牛, 6 hours ago</sub>
- [Ray Dalio Cautions US Treasury Selloff Is ‘Far From Over’](https://fr.tradingview.com/news/stocktwits:90912f9b1094b:0-ray-dalio-cautions-us-treasury-selloff-is-far-from-over/)  
  <sub>TradingView, 20 hours ago</sub>  
  The U.S. government must refinance about $10 trillion in expiring debt while issuing $2.1 trillion in new debt this year, creating a severe funding...
- [Gold's Record ETF Stockpile Is No Match for the Bond Market](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/gold-s-record-etf-stockpile-is-no-match-for-the-bond-market/70318676)  
  <sub>ad-hoc-news.de, 13 hours ago</sub>  
  Gold fell 0.5% to $4148.26 as Bank of America warns of a possible drop to $3750, even as gold fund holdings hit a record 4256 tonnes.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.10 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 81.17 (-0.1%), 50d 81.55 (-0.6%), 200d 82.20 (-1.3%); 50d below 200d
Momentum: RSI(14) 37.6 | MACD -0.106 vs signal -0.132 (histogram 0.026)
Returns: 1d -0.1% | 5d -0.1% | 1m -0.3% | 3m -1.1%
52-week range: 81.05 - 83.18 (now 2.1% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 1.6%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 28.0% of open interest (4,485,811 contracts)
Change on the week: -2.3% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 209.30M | fund size: 16.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, modest bearish positioning, technicals lack decisive break, fundamentals unchanged.

**Main reasons it gave:**
- US Treasury yields changed little this week (10-year down 2 bps, 5-year up 5 bps) – no rate surprise
- CFTC positioning shows net short 30.2% with a modest +2.1% weekly increase – bearish but not extreme
- Technical indicators show price below 20‑day, 50‑day and 200‑day SMAs, RSI 39.6, no decisive breakout
- Fund basics unchanged: 5.0% yield, AA credit quality, modest 3‑year return – no fundamental catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT) · 1.41% · -3.09% · -9.66% · -10.80% · -13.47% · -46.08% · -4.13%.
- [Ray Dalio Warns US Debt Crisis Could Deepen as $2.1T in New Treasury Supply Hits Market: 'Credit Market Players Call That a Death Spiral'](https://www.tradingview.com/news/benzinga:ef9c504ad094b:0-ray-dalio-warns-us-debt-crisis-could-deepen-as-2-1t-in-new-treasury-supply-hits-market-credit-market-players-call-that-a-death-spiral/)  
  <sub>TradingView, 7 hours ago</sub>  
  Investor Ray Dalio warned that the United States faces a “death spiral” due to an oversupply of government debt. This structural imbalance is materializing...
- [Nasdaq, S&P 500 Futures Rise As Chip Rally Counters Iran Jitters Ahead Of Big Tech Earnings: Why IREN, ACHR, TSLA, BA Stocks Are Drawing Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-futures-rise-as-chip-rally-counters-iran-jitters-ahead-of-big-tech-earnings/cZZ1tCdR7HO)  
  <sub>Stocktwits, 16 hours ago</sub>  
  The VanEck Semiconductor ETF was up 0.41% at close, reversing three consecutive days of declines. However, tensions in the Middle East continued to rise...
- [Barlow’s Research Roundup: When to buy Canadian dividend stocks as rates climb](https://www.theglobeandmail.com/investing/markets/inside-the-market/article-barlows-research-roundup-when-to-buy-canadian-dividend-stocks-as-rates/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Daily roundup of research and analysis from The Globe and Mail's market strategist Scott Barlow. Rate sensitive stocks. Scotiabank strategist Hugo Ste-Marie...
- [Cash Is King Again? Record Money Market Inflows Put These Treasury ETFs on the Radar](https://www.benzinga.com/etfs/specialty-etfs/26/10/62328480/cash-is-king-again-record-money-market-inflows-put-these-treasury-etfs-on-the-radar)  
  <sub>Benzinga, 24 hours ago</sub>  
  Global money market funds attracted $166.4B in weekly inflows. Here's how SGOV, BIL, TLT ETFs fit into investors' flight to safety.
- [Daily ETF Flows: RSP Gathers $565M](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-rsp-gathers-210004324.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SPYM · State Street SPDR Portfolio S&P 500 ETF. 1,818.62.
- [BlackRock shifts to buying Treasuries with yiel...](https://pluang.com/en/news-feed/blackrock-klaim-pasar-salah-paham-federal-reserve-dan-beli-treasury-yield-di)  
  <sub>Pluang, 24 hours ago</sub>  
  BlackRock Investment Institute reversed its underweight stance on U.S. Treasuries, upgrading short-term bonds to overweight and long-term bonds to neutral...
- [Nasdaq, S&P 500, Dow Futures Edge Higher, Brushing Off Fresh US-Iran Clashes As Earnings Take Center Stage: TSLA, NOW, GOOGL, NOK In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-dow-futures-edge-higher-brushing-off-fresh-us-iran-clashes-as-earnings-take-center-stage-tsla-now-googl-nok-in-focus/cZZnIS5R7Dz)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Earnings dominated the narrative in the U.S. markets on Wednesday, with Alphabet, Tesla, and IBM reporting Q2 results.
- [Ray Dalio Cautions US Treasury Selloff Is ‘Far From Over’](https://fr.tradingview.com/news/stocktwits:90912f9b1094b:0-ray-dalio-cautions-us-treasury-selloff-is-far-from-over/)  
  <sub>TradingView, 20 hours ago</sub>  
  The U.S. government must refinance about $10 trillion in expiring debt while issuing $2.1 trillion in new debt this year, creating a severe funding...
- [7 of the Riskiest ETFs Investors Can Buy Today](https://money.usnews.com/investing/articles/riskiest-etfs-investors-can-buy-today)  
  <sub>U.S. News - Money, 20 hours ago</sub>  
  From leveraged strategies to complex derivatives, these ETFs expose investors to unusually high volatility, substantial losses and risks that can be...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 78.35 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 78.89 (-0.7%), 50d 80.83 (-3.1%), 200d 85.02 (-7.9%); 50d below 200d
Momentum: RSI(14) 39.6 | MACD -0.933 vs signal -1.065 (histogram 0.133)
Returns: 1d -0.0% | 5d +1.6% | 1m -2.9% | 3m -7.0%
52-week range: 77.11 - 92.06 (now 8.3% of the way up)
Volatility: ATR(14) 0.72 (0.9% of price) | annualised 20d 10.7%
Volume: 0.30x the 20-day average
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
Three-year record: +1.0% a year | beta to the market 2.31
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
Shares outstanding: 109.70M | fund size: 8.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, mixed technicals, thin analyst coverage, minimal net long positioning, and moderate fundamentals.

**Main reasons it gave:**
- Analyst view: 65.7% buy, price target +15.3% (thin coverage 11.4% of fund)
- Positioning: net long 0.1% of open interest, weekly decrease -2.2%
- Fund basics: moderate valuation (P/E 17.85) and solid 3-year performance (+17.5%/yr)
- Technicals: price below 20d/50d/200d SMAs, MACD slightly bullish, low volume
- Macro: no surprise in inflation (3.7%) or Fed policy (target 4.0%), yields stable

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.07 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 87.20 (-1.3%), 50d 89.79 (-4.1%), 200d 87.74 (-1.9%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -1.095 vs signal -1.113 (histogram 0.018)
Returns: 1d -0.3% | 5d +0.6% | 1m -3.2% | 3m -3.1%
52-week range: 77.90 - 93.19 (now 53.4% of the way up)
Volatility: ATR(14) 0.88 (1.0% of price) | annualised 20d 13.6%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +17.5% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 37.17B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.0%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.7%, Shell PLC 1.6%
Sector mix: Financial services 25.3%, Industrials 19.8%, Healthcare 12.1%, Technology 9.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 282.09M | fund size: 24.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, thin analyst coverage, modest positioning, stable fundamentals.

**Main reasons it gave:**
- Analyst coverage thin (22% weight) but all buy with +39.7% price target
- CFTC positioning net long modest 4.3% with small weekly increase (+1.2% OI)
- Fund fundamentals stable: P/E 15.9, yield 2%, no macro surprise
- Technical picture mixed: price below short‑term SMAs, above 200‑day SMA, low volume

<details><summary><b>News</b> — score +0.00</summary>

- [You Have Three Old 401(k)s From Three Jobs and None of Them Talk to Each Other. These 4 ETFs Are the One Account They Roll Into](https://247wallst.com/investing/etf/2026/10/13/you-have-three-old-401ks-from-three-jobs-and-none-of-them-talk-to-each-other-these-4-etfs-are-the-one-account-they-roll-into/)  
  <sub>24/7 Wall St., 19 hours ago</sub>  
  Three old 401(k)s often duplicate holdings across overlapping funds, yet no plan administrator flags it because none can see the others' portfolios.
- [Daily ETF Flows: RSP Gathers $565M](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-rsp-gathers-210004324.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SPYM · State Street SPDR Portfolio S&P 500 ETF. 1,818.62.
- [ETF boom turns specialized as leveraged and thematic funds shine](https://seekingalpha.com/news/4652613-etf-boom-turns-specialized-as-leveraged-and-thematic-funds-shine)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The U.S. ETF market is shifting toward greater specialization and leverage as product launches accelerate. Nearly 1,100 new ETFs have debuted so far in 2026...
- [With renewed volatility, here’s what three money managers think of South Korean stocks](https://www.theglobeandmail.com/investing/globe-advisor/advisor-etfs/article-with-renewed-volatility-heres-what-three-money-managers-think-of-south/)  
  <sub>The Globe and Mail, 6 hours ago</sub>  
  'There's a lot of hidden themes in the South Korean market,' says Ken Chen from Global X Investments Canada.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.13 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 59.90 (-1.3%), 50d 60.16 (-1.7%), 200d 58.20 (+1.6%); 50d above 200d
Momentum: RSI(14) 43.3 | MACD -0.165 vs signal -0.110 (histogram -0.055)
Returns: 1d -0.9% | 5d -1.2% | 1m -0.2% | 3m +0.5%
52-week range: 52.42 - 61.44 (now 74.4% of the way up)
Volatility: ATR(14) 0.62 (1.1% of price) | annualised 20d 15.6%
Volume: 0.17x the 20-day average
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
Three-year record: +18.4% a year | beta to the market 0.75
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +39.7% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 4.3% of open interest (1,059,025 contracts)
Change on the week: +1.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 83.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [October rate hike probability pops to 49%, now a coin flip chance after CPI data](https://seekingalpha.com/news/4652903-october-rate-hike-probability-pops-to-49-now-a-coin-flip-chance-after-cpi-data)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Federal Reserve rate-hike odds for October have surged to a near coin-flip following the latest consumer price index report. Learn more here.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 76.84 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 77.57 (-0.9%), 50d 78.65 (-2.3%), 200d 79.75 (-3.6%); 50d below 200d
Momentum: RSI(14) 26.7 | MACD -0.484 vs signal -0.501 (histogram 0.018)
Returns: 1d -0.3% | 5d -0.4% | 1m -2.0% | 3m -3.7%
52-week range: 76.84 - 81.28 (now 0.0% of the way up)
Volatility: ATR(14) 0.31 (0.4% of price) | annualised 20d 4.3%
Volume: 0.34x the 20-day average
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 195.60M | fund size: 15.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [October rate hike probability pops to 49%, now a coin flip chance after CPI data](https://seekingalpha.com/news/4652903-october-rate-hike-probability-pops-to-49-now-a-coin-flip-chance-after-cpi-data)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Federal Reserve rate-hike odds for October have surged to a near coin-flip following the latest consumer price index report. Learn more here.
- [Thomas Massie Says the Big Beautiful Bill Raised ‘What You Must Pay’ - iShares 7-10 Year Treasury Bond ET](https://www.benzinga.com/markets/economic-data/26/10/62347478/thomas-massie-big-beautiful-bill-increased-what-you-must-pay-deficit-2027)  
  <sub>Benzinga, 4 hours ago</sub>  
  Rep. Thomas Massie says all government spending is paid for by citizens, while the U.S. deficit is projected to hit 6.1% of GDP in 2027.
- [Author Nassim Taleb Pushes Back on Scott Bessent’s Inflation Claim - iShares 7-10 Year Treasury Bond ETF](https://www.benzinga.com/markets/economic-data/26/10/62344394/nassim-taleb-scott-bessent-inflation-oil-shock-doesnt-show-yet)  
  <sub>Benzinga, 10 hours ago</sub>  
  Nassim Taleb pushed back on Scott Bessent's inflation claims, arguing the oil shock, deficit, and borrowing costs point to more pressure.
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [Divergence emerges on Wall Street: Which U.S. Treasuries to buy?](https://news.futunn.com/en/post/1001062885/divergence-emerges-on-wall-street-which-us-treasuries-to-buy)  
  <sub>富途牛牛, 6 hours ago</sub>
- [US GDP Grows At 1.4% In Q4, Economy Expands At A Slower Clip Than Wall Street Estimates](https://stocktwits.com/news-articles/markets/equity/us-gdp-q4-2025-report/cZRNEPYR4xX)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Compared to the third quarter, the deceleration in real GDP in Q4 reflected downturns in government spending and exports and a deceleration in consumer...
- [BofA's Brian Moynihan Expects Fed To Hike Rates Three Times In 2026, Sees Inflation In 'Mid-2s' By End Of 2027](https://stocktwits.com/news-articles/markets/equity/bofa-brian-moynihan-expects-three-rate-hikes-in-2026-inflation-mid-2s-2027/cZo4ULBRJea)  
  <sub>Stocktwits, 8 hours ago</sub>  
  During an interview with CNBC, Moynihan said inflation had been easing before picking up again due to the effects of tariffs and the war on prices,...
- [Americans Bear The Brunt Of Trump’s Tariffs, As Per NY Fed Report](https://stocktwits.com/news-articles/markets/equity/americans-bear-the-brunt-of-trump-tariffs-as-per-ny-fed-report/cZRTtkCR4rt)  
  <sub>Stocktwits, 15 hours ago</sub>  
  In a report published on Thursday, the New York Fed said that almost 90% of the economic weight of the import tax was shouldered by U.S. businesses and...
- [CPI Report: Annual Inflation Rate Comes In At 2.4% In January, Below Wall Street Expectations](https://stocktwits.com/news-articles/markets/equity/us-consumer-inflation-january-2026-cpi-report/cZR5t5IR4sz)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Consumer price index (CPI) rose 0.2% in January on a seasonally adjusted basis, after rising 0.3% in December.
- [Why is BlackRock cutting US stock exposure and boosting Treasuries now](https://invezz.com/au/news/2026/10/13/why-is-blackrock-cutting-us-stock-exposure-and-boosting-treasuries-now/)  
  <sub>Invezz, 22 hours ago</sub>  
  BlackRock has reduced its exposure to US equities and increased its allocation to US Treasuries as rising bond yields create more attractive income...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.31 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 89.76 (-0.5%), 50d 91.41 (-2.3%), 200d 94.19 (-5.2%); 50d below 200d
Momentum: RSI(14) 34.6 | MACD -0.618 vs signal -0.720 (histogram 0.102)
Returns: 1d -0.3% | 5d +0.2% | 1m -1.7% | 3m -4.7%
52-week range: 88.92 - 97.99 (now 4.2% of the way up)
Volatility: ATR(14) 0.45 (0.5% of price) | annualised 20d 6.1%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Long Government
Yield: 4.1%
Credit quality: AA 100.0% | US government debt 99.7%
Three-year record: +3.3% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.56B
What it is made of: Bonds 99.7%, Cash 0.3%
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

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 37.3% of open interest (5,742,990 contracts)
Change on the week: -1.4% of open interest
Crowding: 70% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 146.00M | fund size: 13.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [F/m Long-Term Treasury Inflation-Protected Security (TIPS) ETF (RTHY) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/RTHY/)  
  <sub>Yahoo Finance UK, 11 hours ago</sub>  
  Find the latest F/m Long-Term Treasury Inflation-Protected Security (TIPS) ETF (RTHY) stock quote, history, news and other vital information to help you...
- [Don't let inflation bite — how to hedge with TIPS, commodities and infrastructure funds](https://www.cnbc.com/2026/10/13/inflation-hedge-tips-commodities-infrastructure.html)  
  <sub>CNBC, 18 hours ago</sub>  
  Many investors are turning to inflation-linked bonds amid concerns over rising prices. TIPS are offering high yields, but investors need to keep an eye on...
- [Antifragilität: Was KMU aus dem Erfolg der Schweiz lernen können](https://www.ubs.com/global/en/assetmanagement/insights/cross-divisional-adp/ch/en/services/guide/impulse/articles/physical-ai-in-smes.html)  
  <sub>UBS, 21 hours ago</sub>  
  What sets Physical AI apart from traditional automation and how SMEs can get started with clear benefits, data and pilot projects.
- [Investors eye TIPS and commodities as inflation concerns persist despite recent easing.](https://pluang.com/en/news-feed/cara-melindungi-diri-dari-inflasi-dengan-tips-komoditas-dan-dana-infrastruktur)  
  <sub>Pluang, 18 hours ago</sub>  
  Inflation remains a key concern as the Consumer Price Index is expected to show 3.6% in September, above the Fed's 2% target. Treasury Inflation-Protected...
- [İş Yatırım Details ISX30 ETF Market-Making Transactions](https://www.tipranks.com/news/company-announcements/is-yatirim-details-isx30-etf-market-making-transactions-2)  
  <sub>TipRanks, 3 hours ago</sub>  
  The latest update is out from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ). İş Yatırım Menkul Değerler A.Ş. reported its latest market-making activity in...
- [QQQ ETF Remains Under Pressure on Tuesday, October 13. Here’s Why](https://www.tipranks.com/news/qqq-etf-remains-under-pressure-on-tuesday-october-13-heres-why)  
  <sub>TipRanks, 16 hours ago</sub>  
  The Invesco QQQ Trust ETF ($QQQ) was down 0.53% as of the time of writing on Tuesday, after falling about 0.70% in the previous session.
- [Trump Highlights Ohio Submarine Facility: Potential Ripple Effects on Industrial and Defense ETFs](https://www.tipranks.com/news/catalyst/trump-highlights-ohio-submarine-facility-potential-ripple-effects-on-industrial-and-defense-etfs)  
  <sub>TipRanks, 3 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “Trump's job-creation juggernaut stops in Ohio to unveil...
- [Banco Bradesco Retreats After Brazil ETF Rebalancing](https://www.tipranks.com/news/catalyst/banco-bradesco-retreats-after-brazil-etf-rebalancing)  
  <sub>TipRanks, 15 hours ago</sub>  
  Banco Bradesco ( ($BBDO) ) is experiencing volatility. Read on for a possible explanation for the stock's unusual movement. Banco Bradesco shares are...
- [3 ETFs Tipped for 10% or More Gains by AI Analyst](https://www.tipranks.com/news/3-etfs-tipped-for-10-or-more-gains-by-tipranks-ai-analyst)  
  <sub>TipRanks, 18 hours ago</sub>  
  Exchange-traded funds (ETFs) offer a key way to enter financial markets. For investors looking for a starting point to tap into the growth potential of U.S....
- [How Trump’s Greenland Resource Push Could Jolt Energy and Mining ETFs](https://www.tipranks.com/news/catalyst/how-trumps-greenland-resource-push-could-jolt-energy-and-mining-etfs)  
  <sub>TipRanks, 10 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “Massive Oil, Gas, and Mineral Exploration is getting...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.52 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 104.57 (-0.0%), 50d 105.95 (-1.4%), 200d 109.11 (-4.2%); 50d below 200d
Momentum: RSI(14) 40.6 | MACD -0.464 vs signal -0.587 (histogram 0.123)
Returns: 1d -0.0% | 5d +0.3% | 1m -1.2% | 3m -3.2%
52-week range: 103.98 - 112.20 (now 6.5% of the way up)
Volatility: ATR(14) 0.37 (0.4% of price) | annualised 20d 4.7%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 4.7%
Credit quality: AA 99.9% | US government debt 100.0%
Three-year record: +3.9% a year | beta to the market 0.71
Cost and size: expense ratio 0.18% | net assets 14.23B
What it is made of: Bonds 100.0%
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

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 37.3% of open interest (5,742,990 contracts)
Change on the week: -1.4% of open interest
Crowding: 70% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 177.70M | fund size: 18.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Top 8 Currency ETFs Malaysia 2026](https://www.moomoo.com/my/learn/top-currency-etfs-malaysia)  
  <sub>Moomoo, 2 hours ago</sub>  
  Explore the top currency ETFs for Malaysians in 2026 to hedge Ringgit volatility and diversify globally. Learn how to buy and trade on Moomoo Malaysia,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.20 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 28.80 (+1.4%), 50d 28.37 (+2.9%), 200d 27.82 (+5.0%); 50d above 200d
Momentum: RSI(14) 71.0 | MACD 0.222 vs signal 0.203 (histogram 0.019)
Returns: 1d +0.6% | 5d +0.6% | 1m +3.5% | 3m +3.1%
52-week range: 26.47 - 29.20 (now 100.0% of the way up)
Volatility: ATR(14) 0.13 (0.4% of price) | annualised 20d 5.1%
Volume: 0.17x the 20-day average
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
Three-year record: +3.8% a year | beta to the market -11.39
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
Share count change: 1 week: -0.4% (-1.65M) over 7d
Shares outstanding: 14.85M | fund size: 433.74M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat flows, mixed technicals, bullish analyst view.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +22.7% price target for top holdings
- Technicals: price below 20d, 50d, 200d SMAs; RSI 41.8; MACD negative; low volume
- Fund flows: flat share count (0% change) over past week
- Macro: no surprise data; upward sloping yield curve; VIX low at 15.7

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 118.79 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 121.67 (-2.4%), 50d 122.54 (-3.1%), 200d 122.91 (-3.3%); 50d below 200d
Momentum: RSI(14) 41.8 | MACD -1.422 vs signal -1.013 (histogram -0.409)
Returns: 1d +0.1% | 5d +0.7% | 1m -3.1% | 3m -1.4%
52-week range: 97.88 - 137.69 (now 52.5% of the way up)
Volatility: ATR(14) 1.71 (1.4% of price) | annualised 20d 18.6%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +35.3% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.7% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-12 JP Morgan: main, Overweight -> Overweight
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 2.55M | fund size: 302.93M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro catalyst, no decisive technical break, and flat fund flows. Analyst view is modestly bearish but not enough to shift the overall stance.

**Main reasons it gave:**
- Analyst view: weighted price target -6.2% below current price
- Technicals: price below 20‑day, 50‑day, and 200‑day SMAs with low volume
- Macro: US Treasury yields up and dollar stronger, indicating pressure on equities
- Fund flows flat: 0% share count change over the week

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 28.45 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 28.53 (-0.3%), 50d 29.30 (-2.9%), 200d 28.73 (-1.0%); 50d above 200d
Momentum: RSI(14) 45.1 | MACD -0.194 vs signal -0.261 (histogram 0.067)
Returns: 1d -1.1% | 5d +0.8% | 1m -1.5% | 3m -0.6%
52-week range: 24.95 - 30.43 (now 64.0% of the way up)
Volatility: ATR(14) 0.33 (1.2% of price) | annualised 20d 17.1%
Volume: 0.50x the 20-day average
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
Three-year record: +14.4% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

```text
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.2% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 63.60M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, technicals lack decisive break, fundamentals solid but no catalyst, analyst view modestly bullish but not enough to shift overall stance.

**Main reasons it gave:**
- Analyst view: 62.4% buy rating and +4.9% price target for top holdings
- Fund flows flat (0% change) over past week, indicating no net demand
- Technical indicators: price below 20‑day SMA, RSI 45.8, low volume, no decisive break
- Macro: yields stable, VIX low, no surprise data releases
- Fundamentals: moderate valuation (P/E 18.94) and strong 3‑year performance (+23.7% per year) but no clear catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.03 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 59.28 (-0.4%), 50d 60.60 (-2.6%), 200d 57.93 (+1.9%); 50d above 200d
Momentum: RSI(14) 45.8 | MACD -0.391 vs signal -0.503 (histogram 0.112)
Returns: 1d -1.5% | 5d +1.9% | 1m -2.1% | 3m -0.6%
52-week range: 49.72 - 62.64 (now 72.1% of the way up)
Volatility: ATR(14) 0.68 (1.2% of price) | annualised 20d 15.1%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.94 | P/B 2.75 | P/S 2.69 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +23.7% a year | beta to the market 0.80
Cost and size: expense ratio 0.50% | net assets 7.02B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Royal Bank of Canada 9.1%, The Toronto-Dominion Bank 6.5%, Shopify Inc Registered Shs -A- Subord Vtg 6.0%, Bank of Montreal 3.8%, Bank of Nova Scotia 3.7%
Sector mix: Financial services 39.9%, Energy 17.3%, Basic materials 15.2%, Technology 9.3%
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
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 62.4% | hold 37.6% | sell 0.0% (mean 2.22 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.9% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 94.80M | fund size: 5.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, modest analyst bullishness, technicals slightly bearish but not decisive.

**Main reasons it gave:**
- Flat fund flows (share count unchanged) indicating no net inflow/outflow
- Price below 20‑day and 50‑day SMAs (−0.3% vs 20d SMA, −2.7% vs 50d SMA) showing slight bearish technical bias
- Analyst coverage of top holdings is 81.7% buy with a +10.7% price target, indicating modest bullish sentiment
- Macro data shows no surprise: yields stable, inflation 3.7% near target, VIX low at 15.7

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 50.60 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 50.75 (-0.3%), 50d 52.03 (-2.7%), 200d 51.46 (-1.7%); 50d above 200d
Momentum: RSI(14) 46.4 | MACD -0.387 vs signal -0.489 (histogram 0.103)
Returns: 1d -1.1% | 5d +1.2% | 1m -1.3% | 3m +0.8%
52-week range: 45.38 - 54.72 (now 55.9% of the way up)
Volatility: ATR(14) 0.68 (1.3% of price) | annualised 20d 16.5%
Volume: 0.09x the 20-day average
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
Three-year record: +18.3% a year | beta to the market 1.25
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-12 Cantor Fitzgerald: main, Neutral -> Neutral
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
Shares outstanding: 7.65M | fund size: 387.09M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, bullish analyst view not enough to shift stance.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicating no net demand
- Technical indicators: price below 20‑day SMA, RSI 38.5, MACD slightly negative
- No macro surprise: yields stable, no policy shift, VIX modest
- Analyst view bullish (78.7% buy, +17% price target) but not enough to outweigh neutral macro and technicals

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 40.96 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 41.60 (-1.5%), 50d 42.87 (-4.5%), 200d 42.33 (-3.2%); 50d above 200d
Momentum: RSI(14) 38.5 | MACD -0.530 vs signal -0.527 (histogram -0.003)
Returns: 1d -0.6% | 5d +0.1% | 1m -3.7% | 3m -0.7%
52-week range: 38.08 - 44.59 (now 44.2% of the way up)
Volatility: ATR(14) 0.47 (1.2% of price) | annualised 20d 14.5%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +18.6% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
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
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.0% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bullish analyst coverage is offset by flat fund flows, weak technical momentum and a stable macro backdrop with no clear catalyst.

**Main reasons it gave:**
- Fund flows flat: share count unchanged (+0.0% over 1 week)
- Technical momentum weak: price below 20‑day, 50‑day, 200‑day SMAs; RSI 30.3 (near oversold)
- Analyst view bullish: 100% buy rating on 53% of fund, weighted price target +19.3%
- Macro data stable: yields unchanged, VIX low (15.7), no rate surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 55.97 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 58.47 (-4.3%), 50d 60.79 (-7.9%), 200d 58.10 (-3.7%); 50d above 200d
Momentum: RSI(14) 30.3 | MACD -1.357 vs signal -1.177 (histogram -0.180)
Returns: 1d -1.2% | 5d -0.7% | 1m -7.9% | 3m -7.6%
52-week range: 50.47 - 63.35 (now 42.7% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 19.5%
Volume: 0.05x the 20-day average
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
Three-year record: +27.0% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.3% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 8.55M | fund size: 478.54M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise in rates or data
- Technical indicators mixed: price above 200‑day SMA but below 20‑day SMA, RSI 44.9, MACD negative
- CFTC shows net short 8.2% decreasing by 6.9% (crowded short)
- Analyst coverage thin (17% weight) despite bullish price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 96.28 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 97.63 (-1.4%), 50d 96.94 (-0.7%), 200d 91.08 (+5.7%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD 0.182 vs signal 0.404 (histogram -0.223)
Returns: 1d -1.1% | 5d -2.1% | 1m -0.7% | 3m +4.8%
52-week range: 79.49 - 99.32 (now 84.7% of the way up)
Volatility: ATR(14) 1.23 (1.3% of price) | annualised 20d 17.0%
Volume: 0.17x the 20-day average
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
Three-year record: +20.8% a year | beta to the market 0.83
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.3% above the current prices
Holdings read: 8306.T, 7203.T, 8035.T, 8316.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 8.2% of open interest (20,996 contracts)
Change on the week: -6.9% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 227.85M | fund size: 21.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, mixed technicals, modest analyst buy bias.

**Main reasons it gave:**
- Analyst coverage of top holdings shows 64.8% buy rating and a weighted price target +6.6% above current price
- Fund flows flat over the past week, indicating no net demand or supply pressure
- Technicals mixed: price above 20‑day SMA but below 50‑day and 200‑day SMAs, MACD bullish but low volume and neutral RSI

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.15 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 59.90 (+0.4%), 50d 61.73 (-2.6%), 200d 61.61 (-2.4%); 50d above 200d
Momentum: RSI(14) 48.0 | MACD -0.526 vs signal -0.685 (histogram 0.159)
Returns: 1d +0.4% | 5d +1.3% | 1m -0.2% | 3m -4.5%
52-week range: 55.06 - 65.08 (now 50.7% of the way up)
Volatility: ATR(14) 0.62 (1.0% of price) | annualised 20d 11.1%
Volume: 0.41x the 20-day average
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
Three-year record: +12.7% a year | beta to the market 0.91
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
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.6% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view on top holdings is offset by flat fund flows, bearish technical momentum, and unchanged macro backdrop.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% week)
- Technical momentum bearish: RSI 38.4, MACD negative, price below 20‑day and 50‑day SMA
- Analyst coverage bullish: 100% buy rating on 46.7% of holdings, price target +35.6% above current
- Macro unchanged: no policy surprise, yields stable, inflation 3.7% (within expectations)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 65.47 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 67.24 (-2.6%), 50d 68.21 (-4.0%), 200d 64.72 (+1.2%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -0.534 vs signal -0.350 (histogram -0.184)
Returns: 1d -0.8% | 5d -1.9% | 1m -1.3% | 3m -3.4%
52-week range: 55.33 - 71.61 (now 62.3% of the way up)
Volatility: ATR(14) 0.89 (1.4% of price) | annualised 20d 17.6%
Volume: 0.05x the 20-day average
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
Three-year record: +23.5% a year | beta to the market 1.09
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

<details><summary><b>What analysts and big funds say</b> — score +1.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +1.00</summary>

```text
Rolled up from the 5 largest holdings, 46.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.63 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.6% above the current prices
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
Shares outstanding: 5.55M | fund size: 363.36M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, technicals show price below short‑term averages with low volume and no decisive break, analyst view modestly bullish but not enough to outweigh neutrality, fundamentals moderate.

**Main reasons it gave:**
- US Treasury yields stable, 10‑yr at 5.26% (-0.02% week)
- Fund flows flat: share count unchanged (+0.0% week)
- Price below 20‑day SMA (57.69 vs 59.43) and 50‑day SMA (61.14), RSI 35.1, volume 0.14× avg
- Analyst price target +6.1% above current, buy/hold split 51.5%/48.5%
- Fundamentals moderate: P/E 15.94, yield 2.8%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 57.69 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 59.43 (-2.9%), 50d 61.14 (-5.6%), 200d 57.78 (-0.2%); 50d above 200d
Momentum: RSI(14) 35.1 | MACD -0.955 vs signal -0.853 (histogram -0.102)
Returns: 1d -1.1% | 5d -0.2% | 1m -5.6% | 3m -2.7%
52-week range: 48.95 - 63.23 (now 61.2% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 18.1%
Volume: 0.14x the 20-day average
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
Three-year record: +33.0% a year | beta to the market 0.88
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
Weighted price target: +6.1% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, and technicals show no decisive break; analyst view is bullish but not enough to outweigh neutral macro and technical backdrop.

**Main reasons it gave:**
- US Treasury yields stable, no rate surprise (3‑month +0.06, 10‑year -0.02)
- Fund flows flat (share count +0.0% over 1 week)
- Technical momentum neutral (RSI 48.4, MACD below signal, low volume)
- Analyst ratings all buy with +33% price target, but no supporting macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 17 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 112.09 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 114.15 (-1.8%), 50d 109.77 (+2.1%), 200d 90.87 (+23.4%); 50d above 200d
Momentum: RSI(14) 48.4 | MACD 1.229 vs signal 1.794 (histogram -0.565)
Returns: 1d -1.2% | 5d -3.6% | 1m +5.1% | 3m +11.9%
52-week range: 60.03 - 118.00 (now 89.8% of the way up)
Volatility: ATR(14) 2.09 (1.9% of price) | annualised 20d 25.5%
Volume: 0.26x the 20-day average
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
Three-year record: +45.0% a year | beta to the market 1.26
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.1% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 85.00M | fund size: 9.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst coverage is offset by bearish technicals, flat fund flows, and no macro surprise.

**Main reasons it gave:**
- Analyst view: 90.9% buy rating and +10.5% price target covering 47.8% of fund
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs; RSI 46, MACD negative
- Fund flows: flat share count change (0% over 1 week)
- Macro: no rate or policy surprise; yields unchanged, VIX low (15.7)
- Fundamentals: low P/E 12.2, solid 3‑year return +13.7% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 72.36 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 72.51 (-0.2%), 50d 74.65 (-3.1%), 200d 75.90 (-4.7%); 50d below 200d
Momentum: RSI(14) 46.0 | MACD -0.649 vs signal -0.876 (histogram 0.227)
Returns: 1d -1.2% | 5d +0.5% | 1m -2.3% | 3m -3.8%
52-week range: 64.84 - 81.23 (now 45.9% of the way up)
Volatility: ATR(14) 1.27 (1.8% of price) | annualised 20d 20.3%
Volume: 0.19x the 20-day average
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
Three-year record: +13.7% a year | beta to the market 1.07
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.16 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.5% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, technicals not decisive, analyst view neutral.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week
- Macro: US Treasury yields stable, no policy surprise
- Technical: RSI 34.3 (oversold), MACD negative, volume 0.30x 20‑day average
- Analyst view neutral: no rating changes or price targets for top holdings

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI South Korea ETF (EWY) Options Chain - Yahoo Finance](https://ca.finance.yahoo.com/quote/EWY/options/?date=1807833600&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  View the basic EWY option chain and compare options of iShares MSCI South Korea ETF on Yahoo Finance.
- [Dan Ives’ AI Bull Case Extends To South Korea – With A 9,000 KOSPI Target And 2027 Stock Picks](https://www.tradingview.com/news/stocktwits:f64a2d4b6094b:0-dan-ives-ai-bull-case-extends-to-south-korea-with-a-9-000-kospi-target-and-2027-stock-picks/)  
  <sub>TradingView, 5 hours ago</sub>  
  The South Korean stock market could hit fresh all-time highs over the next six to 12 months as concerns over artificial intelligence (AI) have triggered an...
- [IShares MSCI South Korea ETF Options Spot-On: On October 13th, 125.74K Contracts Were Traded, With 1.13 Million Open Interest](https://news.futunn.com/en/post/1001034850/ishares-msci-south-korea-etf-options-spot-on-on-october)  
  <sub>富途牛牛, 16 hours ago</sub>  
  OnOctober 13th ET, $iShares MSCI South Korea ETF(EWY.US)$ had active options trading, with a total trading volume of 125.74K options for the day,...
- [iShares MSCI South Korea ETF (EWY) Options Chain](https://ca.finance.yahoo.com/quote/EWY/options/?date=1793318400&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  View the basic EWY option chain and compare options of iShares MSCI South Korea ETF on Yahoo Finance.
- [What Triggered the KOSPI’s 5.5% Slide, and What Does It Mean for EWY (NYSEARCA:EWY)?](https://kalkine.ca/news/technology/what-triggered-the-kospis-55-slide-and-what-does-it-mean-for-ewy-nysearcaewy)  
  <sub>kalkine.ca, 1 hour ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 162.18 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 182.31 (-11.0%), 50d 179.54 (-9.7%), 200d 159.64 (+1.6%); 50d above 200d
Momentum: RSI(14) 34.3 | MACD -3.053 vs signal -0.127 (histogram -2.926)
Returns: 1d -2.6% | 5d -11.7% | 1m -8.1% | 3m -0.7%
52-week range: 82.69 - 219.20 (now 58.2% of the way up)
Volatility: ATR(14) 5.90 (3.6% of price) | annualised 20d 42.5%
Volume: 0.30x the 20-day average
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
Three-year record: +45.8% a year | beta to the market 2.48
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 75.60M | fund size: 12.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as technicals are bearish, macro shows no surprise, and fund flows are flat despite a bullish analyst view limited to 43.4% of holdings.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs (63.05 vs 64.97, 67.83, 68.94)
- RSI 38.7 indicating weak momentum
- Flat fund flows (0% change) indicating no net demand
- Analyst coverage 43.4% with all‑buy rating and +34.4% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 63.05 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 64.97 (-3.0%), 50d 67.83 (-7.0%), 200d 68.94 (-8.6%); 50d below 200d
Momentum: RSI(14) 38.7 | MACD -1.355 vs signal -1.358 (histogram 0.003)
Returns: 1d -2.0% | 5d +1.2% | 1m -8.5% | 3m +0.2%
52-week range: 60.43 - 81.60 (now 12.4% of the way up)
Volatility: ATR(14) 1.22 (1.9% of price) | annualised 20d 25.1%
Volume: 0.09x the 20-day average
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
Three-year record: +25.2% a year | beta to the market 1.07
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.4% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Shares outstanding: 7.90M | fund size: 498.09M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows no clear directional catalyst. Fund flows are flat (0% change in share count over the past week), macro data are unchanged (yields stable, inflation 3.7% near target, no surprise rate moves), technicals are neutral (RSI 53.3, MACD histogram 0.039, volume 0.23× 20‑day average), and while analyst consensus is strongly bullish (100% buy, +14.3% price target), there is no supporting macro or technical breakout. Hence the overall signal remains neutral.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% over 1 week)
- Macro data unchanged: yields stable, inflation 3.7%, no rate surprise
- Technical indicators neutral: RSI 53.3, MACD histogram 0.039, volume 0.23× 20‑day avg
- Analyst consensus 100% buy with +14.3% price target, but no macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Expanded Tech-Software Sector ETF (IGV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  iShares Expanded Tech-Software Sector ETF (IGV) · -0.16% · 9.32% · 41.02% · 3.73% · -3.19% · 33.36% · 993.40%. Key Events. Baseline. Advanced...
- [Everyone Declared Software Dead in April. This ETF Is Up 41% Since Then.](https://247wallst.com/investing/2026/10/13/everyone-declared-software-dead-in-april-this-etf-is-up-41-since-then/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Software stocks went from apocalypse to market leaders in six months, but the speed of that reversal raises a harder question than most investors are asking...
- [iShares Expanded Tech-Software Sector ETF (IGV)](https://ca.finance.yahoo.com/quote/IGV/options/?date=1792713600&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  View the basic IGV option chain and compare options of iShares Expanded Tech-Software Sector ETF on Yahoo Finance.
- [SoundHound AI Just Dropped 22% in a Month While Enterprise Software Rallied: Is It Time to Sell?](https://247wallst.com/investing/2026/10/13/soundhound-ai-just-dropped-22-in-a-month-while-enterprise-software-rallied-is-it-time-to-sell/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Enterprise software stocks climbed while SoundHound shares collapsed, a split that points to something specific happening inside this company rather than...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 108.76 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 108.15 (+0.6%), 50d 105.66 (+2.9%), 200d 93.74 (+16.0%); 50d above 200d
Momentum: RSI(14) 53.3 | MACD 1.731 vs signal 1.691 (histogram 0.039)
Returns: 1d -2.0% | 5d -1.0% | 1m +3.0% | 3m +16.1%
52-week range: 74.67 - 117.08 (now 80.4% of the way up)
Volatility: ATR(14) 2.41 (2.2% of price) | annualised 20d 21.6%
Volume: 0.23x the 20-day average
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
Three-year record: +16.4% a year | beta to the market 1.22
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
Weighted price target: +14.3% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-13 Wells Fargo: main, Overweight -> Overweight
  - PLTR: 2026-10-09 Barclays: init, ? -> Overweight
  - CRWD: 2026-10-14 BTIG: main, Buy -> Buy
  - MSFT: 2026-10-13 Barclays: main, Overweight -> Overweight
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
Shares outstanding: 12.50M | fund size: 1.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, modest inflows, mixed technicals, thin analyst coverage, moderate fundamentals.

**Main reasons it gave:**
- Share count rose 0.7% (38.4M) over the past week, indicating net inflows
- Price is below 20‑day (47.07), 50‑day (48.50) and 200‑day (49.56) SMAs, showing a downtrend
- Analyst coverage of top 5 holdings (23.7% of fund) is 100% buy with a +32.6% price target
- Fund fundamentals moderate: P/E 21.36, 3‑year return +1.8%/yr, expense ratio 0.61%
- Macro backdrop neutral: no policy surprise, upward‑sloping yield curve, strong dollar, VIX 15.7

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.90 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 47.07 (-0.4%), 50d 48.50 (-3.3%), 200d 49.56 (-5.4%); 50d below 200d
Momentum: RSI(14) 45.5 | MACD -0.570 vs signal -0.653 (histogram 0.083)
Returns: 1d -0.7% | 5d +1.7% | 1m -1.5% | 3m -3.7%
52-week range: 45.42 - 55.29 (now 14.9% of the way up)
Volatility: ATR(14) 0.51 (1.1% of price) | annualised 20d 14.9%
Volume: 0.68x the 20-day average
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
Three-year record: +1.8% a year | beta to the market 0.62
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 23.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.6% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.7% (38.41M) over 7d
Shares outstanding: 126.35M | fund size: 5.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals not decisive, modest analyst bullishness, flat flows, high valuation.

**Main reasons it gave:**
- US Treasury yields unchanged (10‑yr -0.02% w.e., 2‑yr 4.80% vs Fed 4%) – no rate surprise
- ITA price below 20‑d, 50‑d, 200‑d SMAs; RSI 32.4, volume 0.23× 20‑d avg – no decisive technical break
- Analyst coverage of top holdings all buy, weighted price target +29.4% (covers 53.9% of fund)
- Fund flows flat, share count +0.5% over week – minimal demand

<details><summary><b>News</b> — score +0.00</summary>

- [Trump Highlights Ohio Submarine Facility: Potential Ripple Effects on Industrial and Defense ETFs](https://www.tipranks.com/news/catalyst/trump-highlights-ohio-submarine-facility-potential-ripple-effects-on-industrial-and-defense-etfs)  
  <sub>TipRanks, 3 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “Trump's job-creation juggernaut stops in Ohio to unveil...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 204.92 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 209.26 (-2.1%), 50d 224.93 (-8.9%), 200d 230.13 (-11.0%); 50d below 200d
Momentum: RSI(14) 32.4 | MACD -5.163 vs signal -5.662 (histogram 0.500)
Returns: 1d +0.5% | 5d +0.6% | 1m -4.2% | 3m -11.2%
52-week range: 198.23 - 253.22 (now 12.2% of the way up)
Volatility: ATR(14) 3.47 (1.7% of price) | annualised 20d 14.4%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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
Rolled up from the 5 largest holdings, 53.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.4% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-10-09 TD Cowen: main, Buy -> Buy
  - BA: 2026-10-12 Bernstein: main, Outperform -> Outperform
  - HWM: 2026-10-09 TD Cowen: main, Buy -> Buy
  - LMT: 2026-10-09 TD Cowen: main, Hold -> Hold
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
Share count change: 1 week: +0.5% (59.28M) over 7d
Shares outstanding: 58.71M | fund size: 12.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view is offset by flat fund flows, modest fundamentals, and no decisive technical or macro catalyst.

**Main reasons it gave:**
- Flat fund flows (0% change) over the past week
- Analyst consensus strongly bullish (100% buy) covering 51.6% of the fund
- Price below 20‑day SMA (79.64) and RSI 38.9, no decisive technical break
- Macro environment stable: yields unchanged, VIX low, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 79.04 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 79.64 (-0.8%), 50d 82.99 (-4.8%), 200d 81.44 (-3.0%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.873 vs signal -1.107 (histogram 0.234)
Returns: 1d -1.0% | 5d +0.2% | 1m -3.4% | 3m -12.2%
52-week range: 68.14 - 90.01 (now 49.8% of the way up)
Volatility: ATR(14) 1.07 (1.4% of price) | annualised 20d 12.3%
Volume: 0.15x the 20-day average
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
Three-year record: +12.4% a year | beta to the market 1.32
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
Weighted price target: +28.7% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 2.80M | fund size: 221.31M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend but no decisive break, macro data are stable with no surprises, fund flows are positive, fundamentals are solid, and analyst coverage is thin yet bullish. The mixed signals offset each other, leading to a neutral stance.

**Main reasons it gave:**
- Price below 20‑day SMA (70.36) and 50‑day SMA (73.22) – downtrend
- RSI 33.9 indicating oversold but no decisive breakout
- Share count rose 2.5% in the past week (net inflows)
- Analyst coverage thin (5.7% of fund) but bullish: weighted price target +15.2%
- Macro stable: yields modestly up, VIX 15.7, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Chip Stocks Slide as South Korea's KOSPI Plunges, J&J Sinks 6%: Stock Market Today](https://www.benzinga.com/news/26/10/62333961/chip-stocks-slide-korea-kospi-plunges-5-percent-jj-drops-markets-tuesday)  
  <sub>Benzinga, 22 hours ago</sub>  
  Chip stocks sold off after a 5% KOSPI plunge, with Micron and Applied Materials sinking, while J&J fell despite a guidance raise.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 68.49 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 70.36 (-2.7%), 50d 73.22 (-6.5%), 200d 70.69 (-3.1%); 50d above 200d
Momentum: RSI(14) 33.9 | MACD -1.213 vs signal -1.187 (histogram -0.025)
Returns: 1d -0.8% | 5d -0.6% | 1m -7.5% | 3m -12.1%
52-week range: 58.14 - 77.93 (now 52.3% of the way up)
Volatility: ATR(14) 1.23 (1.8% of price) | annualised 20d 14.3%
Volume: 0.49x the 20-day average
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
Three-year record: +22.3% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.9%, Cash 0.1%
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
Weighted price target: +15.2% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-09 RBC Capital: main, Sector Perform -> Sector Perform
  - HWC: 2026-10-05 Barclays: main, Overweight -> Overweight
  - EWBC: 2026-10-14 Cantor Fitzgerald: main, Overweight -> Overweight
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
Share count change: 1 week: +2.5% (89.77M) over 7d
Shares outstanding: 53.98M | fund size: 3.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no clear macro catalyst, technicals bearish but not decisive, modest fund flows, strong analyst buy rating limited to <50% of fund, and geopolitical tension with uncertain impact.

**Main reasons it gave:**
- No policy or rate surprise this week (US Treasury yields stable, Fed target unchanged)
- Technical indicators show bearish trend (price below SMA, RSI 26.4) but no decisive break on volume
- Fund flows flat with +0.4% share count over 7 days, indicating modest demand
- Analyst coverage 90.3% buy for 44.6% of fund weight, weighted price target +21.2% above current price
- Geopolitical tension (explosions in Riyadh) present but impact on Saudi equities unclear

<details><summary><b>News</b> — score +0.00</summary>

- [Residents in Saudi Arabia's capital say they have heard new explosions in Riyadh](https://www.barchart.com/story/news/7467443/residents-in-saudi-arabia-s-capital-say-they-have-heard-new-explosions-in-riyadh)  
  <sub>Barchart.com, 5 hours ago</sub>  
  New explosions have been heard in Riyadh, with blame falling again on Iran-backed Houthi rebels from Yemen.
- [Dow, S&P 500, Nasdaq Futures Mixed Amid Rising Oil Prices Ahead Of CPI Data: BAC, RIVN, SLS, GME Stocks In Focus](https://www.tradingview.com/news/stocktwits:7f7fbe09e094b:0-dow-s-p-500-nasdaq-futures-mixed-amid-rising-oil-prices-ahead-of-cpi-data-bac-rivn-sls-gme-stocks-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures traded mixed late Tuesday as Middle East tensions spiked oil prices ahead of the Consumer Price Index report expected Wednesday.
- [Trump’s Houthi Warning Raises Middle East Oil Risk, Mixed Outlook for Energy and Saudi Stocks](https://www.tipranks.com/news/catalyst/trumps-houthi-warning-raises-middle-east-oil-risk-mixed-outlook-for-energy-and-saudi-stocks)  
  <sub>TipRanks, 22 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “The Houthis are behaving very badly.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 35.15 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 36.57 (-3.9%), 50d 37.59 (-6.5%), 200d 38.11 (-7.8%); 50d below 200d
Momentum: RSI(14) 26.4 | MACD -0.562 vs signal -0.464 (histogram -0.098)
Returns: 1d -1.8% | 5d -4.3% | 1m -6.1% | 3m -4.8%
52-week range: 35.15 - 41.03 (now 0.0% of the way up)
Volatility: ATR(14) 0.34 (1.0% of price) | annualised 20d 13.1%
Volume: 0.54x the 20-day average
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
Three-year record: +1.7% a year | beta to the market 0.19
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 44.6% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.2% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: +0.4% (2.19M) over 7d
Shares outstanding: 16.29M | fund size: 572.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst coverage is offset by net outflows and bearish technical momentum, with no material macro surprise.

**Main reasons it gave:**
- Fund flows show net outflow of -2.2% (130.41M) over the past week
- Analyst coverage of 32.3% of fund with 100% buy rating and +54.7% price target
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs and RSI 40, indicating bearish momentum
- Macro environment: modest rise in US Treasury yields, dollar up, VIX low, no major data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 17 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 51.45 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 52.43 (-1.9%), 50d 53.80 (-4.4%), 200d 56.47 (-8.9%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -0.524 vs signal -0.548 (histogram 0.025)
Returns: 1d -1.3% | 5d -0.4% | 1m -2.8% | 3m -5.0%
52-week range: 50.48 - 65.59 (now 6.4% of the way up)
Volatility: ATR(14) 0.66 (1.3% of price) | annualised 20d 18.5%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.39 | P/B 1.33 | P/S 1.31 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +9.0% a year | beta to the market 0.45
Cost and size: expense ratio 0.59% | net assets 5.99B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Tencent Holdings Ltd 13.8%, Alibaba Group Holding Ltd Ordinary Shares 9.3%, China Construction Bank Corp Class H 4.3%, Industrial And Commercial Bank Of China Ltd Class H 2.6%, Xiaomi Corp Class B 2.2%
Sector mix: Consumer cyclical 22.5%, Financial services 21.0%, Communication services 18.1%, Technology 11.6%
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
Rolled up from the 5 largest holdings, 32.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.42 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +54.7% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
Recent rating changes among them: none reported
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
Share count change: 1 week: -2.2% (-130.41M) over 7d
Shares outstanding: 113.66M | fund size: 5.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, flat flows, bullish analyst view not material

**Main reasons it gave:**
- SMH on six‑day losing streak, longest since May 2025
- Technicals: price below 20‑day SMA (-4.4%) and RSI 42, MACD below signal
- Fund flows flat (share count +0.0% over 1 week) indicating no net demand
- Macro: no policy surprise; yields stable, inflation 3.7% near target
- Analyst view: 100% buy rating, +41.3% price target but not a macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (SMH) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/SMH/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  VanEck Semiconductor ETF (SMH) · -7.02% · 3.45% · 32.66% · 61.88% · 73.10% · 365.27% · 1,106.40%. Key Events. Baseline. Advanced Chart. Loading chart for SMH.
- [You Bought a Semiconductor Fund. On $500,000, $87,743 of It Is NVIDIA](https://247wallst.com/investing/etf/2026/10/13/you-bought-a-semiconductor-fund-on-500000-87743-of-it-is-nvidia/)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  A single semiconductor ETF sounds like a spread bet across dozens of chip companies, but the math inside one popular fund tells a very different story about...
- [Semiconductors on track for their longest losing streak since May 2025 (SMH:NASDAQ)](https://seekingalpha.com/news/4652582-semiconductors-on-track-for-their-longest-losing-streak-since-may-2025)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  The VanEck Semiconductor ETF (SMH) has fallen for six consecutive days and is on track for its longest losing streak since May 2025, with the fund down over...
- [(10/14/26) SOXX: How Should You Trade Chip Stocks After Recent Thrashing?](https://www.moneyshow.com/articles/tradingidea-65533/soxx-how-should-you-trade-chip-stocks-after-recent-thrashing/)  
  <sub>www.moneyshow.com, 10 hours ago</sub>  
  Was Monday a shot across the bow for semiconductor stocks prior to earnings season? If so, what do the sellers know? The iShares Semiconductor ETF (SOXX)...
- [Nearly 18% of a popular semiconductor ETF is invested in NVIDIA alone, revealing high concentration risk.](https://pluang.com/en/news-feed/anda-memiliki-fund-semikonduktor-dengan-porsi-besar-di-nvidia)  
  <sub>Pluang, 17 hours ago</sub>  
  The VanEck Semiconductor ETF (SMH) holds about 17.55% of its portfolio in NVIDIA, meaning nearly $88000 of a $500000 investment is tied to one company.
- [Michael Burry Shifts Bearish Bets To Nasdaq, Semiconductor ETF Puts — Sees Market Top Within 9 Months](https://stocktwits.com/news-articles/markets/equity/michael-burry-shifts-bearish-bets-to-nasdaq-semiconductor-etf-puts-sees-market-top-within-9-months/cZxIPRTRBF8)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Burry's Nasdaq-100 puts expire in April 2027, while his SMH options run through June 2027. The investor continues to hold long-dated bearish bets on Oracle...
- [How Thematic ETFs Help Investors Meet the AI Moment](https://etfdb.com/equity-etf-content-hub/how-thematic-etfs-help-investors-meet-the-ai-moment/)  
  <sub>ETF Database, 19 hours ago</sub>  
  The recent Nasdaq Vettafi summit on asset allocation saw issuer leaders talk thematic ETFs, AI, and leveraged ETFs.
- [Forget NVIDIA: Jim Cramer Says US Chip Stocks Are 'Joined at the Hip' With SK hynix](https://www.tradingview.com/news/benzinga:94cd2fad1094b:0-forget-nvidia-jim-cramer-says-us-chip-stocks-are-joined-at-the-hip-with-sk-hynix/)  
  <sub>TradingView, 5 hours ago</sub>  
  SK hynix Inc. NASDAQ:SKHY remains at the center of the global memory-chip selloff as investors weigh growing competition from China against tight supply,...
- [S&P 500 Ends Flat, While Nasdaq Drops As Memory Chipmakers Sell Off — BAC, GME, SPCX, ARM, QCOM In Focus](https://www.tradingview.com/news/stocktwits:3d90db3e7094b:0-s-p-500-ends-flat-while-nasdaq-drops-as-memory-chipmakers-sell-off-bac-gme-spcx-arm-qcom-in-focus/)  
  <sub>TradingView, 15 hours ago</sub>  
  The S&P 500 ended flat while the Nasdaq 100 and the Dow Jones fell on Tuesday, pulled down by weakness in memory chip stocks and a mixed set of banking...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 576.85 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 603.40 (-4.4%), 50d 580.12 (-0.6%), 200d 509.55 (+13.2%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD 5.531 vs signal 10.621 (histogram -5.090)
Returns: 1d -1.9% | 5d -7.7% | 1m +6.4% | 3m +1.4%
52-week range: 325.10 - 668.91 (now 73.2% of the way up)
Volatility: ATR(14) 14.89 (2.6% of price) | annualised 20d 28.2%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Technology
What it holds: P/E 32.50 | P/B 11.65 | P/S 13.32 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +57.9% a year | beta to the market 2.00
Cost and size: expense ratio 0.35% | net assets 74.88B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 19.3%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.3%, Advanced Micro Devices Inc 5.5%, Broadcom Inc 5.3%, Micron Technology Inc 4.9%
Sector mix: Technology 100.0%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.3% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-10-06 Barclays: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 11.67M | fund size: 6.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, technicals show no decisive break, analyst coverage limited despite bullish rating.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicate no net demand
- Technicals show price below 20d, 50d, 200d SMAs and RSI 32.5, but volume is low (0.18x avg) and no decisive break
- No macro surprise: Treasury yields stable and inflation 3.7% near expectations
- Analyst coverage only 43.2% of fund, despite 100% buy rating and +24.8% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.70 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 35.29 (-4.5%), 50d 37.91 (-11.1%), 200d 39.29 (-14.2%); 50d below 200d
Momentum: RSI(14) 32.5 | MACD -1.274 vs signal -1.266 (histogram -0.008)
Returns: 1d -1.2% | 5d -0.4% | 1m -13.0% | 3m -14.4%
52-week range: 31.90 - 43.74 (now 15.2% of the way up)
Volatility: ATR(14) 0.61 (1.8% of price) | annualised 20d 26.9%
Volume: 0.18x the 20-day average
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
Three-year record: -1.8% a year | beta to the market 0.61
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

<details><summary><b>What analysts and big funds say</b> — score +0.66</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.66</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.8% above the current prices
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
Shares outstanding: 15.65M | fund size: 527.41M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro catalyst, flat fund flows, mixed technicals, and modest analyst optimism offset by high valuation and rate‑sensitive fundamentals.

**Main reasons it gave:**
- Flat fund flows (0.0% change over 1 week)
- Analyst consensus 100% buy with weighted price target +18.4% above current price
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 40 indicating slight oversold
- US Treasury yields high (2‑yr 4.80% above Fed target) indicating continued rate‑hike expectations

<details><summary><b>News</b> — score +0.00</summary>

- [3 Overlooked Vanguard ETFs with 19%+ Upside](https://www.tipranks.com/news/3-overlooked-vanguard-etfs-with-19-upside)  
  <sub>TipRanks, 23 hours ago</sub>  
  Vanguard ETFs are often known for their low costs and long-term stability, but not all of them get the attention they deserve. Some lesser-known Vanguard...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 90.13 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 90.88 (-0.8%), 50d 94.54 (-4.7%), 200d 94.42 (-4.5%); 50d above 200d
Momentum: RSI(14) 40.0 | MACD -1.245 vs signal -1.544 (histogram 0.299)
Returns: 1d -1.1% | 5d +1.6% | 1m -4.2% | 3m -9.9%
52-week range: 87.00 - 100.95 (now 22.4% of the way up)
Volatility: ATR(14) 1.22 (1.4% of price) | annualised 20d 14.5%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.8%
Three-year record: +10.7% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 66.42B
What it is made of: Stocks 99.1%, Cash 0.7%, Other 0.2%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 8.7%, Prologis Inc 6.9%, Equinix Inc 5.5%, American Tower Corp 4.3%
Sector mix: Real estate 99.4%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-10-13 Scotiabank: up, Sector Perform -> Sector Outperform
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-09-30 Barclays: main, Overweight -> Overweight
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
Shares outstanding: 370.18M | fund size: 33.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical indicators show slight bearish momentum (RSI 38.1, MACD -2.587 vs signal -1.877)
- Fundamentals indicate low valuation (P/B 0.21, P/S 0.12) and strong 3-year record (+30.4% per year)
- Fund flows are flat with a small net creation (+0.4% week over week)
- Analyst view is thin (9.2% weight) with mixed signals (61% buy, price target -9% below current price)

<details><summary><b>News</b> — score +0.00</summary>

- [Split in the Market Widens as Bank Earnings Hit](https://realmoney.thestreet.com/market-commentary/split-in-the-market-widens-as-bank-earnings-hit)  
  <sub>RealMoney Pro, 18 hours ago</sub>  
  New lows topped 500 and more than 60% of stocks are below their 200-day averages, while the mega caps hit another record.
- [Better Buy: Fidelity Health Care ETF (FHLC) or iShares Biotechnology ETF (IBB)?](https://finance.yahoo.com/healthcare/articles/better-buy-fidelity-health-care-201337762.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Fidelity MSCI Health Care Index ETF (NYSEMKT:FHLC) provides broad, low-cost exposure to the healthcare sector, whereas iShares Biotechnology ETF...
- [From Laggard to Leader: The Surprising Comeback of Healthcare](https://etfdb.com/equity-etf-content-hub/laggard-leader-surprising-comeback-healthcare/)  
  <sub>ETF Database, 24 hours ago</sub>  
  Healthcare stocks have finally stepped back into the spotlight. After spending much of the past several years in the shadow of technology and AI, the sector...
- [This Biopharma Stock Offers Compelling Upside After a Pullback](https://www.barrons.com/articles/neurocrine-biopharma-stock-offers-compelling-upside-after-pullback-d3231dd3)  
  <sub>Barron's, 15 hours ago</sub>  
  stock has pulled back from its all-time high, creating an opportunity for investors to buy the commercial-stage biopharma ahead of its next phase of growth.
- [Why Did OPEN, NKE, CCL Stocks Crash To 52-Week Lows Today?](https://stocktwits.com/news-articles/markets/equity/why-did-open-nke-ccl-stocks-crash-to-52-week-lows-today/cZtY2PcRB2d)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Housing weakness, a prolonged athleticwear turnaround, and rising cruise fuel costs weighed on investor sentiment.
- [AAPL Stock Retreats From All-Time High: Research Firm Says Apple Could Sell 6M iPhone Duos This Year](https://stocktwits.com/news-articles/markets/equity/aapl-stock-retreats-from-all-time-high-research-firm-says-apple-could-sell-6-m-i-phone-duos-this-year/cZMnDDFRBWu)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Apple's foldable bet, leadership transition, and expanding payments ecosystem are giving investors fresh factors to watch.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 147.54 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 154.38 (-4.4%), 50d 158.25 (-6.8%), 200d 139.92 (+5.4%); 50d above 200d
Momentum: RSI(14) 38.1 | MACD -2.587 vs signal -1.877 (histogram -0.710)
Returns: 1d +0.5% | 5d -1.8% | 1m -4.2% | 3m -2.9%
52-week range: 105.12 - 169.55 (now 65.8% of the way up)
Volatility: ATR(14) 4.26 (2.9% of price) | annualised 20d 30.6%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.21 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +30.4% a year | beta to the market 1.09
Cost and size: expense ratio 0.35% | net assets 10.36B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Twist Bioscience Corp 2.2%, Moderna Inc 2.0%, Natera Inc 1.8%, Iovance Biotherapeutics Inc 1.6%, Amgen Inc 1.5%
Sector mix: Healthcare 99.3%, Financial services 0.7%
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
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -9.0% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-13 TD Cowen: main, Buy -> Buy
  - MRNA: 2026-10-07 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - NTRA: 2026-10-13 Morgan Stanley: main, Overweight -> Overweight
  - IOVA: 2026-10-13 Barclays: main, Overweight -> Overweight
  - AMGN: 2026-10-13 Guggenheim: main, Neutral -> Neutral
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
Share count change: 1 week: +0.4% (44.38M) over 7d
Shares outstanding: 67.38M | fund size: 9.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: positive fund inflows and bullish analyst coverage on top holdings are offset by bearish technicals and a neutral macro backdrop. No material policy surprise or decisive technical breakout is present, so the overall stance remains neutral.

**Main reasons it gave:**
- Fund flows: share count increased 2% over the past week, indicating net inflows
- Analyst coverage: 100% buy rating on top holdings, weighted price target +21.1% above current prices
- Technicals: price 12.6% below 200‑day SMA, RSI 32.9 (oversold), volume 0.30x 20‑day average
- Macro: upward‑sloping yield curve, no rate or policy surprise, VIX low at 15.7

<details><summary><b>News</b> — score +0.00</summary>

- [Trading (XHB) With Integrated Risk Controls (XHB:CA)](https://news.stocktradersdaily.com/canada/trading-xhb-with-integrated-risk-controls_20261013_8d834c)  
  <sub>Stock Traders Daily, 23 hours ago</sub>  
  Recent Articles on iShares Canadian HYBrid Corporate Bond Index ETF (XHB:CA). (XHB) Proactive Strategies October 10, 2026, 05:39 PM; (XHB) Technical...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 92.41 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 96.30 (-4.0%), 50d 101.25 (-8.7%), 200d 105.74 (-12.6%); 50d below 200d
Momentum: RSI(14) 32.9 | MACD -1.892 vs signal -1.815 (histogram -0.077)
Returns: 1d -2.3% | 5d -2.6% | 1m -5.5% | 3m -16.6%
52-week range: 92.41 - 121.36 (now 0.0% of the way up)
Volatility: ATR(14) 2.10 (2.3% of price) | annualised 20d 20.9%
Volume: 0.30x the 20-day average
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
Three-year record: +8.9% a year | beta to the market 1.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.1% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-08-07 TD Cowen: main, Buy -> Buy
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-09-30 Oppenheimer: init, ? -> Perform
  - JCI: 2026-10-14 RBC Capital: main, Sector Perform -> Sector Perform
  - W: 2026-10-08 Baird: main, Neutral -> Neutral
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
Share count change: 1 week: +2.0% (27.74M) over 7d
Shares outstanding: 15.09M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals modestly bearish, analyst view bullish but limited coverage, flows flat.

**Main reasons it gave:**
- Flat fund flows (0% net change) indicating no demand shift
- Analyst coverage limited to 34.1% of fund with all buy ratings and +15.3% price target
- Technicals show price below 20‑day SMA, RSI 43.4, low volume (0.22x 20‑day avg)
- Macro data stable: yields unchanged, VIX low (15.7), no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 49.37 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 49.54 (-0.3%), 50d 51.23 (-3.6%), 200d 50.81 (-2.8%); 50d above 200d
Momentum: RSI(14) 43.4 | MACD -0.483 vs signal -0.601 (histogram 0.118)
Returns: 1d -0.7% | 5d +0.8% | 1m -2.7% | 3m -3.0%
52-week range: 42.23 - 53.67 (now 62.4% of the way up)
Volatility: ATR(14) 0.70 (1.4% of price) | annualised 20d 14.0%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Natural Resources
What it holds: P/E 22.69 | P/B 2.70 | P/S 1.78 | 3y earnings growth n/a
Yield: 1.8%
Three-year record: +10.3% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 7.78B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Linde PLC 12.2%, Newmont Corp 6.8%, Freeport-McMoRan Inc 5.6%, Ecolab Inc 4.7%, Sherwin-Williams Co 4.7%
Sector mix: Basic materials 83.2%, Consumer cyclical 16.8%
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
Rolled up from the 5 largest holdings, 34.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.3% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals weak, fund flows flat, but analyst view bullish.

**Main reasons it gave:**
- Fund flows flat: -0.1% share count change over 7 days
- Technical indicators weak: price below 20‑day, 50‑day, 200‑day SMAs; RSI 48.3; MACD negative
- Macro environment unchanged: yields stable, no rate surprise, VIX low at 15.7
- Analyst view bullish: 90.6% buy rating, weighted price target +13.4% above current

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  State Street Communication Services Select Sector SPDR ETF (XLC) · 0.56% · -0.28% · -2.21% · -5.08% · -1.37% · 41.43% · 125.92%. Key...
- [Alphabet, Netflix among communication services stocks with top profitability grades (XLC:NYSEARCA)](https://seekingalpha.com/news/4652771-alphabet-netflix-among-communication-services-stocks-with-top-profitability-grades)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Q3 earnings season: 10 communication services stocks with A+ profitability grades (APP, CHTR, CMCSA, DIS, GOOGL, META, NFLX, T, TMUS, VZ)—read now.
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [Skydance Falls 16% as Shares Begin Trading Without Warrant Entitlement; Netflix and Disney Tick Up](https://247wallst.com/investing/2026/10/14/skydance-falls-16-as-shares-begin-trading-without-warrant-entitlement-netflix-and-disney-tick-up/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  SKYD fell 16% as shares went ex-warrant, with 470 million warrants at a $12 strike now trading separately under SKYD WS on the NYSE.
- [Antelope Enterprise Holdings Stock Surges 150% After Hours - State Street Communication Services Select S](https://www.benzinga.com/markets/equities/26/10/62344221/antelope-enterprise-holdings-aehl-stock-surges-after-hours)  
  <sub>Benzinga, 11 hours ago</sub>  
  Antelope Enterprise Holdings shares surged 150.88% in after-hours trading Tuesday to $21.45 after closing down 7.77% during regular session.
- [How to Buy AT&T Stock (NYSE:T) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-att-stock/)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  One of North America's largest telecom providers, AT&T is working to reduce costs and repay debt to boost income, attracting investors with a high-yielding...
- [Cyclicals Lead Sectors In Tuesday Trading As Health Care Trails](https://www.benzinga.com/etfs/sector-etfs/26/10/62328756/cyclicals-lead-sectors-in-tuesday-trading-as-health-care-trails)  
  <sub>Benzinga, 24 hours ago</sub>  
  Four sectors are higher and seven are lower in Tuesday's regular session, with cyclical sectors holding two of the top three positions.
- [Chip Stocks Slide as South Korea's KOSPI Plunges, J&J Sinks 6%: Stock Market Today](https://www.tradingview.com/news/benzinga:46d40e769094b:0-chip-stocks-slide-as-south-korea-s-kospi-plunges-j-j-sinks-6-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks slipped by midday Tuesday as a chip-sector rout — sparked by a 5% plunge in South Korea's KOSPI — offset gains in banks and energy,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 111.28 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 111.84 (-0.5%), 50d 111.90 (-0.6%), 200d 113.57 (-2.0%); 50d below 200d
Momentum: RSI(14) 48.3 | MACD -0.181 vs signal -0.151 (histogram -0.030)
Returns: 1d -0.9% | 5d +0.0% | 1m -2.4% | 3m -1.2%
52-week range: 105.38 - 120.08 (now 40.1% of the way up)
Volatility: ATR(14) 1.59 (1.4% of price) | annualised 20d 19.7%
Volume: 0.25x the 20-day average
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
Three-year record: +19.4% a year | beta to the market 0.85
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 52.5% of the fund by weight
Ratings by weight: buy 90.6% | hold 9.4% | sell 0.0% (mean 1.52 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.4% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2026-10-13 Pivotal Research: main, Buy -> Buy
  - GOOGL: 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOG: 2026-10-08 TD Cowen: main, Buy -> Buy
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
Share count change: 1 week: -0.1% (-19.99M) over 7d
Shares outstanding: 204.10M | fund size: 22.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bullish analyst coverage is offset by bearish EIA oil‑price outlook, mixed inventory signals and flat fund flows; technicals show a strong uptrend but RSI is near overbought and volume is low, with no macro surprise.

**Main reasons it gave:**
- Analyst coverage 58.2% of fund, 100% buy rating, weighted price target +0.3% (bullish)
- EIA forecast WTI crude price falling from $100 now to $86 in six months (bearish)
- Technicals: price above 20‑, 50‑ and 200‑day SMAs, RSI 69.6 (near overbought), volume 0.27× 20‑day avg (caution)
- Fund flows flat (share count +0.0% over 7 days), indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Edge MSCI World Minimum Volatility Advanced UCITS ETF USD (Acc) (MVEW.F)](https://ca.finance.yahoo.com/quote/MVEW.F/news/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Get the latest iShares Edge MSCI World Minimum Volatility Advanced UCITS ETF USD (Acc) (MVEW.F) stock news and headlines to help you in your trading and...
- [XLE Hits Another All-Time High as Energy and India Lead While Healthcare and Semis Face Distribution by John Salama, CMT](https://www.barchart.com/story/news/6978433/xle-hits-another-all-time-high-as-energy-and-india-lead-while-healthcare-and-semis-face-distribution-by-john-salama-cmt)  
  <sub>Barchart.com, 20 hours ago</sub>  
  ETF Market Strategist & Derivatives Trader | CMT | Author, Physical Over Digital Alpha | Featured Author, Barchart | 500+ Institutional Subscribers.
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [Cyclicals Lead Sectors In Tuesday Trading As Health Care Trails](https://www.benzinga.com/etfs/sector-etfs/26/10/62328756/cyclicals-lead-sectors-in-tuesday-trading-as-health-care-trails)  
  <sub>Benzinga, 24 hours ago</sub>  
  Four sectors are higher and seven are lower in Tuesday's regular session, with cyclical sectors holding two of the top three positions.
- [Sector Update: Energy](https://ca.finance.yahoo.com/news/sector-energy-172941161.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Energy stocks were higher Tuesday afternoon, with the NYSE Energy Sector Index rising 1.3% and the State Street Energy Select Sector SPDR ETF (XLE) adding...
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-lower-us-172017687.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.5%.
- [State Street Investment Management Builds on Nearly 30 Years of Sector ETF Leadership with New Market Sector ETFs](https://www.businesswire.com/news/home/20261014723784/en/State-Street-Investment-Management-Builds-on-Nearly-30-Years-of-Sector-ETF-Leadership-with-New-Market-Sector-ETFs)  
  <sub>Business Wire, 2 hours ago</sub>  
  State Street Investment Management today announced the launch of four new State Street® S&P 500® Market Sector SPDR® ETFs, building on the sector ETF...
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Amid September Consumer Inflation Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-132552488.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3% and the actively trad.
- [Sector Update: Energy Stocks Gain Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-gain-afternoon-194954452.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks were higher late Tuesday afternoon, with the NYSE Energy Sector Index rising 1.6% and the State Street Energy Select Sector SPDR ETF (XLE)...
- [Sector Update: Energy Stocks Gain Tuesday Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-gain-tuesday-180102496.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Energy stocks rose Tuesday afternoon with the NYSE Energy Sector Index gaining 1.3% and the State Street Energy Select Sector SPDR ETF (XLE) adding 1.5%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 67.18 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 63.60 (+5.6%), 50d 63.14 (+6.4%), 200d 57.39 (+17.1%); 50d above 200d
Momentum: RSI(14) 69.6 | MACD 0.905 vs signal 0.451 (histogram 0.454)
Returns: 1d -0.0% | 5d +6.0% | 1m +1.9% | 3m +17.8%
52-week range: 42.64 - 67.20 (now 99.9% of the way up)
Volatility: ATR(14) 1.25 (1.9% of price) | annualised 20d 20.3%
Volume: 0.27x the 20-day average
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.3% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - CVX: 2026-10-12 TD Cowen: main, Hold -> Hold
  - COP: 2026-10-07 Jefferies: main, Buy -> Buy
  - VLO: 2026-10-13 Citigroup: main, Neutral -> Neutral
  - MPC: 2026-10-13 Citigroup: main, Neutral -> Neutral
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
Shares outstanding: 186.42M | fund size: 12.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows no clear catalyst: technicals are weak in the short term (price below 20‑day and 50‑day SMAs), fund flows are flat, macro data are stable with no surprise rate or inflation moves, and sector news is mixed. Analyst coverage is bullish but limited to ~43% of the fund and does not outweigh the neutral macro‑technical backdrop.

**Main reasons it gave:**
- Technical trend: price below 20‑day (54.47) and 50‑day (56.37) SMAs, indicating short‑term weakness
- Fund flows flat over the past week, indicating no net demand for the ETF
- Macro environment: normal upward yield curve (+1.16) and expectations of further rate hikes, but no surprise data
- Mixed sector news: Bank of America penalty and overall financial sector mixed performance

<details><summary><b>News</b> — score +0.00</summary>

- [Bank of America Falls 5% as $1.2B Money Laundering Penalty Drives Earnings Miss; JPMorgan Chase and Wells Fargo Hold Steady](https://247wallst.com/investing/2026/10/14/bank-of-america-falls-5-as-1-2b-money-laundering-penalty-drives-earnings-miss-jpmorgan-chase-and-wells-fargo-hold-steady/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  A $1.2 billion regulatory penalty blindsided investors and snapped a six-quarter earnings streak, but the lending numbers underneath tell a very different...
- [Webcast: Long Live Nuclear: How Extended Reactor Lives Drive Investment Opportunities | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/09/long-live-nuclear-how-extended-reactor-lives-drive-investment-opportunities?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Today's nuclear fleet is poised to operate for 100+ years while generating more power. This creates demand today across the nuclear value chain,...
- [Goldman’s Results Outshone A Mixed Day For Banks](https://finimize.com/content/goldmans-results-outshone-a-mixed-day-for-banks)  
  <sub>Finimize, 20 hours ago</sub>  
  As the IMF lifted its 2026 global growth forecast on AI investment, Goldman beat Q3 estimates while Wells Fargo and JPMorgan delivered a more uneven read.
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Amid September Consumer Inflation Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-132552488.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3% and the actively trad.
- [Sector Update: Financial Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-mixed-afternoon-195728008.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Financial stocks were mixed in late Tuesday afternoon trading with the NYSE Financial Index little c.
- [Sector Update: Financial Stocks Mixed Tuesday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-mixed-tuesday-173854575.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Financial stocks were mixed in Tuesday afternoon trading with the NYSE Financial Index steady and the State Street Financial Select Sector SPDR ETF (XLF)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 54.12 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 54.47 (-0.6%), 50d 56.37 (-4.0%), 200d 53.68 (+0.8%); 50d above 200d
Momentum: RSI(14) 40.3 | MACD -0.542 vs signal -0.694 (histogram 0.152)
Returns: 1d -1.3% | 5d +0.7% | 1m -4.8% | 3m -4.6%
52-week range: 47.81 - 58.56 (now 58.7% of the way up)
Volatility: ATR(14) 0.70 (1.3% of price) | annualised 20d 12.3%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Financial
What it holds: P/E 15.21 | P/B 2.25 | P/S 3.26 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +20.3% a year | beta to the market 0.75
Cost and size: expense ratio 0.08% | net assets 50.97B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Berkshire Hathaway Inc Class B 12.3%, JPMorgan Chase & Co 11.7%, Visa Inc Class A 8.1%, Mastercard Inc Class A 5.9%, Bank of America Corp 4.7%
Sector mix: Financial services 98.2%, Technology 1.6%, Industrials 0.2%
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
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.5% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - JPM: 2026-10-14 Barclays: main, Overweight -> Overweight
  - V: 2026-10-12 Baird: main, Outperform -> Outperform
  - MA: 2026-10-09 Baird: main, Outperform -> Outperform
  - BAC: 2026-10-05 UBS: main, Buy -> Buy
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
Shares outstanding: 883.44M | fund size: 47.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to bearish macro backdrop (inflation above target, expected rate hikes) and technical weakness (price below SMAs, low RSI), offset by a bullish analyst view but flat fund flows indicating no net demand.

**Main reasons it gave:**
- US inflation 3.7% (above target) and market expects ~4 quarter-point rate hikes over next 2 years
- XLI price 166.99 below 20‑day SMA 169.19, 50‑day SMA 174.82, and 200‑day SMA 172.86
- RSI(14) 38.3 indicating bearish momentum
- Fund flows flat: share count change +0.0% over the week

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Amid September Consumer Inflation Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-132552488.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3% and the actively trad.
- [What's Going On With Caterpillar Stock Wednesday?](https://www.benzinga.com/trading-ideas/movers/26/10/62353386/whats-going-on-with-caterpillar-stock-wednesday)  
  <sub>Benzinga, 1 hour ago</sub>  
  Caterpillar Inc. (NYSE:CAT) stock traded lower in Wednesday's premarket session amid recent analyst forecast cuts, a premium valuation, and regulatory...
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [Caterpillar Sinks 5% as Deere Edges Higher: Is the Data Center Power Premium Unwinding?](https://247wallst.com/investing/2026/10/13/caterpillar-sinks-5-as-deere-edges-higher-is-the-data-center-power-premium-unwinding/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  Caterpillar built a hefty valuation on its data center power business, but a single afternoon of trading is stripping that premium away while rivals like...
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [RXO and Proto Labs lead industrials quant picks ahead of Q3 earnings](https://fr.tradingview.com/news/seekingalpha:0c2d1bd03094b:0-rxo-and-proto-labs-lead-industrials-quant-picks-ahead-of-q3-earnings/)  
  <sub>TradingView, 21 hours ago</sub>  
  The State Street Industrial Select Sector SPDR ETF AMEX:XLI fell 9.9% in the third quarter of 2026, reversing its roughly 15% gain in Q2.
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-lower-us-172017687.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.5%.
- [Why State Street’s new sector ETFs could give institutional investors cleaner alpha capture](https://www.pionline.com/asset-management/exchange-traded-funds/pi-state-street-uncapped-market-sector-etfs-tighter-benchmark-tracking/)  
  <sub>Pensions & Investments, 2 hours ago</sub>  
  State Street Investment Management launched four uncapped S&P 500 Market Sector SPDR ETFs designed to give institutional investors more precise sector...
- [Webcast: Long Live Nuclear: How Extended Reactor Lives Drive Investment Opportunities | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/09/long-live-nuclear-how-extended-reactor-lives-drive-investment-opportunities?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Today's nuclear fleet is poised to operate for 100+ years while generating more power. This creates demand today across the nuclear value chain,...
- [ETF boom turns specialized as leveraged and thematic funds shine](https://seekingalpha.com/news/4652613-etf-boom-turns-specialized-as-leveraged-and-thematic-funds-shine)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The U.S. ETF market is shifting toward greater specialization and leverage as product launches accelerate. Nearly 1,100 new ETFs have debuted so far in 2026...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 166.99 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 169.19 (-1.3%), 50d 174.82 (-4.5%), 200d 172.86 (-3.4%); 50d above 200d
Momentum: RSI(14) 38.3 | MACD -1.505 vs signal -1.720 (histogram 0.215)
Returns: 1d -1.0% | 5d -0.5% | 1m -1.1% | 3m -7.3%
52-week range: 147.83 - 186.51 (now 49.5% of the way up)
Volatility: ATR(14) 2.31 (1.4% of price) | annualised 20d 13.0%
Volume: 0.46x the 20-day average
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
Three-year record: +19.8% a year | beta to the market 1.01
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.0% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - GEV: 2026-10-14 Susquehanna: main, Positive -> Positive
  - RTX: 2026-10-09 TD Cowen: main, Buy -> Buy
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
Shares outstanding: 136.63M | fund size: 22.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive break, and flat fund flows suggest no net demand despite bullish analyst consensus.

**Main reasons it gave:**
- Flat weekly fund flows (0% change) – no net demand
- Analyst consensus all buy with +20.9% price target, but no macro catalyst
- Price below 20‑day SMA and MACD negative – no decisive technical break
- Macro data (inflation 3.7%, unemployment 4.2%) in line with expectations, no surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Why State Street’s new sector ETFs could give institutional investors cleaner alpha capture](https://www.pionline.com/asset-management/exchange-traded-funds/pi-state-street-uncapped-market-sector-etfs-tighter-benchmark-tracking/)  
  <sub>Pensions & Investments, 2 hours ago</sub>  
  State Street Investment Management launched four uncapped S&P 500 Market Sector SPDR ETFs designed to give institutional investors more precise sector...
- [Sector Update: Tech](https://finance.yahoo.com/markets/stocks/articles/sector-tech-192358302.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Tech stocks were lower late Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) decreasing 0.2% and the State Street SPDR S&P...
- [ETF boom turns specialized as leveraged and thematic funds shine](https://seekingalpha.com/news/4652613-etf-boom-turns-specialized-as-leveraged-and-thematic-funds-shine)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The U.S. ETF market is shifting toward greater specialization and leverage as product launches accelerate. Nearly 1,100 new ETFs have debuted so far in 2026...
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [US stocks mixed as S&P 500 rises nearly 1% whil...](https://pluang.com/en/news-feed/komentar-mingguan-valuengine-dengan-catatan-strategi)  
  <sub>Pluang, 23 hours ago</sub>  
  U.S. equity markets showed mixed performance this week, with the S&P 500 ETF rising by 0.99% driven by gains in value, defensive, and cyclical sectors.
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://ca.finance.yahoo.com/news/exchange-traded-funds-lower-us-172017687.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.5%.
- [State Street Investment Management Builds on Nearly 30 Years of Sector ETF Leadership with New Market Sector ETFs](https://www.businesswire.com/news/home/20261014723784/en/State-Street-Investment-Management-Builds-on-Nearly-30-Years-of-Sector-ETF-Leadership-with-New-Market-Sector-ETFs)  
  <sub>Business Wire, 2 hours ago</sub>  
  State Street Investment Management today announced the launch of four new State Street® S&P 500® Market Sector SPDR® ETFs, building on the sector ETF...
- [S&P 500, Nasdaq End Higher On Support From Strong Tech Gains Led By Nvidia, Dow Hits Record Highs — MSFT, NVDA, LMT, AVGO, SPCX In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-end-higher-on-support-from-strong-tech-gains-led-by-nvidia-dow-hits-record-highs-msft-nvda-lmt-avgo-spcx-in-focus/cZm1YfaR7lU)  
  <sub>Stocktwits, 22 hours ago</sub>  
  U.S. stock indices ended higher on Monday, with the Dow Jones index hitting record highs as technology stocks reversed course from previous week's declines.
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Amid September Consumer Inflation Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-132552488.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3% and the actively trad.
- [Sector Update: Tech Stocks Softer Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-tech-stocks-softer-afternoon-194135391.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Tech stocks were lower late Tuesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) decreasing 0.2% and the State Street SPDR S&P...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 193.68 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 196.23 (-1.3%), 50d 189.97 (+2.0%), 200d 167.12 (+15.9%); 50d above 200d
Momentum: RSI(14) 49.0 | MACD 2.374 vs signal 3.084 (histogram -0.710)
Returns: 1d -1.3% | 5d -3.8% | 1m +5.4% | 3m +9.1%
52-week range: 127.50 - 202.00 (now 88.8% of the way up)
Volatility: ATR(14) 2.99 (1.5% of price) | annualised 20d 17.9%
Volume: 0.36x the 20-day average
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
Three-year record: +32.7% a year | beta to the market 1.45
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.9% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - MSFT: 2026-10-13 Barclays: main, Overweight -> Overweight
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 272.06M | fund size: 52.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% over 7d)
- Technical indicators modestly bullish (price above 20d, 50d, 200d SMAs, RSI 61.4) but low volume (0.32x 20d avg) and no decisive break
- Macro environment stable: yields unchanged, inflation 3.7% in line, no policy surprise
- Analyst view strongly bullish (100% buy, mean rating 1.81) but covers only 41.8% of fund

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Amid September Consumer Inflation Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-132552488.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3% and the actively trad.
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 2.20% · 2.84% · 15.92% · 11.45% · 21.20% · 35.48% · 595.29%. Key Events. Baseline. Advanced Chart.
- [UnitedHealth Raises Guidance: What It Means for XLV and Other Healthcare ETFs](https://www.tradingview.com/news/benzinga:4b8d97ec4094b:0-unitedhealth-raises-guidance-what-it-means-for-xlv-and-other-healthcare-etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  UnitedHealth Group Inc. NYSE:UNH delivered a stronger-than-expected third-quarter earnings report and raised its full-year 2026 outlook,...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-195559592.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) easing 0.1% and the State Street...
- [Sector Update: Consumer](https://finance.yahoo.com/healthcare/articles/sector-consumer-193002990.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) easing 0.1% and the State Street...
- [State Street Investment Management Builds on Nearly 30 Years of Sector ETF Leadership with New Market Sector ETFs](https://www.businesswire.com/news/home/20261014723784/en/State-Street-Investment-Management-Builds-on-Nearly-30-Years-of-Sector-ETF-Leadership-with-New-Market-Sector-ETFs)  
  <sub>Business Wire, 2 hours ago</sub>  
  State Street Investment Management today announced the launch of four new State Street® S&P 500® Market Sector SPDR® ETFs, building on the sector ETF...
- [From Laggard to Leader: The Surprising Comeback of Healthcare](https://etfdb.com/equity-etf-content-hub/laggard-leader-surprising-comeback-healthcare/)  
  <sub>ETF Database, 24 hours ago</sub>  
  Healthcare stocks have finally stepped back into the spotlight. After spending much of the past several years in the shadow of technology and AI, the sector...
- [IHF: A Concentrated And Volatile ETF In Healthcare Providers (NYSEARCA:IHF)](https://seekingalpha.com/article/4954023-ihf-a-concentrated-and-volatile-etf-in-healthcare-providers)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Explore IHF: cap-weighted U.S. healthcare providers with high liquidity and value vs XLV/SPY—but higher volatility and past underperformance.
- [Sector Update: Consumer Stocks Mixed in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-174929277.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) down 0.1% and the State Street Consumer...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 84.79 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 82.38 (+2.9%), 50d 83.99 (+1.0%), 200d 83.91 (+1.1%); 50d above 200d
Momentum: RSI(14) 61.4 | MACD 0.031 vs signal -0.454 (histogram 0.485)
Returns: 1d +0.7% | 5d +3.8% | 1m +1.3% | 3m -1.2%
52-week range: 75.60 - 90.01 (now 63.8% of the way up)
Volatility: ATR(14) 0.99 (1.2% of price) | annualised 20d 13.8%
Volume: 0.32x the 20-day average
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
Three-year record: +11.4% a year | beta to the market 0.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.0% above the current prices
Holdings read: WMT, COST, PG, KO, PM
Recent rating changes among them:
  - WMT: 2026-09-29 Mizuho: main, Outperform -> Outperform
  - COST: 2026-10-09 RBC Capital: reit, Sector Perform -> Sector Perform
  - PG: 2026-10-06 Evercore ISI Group: up, In-Line -> Outperform
  - KO: 2026-10-05 Wells Fargo: main, Overweight -> Overweight
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
Shares outstanding: 210.17M | fund size: 17.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, mixed technicals, flat fund flows, and limited analyst coverage.

**Main reasons it gave:**
- Flat fund flows: share count unchanged over the week
- Technicals show price above 20‑day SMA but below 50‑day and 200‑day SMA, low volume
- Macro data: no surprise in inflation, unemployment, or Fed policy; yields unchanged
- Analyst coverage limited to 39.5% of fund, though 80.6% of covered holdings are rated buy

<details><summary><b>News</b> — score +0.00</summary>

- [UTES: Utilities May Soon Outgrow Their Bond-Proxy Label (NYSEARCA:UTES)](https://seekingalpha.com/article/4954091-utes-utilities-may-soon-outgrow-their-bond-proxy-label)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The Virtus Reaves Utilities ETF is initiated with a buy rating, capitalizing on utilities' transformation from defensive to growth amid AI-driven demand.
- [The Texas Stock Exchange Has Its First New ETF. Its Power Bet Also Sells Calls](https://247wallst.com/investing/etf/2026/10/13/the-texas-stock-exchange-has-its-first-new-etf-its-power-bet-also-sells-calls/)  
  <sub>24/7 Wall St., 16 hours ago</sub>  
  Westwood just debuted the first new ETF on the Texas Stock Exchange, betting on a surge in power demand from AI and data centers. But the fund's income...
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [Duke Energy, Southern Company lead utilities stocks with high profitability grades (XLU:NYSEARCA)](https://seekingalpha.com/news/4652774-duke-energy-southern-company-lead-utilities-stocks-with-high-profitability-grades)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Q3 earnings season: 10 top utility stocks with A+/A profitability grades (DUK, SO, CWEN, EIX & more).
- [TCAF: Recent Gains Are Encouraging, But Valuation Remains A Concern](https://seekingalpha.com/article/4953950-tcaf-recent-gains-encouraging-valuation-remains-a-concern)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  Summary. T. Rowe Price Capital Appreciation Equity ETF retains a 'hold' rating due to elevated valuations versus growth and lack of clear outperformance...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 41.33 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 40.51 (+2.0%), 50d 42.07 (-1.8%), 200d 44.32 (-6.7%); 50d below 200d
Momentum: RSI(14) 51.4 | MACD -0.164 vs signal -0.475 (histogram 0.311)
Returns: 1d -1.3% | 5d +0.4% | 1m +0.0% | 3m -9.1%
52-week range: 39.25 - 47.73 (now 24.6% of the way up)
Volatility: ATR(14) 0.63 (1.5% of price) | annualised 20d 17.7%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.7% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-06 Mizuho: main, Neutral -> Neutral
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
Shares outstanding: 163.27M | fund size: 6.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week
- Technical uptrend: price above 20d, 50d, 200d SMAs with positive momentum but low volume
- Macro unchanged: no rate or data surprise this week
- Analyst ratings: 100% buy for 44.3% of fund, price target +10.1% above current

<details><summary><b>News</b> — score +0.00</summary>

- [Bet on These Healthcare ETFs to Benefit From the Aging US Population](https://finance.yahoo.com/healthcare/articles/bet-healthcare-etfs-benefit-aging-120900374.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  The U.S. aging population is growing at an unprecedented pace, fundamentally reshaping the healthcare investment landscape. According to the National...
- [UnitedHealth Raises Guidance: What It Means for XLV and Other Healthcare ETFs](https://www.tradingview.com/news/benzinga:4b8d97ec4094b:0-unitedhealth-raises-guidance-what-it-means-for-xlv-and-other-healthcare-etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  UnitedHealth Group Inc. NYSE:UNH delivered a stronger-than-expected third-quarter earnings report and raised its full-year 2026 outlook,...
- [From Laggard to Leader: The Surprising Comeback of Healthcare](https://etfdb.com/equity-etf-content-hub/laggard-leader-surprising-comeback-healthcare/)  
  <sub>ETF Database, 24 hours ago</sub>  
  Healthcare stocks have finally stepped back into the spotlight. After spending much of the past several years in the shadow of technology and AI, the sector...
- [FTC wants Martin Shkreli held in contempt for trading pharma stocks](https://seekingalpha.com/news/4652597-ftc-wants-martin-shkreli-held-in-contempt-trading-pharma-stocks)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The Federal Trade Commission has asked a federal judge to hold in contempt the former CEO of Retrophin and Turing Pharmaceuticals (now renamed Vyera...
- [Sector Update: Healthcare Stocks Fall Late Afternoon](https://ca.finance.yahoo.com/news/sector-healthcare-stocks-fall-afternoon-194753597.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Healthcare stocks were lower late Tuesday afternoon, with the NYSE Healthcare Index and the State Street Health Care Select Sector SPDR ETF (XLV) each...
- [Johnson & Johnson Drops 5% as One-Time Charges Overshadow Raised Full-Year Outlook; Eli Lilly Dips, Pfizer Sits Out the Selloff](https://247wallst.com/investing/2026/10/13/johnson-johnson-drops-5-as-one-time-charges-overshadow-raised-full-year-outlook-eli-lilly-dips-pfizer-sits-out-the-selloff/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  A raised full-year outlook failed to cushion Johnson and Johnson shares from a sharp selloff, as a single line item in its earnings release sent reported...
- [J&J Stock Eyes Worst Day Since April 2025 On MedTech Miss - Johnson & Johnson (NYSE:JNJ), State Street He](https://www.benzinga.com/trading-ideas/movers/26/10/62336881/jnj-stock-worst-day-since-april-2025-medtech-miss)  
  <sub>Benzinga, 20 hours ago</sub>  
  Johnson & Johnson beat third-quarter profit estimates and raised its 2026 forecast. After MedTech sales missed estimates, the stock still fell about 6%,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 172.18 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 169.22 (+1.8%), 50d 169.46 (+1.6%), 200d 157.29 (+9.5%); 50d above 200d
Momentum: RSI(14) 58.5 | MACD 0.487 vs signal 0.149 (histogram 0.338)
Returns: 1d +1.5% | 5d +2.0% | 1m +2.7% | 3m +6.4%
52-week range: 142.32 - 175.68 (now 89.5% of the way up)
Volatility: ATR(14) 2.66 (1.5% of price) | annualised 20d 13.7%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Health
What it holds: P/E 30.01 | P/B 4.74 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +11.8% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.39B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Eli Lilly and Co 15.1%, Johnson & Johnson 10.4%, AbbVie Inc 7.5%, Merck & Co Inc 5.8%, UnitedHealth Group Inc 5.4%
Sector mix: Healthcare 100.0%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.1% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - JNJ: 2026-10-14 RBC Capital: main, Outperform -> Outperform
  - ABBV: 2026-10-13 RBC Capital: reit, Outperform -> Outperform
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-14 Barclays: main, Overweight -> Overweight
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
Shares outstanding: 197.42M | fund size: 33.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is strongly bullish (100% buy rating, +21.3% price target) but only covers ~54% of the fund, while fund flows are flat (0% share count change) indicating no directional demand. Fund basics show high valuations (P/E 24, P/B 5.56) despite strong 3‑year returns (+12.6% annual). Technicals are mixed: price below 50‑day and 200‑day SMA, RSI 46.5, MACD negative. Macro data show no surprise, with yields up slightly, inflation 3.7% above target, and Fed target unchanged. Overall, the evidence points to a neutral stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +21.3% (covers 54.4% of fund)
- Fund flows flat: 0% share count change over 1 week
- Fund basics: high valuations (P/E 24, P/B 5.56) but strong 3‑year returns (+12.6% annual)
- Technicals: price below 50‑day and 200‑day SMA, RSI 46.5, MACD negative
- Macro: no data surprise, yields up slightly, inflation 3.7% above target, Fed target unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Investment Management Builds on Nearly 30 Years of Sector ETF Leadership with New Market Sector ETFs](https://www.businesswire.com/news/home/20261014723784/en/State-Street-Investment-Management-Builds-on-Nearly-30-Years-of-Sector-ETF-Leadership-with-New-Market-Sector-ETFs)  
  <sub>Business Wire, 2 hours ago</sub>  
  State Street Investment Management today announced the launch of four new State Street® S&P 500® Market Sector SPDR® ETFs, building on the sector ETF...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-195559592.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks were mixed late Tuesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) easing 0.1% and the State Street...
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-171257151.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Consumer stocks were mixed Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) decreasing 0.2% and the State Street...
- [Exchange-Traded Funds Higher, Equity Futures Mixed Pre-Bell Wednesday Amid September Consumer Inflation Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-higher-equity-132552488.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3% and the actively trad.
- [Sector Update: Consumer Stocks Mixed in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-mixed-afternoon-174929277.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Consumer stocks were mixed Tuesday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) down 0.1% and the State Street Consumer...
- [Exchange-Traded Funds Lower as US Equities Decline After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-us-172017687.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) eased 0.5%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 111.22 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 110.91 (+0.3%), 50d 114.08 (-2.5%), 200d 115.97 (-4.1%); 50d below 200d
Momentum: RSI(14) 46.5 | MACD -0.421 vs signal -0.826 (histogram 0.406)
Returns: 1d -1.0% | 5d -0.1% | 1m +0.3% | 3m -5.2%
52-week range: 105.66 - 124.52 (now 29.5% of the way up)
Volatility: ATR(14) 1.35 (1.2% of price) | annualised 20d 12.7%
Volume: 0.35x the 20-day average
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
Three-year record: +12.6% a year | beta to the market 1.18
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
Weighted price target: +21.3% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-12 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-10-12 Jefferies: main, Hold -> Hold
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 120.25M | fund size: 13.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 87.36 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 88.87 (-1.7%), 50d 91.90 (-4.9%), 200d 92.47 (-5.5%); 50d below 200d
Momentum: RSI(14) 40.8 | MACD -1.304 vs signal -1.499 (histogram 0.194)
Returns: 1d -1.5% | 5d -0.5% | 1m -7.6% | 3m -5.7%
52-week range: 70.49 - 102.94 (now 52.0% of the way up)
Volatility: ATR(14) 1.76 (2.0% of price) | annualised 20d 28.6%
Volume: 0.15x the 20-day average
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
Weighted price target: +32.7% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -4.3% (-31.74M) over 7d
Shares outstanding: 8.13M | fund size: 710.47M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.92 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 44.26 (-0.8%), 50d 44.37 (-1.0%), 200d 39.88 (+10.1%); 50d above 200d
Momentum: RSI(14) 48.2 | MACD -0.118 vs signal -0.086 (histogram -0.032)
Returns: 1d -1.2% | 5d +0.7% | 1m -2.1% | 3m +8.1%
52-week range: 32.22 - 45.76 (now 86.4% of the way up)
Volatility: ATR(14) 0.66 (1.5% of price) | annualised 20d 22.3%
Volume: 0.16x the 20-day average
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
Three-year record: +41.9% a year | beta to the market 0.64
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.26 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +1.7% above the current prices
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
Share count change: 1 week: -2.0% (-17.23M) over 7d
Shares outstanding: 19.01M | fund size: 835.22M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 46.70 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 46.82 (-0.2%), 50d 47.74 (-2.2%), 200d 46.79 (-0.2%); 50d above 200d
Momentum: RSI(14) 45.6 | MACD -0.344 vs signal -0.405 (histogram 0.061)
Returns: 1d -0.3% | 5d +1.7% | 1m -2.3% | 3m -0.6%
52-week range: 41.34 - 49.39 (now 66.6% of the way up)
Volatility: ATR(14) 0.44 (1.0% of price) | annualised 20d 12.1%
Volume: 0.08x the 20-day average
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
Three-year record: +18.1% a year | beta to the market 0.71
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
Weighted price target: +14.8% above the current prices
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 67.80M | fund size: 3.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Daily ETF Flows: RSP Gathers $565M](https://www.etf.com/sections/daily-etf-flows/daily-etf-flows-rsp-gathers-565m)  
  <sub>ETF.com, 22 hours ago</sub>  
  Here are the daily ETF fund flows for October 12, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 42.22 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 39.55 (+6.8%), 50d 37.43 (+12.8%), 200d 36.84 (+14.6%); 50d above 200d
Momentum: RSI(14) 65.4 | MACD 1.657 vs signal 1.301 (histogram 0.356)
Returns: 1d -1.5% | 5d -0.3% | 1m +11.8% | 3m +19.5%
52-week range: 29.10 - 43.54 (now 90.9% of the way up)
Volatility: ATR(14) 1.03 (2.4% of price) | annualised 20d 49.8%
Volume: 0.41x the 20-day average
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
Three-year record: +19.9% a year | beta to the market 0.83
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
Shares outstanding: 200.55M | fund size: 8.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares SLVP vs VanEck GDX: Which Miners ETF Wins](https://finance.yahoo.com/markets/stocks/articles/ishares-slvp-vs-vaneck-gdx-102002882.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  While iShares MSCI Global Silver and Metals Miners ETF (NYSEMKT:SLVP) offers a lower cost and higher yield, VanEck Gold Miners ETF (NYSEMKT:GDX) provides...
- [GDXJ Stock Price, Quote & News](https://www.syfe.com/stocks/us/gdxj)  
  <sub>Syfe, 23 hours ago</sub>  
  Get the latest VanEck Junior Gold Miners ETF (GDXJ) stock price, key stats and news. Track & Trade GDXJ with $0 commission on Syfe.
- [YieldMax® ETFs Announces Weekly Distributions for Group 2 ETFs](https://www.wboc.com/online_features/press_releases/yieldmax-etfs-announces-weekly-distributions-for-group-2-etfs/article_7c2d759f-0c32-5ef1-a577-62fd6d2eebc0.html)  
  <sub>WBOC TV, 4 hours ago</sub>  
  CHICAGO and MILWAUKEE and NEW YORK, Oct. 14, 2026 (GLOBE NEWSWIRE) -- YieldMax® ETFs today announced distributions for.
- [Gold And Silver Lose Their Shine When Held In The Wrong Account (NYSEARCA:SPY)](https://seekingalpha.com/article/4954049-gold-and-silver-lose-their-shine-when-held-in-the-wrong-account)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Use gold and silver funds for diversification. Learn bullion ETF tax rules, why Roth IRAs help, and how mining ETFs fit taxable accounts—read now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 83.79 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 89.92 (-6.8%), 50d 93.30 (-10.2%), 200d 91.05 (-8.0%); 50d above 200d
Momentum: RSI(14) 37.3 | MACD -2.021 vs signal -1.621 (histogram -0.400)
Returns: 1d -4.0% | 5d -2.0% | 1m -11.0% | 3m +17.4%
52-week range: 68.28 - 115.84 (now 32.6% of the way up)
Volatility: ATR(14) 2.92 (3.5% of price) | annualised 20d 39.5%
Volume: 0.48x the 20-day average
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
Three-year record: +48.9% a year | beta to the market 0.81
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.63 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.6% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, FNV.TO
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-10-08 UBS: main, Neutral -> Neutral
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: money going out (1 week)
Share count change: 1 week: -1.5% (-386.52M) over 7d
Shares outstanding: 295.03M | fund size: 24.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields and inflation data in line with expectations
- Technical indicators: RSI 70.7 (overbought) and price at 52‑week high but no decisive break
- Positioning: crowded long (21.8% net long, 100th percentile) with modest weekly increase (+1.9% OI)
- Cost of holding: heavy negative roll cost (-9.8% annual) drags long returns

<details><summary><b>News</b> — score +0.00</summary>

- [Sugar Prices Climb as Brazil Rains Disrupt Cane Crushing](https://www.barchart.com/story/news/6905623/sugar-prices-climb-as-brazil-rains-disrupt-cane-crushing)  
  <sub>Barchart.com, 23 hours ago</sub>  
  March NY world sugar #11 (SBH27 ) is up +0.21 (+1.01%) today, and December London ICE white sugar #5 (SWZ26 ) is up +1.20 (+0.21%). Sugar prices are moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 12.48 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 11.67 (+7.0%), 50d 11.36 (+9.8%), 200d 10.08 (+23.8%); 50d above 200d
Momentum: RSI(14) 70.7 | MACD 0.317 vs signal 0.248 (histogram 0.069)
Returns: 1d +0.8% | 5d +1.6% | 1m +9.7% | 3m +31.0%
52-week range: 9.02 - 12.48 (now 100.0% of the way up)
Volatility: ATR(14) 0.21 (1.7% of price) | annualised 20d 24.2%
Volume: 0.52x the 20-day average
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
Cost of holding this fund instead of sugar itself: -9.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +31.0%, commodity +45.8%, gap -14.8% | 6 months: fund +36.1%, commodity +55.8%, gap -19.7% | 12 months: fund +25.1%, commodity +34.8%, gap -9.8%
A commodity fund holds futures, not sugar, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 21.8% of open interest (1,158,944 contracts)
Change on the week: +1.9% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.9% (-1.07M) over 7d
Shares outstanding: 4.42M | fund size: 55.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, positioning change modestly bearish, heavy roll cost offsets bullish crop trend, overall view remains neutral.

**Main reasons it gave:**
- Positioning: net long 17.7% of open interest, weekly change -2.8% (reduction in bullish bets)
- Cost of holding: -9.9% annual roll cost (heavy cost for longs)
- Crop condition: 56% good/excellent, trend -1 point (worsening, bullish supply factor)
- Macro: no rate or data surprise; yields stable, VIX modest

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 18.36 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 19.24 (-4.6%), 50d 19.20 (-4.4%), 200d 18.17 (+1.0%); 50d above 200d
Momentum: RSI(14) 33.3 | MACD -0.266 vs signal -0.134 (histogram -0.133)
Returns: 1d -0.6% | 5d -3.6% | 1m -8.4% | 3m +4.2%
52-week range: 16.47 - 20.29 (now 49.5% of the way up)
Volatility: ATR(14) 0.31 (1.7% of price) | annualised 20d 20.4%
Volume: 0.16x the 20-day average
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
Cost of holding this fund instead of corn itself: -9.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +4.2%, commodity +8.4%, gap -4.2% | 6 months: fund +1.6%, commodity +6.0%, gap -4.4% | 12 months: fund +6.6%, commodity +16.5%, gap -9.9%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 17.7% of open interest (1,859,993 contracts)
Change on the week: -2.8% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.5% (3.13M) over 7d
Shares outstanding: 7.06M | fund size: 129.62M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Inflation 3.7% in line with expectations
- Fed target unchanged at 4.00% (no policy surprise)
- Technical indicators neutral (RSI 51.2, price near 20‑day SMA)
- Positioning net long down 5.8% week, crowding low (23% percentile)
- Fund flows outflows: share count down 2.2% over 7 days

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 40.08 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 40.15 (-0.2%), 50d 39.94 (+0.4%), 200d 37.70 (+6.3%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD 0.110 vs signal 0.083 (histogram 0.027)
Returns: 1d -0.9% | 5d +0.7% | 1m +3.7% | 3m +5.3%
52-week range: 30.53 - 41.43 (now 87.7% of the way up)
Volatility: ATR(14) 0.57 (1.4% of price) | annualised 20d 20.6%
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
Cost of holding this fund instead of copper itself: -4.3% a year -- a steady drag
Measured: 3 months: fund +5.3%, commodity +6.2%, gap -0.9% | 6 months: fund +7.6%, commodity +10.2%, gap -2.6% | 12 months: fund +26.9%, commodity +31.1%, gap -4.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 20.1% of open interest (304,033 contracts)
Change on the week: -5.8% of open interest
Crowding: 23% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -2.2% (-15.99M) over 7d
Shares outstanding: 17.74M | fund size: 711.27M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro data (inflation 3.7%, unemployment 4.2%) in line with expectations, no surprise
- Technical indicators show price below 20‑day, 50‑day, 200‑day SMAs, RSI 32.1, no decisive break on volume
- CFTC positioning unchanged (net long 7.2%, 0% change, low crowding percentile 15%)
- Cost of holding -5.5% per year indicates heavy roll cost, dampening bullish case

<details><summary><b>News</b> — score +0.00</summary>

- [iShares SLVP vs VanEck GDX: Which Miners ETF Wins](https://finance.yahoo.com/markets/stocks/articles/ishares-slvp-vs-vaneck-gdx-102002882.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>
- [Gold And Silver Lose Their Shine When Held In The Wrong Account (NYSEARCA:SPY)](https://seekingalpha.com/article/4954049-gold-and-silver-lose-their-shine-when-held-in-the-wrong-account)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Use gold and silver funds for diversification. Learn bullion ETF tax rules, why Roth IRAs help, and how mining ETFs fit taxable accounts—read now.
- [Silver ETFs Dump 2.7M Ounces! Can Gold Hold $4,140 Into Today’s CPI? | Metals Minute Phil Streible](https://www.barchart.com/story/news/7562276/silver-etfs-dump-2-7m-ounces-can-gold-hold-4-140-into-todays-cpi-metals-minute-phil-streible)  
  <sub>Barchart.com, 4 hours ago</sub>  
  Dive into todays market action with the Blue Line Futures Metals Minute! (Episode 765)
- [If You Invested $1,000 in abrdn Physical Silver Shares ETF (SIVR)](https://www.stocktitan.net/tools/stock-return-calculator/SIVR)  
  <sub>Stock Titan, 13 hours ago</sub>  
  invested in SIVR 5 years ago is worth $2477 as of 2026-10-13 — +147.7% total return (19.9% CAGR). Free calculator with S&P 500 comparison.
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [Gold futures rise, silver futures fall in domestic, global markets](https://www.business-standard.com/markets/commodities/gold-futures-rise-silver-futures-fall-in-domestic-global-markets-126101400323_1.html)  
  <sub>Business Standard, 10 hours ago</sub>  
  In the global market, gold futures on Comex were trading near $4190 per ounce, while silver was trading near $59.50 per ounce.
- [The SLVR ETF Remains A Buy So Long As Critical Technical Support Holds (NASDAQ:SLVR)](https://seekingalpha.com/article/4953879-the-slvr-etf-remains-a-buy-so-long-as-critical-technical-support-holds)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Sprott Silver Miners & Physical Silver ETF remains a Buy below $55, supported by long-term bullish technicals above $50.36 silver futures.
- [Gold, silver ETFs see sharp rise in inflows in September. Which metal should investors prefer now?](https://cafemutual.com/news/press-news/39048-gold-silver-etfs-see-sharp-rise-in-inflows-in-september-which-metal-should-investors-prefer-now)  
  <sub>Cafemutual, 17 hours ago</sub>  
  In September, investor enthusiasm for gold and silver ETFs saw a notable increase, driven by ongoing market uncertainties and global tensions.
- [Current price of silver as of Wednesday, Oct. 14, 2026](https://fortune.com/article/current-price-of-silver-10-14-2026/)  
  <sub>Fortune, 6 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 50.72 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 55.95 (-9.3%), 50d 57.94 (-12.5%), 200d 65.56 (-22.6%); 50d below 200d
Momentum: RSI(14) 32.1 | MACD -1.468 vs signal -1.097 (histogram -0.371)
Returns: 1d -5.2% | 5d -5.8% | 1m -11.8% | 3m +0.7%
52-week range: 42.40 - 105.60 (now 13.2% of the way up)
Volatility: ATR(14) 1.58 (3.1% of price) | annualised 20d 38.6%
Volume: 0.92x the 20-day average
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
Cost of holding this fund instead of silver itself: -5.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +0.7%, commodity +1.2%, gap -0.5% | 6 months: fund -29.4%, commodity -28.9%, gap -0.5% | 12 months: fund +7.3%, commodity +12.8%, gap -5.5%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 341.45M | fund size: 17.32B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- US inflation 3.7% and unemployment 4.2% in line with expectations, no macro surprise
- Price below 20‑day SMA (27.29 vs 27.60) and MACD negative, low volume, no decisive technical break
- CFTC large speculators net long 23% of OI, +0.4% change, 92nd percentile crowding – ambiguous positioning
- Fund share count down 1.0% over 7 days, indicating outflows
- US soybean crop condition steady (57% good/excellent, no trend change)

<details><summary><b>News</b> — score +0.00</summary>

- [China resumes U.S. soybean buying with 8-10 cargoes after Trump-Xi summit - report (FXI:NYSEARCA)](https://seekingalpha.com/news/4652769-china-resumes-us-soybean-buying-with-8-10-cargoes-after-trump-xi-summit---report)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  China's state-owned firms bought 8–10 U.S. soybean cargoes—first since the Trump-Xi summit.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.29 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 27.60 (-1.1%), 50d 26.98 (+1.2%), 200d 24.84 (+9.9%); 50d above 200d
Momentum: RSI(14) 47.7 | MACD 0.051 vs signal 0.133 (histogram -0.082)
Returns: 1d -0.1% | 5d -1.1% | 1m -2.4% | 3m +7.7%
52-week range: 21.56 - 28.14 (now 87.1% of the way up)
Volatility: ATR(14) 0.31 (1.2% of price) | annualised 20d 12.4%
Volume: 0.17x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.3% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +7.7%, commodity +6.9%, gap +0.8% | 6 months: fund +11.6%, commodity +9.5%, gap +2.1% | 12 months: fund +26.5%, commodity +26.8%, gap -0.3%
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
Share count change: 1 week: -1.0% (-461.53K) over 7d
Shares outstanding: 1.65M | fund size: 44.96M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields stable, inflation 3.7% (no surprise)
- Technical: price 10.99 below 200‑day SMA 11.30, MACD +0.044
- Positioning: net short 8% OI, change -0.5% (crowded short)
- Fundamentals: roll cost -11.6% yr, inventory build +85 BCF, EIA forecast price drop to $2.59 in 6 mo

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.99 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 10.75 (+2.3%), 50d 10.42 (+5.5%), 200d 11.30 (-2.7%); 50d below 200d
Momentum: RSI(14) 54.6 | MACD 0.164 vs signal 0.120 (histogram 0.044)
Returns: 1d -3.6% | 5d -0.3% | 1m +4.3% | 3m +5.5%
52-week range: 9.63 - 16.90 (now 18.8% of the way up)
Volatility: ATR(14) 0.38 (3.4% of price) | annualised 20d 48.7%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.65</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.65</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.65</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.65</summary>

```text
Cost of holding this fund instead of natural gas itself: -11.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +5.5%, commodity +11.1%, gap -5.6% | 6 months: fund +3.9%, commodity +21.7%, gap -17.8% | 12 months: fund -9.7%, commodity +1.9%, gap -11.6%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.65</summary>

```text
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.65</summary>

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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 8.0% of open interest (1,815,990 contracts)
Change on the week: -0.5% of open interest
Crowding: 3% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 12.08M | fund size: 132.87M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to mixed signals: positioning weakening, bearish price outlook, mixed inventory data, strong technical trend but low volume, and no macro surprise.

**Main reasons it gave:**
- CFTC positioning net long 2.8% of OI but down 1.4% week over week, indicating weakening bullish sentiment
- EIA price outlook projects WTI falling from $100 to $86 over six months, a bearish signal
- Crude inventories draw of 3.2 million barrels (bullish) offset by a small petrol build, net mixed but slight bullish
- Technicals show strong uptrend (price above 20/50/200 SMA) but low volume and no decisive break
- Macro data unchanged; no rate or inflation surprise, VIX modestly elevated

<details><summary><b>News</b> — score +0.00</summary>

- [OXY, BATL, USO, UCO Stocks Surge Premarket As Brent Breaks Above $94 A Barrel](https://stocktwits.com/news-articles/markets/equity/oxy-batl-uso-uco-stocks-surge-premarket-as-brent-breaks-above-94-a-barrel/cZZmaEpR7wN)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Brent crude futures expiring in September rose to $94.25 per barrel at the time of writing, while WTI crude futures expiring in September were at $87.54 per...
- [IEA warns diesel supply crunch to extend into 2027 (USO:NYSEARCA)](https://seekingalpha.com/news/4652773-iea-warns-diesel-supply-crunch-to-extend-into-2027)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Diesel prices are surging amid Iran war disruptions and low inventories.
- [Crude Benchmarks Split as USO, UCO Slide While WTI Futures Climb More Than 2%](https://finance.biggo.com/news/93a3fde9-09fc-4812-affc-de0295239c7c)  
  <sub>BigGo Finance, 21 hours ago</sub>  
  Oil prices diverged Tuesday as WTI futures climbed more than 2% while Brent fell nearly 1.5% to $105.05 a barrel, and crude-linked ETFs including USO…
- [United States Oil Fund, LP (USO) Options Chain](https://ca.finance.yahoo.com/quote/USO/options/?date=1792713600&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Contract Name, Last Trade Date (EDT), Strike, Last Price, Bid, Ask, Change, % Change, Volume, Open Interest, Implied Volatility...
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [U.S. diesel futures jump while crude oil closes mixed (USO:NYSEARCA)](https://seekingalpha.com/news/4652723-u-s-diesel-futures-jump-while-crude-oil-closes-mixed)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Crude and refined product futures closed mixed while US diesel futures rose sharply, as the lifting of US sanctions on Russian diesel failed to bring down...
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”
- [Oil Prices Surge Nearly 10% — US Forces To Resume Maritime Blockade Against Iran On Tuesday](https://stocktwits.com/news-articles/markets/equity/oil-prices-surge-10-percent-us-forces-to-resume-maritime-blockade-against-iran-on-tuesday/cZmz6rZR7Yo)  
  <sub>Stocktwits, 12 hours ago</sub>  
  The U.S. Central Command said U.S. forces will enforce the blockade on vessels entering or leaving Iranian ports starting July 14 at 4 p.m. ET.
- [Houthis threaten to attack Aramco as Saudi-led coalition orders evacuation of Yemen oil facility](https://seekingalpha.com/news/4652541-houthis-threaten-to-attack-aramco-as-saudi-led-coalition-orders-evacuation-of-yemen-oil-facility)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The Houthi militia threatened to strike facilities belonging to Saudi Aramco after Saudi authorities told civilians to evacuate a key oil facility in...
- [Peter Schiff Warns ‘Mother Of All Bond Bear Markets’ Is Coming — ‘Something’s Going To Break’](https://stocktwits.com/news-articles/markets/equity/peter-schiff-mother-of-all-bond-bear-markets-coming/cZDZXttRB1T)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Schiff's warning came after Treasury bonds sold off despite a weak September jobs report, lower-than-expected inflation readings and sharply reduced...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 153.45 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 148.71 (+3.2%), 50d 140.97 (+8.8%), 200d 118.36 (+29.6%); 50d above 200d
Momentum: RSI(14) 59.0 | MACD 2.116 vs signal 2.126 (histogram -0.010)
Returns: 1d +0.2% | 5d +6.6% | 1m -5.2% | 3m +28.6%
52-week range: 66.17 - 161.86 (now 91.2% of the way up)
Volatility: ATR(14) 4.75 (3.1% of price) | annualised 20d 37.3%
Volume: 0.27x the 20-day average
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 2.8% of open interest (1,889,422 contracts)
Change on the week: -1.4% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 119.10M | fund size: 18.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed signals across positioning, technicals, macro and flows lead to a neutral stance.

**Main reasons it gave:**
- Positioning: net short decreased by 1.2% of OI, indicating slight bullish tilt
- Technicals: price below 20‑day and 50‑day SMAs, RSI 35.7, MACD negative, showing bearish momentum
- Macro: yields stable, dollar up, no policy surprise; inflation 3.7% near expectations
- Fund flows: share count up 1.5% over the week, indicating modest inflow

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 24.14 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 25.14 (-4.0%), 50d 25.55 (-5.5%), 200d 23.36 (+3.3%); 50d above 200d
Momentum: RSI(14) 35.7 | MACD -0.414 vs signal -0.305 (histogram -0.109)
Returns: 1d -0.6% | 5d -3.1% | 1m -8.3% | 3m -3.1%
52-week range: 19.88 - 28.00 (now 52.5% of the way up)
Volatility: ATR(14) 0.48 (2.0% of price) | annualised 20d 18.8%
Volume: 0.26x the 20-day average
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
Measured: 3 months: fund -3.1%, commodity -1.5%, gap -1.6% | 6 months: fund +7.1%, commodity +11.9%, gap -4.8% | 12 months: fund +19.8%, commodity +33.8%, gap -14.0%
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
Share count change: 1 week: +1.5% (4.07M) over 7d
Shares outstanding: 11.64M | fund size: 280.96M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Gold And Silver Lose Their Shine When Held In The Wrong Account (NYSEARCA:SPY)](https://seekingalpha.com/article/4954049-gold-and-silver-lose-their-shine-when-held-in-the-wrong-account)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Use gold and silver funds for diversification. Learn bullion ETF tax rules, why Roth IRAs help, and how mining ETFs fit taxable accounts—read now.
- [Daily ETF Flows: RSP Gathers $565M](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-rsp-gathers-210004324.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. SPYM · State Street SPDR Portfolio S&P 500 ETF. 1,818.62.
- [Top 10 ETFs in Malaysia 2026](https://www.moomoo.com/my/learn/top-etfs-in-malaysia)  
  <sub>Moomoo, 5 hours ago</sub>  
  Top 10 ETFs in Malaysia 2026: VOO, QQQ, GLD, VDE, SOXL, NVDL, AGG, EQ8MY25, ABFMY1, GOLDETF. Learn ETF basics, benefits, selection tips, and how to invest...
- [Weekly ETFs: All 11 sectors record inflows; Gold leads outflows](https://www.tradingview.com/news/seekingalpha:e8a4773bd094b:0-weekly-etfs-all-11-sectors-record-inflows-gold-leads-outflows/)  
  <sub>TradingView, 22 hours ago</sub>  
  The world's largest exchange-traded fund, SPDR S&P 500 ETF Trust AMEX:SPY, saw outflows of $3.14B for the week ended October 9, while its price performance...
- [Can Gold Hold USD 4,150, and What Does It Mean for GLD (NYSEARCA:GLD)?](https://kalkine.ca/news/general-news/can-gold-hold-usd-4150-and-what-does-it-mean-for-gld-nysearcagld)  
  <sub>kalkine.ca, 1 hour ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [South Korea's KOSPI, S&P 500, Gold Sink On US-Iran Tensions, But Bitcoin Holds $68K Floor](https://stocktwits.com/news-articles/markets/cryptocurrency/kospi-s-and-p-500-gold-sink-on-us-iran-tensions-but-bitcoin-holds/cZd9fmeRI5O)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The Korea Composite Stock Price Index (KOSPI) dropped more than 10% in Asian trading hours, making its worst single-day drop in two years.
- [Gold futures tick lower ahead of key U.S. inflation data (GLD:NYSEARCA)](https://seekingalpha.com/news/4652710-gold-futures-tick-lower-ahead-of-key-u-s-inflation-data)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Gold futures fell slightly as traders lowered exposure a day ahead of US Consumer Price Index data and its implications for Federal Reserve interest rate...
- [ETF boom turns specialized as leveraged and thematic funds shine](https://seekingalpha.com/news/4652613-etf-boom-turns-specialized-as-leveraged-and-thematic-funds-shine)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  The U.S. ETF market is shifting toward greater specialization and leverage as product launches accelerate. Nearly 1,100 new ETFs have debuted so far in 2026...
- [Webcast: Long Live Nuclear: How Extended Reactor Lives Drive Investment Opportunities | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/09/long-live-nuclear-how-extended-reactor-lives-drive-investment-opportunities?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 23 hours ago</sub>  
  Today's nuclear fleet is poised to operate for 100+ years while generating more power. This creates demand today across the nuclear value chain,...
- [Bank Earnings Get a Cool Reception as Chip Jitters Linger](https://pro.thestreet.com/market-commentary/bank-earnings-get-a-cool-reception-as-chip-jitters-linger)  
  <sub>RealMoney Pro, 16 hours ago</sub>  
  Memory makers fell again and the big banks missed Street expectations but Mag-7 strength kept the S&P 500 flat.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.10% (+0.06 on the week) | 5-year 5.07% (+0.05 on the week) | 10-year 5.26% (-0.02 on the week) | 30-year 5.58% (-0.09 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.81 (+0.57 on the week)
Volatility (VIX): 15.70 (+0.6 on the week) -- elevated
Latest US data: inflation 3.7% (2026-09-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.80% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 374.80 (bar of 2026-10-14), from 502 daily bars
Trend: vs 20d SMA 386.00 (-2.9%), 50d 397.45 (-5.7%), 200d 415.14 (-9.7%); 50d below 200d
Momentum: RSI(14) 38.3 | MACD -5.106 vs signal -4.874 (histogram -0.233)
Returns: 1d -1.8% | 5d -0.3% | 1m -4.9% | 3m +2.7%
52-week range: 362.32 - 495.90 (now 9.3% of the way up)
Volatility: ATR(14) 6.13 (1.6% of price) | annualised 20d 21.5%
Volume: 0.50x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.7% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +2.7%, commodity +3.3%, gap -0.6% | 6 months: fund -14.9%, commodity -14.5%, gap -0.4% | 12 months: fund -0.9%, commodity -0.2%, gap -0.7%
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
Shares outstanding: 260.30M | fund size: 97.56B
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

