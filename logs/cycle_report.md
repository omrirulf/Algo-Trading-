# Daily report

**01 Oct 2026, 19:09 Israel time (16:09 UTC)** · 80 names checked · 0 traded · 0 with a problem

**Answers with no explanation:** 11 of 61 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 5 | 11 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 41 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| Developing country bonds (EMB) · Index fund | **Sold part.** Sold 42 of 86 shares at +4.36R, 44 still held. Stop-loss raised 92.14 → 91.07. |
| US regional banks (KRE) · Sector or country | **Sold part.** Sold 17 of 53 shares at +1.19R, 36 still held. Stop-loss raised 71.93 → 70.85. |
| S&P 500, equal weight (RSP) · Index fund | **Sold part.** Sold 4 of 14 shares at +1.08R, 10 still held. Stop-loss raised 212.66 → 211.49. |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop raised.** At +2.93R, following the price. Stop-loss raised 90.26 → 89.90. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.76R, following the price. Stop-loss raised 40.52 → 39.81. |
| US government bonds, 20+ years (TLT) · Index fund | **Stop raised.** At +2.90R, following the price. Stop-loss raised 79.30 → 78.88. |
| US dollar (UUP) · Index fund | **Stop raised.** At +2.26R, following the price. Stop-loss raised 28.54 → 28.65. |
| US shopping and leisure (XLY) · Sector or country | **Stop raised.** At +0.55R, following the price. Stop-loss raised 112.09 → 111.36. |
| ASML (ASML) · Company | **Holding.** +0.75R, holding 1 shares. Stop-loss 1733.63. |
| Caterpillar (CAT) · Company | **Holding.** +0.21R, holding 2 shares. Stop-loss 780.92. |
| Taiwan (EWT) · Sector or country | **Holding.** -0.51R, holding 33 shares. Stop-loss 110.28. |
| Gold (GLD) · Commodity | **Holding.** +0.43R, holding 10 shares. Stop-loss 393.48. |
| HDFC Bank (HDB) · Company | **Holding.** -0.35R, holding 90 shares. Stop-loss 22.23. |
| Eli Lilly (LLY) · Company | **Holding.** -0.04R, holding 4 shares. Stop-loss 1130.70. |
| Microsoft (MSFT) · Company | **Holding.** +1.18R, holding 7 shares. Stop-loss 493.66. |
| Nvidia (NVDA) · Company | **Holding.** +1.17R, holding 16 shares. Stop-loss 219.12. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.19R, holding 128 shares. Stop-loss 37.20. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +2.99R, holding 4 shares. Stop-loss 104.79. |
| Exxon Mobil (XOM) · Company | **Holding.** +0.28R, holding 13 shares. Stop-loss 156.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### MercadoLibre (MELI) · Company — BULLISH, confidence 0.62

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Credit portfolio grew 75% YoY to $16.4B (strong catalyst), analysts are strongly bullish with a mean price target 34.8% above current price, and insiders made recent purchases. Technicals show short‑term weakness (oversold RSI, price below SMAs) and earnings have missed three of the last four quarters, tempering confidence. Overall the bullish fundamentals and sentiment outweigh the technical and earnings drag, yielding a moderate‑high conviction bullish signal.

**Main reasons it gave:**
- Credit portfolio expanded 75% YoY to $16.4B in Q2 2026
- Analyst consensus strong buy; mean price target $2,266 (+34.8% vs last close)
- Insider purchases: 2 insiders bought 724 shares (~$1.2M) in last 180 days
- Technical indicators show oversold RSI (31.1) and price below 20/50/200‑day SMAs

<details><summary><b>News</b> — score +0.60</summary>

- [MercadoLibre, Inc. (MELI) Stock Forecasts](https://finance.yahoo.com/research/reports/MS_0P00009FL7_AnalystReport_1790804868000)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Credit Portfolio Growth Might Change The Case For Investing In MercadoLibre Stock (MELI)](https://simplywall.st/stocks/us/retail/nasdaq-meli/mercadolibre/news/credit-portfolio-growth-might-change-the-case-for-investing)  
  <sub>Simply Wall Street, 24 hours ago</sub>  
  MercadoLibre reported that its credit portfolio reached US$16.4b in Q2 2026, reflecting 75% year-over-year expansion supported by stronger credit card...
- [New Street Research starts coverage of MercadoLibre stock at USD 2,450.00](https://www.ad-hoc-news.de/boerse/news/corporate-news/new-street-research-starts-coverage-of-mercadolibre-stock-at-usd-2-450-00/70209431)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  MELI, US58733R1023. New Street Research starts coverage of MercadoLibre stock at USD 2,450.00. Published on 10/01/2026 at 11:20 | Editorial responsibility:...
- [Oil Prices Surge Nearly 10% — US Forces To Resume Maritime Blockade Against Iran On Tuesday](https://stocktwits.com/news-articles/markets/equity/oil-prices-surge-10-percent-us-forces-to-resume-maritime-blockade-against-iran-on-tuesday/cZmz6rZR7Yo)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The U.S. Central Command said U.S. forces will enforce the blockade on vessels entering or leaving Iranian ports starting July 14 at 4 p.m. ET.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.70</summary>

```text
Last close 1,681.59 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 1,827.88 (-8.0%), 50d 1,862.23 (-9.7%), 200d 1,838.95 (-8.6%); 50d above 200d
Momentum: RSI(14) 31.1 | MACD -48.555 vs signal -31.694 (histogram -16.861)
Returns: 1d -2.7% | 5d -4.1% | 1m -14.4% | 3m -4.6%
52-week range: 1,546.81 - 2,360.76 (now 16.6% of the way up)
Volatility: ATR(14) 56.31 (3.3% of price) | annualised 20d 25.0%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 85.25B
Valuation: trailing P/E 45.67 | forward P/E 30.08 | P/B 10.88 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 17 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 2,266.09 (+34.8% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-08-06 BTIG: reit, Buy -> Buy
  - 2026-07-15 Citigroup: main, Neutral -> Neutral
  - 2026-06-02 BTIG: reit, Buy -> Buy
Institutional ownership: 80.2%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Gemini 4 Argon AI model launch, stock rose ~1% after-hours
- Strong fundamentals: trailing P/E 17.15, profit margin 54.8%, revenue growth 24.2% YoY
- Analyst consensus strong buy, mean price target +25.7% vs last close
- Technical weakness: price below 20‑day SMA, low volume (0.39× 20‑day avg)

<details><summary><b>News</b> — score +0.50</summary>

- [GOOGL Stock Rises After Gemini 4 Argon Launch, But JPMorgan Says Google Must Reclaim AI Leadership](https://finance.yahoo.com/technology/ai/articles/googl-stock-rises-gemini-4-125240353.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  DeepMind-provided benchmarks cited by JPMorgan show Argon competing with models from OpenAI and Anthropic across several complex use cases.
- [Google Unveils New AI Model Gemini 4 Argon, Sending Alphabet Stock Higher](https://www.barrons.com/articles/google-ai-gemini-4-argon-alphabet-stock-d3df631c)  
  <sub>Barron's, 3 hours ago</sub>  
  Google announced its newest artificial-intelligence model Wednesday, sending the tech giant's stock higher as it attempts to keep up with rivals in the race...
- [Stocks making the biggest moves premarket: Alphabet, Accenture, Rocket Lab, Micron and more](https://www.cnbc.com/2026/10/01/stocks-making-the-biggest-moves-premarket-googl-acn-rklb-mu.html)  
  <sub>CNBC, 3 hours ago</sub>  
  These are the stocks posting the largest moves in the premarket.
- [Will Google Turn The Tables In AI Race? Wall Street Reacts To Gemini 4.](https://www.investors.com/news/technology/google-stock-wall-street-reaction-gemini4-artificial-intellience-model/)  
  <sub>Investor's Business Daily, 2 hours ago</sub>  
  Wall Street cheered Alphabet's release of a new artificial-intelligence model, called Gemini 4 Argon, after delays. Google stock climbed.
- [Is Alphabet's Argon AI Model Benchmaxxed? Probably, But The Stock Remains A Buy (GOOG)](https://seekingalpha.com/article/4951347-is-alphabet-argon-ai-model-benchmaxxed-probably-but-stock-remains-buy)  
  <sub>Seeking Alpha, 52 minutes ago</sub>  
  Alphabet Inc. is still a Buy: Gemini 4 Argon doubts, but $240B cash, strong margins, and AI monetization via Cloud/TPUs support upside. Click for this GOOG...
- [GOOGL Stock Adds 1% After Hours As Google Unveils Gemini 4 Argon With Focus On Coding, Cybersecurity](https://www.tradingview.com/news/stocktwits:8e1578e0d094b:0-googl-stock-adds-1-after-hours-as-google-unveils-gemini-4-argon-with-focus-on-coding-cybersecurity/)  
  <sub>TradingView, 15 hours ago</sub>  
  Alphabet's Google (GOOG, GOOGL) unveiled Gemini 4 Argon on Wednesday, its latest frontier artificial intelligence model engineered to manage complex...
- [Alphabet stock slips on report of internal doubts over Gemini 4](https://www.investing.com/news/stock-market-news/alphabet-stock-slips-on-report-of-internal-doubts-over-gemini-4-4925797)  
  <sub>Investing.com, 13 hours ago</sub>  
  Investing.com -- Alphabet Inc. (NASDAQ:GOOGL) shares declined Wednesday heading to the market close, paring gains to up 0.5% from up over 2%, following a...
- [How Gemini 4 Argon Will Impact Google Stock Investors](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/how-gemini-4-argon-will-impact-google-stock-investors)  
  <sub>Simply Wall Street, 13 hours ago</sub>  
  Alphabet launched its most powerful AI model, Gemini 4 Argon, and Google began rolling it out to cybersecurity firms before broader access.
- [KLAR Stock On Track To Hit February Highs – What Is The Google Connection?](https://stocktwits.com/news-articles/markets/equity/why-is-klar-stock-rising-today-googl-connection/cZm3QPSR7Kp)  
  <sub>Stocktwits, 12 hours ago</sub>  
  KLAR Stock On Track To Hit February Highs – What Is The Google Connection? Klarna said a Swedish court awarded PriceRunner about $1.97 billion in damages over...
- [Alphabet Inc. (GOOGL) Stock Forecasts](https://finance.yahoo.com/research/reports/ARGUS_48397_TechnicalAnalysis_1790853013000)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 341.55 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 342.74 (-0.3%), 50d 343.92 (-0.7%), 200d 338.76 (+0.8%); 50d above 200d
Momentum: RSI(14) 48.0 | MACD -0.384 vs signal -0.307 (histogram -0.077)
Returns: 1d -0.7% | 5d -0.2% | 1m +2.0% | 3m -5.1%
52-week range: 236.57 - 402.62 (now 63.2% of the way up)
Volatility: ATR(14) 8.70 (2.5% of price) | annualised 20d 25.4%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.36 (+25.7% vs last close), range 340.00 - 515.00
Recent rating changes:
  - 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - 2026-09-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-09-03 Rosenblatt: main, Buy -> Buy
  - 2026-07-23 UBS: main, Neutral -> Neutral
  - 2026-07-23 Morgan Stanley: main, Overweight -> Overweight
Institutional ownership: 81.0%
Largest holders: Blackrock Inc. (7.9%), Vanguard Capital Management LLC (6.5%), FMR, LLC (4.3%), State Street Corporation (4.1%), Geode Capital Management, LLC (2.6%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Royal Bank of Canada (RY) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Insider purchases: 350k shares on 2026-08-31 and 350k on 2026-08-28 (~$143M total).
- Fundamentals: ROE 16.2%, earnings growth 12.8% YoY, forward P/E 15.3.
- Technical: RSI 29.6 (oversold), price below 20-day SMA, volume 0.25x 20-day avg.
- Analyst consensus: buy, mean rating 2.13, price target +7.6% vs last close.
- News: Q3 net income up 11% (in line with expectations).

<details><summary><b>News</b> — score +0.00</summary>

- [Will the Stock Market Crash? History Gives a 95% Reason to Stay Calm](https://www.fool.com/investing/2026/10/01/will-the-stock-market-crash-history-gives-a-95-rea/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  The S&P 500 has risen an overwhelming majority of the time in the 12 months after midterm elections.
- [Canadian Imperial Bank of Commerce (CM) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/CM/)  
  <sub>Yahoo Finance UK, 4 hours ago</sub>  
  Find the latest Canadian Imperial Bank of Commerce (CM) stock quote, history, news and other vital information to help you with your stock trading and...
- [Royal Bank of Canada announces debentures, the group behind Royal Bank of Canada stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-announces-debentures-the-group-behind-royal-bank-of/70210217)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  Royal Bank of Canada stock costs EUR 174.54 on October 1, 2026. Third-quarter net income rose 11.00 percent, with prior close EUR 173.91.
- [Less friction, no fees, more freedom: RBC offers convenient ways to send money around the world with International Money Transfers](https://www.marketscreener.com/news/less-friction-no-fees-more-freedom-rbc-offers-convenient-ways-to-send-money-around-the-world-with-ce785ad3de88f52c)  
  <sub>www.marketscreener.com, 5 hours ago</sub>  
  Conversion-free transfers for USD, EUR, GBP and HKD currencies held in RBC U.S. and RBC Foreign Currency AccountsDigital self-serve available any time...
- [Why Did Royal Bank of Canada (TSX:RY) Cross This Level?](https://kalkinemedia.com/ca/stocks/financial/why-did-royal-bank-of-canada-tsxry-cross-this-level)  
  <sub>Kalkine Media, 21 hours ago</sub>  
  Royal Bank of Canada shares moved past a key trend line. Explore what is shaping sentiment around this major Canadian bank.
- [Royal Bank of Canada stock after-hours at EUR 173.82: minus 0.61 percent versus prior close](https://www.ad-hoc-news.de/boerse/news/nachboerse/royal-bank-of-canada-stock-after-hours-at-eur-173-82-minus-0-61-percent/70206451)  
  <sub>AD HOC NEWS, 19 hours ago</sub>  
  Royal Bank of Canada stock was at EUR 173.82 after-hours at 10:01 p.m. CEST on September 30, 2026, down 0.61 percent versus the prior Lang & Schwarz close.
- [Royal Bank of Canada (TSX:RY): Can Dividend Growth Continue?](https://kalkinemedia.com/ca/stocks/dividend/royal-bank-of-canada-tsxry-can-dividend-growth-continue)  
  <sub>Kalkine Media, 19 hours ago</sub>  
  Royal Bank of Canada dividend performance, capital management, and shareholder returns strategies.
- [Which Canadian Dividend Names Deserve Attention This Season?](https://kalkinemedia.com/ca/stocks/dividend/which-canadian-dividend-names-deserve-attention-this-season)  
  <sub>Kalkine Media, 23 hours ago</sub>  
  Explore how Royal Bank of Canada and two other Canadian names fit into a broader dividend growth conversation shaping the TSX this season.
- [Royal Bank of Canada shares technical analysis: C$272.30 support under pressure as pullback deepens](https://tradersunion.com/news/stocks/show/3606675-royal-bank-of-canada-slides/)  
  <sub>Traders Union, 42 minutes ago</sub>  
  Royal Bank of Canada trades at C$275.68 today, down 1.52%. RY extends European clearing, with technicals signaling further weakness.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 192.99 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 203.51 (-5.2%), 50d 206.89 (-6.7%), 200d 186.23 (+3.6%); 50d above 200d
Momentum: RSI(14) 29.6 | MACD -2.808 vs signal -1.935 (histogram -0.873)
Returns: 1d -1.8% | 5d -3.3% | 1m -5.2% | 3m -5.8%
52-week range: 143.64 - 217.87 (now 66.5% of the way up)
Volatility: ATR(14) 3.22 (1.7% of price) | annualised 20d 16.9%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 267.17B
Valuation: trailing P/E 17.25 | forward P/E 15.32 | P/B 2.79 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-09-30 in line | 2026-06-30 in line | 2026-03-31 beat by 3% | 2026-03-31 beat by 3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 207.56 (+7.6% vs last close), range 182.74 - 224.85
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.80</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 387,640 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-08-31 Royal Bank of Canada (Issuer): 350,000 shares, 71.49M
  - 2026-08-28 Royal Bank of Canada (Issuer): 350,000 shares, 71.50M
  - 2026-07-31 Royal Bank of Canada (Issuer): 140 shares, 29.28K
  - 2026-07-31 Royal Bank of Canada (Issuer): 153 shares, 32.23K
(105 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.80</summary>

_Not available today._

</details>

### Toyota (TM) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The news of a $1.34 B EV plant investment in Argentina and a new hybrid SUV model provide a modest positive catalyst, while the stock has been trending down technically. Fundamentals are mixed (cheap valuation but high leverage), but the company’s strong earnings record (4 straight beats) and a consensus strong‑buy rating with a 27.5 % price‑target upside strongly support a bullish view. Technical weakness drags conviction down, resulting in a moderate bullish signal.

**Main reasons it gave:**
- Potential $1.34 B EV plant investment in Argentina (news)
- Four consecutive earnings beats (earnings record)
- Consensus strong‑buy with 27.5 % price‑target upside (analyst view)
- Technical weakness: price below 20/50/200‑day SMAs, RSI 38, low volume (technical)
- Low trailing P/E 8.23 indicating cheap valuation (fundamentals)

<details><summary><b>News</b> — score +0.35</summary>

- [Toyota's new SUV comes with all-terrain tires and a removable cooler.](https://www.stocktitan.net/news/TM/room-with-a-view-toyota-grand-highlander-adds-woodland-edition-for-97zlpeg3yv9j.html)  
  <sub>Stock Titan, 46 minutes ago</sub>  
  Toyota (TM) is expanding its Grand Highlander lineup with a new hybrid Woodland Edition for the 2027 model year. The Woodland Edition comes with all-wheel...
- [Toyota Motor Corporation (TM) Dips More Than Broader Market: What You Should Know](https://finance.yahoo.com/markets/stocks/articles/toyota-motor-corporation-tm-dips-205005408.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Toyota Motor Corporation (TM) closed at $183.10 in the latest trading session, marking a -1.93% move from the prior day. The stock fell short of the S&P 500...
- [Toyota eyes a major plant investment in Argentina (TM:NYSE)](https://seekingalpha.com/news/4648945-toyota-eyes-a-major-plant-investment-in-argentina)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Toyota (TM) may invest $1.34B in a new Argentina EV plant in Zárate under RIGI, boosting exports and jobs.
- [Why Is Constellation Energy Stock Trading Higher Today? - Constellation Energy (NASDAQ:CEG)](https://www.benzinga.com/trading-ideas/movers/26/10/62100792/constellation-energy-amazon-lock-20-year-nuclear-power-purchase-agreement-stock-soars)  
  <sub>Benzinga, 4 hours ago</sub>  
  Constellation Energy Corporation (NASDAQ:CEG) shares are trading higher by almost 4% during Thursday's premarket session. On Wednesday, the company penned a...
- [Joby Aviation stock nears 52-week low despite p...](https://pluang.com/en/news-feed/prediksi-revolusi-aviation-besar-berawal-dari-joby)  
  <sub>Pluang, 3 hours ago</sub>  
  Joby Aviation's stock trades near its 52-week low at $6.13 while the company advances toward its first commercial passenger flights, highlighted by a recent...
- [BYD Has Already Lapped Tesla — Now It Says Toyota Is Next And US Market Doesn't Matter](https://stocktwits.com/news-articles/markets/equity/byd-tesla-toyota-next-us-market-dont-matter/cZZ2Dc3R7A9)  
  <sub>Stocktwits, 13 hours ago</sub>  
  BYD's European market share more than doubled to 2.8% in May, surpassing Ford, Tesla and Nissan.
- [The Zacks Analyst Blog Highlights Toyota, Honda and Nissan](https://finance.yahoo.com/markets/stocks/articles/zacks-analyst-blog-highlights-toyota-073300665.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Chicago, IL – October 1, 2026 – Zacks.com announces the list of stocks featured in the Analyst Blog. Every day the Zacks Equity Research analysts discuss...
- [(SMVP) Technical Patterns and Signals (SMVP:CA)](https://news.stocktradersdaily.com/canada/smvp-technical-patterns-and-signals_20261001_6defbe)  
  <sub>Stock Traders Daily, 9 hours ago</sub>  
  Technical Patterns and Signals for HAMILTON CHAMPIONS TM U.S. Dividend Index ETF (SMVP) with Buy and Sell Indicators.
- [A test found nearly fivefold improvement over untreated filters. Zentek shipped its first filters to a federal facility.](https://www.stocktitan.net/news/ZTEKF/zentek-ships-first-government-of-canada-order-of-zen-guard-tm-10rfjdt85ipp.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  A three-month school pilot estimated 22% lower fan energy than standard filters; the federal offer runs to Aug. 18, 2027, with no minimum orders.
- [Why Toyota Motor Corporation (TM) Was Hit by U.S. Tariffs](https://finance.yahoo.com/markets/stocks/articles/why-toyota-motor-corporation-tm-153812534.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Gabelli Investment Management Firm recently released its “Dividend Growth Fund” second-quarter 2026 investor letter. A copy of the letter can be downloaded...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 183.60 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 191.72 (-4.2%), 50d 190.59 (-3.7%), 200d 201.55 (-8.9%); 50d below 200d
Momentum: RSI(14) 38.1 | MACD -1.690 vs signal -0.349 (histogram -1.341)
Returns: 1d +0.3% | 5d -1.7% | 1m -7.3% | 3m +5.2%
52-week range: 166.50 - 248.29 (now 20.9% of the way up)
Volatility: ATR(14) 3.15 (1.7% of price) | annualised 20d 22.4%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 217.42B
Valuation: trailing P/E 8.23 | forward P/E 11.63 | P/B 14.93 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+27.5% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

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

### JPMorgan Chase (JPM) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Buy signal based on strong fundamentals, positive earnings record, bullish analyst consensus, and notable institutional buying, tempered by slightly bearish technicals and neutral insider activity.

**Main reasons it gave:**
- Kintra Wealth LLC increased JPM stake by 35.2% (large institutional purchase)
- Ameritas Advisory Services LLC boosted JPM stake by 48.4% (large institutional purchase)
- JPM raised its dividend (supports dividend sustainability)
- RSI 29.2 indicates oversold condition (technical bullish signal)
- Four consecutive earnings beats (strong earnings record)

<details><summary><b>News</b> — score +0.30</summary>

- [JPMorgan Chase & Co. $JPM Stock Position Raised by Kintra Wealth LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-position-raised-by-kintra-wealth-llc-2026-10-01/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Kintra Wealth LLC increased its position in shares of JPMorgan Chase & Co. (NYSE:JPM) by 35.2% during the 2nd quarter, according to the company in its most...
- [JCDecaux (ENXTPA:DEC) Stock Fair Value Edges Higher After JPMorgan Target Increases](https://finance.yahoo.com/markets/stocks/articles/jcdecaux-enxtpa-dec-stock-fair-231116141.html)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  JCDecaux is back in focus after JPMorgan raised its price target first to €30 and then to €34, while recent valuation work now points to a fair value of...
- [REG - JPMorgan ETFs (Ire.) JPM (Ire) ICAV UST$ - Dividend Declaration](https://www.tradingview.com/news/reuters.com,2026-10-01:newsml_RSA2584Xa:0-reg-jpmorgan-etfs-ire-jpm-ire-icav-ust-dividend-declaration/)  
  <sub>TradingView, 2 hours ago</sub>  
  RNS Number : 2584X JPMorgan ETFs (Ireland) ICAV 01 October 2026 This information is provided by RNS, the news service of the London Stock Exchange.
- [CNMD Stock Hits Highest Level In Over Four Months – Why JPMorgan Believes Firm Would Be Highly Attractive To ‘Financial Acquirers’](https://stocktwits.com/news-articles/markets/equity/cnmd-stock-hits-highest-level-in-over-four-months-why-jp-morgan-believes-firm-would-be-highly-attractive-to-financial-acquirers-1/cZmzvNGR7Yi)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Shares of Conmed (CNMD) attracted significant investor attention on Monday after analysts commented on the reported buyout interest received by the medical...
- [JPMorgan Chase (JPM) CEO Pushes US Europe Trade Pact As Bank Backs Michigan LIFT](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/jpmorgan-chase-jpm-ceo-pushes-us-europe-trade-pact-as-bank-b)  
  <sub>Simply Wall Street, 19 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) CEO Jamie Dimon has proposed a new US Europe free trade pact that includes allied democracies as a counterweight to China.
- [JPM vs. BAC: The Bank Built to Sustain Dividend Growth When Markets Turn](https://247wallst.com/investing/2026/09/30/jpm-vs-bac-the-bank-built-to-sustain-dividend-growth-when-markets-turn/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  JPMorgan and Bank of America both just raised their dividends and both stocks just slid, but only one has the capital cushion and crisis track record to...
- [JPMorgan Chase & Co. $JPM Stock Purchased by Ameritas Advisory Services LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-purchased-by-ameritas-advisory-services-llc-2026-10-01/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Ameritas Advisory Services LLC boosted its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 48.4% during the 2nd quarter, according to...
- [JPAW.MU Interactive Stock Chart | JPM ETFs(I)-ALLCou.REI.SRI PAAR Stock](https://finance.yahoo.com/chart/JPAW.MU)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MSFT Stock Slides 4.5% — Microsoft Price Target Revision By Stifel And Xbox Pricing Changes In Focus](https://stocktwits.com/news-articles/markets/equity/msft-stock-slides-amid-stifel-price-target-cut-and-xbox-price-hikes/cZ1GskER7XZ)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Shares of Microsoft Corp. (MSFT) fell nearly 4.5% on Thursday after Stifel lowered its price target on the stock and the company announced Xbox price hikes.
- [JPMorgan Chase & Co. $JPM Stock Sold by HighTower Advisors LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-sold-by-hightower-advisors-llc-2026-10-01/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  HighTower Advisors LLC lessened its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 1.4% in the 2nd quarter, according to its most...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 327.23 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 346.50 (-5.6%), 50d 352.47 (-7.2%), 200d 321.68 (+1.7%); 50d above 200d
Momentum: RSI(14) 29.2 | MACD -5.847 vs signal -3.647 (histogram -2.201)
Returns: 1d -1.1% | 5d -3.3% | 1m -7.8% | 3m -2.2%
52-week range: 282.84 - 365.18 (now 53.9% of the way up)
Volatility: ATR(14) 6.52 (2.0% of price) | annualised 20d 19.4%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 869.84B
Valuation: trailing P/E 14.03 | forward P/E 13.06 | P/B 2.46 | PEG 1.57
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 0.9% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.60</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 4% | 2026-03-31 beat by 8% | 2025-12-31 beat by 3% | 2025-09-30 beat by 4%
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
Consensus: buy (mean 2.08 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 375.81 (+14.8% vs last close), range 305.00 - 436.00
Recent rating changes:
  - 2026-09-28 HSBC: main, Hold -> Hold
  - 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-03 UBS: main, Buy -> Buy
  - 2026-07-20 Citigroup: main, Neutral -> Neutral
  - 2026-07-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-07-16 B of A Securities: main, Buy -> Buy
Institutional ownership: 75.6%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 230,236 shares in 19
Net: -93,626 shares (-0.9% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
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

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.45

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators show bearish momentum (price below 20‑day, 50‑day, and 200‑day SMAs; RSI 43; MACD histogram negative) and thin volume, while fundamentals indicate modest overvaluation (trailing P/E 21.7, PEG 3.79) and weak earnings growth (YoY earnings down 15.5%). Analyst consensus remains buy with modest upside, and insiders have a small net purchase (+2.4% of holdings), providing limited bullish offset. Overall, the bearish technical and valuation signals outweigh the modest positive analyst and insider cues, leading to a slight sell stance.

**Main reasons it gave:**
- Price below 20‑day, 50‑day, and 200‑day SMAs
- RSI 43 and MACD histogram negative indicating bearish momentum
- Trailing P/E 21.7 and PEG 3.79 suggest overvaluation relative to growth
- YoY earnings decline 15.5% indicating weak earnings growth
- Net insider buying +2.4% of holdings (small bullish offset)

<details><summary><b>News</b> — score +0.00</summary>

- [Procter & Gamble (NYSE:PG) Stock Falls 1.9% - What's Next?](https://www.marketbeat.com/instant-alerts/price-procter-gamble-nyse-pg-stock-falls-19-whats-next-2026-09-30/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  Procter & Gamble (NYSE:PG) Stock Price Down 1.9% - What's Next?
- [Burying power lines could cut wildfire ignition risk by nearly 98%, under a PG&E proposal.](https://www.stocktitan.net/news/PCG/pg-e-files-10-year-electrical-undergrounding-plan-to-deliver-bj97s535w5xe.html)  
  <sub>Stock Titan, 48 minutes ago</sub>  
  Underground lines could mean about 90% fewer outages; PG&E values long-term benefits at $117 billion, and Energy Safety will review the plan.
- [PG Oct 2026 134.000 call (PG261002C00134000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261002C00134000/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest PG Oct 2026 134.000 call (PG261002C00134000) stock quote, history, news and other vital information to help you with your stock trading and...
- [PG Oct 2026 152.500 call (PG261002C00152500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261002C00152500/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest PG Oct 2026 152.500 call (PG261002C00152500) stock quote, history, news and other vital information to help you with your stock trading and...
- [PG Oct 2026 143.000 call (PG261002C00143000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261002C00143000/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest PG Oct 2026 143.000 call (PG261002C00143000) stock quote, history, news and other vital information to help you with your stock trading and...
- [PG Oct 2026 141.000 put (PG261002P00141000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PG261002P00141000/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest PG Oct 2026 141.000 put (PG261002P00141000) stock quote, history, news and other vital information to help you with your stock trading and...
- [Stay informed with the top movers within the dow jones index on Wednesday.](https://www.chartmill.com/news/CVX/Chartmill-55582-Stay-informed-with-the-top-movers-within-the-dow-jones-index-on-Wednesday)  
  <sub>ChartMill, 20 hours ago</sub>  
  Uncover the latest developments among dow jones stocks in today's session. Stay tuned to the dow jones index's top gainers and losers on Wednesday.
- [Uncover the latest developments among dow jones stocks in today's session.](https://www.chartmill.com/news/NVDA/Chartmill-55569-Uncover-the-latest-developments-among-dow-jones-stocks-in-todays-session)  
  <sub>ChartMill, 22 hours ago</sub>  
  Stay updated with the movement of dow jones stocks in today's session. Discover which dow jones stocks are making waves on Wednesday.
- [Procter & Gamble stock costs EUR 128.55 ahead of results](https://www.ad-hoc-news.de/boerse/news/corporate-news/procter-and-gamble-stock-costs-eur-128-55-ahead-of-results/70210471)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  Procter & Gamble reports first-quarter results on October 22, 2026. Procter & Gamble stock costs EUR 128.55 after EUR 128.49, plus 0.05 percent.
- [U.S. Analyst Updates: September 30th, 2026](https://www.theglobeandmail.com/investing/markets/stocks/PG/pressreleases/4888455/us-analyst-updates-september-30th-2026/)  
  <sub>The Globe and Mail, 19 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 143.72 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 146.18 (-1.7%), 50d 145.77 (-1.4%), 200d 147.65 (-2.7%); 50d below 200d
Momentum: RSI(14) 43.0 | MACD 0.129 vs signal 0.299 (histogram -0.171)
Returns: 1d -1.1% | 5d -1.3% | 1m -1.7% | 3m -5.1%
52-week range: 138.04 - 167.20 (now 19.5% of the way up)
Volatility: ATR(14) 2.43 (1.7% of price) | annualised 20d 16.9%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 333.81B
Valuation: trailing P/E 21.71 | forward P/E 19.42 | P/B 6.26 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.0% of float
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
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+11.8% vs last close), range 143.00 - 186.00
Recent rating changes:
  - 2026-09-30 TD Cowen: reit, Hold -> Hold
  - 2026-08-07 Argus Research: down, Buy -> Hold
  - 2026-07-30 HSBC: down, Buy -> Hold
  - 2026-07-30 Citigroup: main, Buy -> Buy
  - 2026-07-21 Barclays: main, Equal-Weight -> Equal-Weight
  - 2026-07-16 JP Morgan: main, Overweight -> Overweight
Institutional ownership: 71.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.6%), State Street Corporation (4.4%), Geode Capital Management, LLC (2.9%), Vanguard Portfolio Management LLC (2.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

```text
Last 180 days: bought 90,364 shares in 25 transaction(s) | sold 40,243 shares in 13
Net: +50,121 shares (+2.4% of insider holdings) | insiders hold 2,115,234 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
  - 2026-08-21 RAMAN SUNDAR G. (Officer): 3,435 shares, 491.27K
  - 2026-08-20 JANZARUK MATTHEW W. (Officer): 156 shares, 22.43K
  - 2026-08-20 SCHULTEN ANDRE (Chief Financial Officer): 5,402 shares, 776.75K
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

_Not available today._

</details>

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: negative sentiment in recent news and a downtrend in technicals offset by strong earnings record and a bullish analyst price target, while fundamentals appear expensive despite solid growth.

**Main reasons it gave:**
- Recent negative sentiment: stock down 3% and overvalued commentary
- Technical downtrend: price below 20‑day, 50‑day, and 200‑day SMAs with low volume
- High valuation (trailing P/E 51.5) despite strong revenue (+15.9%) and earnings (+34.2%) growth
- Four consecutive earnings beats indicating consistent outperformance

<details><summary><b>News</b> — score -0.30</summary>

- [Trading the Move, Not the Narrative: (ESLT) Edition](https://news.stocktradersdaily.com/news_release/150/Trading_the_Move,_Not_the_Narrative:_ESLT_Edition_100126093402_1790861642.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Elbit Systems Ltd. (NASDAQ: ESLT). Weak Near-Term Sentiment Could Challenge Long-Term Strength; No clear price positioning signal...
- [Elbit Systems Ltd (ESLT) Stock Down 3.0% but Still Overvalued -- GF Score: 77/100](https://www.gurufocus.com/news/9104265/elbit-systems-ltd-eslt-stock-down-30-but-still-overvalued-gf-score-77100)  
  <sub>GuruFocus, 17 hours ago</sub>  
  On September 30, 2026, Elbit Systems Ltd (ESLT) shares fell 3.0% to a current price of $682.01. This decline comes amidst a broader context where the stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 685.51 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 722.69 (-5.1%), 50d 756.79 (-9.4%), 200d 772.77 (-11.3%); 50d below 200d
Momentum: RSI(14) 31.3 | MACD -12.417 vs signal -8.584 (histogram -3.833)
Returns: 1d +0.5% | 5d -7.3% | 1m -3.3% | 3m -14.7%
52-week range: 454.95 - 1,014.33 (now 41.2% of the way up)
Volatility: ATR(14) 16.70 (2.4% of price) | annualised 20d 22.4%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.12B
Valuation: trailing P/E 51.54 | forward P/E 37.33 | P/B 7.27 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.9% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+19.1% vs last close), range 518.00 - 960.00
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 82,000 shares in 7 transaction(s) | sold 69,736 shares in 7
Net: +12,264 shares (+0.1% of insider holdings) | insiders hold 19,278,816 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-04-09 DELMAR HAIM DANIEL (Officer): 7,654 shares, 6.79M
  - 2026-04-09 MACHLIS BEZHALEL (Chief Executive Officer): 25,514 shares, 22.64M
  - 2026-04-09 VERED YEHUDA (Officer): 5,953 shares, 5.28M
  - 2026-04-09 KRIL RAN (Officer): 6,803 shares, 6.04M
(5 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [ASML Stock Gains Over 5% — Why Bernstein Thinks ASML Holding Can Keep Climbing After Nearly 140% Run In The Past Year](https://stocktwits.com/news-articles/markets/equity/asml-stock-why-bernstein-sees-more-upside-after-140-percent-rally/cZm11SiR7lF)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Shares of ASML Holding NV (ASML) surged nearly 5.5% on Monday after Bernstein significantly raised its price target on the semiconductor equipment maker.
- [ASML vs. SK Hynix: Which Tech Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/01/asml-vs-sk-hynix-which-tech-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  ASML commands the toolmaking monopoly, while SK Hynix dominates memory, but their valuations and risk profiles diverge sharply.
- [Chip stocks set for $229 billion payday before Nvidia ships a GPU](https://www.thestreet.com/investing/ai-chip-equipment-stocks-asml-amat-lrcx-klac)  
  <sub>TheStreet, 26 minutes ago</sub>  
  Before an AI chip is ever sold, these four semiconductor equipment makers get paid. Explore the stock outlook for ASML, Applied Materials, Lam, and KLA.
- [ASML DCF Analysis: Intrinsic Value $1105 vs Price $1812](https://www.gurufocus.com/news/9105274/asml-dcf-analysis-intrinsic-value-1105-vs-price-1812)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 01, 2026, we conducted a DCF analysis for ASML Holding NV (ASML), a company that has shown remarkable price performance over the past year,...
- [Harvest Announces the Listing of the Harvest All-In-One High Income Shares ETF and Four New Single Stock High Income Shares ETFs](https://www.businesswire.com/news/home/20261001190520/en/Harvest-Announces-the-Listing-of-the-Harvest-All-In-One-High-Income-Shares-ETF-and-Four-New-Single-Stock-High-Income-Shares-ETFs)  
  <sub>Business Wire, 3 hours ago</sub>  
  Harvest ETFs (“Harvest”) is pleased to announce the completion of the initial offering of Class A Units of the following High Income Share ETFs pursuant to...
- [ASML Stocks Slip as High-NA Adoption Extends Into 2030](https://finance.yahoo.com/markets/stocks/articles/asml-stocks-slip-high-na-151211856.html)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  Samsung and SK Hynix target 2028 production, while TSMC plans adoption from 2030.
- [October 2026s Top Growth Stocks To Watch](https://simplywall.st/stocks/us/semiconductors/nasdaq-avgo/broadcom/news/october-2026s-top-growth-stocks-to-watch)  
  <sub>Simply Wall Street, 7 hours ago</sub>  
  Global financial authorities are rolling out new rules to improve transparency in banks and are coordinating stimulus to support growth, which puts well...
- [Not Intel. Not Nvidia. These 2 Chip Stocks Maintain an Unbreachable Moat in Advanced Chip Tech.](https://www.fool.com/investing/2026/10/01/not-intel-not-nvidia-these-2-chip-stocks-hold-an-u/)  
  <sub>The Motley Fool, 2 hours ago</sub>  
  Taiwan Semiconductor Manufacturing and ASML each have their own competitive bulwarks.
- [UBS reaffirms Buy rating for ASML Holding stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/ubs-reaffirms-buy-rating-for-asml-holding-stock/70209779)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  ASML Holding stock costs EUR 1602.70 on October 1, 2026 after EUR 1601.30, plus 0.09 percent. Results follow October 14, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,805.32 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 1,710.63 (+5.5%), 50d 1,720.23 (+4.9%), 200d 1,538.87 (+17.3%); 50d above 200d
Momentum: RSI(14) 59.1 | MACD 21.951 vs signal 3.865 (histogram 18.086)
Returns: 1d -0.4% | 5d +4.8% | 1m +8.4% | 3m +2.0%
52-week range: 936.19 - 1,989.44 (now 82.5% of the way up)
Volatility: ATR(14) 49.52 (2.7% of price) | annualised 20d 41.9%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 693.42B
Valuation: trailing P/E 62.66 | forward P/E 30.69 | P/B 1,552.36 | PEG 1.58
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
Price target: mean 2,101.74 (+16.4% vs last close), range 872.99 - 2,795.45
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

- [LUCK,LINE,CAT,RSG,ITT,ANF,SEIC,PETZ,THC,KIDS | Stock Prices | Quote Comparison](https://ca.finance.yahoo.com/quotes/LUCK,LINE,CAT,RSG,ITT,ANF,SEIC,PETZ,THC,KIDS/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  View and compare LUCK,LINE,CAT,RSG,ITT,ANF,SEIC,PETZ,THC,KIDS on Yahoo Finance.
- [Is Caterpillar Stock Increasing Your Market Risk?](https://www.trefis.com/stock/cat/articles/617146/is-caterpillar-stock-increasing-your-market-risk/2026-09-30)  
  <sub>Trefis, 21 hours ago</sub>  
  Caterpillar (CAT) owners watched the stock rise 2.3% in the last five sessions while the S&P 500 fell 1.2%. If the rest of your money follows the market,...
- [Why Is RCAT Stock Lifting Off Premarket Today?](https://stocktwits.com/news-articles/markets/equity/why-is-rcat-stock-lifting-off-premarket-today/cZKffpLR7do)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Red Cat Holdings (RCAT) stock gained nearly 5% in early premarket trading on Monday after the company unveiled a new small unmanned aircraft system (UAS)...
- [Want Reliable Dividend Income? These 2 Industrial Stocks Deliver.](https://www.fool.com/investing/2026/10/01/want-reliable-dividend-income-these-2-industrial/)  
  <sub>The Motley Fool, 26 minutes ago</sub>  
  Both stocks have increased their dividend by more than 40% in the last five years.
- [Stay informed with the top movers within the dow jones index on Wednesday.](https://www.chartmill.com/news/CVX/Chartmill-55582-Stay-informed-with-the-top-movers-within-the-dow-jones-index-on-Wednesday)  
  <sub>ChartMill, 20 hours ago</sub>  
  Uncover the latest developments among dow jones stocks in today's session. Stay tuned to the dow jones index's top gainers and losers on Wednesday.
- [Caterpillar's $1B Compact Equipment Investment: A Growth Driver?](https://www.zacks.com/stock/news/2998949/caterpillars-1b-compact-equipment-investment-a-growth-driver)  
  <sub>Zacks Investment Research, 1 hour ago</sub>  
  Caterpillar plans a $1 billion facility in Sanford, NC, to boost compact equipment production. CAT expects advanced manufacturing, automation and digital...
- [Caterpillar agrees to buy Fabick dealer and Caterpillar stock has 26 targets](https://www.ad-hoc-news.de/boerse/news/corporate-news/caterpillar-agrees-to-buy-fabick-dealer-and-caterpillar-stock-has-26/70209772)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  Sales rose 24.00 percent to USD 20.50 billion in the second quarter of 2026. Caterpillar stock costs EUR 722.60 on October 1, 2026 after EUR 718.10.
- [CAT Steps Up Acquisitions to Expand Reach and Technology: What Next?](https://www.theglobeandmail.com/investing/markets/stocks/CAT/pressreleases/4884003/cat-steps-up-acquisitions-to-expand-reach-and-technology-what-next/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Caterpillar Inc (CAT-N) from The Globe and Mail including charting and trades.
- [Mobileye Global And 2 AI Driving Stocks To Watch](https://simplywall.st/stocks/us/automobiles/nasdaq-mbly/mobileye-global/news/mobileye-global-and-2-ai-driving-stocks-to-watch)  
  <sub>Simply Wall St, 22 hours ago</sub>  
  Government borrowing costs are at their highest level since before the global financial crisis, which makes long term funding more expensive for traditional...
- [Democrats Block Stock-Trading Bill, Denying the G.O.P. a Pre-Midterm Win](https://www.nytimes.com/2026/09/30/us/politics/democrats-block-stock-trading-bill.html?rref=us)  
  <sub>The New York Times, 21 hours ago</sub>  
  A Republican measure to limit, but not bar, congressional stock trading faltered in the Senate as Democrats thwarted a G.O.P. bid to show progress on an...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 816.39 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 808.53 (+1.0%), 50d 824.23 (-1.0%), 200d 793.77 (+2.9%); 50d above 200d
Momentum: RSI(14) 50.2 | MACD -2.340 vs signal -6.041 (histogram 3.701)
Returns: 1d +0.7% | 5d +1.4% | 1m +4.8% | 3m -15.3%
52-week range: 480.82 - 1,064.90 (now 57.5% of the way up)
Volatility: ATR(14) 21.48 (2.6% of price) | annualised 20d 24.5%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 375.27B
Valuation: trailing P/E 35.20 | forward P/E 25.21 | P/B 19.35 | PEG 1.42
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
Price target: mean 975.61 (+19.5% vs last close), range 575.00 - 1,225.00
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
  - 2026-05-13 JOHNSON DENISE C. (Officer): 6,196 shares, 5.64M
  - 2026-05-13 SCHAUPP WILLIAM E (Officer): 360 shares, 326.16K
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

- [HDB Investor Alert: HDFC Bank Limited Securities Class Action Notice - Contact SueWallSt](https://www.morningstar.com/news/pr-newswire/20261001ny61108/hdb-investor-alert-hdfc-bank-limited-securities-class-action-notice-contact-suewallst)  
  <sub>Morningstar, 36 minutes ago</sub>  
  PR Newswire. NEW YORK, Oct. 1, 2026. Important Notice Regarding Alleged Camouflaged Interest Payment Misrepresentations: a securities class action contends...
- [After 22 years with HDFC Group, Sudhir Kumar Jha retires as HDFC Bank (HDB) General Counsel.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-b18543baa61d.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  HDFC Bank (HDB) said Sudhir Kumar Jha superannuated from his role as Group Head – Legal & Group General Counsel at the close of business on September 30,...
- [HDFC Bank Ltd Stock (HDB) Moved Up by 3.29% on Oct 1: Key Drivers Unveiled](https://www.tradingkey.com/news/market-movers/262196382-market-movers-hdb-20261001)  
  <sub>TradingKey, 29 minutes ago</sub>  
  HDFC Bank ADS rose due to technical buying and emerging market sentiment.Investors are positioning ahead of the mid-October quarterly financial results...
- [HDB Deadline Alert: Levi & Korsinsky Reminds HDFC Bank Limited (HDB) Investors of Securities Class Action Deadline on October 13, 2026](https://www.prnewswire.com/news-releases/hdb-deadline-alert-levi--korsinsky-reminds-hdfc-bank-limited-hdb-investors-of-securities-class-action-deadline-on-october-13-2026-302894663.html)  
  <sub>PR Newswire, 22 hours ago</sub>  
  PRNewswire/ -- Levi & Korsinsky, LLP reminds purchasers of HDFC Bank Limited (NYSE: HDB) securities of a pending securities class action in the United...
- [An ICICI Bank executive receives approval as HDFC Bank (HDB)'s next compliance chief.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-d9de2ac594cb.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  HDFC Bank (HDB) says its board approved V. N. Srivatsan as Chief Compliance Officer for a three-year term beginning on his date of joining; he is proposed...
- [HDB SHAREHOLDER NOTICE: Faruqi & Faruqi, LLP Reminds HDFC Bank Limited Investors of Securities Class Action Lawsuit Deadline on October 12, 2026](https://www.morningstar.com/news/pr-newswire/20261001ny59590/hdb-shareholder-notice-faruqi-faruqi-llp-reminds-hdfc-bank-limited-investors-of-securities-class-action-lawsuit-deadline-on-october-12-2026)  
  <sub>Morningstar, 1 hour ago</sub>  
  HDB SHAREHOLDER NOTICE: Faruqi & Faruqi, LLP Reminds HDFC Bank Limited Investors of Securities Class Action Lawsuit Deadline on October 12, 2026...
- [HDFC Bank Limited (HDB) Investors: Securities Fraud Class](https://www.globenewswire.com/news-release/2026/09/30/3372140/32716/en/hdfc-bank-limited-hdb-investors-securities-fraud-class-action-filed-contact-hagens-berman-before-october-13-2026-lead-plaintiff-deadline.html)  
  <sub>GlobeNewswire, 24 hours ago</sub>  
  Investors who lost money in HDB after its stock plunged due to allegedly misleading financial statements are urged to contact Hagens Berman....
- [HDB Financial Services Share Price Today: 2.66% Decline](https://univest.in/blogs/why-hdb-financial-services-l-share-price-fall-today-2026)  
  <sub>Univest, 6 hours ago</sub>  
  HDB Financial Services Share Price fell 2.66% to Rs 604.5. Review price action, valuation, sector context and peer comparison.
- [$2 billion gone in two days! FIIs accelerate selling as Nifty, Sensex set to fall for 8th week running. Wi](https://m.economictimes.com/markets/stocks/news/2-billion-gone-in-two-days-fiis-accelerate-selling-as-nifty-sensex-set-to-fall-for-8th-week-running-will-they-make-a-comeback/articleshow/134610354.cms)  
  <sub>The Economic Times, 8 hours ago</sub>  
  Foreign institutional investors pulled out over Rs 20000 crore from Indian equities in two trading sessions as the Nifty and Sensex head for an eighth...
- [HDFC Bank Announces Retirement of Long-Serving General Counsel and Names Successor](https://www.tipranks.com/news/company-announcements/hdfc-bank-announces-retirement-of-long-serving-general-counsel-and-names-successor)  
  <sub>TipRanks, 4 hours ago</sub>  
  Hdfc Bank ( ($HDB) ) has issued an announcement. HDFC Bank has announced the superannuation of Sudhir Kumar Jha, Group Head – Legal and Group General...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.87 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 22.79 (+0.3%), 50d 23.16 (-1.2%), 200d 27.13 (-15.7%); 50d below 200d
Momentum: RSI(14) 49.2 | MACD -0.152 vs signal -0.162 (histogram 0.010)
Returns: 1d +2.4% | 5d +0.2% | 1m -0.3% | 3m -11.3%
52-week range: 21.84 - 37.18 (now 6.7% of the way up)
Volatility: ATR(14) 0.57 (2.5% of price) | annualised 20d 36.8%
Volume: 0.69x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 117.54B
Valuation: trailing P/E 15.99 | forward P/E 16.44 | P/B 9.27 | PEG n/a
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
Price target: mean 30.52 (+33.5% vs last close), range 26.10 - 35.00
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

### Eli Lilly (LLY) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [LLY Stock Price and Chart — NYSE:LLY](https://www.tradingview.com/symbols/NYSE-LLY/)  
  <sub>TradingView, 18 hours ago</sub>  
  The current price of LLY is 1,157.08 USD — it has increased by 0.07% in the past 24 hours. Watch Eli Lilly and Company stock price performance more closely on...
- [Eli Lilly (LLY) Stock Stays Undervalued As Its 437% Run Raises Stakes](https://finance.yahoo.com/healthcare/articles/eli-lilly-lly-stock-stays-200926900.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Eli Lilly has become one of the market's most closely watched pharma stocks after a very large multi year run, and the question now is whether the cash it...
- [Lilly's weight-loss pill was linked to lower predicted 10-year risk: 57% for diabetes, 18% for heart disease.](https://www.stocktitan.net/news/LLY/lilly-s-oral-glp-1-foundayo-orforglipron-was-associated-with-r53qd5fkmw4k.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Eli Lilly and Company (LLY) announced analyses linking Foundayo to lower predicted long-term diabetes and cardiovascular risk in adults with obesity or...
- [Foghorn stock down as Lilly exits collaboration (FHTX:NASDAQ)](https://seekingalpha.com/news/4648967-foghorn-plunges-as-lilly-exits-collaboration)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Foghorn Therapeutics (FHTX) stock plunges as Lilly (LLY) ends a 2021 collaboration resulting in nearly a 40% workforce reduction. Read more here.
- [Eli Lilly's Foundayo Shows Major Diabetes Risk Reduction; LLY St](https://www.gurufocus.com/news/9105324/eli-lillys-foundayo-shows-major-diabetes-risk-reduction-lly-stock-modestly-undervalued)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 01, 2026, Eli Lilly and Co (NYSE: LLY) announced that its oral obesity treatment, Foundayo at 17.2 mg, achieved a 57% reduction in the risk of...
- [ABBV Stock Rises 25% in 6 Months: Time to Buy, Hold or Sell?](https://www.theglobeandmail.com/investing/markets/stocks/LLY/pressreleases/4905974/abbv-stock-rises-25-in-6-months-time-to-buy-hold-or-sell/)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [BMO reiterates Eli Lilly stock Outperform on TRIUMPH-2 data By Investing.com](https://uk.investing.com/news/stock-market-news/bmo-reiterates-eli-lilly-stock-outperform-on-triumph2-data-93CH-4891978)  
  <sub>Investing.com UK, 7 minutes ago</sub>  
  Investing.com - BMO Capital reiterated an Outperform rating on Eli Lilly and Company (NYSE:LLY) shares with a $1,400.00 price target.
- [Why Is Eli Lilly (NYSE:LLY) Suddenly a Must-Watch Healthcare Stocks Stock Today?](https://kalkinemedia.com/us/stocks/healthcare/why-is-eli-lilly-nyselly-suddenly-a-must-watch-healthcare-stocks-stock-today)  
  <sub>Kalkine Media, 15 minutes ago</sub>  
  Eli Lilly (NYSE:LLY) enters today's market discussion as sector themes, operations, and broader conditions draw attention.
- [4 Stocks That Could Split Next—and Why Investors Are Watching](https://www.marketbeat.com/articles/4-stocks-that-could-split-nextand-why-investors-are-watching/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  AutoZone, Eli Lilly, Meta Platforms, and Costco all trade at high share prices, making them candidates for stock splits as analysts raise price targets and...
- [Lilly says Foundayo cuts diabetes risk by 57% (LLY:NYSE)](https://seekingalpha.com/news/4648951-lilly-says-foundayo-cuts-diabetes-risk)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Eli Lilly (LLY) says oral obesity drug Foundayo cut type 2 diabetes risk by 57% and predicted cardiovascular disease risk by 18% in a Phase 3 trial.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,148.50 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 1,151.99 (-0.3%), 50d 1,177.62 (-2.5%), 200d 1,073.40 (+7.0%); 50d above 200d
Momentum: RSI(14) 44.6 | MACD -1.583 vs signal -3.943 (histogram 2.360)
Returns: 1d -0.7% | 5d -2.8% | 1m -1.0% | 3m -5.4%
52-week range: 799.57 - 1,280.34 (now 72.6% of the way up)
Volatility: ATR(14) 32.09 (2.8% of price) | annualised 20d 19.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.02T
Valuation: trailing P/E 38.62 | forward P/E 24.26 | P/B 30.22 | PEG 1.14
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
Price target: mean 1,328.83 (+15.7% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - 2026-09-22 TD Cowen: reit, Buy -> Buy
  - 2026-09-18 Guggenheim: main, Buy -> Buy
  - 2026-09-10 HSBC: main, Reduce -> Reduce
  - 2026-08-07 Truist Securities: main, Buy -> Buy
  - 2026-08-06 Wells Fargo: main, Overweight -> Overweight
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 515.97 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 501.46 (+2.9%), 50d 485.07 (+6.4%), 200d 432.63 (+19.3%); 50d above 200d
Momentum: RSI(14) 61.8 | MACD 7.669 vs signal 7.406 (histogram 0.262)
Returns: 1d +0.6% | 5d +3.6% | 1m +3.0% | 3m +32.1%
52-week range: 352.83 - 542.07 (now 86.2% of the way up)
Volatility: ATR(14) 11.68 (2.3% of price) | annualised 20d 24.1%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.83T
Valuation: trailing P/E 28.74 | forward P/E 21.81 | P/B 8.66 | PEG 1.62
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
Price target: mean 578.42 (+12.1% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-30 Piper Sandler: main, Overweight -> Overweight
  - 2026-09-23 Stifel: up, Hold -> Buy
  - 2026-09-22 Oppenheimer: main, Outperform -> Outperform
  - 2026-09-21 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
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
Net: +271,300 shares (+4.2% of insider holdings) | insiders hold 6,682,991 shares
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
- news unavailable: Bright Data unreachable: The read operation timed out

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  521,911.47% · Previous Close 227.21 · Open 229.00 · Bid 227.25 x 2000 · Ask 228.94 x 200 · Day's Range 228.17 - 232.37 · 52 Week Range 164.27 - 236.54 · Volume...
- [NVIDIA Corporation $NVDA Stock Bought by Quent Capital LLC](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-bought-by-quent-capital-llc-2026-10-01/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Quent Capital LLC boosted its position in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 8.1% during the second quarter, according to the...
- [NVDA Stock Rebounds But Remains Below Key Support For Second Session: Retail Sees Massive Upside](https://stocktwits.com/news-articles/markets/equity/nvda-stock-200-dma-rebound-ai-factories-deal/cZ3mgN2RI0Z)  
  <sub>Stocktwits, 12 hours ago</sub>  
  NVDA Stock Rebounds But Remains Below Key Support For Second Session: Retail Sees Massive Upside. NVIDIA announced on Monday that it partnered with Emerald AI...
- [NVIDIA Soars 17% in Three Months: Should Investors Buy the Stock?](https://www.tradingview.com/news/zacks:809c79ed0094b:0-nvidia-soars-17-in-three-months-should-investors-buy-the-stock/)  
  <sub>TradingView, 3 hours ago</sub>  
  NVIDIA Corporation NVDA has delivered a strong performance over the past three months, with shares gaining 17.2%. This compares favorably with the 5.8% rise...
- [The 2 Triggers That Can Help Nvidia Nail a Fresh Stock Milestone](https://www.barrons.com/articles/nvidia-stock-price-record-catalyst-ac00c0d9)  
  <sub>Barron's, 47 minutes ago</sub>  
  Nvidia stock rose 17% in the third quarter but remains below its all-time closing high. Here's why that can change in the fourth quarter.
- [‘Nvidia to Sell Twice as Many Chips as This Next Year’: But Jensen Huang’s Comments Ignore the Market Share Question](https://www.barchart.com/story/news/4906253/nvidia-to-sell-twice-as-many-chips-as-this-next-year-but-jensen-huangs-comments-ignore-the-market-share-question)  
  <sub>Barchart.com, 1 hour ago</sub>  
  Huang said Nvidia will sell double the chips next year, so why is NVDA stock trading 52% below its five-year average forward P/E?
- [Barclays Projects Nvidia's Hyperscaler Revenue Surge, NVDA Shares Eye $275 Target](https://www.gurufocus.com/news/9105637/barclays-projects-nvidias-hyperscaler-revenue-surge-nvda-shares-eye-275-target)  
  <sub>GuruFocus, 1 hour ago</sub>  
  On October 01, 2026, Barclays analyst Tom O'Malley spotlighted Nvidia's (NASDAQ: NVDA) growing dominance in IT capital expenditures among the top five cloud...
- [NVIDIA (NASDAQ:NVDA) Stock Rating Reaffirmed as "Overweight" by Cantor Fitzgerald](https://www.marketbeat.com/instant-alerts/analyst-nvidia-nasdaq-nvda-stock-keeps-overweight-rating-at-cantor-fitzgerald-2026-10-01/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Cantor Fitzgerald reissued an "overweight" rating and set a $350.00 price target on shares of NVIDIA in a report on Thursday.
- [Nvidia Stock Can Top $400 in 5 Years If One Assumption Holds Up](https://finance.yahoo.com/markets/stocks/articles/nvidia-stock-top-400-5-223701566.html)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  Nvidia (NASDAQ:NVDA) closed at around $229 on Monday, Sept. 28, giving the artificial intelligence (AI) chip leader a market cap of about $5.5 trillion.
- [This NVDA Partner’s Stock Jumps 7% — Why UBS Sees 38% Upside For Amkor Technology](https://stocktwits.com/news-articles/markets/equity/this-nvda-partners-stock-jumps-7-percent-why-ubs-sees-38-percent-upside-for-amkor-technology/cZZp2YcR7zI)  
  <sub>Stocktwits, 13 hours ago</sub>  
  This NVDA Partner's Stock Jumps 7% — Why UBS Sees 38% Upside For Amkor Technology · UBS upgraded Amkor to Buy from 'Neutral' and raised its price target. · The...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 230.68 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 223.50 (+3.2%), 50d 217.77 (+5.9%), 200d 200.43 (+15.1%); 50d above 200d
Momentum: RSI(14) 59.9 | MACD 3.055 vs signal 2.452 (histogram 0.603)
Returns: 1d +1.0% | 5d +2.7% | 1m +6.1% | 3m +18.4%
52-week range: 165.17 - 235.74 (now 92.8% of the way up)
Volatility: ATR(14) 5.78 (2.5% of price) | annualised 20d 25.0%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.57T
Valuation: trailing P/E 29.20 | forward P/E 14.70 | P/B 24.33 | PEG 0.48
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
Price target: mean 327.70 (+42.1% vs last close), range 180.00 - 515.00
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
  <sub>Stocktwits, 15 hours ago</sub>  
  Novo Nordisk AS (NVO) shares fell more than 14% in Monday's pre-market trade after the company announced headline results from Redefine 4, an open-label phase 3...
- [Wegovy cut average liver fat from 8.8% to 3.1% in 55 adults with excess liver fat over 72 weeks.](https://www.stocktitan.net/news/NVO/novo-s-wegovy-semaglutide-reduced-liver-fat-to-normal-levels-in-9-m8yn0rbpryzt.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Novo Nordisk (NVO) presented an exploratory STEP UP analysis showing Wegovy reduced liver fat in adults with obesity without diabetes. In a 55-participant...
- [NVO DCF Analysis: Intrinsic Value $95 vs Price $38](https://www.gurufocus.com/news/9105278/nvo-dcf-analysis-intrinsic-value-95-vs-price-38)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On October 01, 2026, we delve into the DCF analysis for Novo Nordisk AS (NVO), a company currently facing significant price performance challenges,...
- [Regeneron drug said to cut muscle loss when combined with Novo's semaglutide (REGN:NASDAQ)](https://seekingalpha.com/news/4648838-regeneron-drug-said-to-cut-muscle-loss-when-combined-with-novos-semaglutide)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  An experimental weight-loss drug being developed by Regeneron (REGN) used in combination with Novo Nordisk's (NVO) semaglutide reduced the loss of muscle...
- [NVO Oct 2026 39.500 call (NVO261002C00039500) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/NVO261002C00039500/)  
  <sub>Yahoo Finance Singapore, 17 hours ago</sub>  
  Find the latest NVO Oct 2026 39.500 call (NVO261002C00039500) stock quote, history, news and other vital information to help you with your stock trading and...
- [Viking Therapeutics Stock Soars 36% on Weight-Loss Drug Data. Why It's Not Too Late to Buy the Stock.](https://www.theglobeandmail.com/investing/markets/stocks/NVO/pressreleases/4890583/viking-therapeutics-stock-soars-36-on-weight-loss-drug-data-why-its-not-too-late-to-buy-the-stock/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [PENN Stock Slips Overnight After Year's High: CEO Says Employment Matters More Than Gas Prices For Casino Visits](https://stocktwits.com/news-articles/markets/equity/penn-stock-slips-overnight-after-year-s-high-ceo-says-employment-matters-more-than-gas-prices-for-casino-visits/cZBWFQdReTJ)  
  <sub>Stocktwits, 8 hours ago</sub>  
  In the first-quarter earnings call, Snowden said higher fuel costs could add slight pressure but are not expected to change how often customers visit.
- [10 Health Care Stocks With Whale Alerts In Today’s Session](https://www.benzinga.com/markets/options/26/09/62087808/10-health-care-stocks-whale-alerts-today-s-session)  
  <sub>Benzinga, 21 hours ago</sub>  
  This whale alert can help traders discover the next big trading opportunities. Whales are entities with large sums of money and we track their transactions...
- [NVO261016P00047000 Interactive Stock Chart | NVO Oct 2026 47.000 put Stock](https://finance.yahoo.com/chart/NVO261016P00047000)  
  <sub>Yahoo Finance, 24 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Zacks Investment Research](https://www.globes.co.il/en/zarticle.aspx?id=2998472)  
  <sub>גלובס, 18 hours ago</sub>  
  Novo's real-world study finds that patients who increase their Ozempic to 2 mg have a lower observed MACE risk than those who switch to Mounjaro. Novo NVO...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 37.61 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 41.62 (-9.6%), 50d 44.90 (-16.2%), 200d 45.72 (-17.7%); 50d below 200d
Momentum: RSI(14) 27.7 | MACD -2.165 vs signal -1.874 (histogram -0.291)
Returns: 1d -0.8% | 5d -2.6% | 1m -16.6% | 3m -25.4%
52-week range: 35.29 - 63.98 (now 8.1% of the way up)
Volatility: ATR(14) 1.11 (2.9% of price) | annualised 20d 36.6%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 166.07B
Valuation: trailing P/E 9.40 | forward P/E 11.21 | P/B 4.95 | PEG 4.32
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
Price target: mean 45.97 (+22.2% vs last close), range 39.33 - 62.23
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

### Teva Pharmaceutical (TEVA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Branded Medicines and Pipeline Successes Drive Teva Pharmaceutical Industries’ (TEVA) Margin Expansion](https://finance.yahoo.com/healthcare/articles/branded-medicines-pipeline-successes-drive-125742069.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  TCW Funds, an investment management firm, published its second-quarter 2026 investor letter for the “TCW Relative Value Mid Cap Fund”.
- [Two potential medicines similar to existing drugs are in Teva's deal, with an option for four more.](https://www.stocktitan.net/news/TEVA/samsung-bioepis-and-teva-expand-strategic-partnership-to-advance-up-8vumwuvv343i.html)  
  <sub>Stock Titan, 6 hours ago</sub>  
  Samsung Bioepis will develop, register and manufacture; Teva will commercialize in the U.S., Europe and Canada, with an option to add territories.
- [Teva Pharmaceutical (NYSE:TEVA) Nears Breakout With Perfect Technical Rating and Bull Flag Setup](https://www.chartmill.com/news/TEVA/Chartmill-55601-Teva-Pharmaceutical-NYSETEVA-Nears-Breakout-With-Perfect-Technical-Rating-and-Bull-Flag-Setup)  
  <sub>ChartMill, 5 hours ago</sub>  
  Technical breakout investing starts with a simple pairing: find stocks that are already technically strong, then wait for a constructive consolidation that...
- [Here Are Thursday’s Top Wall Street Analyst Research Calls: BP, Dollar Tree, Exxon Mobil, Lennar, Occidental Petroleum, Rocket Lab, Teva Pharmaceuticals, United Therapeutics, and More](https://247wallst.com/investing/2026/10/01/here-are-thursdays-top-wall-street-analyst-research-calls-bp-dollar-tree-exxon-mobil-lennar-occidental-petroleum-rocket-lab-teva-pharmaceuticals-united-therapeutics-and-more/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Wall Street analysts reshuffled their bets on energy giants, homebuilders, and emerging space plays on Thursday, and the moves cut in some surprising...
- [TD Cowen initiates Teva Pharma stock with buy rating on pipeline](https://www.investing.com/news/analyst-ratings/td-cowen-initiates-teva-pharma-stock-with-buy-rating-on-pipeline-93CH-4926870)  
  <sub>Investing.com, 4 hours ago</sub>  
  Investing.com - TD Cowen initiated coverage on Teva Pharmaceutical Industries Ltd. (NYSE:TEVA) with a buy rating and set a price target of $55.00,...
- [Teva Pharmaceutical and Samsung Bioepis Forge Global Biosimilar Partnership (TEVA)](https://www.gurufocus.com/news/9105118/teva-pharmaceutical-and-samsung-bioepis-forge-global-biosimilar-partnership-teva)  
  <sub>GuruFocus, 5 hours ago</sub>  
  On October 01, 2026, Teva Pharmaceutical Industries Ltd (NYSE: TEVA) announced a strategic global agreement with Samsung Bioepis Co., Ltd. to develop and...
- [Teva, Samsung Bioepis Partner to Develop and Commercialize Biosimilar Candidates](https://www.marketscreener.com/news/teva-samsung-bioepis-partner-to-develop-and-commercialize-biosimilar-candidates-ce785ad3df8ef527)  
  <sub>marketscreener.com, 5 hours ago</sub>  
  Teva Pharmaceutical Industries has entered into an agreement with Samsung Bioepis for the global licensing, development, and commercialization of up to six...
- [TAPI Appoints Serge Rogasik as Chief Executive Officer](https://www.quiverquant.com/news/TAPI+Appoints+Serge+Rogasik+as+Chief+Executive+Officer)  
  <sub>Quiver Quantitative, 18 hours ago</sub>  
  Serge Rogasik is appointed CEO of TAPI, enhancing its global pharmaceutical operations and capabilities. Quiver AI Summary. TAPI (Technology & API Services)...
- [Teva's Denosumab-Adet (Degevma) Approved as Xgeva Biosimilar](https://www.biopharminternational.com/view/teva-denosumab-adet-degevma-approved-xgeva-biosimilar)  
  <sub>BioPharm International, 22 hours ago</sub>  
  Denosumab-adet now covers all 3 Xgeva indications, widening lower-cost treatment access for cancer patients with bone complications.
- [Samsung Bioepis, Teva expand biosimilar pact to target US and Europe - CHOSUNBIZ](https://biz.chosun.com/en/en-science/2026/10/01/W7QSB7TNHVC6VJPLETCITCL6MM/?outputType=amp)  
  <sub>Chosunbiz, 6 hours ago</sub>  
  Samsung Bioepis said on the 1st that it signed a sales cooperation agreement for biosimilars (copycat biologic drugs) with global pharmaceutical company...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.07 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 38.50 (+1.5%), 50d 36.76 (+6.3%), 200d 33.63 (+16.2%); 50d above 200d
Momentum: RSI(14) 55.0 | MACD 0.808 vs signal 0.871 (histogram -0.062)
Returns: 1d -1.3% | 5d -2.9% | 1m +8.0% | 3m +12.8%
52-week range: 18.95 - 40.22 (now 94.6% of the way up)
Volatility: ATR(14) 1.23 (3.1% of price) | annualised 20d 31.7%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.58B
Valuation: trailing P/E 65.13 | forward P/E 12.83 | P/B 5.87 | PEG n/a
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
Consensus: buy (mean 1.71 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 3 strong buy, 3 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 44.83 (+14.8% vs last close), range 40.00 - 50.00
Recent rating changes:
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
  - 2026-07-28 Piper Sandler: main, Overweight -> Overweight
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
Net: -150,983 shares (-2.3% of insider holdings) | insiders hold 6,514,005 shares
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

- [ExxonMobil (NYSE:XOM) Stock Rating Reaffirmed as "Equal Weight" by Wells Fargo & Company](https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-stock-rating-reaffirmed-as-equal-weight-by-wells-fargo-company-2026-10-01/)  
  <sub>MarketBeat, 2 hours ago</sub>  
  Wells Fargo & Company reissued an "equal weight" rating and issued a $182.00 price target on shares of ExxonMobil in a report on Thursday.
- [XOM Apr 2027 150.000 call (XOM270416C00150000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XOM270416C00150000/)  
  <sub>Yahoo! Finance Canada, 8 hours ago</sub>  
  Find the latest XOM Apr 2027 150.000 call (XOM270416C00150000) stock quote, history, news and other vital information to help you with your stock trading...
- [Costs are pushing 94% of manufacturers to raise prices again in 2027](https://www.stocktitan.net/news/XMTR/access-is-becoming-manufacturing-s-competitive-advantage-according-9xg6g53ourg3.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Xometry (XMTR) released its second annual Manufacturing Outlook report, examining access to resources as a competitive factor for U.S. manufacturers in 2027...
- [Vietnam Crude Deals Might Change The Case For Investing In ExxonMobil Stock](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/vietnam-crude-deals-might-change-the-case-for-investing-in-e)  
  <sub>Simply Wall Street, 11 hours ago</sub>  
  ExxonMobil Holdings recently expanded crude supply agreements in Vietnam, advanced carbon capture projects in Texas, and benefited from tight diesel markets...
- [The Senate Just Voted Down a Ban on Congressional Stock Trading](https://247wallst.com/investing/2026/10/01/the-senate-just-voted-down-a-ban-on-congressional-stock-trading/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Kevin Hern's filing revealed partial sales of DVN and XOM worth up to $250,000, disclosed nearly a month after the trades closed. The Senate's 53 votes fell...
- [Xometry CEO Sells 1,500 Shares Amid a 67% One-Year Return](https://www.fool.com/coverage/filings/2026/09/30/xometry-ceo-sells-1-500-shares-amid-a-67-one-year-return/)  
  <sub>The Motley Fool, 12 hours ago</sub>  
  Sanjeev Singh Sahni, Chief Executive Officer of Xometry, Inc. (XMTR -0.34%), sold 1,500 shares of Class A Common Stock on September 14, 2026, according to a...
- [ExxonMobil Holdings Corp (XOM) Insider Trading Activity | Apple Insider Buys and Sells](https://www.gurufocus.com/stock/XOM/insider?ref=etf-stock)  
  <sub>GuruFocus, 19 hours ago</sub>  
  Find out the latest and most up-to-date insider trades for ExxonMobil Holdings Corp (XOM) at GuruFocus.com.
- [ExxonMobil Holdings Corporation (XOM) Stock Forecasts](https://finance.yahoo.com/research/reports/MS_0P00000220_AnalystReport_1790784705000)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [How Do Oil and Gas Shape ExxonMobil (NYSE:XOM) in the S&P 500?](https://kalkinemedia.com/us/stocks/energy/how-do-oil-and-gas-shape-exxonmobil-nysexom-in-the-sp-500)  
  <sub>Kalkine Media, 1 hour ago</sub>  
  ExxonMobil operates across energy, chemicals and lower-emission technologies, with a major Energy-sector presence within the S&P 500 and global operations.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 163.49 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 162.67 (+0.5%), 50d 160.39 (+1.9%), 200d 148.86 (+9.8%); 50d above 200d
Momentum: RSI(14) 54.0 | MACD 0.571 vs signal 0.817 (histogram -0.246)
Returns: 1d +0.5% | 5d +0.8% | 1m -0.6% | 3m +19.3%
52-week range: 110.64 - 171.47 (now 86.9% of the way up)
Volatility: ATR(14) 3.54 (2.2% of price) | annualised 20d 24.9%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 672.24B
Valuation: trailing P/E 21.07 | forward P/E 14.50 | P/B 2.59 | PEG 1.38
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
Price target: mean 173.05 (+5.8% vs last close), range 142.00 - 200.00
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
- Technical: price below 20‑day (28.65) and 50‑day (28.33) SMAs, RSI 36.9, MACD negative, volume 0.52× 20‑day avg
- Macro: no policy surprise, inflation 3.4% in line with expectations, dollar up 0.47% and yields modestly higher
- Fund flows flat (share count +0.0% week‑over‑week), indicating no net demand
- Fundamentals: 3‑year annualized return +14.2% per year but cash‑heavy composition (46% cash) and yield 3.1% near inflation

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.88 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 28.65 (-2.7%), 50d 28.33 (-1.6%), 200d 27.13 (+2.8%); 50d above 200d
Momentum: RSI(14) 36.9 | MACD -0.094 vs signal 0.024 (histogram -0.118)
Returns: 1d -0.9% | 5d -2.3% | 1m -5.5% | 3m +4.3%
52-week range: 25.44 - 29.49 (now 60.2% of the way up)
Volatility: ATR(14) 0.28 (1.0% of price) | annualised 20d 13.0%
Volume: 0.52x the 20-day average
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
Three-year record: +14.2% a year | beta to the market 0.35
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
Shares outstanding: 27.60M | fund size: 769.49M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, modest inventory builds already priced, mixed technicals, flat fund flows, and no analyst rating bias.

**Main reasons it gave:**
- No macro surprise: yields up modestly, dollar up 0.47% on week
- Energy inventories: crude oil +0.9 mbbl build (bearish but modest)
- EIA price outlook: WTI forecast down 13% over 6 months (bearish but likely priced)
- Technicals mixed: MACD below signal (bearish momentum) and low volume
- Fund flows: share count +0.5% (flat, neutral demand)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.52 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 32.74 (-0.7%), 50d 31.14 (+4.4%), 200d 28.12 (+15.6%); 50d above 200d
Momentum: RSI(14) 54.3 | MACD 0.353 vs signal 0.540 (histogram -0.188)
Returns: 1d +0.6% | 5d -2.0% | 1m +1.8% | 3m +22.4%
52-week range: 22.07 - 33.68 (now 90.0% of the way up)
Volatility: ATR(14) 0.49 (1.5% of price) | annualised 20d 19.1%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +13.5% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.80B
What it is made of: Other 50.6%, Cash 44.8%, Bonds 2.7%, Stocks 1.9%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.8%, Brent Crude Future Nov 26 8.9%, Invesco Short Term Treasury ETF 6.2%, Mini Ibovespa Future Dec 26 1.9%
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
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Crude oil: 427.3 million barrels, +0.9 on the week (a build), 62% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
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
Share count change: 1 week: +0.5% (8.84M) over 7d
Shares outstanding: 55.41M | fund size: 1.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: rising Treasury yields pressure high‑yield bonds, but HYG is at a 52‑week low with oversold RSI, and modest net inflows suggest some demand. No policy surprise or decisive technical breakout.

**Main reasons it gave:**
- 10‑year Treasury yield rose 15 bps this week to 5.31%, indicating higher rates
- HYG price at 52‑week low (76.53) below 20‑day SMA (78.31) and RSI 15.1 (oversold)
- Share count increased 1.8% over the week, indicating net inflows
- No major policy surprise; Fed target unchanged at 4.00% and inflation data in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [Eyeing This Bond ETF Amid Treasury Selloff](https://pro.thestreet.com/trade-ideas/eyeing-this-bond-etf-amid-treasury-selloff)  
  <sub>TheStreet Pro, 2 hours ago</sub>  
  As PCE and GDP show inflation easing, a reversal in the bond selloff could be next.
- [Treasury Yields Haven’t Been This High Since 2007—3 ETFs to Watch](https://www.marketbeat.com/articles/treasury-yields-havent-been-this-high-since-20073-etfs-to-watch/)  
  <sub>MarketBeat, 23 hours ago</sub>  
  The 10-year Treasury yield topped 5.25%, its highest since 2007, prompting a look at TLT, HYG, and SHYG as bond ETFs offering different duration and...
- [U.S. 10-year Treasury yield is on pace to finish higher for an eighth straight week](https://seekingalpha.com/news/4649051-us-10-year-treasury-yield-has-climbed-to-531-a-24-year-high)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  10-year Treasury yield hits 2002 highs after 8 straight weekly rises.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 76.53 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 78.31 (-2.3%), 50d 79.04 (-3.2%), 200d 79.90 (-4.2%); 50d below 200d
Momentum: RSI(14) 15.1 | MACD -0.578 vs signal -0.414 (histogram -0.164)
Returns: 1d -0.9% | 5d -1.7% | 1m -3.2% | 3m -4.0%
52-week range: 76.53 - 81.28 (now 0.0% of the way up)
Volatility: ATR(14) 0.33 (0.4% of price) | annualised 20d 4.7%
Volume: 0.67x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: High Yield Bond
Yield: 5.9%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +7.8% a year | beta to the market 0.67
Cost and size: expense ratio 0.49% | net assets 16.19B
What it is made of: Bonds 98.6%, Cash 1.2%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.3%
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

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.8% (277.35M) over 7d
Shares outstanding: 209.51M | fund size: 16.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals lack decisive break, and fundamentals are moderate.

**Main reasons it gave:**
- Analyst coverage thin (1.7% of fund) but 100% buy rating
- CFTC shows net short 26% in Russell E‑Mini, short position fell 6.4% week‑over‑week
- RSI 27.8 signals oversold yet volume at 0.46× 20‑day average (low)
- US Treasury yields rose (10‑yr +15 bps) and VIX up to 17.13 (moderate volatility)
- Fund fundamentals moderate (P/E 17.3, yield 0.9%) with no clear catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Should iShares Russell 2000 ETF (IWM) Be on Your Investing Radar?](https://ca.finance.yahoo.com/news/ishares-russell-2000-etf-iwm-092002046.html)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Designed to provide broad exposure to the Small Cap Blend segment of the US equity market, the iShares Russell 2000 ETF (IWM) is a passively managed...
- [Nasdaq 100 Climbs as Cooler PCE Cuts Rate Hike Bets, Micron Earnings Loom: Stock Market Today](https://www.tradingview.com/news/benzinga:89ded3b78094b:0-nasdaq-100-climbs-as-cooler-pce-cuts-rate-hike-bets-micron-earnings-loom-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks are higher at midday Wednesday, led by technology and software shares, after softer-than-expected inflation data eased fears of another Federal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 276.36 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 285.56 (-3.2%), 50d 292.73 (-5.6%), 200d 276.16 (+0.1%); 50d above 200d
Momentum: RSI(14) 27.8 | MACD -4.440 vs signal -3.767 (histogram -0.673)
Returns: 1d -0.6% | 5d -1.9% | 1m -4.9% | 3m -7.1%
52-week range: 229.11 - 305.09 (now 62.2% of the way up)
Volatility: ATR(14) 3.40 (1.2% of price) | annualised 20d 10.6%
Volume: 0.46x the 20-day average
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
Three-year record: +17.7% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%, Other 0.1%
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.59 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.9% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-30 Wells Fargo: main, Equal-Weight -> Equal-Weight
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
Shares outstanding: 281.05M | fund size: 77.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund faces mixed signals: rising Treasury yields and a downtrend in price suggest bearish pressure, while recent inflows (+2.5% share count) indicate demand. No policy surprise or decisive technical breakout occurred, so the overall view remains neutral.

**Main reasons it gave:**
- 10-year Treasury yield rose 15 bps this week, hitting 2002 highs
- LQD price below 20‑day, 50‑day and 200‑day SMAs with RSI 21.2, indicating a downtrend
- Share count increased 2.5% over the past week, indicating net inflows

<details><summary><b>News</b> — score +0.00</summary>

- [U.S. 10-year Treasury yield is on pace to finish higher for an eighth straight week](https://seekingalpha.com/news/4649051-us-10-year-treasury-yield-has-climbed-to-531-a-24-year-high)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  10-year Treasury yield hits 2002 highs after 8 straight weekly rises.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 101.46 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 104.11 (-2.5%), 50d 105.40 (-3.7%), 200d 108.45 (-6.4%); 50d below 200d
Momentum: RSI(14) 21.2 | MACD -0.987 vs signal -0.730 (histogram -0.257)
Returns: 1d -0.7% | 5d -1.6% | 1m -3.6% | 3m -6.6%
52-week range: 101.46 - 112.92 (now 0.0% of the way up)
Volatility: ATR(14) 0.63 (0.6% of price) | annualised 20d 7.2%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.5% (788.62M) over 7d
Shares outstanding: 312.84M | fund size: 31.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral outlook as macro data shows modest easing in inflation and stable short‑term yields, but positioning indicates a net short bias among large speculators and the fund trades near its 52‑week low with oversold momentum. No clear catalyst or decisive technical break justifies a directional tilt.

**Main reasons it gave:**
- Large speculators net short 29.8% of 2‑year note, indicating bearish sentiment for short‑term Treasuries
- 3‑month Treasury yield down 6 bps this week, supporting bond prices
- Fund price at 52‑week low (81.02) with RSI 31.8 (oversold) but no decisive technical breakout
- Fund yield 3.6% lower than current 3‑month yield (4.01%), reducing relative attractiveness

<details><summary><b>News</b> — score +0.00</summary>

- [UK's Nest pension picks Wellington in £3.5 billion emerging market active equity shift](https://finance.yahoo.com/markets/stocks/articles/uks-nest-pension-picks-wellington-071018882.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  By Simon Jessop. LONDON, Oct. 1 (Reuters) - Britain's largest workplace pension scheme Nest has moved its entire £3.5 billion ($4.6 billion) in emerging...
- [U.S. 10-year Treasury yield is on pace to finish higher for an eighth straight week](https://seekingalpha.com/news/4649051-us-10-year-treasury-yield-has-climbed-to-531-a-24-year-high)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  10-year Treasury yield hits 2002 highs after 8 straight weekly rises.
- [Advanced AI-Powered Crypto Investment Research Platform](https://sosovalue.com/assets/etf/us-btc-spot)  
  <sub>SoSoValue, 10 hours ago</sub>  
  Welcome to SoSoValue - free cryptocurrency trading data platform. Dive into real-time prices, ETFs inflow and trends within Web 3.0 by SoSoValue crypto...
- [Inflation Just Got Revised Lower: Economists Say The Fed Won't Be Fooled](https://www.tradingview.com/news/benzinga:180b920be094b:0-inflation-just-got-revised-lower-economists-say-the-fed-won-t-be-fooled/)  
  <sub>TradingView, 21 hours ago</sub>  
  The Federal Reserve's preferred inflation gauge came in below expectations in August. Technical revisions—not easing price pressures—drove the decline.
- [SCHD: Here’s why this dividend ETF is slumping and what next](https://invezz.com/pk/news/2026/10/01/schd-heres-why-this-dividend-etf-is-slumping-and-what-next/)  
  <sub>Invezz, 59 seconds ago</sub>  
  The Schwab US Dividend Equity ETF SCHD has pulled back sharply in the past few weeks, moving from a high of $35 in August to the current $32.5.
- [US PCE inflation rises 3.4% in August, below expectations as economy stays resilient](https://invezz.com/au/news/2026/09/30/us-pce-inflation-rises-34percent-in-august-below-expectations-as-economy-stays-resilient/)  
  <sub>Invezz, 23 hours ago</sub>  
  US consumer inflation rose less than expected in August, offering some relief to markets while keeping price pressures well above the Federal Reserve's 2%...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 81.02 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 81.32 (-0.4%), 50d 81.68 (-0.8%), 200d 82.27 (-1.5%); 50d below 200d
Momentum: RSI(14) 31.8 | MACD -0.179 vs signal -0.174 (histogram -0.005)
Returns: 1d -0.2% | 5d -0.1% | 1m -0.7% | 3m -1.1%
52-week range: 81.02 - 83.18 (now 0.0% of the way up)
Volatility: ATR(14) 0.12 (0.2% of price) | annualised 20d 1.9%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.2%
Three-year record: +3.9% a year | beta to the market 0.22
Cost and size: expense ratio 0.15% | net assets 25.91B
What it is made of: Bonds 99.2%, Cash 0.8%
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 29.8% of open interest (4,539,374 contracts)
Change on the week: -0.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.2% (54.26M) over 7d
Shares outstanding: 319.50M | fund size: 25.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no material macro surprise, technicals lack decisive break, analyst coverage thin, and positioning ambiguous.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 28.7 (oversold) with low volume, no decisive break
- Macro: yields modestly higher, no policy surprise, VIX elevated at 17.13
- Analyst view: thin coverage (11.4% weight) with 65.7% buy rating and +15.1% price target
- Positioning: net long 6% of OI, +1.3% change, crowded long (100th percentile) – ambiguous

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Holcim Ltd Stocks](https://www.tradingview.com/symbols/BMV-HOLN/N/etfs/)  
  <sub>TradingView, 17 hours ago</sub>  
  Explore funds investing in HOLN/N in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [ETFs Investing in BKW AG Stocks](https://www.tradingview.com/symbols/HAN-B9W/etfs/)  
  <sub>TradingView, 20 hours ago</sub>  
  Explore funds investing in B9W in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 85.62 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 89.04 (-3.8%), 50d 90.46 (-5.3%), 200d 87.62 (-2.3%); 50d above 200d
Momentum: RSI(14) 28.7 | MACD -1.051 vs signal -0.765 (histogram -0.286)
Returns: 1d -1.4% | 5d -2.8% | 1m -5.6% | 3m -4.2%
52-week range: 77.90 - 93.19 (now 50.5% of the way up)
Volatility: ATR(14) 0.98 (1.1% of price) | annualised 20d 13.2%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +18.5% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 39.06B
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.1% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 6.0% of open interest (487,063 contracts)
Change on the week: +1.3% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.2% (434.31M) over 7d
Shares outstanding: 443.28M | fund size: 37.96B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show slight downtrend without decisive break, analyst coverage thin (22.2% of fund) with bullish tilt, and positioning modestly net long.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (10-year +0.15% on the week)
- Technical indicators show price below 20‑day and 50‑day SMAs, RSI 40.2, no decisive break
- Analyst coverage thin (22.2% of fund) with all buy and +35% price target
- CFTC positioning net long 4.6% of open interest, weekly increase +1.3% OI

<details><summary><b>News</b> — score +0.00</summary>

- [Frankenstein’s Bull-Bear Market](https://dailyreckoning.com/frankensteins-bull-bear-market/)  
  <sub>The Daily Reckoning, 19 hours ago</sub>  
  The S&P 500 is sitting just below a fresh all-time high. Yet 59% of the companies in the index are down more than 20% from their highs.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 59.00 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 60.14 (-1.9%), 50d 59.90 (-1.5%), 200d 57.92 (+1.9%); 50d above 200d
Momentum: RSI(14) 40.2 | MACD -0.184 vs signal -0.034 (histogram -0.150)
Returns: 1d -0.5% | 5d -1.5% | 1m -2.8% | 3m -0.1%
52-week range: 52.42 - 61.44 (now 72.9% of the way up)
Volatility: ATR(14) 0.60 (1.0% of price) | annualised 20d 14.0%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

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
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.2% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 4.6% of open interest (1,036,240 contracts)
Change on the week: +1.3% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 83.67B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Price-Driven Insight from (EMB) for Rule-Based Strategy](https://news.stocktradersdaily.com/news_release/17/Price-Driven_Insight_from_EMB_for_Rule-Based_Strategy_100126073201_1790854321.html)  
  <sub>Stock Traders Daily, 7 hours ago</sub>  
  Key findings for Ishares J.p. Morgan Usd Emerging Markets Bond Etf (NYSE: EMB). Weak Near-Term Sentiment Could Catalyze Bearish Positioning...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.90 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 92.92 (-3.2%), 50d 94.09 (-4.5%), 200d 95.48 (-5.8%); 50d below 200d
Momentum: RSI(14) 17.8 | MACD -0.976 vs signal -0.684 (histogram -0.292)
Returns: 1d -1.0% | 5d -2.5% | 1m -4.5% | 3m -6.5%
52-week range: 89.90 - 97.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.55 (0.6% of price) | annualised 20d 7.5%
Volume: 0.62x the 20-day average
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
Direction: money coming in (1 week)
Share count change: 1 week: +2.4% (349.06M) over 7d
Shares outstanding: 163.40M | fund size: 14.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Core PCE Inflation Holds at 3%: Why TLT ETF Could Be Bond Market’s Next Big Move - iShares 20+ Year Treas](https://www.benzinga.com/etfs/specialty-etfs/26/09/62085030/cooler-core-pce-strengthens-the-case-for-treasuries-and-for-long-duration-tlt)  
  <sub>Benzinga, 20 hours ago</sub>  
  Cooler-than-expected August PCE inflation boosted Treasuries and TLT, though core inflation held at 3.0%, well above the Fed's 2% target.
- [Cooler Core PCE Strengthens the Case for Treasuries — and for Long-Duration TLT](https://www.tradingview.com/news/benzinga:39c9ca82c094b:0-cooler-core-pce-strengthens-the-case-for-treasuries-and-for-long-duration-tlt/)  
  <sub>TradingView, 23 hours ago</sub>  
  A cooler-than-expected reading on the Federal Reserve's preferred inflation gauge has strengthened the case for Treasury bonds, after August data showed...
- [Moving Averages of the Ivy Portfolio and S&P 500: September 2026](https://www.advisorperspectives.com/dshort/updates/2026/09/30/ivy-portfolio-sp500-moving-averages-september-2026)  
  <sub>Advisor Perspectives, 17 hours ago</sub>  
  Valid until the market close on October 31, 2026 This article provides an update on the monthly moving averages we track for the S&P 500 and the Ivy...
- [#us10yearyieldnears5.3% Community Insights & Market Sentiment | Binance Square](https://www.binance.com/en/square/hashtag/us10yearyieldnears5.3%25)  
  <sub>Binance, 1 hour ago</sub>  
  #US10YearYieldNears5.3% BOND YIELDS AT MULTI-YEAR HIGHS! The US 10-year Treasury yield approaching 5.3% is creating a major talking point across global...
- [Inflation Just Got Revised Lower: Economists Say The Fed Won't Be Fooled](https://www.tradingview.com/news/benzinga:180b920be094b:0-inflation-just-got-revised-lower-economists-say-the-fed-won-t-be-fooled/)  
  <sub>TradingView, 21 hours ago</sub>  
  The Federal Reserve's preferred inflation gauge came in below expectations in August. Technical revisions—not easing price pressures—drove the decline.
- [Market News | Dollar Index Hits 101.81, Its Highest Level Since May 2025](https://www.binance.com/en/square/post/372599103629212)  
  <sub>Binance, 2 hours ago</sub>  
  The US Dollar Index briefly climbed to 101.81, its highest level since May last year.The move reverses the decline that followed Wednesday's...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 88.87 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 90.73 (-2.1%), 50d 92.10 (-3.5%), 200d 94.51 (-6.0%); 50d below 200d
Momentum: RSI(14) 23.7 | MACD -0.866 vs signal -0.723 (histogram -0.143)
Returns: 1d -0.5% | 5d -0.9% | 1m -3.5% | 3m -5.6%
52-week range: 88.87 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.48 (0.5% of price) | annualised 20d 6.3%
Volume: 0.30x the 20-day average
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
Three-year record: +2.9% a year | beta to the market 1.16
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.8% (741.59M) over 7d
Shares outstanding: 467.29M | fund size: 41.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · -1.56% · -5.74% · 10.61% · 7.67% · 9.66% · 38.85% · 723.84%. Key Events. Baseline. Advanced Chart.
- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://au.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance Australia, 14 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · -1.56% · -5.74% · 10.61% · 7.67% · 9.66% · 38.85% · 723.84%. Key events. Baseline. Advanced chart.
- [S&P 500 equal weight index is on track for seventh straight weekly decline](https://seekingalpha.com/news/4649031-sp-500-equal-weight-index-is-on-track-for-seventh-straight-weekly-decline)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Equal-weight S&P 500 (RSP) nears a 7th weekly loss, signaling weakening market breadth vs mega-cap-led gains.
- [Futures Rise, S&P 500 Finds Key Support; Micron Crushes Views](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-micron-rises-earnings-treasury-yields/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones futures: The S&P 500 is trying to bounce off its 50-day line amid high oil prices and Treasury yields. Micron earnings easily beat.
- [IVW: The Great Rotation Fizzled; Growth Looks Attractive For Q4 And 2027 (NYSEARCA:IVW)](https://seekingalpha.com/article/4951167-ivw-the-great-rotation-fizzled-growth-looks-attractive-for-q4-and-2027)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  iShares S&P 500 Growth ETF gets a reiterated Buy rating, as the 'great rotation' turned out to be a short tactical move. Click to read more about IVW.
- [A Case of Bad ‘Breadth’](https://www.stockinvestor.com/a-case-of-bad-breadth/)  
  <sub>Stock Investor, 24 hours ago</sub>  
  The big news in markets of late has been the massive surge in Treasury bond yields. As of this writing, the benchmark 10-year Treasury Note yield is now,
- [Trying to Pick Individual Stocks to Buy Is the Most Pointless Thing Investors Can Do Now](https://www.inkl.com/news/trying-to-pick-individual-stocks-to-buy-is-the-most-pointless-thing-investors-can-do-now)  
  <sub>inkl, 19 hours ago</sub>  
  Stock picking for long-term total returns used to be the investing equivalent of the American Way. Now, drip by drip, stock by stock, and sector by…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 207.60 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 212.92 (-2.5%), 50d 216.68 (-4.2%), 200d 205.65 (+0.9%); 50d above 200d
Momentum: RSI(14) 28.3 | MACD -2.456 vs signal -1.965 (histogram -0.491)
Returns: 1d -0.2% | 5d -1.3% | 1m -4.6% | 3m -3.4%
52-week range: 182.18 - 222.77 (now 62.6% of the way up)
Volatility: ATR(14) 1.82 (0.9% of price) | annualised 20d 8.7%
Volume: 0.67x the 20-day average
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
Three-year record: +15.8% a year | beta to the market 0.83
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
Ratings by weight: buy 67.9% | hold 32.1% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -2.7% above the current prices
Holdings read: MRNA, VEEV, ZBRA, CRL, DASH
Recent rating changes among them:
  - MRNA: 2026-09-30 Citigroup: down, Neutral -> Sell
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.4% (1.39B) over 7d
Shares outstanding: 480.96M | fund size: 99.85B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ZTIP.U ETF Holdings List — TSX:ZTIP.U](https://www.tradingview.com/symbols/TSX-ZTIP.U/holdings/)  
  <sub>TradingView, 19 hours ago</sub>  
  Explore BMO Short-Term US TIPS Index ETF USD holdings with weight, market value, and other helpful data to make more informed decisions for ZTIP.U trading.
- [AI ETFs Explained: What Investors Should Know Before Buying](https://www.investopedia.com/ai-etfs-explained-what-investors-should-know-before-buying-12057291)  
  <sub>Investopedia, 20 hours ago</sub>  
  Artificial intelligence has become one of the most popular investment themes in recent years, leading to a surge in AI-focused ETFs.
- [A 12% Yield From Gold? Here’s How This Monthly Income ETF Does It](https://247wallst.com/investing/etf/2026/10/01/a-12-yield-from-gold-heres-how-this-monthly-income-etf-does-it/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  Gold can diversify stocks and bonds because its returns respond to different economic and monetary drivers, but physical gold itself produces no dividends,...
- [3 ETFs With 50%+ Upside to Buy in October, According to Analysts](https://www.tipranks.com/news/3-etfs-with-50-upside-to-buy-in-october-according-to-analysts)  
  <sub>TipRanks, 4 hours ago</sub>  
  Technology stocks have delivered strong gains this year, but analysts still see room for some ETFs to climb further in October. Three funds — Invesco NASDAQ...
- [Rocket Lab Price Forecast: 2 ETFs to Capture 58% Upside Potential as RKLB Stock Jumps Over 5% Today](https://www.tipranks.com/news/3896871-2)  
  <sub>TipRanks, 3 hours ago</sub>  
  Rocket Lab ($RKLB) stock rose over 5% in Thursday's pre-market trading, putting the space company back in focus for investors. The stock jumped after Rocket...
- [3 Vanguard ETFs with 24%+ Upside to Watch Over VOO](https://www.tipranks.com/news/3-vanguard-etfs-with-24-upside-to-watch-over-voo)  
  <sub>TipRanks, 2 minutes ago</sub>  
  The Vanguard SP 500 ETF ($VOO) remains a popular choice for broad market exposure. However, some investors are looking beyond it for higher return potential...
- [3 ETFs to Buy with At Least 12% Upside Potential, Says the AI Analyst](https://www.tipranks.com/news/3-etfs-to-buy-with-at-least-12-upside-potential-says-the-ai-analyst)  
  <sub>TipRanks, 8 hours ago</sub>  
  TipRanks' ETF AI Analyst sees at least 12% upside potential in SPDR SP 500 ETF Trust ($SPY), iShares MSCI USA Value Factor ETF ($VLUE), and Invesco RAFI...
- [SGX lists Amova Asia Credit Index ETF to deepen Asian fixed income access](https://www.tipranks.com/news/company-announcements/sgx-lists-amova-asia-credit-index-etf-to-deepen-asian-fixed-income-access)  
  <sub>TipRanks, 12 hours ago</sub>  
  Singapore Exchange ( ($SG:S68) ) has issued an update. Singapore Exchange's SGX Stock Exchange has strengthened its fixed income offering with the listing...
- [Trump Election-Security Push Spurs Defense ETF Volatility Potential](https://www.tipranks.com/news/catalyst/trump-election-security-push-spurs-defense-etf-volatility-potential)  
  <sub>TipRanks, 12 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “Exclusive: Hegseth directs Defense Dept. to fight...
- [Want to Play Micron Earnings Without Buying the Stock? This $23B ETF Makes MU Its Largest Holding](https://www.tipranks.com/news/want-to-play-micron-earnings-without-buying-the-stock-this-23b-etf-makes-mu-its-largest-holding)  
  <sub>TipRanks, 20 hours ago</sub>  
  Micron Technology($MU) will report fiscal fourth-quarter earningsafter the market closes on Wednesday. Investors who want exposure to the memory chip ma...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 103.99 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 105.45 (-1.4%), 50d 106.50 (-2.4%), 200d 109.36 (-4.9%); 50d below 200d
Momentum: RSI(14) 25.7 | MACD -0.786 vs signal -0.659 (histogram -0.127)
Returns: 1d -0.1% | 5d -0.3% | 1m -2.6% | 3m -4.0%
52-week range: 103.99 - 112.20 (now 0.0% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 4.7%
Volume: 0.24x the 20-day average
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
Three-year record: +3.5% a year | beta to the market 0.68
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.5% (220.94M) over 7d
Shares outstanding: 144.23M | fund size: 15.00B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Core PCE Inflation Holds at 3%: Why TLT ETF Could Be Bond Market’s Next Big Move - iShares 20+ Year Treas](https://www.benzinga.com/etfs/specialty-etfs/26/09/62085030/cooler-core-pce-strengthens-the-case-for-treasuries-and-for-long-duration-tlt)  
  <sub>Benzinga, 20 hours ago</sub>  
  Cooler-than-expected August PCE inflation boosted Treasuries and TLT, though core inflation held at 3.0%, well above the Fed's 2% target.
- [Safe Haven? No Thanks](https://seekingalpha.com/article/4951215-safe-haven-no-thanks)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  The iShares 20+ Year Treasury Bond ETF is trading at a fresh record low yesterday and is on pace for its eighth straight day of declines.
- [Treasury Yields Haven’t Been This High Since 2007—3 ETFs to Watch](https://www.marketbeat.com/articles/treasury-yields-havent-been-this-high-since-20073-etfs-to-watch/)  
  <sub>MarketBeat, 23 hours ago</sub>  
  The 10-year Treasury yield topped 5.25%, its highest since 2007, prompting a look at TLT, HYG, and SHYG as bond ETFs offering different duration and...
- [Cooler Core PCE Strengthens the Case for Treasuries — and for Long-Duration TLT](https://www.tradingview.com/news/benzinga:39c9ca82c094b:0-cooler-core-pce-strengthens-the-case-for-treasuries-and-for-long-duration-tlt/)  
  <sub>TradingView, 23 hours ago</sub>  
  A cooler-than-expected reading on the Federal Reserve's preferred inflation gauge has strengthened the case for Treasury bonds, after August data showed...
- [Retail investors are aggressively piling into this bold contrarian bet through one ETF.](https://www.marketwatch.com/story/retail-investors-are-aggressively-piling-into-this-bold-contrarian-bet-through-one-etf-da26f208)  
  <sub>MarketWatch, 6 hours ago</sub>  
  After a harrowing third quarter for Treasurys and as the stock market stalls , bond yields at multi-decade highs are attracting retail investors into...
- [Nasdaq, S&P 500, Dow Futures Climb As Trump's $2B Quantum Computing Bet Outweighs Iran Jitters: RKLB, IBM, RGTI, NIO In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-sp500-dow-futures-climb-as-trump-quantum-computing-bet-outweighs-iran-jitters/cZgbH1xRe8r)  
  <sub>Stocktwits, 13 hours ago</sub>  
  The Trump administration said on Friday it would invest $2 billion in quantum computing stocks, with about half earmarked for IBM.
- [US 10-Year Treasury Yield Soars To 24-Year High: Will The Selloff Continue?](https://www.tradingview.com/news/stocktwits:088a2060f094b:0-us-10-year-treasury-yield-soars-to-24-year-high-will-the-selloff-continue/)  
  <sub>TradingView, 9 hours ago</sub>  
  Economist Peter Schiff pointed out in a post on X that rising yields were a sign of how bear markets work. Major market experts predict long-term yields are...
- [Cooler PCE, Hotter Software: Why IGV Is Beating Semiconductor ETFs - iShares Expanded Tech-Software Secto](https://www.benzinga.com/etfs/sector-etfs/26/09/62093511/cooler-than-expected-pce-hotter-software-igv-outpaces-chip-etf-soxx)  
  <sub>Benzinga, 19 hours ago</sub>  
  Cooler-than-expected PCE inflation eased Fed rate fears, lifting software stocks as IGV gained while semiconductor ETF SOXX lagged.
- [QUICK SPARK: 30-Year Treasury Yields Top 5.6%, Hitting 24-Year Highs](https://www.tradingview.com/news/benzinga:35ee1fac1094b:0-quick-spark-30-year-treasury-yields-top-5-6-hitting-24-year-highs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Inflation came in cooler than expected on Wednesday. Long-term U.S. bond yields rose anyway.The 30-year Treasury yield climbed to 5.63%, up 14 basis points...
- [TLT ETF analysis: US Treasury yields and inflows jump](https://invezz.com/pk/news/2026/10/01/tlt-etf-analysis-us-treasury-yields-and-inflows-jump/)  
  <sub>Invezz, 4 minutes ago</sub>  
  The iShares 20+ Year Treasury Bond ETF TLT continues its strong freefall, reaching its lowest level since September 2023 as cracks in the bond market...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.18 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 80.50 (-4.1%), 50d 81.77 (-5.6%), 200d 85.47 (-9.7%); 50d below 200d
Momentum: RSI(14) 22.5 | MACD -1.149 vs signal -0.788 (histogram -0.361)
Returns: 1d -0.8% | 5d -2.8% | 1m -5.7% | 3m -9.7%
52-week range: 77.18 - 92.06 (now 0.0% of the way up)
Volatility: ATR(14) 0.78 (1.0% of price) | annualised 20d 10.5%
Volume: 0.61x the 20-day average
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
Three-year record: +0.0% a year | beta to the market 2.39
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
Shares outstanding: 109.70M | fund size: 8.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.90 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 28.39 (+1.8%), 50d 28.26 (+2.3%), 200d 27.75 (+4.1%); 50d above 200d
Momentum: RSI(14) 76.4 | MACD 0.178 vs signal 0.125 (histogram 0.053)
Returns: 1d +0.4% | 5d +0.7% | 1m +2.4% | 3m +2.0%
52-week range: 26.47 - 28.90 (now 100.0% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 4.6%
Volume: 0.33x the 20-day average
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
Three-year record: +3.6% a year | beta to the market -9.48
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
Share count change: 1 week: -0.8% (-2.54M) over 7d
Shares outstanding: 10.41M | fund size: 300.84M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, bearish technicals, strong analyst coverage and inflows, but no decisive catalyst.

**Main reasons it gave:**
- US Treasury yields rose modestly, no policy surprise
- Price below 20d, 50d, 200d SMAs and negative MACD indicate bearish technicals
- Share count increased 6.8% in one week, indicating inflows
- Analyst coverage of top holdings 100% buy with +43% price target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 83.89 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 92.22 (-9.0%), 50d 92.96 (-9.8%), 200d 92.59 (-9.4%); 50d above 200d
Momentum: RSI(14) 21.7 | MACD -2.248 vs signal -1.202 (histogram -1.046)
Returns: 1d -2.7% | 5d -6.3% | 1m -12.1% | 3m -8.3%
52-week range: 67.55 - 102.94 (now 46.2% of the way up)
Volatility: ATR(14) 1.84 (2.2% of price) | annualised 20d 15.8%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.48 | P/B 1.77 | P/S 1.36 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +29.4% a year | beta to the market 0.50
Cost and size: expense ratio 0.59% | net assets 815.33M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 25.4%, YPF SA ADR 9.5%, Vista Energy SAB de CV ADR 6.2%, Grupo Financiero Galicia SA ADR 5.6%, Banco Macro SA ADR 4.3%
Sector mix: Consumer cyclical 30.4%, Energy 19.4%, Financial services 14.4%, Basic materials 12.0%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +43.0% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, BMA
Recent rating changes among them:
  - MELI: 2026-09-03 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
  - BMA: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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
Direction: money coming in (1 week)
Share count change: 1 week: +6.8% (50.40M) over 7d
Shares outstanding: 9.42M | fund size: 790.00M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view and modest fundamentals offset bearish technicals and flat flows.

**Main reasons it gave:**
- Analyst coverage: 100% buy rating on 37.6% of fund, weighted price target +21.5% above current price
- Technical indicators: price below 20‑day, 50‑day, and 200‑day SMAs; RSI 41.1; MACD negative
- Macro data: 10‑year Treasury yield up 0.15% week, VIX up to 17.13 (elevated volatility)
- Fund flows: share count flat (+0.0% change) over the past week
- Fund basics: P/E 17.89, three‑year return +32.8% per year, expense ratio 0.59%

<details><summary><b>News</b> — score +0.00</summary>

- [Technical Reactions to EIS Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/149/Technical_Reactions_to_EIS_Trends_in_Macro_Strategies_100126070802_1790852882.html)  
  <sub>Stock Traders Daily, 8 hours ago</sub>  
  Key findings for Ishares Msci Israel Etf (NYSE: EIS). Weak Near-Term Sentiment Could Challenge Long-Term Strength; Support is being tested.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 120.42 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 123.85 (-2.8%), 50d 122.55 (-1.7%), 200d 122.51 (-1.7%); 50d above 200d
Momentum: RSI(14) 41.1 | MACD -0.408 vs signal 0.153 (histogram -0.561)
Returns: 1d -0.7% | 5d -1.9% | 1m -0.7% | 3m -0.0%
52-week range: 97.88 - 137.69 (now 56.6% of the way up)
Volatility: ATR(14) 1.70 (1.4% of price) | annualised 20d 18.6%
Volume: 0.67x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +32.8% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.27 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.5% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-10-01 TD Cowen: init, ? -> Buy
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
Shares outstanding: 2.55M | fund size: 307.08M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show mixed short‑term weakness, modest inflows and bullish analyst coverage but limited to <50% of the fund. Overall view remains neutral.

**Main reasons it gave:**
- Fund flows: +2.5% share count increase over 7 days indicating modest inflows
- Analyst view: 90.3% buy rating covering 47.4% of fund, weighted price target +2.3% above current price
- Technicals: price below 20‑day and 50‑day SMA, RSI 40.5, MACD negative, indicating short‑term weakness
- Macro: US Treasury yields rose modestly, no surprise data releases, VIX moderate at 17.13

<details><summary><b>News</b> — score +0.00</summary>

- [Technical Reactions to EPOL Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/15/Technical_Reactions_to_EPOL_Trends_in_Macro_Strategies_100126084002_1790858402.html)  
  <sub>Stock Traders Daily, 7 hours ago</sub>  
  Key findings for Ishares Msci Poland Etf (NASDAQ: EPOL). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias; Support is being tested.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.28 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 44.85 (-3.5%), 50d 44.05 (-1.7%), 200d 39.48 (+9.6%); 50d above 200d
Momentum: RSI(14) 40.5 | MACD 0.032 vs signal 0.260 (histogram -0.228)
Returns: 1d -2.3% | 5d -3.2% | 1m -1.1% | 3m +9.7%
52-week range: 31.78 - 45.76 (now 82.3% of the way up)
Volatility: ATR(14) 0.69 (1.6% of price) | annualised 20d 20.6%
Volume: 0.97x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.47 | P/B 2.00 | P/S 1.36 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +44.0% a year | beta to the market 0.73
Cost and size: expense ratio 0.59% | net assets 848.26M
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: PKO Bank Polski SA 15.4%, Orlen SA 13.8%, Bank Polska Kasa Opieki SA 7.1%, Powszechny Zaklad Ubezpieczen SA 6.4%, KGHM Polska Miedz SA 4.6%
Sector mix: Financial services 46.1%, Energy 14.5%, Consumer cyclical 12.7%, Basic materials 6.8%
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
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.3% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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
Direction: money coming in (1 week)
Share count change: 1 week: +2.5% (19.95M) over 7d
Shares outstanding: 19.05M | fund size: 824.47M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish technicals and analyst rating are offset by modest inflows and solid fundamentals.

**Main reasons it gave:**
- Australian manufacturing PMI fell to 49.6 (contraction)
- Technical indicators: price below 20-day, 50-day, 200-day SMAs and RSI 32.9 (bearish)
- Fund flows: share count rose 1.9% over the week (bullish inflows)
- Analyst coverage: weighted rating 3.43 (slightly bearish)

<details><summary><b>News</b> — score +0.00</summary>

- [Australia posts smallest trade surplus since May as import growth outpaces exports](https://www.tradingview.com/news/seekingalpha:a5dd9d82e094b:0-australia-posts-smallest-trade-surplus-since-may-as-import-growth-outpaces-exports/)  
  <sub>TradingView, 10 hours ago</sub>  
  Australia's trade surplus narrowed to AUD 0.50B in August from a downwardly revised AUD 1.35B in July, falling short of market forecasts for an AUD 2B...
- [Australia's manufacturing PMI contracts to 49.6 in September, sharpest fall in 21 months](https://www.tradingview.com/news/seekingalpha:389a30bd9094b:0-australia-s-manufacturing-pmi-contracts-to-49-6-in-september-sharpest-fall-in-21-months/)  
  <sub>TradingView, 10 hours ago</sub>  
  The S&P Global Australia Manufacturing PMI dropped to 49.6 in September, slightly above the preliminary 49.3 reading but down sharply from 52.0 in August.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 27.82 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 28.96 (-3.9%), 50d 29.44 (-5.5%), 200d 28.62 (-2.8%); 50d above 200d
Momentum: RSI(14) 32.9 | MACD -0.390 vs signal -0.295 (histogram -0.096)
Returns: 1d -1.7% | 5d -1.7% | 1m -6.3% | 3m -1.0%
52-week range: 24.95 - 30.43 (now 52.4% of the way up)
Volatility: ATR(14) 0.38 (1.4% of price) | annualised 20d 18.2%
Volume: 0.32x the 20-day average
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
Three-year record: +13.5% a year | beta to the market 0.96
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

<details><summary><b>What analysts and big funds say</b> — score -0.22</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.22</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.43 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -4.2% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Share count change: 1 week: +1.9% (23.81M) over 7d
Shares outstanding: 46.74M | fund size: 1.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage: 74.3% buy, +8.4% price target for top holdings
- Fund flows: +2.4% share count increase over the week, indicating inflows
- Technical indicators: RSI 29.7 (oversold), price below 20‑day and 50‑day SMAs, low volume
- Macro: yields rising modestly, dollar up, VIX elevated, no surprise data releases
- News article suggests weak near‑term sentiment and potential breakdown (source reliability uncertain)

<details><summary><b>News</b> — score +0.00</summary>

- [(EWC) Movement Within Algorithmic Entry Frameworks](https://news.stocktradersdaily.com/news_release/98/EWC_Movement_Within_Algorithmic_Entry_Frameworks_100126103201_1790865121.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Ishares Msci Canada Etf (NYSE: EWC). Weak Near-Term Sentiment Could Challenge Long-Term Strength; Breakdown is underway.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.90 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 60.16 (-3.8%), 50d 60.69 (-4.6%), 200d 57.70 (+0.4%); 50d above 200d
Momentum: RSI(14) 29.7 | MACD -0.662 vs signal -0.403 (histogram -0.260)
Returns: 1d -0.8% | 5d -2.6% | 1m -4.5% | 3m +0.2%
52-week range: 49.72 - 62.64 (now 63.3% of the way up)
Volatility: ATR(14) 0.66 (1.1% of price) | annualised 20d 13.5%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 19.49 | P/B 2.83 | P/S 2.79 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +23.1% a year | beta to the market 0.79
Cost and size: expense ratio 0.50% | net assets 6.85B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Royal Bank of Canada 9.0%, The Toronto-Dominion Bank 6.3%, Shopify Inc Registered Shs -A- Subord Vtg 5.7%, Bank of Montreal 3.7%, Bank of Nova Scotia 3.6%
Sector mix: Financial services 39.2%, Energy 17.9%, Basic materials 16.1%, Industrials 8.8%
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
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +8.4% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-23 Wedbush: reit, Outperform -> Outperform
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: +2.4% (157.55M) over 7d
Shares outstanding: 116.01M | fund size: 6.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals show downtrend but no decisive break, modest inflows, bullish analyst view not enough to shift stance.

**Main reasons it gave:**
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs, RSI 32.1, no decisive break
- Macro: yields rose modestly, no surprise data or policy shift
- Fund flows: +1.8% share count increase over 7 days indicating modest inflow
- Analyst view: 82% buy rating with +14% price target, but not a macro catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 49.30 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 51.53 (-4.3%), 50d 52.25 (-5.6%), 200d 51.38 (-4.0%); 50d above 200d
Momentum: RSI(14) 32.1 | MACD -0.614 vs signal -0.396 (histogram -0.218)
Returns: 1d -1.4% | 5d -3.5% | 1m -5.9% | 3m -2.3%
52-week range: 45.38 - 54.72 (now 42.0% of the way up)
Volatility: ATR(14) 0.72 (1.5% of price) | annualised 20d 16.2%
Volume: 0.37x the 20-day average
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
Three-year record: +19.2% a year | beta to the market 1.19
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-01 Keybanc: main, Overweight -> Overweight
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
Direction: money coming in (1 week)
Share count change: 1 week: +1.8% (13.01M) over 7d
Shares outstanding: 14.90M | fund size: 734.43M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- 10-year Treasury yield rose 15 bps this week, no surprise
- RSI(14) at 29.5 indicates oversold but MACD remains negative and volume is low
- Analyst coverage of top holdings (45.5% weight) shows 78% buy rating and +18.1% price target
- Fund flows flat over the week, indicating no net inflow or outflow

<details><summary><b>News</b> — score +0.00</summary>

- [Price-Driven Insight from (EWG) for Rule-Based Strategy](https://news.stocktradersdaily.com/news_release/132/Price-Driven_Insight_from_EWG_for_Rule-Based_Strategy_100126103602_1790865362.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Ishares Msci Germany Etf (NYSE: EWG). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach; A mid-channel oscillation pattern...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 40.85 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 42.49 (-3.9%), 50d 43.08 (-5.2%), 200d 42.38 (-3.6%); 50d above 200d
Momentum: RSI(14) 29.5 | MACD -0.512 vs signal -0.356 (histogram -0.156)
Returns: 1d -1.1% | 5d -2.4% | 1m -6.0% | 3m -3.5%
52-week range: 38.08 - 44.59 (now 42.5% of the way up)
Volatility: ATR(14) 0.49 (1.2% of price) | annualised 20d 13.4%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.1% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break on heavy volume, but analyst consensus is strongly bullish (+15.6% price target) and fund flows are positive (+2.3% share count week). Fundamentals are solid but not extraordinary. Overall call remains neutral.

**Main reasons it gave:**
- Fund flows positive: share count up 2.3% week
- Analyst consensus 100% buy with +15.6% price target
- Technicals show price below SMAs and RSI 27.4, but low volume (no decisive break)
- Macro: yields rose modestly, no policy surprise, VIX modestly higher

<details><summary><b>News</b> — score +0.00</summary>

- [Why (EWI) Price Action Is Critical for Tactical Trading](https://news.stocktradersdaily.com/news_release/134/Why_EWI_Price_Action_Is_Critical_for_Tactical_Trading_100126103802_1790865482.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Ishares Msci Italy Etf (NYSE: EWI). Weak Near-Term Sentiment Could Challenge Long-Term Strength; Breakdown is underway.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 57.25 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 60.55 (-5.4%), 50d 61.58 (-7.0%), 200d 57.98 (-1.3%); 50d above 200d
Momentum: RSI(14) 27.4 | MACD -0.818 vs signal -0.527 (histogram -0.291)
Returns: 1d -2.5% | 5d -4.5% | 1m -6.5% | 3m -5.6%
52-week range: 50.31 - 63.35 (now 53.2% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 18.4%
Volume: 0.55x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.25 | P/B 1.85 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +29.4% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.8%, Intesa Sanpaolo 13.6%, Enel SpA 10.3%, Ferrari NV 5.2%, Eni SpA 5.0%
Sector mix: Financial services 52.6%, Utilities 16.3%, Industrials 9.7%, Consumer cyclical 9.0%
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
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, RACE.MI, ENI.MI
Recent rating changes among them:
  - RACE.MI: 2026-09-30 Morgan Stanley: main, Overweight -> Overweight
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
Share count change: 1 week: +2.3% (24.58M) over 7d
Shares outstanding: 18.94M | fund size: 1.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals show no decisive break, positioning and flows offset, analyst view thin.

**Main reasons it gave:**
- US Treasury yields rose modestly across curve, no policy surprise
- EWJ price near 52-week high, MACD histogram negative, volume 0.32x 20-day avg
- CFTC net long down 0.7% week, but fund inflows +1.7% share count
- Analyst coverage thin (17% of fund) despite 100% buy rating

<details><summary><b>News</b> — score +0.00</summary>

- [How (EWJ) Movements Inform Risk Allocation Models](https://news.stocktradersdaily.com/news_release/139/How_EWJ_Movements_Inform_Risk_Allocation_Models_100126104002_1790865602.html)  
  <sub>Stock Traders Daily, 5 hours ago</sub>  
  Key findings for Ishares Msci Japan Etf (NYSE: EWJ). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias; Resistance is being tested.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 96.97 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 97.39 (-0.4%), 50d 95.81 (+1.2%), 200d 90.32 (+7.4%); 50d above 200d
Momentum: RSI(14) 50.7 | MACD 0.300 vs signal 0.456 (histogram -0.157)
Returns: 1d -0.5% | 5d +1.2% | 1m +1.8% | 3m +4.1%
52-week range: 78.36 - 98.78 (now 91.1% of the way up)
Volatility: ATR(14) 1.46 (1.5% of price) | annualised 20d 19.0%
Volume: 0.32x the 20-day average
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
Three-year record: +20.4% a year | beta to the market 0.86
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
Weighted price target: +14.6% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 3.6% of open interest (21,974 contracts)
Change on the week: -0.7% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.7% (376.12M) over 7d
Shares outstanding: 234.61M | fund size: 22.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no clear macro catalyst, technicals show downtrend but no decisive break, analyst view bullish but limited weight, fundamentals mixed, flows flat.

**Main reasons it gave:**
- Analyst view: 74.5% buy, weighted price target +12.3% above current
- Technicals: price 58.80 below 20‑day SMA 60.63, RSI 30.5 (near oversold), volume 0.35× 20‑day avg
- Macro: 10‑yr yield up 15 bps to 5.31%, VIX up 1.5 to 17.13, Fed target 4.00% with market pricing ~4 hikes
- Fund flows: share count flat (+0.0% over 1 week)

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in BKW AG Stocks](https://www.tradingview.com/symbols/HAN-B9W/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in B9W in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.80 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 60.63 (-3.0%), 50d 62.34 (-5.7%), 200d 61.62 (-4.6%); 50d above 200d
Momentum: RSI(14) 30.5 | MACD -0.832 vs signal -0.741 (histogram -0.091)
Returns: 1d -0.6% | 5d -2.7% | 1m -6.0% | 3m -8.1%
52-week range: 55.06 - 65.08 (now 37.3% of the way up)
Volatility: ATR(14) 0.70 (1.2% of price) | annualised 20d 14.1%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +13.4% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.3% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.68B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, flat fund flows, technicals showing short‑term pullback, and analyst coverage bullish but limited to 44% of the fund.

**Main reasons it gave:**
- Fund flows flat: 0% change in share count over the week
- Technicals: price below 20‑day SMA (67.67) and 50‑day SMA (68.19), RSI 41.7, MACD slightly negative
- Macro data: inflation 3.4% and unemployment 4.1% in line with expectations; yields modestly up, VIX modestly higher
- Analyst view: 100% buy rating covering 44% of fund, weighted price target +28.8% above current

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 66.53 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 67.67 (-1.7%), 50d 68.19 (-2.4%), 200d 64.27 (+3.5%); 50d above 200d
Momentum: RSI(14) 41.7 | MACD -0.222 vs signal -0.239 (histogram 0.017)
Returns: 1d -1.8% | 5d -1.4% | 1m -1.2% | 3m -1.5%
52-week range: 55.33 - 71.61 (now 68.8% of the way up)
Volatility: ATR(14) 0.93 (1.4% of price) | annualised 20d 17.3%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +25.3% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.8% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, NBIS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-09-30 William Blair: init, ? -> Outperform
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
Shares outstanding: 5.55M | fund size: 369.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bullish analyst view offset by weak technicals and flat flows, with no macro surprise.

**Main reasons it gave:**
- Analyst view: 52% buy, 48% hold, weighted price target +6.8% above current price
- Technicals: price below 20‑day and 50‑day SMAs, RSI 30.5 (near oversold), MACD negative, volume 0.44x 20‑day average
- Macro: US yields rising (10‑yr +0.15% week), VIX elevated at 17.13, no major data surprise
- Fund flows: flat share count (+0.0% over 1 week) indicating neutral positioning

<details><summary><b>News</b> — score +0.00</summary>

- [(EWP) as a Liquidity Pulse for Institutional Tactics](https://news.stocktradersdaily.com/news_release/8/EWP_as_a_Liquidity_Pulse_for_Institutional_Tactics_100126105201_1790866321.html)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Key findings for Ishares Msci Spain Etf (NYSE: EWP). Weak Near-Term Sentiment Could Challenge Long-Term Strength; Breakdown is underway.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 57.81 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 61.04 (-5.3%), 50d 61.59 (-6.1%), 200d 57.57 (+0.4%); 50d above 200d
Momentum: RSI(14) 30.5 | MACD -0.656 vs signal -0.335 (histogram -0.321)
Returns: 1d -2.3% | 5d -4.9% | 1m -6.1% | 3m -3.1%
52-week range: 48.33 - 63.23 (now 63.6% of the way up)
Volatility: ATR(14) 0.89 (1.5% of price) | annualised 20d 18.8%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.28 | P/B 2.22 | P/S 1.82 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +34.1% a year | beta to the market 0.87
Cost and size: expense ratio 0.50% | net assets 2.26B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.0%, Iberdrola SA 12.1%, CaixaBank SA 4.6%, Industria De Diseno Textil SA Share From Split 4.4%
Sector mix: Financial services 45.4%, Utilities 20.0%, Industrials 14.4%, Technology 5.9%
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
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.8% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals are weak but not decisive, analyst coverage is bullish, and fund inflows are modest.

**Main reasons it gave:**
- Analyst coverage of top holdings shows 69.5% buy and a +15.6% price target
- Fund flows show a 1.5% share count increase over the week, indicating net inflows
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs with negative momentum
- Macro data shows no surprise; yields rising modestly and VIX elevated but stable

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 45.73 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 47.53 (-3.8%), 50d 48.00 (-4.7%), 200d 46.66 (-2.0%); 50d above 200d
Momentum: RSI(14) 28.1 | MACD -0.435 vs signal -0.262 (histogram -0.173)
Returns: 1d -1.7% | 5d -3.0% | 1m -5.1% | 3m -3.0%
52-week range: 41.34 - 49.39 (now 54.5% of the way up)
Volatility: ATR(14) 0.50 (1.1% of price) | annualised 20d 12.8%
Volume: 0.58x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.08 | P/B 2.29 | P/S 1.52 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +18.5% a year | beta to the market 0.68
Cost and size: expense ratio 0.50% | net assets 3.79B
What it is made of: Stocks 97.9%, Other 1.1%, Cash 0.9%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 7.8%, AstraZeneca PLC 7.6%, Rolls-Royce Holdings PLC 5.3%, Unilever PLC 4.3%
Sector mix: Financial services 26.4%, Consumer defensive 14.3%, Industrials 13.9%, Healthcare 12.7%
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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 69.5% | hold 30.5% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.6% above the current prices
Holdings read: HSBA.L, SHEL.L, AZN.L, RR.L, ULVR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +1.5% (52.91M) over 7d
Shares outstanding: 80.66M | fund size: 3.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage and fundamentals, neutral flows, and bearish technicals lead to a neutral stance.

**Main reasons it gave:**
- Analyst coverage of top holdings is 100% buy with a weighted price target +20.2% above current price
- Fund flows are flat over the past week, indicating no net demand
- Technicals show price below 20‑day, 50‑day and 200‑day SMAs, RSI 28.6 (oversold) but negative momentum (MACD down)
- Macro backdrop: upward‑sloping yield curve, dollar index up, VIX moderate, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 69.57 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 73.96 (-5.9%), 50d 75.39 (-7.7%), 200d 75.79 (-8.2%); 50d below 200d
Momentum: RSI(14) 28.6 | MACD -1.282 vs signal -0.890 (histogram -0.392)
Returns: 1d -2.1% | 5d -4.1% | 1m -8.0% | 3m -7.9%
52-week range: 64.39 - 81.23 (now 30.8% of the way up)
Volatility: ATR(14) 1.33 (1.9% of price) | annualised 20d 17.7%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.68 | P/B 1.98 | P/S 1.49 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +11.2% a year | beta to the market 1.05
Cost and size: expense ratio 0.50% | net assets 1.82B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Grupo Mexico SAB de CV Class B 16.6%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.3%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Cemex SAB de CV 4.4%
Sector mix: Basic materials 27.3%, Consumer defensive 24.4%, Financial services 19.7%, Industrials 11.7%
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
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.2% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.31B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, technicals lack a decisive breakout, and fundamentals are stable. Modest inflows provide a slight positive tilt but are not enough to shift direction.

**Main reasons it gave:**
- Modest net inflow (+3.7% share count increase) indicates demand but not decisive
- Technicals: price above 50‑day and 200‑day SMAs, but RSI neutral (50.8) and MACD histogram negative, no clear breakout
- Macro: yields rose modestly (10‑year +0.15% on week) and no surprise data, maintaining upward‑sloping curve
- Fundamentals: low P/E 10.41 and stable composition, no new catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [KORU: The Victim Of South Korea’s Semiconductor Bottleneck (NYSEARCA:KORU)](https://seekingalpha.com/article/4951279-koru-the-victim-of-south-koreas-semiconductor-bottleneck)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  The Direxion Daily MSCI South Korea Bull 3X ETF is ultra-volatile, semiconductor-concentrated, and prone to decay and drawdowns. Learn more about KORU ETF...
- [(EWY) Movement as an Input in Quant Signal Sets](https://news.stocktradersdaily.com/news_release/17/EWY_Movement_as_an_Input_in_Quant_Signal_Sets_100126110802_1790867282.html)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Key findings for Ishares Msci South Korea Etf (NYSE: EWY). Neutral Near and Mid-Term Readings Could Moderate Long-Term Positive Bias...
- [Best Performing ETFs of 2026 So Far](https://www.etf.com/sections/features/best-performing-etfs-2026-so-far)  
  <sub>ETF.com, 19 hours ago</sub>  
  Tanker freight, oil and a privacy coin have joined the chip funds at the top of the leaderboard.
- [Trump touts $200B South Korean investment for Texas power, nuclear, and Alaska LNG](https://seekingalpha.com/news/4648820-trump-touts-200b-south-korean-investment-for-texas-power-nuclear-and-alaska-lng)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Trump unveils South Korea's $200B U.S. energy investment plan: Texas power, nuclear reactors & Alaska LNG.
- [South Korea thought it beat Elliott: Samsung merger case returns with $48.5M bill](https://invezz.com/au/news/2026/10/01/south-korea-thought-it-beat-elliott-samsung-merger-case-returns-with-dollar485m-bill/)  
  <sub>Invezz, 9 hours ago</sub>  
  South Korea is facing a multimillion-dollar bill over the 2015 Samsung merger, only seven months after a UK court victory appeared to remove the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 183.26 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 184.37 (-0.6%), 50d 176.23 (+4.0%), 200d 155.73 (+17.7%); 50d above 200d
Momentum: RSI(14) 50.8 | MACD 1.692 vs signal 2.123 (histogram -0.431)
Returns: 1d +0.3% | 5d +0.4% | 1m +4.2% | 3m +1.7%
52-week range: 80.72 - 219.20 (now 74.0% of the way up)
Volatility: ATR(14) 5.98 (3.3% of price) | annualised 20d 47.1%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +50.6% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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
Rolled up from the 5 largest holdings, 53.5% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: 000660.KQ, 005930.KQ, 402340.KQ, 009150.KQ, 105560.KQ
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.35</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +3.7% (991.32M) over 7d
Shares outstanding: 151.49M | fund size: 27.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals, modest fundamentals, analyst coverage limited to 40.9% but bullish.

**Main reasons it gave:**
- Flat fund flows (0% change) – no new inflows/outflows
- Technical momentum neutral: RSI 47.7, MACD histogram -0.211
- Macro environment unchanged: yields up modestly, no policy surprise
- Analyst coverage 40.9% of fund, all buy with +30% price target
- Fundamentals modestly positive: low P/E 10.48, 4.1% yield

<details><summary><b>News</b> — score +0.00</summary>

- [Behavioral Patterns of EWZ and Institutional Flows](https://news.stocktradersdaily.com/news_release/20/Behavioral_Patterns_of_EWZ_and_Institutional_Flows_100126111002_1790867402.html)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Key findings for Ishares Msci Brazil Etf (NYSE: EWZ). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook; A mid-channel oscillation...
- [Frankenstein’s Bull-Bear Market](https://dailyreckoning.com/frankensteins-bull-bear-market/)  
  <sub>The Daily Reckoning, 19 hours ago</sub>  
  The S&P 500 is sitting just below a fresh all-time high. Yet 59% of the companies in the index are down more than 20% from their highs.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 36.67 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 37.58 (-2.4%), 50d 36.29 (+1.0%), 200d 36.35 (+0.9%); 50d below 200d
Momentum: RSI(14) 47.7 | MACD 0.119 vs signal 0.330 (histogram -0.211)
Returns: 1d -1.6% | 5d -0.7% | 1m +0.3% | 3m +6.5%
52-week range: 28.79 - 41.73 (now 60.9% of the way up)
Volatility: ATR(14) 0.78 (2.1% of price) | annualised 20d 20.3%
Volume: 0.45x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.8% above the current prices
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
Shares outstanding: 200.55M | fund size: 7.35B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish technicals, bullish analyst view and fundamentals, flat flows, no macro surprise.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs (68.00, 67.74, 69.17) – bearish
- RSI 31.4 indicating near‑oversold conditions
- Analyst coverage 45.6% of fund, 100% buy, weighted price target +32.3% – bullish
- Fund fundamentals: low P/E 9.31 and high yield 7.1% – attractive
- Fund flows flat over past week – neutral

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 62.69 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 68.00 (-7.8%), 50d 67.74 (-7.5%), 200d 69.17 (-9.4%); 50d below 200d
Momentum: RSI(14) 31.4 | MACD -1.314 vs signal -0.608 (histogram -0.705)
Returns: 1d -2.0% | 5d -4.9% | 1m -9.9% | 3m -2.0%
52-week range: 60.43 - 81.60 (now 10.7% of the way up)
Volatility: ATR(14) 1.33 (2.1% of price) | annualised 20d 27.0%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 9.31 | P/B 2.24 | P/S 1.92 | 3y earnings growth n/a
Yield: 7.1%
Three-year record: +26.7% a year | beta to the market 1.02
Cost and size: expense ratio 0.59% | net assets 578.49M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 13.7%, Gold Fields Ltd 9.9%, Naspers Ltd Class N 8.8%, Firstrand Ltd 7.1%, Standard Bank Group Ltd 6.1%
Sector mix: Basic materials 41.0%, Financial services 33.2%, Consumer cyclical 12.8%, Communication services 6.2%
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
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.98 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.3% above the current prices
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
Shares outstanding: 7.90M | fund size: 495.25M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise or decisive technical break; bullish analyst view and strong fund inflows are offset by weak price momentum and a stalled gold price.

**Main reasons it gave:**
- Gold price stalls near $4,160 despite $3.8B ETF inflows
- GDX price below 20‑day, 50‑day, and 200‑day SMAs; RSI 39.1 (weak momentum)
- Share count up 7.2% in one week, indicating strong inflows
- Analyst coverage 100% buy with +21% price target for top holdings

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners Equity ETF (GDX) Stock Price | Quotes & News](https://www.moomoo.com/stock/GDX-US?chain_id=Name1K9-3FXPhg.1lbs4o0&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A108%2C%22f%22%3A%22www.moomoo.com%2Fcrypto%2FETH-CC%2Fcommunity%22%7D)  
  <sub>Moomoo, 6 hours ago</sub>  
  Track the latest VanEck Gold Miners Equity ETF (GDX) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF trading and...
- [Gold prices stall near $4,160 despite $3.8 billion ETF inflows: here’s why](https://invezz.com/sg/news/2026/10/01/gold-prices-stall-near-dollar4160-despite-dollar38-billion-etf-inflows-heres-why/)  
  <sub>Invezz, 9 hours ago</sub>  
  Gold prices steadied near $4,160 an ounce even as billions of dollars continued flowing into bullion-backed exchange-traded funds, exposing a divide between...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 87.00 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 94.35 (-7.8%), 50d 91.19 (-4.6%), 200d 91.08 (-4.5%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -1.352 vs signal -0.017 (histogram -1.335)
Returns: 1d -0.9% | 5d -5.8% | 1m -8.1% | 3m +10.9%
52-week range: 68.28 - 115.84 (now 39.4% of the way up)
Volatility: ATR(14) 3.11 (3.6% of price) | annualised 20d 40.1%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.84 | P/B 2.68 | P/S 4.10 | 3y earnings growth n/a
Yield: 0.6%
Three-year record: +50.8% a year | beta to the market 0.83
Cost and size: expense ratio 0.51% | net assets 30.54B
What it is made of: Stocks 100.0%
Largest holdings: Newmont Corp 10.7%, Agnico Eagle Mines Ltd 10.7%, Barrick Mining Corp 7.4%, Wheaton Precious Metals Corp 5.8%, Anglogold Ashanti PLC 5.3%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.0% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: money coming in (1 week)
Share count change: 1 week: +7.2% (2.02B) over 7d
Shares outstanding: 346.41M | fund size: 30.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a modest bullish tilt from analyst coverage (all buy with a +4.9% price target) but high valuations, flat fund flows, and mixed technical signals keep the overall view neutral.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (43.2% weight) all buy with +4.9% price target
- Fund flows flat over past week (share count +0.0%)
- High valuations (P/E 34.2, P/B 8.09, P/S 9.07) despite strong 3‑year return
- Technical indicators: price above SMAs, RSI 56.5, MACD slightly below signal, low volume (0.31x 20‑day avg)
- Macro: yields rising (10‑yr +0.15% week), VIX elevated at 17.13, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 107.23 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 105.28 (+1.9%), 50d 102.54 (+4.6%), 200d 93.59 (+14.6%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD 1.059 vs signal 1.181 (histogram -0.122)
Returns: 1d +0.7% | 5d +0.1% | 1m +1.0% | 3m +14.6%
52-week range: 74.67 - 117.08 (now 76.8% of the way up)
Volatility: ATR(14) 2.44 (2.3% of price) | annualised 20d 28.8%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 34.20 | P/B 8.09 | P/S 9.07 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +15.5% a year | beta to the market 1.21
Cost and size: expense ratio 0.38% | net assets 15.74B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Palantir Technologies Inc Ordinary Shares - Class A 10.3%, Palo Alto Networks Inc 9.7%, Microsoft Corp 9.2%, CrowdStrike Holdings Inc Class A 7.4%, Salesforce Inc 6.6%
Sector mix: Technology 94.4%, Communication services 3.8%, Financial services 1.5%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.9% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-23 Rosenblatt: main, Buy -> Buy
  - PANW: 2026-09-28 BTIG: main, Buy -> Buy
  - MSFT: 2026-10-01 Wells Fargo: main, Overweight -> Overweight
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
Shares outstanding: 12.50M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is bullish for a thin slice of the fund (24.7% weight) with 100% buy ratings and a +34.9% price target, but the coverage is limited. Fund flows are positive, showing a 3.2% increase in share count over the week, indicating fresh demand. Fundamentals are modest: P/E 22.87, three‑year return 2.3% per year, beta 0.56, and the macro backdrop (rising US yields, stronger dollar, higher VIX) is slightly negative for emerging‑market equities. Technicals are weak (price below SMAs, RSI 29, low volume) but not a decisive break on heavy volume. Overall, the mixed signals lead to a neutral stance.

**Main reasons it gave:**
- Analyst coverage thin (24.7% of fund) but 100% buy ratings and +34.9% price target
- Fund flows positive: share count up 3.2% in one week indicating inflows
- Fundamentals modest: P/E 22.87, 3‑year return 2.3% per year, beta 0.56
- Macro: US 10‑year yield up 0.15% week, dollar index up 0.47% week, VIX up 1.5 points

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.30 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 48.05 (-3.6%), 50d 49.01 (-5.5%), 200d 49.89 (-7.2%); 50d below 200d
Momentum: RSI(14) 29.0 | MACD -0.660 vs signal -0.500 (histogram -0.160)
Returns: 1d -0.8% | 5d -2.6% | 1m -6.6% | 3m -6.6%
52-week range: 45.42 - 55.29 (now 8.9% of the way up)
Volatility: ATR(14) 0.45 (1.0% of price) | annualised 20d 13.6%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: India Equity
What it holds: P/E 22.87 | P/B 3.14 | P/S 2.72 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.3% a year | beta to the market 0.56
Cost and size: expense ratio 0.61% | net assets 6.75B
What it is made of: Stocks 100.1%, Cash -0.1%
Largest holdings: HDFC Bank Ltd 6.4%, Reliance Industries Ltd 6.0%, ICICI Bank Ltd 5.7%, Bharti Airtel Ltd 4.1%, Infosys Ltd 2.6%
Sector mix: Financial services 30.1%, Consumer cyclical 12.8%, Industrials 9.7%, Energy 8.6%
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
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.9% above the current prices
Holdings read: HDFCBANK.NS, RELIANCE.NS, ICICIBANK.NS, BHARTIARTL.NS, INFY.NS
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.2% (203.60M) over 7d
Shares outstanding: 143.51M | fund size: 6.64B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals oversold but no decisive break, modest inflows, bullish analyst view limited to 57.5% coverage, mixed fundamentals.

**Main reasons it gave:**
- 10-year Treasury yield up 15 bps this week, no policy surprise
- RSI 23.8 indicates oversold, but volume 0.45x 20‑day average (low)
- Share count increased 3.3% over the past week, indicating net inflows
- Analyst coverage 57.5% of fund, 100% buy rating, price target +29.9% above current

<details><summary><b>News</b> — score +0.00</summary>

- [Boeing Lands $20B Navy Deal for Next-Gen Fighter Jet: ETFs to Watch](https://www.zacks.com/stock/news/2999035/boeing-lands-20b-navy-deal-for-next-gen-fighter-jet-etfs-to-watch)  
  <sub>Zacks Investment Research, 6 minutes ago</sub>  
  Boeing's $20B Navy win adds to a string of defense and commercial orders. Here are the ETFs offering exposure to the aerospace giant.
- [What's Going On With Boeing Stock Thursday?](https://www.benzinga.com/markets/large-cap/26/10/62101843/whats-going-on-with-boeing-stock-thursday)  
  <sub>Benzinga, 4 hours ago</sub>  
  Boeing (BA) lands U.S. Navy 6th-gen fighter contract, Ethiopian cargo jet deal, and JAL services agreement. Analyst price forecasts inside.
- [Defense ETF picks: sector oversold with RSI readings below 30](https://www.investing.com/news/stock-market-news/defense-etf-picks-sector-oversold-with-rsi-readings-below-30-93CH-4925788)  
  <sub>Investing.com, 19 hours ago</sub>  
  Investing.com -- Defense ETFs have been under pressure lately — RSI readings across the board are deeply oversold (most below 30), suggesting the sector has...
- [Pentagon launches Project Meridian to identify future warfare technology (PPA:NYSEARCA)](https://seekingalpha.com/news/4648803-pentagon-launches-project-meridian-to-identify-future-warfare-technology)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Pentagon's Project Meridian targets AI, autonomy, drones, robotics, directed energy and biotech—early signals for defense tech investors.
- [Boeing wins $131.23 billion F-15 contract with minimal initial obligation](https://scanx.trade/stock-market-news/companies/boeing-wins-131-23b-indefinite-contract-f-15-eagle-crest/49152716)  
  <sub>scanx.trade, 17 hours ago</sub>  
  Boeing secures $131.23 billion ceiling contract for F-15 Eagle Crest program. Initial FY26 obligation is minimal at $343740 for RDT&E funds.
- [Pomerantz investigates Boeing after software issue delays Max 10 certification](https://scanx.trade/stock-market-news/companies/boeing-shares-fall-4-3-737-max-software-glitch-reported/52155201)  
  <sub>scanx.trade, 19 hours ago</sub>  
  Pomerantz LLP is investigating Boeing for potential securities fraud related to the 737 MAX 10 certification delay. The FAA delayed certification due to a...
- [Boeing to release Q3FY26 results on October 27](https://scanx.trade/stock-market-news/companies/boeing-release-q3fy26-results-october-27/52327508)  
  <sub>scanx.trade, 20 hours ago</sub>  
  Boeing will release third-quarter 2026 financial results on October 27. CEO Kelly Ortberg and CFO Jay Malave will host the earnings call.
- [Trump Election-Security Push Spurs Defense ETF Volatility Potential](https://www.tipranks.com/news/catalyst/trump-election-security-push-spurs-defense-etf-volatility-potential)  
  <sub>TipRanks, 13 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “Exclusive: Hegseth directs Defense Dept. to fight...
- [How Trump’s Iraq Withdrawal Announcement Could Reshape Aerospace & Defense ETFs](https://www.tipranks.com/news/catalyst/how-trumps-iraq-withdrawal-announcement-could-reshape-aerospace-defense-etfs)  
  <sub>TipRanks, 21 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “Today, I am pleased to announce, that the last American...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 206.79 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 215.44 (-4.0%), 50d 231.40 (-10.6%), 200d 230.47 (-10.3%); 50d above 200d
Momentum: RSI(14) 23.8 | MACD -6.400 vs signal -6.313 (histogram -0.087)
Returns: 1d -0.2% | 5d -2.8% | 1m -8.3% | 3m -16.7%
52-week range: 198.23 - 253.22 (now 15.6% of the way up)
Volatility: ATR(14) 3.77 (1.8% of price) | annualised 20d 14.0%
Volume: 0.45x the 20-day average
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
Three-year record: +26.4% a year | beta to the market 0.99
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.9% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-21 Jefferies: main, Buy -> Buy
  - GD: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - LMT: 2026-09-08 UBS: up, Neutral -> Buy
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
Share count change: 1 week: +3.3% (433.22M) over 7d
Shares outstanding: 65.14M | fund size: 13.47B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage: 90.8% buy rating, price target +28.6% above current price
- Fund flows: +1.0% share count increase over 1 week (net inflow)
- Technicals: price below 20d, 50d, 200d SMAs; RSI 28.7 (oversold); low volume
- Macro: Treasury yields up across curve (10y 5.31% +0.15, 30y 5.66% +0.20); VIX 17.13 (+1.5)

<details><summary><b>News</b> — score +0.00</summary>

- [How to Buy Lyft Stock (LYFT) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-lyft-stock/)  
  <sub>The Motley Fool, 13 hours ago</sub>  
  Is Lyft a company you'd be interested in investing in? Here's how to do it and decide whether it's right for you.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 78.14 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 80.78 (-3.3%), 50d 84.22 (-7.2%), 200d 81.24 (-3.8%); 50d above 200d
Momentum: RSI(14) 28.7 | MACD -1.693 vs signal -1.613 (histogram -0.080)
Returns: 1d -0.5% | 5d -1.0% | 1m -5.8% | 3m -11.2%
52-week range: 68.14 - 90.01 (now 45.7% of the way up)
Volatility: ATR(14) 1.14 (1.5% of price) | annualised 20d 13.5%
Volume: 0.12x the 20-day average
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
Three-year record: +12.0% a year | beta to the market 1.28
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.6% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
  - UBER: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
  - CSX: 2026-09-18 B of A Securities: main, Buy -> Buy
  - UPS: 2026-07-29 Stifel: main, Buy -> Buy
  - NSC: 2026-07-27 BMO Capital: main, Market Perform -> Market Perform
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
Share count change: 1 week: +1.0% (20.79M) over 7d
Shares outstanding: 27.88M | fund size: 2.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no clear macro catalyst, no decisive technical breakout, and mixed signals from fundamentals, analyst view, and fund flows.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs, indicating a downtrend
- RSI 24.9 (oversold) but MACD negative and volume at 0.47× 20‑day average, no decisive breakout
- Analyst coverage of 44.4% of fund shows 90% buy rating and weighted price target +18.5% above current prices
- Fund flows show modest net inflow of +0.7% share count (≈$156 M) over the past week
- US Treasury yields rose (10‑yr +15 bps) and VIX up 1.5 points, with no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.10 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 37.45 (-3.6%), 50d 37.76 (-4.4%), 200d 38.12 (-5.3%); 50d below 200d
Momentum: RSI(14) 24.9 | MACD -0.466 vs signal -0.312 (histogram -0.154)
Returns: 1d -0.6% | 5d -2.1% | 1m -6.5% | 3m -3.4%
52-week range: 35.83 - 41.03 (now 5.3% of the way up)
Volatility: ATR(14) 0.30 (0.8% of price) | annualised 20d 8.6%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.00 | P/B 1.81 | P/S 3.04 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +1.0% a year | beta to the market 0.18
Cost and size: expense ratio 0.75% | net assets 638.50M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Al Rajhi Bank 14.1%, Saudi Arabian Oil Co 11.1%, Saudi National Bank 8.8%, Saudi Telecom Co 6.0%, Saudi Arabian Mining Co 4.4%
Sector mix: Financial services 41.9%, Basic materials 12.7%, Energy 12.1%, Communication services 8.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.5% above the current prices
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.7% (4.34M) over 7d
Shares outstanding: 17.29M | fund size: 624.11M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish technicals and macro pressures versus bullish analyst view, fund inflows and modestly attractive fundamentals lead to a neutral overall stance.

**Main reasons it gave:**
- Technical: price below 20‑day (53.12), 50‑day (54.33), and 200‑day (56.85) SMAs; RSI 37, MACD negative
- Analyst view: 100% buy rating on top holdings with +56% price target
- Fund flows: +3% share count increase over past week indicating net inflows
- Macro: rising US yields (10‑yr +0.15% on week) and stronger dollar (+0.47% on week) adding pressure to equities

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 52.06 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 53.12 (-2.0%), 50d 54.33 (-4.2%), 200d 56.85 (-8.4%); 50d below 200d
Momentum: RSI(14) 37.0 | MACD -0.571 vs signal -0.484 (histogram -0.087)
Returns: 1d -0.2% | 5d -1.4% | 1m -4.3% | 3m +2.3%
52-week range: 50.48 - 66.99 (now 9.6% of the way up)
Volatility: ATR(14) 0.59 (1.1% of price) | annualised 20d 15.2%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.90 | P/B 1.39 | P/S 1.38 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +9.1% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 6.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Tencent Holdings Ltd 13.9%, Alibaba Group Holding Ltd Ordinary Shares 9.6%, China Construction Bank Corp Class H 4.0%, Industrial And Commercial Bank Of China Ltd Class H 2.5%, Xiaomi Corp Class B 2.4%
Sector mix: Consumer cyclical 23.4%, Financial services 20.0%, Communication services 18.2%, Technology 11.8%
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
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +56.0% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.0% (181.04M) over 7d
Shares outstanding: 120.28M | fund size: 6.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view offset by modest outflows and mixed fundamentals, with no macro surprise or decisive technical break.

**Main reasons it gave:**
- Fund flows: -0.7% share count change (money out) over 1 week
- Analyst view: 49.2% coverage of holdings, all buy ratings, weighted price target +36% above current price
- Technicals: price above 20d/50d/200d SMAs, RSI 63, MACD positive, but volume 0.28x 20-day average
- Macro: Treasury yields up modestly (10-year +0.15% week), VIX 17.13, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [Don't Quit AI, Insure It: A 10-ETF Diversification Portfolio (NASDAQ:QQQ)](https://seekingalpha.com/article/4951263-dont-quit-ai-insure-it-a-10-etf-diversification-portfolio)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  My 10-ETF portfolio reduces maximum drawdown to ~7.9% versus ~40% for the AI portfolio. Read why I advocate a 10-ETF diversified portfolio as a hedge.
- [Every S&P Sector Fell in September Except One](https://247wallst.com/investing/2026/10/01/every-sp-sector-fell-in-september-except-one/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Ten of eleven S&P sectors dropped in September as oil and Treasury yields surged together, yet one corner of the market kept climbing and now sits at its...
- [S&P 500, Dow Extend Losses From Elevated Yield Pressure — SPCX, TGT, AAPL, MU, NTAP In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-extend-losses-from-elevated-yield-pressure-spcx-tgt-aapl-mu-ntap-in-focus/cZMZLlCRBW0)  
  <sub>Stocktwits, 3 hours ago</sub>  
  The S&P 500 ended Tuesday 0.2% lower, the Nasdaq 100 rose 0.2%, and the Dow Jones Industrial Average fell 0.3%.
- [YieldMax Semiconductor ETF offers 39%+ yield vi...](https://pluang.com/en/news-feed/chpy-investasi-semikonduktor-berhasil-dengan-dividen-tinggi)  
  <sub>Pluang, 7 hours ago</sub>  
  The YieldMax Semiconductor Portfolio Option Income ETF (CHPY) provides a differentiated, high-yield investment option focused on semiconductors,...
- [PLTR, MRCY Stocks Gain After Announcing Partnership To Automate US Defense Manufacturing](https://stocktwits.com/news-articles/markets/equity/pltr-mrcy-stocks-gain-palatir-mercury-systems-defence-partnership/cZoTX6TRJdo)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Wall Street is expecting Palantir to report earnings per share of $0.35 on revenue of $1.8 billion in its Q2 report scheduled after the bell.
- [CHPY: A 39% Yielding Semiconductor Bet I'm Adding To My 21%+ Income Portfolio](https://seekingalpha.com/article/4951257-chpy-a-39-percent-yielding-semiconductor-bet-im-adding-to-my-21-percent-plus-income-portfolio)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  CHPY delivers a 39%+ yield via call spread strategies on a concentrated semiconductor portfolio, benefiting from sector volatility. Read more on CHPY ETF...
- [S&P 500, Dow, Nasdaq End Week Higher On Chipmaker Strength, Easing Oil Amid Signs Of Easing US-Iran Conflict — META, COST, MSFT, CRWD, SKHY In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-end-week-higher-on-chipmaker-strength-easing-oil-amid-signs-of-easing-us-iran-conflict-meta-cost-msft-crwd-skhy-in-focus/cZMOFkXRBOV)  
  <sub>Stocktwits, 10 hours ago</sub>  
  U.S. stock indices ended Friday higher as oil prices cooled after a media report suggested signs of diplomatic talks between the U.S. and Iran,...
- [S&P 500, Nasdaq End Week Higher Following Strong SK Hynix Debut — META, SKHVY, CRCL, BA, DAL In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-end-week-higher-following-strong-sk-hynix-debut-meta-skhvy-crcl-ba-dal-in-focus/cZmr12VR78N)  
  <sub>Stocktwits, 14 hours ago</sub>  
  U.S. stock indices ended higher on Friday following a strong debut from South Korean memory chip maker SK Hynix as investors prepare for the earnings...
- [S&P 500, Nasdaq, Dow End Higher Led By Chipmaker Stocks As Investors Look Past US-Iran Hostility — ORCL, SBUX, WULF, PANW, FATE In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-end-higher-led-by-chipmaker-stocks-as-investors-look-past-us-iran-hostility/cZmY9vSR7nz)  
  <sub>Stocktwits, 12 hours ago</sub>  
  U.S. stock indices ended higher on Thursday as chipmaker stocks rebounded sharply ahead of SK Hynix's highly anticipated Nasdaq debut on July 10,...
- [S&P 500, Dow End Lower As Investors Shrug Off Cooler-Than-Expected Inflation Data — MGM, SPCX, AAPL, TSM In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-end-lower-as-investors-shrug-off-cooler-than-expected-inflation-data-mgm-spcx-aapl-tsm-in-focus/cZMFmUrRBL1)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The S&P 500 and Dow Jones ended Wednesday lower, with the Dow recording its worst month since March this year as investors shrugged off cooler PCE data amid...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 610.91 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 579.90 (+5.3%), 50d 568.70 (+7.4%), 200d 498.08 (+22.7%); 50d above 200d
Momentum: RSI(14) 63.0 | MACD 12.112 vs signal 7.924 (histogram 4.188)
Returns: 1d +0.3% | 5d +1.7% | 1m +12.0% | 3m +3.1%
52-week range: 325.10 - 668.91 (now 83.1% of the way up)
Volatility: ATR(14) 14.60 (2.4% of price) | annualised 20d 30.6%
Volume: 0.28x the 20-day average
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
Three-year record: +61.9% a year | beta to the market 2.06
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.1% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-01 TD Cowen: reit, Buy -> Buy
  - AMD: 2026-09-29 StoneX: reit, Buy -> Buy
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
Share count change: 1 week: -0.7% (-473.36M) over 7d
Shares outstanding: 112.94M | fund size: 68.99B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed fundamentals, bearish technicals, limited analyst coverage.

**Main reasons it gave:**
- Flat fund flows (0% change) indicate no net demand
- No macro surprise: US yields rose modestly, inflation 3.4% in line with expectations
- Technical indicators bearish: price below 20d, 50d, 200d SMAs, RSI 31.8
- Analyst view bullish for 39.5% of holdings but limited coverage
- Fundamentals mixed: three-year record -1.3% a year, moderate valuation

<details><summary><b>News</b> — score +0.00</summary>

- [ProShares UltraPro QQQ (TQQQ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TQQQ/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  Find the latest ProShares UltraPro QQQ (TQQQ) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 34.53 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 37.69 (-8.4%), 50d 38.71 (-10.8%), 200d 39.32 (-12.2%); 50d below 200d
Momentum: RSI(14) 31.8 | MACD -1.290 vs signal -0.870 (histogram -0.419)
Returns: 1d +2.2% | 5d -5.6% | 1m -13.2% | 3m -12.2%
52-week range: 31.90 - 43.74 (now 22.2% of the way up)
Volatility: ATR(14) 0.79 (2.3% of price) | annualised 20d 37.9%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: -1.3% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.0% above the current prices
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
Shares outstanding: 15.65M | fund size: 540.37M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view is bullish, but fund inflows are modest and fundamentals are mixed with high valuation and yield below Treasury rates, while technicals show oversold conditions without a decisive breakout.

**Main reasons it gave:**
- Analyst consensus 100% buy with +22% price target
- Weekly fund inflows increased share count by 3.6% (2.39B)
- P/E ratio 30.19 and yield 3.6% below 10-year Treasury yield 5.31%
- RSI 20.5 (oversold) and price below 20d, 50d, 200d SMAs

<details><summary><b>News</b> — score +0.00</summary>

- [Moving Averages of the Ivy Portfolio and S&P 500: September 2026](https://www.advisorperspectives.com/dshort/updates/2026/09/30/ivy-portfolio-sp500-moving-averages-september-2026)  
  <sub>Advisor Perspectives, 17 hours ago</sub>  
  Valid until the market close on October 31, 2026 This article provides an update on the monthly moving averages we track for the S&P 500 and the Ivy...
- [Major Asset Classes: September 2026 Performance Review](https://seekingalpha.com/article/4951333-major-asset-classes-september-2026-performance-review)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Commodities and cash were the only winners among the major asset classes in September. The rest of the field lost ground, led by property shares in the U.S....
- [ETFs Investing in Broadstone Net Lease, Inc. Stocks](https://www.tradingview.com/symbols/LS-A2QR15/etfs/)  
  <sub>TradingView, 17 hours ago</sub>  
  Explore funds investing in A2QR15 in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [A 14% Yield From Pipelines: The Energy Infrastructure ETF Built for Monthly Income](https://247wallst.com/investing/etf/2026/09/30/a-14-yield-from-pipelines-the-energy-infrastructure-etf-built-for-monthly-income/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Infrastructure is already widely used by institutional investors for cash flow and diversification, while publicly traded MLPs give retail investors...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 88.82 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 93.09 (-4.6%), 50d 96.30 (-7.8%), 200d 94.37 (-5.9%); 50d above 200d
Momentum: RSI(14) 20.5 | MACD -1.911 vs signal -1.570 (histogram -0.341)
Returns: 1d -0.9% | 5d -2.6% | 1m -7.8% | 3m -9.4%
52-week range: 87.00 - 100.95 (now 13.1% of the way up)
Volatility: ATR(14) 1.15 (1.3% of price) | annualised 20d 12.1%
Volume: 0.53x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +10.4% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 70.82B
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.70</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.0% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-09-30 Barclays: main, Overweight -> Overweight
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.6% (2.39B) over 7d
Shares outstanding: 781.80M | fund size: 69.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, technicals show slight bearish bias but low volume, modest inflows, and mixed analyst view.

**Main reasons it gave:**
- Fund flows: +1.0% share count increase over 1 week (net inflow)
- Analyst coverage thin (9% weight) with mixed buy/hold rating and -19.1% price target
- Technical indicators: RSI 47.8, MACD negative, volume 0.47x 20‑day average
- Tariff expansion on imported drugs had no noticeable impact on XBI (price unchanged)
- Macro: No surprise in yields or data; VIX up modestly, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  State Street SPDR S&P Biotech ETF (XBI) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM to 4 AM ET,...
- [Big Pharma Got Its Tariff Exemption. The Biotech ETF Barely Blinked](https://247wallst.com/investing/2026/09/30/big-pharma-got-its-tariff-exemption-the-biotech-etf-barely-blinked/)  
  <sub>24/7 Wall St., 19 hours ago</sub>  
  A 100% tariff on imported drugs just expanded to cover every drugmaker in the country, yet the biotech market's most closely watched fund treated it like a...
- [More Upside Awaits for Gilead Sciences Stock. Stay Invested.](https://www.barrons.com/articles/gilead-sciences-stock-stay-invested-more-upside-awaits-e1c38c22)  
  <sub>Barron's, 36 minutes ago</sub>  
  Shares of Gilead Sciences · GILD. +0.85%. are up some 35% since Barron's highlighted them a year ago, citing the company's strong and growing portfolio of...
- [Stocktwits Pharma Pulse: Lilly, Novo Lead A Busy Week — Here Are The Stocks And Readouts To Watch](https://stocktwits.com/news-articles/markets/equity/stocktwits-pharma-pulse-lilly-novo-lead-busy-week-stocks-readouts-to-watch/cZMSib7RBfS)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Lilly will present Phase 2 results for its eloraTZP combination at the EASD meeting in Milan. SAB BIO, Sana and Century will present type 1 diabetes...
- [IBRX Breaks Above This Key Resistance — Stock On Track To Record Best Single-Day Gains In 6 Months](https://www.tradingview.com/news/stocktwits:f5f870817094b:0-ibrx-breaks-above-this-key-resistance-stock-on-track-to-record-best-single-day-gains-in-6-months/)  
  <sub>TradingView, 22 hours ago</sub>  
  Chairman Patrick Soon-Shiong recently met with Turkish President Recep Tayyip Erdoğan, leading to optimism around a potential expansion of Anktiva into the...
- [Nasdaq 100 Climbs as Cooler PCE Cuts Rate Hike Bets, Micron Earnings Loom: Stock Market Today](https://www.tradingview.com/news/benzinga:89ded3b78094b:0-nasdaq-100-climbs-as-cooler-pce-cuts-rate-hike-bets-micron-earnings-loom-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks are higher at midday Wednesday, led by technology and software shares, after softer-than-expected inflation data eased fears of another Federal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 157.03 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 157.89 (-0.5%), 50d 158.06 (-0.7%), 200d 138.68 (+13.2%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD -0.784 vs signal -0.654 (histogram -0.130)
Returns: 1d -0.4% | 5d +0.6% | 1m -3.9% | 3m -2.1%
52-week range: 101.39 - 169.55 (now 81.6% of the way up)
Volatility: ATR(14) 4.02 (2.6% of price) | annualised 20d 24.5%
Volume: 0.47x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.20 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +29.3% a year | beta to the market 1.12
Cost and size: expense ratio 0.35% | net assets 11.40B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.8%, Twist Bioscience Corp 1.9%, Apogee Therapeutics Inc 1.5%, Kymera Therapeutics Inc Ordinary Shares 1.4%, Halozyme Therapeutics Inc 1.4%
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

```text
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 43.2% | hold 56.8% | sell 0.0% (mean 2.31 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -19.1% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-30 Citigroup: down, Neutral -> Sell
  - TWST: 2026-10-01 Guggenheim: main, Buy -> Buy
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-22 Stifel: main, Buy -> Buy
  - HALO: 2026-09-02 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: +1.0% (117.82M) over 7d
Shares outstanding: 72.83M | fund size: 11.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break occurred; technicals are bearish, flows flat, macro tightening, analyst view bullish but thin.

**Main reasons it gave:**
- Price 94.30 is below 20‑day SMA (98.02), 50‑day SMA (103.32) and 200‑day SMA (106.20)
- RSI 33.7 indicates weak momentum
- Share count down 0.3% (-4.17 M) over the week, flat flow direction
- 10‑year Treasury yield up 0.15% week and VIX up to 17.13, signaling tightening and higher risk
- Analyst coverage thin (20.9% weight) but 74% buy rating and +25.5% price target for top holdings

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 94.30 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 98.02 (-3.8%), 50d 103.32 (-8.7%), 200d 106.20 (-11.2%); 50d below 200d
Momentum: RSI(14) 33.7 | MACD -2.112 vs signal -2.152 (histogram 0.041)
Returns: 1d -1.8% | 5d -2.6% | 1m -6.2% | 3m -16.2%
52-week range: 94.30 - 121.36 (now 0.0% of the way up)
Volatility: ATR(14) 2.12 (2.2% of price) | annualised 20d 22.4%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 19.52 | P/B 2.34 | P/S 1.36 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +9.1% a year | beta to the market 1.46
Cost and size: expense ratio 0.35% | net assets 1.33B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Installed Building Products Inc 4.4%, Owens-Corning Inc 4.3%, Allegion PLC 4.3%, Champion Homes Inc 4.1%, Williams-Sonoma Inc 3.9%
Sector mix: Consumer cyclical 60.7%, Industrials 37.9%, Real estate 1.5%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 74.0% | hold 26.0% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.5% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-25 Evercore ISI Group: main, In-Line -> In-Line
  - OC: 2026-09-11 Wells Fargo: main, Overweight -> Overweight
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-09-30 Oppenheimer: init, ? -> Perform
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.3% (-4.17M) over 7d
Shares outstanding: 13.69M | fund size: 1.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows a neutral overall stance: analyst coverage is extremely bullish (+100% price target), but fund flows are flat (0% change) indicating no net demand, technicals are mixed (oversold RSI but negative MACD and low volume), fundamentals are moderate with high valuation multiples (P/E 24.59, P/B 3.00) and modest yield (1.6%), and macro conditions show modest yield rises and no surprise data. No material macro catalyst or decisive technical break is present, so the net signal remains neutral.

**Main reasons it gave:**
- Analyst view: 100% buy rating with price target +100% above current price
- Fund flows: flat share count change (0% over 1 week), indicating neutral demand
- Technical indicators: RSI 27.5 (oversold) and MACD negative, with volume below 20‑day average
- Fundamentals: high valuation multiples (P/E 24.59, P/B 3.00) and modest yield 1.6%
- Macro: yields rising modestly, VIX elevated at 17.13, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [DeMark Pivot Points Signal Key Price Levels for XLY ETF on October 01, 2026](https://www.gurufocus.com/news/9105464/demark-pivot-points-signal-key-price-levels-for-xly-etf-on-october-01-2026)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 01, 2026, recent calculations using the DeMark method have identified critical pivot points for the State Street Consumer Discretionary Select...
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [Which Automaker Stock Dominated in September: Tesla, Ford, or General Motors?](https://247wallst.com/investing/2026/09/30/which-automaker-stock-dominated-in-september-tesla-ford-or-general-motors/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Three automakers faced the same September market, yet one of them broke sharply from the pack while the other two suffered painful double-digit losses.
- [Growth Leads Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/09/62083340/growth-leads-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with growth sectors holding two of the top three positions.
- [Nasdaq 100 Climbs as Cooler PCE Cuts Rate Hike Bets, Micron Earnings Loom: Stock Market Today](https://www.tradingview.com/news/benzinga:89ded3b78094b:0-nasdaq-100-climbs-as-cooler-pce-cuts-rate-hike-bets-micron-earnings-loom-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks are higher at midday Wednesday, led by technology and software shares, after softer-than-expected inflation data eased fears of another Federal...
- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest State Street Communication Services Select Sector SPDR ETF (XLC) stock quote, history, news and other vital information to help you with...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 47.96 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 50.38 (-4.8%), 50d 51.57 (-7.0%), 200d 50.63 (-5.3%); 50d above 200d
Momentum: RSI(14) 27.5 | MACD -0.875 vs signal -0.661 (histogram -0.214)
Returns: 1d -1.5% | 5d -3.5% | 1m -7.9% | 3m -7.8%
52-week range: 42.23 - 53.67 (now 50.0% of the way up)
Volatility: ATR(14) 0.75 (1.6% of price) | annualised 20d 12.7%
Volume: 0.79x the 20-day average
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
Three-year record: +9.8% a year | beta to the market 0.82
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +100.0% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technicals are weak, no macro surprise, but positive analyst view and fund inflows provide modest bullish bias.

**Main reasons it gave:**
- Fund flows +3.2% share count increase over the week
- Analyst consensus 100% buy with weighted price target +17.6% above current price
- Price below 20‑day, 50‑day, and 200‑day SMAs; RSI 43 indicating weak technicals
- No macro surprise: yields modestly up, VIX up modestly, inflation 3.4% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  State Street Communication Services Select Sector SPDR ETF (XLC) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS,...
- [Should You Tap Meta ETFs on Muse's Success or Wait on the Sidelines?](https://www.tradingview.com/news/zacks:9c6d912f0094b:0-should-you-tap-meta-etfs-on-muse-s-success-or-wait-on-the-sidelines/)  
  <sub>TradingView, 4 hours ago</sub>  
  Meta META CEO Mark Zuckerberg outlined the company's plans to monetize its rapidly growing Muse AI agent during the Meta Connect conference on Sept.
- [AppLovin Stock Extends A 7-Day Losing Streak To A 12% Loss](https://www.trefis.com/stock/app/articles/617272/applovin-stock-extends-a-7-day-losing-streak-to-a-12-loss/2026-10-01)  
  <sub>Trefis, 5 hours ago</sub>  
  Shares of AppLovin (APP) have closed lower in each of the last 7 sessions, a cumulative decline of 12.0%. That erased about $13.3 billion from the company's...
- [Growth Leads Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/09/62083340/growth-leads-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with growth sectors holding two of the top three positions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 109.96 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 112.42 (-2.2%), 50d 111.39 (-1.3%), 200d 113.82 (-3.4%); 50d below 200d
Momentum: RSI(14) 43.2 | MACD -0.132 vs signal 0.243 (histogram -0.374)
Returns: 1d -0.9% | 5d -3.5% | 1m -0.8% | 3m +0.3%
52-week range: 105.38 - 120.08 (now 31.2% of the way up)
Volatility: ATR(14) 1.77 (1.6% of price) | annualised 20d 20.9%
Volume: 0.32x the 20-day average
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
Three-year record: +20.7% a year | beta to the market 0.85
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.6% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
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
Share count change: 1 week: +3.2% (689.07M) over 7d
Shares outstanding: 201.77M | fund size: 22.19B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage of top holdings bullish (+5.5% price target) covering 51.7% of fund weight
- Energy inventories mixed: crude oil build (+0.9 mb, 62% percentile) bearish; gasoline and diesel draws (low percentiles) bullish
- EIA price outlook forecasts falling oil (down ~13% in 6 months) and gas (down ~5% in 6 months)
- Technical indicators mixed: price below 20‑day SMA, MACD negative, low volume
- Fund flows flat with no net creations/redemptions

<details><summary><b>News</b> — score +0.00</summary>

- [Should You Invest in the First Trust NASDAQ Oil & Gas ETF (FTXN)?](https://finance.yahoo.com/energy/articles/invest-first-trust-nasdaq-oil-092002033.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  If you're interested in broad exposure to the Energy - Broad segment of the equity market, look no further than the First Trust NASDAQ Oil & Gas ETF (FTXN),...
- [Don't Quit AI, Insure It: A 10-ETF Diversification Portfolio (NASDAQ:QQQ)](https://seekingalpha.com/article/4951263-dont-quit-ai-insure-it-a-10-etf-diversification-portfolio)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  My 10-ETF portfolio reduces maximum drawdown to ~7.9% versus ~40% for the AI portfolio. Read why I advocate a 10-ETF diversified portfolio as a hedge.
- [Oil executives warn Iran war volatility makes planning difficult (XLE:NYSEARCA)](https://seekingalpha.com/news/4648693-oil-executives-warn-iran-war-volatility-makes-planning-difficult)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Dallas Fed energy survey: Iran war fuels oil-price volatility, lifting $82 forecasts but curbing shale growth.
- [Polish billionaire Solowow brings new investors into nuclear reactor venture (XLE:NYSEARCA)](https://seekingalpha.com/news/4648675-polish-billionaire-solowow-brings-new-investors-into-nuclear-reactor-venture)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Poland's SMR push heats up as Solowow adds top investors to SGE for GE Vernova's BWRX-300—key funding, timeline, and risks.
- [ETFs Are Net Sellers of Williams (WMB) on Sept. 29](https://www.gurufocus.com/news/9105160/etfs-are-net-sellers-of-williams-wmb-on-sept-29)  
  <sub>GuruFocus, 4 hours ago</sub>  
  ETF flows turned negative for Williams (WMB) on Tuesday, ending a two-day run of net buying. The midstream energy company saw a net $13.9 million sold by...
- [Exchange-Traded Funds, Equity Futures up Pre-Bell Thursday as Traders Assess Micron's Fiscal Q4 Results](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132230485.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [Sector Update: Energy Stocks Rise Late Afternoon](https://ca.finance.yahoo.com/news/sector-energy-stocks-rise-afternoon-200406815.html)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Energy stocks advanced late Wednesday afternoon, with the NYSE Energy Sector Index rising 0.6% and the State Street Energy Select Sector SPDR ETF (XLE)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 62.19 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 63.53 (-2.1%), 50d 62.04 (+0.3%), 200d 56.46 (+10.2%); 50d above 200d
Momentum: RSI(14) 46.7 | MACD -0.191 vs signal 0.198 (histogram -0.388)
Returns: 1d +1.1% | 5d -0.6% | 1m -4.0% | 3m +16.9%
52-week range: 42.61 - 65.93 (now 84.0% of the way up)
Volatility: ATR(14) 1.20 (1.9% of price) | annualised 20d 20.1%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.74 | P/B 2.58 | P/S 1.68 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +14.4% a year | beta to the market -0.07
Cost and size: expense ratio 0.08% | net assets 41.44B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 19.9%, Chevron Corp 14.9%, ConocoPhillips 6.2%, Marathon Petroleum Corp 5.4%, Phillips 66 5.3%
Sector mix: Energy 100.0%
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
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Crude oil: 427.3 million barrels, +0.9 on the week (a build), 62% percentile over 52 weeks
  Petrol: 204.4 million barrels, -1.7 on the week (a draw), 2% percentile over 52 weeks -- low for the time of year
  Diesel: 105.2 million barrels, -2.3 on the week (a draw), 23% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.5% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - CVX: 2026-09-28 TD Cowen: main, Hold -> Hold
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-09-22 Jefferies: down, Buy -> Hold
  - PSX: 2026-09-30 TD Cowen: main, Buy -> Buy
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
Shares outstanding: 186.42M | fund size: 11.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, technicals oversold but low volume, analyst consensus bullish but modest price target, macro environment unchanged.

**Main reasons it gave:**
- Flat fund flows over the past week (no net inflows/outflows)
- Technical RSI 22.3 indicates oversold but low volume and no decisive breakout
- Analyst consensus 100% buy with weighted price target +16.5% for top holdings
- Macro environment: rising Treasury yields and expected Fed hikes, but no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [These ten financial stocks posted the biggest one-month losses (XLF:NYSEARCA)](https://seekingalpha.com/news/4648964-these-ten-financial-stocks-posted-the-biggest-one-month-losses)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  September 2026 financials selloff: see the worst-performing financial stocks and ETFs (FNMA, FMCC, ENVA & more) with Quant Ratings—review now.
- [Which Buy Now Pay Later Stock Dominated in September: Klarna, Affirm, or Sezzle?](https://finance.yahoo.com/markets/stocks/articles/buy-now-pay-later-stock-191613525.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Three buy now, pay later stocks all tumbled in September while financial markets wobbled, but one name managed to pull ahead of the pack by losing less...
- [Exchange-Traded Funds, Equity Futures up Pre-Bell Thursday as Traders Assess Micron's Fiscal Q4 Results](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132230485.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [Sector Update: Financial Stocks Decline Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-decline-afternoon-200434530.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Financial stocks were lower in late Wednesday afternoon trading, with the NYSE Financial Index and the State Street Financial Select Sector SPDR ETF (XLF)...
- [Sector Update: Financial Stocks Decline Wednesday Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-decline-wednesday-180128656.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Financial stocks were lower in Wednesday afternoon trading, with the NYSE Financial Index shedding 0.
- [State Street SPDR S&P Biotech ETF (XBI) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XBI/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>  
  Find the latest State Street SPDR S&P Biotech ETF (XBI) stock quote, history, news and other vital information to help you with your stock trading and...
- [Chubb Limited's Quarterly Earnings Preview: What You Need to Know](https://finance.yahoo.com/markets/stocks/articles/chubb-limiteds-quarterly-earnings-preview-175252433.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  With a market cap of $128.1 billion, Chubb Limited (CB) is a global insurance and reinsurance company that offers a wide range of commercial and personal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 52.92 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 55.79 (-5.1%), 50d 56.85 (-6.9%), 200d 53.72 (-1.5%); 50d above 200d
Momentum: RSI(14) 22.3 | MACD -0.996 vs signal -0.690 (histogram -0.306)
Returns: 1d -0.9% | 5d -3.0% | 1m -7.5% | 3m -4.9%
52-week range: 47.81 - 58.56 (now 47.5% of the way up)
Volatility: ATR(14) 0.71 (1.3% of price) | annualised 20d 13.1%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Financial
What it holds: P/E 16.36 | P/B 2.42 | P/S 3.50 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +19.5% a year | beta to the market 0.71
Cost and size: expense ratio 0.08% | net assets 54.59B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: JPMorgan Chase & Co 11.7%, Berkshire Hathaway Inc Class B 11.3%, Visa Inc Class A 7.7%, Mastercard Inc Class A 5.8%, Bank of America Corp 5.0%
Sector mix: Financial services 98.1%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
Holdings read: JPM, BRK-B, V, MA, BAC
Recent rating changes among them:
  - JPM: 2026-09-28 HSBC: main, Hold -> Hold
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - V: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - MA: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - BAC: 2026-10-01 Evercore ISI Group: main, Outperform -> Outperform
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
Shares outstanding: 883.44M | fund size: 46.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view on a quarter of the fund is offset by high valuations and flat fund flows, with technicals showing weakness but no decisive break and macro conditions unchanged.

**Main reasons it gave:**
- Analyst view: 100% buy rating on 25.8% of fund, weighted price target +25% above current price
- Fund flows: share count flat (+0.0% week), indicating no net demand
- Fund fundamentals: high valuation (P/E 28.43, P/B 6.75) offset by strong 3‑yr return +20.3%/yr
- Technical: price below 20‑, 50‑, 200‑day SMAs, RSI 31.4, low volume, no decisive break
- Macro: yields up (10‑yr +0.15% w.e.), inflation 3.4% above target, VIX 17.13, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures up Pre-Bell Thursday as Traders Assess Micron's Fiscal Q4 Results](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132230485.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [XLK Sets Key DeMark Pivot Points at $197.31 and $195.51 Amidst E](https://www.gurufocus.com/news/9105467/xlk-sets-key-demark-pivot-points-at-19731-and-19551-amidst-elevated-valuation)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 01, 2026, the Technology Select Sector SPDR ETF (ticker: XLK) established significant technical pivot levels using the DeMark analysis method,...
- [PSCI: SMID Industrials Are Likely To Trail IVV Amid Higher Rates (NASDAQ:PSCI)](https://seekingalpha.com/article/4951207-psci-smid-industrials-are-likely-to-trail-ivv-amid-higher-rates)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Invesco S&P SmallCap Industrials ETF faces underperformance risk due to weak growth and limited quality exposure, which is why I maintain the Hold rating.
- [Growth Leads Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/09/62083340/growth-leads-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with growth sectors holding two of the top three positions.
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [These 10 industrials stocks suffered the steepest September declines (XLI:NYSEARCA)](https://seekingalpha.com/news/4648669-these-10-industrials-stocks-suffered-the-steepest-september-declines)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  September 2026 industrials selloff: see the month's worst-performing stocks (AXON, KRMN, EFX, TRU, CAR) and key industrial ETFs—review now.
- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://au.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance Australia, 15 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [Only the tech sector rose in September as oil p...](https://pluang.com/en/news-feed/setiap-sektor-sp-fall-september-kecuali-satu)  
  <sub>Pluang, 3 hours ago</sub>  
  In September 2026, ten of the eleven S&P sectors fell due to rising oil prices and Treasury yields, which pressured most parts of the market.
- [Northrop Grumman's Q3 2026 Earnings: What to Expect](https://www.inkl.com/news/northrop-grummans-q3-2026-earnings-what-to-expect)  
  <sub>inkl, 7 hours ago</sub>  
  Northrop Grumman is set to announce its third-quarter results in October, with analysts projecting single-digit decline in its bottom-line figure.
- [What to Expect From Pentair's Next Quarterly Earnings Report](https://www.inkl.com/news/what-to-expect-from-pentairs-next-quarterly-earnings-report)  
  <sub>inkl, 8 hours ago</sub>  
  Pentair is expected to announce its third-quarter results soon, and analysts predict a double-digit decline in the company's bottom-line figure.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 166.52 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 170.31 (-2.2%), 50d 177.04 (-5.9%), 200d 172.27 (-3.3%); 50d above 200d
Momentum: RSI(14) 31.4 | MACD -2.557 vs signal -2.599 (histogram 0.043)
Returns: 1d -0.3% | 5d -1.4% | 1m -3.6% | 3m -9.5%
52-week range: 147.83 - 186.51 (now 48.3% of the way up)
Volatility: ATR(14) 2.28 (1.4% of price) | annualised 20d 12.4%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Industrials
What it holds: P/E 28.43 | P/B 6.75 | P/S 3.00 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +20.3% a year | beta to the market 1.02
Cost and size: expense ratio 0.08% | net assets 31.95B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Caterpillar Inc 6.7%, GE Aerospace 6.4%, RTX Corp 5.1%, GE Vernova Inc 4.4%, Union Pacific Corp 3.2%
Sector mix: Industrials 92.8%, Technology 6.7%, Basic materials 0.3%, Consumer cyclical 0.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.1% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
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
Shares outstanding: 136.63M | fund size: 22.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals bullish but low volume, analyst view positive but limited coverage, flows flat.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +25.8% price target covering 45.7% of fund
- Fund flows: share count up 0.2% over 1 week, flat direction indicating no strong demand shift
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 63.5, MACD positive, but volume 0.37× 20‑day average
- Macro: Treasury yields rose modestly, no policy surprise; VIX up 1.5 points to 17.13

<details><summary><b>News</b> — score +0.00</summary>

- [Every S&P Sector Fell in September Except One](https://247wallst.com/investing/2026/10/01/every-sp-sector-fell-in-september-except-one/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Ten of eleven S&P sectors dropped in September as oil and Treasury yields surged together, yet one corner of the market kept climbing and now sits at its...
- [Only the tech sector rose in September as oil p...](https://pluang.com/en/news-feed/setiap-sektor-sp-fall-september-kecuali-satu)  
  <sub>Pluang, 3 hours ago</sub>  
  In September 2026, ten of the eleven S&P sectors fell due to rising oil prices and Treasury yields, which pressured most parts of the market.
- [Growth Leads Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/09/62083340/growth-leads-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with growth sectors holding two of the top three positions.
- [Most S&P 500 sectors fall below key support, si...](https://pluang.com/en/news-feed/fase-pertama-koreksi-pasar-saham-teknikal-sulit-diabaikan)  
  <sub>Pluang, 1 hour ago</sub>  
  Currently, 8 out of 11 sectors in the S&P 500 are trading below their 200-day moving averages, indicating a potential for a deeper selloff.
- [Exchange-Traded Funds Higher, US Equities Mixed After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-higher-us-171614405.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 0.7%. US equity indexes traded...
- [FDVV: Fidelity's High-Dividend ETF Keeps Passing The Test (NYSEARCA:FDVV)](https://seekingalpha.com/article/4951170-fdvv-fidelitys-high-dividend-etf-keeps-passing-the-test)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  The Fidelity High Dividend ETF is a well-constructed dividend portfolio with a 2.98% estimated dividend yield and solid fundamentals. Read more on FDVV.
- [Sector Update: Tech Stocks Higher Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-tech-stocks-higher-afternoon-195611680.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Tech stocks were higher late Wednesday afternoon, with the State Street Technology Select Sector SPDR ETF (XLK) rising 1% and the State Street SPDR S&P...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 196.06 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 190.49 (+2.9%), 50d 185.84 (+5.5%), 200d 164.64 (+19.1%); 50d above 200d
Momentum: RSI(14) 63.5 | MACD 2.984 vs signal 2.513 (histogram 0.471)
Returns: 1d +0.2% | 5d +0.7% | 1m +6.8% | 3m +8.6%
52-week range: 127.50 - 198.21 (now 97.0% of the way up)
Volatility: ATR(14) 3.08 (1.6% of price) | annualised 20d 17.6%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Technology
What it holds: P/E 33.01 | P/B 11.41 | P/S 8.77 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +34.2% a year | beta to the market 1.50
Cost and size: expense ratio 0.08% | net assets 121.44B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 14.4%, Apple Inc 12.5%, Microsoft Corp 10.1%, Broadcom Inc 4.7%, Micron Technology Inc 4.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.8% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-01 Needham: reit, Hold -> Hold
  - MSFT: 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-01 TD Cowen: reit, Buy -> Buy
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
Share count change: 1 week: +0.2% (222.16M) over 7d
Shares outstanding: 624.38M | fund size: 122.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral as no material macro surprise, technicals lack decisive break, and fund flows are flat. Analyst view is bullish but covers only ~40% of holdings.

**Main reasons it gave:**
- Fund flows flat: share count unchanged (+0.0% week)
- Technical indicators: price below 20d SMA (-3.0%), RSI 32, no decisive break
- Analyst coverage: 100% buy rating on 39.6% of holdings, price target +14.4% above current
- Macro: yields rose modestly (10‑yr +0.15% week), no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Which Consumer Staples ETF Offers Better Value: XLP or IYK?](https://www.fool.com/coverage/etfs/2026/10/01/which-consumer-staples-etf-offers-better-value-xlp-or-iyk/)  
  <sub>The Motley Fool, 9 minutes ago</sub>  
  State Street Consumer Staples Select Sector SPDR ETF (XLP -0.36%)offers a lower-cost, more concentrated approach to the sector than the broader,...
- [Exchange-Traded Funds, Equity Futures up Pre-Bell Thursday as Traders Assess Micron's Fiscal Q4 Results](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132230485.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [Ten consumer staples stocks that tumbled the most in September (XLP:NYSEARCA)](https://seekingalpha.com/news/4648947-ten-consumer-staples-stocks-that-tumbled-the-most-in-september)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  See September 2026's worst-performing consumer staples stocks (LW, GIS, CLX, CASY, FRPT) plus ETFs—spot sector rotation risks and act now.
- [DeMark Pivot Points Signal Key Price Levels for XLY ETF on October 01, 2026](https://www.gurufocus.com/news/9105464/demark-pivot-points-signal-key-price-levels-for-xly-etf-on-october-01-2026)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 01, 2026, recent calculations using the DeMark method have identified critical pivot points for the State Street Consumer Discretionary Select...
- [Sector Update: Consumer Stocks Decline Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-decline-afternoon-195207407.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Consumer stocks fell late Wednesday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) dropping 1.3% and the State Street...
- [Exchange-Traded Funds Higher, US Equities Mixed After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-higher-us-171614405.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV rose. Actively traded Invesco QQQ Trust (QQQ) added 0.7%. US equity indexes traded...
- [Nasdaq 100 Climbs as Cooler PCE Cuts Rate Hike Bets, Micron Earnings Loom: Stock Market Today](https://es.tradingview.com/news/benzinga:89ded3b78094b:0-nasdaq-100-climbs-as-cooler-pce-cuts-rate-hike-bets-micron-earnings-loom-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks are higher at midday Wednesday, led by technology and software shares, after softer-than-expected inflation data eased fears of another Federal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 80.39 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 82.86 (-3.0%), 50d 84.44 (-4.8%), 200d 83.72 (-4.0%); 50d above 200d
Momentum: RSI(14) 32.0 | MACD -1.005 vs signal -0.792 (histogram -0.213)
Returns: 1d -0.3% | 5d -1.6% | 1m -5.7% | 3m -5.4%
52-week range: 75.60 - 90.01 (now 33.2% of the way up)
Volatility: ATR(14) 1.00 (1.2% of price) | annualised 20d 11.4%
Volume: 0.41x the 20-day average
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
Three-year record: +8.9% a year | beta to the market 0.49
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-29 Mizuho: main, Outperform -> Outperform
  - COST: 2026-09-28 Deutsche Bank: main, Buy -> Buy
  - KO: 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - PG: 2026-09-30 TD Cowen: reit, Hold -> Hold
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
Shares outstanding: 210.17M | fund size: 16.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bullish analyst view is limited to ~40% of the fund, flows are flat, technicals show XLU well below its moving averages with low RSI but no decisive breakout, and rising Treasury yields pressure utilities.

**Main reasons it gave:**
- Analyst coverage of top holdings is bullish (+25.5% price target) but only covers 39.4% of the fund
- Fund flows flat over the past week, indicating no net demand
- Utilities sector breadth extreme, historically precedes gains 82% of the time
- XLU trading below 20‑day, 50‑day, and 200‑day SMAs with low RSI (27.6), but no decisive breakout on volume
- Rising Treasury yields (10‑year up 15 bps) and upward‑sloping curve pressure utilities

<details><summary><b>News</b> — score +0.00</summary>

- [Why Is Constellation Energy Stock Trading Higher Today? - Constellation Energy (NASDAQ:CEG)](https://www.benzinga.com/trading-ideas/movers/26/10/62100792/constellation-energy-amazon-lock-20-year-nuclear-power-purchase-agreement-stock-soars)  
  <sub>Benzinga, 4 hours ago</sub>  
  Constellation Energy and Amazon signed a 20-year agreement covering 690 megawatts of nuclear power from Maryland's Calvert Cliffs plant.
- [Utilities breadth reaches extreme, SentimenTrader says (XLU:NYSEARCA)](https://seekingalpha.com/news/4648666-utilities-breadth-reaches-extreme-sentimentrader-says)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Utilities sector breadth just hit an extreme: XLU's 10-day advance/decline ratio plunged, a signal that preceded gains 82% of the time.
- [Every S&P Sector Fell in September Except One](https://247wallst.com/investing/2026/10/01/every-sp-sector-fell-in-september-except-one/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Ten of eleven S&P sectors dropped in September as oil and Treasury yields surged together, yet one corner of the market kept climbing and now sits at its...
- [Nasdaq 100 Climbs as Cooler PCE Cuts Rate Hike Bets, Micron Earnings Loom: Stock Market Today](https://es.tradingview.com/news/benzinga:89ded3b78094b:0-nasdaq-100-climbs-as-cooler-pce-cuts-rate-hike-bets-micron-earnings-loom-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks are higher at midday Wednesday, led by technology and software shares, after softer-than-expected inflation data eased fears of another Federal...
- [Growth Leads Sectors In Wednesday Trading As Defensives Trail](https://www.benzinga.com/etfs/sector-etfs/26/09/62083340/growth-leads-sectors-in-wednesday-trading-as-defensives-trail)  
  <sub>Benzinga, 24 hours ago</sub>  
  Five sectors are higher and six are lower in Wednesday's regular session, with growth sectors holding two of the top three positions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.32 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 41.11 (-4.4%), 50d 42.80 (-8.1%), 200d 44.40 (-11.4%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -1.055 vs signal -0.945 (histogram -0.109)
Returns: 1d -0.3% | 5d -0.1% | 1m -7.6% | 3m -14.1%
52-week range: 39.25 - 47.73 (now 0.8% of the way up)
Volatility: ATR(14) 0.58 (1.5% of price) | annualised 20d 14.1%
Volume: 0.81x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +13.8% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.5% above the current prices
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
Shares outstanding: 163.27M | fund size: 6.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise or decisive technical break occurred; bullish analyst consensus is offset by bearish technical momentum, net outflows, and a slightly pressure‑filled macro backdrop.

**Main reasons it gave:**
- Technical indicators show bearish momentum (RSI 44.3, MACD negative) with low volume
- Analyst consensus is 100% buy with a +13% price target
- Fund flows indicate net outflows of -1.3% (~$569M) over the past week
- Macro backdrop: rising yields and elevated VIX suggest slight pressure on equities

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures up Pre-Bell Thursday as Traders Assess Micron's Fiscal Q4 Results](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132230485.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [These ten healthcare stocks posted the biggest one-month losses (XLV:NYSEARCA)](https://seekingalpha.com/news/4648954-these-ten-healthcare-stocks-posted-the-biggest-one-month-losses)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  September 2026 stock market update: see the worst-performing healthcare stocks and ETFs over the last month, plus key laggards to watch—read now.
- [Stocktwits Pharma Pulse: Lilly, Novo Lead A Busy Week — Here Are The Stocks And Readouts To Watch](https://stocktwits.com/news-articles/markets/equity/stocktwits-pharma-pulse-lilly-novo-lead-busy-week-stocks-readouts-to-watch/cZMSib7RBfS)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Lilly will present Phase 2 results for its eloraTZP combination at the EASD meeting in Milan. SAB BIO, Sana and Century will present type 1 diabetes...
- [Big Pharma Got Its Tariff Exemption. The Biotech ETF Barely Blinked](https://247wallst.com/investing/2026/09/30/big-pharma-got-its-tariff-exemption-the-biotech-etf-barely-blinked/)  
  <sub>24/7 Wall St., 19 hours ago</sub>  
  A 100% tariff on imported drugs just expanded to cover every drugmaker in the country, yet the biotech market's most closely watched fund treated it like a...
- [ETFs Bought $76.5 Million of Gilead Sciences (GILD) on Sept. 29](https://www.gurufocus.com/news/9105139/etfs-bought-765-million-of-gilead-sciences-gild-on-sept-29)  
  <sub>GuruFocus, 3 hours ago</sub>  
  IBB led the buying on Tuesday, adding $43.2 million of Gilead Sciences (GILD) as ETFs overall bought a net $76.5 million. Twenty-nine ETFs were buyers and...
- [Sector Update: Healthcare Stocks Fall Late Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-fall-afternoon-200040277.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Healthcare stocks declined late Wednesday afternoon with the NYSE Healthcare Index and the State Street Health Care Select Sector SPDR ETF (XLV) each...
- [Elevance Health's Quarterly Earnings Preview: What You Need to Know](https://www.inkl.com/news/elevance-healths-quarterly-earnings-preview-what-you-need-to-know)  
  <sub>inkl, 24 hours ago</sub>  
  Elevance Health is scheduled to report its third-quarter results soon, and analysts expect a double-digit earnings decline.
- [Sector Update: Healthcare Stocks Softer Wednesday Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-softer-wednesday-174030682.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Healthcare stocks declined Wednesday afternoon, with the NYSE Healthcare Index easing 0.3% and the State Street Health Care Select Sector SPDR ETF (XLV)...
- [Silver Miners Looking For A Double Correction - TalkMarkets](https://t.co/zR2SfWMzm8)  
  <sub>Howl.Link, 10 hours ago</sub>  
  The Global X Silver Miners ETF remains in a long-term bullish cycle despite a temporary pullback in its Elliott Wave sequence.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 167.29 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 168.79 (-0.9%), 50d 168.46 (-0.7%), 200d 156.66 (+6.8%); 50d above 200d
Momentum: RSI(14) 44.3 | MACD 0.178 vs signal 0.339 (histogram -0.161)
Returns: 1d -0.7% | 5d -1.5% | 1m -2.6% | 3m +2.2%
52-week range: 141.95 - 175.68 (now 75.1% of the way up)
Volatility: ATR(14) 2.36 (1.4% of price) | annualised 20d 13.6%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Health
What it holds: P/E 30.47 | P/B 4.77 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +11.7% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.91B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Eli Lilly and Co 14.9%, Johnson & Johnson 10.4%, AbbVie Inc 7.4%, Merck & Co Inc 5.9%, UnitedHealth Group Inc 5.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.64</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.64</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.0% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - JNJ: 2026-09-29 JP Morgan: main, Neutral -> Neutral
  - ABBV: 2026-09-10 HSBC: main, Buy -> Buy
  - MRK: 2026-09-29 Scotiabank: main, Sector Outperform -> Sector Outperform
  - UNH: 2026-07-21 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: -1.3% (-569.21M) over 7d
Shares outstanding: 256.47M | fund size: 42.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Technical Reactions to EWT Trends in Macro Strategies](https://news.stocktradersdaily.com/news_release/11/Technical_Reactions_to_EWT_Trends_in_Macro_Strategies_100126105802_1790866682.html)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Key findings for Ishares Msci Taiwan Etf (NYSE: EWT). Near-Term Neutral Sentiment Suggests a Stall Amid Mid and Long-Term Strength; Resistance is being...
- [Best Performing ETFs of 2026 So Far](https://www.etf.com/sections/features/best-performing-etfs-2026-so-far)  
  <sub>ETF.com, 19 hours ago</sub>  
  Tanker freight, oil and a privacy coin have joined the chip funds at the top of the leaderboard.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 112.22 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 111.73 (+0.4%), 50d 106.44 (+5.4%), 200d 88.48 (+26.8%); 50d above 200d
Momentum: RSI(14) 54.5 | MACD 1.867 vs signal 2.034 (histogram -0.167)
Returns: 1d -0.6% | 5d -0.8% | 1m +2.3% | 3m +7.0%
52-week range: 60.03 - 115.64 (now 93.9% of the way up)
Volatility: ATR(14) 2.09 (1.9% of price) | annualised 20d 27.1%
Volume: 0.35x the 20-day average
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
Three-year record: +46.1% a year | beta to the market 1.30
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
Weighted price target: +26.9% above the current prices
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
Direction: money coming in (1 week)
Share count change: 1 week: +0.8% (91.89M) over 7d
Shares outstanding: 102.69M | fund size: 11.52B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 68.45 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 72.32 (-5.3%), 50d 74.40 (-8.0%), 200d 70.57 (-3.0%); 50d above 200d
Momentum: RSI(14) 25.5 | MACD -1.413 vs signal -1.087 (histogram -0.326)
Returns: 1d -1.4% | 5d -3.5% | 1m -5.7% | 3m -8.8%
52-week range: 58.14 - 77.93 (now 52.1% of the way up)
Volatility: ATR(14) 1.22 (1.8% of price) | annualised 20d 13.9%
Volume: 0.53x the 20-day average
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
Three-year record: +21.9% a year | beta to the market 1.04
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
Ratings by weight: buy 79.5% | hold 20.5% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.0% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-10-01 Evercore ISI Group: main, In-Line -> In-Line
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - PNFP: 2026-09-30 Wells Fargo: up, Equal-Weight -> Overweight
  - UMBF: 2026-09-30 Wells Fargo: main, Equal-Weight -> Equal-Weight
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
Share count change: 1 week: +2.0% (76.47M) over 7d
Shares outstanding: 56.84M | fund size: 3.89B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [DeMark Pivot Points Signal Key Price Levels for XLY ETF on October 01, 2026](https://www.gurufocus.com/news/9105464/demark-pivot-points-signal-key-price-levels-for-xly-etf-on-october-01-2026)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 01, 2026, recent calculations using the DeMark method have identified critical pivot points for the State Street Consumer Discretionary Select...
- [Which Automaker Stock Dominated in September: Tesla, Ford, or General Motors?](https://finance.yahoo.com/markets/stocks/articles/automaker-stock-dominated-september-tesla-185328122.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Three automakers faced the same September market, yet one of them broke sharply from the pack while the other two suffered painful double-digit losses.
- [Ten consumer discretionary stocks that fell the most over the past month (XLY:NYSEARCA)](https://seekingalpha.com/news/4648678-ten-consumer-discretionary-stocks-that-fell-the-most-over-the-past-month)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  September 2026 stock market update: worst-performing consumer discretionary stocks (NAVN, RSI, MGM, BROS, DKNG) and ETF ideas—see the list now.
- [Consumer Confidence Fell to Its Lowest Level Since 2014 and Consumer Stocks Are Already Paying for It](https://247wallst.com/investing/2026/09/30/consumer-confidence-fell-to-its-lowest-level-since-2014-and-consumer-stocks-are-already-paying-for-it/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Consumer confidence just hit its worst level in over a decade, yet the stocks that depend on American shoppers are barely flinching.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 108.12 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 111.51 (-3.0%), 50d 114.35 (-5.4%), 200d 116.43 (-7.1%); 50d below 200d
Momentum: RSI(14) 32.0 | MACD -1.748 vs signal -1.519 (histogram -0.229)
Returns: 1d -0.7% | 5d -2.0% | 1m -5.6% | 3m -7.7%
52-week range: 105.66 - 124.52 (now 13.0% of the way up)
Volatility: ATR(14) 1.49 (1.4% of price) | annualised 20d 14.7%
Volume: 0.38x the 20-day average
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
Three-year record: +11.6% a year | beta to the market 1.16
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
Weighted price target: +27.5% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-30 Rosenblatt: main, Buy -> Buy
  - TSLA: 2026-09-28 JP Morgan: main, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-29 JP Morgan: main, Overweight -> Overweight
  - BKNG: 2026-09-30 Truist Securities: main, Buy -> Buy
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
Share count change: 1 week: +3.0% (650.67M) over 7d
Shares outstanding: 208.78M | fund size: 22.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Crowded long position in SUGAR futures (100% percentile, net long 18.9%)
- Fund outflows of -0.7% over the past week
- Heavy cost of holding (-8.9% annualized) indicating roll cost drag
- Technicals show price above 20d, 50d, 200d SMAs but no decisive break
- Macro: yields rising modestly, USD stronger, VIX up modestly (no surprise)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.40 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 11.35 (+0.5%), 50d 10.91 (+4.6%), 200d 9.97 (+14.4%); 50d above 200d
Momentum: RSI(14) 56.3 | MACD 0.076 vs signal 0.109 (histogram -0.033)
Returns: 1d +1.3% | 5d +1.2% | 1m -1.4% | 3m +16.7%
52-week range: 9.02 - 11.82 (now 85.2% of the way up)
Volatility: ATR(14) 0.19 (1.7% of price) | annualised 20d 20.8%
Volume: 0.27x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.7%, commodity +26.3%, gap -9.5% | 6 months: fund +10.9%, commodity +22.6%, gap -11.7% | 12 months: fund +7.6%, commodity +16.5%, gap -8.9%
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 18.9% of open interest (1,147,767 contracts)
Change on the week: +0.4% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.7% (-417.85K) over 7d
Shares outstanding: 5.18M | fund size: 59.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields modestly up, inflation and unemployment stable
- Technical indicators show price below 20‑day and 50‑day SMA, RSI 37.2, MACD negative, indicating bearish short‑term momentum
- Fund flows positive: share count +3.2% over 7 days, indicating demand for exposure
- Cost of holding heavy: -11% annual drag on long positions, tailwind for short
- Positioning crowded long (95th percentile) with net long 21.8% and slight weekly reduction (-0.7%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 18.90 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 19.80 (-4.5%), 50d 19.05 (-0.8%), 200d 18.13 (+4.3%); 50d above 200d
Momentum: RSI(14) 37.2 | MACD 0.015 vs signal 0.192 (histogram -0.177)
Returns: 1d -0.7% | 5d -3.9% | 1m -6.8% | 3m +12.1%
52-week range: 16.47 - 20.29 (now 63.7% of the way up)
Volatility: ATR(14) 0.33 (1.7% of price) | annualised 20d 16.4%
Volume: 0.32x the 20-day average
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
Cost of holding this fund instead of corn itself: -11.0% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +12.1%, commodity +16.7%, gap -4.6% | 6 months: fund +4.0%, commodity +9.2%, gap -5.2% | 12 months: fund +8.3%, commodity +19.4%, gap -11.0%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

```text
Corn rated good or excellent: 57% of the US crop (week 39 of 2026)
Direction over 3 weeks: steady, 0 points
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
Share count change: 1 week: +3.2% (4.88M) over 7d
Shares outstanding: 8.43M | fund size: 159.30M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields rose modestly, Fed policy unchanged
- Technical indicators mixed: price below 20d/50d SMA, above 200d SMA, RSI 46.3
- Positioning net long 27.4% of OI with weekly increase +4.9% (moderate crowding)
- Cost of holding -5.1% annual, heavy roll cost tailwinds short

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.41 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 39.89 (-1.2%), 50d 39.75 (-0.9%), 200d 37.41 (+5.3%); 50d above 200d
Momentum: RSI(14) 46.3 | MACD 0.079 vs signal 0.142 (histogram -0.063)
Returns: 1d -0.9% | 5d -3.1% | 1m +0.9% | 3m +5.7%
52-week range: 30.15 - 41.43 (now 82.1% of the way up)
Volatility: ATR(14) 0.67 (1.7% of price) | annualised 20d 28.3%
Volume: 0.36x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +5.7%, commodity +7.2%, gap -1.5% | 6 months: fund +14.8%, commodity +16.6%, gap -1.8% | 12 months: fund +31.4%, commodity +36.4%, gap -5.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 27.4% of open interest (301,657 contracts)
Change on the week: +4.9% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.8% (13.47M) over 7d
Shares outstanding: 18.85M | fund size: 742.82M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Price below 20‑day, 50‑day and 200‑day SMAs, RSI 40, MACD negative – bearish technicals
- US Treasury yields rising and market pricing ~4 quarter‑point hikes, higher rates pressure silver
- Cost of holding drag -2.5% annual, a negative factor for long exposure
- Large speculators net long 12.5% of open interest but down 0.2% week‑over‑week, indicating no strong bullish crowding
- Share count increased 7.4% in one week, showing inflow demand

<details><summary><b>News</b> — score +0.00</summary>

- [Wall Street Veteran Says Gold, Silver Charts "Among the Worst" — Are Inverse ETFs the Answer?](https://finance.biggo.com/news/94622f80-d782-43ec-91c8-2d82b5619c91)  
  <sub>BigGo Finance, 11 hours ago</sub>  
  Wall Street veteran investor Rob Isbitts, former CIO, has warned of further downside in gold and silver prices, suggesting investors consider inverse ETFs.
- [COMEX Silver Drawdown Partially Reversed Last Week](https://seekingalpha.com/article/4951114-comex-silver-drawdown-partially-reversed-last-week)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Last week, silver flowed back into the COMEX system, partially reversing the drawdown. During the week of Sept 18-25, around 2.5 million ounces of silver...
- [Current price of silver as of Wednesday, Sept. 30, 2026](https://fortune.com/article/current-price-of-silver-9-30-2026/)  
  <sub>Fortune, 21 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [As the global high-interest rate trend strengthens, even gold and silver prices, which are called th..](https://www.mk.co.kr/en/stock/12165732)  
  <sub>매일경제, 14 hours ago</sub>  
  International gold futures traded on the New York Mercantile Exchange (COMEX) are trading around 4,200 dollars per ounce, according to Investing.
- [Gold price will break $5,000/oz in H2 2027, and silver’s run to $120 was driven by more than hype – Morgan Stanley’s Gower](https://www.kitco.com/news/article/2026-09-30/gold-price-will-break-5000oz-h2-2027-and-silvers-run-120-was-driven-more)  
  <sub>Kitco, 24 hours ago</sub>  
  (Kitco News) – Gold prices may be under pressure at the moment, but ETF and central bank demand has stayed strong, and the yellow metal will be trading back...
- [News by CNBC TV18 on TradingView, 2026-10-01 — cnbctv:b163803e3094b:0](https://www.tradingview.com/news/cnbctv:b163803e3094b:0/)  
  <sub>TradingView, 13 hours ago</sub>  
  Gold prices were largely steady in early trade on October 1, while silver gained, as investors continued to assess the outlook for US interest rates,...
- [Best Silver ETFs In India Explained For Beginners](https://theprint.in/brandit/best-silver-etfs-in-india-explained-for-beginners/3059040/?amp)  
  <sub>ThePrint, 6 hours ago</sub>
- [Mirae Asset Silver ETF FOF(G)-Direct Plan](https://univest.in/mutual-funds/mirae-asset-silver-etf-fof-g-direct-plan)  
  <sub>Univest, 22 hours ago</sub>  
  Mirae Asset Silver ETF FOF(G)-Direct Plan details: NAV ₹9.783, AUM 33 Cr, Expense Ratio 0.0%. Check returns, holdings, sector allocation, and fund manager...
- [Gold Rate Today in Delhi 1st October 2026 : 22 & 24 Carat, Todays Gold Price in Delhi](https://www.businesstoday.in/commodity/gold-rate-in-delhi-today)  
  <sub>Business Today, 2 hours ago</sub>  
  Gold rate in Delhi on Thursday, Oct 01, 2026 : Today, the price of 24-carat Gold in Delhi is ₹1,49,580 per 10 grams. A day earlier, on Sep 30, 2026,...
- [Silver Rate Today in Bundi 1st October 2026 : 1 KG, Todays Silver Price in Bundi](https://www.businesstoday.in/commodity/silver-rate-in-bundi-today)  
  <sub>Business Today, 12 hours ago</sub>  
  Silver Price in Bundi Today 1st October 2026: Find updated 1 KG Silver rate today in Bundi 1st October 2026. Also check latest gold price related news,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 54.77 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 58.02 (-5.6%), 50d 57.68 (-5.0%), 200d 65.93 (-16.9%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -0.857 vs signal -0.305 (histogram -0.551)
Returns: 1d +0.5% | 5d -4.9% | 1m -5.4% | 3m -0.5%
52-week range: 42.40 - 105.60 (now 19.6% of the way up)
Volatility: ATR(14) 1.70 (3.1% of price) | annualised 20d 39.7%
Volume: 0.37x the 20-day average
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
Cost of holding this fund instead of silver itself: -2.5% a year -- a steady drag
Measured: 3 months: fund -0.5%, commodity +0.5%, gap -0.9% | 6 months: fund -19.6%, commodity -19.7%, gap +0.1% | 12 months: fund +29.3%, commodity +31.7%, gap -2.5%
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 12.5% of open interest (106,474 contracts)
Change on the week: -0.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +7.4% (2.37B) over 7d
Shares outstanding: 626.18M | fund size: 34.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals mixed, positioning crowded but no clear directional signal, fund flows positive but not decisive, crop condition steady.

**Main reasons it gave:**
- Positioning: net long 23.8% of OI, +1.9% change, 97th percentile crowding
- Fund flows: share count +2.7% (money coming in)
- Technicals: price below 20‑day SMA, MACD below signal, low volume
- Macro: yields up modestly, dollar index up, VIX elevated – no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.20 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 27.77 (-2.0%), 50d 26.63 (+2.1%), 200d 24.60 (+10.6%); 50d above 200d
Momentum: RSI(14) 47.0 | MACD 0.219 vs signal 0.373 (histogram -0.154)
Returns: 1d -1.1% | 5d -2.6% | 1m -2.1% | 3m +11.3%
52-week range: 21.56 - 28.14 (now 85.7% of the way up)
Volatility: ATR(14) 0.34 (1.3% of price) | annualised 20d 15.9%
Volume: 0.29x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.7% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +11.3%, commodity +12.8%, gap -1.5% | 6 months: fund +11.8%, commodity +9.2%, gap +2.5% | 12 months: fund +26.7%, commodity +27.4%, gap -0.7%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.00</summary>

```text
Soybeans rated good or excellent: 58% of the US crop (week 39 of 2026)
Direction over 3 weeks: steady, 0 points
Same week last year: 62% (-4 points)
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
Direction: money coming in (1 week)
Share count change: 1 week: +2.7% (1.19M) over 7d
Shares outstanding: 1.69M | fund size: 46.05M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, policy shift, or decisive technical break observed. While bearish pressures exist (net short increase, fund outflows, heavy cost of carry, inventory build), the lack of a material catalyst warrants a neutral stance.

**Main reasons it gave:**
- CFTC net short increased by 1.9% of open interest (week change)
- Fund outflows of -3.7% over the past week
- Heavy cost of holding at -12.3% annualized
- US natural gas inventories built 64 BCF, 79th percentile (bearish)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 10.28 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 10.52 (-2.2%), 50d 10.28 (+0.0%), 200d 11.37 (-9.5%); 50d below 200d
Momentum: RSI(14) 46.0 | MACD 0.067 vs signal 0.102 (histogram -0.035)
Returns: 1d -0.8% | 5d -11.0% | 1m -2.8% | 3m -11.2%
52-week range: 9.63 - 16.90 (now 9.0% of the way up)
Volatility: ATR(14) 0.35 (3.4% of price) | annualised 20d 43.9%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.45</summary>

```text
Cost of holding this fund instead of natural gas itself: -12.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -11.2%, commodity -6.0%, gap -5.2% | 6 months: fund -9.9%, commodity +6.6%, gap -16.5% | 12 months: fund -21.3%, commodity -9.0%, gap -12.3%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.45</summary>

```text
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Natural gas: 3,415.0 billion cubic feet, +64.0 on the week (a build), 79% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.45</summary>

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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 3.6% of open interest (1,837,146 contracts)
Change on the week: +1.9% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -3.7% (-21.37M) over 7d
Shares outstanding: 54.24M | fund size: 557.88M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, mixed fundamentals and positioning, overall neutral stance.

**Main reasons it gave:**
- EIA forecast WTI $87 vs USO price $149, bearish outlook
- CFTC shows net long 5.5% of OI, 98th percentile crowding (potential reversal risk)
- Crude oil inventories up 0.9% to 427.3M barrels (high level) – bearish
- US forces resume maritime blockade of Iran, potential supply shock – bullish
- Fund flows flat with -0.3% share count change (small outflow) – bearish

<details><summary><b>News</b> — score +0.00</summary>

- [Best Performing ETFs of 2026 So Far](https://www.etf.com/sections/features/best-performing-etfs-2026-so-far)  
  <sub>ETF.com, 19 hours ago</sub>  
  Tanker freight, oil and a privacy coin have joined the chip funds at the top of the leaderboard.
- [Oil Prices Surge Nearly 10% — US Forces To Resume Maritime Blockade Against Iran On Tuesday](https://stocktwits.com/news-articles/markets/equity/oil-prices-surge-10-percent-us-forces-to-resume-maritime-blockade-against-iran-on-tuesday/cZmz6rZR7Yo)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The U.S. Central Command said U.S. forces will enforce the blockade on vessels entering or leaving Iranian ports starting July 14 at 4 p.m. ET.
- [Make Or Break for AI Trade–Micron Earnings Ahead; Consumers Spend More Even As Income Drops](https://www.benzinga.com/Opinion/26/09/62087536/make-or-break-for-ai-trade-micron-earnings-ahead-consumers-spend-more-even-as-income-drops)  
  <sub>Benzinga, 22 hours ago</sub>  
  Micron Earnings Ahead Please click here for an enlarged chart of Micron Technology Inc (NASDAQ:MU). Note the following: This article is about the big...
- [Mobix Labs In Retail Radar After Reverse Split, F-22 Order - MOBX Stock Falls 5%](https://stocktwits.com/news-articles/markets/equity/why-did-mobx-stock-crash-25-in-pre-market-today/cZ7xpDoRI85)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Mobix Labs announced a 1-for-10 reverse stock split, effective on April 6.
- [U.S. reportedly tells France, Germany to release diesel inventories or face export ban](https://seekingalpha.com/news/4649078-us-reportedly-tells-france-germany-to-release-diesel-inventories-or-face-export-ban)  
  <sub>Seeking Alpha, 54 minutes ago</sub>  
  The Trump administration has told France and Germany to draw down emergency diesel stockpiles to ease global fuel prices or face a potential US diesel...
- [Brent crude oil price for October: Will it crash to $80 or surge to $120?](https://invezz.com/en-ae/news/2026/10/01/brent-crude-oil-price-for-october-will-it-crash-to-dollar80-or-surge-to-dollar120/)  
  <sub>Invezz, 8 hours ago</sub>  
  Crude oil prices have pulled back in the past two weeks as investors focused on reports of the rising flows through the Strait of Hormuz.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 149.13 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 150.39 (-0.8%), 50d 137.19 (+8.7%), 200d 114.77 (+29.9%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD 2.942 vs signal 4.463 (histogram -1.521)
Returns: 1d +2.4% | 5d -2.6% | 1m +5.8% | 3m +43.4%
52-week range: 66.17 - 161.86 (now 86.7% of the way up)
Volatility: ATR(14) 5.30 (3.6% of price) | annualised 20d 45.4%
Volume: 0.30x the 20-day average
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
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Crude oil: 427.3 million barrels, +0.9 on the week (a build), 62% percentile over 52 weeks
  Petrol: 204.4 million barrels, -1.7 on the week (a draw), 2% percentile over 52 weeks -- low for the time of year
  Diesel: 105.2 million barrels, -2.3 on the week (a draw), 23% percentile over 52 weeks
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 5.5% of open interest (1,841,811 contracts)
Change on the week: +0.1% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.3% (-5.84M) over 7d
Shares outstanding: 12.74M | fund size: 1.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals mixed with no decisive break, positioning shows modest net short but decreasing, heavy cost of holding tailwinds short, fund inflows support demand. Overall balance leads to a neutral call.

**Main reasons it gave:**
- Positioning: net short fell 1.7% of open interest this week
- Cost of holding: -12.9% annual gap (heavy carry)
- Technicals: price 24.60 below 20‑day SMA (25.96) and 50‑day SMA (25.52)
- Fund flows: share count increased 5.1% (17.28M) over the week
- Macro: no rate or policy surprise; yields modestly up, VIX up 1.5 points

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 24.60 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 25.96 (-5.2%), 50d 25.52 (-3.6%), 200d 23.16 (+6.2%); 50d above 200d
Momentum: RSI(14) 36.5 | MACD -0.277 vs signal -0.024 (histogram -0.253)
Returns: 1d +0.1% | 5d -3.8% | 1m -12.1% | 3m +9.8%
52-week range: 19.88 - 28.00 (now 58.1% of the way up)
Volatility: ATR(14) 0.55 (2.2% of price) | annualised 20d 22.8%
Volume: 0.45x the 20-day average
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
Cost of holding this fund instead of wheat itself: -12.9% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +9.8%, commodity +14.1%, gap -4.3% | 6 months: fund +7.8%, commodity +12.8%, gap -5.0% | 12 months: fund +19.7%, commodity +32.6%, gap -12.9%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 2.5% of open interest (483,279 contracts)
Change on the week: -1.7% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +5.1% (17.28M) over 7d
Shares outstanding: 14.50M | fund size: 356.75M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [GLD: Gold’s Structural Bull Market Is Intact, But The Insurance Premium Is Now Expensive](https://seekingalpha.com/article/4951304-gld-golds-structural-bull-market-is-intact-but-the-insurance-premium-is-now-expensive)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  SPDR Gold Shares ETF's structural bull case remains intact, but at roughly $4,284/oz, gold already embeds a historically elevated insurance premium.
- [Gold's structural bull case holds, but high pri...](https://pluang.com/en/news-feed/gld-pasar-bull-emas-struktural-tetap-tapi-premi-asuransi-mahal)  
  <sub>Pluang, 3 hours ago</sub>  
  Gold remains a strong long-term store of value, supported by central bank actions and private investment demand. However, at around $4284 per ounce,...
- [NUGT: Strong Employment Data May Be Bad For Gold (NYSEARCA:NUGT)](https://seekingalpha.com/article/4951169-nugt-strong-employment-data-may-be-bad-for-gold)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Bearish NUGT outlook: strong jobs data may drive rate hikes, pressuring gold and leveraged miners. Learn more about the NUGT ETF here.
- [Bitcoin ETFs Draw $1.32B Amid Record Gold Outflows](https://yellow.com/news/bitcoin-etf-inflows-gold-outflows)  
  <sub>Yellow.com, 20 hours ago</sub>  
  Bloomberg analyst James Seyffart argues Bitcoin ETFs...
- [Don't Quit AI, Insure It: A 10-ETF Diversification Portfolio (NASDAQ:QQQ)](https://seekingalpha.com/article/4951263-dont-quit-ai-insure-it-a-10-etf-diversification-portfolio)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  My 10-ETF portfolio reduces maximum drawdown to ~7.9% versus ~40% for the AI portfolio. Read why I advocate a 10-ETF diversified portfolio as a hedge.
- [Gold prices stall near $4,160 despite $3.8 billion ETF inflows: here’s why](https://invezz.com/ng/news/2026/10/01/gold-prices-stall-near-dollar4160-despite-dollar38-billion-etf-inflows-heres-why/)  
  <sub>Invezz, 10 hours ago</sub>  
  Gold prices steadied near $4,160 an ounce even as billions of dollars continued flowing into bullion-backed exchange-traded funds, exposing a divide between...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.01% (-0.06 on the week) | 5-year 5.08% (+0.05 on the week) | 10-year 5.31% (+0.15 on the week) | 30-year 5.66% (+0.20 on the week)
Yield curve, 10-year minus 3-month: +1.30 points -- upward sloping (normal)
US dollar index: 101.76 (+0.47 on the week)
Volatility (VIX): 17.13 (+1.5 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.89% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 381.36 (bar of 2026-10-01), from 502 daily bars
Trend: vs 20d SMA 394.64 (-3.4%), 50d 396.09 (-3.7%), 200d 416.23 (-8.4%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -4.874 vs signal -2.729 (histogram -2.145)
Returns: 1d +0.1% | 5d -2.6% | 1m -3.9% | 3m +0.9%
52-week range: 354.79 - 495.90 (now 18.8% of the way up)
Volatility: ATR(14) 6.90 (1.8% of price) | annualised 20d 22.4%
Volume: 0.21x the 20-day average
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
Measured: 3 months: fund +0.9%, commodity +1.4%, gap -0.5% | 6 months: fund -12.9%, commodity -13.1%, gap +0.2% | 12 months: fund +7.3%, commodity +8.0%, gap -0.7%
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
Shares outstanding: 260.30M | fund size: 99.27B
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

