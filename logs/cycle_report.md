# Daily report

**28 Sep 2026, 18:39 Israel time (15:39 UTC)** · 80 names checked · 0 traded · 1 with a problem

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 2 | 14 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 40 | 1 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| ASML (ASML) · Company | **Stop raised.** At +0.23R, following the price. Stop-loss raised 1640.82 → 1651.24. |
| Caterpillar (CAT) · Company | **Stop raised.** At +0.31R, following the price. Stop-loss raised 768.09 → 777.80. |
| Developing country bonds (EMB) · Index fund | **Stop raised.** At +2.55R, following the price. Stop-loss raised 92.80 → 92.37. |
| Gold (GLD) · Commodity | **Stop raised.** At +0.69R, following the price. Stop-loss raised 403.77 → 393.48. |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop raised.** At +2.24R, following the price. Stop-loss raised 90.57 → 90.39. |
| Nvidia (NVDA) · Company | **Stop raised.** At +1.22R, following the price. Stop-loss raised 216.23 → 219.01. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.47R, following the price. Stop-loss raised 41.12 → 40.85. |
| Procter & Gamble (PG) · Company | **Stop raised.** At +0.20R, following the price. Stop-loss raised 143.18 → 143.66. |
| S&P 500, equal weight (RSP) · Index fund | **Stop raised.** At +0.54R, following the price. Stop-loss raised 214.01 → 213.56. |
| Royal Bank of Canada (RY) · Company | **Stop raised.** At +0.04R, following the price. Stop-loss raised 194.59 → 195.58. |
| US inflation-linked bonds (TIP) · Index fund | **Stop raised.** At +2.89R, following the price. Stop-loss raised 105.14 → 104.90. |
| US government bonds, 20+ years (TLT) · Index fund | **Stop raised.** At +2.00R, following the price. Stop-loss raised 80.48 → 80.00. |
| US shopping and leisure (XLY) · Sector or country | **Stop raised.** At +0.19R, following the price. Stop-loss raised 113.13 → 112.69. |
| Taiwan (EWT) · Sector or country | **Holding.** -0.39R, holding 33 shares. Stop-loss 110.28. |
| HDFC Bank (HDB) · Company | **Holding.** -0.85R, holding 90 shares. Stop-loss 22.23. |
| JPMorgan Chase (JPM) · Company | **Holding.** +0.13R, holding 6 shares. Stop-loss 327.15. |
| US regional banks (KRE) · Sector or country | **Holding.** +0.19R, holding 53 shares. Stop-loss 72.54. |
| Eli Lilly (LLY) · Company | **Holding.** +0.67R, holding 4 shares. Stop-loss 1130.70. |
| Microsoft (MSFT) · Company | **Holding.** +0.73R, holding 7 shares. Stop-loss 492.61. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.26R, holding 128 shares. Stop-loss 37.12. |
| US dollar (UUP) · Index fund | **Holding.** +1.42R, holding 282 shares. Stop-loss 28.50. |
| Exxon Mobil (XOM) · Company | **Holding.** +0.21R, holding 13 shares. Stop-loss 156.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The news includes a material growth catalyst (TPU sales forecast) and a bullish AI push, offset by concerns over capex and recent earnings misses. Fundamentals are strong with high margins, ROE, and low leverage. Analyst consensus is strongly bullish with a sizable price target upside. Technicals show short‑term weakness (price below 20‑day SMA, very low volume). Overall, bullish factors outweigh bearish, leading to a BUY signal with moderate conviction.

**Main reasons it gave:**
- Piper Sandler forecasts $104B TPU sales by 2028 (material growth catalyst)
- High profitability and low leverage (profit margin 54.8%, ROE 48.7%, debt/equity 18.9%)
- Analyst consensus strong buy with mean price target $429.55 (+25.8% upside)
- Technical weakness: price below 20‑day SMA and volume at 0.19× 20‑day average

<details><summary><b>News</b> — score +0.20</summary>

- [Piper Sandler sees Google TPU sales hitting $104BN by 2028](https://finance.yahoo.com/markets/stocks/articles/piper-sandler-sees-google-tpu-135843693.html)  
  <sub>Yahoo Finance, 43 minutes ago</sub>  
  Investing.com -- Piper Sandler analyst Thomas Champion is projecting Google's newly disclosed external chip business will generate $104 billion in TPU...
- [Alphabet (GOOGL) Stock Price Forecast 2026: Cloud Hit $20B But FCF Collapsed — Buy or Short?](https://www.tradingkey.com/analysis/stocks/us-stocks/262008961-alphabet-googl-stock-price-forecast-2026-google-cloud-tradingkey)  
  <sub>TradingKey, 14 hours ago</sub>  
  The main reason the market is selling Alphabet stock down is the increased $190 billion 2026 capex guidance which has dropped Free Cash Flow margin down from 21...
- [Oracle Stock Slips as Google's Mandiant Flags New PeopleSoft Breach Wave](https://www.benzinga.com/markets/tech/26/09/62024410/oracle-stock-slips-as-googles-mandiant-flags-new-peoplesoft-breach-wave)  
  <sub>Benzinga, 14 minutes ago</sub>  
  Oracle Corp. (NYSE:ORCL) shares moved lower Monday after Alphabet Inc.'s (NASDAQ:GOOGL) (NASDAQ:GOOG) cybersecurity unit, Mandiant, said a notorious hacking...
- [GOOGL Fairly Valued by DCF at $334](https://www.gurufocus.com/news/9099521)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 28, 2026, we delve into the DCF analysis for Alphabet Inc (GOOGL), a company that has shown a year-to-date price increase of 10.1% and a...
- [META, GOOGL, NVDA, BB, SPCX: Why Retail Traders Couldn’t Take Their Eyes Off These Stocks Last Week](https://stocktwits.com/news-articles/markets/equity/meta-googl-nvda-bb-spcx-why-retail-traders-couldn-t-take-their-eyes-off-these-stocks-last-week/cZMSQ6MRBff)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Meta shares jumped nearly 13% last week after new AI and hardware launches, including Muse Charm. China is considering allowing ByteDance and Alibaba to buy...
- [Alphabet (GOOGL) Pushes Deeper Into AI Following Gemini 4 As Valuation Debate Builds](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/alphabet-googl-pushes-deeper-into-ai-following-gemini-4-as-v)  
  <sub>Simply Wall Street, 12 hours ago</sub>  
  Alphabet (GOOGL) has pushed deeper into AI this month, lining up the Gemini 4 model, an early Project Suncatcher satellite launch, and a fresh Experian...
- [Zacks Investment Ideas feature highlights: Alphabet, Apple and NVIDIA](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL/pressreleases/4826766/zacks-investment-ideas-feature-highlights-alphabet-apple-and-nvidia/)  
  <sub>The Globe and Mail, 7 hours ago</sub>  
  Detailed price information for Alphabet Cl A (GOOGL-Q) from The Globe and Mail including charting and trades.
- [S&P 500, Dow, Nasdaq Drop As Yields Spike Amid Calls For More Rate Hikes — AMZN, GOOGL, NFLX, SPCX, RKLB In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-drop-as-yields-spike-amid-calls-for-more-rate-hikes-amzn-googl-nflx-spcx-rklb-in-focus/cZM4IxjRBB9)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Treasury yields jumped across the curve on Wednesday. Traders work on the floor of the New York Stock Exchange (NYSE) on July 23, 2026 in New York City.
- [GOOGL Sep 2026 392.500 call (GOOGL260928C00392500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GOOGL260928C00392500/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  Find the latest GOOGL Sep 2026 392.500 call (GOOGL260928C00392500) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 341.45 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 341.92 (-0.1%), 50d 344.18 (-0.8%), 200d 338.33 (+0.9%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD -0.150 vs signal -0.324 (histogram 0.174)
Returns: 1d -0.7% | 5d -3.8% | 1m +0.2% | 3m -3.4%
52-week range: 236.57 - 402.62 (now 63.2% of the way up)
Volatility: ATR(14) 8.47 (2.5% of price) | annualised 20d 26.7%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.18T
Valuation: trailing P/E 17.15 | forward P/E 22.66 | P/B 6.71 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.55 (+25.8% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - 2026-09-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-09-03 Rosenblatt: main, Buy -> Buy
  - 2026-07-23 UBS: main, Neutral -> Neutral
  - 2026-07-23 Morgan Stanley: main, Overweight -> Overweight
  - 2026-07-23 Truist Securities: main, Buy -> Buy
Institutional ownership: 81.0%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 195,190,800 shares
Distinct insiders: 0 buying, 0 selling
(2 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — BEARISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> SELL

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (downtrend)
- Trailing P/E 46.7 and forward P/E 30.8 indicate high valuation
- Debt/equity ratio 168.6% suggests high leverage
- Earnings record: 1 beat, 3 missed in last four quarters

<details><summary><b>News</b> — score +0.00</summary>

- [Q2 Online Marketplace Earnings: Etsy (NYSE:ETSY) Earns Top Marks](https://www.tradingview.com/news/stockstory:b63c9fd27094b:0-q2-online-marketplace-earnings-etsy-nyse-etsy-earns-top-marks/)  
  <sub>TradingView, 11 hours ago</sub>  
  Looking back on online marketplace stocks' Q2 earnings, we examine this quarter's best and worst performers, including Etsy NYSE:ETSY and its peers.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 1,719.45 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 1,866.79 (-7.9%), 50d 1,868.76 (-8.0%), 200d 1,843.34 (-6.7%); 50d above 200d
Momentum: RSI(14) 33.1 | MACD -37.584 vs signal -18.733 (histogram -18.851)
Returns: 1d -1.9% | 5d -5.5% | 1m -10.9% | 3m +2.2%
52-week range: 1,546.81 - 2,501.31 (now 18.1% of the way up)
Volatility: ATR(14) 59.11 (3.4% of price) | annualised 20d 26.5%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 87.17B
Valuation: trailing P/E 46.72 | forward P/E 30.76 | P/B 11.13 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.40</summary>

```text
Earnings record, last 4 quarters: 1 beat, 3 missed
  2026-06-30 beat by 4% | 2026-03-31 missed by 7% | 2025-12-31 missed by 6% | 2025-09-30 missed by 13%
```

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 1.56 on a 1=strong buy to 5=strong sell scale, 25 analysts)
Ratings: 4 strong buy, 16 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,272.28 (+32.2% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-08-06 BTIG: reit, Buy -> Buy
  - 2026-07-15 Citigroup: main, Neutral -> Neutral
  - 2026-06-02 BTIG: reit, Buy -> Buy
Institutional ownership: 80.3%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: technicals are bearish (price below key SMAs, low RSI, low volume), fundamentals are neutral (high valuation offset by strong growth and earnings beats), analyst view modestly bullish (mean price target +15%), insider activity slightly bearish (executive sales). The contradictory inputs lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Price 709.91 below 20d SMA (725.35) and 200d SMA (770.08)
- Trailing P/E 53.38 (high valuation)
- Four consecutive earnings beats (10% to 21%)
- Mean analyst price target 816.33 (+15% vs last close)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 709.91 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 725.35 (-2.1%), 50d 761.92 (-6.8%), 200d 770.08 (-7.8%); 50d below 200d
Momentum: RSI(14) 37.1 | MACD -4.975 vs signal -6.752 (histogram 1.777)
Returns: 1d -3.4% | 5d -5.4% | 1m -1.2% | 3m -3.1%
52-week range: 454.95 - 1,014.33 (now 45.6% of the way up)
Volatility: ATR(14) 16.72 (2.4% of price) | annualised 20d 18.4%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 33.27B
Valuation: trailing P/E 53.38 | forward P/E 38.66 | P/B 7.53 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.9% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 10% | 2026-03-31 beat by 16% | 2025-12-31 beat by 16% | 2025-09-30 beat by 21%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+15.0% vs last close), range 518.00 - 960.00
Recent rating changes:
  - 2026-08-19 JP Morgan: main, Neutral -> Neutral
  - 2026-06-24 Jefferies: main, Hold -> Hold
  - 2026-05-27 Jefferies: main, Hold -> Hold
  - 2026-05-27 JP Morgan: main, Neutral -> Neutral
  - 2026-04-13 JP Morgan: main, Neutral -> Neutral
  - 2026-03-22 Jefferies: main, Hold -> Hold
Institutional ownership: 23.0%
Largest holders: Clal Insurance Enterprises Holdings Ltd (3.5%), Vanguard Capital Management LLC (1.6%), Van Eck Associates Corporation (1.2%), Y.D. More Investments Ltd (1.0%), Altshuler Shaham Ltd (1.0%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

```text
Last 180 days: bought 82,000 shares in 7 transaction(s) | sold 69,736 shares in 7
Net: +12,264 shares (+0.1% of insider holdings) | insiders hold 19,278,816 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-04-09 MACHLIS BEZHALEL (Chief Executive Officer): 25,514 shares, 22.64M
  - 2026-04-09 VERED YEHUDA (Officer): 5,953 shares, 5.28M
  - 2026-04-09 KRIL RAN (Officer): 6,803 shares, 6.04M
  - 2026-04-09 ARIEL JONATHAN (Officer): 7,654 shares, 6.79M
(5 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators are bearish (price below all major SMAs, negative momentum, very low volume) while fundamentals and analyst sentiment are moderately bullish (low trailing P/E, strong earnings growth, 4‑quarter beat streak, strong‑buy consensus). News provides only modest, non‑material catalysts. The contradictory signals lead to a neutral short‑term view with low conviction.

**Main reasons it gave:**
- Technical: price below 20‑day (193.74), 50‑day (190.32) and 200‑day (201.85) SMAs at 189.13; RSI 45.3; MACD negative; volume 0.08× 20‑day average
- Analyst consensus strong_buy with mean price target $234.08 (+23.8% vs last close)
- Four consecutive earnings beats and YoY earnings growth +86.9% indicate strong performance
- News: modest positive catalyst from buybacks (stock up 1.94%) and $200k CSR investment, but no major material catalyst

<details><summary><b>News</b> — score +0.20</summary>

- [Toyota and Truliant will help bring money lessons to more than 5,000 students a year.](https://www.stocktitan.net/news/TM/junior-achievement-of-the-triad-launches-finance-park-wy22w20pj85s.html)  
  <sub>Stock Titan, 41 minutes ago</sub>  
  Toyota (TM) and Truliant Federal Credit Union invested a combined $200,000 in Junior Achievement of the Triad's Finance Park Mobile.
- [REG - Renalytix PLC - Result of GM](https://www.tradingview.com/news/reuters.com,2026-09-28:newsml_RSb6078Wa:0-reg-renalytix-plc-result-of-gm/)  
  <sub>TradingView, 3 hours ago</sub>  
  RNS Number : 6078W Renalytix PLC 28 September 2026 TMRenalytix plc(“Renalytix” or the “Company”)Result of General MeetingLONDON and NEW YORK, 28 September...
- [Green Steel Environmental Returns to WEFTEC with Full-Scale Pilot Results for its Game-changing Wastewater Treatment Solution](https://www.investorideas.com/news/2026/water/09281-green-steel-environmental-returns-to-weftec-with-full-scale-pilot-results-for-its-game-changing-wastewater-treatment-solution.asp)  
  <sub>Investorideas.com, 1 hour ago</sub>  
  A year after debuting Green Steel PSR at WEFTEC 2025, the Boulder-based cleantech company brings performance data from its first full-scale deployment at...
- [A new platform is set to give utilities a live view of water, sewer and stormwater systems without replacing existing tools.](https://www.stocktitan.net/news/BMI/badger-meter-introduces-one-network-tm-software-platform-for-water-f16wvmxxa357.html)  
  <sub>Stock Titan, 30 minutes ago</sub>  
  It combines smart-meter, network-monitoring and water-quality data with alerts; North American availability is planned for September 2026.
- [Toyota Motor stock gains 1.94 percent as buybacks continue](https://www.ad-hoc-news.de/boerse/news/corporate-news/toyota-motor-stock-gains-1-94-percent-as-buybacks-continue/70191716)  
  <sub>AD HOC NEWS, 6 hours ago</sub>  
  TM, US8923313071. Toyota Motor stock gains 1.94 percent as buybacks continue. Published on 09/28/2026 at 10:30 | Editorial responsibility: Rafael Müller,...
- [Toyota’s $6.4 Billion Factory Bet Could Reshape its Manufacturing Future](https://www.insidermonkey.com/news/toyotas-6-4-billion-factory-bet-could-reshape-its-manufacturing-future-1845123/?amp=1)  
  <sub>Insider Monkey, 18 hours ago</sub>  
  Toyota Motor Corporation (NYSE:TM) estimates that modernizing its factories could require about 1 trillion yen ($6.4 billion) annually from 2028,...
- [A new broadband platform supports up to 12-gigabit internet speeds on existing cable networks](https://www.stocktitan.net/news/MXL/max-linear-launches-puma-tm-9-enabling-operators-to-accelerate-ai-k94bx4njevq2.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  One platform supports DOCSIS 3.1, 3.1+ and 4.0, Wi-Fi 8 and DDR5 memory. Puma 9 is available to operators and OEMs developing next-generation gateways.
- [Cochin Shipyard Acquires Strategic Stake in Conoship | TCPL Packaging Forms Battery Materials Subsidiary | Top Buzzing Stocks Today](https://www.equitymaster.com/indian-share-markets/09/28/2026/Cochin-Shipyard-Acquires-Strategic-Stake-in-Conoship--TCPL-Packaging-Forms-Battery-Materials-Subsidiary--Top-Buzzing-Stocks-Today?utm_source=todays-market-plug&utm_medium=website&utm_campaign=content&utm_content=TM)  
  <sub>Equitymaster, 14 hours ago</sub>  
  Top cues to track in today's stock market session.
- [Operational data will help the FAA refine tools for spotting flight conflicts](https://www.stocktitan.net/news/PLTR/surf-air-mobility-selected-as-participating-airspace-user-in-faa-s-5jd0qd2z8t13.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Surf Air Mobility's participation draws on its experience with Part 135 scheduled airline operations and on its SurfOS<sup>TM</sup> data infrastructure and operating...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 189.13 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 193.74 (-2.4%), 50d 190.32 (-0.6%), 200d 201.85 (-6.3%); 50d below 200d
Momentum: RSI(14) 45.3 | MACD -0.387 vs signal 0.602 (histogram -0.989)
Returns: 1d -0.6% | 5d -1.7% | 1m -1.5% | 3m +10.4%
52-week range: 166.50 - 248.29 (now 27.7% of the way up)
Volatility: ATR(14) 3.20 (1.7% of price) | annualised 20d 22.1%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 223.97B
Valuation: trailing P/E 8.55 | forward P/E 11.99 | P/B 15.00 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+23.8% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

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

- [ASML Holding N.V. (ASML) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/ASML/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  ASML Holding N.V. Overview Semiconductor Equipment & Materials / Technology.
- [ASML Warns Trump on China Chip Restrictions - ASML Holding (NASDAQ:ASML)](https://www.benzinga.com/trading-ideas/long-ideas/26/09/62024081/asml-china-trump-warning)  
  <sub>Benzinga, 21 minutes ago</sub>  
  ASML CEO Christophe Fouquet warns that excessive China restrictions could accelerate domestic chip technology.
- [ASML High-NA EUV: Why TSMC, Samsung and Intel Are Betting on It](https://www.indmoney.com/blog/us-stocks/asml-high-na-euv-tsmc-samsung-intel)  
  <sub>INDmoney, 7 hours ago</sub>  
  ASML's High-NA EUV could make advanced chip manufacturing more efficient. See why TSMC, Samsung and Intel are adopting it and what it means for ASML stock.
- [ASML CEO Highlights Barriers in EUV Lithography Market](https://www.gurufocus.com/news/9099329/asml-ceo-highlights-barriers-in-euv-lithography-market)  
  <sub>GuruFocus, 6 hours ago</sub>  
  On September 28, 2026, ASML's CEO, Christoph H. de Vries, highlighted the formidable challenges in manufacturing extreme ultraviolet (EUV) lithography...
- [ASML Holding N.V. : UBS reiterates its Buy rating](https://www.marketscreener.com/news/asml-holding-n-v-ubs-reiterates-its-buy-rating-ce785adcdf89f327)  
  <sub>www.marketscreener.com, 2 hours ago</sub>  
  In a research note published by Francois-Xavier Bouvignies, UBS advises its customers to buy the stock. The target price is unchanged and still at EUR 2350.
- [What company Is ASML? Between ASML and AMD, Which Is a Better Investment?](https://www.tradingkey.com/analysis/stocks/us-stocks/261749862-asml-amd-investment-tradingkey)  
  <sub>TradingKey, 18 hours ago</sub>  
  TradingKey - ASML Holding N.V. (NASDAQ: ASML) is not a chip designer; instead, it's best understood as a supplier of equipment for producing semiconductors...
- [Lam Research: A Key AI Infrastructure Player With Growth Upside (NASDAQ:LRCX)](https://seekingalpha.com/article/4950185-lam-research-stock-key-ai-infrastructure-player-with-growth-upside)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Lam Research (LRCX) could gain from rising AI CapEx and data center buildouts; margin strength may drive a 30x P/E re-rating.
- [ASML Holding stock rises 1.29 percent as target is cut](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-holding-stock-rises-1-29-percent-as-target-is-cut/70193039)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  ASML Holding stock faced a Morgan Stanley target cut to EUR 1700 from EUR 1930 on September 8, 2026. Q2 revenue rose 21.30 percent year over year.
- [ASML N : reports transactions under its current share buyback program](https://www.marketscreener.com/news/asml-n-reports-transactions-under-its-current-share-buyback-program-ce785adcdf8bf627)  
  <sub>www.marketscreener.com, 2 hours ago</sub>  
  ASML's current share buyback program was announced on 28 January 2026, and details are available on our website. This regular update of the transactions...
- [META Stock Dips Premarket After Q2 Report: Meta’s Forecast Miss Has Investors Worried, Retail Turns More Bearish](https://stocktwits.com/news-articles/markets/equity/meta-stock-dips-premarket-after-q2-report-meta-s-forecast-miss-has-investors-worried-retail-turns-more-bearish/cZNPD4NRJcJ)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Traders intensely debated whether the post-earnings sell-off represents a catastrophic break of support or a bargain buying opportunity.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,750.25 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 1,689.18 (+3.6%), 50d 1,717.63 (+1.9%), 200d 1,528.12 (+14.5%); 50d above 200d
Momentum: RSI(14) 55.3 | MACD 2.172 vs signal -10.434 (histogram 12.606)
Returns: 1d +0.4% | 5d +2.3% | 1m +0.9% | 3m -7.1%
52-week range: 936.19 - 1,989.44 (now 77.3% of the way up)
Volatility: ATR(14) 50.28 (2.9% of price) | annualised 20d 40.3%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 672.27B
Valuation: trailing P/E 60.46 | forward P/E 29.71 | P/B 1,502.41 | PEG 1.58
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.36 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 2 beats, 1 in line, 1 missed
  2026-06-30 beat by 9% | 2026-03-31 beat by 7% | 2025-12-31 missed by 5% | 2025-09-30 in line
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
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,117.03 (+21.0% vs last close), range 879.34 - 2,815.78
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,414,222 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [A deeper Colorado drill hole showed copper minerals too, though Solitario expected molybdenum alone.](https://www.stocktitan.net/news/XPL/drilling-at-cat-creek-intersects-a-copper-molybdenum-porphyry-system-ifdsyz1qsqyd.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Solitario Resources (XPL) reported visible copper-molybdenum mineralization in its first two drill holes at Cat Creek in Colorado.
- [Nvidia's new AI platform, Nor'easter flight delays, NFL's drone focus and more in Morning Squawk](https://www.cnbc.com/2026/09/28/5-things-to-know-before-the-stock-market-opens.html)  
  <sub>CNBC, 3 hours ago</sub>  
  Here are five key things investors need to know to start the trading day.
- [Dell To Officially Join Tesla, Oracle, Caterpillar In Texas As Stock Eyes Best Year Since Returning To Public Markets](https://stocktwits.com/news-articles/markets/equity/dell-to-officially-join-tesla-oracle-caterpillar-in-texas-as-stock-eyes-best-year-since-returning-to-public-markets/cZ1cXbeR7g3)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Wall Street believes it might have some more room to run. Currently, 19 out of 27 analysts rate the stock 'Buy' or higher, and eight rate it 'Hold,' with an...
- [Advanced AI-Powered Crypto Investment Research Platform](https://sosovalue.com/stocks/t)  
  <sub>SoSoValue, 6 hours ago</sub>  
  The following metrics are calculated using stock market data. High$25.44. Low$25.22. Avg Price$25.35. Range %0.86%. Turnover Ratio0.34%. 52wk High$28.75.
- [How Long Can You Really Leave A Cat Alone? Veterinarians Are Clearer Than You Would Expect](https://studyfinds.com/ow-long-can-you-really-leave-cats-alone-2180/)  
  <sub>StudyFinds, 2 hours ago</sub>  
  How long can you leave a cat alone? Vets say healthy adult cats can typically handle 8 to 12 hours. Kittens and senior cats need far more frequent checks.
- [Catecoin (cate.meme) price today, CATE to USD live price, marketcap and chart](https://coinmarketcap.com/currencies/catecoin-cate-meme/)  
  <sub>CoinMarketCap, 6 hours ago</sub>  
  The cat version of Doge. Born from the same pure meme energy that turned a Shiba Inu into a global phenomenon, C* is the feline answer to the internet's...
- [Caterpillar stock at USD 821.58 on September 25, 2026](https://www.ad-hoc-news.de/boerse/news/vorboerse/caterpillar-stock-at-usd-821-58-on-september-25-2026/70191364)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  Caterpillar stock last traded at USD 821.58 on September 25, 2026, up 2.03 percent. The company has also announced a collaboration with FieldAI focused on...
- [This Analyst Sees 34% Upside For SRPT Stock — Here's Why They Expect A Sustained Rally Next](https://stocktwits.com/news-articles/markets/equity/srpt-stock-bullish-upgrade-novartis-readthrough-other-catalysts/cZmovIpR7nb)  
  <sub>Stocktwits, 20 hours ago</sub>  
  Sarepta Therapeutics Inc. (SRPT) shares were in focus on Thursday after a new analyst upgrade as Wall Street keeps an eye on multiple potential catalysts...
- [7 Essential Foods To Stock Up For Emergencies](https://www.ndtv.com/webstories/feature/7-essential-foods-to-stock-up-for-emergencies-52903)  
  <sub>NDTV, 20 hours ago</sub>  
  When stocking an emergency pantry, prioritise items that are high in calories, require little to no cooking or water, and have a long shelf life.
- [Distraught owners find cat's body after tail posted through letterbox](https://www.manchestereveningnews.co.uk/news/uk-news/distraught-owners-find-cats-body-34682064.amp)  
  <sub>Manchester Evening News, 3 hours ago</sub>  
  The devastated owners of a cat whose severed tail was posted through their letterbox have now found his remains in woodland.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 820.87 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 804.33 (+2.1%), 50d 828.05 (-0.9%), 200d 790.70 (+3.8%); 50d above 200d
Momentum: RSI(14) 52.0 | MACD -4.557 vs signal -9.229 (histogram 4.672)
Returns: 1d -0.1% | 5d +0.5% | 1m +0.5% | 3m -20.5%
52-week range: 465.76 - 1,064.90 (now 59.3% of the way up)
Volatility: ATR(14) 21.70 (2.6% of price) | annualised 20d 25.4%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 377.33B
Valuation: trailing P/E 35.31 | forward P/E 25.35 | P/B 19.46 | PEG 1.42
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 2.0% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 31% | 2026-03-31 beat by 19% | 2025-12-31 beat by 9% | 2025-09-30 beat by 8%
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
Consensus: buy (mean 2.07 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 14 buy, 11 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+18.9% vs last close), range 575.00 - 1,225.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

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

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### HDFC Bank (HDB) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [HDB Shareholder Alert: HDFC Bank Limited Securities Class](https://www.globenewswire.com/news-release/2026/09/28/3369984/3080/en/hdb-shareholder-alert-hdfc-bank-limited-securities-class-action-lawsuit-investors-should-contact-levi-korsinsky.html)  
  <sub>GlobeNewswire, 31 minutes ago</sub>  
  Notice to Pension Funds, Asset Managers, and Fiduciaries: HDFC Bank Limited (NYSE: HDB) allegedly routed approximately Rs 45 crore ($4.7 million) of...
- [Vietnam Stock Market Live: VNI Index Trading in Red by 0.16%; Hanoi’s HNX Index Slips 0.43% to 271.05 Points – Check Stocks in Focus, Investor Outlook & More](https://sundayguardianlive.com/business/vietnam-stock-market-live-vni-index-trading-in-red-by-016-hanois-hnx-index-slips-043-to-27105-points-check-stocks-in-focus-investor-outlook-more-294261/amp/)  
  <sub>The Sunday Guardian, 11 hours ago</sub>  
  This morning, Vietnam's benchmark index VNI is down by 0.16%. While Hanoi's HNX index has seen a 0.43% drop after also opening in red.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.41 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 22.84 (-1.9%), 50d 23.21 (-3.5%), 200d 27.33 (-18.0%); 50d below 200d
Momentum: RSI(14) 43.5 | MACD -0.137 vs signal -0.166 (histogram 0.029)
Returns: 1d -2.6% | 5d -5.3% | 1m -0.2% | 3m -13.5%
52-week range: 21.84 - 37.18 (now 3.7% of the way up)
Volatility: ATR(14) 0.54 (2.4% of price) | annualised 20d 36.2%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 115.15B
Valuation: trailing P/E 15.67 | forward P/E 16.10 | P/B 9.02 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.40 | short interest 0.7% of float
Next earnings: 2026-10-17
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
Price target: mean 30.52 (+36.2% vs last close), range 26.10 - 35.00
Recent rating changes:
  - 2024-07-22 JP Morgan: down, Overweight -> Neutral
  - 2019-09-09 Bernstein: down, Outperform -> Market Perform
  - 2019-06-11 Nomura: down, Buy -> Neutral
  - 2017-03-21 Morgan Stanley: down, Overweight -> Equal-Weight
  - 2016-09-14 Goldman Sachs: main, ? -> Buy
  - 2015-03-11 Societe Generale: init, ? -> Buy
Institutional ownership: 13.6%
Largest holders: Morgan Stanley (1.0%), Royal Bank of Canada (0.8%), Schroder Investment Management Group (0.4%), JPMORGAN CHASE & CO (0.4%), Bank of America Corporation (0.3%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 6,928,096 shares
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

- [JPMorgan Stock Sits 6% Below Its High After a Record Year. Here’s What Q3 Earnings Must Prove](https://www.tikr.com/blog/jpmorgan-stock-sits-6-below-its-high-after-a-record-year-heres-what-q3-earnings-must-prove?)  
  <sub>TIKR.com, 1 hour ago</sub>  
  Here's why JPMorgan's record 2026 still leaves only modest upside at today's price.
- [JPMorgan Chase & Co. (NYSE:JPM) Stock Price Target Raised at HSBC](https://www.marketbeat.com/instant-alerts/analyst-jpmorgan-chase-co-nyse-jpm-stock-price-target-raised-at-hsbc-2026-09-28/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  HSBC upped their target price on shares of JPMorgan Chase & Co. from $369.00 to $377.00 and gave the stock a "hold" rating in a research note on Monday.
- [Why Did IMAX, JPM, CSX Stocks Surge To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/imax-jpm-csx-stocks-52-week-highs-last-week/cZZxcQ3R7C3)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Citi raised the price target on CSX to $54 from $53 and maintained a Neutral rating on the shares, implying an upside of about 1.5% from its last close.
- [Citigroup aims to raise $3B in Banamex IPO - report (C:NYSE)](https://seekingalpha.com/news/4647496-citigroup-aims-to-raise-3b-in-banamex-ipo---report)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Citigroup plans a January IPO for Mexico's Banamex, aiming to raise $3B+ with BAC, GS and JPM.
- [REG - Beazley PLC JPMorgan Chase & Co - Holding(s) in Company](https://www.tradingview.com/news/reuters.com,2026-09-28:newsml_RSb5900Wa:0-reg-beazley-plc-jpmorgan-chase-co-holding-s-in-company/)  
  <sub>TradingView, 5 hours ago</sub>  
  RNS Number : 5900W Beazley PLC 28 September 2026 TR-1: Standard form for notification of major holdings1. Issuer DetailsISINGB00BYQ0JC66Issuer NameBEAZLEY...
- [Should JPMorgan Investors Fear Meta’s Muse? Here’s What the Deposit Data Shows](https://www.tikr.com/blog/should-jpmorgan-investors-fear-metas-muse-heres-what-the-deposit-data-shows)  
  <sub>TIKR.com, 5 hours ago</sub>  
  JPMorgan shares lost more than 3% in the first days of the week of September 21 as investors worried Meta's Muse AI agent could pull deposits toward...
- [JP Morgan forecasts a 20x revenue increase for this AI stock](https://ukinvestormagazine.co.uk/jp-morgan-forecasts-a-20x-revenue-increase-for-this-ai-stock/)  
  <sub>UK Investor Magazine, 5 hours ago</sub>  
  US-listed IREN is forecast to see a 20x increase in revenue by 2030, according to JP Morgan, as demand for compute continues to balloon and the price...
- [A Decade of JPMorgan Chase Delivered 572% Returns but This Year Tells a Different Story](https://finance.yahoo.com/markets/stocks/articles/decade-jpmorgan-chase-delivered-572-152856455.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  JPMorgan (JPM) turned a $1,000 investment in 2016 into roughly $6,700 by 2026, a 572% gain driven by deposit dominance and surging fee revenue.
- [Athena Investment Management Sells 5,294 Shares of JPMorgan Chase & Co. $JPM](https://www.marketbeat.com/instant-alerts/filing-athena-investment-management-sells-5294-shares-of-jpmorgan-chase-co-jpm-2026-09-28/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Athena Investment Management reduced its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 21.8% in the 2nd quarter, according to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 339.99 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 350.38 (-3.0%), 50d 353.32 (-3.8%), 200d 321.46 (+5.8%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -3.640 vs signal -2.090 (histogram -1.550)
Returns: 1d -0.9% | 5d -3.4% | 1m -4.0% | 3m +3.2%
52-week range: 282.84 - 365.18 (now 69.4% of the way up)
Volatility: ATR(14) 6.52 (1.9% of price) | annualised 20d 18.4%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 903.77B
Valuation: trailing P/E 14.57 | forward P/E 13.61 | P/B 2.56 | PEG 1.57
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 0.9% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3% | 2025-09-30 beat by 4%
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
Consensus: buy (mean 2.08 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 375.81 (+10.5% vs last close), range 305.00 - 436.00
Recent rating changes:
  - 2026-09-28 HSBC: main, Hold -> Hold
  - 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-03 UBS: main, Buy -> Buy
  - 2026-07-20 Citigroup: main, Neutral -> Neutral
  - 2026-07-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-07-16 B of A Securities: main, Buy -> Buy
Institutional ownership: 75.7%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 137,226 shares in 11 transaction(s) | sold 230,236 shares in 19
Net: -93,010 shares (-0.9% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
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

- [Eli Lilly and Company (LLY) is Attracting Investor Attention: Here is What You Should Know](https://uk.finance.yahoo.com/news/eli-lilly-company-lly-attracting-120006354.html)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  Recently, Zacks.com users have been paying close attention to Lilly (LLY). This makes it worthwhile to examine what the stock has in store.
- [Eli Lilly Wins FDA Approval for Weekly Insulin. Here’s What Comes Next](https://www.tikr.com/blog/eli-lilly-wins-fda-approval-for-weekly-insulin-heres-what-comes-next)  
  <sub>TIKR.com, 1 hour ago</sub>  
  Here's why Lilly's weekly insulin approval strengthens a growth story the model still prices attractively.
- [Lilly targets diabetes, obesity treatment parity before 2040 | LLY Stock News](https://www.stocktitan.net/news/LLY/lilly-launches-the-lilly-change-the-course-commitment-aiming-to-ozr70ibvykng.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Lilly (LLY) launched an initiative targeting equal diabetes and obesity treatment reach in resource-limited and high-income settings before 2040.
- [Stock Market Today: S&P 500, Dow, Nasdaq 100 Futures Fall as Rising Yields and Trump's Rejection of Hormu](https://www.benzinga.com/markets/equities/26/09/62016443/stock-market-today-sp-500-dow-jones-futures-fall-as-rising-yields-and-trumps-hormuz-deal-rejection-spook-investors-lly-pep-jef-in-focus)  
  <sub>Benzinga, 2 hours ago</sub>  
  U.S. stock futures declined on Monday, as the Dow Jones, S&P 500, and Nasdaq 100 indices fell, following Friday's higher close.
- [Eli Lilly Wavered Over the Last Month: One of Wall Street's Biggest Banks Says 35% Gains Still to Come](https://247wallst.com/investing/2026/09/28/eli-lilly-wavered-over-the-last-month-one-of-wall-streets-biggest-banks-says-35-gains-still-to-come/?tpid=1669130&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Citigroup sees a path to 35% gains from here, but Eli Lilly's pricing headwinds, a slow oral GLP-1 launch, and a rival in freefall raise a real question...
- [LLY Stock Climbs As Oral GLP-1 Pill Beats Novo Nordisk, AstraZeneca’s Therapies In Diabetes Trials](https://stocktwits.com/news-articles/markets/equity/lly-stock-climbs-as-oral-glp-1-pill-crushes-rivals-in-diabetes-trials/cZ0vSJmR7bG)  
  <sub>Stocktwits, 16 hours ago</sub>  
  According to data from Koyfin, all nine of the analysts covering ZVRA rate it 'Buy' or higher. The stock has an average 12-month price target of $23,...
- [Eli Lilly Launches Global Initiative to Expand Access to Diabetes and Obesity Drugs (LLY)](https://www.gurufocus.com/news/9099576/eli-lilly-launches-global-initiative-to-expand-access-to-diabetes-and-obesity-drugs-lly)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 28, 2026, Eli Lilly and Co (NYSE: LLY) announced the Lilly Change the Course Commitment, a groundbreaking global health initiative aimed at...
- [LLY's Olumiant Gets FDA Nod for Expanded Use in Pediatric Hair Loss](https://www.zacks.com/stock/news/2996782/llys-olumiant-gets-fda-nod-for-expanded-use-in-pediatric-hair-loss)  
  <sub>Zacks Investment Research, 9 minutes ago</sub>  
  Eli Lilly's Olumiant wins FDA nod to treat pediatric patients 12 years of age and older with severe alopecia areata, expanding its U.S. use after strong...
- [Why Are Investors Watching Eli Lilly and Company (NYSE:LLY) in Blue-Chip Stocks Right Now?](https://kalkinemedia.com/us/stocks/bluechip/why-are-investors-watching-eli-lilly-and-company-nyselly-in-blue-chip-stocks-right-now)  
  <sub>Kalkine Media, 2 hours ago</sub>  
  Eli Lilly and Company (NYSE:LLY) is in the spotlight in Blue-Chip Stocks after a fresh development. Here is what changed, why it matters, and what to watch...
- [Stocktwits Pharma Pulse: Lilly, Novo Lead A Busy Week — Here Are The Stocks And Readouts To Watch](https://finance.yahoo.com/healthcare/articles/stocktwits-pharma-pulse-lilly-novo-033120543.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  Lilly will present Phase 2 results for its eloraTZP combination at the EASD meeting in Milan. SAB BIO, Sana and Century will present type 1 diabetes...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,189.26 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 1,151.54 (+3.3%), 50d 1,177.61 (+1.0%), 200d 1,071.13 (+11.0%); 50d above 200d
Momentum: RSI(14) 57.2 | MACD -0.525 vs signal -7.144 (histogram 6.619)
Returns: 1d +0.5% | 5d +2.1% | 1m +1.1% | 3m -3.3%
52-week range: 724.54 - 1,280.34 (now 83.6% of the way up)
Volatility: ATR(14) 31.63 (2.7% of price) | annualised 20d 18.4%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.06T
Valuation: trailing P/E 39.88 | forward P/E 25.01 | P/B 31.29 | PEG 1.14
Profitability: profit margin 33.5% | operating margin 54.2% | ROE 102.3%
Growth (YoY): revenue +47.7% | earnings +26.2%
Balance sheet: debt/equity 162.1% | free cash flow 11.07B
Risk: beta 0.50 | short interest 0.8% of float
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
Consensus: buy (mean 1.63 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 6 strong buy, 19 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,328.83 (+11.7% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
  - 2026-09-18 Guggenheim: main, Buy -> Buy
  - 2026-09-10 HSBC: main, Reduce -> Reduce
  - 2026-08-07 Truist Securities: main, Buy -> Buy
  - 2026-08-06 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
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
Net: -306,736 shares (-18.0% of insider holdings) | insiders hold 1,399,430 shares
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

- [Microsoft Rolls Out Refreshed Copilot App as Stock Lags Megacap Peers](https://www.tikr.com/blog/microsoft-msft-stock-copilot-app-launch-cowork-code-autopilot)  
  <sub>TIKR.com, 2 hours ago</sub>  
  Price change for Microsoft stock in last 6 months: 41%; $MSFT Stock Price as of Sep. 25: $516; 52-Week High: $554; $MSFT Stock Price Target: $577.
- [3 Cash-Heavy Stocks with Impressive Fundamentals](https://stockstory.org/us/stocks/nasdaq/msft/news/buy-or-sell/3-cash-heavy-stocks-with-impressive-fundamentals)  
  <sub>StockStory, 5 hours ago</sub>  
  In a world where many businesses have shaky balance sheets, some have ignored the crowd and exercised prudence. These cash-heavy companies shine bright for...
- [Microsoft: Why The $3.8T Fortress Won't Deliver An AI Moonshot (NASDAQ:MSFT)](https://seekingalpha.com/article/4950262-microsoft-why-the-3-8t-fortress-wont-deliver-an-ai-moonshot)  
  <sub>Seeking Alpha, 16 minutes ago</sub>  
  Microsoft Corporation stock has rebounded to $516, reflecting market optimism, but it faces a fundamental strategic shift. MSFT's AI partnership with OpenAI...
- [Microsoft (MSFT) Stock Soars with AI-Focused Strategy](https://www.gurufocus.com/news/9099288/microsoft-msft-stock-soars-with-aifocused-strategy)  
  <sub>GuruFocus, 7 hours ago</sub>  
  On September 28, 2026, Microsoft (MSFT) has made headlines with its strategic positioning as a software company that operates independently from major AI...
- [Satya Nadella Says Xbox Is on Track for a Comeback After Major Layoffs — ‘I Feel Fantastic’ About Its Gaming IP](https://www.benzinga.com/markets/equities/26/09/62020149/satya-nadella-says-xbox-is-on-track-for-a-comeback-after-major-layoffs-i-feel-fantastic-about-its-gaming-ip)  
  <sub>Benzinga, 2 hours ago</sub>  
  Microsoft Corp.'s (NASDAQ:MSFT) CEO, Satya Nadella, expressed confidence in the future of Xbox amid major restructuring and layoffs. Nadella, on the Sources...
- [Microsoft Copilot Is Turning Into An ‘AI Operating System’ — Here’s What It Means For MSFT Stock, According To Oppenheimer’s Brian Schwartz](https://stocktwits.com/news-articles/markets/equity/msft-copilot-operating-system-higher-engagement-monetization-oppenheinmer/cZMgQ8IRBOw)  
  <sub>Stocktwits, 14 hours ago</sub>  
  During an interview with CNBC, Schwartz said Microsoft's Copilot announcement changes the narrative around the company as investors continue to search for...
- [Is Microsoft (MSFT) Fully Priced As AI And Quantum News Builds?](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/is-microsoft-msft-fully-priced-as-ai-and-quantum-news-builds)  
  <sub>Simply Wall Street, 10 hours ago</sub>  
  Microsoft (MSFT) has been in focus after fresh client and partner announcements across security, quantum research, telecom data, and industry specific AI,...
- [Microsoft Stock Forecast: Copilot Gets Major Upgrade, Autopilot Can Run Continuously, Can MSFT Keep Rising?](https://www.tradingkey.com/analysis/stocks/us-stocks/262188925-copilot-autopilot-msft-microsoftcorp-jay-tradingkey)  
  <sub>TradingKey, 11 hours ago</sub>  
  TradingKey - On September 25, Eastern Time, Microsoft (MSFT) unveiled the next-generation Microsoft Copilot and announced three features: Home, Code,...
- [Microsoft (MSFT) Stock Price, Quote & Analysis](https://www.tipranks.com/stocks/msft)  
  <sub>TipRanks, 19 hours ago</sub>  
  Disclaimer: The TipRanks Smart Score performance is based on backtested results. Backtested performance is not an indicator of future actual results. The...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 506.82 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 499.70 (+1.4%), 50d 478.07 (+6.0%), 200d 432.13 (+17.3%); 50d above 200d
Momentum: RSI(14) 57.1 | MACD 6.780 vs signal 7.397 (histogram -0.617)
Returns: 1d -1.8% | 5d +1.0% | 1m +0.3% | 3m +37.5%
52-week range: 352.83 - 542.07 (now 81.4% of the way up)
Volatility: ATR(14) 11.93 (2.4% of price) | annualised 20d 25.4%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.76T
Valuation: trailing P/E 28.22 | forward P/E 21.41 | P/B 8.51 | PEG 1.62
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.11 | short interest 0.9% of float
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
Consensus: strong_buy (mean 1.33 on a 1=strong buy to 5=strong sell scale, 52 analysts)
Ratings: 14 strong buy, 39 buy, 2 hold, 0 sell, 0 strong sell
Price target: mean 577.26 (+13.9% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-09-23 Stifel: up, Hold -> Buy
  - 2026-09-22 Oppenheimer: main, Outperform -> Outperform
  - 2026-09-21 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - 2026-09-04 Stifel: main, Hold -> Hold
  - 2026-09-01 B of A Securities: main, Buy -> Buy
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
Net: +271,300 shares (+4.2% of insider holdings) | insiders hold 6,831,502 shares
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

- [NVIDIA Announces a $150 Billion Share Repurchase Authorization Increase](https://nvidianews.nvidia.com/news/nvidia-announces-a-150-billion-share-repurchase-authorization-increase)  
  <sub>NVIDIA Newsroom, 4 hours ago</sub>  
  NVIDIA today announced that its Board of Directors has authorized an additional $150 billion under the company's existing share repurchase program,...
- [Nvidia announces jaw-dropping $150 billion stock buyback, largest single authorization in history](https://finance.yahoo.com/technology/article/nvidia-announces-jaw-dropping-150-billion-stock-buyback-largest-single-authorization-in-history-121342628.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The valuation on Nvidia (NVDA) is too appetizing for CEO Jensen Huang to ignore any longer. The king of AI chips revealed a stunning new $150 billion stock...
- [Stocks making the biggest moves premarket: Meta Platforms, United Airlines, Nvidia & more](https://www.cnbc.com/2026/09/28/stocks-making-the-biggest-moves-premarket-meta-ual-nvda.html)  
  <sub>CNBC, 3 hours ago</sub>  
  ... and Financial News, Stock Quotes, and Market Data and Analysis. Market Data Terms of Use and Disclaimers. Data also provided by Reuters logo.
- [Nvidia Adds Record $150 Billion to Stock Buyback](https://www.wsj.com/tech/ai/nvidia-adds-record-150-billion-to-stock-buyback-910f96a8)  
  <sub>WSJ, 1 hour ago</sub>  
  Board approves share-repurchase program, bringing total buyback authorization to $235 billion.
- [Nvidia’s 2026 Dividend Hike Puts Dividend Growth Stocks in the Spotlight](https://global.morningstar.com/en-nd/stocks/nvidias-2026-dividend-hike-puts-dividend-growth-stocks-spotlight)  
  <sub>Morningstar, 8 hours ago</sub>  
  The Nvidia news also comes at a time when the Morningstar US Dividend Growth Index is neck and neck with the broad US stock market, which is unusual in an...
- [Why Is NVIDIA Stock Gaining Monday? - NVIDIA (NASDAQ:NVDA)](https://www.benzinga.com/markets/buybacks/26/09/62018971/nvidia-flexes-its-cash-muscle-with-record-150-billion-buyback-increase)  
  <sub>Benzinga, 2 hours ago</sub>  
  NVIDIA Corp. (NASDAQ:NVDA) stock gained nearly 2% in Monday premarket trading after the board significantly expanded its share repurchase program,...
- [Nvidia Boosts Share Buyback by a Record $150 Billion](https://www.bloomberg.com/news/articles/2026-09-28/nvidia-boosts-share-buyback-authorization-by-150-billion-mul5jmu7)  
  <sub>Bloomberg, 3 hours ago</sub>  
  Nvidia Corp., the chip developer at the heart of the artificial intelligence boom, increased the size of its share buyback plan by a record $150 billion,...
- [Why Nvidia (NVDA) Stock Is Trading Up Today](https://markets.financialcontent.com/stocks/article/stockstory-2026-9-28-why-nvidia-nvda-stock-is-trading-up-today)  
  <sub>FinancialContent, 21 minutes ago</sub>  
  Shares of leading designer of graphics chips Nvidia (NASDAQ: NVDA) jumped 2.7% in the morning session after the company authorized an additional $150...
- [NVDA Stock Rides Massive AI Spending And Bold Growth Bets](https://www.timothysykes.com/news/nvidia-corporation-nvda-news-2026_09_28/)  
  <sub>Timothy Sykes, 1 hour ago</sub>  
  NVIDIA Corporation stocks have been trading up by 2.06 percent after upbeat AI chip demand headlines lifted investor optimism. Key Takeaways CEO Jensen...
- [Biggest stock movers Monday: MDB, NVDA, and more](https://seekingalpha.com/news/4647444-biggest-stock-movers-monday-gfi-nio-and-more)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock futures were lower Monday morning as Washington rejected Iran's truce offer, sending Brent crude above $107 and Treasury yields toward 5% alongside...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 230.97 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 222.43 (+3.8%), 50d 216.54 (+6.7%), 200d 199.70 (+15.7%); 50d above 200d
Momentum: RSI(14) 60.4 | MACD 2.761 vs signal 2.084 (histogram 0.676)
Returns: 1d +2.6% | 5d +1.6% | 1m +1.3% | 3m +18.5%
52-week range: 165.17 - 235.74 (now 93.2% of the way up)
Volatility: ATR(14) 6.03 (2.6% of price) | annualised 20d 28.8%
Volume: 0.49x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.58T
Valuation: trailing P/E 29.24 | forward P/E 14.73 | P/B 24.36 | PEG 0.48
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
Consensus: strong_buy (mean 1.30 on a 1=strong buy to 5=strong sell scale, 59 analysts)
Ratings: 10 strong buy, 48 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 327.70 (+41.9% vs last close), range 180.00 - 515.00
Recent rating changes:
  - 2026-09-10 Piper Sandler: init, ? -> Overweight
  - 2026-09-04 Rosenblatt: main, Buy -> Buy
  - 2026-09-04 Needham: reit, Buy -> Buy
  - 2026-08-27 Citigroup: main, Buy -> Buy
  - 2026-08-27 Mizuho: main, Outperform -> Outperform
  - 2026-08-27 JP Morgan: main, Overweight -> Overweight
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

- [Can Novo Nordisk (NVO) Find a Second Act Before its First One Fades?](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nvo-second-act-015519811.html)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  A stock that has lost more than 70% of its value from the peak tends to invite hard questions, and Novo Nordisk A/S (NYSE:NVO) is now facing them from its...
- [LLY Stock Climbs As Oral GLP-1 Pill Beats Novo Nordisk, AstraZeneca’s Therapies In Diabetes Trials](https://stocktwits.com/news-articles/markets/equity/lly-stock-climbs-as-oral-glp-1-pill-crushes-rivals-in-diabetes-trials/cZ0vSJmR7bG)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Lilly's Foundayo outperformed existing treatments on blood sugar control and weight loss in type 2 diabetes patients in three late-stage trials.
- [Bristol Myers Squibb vs. Novo Nordisk: Which Healthcare Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/09/27/bristol-myers-squibb-vs-novo-nordisk-healthcare-stock-better-buy-2026/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  Bristol Myers Squibb (BMY +2.21%) and Novo Nordisk (NVO +0.47%) are heading in opposite directions this year. Bristol Myers Squibb raised its 2026 revenue...
- [Stocktwits Pharma Pulse: Lilly, Novo Lead A Busy Week — Here Are The Stocks And Readouts To Watch](https://www.tradingview.com/news/stocktwits:21d8d44a9094b:0-stocktwits-pharma-pulse-lilly-novo-lead-a-busy-week-here-are-the-stocks-and-readouts-to-watch/)  
  <sub>TradingView, 11 hours ago</sub>  
  Biotech investors face a crowded final week of September as Eli Lilly (LLY) and Novo Nordisk (NVO) bring their latest obesity and diabetes research to a...
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”
- [Novo’s Pipeline Strategy Takes Another Step Forward](https://www.insidermonkey.com/news/novos-pipeline-strategy-takes-another-step-forward-1843191/?amp=1)  
  <sub>Insider Monkey, 18 hours ago</sub>  
  Novo Nordisk A/S (NYSE:NVO) has signed a drug-discovery and licensing agreement with Orbis Medicines worth up to $1.4 billion to develop oral therapies for...
- [S&P 500, Dow, Nasdaq Drop As Yields Spike Amid Calls For More Rate Hikes — AMZN, GOOGL, NFLX, SPCX, RKLB In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-drop-as-yields-spike-amid-calls-for-more-rate-hikes-amzn-googl-nflx-spcx-rklb-in-focus/cZM4IxjRBB9)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Treasury yields jumped across the curve on Wednesday. Traders work on the floor of the New York Stock Exchange (NYSE) on July 23, 2026 in New York City.
- [DPZ Stock Pops Pre-Market As Domino’s ‘Hungry For More’ Strategy Drives 32nd Straight Year Of International Same-Store Sales Growth](https://stocktwits.com/news-articles/markets/equity/dpz-stock-rises-pre-market-dominos-hungry-for-more-q4-results/cZRt8KGR4yI)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The company said that its market share in the U.S. increased by another point, keeping it ahead of the Quick Service Restaurant pizza category.
- [SLS Stock In Spotlight After Vanguard Capital Discloses 5.19% Stake – Retail Calls It ‘Huge Vote Of Conviction’ As AML Trial Readout Nears](https://stocktwits.com/news-articles/markets/equity/sls-stock-in-spotlight-after-vanguard-capital-discloses-beneficial-stake/cZN4WEaRJPY)  
  <sub>Stocktwits, 20 hours ago</sub>  
  A new Schedule 13G filing showed Vanguard Capital Management owned 9.67 million SLS shares as of June 30, 2026.
- [Novo Nordisk A/S - share repurchase programme](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-share-repurchase-programme-135000341.html)  
  <sub>Yahoo Finance, 52 minutes ago</sub>  
  Bagsværd, Denmark, 28 September 2026 – On 6 May 2026, Novo Nordisk initiated a share repurchase programme in accordance with Article 5 of Regulation No...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.42 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 42.77 (-10.2%), 50d 45.56 (-15.7%), 200d 45.89 (-16.3%); 50d below 200d
Momentum: RSI(14) 30.0 | MACD -2.083 vs signal -1.627 (histogram -0.456)
Returns: 1d -1.0% | 5d -3.5% | 1m -16.9% | 3m -20.5%
52-week range: 35.29 - 63.98 (now 10.9% of the way up)
Volatility: ATR(14) 1.21 (3.1% of price) | annualised 20d 40.3%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 169.71B
Valuation: trailing P/E 9.63 | forward P/E 11.45 | P/B 4.98 | PEG 4.32
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.34 | short interest 0.8% of float
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
Price target: mean 46.27 (+20.4% vs last close), range 39.63 - 62.71
Recent rating changes:
  - 2026-09-11 Morgan Stanley: down, Equal-Weight -> Underweight
  - 2026-03-02 Goldman Sachs: down, Buy -> Neutral
  - 2026-02-24 JP Morgan: down, Overweight -> Neutral
  - 2026-01-09 CICC: init, ? -> Outperform
  - 2025-12-08 Argus Research: down, Buy -> Hold
  - 2025-11-28 Goldman Sachs: main, Buy -> Buy
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

### Procter & Gamble (PG) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Clorox Just Raised Its Dividend Again. Can Earnings Keep Up?](https://247wallst.com/investing/2026/09/28/clorox-just-raised-its-dividend-again-can-earnings-keep-up/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Clorox has raised its dividend for decades, but a cratering stock price, a payout ratio management calls elevated, and a debt load that ballooned after two...
- [Thirty families got a year's supply of diapers at Pampers' Los Angeles baby shower.](https://www.stocktitan.net/news/PG/pampers-4kira4moms-host-los-angeles-community-baby-shower-supporting-e4ei30w7p7h9.html)  
  <sub>Stock Titan, 19 hours ago</sub>  
  Families also got $100 Walmart gift cards and maternal health guidance from doulas and midwives, part of a three-year Pampers-4Kira4Moms partnership.
- [Realty Income, Stryker and more dividends 2026 • Vienna Stock Exchange](https://www.wienerborse.at/en/news/vienna-stock-exchange-news/realty-income-stryker-dividends-global-market-09302026)  
  <sub>Wiener Börse, 2 hours ago</sub>  
  Current Vienna Stock Exchange News: Realty Income, Stryker and more dividends 2026 ▻ inform now.
- [3 US Staples Stocks To Watch As Tariffs Pressure Everyday Consumer Spending](https://simplywall.st/stocks/us/household/nyse-chd/church-dwight/news/3-us-staples-stocks-to-watch-as-tariffs-pressure-everyday-co)  
  <sub>Simply Wall Street, 21 hours ago</sub>  
  Trade policy is back in the headlines, with G20 ministers descending on Milwaukee, tariffs still lifting the price of basics, and war in Iran adding another...
- [Procter & Gamble stock at USD 146.22 on September 25, 2026, up 0.37 percent](https://www.ad-hoc-news.de/boerse/news/vorboerse/procter-and-gamble-stock-at-usd-146-22-on-september-25-2026-up-0-37/70191377)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  Procter & Gamble was quoted at USD 146.22 on September 25, 2026, up 0.37 percent. The company plans to webcast its fiscal first-quarter results discussion...
- [Advanced AI-Powered Crypto Investment Research Platform](https://sosovalue.com/stocks/o)  
  <sub>SoSoValue, 23 hours ago</sub>  
  The following metrics are calculated using stock market data. High$55.66. Low$55.08. Avg Price$55.33. Range %1.06%. Turnover Ratio1.27%. 52wk High$66.58.
- [Why Is the Stock Market Falling Today? From US-Iran Talks to Crude Oil Prices, Key Reasons Behind the Decline](https://www.jagranjosh.com/general-knowledge/why-is-the-stock-market-falling-today-from-us-iran-talks-to-crude-oil-prices-key-reasons-behind-the-sensex-nifty-decline-1820012572-1)  
  <sub>Jagran Josh, 8 hours ago</sub>  
  Indian stock markets fall sharply as Sensex and Nifty decline amid US-Iran tensions, rising crude oil prices, elevated bond yields, and sustained foreign...
- [US stocks futures ease amid volatile crude oil prices](https://www.business-standard.com/markets/capital-market-news/us-stocks-futures-ease-amid-volatile-crude-oil-prices-126092800141_1.html)  
  <sub>Business Standard, 11 hours ago</sub>  
  The US stocks ended on postive note in last session but overall mood was cautious amid rising bond yields and volatile crude oil prices.
- [Hyundai among 3 stock ideas for today from Sachin Gupta of Choice Broking](https://www.business-standard.com/markets/news/hyundai-among-3-stock-ideas-for-today-from-sachin-gupta-of-choice-broking-126092800063_1.html)  
  <sub>Business Standard, 12 hours ago</sub>  
  Stocks to buy today: On the weekly chart, PGIL has given a breakout from a Pole & Flag pattern, supported by higher trading volumes, indicating strong...
- [Stock Alert: RCF, SAIL , JSW Energy, Augmont Enterprises, Balrampur Chini Mills](https://www.business-standard.com/markets/capital-market-news/stock-alert-rcf-sail-jsw-energy-augmont-enterprises-balrampur-chini-mills-126092800108_1.html)  
  <sub>Business Standard, 11 hours ago</sub>  
  Shares of Kaynes Technology, LIC Housing Finance, Manappuram Finance, SAIL are barred from F&O trading on Monday, 28 September 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 148.32 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 146.22 (+1.4%), 50d 145.94 (+1.6%), 200d 147.57 (+0.5%); 50d below 200d
Momentum: RSI(14) 57.0 | MACD 0.434 vs signal 0.253 (histogram 0.181)
Returns: 1d +1.4% | 5d +1.5% | 1m +3.6% | 3m -0.1%
52-week range: 138.04 - 167.20 (now 35.2% of the way up)
Volatility: ATR(14) 2.33 (1.6% of price) | annualised 20d 14.8%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 344.75B
Valuation: trailing P/E 22.40 | forward P/E 20.04 | P/B 6.46 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+8.3% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-08-07 Argus Research: down, Buy -> Hold
  - 2026-07-30 HSBC: down, Buy -> Hold
  - 2026-07-30 Citigroup: main, Buy -> Buy
  - 2026-07-21 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
  - 2026-07-10 B of A Securities: main, Buy -> Buy
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 90,364 shares in 25 transaction(s) | sold 40,243 shares in 13
Net: +50,121 shares (+2.4% of insider holdings) | insiders hold 2,115,234 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
  - 2026-08-21 RAMAN SUNDAR G. (Officer): 3,435 shares, 491.27K
  - 2026-08-20 JANZARUK MATTHEW W. (Officer): 156 shares, 22.43K
  - 2026-08-20 PURUSHOTHAMAN BALAJI (Officer): 2,019 shares, 290.31K
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Royal Bank of Canada (TSX:RY): What Is Driving Attention?](https://kalkinemedia.com/ca/stocks/bluechip/royal-bank-of-canada-tsxry-what-is-driving-attention-1)  
  <sub>Kalkine Media, 51 minutes ago</sub>  
  Royal Bank of Canada coverage uses S&P/TSX 60 context to explain current company developments, banking and capital markets, and the latest Canadian market...
- [Royal Bank of Canada stock at CAD 285.63 on September 25, 2026](https://www.ad-hoc-news.de/boerse/news/vorboerse/royal-bank-of-canada-stock-at-cad-285-63-on-september-25-2026/70191166)  
  <sub>AD HOC NEWS, 9 hours ago</sub>  
  Royal Bank of Canada shares closed at CAD 285.63 on the TSX on September 25, up 1.25 percent. The bank announced an NVCC AT1 notes offering with an expected...
- [Can new fixed income and NVCC instruments support Royal Bank of Canada stock?](https://tradersunion.com/news/stocks/show/3541070-royal-bank-of-canada-up/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada trades at C$286.55 today, up 0.31%. Get the latest on RY stock price action and technical outlook.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 201.82 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 204.86 (-1.5%), 50d 207.77 (-2.9%), 200d 185.78 (+8.6%); 50d above 200d
Momentum: RSI(14) 42.8 | MACD -1.794 vs signal -1.457 (histogram -0.336)
Returns: 1d -0.1% | 5d -2.1% | 1m -1.3% | 3m -1.5%
52-week range: 143.64 - 217.87 (now 78.4% of the way up)
Volatility: ATR(14) 3.10 (1.5% of price) | annualised 20d 17.2%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 279.41B
Valuation: trailing P/E 18.00 | forward P/E 15.97 | P/B 2.94 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
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
Price target: mean 208.66 (+3.4% vs last close), range 183.81 - 226.18
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.7%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.4%), Vanguard Capital Management LLC (3.1%), FIL LTD (1.7%), TD Asset Management, Inc (1.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 387,640 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-08-31 Royal Bank of Canada (Issuer): 350,000 shares, 71.49M
  - 2026-08-28 Royal Bank of Canada (Issuer): 350,000 shares, 71.50M
  - 2026-07-31 Royal Bank of Canada (Issuer): 211 shares, 44.11K
  - 2026-07-31 Royal Bank of Canada (Issuer): 140 shares, 29.28K
(105 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Teva stock falls 1.22 percent as Oppenheimer sets USD 50.00 target](https://www.ad-hoc-news.de/boerse/news/nebenwerte/teva-stock-falls-1-22-percent-as-oppenheimer-sets-usd-50-00-target/70193363)  
  <sub>AD HOC NEWS, 24 minutes ago</sub>  
  Teva stock stood at USD 38.71 on September 28, 2026, with a USD 45.1 billion market capitalization. Q2 revenue reached USD 4.14 billion.
- [Short Interest Increases — Sep 15, 2026 Settlement](https://www.stocktitan.net/rankings/companies-short-interest-increase?page=1&e=0&symbol=TMS)  
  <sub>Stock Titan, 3 hours ago</sub>  
  TEVA (up more than tenfold) leads FINRA short interest increases, Sep 15, 2026 settlement. 2814 companies ranked; figures 13 days old.
- [Cash or shares?](https://www.globes.co.il/serveen/globes/docview.asp?did=1001557698)  
  <sub>גלובס, 19 hours ago</sub>  
  Globes” examines which form of payment is preferable in an acquisition deal and discusses whether CyberArk, Mellanox, and Teva made the right M&A decisions.
- [Medincell share among the most sought-after values of the SBF 120, +8% in one week](https://www.ideal-investisseur.fr/en/stock-news/medincell-share-among-the-most-sought-after-values-of-the-sbf-120-8-in-one-week/25919.html)  
  <sub>Ideal Investisseur, 3 hours ago</sub>  
  After last Friday's decline, Medincell regains momentum this Monday, in a quasi-stable SBF 120. The share benefits from an improving technical context,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.75 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 38.06 (+1.8%), 50d 36.23 (+6.9%), 200d 33.49 (+15.7%); 50d above 200d
Momentum: RSI(14) 54.8 | MACD 0.879 vs signal 0.884 (histogram -0.005)
Returns: 1d -1.1% | 5d -3.3% | 1m +3.0% | 3m +16.3%
52-week range: 18.34 - 40.22 (now 93.3% of the way up)
Volatility: ATR(14) 1.23 (3.2% of price) | annualised 20d 32.9%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.19B
Valuation: trailing P/E 64.58 | forward P/E 12.73 | P/B 5.82 | PEG n/a
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.80 | short interest 2.7% of float
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
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 5 analysts)
Ratings: 3 strong buy, 3 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 44.00 (+13.5% vs last close), range 40.00 - 50.00
Recent rating changes:
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
  - 2026-07-28 Piper Sandler: main, Overweight -> Overweight
  - 2026-05-06 Barclays: main, Overweight -> Overweight
Institutional ownership: 23.0%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.4% of insider holdings) | insiders hold 6,094,499 shares
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

- [What's Going On With Exxon Mobil Stock on Monday?](https://www.benzinga.com/trading-ideas/movers/26/09/62020855/whats-going-on-with-exxon-mobil-stock-on-monday)  
  <sub>Benzinga, 2 hours ago</sub>  
  ExxonMobil Holdings Corporation (NYSE:XOM) shares are trading higher by almost 2% during Monday's premarket session as Brent crude futures rebounded.
- [ExxonMobil (NYSE:XOM) Stock Price Expected to Rise, TD Cowen Analyst Says](https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-stock-price-expected-to-rise-td-cowen-analyst-says-2026-09-28/)  
  <sub>MarketBeat, 55 minutes ago</sub>  
  TD Cowen upped their price objective on ExxonMobil from $168.00 to $180.00 and gave the company a "buy" rating in a research note on Monday.
- [ExxonMobil (NYSE:XOM) Nears Breakout as Technical Strength and Setup Quality Align](https://www.chartmill.com/news/XOM/Chartmill-55438-ExxonMobil-NYSEXOM-Nears-Breakout-as-Technical-Strength-and-Setup-Quality-Align)  
  <sub>ChartMill, 2 hours ago</sub>  
  The Technical Breakout Setups methodology screens the market for stocks that answer two separate questions: is the underlying trend healthy,...
- [ExxonMobil Holdings (XOM), Why Is It Back In The Spotlight?](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/exxonmobil-holdings-xom-why-is-it-back-in-the-spotlight)  
  <sub>Simply Wall Street, 3 hours ago</sub>  
  ExxonMobil Holdings (XOM) is back in focus after management paused its Baytown blue hydrogen project, citing limited customer demand and policy uncertainty...
- [The Zacks Analyst Blog Highlights ExxonMobil, Automatic Data Processing and Cadence Design, BranchOut Food](https://finance.yahoo.com/markets/stocks/articles/zacks-analyst-blog-highlights-exxonmobil-061800247.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  XOM, ADP, CDNS and BOF feature in Zacks research, with AI, operational efficiency, recurring revenue and growth opportunities shaping their outlooks.
- [ETFs Are Net Sellers of ExxonMobil (XOM) on Thursday](https://www.gurufocus.com/news/9099410/etfs-are-net-sellers-of-exxonmobil-xom-on-thursday)  
  <sub>GuruFocus, 4 hours ago</sub>  
  ExxonMobil (XOM) snapped a two-day streak of net ETF buying, as ETF flows turned to $62.3 million in net selling in Thursday's session.
- [XOM, CVX Stocks In Focus: Trump Criticizes Exxon And Chevron For Profiting From Iran-Driven Oil Price Surge — ‘They’re Making Too Much Money’](https://stocktwits.com/news-articles/markets/equity/xom-cvx-stocks-in-focus-trump-criticizes-exxon-chevron-for-profiting-from-iran-driven-oil-price-surge/cZoTFnxRJ3i)  
  <sub>Stocktwits, 15 hours ago</sub>  
  According to data from Fiscal AI, the company is expected to report quarterly revenue of $52.06 million, down from $239.24 in the corresponding quarter of 2025.
- [Industrial stock winners: Vicor, Bloom Energy lead September’s top ten](https://www.tradingview.com/news/seekingalpha:4bf889aa4094b:0-industrial-stock-winners-vicor-bloom-energy-lead-september-s-top-ten/)  
  <sub>TradingView, 1 hour ago</sub>  
  As the month of September 2026 comes to a close, the broader stock market has exhibited a mix of late-summer consolidation and selective sector rotation.
- [LMP Capital And Income Fund Inc. Q2 2026 Commentary](https://seekingalpha.com/article/4950122-lmp-capital-and-income-fund-inc-q2-2026-commentary)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Key Takeaways. Markets: After pausing during the first quarter, technology shares reasserted market leadership in the second quarter, with the IT sector...
- [Crescent Energy and Kosmos Energy Stocks Trade Up, What You Need To Know](https://www.financialcontent.com/article/stockstory-2026-9-28-crescent-energy-and-kosmos-energy-stocks-trade-up-what-you-need-to-know)  
  <sub>FinancialContent, 36 minutes ago</sub>  
  What Happened? A number of stocks jumped in the pre-market session after crude oil prices jumped following President Donald Trump's rejection of an Iranian...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 162.64 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 162.78 (-0.1%), 50d 159.73 (+1.8%), 200d 148.22 (+9.7%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD 0.556 vs signal 1.107 (histogram -0.551)
Returns: 1d +1.3% | 5d +2.7% | 1m +4.0% | 3m +19.5%
52-week range: 110.64 - 171.47 (now 85.5% of the way up)
Volatility: ATR(14) 3.66 (2.2% of price) | annualised 20d 27.5%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 668.76B
Valuation: trailing P/E 20.93 | forward P/E 14.68 | P/B 2.58 | PEG 1.38
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.17 | short interest 1.1% of float
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
Consensus: buy (mean 2.32 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 7 buy, 15 hold, 0 sell, 0 strong sell
Price target: mean 172.55 (+6.1% vs last close), range 142.00 - 200.00
Recent rating changes:
  - 2026-09-28 TD Cowen: main, Buy -> Buy
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
  - 2026-08-17 Barclays: main, Overweight -> Overweight
  - 2026-08-07 TD Cowen: main, Buy -> Buy
  - 2026-08-04 Freedom Broker: up, Sell -> Hold
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

> Neutral overall as there are no material macro surprises, technicals lack decisive break, and fund flows are flat.

**Main reasons it gave:**
- Flat fund flows: 0% share count change over 1 week
- Price below 20‑day SMA (28.24 vs 28.84) and RSI 43.2, indicating weak short‑term momentum
- Higher Treasury yields (+0.27 on 10‑yr) and stronger dollar (+0.76% on week) are bearish for commodities
- Fund composition: 46.2% cash and 51.8% other, limiting direct commodity exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.24 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 28.84 (-2.1%), 50d 28.33 (-0.3%), 200d 27.11 (+4.2%); 50d above 200d
Momentum: RSI(14) 43.2 | MACD 0.005 vs signal 0.104 (histogram -0.099)
Returns: 1d -1.1% | 5d -1.5% | 1m -2.0% | 3m +6.5%
52-week range: 25.44 - 29.49 (now 69.1% of the way up)
Volatility: ATR(14) 0.29 (1.0% of price) | annualised 20d 13.4%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Commodities Focused
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +14.0% a year | beta to the market 0.35
Cost and size: expense ratio 0.85% | net assets 1.33B
What it is made of: Other 51.8%, Cash 46.2%, Bonds 2.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 43.1%, Invesco Short Term Treasury ETF 4.4%
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
Rolled up from the 2 largest holdings, 47.5% of the fund by weight
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
Shares outstanding: 27.60M | fund size: 779.42M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicating no net demand shift
- Energy inventories show a build (+3.0 MMbbl oil, +53 BCF gas) which is bearish
- EIA price outlook forecasts oil price decline (~10% over six months) and gas price rise (~7%)
- Technicals show price near 52‑week high with low volume and MACD below signal, no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.71 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 32.67 (+0.1%), 50d 30.98 (+5.6%), 200d 27.98 (+16.9%); 50d above 200d
Momentum: RSI(14) 56.9 | MACD 0.552 vs signal 0.691 (histogram -0.140)
Returns: 1d +0.3% | 5d +0.4% | 1m +6.0% | 3m +23.2%
52-week range: 22.07 - 33.68 (now 91.6% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 19.5%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +14.0% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.80B
What it is made of: Other 50.6%, Cash 44.8%, Bonds 2.7%, Stocks 1.9%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.8%, Brent Crude Future Nov 26 8.9%, Invesco Short Term Treasury ETF 6.2%, Mini Ibovespa Future Dec 26 1.9%
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
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
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
Rolled up from the 4 largest holdings, 57.7% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX, BRNF6, TBLL, WINZ26
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
Shares outstanding: 111.40M | fund size: 3.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show oversold but no decisive break, flat fund flows, fundamentals unchanged.

**Main reasons it gave:**
- Treasury yields rose modestly across the curve (+0.10 to +0.27) this week
- Fund flows flat over the past week, indicating no net demand
- Technicals show price at 52‑week low with RSI 22, but no decisive break on heavy volume
- Macro data releases (inflation 3.4%, unemployment 4.1%) in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [Pantheon Macro forecasts a weak jobs print and urges for Fed caution](https://seekingalpha.com/news/4647578-pantheon-macro-forecasts-a-weak-jobs-print-and-urges-for-fed-caution)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Wall Street is looking ahead to Friday's September nonfarm payrolls report for a clearer read on how far the Federal Reserve may still need to go on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 77.44 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 78.65 (-1.5%), 50d 79.20 (-2.2%), 200d 79.96 (-3.1%); 50d below 200d
Momentum: RSI(14) 22.0 | MACD -0.419 vs signal -0.316 (histogram -0.103)
Returns: 1d -0.5% | 5d -1.6% | 1m -3.0% | 3m -3.2%
52-week range: 77.44 - 81.28 (now 0.0% of the way up)
Volatility: ATR(14) 0.27 (0.3% of price) | annualised 20d 4.9%
Volume: 0.57x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: High Yield Bond
Yield: 5.9%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +8.0% a year | beta to the market 0.67
Cost and size: expense ratio 0.49% | net assets 16.19B
What it is made of: Bonds 98.6%, Cash 1.2%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.3%
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
Shares outstanding: 195.60M | fund size: 15.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, mixed technicals, modest bullish analyst view, slight bullish shift in positioning but overall balanced.

**Main reasons it gave:**
- Analyst coverage thin (1.7% weight) but all buy ratings and +24.3% price target suggest modest bullish bias
- CFTC positioning shows net short 26% with short positions reduced 6.4% week‑over‑week, indicating slight bullish shift but crowding remains high
- Technical indicators mixed: price below 20‑day and 50‑day SMAs, RSI 31.8 (oversold) but no decisive breakout on volume
- Macro environment unchanged: yields rose modestly across curve, VIX stable, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [AVUV's Profitability Screen Has Holes (NYSEARCA:AVUV)](https://seekingalpha.com/article/4950076-avuvs-profitability-screen-has-holes)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  The Avantis US Small Cap Value ETF is a buy for long-term investors who need a small-cap sleeve, but it's not a buy for the short or medium term,...
- [Should ALPS O'Shares U.S. Small-Cap Quality Dividend ETF (OUSM) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/alps-oshares-u-small-cap-092002533.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Designed to provide broad exposure to the Small Cap Blend segment of the US equity market, the ALPS O'Shares U.S. Small-Cap Quality Dividend ETF (OUSM) is a...
- [ETFs Investing in Upwork, Inc. Stocks](https://www.tradingview.com/symbols/TRADEGATE-UP2/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in UP2 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [BE Stock Rises Premarket: Retail Dismisses Short-Seller Report As ‘Manipulation’](https://stocktwits.com/news-articles/markets/equity/be-stock-rises-premarket-retail-dismisses-short-seller-report/cZmoqWxR7VA)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Retail investors on Stocktwits dismissed Hunterbrook Capital's short-seller report, with some noting that the company's shares were holding up despite the...
- [Inflation Watch Mode: Preparing For Wednesday's PCE Data (NDX)](https://seekingalpha.com/article/4950086-inflation-watch-mode-preparing-for-wednesdays-pce-data)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  September broke the slump as the Nasdaq-100 hit records and the S&P 500 neared highs. Read why I anticipate PCE inflation data will trigger significant...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 279.60 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 287.80 (-2.9%), 50d 293.71 (-4.8%), 200d 275.82 (+1.4%); 50d above 200d
Momentum: RSI(14) 31.8 | MACD -3.918 vs signal -3.295 (histogram -0.623)
Returns: 1d -0.8% | 5d -2.1% | 1m -6.7% | 3m -6.5%
52-week range: 229.11 - 305.09 (now 66.5% of the way up)
Volatility: ATR(14) 3.44 (1.2% of price) | annualised 20d 12.3%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Small Blend
What it holds: P/E 17.30 | P/B 2.13 | P/S 1.31 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +18.2% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: JFrog Ltd Ordinary Shares 0.3%, Moog Inc Class A 0.3%, BlackRock Cash Funds Treasury SL Agency 0.3%, UMB Financial Corp 0.3%, Glaukos Corp 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.1%, Technology 13.8%, Industrials 13.2%
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
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.3% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - GKOS: 2026-09-22 Jefferies: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 26.0% of open interest (415,047 contracts)
Change on the week: -6.4% of open interest
Crowding: 5% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 78.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance based on flat flows, bearish technicals without decisive break, and a tightening macro environment with no surprise catalyst.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicate no net demand
- Technical RSI 25.4 and MACD negative show bearish momentum but low volume (0.27x 20‑day avg) lacks decisive break
- Rising Treasury yields (10‑year up 27 bps to 5.23%) and upward‑sloping curve reflect tightening environment
- Fund basics stable: yield 4.7%, high credit quality (A/B), low expense ratio, no significant change

<details><summary><b>News</b> — score +0.00</summary>

- [Pantheon Macro forecasts a weak jobs print and urges for Fed caution](https://seekingalpha.com/news/4647578-pantheon-macro-forecasts-a-weak-jobs-print-and-urges-for-fed-caution)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Wall Street is looking ahead to Friday's September nonfarm payrolls report for a clearer read on how far the Federal Reserve may still need to go on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 102.32 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 104.64 (-2.2%), 50d 105.69 (-3.2%), 200d 108.58 (-5.8%); 50d below 200d
Momentum: RSI(14) 25.4 | MACD -0.750 vs signal -0.562 (histogram -0.187)
Returns: 1d -0.9% | 5d -2.6% | 1m -4.1% | 3m -6.7%
52-week range: 102.32 - 112.92 (now 0.0% of the way up)
Volatility: ATR(14) 0.61 (0.6% of price) | annualised 20d 7.6%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Corporate Bond
Yield: 4.7%
Credit quality: A 46.6%, BBB 40.2%, AA 12.3%, AAA 1.0%
Three-year record: +4.7% a year | beta to the market 1.35
Cost and size: expense ratio 0.14% | net assets 32.04B
What it is made of: Bonds 98.9%, Cash 1.1%, Convertible 0.0%
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
Shares outstanding: 293.50M | fund size: 30.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals bearish but not decisive, positioning unchanged, fundamentals stable.

**Main reasons it gave:**
- US Treasury yields rose across the curve this week (+0.10 to +0.27) indicating higher rates
- Technical indicators show bearish momentum (RSI 31.7, price below 20d/50d/200d SMAs)
- CFTC data shows large speculators net short 2Y note decreased slightly (-0.6% OI) with high crowding (92% percentile)
- Fund basics: high credit quality AA, 3.6% yield, modest 3-year return +4% per year

<details><summary><b>News</b> — score +0.00</summary>

- [Pantheon Macro forecasts a weak jobs print and urges for Fed caution](https://seekingalpha.com/news/4647578-pantheon-macro-forecasts-a-weak-jobs-print-and-urges-for-fed-caution)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Wall Street is looking ahead to Friday's September nonfarm payrolls report for a clearer read on how far the Federal Reserve may still need to go on...
- [5% U.S. Treasury yields weigh heavily on global assets; does Australia's sovereign debt present a strategic entry window? Fixed-income giant Pimco warns that rate-hike expectations are too aggressive.](https://news.futunn.com/en/post/1000271216/5-us-treasury-yields-weigh-heavily-on-global-assets-does)  
  <sub>富途牛牛, 8 hours ago</sub>  
  PacificInvestment Management Company (Pimco) holds a constructive view on Australian bonds, believing that market expectations for interest-rate hikes are...
- [Oil and Bond Yields Rain on Vanguard All-World ETF's Parade After Its Best Week Since August](https://www.aktiencheck.de/analysen/Artikel-Oil_and_Bond_Yields_Rain_on_Vanguard_All_World_ETF_s_Parade_After_Its_Best_Week_Since_August-20126525)  
  <sub>aktiencheck.de, 5 hours ago</sub>  
  A rally that had carried global equities to their strongest weekly showing since early August ran into a wall of rising oil prices and climbing bond yields...
- [Following the Federal Reserve's rate hike, is the Reserve Bank of Australia poised for consecutive moves? Market focus shifts to a potential restart of rate hikes in September, followed by another increase in November.](https://news.futunn.com/en/post/1000248401/following-the-federal-reserve-s-rate-hike-is-the-reserve)  
  <sub>富途牛牛, 14 hours ago</sub>

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 81.10 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 81.41 (-0.4%), 50d 81.73 (-0.8%), 200d 82.30 (-1.5%); 50d below 200d
Momentum: RSI(14) 31.7 | MACD -0.189 vs signal -0.170 (histogram -0.018)
Returns: 1d -0.1% | 5d -0.2% | 1m -1.2% | 3m -1.3%
52-week range: 81.09 - 83.18 (now 0.2% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 2.1%
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
Credit quality: AA 100.0% | US government debt 99.2%
Three-year record: +4.0% a year | beta to the market 0.22
Cost and size: expense ratio 0.15% | net assets 25.91B
What it is made of: Bonds 99.2%, Cash 0.8%
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 29.8% of open interest (4,539,374 contracts)
Change on the week: -0.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 209.30M | fund size: 16.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish technicals and macro are offset by modestly bullish analyst view and solid fundamentals, with no clear catalyst.

**Main reasons it gave:**
- RSI(14) 39.4 and price below 20‑day SMA (88.15 vs 89.68) indicating bearish momentum
- Analyst coverage of top holdings 11.4% of fund, weighted price target +14.1% above current prices
- CFTC positioning net long 6% of open interest, change +1.3% OI, crowding at 100% percentile suggests reversal risk
- US Treasury yields rose (10‑yr +27 bps) and dollar index up 0.76% this week, pressuring European equities
- Fund flows flat over the week, no net creation or redemption

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/VWO/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  Find the latest Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) stock quote, history, news and other vital information to help you with your...
- [ETFs Investing in Compagnie Financiere Richemont SA Stocks](https://www.tradingview.com/symbols/HAM-RITN/etfs/)  
  <sub>TradingView, 12 hours ago</sub>  
  Explore funds investing in RITN in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 88.15 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 89.68 (-1.7%), 50d 90.56 (-2.7%), 200d 87.56 (+0.7%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -0.768 vs signal -0.614 (histogram -0.154)
Returns: 1d -0.5% | 5d -1.2% | 1m -4.5% | 3m +0.1%
52-week range: 77.90 - 93.19 (now 67.0% of the way up)
Volatility: ATR(14) 0.90 (1.0% of price) | annualised 20d 12.5%
Volume: 0.13x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +18.6% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 39.06B
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
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 6.0% of open interest (487,063 contracts)
Change on the week: +1.3% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 282.09M | fund size: 24.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Treasury yields rose modestly across the curve, no policy surprise
- Price below 20‑day SMA (59.44 vs 60.33) and RSI 43.9, MACD negative, low volume
- CFTC speculators net long 4.6% of open interest, +1.3% weekly change, crowding 60th percentile
- Analyst coverage thin: only 22.2% of fund weight covered, despite 100% buy rating

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/VWO/)  
  <sub>Yahoo Finance Singapore, 5 hours ago</sub>  
  Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) · 0.25% · -0.79% · 10.71% · 11.90% · 12.13% · 19.39% · 139.20%. Key events. Baseline. Advanced...
- [VWO: The AI Boom Isn’t Enough To Offset China’s Weakness (NYSEARCA:VWO)](https://seekingalpha.com/article/4950183-vwo-the-ai-boom-isnt-enough-to-offset-chinas-weakness)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  The Vanguard FTSE Emerging Markets ETF's (VWO) Taiwan exposure benefits from strong AI infrastructure spending and semiconductor demand, led by holdings...
- [Vanguard FTSE Emerging Markets ETF shows mixed ...](https://pluang.com/en/news-feed/vwo-boom-ai-tidak-kompensasi-lemahnya-china)  
  <sub>Pluang, 4 hours ago</sub>  
  The Vanguard FTSE Emerging Markets ETF (VWO) benefits from strong AI infrastructure spending and semiconductor demand in Taiwan, led by key holdings like...
- [ETFs Investing in China Petroleum & Chemical Corporation Class H Stocks](https://www.tradingview.com/symbols/OTC-SNPMF/etfs/)  
  <sub>TradingView, 8 hours ago</sub>  
  Explore funds investing in SNPMF in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.44 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 60.33 (-1.5%), 50d 59.85 (-0.7%), 200d 57.85 (+2.8%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD -0.038 vs signal 0.052 (histogram -0.091)
Returns: 1d -1.2% | 5d -2.8% | 1m -2.6% | 3m +0.4%
52-week range: 52.42 - 61.44 (now 77.8% of the way up)
Volatility: ATR(14) 0.65 (1.1% of price) | annualised 20d 14.3%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 15.91 | P/B 2.13 | P/S 1.86 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +18.3% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 168.36B
What it is made of: Stocks 95.3%, Cash 4.6%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 14.7%, Tencent Holdings Ltd 2.9%, Alibaba Group Holding Ltd Ordinary Shares 2.2%, MediaTek Inc 1.5%, Delta Electronics Inc 0.9%
Sector mix: Technology 31.8%, Financial services 20.2%, Consumer cyclical 9.9%, Basic materials 7.9%
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
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.4% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 4.6% of open interest (1,036,240 contracts)
Change on the week: +1.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 84.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Embelton Limited Lodges Appendix 4G Corporate Governance Key to Disclosures for FY2026](https://kalkine.com.au/news/announcements/embelton-limited-lodges-appendix-4g-corporate-governance-key-to-disclosures-for-fy2026)  
  <sub>Kalkine, 8 hours ago</sub>  
  Embelton Limited (ASX:EMB) has lodged its Appendix 4G Key to Disclosures document with the ASX, covering corporate governance practices for the financial...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.26 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 93.46 (-2.4%), 50d 94.36 (-3.3%), 200d 95.57 (-4.5%); 50d below 200d
Momentum: RSI(14) 24.0 | MACD -0.684 vs signal -0.504 (histogram -0.181)
Returns: 1d -1.0% | 5d -2.7% | 1m -4.1% | 3m -5.7%
52-week range: 91.26 - 97.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.50 (0.5% of price) | annualised 20d 7.2%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Emerging Markets Bond
Yield: 5.1%
Credit quality: BBB 33.9%, BB 25.2%, B 19.3%, A 17.6% | US government debt 87.3%
Three-year record: +9.0% a year | beta to the market 1.08
Cost and size: expense ratio 0.39% | net assets 14.92B
What it is made of: Bonds 98.4%, Cash 1.6%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.5%
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
Share count change: 1 week: +0.1% (13.65M) over 7d
Shares outstanding: 160.41M | fund size: 14.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Ed Yardeni Says ‘Phenomenal’ Earnings Keep Bull Case Intact, But Pushes His S&P 500 Target Of 8,400 To Mid-2027](https://www.tradingview.com/news/stocktwits:52fefeb1f094b:0-ed-yardeni-says-phenomenal-earnings-keep-bull-case-intact-but-pushes-his-s-p-500-target-of-8-400-to-mid-2027/)  
  <sub>TradingView, 3 hours ago</sub>  
  Ed Yardeni, President at Yardeni Research, said he could not rule out the 10-year U.S. Treasury yield reaching 5.5% or even higher, but strong corporate...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.39 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 91.20 (-2.0%), 50d 92.34 (-3.2%), 200d 94.62 (-5.5%); 50d below 200d
Momentum: RSI(14) 27.1 | MACD -0.760 vs signal -0.624 (histogram -0.136)
Returns: 1d -0.7% | 5d -1.9% | 1m -4.1% | 3m -6.0%
52-week range: 89.39 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.47 (0.5% of price) | annualised 20d 6.6%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +3.1% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.82B
What it is made of: Bonds 99.6%, Cash 0.4%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 35.6% of open interest (5,407,726 contracts)
Change on the week: -0.9% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 146.00M | fund size: 13.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Equal-Weight S&P 500 slides to a 3-month low as selling pressures broaden](https://seekingalpha.com/news/4647643-equal-weight-sp-500-slides-to-a-3-month-low-as-selling-pressures-broaden)  
  <sub>Seeking Alpha, 6 minutes ago</sub>  
  The equal-weight S&P 500 is flashing a broader warning than the headline averages. On Monday, the Invesco S&P 500 Equal Weight ETF (RSP) traded as low as...
- [Why Stocks Can Rally Despite 20-Year-High Bond Yields? ETFs in Focus](https://www.tradingview.com/news/zacks:f14db0e94094b:0-why-stocks-can-rally-despite-20-year-high-bond-yields-etfs-in-focus/)  
  <sub>TradingView, 3 hours ago</sub>  
  Wall Street's optimism for the stock market is building up as 2026 draws to a close, despite the ongoing concerns over high bond yields.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 209.79 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 214.44 (-2.2%), 50d 216.94 (-3.3%), 200d 205.44 (+2.1%); 50d above 200d
Momentum: RSI(14) 33.0 | MACD -2.077 vs signal -1.610 (histogram -0.467)
Returns: 1d -0.6% | 5d -1.4% | 1m -5.3% | 3m -1.5%
52-week range: 182.18 - 222.77 (now 68.0% of the way up)
Volatility: ATR(14) 1.83 (0.9% of price) | annualised 20d 9.2%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Large Blend
What it holds: P/E 21.39 | P/B 3.11 | P/S 1.95 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +15.7% a year | beta to the market 0.83
Cost and size: expense ratio 0.20% | net assets 100.87B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.6%, Veeva Systems Inc Class A 0.3%, Zebra Technologies Corp Ordinary Shares - Class A 0.3%, Charles River Laboratories International Inc 0.3%, DoorDash Inc Ordinary Shares - Class A 0.3%
Sector mix: Technology 17.3%, Industrials 14.7%, Financial services 14.6%, Healthcare 13.1%
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
Rolled up from the 5 largest holdings, 1.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.9% | hold 32.1% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.0% above the current prices
Holdings read: MRNA, VEEV, ZBRA, CRL, DASH
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - VEEV: 2026-08-28 Citigroup: main, Neutral -> Neutral
  - ZBRA: 2026-09-15 Needham: main, Buy -> Buy
  - CRL: 2026-09-28 Jefferies: main, Buy -> Buy
  - DASH: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 19.9% of open interest (1,890,653 contracts)
Change on the week: -7.9% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 155.55M | fund size: 32.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [SCHP: Solid TIPs ETF, But I Prefer Shorter-Term Alternatives (NYSEARCA:SCHP)](https://seekingalpha.com/article/4950129-schp-solid-tips-etf-but-i-prefer-shorter-term-alternatives)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Treasury inflation-protected securities have outperformed most treasuries and bonds these past few years due to elevated inflation. The Schwab U.S. TIPS ETF...
- [Bitcoin Rally Wobbles as Macro Risks Overshadow ETF Demand](https://www.bloomberg.com/news/articles/2026-09-28/bitcoin-rally-wobbles-as-macro-risks-overshadow-etf-demand?srnd=phx-latinamerica)  
  <sub>Bloomberg.com, 6 hours ago</sub>  
  Bitcoin continued to lose momentum on Monday, cooling after a blistering rally in recent weeks, as a fresh bout of macro uncertainty weighed on risk assets.
- [Schwab U.S. TIPS ETF underperforms peers despite inflation protection and dividend benefits](https://pluang.com/en/news-feed/schp-etf-tips-yang-kuat-tapi-saya-memilih-alternatif-jangka-pendek)  
  <sub>Pluang, 6 hours ago</sub>  
  The Schwab U.S. TIPS ETF (SCHP), a major fund investing in Treasury inflation-protected securities (TIPS), has lagged behind other similar ETFs in terms of...
- [SCHD vs. VYMI vs. JEPI: Which Popular Dividend ETF Delivers the Highest Yield?](https://www.tipranks.com/news/schd-vs-vymi-vs-jepi-which-popular-dividend-etf-delivers-the-highest-yield)  
  <sub>TipRanks, 32 minutes ago</sub>  
  Dividend ETFs remain one of the most popular ways for investors to generate passive income. Among the leading options are Schwab U.S. Dividend Equity ETF...
- [Solana Fever: VanEck’s VSOL ETF Sees 5% AUM Jolt as Traders Pile Into the Rally](https://www.tipranks.com/news/cryptocurrencies/solana-fever-vanecks-vsol-etf-sees-5-aum-jolt-as-traders-pile-into-the-rally)  
  <sub>TipRanks, 2 hours ago</sub>  
  Solana surge: VanEck's VSOL ETF pulls in fresh cash as traders chase the rally. VanEck's Solana ETF, VSOL, recorded net inflows of $1539990 on September 24,...
- [Beyond the Semiconductor Names: Four ADRhedged™ ETFs Covering Enterprise Software, Healthcare and Energy](https://www.tipranks.com/news/beyond-the-semiconductor-names-four-adrhedged-etfs-covering-enterprise-software-healthcare-and-energy)  
  <sub>TipRanks, 4 hours ago</sub>  
  Ringing the Bell for a Ten-Fund Lineup Precidian Investments, the sponsor behind the ADRhedged™ platform, rang the opening bell at the New York Stock...
- [ETF Exodus Sends Fortuna Mining Stock Reeling](https://www.tipranks.com/news/catalyst/etf-exodus-sends-fortuna-mining-stock-reeling)  
  <sub>TipRanks, 6 hours ago</sub>  
  Fortuna Mining Corp ( ($TSE:FVI) ) is experiencing volatility. Read on for a possible explanation for the stock's unusual movement. Fortuna Mining Corp.
- [FUTR Planning Taps NextMove Capital to Capture First-Time Investors and Monetize Smaller Accounts](https://www.tipranks.com/news/company-announcements/futr-planning-taps-nextmove-capital-to-capture-first-time-investors-and-monetize-smaller-accounts)  
  <sub>TipRanks, 1 minute ago</sub>  
  An update from FUTR Corporation ( ($TSE:FTRC) ) is now available. FUTR Planning, a division of The FUTR Corporation, has partnered with newly launched...
- [3 Best Vanguard ETFs for 24%+ Annual Returns](https://www.tipranks.com/news/3-best-vanguard-etfs-for-10-annual-returns)  
  <sub>TipRanks, 19 hours ago</sub>  
  Investors chasing growth don't necessarily need to bet on individual stocks to get it. Vanguard offers a wide range of low-cost ETFs that provide exposure...
- [Pinnacle Shares Slide as Affiliate ETFs Halted](https://www.tipranks.com/news/catalyst/pinnacle-shares-slide-as-affiliate-etfs-halted)  
  <sub>TipRanks, 13 hours ago</sub>  
  Pinnacle Investment Management Group Limited ( ($AU:PNI) ) is experiencing volatility. Read on for a possible explanation for the stock's unusual movement.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.04 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 105.87 (-1.7%), 50d 106.73 (-2.5%), 200d 109.46 (-5.0%); 50d below 200d
Momentum: RSI(14) 25.7 | MACD -0.715 vs signal -0.551 (histogram -0.164)
Returns: 1d -0.5% | 5d -1.6% | 1m -3.2% | 3m -5.3%
52-week range: 104.04 - 112.20 (now 0.0% of the way up)
Volatility: ATR(14) 0.41 (0.4% of price) | annualised 20d 4.8%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 5.0%
Credit quality: AA 99.9% | US government debt 99.9%
Three-year record: +3.7% a year | beta to the market 0.68
Cost and size: expense ratio 0.18% | net assets 15.01B
What it is made of: Bonds 99.9%, Cash 0.1%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 35.6% of open interest (5,407,726 contracts)
Change on the week: -0.9% of open interest
Crowding: 87% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 177.70M | fund size: 18.49B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [4 Best ETF Areas of Q3 That Are in High Momentum](https://ca.finance.yahoo.com/news/4-best-etf-areas-q3-130000609.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Crypto, oil, rate hedges and AI-driven themes powered Q3 ETF winners. Here are the high-momentum areas investors should watch.
- [TLT Is Down More Than Half From Its Peak. Is It a Bargain or a Trap?](https://247wallst.com/investing/2026/09/27/tlt-is-down-more-than-half-from-its-peak-is-it-a-bargain-or-a-trap/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Long-duration Treasuries have shed more than half their peak value, and retail investors keep loading up expecting a rate reversal that refuses to arrive.
- [Long-term Treasury ETF TLT falls over 50% from peak, signaling risk amid rising yields and Fed tightening.](https://pluang.com/en/news-feed/tlt-turun-lebih-dari-setengah-dari-puncaknya-apakah-ini-peluang-atau-perangkap)  
  <sub>Pluang, 20 hours ago</sub>  
  The iShares 20+ Year Treasury Bond ETF (TLT) has dropped to $79.42, less than half its August 2020 peak of around $179, due to rising long-term Treasury...
- [S&P 500, Nasdaq Futures Pull Back After Trump Wants 'Couple Days To Think' About Iran Ceasefire Deal: ASTS, DELL, BB, SMCI In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-futures-pull-back-after-trump-wants-couple-days-to-think-about-iran-ceasefire-deal/cZgS7tGRet0)  
  <sub>Stocktwits, 16 hours ago</sub>  
  According to a report from Axios, the U.S. and Iran have reached a tentative deal to extend the ceasefire between the two nations by 60 days and are on...
- [Ed Yardeni Says ‘Phenomenal’ Earnings Keep Bull Case Intact, But Pushes His S&P 500 Target Of 8,400 To Mid-2027](https://www.tradingview.com/news/stocktwits:52fefeb1f094b:0-ed-yardeni-says-phenomenal-earnings-keep-bull-case-intact-but-pushes-his-s-p-500-target-of-8-400-to-mid-2027/)  
  <sub>TradingView, 3 hours ago</sub>  
  Ed Yardeni, President at Yardeni Research, said he could not rule out the 10-year U.S. Treasury yield reaching 5.5% or even higher, but strong corporate...
- [Pantheon Macro forecasts a weak jobs print and urges for Fed caution](https://seekingalpha.com/news/4647578-pantheon-macro-forecasts-a-weak-jobs-print-and-urges-for-fed-caution)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Wall Street is looking ahead to Friday's September nonfarm payrolls report for a clearer read on how far the Federal Reserve may still need to go on...
- [U.S. Treasury Yields Surpass 5% as ETF Returns Plummet](https://www.chosun.com/english/market-money-en/2026/09/27/K7ZTP5OTJFH7FERBFDRZSKKCYU/)  
  <sub>조선일보, 24 hours ago</sub>  
  U.S. Treasury Yields Surpass 5% as ETF Returns Plummet Rising rates driven by strong economy, geopolitical tensions; investors sell 890 billion won in.
- [S&P 500, Nasdaq, Dow Futures Retreat After Rally Fueled By SpaceX, US-Iran Deal As Fed Meeting Looms: TSLA, PLAY, FISV In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-retreat-after-rally-fueled-by-spacex-us-iran-deal-as-fed-meeting-looms/cZKW76IR7ER)  
  <sub>Stocktwits, 21 hours ago</sub>  
  The Dow index jumped to a new all-time intraday high on Monday, while the Nasdaq jumped to its best close since the end of March.
- [Dow, S&P 500, Nasdaq Futures Fall As Brent Tops $106 After Trump Rejects Iran Proposal: MU, SLV, QNT, META In Focus](https://de.tradingview.com/news/stocktwits:90bdaed6f094b:0-dow-s-p-500-nasdaq-futures-fall-as-brent-tops-106-after-trump-rejects-iran-proposal-mu-slv-qnt-meta-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures fell in overnight trading late Sunday as oil prices climbed after President Donald Trump rejected an Iranian proposal to reopen the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 78.39 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 81.14 (-3.4%), 50d 82.12 (-4.5%), 200d 85.62 (-8.4%); 50d below 200d
Momentum: RSI(14) 27.3 | MACD -0.793 vs signal -0.552 (histogram -0.242)
Returns: 1d -1.2% | 5d -4.2% | 1m -5.7% | 3m -10.4%
52-week range: 78.39 - 92.06 (now 0.0% of the way up)
Volatility: ATR(14) 0.76 (1.0% of price) | annualised 20d 10.8%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Long Government
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +0.3% a year | beta to the market 2.39
Cost and size: expense ratio 0.15% | net assets 47.05B
What it is made of: Bonds 99.6%, Cash 0.4%
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 33.3% of open interest (2,476,197 contracts)
Change on the week: -0.4% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 109.70M | fund size: 8.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.70 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 28.29 (+1.5%), 50d 28.23 (+1.7%), 200d 27.74 (+3.5%); 50d above 200d
Momentum: RSI(14) 70.8 | MACD 0.143 vs signal 0.086 (histogram 0.057)
Returns: 1d +0.3% | 5d +0.8% | 1m +2.4% | 3m +1.2%
52-week range: 26.47 - 28.70 (now 100.0% of the way up)
Volatility: ATR(14) 0.10 (0.4% of price) | annualised 20d 4.8%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Trading--Miscellaneous
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +3.5% a year | beta to the market -9.48
Cost and size: expense ratio 0.75% | net assets 298.71M
What it is made of: Cash 100.0%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 48.8%
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
Rolled up from the 1 largest holdings, 48.8% of the fund by weight
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 9.7% of open interest (46,328 contracts)
Change on the week: +1.5% of open interest
Crowding: 58% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.9% (-2.64M) over 7d
Shares outstanding: 10.43M | fund size: 299.37M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals show downtrend without decisive break, analyst view bullish but limited coverage, modest inflows.

**Main reasons it gave:**
- US macro unchanged: yields up modestly, dollar up, no policy surprise
- Technical downtrend: price ~6% below 20d/50d/200d SMAs, RSI 27.4, low volume, no decisive break
- Analyst view: 100% buy rating, +38.5% price target, but covers only 51% of fund weight
- Fund flows: share count +2.4% over week, indicating modest inflows

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 87.09 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 93.84 (-7.2%), 50d 93.52 (-6.9%), 200d 92.67 (-6.0%); 50d above 200d
Momentum: RSI(14) 27.4 | MACD -1.319 vs signal -0.441 (histogram -0.877)
Returns: 1d -1.7% | 5d -5.7% | 1m -7.5% | 3m -4.8%
52-week range: 67.55 - 102.94 (now 55.2% of the way up)
Volatility: ATR(14) 1.84 (2.1% of price) | annualised 20d 18.5%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.48 | P/B 1.77 | P/S 1.36 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +29.3% a year | beta to the market 0.50
Cost and size: expense ratio 0.59% | net assets 815.33M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 25.4%, YPF SA ADR 9.5%, Vista Energy SAB de CV ADR 6.2%, Grupo Financiero Galicia SA ADR 5.6%, Banco Macro SA ADR 4.3%
Sector mix: Consumer cyclical 30.4%, Energy 19.4%, Financial services 14.4%, Basic materials 12.0%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +38.5% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, BMA
Recent rating changes among them:
  - MELI: 2026-09-03 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
  - BMA: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: +2.4% (18.06M) over 7d
Shares outstanding: 8.93M | fund size: 777.82M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals are bearish, macro shows no surprise, analyst view is bullish but covers only ~38% of the fund, and flows are flat.

**Main reasons it gave:**
- Price 120.35 below 20‑day SMA 124.05 (‑3%)
- Analyst coverage 37.6% of fund, 100% buy, price target +19.8% above current
- Fund flows flat (share count change +0.0% over 1 week)
- US Treasury yields rose across curve (10‑yr +0.27% week)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 120.35 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 124.05 (-3.0%), 50d 122.44 (-1.7%), 200d 122.36 (-1.6%); 50d above 200d
Momentum: RSI(14) 41.4 | MACD 0.087 vs signal 0.516 (histogram -0.429)
Returns: 1d -2.1% | 5d -5.7% | 1m -3.8% | 3m +0.6%
52-week range: 94.64 - 137.69 (now 59.7% of the way up)
Volatility: ATR(14) 1.90 (1.6% of price) | annualised 20d 21.9%
Volume: 0.33x the 20-day average
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
Three-year record: +33.3% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.8% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-09-23 Oppenheimer: init, ? -> Outperform
  - TSEM.TA: 2026-09-25 Mizuho: init, ? -> Outperform
  - ESLT.TA: 2026-08-19 JP Morgan: main, Neutral -> Neutral
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
Shares outstanding: 2.55M | fund size: 306.89M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no material macro surprise or decisive technical break; mixed signals from bullish analyst view and fundamentals versus bearish outflows and weak technical momentum.

**Main reasons it gave:**
- Analyst coverage: 90.3% buy rating for 47.4% of fund
- Fund flows: -1.1% share count (outflows) over past week
- Technical momentum: RSI 49.7, MACD histogram -0.130, 5‑day return -2.6%
- Macro: yields up modestly, no rate surprise, VIX low (15.86)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 44.49 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 44.85 (-0.8%), 50d 43.87 (+1.4%), 200d 39.35 (+13.1%); 50d above 200d
Momentum: RSI(14) 49.7 | MACD 0.262 vs signal 0.393 (histogram -0.130)
Returns: 1d -0.8% | 5d -2.6% | 1m +2.1% | 3m +15.6%
52-week range: 31.78 - 45.76 (now 90.9% of the way up)
Volatility: ATR(14) 0.65 (1.5% of price) | annualised 20d 19.6%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.47 | P/B 2.00 | P/S 1.36 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +43.7% a year | beta to the market 0.73
Cost and size: expense ratio 0.59% | net assets 848.26M
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: PKO Bank Polski SA 15.4%, Orlen SA 13.8%, Bank Polska Kasa Opieki SA 7.1%, Powszechny Zaklad Ubezpieczen SA 6.4%, KGHM Polska Miedz SA 4.6%
Sector mix: Financial services 46.1%, Energy 14.5%, Consumer cyclical 12.7%, Basic materials 6.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.9% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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
Direction: money going out (1 week)
Share count change: 1 week: -1.1% (-9.23M) over 7d
Shares outstanding: 19.03M | fund size: 846.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bearish analyst view offset by neutral flows and solid fundamentals, with no material macro catalyst or decisive technical break.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% week)
- Analyst view of top holdings (46.4% weight): 40% sell, 59.6% hold, weighted price target -5.8% vs current price
- Technical indicators: price below 20d, 50d, 200d SMAs; RSI 39.4; MACD negative; low volume
- Macro data: no policy surprise, yields modestly higher, inflation 3.4% in line, VIX low (15.86)

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Singapore ETF (EWS) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/EWS/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  Find the latest iShares MSCI Singapore ETF (EWS) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 28.44 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 29.21 (-2.6%), 50d 29.47 (-3.5%), 200d 28.60 (-0.5%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -0.331 vs signal -0.231 (histogram -0.101)
Returns: 1d +0.1% | 5d -2.0% | 1m -5.5% | 3m +1.2%
52-week range: 24.95 - 30.43 (now 63.8% of the way up)
Volatility: ATR(14) 0.37 (1.3% of price) | annualised 20d 18.5%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 21.06 | P/B 2.81 | P/S 3.39 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +13.4% a year | beta to the market 0.96
Cost and size: expense ratio 0.50% | net assets 1.33B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: BHP Group Ltd 16.3%, Commonwealth Bank of Australia 13.0%, National Australia Bank Ltd 5.9%, Westpac Banking Corp 5.7%, ANZ Group Holdings Ltd 5.5%
Sector mix: Financial services 41.1%, Basic materials 26.7%, Consumer cyclical 6.5%, Healthcare 5.2%
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

<details><summary><b>What analysts and big funds say</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.30</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.8% above the current prices
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
Shares outstanding: 63.60M | fund size: 1.81B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no material macro surprise, technicals show weak short‑term momentum, fund flows flat, and analyst view is modestly bullish but limited in coverage.

**Main reasons it gave:**
- Price below 20‑day SMA (58.97 vs 60.56) and 50‑day SMA (58.97 vs 60.72)
- RSI 36.2 indicating weak momentum
- Fund flows flat: 0% share count change over 1 week
- Macro yields up modestly, no surprise in inflation (3.4%) or unemployment (4.1%)
- Analyst coverage 28.3% of fund, 74% buy rating, +7% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.97 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 60.56 (-2.6%), 50d 60.72 (-2.9%), 200d 57.63 (+2.3%); 50d above 200d
Momentum: RSI(14) 36.2 | MACD -0.430 vs signal -0.233 (histogram -0.197)
Returns: 1d -1.0% | 5d -2.4% | 1m -5.3% | 3m +2.6%
52-week range: 49.72 - 62.64 (now 71.6% of the way up)
Volatility: ATR(14) 0.66 (1.1% of price) | annualised 20d 14.7%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 19.49 | P/B 2.83 | P/S 2.79 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +22.7% a year | beta to the market 0.79
Cost and size: expense ratio 0.50% | net assets 6.85B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Royal Bank of Canada 9.0%, The Toronto-Dominion Bank 6.3%, Shopify Inc Registered Shs -A- Subord Vtg 5.7%, Bank of Montreal 3.7%, Bank of Nova Scotia 3.6%
Sector mix: Financial services 39.2%, Energy 17.9%, Basic materials 16.1%, Industrials 8.8%
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
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.0% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-23 Wedbush: reit, Outperform -> Outperform
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
Shares outstanding: 94.80M | fund size: 5.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, mixed signals from bullish analyst view and fundamentals versus bearish technicals, and flat fund flows.

**Main reasons it gave:**
- No macro surprise: US Treasury yields rose modestly, inflation 3.4% in line with expectations
- Technical indicators bearish: price below 20‑day and 50‑day SMAs, RSI 40.3, MACD negative
- Analyst coverage bullish: 82% buy rating, weighted price target +11.4% above current price
- Fund flows flat: share count unchanged over the past week

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Singapore ETF (EWS) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/EWS/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  Find the latest iShares MSCI Singapore ETF (EWS) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 50.71 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 51.94 (-2.4%), 50d 52.24 (-2.9%), 200d 51.37 (-1.3%); 50d above 200d
Momentum: RSI(14) 40.3 | MACD -0.387 vs signal -0.276 (histogram -0.111)
Returns: 1d -1.6% | 5d -2.0% | 1m -5.9% | 3m +2.2%
52-week range: 45.38 - 54.72 (now 57.1% of the way up)
Volatility: ATR(14) 0.72 (1.4% of price) | annualised 20d 16.9%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.99 | P/B 2.88 | P/S 2.90 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +20.2% a year | beta to the market 1.19
Cost and size: expense ratio 0.51% | net assets 755.74M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: Spotify Technology SA 10.2%, Investor AB Class B 9.5%, Volvo AB Class B 7.1%, Atlas Copco AB Class A 6.9%, Sandvik AB 5.3%
Sector mix: Industrials 46.0%, Financial services 24.9%, Communication services 13.9%, Technology 6.2%
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
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.4% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-08-13 Argus Research: reit, Buy -> Buy
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
Shares outstanding: 7.65M | fund size: 387.93M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, price below key moving averages, and modest bullish analyst view covering less than half of the fund.

**Main reasons it gave:**
- Price 41.95 below 20‑day SMA (42.84) and 50‑day SMA (43.07)
- Fund flows flat (share count change +0.0% over 7 days)
- Analyst view bullish (+16.5% price target) but covers only 45.5% of fund
- US Treasury yields rose modestly, no macro surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 41.95 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 42.84 (-2.1%), 50d 43.07 (-2.6%), 200d 42.40 (-1.1%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -0.378 vs signal -0.267 (histogram -0.111)
Returns: 1d -0.7% | 5d -1.5% | 1m -5.9% | 3m +2.5%
52-week range: 38.08 - 44.59 (now 59.4% of the way up)
Volatility: ATR(14) 0.47 (1.1% of price) | annualised 20d 13.9%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.40 | P/B 1.94 | P/S 1.28 | 3y earnings growth n/a
Yield: 1.9%
Three-year record: +19.3% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Siemens AG 12.1%, SAP SE 11.3%, Allianz SE 10.0%, Siemens Energy AG Ordinary Shares 6.4%, Deutsche Telekom AG 5.6%
Sector mix: Industrials 28.7%, Financial services 23.2%, Technology 15.9%, Consumer cyclical 7.4%
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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – short‑term technical weakness and rising rates offset bullish analyst coverage and solid fundamentals.

**Main reasons it gave:**
- Price below 20‑day (61.00) and 50‑day (61.70) SMAs, RSI 39.9, MACD negative – short‑term technical weakness
- US Treasury yields rose across the curve, 10‑yr at 5.23% (+0.27) and market pricing ~4 hikes – higher rates may pressure equities
- Analyst coverage spans 50.9% of fund, rating 100% buy with +11% price target – bullish but limited scope
- Fund fundamentals moderate: P/E 15.25, yield 3.0%, 3‑yr return +29.5%/yr – solid but not compelling

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 59.83 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 61.00 (-1.9%), 50d 61.70 (-3.0%), 200d 57.91 (+3.3%); 50d above 200d
Momentum: RSI(14) 39.9 | MACD -0.502 vs signal -0.384 (histogram -0.118)
Returns: 1d -0.9% | 5d -2.3% | 1m -3.8% | 3m +1.6%
52-week range: 50.31 - 63.35 (now 73.0% of the way up)
Volatility: ATR(14) 0.72 (1.2% of price) | annualised 20d 17.0%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.25 | P/B 1.85 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +29.5% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.8%, Intesa Sanpaolo 13.6%, Enel SpA 10.3%, Ferrari NV 5.2%, Eni SpA 5.0%
Sector mix: Financial services 52.6%, Utilities 16.3%, Industrials 9.7%, Consumer cyclical 9.0%
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
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.0% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, RACE.MI, ENI.MI
Recent rating changes among them:
  - RACE.MI: 2026-07-31 UBS: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and mixed signals from analyst view (strong buy but thin coverage), insider positioning (small net long decreasing), and fundamentals (moderate valuation, decent yield). Overall the evidence does not justify a directional tilt.

**Main reasons it gave:**
- Analyst view: all buy rating with +16.7% price target (thin coverage 17% of fund)
- CFTC positioning: net long 3.6% down 0.7% week, indicating slight bearish sentiment
- Technical: price below 20‑day SMA, RSI 48.7 (neutral), MACD below signal
- Macro: US yields up, no surprise in data, VIX low; no material macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.
- [KOSPI leads Asia lower as 5% US yields and $106 oil hit expensive tech](https://invezz.com/ie/news/2026/09/28/kospi-leads-asia-lower-as-5percent-us-yields-and-dollar106-oil-hit-expensive-tech/)  
  <sub>Invezz, 10 hours ago</sub>  
  Asian stocks came under renewed pressure on Monday as another rise in oil prices and global bond yields reopened questions over how long expensive equity...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 96.36 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 97.18 (-0.8%), 50d 95.49 (+0.9%), 200d 90.12 (+6.9%); 50d above 200d
Momentum: RSI(14) 48.7 | MACD 0.388 vs signal 0.576 (histogram -0.188)
Returns: 1d -1.6% | 5d -1.6% | 1m +0.5% | 3m +3.4%
52-week range: 78.36 - 98.78 (now 88.2% of the way up)
Volatility: ATR(14) 1.49 (1.5% of price) | annualised 20d 19.4%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Japan Stock
What it holds: P/E 19.11 | P/B 2.01 | P/S 1.68 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +20.1% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 22.69B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.6%, Toyota Motor Corp 3.5%, Sumitomo Mitsui Financial Group Inc 3.0%, Tokyo Electron Ltd 3.0%, Advantest Corp 2.9%
Sector mix: Industrials 22.9%, Technology 21.5%, Financial services 19.1%, Consumer cyclical 11.6%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.7% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 3.6% of open interest (21,974 contracts)
Change on the week: -0.7% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 227.85M | fund size: 21.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to lack of material macro surprise, flat fund flows, modest bullish analyst coverage limited to <50% of fund, and technicals showing price below key moving averages with low volume.

**Main reasons it gave:**
- Technical trend: price below 20‑day, 50‑day, and 200‑day SMAs with low volume
- Analyst coverage: 74.5% buy rating but only covers 48.5% of fund weight
- Fund flows: flat share count over the past week indicating no net demand
- Macro: no surprise data; yields modestly higher, VIX low, dollar up

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 60.15 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 61.13 (-1.6%), 50d 62.53 (-3.8%), 200d 61.61 (-2.4%); 50d above 200d
Momentum: RSI(14) 38.5 | MACD -0.704 vs signal -0.715 (histogram 0.011)
Returns: 1d -0.8% | 5d -1.1% | 1m -5.6% | 3m -4.9%
52-week range: 54.26 - 65.08 (now 54.4% of the way up)
Volatility: ATR(14) 0.67 (1.1% of price) | annualised 20d 14.1%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +13.3% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.5% above the current prices
Holdings read: ROP.SW, NOVN.SW, NESN.SW, UBSG.SW, CFR.SW
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

> Neutral stance given flat fund flows, no decisive technical break, stable macro backdrop, and moderate fundamentals. Analyst view is bullish but only covers 44% of the fund, limiting its impact.

**Main reasons it gave:**
- Flat fund flows (0.0% share count change) indicating no net demand
- Technicals: price near 20‑day SMA (+0.4%) but below 50‑day SMA, RSI 50.2, no decisive break
- Macro: upward‑sloping yield curve (+1.15) and modest VIX (15.86) suggest stable environment
- Analyst view covers 44.1% of fund, rating 100% buy with +29.8% price target
- Fund fundamentals moderate: P/E 18.97, 3‑yr return +24.9%/yr, yield 4.1%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 67.96 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 67.70 (+0.4%), 50d 68.19 (-0.3%), 200d 64.14 (+6.0%); 50d above 200d
Momentum: RSI(14) 50.2 | MACD -0.225 vs signal -0.310 (histogram 0.085)
Returns: 1d -0.1% | 5d +0.2% | 1m -1.4% | 3m -1.6%
52-week range: 55.33 - 71.61 (now 77.6% of the way up)
Volatility: ATR(14) 0.87 (1.3% of price) | annualised 20d 16.5%
Volume: 0.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +24.9% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.8% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, NBIS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-09-24 BNP Paribas: up, Neutral -> Outperform
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
Shares outstanding: 5.55M | fund size: 377.18M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals show short‑term weakness but long‑term uptrend, flat fund flows, modest analyst bullishness, fundamentals moderately positive.

**Main reasons it gave:**
- Analyst coverage: 52% buy, 48% hold, weighted price target +2.1% (slight bullish bias)
- Fund flows: flat share count change (0% net inflow/outflow) over the past week
- Technicals: price 1.7% below 20‑day SMA and 1.9% below 50‑day SMA, MACD negative, volume 0.14× 20‑day average (short‑term weakness)
- Macro: US Treasury yields rose modestly, dollar index up 0.76% on the week, VIX at 15.86 (no major surprise)
- Fundamentals: P/E 16.28, 3‑yr return +34.9%/yr, yield 2.7% (moderately positive)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 60.41 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 61.47 (-1.7%), 50d 61.61 (-1.9%), 200d 57.48 (+5.1%); 50d above 200d
Momentum: RSI(14) 43.0 | MACD -0.295 vs signal -0.172 (histogram -0.123)
Returns: 1d -1.3% | 5d -1.6% | 1m -3.2% | 3m +2.0%
52-week range: 48.33 - 63.23 (now 81.1% of the way up)
Volatility: ATR(14) 0.81 (1.3% of price) | annualised 20d 17.4%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.28 | P/B 2.22 | P/S 1.82 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +34.9% a year | beta to the market 0.87
Cost and size: expense ratio 0.50% | net assets 2.26B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.0%, Iberdrola SA 12.1%, CaixaBank SA 4.6%, Industria De Diseno Textil SA Share From Split 4.4%
Sector mix: Financial services 45.4%, Utilities 20.0%, Industrials 14.4%, Technology 5.9%
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
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.1% above the current prices
Holdings read: SAN.MC, BBVA.MC, IBE.MC, CABK.MC, ITX.MC
Recent rating changes among them:
  - SAN.MC: 2023-11-08 JP Morgan: main, Neutral -> Neutral
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
Shares outstanding: 37.35M | fund size: 2.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – technicals show slight bearishness, flows are flat, and no macro surprise; analyst view is moderately bullish but not enough to shift direction.

**Main reasons it gave:**
- Price below 20‑day and 50‑day SMA (‑1.2%/‑1.6%) indicating slight bearish technicals
- Negative MACD and RSI 42 suggesting modest downside momentum
- Fund flows flat (share count +0.0% over 1 week) showing no net demand
- Analyst coverage 69.5% buy with +11.1% price target, moderately bullish but not decisive
- Treasury yields up across curve (+0.10 to +0.27) with steepening yield curve (+1.15) and no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 47.24 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 47.81 (-1.2%), 50d 48.02 (-1.6%), 200d 46.62 (+1.3%); 50d above 200d
Momentum: RSI(14) 42.0 | MACD -0.250 vs signal -0.166 (histogram -0.084)
Returns: 1d -0.2% | 5d -0.9% | 1m -2.8% | 3m +2.4%
52-week range: 41.34 - 49.39 (now 73.4% of the way up)
Volatility: ATR(14) 0.45 (0.9% of price) | annualised 20d 11.2%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.08 | P/B 2.29 | P/S 1.52 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +18.6% a year | beta to the market 0.68
Cost and size: expense ratio 0.50% | net assets 3.79B
What it is made of: Stocks 97.9%, Other 1.1%, Cash 0.9%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 7.8%, AstraZeneca PLC 7.6%, Rolls-Royce Holdings PLC 5.3%, Unilever PLC 4.3%
Sector mix: Financial services 26.4%, Consumer defensive 14.3%, Industrials 13.9%, Healthcare 12.7%
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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 69.5% | hold 30.5% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.1% above the current prices
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 67.80M | fund size: 3.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – technicals are bearish but low volume, analyst coverage is strongly positive, fundamentals are solid, and macro pressures on emerging markets are modest with no surprise data. No clear catalyst to tilt the view.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs with negative momentum (RSI 37.9, MACD -0.884)
- Analyst coverage of top holdings is 100% buy with a weighted price target +16.7% above current prices
- Fund flows flat over the past week (share count unchanged)
- US yields rising and dollar strengthening, which can pressure emerging‑market equities

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 72.37 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 74.76 (-3.2%), 50d 75.68 (-4.4%), 200d 75.78 (-4.5%); 50d below 200d
Momentum: RSI(14) 37.9 | MACD -0.884 vs signal -0.661 (histogram -0.223)
Returns: 1d -1.3% | 5d -1.8% | 1m -6.2% | 3m -4.9%
52-week range: 64.39 - 81.23 (now 47.4% of the way up)
Volatility: ATR(14) 1.25 (1.7% of price) | annualised 20d 17.2%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.68 | P/B 1.98 | P/S 1.49 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +11.5% a year | beta to the market 1.05
Cost and size: expense ratio 0.50% | net assets 1.82B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Grupo Mexico SAB de CV Class B 16.6%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.3%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Cemex SAB de CV 4.4%
Sector mix: Basic materials 27.3%, Consumer defensive 24.4%, Financial services 19.7%, Industrials 11.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.44</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.44</summary>

```text
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.7% above the current prices
Holdings read: GMEXICOB.MX, GFNORTEO.MX, FEMSAUBD.MX, AMXB.MX, CEMEXCPO.MX
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

> Neutral overall: no macro surprise, flat fund flows, low valuation, technicals show slight bearish momentum but no decisive break.

**Main reasons it gave:**
- Flat fund flows (share count change +0.0% over 1 week) indicating no net demand
- Low P/E ratio (10.41) suggests undervaluation
- Price below 20‑day SMA (-0.9%) and negative MACD histogram (-0.264) indicate slight bearish momentum
- US Treasury yields rose across the curve (10‑year +0.27% week) and dollar index up 0.76% may pressure risk assets

<details><summary><b>News</b> — score +0.00</summary>

- [Tokenized iShares MSCI South Korea ETF Arrives on StonkFun for Solana Coin Launches](https://www.cryptoninjas.net/news/tokenized-ishares-msci-south-korea-etf-arrives-on-stonkfun-for-solana-coin-launches/)  
  <sub>CryptoNinjas, 23 hours ago</sub>  
  Key Takeaways: StonkFun now supports coin launches paired with $EWY, the tokenized iShares MSCI South Korea ETF. Overall, the integration bridges the gap...
- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 181.66 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 183.39 (-0.9%), 50d 175.26 (+3.7%), 200d 154.38 (+17.7%); 50d above 200d
Momentum: RSI(14) 49.9 | MACD 2.028 vs signal 2.292 (histogram -0.264)
Returns: 1d -2.9% | 5d -4.0% | 1m -0.3% | 3m -8.0%
52-week range: 78.87 - 219.20 (now 73.2% of the way up)
Volatility: ATR(14) 6.47 (3.6% of price) | annualised 20d 48.1%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +49.2% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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
Rolled up from the 5 largest holdings, 53.5% of the fund by weight
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
Shares outstanding: 75.60M | fund size: 13.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Analyst view is bullish (100% buy, +30.8% price target) but covers only 40.9% of the fund; fundamentals are modestly attractive (P/E 10.48, yield 4.1%); fund flows are flat, indicating neutral demand; technicals show slight bearish momentum (price below 20‑day SMA, MACD negative, RSI 43.6). No macro surprise or decisive technical break, so overall stance remains neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 40.9% of fund, weighted price target +30.8% above current price
- Fund flows: share count unchanged (+0.0% over 7 days), indicating neutral demand
- Fund basics: P/E 10.48 and dividend yield 4.1% suggest modest valuation attractiveness
- Technical indicators: price 3.4% below 20‑day SMA, MACD histogram -0.244, RSI 43.6 indicate slight bearish momentum

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.31 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 37.60 (-3.4%), 50d 36.24 (+0.2%), 200d 36.30 (+0.0%); 50d below 200d
Momentum: RSI(14) 43.6 | MACD 0.260 vs signal 0.504 (histogram -0.244)
Returns: 1d -1.4% | 5d -4.6% | 1m +1.5% | 3m +5.1%
52-week range: 28.79 - 41.73 (now 58.1% of the way up)
Volatility: ATR(14) 0.78 (2.1% of price) | annualised 20d 24.2%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.48 | P/B 1.79 | P/S 1.28 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +12.3% a year | beta to the market 0.84
Cost and size: expense ratio 0.59% | net assets 8.17B
What it is made of: Stocks 96.5%, Cash 2.7%, Preferred 0.8%
Largest holdings: Vale SA 10.1%, Nu Holdings Ltd Ordinary Shares Class A 9.5%, Itau Unibanco Holding SA Participating Preferred 7.7%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.0%, Petroleo Brasileiro SA Petrobras 6.6%
Sector mix: Financial services 34.1%, Energy 17.4%, Basic materials 14.5%, Utilities 12.4%
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
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.8% above the current prices
Holdings read: VALE3.SA, NU, ITUB4, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-09-28 Needham: reit, Buy -> Buy
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
Shares outstanding: 200.55M | fund size: 7.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Technicals show price below 20‑day, 50‑day and 200‑day SMAs with RSI 34.9 (weak momentum)
- Fund flows flat over the past week (no net inflow or outflow)
- Analyst coverage bullish for 45.6% of the fund with a weighted price target +31.5% above current price
- Macro environment unchanged; yields rising, dollar up, VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 64.31 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 68.92 (-6.7%), 50d 67.64 (-4.9%), 200d 69.25 (-7.1%); 50d below 200d
Momentum: RSI(14) 34.9 | MACD -0.761 vs signal -0.114 (histogram -0.646)
Returns: 1d -3.3% | 5d -5.7% | 1m -10.1% | 3m +1.4%
52-week range: 60.43 - 81.60 (now 18.3% of the way up)
Volatility: ATR(14) 1.40 (2.2% of price) | annualised 20d 26.8%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 9.31 | P/B 2.24 | P/S 1.92 | 3y earnings growth n/a
Yield: 7.1%
Three-year record: +26.9% a year | beta to the market 1.02
Cost and size: expense ratio 0.59% | net assets 578.49M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 13.7%, Gold Fields Ltd 9.9%, Naspers Ltd Class N 8.8%, Firstrand Ltd 7.1%, Standard Bank Group Ltd 6.1%
Sector mix: Basic materials 41.0%, Financial services 33.2%, Consumer cyclical 12.8%, Communication services 6.2%
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
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.5% above the current prices
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
Shares outstanding: 7.90M | fund size: 508.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Fund flows: -0.9% share count change (outflows) over 1 week
- Analyst view: 100% buy rating with +18% price target for 39.9% of fund
- Technicals: price below 20d, 50d, 200d SMAs; RSI 40.3, MACD negative, low volume
- Macro: yields rose modestly (10y +0.27% week) and dollar strengthened (+0.76% week) with no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [[Quiddity Index] MV Global Gold Miners Dec26 Rebal: No Changes Likely; Vault-Genesis Deal Flows](https://www.smartkarma.com/insights/quiddity-index-mv-global-gold-miners-dec26-rebal-no-changes-likely-vault-genesis-deal-flows)  
  <sub>Smartkarma, 5 hours ago</sub>  
  For now, no changes are expected for the GDX ETF rebal in December 2026. Between now and then, there will be ad hoc changes due to the expected completion...
- [Gold resilience tested as yield surge and stronger dollar weigh (GLD:NYSEARCA)](https://seekingalpha.com/news/4647447-gold-resilience-tested-as-yield-surge-and-stronger-dollar-weigh)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  How much longer can the divergence between gold investment demand and US real yields continue? Saxo Bank says Monday's price action suggests the...
- [Gold Bull Run Looks Finished—Unless You Look Closer](https://www.benzinga.com/markets/commodities/26/09/62016691/gold-bull-run-looks-finished-unless-you-look-closer)  
  <sub>Benzinga, 4 hours ago</sub>  
  Gold prices drop 3.35% as hawkish Fed sentiment and Chinese profit-taking end the August rally. Key chart patterns & outlook inside.
- [September saw Nasdaq-100 hit records; PCE infla...](https://pluang.com/en/news-feed/mode-waspada-inflasi-mempersiapkan-data-pce-rabu)  
  <sub>Pluang, 13 hours ago</sub>  
  September defied its usual bearish trend with the Nasdaq-100 reaching new highs and the S&P 500 nearing its peak. The upcoming PCE inflation report is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 88.40 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 95.72 (-7.7%), 50d 90.35 (-2.2%), 200d 91.04 (-2.9%); 50d below 200d
Momentum: RSI(14) 40.3 | MACD -0.238 vs signal 0.977 (histogram -1.215)
Returns: 1d -4.8% | 5d -6.4% | 1m -14.7% | 3m +16.8%
52-week range: 68.28 - 115.84 (now 42.3% of the way up)
Volatility: ATR(14) 3.49 (3.9% of price) | annualised 20d 42.6%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.84 | P/B 2.68 | P/S 4.10 | 3y earnings growth n/a
Yield: 0.6%
Three-year record: +50.0% a year | beta to the market 0.83
Cost and size: expense ratio 0.51% | net assets 30.54B
What it is made of: Stocks 100.0%
Largest holdings: Newmont Corp 10.7%, Agnico Eagle Mines Ltd 10.7%, Barrick Mining Corp 7.4%, Wheaton Precious Metals Corp 5.8%, Anglogold Ashanti PLC 5.3%
Sector mix: Basic materials 100.0%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.0% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: money going out (1 week)
Share count change: 1 week: -0.9% (-263.57M) over 7d
Shares outstanding: 325.83M | fund size: 28.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, mixed technicals, high valuations, but strong analyst consensus.

**Main reasons it gave:**
- Fund flows flat: 0% change in share count over the week
- IGV slid 2% on news of Meta's enterprise platform launch, indicating sector weakness
- Price below 20‑day SMA (104.43 vs 105.26) and MACD histogram negative (-0.197)
- Valuation metrics high: P/E 34.2, P/B 8.09, P/S 9.07
- Analyst consensus 100% buy with weighted price target +7.4% above current price

<details><summary><b>News</b> — score +0.00</summary>

- [JPMorgan’s basket of security software stocks outperforms as AI threats mount (CIBR:NASDAQ)](https://seekingalpha.com/news/4647628-jpmorgan-s-basket-of-security-software-stocks-rallies-as-ai-threats-mount)  
  <sub>Seeking Alpha, 7 minutes ago</sub>  
  Cybersecurity stocks are rallying on AI security fears, beating the shaky software sector despite rich valuations.
- [Stocktwits Tech Watch: Micron’s Q4 Report, OpenAI Developer Conference Keep AI Trade In Focus This Week](https://www.tradingview.com/news/stocktwits:3d63b581b094b:0-stocktwits-tech-watch-micron-s-q4-report-openai-developer-conference-keep-ai-trade-in-focus-this-week/)  
  <sub>TradingView, 8 hours ago</sub>  
  It's been a lull on the earnings front, but analysts and investors will be waking from their slumber for one of the most crucial reports this week: Micron's...
- [Meta and ServiceNow Drop 4% as Enterprise Platform Launch Reprices Software; MongoDB Tumbles 19%](https://247wallst.com/investing/2026/09/28/meta-and-servicenow-drop-4-as-enterprise-platform-launch-reprices-software-mongodb-tumbles-19/)  
  <sub>24/7 Wall St., 9 minutes ago</sub>  
  Meta's enterprise platform launch and hire of MongoDB CEO CJ Desai sent META down 4% and MDB plunging 19% in morning trading. IGV slid just 1% while...
- [My Research](https://www.bespokepremium.com/interactive/posts/think-big-blog/bespokes-morning-lineup-5-12-26-cpi-looms)  
  <sub>Bespoke Investment Group, 7 hours ago</sub>  
  See what's driving market performance around the world in today's Morning Lineup. Bespoke's Morning Lineup is the best way to start your trading day.
- [Meta's new enterprise push hits ServiceNow, Salesforce and Microsoft](https://seekingalpha.com/news/4647601-metas-new-enterprise-push-hits-servicenow-salesforce-and-microsoft)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Meta's new Enterprise Platform shook SaaS stocks—IGV slid 2% and major names fell.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 104.43 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 105.26 (-0.8%), 50d 101.62 (+2.8%), 200d 93.63 (+11.5%); 50d above 200d
Momentum: RSI(14) 49.9 | MACD 1.099 vs signal 1.296 (histogram -0.197)
Returns: 1d -1.5% | 5d -2.5% | 1m -5.3% | 3m +16.2%
52-week range: 74.67 - 117.08 (now 70.2% of the way up)
Volatility: ATR(14) 2.55 (2.4% of price) | annualised 20d 32.8%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 34.20 | P/B 8.09 | P/S 9.07 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +15.9% a year | beta to the market 1.21
Cost and size: expense ratio 0.38% | net assets 15.74B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Palantir Technologies Inc Ordinary Shares - Class A 10.3%, Palo Alto Networks Inc 9.7%, Microsoft Corp 9.2%, CrowdStrike Holdings Inc Class A 7.4%, Salesforce Inc 6.6%
Sector mix: Technology 94.4%, Communication services 3.8%, Financial services 1.5%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.4% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-23 Rosenblatt: main, Buy -> Buy
  - PANW: 2026-09-28 BTIG: main, Buy -> Buy
  - MSFT: 2026-09-23 Stifel: up, Hold -> Buy
  - CRWD: 2026-09-21 Morgan Stanley: main, Overweight -> Overweight
  - CRM: 2026-09-18 Citizens: reit, Market Outperform -> Market Outperform
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
Shares outstanding: 12.50M | fund size: 1.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest outflows, thin but bullish analyst coverage, technicals bearish but not decisive.

**Main reasons it gave:**
- Analyst coverage thin (24.7% weight) but bullish (buy 100%, price target +34.6%)
- Fund flows net outflows of -1.4% (≈ -$95.8M) over the past week
- US Treasury yields up (10-year +0.27% on week) and dollar stronger (+0.76% on week) – bearish for emerging markets
- Technical indicators bearish: price below 20d, 50d, 200d SMAs; RSI 33.9

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 47.01 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 48.51 (-3.1%), 50d 49.12 (-4.3%), 200d 49.99 (-6.0%); 50d below 200d
Momentum: RSI(14) 33.9 | MACD -0.498 vs signal -0.400 (histogram -0.098)
Returns: 1d -1.8% | 5d -3.1% | 1m -5.1% | 3m -4.4%
52-week range: 45.42 - 55.29 (now 16.1% of the way up)
Volatility: ATR(14) 0.47 (1.0% of price) | annualised 20d 14.4%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: India Equity
What it holds: P/E 22.87 | P/B 3.14 | P/S 2.72 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.6% a year | beta to the market 0.56
Cost and size: expense ratio 0.61% | net assets 6.75B
What it is made of: Stocks 100.1%, Cash -0.1%
Largest holdings: HDFC Bank Ltd 6.4%, Reliance Industries Ltd 6.0%, ICICI Bank Ltd 5.7%, Bharti Airtel Ltd 4.1%, Infosys Ltd 2.6%
Sector mix: Financial services 30.1%, Consumer cyclical 12.8%, Industrials 9.7%, Energy 8.6%
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
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.6% above the current prices
Holdings read: HDFCBANK.NS, RELIANCE.NS, ICICIBANK.NS, BHARTIARTL.NS, INFY.NS
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
Share count change: 1 week: -1.4% (-95.84M) over 7d
Shares outstanding: 139.62M | fund size: 6.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows modest net inflows (+0.6% share count) indicating slight demand, while analyst coverage is uniformly bullish (100% buy, price target +27.9% above current) but lacks a macro catalyst. Technicals show the price below key moving averages and a low RSI (27.5) with low volume, suggesting no decisive break. Macro conditions (rising yields, low VIX) are neutral with no surprise data. Overall, these factors balance out to a neutral stance.

**Main reasons it gave:**
- Fund flows: share count +0.6% over 1 week (net inflow)
- Analyst coverage: 100% buy, weighted price target +27.9% above current
- Technicals: price 210.65 below 20‑day SMA 218.21, RSI 27.5 (oversold) with low volume
- Macro: Treasury yields up (10‑yr +0.27% week) and VIX 15.86 (low), no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [Why Is Boeing Stock Falling Monday?](https://www.benzinga.com/trading-ideas/movers/26/09/62023166/why-is-boeing-stock-falling-monday)  
  <sub>Benzinga, 49 minutes ago</sub>  
  Boeing stock falls as a 737 MAX software glitch risks automated navigation failure during landing. Get the full market breakdown.
- [Boeing Drops 3% as 737 MAX Landing Software Glitch Draws Regulator Review; GE Aerospace Eases, RTX Treads Water](https://finance.yahoo.com/markets/stocks/articles/boeing-drops-3-737-max-130009478.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  A software glitch buried in the 737 MAX cockpit just drew regulator attention, and the timing could not be worse for a company already fighting to prove its...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 210.65 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 218.21 (-3.5%), 50d 232.77 (-9.5%), 200d 230.47 (-8.6%); 50d above 200d
Momentum: RSI(14) 27.5 | MACD -6.128 vs signal -6.258 (histogram 0.130)
Returns: 1d -1.5% | 5d -2.5% | 1m -10.1% | 3m -11.9%
52-week range: 198.23 - 253.22 (now 22.6% of the way up)
Volatility: ATR(14) 4.02 (1.9% of price) | annualised 20d 14.3%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 34.66 | P/B 6.62 | P/S 3.21 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +27.1% a year | beta to the market 0.99
Cost and size: expense ratio 0.37% | net assets 13.63B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: GE Aerospace 21.6%, RTX Corp 17.2%, Boeing Co 9.1%, General Dynamics Corp 4.8%, Lockheed Martin Corp 4.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.9% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-09-23 Jefferies: main, Buy -> Buy
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-21 Jefferies: main, Buy -> Buy
  - GD: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - LMT: 2026-09-08 UBS: up, Neutral -> Buy
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
Share count change: 1 week: +0.6% (85.10M) over 7d
Shares outstanding: 63.72M | fund size: 13.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Analyst coverage of top holdings (53.1% weight) shows 90.8% buy rating and a weighted price target +26.8% above current price
- Fund flows are flat over the past week, indicating no net demand shift
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs with RSI 29.4, but no decisive break on volume
- Macro data show no surprise: yields up modestly, inflation 3.4% near target, VIX low at 15.86

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Are Net Sellers of Uber (UBER) on Sept. 24](https://www.gurufocus.com/news/9099422/etfs-are-net-sellers-of-uber-uber-on-sept-24)  
  <sub>GuruFocus, 4 hours ago</sub>  
  The iShares U.S. Transportation ETF (IYT) led the move, cutting 319865 shares worth $22.1 million. On Thursday, ETFs sold a net $33.9 million of Uber (UBER)...
- [ETFs Are Net Sellers of Union Pacific (UNP) on Thursday](https://www.gurufocus.com/news/9099412/etfs-are-net-sellers-of-union-pacific-unp-on-thursday)  
  <sub>GuruFocus, 4 hours ago</sub>  
  In Thursday's session, 29 ETFs bought Union Pacific (UNP) while 23 sold, but the sellers traded larger amounts, leaving net selling of $56.8 million.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 78.79 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 81.53 (-3.4%), 50d 84.78 (-7.1%), 200d 81.20 (-3.0%); 50d above 200d
Momentum: RSI(14) 29.4 | MACD -1.723 vs signal -1.559 (histogram -0.164)
Returns: 1d -0.7% | 5d -1.3% | 1m -8.8% | 3m -10.1%
52-week range: 68.14 - 90.01 (now 48.7% of the way up)
Volatility: ATR(14) 1.19 (1.5% of price) | annualised 20d 15.9%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Industrials
What it holds: P/E 20.28 | P/B 4.25 | P/S 1.45 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +11.8% a year | beta to the market 1.28
Cost and size: expense ratio 0.37% | net assets 2.20B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Union Pacific Corp 17.8%, Uber Technologies Inc 15.4%, CSX Corp 9.4%, United Parcel Service Inc Class B 5.6%, Norfolk Southern Corp 4.9%
Sector mix: Industrials 83.8%, Technology 16.2%
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
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.8% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
  - UBER: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
  - CSX: 2026-09-18 B of A Securities: main, Buy -> Buy
  - UPS: 2026-07-29 Stifel: main, Buy -> Buy
  - NSC: 2026-07-27 BMO Capital: main, Market Perform -> Market Perform
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
Shares outstanding: 2.80M | fund size: 220.61M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show price below key SMAs and weak momentum, but no decisive break; fund flows are flat with a slight uptick; analyst coverage is bullish but limited to 44.4% of the fund; macro data show modest yield rises with no surprise. The mix of these factors leads to a neutral stance.

**Main reasons it gave:**
- Price 36.85 below 20‑day SMA 37.80 (‑2.5%) and 200‑day SMA 38.14 (‑3.4%)
- RSI 32.9 and MACD negative, indicating weak momentum
- Share count up 0.5% (3.14 M) over 7 days, flat flow
- Analyst coverage 44.4% of fund, 90% buy rating, +16.7% price target
- US Treasury yields rose modestly (3‑month +0.10%, 10‑year +0.27% on week), no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.85 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 37.80 (-2.5%), 50d 37.80 (-2.5%), 200d 38.14 (-3.4%); 50d below 200d
Momentum: RSI(14) 32.9 | MACD -0.331 vs signal -0.204 (histogram -0.126)
Returns: 1d -0.5% | 5d -0.8% | 1m -6.2% | 3m -1.5%
52-week range: 35.83 - 41.03 (now 19.6% of the way up)
Volatility: ATR(14) 0.28 (0.8% of price) | annualised 20d 8.2%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.00 | P/B 1.81 | P/S 3.04 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +1.6% a year | beta to the market 0.18
Cost and size: expense ratio 0.75% | net assets 638.50M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.1%, Saudi National Bank 8.8%, Saudi Telecom Co 6.0%, Saudi Arabian Mining Co 4.4%
Sector mix: Financial services 41.9%, Basic materials 12.7%, Energy 12.1%, Communication services 8.8%
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
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.7% above the current prices
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
Share count change: 1 week: +0.5% (3.14M) over 7d
Shares outstanding: 17.12M | fund size: 630.80M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst view on top holdings (32.2% weight) and cheap fundamentals, but bearish fund outflows, weak technicals, and rising US yields/dollar.

**Main reasons it gave:**
- Fund flows: 1.5% share count decline (outflow) over 1 week
- Technicals: price below 20d, 50d, 200d SMAs; RSI 39.8, MACD negative
- Macro: US Treasury yields rising across curve; dollar up; VIX up
- Analyst view: 100% buy rating on top 5 holdings (32.2% weight) with +53.6% price target
- Fundamentals: low P/E 11.9, low P/B 1.39, 3-year return 9.4% per year

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 52.53 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 53.48 (-1.8%), 50d 54.44 (-3.5%), 200d 57.00 (-7.8%); 50d below 200d
Momentum: RSI(14) 39.8 | MACD -0.469 vs signal -0.422 (histogram -0.047)
Returns: 1d -0.2% | 5d -2.7% | 1m -4.3% | 3m +3.4%
52-week range: 50.48 - 66.99 (now 12.4% of the way up)
Volatility: ATR(14) 0.59 (1.1% of price) | annualised 20d 15.4%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.90 | P/B 1.39 | P/S 1.38 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +9.4% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 6.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Tencent Holdings Ltd 13.9%, Alibaba Group Holding Ltd Ordinary Shares 9.6%, China Construction Bank Corp Class H 4.0%, Industrial And Commercial Bank Of China Ltd Class H 2.5%, Xiaomi Corp Class B 2.4%
Sector mix: Consumer cyclical 23.4%, Financial services 20.0%, Communication services 18.2%, Technology 11.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +53.6% above the current prices
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
Share count change: 1 week: -1.5% (-97.51M) over 7d
Shares outstanding: 118.65M | fund size: 6.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show an uptrend but recent price drop on low volume, flat fund flows, and strong analyst bullishness is offset by high valuation and rising yields.

**Main reasons it gave:**
- Treasury yields rose modestly across the curve (+0.10 to +0.27) with no policy surprise
- SMH price above 20‑, 50‑, and 200‑day SMAs, but down 2.1% on low volume
- Fund flows flat (0.0% share count change) over the past week
- Analyst consensus 100% buy with +36.7% price target, but high valuation (P/E 37.78) and rising yields temper bullishness

<details><summary><b>News</b> — score +0.00</summary>

- [The Nasdaq Nears a Major Breakout: 5 Tech ETFs to Play the Move](https://www.marketbeat.com/articles/the-nasdaq-nears-a-major-breakout-5-tech-etfs-to-play-the-move/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  As the Nasdaq-100 nears its all-time high, QQQ, XLK, SMH, QQQI, and SOXX offer distinct ways to gain tech and semiconductor exposure, from low-cost to...
- [CHIP vs NECK vs AIBF: Which Part of the AI Boom Does Each ETF Cover?](https://www.ebc.com/forex/chip-vs-neck-vs-aibf-ai-etf-comparison)  
  <sub>EBC Financial Group, 7 hours ago</sub>  
  CHIP, NECK and AIBF target different parts of AI. Compare holdings, fees, overlap and risks across three newly launched AI ETFs.
- [S&P 500, Dow, Nasdaq Drop As Yields Spike Amid Calls For More Rate Hikes — AMZN, GOOGL, NFLX, SPCX, RKLB In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-drop-as-yields-spike-amid-calls-for-more-rate-hikes-amzn-googl-nflx-spcx-rklb-in-focus/cZM4IxjRBB9)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Treasury yields jumped across the curve on Wednesday.
- [S&P 500, Dow Snap Three-Day Losses, Nasdaq Ends Best Day In Three Weeks As Earnings Take Centerstage — GOOGL, AAPL, AMD, TSLA, DIS In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-snap-three-day-losses-nasdaq-ends-best-day-in-three-weeks-earnings-take-centerstage/cZZS8knR7vC)  
  <sub>Stocktwits, 21 hours ago</sub>  
  U.S. stock indices ended higher on Tuesday, as a surge in chipmaker stocks and a strong set of earnings reports boosted investor sentiment.
- [This Week's Market Watch (September 28 - October 2)](https://www.moomoo.com/community/feed/this-week-s-market-watch-september-28-october-2-117349129519509)  
  <sub>Moomoo, 25 minutes ago</sub>  
  Stocks have surged—but can the rally hold? This week brings two major tests: Micron's earnings on Wednesday and the U.S. jobs report on Friday. With m...
- [Dow Soars 800 Points Driven By Healthcare Stocks — But Chip Stocks Drag S&P 500, Nasdaq](https://stocktwits.com/news-articles/markets/equity/dow-soars-as-investors-flee-chip-stocks-pile-into-healthcare-sector/cZ0ZLU0Reys)  
  <sub>Stocktwits, 14 hours ago</sub>  
  U.S. equities were split in Thursday morning's trade as investors rotated out of chip stocks and piled into healthcare, financials, and communication...
- [Nasdaq Posts Worst Drop Since April 2025, S&P 500 And Dow Drop As Strong Jobs Data Ignites Rate Hike Bets — TSLA, GME, META, BA, MSTR, GOOGL In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-posts-worst-drop-since-april-2025-s-and-p-500-and-dow-drop-as-strong-jobs-data-ignites-rate-hike-bets-tsla-gme-meta-ba-mstr-in-focus/cZ0FUXKReCv)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Nasdaq, S&P 500 and Dow Jones indices all ended the week ending June 5, lower.
- [Dow Ends Higher For Third Straight Session As Oil Cools, Nasdaq Slides On Chipmaker Rout — PYPL, SPCX, AAPL, V, F Stocks In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-continues-to-drop-on-chipmaker-rout/cZZ6TnzRJbt)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The S&P 500 ended 0.2% higher, while the Nasdaq 100 slipped 1% and the Dow Jones Industrial Average added 1%. Brent crude prices dropped close to 5% to end...
- [Dow, S&P 500, Nasdaq Futures Climb As AI Frenzy Drives Record Rally: Why CSCO, LUNR, ONDS, NVDA, NOK Are In Focus](https://stocktwits.com/news-articles/markets/equity/dow-sp500-nasdaq-futures-ai-rally-csco-lunr-onds-nvda-nok/cZX1B5sReKw)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Investors monitored Trump's Beijing trip to meet Chinese President Xi Jinping, fueling hopes of easing tensions around AI chip exports to China.
- [Dow, S&P 500, Nasdaq Futures Rise As Investors Shrug Off Fed Hold, Big Tech Earnings: IBRX, MSFT, SOFI, META In Focus](https://stocktwits.com/news-articles/markets/equity/dow-s-and-p-500-nasdaq-futures-rise-as-investors-shrug-off-fed-hold-big-tech-earnings-ibrx-msft-sofi-meta-in-focus/cZNPmOkRJTM)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Fed Chair Kevin Warsh's second policy decision passed by a 9-3 vote, with three policymakers favouring a quarter-point hike.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 593.56 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 570.85 (+4.0%), 50d 566.63 (+4.8%), 200d 494.40 (+20.1%); 50d above 200d
Momentum: RSI(14) 56.9 | MACD 9.296 vs signal 4.369 (histogram 4.928)
Returns: 1d -2.1% | 5d -0.4% | 1m +3.6% | 3m -6.1%
52-week range: 321.82 - 668.91 (now 78.3% of the way up)
Volatility: ATR(14) 16.08 (2.7% of price) | annualised 20d 32.8%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Technology
What it holds: P/E 37.78 | P/B 11.07 | P/S 13.20 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +62.6% a year | beta to the market 2.06
Cost and size: expense ratio 0.35% | net assets 67.79B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 22.6%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.7%, Broadcom Inc 6.1%, Micron Technology Inc 5.5%, Advanced Micro Devices Inc 5.4%
Sector mix: Technology 100.0%
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
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.7% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-28 Wedbush: reit, Outperform -> Outperform
  - AMD: 2026-09-25 B of A Securities: main, Buy -> Buy
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
Shares outstanding: 11.67M | fund size: 6.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro risk‑off, bearish technicals, bullish analyst view, flat flows.

**Main reasons it gave:**
- US Treasury yields rose across the curve (+0.10 to +0.27) and the dollar index gained 0.76% on the week, indicating a risk‑off environment for emerging markets
- TUR price is below its 20‑day, 50‑day and 200‑day SMAs (down 8‑10%) with RSI 31.4 and negative MACD, showing bearish technical momentum
- Analyst coverage of the top holdings (39.5% of fund) is 100% buy with a +19.9% price target, indicating bullish sentiment on the underlying stocks
- Fund flows are flat over the past week (share count unchanged), suggesting no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 35.46 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 38.52 (-8.0%), 50d 39.02 (-9.1%), 200d 39.33 (-9.9%); 50d below 200d
Momentum: RSI(14) 31.4 | MACD -0.899 vs signal -0.552 (histogram -0.346)
Returns: 1d -2.5% | 5d -5.8% | 1m -12.5% | 3m -9.1%
52-week range: 31.90 - 43.74 (now 30.0% of the way up)
Volatility: ATR(14) 0.76 (2.1% of price) | annualised 20d 35.6%
Volume: 0.61x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: -0.1% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.9% above the current prices
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
Shares outstanding: 15.65M | fund size: 554.87M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro pressure from rising yields but no surprise, mixed fundamentals, bullish analyst coverage limited to ~40% of fund, technicals show downtrend but oversold.

**Main reasons it gave:**
- 10-year Treasury yield rose 27 bps this week, pressuring REIT valuations
- Analyst coverage 39.9% of VNQ, 100% buy rating with +18.5% price target
- RSI at 26 indicating oversold conditions, but price below 20d, 50d, 200d SMAs
- Fund fundamentals: P/E 30.19, yield 3.6%, 3-year annual return +10.1%

<details><summary><b>News</b> — score +0.00</summary>

- [VNQ: The REIT Bloodbath Is Here (NYSEARCA:VNQ)](https://seekingalpha.com/article/4950132-vnq-the-reit-bloodbath-is-here)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  The Vanguard Real Estate ETF faces sharp declines, down nearly 10% in the past month amid surging Treasury yields and a Fed rate hike. Learn more about VNQ...
- [Vanguard Real Estate ETF drops nearly 10% amid rising Treasury yields and Fed rate hikes](https://pluang.com/en/news-feed/vnq-darah-dingin-reit-saat-suku-bunga-naik)  
  <sub>Pluang, 6 hours ago</sub>  
  The Vanguard Real Estate ETF (VNQ) has fallen almost 10% in the last month due to rising Treasury yields and a recent Federal Reserve interest rate hike.
- [ETFs Investing in Essential Properties Realty Trust, Inc. Stocks](https://www.tradingview.com/symbols/FWB-2OU/etfs/)  
  <sub>TradingView, 14 hours ago</sub>  
  Explore funds investing in 2OU in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/VWO/)  
  <sub>Yahoo Finance Singapore, 6 hours ago</sub>  
  Find the latest Vanguard FTSE Emerging Markets Index Fund ETF Shares (VWO) stock quote, history, news and other vital information to help you with your...
- [The REIT Market Is Crashing: Here Is What I Am Buying](https://seekingalpha.com/article/4950191-reit-market-crashing-here-is-what-i-am-buying)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  REITs are sliding as rates spike. Learn why higher yields could boost long-term rent growth and which well-capitalized landlords to watch—read now.
- [Zurich and Tokyo top UBS housing bubble risk index as global price growth slows (VNQ:NYSEARCA)](https://seekingalpha.com/news/4647397-zurich-and-tokyo-top-ubs-housing-bubble-risk-index-as-global-price-growth-slows)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  UBS Global Real Estate Bubble Index 2026 flags Zurich & Tokyo as high risk, Miami elevated.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 90.73 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 94.07 (-3.6%), 50d 96.89 (-6.4%), 200d 94.36 (-3.9%); 50d above 200d
Momentum: RSI(14) 26.0 | MACD -1.633 vs signal -1.333 (histogram -0.300)
Returns: 1d -0.3% | 5d -3.3% | 1m -7.1% | 3m -7.6%
52-week range: 87.00 - 100.95 (now 26.7% of the way up)
Volatility: ATR(14) 1.10 (1.2% of price) | annualised 20d 11.9%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +10.1% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 70.82B
What it is made of: Stocks 99.1%, Cash 0.7%, Other 0.2%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 8.7%, Prologis Inc 6.9%, Equinix Inc 5.5%, American Tower Corp 4.3%
Sector mix: Real estate 99.4%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.5% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-08-20 Barclays: up, Equal-Weight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed evidence: bullish analyst view (78.9% buy, +21% price target) but thin coverage; slight net redemption of -0.3% over the week; technicals show price below short‑, medium‑ and long‑term averages with RSI 41 and negative MACD; macro shows rising yields and inflation above target, pressuring consumer‑cyclical exposure. No clear macro catalyst or decisive technical break, so overall neutral.

**Main reasons it gave:**
- Analyst coverage: 78.9% buy, price target +21% (covers 20.9% of fund)
- Fund flows: -0.3% share count change (~-4.1M) over 1 week (slight outflow)
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 41; MACD negative (downtrend)
- Macro: yields up (10‑yr +0.27% week) and inflation 3.4% above Fed target (consumer cyclical pressure)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 97.44 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 98.89 (-1.5%), 50d 103.95 (-6.3%), 200d 106.39 (-8.4%); 50d below 200d
Momentum: RSI(14) 41.1 | MACD -2.037 vs signal -2.257 (histogram 0.220)
Returns: 1d -0.9% | 5d +0.5% | 1m -6.8% | 3m -15.6%
52-week range: 94.86 - 121.36 (now 9.7% of the way up)
Volatility: ATR(14) 2.13 (2.2% of price) | annualised 20d 23.4%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 19.52 | P/B 2.34 | P/S 1.36 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +9.5% a year | beta to the market 1.46
Cost and size: expense ratio 0.35% | net assets 1.33B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Installed Building Products Inc 4.4%, Owens-Corning Inc 4.3%, Allegion PLC 4.3%, Champion Homes Inc 4.1%, Williams-Sonoma Inc 3.9%
Sector mix: Consumer cyclical 60.7%, Industrials 37.9%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.9% | hold 21.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.2% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-25 Evercore ISI Group: main, In-Line -> In-Line
  - OC: 2026-09-11 Wells Fargo: main, Overweight -> Overweight
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-08-06 UBS: main, Buy -> Buy
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.3% (-4.10M) over 7d
Shares outstanding: 13.72M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, technicals show a pull‑back but no decisive break, and analyst view is bullish but limited to 37% of the fund.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over past week
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 35.7; MACD negative
- Analyst consensus 100% buy on top holdings (37% weight) with +14.8% price target
- Macro unchanged: yields up modestly, upward‑sloping curve, inflation 3.4%

<details><summary><b>News</b> — score +0.00</summary>

- [These five materials stocks posted the biggest one-month gains in September (XLB:NYSEARCA)](https://seekingalpha.com/news/4647561-these-five-materials-stocks-posted-the-biggest-one-month-gains-in-september)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Top materials stocks for September 2026: MTRN leads 1-month gains, plus HWKN, CE, CLF, NGVT and key ETFs (XLB, VAW).
- [Stocktwits Retail Therapy: Defensive Bets Take Off As COST, DG, WMT Lead Weekly Consumer Staples Gains](https://es.tradingview.com/news/stocktwits:b5f68bdaf094b:0-stocktwits-retail-therapy-defensive-bets-take-off-as-cost-dg-wmt-lead-weekly-consumer-staples-gains/)  
  <sub>TradingView, 11 hours ago</sub>  
  U.S. consumer stocks ended mixed last week as sticky inflation and higher bond yields kept investors cautious. The Consumer Staples Select Sector SPDR Fund...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 49.44 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 50.98 (-3.0%), 50d 51.68 (-4.3%), 200d 50.58 (-2.2%); 50d above 200d
Momentum: RSI(14) 35.7 | MACD -0.672 vs signal -0.528 (histogram -0.144)
Returns: 1d -0.7% | 5d -0.5% | 1m -7.1% | 3m -2.4%
52-week range: 42.23 - 53.67 (now 63.0% of the way up)
Volatility: ATR(14) 0.75 (1.5% of price) | annualised 20d 14.6%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Natural Resources
What it holds: P/E 24.59 | P/B 3.00 | P/S 2.01 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +10.1% a year | beta to the market 0.82
Cost and size: expense ratio 0.08% | net assets 8.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Linde PLC 13.1%, Newmont Corp 7.8%, Freeport-McMoRan Inc 6.3%, Corteva Inc 4.9%, Air Products and Chemicals Inc 4.8%
Sector mix: Basic materials 84.5%, Consumer cyclical 15.5%
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
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.8% above the current prices
Holdings read: LIN, NEM, FCX, CTVA, APD
Recent rating changes among them:
  - LIN: 2026-09-28 Argus Research: main, Buy -> Buy
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - FCX: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - CTVA: 2026-09-18 Argus Research: reit, Buy -> Buy
  - APD: 2026-09-11 Keybanc: init, ? -> Sector Weight
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
Shares outstanding: 71.92M | fund size: 3.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, technicals lack decisive breakout, and flows are flat despite bullish analyst view

**Main reasons it gave:**
- 10‑yr Treasury yield up 0.27% week, Fed target unchanged
- RSI 46.9, price below 20‑day SMA, MACD histogram -0.132, low volume
- Fund share count +0.4% week, flat flows
- Analyst coverage 45.5% of fund, 100% buy, price target +17% above current

<details><summary><b>News</b> — score +0.00</summary>

- [Advanced AI-Powered Crypto Investment Research Platform](https://sosovalue.com/stocks/t)  
  <sub>SoSoValue, 6 hours ago</sub>  
  Live Crypto Prices, Bitcoin/ETH ETFs Data, On-Chain Data Dashboard, Bitcoin Spot ETF Trends, and Up-to-the-Second Cryptocurrency News.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 111.33 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 112.55 (-1.1%), 50d 111.34 (-0.0%), 200d 113.91 (-2.3%); 50d below 200d
Momentum: RSI(14) 46.9 | MACD 0.328 vs signal 0.461 (histogram -0.132)
Returns: 1d -1.4% | 5d -3.0% | 1m -0.1% | 3m +3.2%
52-week range: 105.38 - 120.08 (now 40.5% of the way up)
Volatility: ATR(14) 1.82 (1.6% of price) | annualised 20d 21.8%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Communications
What it holds: P/E 15.38 | P/B 2.92 | P/S 2.06 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +21.1% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.43B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 16.8%, Alphabet Inc Class A 10.3%, Alphabet Inc Class C 8.2%, AT&T Inc 5.3%, Verizon Communications Inc 5.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.1% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
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
Share count change: 1 week: +0.4% (89.45M) over 7d
Shares outstanding: 199.34M | fund size: 22.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; mixed macro, analyst, inventory, and price outlook signals with no decisive technical breakout.

**Main reasons it gave:**
- Iranian geopolitical shock drove Brent crude up 13% and XLE up 4% (macro news)
- Analyst coverage of top holdings is 100% buy with +5.8% price target (analyst view)
- Energy inventories show gasoline and diesel draws (bullish) and a small crude build (bearish) (inventory data)
- EIA forecast predicts WTI crude price falling ~10% over six months (price outlook)
- Technicals: price below 20‑day SMA, weak momentum, negative MACD, low volume (technical)

<details><summary><b>News</b> — score +0.00</summary>

- [These 10 energy stocks posted the biggest one-month gains as September ends (XLE:NYSEARCA)](https://seekingalpha.com/news/4647494-these-10-energy-stocks-posted-the-biggest-one-month-gains-as-september-ends)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Top energy stocks for September 2026: see the 10 best 1-month performers, key sector trends, and Strong Buy Quant Ratings—review the list now.
- [INDO, USO, XLE, BATL In Focus As Iran Shock Hits Oil — Why Analysts Think Market May Look Past Doomsday Calls](https://stocktwits.com/news-articles/markets/equity/iran-oil-shock-indo-uso-xle-batl-analysts-market-outlook/cZddtF9RIch)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Energy stocks rallied overnight after the U.S.-Israeli strikes on Iran killed Supreme Leader Khamenei, sending Brent crude up 13%. USO and XLE rose 4%,...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Monday as Oil Prices Rise](https://finance.yahoo.com/markets/articles/exchange-traded-funds-equity-futures-131704585.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Diesel export ban carries hidden costs for U.S. fuel market (USO:NYSEARCA)](https://seekingalpha.com/news/4647543-diesel-export-ban-carries-hidden-costs-for-us-fuel-market)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. diesel export ban debate: SocGen warns a ban may briefly cut prices but later raise pump costs via refinery run cuts and global impacts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 62.38 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 63.98 (-2.5%), 50d 61.85 (+0.9%), 200d 56.23 (+10.9%); 50d above 200d
Momentum: RSI(14) 46.6 | MACD 0.073 vs signal 0.536 (histogram -0.463)
Returns: 1d +0.5% | 5d -0.1% | 1m +0.1% | 3m +16.4%
52-week range: 42.61 - 65.93 (now 84.8% of the way up)
Volatility: ATR(14) 1.23 (2.0% of price) | annualised 20d 21.8%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.74 | P/B 2.58 | P/S 1.68 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +14.7% a year | beta to the market -0.07
Cost and size: expense ratio 0.08% | net assets 41.44B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 19.9%, Chevron Corp 14.9%, ConocoPhillips 6.2%, Marathon Petroleum Corp 5.4%, Phillips 66 5.3%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.20</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.8% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-28 TD Cowen: main, Buy -> Buy
  - CVX: 2026-09-28 TD Cowen: main, Hold -> Hold
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-09-22 Jefferies: down, Buy -> Hold
  - PSX: 2026-09-17 BMO Capital: main, Outperform -> Outperform
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
Shares outstanding: 186.42M | fund size: 11.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals lack decisive break, and flows are flat despite bullish analyst consensus.

**Main reasons it gave:**
- Treasury yields rose 10-27 bps across the curve this week without a policy surprise
- RSI 29.9 indicates oversold conditions but price remains below 20‑day SMA and MACD stays negative
- Analyst consensus 100% buy with +13.1% price target, but no macro catalyst
- Fund flows flat (0% share count change) over the past week

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Monday as Oil Prices Rise](https://finance.yahoo.com/markets/articles/exchange-traded-funds-equity-futures-131704585.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Globe Life Stock: Is GL Outperforming the Financial Service Sector?](https://www.barchart.com/story/news/4832071/globe-life-stock-is-gl-outperforming-the-financial-service-sector)  
  <sub>Barchart.com, 2 hours ago</sub>  
  While Globe Life has outperformed relative to the financial service sector over the past year, Wall Street analysts maintain a cautiously optimistic outlook...
- [Dow Jones Futures Fall As Oil Prices, Yields Rise After Trump Iran Comments; Micron, SpaceX, Tesla Eye Buy Points](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-trump-iran-comments-micron-spacex-tesla-economic-data/)  
  <sub>Investor's Business Daily, 5 hours ago</sub>  
  Dow Jones futures fell Monday morning, along with S&P 500 futures and Nasdaq futures. Crude oil futures and Treasury yields rose. President Donald Trump...
- [Jabil Earnings Preview: What to Expect](https://finance.yahoo.com/markets/stocks/articles/jabil-earnings-preview-expect-072149748.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Jabil Inc. (JBL) is a global manufacturing solutions provider offering engineering, supply chain and manufacturing services based in Saint Petersburg,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 54.39 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 56.41 (-3.6%), 50d 57.01 (-4.6%), 200d 53.73 (+1.2%); 50d above 200d
Momentum: RSI(14) 29.9 | MACD -0.739 vs signal -0.470 (histogram -0.269)
Returns: 1d -0.8% | 5d -2.7% | 1m -6.0% | 3m +1.2%
52-week range: 47.81 - 58.56 (now 61.2% of the way up)
Volatility: ATR(14) 0.70 (1.3% of price) | annualised 20d 13.3%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Financial
What it holds: P/E 16.36 | P/B 2.42 | P/S 3.50 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +19.4% a year | beta to the market 0.71
Cost and size: expense ratio 0.08% | net assets 54.59B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: JPMorgan Chase & Co 11.7%, Berkshire Hathaway Inc Class B 11.3%, Visa Inc Class A 7.7%, Mastercard Inc Class A 5.8%, Bank of America Corp 5.0%
Sector mix: Financial services 98.1%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.1% above the current prices
Holdings read: JPM, BRK-B, V, MA, BAC
Recent rating changes among them:
  - JPM: 2026-09-28 HSBC: main, Hold -> Hold
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - V: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - MA: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - BAC: 2026-08-03 UBS: main, Buy -> Buy
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
Shares outstanding: 883.44M | fund size: 48.05B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view is strongly positive but limited to 25.8% of the fund; technicals show price below key moving averages with low volume, indicating weak bullish momentum; macro environment shows rising yields and low VIX without surprise data; fund flows are flat, indicating no net demand; fundamentals show high valuation multiples and low yield, providing limited upside.

**Main reasons it gave:**
- Analyst view: all buy with +23.8% price target but only 25.8% of fund coverage
- Technical: price below 20‑day, 50‑day, 200‑day SMAs and volume at 0.25× 20‑day average
- Macro: yields up (10‑yr 5.23% +0.27) and VIX low (15.86) with no surprise data
- Fund flows flat: share count unchanged (+0.0% week)
- Fundamentals: high valuation (P/E 28.43, P/B 6.75) and low yield (1.2%)

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Monday as Oil Prices Rise](https://finance.yahoo.com/markets/articles/exchange-traded-funds-equity-futures-131704585.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Industrial stock winners: Vicor, Bloom Energy lead September’s top ten (XLI:NYSEARCA)](https://seekingalpha.com/news/4647608-industrial-stock-winners-vicor-bloom-energy-lead-septembers-top-ten)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Discover September 2026's top 10 industrials stocks by 1-month gains—VICR, BE, PRLB and more—plus key sector ETFs.
- [Why Is Rocket Lab Stock Falling Today?](https://www.benzinga.com/trading-ideas/movers/26/09/62021213/why-is-rocket-lab-stock-falling-today)  
  <sub>Benzinga, 1 hour ago</sub>  
  Rocket Lab Stock slips premarket as investors weigh Iridium funding, recent catalysts and broader pressure on growth stocks.
- [The Nasdaq Nears a Major Breakout: 5 Tech ETFs to Play the Move](https://www.marketbeat.com/articles/the-nasdaq-nears-a-major-breakout-5-tech-etfs-to-play-the-move/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  As the Nasdaq-100 nears its all-time high, QQQ, XLK, SMH, QQQI, and SOXX offer distinct ways to gain tech and semiconductor exposure, from low-cost to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 168.91 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 171.22 (-1.3%), 50d 177.70 (-4.9%), 200d 172.11 (-1.9%); 50d above 200d
Momentum: RSI(14) 36.1 | MACD -2.494 vs signal -2.694 (histogram 0.200)
Returns: 1d -0.9% | 5d -0.6% | 1m -5.5% | 3m -7.6%
52-week range: 147.83 - 186.51 (now 54.5% of the way up)
Volatility: ATR(14) 2.27 (1.3% of price) | annualised 20d 12.8%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 28.43 | P/B 6.75 | P/S 3.00 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +20.2% a year | beta to the market 1.02
Cost and size: expense ratio 0.08% | net assets 31.95B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Caterpillar Inc 6.7%, GE Aerospace 6.4%, RTX Corp 5.1%, GE Vernova Inc 4.4%, Union Pacific Corp 3.2%
Sector mix: Industrials 92.8%, Technology 6.7%, Basic materials 0.3%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.8% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-23 Jefferies: main, Buy -> Buy
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - GEV: 2026-09-15 Bernstein: reit, Outperform -> Outperform
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
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
Shares outstanding: 136.63M | fund size: 23.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, valuation reset appears largely complete, technicals lack decisive break, analyst view bullish but not a macro catalyst.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.10 to +0.27) with no surprise rate change
- Inflation at 3.4% and unemployment at 4.1% are in line with expectations, no data surprise
- Magnificent Seven valuation reset appears largely complete, limiting upside for XLK's top holdings
- Technical indicators show XLK above 20‑day, 50‑day and 200‑day SMAs but with low volume (0.30× avg) and no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Mag-7 valuation reset may be largely complete, J.P. Morgan says (XLK:NYSEARCA)](https://seekingalpha.com/news/4647638-mag-7-valuation-reset-may-be-largely-complete-jp-morgan-says)  
  <sub>Seeking Alpha, 7 minutes ago</sub>  
  The Magnificent Seven have undergone a significant valuation reset, with their 12-month forward price-to-earnings multiple relative to the broader market...
- [The Nasdaq Nears a Major Breakout: 5 Tech ETFs to Play the Move](https://www.marketbeat.com/articles/the-nasdaq-nears-a-major-breakout-5-tech-etfs-to-play-the-move/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  As the Nasdaq-100 nears its all-time high, QQQ, XLK, SMH, QQQI, and SOXX offer distinct ways to gain tech and semiconductor exposure, from low-cost to...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Monday as Oil Prices Rise](https://finance.yahoo.com/markets/articles/exchange-traded-funds-equity-futures-131704585.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Watch CNBC's full interview with Jeffrey Cole](https://www.cnbc.com/video/2026/09/28/watch-cnbcs-full-interview-with-jeffrey-cole.html)  
  <sub>CNBC, 4 hours ago</sub>  
  Jeffrey Cole, director of the Center for the Digital Future at USC and author of 'Disrupters at the Gate,' joins 'Squawk Box' to discuss his new book,...
- [Watch CNBC’s full interview with Yardeni Research’s Ed Yardeni](https://www.cnbc.com/video/2026/09/28/watch-cnbcs-full-interview-with-yardeni-researchs-ed-yardeni.html)  
  <sub>CNBC, 4 hours ago</sub>  
  Ed Yardeni, president of Yardeni Research, joins 'Squawk Box 'to discuss the latest market trends, his outlook, and more.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 192.98 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 188.78 (+2.2%), 50d 184.82 (+4.4%), 200d 163.91 (+17.7%); 50d above 200d
Momentum: RSI(14) 57.8 | MACD 2.786 vs signal 2.072 (histogram 0.714)
Returns: 1d -1.7% | 5d -1.0% | 1m +2.3% | 3m +4.1%
52-week range: 127.50 - 198.21 (now 92.6% of the way up)
Volatility: ATR(14) 3.31 (1.7% of price) | annualised 20d 19.5%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 33.01 | P/B 11.41 | P/S 8.77 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +34.3% a year | beta to the market 1.50
Cost and size: expense ratio 0.08% | net assets 121.44B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 14.4%, Apple Inc 12.5%, Microsoft Corp 10.1%, Broadcom Inc 4.7%, Micron Technology Inc 4.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.73</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.73</summary>

```text
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.3% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - AAPL: 2026-09-23 B of A Securities: reit, Buy -> Buy
  - MSFT: 2026-09-23 Stifel: up, Hold -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-28 Wedbush: reit, Outperform -> Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Analyst view: 100% buy rating on top holdings, weighted price target +11.6%
- Fund flows: flat share count (+0.0% change) indicating no net demand shift
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 42.1, MACD negative
- Macro: yields rose across curve, inflation 3.4% and unemployment 4.1% in line with expectations, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Monday as Oil Prices Rise](https://finance.yahoo.com/markets/articles/exchange-traded-funds-equity-futures-131704585.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Stocktwits Retail Therapy: Defensive Bets Take Off As COST, DG, WMT Lead Weekly Consumer Staples Gains](https://es.tradingview.com/news/stocktwits:b5f68bdaf094b:0-stocktwits-retail-therapy-defensive-bets-take-off-as-cost-dg-wmt-lead-weekly-consumer-staples-gains/)  
  <sub>TradingView, 11 hours ago</sub>  
  U.S. consumer stocks ended mixed last week as sticky inflation and higher bond yields kept investors cautious. The Consumer Staples Select Sector SPDR Fund...
- [Consumer Sentiment Drops in September: ETFs to Consider](https://www.zacks.com/stock/news/2996808/consumer-sentiment-drops-in-september-etfs-to-consider?cid=CS-YAHOO-FT-etf_news_and_commentary-2996808)  
  <sub>Zacks Investment Research, 6 minutes ago</sub>  
  Consumer sentiment falls to a four-month low amid persistent inflation and uncertainty. Here are some ETFs that investors may consider.
- [Biotech Week Ahead: XLV Beats The Market — Here Are The Stocks, Readouts And Events To Watch Next](https://stocktwits.com/news-articles/markets/equity/biotech-week-ahead-xlv-beats-market-stocks-readouts-events-watch/cZMRPApRB4O)  
  <sub>Stocktwits, 19 hours ago</sub>  
  The Health Care Select Sector SPDR Fund (XLV) gained 1.8% last week, outperforming the broader market and biotech ETFs. Sellas Life Sciences (SLS) will...
- [Stocktwits Pharma Pulse: Lilly, Novo Lead A Busy Week — Here Are The Stocks And Readouts To Watch](https://www.tradingview.com/news/stocktwits:21d8d44a9094b:0-stocktwits-pharma-pulse-lilly-novo-lead-a-busy-week-here-are-the-stocks-and-readouts-to-watch/)  
  <sub>TradingView, 11 hours ago</sub>  
  Biotech investors face a crowded final week of September as Eli Lilly (LLY) and Novo Nordisk (NVO) bring their latest obesity and diabetes research to a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 82.45 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 83.51 (-1.3%), 50d 84.65 (-2.6%), 200d 83.69 (-1.5%); 50d above 200d
Momentum: RSI(14) 42.1 | MACD -0.786 vs signal -0.661 (histogram -0.125)
Returns: 1d +0.5% | 5d +0.6% | 1m -3.1% | 3m -2.3%
52-week range: 75.60 - 90.01 (now 47.5% of the way up)
Volatility: ATR(14) 0.98 (1.2% of price) | annualised 20d 11.0%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 25.14 | P/B 4.58 | P/S 1.36 | 3y earnings growth n/a
Yield: 2.6%
Three-year record: +8.4% a year | beta to the market 0.49
Cost and size: expense ratio 0.08% | net assets 14.52B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 9.8%, Costco Wholesale Corp 8.9%, Coca-Cola Co 7.3%, Procter & Gamble Co 7.2%, Philip Morris International Inc 6.2%
Sector mix: Consumer defensive 98.2%, Consumer cyclical 1.8%
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
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.6% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-10 DA Davidson: main, Buy -> Buy
  - COST: 2026-09-28 Argus Research: reit, Buy -> Buy
  - KO: 2026-07-30 Argus Research: main, Buy -> Buy
  - PG: 2026-08-07 Argus Research: down, Buy -> Hold
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
Shares outstanding: 210.17M | fund size: 17.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no clear macro surprise or decisive technical break is present; bullish analyst view is offset by downtrend technicals, higher rates pressure utilities, and flat fund flows.

**Main reasons it gave:**
- Technical downtrend: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 22.8; low volume, no decisive break
- Macro: Treasury yields rising (10‑yr +0.27% week) and higher rates pressure utilities
- Analyst view bullish (80.9% buy, weighted price target +26.4% above current) but not enough to outweigh macro and technicals
- Fund flows flat, indicating no net demand for the ETF

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 39.26 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 41.56 (-5.5%), 50d 43.15 (-9.0%), 200d 44.45 (-11.7%); 50d below 200d
Momentum: RSI(14) 22.8 | MACD -1.064 vs signal -0.840 (histogram -0.223)
Returns: 1d -0.6% | 5d -3.5% | 1m -9.1% | 3m -14.7%
52-week range: 39.26 - 47.73 (now 0.0% of the way up)
Volatility: ATR(14) 0.59 (1.5% of price) | annualised 20d 14.1%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +11.0% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
Sector mix: Utilities 100.0%
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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.4% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - SO: 2026-09-25 Citigroup: main, Buy -> Buy
  - DUK: 2026-09-18 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - CEG: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - AEP: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
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
Shares outstanding: 163.27M | fund size: 6.41B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, modest technical bullishness with low volume, and analyst coverage positive but limited to 44% of the fund; fundamentals are solid but valuation is high, leading to a neutral overall stance.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (44.3% weight) all buy with +9.3% price target
- Fund flows flat (0% change) over the past week
- Technicals show price above 20‑day, 50‑day, 200‑day SMAs and positive MACD, but volume is low (0.27× 20‑day average)
- Macro: Treasury yields rose modestly, upward‑sloping curve, VIX low, no surprise data releases
- Fund fundamentals: high P/E (30.5) and P/B (4.8) suggest valuation caution despite 11.1% annualized 3‑year return

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Pharma Pulse: Lilly, Novo Lead A Busy Week — Here Are The Stocks And Readouts To Watch](https://www.tradingview.com/news/stocktwits:21d8d44a9094b:0-stocktwits-pharma-pulse-lilly-novo-lead-a-busy-week-here-are-the-stocks-and-readouts-to-watch/)  
  <sub>TradingView, 11 hours ago</sub>  
  Biotech investors face a crowded final week of September as Eli Lilly (LLY) and Novo Nordisk (NVO) bring their latest obesity and diabetes research to a...
- [Biotech Week Ahead: XLV Beats The Market — Here Are The Stocks, Readouts And Events To Watch Next](https://stocktwits.com/news-articles/markets/equity/biotech-week-ahead-xlv-beats-market-stocks-readouts-events-watch/cZMRPApRB4O)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The Health Care Select Sector SPDR Fund (XLV) gained 1.8% last week, outperforming the broader market and biotech ETFs. Sellas Life Sciences (SLS) will...
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Monday as Oil Prices Rise](https://finance.yahoo.com/markets/articles/exchange-traded-funds-equity-futures-131704585.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Consumer Sentiment Drops in September: ETFs to Consider](https://www.zacks.com/stock/news/2996808/consumer-sentiment-drops-in-september-etfs-to-consider?cid=CS-YAHOO-FT-etf_news_and_commentary-2996808)  
  <sub>Zacks Investment Research, 2 minutes ago</sub>  
  Consumer sentiment falls to a four-month low amid persistent inflation and uncertainty. Here are some ETFs that investors may consider.
- [MRNA Stock Eyes Best Year Ever: Analyst Calls China’s AI Drug Lead ‘Baseless’ As Moderna Awaits Cancer Data](https://www.tradingview.com/news/stocktwits:c6eebca20094b:0-mrna-stock-eyes-best-year-ever-analyst-calls-china-s-ai-drug-lead-baseless-as-moderna-awaits-cancer-data/)  
  <sub>TradingView, 7 hours ago</sub>  
  Shares of Moderna (MRNA) are on track for their best year on record as investors await detailed melanoma trial results, while an analyst said that China...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 170.97 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 169.21 (+1.0%), 50d 167.90 (+1.8%), 200d 156.43 (+9.3%); 50d above 200d
Momentum: RSI(14) 57.2 | MACD 0.444 vs signal 0.336 (histogram 0.109)
Returns: 1d +0.2% | 5d +1.2% | 1m -0.4% | 3m +6.4%
52-week range: 135.50 - 175.68 (now 88.3% of the way up)
Volatility: ATR(14) 2.35 (1.4% of price) | annualised 20d 13.2%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Health
What it holds: P/E 30.47 | P/B 4.77 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +11.1% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.91B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Eli Lilly and Co 14.9%, Johnson & Johnson 10.4%, AbbVie Inc 7.4%, Merck & Co Inc 5.9%, UnitedHealth Group Inc 5.7%
Sector mix: Healthcare 100.0%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.3% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-22 TD Cowen: reit, Buy -> Buy
  - JNJ: 2026-09-10 HSBC: main, Buy -> Buy
  - ABBV: 2026-09-10 HSBC: main, Buy -> Buy
  - MRK: 2026-09-10 HSBC: main, Buy -> Buy
  - UNH: 2026-07-21 JP Morgan: main, Overweight -> Overweight
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
Shares outstanding: 197.42M | fund size: 33.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.
- [iShares MSCI Singapore ETF (EWS) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/EWS/)  
  <sub>Yahoo Finance Singapore, 4 hours ago</sub>  
  Find the latest iShares MSCI Singapore ETF (EWS) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 112.58 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 111.04 (+1.4%), 50d 105.59 (+6.6%), 200d 87.76 (+28.3%); 50d above 200d
Momentum: RSI(14) 56.2 | MACD 2.100 vs signal 2.026 (histogram 0.074)
Returns: 1d -1.9% | 5d -2.6% | 1m +3.6% | 3m +6.4%
52-week range: 60.03 - 115.64 (now 94.5% of the way up)
Volatility: ATR(14) 2.29 (2.0% of price) | annualised 20d 28.0%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.26 | P/B 4.29 | P/S 2.54 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +46.0% a year | beta to the market 1.30
Cost and size: expense ratio 0.59% | net assets 11.76B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.1%, MediaTek Inc 6.0%, Delta Electronics Inc 4.0%, Hon Hai Precision Industry Co Ltd 3.3%, ASE Technology Holding Co Ltd 2.6%
Sector mix: Technology 73.9%, Financial services 14.0%, Basic materials 3.8%, Industrials 2.8%
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
Rolled up from the 5 largest holdings, 38.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.0% above the current prices
Holdings read: 2330.TW, 2454.TW, 2308.TW, 2317.TW, 3711.TW
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
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 85.00M | fund size: 9.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Should You Invest in the State Street SPDR S&P Capital Markets ETF (KCE)?](https://finance.yahoo.com/markets/stocks/articles/invest-state-street-spdr-p-092002747.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Designed to provide broad exposure to the Financials - Brokers/ Capital markets segment of the equity market, the State Street SPDR S&P Capital Markets ETF...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 70.82 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 72.96 (-2.9%), 50d 74.80 (-5.3%), 200d 70.54 (+0.4%); 50d above 200d
Momentum: RSI(14) 34.3 | MACD -1.078 vs signal -0.869 (histogram -0.209)
Returns: 1d -1.0% | 5d -1.6% | 1m -4.7% | 3m -5.3%
52-week range: 58.14 - 77.93 (now 64.1% of the way up)
Volatility: ATR(14) 1.16 (1.6% of price) | annualised 20d 16.3%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Financial
What it holds: P/E 12.60 | P/B 1.27 | P/S 3.77 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +22.9% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Cullen/Frost Bankers Inc 1.5%, SouthState Bank Corp 1.4%, Popular Inc 1.4%, Pinnacle Financial Partners Inc 1.4%, UMB Financial Corp 1.4%
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
Rolled up from the 5 largest holdings, 7.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 79.5% | hold 20.5% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.9% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-09-22 Citigroup: main, Buy -> Buy
  - PNFP: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - UMBF: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
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
Share count change: 1 week: +3.4% (133.68M) over 7d
Shares outstanding: 57.00M | fund size: 4.04B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — no answer, no confidence given

**This one did not finish:** invalid LLM output: 1 validation error for LLMSignal
conviction
  Input should be greater than or equal to 0 [type=greater_than_equal, input_value=-0.35, input_type=float]
    For further information visit https://errors.pydantic.dev/2.9/v/greater_than_equal

<details><summary><b>News</b> — score n/a</summary>

- [Stocktwits Pharma Pulse: Lilly, Novo Lead A Busy Week — Here Are The Stocks And Readouts To Watch](https://es.tradingview.com/news/stocktwits:21d8d44a9094b:0-stocktwits-pharma-pulse-lilly-novo-lead-a-busy-week-here-are-the-stocks-and-readouts-to-watch/)  
  <sub>TradingView, 11 hours ago</sub>  
  Biotech investors face a crowded final week of September as Eli Lilly (LLY) and Novo Nordisk (NVO) bring their latest obesity and diabetes research to a...
- [MRNA Stock Eyes Best Year Ever: Analyst Calls China’s AI Drug Lead ‘Baseless’ As Moderna Awaits Cancer Data](https://finance.yahoo.com/healthcare/articles/mrna-stock-eyes-best-ever-075902416.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Laidlaw analyst Yale Jen flagged possible data in other cancers from 2027, while warning that personalized manufacturing costs, capacity and reimbursement...
- [Biotech Week Ahead: XLV Beats The Market — Here Are The Stocks, Readouts And Events To Watch Next](https://stocktwits.com/news-articles/markets/equity/biotech-week-ahead-xlv-beats-market-stocks-readouts-events-watch/cZMRPApRB4O)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The Health Care Select Sector SPDR Fund (XLV) gained 1.8% last week, outperforming the broader market and biotech ETFs. Sellas Life Sciences (SLS) will...
- [Stocktwits Retail Therapy: Defensive Bets Take Off As COST, DG, WMT Lead Weekly Consumer Staples Gains](https://stocktwits.com/news-articles/markets/equity/stocktwits-retail-therapy-defensive-bets-take-off-as-cost-dg-wmt-lead-weekly-consumer-staples-gains/cZMSipvRBfk)  
  <sub>Stocktwits, 7 hours ago</sub>  
  U.S. consumer stocks ended mixed last week as sticky inflation and higher bond yields kept investors cautious. The Consumer Staples Select Sector SPDR Fund...
- [Nasdaq, S&P 500 Futures Fall As Oil Spikes On Trump’s Snub To Iran: MU, NVDA, SKHY, SPCX, NIO Stocks In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-sp500-futures-fall-as-oil-spikes-on-trump-snub-to-iran-mu-nvda-skhy-spcx-nio-stocks-in-focus/cZMSFEIRBQR)  
  <sub>Stocktwits, 6 hours ago</sub>  
  U.S. stock futures were under pressure early Monday as rising geopolitical tensions in the Middle East and a sharp spike in energy prices weighed on market...
- [Why Did AMD, HPE, MRNA Stocks Surge To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/why-did-amd-hpe-mrna-stocks-surge-to-52-week-highs-last-week/cZMS1RURBfm)  
  <sub>Stocktwits, 23 hours ago</sub>  
  Advanced Micro Devices (AMD), Hewlett Packard Enterprise (HPE) and Moderna (MRNA) surged to fresh 52-week highs Friday as investors piled into AI...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 154.81 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 158.79 (-2.5%), 50d 157.74 (-1.9%), 200d 138.16 (+12.1%); 50d above 200d
Momentum: RSI(14) 43.9 | MACD -1.087 vs signal -0.514 (histogram -0.573)
Returns: 1d -0.1% | 5d -2.2% | 1m -8.0% | 3m -2.2%
52-week range: 97.95 - 169.55 (now 79.4% of the way up)
Volatility: ATR(14) 4.04 (2.6% of price) | annualised 20d 24.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.20 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +29.5% a year | beta to the market 1.12
Cost and size: expense ratio 0.35% | net assets 11.40B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.8%, Twist Bioscience Corp 1.9%, Apogee Therapeutics Inc 1.5%, Kymera Therapeutics Inc Ordinary Shares 1.4%, Halozyme Therapeutics Inc 1.4%
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
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 43.2% | hold 56.8% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -18.1% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - TWST: 2026-09-18 BWS Financial: main, Sell -> Sell
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-22 Stifel: main, Buy -> Buy
  - HALO: 2026-09-02 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: -1.0% (-116.83M) over 7d
Shares outstanding: 73.23M | fund size: 11.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [These ten consumer discretionary stocks outperformed in September, GameStop leads (XLY:NYSEARCA)](https://seekingalpha.com/news/4647613-these-ten-consumer-discretionary-stocks-outperformed-in-september-gamestop-leads)  
  <sub>Seeking Alpha, 60 minutes ago</sub>  
  Top consumer discretionary stock winners for September 2026: GME, ANF, SONO, TSLA & more with 1-month returns, ratings and ETF ideas—read now.
- [Consumer Discretionary Is On Sale. Is Anyone Buying?](https://www.thedailyupside.com/etf/thematics-sectors/consumer-discretionary-is-on-sale-is-anyone-buying/)  
  <sub>The Daily Upside, 11 hours ago</sub>  
  The market's worst-performing sector is down 6% this year. Do recent inflows suggest a turnaround or just a trade?
- [Exchange-Traded Funds, Equity Futures Lower Pre-Bell Monday as Oil Prices Rise](https://finance.yahoo.com/markets/articles/exchange-traded-funds-equity-futures-131704585.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.3% and the actively tr.
- [Stocktwits Retail Therapy: Defensive Bets Take Off As COST, DG, WMT Lead Weekly Consumer Staples Gains](https://www.tradingview.com/news/stocktwits:b5f68bdaf094b:0-stocktwits-retail-therapy-defensive-bets-take-off-as-cost-dg-wmt-lead-weekly-consumer-staples-gains/)  
  <sub>TradingView, 11 hours ago</sub>  
  U.S. consumer stocks ended mixed last week as sticky inflation and higher bond yields kept investors cautious. The Consumer Staples Select Sector SPDR Fund...
- [Forget Inflation: Funflation Is Here and These ETFs Are Riding on It](https://ca.finance.yahoo.com/news/forget-inflation-funflation-etfs-riding-125400975.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  ETFs like AWAY are riding on "funflation" as consumers keep spending on hobbies, travel, music and leisure despite higher prices.
- [Halloween spending is expected to rise 3% amid affordability concerns (XRT:NYSEARCA)](https://seekingalpha.com/news/4647499-halloween-spending-is-expected-to-rise-3-amid-affordability-concerns)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  NRF forecasts 2026 Halloween spending to hit $13.5B, led by candy, costumes & decor.
- [NIKE’s Q1 2027 Earnings: What to Expect](https://www.inkl.com/news/nikes-q1-2027-earnings-what-to-expect)  
  <sub>inkl, 7 hours ago</sub>  
  NIKE is set to report its Q1 earnings soon, with analysts expecting a double-digit year-over-year decline in EPS.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 109.26 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 112.52 (-2.9%), 50d 114.70 (-4.7%), 200d 116.61 (-6.3%); 50d below 200d
Momentum: RSI(14) 34.9 | MACD -1.541 vs signal -1.353 (histogram -0.188)
Returns: 1d -1.2% | 5d -2.6% | 1m -5.7% | 3m -6.7%
52-week range: 105.66 - 124.52 (now 19.1% of the way up)
Volatility: ATR(14) 1.58 (1.4% of price) | annualised 20d 15.3%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 25.48 | P/B 5.89 | P/S 2.51 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +11.9% a year | beta to the market 1.16
Cost and size: expense ratio 0.08% | net assets 22.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 24.4%, Tesla Inc 17.3%, The Home Depot Inc 5.4%, McDonald's Corp 4.1%, Booking Holdings Inc 3.9%
Sector mix: Consumer cyclical 98.8%, Technology 1.2%
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
Rolled up from the 5 largest holdings, 55.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.2% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-03 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-09-28 JP Morgan: main, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-28 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - BKNG: 2026-09-24 BTIG: reit, Buy -> Buy
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
Shares outstanding: 120.25M | fund size: 13.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Treasury yields rose modestly and inflation 3.4% near target, no policy surprise
- CFTC positioning shows net long 18.9% of OI, crowding at 100% percentile, but only +0.4% weekly change
- Cost of holding is -9.5% annual, heavy roll cost, a bearish drag on fund performance
- Technicals: price 1.3% below 20‑day SMA, RSI 51.7, MACD histogram negative, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.23 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 11.38 (-1.3%), 50d 10.81 (+3.9%), 200d 9.95 (+13.0%); 50d above 200d
Momentum: RSI(14) 51.7 | MACD 0.079 vs signal 0.142 (histogram -0.063)
Returns: 1d +0.2% | 5d +0.9% | 1m -2.0% | 3m +14.8%
52-week range: 9.02 - 11.82 (now 79.1% of the way up)
Volatility: ATR(14) 0.19 (1.7% of price) | annualised 20d 21.7%
Volume: 0.29x the 20-day average
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
Cost of holding this fund instead of sugar itself: -9.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +14.8%, commodity +29.7%, gap -15.0% | 6 months: fund +5.8%, commodity +17.6%, gap -11.8% | 12 months: fund +8.1%, commodity +17.6%, gap -9.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 18.9% of open interest (1,147,767 contracts)
Change on the week: +0.4% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.2% (98.74K) over 7d
Shares outstanding: 5.12M | fund size: 57.56M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no clear macro catalyst or decisive technical break is present; mixed signals from heavy cost of holding, crowded long positioning, fund inflows, and short‑term technical weakness.

**Main reasons it gave:**
- Heavy cost of holding -12.3% per year (tailwind for short)
- Crowded long position: net long 21.8% of OI, -0.7% change, 95th percentile
- Fund share count up 0.9% (inflow) indicating demand
- Price below 20‑day SMA and negative MACD (short‑term bearish technical)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 19.42 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 19.95 (-2.6%), 50d 18.98 (+2.3%), 200d 18.11 (+7.3%); 50d above 200d
Momentum: RSI(14) 46.5 | MACD 0.177 vs signal 0.305 (histogram -0.128)
Returns: 1d -1.5% | 5d -4.2% | 1m -1.9% | 3m +17.9%
52-week range: 16.47 - 20.29 (now 77.4% of the way up)
Volatility: ATR(14) 0.31 (1.6% of price) | annualised 20d 15.9%
Volume: 0.22x the 20-day average
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
Cost of holding this fund instead of corn itself: -12.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +17.9%, commodity +29.1%, gap -11.2% | 6 months: fund +4.5%, commodity +12.3%, gap -7.8% | 12 months: fund +9.6%, commodity +21.9%, gap -12.3%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.50</summary>

```text
Corn rated good or excellent: 57% of the US crop (week 38 of 2026)
Direction over 3 weeks: steady, +1 points
Same week last year: 66% (-9 points)
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 21.8% of open interest (1,854,505 contracts)
Change on the week: -0.7% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +0.9% (1.46M) over 7d
Shares outstanding: 8.34M | fund size: 161.97M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Positioning: net long 27.4% of OI, up 4.9% week, crowding 88th percentile (high but not extreme)
- Cost of holding: -5.7% annual roll cost, heavy drag on long exposure
- Fund flows: -3.7% share count over 1 week, indicating outflows
- Macro: no policy surprise; yields up modestly, inflation stable, Fed target unchanged

<details><summary><b>News</b> — score +0.00</summary>

- [[ETF 특징주] 노던트러스트, 뮤추얼펀드 역대 최대 규모 ETF 전환](https://www.newspim.com/news/view/20260928000933)  
  <sub>뉴스핌, 8 hours ago</sub>  
  이 기사는 인공지능(AI) 모델의 번역을 기반으로 전문 기자의 검증과 분석을 통해 생성한 콘텐츠로, 원문은 9월28일 블룸버그 보도입니다.
- [[ETF 특징주] 앤트로픽 상장 기다리기 힘들면…'우회로' ETF 등장](https://www.newspim.com/news/view/20260928000946)  
  <sub>뉴스핌, 8 hours ago</sub>  
  이 기사는 인공지능(AI) 모델의 번역을 기반으로 전문 기자의 검증과 분석을 통해 생성한 콘텐츠로, 원문은 9월23일(현지시각) 배런스 보도입니다.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.81 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 39.87 (-0.2%), 50d 39.72 (+0.2%), 200d 37.32 (+6.7%); 50d above 200d
Momentum: RSI(14) 49.2 | MACD 0.221 vs signal 0.160 (histogram 0.061)
Returns: 1d -2.0% | 5d -2.1% | 1m -0.4% | 3m +6.9%
52-week range: 29.37 - 41.43 (now 86.6% of the way up)
Volatility: ATR(14) 0.73 (1.8% of price) | annualised 20d 29.4%
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
Cost of holding this fund instead of copper itself: -5.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +6.9%, commodity +8.4%, gap -1.5% | 6 months: fund +19.0%, commodity +20.9%, gap -1.9% | 12 months: fund +34.9%, commodity +40.6%, gap -5.7%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 27.4% of open interest (301,657 contracts)
Change on the week: +4.9% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -3.7% (-28.21M) over 7d
Shares outstanding: 18.53M | fund size: 737.57M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals bearish but no decisive break, positioning unchanged, flat fund flows, modest negative cost of holding.

**Main reasons it gave:**
- Treasury yields rose modestly across curve (+0.10 to +0.27) with no surprise
- SLV price below 20d/50d/200d SMAs, RSI 40, MACD negative, volume 0.75x 20‑day avg
- CFTC net long 12.5% OI, weekly change -0.2% (tiny decrease)
- Fund share count flat (+0.0%) indicating no net inflow/outflow
- Cost of holding -2.6% annual drag, modest negative for long

<details><summary><b>News</b> — score +0.00</summary>

- [Gold And Silver: Lower Implied Volatility Met Higher Churn—Buy Options](https://seekingalpha.com/article/4950169-gold-and-silver-lower-implied-volatility-met-higher-churn-buy-options)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Implied volatility for SPDR Gold Shares and iShares Silver Trust is at unusually low percentiles—8th for GLD, and 6th for SLV—despite rising intraday price...
- [Gold, silver ETFs tumble up to 3.6% as precious metals slide on US Fed rate-hike fears](https://www.moneycontrol.com/news/business/markets/gold-silver-etfs-tumble-up-to-3-6-as-precious-metals-slide-on-us-fed-rate-hike-fears-14039881.html)  
  <sub>Moneycontrol.com, 8 hours ago</sub>  
  Gold and silver exchange-traded funds (ETFs) came under sharp selling pressure on Monday, tracking a steep fall in precious metal prices as rising crude oil...
- [Gold, silver ETFs tumble up to 4% as precious metals melt on rising yields](https://www.business-standard.com/markets/news/gold-silver-etfs-tumble-up-to-4-as-precious-metals-melt-on-rising-yields-126092800567_1.html)  
  <sub>Business Standard, 6 hours ago</sub>  
  Since gold ETFs and silver ETFs are designed to track the price of the underlying metal, a decline in the bullion prices weighs on them.
- [Your gold or silver ETF holds physical bullion: Here's what SEBI's new vault rules mean for investors](https://www.livemint.com/money/personal-finance/your-gold-or-silver-etf-holds-physical-bullion-heres-what-sebis-new-vault-rules-mean-for-investors-11790518596044.html)  
  <sub>Livemint, 22 hours ago</sub>  
  SEBI has approved changes to its vault manager rules, bringing physical bullion underlying gold and silver ETFs under a common framework.
- [Global X Silver Miners ETF Reports Inaugural Financial Results for Period Ended 30 June 2026](https://kalkine.com.au/news/announcements/global-x-silver-miners-etf-reports-inaugural-financial-results-for-period-ended-30-june-2026)  
  <sub>Kalkine, 7 hours ago</sub>  
  Global X Silver Miners ETF (ASX:SLV), managed by Global X Management (AUS) Limited as Responsible Entity, has released its inaugural financial report...
- [Gold, Silver ETFs fall up to 3.6%: Why precious metals are slipping as US Fed rate fears mount](https://www.india.com/business/gold-silver-etfs-fall-up-to-3-6-why-precious-metals-are-slipping-as-us-fed-rate-fears-mount-nifty-sensex-stock-market-8530945/)  
  <sub>India.com, 4 hours ago</sub>  
  ETFs of both Gold and silver plunged up to 3.6 percent on Monday following a global sell-off in precious metals. The massive drop came as surging crude oil...
- [Gold and Silver ETFs Extend Losses, Silver Down 3.6%, as Oil Lifts Rate Bets](https://www.niftytrader.in/markets/gold-and-silver-etfs-extend-losses-silver/)  
  <sub>NiftyTrader, 6 hours ago</sub>  
  Gold and Silver ETFs Extend Losses as oil prices rose and Fed rate-hike fears intensified. Here's what the fall means for investors.
- [Silver ETFs Slide Nearly 4% As Oil Surge Triggers Bullion Sell-off](https://www.businessworld.in/article/silver-etfs-slide-nearly-4-as-oil-surge-triggers-bullion-sell-off-625943)  
  <sub>BW Businessworld, 16 hours ago</sub>  
  Gold and silver exchange-traded funds (ETFs) came under heavy selling pressure on 28 September, with silver ETFs falling nearly 4 per cent and gold ETFs...
- [Gold, Silver ETF Crash Up To 7%: Tata, HDFC, Nippon India, Kotak To ICICI Prudential | Time To Buy?](https://www.goodreturns.in/news/gold-etf-silver-etf-crash-up-to-7-tata-hdfc-nippon-india-kotak-icici-prudential-time-to-buy-1496991.html)  
  <sub>Goodreturns, 22 hours ago</sub>  
  Gold, Silver ETF Crash Up To 7%: Tata, HDFC, Nippon India, Kotak To ICICI Prudential | Time To Buy? ... Gold, Silver ETF: Gold and silver exchange traded funds (...
- [Silver Stock Performance](https://finance.yahoo.com/sectors/basic-materials/silver/)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  PAN AMERICAN SILVER CORP has an Investment Rating of HOLD; a target price of $19.000000; an Industry Subrating of High; a Management Subrating of Low;...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 55.15 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 58.65 (-6.0%), 50d 57.55 (-4.2%), 200d 65.96 (-16.4%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -0.288 vs signal 0.088 (histogram -0.376)
Returns: 1d -5.1% | 5d -7.5% | 1m -12.1% | 3m +4.7%
52-week range: 41.86 - 105.60 (now 20.9% of the way up)
Volatility: ATR(14) 1.89 (3.4% of price) | annualised 20d 41.2%
Volume: 0.75x the 20-day average
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
Cost of holding this fund instead of silver itself: -2.6% a year -- a steady drag
Measured: 3 months: fund +4.7%, commodity +5.3%, gap -0.6% | 6 months: fund -13.1%, commodity -11.9%, gap -1.1% | 12 months: fund +34.4%, commodity +37.0%, gap -2.6%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 12.5% of open interest (106,474 contracts)
Change on the week: -0.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 341.45M | fund size: 18.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Macro unchanged: yields up 0.10‑0.27% this week, Fed target steady
- Technical mix: price 27.27 below 20‑day SMA, above 50‑day and 200‑day SMA
- Positioning crowded long (97th percentile) with +1.9% weekly net‑long increase
- Crop condition steady (58% good/excellent, 0‑point change) and cost of holding -1.0% annual drag

<details><summary><b>News</b> — score +0.00</summary>

- [El mercado de capitales suma nuevas opciones de inversión para el último trimestre del año: cuáles son y cómo funcionan](https://tn.com.ar/economia/2026/09/28/el-mercado-de-capitales-suma-nuevas-opciones-de-inversion-para-el-ultimo-trimestre-del-ano-cuales-son-y-como-funcionan/?outputType=amp)  
  <sub>TN, 6 hours ago</sub>  
  Se anunció el lanzamiento de nuevos cedears sobre plazas bursátiles internacionales, commodities y futuros del sector agropecuario.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.27 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 27.78 (-1.8%), 50d 26.54 (+2.7%), 200d 24.53 (+11.2%); 50d above 200d
Momentum: RSI(14) 48.6 | MACD 0.351 vs signal 0.475 (histogram -0.124)
Returns: 1d -1.6% | 5d -3.0% | 1m +1.9% | 3m +12.6%
52-week range: 21.46 - 28.14 (now 87.0% of the way up)
Volatility: ATR(14) 0.35 (1.3% of price) | annualised 20d 17.1%
Volume: 0.36x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.0% a year -- a steady drag
Measured: 3 months: fund +12.6%, commodity +15.8%, gap -3.2% | 6 months: fund +12.7%, commodity +10.8%, gap +2.0% | 12 months: fund +25.8%, commodity +26.8%, gap -1.0%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

```text
Soybeans rated good or excellent: 58% of the US crop (week 38 of 2026)
Direction over 3 weeks: steady, 0 points
Same week last year: 61% (-3 points)
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
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 23.8% of open interest (1,114,328 contracts)
Change on the week: +1.9% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (2.91K) over 7d
Shares outstanding: 1.66M | fund size: 45.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Positioning: net short increased by 1.9% of open interest, modest bearish pressure
- Cost of holding: -22.5% annual cost, heavy drag on long exposure
- Energy inventories: 53 BCF build, bearish supply signal
- EIA price outlook: forecast rise to $3.51 in 3 months, bullish for natural gas

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.75 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 10.56 (+1.8%), 50d 10.29 (+4.5%), 200d 11.41 (-5.8%); 50d below 200d
Momentum: RSI(14) 53.5 | MACD 0.178 vs signal 0.107 (histogram 0.071)
Returns: 1d -3.4% | 5d +4.8% | 1m +3.1% | 3m -5.9%
52-week range: 9.63 - 16.90 (now 15.4% of the way up)
Volatility: ATR(14) 0.36 (3.4% of price) | annualised 20d 42.6%
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
Cost of holding this fund instead of natural gas itself: -22.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -5.9%, commodity -1.5%, gap -4.4% | 6 months: fund -12.5%, commodity +1.2%, gap -13.7% | 12 months: fund -14.6%, commodity +7.9%, gap -22.5%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 3.6% of open interest (1,837,146 contracts)
Change on the week: +1.9% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 12.08M | fund size: 129.91M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- CFTC speculators net long 5.5% of OI, crowding 98th percentile, weekly change +0.1%
- U.S. crude inventories built +3.0 MMbbl (58th percentile)
- EIA outlook projects WTI price down ~10% over six months
- No policy or data surprise this week

<details><summary><b>News</b> — score +0.00</summary>

- [Diesel export ban carries hidden costs for U.S. fuel market (USO:NYSEARCA)](https://seekingalpha.com/news/4647543-diesel-export-ban-carries-hidden-costs-for-us-fuel-market)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. diesel export ban debate: SocGen warns a ban may briefly cut prices but later raise pump costs via refinery run cuts and global impacts.
- [Dow Soars 800 Points Driven By Healthcare Stocks — But Chip Stocks Drag S&P 500, Nasdaq](https://stocktwits.com/news-articles/markets/equity/dow-soars-as-investors-flee-chip-stocks-pile-into-healthcare-sector/cZ0ZLU0Reys)  
  <sub>Stocktwits, 14 hours ago</sub>  
  U.S. equities were split in Thursday morning's trade as investors rotated out of chip stocks and piled into healthcare, financials, and communication...
- [Gavin Newsom Slams Trump Fuel Economy Rollback, Says New Standards Will Make ‘America Smoggy Again’](https://www.benzinga.com/news/politics/26/09/62016706/gavin-newsom-slams-trump-fuel-economy-rollback-says-new-standards-will-make-america-smoggy-again)  
  <sub>Benzinga, 4 hours ago</sub>  
  Newsom slammed Trump's rollback of Biden-era fuel standards, saying it benefits Big Oil as the Iran war drives gas prices higher.
- [Oil jumps 3% after Trump rejects Iran peace proposal (CO1:COM:Commodity)](https://seekingalpha.com/news/4647544-oil-jumps-3-percent-after-trump-rejects-iran-peace-proposal)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Oil prices climbed about 3% Monday after President Donald Trump rejected an Iranian proposal aimed at ending the conflict and reopening the Strait of Hormuz...
- [INDO, USO, XLE, BATL In Focus As Iran Shock Hits Oil — Why Analysts Think Market May Look Past Doomsday Calls](https://stocktwits.com/news-articles/markets/equity/iran-oil-shock-indo-uso-xle-batl-analysts-market-outlook/cZddtF9RIch)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Energy stocks rallied overnight after the U.S.-Israeli strikes on Iran killed Supreme Leader Khamenei, sending Brent crude up 13%. USO and XLE rose 4%,...
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”
- [Trump Reportedly Says Oil Prices Won’t Tumble Until After Midterms, While Iran Signals More Intense War — USO, UCO Rise](https://stocktwits.com/news-articles/markets/equity/trump-reportedly-says-oil-prices-wont-tumble-until-after-midterms-while-iran-signals-more-intense-war-uso-uco-rise/cZt7k6WRJC2)  
  <sub>Stocktwits, 21 hours ago</sub>  
  President Donald Trump reportedly said on Wednesday that energy prices elevated by the Iran war are unlikely to come down until after the midterm elections,...
- [Dow futures tumble 305 points: 5 things to know before Wall Street opens](https://invezz.com/ie/news/2026/09/28/dow-futures-tumble-305-points-5-things-to-know-before-wall-street-opens/)  
  <sub>Invezz, 3 hours ago</sub>  
  US stock futures fell on Monday as a fresh surge in oil prices revived inflation concerns and pushed Treasury yields higher, putting technology shares under...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 153.68 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 149.46 (+2.8%), 50d 136.22 (+12.8%), 200d 113.64 (+35.2%); 50d above 200d
Momentum: RSI(14) 58.7 | MACD 4.766 vs signal 5.748 (histogram -0.982)
Returns: 1d +3.6% | 5d +3.7% | 1m +18.2% | 3m +43.5%
52-week range: 66.17 - 161.86 (now 91.5% of the way up)
Volatility: ATR(14) 5.30 (3.5% of price) | annualised 20d 46.7%
Volume: 0.39x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.50</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 5.5% of open interest (1,841,811 contracts)
Change on the week: +0.1% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 8d
Shares outstanding: 119.10M | fund size: 18.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, positioning shows modest bullish tilt, but heavy cost of holding penalizes longs; overall neutral.

**Main reasons it gave:**
- No macro surprise: yields modestly up, inflation and unemployment in line with expectations
- Technicals: price below 20‑day and 50‑day SMA, RSI 38.8, no decisive break
- Positioning: net short 2.5% of OI, down 1.7% week‑over‑week (reduction in short bias)
- Cost of holding: -12.1% annual gap, heavy roll cost penalizing longs
- Fund flows: +2.8% share count over week indicating inflow

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 24.93 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 26.43 (-5.7%), 50d 25.56 (-2.5%), 200d 23.10 (+7.9%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -0.077 vs signal 0.162 (histogram -0.239)
Returns: 1d -2.2% | 5d -5.2% | 1m -8.4% | 3m +14.3%
52-week range: 19.88 - 28.00 (now 62.2% of the way up)
Volatility: ATR(14) 0.58 (2.3% of price) | annualised 20d 22.5%
Volume: 0.44x the 20-day average
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
Cost of holding this fund instead of wheat itself: -12.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +14.3%, commodity +20.3%, gap -6.0% | 6 months: fund +7.6%, commodity +13.2%, gap -5.6% | 12 months: fund +17.9%, commodity +30.0%, gap -12.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 2.5% of open interest (483,279 contracts)
Change on the week: -1.7% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.8% (9.43M) over 7d
Shares outstanding: 14.10M | fund size: 351.51M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Gold And Silver: Lower Implied Volatility Met Higher Churn—Buy Options](https://seekingalpha.com/article/4950169-gold-and-silver-lower-implied-volatility-met-higher-churn-buy-options)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Implied volatility for SPDR Gold Shares and iShares Silver Trust is at unusually low percentiles—8th for GLD, and 6th for SLV—despite rising intraday price...
- [Gold Bull Run Looks Finished—Unless You Look Closer](https://www.benzinga.com/markets/commodities/26/09/62016691/gold-bull-run-looks-finished-unless-you-look-closer)  
  <sub>Benzinga, 4 hours ago</sub>  
  Gold prices drop 3.35% as hawkish Fed sentiment and Chinese profit-taking end the August rally. Key chart patterns & outlook inside.
- [Gold resilience tested as yield surge and stronger dollar weigh (GLD:NYSEARCA)](https://seekingalpha.com/news/4647447-gold-resilience-tested-as-yield-surge-and-stronger-dollar-weigh)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  How much longer can the divergence between gold investment demand and US real yields continue? Saxo Bank says Monday's price action suggests the...
- [Dow, S&P 500, Nasdaq Futures Fall As Brent Tops $106 After Trump Rejects Iran Proposal: MU, SLV, QNT, META In Focus](https://de.tradingview.com/news/stocktwits:90bdaed6f094b:0-dow-s-p-500-nasdaq-futures-fall-as-brent-tops-106-after-trump-rejects-iran-proposal-mu-slv-qnt-meta-in-focus/)  
  <sub>TradingView, 12 hours ago</sub>  
  U.S. stock futures fell in overnight trading late Sunday as oil prices climbed after President Donald Trump rejected an Iranian proposal to reopen the...
- [The Next Move Looks Bullish, But It Needs To Come Sooner Rather Than Later (Technical Analysis)](https://seekingalpha.com/article/4950096-the-next-move-looks-bullish-but-it-needs-to-come-sooner-rather-than-later-technical-analysis)  
  <sub>Seeking Alpha, 11 hours ago</sub>  
  Gold and silver are still digesting the massive move seen in 2025 and January of 2026. In gold, trade volume dropped but has recovered some. Read more here.
- [Fed Rate Hike Odds Hit 70%: Gold, Treasury Yields Signal - SPDR Gold Shares (ARCA:GLD)](https://www.benzinga.com/markets/economic-data/26/09/62020961/fed-rate-hike-odds-70-percent-gold-treasury-yields-2007)  
  <sub>Benzinga, 2 hours ago</sub>  
  Fed rate hike odds hit 70% as the 10-year yield sits at 5.22%, its highest since 2007, and gold slides 3%. What SPDR Gold Shares (GLD) and bonds are...
- [Gold, Silver Take A Hit: What’s Driving The Sharp Selloff In GLD, SLV, NEM And PAAS?](https://stocktwits.com/news-articles/markets/equity/gold-sinks-to-7-week-low-as-treasury-yields-fed-hike-bets-rise-hansen-warns-bullion-s-resilience-faces-its-toughest-test-yet/cZMSsPcRBQh)  
  <sub>Stocktwits, 3 hours ago</sub>  
  Ole Hansen warned that rising credit stress could trigger further selling if investors turn to liquid assets such as gold to raise cash.
- [BofA Securities Maintains Kinross Gold(KGC.US) With Buy Rating, Cuts Target Price to $32.25](https://news.futunn.com/en/post/1000247338/bofa-securities-maintains-kinross-gold-kgcus-with-buy-rating-cuts)  
  <sub>富途牛牛, 9 hours ago</sub>  
  BofASecurities analyst Lawson Winder maintains $Kinross Gold(KGC.US)$ with a buy rating, and adjusts the target price from $35 to $32.25.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.10 on the week) | 5-year 5.06% (+0.22 on the week) | 10-year 5.23% (+0.27 on the week) | 30-year 5.55% (+0.26 on the week)
Yield curve, 10-year minus 3-month: +1.15 points -- upward sloping (normal)
US dollar index: 101.19 (+0.76 on the week)
Volatility (VIX): 15.86 (+1.0 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.87% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 377.87 (bar of 2026-09-28), from 500 daily bars
Trend: vs 20d SMA 397.78 (-5.0%), 50d 395.62 (-4.5%), 200d 416.39 (-9.3%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -3.205 vs signal -1.066 (histogram -2.140)
Returns: 1d -4.0% | 5d -5.1% | 1m -10.6% | 3m +2.5%
52-week range: 346.74 - 495.90 (now 20.9% of the way up)
Volatility: ATR(14) 7.65 (2.0% of price) | annualised 20d 24.4%
Volume: 0.68x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +2.5%, commodity +2.7%, gap -0.2% | 6 months: fund -8.9%, commodity -7.7%, gap -1.2% | 12 months: fund +9.6%, commodity +10.0%, gap -0.4%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 30.9% of open interest (412,800 contracts)
Change on the week: -1.6% of open interest
Crowding: 63% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 260.30M | fund size: 98.36B
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

