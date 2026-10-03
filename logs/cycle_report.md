# Daily report

**02 Oct 2026, 18:38 Israel time (15:38 UTC)** · 80 names checked · 2 traded · 1 with a problem

**Answers with no explanation:** 14 of 61 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 4 | 12 | 0 |
| Whole-market funds | 14 | 1 | 13 | 0 |
| Sector and country funds | 41 | 1 | 39 | 1 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| ASML (ASML) · Company | **Stop raised.** At +1.30R, following the price. Stop-loss raised 1733.63 → 1764.83. |
| Caterpillar (CAT) · Company | **Stop raised.** At +0.75R, following the price. Stop-loss raised 780.92 → 795.82. |
| Taiwan (EWT) · Sector or country | **Stop raised.** At +0.37R, following the price. Stop-loss raised 110.28 → 112.03. |
| Microsoft (MSFT) · Company | **Stop raised.** At +1.22R, following the price. Stop-loss raised 493.66 → 493.77. |
| Nvidia (NVDA) · Company | **Stop raised.** At +1.69R, following the price. Stop-loss raised 219.12 → 225.46. |
| Novo Nordisk (NVO) · Company | **Stop raised.** At +0.77R, following the price. Stop-loss raised 39.81 → 39.69. |
| Developing country bonds (EMB) · Index fund | **Holding.** +3.77R, holding 44 shares. Stop-loss 91.07. |
| Gold (GLD) · Commodity | **Holding.** +0.41R, holding 10 shares. Stop-loss 393.48. |
| HDFC Bank (HDB) · Company | **Holding.** -0.67R, holding 90 shares. Stop-loss 22.23. |
| US government bonds, 7-10 years (IEF) · Index fund | **Holding.** +2.24R, holding 80 shares. Stop-loss 89.90. |
| Eli Lilly (LLY) · Company | **Holding.** +0.12R, holding 4 shares. Stop-loss 1130.70. |
| S&P 500, equal weight (RSP) · Index fund | **Holding.** +0.43R, holding 10 shares. Stop-loss 211.49. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.04R, holding 128 shares. Stop-loss 37.20. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +2.45R, holding 4 shares. Stop-loss 104.79. |
| US government bonds, 20+ years (TLT) · Index fund | **Holding.** +2.26R, holding 90 shares. Stop-loss 78.88. |
| US dollar (UUP) · Index fund | **Holding.** +2.23R, holding 282 shares. Stop-loss 28.65. |
| US shopping and leisure (XLY) · Sector or country | **Holding.** -0.09R, holding 63 shares. Stop-loss 111.36. |
| Exxon Mobil (XOM) · Company | **Holding.** +0.20R, holding 13 shares. Stop-loss 156.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### MercadoLibre (MELI) · Company — BEARISH, confidence 0.58

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The technicals show clear weakness (price below key SMAs, low RSI, negative MACD, and thin volume) and fundamentals are strained by high leverage and expensive valuation. The earnings record is poor with three misses out of four quarters, outweighing the modest bullish signals from analyst consensus and insider buying. Overall, the balance of evidence points to a moderate probability of a near‑term downside move.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day and 200‑day SMAs; RSI 35.4; MACD negative; volume 0.17× 20‑day avg
- Fundamentals: debt/equity 168.6% and forward P/E 30.5 indicate high leverage and expensive valuation
- Earnings record: 3 of last 4 quarters missed consensus, showing weak earnings momentum
- Analyst view: consensus strong‑buy already reflected; no fresh upgrade despite $2,266 mean target

<details><summary><b>News</b> — score +0.00</summary>

- [MercadoLibre (MELI) Stock Falls Amid Market Uptick: What Investors Need to Know](https://finance.yahoo.com/markets/stocks/articles/mercadolibre-meli-stock-falls-amid-205004724.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  MercadoLibre (MELI) closed at $1,685.12 in the latest trading session, marking a -2.51% move from the prior day. The stock trailed the S&P 500,...
- [Why MercadoLibre (MELI) Stock Is Down Today](https://www.quiverquant.com/news/Why+MercadoLibre+%28MELI%29+Stock+Is+Down+Today)  
  <sub>Quiver Quantitative, 23 hours ago</sub>  
  MercadoLibre (MELI) is down 3.0% today. Here is some analysis on what might have caused this price m.
- [Sea Limited (SE) stock price, news, quote and history](https://au.finance.yahoo.com/quote/SE/latest-news/)  
  <sub>Yahoo Finance Australia, 4 hours ago</sub>  
  Find the latest Sea Limited (SE) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [New Street starts coverage of MercadoLibre stock with USD 2,450 target](https://www.ad-hoc-news.de/boerse/news/corporate-news/new-street-starts-coverage-of-mercadolibre-stock-with-usd-2-450-target/70215769)  
  <sub>AD HOC NEWS, 2 hours ago</sub>  
  MELI, US58733R1023. New Street starts coverage of MercadoLibre stock with USD 2,450 target. Published on 10/02/2026 at 15:02 | Editorial responsibility:...
- [MELI261002C01740000 Interactive Stock Chart | MELI Oct 2026 1740.000 call Stock](https://ca.finance.yahoo.com/chart/MELI261002C01740000)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MercadoLibre stock after-hours at EUR 1,491.70: minus 2.35 percent versus Lang & Schwarz prior close](https://www.ad-hoc-news.de/boerse/news/nachboerse/mercadolibre-stock-after-hours-at-eur-1-491-70-minus-2-35-percent-versus/70211581)  
  <sub>AD HOC NEWS, 23 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock after-hours at EUR 1,491.70: minus 2.35 percent versus Lang & Schwarz prior close. Published on 10/01/2026 at 17:52...
- [MELI290119C01700000 Interactive Stock Chart | MELI Jan 2029 1700.000 call Stock](https://finance.yahoo.com/chart/MELI290119C01700000)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI261120P02020000 Interactive Stock Chart | MELI Nov 2026 2020.000 put Stock](https://finance.yahoo.com/chart/MELI261120P02020000)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,707.21 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 1,813.86 (-5.9%), 50d 1,860.47 (-8.2%), 200d 1,837.67 (-7.1%); 50d above 200d
Momentum: RSI(14) 35.4 | MACD -49.524 vs signal -35.215 (histogram -14.310)
Returns: 1d +1.3% | 5d -2.6% | 1m -14.9% | 3m -5.5%
52-week range: 1,546.81 - 2,360.76 (now 19.7% of the way up)
Volatility: ATR(14) 55.08 (3.2% of price) | annualised 20d 25.9%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 86.55B
Valuation: trailing P/E 46.37 | forward P/E 30.54 | P/B 11.05 | PEG 1.00
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 5 strong buy, 17 buy, 4 hold, 0 sell, 0 strong sell
Price target: mean 2,266.09 (+32.7% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

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

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Fundamentals are strong (high ROE, solid margins, low debt) and the stock trades above key moving averages, while recent AI‑related news (Gemini 4 Argon launch) is largely positive. Earnings have been mixed with recent misses, and insider activity is neutral, tempering the view. Overall, a modest bullish stance with moderate conviction is warranted.

**Main reasons it gave:**
- Gemini 4 Argon AI model launch (news)
- Trailing P/E 17.31 and ROE 48.7% indicate strong fundamentals (fundamentals)
- Price above 20‑day SMA; RSI 51 (technical)
- Analyst consensus strong buy, mean target $429.36 (+24.5%) (analyst view)
- Earnings record: 2 beats, 2 misses; recent two quarters missed (earnings)

<details><summary><b>News</b> — score +0.20</summary>

- [Alphabet (GOOGL) Stock May Be 30% Below Fair Value After Cloud Backlog News](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/alphabet-googl-stock-may-be-30-below-fair-value-after-cloud)  
  <sub>Simply Wall Street, 5 hours ago</sub>  
  Alphabet has delivered a 152.8% gain over the past 3 years, and with the stock recently closing at US$338.24, the key question for investors is whether that...
- [GOOGL Stock Rises After Gemini 4 Argon Launch, But JPMorgan Says Google Must Reclaim AI Leadership](https://stocktwits.com/news-articles/markets/equity/googl-stock-gemini-4-argon-launch-reclaim-leadership/cZD05VWRBip)  
  <sub>Stocktwits, 5 hours ago</sub>  
  Alphabet (GOOG, GOOGL) shares rose Thursday after Google unveiled Gemini 4 Argon, its latest frontier AI model, with JPMorgan saying the launch could help...
- [Alphabet (GOOGL) Stock Sinks As Market Gains: What You Should Know](https://sg.finance.yahoo.com/news/alphabet-googl-stock-sinks-market-204505741.html)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  Alphabet (GOOGL) concluded the recent trading session at $338.24, signifying a -1.7% move from its prior day's close.
- [J.P. Morgan Remains a Buy on Alphabet Class A (GOOGL)](https://www.theglobeandmail.com/investing/markets/stocks/GOOG-Q/pressreleases/4926121/j-p-morgan-remains-a-buy-on-alphabet-class-a-googl/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Alphabet Cl C (GOOG-Q) from The Globe and Mail including charting and trades.
- [JPMorgan sets Google stock price target](https://finbold.com/jpmorgan-sets-google-stock-price-target/)  
  <sub>Finbold, 5 hours ago</sub>  
  Despite retracing 16% from the May highs, Google (NASDAQ: GOOGL) stock remains more than 7% in the green in 2026 and, per JPMorgan's (NYSE: JPM) assessment,...
- [The Trump Administration Is Launching America.gov Using Models From Alphabet and SpaceX. GOOGL Stock Is the Better Buy.](https://www.barchart.com/story/news/4927077/the-trump-administration-is-launching-america-gov-using-models-from-alphabet-and-spacex-googl-stock-is-the-better-buy)  
  <sub>Barchart.com, 3 hours ago</sub>  
  The Trump administration launched America.gov on Sept. 29, a federal chatbot built with models from Alphabet and SpaceX, putting both companies' AI...
- [Will Google Turn The Tables In AI Race? Wall Street Reacts To Gemini 4.](https://www.investors.com/news/technology/google-stock-wall-street-reaction-gemini4-artificial-intellience-model/)  
  <sub>Investor's Business Daily, 20 hours ago</sub>  
  Wall Street mulled Alphabet's release of a new artificial-intelligence model, called Gemini 4 Argon, after delays. Google stock fell.
- [Why Is Alphabet (NASDAQ:GOOGL) Stock Falling Despite the Gemini 4 Argon Launch? Analysts Stay Bullish](https://stocksdownunder.com/why-alphabet-googl-stock-falling-gemini-argon/)  
  <sub>Stocks Down Under, 20 hours ago</sub>  
  Alphabet stock fell about 1.3% despite Google launching Gemini 4 Argon. Here's why GOOGL is down and why analysts remain bullish.
- [Google Turns Up AI Heat With Gemini 4 Argon, Rivals May Have to Cut Prices: Analyst](https://www.benzinga.com/markets/tech/26/10/62129995/google-turns-up-ai-heat-with-gemini-4-argon-rivals-may-have-to-cut-prices-analyst)  
  <sub>Benzinga, 3 hours ago</sub>  
  Analysts say Google's Gemini 4 Argon launch proves its ecosystem & infrastructure give Alphabet a major advantage in the AI race.
- [Google, Planet Labs launch prototype AI satellite on SpaceX rocket (GOOG:NASDAQ)](https://seekingalpha.com/news/4649711-google-planet-labs-launch-prototype-ai-satellite-on-spacex-rocket)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Google's Project Suncatcher satellite reached orbit with SpaceX, testing TPUs for scalable space-based machine learning.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 344.78 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 342.68 (+0.6%), 50d 344.39 (+0.1%), 200d 338.92 (+1.7%); 50d above 200d
Momentum: RSI(14) 51.0 | MACD -0.444 vs signal -0.377 (histogram -0.067)
Returns: 1d +1.9% | 5d +0.3% | 1m +2.3% | 3m -5.9%
52-week range: 236.57 - 402.62 (now 65.2% of the way up)
Volatility: ATR(14) 8.97 (2.6% of price) | annualised 20d 26.3%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.22T
Valuation: trailing P/E 17.31 | forward P/E 22.88 | P/B 6.77 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.50</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.36 (+24.5% vs last close), range 340.00 - 515.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### JPMorgan Chase (JPM) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The company shows strong fundamentals, a solid earnings beat record, and a positive analyst consensus with a sizable price‑target upside. Institutional buying (West Family Investments) adds a bullish news element, while technicals are currently weak (price below short‑term averages, low volume) which tempers conviction to a moderate level.

**Main reasons it gave:**
- 4 consecutive earnings beats (last 4 quarters)
- Strong fundamentals: trailing P/E 14.2, profit margin 34.9%, revenue growth +30.4% YoY
- Analyst consensus buy with mean price target $375.81 (+13% vs last close)
- West Family Investments increased stake by 92% in Q2

<details><summary><b>News</b> — score +0.20</summary>

- [JPMorgan Chase & Co. $JPM Stock Bought by West Family Investments Inc.](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-bought-by-west-family-investments-inc-2026-10-02/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  West Family Investments Inc. increased its stake in JPMorgan Chase & Co. (NYSE:JPM) by 92.0% during the 2nd quarter, according to the company in its most...
- [JPMorgan Chase (JPM) Taps Bond Markets, Is The Stock Fully Priced?](https://simplywall.st/stocks/us/banks/nyse-jpm/jpmorgan-chase/news/jpmorgan-chase-jpm-taps-bond-markets-is-the-stock-fully-pric)  
  <sub>Simply Wall Street, 11 hours ago</sub>  
  JPMorgan Chase (JPM) has been active in the bond market, completing and announcing a series of fixed income offerings across maturities from 2030 to 2056,...
- [Why Did IMAX, JPM, CSX Stocks Surge To 52-Week Highs Last Week?](https://stocktwits.com/news-articles/markets/equity/imax-jpm-csx-stocks-52-week-highs-last-week/cZZxcQ3R7C3)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Why Did IMAX, JPM, CSX Stocks Surge To 52-Week Highs Last Week? · IMAX stock jumped to a 52-week high of $45.88 after it received a series of price target hikes...
- [JPM Forecast — Price Target — Prediction for 2027](https://www.tradingview.com/symbols/BCBA-JPM/forecast-price-target/)  
  <sub>TradingView, 4 hours ago</sub>  
  See JPMorgan Chase & Co Shs Cert Deposito Arg Repr 0.06666667 Sh price prediction for 2027 made by analysts and compare to the performance for the past 2...
- [JPMorgan Chase (JPM) Taps Bond Markets, Is The Stock Still Undervalued?](https://finance.yahoo.com/markets/stocks/articles/jpmorgan-chase-jpm-taps-bond-180942734.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  JPMorgan Chase (JPM) has been active in the bond market, completing a series of small to mid sized fixed income offerings across multiple maturities.
- [RBC Capital Keeps Their Buy Rating on JPMorgan Chase (JPM)](https://www.theglobeandmail.com/investing/markets/stocks/JPM/pressreleases/4919946/rbc-capital-keeps-their-buy-rating-on-jpmorgan-chase-jpm/)  
  <sub>The Globe and Mail, 13 hours ago</sub>  
  Detailed price information for JP Morgan Chase & Company (JPM-N) from The Globe and Mail including charting and trades.
- [JPMorgan Chase & Co. (NYSE:JPM) Stock Has Average Price Target of $363.29](https://www.marketbeat.com/instant-alerts/consensus-jpmorgan-chase-co-nyse-jpm-stock-has-average-price-target-of-36329-2026-10-02/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Shares of JPMorgan Chase & Co. (NYSE:JPM) have been assigned an average rating of "Moderate Buy" from the twenty-eight analysts that are covering the stock,...
- [JPMorgan sets Google stock price target](https://finbold.com/jpmorgan-sets-google-stock-price-target/)  
  <sub>Finbold, 5 hours ago</sub>  
  Despite retracing 16% from the May highs, Google (NASDAQ: GOOGL) stock remains more than 7% in the green in 2026 and, per JPMorgan's (NYSE: JPM) assessment,...
- [Bank Stocks Slide as Money-Center Names Lead Financials Lower: Citigroup Falls 4%, Bank of America Drops 3%, JPMorgan Chase Slips](https://247wallst.com/investing/2026/10/01/bank-stocks-slide-as-money-center-names-lead-financials-lower-citigroup-falls-4-bank-of-america-drops-3-jpmorgan-chase-slips/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Citigroup is getting hit harder than Bank of America despite the legal headline landing at Merrill Lynch, and the gap between the two lenders points to...
- [JPMorgan Chase & Co. $JPM Stock Bought by RFG Advisory LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-bought-by-rfg-advisory-llc-2026-10-02/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  RFG Advisory LLC lifted its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 9.2% during the 2nd quarter, according to its most recent...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 332.07 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 345.30 (-3.8%), 50d 352.23 (-5.7%), 200d 321.77 (+3.2%); 50d above 200d
Momentum: RSI(14) 34.2 | MACD -5.622 vs signal -3.966 (histogram -1.656)
Returns: 1d -0.3% | 5d -3.2% | 1m -6.8% | 3m -1.7%
52-week range: 282.84 - 365.18 (now 59.8% of the way up)
Volatility: ATR(14) 6.42 (1.9% of price) | annualised 20d 18.2%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 882.69B
Valuation: trailing P/E 14.22 | forward P/E 13.27 | P/B 2.50 | PEG 1.57
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 2.08 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 375.81 (+13.2% vs last close), range 305.00 - 436.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Toyota (TM) · Company — BULLISH, confidence 0.50

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> The battery‑center announcement provides a modest, ticker‑specific catalyst, while the stock trades at a cheap trailing P/E and has a strong earnings‑beat record, suggesting upside potential. However, technicals are bearish (price below key SMAs, low RSI, negative MACD) and volume is thin, limiting conviction. Analyst consensus is already strong‑buy and thus adds little new information. Overall, the modest bullish factors outweigh the technical weakness, leading to a low‑to‑moderate confidence BUY signal.

**Main reasons it gave:**
- Toyota opened new Battery Center in Michigan, expanding EV/hybrid battery development.
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs and RSI 36.3, indicating bearish momentum.
- Trailing P/E 8.17 suggests cheap valuation relative to earnings.
- Four consecutive earnings beats indicate strong earnings momentum.

<details><summary><b>News</b> — score +0.30</summary>

- [Toyota Motor Corporation (NYSE:TM) Stock Now Rated "Buy" by Wall Street Analysts](https://www.marketbeat.com/instant-alerts/consensus-toyota-motor-corporation-nyse-tm-stock-now-rated-buy-by-wall-street-analysts-2026-10-02/)  
  <sub>MarketBeat, 6 hours ago</sub>  
  Toyota Motor Corporation (NYSE:TM - Get Free Report) has received an average recommendation of "Buy" from the seven ratings firms that are presently...
- [One winner gets a talent-agency offer or private mentorship in Morgan Dudley's Broadway challenge](https://www.stocktitan.net/news/STGZ/broadway-star-morgan-dudley-returns-to-stargaze-stage-tm-to-discover-41dq0zcqnmfz.html)  
  <sub>Stock Titan, 12 minutes ago</sub>  
  Submissions remain open through Oct. 31 on Stargaze Stage; predecessor Scenebot Stage helped facilitate nearly 1000 career opportunities.
- [60 Degrees Pharmaceuticals and Exyn Technologies Interviews to Air Nationally on the RedChip Small Stocks, Big Money(TM) Show on CNBC and Bloomberg TV](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/60-degrees-pharmaceuticals-and-exyn-technologies-interviews-to-a-1230508)  
  <sub>ACCESS Newswire, 2 hours ago</sub>  
  ORLANDO, FL / ACCESS Newswire / October 2, 2026 / RedChip Companies will air interviews with 60 Degrees Pharmaceuticals, Inc. (NASDAQ:SXTP; SXTPW) and Exyn...
- [(HBND.U) Strategic Market Analysis (HBND.U:CA)](https://news.stocktradersdaily.com/canada/hbndu-strategic-market-analysis_20261002_904e27)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  Strategic Market Analysis for Hamilton U.S. Bond YIELD MAXIMIZER TM ETF (HBND.U) with Trading Signals.
- [Nvidia Authorizes a Record $150 Billion in Stock Buybacks. The Real Prize Is Where the Rest of Its Cash Is Going.](https://www.theglobeandmail.com/investing/markets/stocks/TM/pressreleases/4914603/nvidia-authorizes-a-record-150-billion-in-stock-buybacks-the-real-prize-is-where-the-rest-of-its-cash-is-going/)  
  <sub>The Globe and Mail, 19 hours ago</sub>  
  Detailed price information for Toyota Motor Corp Ord ADR (TM-N) from The Globe and Mail including charting and trades.
- [7.7 million shares are proposed for past services and outstanding debt at AI/ML Innovations.](https://www.stocktitan.net/news/AIMLF/ai-ml-innovations-appoints-lynn-chapman-as-chief-financial-officer-k0smgjipqsv6.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Insiders expect to buy 4900001 shares directly or indirectly. The issuance, priced at a deemed CAD$0.05 per share, awaits Canadian Securities Exchange...
- [How to Take Advantage of moves in (HBIL) (HBIL:CA)](https://news.stocktradersdaily.com/canada/how-to-take-advantage-of-moves-in-hbil-_20261002_a105a4)  
  <sub>Stock Traders Daily, 4 hours ago</sub>  
  When Investors Make Decisions in Hamilton U.S. T-Bill YIELD MAXIMIZER TM ETF HBIL Opportunities Surface.
- [Form 4 SPROTT FOCUS TRUST INC. For: 1 October By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-sprott-focus-trust-inc-for-1-october-93CH-4863156)  
  <sub>Investing.com, 15 hours ago</sub>  
  FORM 4, UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549. STATEMENT OF CHANGES IN BENEFICIAL OWNERSHIP
- [Toyota Motor stock after-hours at EUR 162.00: plus 0.00 percent versus prior close](https://www.ad-hoc-news.de/boerse/news/nachboerse/toyota-motor-stock-after-hours-at-eur-162-00-plus-0-00-percent-versus-prior-close/70213201)  
  <sub>AD HOC NEWS, 18 hours ago</sub>  
  TM, US8923313071. Toyota Motor stock after-hours at EUR 162.00: plus 0.00 percent versus prior close. Published on 10/01/2026 at 22:38 | Editorial...
- [Toyota's new center tests batteries for hybrid, plug-in hybrid, hydrogen and electric vehicles](https://www.stocktitan.net/news/TM/toyota-battery-center-of-north-america-unveiled-at-michigan-r-d-tl01j93ur86d.html)  
  <sub>Stock Titan, 22 hours ago</sub>  
  Toyota (TM) opened the Toyota Battery Center of North America in Saline, Michigan, expanding its battery development and evaluation capabilities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 182.41 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 190.84 (-4.4%), 50d 190.70 (-4.3%), 200d 201.39 (-9.4%); 50d below 200d
Momentum: RSI(14) 36.3 | MACD -2.068 vs signal -0.696 (histogram -1.372)
Returns: 1d -0.5% | 5d -4.2% | 1m -8.0% | 3m +1.5%
52-week range: 166.50 - 248.29 (now 19.5% of the way up)
Volatility: ATR(14) 3.12 (1.7% of price) | annualised 20d 22.0%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 216.01B
Valuation: trailing P/E 8.17 | forward P/E 11.56 | P/B 14.83 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+28.3% vs last close), range 230.00 - 239.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

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

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.38

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Technical indicators show bearish trend: price below 20‑day, 50‑day, and 200‑day SMAs
- Low trading volume (0.07× 20‑day average) suggests weak momentum
- High valuation (trailing P/E 52.7, forward P/E 38.1) despite strong revenue (+15.9% YoY) and earnings growth (+34.2% YoY)
- Analyst consensus neutral/hold with modest upside target (+16.8% vs current price)
- Insider activity net small buy (+0.1% holdings) but multiple insider sales, no clear signal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 699.17 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 723.10 (-3.3%), 50d 754.80 (-7.4%), 200d 773.75 (-9.6%); 50d below 200d
Momentum: RSI(14) 38.3 | MACD -12.145 vs signal -9.166 (histogram -2.979)
Returns: 1d +0.5% | 5d -4.9% | 1m -1.4% | 3m -13.8%
52-week range: 454.95 - 1,014.33 (now 43.7% of the way up)
Volatility: ATR(14) 16.68 (2.4% of price) | annualised 20d 23.3%
Volume: 0.07x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 32.76B
Valuation: trailing P/E 52.69 | forward P/E 38.08 | P/B 7.41 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.9% of float
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
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+16.8% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material news catalyst; technicals show price below key moving averages and low volume, indicating short‑term weakness; analyst consensus remains buy but recent downgrades to hold temper the outlook; insider activity shows net buying but no distinct insider purchases, making it neutral.

**Main reasons it gave:**
- Technical: price below 20‑day, 50‑day, and 200‑day SMAs; volume 0.10× 20‑day average
- Technical: RSI 45.1 and MACD negative indicating weak momentum
- Analyst: consensus buy but recent downgrades to hold (TD Cowen, Argus, HSBC)
- News: no material ticker‑specific catalyst in past 24 hours

<details><summary><b>News</b> — score +0.00</summary>

- [1 S&P 500 Stock Worth Your Attention and 2 We Turn Down](https://stockstory.org/us/stocks/nyse/pg/news/buy-or-sell/1-sandp-500-stock-worth-your-attention-and-2-we-turn-down)  
  <sub>StockStory, 5 hours ago</sub>  
  While the S&P 500 (^GSPC) includes industry leaders, not every stock in the index is a winner. Some companies are past their prime, weighed down by poor...
- [Would You Buy P&G at this Valuation?](https://finance.yahoo.com/markets/stocks/articles/buy-p-g-valuation-170801727.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  The Procter & Gamble Company (NYSE:PG) is the kind of business investors usually look at when they want stability rather than rapid growth.
- [These dow jones stocks are moving in today's session](https://www.chartmill.com/news/TRV/Chartmill-55630-These-dow-jones-stocks-are-moving-in-todays-session)  
  <sub>ChartMill, 22 hours ago</sub>  
  Get insights into the dow jones index performance on Thursday. Explore the top gainers and losers within the dow jones index in today's session.
- [Three Dividend ETFs Offer a Safer Path to Retirement Income Than Stock Picking](https://finance.biggo.com/news/968111d7-5e70-4c5b-998b-6c5794f3ad1d)  
  <sub>BigGo Finance, 2 hours ago</sub>  
  Retirement investors seeking reliable income may benefit more from dividend ETFs than from picking individual stocks, according to a recent analysis.…
- [SEC Filings for Oct 1, 2026 - 10-K, 10-Q, 8-K Forms](https://www.stocktitan.net/sec-filings/2026-10-01/?page=7)  
  <sub>Stock Titan, 17 hours ago</sub>  
  SEC filings for October 1, 2026 including 10-K annual reports, 10-Q quarterly earnings, 8-K material events, and Form 4 insider trades.
- [Perrigo Co. PLC stock underperforms Thursday when compared to competitors](https://www.marketwatch.com/data-news/perrigo-co-plc-stock-underperforms-thursday-when-compared-to-competitors-a31a2f25-51ec8b9bed6e?mod=goog_fin_scmw)  
  <sub>MarketWatch, 17 hours ago</sub>  
  slid 5.01% to $14.02 Thursday, on what proved to be an all-around great trading session for the stock market, with the S&P 500 Index.
- [Procter & Gamble Tokenized Stock price today, PGX to USD chart, marketcap and volume](https://cryptoslate.com/coins/procter-gamble-tokenized-stock/)  
  <sub>CryptoSlate, 19 hours ago</sub>  
  Procter & Gamble Tokenized Stock price is $148.54 on Oct 1, 2026. Market cap $447.29K; 24h volume $40.18K.
- [Household Products Stocks Q2 Recap: Benchmarking Clorox (NYSE:CLX)](https://stockstory.org/us/stocks/nyse/clx/news/earnings/household-products-stocks-q2-recap-benchmarking-clorox-nyseclx)  
  <sub>StockStory, 5 hours ago</sub>  
  As the Q2 earnings season wraps, let's dig into this quarter's best and worst performers in the household products industry, including Clorox (NYSE:CLX) and...
- [PG261030P00120000 Interactive Stock Chart | PG Oct 2026 120.000 put Stock](https://finance.yahoo.com/chart/PG261030P00120000)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Innovative Advisory Group, LLC - Portfolio Stock Holdings](https://www.quiverquant.com/institutions/Innovative%20Advisory%20Group,%20LLC/)  
  <sub>Quiver Quantitative, 23 hours ago</sub>  
  Track which stocks Innovative Advisory Group, LLC is buying and selling. See stock portfolio updates, holdings by sector, and more.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 144.43 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 146.06 (-1.1%), 50d 145.72 (-0.9%), 200d 147.64 (-2.2%); 50d below 200d
Momentum: RSI(14) 45.1 | MACD -0.014 vs signal 0.240 (histogram -0.253)
Returns: 1d +0.3% | 5d -1.2% | 1m -2.2% | 3m -3.3%
52-week range: 138.04 - 167.20 (now 21.9% of the way up)
Volatility: ATR(14) 2.34 (1.6% of price) | annualised 20d 16.8%
Volume: 0.10x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 335.46B
Valuation: trailing P/E 21.82 | forward P/E 19.52 | P/B 6.29 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.0% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.00</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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

<details><summary><b>What analysts and big funds say</b> — score -0.20</summary>

```text
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+11.2% vs last close), range 143.00 - 186.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technical indicators (RSI 35.2, price below 20‑day SMA, negative MACD, thin volume) suggest bearish short‑term momentum, while fundamentals are solid but PEG 2.26 indicates overvaluation. Analyst consensus is bullish with a modest price‑target uplift, and insiders have purchased ~700k shares, adding bullish sentiment. News is mixed, with record net income and deposit base expansion offset by rising bond yields. Conflicting signals lead to a neutral stance with low conviction.

**Main reasons it gave:**
- Technical indicators (RSI 35.2, price below 20‑day SMA) signal bearish short‑term momentum
- Insider open‑market purchases of ~700k shares show bullish confidence
- Analyst consensus buy with +5.8% price target indicates moderate bullish outlook
- Fundamentals solid but PEG 2.26 suggests overvaluation relative to growth

<details><summary><b>News</b> — score +0.20</summary>

- [RBC sets 4.125% note rate. Royal Bank of Canada stock yields 3.50 percent](https://www.ad-hoc-news.de/boerse/news/corporate-news/rbc-sets-4-125-percent-note-rate-royal-bank-of-canada-stock-yields-3-50/70215274)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  RBC earned CAD 6.0 billion in the third quarter of 2026. Royal Bank of Canada stock costs EUR 174.67 on October 2, 2026 versus EUR 173.76.
- [Got $10,000 for a TFSA? This Dividend Stock Could Start Paying You Now](https://www.theglobeandmail.com/investing/markets/stocks/RY-T/pressreleases/4915201/got-10000-for-a-tfsa-this-dividend-stock-could-start-paying-you-now/)  
  <sub>The Globe and Mail, 19 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-T) from The Globe and Mail including charting and trades.
- [Royal Bank of Canada Offers International Money Transfers from Euro, British Pound, and Hong Kong Dollar Accounts with No RBC Transfer Fees](https://www.marketscreener.com/news/royal-bank-of-canada-offers-international-money-transfers-from-euro-british-pound-and-hong-kong-do-ce785ddad88df024)  
  <sub>marketscreener.com, 22 hours ago</sub>  
  Royal Bank of Canada was making it simpler to send money around the world. Following the launch of International Money Transfers from USD accounts earlier...
- [Why Does Royal Bank of Canada (TSX:RY) Matter This Session?](https://kalkinemedia.com/ca/stocks/bluechip/why-does-royal-bank-of-canada-tsxry-matter-this-session)  
  <sub>Kalkine Media, 21 hours ago</sub>  
  Highlights. The current company story centres on financial shares weakening as global bond yields rise. Core operations remain tied to banking and capital...
- [Many happy returns for resale homes](https://www.businesstimes.com.sg/property/many-happy-returns-resale-homes)  
  <sub>The Business Times, 9 hours ago</sub>  
  But buyers of new launches face slimmer gains on higher purchase prices Read more at The Business Times.
- [RY stock after-hours at EUR 172.59: minus 0.76 percent versus the prior close](https://www.ad-hoc-news.de/boerse/news/nachboerse/ry-stock-after-hours-at-eur-172-59-minus-0-76-percent-versus-the-prior-close/70212603)  
  <sub>AD HOC NEWS, 20 hours ago</sub>  
  RY stock was at EUR 172.59 after-hours at 8:40 p.m. CEST on October 1, 2026, down minus 0.76 percent versus the Lang & Schwarz prior close.
- [Royal Bank of Canada (TSX:RY) Strengthens Deposit Base Amid Rate Transition](https://kalkinemedia.com/ca/stocks/dividend/royal-bank-of-canada-tsxry-strengthens-deposit-base-amid-rate-transition)  
  <sub>Kalkine Media, 20 hours ago</sub>  
  Net income reached record levels with deposit base expanding significantly across retail and commercial segments. Capital ratios remain well above...
- [Will RY break resistance after Vancouver Canucks jersey partnership launched?](https://tradersunion.com/news/stocks/show/3630521-royal-bank-of-canada-up/)  
  <sub>Traders Union, 40 minutes ago</sub>  
  Royal Bank of Canada (RY) stock is trading at C$278.41 after closing with a modest daily gain. The stock finished the session near its high and remains...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 196.34 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 202.84 (-3.2%), 50d 206.69 (-5.0%), 200d 186.39 (+5.3%); 50d above 200d
Momentum: RSI(14) 35.2 | MACD -2.764 vs signal -2.070 (histogram -0.693)
Returns: 1d +0.5% | 5d -2.8% | 1m -5.5% | 3m -5.6%
52-week range: 143.64 - 217.87 (now 71.0% of the way up)
Volatility: ATR(14) 3.11 (1.6% of price) | annualised 20d 13.8%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 271.82B
Valuation: trailing P/E 17.58 | forward P/E 15.64 | P/B 2.84 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
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
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 207.80 (+5.8% vs last close), range 182.95 - 225.11
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.50</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.50</summary>

_Not available today._

</details>

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML Holding N.V. - New York Registry Shares Price Today | xASML Live Price, Chart & Market Cap](https://www.okx.com/en-eu/price/asml-holding-n-v----new-york-registry-shares-xasml)  
  <sub>OKX, 5 hours ago</sub>  
  The current ASML Holding N.V. - New York Registry Shares to USD conversion rate is $1,833.1 per ASML Holding N.V. - New York Registry Shares. Read more...
- [ASML Stock Eyes Second Weekly Gains: Retail Bulls Call Chipmaker The 'Ultimate Gatekeeper Of Tech'](https://stocktwits.com/news-articles/markets/equity/asml-stock-eyes-second-weekly-gains-retail-bulls-call-chipmaker-the-ultimate-gatekeeper-of-tech/cZZ3CuOR7rp)  
  <sub>Stocktwits, 16 hours ago</sub>  
  ASML Holding NV (ASML) stock is poised for a second straight week of gains as an upgraded outlook boosts investor confidence in the semiconductor equipment...
- [ASML vs. Applied Digital: Which Is the Better Semiconductor Equipment Stock to Own for the Next 1 Year?](https://finance.yahoo.com/markets/stocks/articles/asml-vs-applied-digital-better-192000964.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  ASML offers unmatched demand visibility, while Applied Materials brings broader AI-driven growth at a lower valuation.
- [ASML Holding NV Stock (ASML) Opened Up by 3.09% on Oct 2: Key Drivers Unveiled](https://www.tradingkey.com/news/market-movers/262198063-market-movers-asml-20261002)  
  <sub>TradingKey, 54 minutes ago</sub>  
  ASML rose amid institutional optimism for artificial intelligence semiconductor equipment.Wall Street anticipates substantial year-over-year revenue and...
- [Arm vs. ASML: Which Semiconductor Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/10/01/arm-vs-asml-which-semiconductor-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  One designs the chips, while the other manufactures the machines that build them. But their valuations tell a starkly different story.
- [Top 3 Growth Stocks To Watch In October 2026](https://simplywall.st/stocks/us/semiconductors/nasdaq-avgo/broadcom/news/top-3-growth-stocks-to-watch-in-october-2026/amp)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  Central banks are sharpening their focus on inflation control, while growth signals send mixed messages. That kind of push and pull tends to reward...
- [Airbus names ASML, Michelin CEOs to board as Obermann steps down (EADSF:OTCMKTS)](https://seekingalpha.com/news/4649263-airbus-names-asml-michelin-ceos-to-board-as-obermann-steps-down)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Airbus board reshuffle adds ASML CEO Christophe Fouquet and plans Michelin CEO Florent Menegaux—key for supply-chain and production ramp.
- [UBS reaffirms Buy rating for ASML Holding stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/ubs-reaffirms-buy-rating-for-asml-holding-stock/70216064)  
  <sub>AD HOC NEWS, 41 minutes ago</sub>  
  UBS keeps a EUR 2350 target and Buy on September 25, 2026. ASML Holding stock costs EUR 1649.20 on October 2, 2026, 5.27 percent below its high.
- [ASML vs. SK Hynix: What Revenue Trends Reveal to Investors About These Artificial Intelligence Companies](https://www.theglobeandmail.com/investing/markets/stocks/ASML-Q/pressreleases/4914600/asml-vs-sk-hynix-what-revenue-trends-reveal-to-investors-about-these-artificial-intelligence-companies/)  
  <sub>The Globe and Mail, 19 hours ago</sub>  
  Detailed price information for ASML Holding NV (ASML-Q) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,866.47 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 1,721.81 (+8.4%), 50d 1,721.56 (+8.4%), 200d 1,542.78 (+21.0%); 50d above 200d
Momentum: RSI(14) 64.7 | MACD 29.483 vs signal 9.029 (histogram 20.454)
Returns: 1d +3.2% | 5d +7.0% | 1m +10.9% | 3m +2.3%
52-week range: 936.19 - 1,989.44 (now 88.3% of the way up)
Volatility: ATR(14) 50.75 (2.7% of price) | annualised 20d 41.9%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 716.91B
Valuation: trailing P/E 64.92 | forward P/E 31.73 | P/B 1,611.12 | PEG 1.58
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
Price target: mean 2,101.74 (+12.6% vs last close), range 872.99 - 2,795.45
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

- [What Could Lift Caterpillar Stock?](https://finance.yahoo.com/markets/stocks/articles/could-lift-caterpillar-stock-095500419.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Caterpillar (CAT) stock returned 75% over the past twelve months, against 16.0% for the S&P 500. The shares now cost 35.1 times the past year's profit,...
- [A director acquires 28 stock-linked units instead of cash compensation at Caterpillar (CAT).](https://www.stocktitan.net/sec-filings/CAT/form-4-caterpillar-inc-insider-trading-activity-671981523f87.html)  
  <sub>Stock Titan, 17 hours ago</sub>  
  Caterpillar Inc. (CAT) director David MacLennan acquired 28 phantom stock units on September 30, 2026, in lieu of director cash compensation.
- [Top 3 Drone Defense Stocks With Revenue Growth Over 18%](https://simplywall.st/stocks/us/capital-goods/nasdaq-rcat/red-cat-holdings/news/top-3-drone-defense-stocks-with-revenue-growth-over-18)  
  <sub>Simply Wall Street, 10 hours ago</sub>  
  Global bond yields have surged to multi decade highs, which has lifted borrowing costs and squeezed heavily indebted firms. Investors are hunting for...
- [These dow jones stocks are moving in today's session](https://www.chartmill.com/news/TRV/Chartmill-55630-These-dow-jones-stocks-are-moving-in-todays-session)  
  <sub>ChartMill, 22 hours ago</sub>  
  Get insights into the dow jones index performance on Thursday. Explore the top gainers and losers within the dow jones index in today's session.
- [Caterpillar (CAT) Surpasses Market Returns: Some Facts Worth Knowing](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-surpasses-market-returns-204503384.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Caterpillar (CAT) closed the most recent trading day at $826.35, moving +1.92% from the previous trading session.
- [Dell To Officially Join Tesla, Oracle, Caterpillar In Texas As Stock Eyes Best Year Since Returning To Public Markets](https://stocktwits.com/news-articles/markets/equity/dell-to-officially-join-tesla-oracle-caterpillar-in-texas-as-stock-eyes-best-year-since-returning-to-public-markets/cZ1cXbeR7g3)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Wall Street believes it might have some more room to run. Currently, 19 out of 27 analysts rate the stock 'Buy' or higher, and eight rate it 'Hold,' with an...
- [Caterpillar Inc. stock outperforms competitors on strong trading day](https://www.marketwatch.com/data-news/caterpillar-inc-stock-outperforms-competitors-on-strong-trading-day-bebde079-4130f6a071e4?mod=goog_fin_scmw)  
  <sub>MarketWatch, 18 hours ago</sub>  
  Shares of Caterpillar Inc. CAT rallied 1.92% to $826.35 Thursday, on what proved to be an all-around positive trading session for the stock market,...
- [Unusual Machines Tumbles 8% Despite Pentagon's Autonomous Warfare Push; AeroVironment Eases, Red Cat Pulls Back](https://247wallst.com/investing/2026/10/01/unusual-machines-tumbles-8-despite-pentagons-autonomous-warfare-push-aerovironment-eases-red-cat-pulls-back/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  The Pentagon handed drone suppliers the autonomous warfare announcement they craved, yet one stock with a 75% year-to-date gain is tumbling while its rivals...
- [In lieu of cash pay, Caterpillar (CAT) director Lynn J. Good acquires 30 stock-linked units.](https://www.stocktitan.net/sec-filings/CAT/form-4-caterpillar-inc-insider-trading-activity-e0833d4ad2ad.html)  
  <sub>Stock Titan, 17 hours ago</sub>  
  Caterpillar Inc. director Lynn J. Good acquired 30 phantom stock units on September 30, 2026, in lieu of director cash compensation.
- [Caterpillar plans USD 1.0 billion expansion: Caterpillar stock gains 1.61 percent](https://www.ad-hoc-news.de/boerse/news/corporate-news/caterpillar-plans-usd-1-0-billion-expansion-caterpillar-stock-gains-1-61/70216121)  
  <sub>AD HOC NEWS, 37 minutes ago</sub>  
  Second-quarter revenue reached USD 20.54 billion, up 23.70 percent year over year. Caterpillar stock costs EUR 745.80 on October 2, 2026 after EUR 734.00.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 842.38 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 811.14 (+3.9%), 50d 823.39 (+2.3%), 200d 795.08 (+5.9%); 50d above 200d
Momentum: RSI(14) 58.0 | MACD 0.798 vs signal -4.546 (histogram 5.343)
Returns: 1d +1.9% | 5d +2.5% | 1m +6.3% | 3m -13.1%
52-week range: 486.71 - 1,064.90 (now 61.5% of the way up)
Volatility: ATR(14) 23.31 (2.8% of price) | annualised 20d 25.8%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 387.22B
Valuation: trailing P/E 36.28 | forward P/E 26.02 | P/B 19.96 | PEG 1.42
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
Price target: mean 975.61 (+15.8% vs last close), range 575.00 - 1,225.00
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

- [A three-year CEO term is approved at HDFC Bank (HDB) for a life insurance executive.](https://www.stocktitan.net/sec-filings/HDB/6-k-hdfc-bank-ltd-current-report-foreign-issuer-703e6ba27627.html)  
  <sub>Stock Titan, 5 hours ago</sub>  
  HDFC Bank (HDB) said the Reserve Bank of India approved Anup Bagchi's appointment as managing director and chief executive officer, including his...
- [Kaplan Fox Encourages Investors of HDFC Bank Limited (NYSE: HDB) to Contact the Firm Before Lead Plaintiff Deadline on October 13, 2026](https://www.theglobeandmail.com/investing/markets/stocks/HDB-N/pressreleases/4927965/kaplan-fox-encourages-investors-of-hdfc-bank-limited-nyse-hdb-to-contact-the-firm-before-lead-plaintiff-deadline-on-october-13-2026/)  
  <sub>The Globe and Mail, 1 hour ago</sub>  
  Detailed price information for Hdfc Bank Ltd ADR (HDB-N) from The Globe and Mail including charting and trades.
- [Liquidity Mapping Around (HDB) Price Events](https://news.stocktradersdaily.com/news_release/139/Liquidity_Mapping_Around_HDB_Price_Events_100226010401_1790917441.html)  
  <sub>Stock Traders Daily, 14 hours ago</sub>  
  Key findings for Hdfc Bank Limited (NYSE: HDB). Stable Neutral Readings in Shorter Horizons Could Signal Easing of Long-Term Weak Bias...
- [HDFC Bank (HDB) Balances CEO Search, Lawsuit, And Choppy ADR Action](https://stockstotrade.com/news/hdfc-bank-limited-hdb-news-2026_10_01/)  
  <sub>StocksToTrade, 18 hours ago</sub>  
  HDFC Bank Limited gained momentum as strong loan growth and improving asset quality lifted investor sentiment; stocks have been trading up by 3.04 percent...
- [HDFC Bank names Anup Bagchi CEO. HDFC Bank stock yields 1.50 percent](https://www.ad-hoc-news.de/boerse/news/nebenwerte/hdfc-bank-names-anup-bagchi-ceo-hdfc-bank-stock-yields-1-50-percent/70213854)  
  <sub>AD HOC NEWS, 13 hours ago</sub>  
  HDB, US40415F1012. HDFC Bank names Anup Bagchi CEO. HDFC Bank stock yields 1.50 percent. Published on 10/02/2026 at 03:56 | Editorial responsibility: Rafael...
- [Sri Lotus shares rally 29% in a month. Can luxury and redevelopment sustain the momentum?](https://m.economictimes.com/markets/stocks/news/sri-lotus-shares-rally-29-in-a-month-can-luxury-and-redevelopment-sustain-the-momentum/articleshow/134630924.cms)  
  <sub>The Economic Times, 11 hours ago</sub>  
  Sri Lotus Developers & Realty has seen a remarkable 29% increase in shares, significantly outpacing the wider market. This boost is attributed to the...
- [These large-, mid- & small-cap stocks can give more than 20% return in 1 year, according to analysts](https://economictimes.indiatimes.com/markets/stocks/news/these-large-mid-small-cap-stocks-can-give-more-than-20-return-in-1-year-according-to-analysts/articleshow/134624758.cms)  
  <sub>The Economic Times, 21 hours ago</sub>  
  Oil prices are still up, and so are bond yields, both in the US and in other major markets. And fresh troubles seem to crop up somewhere or the other in the...
- [D-Street logs longest spell of week slump in 25 years](https://m.economictimes.com/markets/stocks/news/d-street-logs-longest-spell-of-week-slump-in-25-years/articleshow/134630946.cms)  
  <sub>The Economic Times, 11 hours ago</sub>  
  Indian equity markets faced significant pressure as US bond yields surged, leading to a record selloff. The Sensex and Nifty experienced prolonged declines,...
- [HDFC Bank Taps ICICI Veteran Anup Bagchi as New MD & CEO from October 27](https://www.tipranks.com/news/company-announcements/hdfc-bank-taps-icici-veteran-anup-bagchi-as-new-md-ceo-from-october-27)  
  <sub>TipRanks, 4 hours ago</sub>  
  Hdfc Bank ( ($HDB) ) just unveiled an update. On October 1, 2026, HDFC Bank disclosed that the Reserve Bank of India has approved the appointment of veteran...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.59 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 22.76 (-0.7%), 50d 23.15 (-2.4%), 200d 27.07 (-16.5%); 50d below 200d
Momentum: RSI(14) 46.5 | MACD -0.151 vs signal -0.159 (histogram 0.008)
Returns: 1d -1.6% | 5d -1.8% | 1m -2.7% | 3m -17.6%
52-week range: 21.84 - 37.18 (now 4.9% of the way up)
Volatility: ATR(14) 0.57 (2.5% of price) | annualised 20d 37.5%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 116.11B
Valuation: trailing P/E 15.80 | forward P/E 16.24 | P/B 9.15 | PEG n/a
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
Price target: mean 30.52 (+35.1% vs last close), range 26.10 - 35.00
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

- [Prediction: Eli Lilly Could Be the Next $2 Trillion Drugmaker](https://247wallst.com/investing/2026/10/02/prediction-eli-lilly-could-be-the-next-2-trillion-drugmaker/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Eli Lilly just posted a 47.7% revenue surge while rivals like Novo Nordisk are watching earnings fall, and a fresh pipeline catalyst could push Lilly toward...
- [Most and least shorted mid- to mega-cap healthcare stocks at the end of September](https://seekingalpha.com/news/4648943-most-and-least-shorted-mid-to-mega-cap-healthcare-stocks-at-the-end-of-september)  
  <sub>Seeking Alpha, 42 minutes ago</sub>  
  Short interest data from late September 2026 highlights deeply divided investor sentiment across the healthcare sector. Strong bearish bets remain heavily...
- [LLY Highlights New Efficacy Data From Foundayo and EloraTZP Studies](https://ca.finance.yahoo.com/news/lly-highlights-efficacy-data-foundayo-121500805.html)  
  <sub>Yahoo! Finance Canada, 2 hours ago</sub>  
  Eli Lilly and Company LLY presented new efficacy data from studies of its marketed and investigational metabolic medicines at the annual European...
- [38 ETFs Add to Lilly (Eli) & Co (LLY) on Sept. 30](https://www.gurufocus.com/news/9107320/38-etfs-add-to-lilly-eli-co-lly-on-sept-30)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On Wednesday, Sept. 30, 38 ETFs were buying shares of Lilly (Eli) & Co (LLY) while 22 were selling, resulting in net ETF buying of $62.1 million.
- [What Is The Options Market Telling Us About Eli Lilly Stock?](https://www.trefis.com/stock/lly/articles/617302/what-is-the-options-market-telling-us-about-eli-lilly-stock/2026-10-01)  
  <sub>Trefis, 23 hours ago</sub>  
  Eli Lilly (LLY) management said on its second-quarter 2026 call that the price of Zepbound, its obesity drug, will go down. The company's sales growth rests...
- [LLY Stock Rides Trump Spotlight: President Touts Eli Lilly’s $3.5B Factory As Weight-Loss Pill Plans Go Global](https://stocktwits.com/news-articles/markets/equity/lly-trump-touts-factory-weight-loss-pill-plans-go-global/cZKUwnZR7OX)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Shares of Eli Lilly and Company (LLY) drew attention late Tuesday after U.S. President Donald Trump put the drugmaker's $3.5 billion Pennsylvania factory in the...
- [Johnson & Johnson vs. Eli Lilly: Which Pharma Stock Can Make Your Portfolio Healthier in 2026?](https://www.fool.com/coverage/better-buy/2026/10/01/johnson-and-johnson-vs-eli-lilly-which-pharma-stock-can-make-your-portfolio-healthier-in-2026/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  JNJ trades at a 28% discount on valuation while LLY's cardiometabolic drugs drive 82% of revenue, each bet carries distinct growth and concentration risks.
- [Eli Lilly's revenue jumps 47.7%, eyeing $2 tril...](https://pluang.com/en/news-feed/prediksi-eli-lilly-bisa-jadi-perusahaan-obat-2-triliun)  
  <sub>Pluang, 1 hour ago</sub>  
  Eli Lilly reported a 47.7% revenue increase to $22.97 billion in Q2 2026, surpassing expectations and raising its full-year revenue guidance to $85-$87...
- [Eli Lilly (LLY) Posts Strong Late Stage Obesity And Diabetes Trial Results](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-posts-strong-late-stage-obesity-and-diabetes-t)  
  <sub>Simply Wall Street, 18 hours ago</sub>  
  Eli Lilly (NYSE: LLY) reported new Phase 2b and Phase 3 data for EloraTZP and retatrutide in obesity and type 2 diabetes.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,154.28 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 1,151.79 (+0.2%), 50d 1,177.02 (-1.9%), 200d 1,073.87 (+7.5%); 50d above 200d
Momentum: RSI(14) 46.5 | MACD -2.124 vs signal -3.562 (histogram 1.438)
Returns: 1d +0.4% | 5d -2.5% | 1m -0.5% | 3m -3.8%
52-week range: 799.57 - 1,280.34 (now 73.8% of the way up)
Volatility: ATR(14) 31.58 (2.7% of price) | annualised 20d 19.6%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.03T
Valuation: trailing P/E 38.76 | forward P/E 24.38 | P/B 30.37 | PEG 1.14
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
Price target: mean 1,328.83 (+15.1% vs last close), range 930.00 - 1,600.00
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

- [MSFT Stock Posts Best Quarter Since 1998 As Azure Growth Revives AI Optimism](https://finance.yahoo.com/markets/stocks/articles/msft-stock-posts-best-quarter-084616308.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  MSFT was also the top gainer among the Magnificent Seven stocks in Q3.
- [Microsoft (MSFT) Stock Looks Fully Valued Despite Fresh AI Liability Warnings](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/microsoft-msft-stock-looks-fully-valued-despite-fresh-ai-lia)  
  <sub>Simply Wall Street, 19 hours ago</sub>  
  Microsoft has become one of the clearest ways to play the AI buildout, and with the stock around US$512.90 and a 5 year return of 82.3%, the live question...
- [Which Dates Could Move Microsoft Stock Most?](https://www.trefis.com/stock/msft/articles/617316/which-dates-could-move-microsoft-stock-most/2026-10-01)  
  <sub>Trefis, 23 hours ago</sub>  
  Microsoft (MSFT) stock has gained about 34% in three months, and you may wonder whether it can hold that gain. Management expects about $175 billion of...
- [Is Microsoft Stock Paying You Enough For The Swings?](https://finance.yahoo.com/markets/stocks/articles/microsoft-stock-paying-enough-swings-095354030.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  You may hold Microsoft (MSFT) stock, or be about to, after its shares jumped more than a third from July through September. If you also hold funds that...
- [What's Going On With Microsoft Stock?](https://www.benzinga.com/trading-ideas/movers/26/10/62111178/whats-going-on-with-microsoft-stock-6)  
  <sub>Benzinga, 24 hours ago</sub>  
  Microsoft Corp (NASDAQ:MSFT) shares are trading higher Thursday after Wells Fargo raised its price target on the stock, adding to a string of bullish...
- [I Correctly Predicted Nvidia Would Overtake Apple in Stock Buybacks and Dividends. Here's the Better Buy Now.](https://www.theglobeandmail.com/investing/markets/stocks/MSFT-Q/pressreleases/4925949/i-correctly-predicted-nvidia-would-overtake-apple-in-stock-buybacks-and-dividends-here-s-the-better-buy-now/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [MSFT Stock Soars After Results: CFO Dismisses AI Overcapacity Narrative, Says Can Rein In Spending If Demand Changes](https://stocktwits.com/news-articles/markets/equity/msft-stock-soars-after-results-cfo-dismisses-ai-overcapacity-narrative-says-can-rein-in-spending-if-demand-changes/cZNPZxzRJTH)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Microsoft beat fourth-quarter sales and profit expectations, with its Azure cloud posting 43% growth.
- [MSFT Stock Lands On Wells Fargo’s Q4 ‘Tactical Ideas List’ – Analyst Sees A 41% Upside Potential](https://fr.tradingview.com/news/stocktwits:13cf507ad094b:0-msft-stock-lands-on-wells-fargo-s-q4-tactical-ideas-list-analyst-sees-a-41-upside-potential/)  
  <sub>TradingView, 21 hours ago</sub>  
  Microsoft (MSFT) was in focus on Thursday after Wells Fargo added the tech behemoth to its fourth-quarter “Tactical Ideas” list, highlighting several...
- [Latest News In Cloud AI - Digital Realty Expands AI Capacity with Blackfuel Platform](https://simplywall.st/stocks/us/software/nasdaq-msft/microsoft/news/latest-news-in-cloud-ai-digital-realty-expands-ai-capacity-w)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  Digital Realty has announced the deployment of Blackfuel's AI inference platform at its BCN1 data center in Barcelona, utilizing liquid-cooled...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 516.82 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 501.64 (+3.0%), 50d 487.71 (+6.0%), 200d 432.83 (+19.4%); 50d above 200d
Momentum: RSI(14) 62.3 | MACD 7.748 vs signal 7.434 (histogram 0.314)
Returns: 1d +0.8% | 5d +0.1% | 1m +4.0% | 3m +33.6%
52-week range: 352.83 - 542.07 (now 86.7% of the way up)
Volatility: ATR(14) 11.59 (2.2% of price) | annualised 20d 22.3%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.84T
Valuation: trailing P/E 28.79 | forward P/E 21.86 | P/B 8.68 | PEG 1.62
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
Price target: mean 578.90 (+12.0% vs last close), range 440.00 - 870.00
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

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA Corporation (NVDA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVDA/)  
  <sub>Yahoo! Finance Canada, 4 hours ago</sub>  
  527,580.03% · Previous Close 228.38 · Open 229.95 · Bid 225.20 x 100 · Ask 231.51 x 200 · Day's Range 228.16 - 232.29 · 52 Week Range 164.27 - 236.54 · Volume...
- [NVDA Stock Is Back As Morgan Stanley’s Top Pick – All AI Trends Play To Nvidia’s ‘Strengths,’ Says Analyst](https://finance.yahoo.com/markets/stocks/articles/nvda-stock-back-morgan-stanley-124934015.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Morgan Stanley reinstated Nvidia as its 'Top Pick' in semiconductors after meetings with CEO Jensen Huang and CFO Colette Kress.
- [Nvidia (NVDA) Shares Rise Premarket as Morgan Stanley Names It T](https://www.gurufocus.com/news/9107503/nvidia-nvda-shares-rise-premarket-as-morgan-stanley-names-it-top-semiconductor-pick)  
  <sub>GuruFocus, 2 hours ago</sub>  
  On October 02, 2026, Nvidia (NVDA) shares gained approximately 1.7% in premarket trading following Morgan Stanley's designation of the company as its...
- [Stocks to watch on Friday: NVDA, GS, NKE, and more](https://seekingalpha.com/news/4649796-stocks-to-watch-of-friday-nvda-gs-nke-and-more)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  U.S. stock futures rise as investors watch Treasury yields and the upcoming nonfarm payrolls report.
- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound](https://stocktwits.com/news-articles/markets/equity/intc-amd-mu-nvda-chip-stocks-tumble-again-stalling-a-nascent-rebound/cZZmX14R7wo)  
  <sub>Stocktwits, 3 hours ago</sub>  
  The company raised its 2026 adjusted EPS outlook to $8.80 to $8.95 from the previous range of $8.50 to $8.70. Brown said 3M is growing faster than the overall...
- [Nvidia and Micron Can't Make AI Chips Without This Growth Stock. Here's Why It Could Soar.](https://www.fool.com/investing/2026/10/02/nvidia-and-micron-cant-make-ai-chips-without-this/)  
  <sub>The Motley Fool, 4 hours ago</sub>  
  Nvidia (NVDA +1.09%) and Micron (MU +3.03%) are synonymous with the artificial intelligence (AI) boom. Both are chip stocks, both have posted enormous...
- [NVDA Stock Rallies As Massive AI Deals And Record Buyback Fuel Bull Case](https://www.timothysykes.com/news/nvidia-corporation-nvda-news-2026_10_02/)  
  <sub>Timothy Sykes, 2 hours ago</sub>  
  NVIDIA Corporation stocks have been trading up by 2.26 percent amid bullish sentiment on surging AI chip demand. Key Takeaways For NVDA Traders Record...
- [3 Reasons Investors Love Nvidia (NVDA)](https://stockstory.org/us/stocks/nasdaq/nvda/news/buy-or-sell/3-reasons-investors-love-nvidia-nvda-2)  
  <sub>StockStory, 5 hours ago</sub>  
  Nvidia currently trades at $231.49 and has been a dream stock for shareholders. It's returned 1073% since October 2021, blowing past the S&P 500's 77.9% gai...
- [NVDA Stock Climbs As Record Buybacks Meet Massive AI Demand](https://stockstotrade.com/news/nvidia-corporation-nvda-news-2026_10_02/)  
  <sub>StocksToTrade, 2 hours ago</sub>  
  NVIDIA Corporation stocks have been trading up by 2.23 percent after upbeat AI chip demand news fueled investor optimism. Key Takeaways Nvidia's board...
- [Nvidia returns as Morgan Stanley’s Top Pick on attractive valuation](https://www.investing.com/news/stock-market-news/nvidia-returns-as-morgan-stanleys-top-pick-on-attractive-valuation-4929404)  
  <sub>Investing.com, 4 hours ago</sub>  
  Investing.com -- Morgan Stanley reinstated Nvidia as its top semiconductor pick in a note Friday, telling investors the chipmaker is well positioned at an...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 237.23 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 223.95 (+5.9%), 50d 218.34 (+8.6%), 200d 200.73 (+18.2%); 50d above 200d
Momentum: RSI(14) 65.5 | MACD 3.750 vs signal 2.714 (histogram 1.037)
Returns: 1d +2.8% | 5d +5.4% | 1m +5.7% | 3m +21.3%
52-week range: 165.17 - 237.23 (now 100.0% of the way up)
Volatility: ATR(14) 5.91 (2.5% of price) | annualised 20d 26.1%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.73T
Valuation: trailing P/E 29.95 | forward P/E 15.11 | P/B 25.02 | PEG 0.48
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
Price target: mean 327.70 (+38.1% vs last close), range 180.00 - 515.00
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

- [Novo Nordisk (NVO) Stock Looks Reasonable Given Uncertain Long Term Earnings](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-nvo/novo-nordisk/news/novo-nordisk-nvo-stock-looks-reasonable-given-uncertain-long)  
  <sub>Simply Wall Street, 11 hours ago</sub>  
  Novo Nordisk has seen a steep share price reset in recent years, and the question now is whether the current valuation still lines up with the earnings...
- [NVO261023C00043000 Interactive Stock Chart | NVO Oct 2026 43.000 call Stock](https://finance.yahoo.com/chart/NVO261023C00043000)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [SPCX Stock Declines As Investors Weigh AI Investment Scale Despite Upbeat Q2 Earnings](https://stocktwits.com/news-articles/markets/equity/spcx-stock-declines-as-investors-weigh-ai-investment-scale-despite-upbeat-q2-earnings/cZo5vpxRJ40)  
  <sub>Stocktwits, 21 hours ago</sub>  
  The Elon Musk-led company posted second-quarter revenue of $7.8 billion, a 92% increase from $4.1 billion a year earlier. Net loss narrowed to $541 million,...
- [Over 88% Of Wegovy Trial Participants Achieve Normal Liver Fat Levels, Novo Reports](https://www.benzinga.com/news/health-care/26/10/62119469/over-88-of-wegovy-trial-participants-achieve-normal-liver-fat-levels-novo-reports)  
  <sub>Benzinga, 20 hours ago</sub>  
  Novo Nordisk A/S (NYSE:NVO) on Thursday presented a post hoc analysis from a STEP UP trial sub-population, indicating that Wegovy (pooled semaglutide 7.2...
- [SOFI Stock Got Hit With Price-Target Cuts After Q2 Earnings, But One Contrarian Says Market Is Missing Bigger Story](https://stocktwits.com/news-articles/markets/equity/sofi-stock-got-hit-with-price-target-cuts-after-q2-earnings-but-one-contrarian-says-market-is-missing-bigger-story/cZoRwebRJ5l)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Shay Boloor, chief market strategist at Futrum Equities, said in a post on X that the market is overpricing credit risk and underpricing the platform even...
- [NVO261016C00041000 interactive stock chart | NVO Oct 2026 41.000 call stock](https://uk.finance.yahoo.com/chart/NVO261016C00041000)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Novo Nordisk Lawsuit Against Eli Lilly: Wegovy Maker Alleges Misleading Zepbound, Mounjaro Ads](https://stocktwits.com/news-articles/markets/equity/novo-nordisk-lawsuit-against-eli-lilly-wegovy-maker-alleges-misleading-zepbound-mounjaro-ads/cZZSBtpR7vE)  
  <sub>Stocktwits, 10 hours ago</sub>  
  Novo Nordisk (NVO) filed a lawsuit against Eli Lilly (LLY) on Monday, accusing its rival of running misleading nationwide advertising campaigns for its...
- [S&P 500, Dow, Nasdaq Drop As Yields Spike Amid Calls For More Rate Hikes — AMZN, GOOGL, NFLX, SPCX, RKLB In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-drop-as-yields-spike-amid-calls-for-more-rate-hikes-amzn-googl-nflx-spcx-rklb-in-focus/cZM4IxjRBB9)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Treasury yields jumped across the curve on Wednesday. Traders work on the floor of the New York Stock Exchange (NYSE) on July 23, 2026 in New York City.
- [CAVA Group Stock Rallies After-Hours On FY26 Expectations Match, Q4 Earnings Beat](https://stocktwits.com/news-articles/markets/equity/cava-group-stock-rallies-after-hours-on-fy26-expectations-match-q4-earnings-beat/cZRwgG0R46c)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The company now sees FY26 adjusted core profit of $176 million to $184 million for FY26, in line with an analyst estimate of $182.70 million.
- [Why is Novo Nordisk stock down today? Key support levels to watch](https://tradersunion.com/news/stocks/show/3621623-novo-nordisk-drops-1-35percent-to/)  
  <sub>Traders Union, 7 hours ago</sub>  
  Highlights. Shares of Novo Nordisk are under pressure, trading below key short and long-term moving averages on both hourly and daily charts.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 37.60 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 41.11 (-8.5%), 50d 44.69 (-15.9%), 200d 45.65 (-17.6%); 50d below 200d
Momentum: RSI(14) 28.6 | MACD -2.177 vs signal -1.937 (histogram -0.240)
Returns: 1d +0.5% | 5d -3.1% | 1m -19.6% | 3m -23.7%
52-week range: 35.29 - 63.98 (now 8.1% of the way up)
Volatility: ATR(14) 1.06 (2.8% of price) | annualised 20d 35.8%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 166.03B
Valuation: trailing P/E 9.54 | forward P/E 11.21 | P/B 4.96 | PEG 4.32
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
Price target: mean 46.01 (+22.4% vs last close), range 39.36 - 62.29
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

- [Nearly 70% of patients had meaningful tic improvement within 8 weeks on an experimental drug](https://www.stocktitan.net/news/TEVA/teva-presents-new-efficacy-and-safety-data-with-ecopipam-an-ema4z79vha21.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Among 216 Phase 3 participants, common psychiatric conditions did not negatively affect tic-score reductions; ecopipam's application is under FDA Priority...
- [Post Hoc SOLARIS Data Support Stabilization and Remission With Subcutaneous Olanzapine](https://www.psychiatrictimes.com/view/post-hoc-solaris-data-support-stabilization-and-remission-with-subcutaneous-olanzapine)  
  <sub>Psychiatric Times, 1 hour ago</sub>  
  Once-monthly subcutaneous olanzapine TEV-749 shows sustained stabilization and remission in schizophrenia, supports direct switching, and avoids...
- [TEVA Oct 2026 39.000 call (TEVA261002C00039000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA261002C00039000/)  
  <sub>Yahoo! Finance Canada, 13 hours ago</sub>  
  Find the latest TEVA Oct 2026 39.000 call (TEVA261002C00039000) stock quote, history, news and other vital information to help you with your stock trading...
- [An experimental Tourette drug cut children's tic relapse risk by 50% vs placebo](https://www.stocktitan.net/news/TEVA/journal-of-child-neurology-publishes-review-highlighting-dopamine-s-objai60hs2ck.html)  
  <sub>Stock Titan, 3 hours ago</sub>  
  Ecopipam selectively targets dopamine D1 receptors, unlike D2 antipsychotics. FDA granted it Priority Review; Teva's accepted NDA seeks a pediatric...
- [Teva Presents New Efficacy and Safety Data with Ecopipam, an Investigational Treatment for Pediatric Patients with Tourette Syndrome](https://macaubusiness.com/teva-presents-new-efficacy-and-safety-data-with-ecopipam-an-investigational-treatment-for-pediatric-patients-with-tourette-syndrome/)  
  <sub>Macau Business, 2 hours ago</sub>  
  Clinical Study, GlobeNewswire, Pharmaceuticals | Based on a post hoc analysis, a majority of participants (~7.
- [Teva's Degevma Wins FDA Approval, Joining a Crowded Field of Xgeva Biosimilars for Cancer That Reaches Bone](https://www.medicaldaily.com/teva-degevma-xgeva-biosimilar-fda-approval-479373)  
  <sub>Medical Daily, 15 hours ago</sub>  
  Teva Pharmaceuticals announced Sept. 28 that the U.S. Food and Drug Administration approved Degevma (denosumab-adet), a biosimilar to Amgen's Xgeva.
- [This Toll Brothers Analyst Begins Coverage On A Bullish Note; Here Are Top 5 Initiations For Thursday](https://www.benzinga.com/analyst-stock-ratings/initiation/26/10/62113639/this-toll-brothers-analyst-begins-coverage-on-a-bullish-note-here-are-top-5-initiations-for-thursday)  
  <sub>Benzinga, 23 hours ago</sub>  
  Analysts initiated bullish coverage on Vita Coco, Toll Brothers, Civeo, Teva and Kura Oncology, with price targets of $70, $159, $42, $55 and $30.
- [TEVA Initiates Coverage On TD Cowen -- Rating Set to Buy](https://www.gurufocus.com/news/9105784/teva-initiates-coverage-on-td-cowen-rating-set-to-buy)  
  <sub>GuruFocus, 24 hours ago</sub>  
  Teva Pharmaceutical Industries: Analyst Rating and Valuation Insights On October 1, 2026, TD Cowen initiated coverage on Teva Pharmaceutical Industries...
- [Trailing the SBF 120, Medincell stock plunges nearly 23% in quarterly decline](https://www.ideal-investisseur.fr/en/stock-news/trailing-the-sbf-120-medincell-stock-plunges-nearly-23-in-quarterly-decline/26363.html)  
  <sub>Ideal Investisseur, 2 hours ago</sub>  
  The Montpellier-based biopharmaceutical company is losing ground in early afternoon trading, while the SBF 120 advances. The stock is among the most lagging...
- [Real-World Data Link LAI Risperidone to Fewer Emergency Visits in Schizophrenia, Improved Bipolar Treatment](https://www.psychiatrictimes.com/view/real-world-data-link-lai-risperidone-to-fewer-emergency-visits-in-schizophrenia-improved-bipolar-treatment)  
  <sub>Psychiatric Times, 20 hours ago</sub>  
  Real-world data links once-monthly Uzedy to fewer ER visits, better adherence, and lower costs—plus fewer bipolar I relapses when switching from pills.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.30 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 38.65 (+1.7%), 50d 36.92 (+6.4%), 200d 33.68 (+16.7%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD 0.779 vs signal 0.855 (histogram -0.077)
Returns: 1d -0.0% | 5d +0.3% | 1m +4.8% | 3m +11.4%
52-week range: 18.95 - 40.22 (now 95.7% of the way up)
Volatility: ATR(14) 1.17 (3.0% of price) | annualised 20d 29.9%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.84B
Valuation: trailing P/E 65.50 | forward P/E 12.74 | P/B 5.91 | PEG 0.71
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
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 7 analysts)
Ratings: 3 strong buy, 4 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 46.29 (+17.8% vs last close), range 40.00 - 55.00
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

- [ExxonMobil (NYSE:XOM) Stock Rating Lowered by Wells Fargo & Company](https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-stock-rating-lowered-by-wells-fargo-company-2026-10-02/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Wells Fargo & Company lowered ExxonMobil from a "strong-buy" rating to a "hold" rating in a research note on Wednesday.
- [ExxonMobil Returned $9.4 Billion to Shareholders Last Quarter. Here's the Buyback-to-Dividend Split.](https://www.fool.com/investing/2026/10/02/exxonmobil-return-shares-dividend-buyback/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  With more than one century of paying dividends under its belt, it's difficult to argue that ExxonMobil (XOM +0.66%) isn't dedicated to returning capital to...
- [Exxon, Chevron Head Into Earnings With Venezuela, LNG and Higher Oil Prices in Focus](https://www.benzinga.com/markets/large-cap/26/10/62127637/exxon-chevron-head-into-earnings-with-venezuela-lng-and-higher-oil-prices-in-focus)  
  <sub>Benzinga, 5 hours ago</sub>  
  ExxonMobil Holdings Corp. (NYSE:XOM) and Chevron Corp. (NYSE:CVX) head into third-quarter earnings with investors focused on refining margins, crude prices,...
- [MRNA, LNTH, BMY, CAPR, RARE Stocks In Focus — These FDA Decisions Could Shape August Trading](https://stocktwits.com/news-articles/markets/equity/mrna-lnth-bmy-capr-rare-stocks-in-focus-these-fda-decisions-could-shape-august-trading/cZoTYS7RJ30)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Moderna is seeking approval for mRNA-1010, its experimental mRNA-based seasonal flu vaccine for adults 50 and older.Capricor is seeking full approval for...
- [Marathon Petroleum Climbs 5%, Valero Energy Gains 4% as Refiners Outrun Integrated Majors; Exxon Mobil Stays Flat](https://247wallst.com/investing/2026/10/01/marathon-petroleum-climbs-5-valero-energy-gains-4-as-refiners-outrun-integrated-majors-exxon-mobil-stays-flat/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Pure refiners and integrated oil majors are trading as if they belong to entirely different industries today, and the reason comes down to one economic...
- [XOM261030P00175000 Interactive Stock Chart | XOM Oct 2026 175.000 put Stock](https://finance.yahoo.com/chart/XOM261030P00175000)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [ExxonMobil (XOM) Rating Downgraded to Equal Weight by Wells Farg](https://www.gurufocus.com/news/9106187/exxonmobil-xom-rating-downgraded-to-equal-weight-by-wells-fargo)  
  <sub>GuruFocus, 21 hours ago</sub>  
  On October 01, 2026, Wells Fargo downgraded ExxonMobil's (XOM) rating to "equal weight," while maintaining a price target of $182 per share.
- [XOM vs CVX: scale, value, and income compared](https://www.investing.com/news/stock-market-news/xom-vs-cvx-scale-value-and-income-compared-93CH-4928078)  
  <sub>Investing.com, 20 hours ago</sub>  
  Investing.com -- ExxonMobil Holdings Corporation (XOM) offers greater scale, while Chevron Corp (CVX) offers better income and modeled upside.
- [BP upgraded, Exxon downgraded at Wells Fargo as relative valuation favors BP (BP:NYSE)](https://seekingalpha.com/news/4649393-bp-upgraded-exxon-downgraded-at-wells-fargo-as-relative-valuation-favors-bp)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  BP (BP) gained 1.1% in Thursday's trading as Wells Fargo upgraded shares to Overweight from Equal Weight with a $57 price target, raised from $48,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 162.63 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 162.71 (-0.0%), 50d 160.51 (+1.3%), 200d 149.09 (+9.1%); 50d above 200d
Momentum: RSI(14) 52.0 | MACD 0.580 vs signal 0.774 (histogram -0.194)
Returns: 1d -0.7% | 5d +1.3% | 1m -0.9% | 3m +19.2%
52-week range: 110.64 - 171.47 (now 85.5% of the way up)
Volatility: ATR(14) 3.49 (2.1% of price) | annualised 20d 24.7%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 668.72B
Valuation: trailing P/E 20.93 | forward P/E 14.38 | P/B 2.58 | PEG 1.38
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
Ratings: 3 strong buy, 6 buy, 16 hold, 0 sell, 0 strong sell
Price target: mean 173.05 (+6.4% vs last close), range 142.00 - 200.00
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

### US company bonds, riskier (HYG) · Index fund — BULLISH, confidence 0.30

**Result:** ACCEPTED · 158 shares · submitted buy 158 HYG @ ~77.10, stop 76.43

**In the model's own words:**

> Softer September payrolls reduced odds of a Fed rate hike in October, providing a macro catalyst; fund share count rose 1.8% over the week, indicating net inflows; RSI at 28 suggests oversold conditions and potential bounce; the fund's 5.9% yield exceeds the 10‑year Treasury yield of 5.2%, offering a positive spread.

**Main reasons it gave:**
- Cooler September payrolls reduced Fed rate hike odds for October (macro surprise)
- Share count rose 1.8% over the week, indicating net inflows
- RSI 28 indicates oversold conditions, potential bounce
- Yield 5.9% exceeds 10‑year Treasury yield 5.2%, providing a positive spread

<details><summary><b>News</b> — score +0.20</summary>

- [Responsive Playbooks and the HYG Inflection](https://news.stocktradersdaily.com/news_release/23/Responsive_Playbooks_and_the_HYG_Inflection_100226040401_1790928241.html)  
  <sub>Stock Traders Daily, 11 hours ago</sub>  
  Price-action only: Ishares Iboxx Usd High Yield Corporate Bond Etf (HYG) movements set the tone for institutional models. Responsive Playbooks and the HYG...
- [Ishares Iboxx $ High Yield Corporate Bond Etf Options Spot-On: On October 1st, 892.05K Contracts Were Traded, With 9.58 Million Open Interest](https://news.futunn.com/en/post/1000504181/ishares-iboxx-high-yield-corporate-bond-etf-options-spot-on)  
  <sub>富途牛牛, 14 hours ago</sub>  
  OnOctober 1st ET, $Ishares Iboxx $ High Yield Corporate Bond Etf(HYG.US)$ had active options trading, with a total trading volume of 892.05K options for the...
- [Treasury yields retreat after the softer September payrolls report](https://seekingalpha.com/news/4649817-treasury-yields-retreat-after-the-softer-september-payrolls-report)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. Treasury yields slipped across the curve Friday morning after a softer-than-expected September jobs report landed.
- [SPDR Barclays High Yield Bond ETF declares monthly distribution of $0.5313](https://www.tradingview.com/news/seekingalpha:285ea3a92094b:0-spdr-barclays-high-yield-bond-etf-declares-monthly-distribution-of-0-5313/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Up 2,500%… Is This the Correction to Buy?](https://daily.fattail.com.au/up-2500-is-this/20261002/)  
  <sub>Fat Tail Daily, 2 hours ago</sub>  
  Bond yields continue to rise, and high-yield corporate bonds are coming under pressure. Meanwhile, US equities remain worryingly narrow, while Australian...
- [October rate hike odds collapse after cooler payrolls print](https://seekingalpha.com/news/4649846-october-rate-hike-odds-collapse-after-cooler-payrolls-print)  
  <sub>Seeking Alpha, 28 minutes ago</sub>  
  A cooler September jobs report has sharply reduced the odds that the Federal Reserve will decide to raise rates at its October 28 meeting.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 77.25 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 78.23 (-1.3%), 50d 79.01 (-2.2%), 200d 79.89 (-3.3%); 50d below 200d
Momentum: RSI(14) 28.0 | MACD -0.555 vs signal -0.438 (histogram -0.117)
Returns: 1d +0.4% | 5d -0.8% | 1m -2.4% | 3m -3.3%
52-week range: 76.90 - 81.28 (now 7.9% of the way up)
Volatility: ATR(14) 0.33 (0.4% of price) | annualised 20d 4.4%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.8% (282.15M) over 7d
Shares outstanding: 209.66M | fund size: 16.20B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows flat: share count unchanged (+0.0% over 7d)
- Analyst view provides no rating or price target (no consensus)
- Macro data unchanged: Fed target unchanged at 4.00%, yields stable, inflation and unemployment in line with expectations
- Technical indicators mixed: price below 20‑day SMA, RSI neutral (45.2), MACD slightly negative, low volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.28 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 28.62 (-1.2%), 50d 28.34 (-0.2%), 200d 27.14 (+4.2%); 50d above 200d
Momentum: RSI(14) 45.2 | MACD -0.079 vs signal 0.007 (histogram -0.086)
Returns: 1d +0.5% | 5d -0.9% | 1m -3.4% | 3m +2.7%
52-week range: 25.44 - 29.49 (now 70.1% of the way up)
Volatility: ATR(14) 0.27 (1.0% of price) | annualised 20d 12.9%
Volume: 0.13x the 20-day average
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
Shares outstanding: 27.60M | fund size: 780.55M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, mixed fundamentals and flows

**Main reasons it gave:**
- Energy inventories built (crude +0.9M bbl, gas +64 BCF) – bearish for commodity exposure
- EIA price outlook forecasts falling WTI prices (down ~13% over 6 months) – bearish
- Fund flows positive (+1.4% share count increase) – bullish demand
- Technical indicators mixed: price above 50d/200d SMA but below 20d SMA, MACD below signal – no clear trend

<details><summary><b>News</b> — score +0.00</summary>

- [The Risks Of Returning To Hyper-Concentration (NASDAQ:META)](https://seekingalpha.com/article/4951536-the-risks-of-returning-to-hyper-concentration)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Meta Platforms surged 28.9% in three months, singlehandedly driving gains in the Communication Services sector and VOX ETF. META's launch of Muse,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 32.12 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 32.76 (-2.0%), 50d 31.18 (+3.0%), 200d 28.17 (+14.0%); 50d above 200d
Momentum: RSI(14) 49.4 | MACD 0.306 vs signal 0.496 (histogram -0.190)
Returns: 1d -1.9% | 5d -1.5% | 1m +0.6% | 3m +19.0%
52-week range: 22.07 - 33.68 (now 86.6% of the way up)
Volatility: ATR(14) 0.52 (1.6% of price) | annualised 20d 20.8%
Volume: 0.78x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.40</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +13.9% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.80B
What it is made of: Other 50.6%, Cash 44.8%, Bonds 2.7%, Stocks 1.9%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.8%, Brent Crude Future Nov 26 8.9%, Invesco Short Term Treasury ETF 6.2%, Mini Ibovespa Future Dec 26 1.9%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.40</summary>

```text
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Crude oil: 427.3 million barrels, +0.9 on the week (a build), 62% percentile over 52 weeks
  Natural gas: 3,415.0 billion cubic feet, +64.0 on the week (a build), 79% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.40</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.4% (25.52M) over 7d
Shares outstanding: 56.13M | fund size: 1.80B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: yields stable, no policy surprise (10y +0.02% week, Fed target 4.00%)
- Technical: price below 20‑day SMA (-0.6%), RSI 43.5, MACD slightly negative
- Positioning: net short 26% of OI, short decreased -6.4% OI (crowded short but weakening)
- Analyst view: bullish on top 1.7% holdings, but coverage thin

<details><summary><b>News</b> — score +0.00</summary>

- [IWM Has Trailed the S&P 500 for a Decade While Carrying More Risk: The Small-Cap Premium That Never Fully Arrived](https://247wallst.com/investing/etf/2026/10/02/iwm-has-trailed-the-sp-500-for-a-decade-while-carrying-more-risk-the-small-cap-premium-that-never-fully-arrived/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Millions of retirement portfolios hold small-cap funds on the promise that extra risk earns extra reward over time. That bargain deserves a hard look at...
- [Screened small-cap ETF AVUV outperforms broad R...](https://pluang.com/en/news-feed/lupakan-iwm-dana-kecil-terpilih-lebih-baik-tahun-ini)  
  <sub>Pluang, 17 hours ago</sub>  
  The Avantis U.S. Small Cap Value ETF (AVUV), which screens for cheaper and more profitable small-cap stocks, has outperformed the iShares Russell 2000 ETF...
- [Forget IWM: This Screened Small-Cap Fund Beat It Year to Date, Over One Year and Over Five Years](https://www.aol.com/articles/forget-iwm-screened-small-cap-210312000.html)  
  <sub>AOL.com, 18 hours ago</sub>  
  IWM owns every small cap the Russell 2000 will take, profitable or not, and that open-door policy has a measurable cost that most investors never calculate...
- [Exchange-Traded Funds Mixed, US Equities Fall After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-mixed-us-171345834.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded fund IWM rose and IVV edged lower. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [XV: Fears Of A Black Swan Event May Result In Underperformance Despite Durable Structure](https://seekingalpha.com/article/4951465-xv-fears-of-a-black-swan-event-may-result-in-underperformance-despite-durable-structure?source=generic_rss)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Simplify Target 15 Distribution ETF review: 20%+ yield via barrier put spreads with 25% downside cushion—yet macro risks loom. Learn more about the XV ETF...
- [Daily ETF Flows: BIL On Top](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-bil-top-210005431.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for September 30, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 283.26 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 285.10 (-0.6%), 50d 292.61 (-3.2%), 200d 276.33 (+2.5%); 50d above 200d
Momentum: RSI(14) 43.5 | MACD -3.840 vs signal -3.747 (histogram -0.093)
Returns: 1d +1.5% | 5d +0.5% | 1m -3.7% | 3m -5.2%
52-week range: 229.11 - 305.09 (now 71.3% of the way up)
Volatility: ATR(14) 3.62 (1.3% of price) | annualised 20d 12.3%
Volume: 0.47x the 20-day average
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
Three-year record: +17.6% a year | beta to the market 1.24
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
Weighted price target: +18.3% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-10-01 JP Morgan: main, Overweight -> Overweight
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
Shares outstanding: 281.05M | fund size: 79.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: no macro surprise, technicals still bearish, modest positive fund flows, fundamentals stable.

**Main reasons it gave:**
- Positive fund flows: +2.6% share count increase over 1 week
- Technical indicators remain bearish: price below 20d, 50d, 200d SMAs, RSI 30.1, MACD negative
- No macro surprise: Treasury yields moved modestly, no policy surprise
- Fund fundamentals stable: yield 4.7%, credit quality unchanged, expense ratio low

<details><summary><b>News</b> — score +0.00</summary>

- [ETF Inflows Top Last Year's Record With a Quarter to Spare](https://finance.yahoo.com/markets/stocks/articles/etf-inflows-top-last-years-043228801.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  Investors added $150.6 billion to US-listed ETFs in September, according to fresh data from Bloomberg. That brought year-to-date inflows to $1.54 trillion,...
- [iShares iBoxx $ Investment Grade Corporate Bond ETF declares monthly distribution of $0.4387](https://www.tradingview.com/news/seekingalpha:5257585f2094b:0-ishares-iboxx-investment-grade-corporate-bond-etf-declares-monthly-distribution-of-0-4387/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [AI Debt Issuance Taking Up More Room in Bond Indexes](https://www.ai-cio.com/news/ai-debt-issuance-taking-up-more-room-in-bond-indexes/)  
  <sub>Chief Investment Officer, 21 hours ago</sub>  
  Bonds sold to finance corporate capital spending on artificial intelligence by technology companies are flooding the bond markets, and the impact is...
- [Treasury yields retreat after the softer September payrolls report](https://seekingalpha.com/news/4649817-treasury-yields-retreat-after-the-softer-september-payrolls-report)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. Treasury yields slipped across the curve Friday morning after a softer-than-expected September jobs report landed.
- [3 Stocks For Higher Bond Yields Through Pension De Risking](https://finance.yahoo.com/markets/stocks/articles/3-stocks-higher-bond-yields-210826388.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Bond markets are throwing out big signals right now, with UK 30-year gilt yields around 6% and US long-dated Treasuries at multi-decade highs,...
- [Why Broadcom stock is gaining today?](https://invezz.com/au/news/2026/10/02/why-broadcom-stock-is-gaining-today/)  
  <sub>Invezz, 12 minutes ago</sub>  
  Broadcom stock AVGO gained more than 2.7% in trading on Friday as Wall Street banks prepared a potential USD 60 billion (approx.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 102.43 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 103.99 (-1.5%), 50d 105.34 (-2.8%), 200d 108.42 (-5.5%); 50d below 200d
Momentum: RSI(14) 30.1 | MACD -0.943 vs signal -0.765 (histogram -0.178)
Returns: 1d +0.4% | 5d -0.8% | 1m -2.8% | 3m -5.7%
52-week range: 102.03 - 112.92 (now 3.6% of the way up)
Volatility: ATR(14) 0.63 (0.6% of price) | annualised 20d 7.1%
Volume: 0.32x the 20-day average
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
Three-year record: +4.6% a year | beta to the market 1.35
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.6% (820.84M) over 7d
Shares outstanding: 313.12M | fund size: 32.07B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; macro data (cooler payrolls) slightly reduces rate‑hike odds, but yields are mixed and technicals show price near 52‑week low with low volume. Insider positioning is net short on 2‑year notes (bearish) but highly crowded, while fundamentals are solid (AA‑rated, 3.6% yield, low beta). The mix of modest bullish and bearish signals leads to a neutral stance.

**Main reasons it gave:**
- Cooler September payrolls reduced odds of an October rate hike
- CFTC data shows large speculators net short 29.8% of open interest on 2‑year note, with 92% crowding percentile
- Fund basics: AA‑rated short‑term Treasury ETF with 3.6% yield and low beta (0.22)
- Technicals: price near 52‑week low, RSI 35.6, low volume, slight bullish MACD

<details><summary><b>News</b> — score +0.00</summary>

- [Citi Projects Ethereum at $3,028 and Bitcoin at $113,000. Why Is the Bank So Much More Bullish on Bitcoin?](https://247wallst.com/investing/cryptocurrency/2026/10/02/citi-projects-ethereum-at-3028-and-bitcoin-at-113000-why-is-the-bank-so-much-more-bullish-on-bitcoin/)  
  <sub>24/7 Wall St., 5 hours ago</sub>  
  Citigroup just raised its price targets for both Bitcoin and Ethereum by similar margins, yet the two forecasts tell very different stories about which coin...
- [October rate hike odds collapse after cooler payrolls print](https://seekingalpha.com/news/4649846-october-rate-hike-odds-collapse-after-cooler-payrolls-print)  
  <sub>Seeking Alpha, 27 minutes ago</sub>  
  A cooler September jobs report has sharply reduced the odds that the Federal Reserve will decide to raise rates at its October 28 meeting.
- [The Weekly Spread: What Shaped US Yields And The Dollar This Week](https://stocktwits.com/news-articles/markets/equity/the-weekly-spread-what-shaped-yields-and-the-dollar-this-week-1/cZMXz82RBO8)  
  <sub>Stocktwits, 16 hours ago</sub>  
  U.S. bond yields climbed for the second straight week across the curve, with yields at their highest in over a decade, as hawkish commentary from multiple...
- [Treasury yields retreat after the softer September payrolls report](https://seekingalpha.com/news/4649817-treasury-yields-retreat-after-the-softer-september-payrolls-report)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. Treasury yields slipped across the curve Friday morning after a softer-than-expected September jobs report landed.
- [Vanguard All-World ETF Sits 0.6% Below Its Peak as Bond Yields Call the Tune](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-all-world-etf-sits-0-6-percent-below-its-peak-as-bond-yields/70212386)  
  <sub>AD HOC NEWS, 21 hours ago</sub>  
  Vanguard FTSE All-World ETF trades at EUR 169.88, 0.6% below its 52-week high, up 17% year to date as rising bond yields pressure global equities.
- [SCHD: Here’s why this dividend ETF is slumping and what next](https://invezz.com/sg/news/2026/10/01/schd-heres-why-this-dividend-etf-is-slumping-and-what-next/)  
  <sub>Invezz, 24 hours ago</sub>  
  The Schwab US Dividend Equity ETF SCHD has pulled back sharply in the past few weeks, moving from a high of $35 in August to the current $32.5.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.12 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 81.30 (-0.2%), 50d 81.67 (-0.7%), 200d 82.26 (-1.4%); 50d below 200d
Momentum: RSI(14) 35.6 | MACD -0.169 vs signal -0.172 (histogram 0.003)
Returns: 1d +0.0% | 5d -0.1% | 1m -0.6% | 3m -1.0%
52-week range: 81.09 - 83.18 (now 1.4% of the way up)
Volatility: ATR(14) 0.12 (0.1% of price) | annualised 20d 1.7%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Short Government
Yield: 3.6%
Credit quality: AA 100.0% | US government debt 99.2%
Three-year record: +3.9% a year | beta to the market 0.22
Cost and size: expense ratio 0.15% | net assets 25.91B
What it is made of: Bonds 99.2%, Cash 0.8%
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 29.8% of open interest (4,539,374 contracts)
Change on the week: -0.6% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.2% (42.83M) over 7d
Shares outstanding: 319.29M | fund size: 25.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals not decisive, analyst coverage thin, positioning crowded but flows positive.

**Main reasons it gave:**
- No macro surprise: yields unchanged, Fed policy unchanged
- Technical indicators not decisive: price below 20‑day and 50‑day SMA, RSI low, low volume
- Analyst coverage thin (11.4% of fund) despite bullish rating and +13.7% price target
- Positioning shows a crowded long (6% net long, 100th percentile) suggesting potential reversal
- Fund flows positive (+1.6% share count) but mixed with crowded positioning

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Securitas AB Class B Stocks](https://www.tradingview.com/symbols/HAN-S7MB/etfs/)  
  <sub>TradingView, 22 hours ago</sub>  
  Explore funds investing in S7MB in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 86.49 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 88.77 (-2.6%), 50d 90.43 (-4.4%), 200d 87.63 (-1.3%); 50d above 200d
Momentum: RSI(14) 35.9 | MACD -1.108 vs signal -0.835 (histogram -0.272)
Returns: 1d +1.2% | 5d -2.4% | 1m -4.9% | 3m -3.9%
52-week range: 77.90 - 93.19 (now 56.1% of the way up)
Volatility: ATR(14) 1.01 (1.2% of price) | annualised 20d 13.8%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +18.0% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 39.06B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.0%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.7%, Shell PLC 1.6%
Sector mix: Financial services 25.3%, Industrials 19.8%, Healthcare 12.1%, Technology 9.0%
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
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.7% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 6.0% of open interest (487,063 contracts)
Change on the week: +1.3% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.6% (598.83M) over 7d
Shares outstanding: 444.59M | fund size: 38.45B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows moderate bullish fundamentals and analyst coverage, modest insider positioning, but macro headwinds (stronger dollar, higher yields) and neutral technicals keep the overall view neutral.

**Main reasons it gave:**
- Analyst coverage of top 5 holdings (22.2% weight) is 100% buy with +36.6% price target
- CFTC large speculators net long 4.6% of open interest, up 1.3% week over week
- Fund fundamentals: moderate valuations (P/E 15.9) and strong 3‑year performance (+18% annual) with low expense ratio 0.06%
- Macro: US dollar index up 0.72% on the week and VIX up 0.7, indicating slight headwinds for emerging markets
- Technicals: price below 20‑day and 50‑day SMA, RSI 46.9, MACD negative, low volume (0.25× 20‑day average)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.65 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 60.07 (-0.7%), 50d 59.93 (-0.5%), 200d 57.95 (+2.9%); 50d above 200d
Momentum: RSI(14) 46.9 | MACD -0.182 vs signal -0.063 (histogram -0.118)
Returns: 1d +1.0% | 5d -0.9% | 1m -1.9% | 3m -0.7%
52-week range: 52.42 - 61.44 (now 80.1% of the way up)
Volatility: ATR(14) 0.62 (1.0% of price) | annualised 20d 14.5%
Volume: 0.25x the 20-day average
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
Three-year record: +18.1% a year | beta to the market 0.75
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.6% above the current prices
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
Shares outstanding: 1.42B | fund size: 84.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares J.P. Morgan USD Emerging Markets Bond ETF declares monthly distribution of $0.4436](https://www.tradingview.com/news/seekingalpha:d6fad7508094b:0-ishares-j-p-morgan-usd-emerging-markets-bond-etf-declares-monthly-distribution-of-0-4436/)  
  <sub>TradingView, 20 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [ETF Inflows Top Last Year's Record With a Quarter to Spare](https://www.etf.com/sections/monthly-etf-flows/etf-inflows-top-last-years-record-quarter-spare)  
  <sub>ETF.com, 14 hours ago</sub>  
  Investors added $150.6 billion to US-listed ETFs in September, according to fresh data from Bloomberg. That brought year-to-date inflows to $1.54 trillion,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 90.46 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 92.74 (-2.5%), 50d 94.02 (-3.8%), 200d 95.46 (-5.2%); 50d below 200d
Momentum: RSI(14) 22.6 | MACD -1.003 vs signal -0.743 (histogram -0.259)
Returns: 1d +0.2% | 5d -1.9% | 1m -3.9% | 3m -6.1%
52-week range: 90.26 - 97.74 (now 2.7% of the way up)
Volatility: ATR(14) 0.54 (0.6% of price) | annualised 20d 6.9%
Volume: 0.28x the 20-day average
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
Three-year record: +8.8% a year | beta to the market 1.08
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
Share count change: 1 week: +2.6% (372.07M) over 7d
Shares outstanding: 163.41M | fund size: 14.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [(IEF) and the Role of Price-Sensitive Allocations](https://news.stocktradersdaily.com/news_release/14/IEF_and_the_Role_of_Price-Sensitive_Allocations_100226061401_1790936041.html)  
  <sub>Stock Traders Daily, 8 hours ago</sub>  
  Key findings for Ishares 7-10 Year Treasury Bond Etf (NYSE: IEF). Full Alignment in Neutral Sentiment Favors Wait-and-See Approach...
- [Moving Averages Of The Ivy Portfolio And S&P 500: September 2026](https://seekingalpha.com/article/4951497-moving-averages-of-ivy-portfolio-s-p-500-september-2026?source=generic_rss)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  The Ivy Portfolio 10- and 12-month simple moving average had two cash positions: the IEF and VNQ ETFs.
- [Peter Schiff Warns Bond Market Debt Costs Could Top Social Security - iShares 7-10 Year Treasury Bond ETF](https://www.benzinga.com/markets/bonds/26/10/62126175/ai-kill-us-10-years-bond-market-next-week-treasury-yields-24-year-highs)  
  <sub>Benzinga, 10 hours ago</sub>  
  The 10- and 30-year Treasury yields hit their highest levels since 2002, and Peter Schiff warns the national debt is about to get costly.
- [Ed Yardeni Says Stocks Could Face Trouble If Bond Yields Hit 6% — ‘We’d All Start To Get Concerned’](https://stocktwits.com/news-articles/markets/equity/ed-yardeni-stocks-trouble-bond-yields-6/cZMggCYRBOU)  
  <sub>Stocktwits, 12 hours ago</sub>  
  Yardeni said the 5.2% level on bond yields is not high enough to “kneecap” the stock market or the broader economy. However, he identified 6% yield as the...
- [Gold ETFs Keep the Bid, but Investors Miss This Key Seasonality Pattern](https://www.benzinga.com/markets/commodities/26/10/62128652/gold-etfs-keep-the-bid-but-investors-miss-this-key-seasonality-pattern)  
  <sub>Benzinga, 4 hours ago</sub>  
  Despite rising yields, gold ETF demand holds firm near multi-year highs. Explore why central bank buying keeps a $4000 price floor.
- [Jim Cramer Says 'Tough For Bonds to Rally' As Troops Head to Middle East - iShares 7-10 Year Treasury Bon](https://www.benzinga.com/markets/bonds/26/10/62126632/jim-cramer-third-aircraft-carrier-middle-east-10000-troops-bonds-rally)  
  <sub>Benzinga, 8 hours ago</sub>  
  CNBC host Jim Cramer said Thursday that the Pentagon's reported move to send a third aircraft carrier strike group and up to 10,000 more troops to the...
- [Will US Strike Iran Anytime Soon Given Trump's 10-Day Window For More Clarity? Here's What Bettors Think Amid The Military Build-Up In Middle East](https://stocktwits.com/news-articles/markets/equity/us-strike-on-iran-imminent-trump-10-day-window-what-bettors-think-prediction-markets/cZRNcKHR4x7)  
  <sub>Stocktwits, 13 hours ago</sub>  
  The U.S. military has reportedly deployed a vast array of forces in the Middle East, comprising fighter jets, refueling tankers, and two aircraft carriers.
- [October rate hike odds collapse after cooler payrolls print](https://seekingalpha.com/news/4649846-october-rate-hike-odds-collapse-after-cooler-payrolls-print)  
  <sub>Seeking Alpha, 27 minutes ago</sub>  
  A cooler September jobs report has sharply reduced the odds that the Federal Reserve will decide to raise rates at its October 28 meeting.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.45 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 90.61 (-1.3%), 50d 92.04 (-2.8%), 200d 94.48 (-5.3%); 50d below 200d
Momentum: RSI(14) 29.3 | MACD -0.822 vs signal -0.737 (histogram -0.085)
Returns: 1d +0.2% | 5d -0.6% | 1m -3.0% | 3m -5.0%
52-week range: 89.30 - 97.99 (now 1.7% of the way up)
Volatility: ATR(14) 0.48 (0.5% of price) | annualised 20d 6.2%
Volume: 0.56x the 20-day average
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
Share count change: 1 week: +1.9% (778.65M) over 7d
Shares outstanding: 467.65M | fund size: 41.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance Singapore, 7 hours ago</sub>  
  Invesco S&P 500 Equal Weight ETF (RSP) · -0.60% · -3.95% · 8.55% · 8.17% · 9.92% · 37.64% · 727.72%. Key events. Baseline. Advanced chart.
- [Invesco Exchange Traded Fd Tr S&P 500 Equal Weight Etf (RSP) Stock Price | Quotes & News](https://www.moomoo.com/stock/RSP-US?chain_id=Name1K9-3FXPhg.1lbtieg&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FAGG-US%22%7D)  
  <sub>Moomoo, 18 hours ago</sub>  
  Track the latest Invesco Exchange Traded Fd Tr S&P 500 Equal Weight Etf (RSP) price, quotes, financial information, news, and analyst ratings on moomoo App...
- [Why Stocks Could Defy Higher Rates & Keep Rallying: ETFs to Watch](https://www.tradingview.com/news/zacks:569853d1a094b:0-why-stocks-could-defy-higher-rates-keep-rallying-etfs-to-watch/)  
  <sub>TradingView, 4 hours ago</sub>  
  The stock market has enjoyed a strong run this year, and investors are wondering whether the rally will continue despite elevated bond yields and another...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 210.38 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 212.50 (-1.0%), 50d 216.68 (-2.9%), 200d 205.75 (+2.3%); 50d above 200d
Momentum: RSI(14) 39.8 | MACD -2.224 vs signal -1.999 (histogram -0.225)
Returns: 1d +0.7% | 5d -0.3% | 1m -3.8% | 3m -2.2%
52-week range: 182.18 - 222.77 (now 69.5% of the way up)
Volatility: ATR(14) 1.84 (0.9% of price) | annualised 20d 9.1%
Volume: 0.57x the 20-day average
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
Three-year record: +15.5% a year | beta to the market 0.83
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
Weighted price target: -1.1% above the current prices
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
Share count change: 1 week: +1.6% (1.56B) over 7d
Shares outstanding: 481.54M | fund size: 101.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Bitcoin Rises for Third Straight Week on Strong ETF Demand](https://www.bloomberg.com/news/articles/2026-10-02/bitcoin-rises-for-third-straight-week-on-strong-etf-demand?srnd=homepage-americas)  
  <sub>Bloomberg, 5 hours ago</sub>  
  Bitcoin climbed above $86000 on Friday, extending its rebound into a third straight week as investors returned to risk assets heading into October.
- [SPDR Portfolio TIPS ETF declares monthly distribution of $0.0189](https://www.tradingview.com/news/seekingalpha:ec1974919094b:0-spdr-portfolio-tips-etf-declares-monthly-distribution-of-0-0189/)  
  <sub>TradingView, 21 hours ago</sub>  
  Content provided by Seeking Alpha is intended for information purposes only, and that Seeking Alpha does not offer any personalist investment advice and is...
- [Investors Shed Mortgage Bond ETFs At Fastest Rate Since 2020](https://www.bloomberg.com/news/articles/2026-10-01/investors-shed-mortgage-bond-etfs-at-fastest-rate-since-2020?srnd=homepage-europe)  
  <sub>Bloomberg, 22 hours ago</sub>  
  Investors are selling mortgage bond funds at the fastest clip in more than six years as the debt takes a hit from big jumps in yields. Exchange-traded funds...
- [Skip Individual Dividend Stocks: These 3 ETFs Cut Your Risk in Half](https://247wallst.com/investing/etf/2026/10/02/skip-individual-dividend-stocks-these-3-etfs-cut-your-risk-in-half/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  One dividend cut in a 15-stock portfolio can wipe out a month of grocery money, but three ETFs solve that problem in very different ways, and the one built...
- [3 Growth ETFs to Buy Before 2027: One Charges Just 0.03%](https://247wallst.com/investing/etf/2026/10/01/3-growth-etfs-to-buy-before-2027-one-charges-just-0-03/)  
  <sub>24/7 Wall St., 15 hours ago</sub>  
  Three growth ETFs from Vanguard, Schwab, and State Street all chase the same megacap names yet deliver different outcomes depending on which index rulebook...
- [İş Yatırım Reports Market-Making Activity in ISMDL ETF](https://www.tipranks.com/news/company-announcements/is-yatirim-reports-market-making-activity-in-ismdl-etf-4)  
  <sub>TipRanks, 4 hours ago</sub>  
  The latest update is out from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ). İş Yatırım Menkul Değerler A.Ş., an investment services and brokerage firm...
- [İş Yatırım Discloses ISX30 ETF Market Making Transactions](https://www.tipranks.com/news/company-announcements/is-yatirim-discloses-isx30-etf-market-making-transactions)  
  <sub>TipRanks, 4 hours ago</sub>  
  An update from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) is now available. İş Yatırım Menkul Değerler A.Ş. reported its latest market making activity in...
- [Is Yatirim Reports No Market Making Activity in ISGLK ETF on 1 October](https://www.tipranks.com/news/company-announcements/is-yatirim-reports-no-market-making-activity-in-isglk-etf-on-1-october)  
  <sub>TipRanks, 4 hours ago</sub>  
  An update from Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) is now available. Is Yatirim Menkul Degerler AS reported that it conducted no market making...
- [Trump’s $8.4 Billion Korea Oil Deal Claim: Potential Ripple Effects on Energy and South Korea ETFs](https://www.tipranks.com/news/catalyst/trumps-8-4-billion-korea-oil-deal-claim-potential-ripple-effects-on-energy-and-south-korea-etfs)  
  <sub>TipRanks, 2 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “I am thrilled to announce the Republic of Korea Deal...
- [3 Best Vanguard ETFs With 20%+ Upside That Are Crushing the S&P 500](https://www.tipranks.com/news/3-best-vanguard-etfs-with-20-upside-that-are-crushing-the-sp-500)  
  <sub>TipRanks, 16 hours ago</sub>  
  The SP 500 has taken investors on quite a ride this year, yet it has still managed to climb about 13%. That's a solid return, but some Vanguard ETFs have <.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.39 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 105.33 (-0.9%), 50d 106.45 (-1.9%), 200d 109.34 (-4.5%); 50d below 200d
Momentum: RSI(14) 33.1 | MACD -0.734 vs signal -0.670 (histogram -0.065)
Returns: 1d +0.1% | 5d -0.1% | 1m -2.3% | 3m -3.8%
52-week range: 104.01 - 112.20 (now 4.6% of the way up)
Volatility: ATR(14) 0.41 (0.4% of price) | annualised 20d 4.9%
Volume: 0.26x the 20-day average
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
Three-year record: +3.6% a year | beta to the market 0.68
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
Share count change: 1 week: +1.5% (217.66M) over 7d
Shares outstanding: 144.30M | fund size: 15.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [The secret signs the bond sell-off might be ending](https://www.cnbc.com/amp/2026/10/02/the-secret-signs-the-bond-sell-off-might-be-ending.html)  
  <sub>CNBC, 4 hours ago</sub>  
  As the U.S. bond market firmed Thursday and the iShares 20+ Year Treasury Bond ETF (TLT) posted its best intraday rally in at least a month,...
- [BofA’s Hartnett calls on investors to ‘buy humiliation’ in bond rout (TLT:NASDAQ)](https://seekingalpha.com/news/4649830-bofa-s-hartnett-calls-on-investors-to-buy-humiliation-in-bond-rout)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  BofA's Hartnett says “buy humiliation”: add Treasuries and IG tech bonds as returns hit century lows.
- [The Bond Market Is Repeating a Pattern Not Seen in Years. Here's What History Says Comes Next.](https://www.theglobeandmail.com/investing/markets/stocks/TLT-Q/pressreleases/4923415/the-bond-market-is-repeating-a-pattern-not-seen-in-years-here-s-what-history-says-comes-next/)  
  <sub>The Globe and Mail, 6 hours ago</sub>  
  Detailed price information for 20+ Year Treas Bond Ishares ETF (TLT-Q) from The Globe and Mail including charting and trades.
- [TLT Hits Record Low as 30-Year Yield Nears 5.7%. Why Are Retail Buyers Piling In?](https://www.ebc.com/forex/tlt-hits-record-low-as-30-year-yield-nears-5-7-why-are-retail-buyers-piling-in)  
  <sub>EBC Financial Group, 8 hours ago</sub>  
  TLT has fallen to record-low territory as the 30-year Treasury yield climbed toward 5.7%, yet reported retail demand for long-duration Treasury ETFs has...
- [Daily ETF Flows: BIL On Top](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-bil-top-210005431.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for September 30, 2026.
- [Bond Markets Functioning In An ‘Orderly’ Manner? El-Erian Calls IMF's Reassurance 'Highly Unusual'](https://www.tradingview.com/news/stocktwits:4e5584379094b:0-bond-markets-functioning-in-an-orderly-manner-el-erian-calls-imf-s-reassurance-highly-unusual/)  
  <sub>TradingView, 10 hours ago</sub>  
  Mohamed El-Erian, chief economic adviser at Allianz, said on Thursday that the International Monetary Fund's comments about how bond markets are functioning...
- [Market Reaction To Micron Earnings And Broadcom Deal Signals A Shift In AI Trade](https://www.benzinga.com/Opinion/26/10/62119909/market-reaction-to-micron-earnings-and-broadcom-deal-signals-a-shift-in-ai-trade)  
  <sub>Benzinga, 20 hours ago</sub>  
  Bond Danger Signal Please click here for an enlarged chart of iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT). Note the following: The chart shows TLT has...
- [Top Citadel Strategist Sees October Offering A Good Entry Point To Retail Investors Ahead Of Earnings Season](https://www.tradingview.com/news/stocktwits:ea2cac435094b:0-top-citadel-strategist-sees-october-offering-a-good-entry-point-to-retail-investors-ahead-of-earnings-season/)  
  <sub>TradingView, 21 hours ago</sub>  
  Retail traders are positioned to return to the U.S. equity market in October following a noticeable retreat last month, according to analysis from Citadel...
- [The Market’s Hidden Weakness Is Finally Too Big to Ignore](https://pro.thestreet.com/market-commentary/the-markets-hidden-weakness-is-finally-too-big-to-ignore)  
  <sub>TheStreet Pro, 4 hours ago</sub>  
  Oil is down about 4% early Friday and the iShares 20+ Year Treasury Bond ETF (TLT) is flat as we wait for the September jobs report.
- [Nasdaq, S&P 500 Futures Rise As Chip Rally Counters Iran Jitters Ahead Of Big Tech Earnings: Why IREN, ACHR, TSLA, BA Stocks Are Drawing Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-futures-rise-as-chip-rally-counters-iran-jitters-ahead-of-big-tech-earnings/cZZ1tCdR7HO)  
  <sub>Stocktwits, 16 hours ago</sub>  
  The VanEck Semiconductor ETF was up 0.41% at close, reversing three consecutive days of declines. However, tensions in the Middle East continued to rise...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 78.17 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 80.33 (-2.7%), 50d 81.68 (-4.3%), 200d 85.43 (-8.5%); 50d below 200d
Momentum: RSI(14) 30.1 | MACD -1.127 vs signal -0.849 (histogram -0.278)
Returns: 1d +0.6% | 5d -1.5% | 1m -4.6% | 3m -8.5%
52-week range: 77.71 - 92.06 (now 3.2% of the way up)
Volatility: ATR(14) 0.79 (1.0% of price) | annualised 20d 10.7%
Volume: 0.47x the 20-day average
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
Three-year record: -0.1% a year | beta to the market 2.39
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
Shares outstanding: 109.70M | fund size: 8.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Gold falls for a second week: why is $4,000 proving so hard to break?](https://invezz.com/sg/news/2026/10/02/gold-falls-for-a-second-week-why-is-dollar4000-proving-so-hard-to-break/)  
  <sub>Invezz, 7 hours ago</sub>  
  Gold prices headed for a second straight weekly decline on Friday as a firm dollar and historically high US Treasury yields kept pressure on bullion,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.85 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 28.43 (+1.5%), 50d 28.26 (+2.1%), 200d 27.75 (+4.0%); 50d above 200d
Momentum: RSI(14) 70.2 | MACD 0.189 vs signal 0.139 (histogram 0.050)
Returns: 1d -0.4% | 5d +0.8% | 1m +2.4% | 3m +1.9%
52-week range: 26.47 - 28.96 (now 95.8% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 4.6%
Volume: 0.16x the 20-day average
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
Share count change: 1 week: -0.8% (-2.53M) over 7d
Shares outstanding: 10.39M | fund size: 299.90M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### US technology (XLK) · Sector or country — BULLISH, confidence 0.40

**Result:** ACCEPTED · 35 shares · submitted buy 35 XLK @ ~199.99, stop 193.58

**In the model's own words:**

> Slightly bullish based on strong analyst coverage, modest net inflows, and continued uptrend despite high valuations and overbought technicals.

**Main reasons it gave:**
- All analyst ratings are buy with a +22.8% price target
- Net inflows of +0.9% share count over the past week
- Technicals show price above 20d, 50d, 200d SMAs and RSI at 70 (overbought)
- High valuation metrics (P/E 33, P/B 11.4) amid rising yields
- Macro environment stable with no policy surprise; yields slightly up

<details><summary><b>News</b> — score +0.20</summary>

- [Sector Update: Tech Stocks Gain Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-tech-stocks-gain-afternoon-195143826.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Tech stocks advanced late Thursday afternoon with the State Street Technology Select Sector SPDR ETF (XLK) rising 1.2% and the State Street SPDR S&P...
- [Exchange-Traded Funds Mixed, US Equities Fall After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-mixed-us-171345834.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded fund IWM rose and IVV edged lower. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [Alphabet Slips After Gemini 4 Argon Launch as Tech Sector Rises; Microsoft Holds Steady, Amazon Dips](https://247wallst.com/investing/2026/10/01/alphabet-slips-after-gemini-4-argon-launch-as-tech-sector-rises-microsoft-holds-steady-amazon-dips/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Google just launched a frontier AI model that can hunt down security vulnerabilities automatically, yet investors are selling the stock while the rest of...
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday Amid Jobs Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-133147980.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.9% and the actively trad.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 200.85 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 191.32 (+5.0%), 50d 186.32 (+7.8%), 200d 164.95 (+21.8%); 50d above 200d
Momentum: RSI(14) 70.0 | MACD 3.466 vs signal 2.726 (histogram 0.740)
Returns: 1d +1.5% | 5d +2.3% | 1m +9.4% | 3m +9.4%
52-week range: 127.50 - 200.85 (now 100.0% of the way up)
Volatility: ATR(14) 3.20 (1.6% of price) | annualised 20d 17.9%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 33.01 | P/B 11.41 | P/S 8.77 | 3y earnings growth n/a
Yield: 0.4%
Three-year record: +34.5% a year | beta to the market 1.50
Cost and size: expense ratio 0.08% | net assets 121.44B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 14.4%, Apple Inc 12.5%, Microsoft Corp 10.1%, Broadcom Inc 4.7%, Micron Technology Inc 4.0%
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
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.8% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-01 Morgan Stanley: main, Overweight -> Overweight
  - MSFT: 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-01 Mizuho: main, Outperform -> Outperform
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
Share count change: 1 week: +0.9% (1.16B) over 7d
Shares outstanding: 624.53M | fund size: 125.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.15

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Overall neutral stance; analyst view bullish but limited coverage, no net fund flows, fundamentals slightly overvalued, technicals modestly oversold with low volume.

**Main reasons it gave:**
- Analyst coverage: 100% buy rating on 39.6% of fund, weighted price target +14.5%
- Fund flows: share count unchanged (+0.0%) over past week
- Fund fundamentals: high valuation (P/E 25.14, P/B 4.58) vs moderate yield 2.6%
- Technicals: price below 20‑day SMA (80.54 vs 82.62) and RSI 33.6 (oversold) with low volume

<details><summary><b>News</b> — score +0.00</summary>

- [Which Consumer Staples ETF Offers Better Value: XLP or IYK?](https://www.fool.com/coverage/etfs/2026/10/01/which-consumer-staples-etf-offers-better-value-xlp-or-iyk/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  State Street Consumer Staples Select Sector SPDR ETF (XLP -0.34%)offers a lower-cost, more concentrated approach to the sector than the broader,...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday Amid Jobs Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-133147980.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.9% and the actively trad.
- [Exchange-Traded Funds Mixed, US Equities Fall After Midday](https://www.moomoo.com/news/post/1000521505/exchange-traded-funds-mixed-us-equities-fall-after-midday)  
  <sub>Moomoo, 21 hours ago</sub>  
  BroadMarket IndicatorsBroad-market exchange-traded fund IWM rose and IVV edged lower. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [Sector Update: Consumer](https://www.bitget.com/amp/news/detail/12560605901065)  
  <sub>Bitget, 16 hours ago</sub>  
  03:23 PM EDT, 10/01/2026 (MT Newswires) -- Consumer stocks were mixed late Thursday afternoon with the State Street Consumer Staples Select Sector SPDR ETF...
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://www.bitget.com/amp/news/detail/12560605901115)  
  <sub>Bitget, 16 hours ago</sub>  
  03:44 PM EDT, 10/01/2026 (MT Newswires) -- Consumer stocks were mixed late Thursday afternoon with the State Street Consumer Staples Select Sector SPDR ETF...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 80.54 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 82.62 (-2.5%), 50d 84.39 (-4.6%), 200d 83.73 (-3.8%); 50d above 200d
Momentum: RSI(14) 33.6 | MACD -1.053 vs signal -0.845 (histogram -0.208)
Returns: 1d +0.3% | 5d -1.9% | 1m -5.8% | 3m -4.2%
52-week range: 75.60 - 90.01 (now 34.3% of the way up)
Volatility: ATR(14) 0.97 (1.2% of price) | annualised 20d 11.6%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 25.14 | P/B 4.58 | P/S 1.36 | 3y earnings growth n/a
Yield: 2.6%
Three-year record: +8.3% a year | beta to the market 0.49
Cost and size: expense ratio 0.08% | net assets 14.52B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 9.8%, Costco Wholesale Corp 8.9%, Coca-Cola Co 7.3%, Procter & Gamble Co 7.2%, Philip Morris International Inc 6.2%
Sector mix: Consumer defensive 98.2%, Consumer cyclical 1.8%
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
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.5% above the current prices
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
Shares outstanding: 210.17M | fund size: 16.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals show a downtrend but no decisive break, while analyst coverage is bullish and fund inflows are positive.

**Main reasons it gave:**
- Fund inflows: share count +7.4% over 7 days
- Analyst rating: 100% buy, price target +41.6% above current price
- Technical trend: price below 20d/50d/200d SMAs, RSI 25.9, negative MACD
- Macro: no policy or rate surprise; yields stable, VIX low

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 84.93 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 91.65 (-7.3%), 50d 92.79 (-8.5%), 200d 92.57 (-8.3%); 50d above 200d
Momentum: RSI(14) 25.9 | MACD -2.375 vs signal -1.431 (histogram -0.944)
Returns: 1d +0.7% | 5d -4.1% | 1m -13.2% | 3m -9.6%
52-week range: 68.39 - 102.94 (now 47.9% of the way up)
Volatility: ATR(14) 1.78 (2.1% of price) | annualised 20d 15.8%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.60 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.6% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, BMA
Recent rating changes among them:
  - MELI: 2026-09-03 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
  - BMA: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: +7.4% (55.32M) over 7d
Shares outstanding: 9.44M | fund size: 801.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, mixed technicals, flat flows, but strong analyst coverage and solid fundamentals keep the view neutral overall.

**Main reasons it gave:**
- Analyst coverage: 100% buy rating on top holdings covering 37.6% of fund, weighted price target +22.5% above current price
- Fund fundamentals: moderate valuation (P/E 17.9), strong 3‑year performance (+32.8% per year), low expense ratio (0.59%)
- Technical indicators: price below 20‑day SMA, MACD negative, low volume (0.18× 20‑day average) indicating weak momentum
- Macro environment: no policy surprise, yields slightly up, dollar stronger, VIX low, no major data shock

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 122.50 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 123.72 (-1.0%), 50d 122.62 (-0.1%), 200d 122.58 (-0.1%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD -0.348 vs signal 0.063 (histogram -0.411)
Returns: 1d +1.1% | 5d -0.4% | 1m -1.3% | 3m -0.4%
52-week range: 97.88 - 137.69 (now 61.8% of the way up)
Volatility: ATR(14) 1.75 (1.4% of price) | annualised 20d 18.1%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.23 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.5% above the current prices
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
Shares outstanding: 2.55M | fund size: 312.38M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals mixed with no decisive break, positive but modest fund flows and analyst coverage, strong fundamentals but not enough for a clear directional edge.

**Main reasons it gave:**
- Fund flows +2.9% share count increase (net inflow)
- Analyst coverage 90.3% buy, weighted price target +3% above current
- RSI 39 (near oversold) and price below 20‑day SMA, no decisive technical break
- US macro stable: yields unchanged, inflation 3.4% below Fed target 4%

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 43.06 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 44.77 (-3.8%), 50d 44.09 (-2.3%), 200d 39.52 (+9.0%); 50d above 200d
Momentum: RSI(14) 39.0 | MACD -0.085 vs signal 0.190 (histogram -0.275)
Returns: 1d -0.4% | 5d -4.0% | 1m -2.5% | 3m +7.9%
52-week range: 31.78 - 45.76 (now 80.7% of the way up)
Volatility: ATR(14) 0.68 (1.6% of price) | annualised 20d 20.4%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.47 | P/B 2.00 | P/S 1.36 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +44.1% a year | beta to the market 0.73
Cost and size: expense ratio 0.59% | net assets 848.26M
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: PKO Bank Polski SA 15.4%, Orlen SA 13.8%, Bank Polska Kasa Opieki SA 7.1%, Powszechny Zaklad Ubezpieczen SA 6.4%, KGHM Polska Miedz SA 4.6%
Sector mix: Financial services 46.1%, Energy 14.5%, Consumer cyclical 12.7%, Basic materials 6.8%
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
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.0% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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
Share count change: 1 week: +2.9% (23.19M) over 7d
Shares outstanding: 19.19M | fund size: 826.48M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: analyst view slightly bearish, fund inflows modestly bullish, technicals slightly bearish, macro neutral; overall net effect is neutral.

**Main reasons it gave:**
- Weighted analyst rating: 40.4% sell, price target -5.6% below current price (bearish)
- Fund flows: +2.4% share count increase over 1 week indicating net inflows (bullish)
- Technical indicators: price below 20d, 50d, 200d SMAs; RSI 41.8; MACD negative (slightly bearish)
- Macro: US Treasury yields stable, no major data surprise; VIX modestly up (neutral)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 28.39 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 28.87 (-1.7%), 50d 29.44 (-3.6%), 200d 28.63 (-0.9%); 50d above 200d
Momentum: RSI(14) 41.8 | MACD -0.364 vs signal -0.306 (histogram -0.057)
Returns: 1d +1.4% | 5d -0.2% | 1m -5.5% | 3m +0.2%
52-week range: 24.95 - 30.43 (now 62.7% of the way up)
Volatility: ATR(14) 0.38 (1.4% of price) | annualised 20d 18.1%
Volume: 0.63x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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

<details><summary><b>What analysts and big funds say</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.35</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.43 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.6% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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
Share count change: 1 week: +2.4% (31.32M) over 7d
Shares outstanding: 46.92M | fund size: 1.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, but modestly positive analyst coverage, net inflows, and supportive fundamentals keep the view neutral.

**Main reasons it gave:**
- Analyst coverage: 74.3% buy, weighted price target +6.1% above current price
- Fund flows: +3.1% share count over the week indicating net inflows
- Technical: price above 200‑day SMA and RSI 38.4 suggesting potential oversold condition
- Macro: stable yields and low VIX, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.81 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 60.00 (-2.0%), 50d 60.70 (-3.1%), 200d 57.72 (+1.9%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -0.635 vs signal -0.444 (histogram -0.191)
Returns: 1d +0.9% | 5d -1.3% | 1m -4.0% | 3m +1.3%
52-week range: 49.72 - 62.64 (now 70.4% of the way up)
Volatility: ATR(14) 0.65 (1.1% of price) | annualised 20d 11.4%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.1% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-23 Wedbush: reit, Outperform -> Outperform
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.1% (205.65M) over 7d
Shares outstanding: 116.20M | fund size: 6.83B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst coverage is bullish (82% buy, +14.1% price target) and fund flows are positive (+2.9% share count), but technicals are bearish (price below 20‑day SMA, RSI 39.3, MACD negative) and macro data show no surprise. No decisive macro catalyst or technical break justifies a directional tilt.

**Main reasons it gave:**
- Analyst coverage: 82% buy rating, weighted price target +14.1% above current price
- Fund flows: share count up 2.9% over the past week
- Technical indicators: price below 20‑day SMA, RSI 39.3, MACD negative
- Macro: yields unchanged, VIX low at 15.5, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 50.08 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 51.37 (-2.5%), 50d 52.26 (-4.2%), 200d 51.39 (-2.5%); 50d above 200d
Momentum: RSI(14) 39.3 | MACD -0.627 vs signal -0.441 (histogram -0.187)
Returns: 1d +1.4% | 5d -2.8% | 1m -4.7% | 3m -2.0%
52-week range: 45.38 - 54.72 (now 50.4% of the way up)
Volatility: ATR(14) 0.73 (1.5% of price) | annualised 20d 15.7%
Volume: 0.23x the 20-day average
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
Three-year record: +18.7% a year | beta to the market 1.19
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.1% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-01 Keybanc: main, Overweight -> Overweight
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
Share count change: 1 week: +2.9% (21.06M) over 7d
Shares outstanding: 14.94M | fund size: 748.09M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall due to lack of macro surprise, flat fund flows, bearish technicals, and a bullish analyst view that is not enough to outweigh other neutral factors.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand shift
- Technical indicators bearish: price below 20‑day SMA, RSI 38.2, MACD negative
- No macro surprise; inflation 3.4% and unemployment 4.2% in line with expectations
- Analyst view bullish (78% buy, +17% price target) but not supported by macro or technicals

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 41.41 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 42.37 (-2.3%), 50d 43.10 (-3.9%), 200d 42.38 (-2.3%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.523 vs signal -0.390 (histogram -0.133)
Returns: 1d +1.4% | 5d -2.0% | 1m -4.8% | 3m -2.9%
52-week range: 38.08 - 44.59 (now 51.2% of the way up)
Volatility: ATR(14) 0.51 (1.2% of price) | annualised 20d 14.2%
Volume: 0.20x the 20-day average
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
Three-year record: +18.8% a year | beta to the market 0.98
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.1% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed signals: bearish technicals but bullish analyst view and modest inflows.

**Main reasons it gave:**
- RSI(14) at 29.4, price below 20‑day, 50‑day and 200‑day SMAs
- Analyst consensus 100% buy with weighted price target +16% above current price
- Share count up 1.7% over the past week, indicating net inflows
- Macro data shows no surprise; yields stable, VIX low (15.5) and no policy shock

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 57.46 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 60.32 (-4.7%), 50d 61.53 (-6.6%), 200d 58.00 (-0.9%); 50d above 200d
Momentum: RSI(14) 29.4 | MACD -0.940 vs signal -0.610 (histogram -0.330)
Returns: 1d +0.4% | 5d -4.9% | 1m -6.4% | 3m -6.0%
52-week range: 50.31 - 63.35 (now 54.8% of the way up)
Volatility: ATR(14) 0.82 (1.4% of price) | annualised 20d 17.9%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.25 | P/B 1.85 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +28.8% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.8%, Intesa Sanpaolo 13.6%, Enel SpA 10.3%, Ferrari NV 5.2%, Eni SpA 5.0%
Sector mix: Financial services 52.6%, Utilities 16.3%, Industrials 9.7%, Consumer cyclical 9.0%
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
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.0% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, RACE.MI, ENI.MI
Recent rating changes among them:
  - RACE.MI: 2026-09-30 Morgan Stanley: main, Overweight -> Overweight
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
Share count change: 1 week: +1.7% (18.14M) over 7d
Shares outstanding: 19.01M | fund size: 1.09B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro data (inflation 3.4%, unemployment 4.2%) in line with expectations, no surprise
- Technicals: price above 20d, 50d, 200d SMAs, RSI 58.7, MACD near zero, but volume 0.28x average
- Analyst coverage thin (17% of fund) with 100% buy rating and +17% price target
- Positioning: net long 3.6% of OI down 0.7% week, while fund inflows +1.5% share count

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: QQQ Holds Up Better Than SPY, DIA And Asian Stocks Amid Bond Market Rout This Week](https://finance.yahoo.com/markets/stocks/articles/stocktwits-passport-portfolio-qqq-holds-061913514.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  The Invesco QQQ Trust, which tracks the Nasdaq, has posted the lowest decline amongst its peers so far this week, bolstered in part by the resilience of...
- [Asian equities mostly lower amid bond volatility, oil pressures (EWJ:NYSEARCA)](https://seekingalpha.com/news/4649715-asian-equities-mostly-lower-amid-bond-volatility-oil-pressures)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Asian stock market update: Nikkei slips, Hang Seng plunges, ASX rises as investors weigh Fed rate outlook, oil and geopolitics.
- [Stocktwits AI Roundup: Micron’s Blowout Quarter, Nvidia’s $150B Buyback And The Race For AI Agents](https://stocktwits.com/news-articles/markets/equity/stocktwits-ai-roundup-micron-s-blowout-quarter-nvidia-s-150-b-buyback-and-the-race-for-ai-agents/cZDj2YGRB0x)  
  <sub>Stocktwits, 15 hours ago</sub>  
  AI infrastructure demand remains strong, but soaring costs and intensifying competition are keeping investors on edge.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 99.14 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 97.48 (+1.7%), 50d 95.98 (+3.3%), 200d 90.39 (+9.7%); 50d above 200d
Momentum: RSI(14) 58.7 | MACD 0.462 vs signal 0.463 (histogram -0.000)
Returns: 1d +1.8% | 5d +1.2% | 1m +3.2% | 3m +4.1%
52-week range: 78.36 - 99.14 (now 100.0% of the way up)
Volatility: ATR(14) 1.49 (1.5% of price) | annualised 20d 18.7%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Japan Stock
What it holds: P/E 19.11 | P/B 2.01 | P/S 1.68 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +20.8% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 22.69B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.6%, Toyota Motor Corp 3.5%, Sumitomo Mitsui Financial Group Inc 3.0%, Tokyo Electron Ltd 3.0%, Advantest Corp 2.9%
Sector mix: Industrials 22.9%, Technology 21.5%, Financial services 19.1%, Consumer cyclical 11.6%
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
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.0% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 3.6% of open interest (21,974 contracts)
Change on the week: -0.7% of open interest
Crowding: 32% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.5% (345.75M) over 7d
Shares outstanding: 233.24M | fund size: 23.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance due to lack of material macro or flow catalyst; mixed fundamentals and weak technical momentum offset bullish analyst coverage.

**Main reasons it gave:**
- Fund flows flat (0% change) over the past week, indicating no net demand
- Analyst coverage: 74.5% buy, 25.5% hold, weighted price target +12.3% above current price
- Technical indicators: price below 20‑day SMA (-1.9%) and RSI 35.4, showing weak momentum
- Macro data: Treasury yields stable, inflation 3.4% and unemployment 4.2% in line with expectations, no surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 59.24 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 60.42 (-1.9%), 50d 62.29 (-4.9%), 200d 61.62 (-3.9%); 50d above 200d
Momentum: RSI(14) 35.4 | MACD -0.842 vs signal -0.761 (histogram -0.081)
Returns: 1d +0.7% | 5d -2.3% | 1m -5.8% | 3m -7.0%
52-week range: 55.06 - 65.08 (now 41.8% of the way up)
Volatility: ATR(14) 0.69 (1.2% of price) | annualised 20d 13.9%
Volume: 0.91x the 20-day average
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
Three-year record: +12.9% a year | beta to the market 0.91
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
Shares outstanding: 28.62M | fund size: 1.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, flat fund flows, mixed technicals, and bullish analyst view limited to <50% of fund weight keep the overall stance neutral.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% over 7d)
- No macro surprise: yields stable, inflation 3.4% and unemployment 4.2% in line with expectations
- Technical indicators mixed: price slightly above 20‑day SMA, below 50‑day SMA, low volume (0.18× avg)
- Analyst consensus strongly bullish (100% buy, +25% price target) but covers only 44% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

- [Playing it safe with your money? You could be missing out](https://www.ewn.co.za/2026/10/02/playing-it-safe-with-your-money-you-could-be-missing-out)  
  <sub>EWN, 6 hours ago</sub>  
  Economic uncertainty can make it tempting to do nothing with your money, but inaction can be a decision in itself.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 68.08 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 67.67 (+0.6%), 50d 68.21 (-0.2%), 200d 64.32 (+5.8%); 50d above 200d
Momentum: RSI(14) 51.1 | MACD -0.163 vs signal -0.222 (histogram 0.059)
Returns: 1d +2.2% | 5d +0.1% | 1m +0.1% | 3m -1.1%
52-week range: 55.33 - 71.61 (now 78.3% of the way up)
Volatility: ATR(14) 0.98 (1.4% of price) | annualised 20d 18.9%
Volume: 0.18x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +24.8% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.0% above the current prices
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
Shares outstanding: 5.55M | fund size: 377.84M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals show a downtrend but no decisive break, and fund flows are flat. Analyst coverage is modestly bullish (+7% target) and fundamentals are solid, but none provide a clear directional catalyst.

**Main reasons it gave:**
- Flat fund flows (share count +0.0% week)
- Technicals: price 58.26 below 20‑day SMA 60.83 and 50‑day SMA 61.57, RSI 33.9, MACD negative, volume 0.20× 20‑day average
- Macro: yields stable (10‑yr +0.02, 3‑mo -0.09), dollar up modestly, VIX unchanged
- Analyst coverage: 52% buy, 48% hold, price target +7% (moderately bullish) but no decisive catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 58.26 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 60.83 (-4.2%), 50d 61.57 (-5.4%), 200d 57.59 (+1.2%); 50d above 200d
Momentum: RSI(14) 33.9 | MACD -0.764 vs signal -0.420 (histogram -0.344)
Returns: 1d +0.7% | 5d -4.8% | 1m -5.9% | 3m -3.4%
52-week range: 48.33 - 63.23 (now 66.6% of the way up)
Volatility: ATR(14) 0.88 (1.5% of price) | annualised 20d 18.3%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.28 | P/B 2.22 | P/S 1.82 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +33.4% a year | beta to the market 0.87
Cost and size: expense ratio 0.50% | net assets 2.26B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.0%, Iberdrola SA 12.1%, CaixaBank SA 4.6%, Industria De Diseno Textil SA Share From Split 4.4%
Sector mix: Financial services 45.4%, Utilities 20.0%, Industrials 14.4%, Technology 5.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.42</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.42</summary>

```text
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.0% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals are below short‑term averages, modest inflows, and analyst coverage is bullish but limited to 36% of the fund.

**Main reasons it gave:**
- Technical price below 20‑day SMA (46.17 vs 47.41) indicating bearish short‑term trend
- Analyst coverage shows 69.5% buy rating with +15.3% price target, but only covers 36% of the fund
- Fund flows show 1.5% share count increase over the week, indicating modest net inflow
- Macro data shows no policy or rate surprise; yields unchanged, VIX low, dollar modestly higher

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 46.17 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 47.41 (-2.6%), 50d 47.99 (-3.8%), 200d 46.67 (-1.1%); 50d above 200d
Momentum: RSI(14) 34.0 | MACD -0.462 vs signal -0.300 (histogram -0.163)
Returns: 1d +0.6% | 5d -2.4% | 1m -4.2% | 3m -2.2%
52-week range: 41.34 - 49.39 (now 60.1% of the way up)
Volatility: ATR(14) 0.49 (1.1% of price) | annualised 20d 12.0%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.08 | P/B 2.29 | P/S 1.52 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +18.2% a year | beta to the market 0.68
Cost and size: expense ratio 0.50% | net assets 3.79B
What it is made of: Stocks 97.9%, Other 1.1%, Cash 0.9%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 7.8%, AstraZeneca PLC 7.6%, Rolls-Royce Holdings PLC 5.3%, Unilever PLC 4.3%
Sector mix: Financial services 26.4%, Consumer defensive 14.3%, Industrials 13.9%, Healthcare 12.7%
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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 69.5% | hold 30.5% | sell 0.0% (mean 2.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.3% above the current prices
Holdings read: HSBA.L, SHEL.L, AZN.L, RR.L, ULVR.L
Recent rating changes among them:
  - AZN.L: 2026-08-24 CICC: init, ? -> Outperform
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
Share count change: 1 week: +1.5% (53.62M) over 7d
Shares outstanding: 81.04M | fund size: 3.74B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals bearish but not decisive, analyst view bullish, fundamentals modestly positive, flat fund flows.

**Main reasons it gave:**
- Analyst consensus 100% buy with +18.9% price target
- Technical indicators show price below 20/50/200‑day SMAs, RSI 33.6, negative MACD
- Fund flows flat over past week (share count unchanged)
- Macro data unchanged, no policy or rate surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 70.45 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 73.65 (-4.3%), 50d 75.30 (-6.4%), 200d 75.79 (-7.0%); 50d below 200d
Momentum: RSI(14) 33.6 | MACD -1.345 vs signal -0.978 (histogram -0.367)
Returns: 1d +1.0% | 5d -3.9% | 1m -7.6% | 3m -7.8%
52-week range: 64.39 - 81.23 (now 36.0% of the way up)
Volatility: ATR(14) 1.33 (1.9% of price) | annualised 20d 17.4%
Volume: 0.28x the 20-day average
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
Three-year record: +10.7% a year | beta to the market 1.05
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.9% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals positive but no decisive break, modest inflows, fundamentals modestly attractive; overall neutral stance.

**Main reasons it gave:**
- Fund flows: share count +2.7% over the past week
- Technical: price above 20‑day, 50‑day, 200‑day SMAs; MACD positive; volume 0.41× 20‑day average
- Fundamentals: P/E 10.41 indicating low valuation
- Macro: US Treasury yields stable; no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [ETF Inflows Top Last Year's Record With a Quarter to Spare](https://finance.yahoo.com/markets/stocks/articles/etf-inflows-top-last-years-043228801.html)  
  <sub>Yahoo Finance, 10 hours ago</sub>  
  Investors added $150.6 billion to US-listed ETFs in September, according to fresh data from Bloomberg. That brought year-to-date inflows to $1.54 trillion,...
- [Stocktwits AI Roundup: Micron’s Blowout Quarter, Nvidia’s $150B Buyback And The Race For AI Agents](https://stocktwits.com/news-articles/markets/equity/stocktwits-ai-roundup-micron-s-blowout-quarter-nvidia-s-150-b-buyback-and-the-race-for-ai-agents/cZDj2YGRB0x)  
  <sub>Stocktwits, 15 hours ago</sub>  
  AI infrastructure demand remains strong, but soaring costs and intensifying competition are keeping investors on edge.
- [America buys AI, Asia reaps the rewards (AIQ:NASDAQ)](https://seekingalpha.com/news/4649175-america-buys-ai-asia-reaps-the-rewards)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  AI investment is boosting Asia more than the U.S. as hardware imports surge.
- [Stocktwits Passport Portfolio: QQQ Holds Up Better Than SPY, DIA And Asian Stocks Amid Bond Market Rout This Week](https://finance.yahoo.com/markets/stocks/articles/stocktwits-passport-portfolio-qqq-holds-061913514.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  The Invesco QQQ Trust, which tracks the Nasdaq, has posted the lowest decline amongst its peers so far this week, bolstered in part by the resilience of...
- [SK Hynix stock falls 8% on AI development slowdown fears](https://scanx.trade/stock-market-news/equity-markets/sk-hynix-stock-falls-3-5-profit-taking-macro-pressures/50587236)  
  <sub>scanx.trade, 15 hours ago</sub>  
  SK Hynix shares fell 7.53% to $175.76 in premarket trading on Monday. Nasdaq futures dropped 1.59% amid concerns over slowed frontier AI development.
- [Trump’s $8.4 Billion Korea Oil Deal Claim: Potential Ripple Effects on Energy and South Korea ETFs](https://www.tipranks.com/news/catalyst/trumps-8-4-billion-korea-oil-deal-claim-potential-ripple-effects-on-energy-and-south-korea-etfs)  
  <sub>TipRanks, 2 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “I am thrilled to announce the Republic of Korea Deal...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 192.24 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 185.10 (+3.9%), 50d 176.66 (+8.8%), 200d 156.24 (+23.0%); 50d above 200d
Momentum: RSI(14) 57.7 | MACD 2.381 vs signal 2.211 (histogram 0.170)
Returns: 1d +3.3% | 5d +2.7% | 1m +7.5% | 3m +1.3%
52-week range: 80.72 - 219.20 (now 80.5% of the way up)
Volatility: ATR(14) 6.15 (3.2% of price) | annualised 20d 48.6%
Volume: 0.41x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +49.4% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.7% (760.22M) over 7d
Shares outstanding: 148.93M | fund size: 28.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, mixed technicals, and bullish analyst view limited to 40.9% coverage do not justify a directional tilt.

**Main reasons it gave:**
- No macro surprise: yields stable, inflation 3.4% near target, Fed unchanged
- Flat fund flows: share count unchanged (+0.0% over 7d)
- Technical indicators mixed: price slightly below 20‑day SMA, RSI 51, MACD histogram negative
- Analyst view bullish (100% buy, +27.3% price target) but covers only 40.9% of fund
- No news in past 24h

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 37.08 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 37.56 (-1.3%), 50d 36.32 (+2.1%), 200d 36.37 (+2.0%); 50d below 200d
Momentum: RSI(14) 51.1 | MACD 0.140 vs signal 0.298 (histogram -0.158)
Returns: 1d -0.1% | 5d +0.7% | 1m -2.6% | 3m +6.2%
52-week range: 28.79 - 41.73 (now 64.1% of the way up)
Volatility: ATR(14) 0.77 (2.1% of price) | annualised 20d 19.6%
Volume: 0.56x the 20-day average
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
Three-year record: +13.1% a year | beta to the market 0.84
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
Weighted price target: +27.3% above the current prices
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
Shares outstanding: 200.55M | fund size: 7.44B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, bearish technicals but no decisive break, flat fund flows, and strong analyst buy bias offset by neutral overall outlook.

**Main reasons it gave:**
- Technical: price ~6% below 20‑day SMA, RSI 35.3 (weak momentum)
- Analyst: 78% buy rating, weighted price target +33% above current
- Fund flows: share count unchanged (flat) over past week
- Macro: US Treasury yields stable, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 63.53 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 67.60 (-6.0%), 50d 67.80 (-6.3%), 200d 69.14 (-8.1%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -1.403 vs signal -0.765 (histogram -0.638)
Returns: 1d +1.1% | 5d -4.4% | 1m -9.2% | 3m -1.7%
52-week range: 60.43 - 81.60 (now 14.6% of the way up)
Volatility: ATR(14) 1.29 (2.0% of price) | annualised 20d 24.9%
Volume: 0.09x the 20-day average
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
Three-year record: +26.2% a year | beta to the market 1.02
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 78.3% | hold 21.7% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.1% above the current prices
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
Shares outstanding: 7.90M | fund size: 501.89M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as macro conditions (higher yields, strong dollar) are slightly bearish, technicals show modest bearish momentum, but analyst consensus is fully bullish (+19.3% price target) and fund flows are strongly positive (+9.6% share count increase). Fundamentals are modestly attractive (P/E 12.84). No clear policy surprise or decisive technical break, so maintain neutral stance.

**Main reasons it gave:**
- 10-year Treasury yield rose 2 bps this week, indicating higher rates
- Share count rose 9.6% in one week, showing strong inflows
- RSI 41.8 and price below 20‑day SMA, indicating bearish momentum
- Analyst consensus 100% buy with +19.3% price target
- BofA warns gold price could fall below $4,000 in Q4

<details><summary><b>News</b> — score +0.00</summary>

- [Gold ETFs Keep the Bid, but Investors Miss This Key Seasonality Pattern](https://www.benzinga.com/markets/commodities/26/10/62128652/gold-etfs-keep-the-bid-but-investors-miss-this-key-seasonality-pattern)  
  <sub>Benzinga, 4 hours ago</sub>  
  Despite rising yields, gold ETF demand holds firm near multi-year highs. Explore why central bank buying keeps a $4000 price floor.
- [VanEck UCITS ETFs Plc - Net Asset Value(s)](https://uk.finance.yahoo.com/news/vaneck-ucits-etfs-plc-net-060000844.html)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Fund Name. NAV Date. Ticker Symbol. ISIN. Shares in Issue. Net Asset Value. NAV per Share. VanEck Emerging Markets High Yield Bond UCITS ETF. 2026-10-01.
- [Webcast: Navigate the Evolving Landscape of Options-Based Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/04/navigate-the-evolving-landscape-of-options-based-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 24 hours ago</sub>  
  Generating meaningful income for clients while balancing tax efficiency, total return potential, and risk has become increasingly complex.
- [Why I Made Gold A Full Position In My Portfolio (NYSEARCA:GLD)](https://seekingalpha.com/article/4951433-why-i-made-gold-a-full-position-in-my-portfolio)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Buy the dip in SPDR Gold Shares ETF as high yields, U.S. debt, and potential Fed action could spark a gold bull run. Click to review gold risks and upside...
- [Form 4 iShares Semiconductor ETF For: 2 October By Investing.com](https://ca.investing.com/news/stock-market-news/form-4-ishares-semiconductor-etf-for-2-october-93CH-4863904)  
  <sub>Investing.com, 3 hours ago</sub>  
  This pricing supplement, which is not complete and may be changed, relates to an effective Registration Statement under the Securities Act of 1933.
- [Gold prices at risk of sliding below $4,000 in Q4, BofA warns (GLD:NYSEARCA)](https://seekingalpha.com/news/4649576-gold-prices-at-risk-of-sliding-below-4000-in-q4-bofa-warns)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  BofA maintains a bullish 2027 gold price forecast but said their outlook is not without risks, seeing gold prices falling to $3750/oz in Q4 with energy...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 88.12 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 93.67 (-5.9%), 50d 91.45 (-3.6%), 200d 91.09 (-3.3%); 50d above 200d
Momentum: RSI(14) 41.8 | MACD -1.533 vs signal -0.323 (histogram -1.210)
Returns: 1d +1.6% | 5d -5.1% | 1m -9.7% | 3m +11.9%
52-week range: 68.28 - 115.84 (now 41.7% of the way up)
Volatility: ATR(14) 3.04 (3.5% of price) | annualised 20d 37.4%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.3% above the current prices
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
Share count change: 1 week: +9.6% (2.64B) over 7d
Shares outstanding: 343.26M | fund size: 30.25B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, flat fund flows, modest bullish technicals on low volume, strong analyst coverage but limited to <50% of the fund, and high valuation multiples suggest caution.

**Main reasons it gave:**
- Treasury yields unchanged this week (3‑month -0.09, 5‑year -0.02, 10‑year +0.02) and VIX low at 15.5
- Fund flows flat (share count +0.0% week‑over‑week)
- Technicals show price above 20‑day SMA (+3.7%) with low volume (0.23× 20‑day avg)
- Analyst coverage of top holdings (43.2% weight) is 100% buy, mean rating 1.67 (strong buy)
- Fund fundamentals show high valuation (P/E 34.2, P/B 8.09) indicating caution

<details><summary><b>News</b> — score +0.00</summary>

- [Software roared back last quarter. Cramer says these stocks can keep climbing](https://www.cnbc.com/amp/2026/10/01/jim-cramer-software-stocks-q3.html)  
  <sub>CNBC, 16 hours ago</sub>  
  Software stocks bounced back from their AI-driven sell-off, while chip stocks cooled after a massive first-half run.
- [Atlassian Climbs 6% as Beaten-Down Software Names Bounce; HubSpot and Monday.com Gain 4%](https://247wallst.com/investing/2026/10/01/atlassian-climbs-6-as-beaten-down-software-names-bounce-hubspot-and-monday-com-gain-4/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Work management software stocks are bouncing together after a bruising stretch, but a fresh analyst downgrade and a sector-wide rally that could reverse...
- [ServiceNow Rallies as Accenture Earnings Lift Software Stocks](https://www.tradingview.com/news/benzinga:0f7ab542e094b:0-servicenow-rallies-as-accenture-earnings-lift-software-stocks/)  
  <sub>TradingView, 21 hours ago</sub>  
  ServiceNow, Inc. NYSE:NOW shares are trading higher amid sympathy with Accenture plc NYSE:ACN after the company reported better-than-expected fourth-quarter...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 109.37 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 105.45 (+3.7%), 50d 103.00 (+6.2%), 200d 93.61 (+16.8%); 50d above 200d
Momentum: RSI(14) 61.1 | MACD 1.306 vs signal 1.218 (histogram 0.087)
Returns: 1d +1.1% | 5d +3.2% | 1m +5.8% | 3m +15.4%
52-week range: 74.67 - 117.08 (now 81.8% of the way up)
Volatility: ATR(14) 2.42 (2.2% of price) | annualised 20d 26.9%
Volume: 0.23x the 20-day average
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
Three-year record: +16.0% a year | beta to the market 1.21
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

<details><summary><b>What analysts and big funds say</b> — score +0.66</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.66</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.9% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-23 Rosenblatt: main, Buy -> Buy
  - PANW: 2026-10-02 TD Cowen: main, Buy -> Buy
  - MSFT: 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - CRWD: 2026-10-02 TD Cowen: main, Buy -> Buy
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
Shares outstanding: 12.50M | fund size: 1.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: share count up 2.9% in the week, indicating net inflows
- Technical trend: price below 20‑day, 50‑day, and 200‑day SMAs, RSI 34.8, low volume, no decisive break
- Analyst view: 100% buy rating for top holdings (24.7% weight) with +34.8% price target, but coverage is thin
- Macro: no policy or rate surprise; yields stable, VIX low
- News: US‑India trade deal not imminent, a negative but not a macro surprise

<details><summary><b>News</b> — score +0.00</summary>

- [US trade deal with India not ‘imminent’ despite ‘constructive’ Modi-Trump call, says USTR Greer (INDA:BATS)](https://seekingalpha.com/news/4649714-us-trade-deal-with-india-not-imminent-despite-constructive-modi-trump-call-says-ustr-greer)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  U.S.-India trade deal not imminent as sticking points remain, says USTR Jamieson Greer, despite constructive talks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 46.72 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 47.90 (-2.4%), 50d 48.99 (-4.6%), 200d 49.85 (-6.3%); 50d below 200d
Momentum: RSI(14) 34.8 | MACD -0.666 vs signal -0.533 (histogram -0.134)
Returns: 1d +0.8% | 5d -2.4% | 1m -6.5% | 3m -6.3%
52-week range: 45.42 - 55.29 (now 13.2% of the way up)
Volatility: ATR(14) 0.45 (1.0% of price) | annualised 20d 14.1%
Volume: 0.25x the 20-day average
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
Three-year record: +2.1% a year | beta to the market 0.56
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +34.8% above the current prices
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
Share count change: 1 week: +2.9% (187.43M) over 7d
Shares outstanding: 144.02M | fund size: 6.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, technicals lack decisive breakout, high valuations temper upside despite strong analyst consensus and modest inflows.

**Main reasons it gave:**
- US inflation 3.4% and unemployment 4.2% matched expectations, no macro surprise
- ETF price below 20‑day, 50‑day, and 200‑day SMAs with low volume, no decisive technical breakout
- Analyst consensus 100% buy with +29.3% price target, but not enough to offset neutral macro and technicals
- Fund flows show a 2.2% share count increase over the week, indicating modest net inflow
- Fund basics reveal high valuation multiples (P/E 34.66, P/B 6.62) tempering upside potential

<details><summary><b>News</b> — score +0.00</summary>

- [Aerospace ETF Showdown for Defense Investors: iShares ITA vs. Global X SHLD](https://www.fool.com/coverage/etfs/2026/10/01/aerospace-etf-showdown-for-defense-investors-ishares-ita-vs-global-x-shld/)  
  <sub>The Motley Fool, 12 hours ago</sub>  
  The iShares U.S. Aerospace & Defense ETF (ITA -0.22%) provides established exposure to domestic aviation leaders, while the Global X Defense Tech ETF (SHLD...
- [iShares US Aerospace & Defense ETF (ITA) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ITA/)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  iShares US Aerospace &amp; Defense ETF (ITA) · -2.22% · -7.73% · -6.98% · -3.84% · -0.58% · 95.89% · 703.55%. Key...
- [Boeing Lands $20B Navy Deal for Next-Gen Fighter Jet: ETFs to Watch](https://www.theglobeandmail.com/investing/markets/stocks/NOC/pressreleases/4911741/boeing-lands-20b-navy-deal-for-next-gen-fighter-jet-etfs-to-watch/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Detailed price information for Northrop Grumman Corp (NOC-N) from The Globe and Mail including charting and trades.
- [U.S. surges forces in Middle East as Trump weighs renewed Iran strikes - report (ITA:BATS)](https://seekingalpha.com/news/4649399-u-s-surges-forces-in-middle-east-as-trump-weighs-renewed-iran-strikes-report)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The Pentagon is deploying up to 10K additional troops and a third aircraft-carrier strike group to the Middle East, according to a media report published...
- [ETFs Are Selling Woodward (WWD) on Sept. 30](https://www.gurufocus.com/news/9107342/etfs-are-selling-woodward-wwd-on-sept-30)  
  <sub>GuruFocus, 4 hours ago</sub>  
  ETFs sold a net $29.7 million worth of Woodward (WWD) shares on Wednesday, with 16 ETFs selling and 13 buying. The move reversed the prior day's net buying...
- [Which Consumer Staples ETF Offers Better Value: XLP or IYK?](https://www.fool.com/coverage/etfs/2026/10/01/which-consumer-staples-etf-offers-better-value-xlp-or-iyk/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  State Street's XLP charges just 0.08% annually versus iShares' 0.37%, but IYK diversifies into healthcare and materials. Similar returns and low volatility...
- [Which Energy ETF Fits Your Portfolio? State Street Energy Select Sector SPDR ETF (XLE) or the Alerian MLP ETF (AMLP)?](https://www.fool.com/coverage/etfs/2026/10/01/which-energy-etf-fits-your-portfolio-state-street-energy-select-sector-spdr-etf-xle-or-the-alerian-mlp-etf-amlp/)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  One offers broad energy exposure at rock-bottom costs; the other targets infrastructure with a 7.8% yield. Here's how to choose.
- [Better iShares Financial ETF: European-Targeted EUFN vs. IAT's U.S. Regional Banks Focus](https://www.fool.com/coverage/etfs/2026/10/01/better-ishares-financial-etf-european-targeted-eufn-vs-iat-s-u-s-regional-banks-focus/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  EUFN's 4.1% dividend and lower volatility appeal to income investors, though IAT's cheaper expense ratio suits cost-conscious traders.
- [How Do the Invesco KBW Bank ETF (KBWB) and the State Street Regional Banking Fund ETF (KRE) Compare With Each Other?](https://www.fool.com/coverage/etfs/2026/10/01/how-do-the-invesco-kbw-bank-etf-kbwb-and-the-state-street-regional-banking-fund-etf-kre-compare-with-each-other/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  KBWB's concentrated portfolio of 26 major banks delivered 14.7% returns over one year, while KRE's broader 167-holding approach yielded 12.5%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 208.71 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 214.64 (-2.8%), 50d 230.84 (-9.6%), 200d 230.47 (-9.4%); 50d above 200d
Momentum: RSI(14) 28.7 | MACD -6.130 vs signal -6.260 (histogram 0.130)
Returns: 1d +0.3% | 5d -2.4% | 1m -6.6% | 3m -16.8%
52-week range: 198.23 - 253.22 (now 19.1% of the way up)
Volatility: ATR(14) 3.75 (1.8% of price) | annualised 20d 13.4%
Volume: 0.23x the 20-day average
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
Three-year record: +25.9% a year | beta to the market 0.99
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.74 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.3% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-09-21 Jefferies: main, Buy -> Buy
  - GD: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - LMT: 2026-09-08 UBS: up, Neutral -> Buy
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
Share count change: 1 week: +2.2% (298.97M) over 7d
Shares outstanding: 65.11M | fund size: 13.59B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro or policy surprise, technicals lack decisive break, but analyst view and flows are modestly positive.

**Main reasons it gave:**
- Analyst coverage of top holdings (53.1% weight) shows 90.8% buy rating and +26.4% price target
- Fund flows show 0.9% share count increase over the week, indicating net inflows
- Fund basics show 3-year annualized return of +11.5% and moderate valuation (P/E 20.28)
- Technical indicators show price below 20‑day SMA and low volume, limiting bullish momentum
- Macro data shows stable yields and low VIX, no surprise catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 80.10 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 80.65 (-0.7%), 50d 84.07 (-4.7%), 200d 81.27 (-1.4%); 50d above 200d
Momentum: RSI(14) 41.9 | MACD -1.482 vs signal -1.575 (histogram 0.094)
Returns: 1d +1.3% | 5d +0.9% | 1m -3.9% | 3m -8.4%
52-week range: 68.14 - 90.01 (now 54.7% of the way up)
Volatility: ATR(14) 1.17 (1.5% of price) | annualised 20d 14.9%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Industrials
What it holds: P/E 20.28 | P/B 4.25 | P/S 1.45 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +11.5% a year | beta to the market 1.28
Cost and size: expense ratio 0.37% | net assets 2.20B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Union Pacific Corp 17.8%, Uber Technologies Inc 15.4%, CSX Corp 9.4%, United Parcel Service Inc Class B 5.6%, Norfolk Southern Corp 4.9%
Sector mix: Industrials 83.8%, Technology 16.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.4% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-10-02 Susquehanna: main, Positive -> Positive
  - UBER: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
  - CSX: 2026-10-02 Susquehanna: main, Positive -> Positive
  - UPS: 2026-07-29 Stifel: main, Buy -> Buy
  - NSC: 2026-10-02 Susquehanna: main, Neutral -> Neutral
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
Share count change: 1 week: +0.9% (19.14M) over 7d
Shares outstanding: 27.74M | fund size: 2.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals lack a decisive break, modest positive flows and analyst sentiment, fundamentals are solid but not compelling.

**Main reasons it gave:**
- Fund flows: +2.0% share count increase over the past week
- Analyst coverage: 7.1% of fund weight, 79.5% buy, +20.5% price target
- Technical: price above 200‑day SMA (+0.6%) but below 20‑day SMA (-1.7%), RSI 41.5, no decisive break
- Macro: Treasury yields stable, yield curve normal (+1.22), no rate surprise
- Fundamentals: low P/E 12.6, low P/B 1.27, dividend yield 2.2%

<details><summary><b>News</b> — score +0.00</summary>

- [How Do the Invesco KBW Bank ETF (KBWB) and the State Street Regional Banking Fund ETF (KRE) Compare With Each Other?](https://www.fool.com/coverage/etfs/2026/10/01/how-do-the-invesco-kbw-bank-etf-kbwb-and-the-state-street-regional-banking-fund-etf-kre-compare-with-each-other/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  KBWB's concentrated portfolio of 26 major banks delivered 14.7% returns over one year, while KRE's broader 167-holding approach yielded 12.5%.
- [KBWB hits most oversold RSI since the 2023 regional-banking crisis](https://seekingalpha.com/news/4649190-kbwb-hits-most-oversold-rsi-since-the-2023-regional-banking-crisis)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  Shares of the Invesco KBW Bank ETF (KBWB) have slipped to their most oversold reading on the 14-day relative strength index since the first quarter of 2023,...
- [Citigroup Q3 Preview: Earnings Should Be Alright Despite Macro Risks (Upgrade) (NYSE:C)](https://seekingalpha.com/article/4951454-citigroup-q3-preview-earnings-should-be-alright-despite-macro-risks-upgrade?source=generic_rss)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  Citigroup is upgraded based on strong operating results and a somewhat improved starting valuation. Click to read more on the C stock.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 71.00 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 72.20 (-1.7%), 50d 74.35 (-4.5%), 200d 70.59 (+0.6%); 50d above 200d
Momentum: RSI(14) 41.5 | MACD -1.206 vs signal -1.091 (histogram -0.114)
Returns: 1d +1.5% | 5d -0.8% | 1m -4.4% | 3m -6.0%
52-week range: 58.14 - 77.93 (now 65.0% of the way up)
Volatility: ATR(14) 1.27 (1.8% of price) | annualised 20d 14.8%
Volume: 0.49x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Financial
What it holds: P/E 12.60 | P/B 1.27 | P/S 3.77 | 3y earnings growth n/a
Yield: 2.2%
Three-year record: +21.7% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 4.01B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Cullen/Frost Bankers Inc 1.5%, SouthState Bank Corp 1.4%, Popular Inc 1.4%, Pinnacle Financial Partners Inc 1.4%, UMB Financial Corp 1.4%
Sector mix: Financial services 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 7.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 79.5% | hold 20.5% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.5% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-10-01 Evercore ISI Group: main, In-Line -> In-Line
  - SSB: 2026-10-01 JP Morgan: main, Overweight -> Overweight
  - BPOP: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - PNFP: 2026-10-02 Piper Sandler: main, Overweight -> Overweight
  - UMBF: 2026-10-01 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: +2.0% (79.06M) over 7d
Shares outstanding: 57.45M | fund size: 4.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst buy coverage and recent inflows suggest modest bullishness, but technicals are bearish and fundamentals are neutral.

**Main reasons it gave:**
- Analyst coverage: 90% buy, price target +18.5% above current price
- Fund flows: share count up 2.3% in the past week
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 28.6 (oversold); volume 0.51× 20‑day average
- Fundamentals: P/E 15, expense ratio 0.75%, three‑year return +0.9% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.24 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 37.34 (-2.9%), 50d 37.75 (-4.0%), 200d 38.12 (-4.9%); 50d below 200d
Momentum: RSI(14) 28.6 | MACD -0.486 vs signal -0.347 (histogram -0.139)
Returns: 1d +0.4% | 5d -2.2% | 1m -5.7% | 3m -2.8%
52-week range: 35.83 - 41.03 (now 8.0% of the way up)
Volatility: ATR(14) 0.29 (0.8% of price) | annualised 20d 8.7%
Volume: 0.51x the 20-day average
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
Three-year record: +0.9% a year | beta to the market 0.18
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
Weighted price target: +18.5% above the current prices
Holdings read: 1120.SR, 2222.SR, 1180.SR, 7010.SR, 1211.SR
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
Share count change: 1 week: +2.3% (14.08M) over 7d
Shares outstanding: 17.50M | fund size: 634.23M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, flat flows, high valuation.

**Main reasons it gave:**
- Flat fund flows: share count +0.1% week
- Technical momentum bullish (RSI 69.4, price above SMAs) but volume low (0.44x avg)
- Macro: yields up slightly (10‑yr +0.02% week) with no surprise data
- Fund fundamentals: high P/E 37.8 and beta 2.06 indicate valuation risk

<details><summary><b>News</b> — score +0.00</summary>

- [The Semiconductor ETF's 2026 Return Is About 3 Times Nvidia's](https://www.theglobeandmail.com/investing/markets/markets-news/Motley%20Fool/4919513/the-semiconductor-etf-s-2026-return-is-about-3-times-nvidia-s/)  
  <sub>The Globe and Mail, 14 hours ago</sub>  
  The VanEck Semiconductor ETF was up around 69% in 2026 as of midday Sept. 30, but Nvidia shares were up about 23%. Micron, AMD, and Intel were about 14% of...
- [S&P 500, Nasdaq, Dow Futures Inch Higher As Investors Cheer Cooling Yields — GOOGL, MU, MAT, NVDA In Focus](https://www.tradingview.com/news/stocktwits:a853af257094b:0-s-p-500-nasdaq-dow-futures-inch-higher-as-investors-cheer-cooling-yields-googl-mu-mat-nvda-in-focus/)  
  <sub>TradingView, 15 hours ago</sub>  
  S&P 500, Dow and Nasdaq futures rose after the market closed higher on Thursday, mainly on easing Treasury yields.The S&P 500 ended Thursday 0.2% higher,...
- [US Stocks End Third Session Lower As Higher Treasury Yields, Oil Prices Weigh— TSLA, PSKY, MSTR, BABA, NVDA In Focus](https://stocktwits.com/news-articles/markets/equity/us-stocks-end-third-session-lower-as-higher-treasury-yields-oil-prices-weigh/cZYcnUERJjD)  
  <sub>Stocktwits, 6 hours ago</sub>  
  The S&P 500 ended 0.7% lower, while the Nasdaq 100 lost 1.7% and the Dow Jones Industrial Average marginally eased 0.2%. 10-year Treasury yields hovered...
- [S&P 500, Dow, Nasdaq End Week Higher On Chipmaker Strength, Easing Oil Amid Signs Of Easing US-Iran Conflict — META, COST, MSFT, CRWD, SKHY In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-end-week-higher-on-chipmaker-strength-easing-oil-amid-signs-of-easing-us-iran-conflict-meta-cost-msft-crwd-skhy-in-focus/cZMOFkXRBOV)  
  <sub>Stocktwits, 12 hours ago</sub>  
  U.S. stock indices ended Friday higher as oil prices cooled after a media report suggested signs of diplomatic talks between the U.S. and Iran,...
- [S&P 500, Dow, Nasdaq Drop As Yields Spike Amid Calls For More Rate Hikes — AMZN, GOOGL, NFLX, SPCX, RKLB In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-drop-as-yields-spike-amid-calls-for-more-rate-hikes-amzn-googl-nflx-spcx-rklb-in-focus/cZM4IxjRBB9)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Treasury yields jumped across the curve on Wednesday.
- [S&P 500, Nasdaq, Dow Drop As US-Iran War Jitters, Inflation Risk Spur Tech Selloffs — SMCI, AMZN, OPEN, SEGG, TSLA In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-drop-as-us-iran-war-jitters-inflation-risk-spur-tech-selloffs-smci-amzn-open-segg-tsla-in-focus/cZ06yd5R7cQ)  
  <sub>Stocktwits, 15 hours ago</sub>  
  U.S. stock indices dropped on Wednesday as renewed energy cost concerns tied to rising US-Iran war signals, along with signs of persistent inflation...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 634.04 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 584.32 (+8.5%), 50d 569.92 (+11.3%), 200d 499.52 (+26.9%); 50d above 200d
Momentum: RSI(14) 69.4 | MACD 14.730 vs signal 9.373 (histogram 5.357)
Returns: 1d +2.6% | 5d +4.5% | 1m +15.2% | 3m +4.9%
52-week range: 325.10 - 668.91 (now 89.9% of the way up)
Volatility: ATR(14) 15.30 (2.4% of price) | annualised 20d 31.6%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Technology
What it holds: P/E 37.78 | P/B 11.07 | P/S 13.20 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +62.1% a year | beta to the market 2.06
Cost and size: expense ratio 0.35% | net assets 67.79B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 22.6%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.7%, Broadcom Inc 6.1%, Micron Technology Inc 5.5%, Advanced Micro Devices Inc 5.4%
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
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +31.3% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-01 Mizuho: main, Outperform -> Outperform
  - AMD: 2026-09-29 StoneX: reit, Buy -> Buy
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
Share count change: 1 week: +0.1% (57.09M) over 7d
Shares outstanding: 111.65M | fund size: 70.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise or policy shift this week
- Technical downtrend with price below 20‑day, 50‑day, and 200‑day SMAs and low volume, no decisive break
- Analyst view bullish on top holdings (100% buy, +23.8% price target) covering only 39.5% of fund
- Fundamentals mixed: moderate valuation, negative 3‑year performance, low earnings growth
- Fund flows flat over past week

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Bitcoin Trust ETF (IBIT) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/IBIT/)  
  <sub>Yahoo Finance UK, 23 hours ago</sub>  
  Find the latest iShares Bitcoin Trust ETF (IBIT) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 34.48 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 37.46 (-8.0%), 50d 38.61 (-10.7%), 200d 39.32 (-12.3%); 50d below 200d
Momentum: RSI(14) 31.5 | MACD -1.339 vs signal -0.966 (histogram -0.374)
Returns: 1d +0.2% | 5d -5.2% | 1m -12.8% | 3m -12.6%
52-week range: 31.90 - 43.74 (now 21.8% of the way up)
Volatility: ATR(14) 0.75 (2.2% of price) | annualised 20d 37.6%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: -2.2% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.8% above the current prices
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
Shares outstanding: 15.65M | fund size: 539.61M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as there is no macro surprise, technicals show a downtrend without a decisive break, modest inflows, bullish analyst view limited to ~40% of the fund, and slightly overvalued fundamentals.

**Main reasons it gave:**
- No macro surprise: yields stable, Fed target unchanged
- Technicals: price below 20‑, 50‑, 200‑day SMAs and RSI 30.5 (near oversold) but no decisive break on volume
- Fund flows: share count up 3.4% in the past week, indicating modest inflows
- Analyst coverage: 100% buy rating with +20.7% price target, but only covers 39.9% of the fund
- Fundamentals: high P/E (30.2) and yield (3.6%) lower than 10‑year Treasury yield (5.2%), suggesting slight overvaluation

<details><summary><b>News</b> — score +0.00</summary>

- [Moving Averages Of The Ivy Portfolio And S&P 500: September 2026](https://seekingalpha.com/article/4951497-moving-averages-of-ivy-portfolio-s-p-500-september-2026?source=generic_rss)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  The Ivy Portfolio 10- and 12-month simple moving average had two cash positions: the IEF and VNQ ETFs.
- [Telecom and real estate sectors lead dividend g...](https://pluang.com/en/news-feed/dividen-sektor-sp-500-2026-september-terbaik-bukan-teknologi)  
  <sub>Pluang, 20 hours ago</sub>  
  In September, telecom and real estate sectors stood out for their dividend growth and relative value amid an otherwise expensive market.
- [Medical Properties tops most-shorted REITs; American Tower records the lowest](https://seekingalpha.com/news/4649277-medical-properties-tops-most-shorted-reits-american-tower-records-the-lowest)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Within the real estate sector, represented by the Real Estate Select Sector SPDR ETF (XLRE), healthcare, hotel, and office REITs were among the most shorted...
- [Most vs. least shorted REITs with up to $2B market cap by September end](https://seekingalpha.com/news/4649276-most-vs-least-shorted-reits-with-up-to-2b-market-cap-by-september-end)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Within the real estate sector, represented by the Real Estate Select Sector SPDR ETF (XLRE), mortgage and office REITs were among the most shorted stocks at...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 90.17 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 92.78 (-2.8%), 50d 96.14 (-6.2%), 200d 94.37 (-4.5%); 50d above 200d
Momentum: RSI(14) 30.5 | MACD -1.853 vs signal -1.622 (histogram -0.231)
Returns: 1d +1.1% | 5d -0.9% | 1m -5.9% | 3m -7.3%
52-week range: 87.00 - 100.95 (now 22.7% of the way up)
Volatility: ATR(14) 1.16 (1.3% of price) | annualised 20d 12.3%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.7% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-09-30 Barclays: main, Overweight -> Overweight
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
Share count change: 1 week: +3.4% (2.33B) over 7d
Shares outstanding: 782.23M | fund size: 70.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and only moderate positive flow and fundamentals. The fund’s fundamentals are attractive (low P/B and P/S, strong 3‑year record) and analyst coverage is slightly bullish, but recent price action is weak and there is no material macro catalyst, so the overall view remains neutral.

**Main reasons it gave:**
- Fund flows: share count up 3.2% over the week indicating net inflows
- Analyst ratings: 43.2% buy, 56.8% hold, mean rating 2.31 (slightly bullish)
- Fundamentals: low P/B (0.20) and P/S (0.12) with strong 3‑year record (+29.5% per year)
- Technicals: price below 20‑day and 50‑day SMA, RSI 44.8, MACD negative, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [SLS, IBRX Eye Green Month As Biotech ETF Gains Steam: Analyst Sees ‘Continued Opportunities’ In Immuno-Oncology](https://stocktwits.com/news-articles/markets/equity/sls-ibrx-xbi-analyst-continued-opportunities-immuno-oncology/cZ1BDwKR7hT)  
  <sub>Stocktwits, 9 hours ago</sub>  
  XBI, which includes both SLS and IBRX, is on track for its strongest monthly performance since December 2023.
- [More Upside Awaits for Gilead Sciences Stock. Stay Invested.](https://www.barrons.com/articles/gilead-sciences-stock-stay-invested-more-upside-awaits-e1c38c22)  
  <sub>Barron's, 12 hours ago</sub>  
  Gilead shares are up 35% since Barron's highlighted them, but our catalysts have yet to fully play out.
- [Xenon’s Insider Buying Tops $1.6M – XENE Stock Heads For Best Day In Over Month](https://www.tradingview.com/news/stocktwits:5f40a1916094b:0-xenon-s-insider-buying-tops-1-6m-xene-stock-heads-for-best-day-in-over-month/)  
  <sub>TradingView, 23 hours ago</sub>  
  Xenon Pharmaceuticals (XENE) was on investors' radar on Thursday after the biotech company's top executives bought a combined $1.68 million in shares,...
- [Why Did OPEN, NKE, CCL Stocks Crash To 52-Week Lows Today?](https://stocktwits.com/news-articles/markets/equity/why-did-open-nke-ccl-stocks-crash-to-52-week-lows-today/cZtY2PcRB2d)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Housing weakness, a prolonged athleticwear turnaround, and rising cruise fuel costs weighed on investor sentiment.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 155.07 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 157.30 (-1.4%), 50d 158.07 (-1.9%), 200d 138.83 (+11.7%); 50d above 200d
Momentum: RSI(14) 44.8 | MACD -1.059 vs signal -0.767 (histogram -0.292)
Returns: 1d +0.4% | 5d +0.0% | 1m -6.2% | 3m -3.6%
52-week range: 102.59 - 169.55 (now 78.4% of the way up)
Volatility: ATR(14) 4.00 (2.6% of price) | annualised 20d 25.3%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 43.2% | hold 56.8% | sell 0.0% (mean 2.31 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -16.9% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-30 Citigroup: down, Neutral -> Sell
  - TWST: 2026-10-01 Guggenheim: main, Buy -> Buy
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-22 Stifel: main, Buy -> Buy
  - HALO: 2026-09-02 HC Wainwright & Co.: reit, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.32</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.32</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.32</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +3.2% (350.36M) over 7d
Shares outstanding: 72.73M | fund size: 11.28B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Fund flows: share count +2.5% over 7 days indicating net inflows
- Analyst view: 74% buy rating and +21.4% price target for top holdings (20.9% weight)
- Technicals: price below 50‑day and 200‑day SMAs, downtrend, RSI 44.1, low volume
- Macro: yields high but stable, mortgage rates rising modestly, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [(XHB) Technical Pivots with Risk Controls (XHB:CA)](https://news.stocktradersdaily.com/canada/xhb-technical-pivots-with-risk-controls_20261001_948bff)  
  <sub>Stock Traders Daily, 16 hours ago</sub>  
  Technical analysis for iShares Canadian HYBrid Corporate Bond Index ETF XHB including support levels resistance levels and stop losses for XHB.
- [Mortgage rates hit three-year high as bond yields surge (XLRE:NYSEARCA)](https://seekingalpha.com/news/4649208-mortgage-rates-hit-three-year-high-as-bond-yields-surge)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  30-year fixed-rate mortgages averaged 7.28% as of October 1, up from 7.03% last week and 6.34% in the same period a year ago, according to the Freddie Mac...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 97.70 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 97.91 (-0.2%), 50d 103.19 (-5.3%), 200d 106.16 (-8.0%); 50d below 200d
Momentum: RSI(14) 44.1 | MACD -1.757 vs signal -2.042 (histogram 0.285)
Returns: 1d +1.0% | 5d -0.6% | 1m -3.4% | 3m -12.2%
52-week range: 94.86 - 121.36 (now 10.7% of the way up)
Volatility: ATR(14) 2.18 (2.2% of price) | annualised 20d 22.0%
Volume: 0.54x the 20-day average
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
Three-year record: +8.8% a year | beta to the market 1.46
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 74.0% | hold 26.0% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.4% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-25 Evercore ISI Group: main, In-Line -> In-Line
  - OC: 2026-10-01 Evercore ISI Group: main, Outperform -> Outperform
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-09-30 Oppenheimer: init, ? -> Perform
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
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
Share count change: 1 week: +2.5% (32.61M) over 7d
Shares outstanding: 13.73M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show no decisive break, fund flows are flat, and analyst coverage is limited to 37% of the fund despite bullish ratings. Overall view remains neutral.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicating no net demand
- Technical momentum weak (RSI 39.4, MACD negative) with no decisive break
- No macro surprise (yields stable, inflation 3.4% near target, Fed unchanged)
- Analyst coverage limited to 37% of fund despite 100% buy rating and +92.9% price target

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  State Street Materials Select Sector SPDR ETF (XLB) · -2.29% · -6.78% · -3.80% · 7.03% · 9.47% · 20.79% · 367.15%. Key Events. Baseline.
- [Ignoring the Noise: The Long-Term Case for Materials](https://www.etftrends.com/sector-investing-content-hub/ignoring-noise-long-term-case-materials/)  
  <sub>ETF Trends, 18 hours ago</sub>  
  September may have been a troubling month for the materials sector, but the long-term thesis for materials remains sound.
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [8 Of 11 Sectors Fall In Thursday Trading As Cyclicals Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62111517/8-of-11-sectors-fall-in-thursday-trading-as-cyclicals-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with cyclical sectors holding two of the top three positions.
- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest State Street Communication Services Select Sector SPDR ETF (XLC) stock quote, history, news and other vital information to help you with...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 49.31 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 50.24 (-1.9%), 50d 51.57 (-4.4%), 200d 50.66 (-2.7%); 50d above 200d
Momentum: RSI(14) 39.4 | MACD -0.798 vs signal -0.681 (histogram -0.117)
Returns: 1d +1.6% | 5d -1.0% | 1m -6.9% | 3m -5.1%
52-week range: 42.23 - 53.67 (now 61.9% of the way up)
Volatility: ATR(14) 0.75 (1.5% of price) | annualised 20d 14.0%
Volume: 0.39x the 20-day average
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
Three-year record: +9.5% a year | beta to the market 0.82
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +92.9% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break occurred; positive analyst coverage and modest inflows are offset by slight bearish technical bias and unchanged macro backdrop.

**Main reasons it gave:**
- Analyst ratings 100% buy covering 45.5% of fund weight with +16.1% price target
- Fund flows show +1.9% share count increase over 7 days indicating net inflows
- Technical indicators show slight bearish bias (price below SMAs, negative MACD, RSI 47) but no decisive break
- Macro data unchanged; no surprise in inflation, unemployment, or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  State Street Communication Services Select Sector SPDR ETF (XLC) · -3.55% · -0.85% · -1.17% · -7.06% · -5.80% · 34.96% · 121.21%.
- [Bet on These ETFs to Ride on META's 27% September Jump](https://www.tradingview.com/news/zacks:ca7192fe0094b:0-bet-on-these-etfs-to-ride-on-meta-s-27-september-jump/)  
  <sub>TradingView, 3 hours ago</sub>  
  Meta Platforms META delivered a stunning performance in September, with shares surging approximately 27% during the month. The social media giant started...
- [S&P 500 2026 September Dividends Reveal Most Promising Sectors (And It’s Not Tech) (SPY)](https://seekingalpha.com/article/4951432-sp500-2026-september-dividends-reveal-most-promising-sectors-and-its-not-tech)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Communication Services (XLC) and real estate (VNQ) offer dividend growth and value amid an expensive market. Here's what investors need to consider.
- [Paramount Skydance Falls 5% Despite Antitrust Clearance and $41.4B Debt Pricing, Warner Bros. Discovery Holds Flat; Netflix Eases](https://247wallst.com/investing/2026/10/01/paramount-skydance-falls-5-despite-antitrust-clearance-and-41-4b-debt-pricing-warner-bros-discovery-holds-flat-netflix-eases/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  A federal judge just cleared the final legal hurdle for one of Hollywood's biggest mergers, yet the buyer's stock is sinking fast. The reason comes down to...
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 111.10 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 112.31 (-1.1%), 50d 111.50 (-0.4%), 200d 113.79 (-2.4%); 50d below 200d
Momentum: RSI(14) 47.1 | MACD -0.188 vs signal 0.156 (histogram -0.344)
Returns: 1d +1.1% | 5d -1.6% | 1m -1.2% | 3m +0.8%
52-week range: 105.38 - 120.08 (now 38.9% of the way up)
Volatility: ATR(14) 1.75 (1.6% of price) | annualised 20d 21.1%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Communications
What it holds: P/E 15.38 | P/B 2.92 | P/S 2.06 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +20.5% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.43B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 16.8%, Alphabet Inc Class A 10.3%, Alphabet Inc Class C 8.2%, AT&T Inc 5.3%, Verizon Communications Inc 5.0%
Sector mix: Communication services 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.90</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.90</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.1% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-28 Piper Sandler: reit, Overweight -> Overweight
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-28 Morgan Stanley: main, Overweight -> Overweight
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
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
Share count change: 1 week: +1.9% (411.76M) over 7d
Shares outstanding: 201.30M | fund size: 22.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals show no decisive break, fund flows are flat, and inventory data are mixed, leading to a neutral stance.

**Main reasons it gave:**
- Macro: yields stable, no policy surprise
- Technical: price above 50‑day and 200‑day SMA but below 20‑day SMA, MACD negative, low volume
- Fund flows: flat share count, no net inflow/outflow
- Energy inventories: crude and gas builds (bearish) offset by petrol and diesel draws (bullish)

<details><summary><b>News</b> — score +0.00</summary>

- [Which Energy ETF Fits Your Portfolio? State Street Energy Select Sector SPDR ETF (XLE) or the Alerian MLP ETF (AMLP)?](https://www.fool.com/coverage/etfs/2026/10/01/which-energy-etf-fits-your-portfolio-state-street-energy-select-sector-spdr-etf-xle-or-the-alerian-mlp-etf-amlp/)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  While the State Street Energy Select Sector SPDR ETF (XLE +1.95%) offers broad energy exposure with a significantly lower expense ratio, the Alerian MLP ETF...
- [Westwood Salient Enhanced Energy Income ETF yie...](https://pluang.com/en/news-feed/wee-high-yield-tapi-bisa-kalah-dari-pure-equity-funds)  
  <sub>Pluang, 7 hours ago</sub>  
  The Westwood Salient Enhanced Energy Income ETF (WEEI) offers an 11.16% yield by employing a covered call-writing strategy on North American energy equities...
- [WEEI: High Yield But Could Underperform Pure Equity Funds](https://seekingalpha.com/article/4951524-weei-high-yield-but-could-underperform-pure-equity-funds)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  WEEI sacrifices capital gains in strong bull markets, underperforming pure equity energy ETFs like XLE during periods of sector strength.
- [Marathon Petroleum Climbs 5%, Valero Energy Gains 4% as Refiners Outrun Integrated Majors; Exxon Mobil Stays Flat](https://247wallst.com/investing/2026/10/01/marathon-petroleum-climbs-5-valero-energy-gains-4-as-refiners-outrun-integrated-majors-exxon-mobil-stays-flat/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Pure refiners and integrated oil majors are trading as if they belong to entirely different industries today, and the reason comes down to one economic...
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [8 Of 11 Sectors Fall In Thursday Trading As Cyclicals Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62111517/8-of-11-sectors-fall-in-thursday-trading-as-cyclicals-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with cyclical sectors holding two of the top three positions.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday Amid Jobs Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-133147980.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.9% and the actively trad.
- [Sector Update: Energy Stocks Fall in Early Trading Friday](https://finance.yahoo.com/energy/articles/sector-energy-stocks-fall-early-133240376.html?.tsrc=rss)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Energy stocks were falling in early trading Friday, with the State Street Energy Select Sector SPDR ETF (XLE) declining by 1%.
- [Sector Update: Energy Stocks Rise Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-rise-afternoon-195951658.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks rose late Thursday afternoon with the NYSE Energy Sector Index gaining 1.3% and the State Street Energy Select Sector SPDR ETF (XLE) adding...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 62.36 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 63.45 (-1.7%), 50d 62.11 (+0.4%), 200d 56.55 (+10.3%); 50d above 200d
Momentum: RSI(14) 47.8 | MACD -0.160 vs signal 0.132 (histogram -0.293)
Returns: 1d -0.5% | 5d +0.5% | 1m -4.2% | 3m +17.4%
52-week range: 42.61 - 65.93 (now 84.7% of the way up)
Volatility: ATR(14) 1.21 (1.9% of price) | annualised 20d 21.0%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

```text
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Crude oil: 427.3 million barrels, +0.9 on the week (a build), 62% percentile over 52 weeks
  Petrol: 204.4 million barrels, -1.7 on the week (a draw), 2% percentile over 52 weeks -- low for the time of year
  Diesel: 105.2 million barrels, -2.3 on the week (a draw), 23% percentile over 52 weeks
  Natural gas: 3,415.0 billion cubic feet, +64.0 on the week (a build), 79% percentile over 52 weeks
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
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.9% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - CVX: 2026-09-28 TD Cowen: main, Hold -> Hold
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-10-02 B of A Securities: main, Neutral -> Neutral
  - PSX: 2026-10-01 Goldman Sachs: main, Neutral -> Neutral
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

> Neutral overall as there is no material macro catalyst, technical break, or flow imbalance. Analyst view is bullish but only covers 41.5% of the fund, and technicals show oversold conditions without decisive momentum. Fund flows are flat, and macro data are stable.

**Main reasons it gave:**
- Fund flows flat: 0% share count change over 1 week
- Technical RSI low (27.9) but price below 20d/50d SMAs, no decisive break
- Macro data stable: inflation 3.4%, Fed target 4.0%, no surprise
- Analyst coverage 41.5% of fund, all buy with +15.4% price target but limited coverage

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Are Net Sellers of Goldman Sachs (GS) on Sept. 30](https://www.gurufocus.com/news/9107338/etfs-are-net-sellers-of-goldman-sachs-gs-on-sept-30)  
  <sub>GuruFocus, 4 hours ago</sub>  
  In Wednesday's session, XLF led ETF activity by selling $36.0 million worth of Goldman Sachs (GS), as ETFs were net sellers of $33.4 million.
- [Bank Stocks Slide as Money-Center Names Lead Financials Lower: Citigroup Falls 4%, Bank of America Drops 3%, JPMorgan Chase Slips](https://247wallst.com/investing/2026/10/01/bank-stocks-slide-as-money-center-names-lead-financials-lower-citigroup-falls-4-bank-of-america-drops-3-jpmorgan-chase-slips/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Citigroup is getting hit harder than Bank of America despite the legal headline landing at Merrill Lynch, and the gap between the two lenders points to...
- [ETFs Are Net Sellers of Visa (V) on Wednesday](https://www.gurufocus.com/news/9107331/etfs-are-net-sellers-of-visa-v-on-wednesday)  
  <sub>GuruFocus, 4 hours ago</sub>  
  The largest mover was XLF, which sold $84.3 million in Visa (V) shares on Wednesday. Overall, ETF activity resulted in $43.7 million in net selling,...
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday Amid Jobs Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-133147980.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.9% and the actively trad.
- [Webcast: Navigate the Evolving Landscape of Options-Based Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/04/navigate-the-evolving-landscape-of-options-based-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 24 hours ago</sub>  
  Generating meaningful income for clients while balancing tax efficiency, total return potential, and risk has become increasingly complex.
- [Opinion: Financial stocks are falling below a key chart level to warn the worst is yet to come](https://www.marketwatch.com/story/financial-stocks-are-falling-below-a-key-chart-level-to-warn-the-worst-is-yet-to-come-86e43092)  
  <sub>MarketWatch, 20 hours ago</sub>  
  Financial stocks have struggled over the past several weeks, and it's becoming clear the decline may not be over.
- [Sector Update: Financial Stocks Rise Premarket Friday](https://ca.finance.yahoo.com/news/sector-financial-stocks-rise-premarket-132454126.html)  
  <sub>Yahoo! Finance Canada, 1 hour ago</sub>  
  Financial stocks were rising premarket Friday, with the State Street Financial Select Sector SPDR ETF (XLF) advancing by 0.5%. The Direxion Daily Financial...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 53.62 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 55.57 (-3.5%), 50d 56.81 (-5.6%), 200d 53.71 (-0.2%); 50d above 200d
Momentum: RSI(14) 27.9 | MACD -0.971 vs signal -0.739 (histogram -0.231)
Returns: 1d +0.3% | 5d -2.2% | 1m -7.0% | 3m -4.5%
52-week range: 47.81 - 58.56 (now 54.0% of the way up)
Volatility: ATR(14) 0.69 (1.3% of price) | annualised 20d 11.3%
Volume: 0.34x the 20-day average
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
Three-year record: +19.0% a year | beta to the market 0.71
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.4% above the current prices
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
Shares outstanding: 883.44M | fund size: 47.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, policy shift, or decisive technical break; fund flows flat, technicals mixed, and analyst coverage, while bullish, only spans ~26% of weight. Overall stance remains neutral.

**Main reasons it gave:**
- Analyst coverage of top holdings (25.8% weight) is 100% buy with a +22.5% price target
- Fund flows flat over the past week, indicating neutral demand
- Fundamentals: 3‑year annual return +19.7% per year, P/E 28.43, yield 1.2%, beta 1.02
- Macro: yields stable, VIX low, no surprise data; technicals show slight positive momentum but overall downtrend

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday Amid Jobs Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-133147980.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.9% and the actively trad.
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [Invesco S&P 500 Equal Weight ETF (RSP) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo Finance Singapore, 7 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [8 Of 11 Sectors Fall In Thursday Trading As Cyclicals Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62111517/8-of-11-sectors-fall-in-thursday-trading-as-cyclicals-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with cyclical sectors holding two of the top three positions.
- [iShares US Aerospace & Defense ETF (ITA) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/ITA/)  
  <sub>Yahoo Finance UK, 24 hours ago</sub>  
  Find the latest iShares US Aerospace & Defense ETF (ITA) stock quote, history, news and other vital information to help you with your stock trading and...
- [Webcast: Navigate the Evolving Landscape of Options-Based Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/04/navigate-the-evolving-landscape-of-options-based-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 24 hours ago</sub>  
  Generating meaningful income for clients while balancing tax efficiency, total return potential, and risk has become increasingly complex.
- [Exchange-Traded Funds Mixed, US Equities Fall After Midday](https://www.moomoo.com/news/post/1000521505/exchange-traded-funds-mixed-us-equities-fall-after-midday)  
  <sub>Moomoo, 21 hours ago</sub>  
  BroadMarket IndicatorsBroad-market exchange-traded fund IWM rose and IVV edged lower. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [State Street Communication Services Select Sector SPDR ETF (XLC) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLC/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest State Street Communication Services Select Sector SPDR ETF (XLC) stock quote, history, news and other vital information to help you with...
- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest State Street Materials Select Sector SPDR ETF (XLB) stock quote, history, news and other vital information to help you with your stock...
- [Trump’s Boeing Praise: Potential Short-Term Lift for BA and Industrial ETFs](https://www.tipranks.com/news/catalyst/trumps-boeing-praise-potential-short-term-lift-for-ba-and-industrial-etfs)  
  <sub>TipRanks, 23 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “RT @realDonaldTrump Congratulations to the GREAT Boeing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 170.03 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 170.19 (-0.1%), 50d 176.84 (-3.9%), 200d 172.34 (-1.3%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -2.170 vs signal -2.487 (histogram 0.317)
Returns: 1d +0.8% | 5d -0.2% | 1m -1.6% | 3m -8.4%
52-week range: 147.83 - 186.51 (now 57.4% of the way up)
Volatility: ATR(14) 2.37 (1.4% of price) | annualised 20d 12.8%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Industrials
What it holds: P/E 28.43 | P/B 6.75 | P/S 3.00 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +19.7% a year | beta to the market 1.02
Cost and size: expense ratio 0.08% | net assets 31.95B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Caterpillar Inc 6.7%, GE Aerospace 6.4%, RTX Corp 5.1%, GE Vernova Inc 4.4%, Union Pacific Corp 3.2%
Sector mix: Industrials 92.8%, Technology 6.7%, Basic materials 0.3%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.5% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-09-23 Bernstein: main, Market Perform -> Market Perform
  - GEV: 2026-09-15 Bernstein: reit, Outperform -> Outperform
  - UNP: 2026-10-02 Susquehanna: main, Positive -> Positive
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
Shares outstanding: 136.63M | fund size: 23.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Bond sell‑off may be ending, suggesting yields could peak and support utilities
- Technicals show XLU below 20‑day, 50‑day, and 200‑day SMAs, RSI 37.7, bearish momentum
- Analyst coverage of top holdings is 80.9% buy with a +23.1% price target
- Fund flows flat over the week, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

- [The secret signs the bond sell-off might be ending](https://www.cnbc.com/amp/2026/10/02/the-secret-signs-the-bond-sell-off-might-be-ending.html)  
  <sub>CNBC, 4 hours ago</sub>  
  As the U.S. bond market firmed Thursday and the iShares 20+ Year Treasury Bond ETF (TLT) posted its best intraday rally in at least a month,...
- [Webcast: Navigate the Evolving Landscape of Options-Based Income ETFs | ETF Trends](https://www.advisorperspectives.com/webinars/2026/11/04/navigate-the-evolving-landscape-of-options-based-income-etfs?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 24 hours ago</sub>  
  Generating meaningful income for clients while balancing tax efficiency, total return potential, and risk has become increasingly complex.
- [Options trades suggest bond sell-off may be ending as utilities and bond futures see bullish bets.](https://pluang.com/en/news-feed/tanda-rahasia-akhir-penjualan-obligasi)  
  <sub>Pluang, 4 hours ago</sub>  
  Recent options activity indicates a potential slowdown in the U.S. bond sell-off. A notable $1 million options trade in the State Street Utilities Select...
- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest State Street Materials Select Sector SPDR ETF (XLB) stock quote, history, news and other vital information to help you with your stock...
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [8 Of 11 Sectors Fall In Thursday Trading As Cyclicals Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62111517/8-of-11-sectors-fall-in-thursday-trading-as-cyclicals-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with cyclical sectors holding two of the top three positions.
- [U.S. options trades signal bond sell-off may be nearing an end](https://tradersunion.com/news/financial-news/show/3626117-us-options-bond-selloff-end/)  
  <sub>Traders Union, 4 hours ago</sub>  
  Options trades and utilities activity hint U.S. bond sell-off may be ending as investors anticipate yields peaking and lower borrowing costs ahead.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 40.09 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 40.98 (-2.2%), 50d 42.69 (-6.1%), 200d 44.38 (-9.7%); 50d below 200d
Momentum: RSI(14) 37.7 | MACD -0.958 vs signal -0.943 (histogram -0.015)
Returns: 1d +1.0% | 5d +1.5% | 1m -6.0% | 3m -11.5%
52-week range: 39.25 - 47.73 (now 9.9% of the way up)
Volatility: ATR(14) 0.60 (1.5% of price) | annualised 20d 14.8%
Volume: 1.13x the 20-day average
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
Three-year record: +13.5% a year | beta to the market 0.43
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

<details><summary><b>What analysts and big funds say</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.80</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.1% above the current prices
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
Shares outstanding: 163.27M | fund size: 6.55B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Yield curve remains upward sloping with no rate surprise this week
- Technical: price below 20‑day and 50‑day SMA, RSI 41.1, low volume, MACD negative
- Fund flows show slight redemption (-0.5% share count) indicating weak demand
- Analyst coverage (44% of fund) is 100% buy with +13.6% price target, but limited to less than half the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday Amid Jobs Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-133147980.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.9% and the actively trad.
- [Short Interest Alert: Most and least shorted sub-$2B healthcare stocks in Sep. 2026](https://seekingalpha.com/news/4648944-short-interest-alert-most-and-least-shorted-sub-2b-healthcare-stocks-in-sep-2026)  
  <sub>Seeking Alpha, 31 minutes ago</sub>  
  Short interest data from late September 2026 highlights deeply divided investor sentiment across small-cap healthcare stocks (market capitalizations up to...
- [Most and least shorted mid- to mega-cap healthcare stocks at the end of September](https://seekingalpha.com/news/4648943-most-and-least-shorted-mid-to-mega-cap-healthcare-stocks-at-the-end-of-september)  
  <sub>Seeking Alpha, 47 minutes ago</sub>  
  Short interest data from late September 2026 highlights deeply divided investor sentiment across the healthcare sector. Strong bearish bets remain heavily...
- [JNJ or MRK: One Dividend Is Built to Last, One Faces a Reckoning](https://247wallst.com/investing/2026/10/01/jnj-or-mrk-one-dividend-is-built-to-last-one-faces-a-reckoning/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Both JNJ and MRK have surged in 2026, but a looming patent cliff and a balance sheet loaded with acquisition debt mean one of these pharma dividends faces a...
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [Sector Update: Healthcare Stocks Fall in Afternoon Trading](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-fall-afternoon-175059698.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Healthcare stocks declined Thursday afternoon, with the NYSE Healthcare Index falling 0.9% and the State Street Health Care Select Sector SPDR ETF (XLV)...
- [Sector Update: Healthcare Stocks Fall Late Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-fall-afternoon-195756861.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Healthcare stocks declined late Thursday afternoon, with the NYSE Healthcare Index falling 1% and the State Street Health Care Select Sector SPDR ETF (XLV)...
- [Sector Update: Healthcare](https://finance.yahoo.com/healthcare/articles/sector-healthcare-192953639.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Healthcare stocks declined late Thursday afternoon, with the NYSE Healthcare Index falling 1% and the State Street Health Care Select Sector SPDR ETF (XLV)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 166.07 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 168.38 (-1.4%), 50d 168.53 (-1.5%), 200d 156.70 (+6.0%); 50d above 200d
Momentum: RSI(14) 41.1 | MACD -0.151 vs signal 0.227 (histogram -0.378)
Returns: 1d -0.1% | 5d -2.7% | 1m -4.0% | 3m +2.5%
52-week range: 141.95 - 175.68 (now 71.5% of the way up)
Volatility: ATR(14) 2.38 (1.4% of price) | annualised 20d 14.0%
Volume: 0.31x the 20-day average
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
Three-year record: +11.2% a year | beta to the market 0.52
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
Weighted price target: +13.6% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-28 JP Morgan: main, Overweight -> Overweight
  - JNJ: 2026-09-29 JP Morgan: main, Neutral -> Neutral
  - ABBV: 2026-09-10 HSBC: main, Buy -> Buy
  - MRK: 2026-09-29 Scotiabank: main, Sector Outperform -> Sector Outperform
  - UNH: 2026-07-21 JP Morgan: main, Overweight -> Overweight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.5% (-200.01M) over 7d
Shares outstanding: 257.29M | fund size: 42.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Stocktwits Passport Portfolio: QQQ Holds Up Better Than SPY, DIA And Asian Stocks Amid Bond Market Rout This Week](https://finance.yahoo.com/markets/stocks/articles/stocktwits-passport-portfolio-qqq-holds-061913514.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  The Invesco QQQ Trust, which tracks the Nasdaq, has posted the lowest decline amongst its peers so far this week, bolstered in part by the resilience of...
- [Stocktwits AI Roundup: Micron’s Blowout Quarter, Nvidia’s $150B Buyback And The Race For AI Agents](https://stocktwits.com/news-articles/markets/equity/stocktwits-ai-roundup-micron-s-blowout-quarter-nvidia-s-150-b-buyback-and-the-race-for-ai-agents/cZDj2YGRB0x)  
  <sub>Stocktwits, 15 hours ago</sub>  
  AI infrastructure demand remains strong, but soaring costs and intensifying competition are keeping investors on edge.
- [iShares U.S. Telecommunications ETF (IYZ) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IYZ/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares U.S. Telecommunications ETF (IYZ) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 116.29 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 112.06 (+3.8%), 50d 106.78 (+8.9%), 200d 88.74 (+31.0%); 50d above 200d
Momentum: RSI(14) 63.5 | MACD 2.056 vs signal 2.046 (histogram 0.010)
Returns: 1d +3.1% | 5d +1.3% | 1m +6.3% | 3m +8.4%
52-week range: 60.03 - 116.29 (now 100.0% of the way up)
Volatility: ATR(14) 2.23 (1.9% of price) | annualised 20d 28.9%
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
Three-year record: +45.6% a year | beta to the market 1.30
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
Weighted price target: +27.7% above the current prices
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
Share count change: 1 week: +1.6% (191.67M) over 7d
Shares outstanding: 103.38M | fund size: 12.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Stocktwits Passport Portfolio: QQQ Holds Up Better Than SPY, DIA And Asian Stocks Amid Bond Market Rout This Week](https://finance.yahoo.com/markets/stocks/articles/stocktwits-passport-portfolio-qqq-holds-061913514.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  The Invesco QQQ Trust, which tracks the Nasdaq, has posted the lowest decline amongst its peers so far this week, bolstered in part by the resilience of...
- [Stocktwits AI Roundup: Micron’s Blowout Quarter, Nvidia’s $150B Buyback And The Race For AI Agents](https://stocktwits.com/news-articles/markets/equity/stocktwits-ai-roundup-micron-s-blowout-quarter-nvidia-s-150-b-buyback-and-the-race-for-ai-agents/cZDj2YGRB0x)  
  <sub>Stocktwits, 15 hours ago</sub>  
  AI infrastructure demand remains strong, but soaring costs and intensifying competition are keeping investors on edge.
- [How to Buy Tencent Stock (TCEHY) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-tencent-stock/)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  Tencent is a huge Chinese technology company. Its stock trades on the OTC market, but you can buy shares through most brokerages. Here's what you need to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 51.44 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 52.97 (-2.9%), 50d 54.30 (-5.3%), 200d 56.81 (-9.5%); 50d below 200d
Momentum: RSI(14) 32.8 | MACD -0.631 vs signal -0.513 (histogram -0.118)
Returns: 1d -1.3% | 5d -2.3% | 1m -5.7% | 3m -1.1%
52-week range: 50.48 - 66.99 (now 5.8% of the way up)
Volatility: ATR(14) 0.62 (1.2% of price) | annualised 20d 15.7%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Greater China Region
What it holds: P/E 11.90 | P/B 1.39 | P/S 1.38 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +9.2% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 6.33B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Tencent Holdings Ltd 13.9%, Alibaba Group Holding Ltd Ordinary Shares 9.6%, China Construction Bank Corp Class H 4.0%, Industrial And Commercial Bank Of China Ltd Class H 2.5%, Xiaomi Corp Class B 2.4%
Sector mix: Consumer cyclical 23.4%, Financial services 20.0%, Communication services 18.2%, Technology 11.8%
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
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +59.9% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Share count change: 1 week: +4.1% (245.18M) over 7d
Shares outstanding: 121.14M | fund size: 6.23B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Nike Sinks 8% as Weak Outlook and Layoffs Follow Revenue Miss; Lululemon and On Holding Remain Flat](https://247wallst.com/investing/2026/10/02/nike-sinks-8-as-weak-outlook-and-layoffs-follow-revenue-miss-lululemon-and-on-holding-remain-flat/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Nike sinks 7% after missing revenue estimates and guiding for a high-single-digit decline, while Lululemon and On Holding drop less than 1%.
- [Exchange-Traded Funds, Equity Futures Higher Pre-Bell Friday Amid Jobs Data](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-133147980.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.9% and the actively trad.
- [Sector Update: Consumer](https://www.bitget.com/amp/news/detail/12560605901065)  
  <sub>Bitget, 16 hours ago</sub>  
  03:23 PM EDT, 10/01/2026 (MT Newswires) -- Consumer stocks were mixed late Thursday afternoon with the State Street Consumer Staples Select Sector SPDR ETF...
- [Exchange-Traded Funds Mixed, US Equities Fall After Midday](https://finance.yahoo.com/markets/articles/exchange-traded-funds-mixed-us-171345834.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded fund IWM rose and IVV edged lower. Actively traded Invesco QQQ Trust (QQQ) eased 0.1%.
- [Sector Update: Consumer Stocks Mixed Late Afternoon](https://www.bitget.com/amp/news/detail/12560605901115)  
  <sub>Bitget, 16 hours ago</sub>  
  03:44 PM EDT, 10/01/2026 (MT Newswires) -- Consumer stocks were mixed late Thursday afternoon with the State Street Consumer Staples Select Sector SPDR ETF...
- [State Street Materials Select Sector SPDR ETF (XLB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLB/)  
  <sub>Yahoo! Finance Canada, 20 hours ago</sub>  
  Find the latest State Street Materials Select Sector SPDR ETF (XLB) stock quote, history, news and other vital information to help you with your stock...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 110.59 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 111.25 (-0.6%), 50d 114.40 (-3.3%), 200d 116.38 (-5.0%); 50d below 200d
Momentum: RSI(14) 43.6 | MACD -1.550 vs signal -1.516 (histogram -0.034)
Returns: 1d +1.6% | 5d +0.0% | 1m -3.7% | 3m -6.3%
52-week range: 105.66 - 124.52 (now 26.1% of the way up)
Volatility: ATR(14) 1.52 (1.4% of price) | annualised 20d 15.0%
Volume: 0.33x the 20-day average
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
Three-year record: +11.5% a year | beta to the market 1.16
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
Weighted price target: +24.1% above the current prices
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
Share count change: 1 week: +2.9% (658.19M) over 7d
Shares outstanding: 208.49M | fund size: 23.06B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals are bullish but not decisive, heavy roll cost and recent outflows offset bullish sentiment, and positioning is extremely crowded.

**Main reasons it gave:**
- Heavy roll cost: -8.1% per year (COST OF HOLDING)
- Fund outflows: share count down 1.3% over past week (FUND FLOWS)
- Crowded long position: net long 18.9% and 100% percentile over 52 weeks (POSITIONING)
- Technicals bullish: price above 20‑day, 50‑day, 200‑day SMAs, RSI 64.7, but no decisive break (TECHNICALS)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 11.77 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 11.37 (+3.5%), 50d 10.95 (+7.5%), 200d 9.98 (+17.9%); 50d above 200d
Momentum: RSI(14) 64.7 | MACD 0.111 vs signal 0.110 (histogram 0.001)
Returns: 1d +2.7% | 5d +5.0% | 1m +0.9% | 3m +18.4%
52-week range: 9.02 - 11.82 (now 98.2% of the way up)
Volatility: ATR(14) 0.20 (1.7% of price) | annualised 20d 21.7%
Volume: 0.61x the 20-day average
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
Cost of holding this fund instead of sugar itself: -8.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +18.4%, commodity +29.0%, gap -10.6% | 6 months: fund +16.1%, commodity +30.9%, gap -14.8% | 12 months: fund +13.6%, commodity +21.7%, gap -8.1%
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
Direction: money going out (1 week)
Share count change: 1 week: -1.3% (-782.57K) over 7d
Shares outstanding: 5.11M | fund size: 60.17M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro data surprise this week (inflation 3.4%, unemployment 4.2%)
- Technicals show price below 20‑day SMA and negative momentum, but no decisive break on volume
- CFTC shows crowded long (21.8% net long, 95th percentile) with a slight weekly decrease (-0.7%)
- Cost of holding is heavy at -12.4% annual gap, a tailwind for shorts

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 18.97 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 19.74 (-3.9%), 50d 19.07 (-0.5%), 200d 18.14 (+4.6%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.026 vs signal 0.149 (histogram -0.175)
Returns: 1d -0.1% | 5d -3.9% | 1m -6.2% | 3m +8.7%
52-week range: 16.47 - 20.29 (now 65.4% of the way up)
Volatility: ATR(14) 0.31 (1.7% of price) | annualised 20d 16.3%
Volume: 0.15x the 20-day average
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
Cost of holding this fund instead of corn itself: -12.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +8.7%, commodity +13.9%, gap -5.2% | 6 months: fund +4.3%, commodity +11.0%, gap -6.7% | 12 months: fund +8.1%, commodity +20.5%, gap -12.4%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.20</summary>

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
Share count change: 1 week: +2.4% (3.74M) over 7d
Shares outstanding: 8.45M | fund size: 160.24M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals neutral, modest positioning increase, heavy cost of holding.

**Main reasons it gave:**
- Macro environment stable: Treasury yields unchanged, inflation 3.4% near target, Fed policy unchanged
- Technical indicators neutral: price near 20‑day SMA, RSI 47, MACD below signal, no decisive break
- Positioning shows modest net‑long increase (+4.9% week) with 27.4% net long, crowding at 88% percentile – not extreme
- Cost of holding is heavy (‑5.6% annual), a drag on long positions

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 39.53 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 39.88 (-0.9%), 50d 39.78 (-0.6%), 200d 37.45 (+5.6%); 50d above 200d
Momentum: RSI(14) 47.2 | MACD 0.046 vs signal 0.124 (histogram -0.078)
Returns: 1d +0.1% | 5d -2.7% | 1m +0.0% | 3m +4.5%
52-week range: 30.27 - 41.43 (now 83.0% of the way up)
Volatility: ATR(14) 0.65 (1.6% of price) | annualised 20d 28.0%
Volume: 0.12x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.6% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +4.5%, commodity +6.9%, gap -2.4% | 6 months: fund +15.0%, commodity +18.7%, gap -3.7% | 12 months: fund +31.1%, commodity +36.7%, gap -5.6%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.25</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 27.4% of open interest (301,657 contracts)
Change on the week: +4.9% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.25</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +3.4% (24.73M) over 7d
Shares outstanding: 18.93M | fund size: 748.44M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: inflation 3.4% in line with expectations, no rate change
- Technical indicators show price below 20‑day, 50‑day and 200‑day SMAs, RSI 41, MACD negative, but low volume and no decisive break
- Positioning: large speculators net long 12.5% with a -0.2% change, indicating neutral sentiment
- Cost of holding: -2.1% annual drag, a bearish factor for long exposure

<details><summary><b>News</b> — score +0.00</summary>

- [Dow, S&P 500, Nasdaq Futures Fall As Brent Tops $106 After Trump Rejects Iran Proposal: MU, SLV, QNT, META In Focus](https://stocktwits.com/news-articles/markets/equity/dow-s-and-p-500-nasdaq-futures-fall-as-brent-tops-106-after-trump-rejects-iran-proposal-mu-slv-qnt-meta-in-focus/cZMSLOqRBfL)  
  <sub>Stocktwits, 9 hours ago</sub>  
  On Saturday, reports said U.S. President Donald Trump rejected an Iranian proposal to reopen the Strait of Hormuz, arguing that Iran sought a deal to reopen...
- [Gold vs silver ETFs: All mutual fund schemes in red in September 2026 after a strong run in August — what to know](https://www.livemint.com/money/personal-finance/gold-vs-silver-etfs-all-mutual-fund-schemes-in-red-in-september-2026-after-a-strong-run-in-august-what-to-know-11790879926403.html)  
  <sub>Livemint, 19 hours ago</sub>  
  Gold and silver ETFs reversed their strong August performance in September 2026 as domestic prices declined. How did the two commodity ETFs fare during the...
- [Silver ETFs Slide Nearly 4% As Oil Surge Triggers Bullion Sell-off](https://www.businessworld.in/article/silver-etfs-slide-nearly-4-as-oil-surge-triggers-bullion-sell-off-625943)  
  <sub>BW Businessworld, 7 hours ago</sub>  
  Gold and silver exchange-traded funds (ETFs) came under heavy selling pressure on 28 September, with silver ETFs falling nearly 4 per cent and gold ETFs...
- [Silver Rate Today in Bangalore 2nd October 2026 : 1 KG, Todays Silver Price in Bangalore](https://www.businesstoday.in/commodity/silver-rate-in-bangalore-today)  
  <sub>Business Today, 6 hours ago</sub>  
  Silver Price in Bangalore Today 2nd October 2026: Find updated 1 KG Silver rate today in Bangalore 2nd October 2026. Also check latest gold price related...
- [Gold Rate Today in Delhi 2nd October 2026 : 22 & 24 Carat, Todays Gold Price in Delhi](https://www.businesstoday.in/commodity/gold-rate-in-delhi-today)  
  <sub>Business Today, 3 hours ago</sub>  
  Gold rate in Delhi on Friday, Oct 02, 2026 : Today, the price of 24-carat Gold in Delhi is ₹1,49,400 per 10 grams. A day earlier, on Oct 01, 2026, the rate...
- [Gold and Silver Price Predictions for October](https://captainaltcoin.com/gold-and-silver-price-predictions-for-october/)  
  <sub>CaptainAltcoin, 18 hours ago</sub>  
  Gold and silver are heading into October at important technical levels after falling from their recent highs. The silver price is around $60.98,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 55.08 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 57.76 (-4.6%), 50d 57.75 (-4.6%), 200d 65.92 (-16.4%); 50d below 200d
Momentum: RSI(14) 41.2 | MACD -0.919 vs signal -0.425 (histogram -0.494)
Returns: 1d +0.1% | 5d -5.3% | 1m -6.8% | 3m -1.8%
52-week range: 42.40 - 105.60 (now 20.1% of the way up)
Volatility: ATR(14) 1.62 (2.9% of price) | annualised 20d 38.5%
Volume: 0.45x the 20-day average
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
Cost of holding this fund instead of silver itself: -2.1% a year -- a steady drag
Measured: 3 months: fund -1.8%, commodity -0.4%, gap -1.5% | 6 months: fund -16.3%, commodity -15.2%, gap -1.1% | 12 months: fund +28.4%, commodity +30.4%, gap -2.1%
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
Share count change: 1 week: +7.9% (2.53B) over 7d
Shares outstanding: 630.97M | fund size: 34.75B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, crowded long positioning with modest weekly change, modest inflows, and near‑zero cost of holding suggest no clear directional edge.

**Main reasons it gave:**
- Macro data: inflation 3.4% and unemployment 4.2% were as expected, no surprise
- Technicals: price near 52‑week high, RSI 49.9 (neutral), MACD histogram -0.152 (slight bearish), low volume
- Positioning: net long 23.8% of OI, crowding 97th percentile, weekly change +1.9% (modest increase)
- Fund flows: share count +1.8% over 7 days, indicating modest inflow
- Cost of holding: near‑zero annual cost (-0.9%), indicating low drag but not directional

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.36 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 27.74 (-1.4%), 50d 26.66 (+2.6%), 200d 24.63 (+11.1%); 50d above 200d
Momentum: RSI(14) 49.9 | MACD 0.183 vs signal 0.335 (histogram -0.152)
Returns: 1d +0.6% | 5d -1.3% | 1m -0.9% | 3m +8.4%
52-week range: 21.56 - 28.14 (now 88.2% of the way up)
Volatility: ATR(14) 0.33 (1.2% of price) | annualised 20d 15.9%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.10</summary>

```text
Cost of holding this fund instead of soybeans itself: -0.9% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +8.4%, commodity +8.7%, gap -0.3% | 6 months: fund +12.4%, commodity +10.4%, gap +1.9% | 12 months: fund +25.9%, commodity +26.8%, gap -0.9%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.20</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net long 23.8% of open interest (1,114,328 contracts)
Change on the week: +1.9% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.20</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.8% (826.46K) over 7d
Shares outstanding: 1.68M | fund size: 46.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Large speculators net short increased by 1.9% of open interest
- Cost of holding heavy at -10.8% per year
- US natural gas inventories built 64 Bcf (79th percentile)
- EIA forecast expects price rise to $4.03 in 3 months
- Fund inflows increased share count by 3.5% over 1 week

<details><summary><b>News</b> — score +0.00</summary>

- [UNG Oct 2026 13.000 put (UNG261002P00013000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/UNG261002P00013000/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest UNG Oct 2026 13.000 put (UNG261002P00013000) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 10.32 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 10.50 (-1.8%), 50d 10.27 (+0.4%), 200d 11.36 (-9.1%); 50d below 200d
Momentum: RSI(14) 47.0 | MACD 0.034 vs signal 0.087 (histogram -0.053)
Returns: 1d +1.6% | 5d -7.3% | 1m -4.0% | 3m -11.9%
52-week range: 9.63 - 16.90 (now 9.5% of the way up)
Volatility: ATR(14) 0.35 (3.4% of price) | annualised 20d 44.0%
Volume: 0.35x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -10.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -11.9%, commodity -7.3%, gap -4.6% | 6 months: fund -9.1%, commodity +7.5%, gap -16.5% | 12 months: fund -24.2%, commodity -13.4%, gap -10.8%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.30</summary>

```text
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Natural gas: 3,415.0 billion cubic feet, +64.0 on the week (a build), 79% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 3.6% of open interest (1,837,146 contracts)
Change on the week: +1.9% of open interest
Crowding: 67% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +3.5% (19.35M) over 7d
Shares outstanding: 55.95M | fund size: 577.39M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- EIA price outlook forecasts WTI to fall to $87 this month, well below current price of $144.18
- Crude oil inventories built 0.9% week over week, indicating bearish supply pressure
- CFTC positioning shows a crowded long (98th percentile) with only a +0.1% change, suggesting limited upside
- Macro data unchanged: Treasury yields stable, inflation 3.4% near target, VIX modestly higher
- Technicals: price below 20‑day SMA and negative MACD histogram, indicating short‑term weakness

<details><summary><b>News</b> — score +0.00</summary>

- [5 Energy ETFs That Have Soared in 2026](https://oilprice.com/Energy/Energy-General/5-Energy-ETFs-That-Have-Soared-in-2026.html)  
  <sub>Crude Oil Prices Today | OilPrice.com, 15 hours ago</sub>  
  Freight, gasoline, crude oil and broad-energy ETFs have delivered triple- and even four-digit gains in 2026 as the Iran war has driven energy and shipping...
- [Crude oil jumps as U.S. reportedly sends third carrier, more troops to Middle East (USO:NYSEARCA)](https://seekingalpha.com/news/4649599-crude-oil-jumps-as-us-reportedly-sends-third-carrier-more-troops-to-middle-east)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  Crude oil jumped on reports the US has deployed third aircraft carrier to the Middle East while China suspended exports of oil products, sparking concerns...
- [Brent Oil Is Back Above $100 as a Third Aircraft Carrier Heads to the Middle East](https://247wallst.com/investing/2026/10/02/brent-oil-is-back-above-100-as-a-third-aircraft-carrier-heads-to-the-middle-east/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  USO jumped 3% as Brent crossed $100, but Trump called escalation only "possible" and no confirmed event has cut actual supply.
- [Scott Bessent Says Iran Transported 'Zero' Oil Onto Tankers Last Month — Trump’s Sanctions Are Targeting Tehran’s ‘Most Critical’ Revenue Stream](https://www.tradingview.com/news/benzinga:c9e675dca094b:0-scott-bessent-says-iran-transported-zero-oil-onto-tankers-last-month-trump-s-sanctions-are-targeting-tehran-s-most-critical-revenue-stream/)  
  <sub>TradingView, 10 hours ago</sub>  
  Treasury Secretary Scott Bessent says the President Donald Trump-led Operation Economic Outcast, which focuses on imposing trade restrictions on Iran,...
- [Iran Says 'Only A Negotiated Solution' Can Get US Out Of The Deadlock After Trump Rejects Proposal To Reopen Strait Of Hormuz](https://stocktwits.com/news-articles/markets/equity/iran-negotiated-solution-us-deadlock-trump-rejects-strait-of-hormuz-proposal/cZMi1aSRBf2)  
  <sub>Stocktwits, 19 hours ago</sub>  
  According to a Reuters report, Iranian Foreign Minister Abbas Araqchi said Sunday that Tehran's conditions for reopening the strategic waterway remain...
- [BWET fund rises 4,050% since start of 2026 — OilPrice](https://ua.news/en/energetika/fond-bwet-zris-na-4-050-vid-pochatku-2026-roku-oilprice)  
  <sub>UA.NEWS, 15 hours ago</sub>  
  The Breakwave Tanker Shipping ETF gained 4050% since the start of 2026, the highest result among five energy ETFs analyzed by OilPrice.
- [Europe to release stocked diesel oil, Trump says; G7 may release up to 100M barrels](https://seekingalpha.com/news/4649847-europe-to-release-stocked-diesel-oil-trump-says-g7-may-release-up-to-100m-barrels)  
  <sub>Seeking Alpha, 12 minutes ago</sub>  
  Crude oil futures added to losses after President ​Trump said on Truth Social that Europe has agreed to ​release a "massive ​amount" of diesel oil...
- [Trump Wants to Keep America’s Diesel at Home: It's Having a Strange Effect on Oil Prices](https://www.tradingview.com/news/benzinga:a4372e5c2094b:0-trump-wants-to-keep-america-s-diesel-at-home-it-s-having-a-strange-effect-on-oil-prices/)  
  <sub>TradingView, 19 hours ago</sub>  
  When President Donald Trump said last week that the U.S. should stop sending its diesel abroad, the goal was simple: bring down record fuel prices for...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 144.18 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 150.54 (-4.2%), 50d 137.30 (+5.0%), 200d 115.16 (+25.2%); 50d above 200d
Momentum: RSI(14) 49.0 | MACD 2.439 vs signal 4.070 (histogram -1.631)
Returns: 1d -3.9% | 5d -2.8% | 1m +2.2% | 3m +38.2%
52-week range: 66.17 - 161.86 (now 81.5% of the way up)
Volatility: ATR(14) 5.59 (3.9% of price) | annualised 20d 48.2%
Volume: 0.57x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.60</summary>

```text
US inventories, week ending 2026-09-25 (published the following Wednesday)
  Crude oil: 427.3 million barrels, +0.9 on the week (a build), 62% percentile over 52 weeks
  Petrol: 204.4 million barrels, -1.7 on the week (a draw), 2% percentile over 52 weeks -- low for the time of year
  Diesel: 105.2 million barrels, -2.3 on the week (a draw), 23% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.60</summary>

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
Direction: money coming in (1 week)
Share count change: 1 week: +1.2% (23.32M) over 7d
Shares outstanding: 13.20M | fund size: 1.90B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro data surprise this week (inflation, unemployment, jobless claims in line with expectations)
- Technicals show price below 20‑day and 50‑day SMAs, RSI 40.1, MACD negative, no decisive break
- Positioning: net short 2.5% of OI, decreasing by 1.7% this week (small bullish shift)
- Cost of holding -14.7% annual, heavy drag on long exposure

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 24.85 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 25.85 (-3.9%), 50d 25.51 (-2.6%), 200d 23.18 (+7.2%); 50d above 200d
Momentum: RSI(14) 40.1 | MACD -0.293 vs signal -0.076 (histogram -0.217)
Returns: 1d +0.5% | 5d -2.5% | 1m -10.8% | 3m +8.4%
52-week range: 19.88 - 28.00 (now 61.2% of the way up)
Volatility: ATR(14) 0.53 (2.1% of price) | annualised 20d 22.0%
Volume: 0.16x the 20-day average
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
Cost of holding this fund instead of wheat itself: -14.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +8.4%, commodity +13.4%, gap -5.1% | 6 months: fund +8.7%, commodity +14.9%, gap -6.3% | 12 months: fund +20.3%, commodity +35.0%, gap -14.7%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.15</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-22, published the following Friday)
Large speculators: net short 2.5% of open interest (483,279 contracts)
Change on the week: -1.7% of open interest
Crowding: 78% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.15</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +3.8% (13.26M) over 7d
Shares outstanding: 14.48M | fund size: 359.79M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Gold ETFs Keep the Bid, but Investors Miss This Key Seasonality Pattern](https://www.tradingview.com/news/benzinga:5dff6bede094b:0-gold-etfs-keep-the-bid-but-investors-miss-this-key-seasonality-pattern/)  
  <sub>TradingView, 4 hours ago</sub>  
  Over the last two months, gold has completed a round trip. Spot bullion prices rose to nearly $4700 before erasing the entire move.
- [Gold In Pension Funds: Case Studies](https://seekingalpha.com/article/4951526-gold-pension-funds-case-studies)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Gold has received increased attention from some pension funds as they reassess portfolio construction against a backdrop of geopolitical tensions,...
- [Gold Stocks, ETFs See Best Week In Over A Year — Why Gold Is Back In Vogue?](https://stocktwits.com/news-articles/markets/equity/gold-stocks-et-fs-see-best-week-in-over-a-year-why-gold-is-back-in-vogue/cZofjpERJ9U)  
  <sub>Stocktwits, 16 hours ago</sub>  
  U.S. gold equities and exchange-traded funds are pacing toward their strongest weekly performance in over a year, with spot gold climbing back above the...
- [Gold as a Hedge: Navigating Global Debt & Persistent Inflation](https://etfdb.com/etf-strategist-channel/gold-as-a-hedge-navigating-global-debt-persistent-inflation/)  
  <sub>ETF Database, 18 hours ago</sub>  
  Financial advisors in 2026 are increasingly leveraging gold as a core structural hedge and portfolio diversifier, typically advising a 5% to 10% allocation...
- [Daily ETF Flows: BIL On Top](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-bil-top-210005431.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Here are the daily ETF fund flows for September 30, 2026.
- [Gold Is Defying 5% Treasury Yields. Could Falling Rates Reignite Gold ETFs? - SPDR Gold Shares (ARCA:GLD)](https://www.benzinga.com/etfs/specialty-etfs/26/10/62118420/gold-is-defying-24-year-high-treasury-yields-will-gold-etfs-follow)  
  <sub>Benzinga, 21 hours ago</sub>  
  Gold is holding above $4000 despite soaring Treasury yields. Here's why falling rates could reignite demand for gold ETFs.
- [SPDR Gold ETF Options Spot-On: On October 1st, 255.65K Contracts Were Traded, With 5.53 Million Open Interest](https://news.futunn.com/en/post/1000504199/spdr-gold-etf-options-spot-on-on-october-1st-255)  
  <sub>富途牛牛, 18 hours ago</sub>  
  OnOctober 1st ET, $SPDR Gold ETF(GLD.US)$ had active options trading, with a total trading volume of 255.65K options for the day, of which put options...
- [Why I Made Gold A Full Position In My Portfolio (NYSEARCA:GLD)](https://seekingalpha.com/article/4951433-why-i-made-gold-a-full-position-in-my-portfolio)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Buy the dip in SPDR Gold Shares ETF as high yields, U.S. debt, and potential Fed action could spark a gold bull run. Click to review gold risks and upside...
- [Stock Market Today: S&P 500 Slips as Micron Fails to Impress, 10-Year Yields Ease to 5.25%](https://www.tradingview.com/news/benzinga:2e1fd44ac094b:0-stock-market-today-s-p-500-slips-as-micron-fails-to-impress-10-year-yields-ease-to-5-25/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 slipped at midday Thursday as Micron Technology Inc. NASDAQ:MU fell 1.6% despite a record quarter, with the 10-year Treasury yield hovering near...
- [Gold prices at risk of sliding below $4,000 in Q4, BofA warns (GLD:NYSEARCA)](https://seekingalpha.com/news/4649576-gold-prices-at-risk-of-sliding-below-4000-in-q4-bofa-warns)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  BofA maintains a bullish 2027 gold price forecast but said their outlook is not without risks, seeing gold prices falling to $3750/oz in Q4 with energy...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 3.98% (-0.09 on the week) | 5-year 4.99% (-0.02 on the week) | 10-year 5.20% (+0.02 on the week) | 30-year 5.57% (+0.07 on the week)
Yield curve, 10-year minus 3-month: +1.22 points -- upward sloping (normal)
US dollar index: 101.69 (+0.72 on the week)
Volatility (VIX): 15.52 (+0.7 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-09-26)
Policy and expectations: Fed target 4.00% | market expects 2.4% inflation over 10 years
Rate path: 2-year Treasury 4.88% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 382.00 (bar of 2026-10-02), from 502 daily bars
Trend: vs 20d SMA 393.30 (-2.9%), 50d 396.33 (-3.6%), 200d 416.16 (-8.2%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -4.993 vs signal -3.164 (histogram -1.829)
Returns: 1d -0.2% | 5d -2.9% | 1m -5.2% | 3m -0.0%
52-week range: 354.79 - 495.90 (now 19.3% of the way up)
Volatility: ATR(14) 6.71 (1.8% of price) | annualised 20d 21.1%
Volume: 0.43x the 20-day average
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
Measured: 3 months: fund -0.0%, commodity +1.0%, gap -1.1% | 6 months: fund -11.0%, commodity -10.0%, gap -1.0% | 12 months: fund +7.3%, commodity +8.0%, gap -0.7%
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
Shares outstanding: 260.30M | fund size: 99.43B
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

