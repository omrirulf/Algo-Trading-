# Daily report

**18 Sep 2026, 20:02 Israel time (17:02 UTC)** · 80 names checked · 2 traded · 1 with a problem

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 3 | 12 | 1 |
| Whole-market funds | 14 | 5 | 9 | 0 |
| Sector and country funds | 41 | 2 | 39 | 0 |
| Commodities | 9 | 0 | 9 | 0 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| US government bonds, 7-10 years (IEF) · Index fund | **Stop raised.** At +0.42R, following the price. Stop-loss raised 91.76 → 91.61. |
| Nvidia (NVDA) · Company | **Stop raised.** At +0.33R, following the price. Stop-loss raised 201.80 → 206.79. |
| US inflation-linked bonds (TIP) · Index fund | **Stop raised.** At +0.87R, following the price. Stop-loss raised 106.41 → 106.08. |
| US dollar (UUP) · Index fund | **Stop raised.** At +0.19R, following the price. Stop-loss raised 28.16 → 28.21. |
| Alphabet (Google) (GOOGL) · Company | **Stop placed.** Had no stop-loss order, so a new one was placed at 330.44 (from the trade's own record). |
| Developing country bonds (EMB) · Index fund | **Holding.** +0.08R, holding 128 shares. Stop-loss 94.05. |
| Gold (GLD) · Commodity | **Holding.** -0.69R, holding 10 shares. Stop-loss 404.87. |
| Eli Lilly (LLY) · Company | **Holding.** -0.07R, holding 4 shares. Stop-loss 1085.29. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.22R, holding 127 shares. Stop-loss 37.03. |
| US government bonds, 20+ years (TLT) · Index fund | **Holding.** -0.02R, holding 147 shares. Stop-loss 82.41. |
| Biotech (XBI) · Sector or country | **Holding.** -0.39R, holding 45 shares. Stop-loss 161.15. |
| US shopping and leisure (XLY) · Sector or country | **Holding.** -0.29R, holding 63 shares. Stop-loss 113.36. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Alphabet (Google) (GOOGL) · Company — BULLISH, confidence 0.56

**Result:** REJECTED · no room for equity GOOGL under its 5% cap or the sleeve budget limit: equity 99821.40, price 349.71, existing exposure 4896.22, headroom 5503.96

**In the model's own words:**

> Antitrust remedies ruling unsealed with a market-friendly read plus fresh AI-driven target hikes lifted the stock ~3% intraday; this lands on a business with 24% revenue growth, 55% margins, low leverage and a modest 17.5x trailing P/E. Technicals are constructive but not extended (RSI 55, price above 20/50/200d, MACD crossing up) though volume is below average and 3m return is still negative. Consensus is already strong_buy, so the 22% gap to mean target is the main incremental support. No insider transactions in 180 days - treated as no information. Several news items are promotional/listicle content and were discounted.

**Main reasons it gave:**
- Advertising antitrust remedies decision unsealed, read as relief; stock +3% intraday
- Fresh AI-related price target hikes; mean target 428 (+22.5%)
- Revenue +24% YoY, 54.8% margin, trailing P/E 17.5, D/E 19%
- Price above 20/50/200d SMAs with MACD histogram turning positive, RSI 55
- Volume only 0.89x average and 3-month return -4.9%

<details><summary><b>News</b> — score +0.45</summary>

- [Why Alphabet Stock Popped This Morning](https://www.google.com/goto?url=CAESmgEB6zswFVfbW6cWv9nb2KRCyjx6q6fRiFZSKDikyd_em3F7NZxgpnXFT2-hzNXAVK--hhtKmTgwtBJnzjfwr44wM97Hb3EBd39IqzHuU9tLRtM4Inq6I6DY-3dwRDDA_rKCoECi2v4MTqouz303kNWbhlrVdCRIednRs2fDQWXTH_o73S2aTUgIx8jX7FkTiuxoeJf5m5uV4v-Z)  
  <sub>Yahoo Finance, 42 minutes ago</sub>  
  Alphabet (NASDAQ: GOOG) (NASDAQ: GOOGL) stock jumped as much as 3% in early trading Friday before retracing a bit later in the morning. As of 11 a.m. ET,...
- [Here's How Google Advertising Antitrust Ruling Could Play Out](https://www.google.com/goto?url=CAESnQEB6zswFR_Jwpk3xaZxAUY8ltnT_ZZi3AZ1Aj8h4sDssWJPRFU7eeUBBFJz1HEU7kFsUNoGjSHD4vsxXNeybCZSQBNTOGfZYGL9B3fJuzKPuoGH_HyZEss-t6APeIANpF9dsMgY_Dwcmud32oQC_KAOEhEv3Y4syvjpRZqd3180-gsvzA8LZzWao6Qs-0z2zbJl5HiLou3xIbCMkve6)  
  <sub>Investor's Business Daily, 5 hours ago</sub>  
  Google stock edged up on Thursday after the federal judge unsealed a detailed remedies decision in an advertising antitrust case.
- [Alphabet Stock Stays Flat - Ideal for GOOGL Short Put and Put Credit Spread Plays](https://www.barchart.com/story/news/4679372/alphabet-stock-stays-flat-ideal-for-googl-short-put-and-put-credit-spread-plays)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Alphabet stock (GOOGL and GOOG) has been flat for the last 1 to 3 months. That works for investors who short out-of-the-money (OTM) puts or do vertical put...
- [Alphabet GOOGL Stock Draws Fresh AI Price Target Hikes](https://www.google.com/goto?url=CAESfwHrOzAVLfglRi9Si5vzVp5WEkZ8sexko4n3CiQl3AxpDbNbMzUYKXTJF_m_DcBkY-CO1Rhu9L-9Zl6qZTvE_yv_W_j17zGcZOZF_h1O_LSHK3OZuw99jsRhvSKApq7Thy9IX1QAbRHvm9i-IbVRISxg32_0UjX8bBmgmUYLxnk)  
  <sub>Timothy Sykes, 4 hours ago</sub>  
  Alphabet Inc. stocks have been trading up by 2.02 percent amid strong AI product momentum and robust cloud growth optimism. Key Takeaways For GOOGL Traders.
- [GOOGL Stock Draws Bullish Targets As AI Bets Scale Up](https://www.google.com/goto?url=CAESfAHrOzAVzg-hsDAaTjyiZQXGtL1VLYGtJ7NBcxM5qnGzZ9Bcry-0JRA8JTdQfVt6ABHOIDKyYte8buVTRWATLmDKtPjG4xCFutoQ8ImBIKz0xbpRoyBYhZt5HBGPgQQga6OE3sqMFmA4RrIR0iqlTNsq73q950tcILggWvI)  
  <sub>StocksToTrade, 3 hours ago</sub>  
  Alphabet Inc. stocks have been trading up by 2.37 percent following strong AI-driven ad revenue growth and bullish analyst upgrades. Key Takeaways For GOOGL...
- [GOOGL Jumps as Upgrades & Antitrust Relief Lift Stock](https://www.google.com/goto?url=CAESlAEB6zswFaYbuMZj6abNX9ByxIHT-hjC28UyxdxWyAoTaEkkATxqTUr7kS-EznzxZ8_3Cr_cCDBJLDV8bnvp-O4oJMgWofdErM9uyznwqm9q0xPM5PfdMAa0YX0LsQjsiZlIrHD8_5hdwR6njd42197vx0-K_8JkHlVBWRC_OBWaddNrwRVxMd-WcFabVILqvbeM65Fv)  
  <sub>TradingPedia, 4 hours ago</sub>  
  Sandra Leggero. Sandra Leggero has a background in financial markets, having spent more than 9 years in commodities trading for several European and Asian...
- [Alphabet Inc. - GOOGL 6 1/4 05/15/29 (NASDAQ:GOOGM) Passes the GARP Screen for Growth at a Reasonable Price](https://www.google.com/goto?url=CAES0gEB6zswFcZJ7LfaOtacy2YveILgE5xy8d4BAoYYMzPcYW1XX5-Z1ozwVVUrlWDQ-p9AxpeECinpzmxGk1Bxm2VzEiCYUl3fwN7kzOHJr6LPm6cQdipOXUaTc9_Sf7QoQO6In9MH_BKuVyIjk-26KnvYa5d4JdaX2BncisMQo6ri2xaVcnPhfXAbpBFAqlZPeiEucRfDp2wpDc-c9wcW7INlIXfPSqehc9AX2z-lxSYeUvkoQL-ZCZaURZJL9J7s_IgzPENAKTq4wKLeLA_tOt0xn-E)  
  <sub>ChartMill, 8 hours ago</sub>  
  Alphabet (GOOGM) scores well on Peter Lynch GARP criteria: 29% EPS growth, low PEG, strong balance sheet and attractive valuation.
- [GOOGL 260925 347.50C (GOOGL260925C347500) Stock Options Chain | Quotes & News](https://www.moomoo.com/stock/GOOGL260925C347500-US)  
  <sub>Moomoo, 12 hours ago</sub>  
  Track real-time GOOGL 260925 347.50C (GOOGL260925C347500) stock options chain data and pricing information and news on moomoo App for your options trading...
- [Stock Market Research & Investor Analysis Tools - TIKR](https://www.google.com/goto?url=CAESoAEB6zswFX2g70ktBkq3wajdxbxYx8WcQuq1ag5RM8T6u4ksuUI6MbzRH4pFOpRLpBAJoe7z-AxCNgXHvtEnltt5GCoSK9Z8-aWW0Hgg8PWiXM4UzWoMXsMdSZa8pyS25co3TijaLO3Ok7WGFNVaAcuMRVQydUenR0d6LJSi5gqSEgXkBOrgTULlmgvuRCwVtBxaBnrYgvcMAAc1iN8eTNW1)  
  <sub>TIKR.com, 8 hours ago</sub>  
  High-quality data and tools for global stocks. Follow top investors, analyze businesses, & monitor your portfolio with TIKR. Get started for free today!
- [GOOGL Maintains by Tigress Financial -- Price Target Raised to $485](https://www.google.com/goto?url=CAESngEB6zswFb_YQdIAG0oPorArv3dj2q-AvGgsOV6GLFtOSWG2lhmYKJhg5vhkgRlwkF-Qii_3qX6Ioq8LdeY8gY3Hr1g6drIu3p2AdJ_8Dzyu0NJFmzgpxaWTydKkLr30TPcSAhvDiGWDqZe6liEHx61xZs5gs9DLc3m69uf5ElDoiSF6CGRW1G3iiSU6nzaZ3pkP4bgSMBAvUui3kkvOOA)  
  <sub>GuruFocus, 3 hours ago</sub>  
  Alphabet Inc (GOOGL) Analyst Rating Update On October 24, 2023, Tigress Financial has maintained a "Strong Buy" rating for Alphabet Inc (GOOGL) while...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 349.82 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 341.80 (+2.3%), 50d 345.58 (+1.2%), 200d 337.50 (+3.7%); 50d above 200d
Momentum: RSI(14) 55.2 | MACD -0.299 vs signal -1.861 (histogram 1.562)
Returns: 1d +0.7% | 5d +3.3% | 1m +1.5% | 3m -4.9%
52-week range: 236.57 - 402.62 (now 68.2% of the way up)
Volatility: ATR(14) 8.40 (2.4% of price) | annualised 20d 23.3%
Volume: 0.89x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.28T
Valuation: trailing P/E 17.54 | forward P/E 23.55 | P/B 6.87 | PEG 1.23
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.3% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: strong_buy (mean 1.37 on a 1=strong buy to 5=strong sell scale, 53 analysts)
Ratings: 13 strong buy, 44 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 428.41 (+22.5% vs last close), range 340.00 - 515.00
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

### Nvidia (NVDA) · Company — BULLISH, confidence 0.55

**Result:** REJECTED · no room for equity NVDA under its 5% cap or the sleeve budget limit: equity 99819.45, price 219.45, existing exposure 5047.23, headroom 5502.85

**In the model's own words:**

> Fundamentals remain exceptional (106% revenue growth, 64% margins, forward P/E ~14, PEG 0.47) and consensus is strong_buy with ~50% upside to mean target. News flow is positive but largely commentary/roundups rather than a fresh catalyst; the Vera Rubin efficiency datapoint is mildly incremental. Technicals are neutral-to-soft: price hovering at the 20d SMA, MACD below signal, RSI ~52, volume 0.42x average — no momentum thrust. Insider net share count is distorted by grants; the only distinct actors are sellers (Director Stevens large sales), weak evidence. Net: modest bullish tilt on valuation/growth, not a high-conviction catalyst trade.

**Main reasons it gave:**
- Revenue +105.9% YoY, earnings +127.8%, forward P/E 13.99, PEG 0.47
- Mean analyst target 328.49, +49.7% vs last close; 58 analysts at strong_buy
- MACD below signal (-0.913 histogram), RSI 51.8, volume 0.42x average — no momentum confirmation
- Director Mark Stevens sold ~2.9M shares in early September; no distinct insider buyers
- News is mostly opinion pieces and 13F roundups, no hard ticker-specific catalyst

<details><summary><b>News</b> — score +0.25</summary>

- [NVIDIA (NASDAQ:NVDA): High-Growth Leadership and Strong Momentum](https://www.chartmill.com/news/NVDA/Chartmill-55023-NVIDIA-NASDAQNVDA-High-Growth-Leadership-and-Strong-Momentum)  
  <sub>ChartMill, 3 hours ago</sub>  
  NVIDIA clears every CANSLIM hurdle with 111% EPS growth, strong fundamentals, and leadership. See the full breakout setup, risks, and key levels.
- [Prediction: This Is Where Nvidia Stock Could Be by the End of Next Year](https://finance.yahoo.com/markets/stocks/articles/prediction-where-nvidia-stock-could-123059579.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  NVDA trades at just 23x forward earnings despite 106% revenue growth, and a 26x multiple on FY2028 EPS estimates puts the stock near $400.
- [Jensen Huang Calls Nvidia the "World's First and Only Growth Value Stock," Pointing to Its 70% Revenue Growth Forecast Next Year. Here's Why That Framing Matters for How Investors Price NVDA.](https://www.fool.com/investing/2026/09/18/jensen-huang-calls-nvidia-the-worlds-first-and-onl/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  Speaking at Goldman Sachs' Communacopia + Technology Conference on Sept. 10, Nvidia (NVDA +0.11%) CEO Jensen Huang highlighted a series of growth forecasts...
- [Why Is NVDA Stock Rising 3% Premarket Today?](https://stocktwits.com/news-articles/markets/equity/why-is-nvda-stock-rising-3-premarket-today/cZKffxCR7dY)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Nvidia Corp. shares rose about 3% in early premarket trading on Monday, joining a broader market rally after U.S. President Donald Trump and Iranian officials...
- [NVIDIA Corporation $NVDA Shares Acquired by Fischer Investment Strategies LLC](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-shares-acquired-by-fischer-investment-strategies-llc-2026-09-18/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Fischer Investment Strategies LLC grew its holdings in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 27.6% in the 2nd quarter, according to...
- [Are Nvidia shares a screaming buy – or do they scream AI bubble?](https://uk.finance.yahoo.com/news/nvidia-shares-screaming-buy-scream-151100591.html)  
  <sub>Yahoo Finance UK, 1 hour ago</sub>  
  Nvidia (NASDAQ: NVDA) shares aren't the growth monster they once were. The S&P 500 chip maker's stock is up an astonishing 869% over five years.
- [NVDA Stock Rises Premarket: Vera Rubin AI Accelerator Delivers 2X Profit Per GW Than Blackwell, Semianalysis Says](https://stocktwits.com/news-articles/markets/equity/nvda-stock-rises-premarket-vera-rubin-ai-accelerator-delivers-2-x-profit-per-gw-than-blackwell-semianalysis-says/cZtYaLHRB2m)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Nvidia's next-generation AI platform targets a key hyperscaler bottleneck: getting more AI output from every unit of power.
- [History Says This Will Happen to Nvidia's Stock in 2027 (Hint: You're Going to Want to Buy Now)](https://www.fool.com/investing/2026/09/17/history-says-this-will-happen-to-nvidias-stock-in/)  
  <sub>The Motley Fool, 22 hours ago</sub>  
  Nvidia (NVDA +0.04%) has been an OK performer in 2026. The stock is up about 17% year to date, modestly outpacing the S&P 500 (^GSPC -0.16%),...
- [James Investment Research Inc. Sells 2,845 Shares of NVIDIA Corporation $NVDA](https://www.marketbeat.com/instant-alerts/filing-james-investment-research-inc-sells-2845-shares-of-nvidia-corporation-nvda-2026-09-18/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  James Investment Research Inc. cut its holdings in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 1.5% in the second quarter, according to the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 219.39 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 218.73 (+0.3%), 50d 214.21 (+2.4%), 200d 198.36 (+10.6%); 50d above 200d
Momentum: RSI(14) 51.8 | MACD 0.559 vs signal 1.472 (histogram -0.913)
Returns: 1d +0.0% | 5d +0.5% | 1m +0.8% | 3m +4.1%
52-week range: 165.17 - 235.74 (now 76.8% of the way up)
Volatility: ATR(14) 6.29 (2.9% of price) | annualised 20d 46.3%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.80</summary>

```text
Sector: Technology / Semiconductors | market cap 5.30T
Valuation: trailing P/E 27.70 | forward P/E 13.99 | P/B 23.14 | PEG 0.47
Profitability: profit margin 63.7% | operating margin 66.2% | ROE 117.2%
Growth (YoY): revenue +105.9% | earnings +127.8%
Balance sheet: debt/equity 17.0% | free cash flow 41.81B
Risk: beta 2.22 | short interest 1.3% of float
Next earnings: 2026-11-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.80</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.80</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: strong_buy (mean 1.30 on a 1=strong buy to 5=strong sell scale, 58 analysts)
Ratings: 10 strong buy, 48 buy, 2 hold, 1 sell, 0 strong sell
Price target: mean 328.49 (+49.7% vs last close), range 180.00 - 515.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

```text
Last 180 days: bought 61,415,957 shares in 19 transaction(s) | sold 5,410,593 shares in 12
Net: +56,005,364 shares (+6.2% of insider holdings) | insiders hold 965,928,000 shares
Distinct insiders: 0 buying, 4 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-04 STEVENS MARK A (Director): 1,022,239 shares, 235.64M
  - 2026-09-02 STEVENS MARK A (Director): 1,848,501 shares, 410.84M
  - 2026-08-31 TETER TIMOTHY S (General Counsel): 30,000 shares, 6.54M
  - 2026-06-18 STEVENS MARK A (Director): 885,000 shares, 186.00M
(17 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### Teva Pharmaceutical (TEVA) · Company — BULLISH, confidence 0.52

**Result:** ACCEPTED · 1 shares · submitted buy 1 TEVA @ ~38.87, stop 36.63

**In the model's own words:**

> Strong intact uptrend: price near 52-week highs, above all major SMAs, positive MACD, RSI 61 (not yet overbought), +23.5% in 3 months. Valuation is supportive on forward numbers (fwd P/E 12.6, PEG 0.72, $2.2B FCF), though leverage is heavy at 218% D/E and revenue is flat. News flow is neutral-to-mildly-constructive: the debt offering reshapes the balance sheet but is not a fresh earnings catalyst, and the biosimilar-void story is sector-level. Recent Leerink Outperform initiation and 8% gap to the $42 target add mild support, but analyst coverage in this dataset is thin. Insider activity is net selling across 8 insiders with no buyers — weak evidence, but it removes any upside tilt. Light volume (0.27x) at highs argues for modest conviction rather than a high-conviction breakout call.

**Main reasons it gave:**
- Price 98% of 52-week range, above 20/50/200d SMAs with 50d>200d
- RSI 61.4 and positive MACD histogram, +23.5% 3-month return
- Forward P/E 12.56 and PEG 0.72 with $2.22B FCF, but D/E 218%
- Leerink initiated Outperform 2026-09-09; mean target $42 (+8.1%)
- 8 insiders selling, 0 buying over 180 days; volume only 0.27x 20-day average

<details><summary><b>News</b> — score +0.10</summary>

- [Halozyme Therapeutics, Inc. Announces Pricing of Upsized Private Offering of $1.3 Billion of Convertible Senior Notes due 2033](https://www.tradingview.com/news/prnewswire:a577966705f3d:0-halozyme-therapeutics-inc-announces-pricing-of-upsized-private-offering-of-1-3-billion-of-convertible-senior-notes-due-2033/)  
  <sub>TradingView, 13 hours ago</sub>  
  SAN DIEGO, Sept. 17, 2026 /PRNewswire/ -- Halozyme Therapeutics, Inc. (Nasdaq: HALO) ("Halozyme" or the "Company"), today announced the pricing of $1.3...
- [Looming biosimilar void risks $189B in lost U.S. healthcare savings: report](https://seekingalpha.com/news/4643986-looming-biosimilar-void-risks-189b-lost-healthcare-savings?source=generic_rss)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  A looming U.S. “biosimilar void” where there will be no off-patent versions for 90% of brand-name biologics could mean $189B in lost healthcare savings.
- [Alvotech (NASDAQ:ALVO) Given Average Recommendation of "Moderate Buy" by Brokerages](https://www.marketbeat.com/instant-alerts/consensus-alvotech-nasdaq-alvo-given-average-recommendation-of-moderate-buy-by-brokerages-2026-09-18/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Shares of Alvotech (NASDAQ:ALVO - Get Free Report) have been assigned a consensus rating of "Moderate Buy" from the eight research firms that are currently...
- [Teva Pharmaceutical Industries stock trades near recent highs as new debt offering reshapes balance](https://www.google.com/goto?url=CAESvQEB6zswFUb28winpE6Tdcn_hEmXSGIcnKWGfZcwLGdv2JVct34W9xTfsRzkuAt8UtnCuuEEXbltj7Hjzd5Co_lCTqk2ZCiNMC5Lp-AONbNg11qtuKPR9yLPCGiFfMTAjhL2UrEwleTDKR3Y-RHUlNGEvGlfiqJbaQBFSBmU1LU69W23cpGGxtzB30jRM5rG6-uIiz7TD17d5LIkbugIWhJgYGpFOT3n7LjCiSffVVF-L9UWhrpYxWgDkQduRwI)  
  <sub>AD HOC NEWS, 22 hours ago</sub>  
  Teva Pharmaceutical Industries stock is trading around USD 38.92 as of September 17, 2026, close to recent highs after a multi-billion senior notes offering...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.55</summary>

```text
Last close 38.87 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 37.43 (+3.8%), 50d 35.35 (+10.0%), 200d 33.15 (+17.3%); 50d above 200d
Momentum: RSI(14) 61.4 | MACD 0.840 vs signal 0.711 (histogram 0.130)
Returns: 1d -0.8% | 5d +4.8% | 1m +3.7% | 3m +23.5%
52-week range: 18.34 - 39.25 (now 98.2% of the way up)
Volatility: ATR(14) 1.12 (2.9% of price) | annualised 20d 32.1%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.33B
Valuation: trailing P/E 64.78 | forward P/E 12.56 | P/B 5.84 | PEG 0.72
Profitability: profit margin 4.1% | operating margin 4.0% | ROE 9.7%
Growth (YoY): revenue -0.8% | earnings n/a
Balance sheet: debt/equity 217.8% | free cash flow 2.22B
Risk: beta 0.80 | short interest n/a of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

_Not available today._

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

```text
Consensus: buy (mean 2.00 on a 1=strong buy to 5=strong sell scale, 1 analysts)
Ratings: 1 strong buy, 0 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 42.00 (+8.1% vs last close), range 42.00 - 42.00
Recent rating changes:
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
  - 2026-07-28 Piper Sandler: main, Overweight -> Overweight
  - 2026-05-06 Barclays: main, Overweight -> Overweight
  - 2026-04-30 JP Morgan: main, Overweight -> Overweight
Institutional ownership: 23.0%
Largest holders: Blackrock Inc. (5.5%), Harel Insurance Investments & Financial Services Ltd. (4.1%), Phoenix Financial Ltd. (3.7%), WCM Investment Management, LLC (3.5%), Clal Insurance Enterprises Holdings Ltd (3.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

```text
Last 180 days: bought 43,476 shares in 3 transaction(s) | sold 194,459 shares in 6
Net: -150,983 shares (-2.4% of insider holdings) | insiders hold 6,094,499 shares
Distinct insiders: 0 buying, 8 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-21 WEISS AMIR (Officer): 9,445 shares, 355.30K
  - 2026-08-03 HUGHES ERIC A (Officer): 25,578 shares, 892.05K
  - 2026-08-03 JOVER PLACID (Officer): 12,827 shares, 447.35K
  - 2026-06-11 KALIF ELIYAHU SHARON (Chief Financial Officer): 106,563 shares, 3.63M
(12 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### Caterpillar (CAT) · Company — NEUTRAL, confidence 0.45

**In the model's own words:**

> CAT presents a conflicted picture with multiple dimensions disagreeing meaningfully. On the bullish side: autonomous quarry expansion continues (material, ticker-specific), analyst consensus remains very bullish with 14 buy/strong-buy ratings and a $976 target (+21.6%), strong fundamentals show 68.2% earnings growth YoY with 22.2% operating margins and stellar ROE of 57.0%, and insider net buying of 41k shares over 180 days. The technical setup is not broken—price sits above the 200-day MA and RSI at 45.8 suggests room to run. However, conviction is heavily dampened by valuation and positioning concerns: trailing P/E of 34.52 on a stock that has already run 78% in one year, trading 56% of the way through its 52-week range after a -18.6% three-month drawdown, leaves minimal margin for surprise. Volume is 0.54x the 20-day average, suggesting thin conviction among buyers at these levels. The near-term technicals show a -2.0% five-day decline and price 4.5% below the 50-day SMA, indicating recent weakness. While news of the autonomous expansion is positive, it lands on an already richly valued stock with elevated expectations baked into a consensus that JPMorgan reaffirmed as Overweight just recently. The one-directional view would be bullish if valuation were moderate or if technicals were showing fresh momentum, but the combination of extended valuation, recent underperformance, thin volume, and consensus already very bullish points to limited near-term upside surprise. The gap between the current price and analyst targets incentivizes existing believers to hold rather than new money to enter. This is a hold-rated analyst setup on a fundamentally strong company, not a clear catalyst.

**Main reasons it gave:**
- Autonomous quarry expansion to two more Virginia quarries demonstrates organic technology adoption
- 68.2% YoY earnings growth and 22.2% operating margins show strong business execution
- Trailing P/E 34.52 after 78% one-year run leaves limited room for consensus-aligned surprises
- Price 4.5% below 50-day SMA with 0.54x volume suggests weak near-term momentum despite bullish view
- Analyst target of $976 is +21.6% but consensus already very bullish at 14 buy ratings

<details><summary><b>News</b> — score +0.35</summary>

- [Caterpillar's Robot Trucks Are Heading to Two More Quarries. Should You Buy the Dip Under $800?](https://247wallst.com/investing/2026/09/18/caterpillars-robot-trucks-are-heading-to-two-more-quarries-should-you-buy-the-dip-under-800/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  CAT sits at $799 with analysts targeting $976, though a 78% one-year run at a trailing PE of 34 leaves limited room for surprises. Power & Energy, not robot...
- [Red Cat and Unusual Machines Fall 3% as Drone Selloff Extends; Ondas Slips](https://finance.yahoo.com/markets/stocks/articles/red-cat-unusual-machines-fall-145714667.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  Small-cap drone stocks are sliding in lockstep again Friday while the broader market barely flinches, and the pattern behind the selloff tells a very...
- [Buy AI-Led EME, PWR and CAT for Long-Term to Gain From Recent Softness](https://www.tradingview.com/news/zacks:f7744c163094b:0-buy-ai-led-eme-pwr-and-cat-for-long-term-to-gain-from-recent-softness/)  
  <sub>TradingView, 5 hours ago</sub>  
  The artificial intelligence (AI)-powered data center industry is booming backed by an extremely bullish demand scenario. AI-led data centers are generating...
- [Learn Why The Bull Case For Caterpillar Stock Could Change Following Autonomous Quarry Expansion](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/descubre-por-que-las-perspectivas-alcistas-para-las-acciones-11)  
  <sub>Simply Wall Street, 14 hours ago</sub>  
  Luck Stone announced that its autonomous hauling partnership with Caterpillar is expanding to two more Virginia quarries, applying Caterpillar technology to...
- [Red Cat Holdings chairman & CEO sells $1.16m in stock](https://www.investing.com/news/insider-trading-news/red-cat-holdings-chairman--ceo-sells-116m-in-stock-93CH-4906650)  
  <sub>Investing.com, 13 hours ago</sub>  
  Jeffrey M. Thompson, Chairman of the Board and CEO of Red Cat Holdings, Inc. (NASDAQ:RCAT), sold 150,000 shares of the company's common stock on September...
- [Dow Ends Sees Worst Day In Over A Year, Nasdaq Enters Correction Territory As Fed Decision Piques Inflation Concerns — SPCX, CAT, ADBE, SOFI, HIMS Stock In Focus](https://www.google.com/goto?url=CAESwgEB6zswFWba07EN03qkdLPkECYd77MmLaDfIzmcVc6CeZvxbY-i5DMl8_vWpZ_AdGA3QfiMpAW-xRJCVES1JJfyYvwc0TdgHVz54NO1zvMiz9-3cbsD7woOOQIogG2YWDN8fNHDqftP6P-0AnLgVtgPlfhu8VkrBCnnyX1zjgXMeubGuk5VtK8QyNIhwRlv8np-H2KRogXvAzUOkmPHI6y6Ka22-jFWeFbVqsPsl7Y5JPOHiloBAHiwTigD09B2rM555w)  
  <sub>Stocktwits, 13 hours ago</sub>  
  U.S. equity futures were little changed on Wednesday as investors digested Microsoft, Meta and Qualcomm earnings and the Federal Reserve's decision.
- [Red Cat (NASDAQ: RCAT) CEO sells stock, lines up multimillion forward deal](https://www.stocktitan.net/sec-filings/RCAT/form-4-red-cat-holdings-inc-insider-trading-activity-a8efca4a9dab.html)  
  <sub>Stock Titan, 15 hours ago</sub>  
  Red Cat Holdings, Inc. (RCAT) insider Jeffrey M. Thompson, Chairman, CEO and more-than-10% owner, reported complex share transactions involving variable...
- [Caterpillar (CAT) Outpaces Stock Market Gains: What You Should Know](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-outpaces-stock-market-214508724.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Caterpillar (CAT) closed at $798.57 in the latest trading session, marking a +2.02% move from the prior day. The stock exceeded the S&P 500,...
- [Rockford’s Winnebago County Animal Services faces surge of 127 cats needing homes](https://www.mystateline.com/news/local-news/empty-shelters-event-rockford/)  
  <sub>MyStateline, 19 hours ago</sub>  
  Winnebago County Animal Services is set to reduce cat adoption fees starting Friday, Sept. 18, as part of the BISSELL Pet Foundation's Empty the Shelters...
- [Caterpillar offers faster growth, Coca-Cola pay...](https://pluang.com/en/news-feed/dividen-aristokrat-coca-cola-vs-caterpillar-untuk-roth-ira)  
  <sub>Pluang, 2 hours ago</sub>  
  Caterpillar and Coca-Cola are both Dividend Aristocrats with decades of dividend increases, but they serve different investor needs inside a Roth IRA.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 802.22 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 804.25 (-0.3%), 50d 840.00 (-4.5%), 200d 784.08 (+2.3%); 50d above 200d
Momentum: RSI(14) 45.8 | MACD -13.531 vs signal -15.270 (histogram 1.739)
Returns: 1d +0.5% | 5d -2.0% | 1m -1.7% | 3m -18.6%
52-week range: 463.72 - 1,064.90 (now 56.3% of the way up)
Volatility: ATR(14) 24.93 (3.1% of price) | annualised 20d 26.6%
Volume: 0.54x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.65</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 368.76B
Valuation: trailing P/E 34.52 | forward P/E 24.78 | P/B 19.01 | PEG 1.37
Profitability: profit margin 14.5% | operating margin 22.2% | ROE 57.0%
Growth (YoY): revenue +24.0% | earnings +68.2%
Balance sheet: debt/equity 232.8% | free cash flow 5.05B
Risk: beta 1.59 | short interest 1.8% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

```text
Consensus: buy (mean 2.14 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 13 buy, 12 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+21.6% vs last close), range 575.00 - 1,225.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.25</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.25</summary>

_Not available today._

</details>

### JPMorgan Chase (JPM) · Company — NEUTRAL, confidence 0.45

**In the model's own words:**

> JPMorgan shows mixed signals across dimensions with no clear catalyst dominating. The news flow is generic: an India conference, blockchain expansion, and banking partnerships are routine operational updates, not material catalysts. The dividend hike is positive but already reflected in consensus. On technicals, JPM is pullback-strained: the stock sits below both 20d and 50d SMAs (−2.2% and −1.9%), RSI is depressed at 40.7 with negative MACD histogram, and volume is 37% below average—all suggesting near-term weakness or consolidation, not directional conviction. Fundamentals are solid: 34.9% profit margins, 17.8% ROE, 46.9% earnings growth, and a reasonable forward P/E of 13.87 do not argue for a sell, but they do not constitute a fresh catalyst either. The analyst consensus remains constructively biased (mean rating 2.12, mean target +8.3%), yet no recent upgrades and no narrow target range tell us that view is already baked in. Insider activity is muddled: buying outweighs selling on a net basis by 7.7%, but the buying is transactional (grants/options excluded), while selling is routine (scheduled sales by officers, likely tax-driven), so the net signal is weak. The stock is near its 52-week high (77.3%) and has delivered +6.5% over three months, reducing the edge of mean-reversion bullishness. Earnings are not until 2026-10-13, so no event catalyst is imminent. The bank is not cheap or broken, but the technical pullback, flat momentum, and absence of a fresh catalyst argue against a high-conviction directional call over the next few days.

**Main reasons it gave:**
- RSI 40.7 and negative MACD histogram signal near-term momentum weakness
- Stock trading 2.2% below 20d SMA with volume 37% below average
- No recent analyst upgrades; consensus rating already priced in
- Strong YoY earnings growth (+46.9%) and ROE (17.8%) do not constitute fresh catalyst
- Generic news flow: India conference, blockchain rollout, routine partnerships—no material ticker-specific driver

<details><summary><b>News</b> — score +0.10</summary>

- [Nearly 1,200 delegates are expected at J.P. Morgan’s India conference](https://www.stocktitan.net/news/JPM/j-p-morgan-to-host-its-11th-india-conference-in-fv7nv7lrj96n.html)  
  <sub>Stock Titan, 6 hours ago</sub>  
  Delegates from over 100 companies and institutional investors are expected at the two-day Mumbai event, covering AI, manufacturing, capital flows and...
- [This J.P. Morgan ETF Targets High Income From US Stocks](https://www.google.com/goto?url=CAESkQEB6zswFe7Bid-Jrl30v3-PO-2uA4xVVC8sFUkhTCthc2USEPyK22YZAYUxXXk0AuvnpgnTdEsoHNQCHIpeGBtVjSsXpse19e4oDoaupqZebJxGoAQN4vZrpcVYOyKT1B0brQpIm8QvCsI0g0fDTCxUioEnNCUPFiZKH9xEWh-rfaoBJVkU3zM8FZIEH5w6xBcH)  
  <sub>Morningstar, 2 hours ago</sub>  
  The Gold-rated ETF uses covered calls to target 5%-8% income while cushioning losses in market downturns.
- [JPMorgan Chase (JPM) Expands Blockchain Banking And Lets Customers Invest Reward Points](https://www.google.com/goto?url=CAEStwEB6zswFYxeaH4Rgw06o8mhr8j_sua89M2LlWRg_gCq-l3h-g5X6yrSzNDVmItYA1yFEdorj9zCTtTPgRBuiKdE6Em3f3uPRX2Srm6D9AKqvFxkzsD8YSufKMuHXKQEb0B5Aao7C9A8ajCz23fnspwBjnPIbG2_6NiH9fbgRr_Rp2vLohMa6YeD_8mUzEajbRKXG3PBHukyISNO5MDpHLLl2T_hcX4w8M7VQ8p7dmgFca6dNVeEQ50)  
  <sub>Simply Wall Street, 2 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) is expanding its digital assets team to build blockchain-based banking tools for Chase customers. The bank is rolling out new...
- [JPMorgan Chase & Co. $JPM Stock Holdings Trimmed by Commerce Bank](https://www.google.com/goto?url=CAESsgEB6zswFcWvNbCepE-AL_xhzyODAguy1Yden_mNeuUz18zEbwd12ycvq4rSlp0qDe692s6w-fFT_7C4SN6K6CCczyCYp-THn1tzeBB_EnWIrVzMxVFnRLfkDIePiVqD8F7y_bziXJ1bNin-CXTqn3B4N1_pdlQMtQFAW_Gs_l0RHLZ4YLChoD5htJ70kTQldlANYzzDfEXJo1NmtIY3NsGxmNSr1iVT3H22dYVpZuR55lYt)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Commerce Bank reduced its stake in shares of JPMorgan Chase & Co. (NYSE:JPM) by 3.9% during the 2nd quarter, according to the company in its most recent...
- [Dividend Roundup: Microsoft, JPMorgan Chase, McDonald's, Broadcom, and more (VIG:NYSEARCA)](https://seekingalpha.com/news/4644272-dividend-roundup-microsoft-jpmorgan-chase-mcdonalds-broadcom-and-more)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Weekly dividend updates: Microsoft, JPM & McDonald's raise payouts; BMY and Kroger declare dividends; track next week's ex-div dates for META & AVGO—read...
- [JPM Looks 9.6% Overvalued on GF Value™ Amid Dividend Sustainabil](https://www.google.com/goto?url=CAESqAEB6zswFbV7jwWV34L7aNepXEMi61gp0cMeesZzazYwzYaYMef1cn_88T_F_ukXbWllvr6nf4VnTCxC17kcd38I0b0VGiG9gqqs-vMP6BChFhJrQfmVf6VrtLkzihoF83gAAL18Hczjs4egbMQWgoAFaQkcZgHJ1-r32wFnOdA8jIT887ar78383tiMfsKgTuPKoQUKDlh39eDpmzIo-RRzWHYGrpOL_dw)  
  <sub>GuruFocus, 1 hour ago</sub>  
  On September 18, 2026, JPMorgan Chase & Co. (NYSE: JPM) saw its stock price decline by $2.04 to approximately $347.27. Options trading remained steady with...
- [Watch 5 Stocks on Recent Dividend Hikes Amid Rising Rates & Volatility](https://www.tradingview.com/news/zacks:3e8cd094f094b:0-watch-5-stocks-on-recent-dividend-hikes-amid-rising-rates-volatility/)  
  <sub>TradingView, 5 hours ago</sub>  
  The U.S. economy continues to hold up well, despite various domestic and geopolitical challenges. Consumer demand remains a bright spot, with August retail...
- [JPMorgan, Banco Santander lead £1.1B loan for Drax's solar acquisition - report (JPM:NYSE)](https://www.google.com/goto?url=CAESqQEB6zswFXW4LJHfYh6hiNyejoXLytzAvxZwPfC97xOsqqtXbhzRCDP6yZGrtTV90s26fm2dHzZgI8OO1vqyLrWilIyGSczYgb7DHDI13ZKrVS7Bvltdsx8VHdPi5eSON-guf1YzN_twDcxvpk3i752yhx39TdejszF9xoRBxU0iOuZgE1GI45EO1kWNpMxuD-X_z7jfCWDSPzuXKFM_wHp-9BF7ENzsZsBS)  
  <sub>Seeking Alpha, 14 minutes ago</sub>  
  JPMorgan Chase (JPM) and Banco Santander (SAN) are leading a group of banks arranging debt financing of more than £1B to fund Drax Group's (DRXGF) (DRXGY)...
- [Quantbot Technologies LP Sells 15,174 Shares of JPMorgan Chase & Co. $JPM](https://www.google.com/goto?url=CAESugEB6zswFRanVXH-nYbbtLsYe4SmhaWouL7tH1dXJ6GfdZ_9MRx1_66Rh9wf_kASGbUv72FjdL9gSNDRwta14ToaWobcrkQTCzFwl9iWaMZDhRXavwQgrXa0FxpnWH39vzMVqvSwaXUkZE_bp_Ew0d56SvYmpCw1LBBaIs5UcID2fNu349jTqVLJuFtqZEVzKPizI-BpemuWX6_v7qlF5WqY1Gl-oae9Ufua0TtuX8USIrzBtnqiK5E_anw)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Quantbot Technologies LP lessened its stake in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 59.2% during the 2nd quarter, according to its...
- [Gabelli Funds LLC Sells 12,191 Shares of JPMorgan Chase & Co. $JPM](https://www.marketbeat.com/instant-alerts/filing-gabelli-funds-llc-sells-12191-shares-of-jpmorgan-chase-co-jpm-2026-09-18/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Gabelli Funds LLC decreased its holdings in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 4.1% during the 2nd quarter, according to the company...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 346.50 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 354.31 (-2.2%), 50d 353.14 (-1.9%), 200d 320.52 (+8.1%); 50d above 200d
Momentum: RSI(14) 40.7 | MACD -1.132 vs signal 0.261 (histogram -1.392)
Returns: 1d -0.8% | 5d -2.7% | 1m -3.0% | 3m +6.5%
52-week range: 282.84 - 365.18 (now 77.3% of the way up)
Volatility: ATR(14) 6.73 (1.9% of price) | annualised 20d 14.1%
Volume: 0.63x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 921.06B
Valuation: trailing P/E 14.85 | forward P/E 13.87 | P/B 2.61 | PEG 1.62
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.97 | short interest 1.0% of float
Next earnings: 2026-10-13
```

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

_Not available today._

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

```text
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 21 analysts)
Ratings: 4 strong buy, 9 buy, 10 hold, 0 sell, 1 strong sell
Price target: mean 375.38 (+8.3% vs last close), range 305.00 - 436.00
Recent rating changes:
  - 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-03 UBS: main, Buy -> Buy
  - 2026-07-20 Citigroup: main, Neutral -> Neutral
  - 2026-07-17 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-07-16 B of A Securities: main, Buy -> Buy
  - 2026-07-15 Baird: main, Neutral -> Neutral
Institutional ownership: 75.7%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

```text
Last 180 days: bought 969,320 shares in 22 transaction(s) | sold 230,669 shares in 20
Net: +738,651 shares (+7.7% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(22 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

_Not available today._

</details>

### Microsoft (MSFT) · Company — NEUTRAL, confidence 0.45

**In the model's own words:**

> MSFT presents a conflicted picture after a strong 31% run in three months that has brought the stock to 74.5% of its 52-week range. The analyst consensus remains very strong (mean 1.36, 52 analysts, 16.0% upside to $572.92 target), supported by tangible cloud demand, enterprise stickiness, and Azure growth evidenced by recent earnings beats. Fundamentals are solid with 31.7% YoY earnings growth, 40%+ profit margins, and 34% ROE. However, several dimensions argue for caution. Technically, momentum has rolled over: RSI at 53.1 is cooling from overbought, MACD has turned negative (-3.167 histogram), and the stock is down 0.8% on the day and only 0.8% below its 20-day SMA despite a +30% three-month move. Volume is only 0.51x average, suggesting the recent rally may lack conviction. The news backdrop is mixed: while distribution advantages and FY forecasts support a bullish case, copyright litigation risks from AI training data scraping have materialized with employee backlash, and a recent Seeking Alpha downgrade cites capex and margin pressures constraining the valuation at current levels. The valuation itself—27.48 trailing P/E, 8.29 P/B, 20.93 forward P/E—is elevated even for MSFT's quality, and one analyst has already hit their target and downgraded. Insider activity is neutral to slightly bearish: no distinct insiders bought in the past 180 days, while the CFO and CEO both sold in recent weeks (though these are likely routine, not conviction indicators). The stock is priced for continued acceleration into earnings on 2026-10-28, but technicals suggest short-term momentum exhaustion and the consensus is already fully reflected in the price. This is a quality name at a stretched entry after a powerful move, not a fresh catalyst.

**Main reasons it gave:**
- Strong analyst consensus with 16% upside already priced in
- Negative MACD histogram and cooling RSI despite 31% rally in three months
- Azure growth and earnings beats offset by capex/margin headwinds and valuation stretch
- Recent downgrade citing target hit and valuation concerns
- No insider buying in 180 days; CEO and CFO recent sellers

<details><summary><b>News</b> — score +0.30</summary>

- [Microsoft Corporation (MSFT) is Attracting Investor Attention: Here is What You Should Know](https://www.google.com/goto?url=CAESpwEB6zswFUts5NUQjLJWKtoJXaguMjri9KwbDuhPva3WOXas5y4y4FMRB8AnRgp2yay3Zg08LykC067d3Ye8cpz88iW_lflo4pSdkw_MxO0mebi5NGmuNXfLdKLhnt575wtQT6vhMzasOe5z8aahncHQ-_pBH68cg6zG5CDpst_nwonD0e-4GVzI539nqZwde1gzbd3vSEXlv5MbSfpw_cJX7cdyV5kjUA)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Microsoft (MSFT) has been one of the stocks most watched by Zacks.com users lately. So, it is worth exploring what lies ahead for the stock.
- [What Did Microsoft Tell You Before Its Stock Ran?](https://www.google.com/goto?url=CAESpQEB6zswFTmHcXvqMzEsh9OXeVzOFp-BlsFlgcBTNDGeptcdrv0p_T8zvMe4tvFrNk5RaGQd_iWXLAwq8BXY4Wa9Wtmzy50Q85F2DHRBbRk9iQx_2t0WGtdeTz4t4B2wuHreBS60i00AOkcoZHAcn3DFRtrhvGvK-1c6nS9XE-RwttLARx6JfJMk_jLYotk69IXNTAWbse-4wG6ID9WkRIGCSIAxvv8)  
  <sub>Trefis, 3 hours ago</sub>  
  Microsoft (MSFT) stock has returned about 32% since mid-June 2026. The S&P 500 returned about 3% over the same window, and peers moved in both directions:...
- [3 Reasons to Hold Microsoft Stock After a 31.2% Surge in 3 Months](https://www.google.com/goto?url=CAESzQEB6zswFZLCn-8RqMen80TN6DnbyFoxzh3Mg_tdOGFla1Zyau6TWXo1kpT_1kkFDUO4QK1pN7DfqfdY1yFHPh_MNaYS3OjFSa2go56fBG5mdpzz2GePSvZAcz0sNujwc3QX4EkStoEw4g4nX4_Lrm4Ggl-TVDVhFLa_U84kJB7lwILVGuAK6ghdn6JGVulxoUgHLk-a9lSuDsDCV9pCHDmHVYK84_lfA7xlqDAcTk-SEcJ2sqyvtdxe2o8esMDgpQbBHJT1NeQP1Lyg1PlP)  
  <sub>The Globe and Mail, 28 minutes ago</sub>  
  Detailed price information for Microsoft Corp (MSFT-Q) from The Globe and Mail including charting and trades.
- [Microsoft Stock Hit My Target. Now I'm Stepping Back (Rating Downgrade)](https://www.google.com/goto?url=CAESkwEB6zswFYcrfOQVS7UC7Da2nXVddUkXk92FdJ5or3bst6dH2OkFKFUDn-nv-v_SZpOI1KTD8IajubA6Fix9vTzJ71WkANX3M4bpkJ3odW3L0gM5JGYWgI9WxKg-GqOl89GHzcs3etfFfIJ8brvRfl4p8cTqYKIpsP8kB02mDrJu2IJWv7nbSuXcrk3KyCf1uVaepbo)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Microsoft Q4 earnings beat lifts MSFT near $500 on Azure growth and Copilot demand; capex and margins pressure valuation.
- [Microsoft AI copyright risks: What MSFT investors should know](https://www.google.com/goto?url=CAEShwEB6zswFV0HvuuEnvKPaRXySMDS6AQiKTPCPPI-k3Fm8NdqBOdCDdXqMJQl_oDu9VzlSZa7nPLaHIaZexYAUTIbYA6szmwTPAvRPyuia_93IeXQf9TuI0fwLwvGo3Zsh9pHPVbyKlvWNrgamQn7pICwGLNsmOWisbnE-5QjHWQyuaS2eafhW9s)  
  <sub>INDmoney, 3 hours ago</sub>  
  New AI scraping evidence raises copyright risks for Microsoft. See how lawsuits licensing costs and model restrictions could affect MSFT stock.
- [MSFT Looks 15.0% Undervalued on GF Value™ After Dividend Boost](https://www.google.com/goto?url=CAESmgEB6zswFSggdyT5rrIqUuF2WdL6br9znP91_9qRRGTt4B-ZG4E85GCUZZ0BF2sDEPNZEvv-dR6x7xK9YFz6ePRgPpnUUDZ6qdMayqDr5T621rW4L5thPuR75uEaAQm7B4NQZlUNzJDtxnXEStTMGQS2_InBBL6qA2hUQWoMf1uAjNmWVXQIEod1MOogjRJusLa2yCCeatAN99cy)  
  <sub>GuruFocus, 3 hours ago</sub>  
  On September 18, 2026, Microsoft Corp (MSFT) announced a dividend increase from $0.91 to $0.98 per share, representing a 7.7% hike.
- [Microsoft (NASDAQ: MSFT) EVP gets 29,077-share award vesting over four years](https://www.google.com/goto?url=CAESpAEB6zswFYi6u_JGYPhrZ1fQihrfccm5TAVNRXZ0MaFKRNa8CtWFyVfwe5ABwpwpZ1nPO7uSvghSH82COIXXn0g-8o8tC7sWC_vUp7MQAhNSH_l7rq9wfVNpOoo7zcgvCodV5TwTbm-vx7Xu7YtNHxfA7EKwln0oZoOVl_L4Y8AkXukcijp9vMegXI-lLXvj2WZRgqmDS2hFISSqA04WoTUKjuVDGQ)  
  <sub>Stock Titan, 18 hours ago</sub>  
  MICROSOFT CORP (symbol: MSFT) is the issuer of record for a Form 4 filing submitted to the SEC. Althoff Judson reported acquisition or exercise transactions...
- [Why Retail Traders Couldn’t Take Their Eyes Off These Stocks Last Week: AAPL, MU, MSFT, INFQ, RKLB](https://www.google.com/goto?url=CAES1gEB6zswFYZtIq0qAlQ6jJH6gl_ad05xkLnPtUWdzVAd3l036mKTzBlNL56U-FB_cszltgQG0bBdl8DmQV7E25LSrQH56p7Y_hG2zSHPA86huCIYKyC9JMWv3aa_zW2cHg1b5cucN6_SwU--xHtmwoTggX-TE8qShQJ0dInWJno3SUVDZYIqzHsbYKHVE4xYKecRdOzAS29QknmA5N4gHdX9YBi4G-XHmMBuV0OZQ77W2ju2R0Dg8VDmmWkRcjP38tfLW4HsujxpYRm8YouE0aP25dWxmO6n)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Consumer Hardware Under Pressure. Apple (AAPL) and Microsoft (MSFT) came under selling pressure after announcing price hikes across several flagship hardware...
- [Microsoft: Distribution Advantage Worth More Than Another Model Breakthrough (NASDAQ:MSFT)](https://www.google.com/goto?url=CAESrAEB6zswFdlboiLTq2CJvcfJdK5BnmqLYXZBe6nWZzWBslVkbNzf3hv1YhlhqlfZblkHAZgkjybJiFJZMlUKac8T31Nl8w3B3OCUmdpYATz5tZMwhASowhbG8AwgkFh5mEJBwPcD6Qh3-xmbFpWCfyL2yKGsKSFRkJfdDCi8t5KVBlol4bUBgaBGNyupA8PnAtnas-Bd3jHq0iNI7JbkCY8d3Hp1YuSjhCrjHa3F)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Bullish Microsoft (MSFT) outlook: cloud demand, enterprise stickiness, and FY forecasts ($390B rev, $19.30 EPS).
- [Microsoft and OpenAI face internal backlash ove...](https://www.google.com/goto?url=CAESmwEB6zswFVhlpjt5shFuIVkYaCSipEvm8vjsaHfYZBGgQJ90XqO7_93z7_QAcLghBJYlJ2TaJs_ra4bmkqf44boMlXfOaFrhQV98rN2g6xEXi7WHo3DZYj5fbNBZdLnlAW_xy9QIdTRvuZGakiub9s_E2ea5NTq_RFN0O9nq8XqMTl2JDCjIYAcXXKCHT3iiCzOyLsUeMc9hO4S2Dg)  
  <sub>Pluang, 2 hours ago</sub>  
  Internal documents reveal that Microsoft and OpenAI employees privately criticized the use of millions of news articles to train AI models,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 493.74 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 497.51 (-0.8%), 50d 464.68 (+6.3%), 200d 431.60 (+14.4%); 50d above 200d
Momentum: RSI(14) 53.1 | MACD 6.846 vs signal 10.014 (histogram -3.167)
Returns: 1d -0.8% | 5d -0.4% | 1m +1.9% | 3m +30.1%
52-week range: 352.83 - 542.07 (now 74.5% of the way up)
Volatility: ATR(14) 10.62 (2.2% of price) | annualised 20d 22.0%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.67T
Valuation: trailing P/E 27.48 | forward P/E 20.93 | P/B 8.29 | PEG n/a
Profitability: profit margin 40.3% | operating margin 45.1% | ROE 34.0%
Growth (YoY): revenue +17.7% | earnings +31.7%
Balance sheet: debt/equity 29.1% | free cash flow 16.55B
Risk: beta 1.11 | short interest 1.0% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

```text
Consensus: strong_buy (mean 1.36 on a 1=strong buy to 5=strong sell scale, 52 analysts)
Ratings: 14 strong buy, 38 buy, 3 hold, 0 sell, 0 strong sell
Price target: mean 572.92 (+16.0% vs last close), range 400.00 - 870.00
Recent rating changes:
  - 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - 2026-09-04 Stifel: main, Hold -> Hold
  - 2026-09-01 B of A Securities: main, Buy -> Buy
  - 2026-08-12 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-05 Tigress Financial: main, Buy -> Buy
  - 2026-07-30 Bernstein: main, Outperform -> Outperform
Institutional ownership: 75.8%
Largest holders: Blackrock Inc. (8.2%), Vanguard Capital Management LLC (6.5%), State Street Corporation (4.2%), Geode Capital Management, LLC (2.5%), FMR, LLC (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.05</summary>

```text
Last 180 days: bought 513,644 shares in 16 transaction(s) | sold 242,344 shares in 9
Net: +271,300 shares (+4.2% of insider holdings) | insiders hold 6,757,246 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-14 HOOD AMY E (Chief Financial Officer): 41,674 shares, 20.76M
  - 2026-09-01 NADELLA SATYA (Chief Executive Officer): 86,525 shares, 43.39M
  - 2026-08-05 ALTHOFF JUDSON (Officer): 10,000 shares, 4.88M
  - 2026-08-04 NUMOTO TAKESHI (Officer): 4,810 shares, 2.39M
(15 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.05</summary>

_Not available today._

</details>

### ASML (ASML) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is mostly roundups and rehashes with no fresh ticker-specific catalyst; the High NA order commentary is positive but incremental. Technicals are soft — price below 20d and 50d, MACD negative, 3m -14.5%, thin volume — while fundamentals are strong (21% revenue growth, 54% ROE, low leverage) and analyst consensus is strong buy with ~29% upside. Conflicting dimensions plus earnings on Oct 14 argue for a neutral stance with modest conviction; no insider transactions is simply no information.

**Main reasons it gave:**
- Price -4.2% vs 50d SMA, MACD histogram -7.5, RSI 45
- 3-month return -14.5% despite 50d above 200d
- Revenue +21.3% YoY, earnings +28.5%, ROE 53.9%, D/E 9.1%
- Consensus strong_buy, mean target +29.4% above last close
- News flow dominated by generic listicles and sector roundups
- No insider transactions in 180 days

<details><summary><b>News</b> — score +0.15</summary>

- [3 Stocks to Buy as an Analyst Sees Semiconductor Spending Surging 88%](https://www.fool.com/investing/2026/09/18/stocks-buy-analyst-semiconductor-spend/)  
  <sub>The Motley Fool, 6 hours ago</sub>  
  SK Hynix, Nvidia, and ASML all look like top stocks to own as chip sales are set to soar.
- [ASML Rides on Strength in Installed Base Business: Will it Sustain?](https://www.tradingview.com/news/zacks:6200236e6094b:0-asml-rides-on-strength-in-installed-base-business-will-it-sustain/)  
  <sub>TradingView, 3 hours ago</sub>  
  ASML Holding N.V. ASML is benefiting from strong momentum in its Installed Base Management business. Semiconductor manufacturers are aiming to boost the...
- [Eisman Says Buy Micron And SK Hynix. “In This Knife Fight You Want To Be The One Selling The Knives”](https://finance.yahoo.com/markets/stocks/articles/eisman-says-buy-micron-sk-143852701.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>
- [Did High NA Orders Just Shift ASML's (ENXTAM:ASML) Investment Narrative?](https://simplywall.st/stocks/nl/semiconductors/ams-asml/asml-holding-shares/news/did-high-na-orders-just-shift-asmls-enxtamasml-investment-na)  
  <sub>Simply Wall Street, 7 hours ago</sub>  
  Samsung, TSMC, Intel and others have committed to ASML Holding's High NA EUV systems, while ASML prepares major EUV capacity expansion supported by new...
- [ASML Holding stock gains as chip outlook and Q2 2026 figures impress](https://www.ad-hoc-news.de/boerse/news/corporate-news/asml-holding-stock-gains-as-chip-outlook-and-q2-2026-figures-impress/70125009)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  ASML Holding stock rose around 1.6 percent on September 18, 2026 as chipmakers led a rebound and investors focused on strong Q2 2026 results.
- [Top 10 European Stocks to Watch Today — The Companies With Momentum Behind Them](https://europeanbusinessmagazine.com/top-10-european-stocks-to-watch-today/)  
  <sub>European Business Magazine, 8 hours ago</sub>  
  The top European stocks to watch today, including ASML, Siemens Energy, Schneider Electric and Rolls-Royce, and the trends.
- [Chasing ASML’s Dominance: Canon and Nikon Are Doing Something The Market Misses](https://247wallst.com/investing/2026/09/17/chasing-asmls-dominance-canon-and-nikon-are-doing-something-the-market-misses/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  ASML just dominated another quarter, but Canon and Nikon are quietly carving out a position in chip manufacturing that Wall Street's models barely account...
- [ASML Gains 1.5% as 110 EUV Machines Test Assembly Speed](https://finance.yahoo.com/markets/stocks/articles/asml-gains-1-5-110-183616992.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>
- [European shares rise as oil slips, yields stall](https://kwsn.com/2026/09/17/european-shares-rise-as-oil-slips-yields-stall/)  
  <sub>KWSN, 15 hours ago</sub>  
  Sept 17 (Reuters) - European shares edged higher on Thursday, with risk sentiment getting a lift as crude oil prices continued ​to fall and a global bond...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 1,649.24 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 1,687.86 (-2.3%), 50d 1,721.54 (-4.2%), 200d 1,509.32 (+9.3%); 50d above 200d
Momentum: RSI(14) 45.2 | MACD -31.519 vs signal -24.057 (histogram -7.463)
Returns: 1d +1.2% | 5d -2.9% | 1m -5.9% | 3m -14.5%
52-week range: 927.80 - 1,989.44 (now 68.0% of the way up)
Volatility: ATR(14) 54.17 (3.3% of price) | annualised 20d 38.2%
Volume: 0.52x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.55</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 633.47B
Valuation: trailing P/E 56.23 | forward P/E 27.80 | P/B 1,405.91 | PEG 1.46
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.36 | short interest 0.4% of float
Next earnings: 2026-10-14
```

</details>

<details><summary><b>What this fund holds</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

```text
Consensus: strong_buy (mean 1.40 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 7 strong buy, 31 buy, 3 hold, 1 sell, 0 strong sell
Price target: mean 2,134.44 (+29.4% vs last close), range 887.61 - 2,842.27
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 3,414,222 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Exxon Mobil (XOM) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is mostly soft: Venezuela re-entry talks are early-stage and speculative, a refinery outage is mildly negative for volumes but supportive for crack spreads, and most items are roundups or comparisons. Technically the name is mid-range, RSI 52, MACD rolling over slightly, near 20d SMA and 86% up the 52-week range on thin volume — no timing edge. Fundamentals are solid (low leverage, 20.7B FCF, strong YoY growth on a high oil-price base) but forward P/E 15 with the stock near highs and only ~5% upside to consensus target leaves little asymmetry; a recent BofA downgrade offsets the buy skew. Insider data shows aggregate share counts with zero distinct buyers or sellers, likely plan/trust noise rather than a real signal. No single catalyst justifies a directional call in the next few days.

**Main reasons it gave:**
- Venezuela re-entry talks early-stage and non-binding
- Price target mean 170.91, only +4.9% above last close
- MACD histogram negative (-0.307) with RSI 52 and 0.46x volume
- Strong balance sheet: D/E 15.9%, FCF 20.7B, forward P/E 15.1
- BofA downgrade to Neutral (Jul 28) against 15 hold ratings

<details><summary><b>News</b> — score +0.15</summary>

- [ExxonMobil Is Reportedly Nearing a Deal to Invest in Venezuela's Oil Fields. Is XOM Stock a Buy?](https://www.fool.com/investing/2026/09/18/exxonmobil-is-reportedly-nearing-a-deal-to-invest-in-venezuelas-oil-fields-is-xom-stock-a-buy/)  
  <sub>The Motley Fool, 6 hours ago</sub>  
  That would be quite a splashy return for the company, which exited the country in 2007.
- [Chevron vs. Exxon: Which Dividend Survives the Downturn](https://247wallst.com/investing/2026/09/18/chevron-vs-exxon-which-dividend-survives-the-downturn/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Chevron (CVX) yields 3.07% versus Exxon's (XOM) 2.57%, but Exxon's 56x interest coverage and 0.548 net debt/EBITDA make its dividend far more durable.
- [Exxon Mobil CFO warns of hidden risks behind oil supply shock](https://www.sacbee.com/news/business/article317289166.html)  
  <sub>Sacramento Bee, 16 hours ago</sub>  
  Oil prices have been on a wild ride this year, and most investors assume the story is simple: Less crude moving through the Strait of Hormuz means higher...
- [ExxonMobil Highlights Refining Capacity Challenges Amid Oil Pric](https://www.gurufocus.com/news/9087740/exxonmobil-highlights-refining-capacity-challenges-amid-oil-price-fluctuations-xom)  
  <sub>GuruFocus, 6 hours ago</sub>  
  On September 18, 2026, ExxonMobil Holdings Corp (XOM) addressed significant challenges in the energy sector, particularly focusing on refining capacity...
- [Is ExxonMobil (XOM) Rewriting Its Global Oil Play With Venezuela And Vietnam?](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings/news/is-exxonmobil-xom-rewriting-its-global-oil-play-with-venezue)  
  <sub>Simply Wall Street, 20 hours ago</sub>  
  ExxonMobil Holdings (NYSE:XOM) has begun talks with Venezuelan authorities about potential investment terms for reentering the country's oil sector.
- [Exxon’s 11 Million-Gallon Refinery Goes Dark. How High Can Midwest Gas Prices Go?](https://247wallst.com/investing/2026/09/18/exxons-11-million-gallon-refinery-goes-dark-how-high-can-midwest-gas-prices-go/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Gasoline and diesel prices were already moving higher before a floodwater-overwhelmed pump forced Exxon Mobil (NYSE:XOM | XOM Price Prediction) to keep its...
- [Exxon Sees Power Demand Exploding 65% By 2050](https://www.benzinga.com/markets/large-cap/26/09/61868772/exxon-sees-power-demand-exploding-65-by-2050)  
  <sub>Benzinga, 3 hours ago</sub>  
  Exxon predicts 2050 global power demand will jump 65%, with oil and gas continuing to supply over half of the world's energy.
- [Can Strong Oil Prices Drive ExxonMobil's Business Growth?](https://www.globes.co.il/en/zarticle.aspx?id=2991552)  
  <sub>גלובס, 10 hours ago</sub>  
  WTI near $100 and low-cost production in the Permian and Guyana could support XOM's earnings as drilling and AI boost output efficiency.
- [Energy Stocks And Industry News: Oil, Gas, Solar, Coal And Nuclear Energy](https://www.investors.com/news/oil-gas-stocks-industry-news-oil-prices-opec-exxon-haliburton-schlumberger-chevron-continental-resources/)  
  <sub>Investor's Business Daily, 23 hours ago</sub>  
  Track the latest news, trends and analysis on oil stocks and energy industry news.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 162.96 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 162.63 (+0.2%), 50d 157.77 (+3.3%), 200d 146.90 (+10.9%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD 1.886 vs signal 2.193 (histogram -0.307)
Returns: 1d -0.2% | 5d -1.8% | 1m -1.1% | 3m +18.2%
52-week range: 110.64 - 171.47 (now 86.0% of the way up)
Volatility: ATR(14) 3.63 (2.2% of price) | annualised 20d 25.9%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 669.99B
Valuation: trailing P/E 20.97 | forward P/E 15.10 | P/B 2.58 | PEG 1.40
Profitability: profit margin 9.1% | operating margin 15.9% | ROE 12.6%
Growth (YoY): revenue +44.1% | earnings +112.8%
Balance sheet: debt/equity 15.9% | free cash flow 20.67B
Risk: beta 0.17 | short interest 1.1% of float
Next earnings: 2026-10-30
```

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: buy (mean 2.32 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 3 strong buy, 7 buy, 15 hold, 0 sell, 0 strong sell
Price target: mean 170.91 (+4.9% vs last close), range 142.00 - 200.00
Recent rating changes:
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
  - 2026-08-17 Barclays: main, Overweight -> Overweight
  - 2026-08-07 TD Cowen: main, Buy -> Buy
  - 2026-08-04 Freedom Broker: up, Sell -> Hold
  - 2026-07-28 B of A Securities: down, Buy -> Neutral
Institutional ownership: 67.1%
Largest holders: Blackrock Inc. (8.1%), Vanguard Capital Management LLC (6.5%), State Street Corporation (5.0%), FMR, LLC (3.3%), Vanguard Portfolio Management LLC (2.8%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 10,818,651 shares in 251 transaction(s) | sold 3,904,152 shares in 49
Net: +6,914,499 shares (-194.8% of insider holdings) | insiders hold 3,371,767 shares
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

**In the model's own words:**

> Elbit Systems filed a two-year shelf prospectus in Israel today, enabling future fundraising flexibility. This is a corporate action, not a new contract or catalyst; shelf filings are routine and do not signal imminent capital raises or management confidence in near-term valuation. The defense backlog of $32B is material to the business but is pre-existing context already reflected in analyst consensus. Technicals are mixed: the stock trades 2.5% above its 20-day MA but 3% below both 50d and 200d, with the 50d below the 200d signaling weakness. RSI is neutral at 49.7, MACD histogram is positive but still below signal, and volume is thin at 0.21x average—all consistent with indecision. Momentum over 1m and 3m is negative, and the stock is only midway through its 52-week range. Fundamentals are solid: revenue growth of 15.9% YoY, earnings growth of 34.2%, and free cash flow turned negative recently (-$38.48M), which warrants scrutiny. Valuation at 55.5x trailing P/E and 40.2x forward P/E is elevated for a defense contractor, even with strong growth; P/B of 7.84 is rich. Analyst consensus is hold with a mean target of $816.33 (+10.5%), but 5 of 6 analysts rate it hold with only one buy and no strong convictions—this reflects caution already baked in. Insider activity in April showed four officers and the CEO selling (25.5k shares by the CEO on 2026-04-09 for ~$22.6M), typical of scheduled vesting or diversification but not bullish; recent buying activity is minimal. The shelf filing is neutral procedural news with no material catalyst timing. Conflicting signals—solid growth and backlog offset by rich valuation, thin technicals, and lukewarm analyst sentiment—argue for a neutral stance with modest conviction.

**Main reasons it gave:**
- Shelf prospectus filed is routine corporate action, not a catalyst or confidence signal
- $32B defense backlog is pre-existing context already in consensus
- Trailing P/E 55.5x and forward 40.2x are rich despite 34% earnings growth
- Technicals show 50d below 200d with thin 0.21x volume, neither bullish nor decisively bearish
- Analyst consensus is hold with only 1 of 6 buy-rated, mean target +10.5% offers modest upside already reflected

<details><summary><b>News</b> — score +0.00</summary>

- [A defense technology company may raise money in Israel for two years. No offering is certain from Elbit Systems.](https://www.stocktitan.net/news/ESLT/elbit-systems-files-a-shelf-prospectus-in-chkymn4ujtls.html)  
  <sub>Stock Titan, 7 hours ago</sub>  
  Elbit Systems (ESLT) has filed a two-year shelf prospectus with the Israel Securities Authority and the Tel Aviv Stock Exchange, enabling potential...
- [Defense backlog hits $32B as Elbit Systems (NASDAQ: ESLT) sets up new Israeli funding shelf](https://www.google.com/goto?url=CAESqQEB6zswFX3JEnqsvxBvdS0A_movjXiv1qDPaQn1AHxdCYIQ8Ha3TPBfOqrOxORe6X75xiYlISE8P_YettNOR26OQM3f9qXhHtQcfR59oxBuk3H3gfxqCmu2b4Bxi8CcEjNkgAzb91mUzQLoayofGCRq-ZMWx1Rvr4wTEEYWEaOY8ZksrK-h6PMxilRXECpBab-7l5f0FokqfBnsW_UBeD3xvqvEKIljaNBv)  
  <sub>Stock Titan, 6 hours ago</sub>  
  Elbit Systems Ltd. (ESLT) has filed a two-year shelf prospectus in Israel with the Israel Securities Authority and the Tel Aviv Stock Exchange.
- [Elbit Systems Files a Shelf Prospectus in Israel](https://www.google.com/goto?url=CAESowEB6zswFRpqStSZsj0JlfAdYnSc6levvOh4y9nWm9tWegU23E9nYCxnmoOzu8bwfyJ-5NhE1n4mHS2sq7griFyPHspnLOqQr4x7GLF7xnCWsR4RpsLdf8xsqLOkJIhoIFHSK2EDjiBbr7OlunKEsflH4kaS75wAhCl0nnKu0hKT9g6669Cng6H1Wqrj2K1RIfQ5KIeBBclWm5wKPOdFW5HfoGsw)  
  <sub>PR Newswire, 9 hours ago</sub>  
  PRNewswire/ -- Elbit Systems Ltd. (NASDAQ: ESLT) (TASE: ESLT) ("Elbit Systems" or the "Company") announced today that it has filed a shelf prospectus with...
- [Elbit Systems Files Two-Year Shelf Prospectus in Israel to Boost Fundraising Flexibility](https://www.tipranks.com/news/company-announcements/elbit-systems-files-two-year-shelf-prospectus-in-israel-to-boost-fundraising-flexibility)  
  <sub>TipRanks, 6 hours ago</sub>  
  Elbit Systems ( ($IL:ESLT) ) has provided an announcement. On September 18, 2026, Elbit Systems filed a two‑year shelf prospectus with the Israel Securities...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 738.96 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 721.20 (+2.5%), 50d 762.08 (-3.0%), 200d 762.43 (-3.1%); 50d below 200d
Momentum: RSI(14) 49.7 | MACD -8.172 vs signal -14.462 (histogram 6.291)
Returns: 1d -1.3% | 5d +1.5% | 1m -1.8% | 3m -6.3%
52-week range: 454.95 - 1,014.33 (now 50.8% of the way up)
Volatility: ATR(14) 16.62 (2.2% of price) | annualised 20d 15.7%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.63B
Valuation: trailing P/E 55.48 | forward P/E 40.24 | P/B 7.84 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
Next earnings: 2026-11-24
```

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.05</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+10.5% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

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

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### HDFC Bank (HDB) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed picture: a securities class action notice and CEO succession uncertainty are mild negatives, but both are low-substance/known items. Price sits near 52-week lows with 50d below 200d (downtrend) yet MACD is turning up and RSI is neutral at 50.5 on very thin volume (0.37x). Fundamentals remain solid (16-18% revenue/earnings growth, 26.8% margins) though P/B 9.2 is rich, and analysts see +33% to target with no fresh rating action. No insider transactions in 180 days — neutral, not bearish. Nothing here is a tradable catalyst for the next few days.

**Main reasons it gave:**
- Securities class action notice filed (Levi & Korsinsky) plus CEO succession weighing on sentiment
- Price 8% off 52-week low, 50d SMA below 200d, -16.6% vs 200d
- MACD histogram turned positive, RSI 50.5, volume only 0.37x 20d average
- Revenue +16.6% / earnings +18.1% YoY, 26.8% profit margin, but P/B 9.2
- Consensus buy with mean target 30.77 (+33%), no rating changes since 2024
- Zero insider transactions in past 180 days

<details><summary><b>News</b> — score -0.20</summary>

- [HDB Shareholder Alert: Investors With Losses May Seek to Lead the Class Action in HDFC Bank Limited Securities Lawsuit - Contact Levi & Korsinsky](https://www.google.com/goto?url=CAESgAIB6zswFaph9HAtxy6coDsFvzbUPF1mlI11FJ3HmG0YQaD80bBh6EfzBOlxQyIfl_Fx5mvwtVCxJm7qhiDwf697vTpqpge8oWe4HViB_TrtrRz_XvOkKAtgZJylUynDmjRIvftx0DjhcCCvnB3nHqfsRPHF6_UmIPm7bpd4yjnbtfGYlavBRcK9yHk8PceMBJxwl3fYcKHqq60RncFvEn7Pn8L1KRrbC72chE3Z09tSMK-YCtVVXT370SYUMS0c1MiOj6CUtZPbabecdeGFjdIyG9Vj5cKUHlAx3nPif_Ey2KXSXQcisV0xYVXu9xVhKlx-xZdgxx7uayGghE5a89Tz)  
  <sub>Business Wire, 2 hours ago</sub>  
  Levi & Korsinsky, LLP notifies investors in HDFC Bank Limited (NYSE: HDB) that a securities class action has been filed on behalf of shareholders who...
- [Squarepoint Ops LLC Sells 873,163 Shares of HDFC Bank Limited $HDB](https://www.google.com/goto?url=CAEStQEB6zswFXxRrjyShnnDRmcyJeKt0W6EltwW4ruYlZ709BER0Fogf9ujwPfCZ6FHEuC-cx3ST2Gn2frgvEtq5ka7ip7GEzec9DU6JFkSGlBy_Z76WWQq2YHYclThCpirr3OUnqSb62Ms8jh8Hj-DWonw5d8sqQi38A3Fb1aKquQuG4Pvvm043aFVGb23AQaPxpB31EdARf_n2DIQ7TVT6tnTWWDNZsxrWPuCuoSSKHcq4XGjqL6R)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Squarepoint Ops LLC cut its position in shares of HDFC Bank Limited (NYSE:HDB - Free Report) by 96.0% during the second quarter, according to the company in...
- [Tidal Investments LLC Takes Position in HDFC Bank Limited $HDB](https://www.google.com/goto?url=CAESsgEB6zswFZ-s7MWmV16W_jp-TvNV9BPVDE-eNUSZ-ZD5tEAKpIC7331IRyk7sDYhHHUjrpVE9ek2M29r2dkqAj3xq9Y5JP6RYIkWuPG21f7Tx0cqTACII9bxqi7OiaLRHKtoN3WiZyDEgXmEOMcZ0zEDCy6RZoe-22BkqU4px6VXNlasUwa2CqUgLqLP8C34S8mKdDYGNikaRGZnZxQjQW9YR9qmkJ1HZNMjwXtL25S5PUyC)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Tidal Investments LLC purchased a new stake in HDFC Bank Limited (NYSE:HDB - Free Report) in the second quarter, according to the company in its most recent...
- [SMPL Investor Alert: The Simply Good Foods Company Securities Class Action Notice - Contact Levi & Korsinsky](https://www.google.com/goto?url=CAES2wEB6zswFaFuc3-xjv8-Y-Kxd1qa_05-m8N4KTnZsXSzYAaLQcRfS6COsEb9FLuAtqyMOJnBPkt5QwAc8SvnsBl49Ic4ZtYY1dWrt2VU4UikAJH67qNBuu-qyTJyOjnCsWaYDFgob1m7x2LTROyW5-wOpkybB3XrsG0NR86Ys_nzzpx5cQZzrRs8hZ7WSrdObsqaa1IANHDTywADx6kYs-0w2rnJ7E-hFZLIVh79GkPjpfeK3KjHcmbALwAXYWYEHzUGC35TpzCupSVcTyzoV1E5ac7HDbaZFyiQepo)  
  <sub>Business Wire, 2 hours ago</sub>  
  Levi & Korsinsky, LLP notifies investors in The Simply Good Foods Company (NASDAQ: SMPL) that a class action has been filed on behalf of shareholders who...
- [Mutual funds get back losses and more as stock market rebounds](https://www.google.com/goto?url=CAESogEB6zswFX_oGb5sY2RW4P4BtvnYUuTKixngpZ53Qr9r8Pj_3HZD0SI4ouQVZzNQr56tuhULt9uuZqIB6sr0HsGIdgXuR552Z3i7u_3J1SwcXM_pBTXoKhKAkmnZ2DH50LBaZVi58er6yt1G5sI6D-E8OnSP87gMtlCQRdYyk0cZK3uaQXYnwPRPzHaQWW4aLZzsTi3rLRFG6GzofMawnP5DFNw)  
  <sub>vietnamnews.vn, 15 hours ago</sub>  
  Open-ended equity funds benefited from the strong recovery in the benchmark VN-Index in August, with some posting monthly gains of more than 10 per cent,...
- [NYSE Composite (NYA) Index Price Live | NYSE](https://www.google.com/goto?url=CAESZAHrOzAVjuETFVjpkJEKJIOjkiNR2IPSp2gMwKfmgAzr4nB1WWMVDoZapZZnlm6wBIvK0CKOzlfcuCH2_BKcoqzDUyNaOafPP8uq4DlYMg6qutH4P5X-bE4cLsYm9rh4I1z8kOI)  
  <sub>TechGraph, 10 hours ago</sub>  
  New York Stock Exchange Building · United States · Founded 17 May 1792. The New York Stock Exchange (NYSE, nicknamed "the Big Board") is an American stock...
- [Stock market on September 18th: VN-Index unexpectedly reverses direction at the end of ATC session](https://www.google.com/goto?url=CAESpQEB6zswFUODAqN8qViR62v9zRkQfFYl51Ztz-pTRfXCsGWOqOV_el1aPy4kDuXq-VXAUpFHdQ7ck1vkSuz2pc9fUH2MIzL8vbwvehOKjhWWCIuTNesSz4-ocrns6Lg3mfhFUIS4IMgvlDFGe36WFDgX9pKJKtOFKATpWB_zBJQBZmmhl4Euqpn9ELowQOyqOvkDbCXLkUS9Go7y15AtnWMg0b4nj_Q)  
  <sub>Laodong.vn, 7 hours ago</sub>  
  The stock market unexpectedly turned down when ETF funds restructured their portfolios.
- [These large- and mid-cap stocks with ‘Strong Buy’ & ‘Buy’ recos have upside potential of up to 25%, according to analysts](https://www.google.com/goto?url=CAES8wEB6zswFcuKW3bmilUrFVknrbziNUeGy3AUdN4LIsCoZX2FOyStLjl-4YfEm8nS1G1QlJNRl6-rEzkUCHJrbTYwsRLygWclI5I8dG0U2pEL-_vafZ4dqt2PmoItJO0wO17eqkhPHvALdFIAd-hnrDCt5WMHrBnKd_2A83W4RI8yHepdaZkb7w_CGUFsBI5CP_cLoFSC3sWpOhUdWxs9kG8u_jDv97caa4GFdurbKy0T91c1LHSW--1jx8QUrxFNagfQSrLcg6kAcShvTO7cckQd5K32K-dtL79r1_uzgNjuBe19r15X_IGfT5AB8bLnsZdM-ss)  
  <sub>The Economic Times, 8 hours ago</sub>  
  Talk of tariffs, especially steep ones, makes the market nervous. Which is exactly why the next few trading sessions are critical, and why being in a hurry...
- [Neighbourhood retailers can apply for grace period to sell non-BCRS Return Right-labelled drinks until Oct 31](https://www.google.com/goto?url=CAESdQHrOzAVQv_ya7dOwAbBz1CyX-_liwM6glE8B6ciLAw-er66_CT_BoYAjEFZULt40PzHRssoc3ZPXQ5p_CqfUVm56SQKWQQ6spSHVUOz-689URg1tZ_b3eCk1njgE4mc3eLnXGJvYit_a7wycannztYeCrt-Yw)  
  <sub>AsiaOne, 2 hours ago</sub>  
  With less than two weeks before the full implementation of the Beverage Container Return Scheme (BCRS), retailers and distributors have been trying to clear...
- [HDFC Bank stock slips as CEO succession weighs on sentiment](https://www.google.com/goto?url=CAESrgEB6zswFdT4Ey0fJgg_MtmSti2zT1BIiZZTJaBHCuk6xXLf6-URqFqR-87c_t6XuAfztsny35AMjhyhJKMdIgrKXW4umbsYehVfnamAUxMUy0yB1EoI2uUDxLyRKcPwOsT0aa5krlNvoZCEMrO3TMs2-c1QC1PmG6j2oSauy7pvpv1EK2h3nUrcsuOGCULr387Ws7JjtVlKJiNtZRSW2U6RZA5Iohb-3EY1VufQE2w)  
  <sub>AD HOC NEWS, 23 hours ago</sub>  
  HDB, US40415F1012. HDFC Bank stock slips as CEO succession weighs on sentiment. Published on 09/17/2026 at 18:50 | Editorial responsibility: Rafael Müller,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 23.09 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 22.91 (+0.8%), 50d 23.60 (-2.1%), 200d 27.71 (-16.6%); 50d below 200d
Momentum: RSI(14) 50.5 | MACD -0.244 vs signal -0.301 (histogram 0.057)
Returns: 1d +1.9% | 5d -1.0% | 1m -0.3% | 3m -7.8%
52-week range: 21.84 - 37.18 (now 8.2% of the way up)
Volatility: ATR(14) 0.55 (2.4% of price) | annualised 20d 36.4%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 118.68B
Valuation: trailing P/E 16.15 | forward P/E 16.27 | P/B 9.23 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.40 | short interest 0.7% of float
Next earnings: 2026-10-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.77 (+33.3% vs last close), range 26.10 - 35.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 6,928,096 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Eli Lilly (LLY) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> News is mostly roundups and a marginal Guggenheim PT tweak ($1,273 -> $1,284), offset by a genuine policy overhang: Trump's MFN Medicaid pricing announcement for all 50 states, which is sector-negative and pricing-relevant for Zepbound/Mounjaro. Technicals are soft — price below 20d and 50d, RSI 44, MACD negative, -10.8% over a month — though still above the 200d. Fundamentals are strong (rev +47.7%, 54% operating margin, forward P/E 24 with PEG 1.14) but high P/B and 162% debt/equity temper it, and earnings are six weeks out. Consensus buy with +16% target gap is already in the price. Insider activity is sales-only across five insiders with no buys, which is weak evidence at best. Conflicting dimensions, no fresh ticker-specific catalyst, so NEUTRAL.

**Main reasons it gave:**
- Trump MFN Medicaid pricing announcement for all 50 states is a drug-pricing overhang
- Guggenheim PT nudged $1,273 -> $1,284, Buy maintained — a rehash, not new information
- Price below 20d (-1.7%) and 50d (-2.9%) SMA, RSI 44.5, MACD histogram negative, -10.8% 1m
- Revenue +47.7% YoY, 54.2% operating margin, forward P/E 24.1, PEG 1.14
- Five insiders selling, zero buyers over 180 days; volume only 0.46x 20-day average

<details><summary><b>News</b> — score -0.10</summary>

- [Better Buy for Cautious Investors: Eli Lilly vs Costco](https://www.google.com/goto?url=CAESmgEB6zswFeThqDHsQPe4zewj4p0A05MT8YK78Qbg_oS1KXIpZU8llYNO6-tJxQhu61yd31z0Ho08nt585RZA356AjVvNU6OmfH1n0-ioQumUd0nKY-vcYISl52UOHnwv-CAFLwfzCZzILCO_ZTIUbQUzK5KJlhLI0w-nrNlMe4RVlSIxdls15s3Inx9hQO9T21Xs5DeEJF-87xc8)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Investors piled into growth stocks in recent years, particularly in the area of artificial intelligence (AI), and this movement offered the overall market...
- [1 Safe-and-Steady Stock Worth Your Attention and 2 We Question](https://stockstory.org/us/stocks/nyse/lly/news/buy-or-sell/1-safe-and-steady-stock-worth-your-attention-and-2-we-question)  
  <sub>StockStory, 9 hours ago</sub>  
  Stability is great, but low-volatility stocks may struggle to deliver market-beating returns over time as they sometimes underperform during bull markets.
- [Guggenheim maintains Buy rating on Eli Lilly, $1284 price target](https://www.google.com/goto?url=CAEStAEB6zswFew7m4tvZyjyDwBRftnY4Q50KVpOktsWmDCRT14-_-CF00ik6VoPVL_peWelSUnffWiLqAJtiVsq7ubiZ4Y7E6R1yT151zsGD46bgGpcD0BEELHQ5TKoQTBYKMYYLI9gLPPDMTwVAkNqaO6PlRW-3EBZCdKWbFSoYPlOeDx3go3GKFB8qdMezjFtQIfLxKnW1nPCNGO_Mg4jpoojkBP5BkvkU_QLbylVJ66tYuzh2PA)  
  <sub>TradingView, 1 hour ago</sub>  
  Guggenheim maintained their Buy rating on Eli Lilly's stock with a price target of $1284.00.The price target implies an upside of 11.4% from the Sep 17...
- [Trump set to announce MFN pricing for Medicaid in all states](https://seekingalpha.com/news/4644426-trump-set-announce-mfn-pricing-medicaid-all-states)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  President Trump on Friday will announce that Medicaid beneficiaries in all 50 states will benefit from "Most Favored Nation" pricing discounts for some...
- [Guggenheim raises Eli Lilly stock price target to $1,284 on drug growth](https://uk.investing.com/news/stock-market-news/guggenheim-raises-eli-lilly-stock-price-target-to-1284-on-drug-growth-93CH-4874499)  
  <sub>Investing.com UK, 5 hours ago</sub>  
  Investing.com - Guggenheim raised its price target on Eli Lilly and Company shares (NYSE:LLY) to $1,284 from $1,273 while maintaining a Buy rating on the...
- [Eli Lilly Diabetes Drug Franchise Remains Strong, Analyst Praises Foundayo Trajectory](https://www.google.com/goto?url=CAESwQEB6zswFVNfOtpQvvMqaFXg580avq2XhMgibiKDC9JeMbBExZI-GDiZ6t55ojAFq47NuSlCk3PKBBpg66J65Lj4CtwaUgxQD0TKn385p5lrM9rNaohiggr-6VLLZv_LnBAEce9nT8kcvBtH-VgSIvxHUM3g_IQtHal_O8eWVN6cLsIU6J09fHdf-K20YgV7OyOlh3Z4_4ZmFQgY-IiJ2m0igty9BCscUWhi2P3AmqficNkIRT8IueZH09ig2YtitFc6)  
  <sub>Benzinga, 21 minutes ago</sub>  
  As Eli Lilly And Co (NYSE:LLY) prepares to report third-quarter results in late October, Guggenheim analyst Seamus Fernandez maintains a Buy rating,...
- [J&J Up 18% in Three Months: Buy, Sell or Hold the Stock?](https://finance.yahoo.com/markets/stocks/articles/j-j-18-three-months-130500694.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Johnson & Johnson JNJ stock has risen 18.3% in the past three months, backed by improving earnings and sales, a raised 2026 outlook, strong performance from...
- [Can Volume Keep Covering Eli Lilly’s Price Cuts?](https://www.trefis.com/stock/lly/articles/615683/can-volume-keep-covering-eli-lillys-price-cuts/2026-09-17)  
  <sub>Trefis, 21 hours ago</sub>  
  Eli Lilly (LLY) grew revenue 48% in Q2 2026, driven by Zepbound and Mounjaro. A more understated metric for investors to watch is pricing.
- [Trump administration is said to weigh allowing most pharma licensing deals with China](https://seekingalpha.com/news/4644250-usweighs-allowing-most-pharma-licensing-deals-china)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  The U.S. is drafting rules for biopharma firms investing in China that would likely maintain their ability to ink most licensing deals for Chinese drugs.
- [Could Eli Lilly (NYSE:LLY) Be the Clearest Healthcare Stocks Signal Right Now?](https://www.google.com/goto?url=CAESsAEB6zswFYX1hJOhIt1_wwfFa7ZzY6b4fVaF--LFjKQeLclzm28m3jen3Y1Y84JFReA6mwbZNF9m8dusEZa4icRrB4W4m9CIPeVrNkWUONoQeg9ZdD3dP5cF6s2HORQz0ZvMj6E3Dszw-7_Rg0Zn4bFAihofpN3kwFsTL87WrAojKodnfSgzC4C4NuM5IZJEG62b3q_aINaPXcqPGXRsJWFG96atvf4Wy6DPqgT5X6p2cQ)  
  <sub>Kalkine Media, 19 hours ago</sub>  
  Eli Lilly (NYSE:LLY) returns to the Healthcare Stocks conversation, with focus on product demand, regulatory milestones, pipeline execution, reimbursement,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 1,142.54 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 1,162.79 (-1.7%), 50d 1,177.15 (-2.9%), 200d 1,066.29 (+7.2%); 50d above 200d
Momentum: RSI(14) 44.5 | MACD -14.532 vs signal -13.667 (histogram -0.865)
Returns: 1d -0.9% | 5d +2.4% | 1m -10.8% | 3m +4.0%
52-week range: 714.59 - 1,280.34 (now 75.6% of the way up)
Volatility: ATR(14) 29.45 (2.6% of price) | annualised 20d 19.3%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.02T
Valuation: trailing P/E 38.43 | forward P/E 24.13 | P/B 30.07 | PEG 1.14
Profitability: profit margin 33.5% | operating margin 54.2% | ROE 102.3%
Growth (YoY): revenue +47.7% | earnings +26.2%
Balance sheet: debt/equity 162.1% | free cash flow 11.07B
Risk: beta 0.50 | short interest 0.9% of float
Next earnings: 2026-10-29
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 1.63 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 6 strong buy, 19 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,324.87 (+16.0% vs last close), range 930.00 - 1,600.00
Recent rating changes:
  - 2026-09-18 Guggenheim: main, Buy -> Buy
  - 2026-09-10 HSBC: main, Reduce -> Reduce
  - 2026-08-07 Truist Securities: main, Buy -> Buy
  - 2026-08-06 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-07-15 Citigroup: main, Buy -> Buy
Institutional ownership: 85.3%
Largest holders: Lilly Endowment, Inc (9.6%), Blackrock Inc. (7.2%), Vanguard Capital Management LLC (5.7%), PNC Financial Services Group, Inc. (5.5%), State Street Corporation (3.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

```text
Last 180 days: bought 1,442 shares in 24 transaction(s) | sold 308,215 shares in 8
Net: -306,773 shares (-18.0% of insider holdings) | insiders hold 1,399,430 shares
Distinct insiders: 0 buying, 5 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-17 JONSSON PATRIK (Officer): 6,500 shares, 7.64M
  - 2026-08-10 ZAKROWSKI DONALD A (Officer): 2,000 shares, 2.37M
  - 2026-08-07 HAKIM ANAT (General Counsel): 5,000 shares, 5.95M
  - 2026-06-10 YUFFA ILYA (Officer): 2,500 shares, 2.88M
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> MercadoLibre is caught between a structurally bullish business and a valuation debate that has intensified sharply in the past week. Revenue growth of 49.8% YoY and a PEG of 0.89 suggest growth is priced reasonably relative to expansion, and analyst consensus remains strongly buy with a 26% upside to target. However, the technical picture has deteriorated materially: the stock is down 5.3% over five days and 5.9% over one month on elevated volatility, with RSI at 38.7 (oversold territory but momentum still negative), MACD deeply negative, and price now 6.4% below the 20-day moving average. Volume is running 0.55x average, suggesting weak conviction behind the move. The news flow is generic valuation debate (multiple rehashes of the P/E being high, a $1B notes issuance, and a sector comparison) rather than a ticker-specific catalyst. Insider activity from June and May shows two executives buying modestly, which is mild support but not recent enough to signal confidence in current levels. The fundamental tension—strong revenue growth and solid ROE against a trailing P/E of 49.2 and leverage at 168.6% debt/equity—does not resolve cleanly. Earnings arrive 2026-11-04, roughly 6 weeks out, so near-term catalysts are thin. The combination of weak technicals, generic bearish sentiment on valuation, and lack of fresh conviction drivers justifies a neutral stance with low conviction; this is a name where the fundamentals support holding but the technicals and sentiment do not yet justify stepping in.

**Main reasons it gave:**
- RSI 38.7 and MACD deeply negative on 5.3% weekly decline
- Analyst consensus buy with 26% upside target; no recent rating changes
- 49.8% revenue growth and PEG of 0.89 imply reasonable growth pricing
- Trailing P/E 49.2 well above peers; valuation debate dominates recent headlines
- Two insider purchases in May-June but none in last 90 days

<details><summary><b>News</b> — score -0.35</summary>

- [MercadoLibre Trading at 35.63X P/E: Should You Exit MELI Stock?](https://www.tradingview.com/news/zacks:a3a3e53b9094b:0-mercadolibre-trading-at-35-63x-p-e-should-you-exit-meli-stock/)  
  <sub>TradingView, 2 hours ago</sub>  
  MercadoLibre, Inc. MELI has a premium valuation, with its forward P/E multiple well above the industry average and key peers. The stock is currently trading...
- [Is MercadoLibre (MELI) Reasonably Priced After Its $1B Notes Issue?](https://simplywall.st/stocks/us/retail/nasdaq-meli/mercadolibre/news/is-mercadolibre-meli-reasonably-priced-after-its-1b-notes-is)  
  <sub>Simply Wall Street, 15 hours ago</sub>  
  MercadoLibre has seen its share price swing sharply in recent years, which puts fresh focus on whether the current valuation lines up with the cash the...
- [Here's Why You Should Hold on to Republic Services Stock for Now](https://www.zacks.com/stock/news/2992138/heres-why-you-should-hold-on-to-republic-services-stock-for-now)  
  <sub>Zacks Investment Research, 2 hours ago</sub>  
  RSG is benefiting from strong pricing, margin expansion and cash flow, while Environmental Solutions adds another growth avenue.
- [MercadoLibre stock edges lower as valuation debate intensifies](https://www.ad-hoc-news.de/boerse/news/corporate-news/mercadolibre-stock-edges-lower-as-valuation-debate-intensifies/70124856)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  MELI, US58733R1023. MercadoLibre stock edges lower as valuation debate intensifies. Published on 09/18/2026 at 13:47 | Editorial responsibility: Rafael...
- [Mercado Libre Stock Falls 10% In A Week As Valuation Debate Grows](https://journalarta.com/en/2026/09/05/mercado-libre-stock-price-weekly-drop-valuation/)  
  <sub>JournalArta, 10 hours ago</sub>  
  MercadoLibre stock price last closed at US$1632.52 after a 10% weekly slide, keeping investors focused on whether the pullback changes the case for the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 1,795.92 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 1,919.35 (-6.4%), 50d 1,877.64 (-4.4%), 200d 1,853.04 (-3.1%); 50d above 200d
Momentum: RSI(14) 38.7 | MACD -12.434 vs signal 8.054 (histogram -20.488)
Returns: 1d -1.6% | 5d -5.3% | 1m -5.9% | 3m +9.8%
52-week range: 1,546.81 - 2,510.97 (now 25.8% of the way up)
Volatility: ATR(14) 61.10 (3.4% of price) | annualised 20d 28.2%
Volume: 0.55x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.45</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 91.05B
Valuation: trailing P/E 49.20 | forward P/E 31.82 | P/B 11.62 | PEG 0.89
Profitability: profit margin 5.3% | operating margin 6.7% | ROE 27.5%
Growth (YoY): revenue +49.8% | earnings -10.9%
Balance sheet: debt/equity 168.6% | free cash flow 353.38M
Risk: beta 1.31 | short interest 1.6% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.65</summary>

```text
Consensus: buy (mean 1.58 on a 1=strong buy to 5=strong sell scale, 24 analysts)
Ratings: 4 strong buy, 15 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,264.88 (+26.1% vs last close), range 1,750.00 - 2,800.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.65</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.25</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.25</summary>

_Not available today._

</details>

### Novo Nordisk (NVO) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Two positive CHMP opinions (Frehemgo for haemophilia A, Sogroya for ISS) are genuine but low-revenue-impact regulatory wins already partly captured in Thursday's 4% pop, and the stock closed flat on 0.5x volume. Offsetting: Sandoz generic Ozempic approval in Canada, halted ziltivekimab CV trials, and a Morgan Stanley downgrade to Underweight on Sep 11. Technicals are broken (below 20/50/200d SMAs, MACD negative, RSI 41). Valuation is cheap at 10x trailing with 42% operating margins and 60% ROE, but earnings are -21% YoY as GLP-1 pricing/competition bites. Conflicting dimensions argue for no directional bet.

**Main reasons it gave:**
- Two positive CHMP opinions (Frehemgo haemophilia A, Sogroya ISS) already drove a 4% move
- Sandoz Canadian approval for off-patent Ozempic adds generic pressure
- Morgan Stanley cut to Underweight Sep 11; consensus hold, 10 of 12 at hold
- Price below 20d/50d/200d SMAs, MACD histogram -0.24, volume 0.53x average
- Trailing P/E 10.3 with 42.5% operating margin but earnings -20.6% YoY
- Ziltivekimab cardiovascular trials halted

<details><summary><b>News</b> — score +0.10</summary>

- [A weekly shot may become Europe’s first approved growth-hormone treatment for children with unexplained shortness](https://www.stocktitan.net/news/NVO/novo-s-once-weekly-sogroya-somapacitan-receives-positive-chmp-t7iotyc7xc3o.html)  
  <sub>Stock Titan, 6 hours ago</sub>  
  Novo Nordisk (NVO) received a positive CHMP opinion recommending once-weekly Sogroya (somapacitan) for children in Europe with idiopathic short stature...
- [NVO Stock Jumps 4% As European Committee Backs Novo’s Haemophilia Pen](https://www.google.com/goto?url=CAESvQEB6zswFeP1ej2F4xZxYrvhYyLrR5BSo0Oar2Mx8Tk2bSUlsLKFbXX5kCSIK45SG3rs4V5z-kh-pXp2XQXaeH-_IPqcp6XuxS31obucfRFCz2DQKIFiu33X1-we0SasDPsvGgBuVZQ3RDnV1-ZNqMImF0BSpZ6nKxVlEj1nOOMNWPYSv1C9cY08pylueWslwh_GVB7gpHtgd3YUOFZ_W337jn5KVDKlQwt9WBTpok9Qp8QVLhLOLCVbvcl5c6E)  
  <sub>Stocktwits, 22 hours ago</sub>  
  The Committee for Medicinal Products for Human Use recommended European Union marketing authorization for Frehemgo in adults and children with haemophilia A...
- [Sandoz wins Canada nod for generic Ozempic; inks licensing deal for generic Hemlibra](https://seekingalpha.com/news/4644292-sandoz-wins-canada-nod-generic-ozempic)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Sandoz (SDZNY) on Thursday announced Canadian approval for an off-patent version of Novo's (NVO) popular GLP-1 therapy, Ozempic, and a licensing deal with...
- [Is It Too Late to Buy Novo Nordisk AS (NVO) After 3.5% Rally? GF Value Says Undervalued](https://www.gurufocus.com/news/9086937/is-it-too-late-to-buy-novo-nordisk-as-nvo-after-35-rally-gf-value-says-undervalued)  
  <sub>GuruFocus, 19 hours ago</sub>  
  On September 17, 2026, Novo Nordisk AS (NVO) shares rose 3.5% today, currently trading at $43.19. This price remains within a 52-week range, with a high of...
- [Why Is Novo Nordisk Stock Trading Higher Today? - Novo Nordisk (NYSE:NVO)](https://www.benzinga.com/trading-ideas/movers/26/09/61850700/ema-committee-endorses-novo-nordisks-hemophilia-a-therapy)  
  <sub>Benzinga, 24 hours ago</sub>  
  Novo Nordisk A/S (NYSE:NVO) stock is trading higher on Thursday after the Danish drug maker achieved major advances across its therapeutic pipeline after...
- [Why Is GLW Stock Dipping Premarket Today?](https://stocktwits.com/news-articles/markets/equity/glw-stock-drops-premarket-as-corning-launches-2-b-equity-offering/cZtlxZ2RBRi)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The offering comes after a huge run for Corning shares this year. GLW has gained roughly 91% year to date, driven largely by growing investor enthusiasm...
- [EU backs new haemophilia A shot from Novo Nordisk (NYSE: NVO)](https://www.google.com/goto?url=CAESpwEB6zswFdShvJivi68bFbfF01-4o3MC8JWgtGdLBAYntKjFjsZuwQlkVQk_FOt7DzJlAtbsbr7ghok4iyMEkUXNlbSEqUrQG2JPzOMgBjl1sKCr1fTN4t4lAPqkoZpR8ET_d6N7Z4KO3rtaUCpqeBg78sJCHGpxOroznnyZeW3z3AQTBIz-M4xHvXDChFFYfFQUEVyUmE03Wq9ZYFNA_eoZbqoc1JS4lg)  
  <sub>Stock Titan, 24 hours ago</sub>  
  Novo Nordisk A/S (NVO) announced that the EMA's Committee for Medicinal Products for Human Use (CHMP) has issued a positive opinion recommending EU...
- [MCD Stock Fades After 0.7% Pop On Value-Menu Revamp Report](https://stocktwits.com/news-articles/markets/equity/mcd-stock-fades-after-0-7-pop-on-value-menu-revamp-report/cZtsG7DRBdF)  
  <sub>Stocktwits, 19 hours ago</sub>  
  McDonald's told franchisees it will spend the coming weeks building a “longer-term” value plan aimed at price-sensitive customers, Bloomberg reported.
- [SPCX Stock In Focus — SpaceX Pushes Starship Launch To September 28, Reportedly Weighs Startup-Data Buys for AI](https://www.google.com/goto?url=CAES5gEB6zswFR2f5MN6ravVYnzeWmBfCv5wKRG-0yZYP5u5WELDkg_lbPBwzhsnusJtED67N2ZzJcIdfvW4OIJmqg-DihMSwDZpDTyYAK3a72frAG-Y2JyYLl9E4CVv3y6Ks7kMbWTNOGvBsw9XBySkNQk3OTgERBwNAVxWYnwz3d_G7mqi19F_v4Lan7ZBcjDEHuHmTJludHEDjR040-BiUse-VVZLQgKwi6lPkI8TRyA9RHCBzOGgTXFiTq0QvUA-ukPP7_lJ9ajirUGrvzdhYcj8CyIQCqcS2qaDj_o9xyT_7mf__Q8oOA)  
  <sub>Stocktwits, 20 hours ago</sub>  
  SpaceX said on Thursday that Starship's Flight 14 is now targeted for Monday, September 28, pending regulatory approval.
- [Novo Nordisk (NVO) Pulls the Plug on Two More Heart Drug Trials](https://finance.yahoo.com/healthcare/articles/novo-nordisk-nvo-pulls-plug-233726977.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  On September 7, 2026, Reuters reported that Novo Nordisk A/S (NYSE:NVO) halted two additional trials of its experimental cardiovascular drug ziltivekimab,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 43.19 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 45.18 (-4.4%), 50d 46.90 (-7.9%), 200d 46.15 (-6.4%); 50d above 200d
Momentum: RSI(14) 41.0 | MACD -1.126 vs signal -0.884 (histogram -0.243)
Returns: 1d -0.0% | 5d +0.3% | 1m -7.1% | 3m -0.0%
52-week range: 35.29 - 63.98 (now 27.5% of the way up)
Volatility: ATR(14) 1.24 (2.9% of price) | annualised 20d 34.1%
Volume: 0.53x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 190.79B
Valuation: trailing P/E 10.28 | forward P/E 12.85 | P/B 5.59 | PEG 3.07
Profitability: profit margin 35.3% | operating margin 42.5% | ROE 59.8%
Growth (YoY): revenue +2.1% | earnings -20.6%
Balance sheet: debt/equity 63.3% | free cash flow 37.67B
Risk: beta 0.34 | short interest 1.0% of float
Next earnings: 2026-11-04
```

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score -0.25</summary>

```text
Consensus: hold (mean 2.71 on a 1=strong buy to 5=strong sell scale, 12 analysts)
Ratings: 0 strong buy, 3 buy, 10 hold, 1 sell, 0 strong sell
Price target: mean 46.74 (+8.2% vs last close), range 39.54 - 63.31
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

<details><summary><b>What analysts say about what this fund holds</b> — score -0.25</summary>

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

### Procter & Gamble (PG) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> PG presents a conflicted picture with offsetting signals across dimensions. News flow is generic and promotional (analyst reaffirmations, institutional purchases, listicle inclusion) rather than material catalysts. Technicals show neutral positioning: the stock trades near its 20d and 50d SMAs with RSI at 51 (middle of the band), but volume is notably weak at 0.38x the 20-day average and the 50d is rolling below the 200d, suggesting a subtle downtrend. Fundamentals reveal a mature, expensive business: forward P/E of 19.73, PEG of 3.76, and trailing earnings down 15.5% YoY despite 30.3% ROE and strong 22.1% operating margins. The analyst consensus is supportive (mean rating 2.20, mean target +10%) but recent downgrades from Argus and HSBC (July-August) signal fading enthusiasm among sell-side researchers. Insider activity is mixed: a net +50k shares purchased in 26 transactions over 180 days is constructive, but the absence of any specific buying by named insiders in the raw transaction list (all entries shown are sales by officers) and the routine nature of compensation-related transfers weaken this signal. The upcoming earnings date (Oct 22) is 34 days away and historically important for this name given the earnings miss pattern, but it is not an immediate catalyst. The valuation is reasonable for a defensive compounder but not compelling at current multiples given headwinds to top-line growth and margin pressure. No clear, material, ticker-specific catalyst is evident in the past 24 hours.

**Main reasons it gave:**
- Recent downgrades from Argus (Buy→Hold) and HSBC despite analyst consensus still supportive
- Earnings down 15.5% YoY on 1.5% revenue growth; PEG 3.76 suggests limited multiple expansion room
- Volume 0.38x average on flat price action; 50d SMA rolling below 200d SMA
- CEO option grant at $146.67 strike (near current price) is routine compensation, not a conviction buy signal
- Generic news flow (listicles, institutional routine purchases) lacks material, ticker-specific catalyst

<details><summary><b>News</b> — score +0.10</summary>

- [Investors Heavily Search Procter & Gamble Company (The) (PG): Here is What You Need to Know](https://finance.yahoo.com/markets/stocks/articles/investors-heavily-search-procter-gamble-130006084.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  P&G (PG) has received quite a bit of attention from Zacks.com users lately. Therefore, it is wise to be aware of the facts that can impact the stock's...
- [Nykredit A S Purchases New Position in Procter & Gamble Company (The) $PG](https://www.marketbeat.com/instant-alerts/filing-nykredit-a-s-purchases-new-position-in-procter-gamble-company-the-pg-2026-09-18/)  
  <sub>MarketBeat, 9 hours ago</sub>  
  Nykredit A S acquired a new position in Procter & Gamble Company (The) (NYSE:PG - Free Report) during the second quarter, according to the company in its...
- [P&G Has Cut 5,000 Jobs So Far. At 60, a Worker Leaving With Company Stock Can Lose a Capital-Gains Tax Break by Rolling Everything Into an IRA.](https://247wallst.com/personal-finance/social-security/2026/09/18/pg-has-cut-5000-jobs-so-far-at-60-a-worker-leaving-with-company-stock-can-lose-a-capital-gains-tax-break-by-rolling-everything-into-an-ira/)  
  <sub>24/7 Wall St., 6 hours ago</sub>  
  Thousands of P&G workers leaving with company stock in their 401(k) face a rollover decision that looks routine but can quietly erase a tax break worth tens...
- [Procter And Gamble (PG) Stock Could Be Cheap As 16% Five Year Gain Continues](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-stock-could-021216324.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  Procter & Gamble has delivered steady long term gains for shareholders, yet the current share price raises a clear question about how fully its cash flows...
- [9 Stocks To Buy For October 2026](https://www.forbes.com/sites/investor-hub/article/best-stocks-buy-now-october-2026/)  
  <sub>Forbes, 6 hours ago</sub>  
  Stock prices are taking a breather after months of robust gains. In an interview, David Katz, CIO of Matrix Asset Advisors, said the backdrop favors a more...
- [PG&E Sets Dates for Quarterly Stock Dividends](https://www.google.com/goto?url=CAESogEB6zswFaCqQ5xUZ90iG6XnfJfYdCq6GmvtniT_-U5sU88jFkNxNlQOeati8O5NIOK1w55Bhvztrs5ttjNpoQ67TSF--kltPw8Bwtq-w8-xWDE8l2OMHuzaNsZ5Ff-jXBuF6TUqmiSd9cFtWhiZ82jhCIBYUcQGGt-za7MbXZgYzK3gnGEbxvUt7PeSnxFl4SIYO7Or6b7PScu_w1gUO_svgWs)  
  <sub>TradingView, 6 hours ago</sub>  
  18, 2026 /PRNewswire/ -- PG&E Corporation ( PCG) declared its third quarter 2026 regular cash dividend of $0.05 per share on the Corporation's common stock.
- [Procter & Gamble (NYSE: PG) CEO granted 22,787 new options](https://www.stocktitan.net/sec-filings/PG/form-4-procter-gamble-co-insider-trading-activity-0afb67bf2818.html)  
  <sub>Stock Titan, 23 hours ago</sub>  
  CEO Shailesh Jejurikar receives 22787 PG stock options at a $146.67 strike, exercisable from Sept. 14, 2029 to Sept. 15, 2036, plus reports 39325.9973...
- [Ohio Rep. David Taylor Bought Up to $30K Worth of Installed Building Prods Stock](https://www.benzinga.com/government/26/09/61871667/ohio-rep-david-taylor-bought-30k-worth-installed-building-prods-stock)  
  <sub>Benzinga, 1 hour ago</sub>  
  A September filing shows that Representative David Taylor reported a purchase in Installed Building Prods (NYSE:IBP), valued between $2002 and $30000.
- [Procter & Gamble stock edges higher as analysts reaffirm upside potential](https://www.ad-hoc-news.de/boerse/news/corporate-news/procter-and-gamble-stock-edges-higher-as-analysts-reaffirm-upside/70125359)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  Procter & Gamble stock closed at USD 147.55 on the NYSE on September 17, 2026, 0.36% above the prior session. Analysts see further upside, with an average...
- [Long-Term Treasury Yields Now Beat These Dividend Stalwarts. Is Government Debt the Top Passive-Income Play?](https://www.theglobeandmail.com/investing/markets/stocks/PG/pressreleases/4670495/long-term-treasury-yields-now-beat-these-dividend-stalwarts-is-government-debt-the-top-passive-income-play/)  
  <sub>The Globe and Mail, 17 hours ago</sub>  
  Detailed price information for Procter & Gamble (PG-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 146.03 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 145.54 (+0.3%), 50d 146.11 (-0.1%), 200d 147.46 (-1.0%); 50d below 200d
Momentum: RSI(14) 51.0 | MACD 0.197 vs signal -0.060 (histogram 0.257)
Returns: 1d -1.0% | 5d +0.5% | 1m +1.1% | 3m -2.9%
52-week range: 138.04 - 167.20 (now 27.4% of the way up)
Volatility: ATR(14) 2.35 (1.6% of price) | annualised 20d 15.0%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 339.18B
Valuation: trailing P/E 22.06 | forward P/E 19.73 | P/B 6.36 | PEG 3.76
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.2% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

```text
Consensus: buy (mean 2.20 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 7 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 160.61 (+10.0% vs last close), range 143.00 - 186.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

```text
Last 180 days: bought 90,413 shares in 26 transaction(s) | sold 40,243 shares in 13
Net: +50,170 shares (+2.4% of insider holdings) | insiders hold 2,115,234 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-08-24 JANZARUK MATTHEW W. (Officer): 359 shares, 52.14K
  - 2026-08-21 RAMAN SUNDAR G. (Officer): 3,435 shares, 491.27K
  - 2026-08-20 JANZARUK MATTHEW W. (Officer): 156 shares, 22.43K
  - 2026-08-20 PURUSHOTHAMAN BALAJI (Officer): 2,019 shares, 290.31K
(24 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.35

**In the model's own words:**

> RY presents a mixed picture with conflicting signals across dimensions. Technicals show weakness: price is 3.3% below the 50-day moving average, RSI at 39.6 indicates potential oversold conditions but momentum is deteriorating (MACD histogram negative), and volume is thin at 0.17x average. The stock is at 79% of its 52-week range, suggesting it has run significantly but now lacks follow-through. Fundamentals remain solid with 12.8% earnings growth, 16.2% ROE, and a reasonable forward P/E of 15.83 for a large-cap bank, but valuation is not particularly compelling at 17.78x trailing. Analysts maintain a buy consensus with modest 3.7% upside to mean target of 209.71, suggesting the market has already priced in reasonable expectations. News is generic sector commentary and listicle material, lacking a material ticker-specific catalyst. The most interesting data point is share buybacks by the issuer (700k shares in late August at C$70/share), which is weakly bullish and suggests management sees value, but this alone does not overcome the technical deterioration and lack of catalytic news. Short interest rose 56.9% in August, which could indicate crowding on either side but is not actionable directional evidence. The next earnings date is December 3rd, 2026, which is 2.5 months away. Overall, this is a defensible, dividend-paying blue chip in a consolidation phase with no clear near-term catalyst, warranting a neutral stance with low conviction.

**Main reasons it gave:**
- Price 3.3% below 50-day MA with thin volume and negative MACD histogram
- Analyst consensus buy with only 3.7% upside to mean target suggests limited near-term catalyst
- Solid but unspectacular fundamentals: 12.8% earnings growth, forward P/E 15.83
- Management buybacks in August at C$70/share suggests modest confidence in valuation
- Next earnings 2.5 months away with no material near-term news catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [Royal Bank Of Canada (NYSE:RY) Short Interest Up 56.9% in August](https://www.google.com/goto?url=CAESsgEB6zswFX0snSWB_fEUajNE7zXwQE8uHLJjaNnfahDzCHjIvRItnDRWGNKQRA7nCozH5w-HSsDng3cGinZTPDVdZasteIbL487NlZnLJBtayO7oX3SP2vvq8O54LmWDFncPfe6Jc-cYVfgm9pb5zNMn5_RFfOL_3Fh5QKPHazwHu518LX-dGQWZljmF_XCylTOQfehfP12gnneuqX4n-qNUGUTM7wXSSr1v2wk-L8vdZelU)  
  <sub>MarketBeat, 17 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Get Free Report) (TSE:RY) saw a large growth in short interest during the month of August. As of August 31st,...
- [Royal Bank of Canada stock holds near a 52-week high](https://www.google.com/goto?url=CAESqwEB6zswFYap1aD5HYXN2YYBTQrmWgd5pKPp_iqcfYi9C7Wjxf8L8fSn7-w5KkjKXcV-F8h5UTs69Pcyk1ZQlRQml2rytE-7wn4sorfMVBN0l1qbQtsf4NwOi8T9q6XxJ1eB3tLgwzYatHrYW9zvoqtmRezsZWd7CHfXetpG2sKP4lnQF-lsAL8WUNo2rPkQc_GLKL6svOXoWrCMq7fR6tqgaL5QiwngdsE4aCs)  
  <sub>AD HOC NEWS, 4 hours ago</sub>  
  Royal Bank of Canada stock closed at USD 203.57 on September 17, 2026, up 0.63 percent. MarketBeat said August quarter EPS was USD 3.07 and revenue was USD...
- [What Keeps Royal Bank of Canada (NYSE:RY) in NYSE Focus?](https://www.google.com/goto?url=CAESmQEB6zswFRzhbPlFpX9UzYxn2KOqS1GCgVfmFYXKZLmdgM9ssTZWfY97RJt8nITddvCcJWHmJifquWb4zfZIR4Bow98uPNU8P0nng9DEjpfQZpqaIVLpxZyTQorLL9O_NKk9NIalCB-lTmVcxvelQgxFhkpQ54ePU8pl8mdxJJLwQ-3ntMH1Y7oR8kJ-tSNWXbo_Ot9V2ia8MZA)  
  <sub>Kalkine Media, 10 hours ago</sub>  
  Royal Bank of Canada operates across banking, wealth management, insurance and capital markets, with NYSE Composite context and broad international...
- [For Investors Who Want to Stop Checking the Market Every Day: 1 Stock to Own](https://www.google.com/goto?url=CAESowEB6zswFYNSUERWG8yyTZotVGv5K285jDrim7mV1ncDaIHtYtVX2zrxluOei_lAfmYW4-6Djb7qiiqUQF2hRjqORVyC9w1ANKyaLd8eteu_XDzo7AY4nbSiVtSRY8l3GQoNxAD2udlrCa9BeZFP8V7qQ-j2SZiIuMA7RfSLWXjfQe_hMdudS1lxwkW2_hSIV9BI-rPXlfJOYfq3yPOGY_AOKZGU)  
  <sub>The Motley Fool Canada, 20 hours ago</sub>  
  Understand the stock market landscape. Discover how prioritizing your life need not affect your investment strategy and decisions.
- [What Is Putting Royal Bank of Canada (TSX:RY) in Focus?](https://www.google.com/goto?url=CAESlwEB6zswFZbfZ_wZgHTVCM8lK0hTVU8V-D9cX2C-Lz_EZJcDr23Aqi1qXYdFyw_MEZhzv39L__lIz3iMFhz-8bqL3rZiobpQcdBlnu1IvMB_VXAY-lqKQjVHlGKwWkoeftz29Hq4iDZI62tZJ9jft88be0SVRPXJRqJXGi6UG0hFY04H5bWJsqbkol5GO7JJ2d2bDYaafvcu)  
  <sub>Kalkine Media, 10 hours ago</sub>  
  The current story centres on the latest TSX rebound led by financial and metal-mining strength as bond yields eased. The business remains rooted in banking.
- [Purpose Investments Inc. Announces September 2026 Distributions](https://www.google.com/goto?url=CAESxQEB6zswFZmtnfq_II1Aybgt2szUsG9pdqZQpvq1R3hcjc8K3YxVWf72cvmDkkOj7nkkkFny9HxKEBDv0Hr3QYUUaStpX_gCLMDBvJhuf-JguPxKuKNsJ2NDD46DwFzTA1AXEbZ5k31gxXi-326S6Nqrq3zVWoeQttL8Ned87VtRNwNjFHzv7TgGUOlAJos30ZyOX-OpLutKenqYf_tOTz894LbFhTvB_EnuCz0b5xR3VL19uK7mQVBrOuLZg3hXaupcc29VUg)  
  <sub>The Manila Times, 19 hours ago</sub>  
  Payable. Date. Distribution. Frequency. Apple (AAPL) Yield Shares Purpose ETF - ETF Units, APLY, $0.1667, 09/28/2026, 10/02/2026, Monthly.
- [3 TSX Blue-Chip Stocks to Buy With $10,000 Now](https://www.google.com/goto?url=CAEShAEB6zswFWhlIR9Olzo7YisPM9uhhWt3Q3RKyiz1hZHvhG8imv06XR4dnsgGlUCeU7Vca2RDf6Q-855qkvNKs6k6Mz75kiVhHdxJbFDdIpYCsAToGPDNoVZYe0Lx_IVYACuk07Bhanaqf6Snkzmutq_JWS4psMGLtgmNPtJZeTQ4jURKZkc)  
  <sub>The Motley Fool Canada, 21 hours ago</sub>  
  These TSX blue-chip stocks have a history of paying reliable dividends while continuing to grow their businesses over the long run.
- [Royal Bank of Canada stock support test at C$280.45: Key levels to watch](https://www.google.com/goto?url=CAEShAEB6zswFcEFVY033wA39wkRLLtaPszcJWAyM8O8gegxx1lw6fRE0scL3znUdKebMxVFoKHrGzjd1Ujj-yjVLw3_Mez2pjZweDJAS3XGZGM1qXDQUaE3VIH2vTM_bLsOnk-6eCRVuZicibkClPxygA5SPzIR5L5xgwLxspa7UCQZKZamjHs)  
  <sub>Traders Union, 2 hours ago</sub>  
  Royal Bank of Canada (RY) stock is trading at C$283.33, reflecting a slight decline on the day. The price sits below its key short- and medium-term moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 202.32 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 205.79 (-1.7%), 50d 209.20 (-3.3%), 200d 184.52 (+9.6%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD -1.414 vs signal -0.939 (histogram -0.476)
Returns: 1d -0.6% | 5d -1.7% | 1m -2.6% | 3m +0.4%
52-week range: 143.64 - 217.87 (now 79.1% of the way up)
Volatility: ATR(14) 3.23 (1.6% of price) | annualised 20d 15.2%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 280.10B
Valuation: trailing P/E 17.78 | forward P/E 15.83 | P/B 2.90 | PEG 2.26
Profitability: profit margin 33.9% | operating margin 46.4% | ROE 16.2%
Growth (YoY): revenue +8.9% | earnings +12.8%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.92 | short interest n/a of float
Next earnings: 2026-12-03
```

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

_Not available today._

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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 209.71 (+3.7% vs last close), range 182.01 - 228.70
Recent rating changes:
  - 2025-08-29 Argus Research: main, Buy -> Buy
  - 2024-12-05 BMO Capital: main, Outperform -> Outperform
  - 2024-08-29 BMO Capital: main, Outperform -> Outperform
  - 2024-06-06 Argus Research: main, Buy -> Buy
  - 2024-04-05 BMO Capital: up, Market Perform -> Outperform
  - 2023-12-18 B of A Securities: up, Neutral -> Buy
Institutional ownership: 49.6%
Largest holders: Royal Bank of Canada (5.1%), Bank of Montreal /CAN/ (4.4%), Vanguard Capital Management LLC (3.1%), FIL LTD (1.7%), TD Asset Management, Inc (1.7%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 387,640 shares
Distinct insiders: 1 buying, 0 selling
Open-market purchases — insiders spending their own money:
  - 2026-08-31 Royal Bank of Canada (Issuer): 350,000 shares, 69.76M
  - 2026-08-28 Royal Bank of Canada (Issuer): 350,000 shares, 70.00M
  - 2026-07-31 Royal Bank of Canada (Issuer): 211 shares, 43.82K
  - 2026-07-31 Royal Bank of Canada (Issuer): 140 shares, 29.09K
(105 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

_Not available today._

</details>

### Toyota (TM) · Company — no answer, no confidence given

**This one did not finish:** Bright Data response is not JSON: Expecting value: line 1 column 1 (char 0)

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

_Not available today._

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

_Not available today._

</details>

## Whole-market funds

### S&P 500, equal weight (RSP) · Index fund — BEARISH, confidence 0.40

**Result:** ACCEPTED · 14 shares · submitted sell 14 RSP @ ~211.97, stop 215.78

**In the model's own words:**

> A Fed hike to 3.75-4.00% -- the first since 2023 -- with the 10-year at 5.00% and the dollar up 1.23 on the week is a genuine policy tightening, and the equal-weight basket, which is more cyclical and rate-sensitive than the cap-weighted index (industrials 14.7%, financials 14.6%), has already broken below both its 20d and 50d averages with MACD negative and RSI 35.7. Volume is light and price is still above the 200d, so this is a drift lower rather than a decisive break, which caps conviction. Spec positioning in E-mini is net short at the 83rd percentile -- crowded on the bearish side, which argues against pressing. Analyst roll-up covers only 1.8% of the fund and is near-meaningless. The SPMO-vs-RSP promotional piece rating RSP a Hold is marketing content, not evidence, and was disregarded.

**Main reasons it gave:**
- Fed raised rates 25bp to 3.75-4.00%, first hike since 2023, unanimous
- 10-year Treasury at 5.00% (+0.03 wk), 5-year +0.07; dollar index +1.23 on the week
- Price 212.01 is -2.5% vs 20d and -2.4% vs 50d, RSI 35.7, MACD histogram -0.786
- Equal-weight sector mix cyclically tilted: industrials 14.7%, financials 14.6%
- Large specs net short 16.5% of OI at 83rd percentile -- crowded short limits downside edge

<details><summary><b>News</b> — score -0.35</summary>

- [SPMO Vs. RSP: The 16-Point Lead Is Hiding A New Risk (NYSEARCA:SPMO)](https://seekingalpha.com/article/4947624-spmo-vs-rsp-the-16-point-lead-is-hiding-a-new-risk)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The Invesco S&P 500 Momentum ETF remains a Buy, while the Invesco S&P 500 Equal Weight ETF is rated Hold. Click for this comparative analysis of SPMO and...
- [ETF Prime: Record Inflows and the First TXSE ETF Launch](https://www.etftrends.com/etf-prime/etf-prime-record-inflows-first-txse-etf-launch/)  
  <sub>ETF Trends, 23 hours ago</sub>  
  VettaFi's Todd Rosenbluth breaks down 2026's record ETF inflows, while Westwood launches the first ETF on the Texas Stock Exchange.
- [Flow Focus | Warsh Hit the Tape. Triple Witching Comes Next. Where to Look?](https://www.moomoo.com/community/feed/flow-focus-warsh-hit-the-tape-triple-witching-comes-next-117291397349382)  
  <sub>Moomoo, 7 hours ago</sub>  
  Kevin Warsh made his move. On Wednesday the Fed raised rates a quarter point to 3.75-4.00% -- its first hike since 2023, a unanimous vote. The $U.S. 1...
- [Daily ETF Flows: QQQ Inflows Total Nearly $1B](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-qqq-inflows-210005358.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Here are the daily ETF fund flows for September 16, 2026.
- [Form FWP TORONTO DOMINION BANK Filed by: TORONTO DOMINION BANK](https://www.streetinsider.com/SEC+Filings/Form+FWP+TORONTO+DOMINION+BANK+Filed+by%3A+TORONTO+DOMINION+BANK/27076884.html)  
  <sub>StreetInsider, 19 hours ago</sub>  
  An international equity index and ETF basket comprised of the Invesco S&P 500 <sup>®</sup> Equal Weight ETF (the “Underlying Fund”) (Bloomberg symbol: “RSP UP”),...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.35</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 212.01 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 217.51 (-2.5%), 50d 217.24 (-2.4%), 200d 204.83 (+3.5%); 50d above 200d
Momentum: RSI(14) 35.7 | MACD -1.584 vs signal -0.798 (histogram -0.786)
Returns: 1d -0.6% | 5d -1.3% | 1m -4.5% | 3m +1.0%
52-week range: 182.18 - 222.77 (now 73.5% of the way up)
Volatility: ATR(14) 1.90 (0.9% of price) | annualised 20d 9.2%
Volume: 0.52x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Large Blend
What it holds: P/E 21.39 | P/B 3.11 | P/S 1.95 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +14.7% a year | beta to the market 0.83
Cost and size: expense ratio 0.20% | net assets 100.87B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Moderna Inc 0.6%, Veeva Systems Inc Class A 0.3%, Zebra Technologies Corp Ordinary Shares - Class A 0.3%, Charles River Laboratories International Inc 0.3%, DoorDash Inc Ordinary Shares - Class A 0.3%
Sector mix: Technology 17.3%, Industrials 14.7%, Financial services 14.6%, Healthcare 13.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

```text
Rolled up from the 5 largest holdings, 1.8% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 67.9% | hold 32.1% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +3.9% above the current prices
Holdings read: MRNA, VEEV, ZBRA, CRL, DASH
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - VEEV: 2026-08-28 Citigroup: main, Neutral -> Neutral
  - ZBRA: 2026-09-15 Needham: main, Buy -> Buy
  - CRL: 2026-09-11 Evercore ISI Group: main, Outperform -> Outperform
  - DASH: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 16.5% of open interest (2,071,836 contracts)
Change on the week: -0.9% of open interest
Crowding: 83% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### US company bonds, safer (LQD) · Index fund — BEARISH, confidence 0.35

**Result:** REJECTED · no room for broad fund LQD under its 12% cap or the sleeve budget limit: equity 99822.62, price 104.64, existing exposure 0.00, headroom 47.32

**In the model's own words:**

> Investment-grade credit fund sitting at the bottom of its 52-week range with 10y at 5.00% and yields up across the belly (+7bp 5y) on the week, a firming dollar (+1.23) and price below 20/50/200d SMAs with 50d under 200d. Duration risk dominates: a 4.7% yield is thin cushion against further rate rises, and the trend and momentum (RSI 39, MACD below signal) corroborate. No policy shock though -- curve normally sloped, VIX easing -- so this is a drift, not a catalyst, hence modest conviction. News items are generic flow roundups and a BND duration-math piece, not LQD-specific evidence. No positioning, flow or analyst roll-up data was on offer, so those are left null.

**Main reasons it gave:**
- Close 104.62, only 4.0% up from 52-week low of 104.28
- Below 20d/50d/200d SMAs with 50d beneath 200d; 3m return -4.1%
- 10-year yield 5.00% (+3bp week), 5-year 4.86% (+7bp)
- Dollar index +1.23 on the week, tightening financial conditions
- 4.7% yield vs 86.8% A/BBB credit mix offers limited cushion to duration losses

<details><summary><b>News</b> — score -0.10</summary>

- [Daily ETF Flows: QQQ Inflows Total Nearly $1B](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-qqq-inflows-210005358.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Here are the daily ETF fund flows for September 16, 2026.
- [A 1-Point Rise in Bond Yields Could Swamp BND’s 4.7% Yield](https://247wallst.com/investing/etf/2026/09/17/a-1-point-rise-in-bond-yields-could-swamp-bnds-4-7-yield/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  BND's 4.7% yield offers less cushion than it appears, given that a 1-point yield rise erases 5.7% of NAV and wipes out more than a full year of income.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 104.62 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 105.44 (-0.8%), 50d 106.12 (-1.4%), 200d 108.79 (-3.8%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -0.513 vs signal -0.481 (histogram -0.033)
Returns: 1d -0.5% | 5d +0.3% | 1m -1.8% | 3m -4.1%
52-week range: 104.28 - 112.92 (now 4.0% of the way up)
Volatility: ATR(14) 0.53 (0.5% of price) | annualised 20d 6.4%
Volume: 0.57x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Developing country bonds (EMB) · Index fund — BEARISH, confidence 0.30

**Result:** REJECTED · no room for broad fund EMB under its 12% cap or the sleeve budget limit: equity 99828.48, price 93.36, existing exposure 11949.44, headroom 55.08

**In the model's own words:**

> EM dollar-debt fund facing a tightening backdrop: 10y at 5.00% and up on the week, 5y +7bp, and a dollar index up 1.23 -- both headwinds for EM credit. Technicals corroborate mildly: price below 20/50/200d SMAs, 50d under 200d, RSI 37.7, MACD below signal, and price sitting only 8% off the 52-week low. Nothing is a decisive break though -- volume is 0.45x average and volatility is low -- so this is a modest tilt rather than a catalyst trade. Fundamentals are mixed: 5.1% yield and +8.8%/yr three-year record against a basket where ~45% is BB or lower. No analyst roll-up and no positioning data for this instrument; flows not provided, so insider dimension left null.

**Main reasons it gave:**
- 10-year Treasury at 5.00%, +3bp on week; 5-year +7bp
- Dollar index +1.23 on the week -- headwind for EM debt
- Price below 20d/50d/200d SMAs with 50d under 200d
- Only 8.4% above 52-week low; RSI 37.7, MACD below signal
- Volume 0.45x 20-day average -- no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Fed Outlook 2026: Rising Rates Are Back. Is Your Bond Portfolio Ready?](https://seekingalpha.com/article/4947891-fed-outlook-2026-rising-rates-back-bond-portfolio-ready)  
  <sub>Seeking Alpha, 42 minutes ago</sub>  
  For investors, we believe bonds offer a compelling opportunity set for income generation.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 93.35 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 94.19 (-0.9%), 50d 94.72 (-1.5%), 200d 95.68 (-2.4%); 50d below 200d
Momentum: RSI(14) 37.7 | MACD -0.468 vs signal -0.391 (histogram -0.077)
Returns: 1d -0.3% | 5d +0.0% | 1m -1.9% | 3m -3.5%
52-week range: 92.95 - 97.74 (now 8.4% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 5.5%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US company bonds, riskier (HYG) · Index fund — BEARISH, confidence 0.30

**Result:** REJECTED · no room for broad fund HYG under its 12% cap or the sleeve budget limit: equity 99830.52, price 78.50, existing exposure 0.00, headroom 57.62

**In the model's own words:**

> HYG sits at the bottom of its 52-week range (78.50 vs low 78.38), below 20/50/200d SMAs with 50d under 200d, RSI 34 and MACD below signal. The macro backdrop is unhelpful: the 10-year at 5.00% and 5-year +7bp on the week, with a firmer dollar (+1.23), keeps duration and spread pressure on high yield. Fundamentals are unremarkable rather than alarming -- 5.9% yield, 57.9% BB and only 8.3% below B, so credit quality is decent; carry partly offsets price drift. No macro news and light volume (0.38x) argue against a strong call, so this is a mild trend-following tilt, not a conviction macro bet. No analyst roll-up or CFTC positioning exists for this instrument; share-count flow data was not provided, so insider_score is null.

**Main reasons it gave:**
- Close 78.50 is 3.9% of the way up the 52-week range, near the 78.38 low
- Below 20d/50d/200d SMAs with 50d below 200d; RSI 33.9, MACD histogram -0.068
- 10-year at 5.00% and 5-year +7bp on the week; dollar index +1.23
- 5.9% yield with 57.9% BB and only 8.3% below B tempers the downside
- Volume just 0.38x 20-day average and no macro news -- weak-conviction drift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 78.50 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 79.15 (-0.8%), 50d 79.39 (-1.1%), 200d 80.03 (-1.9%); 50d below 200d
Momentum: RSI(14) 33.9 | MACD -0.295 vs signal -0.227 (histogram -0.068)
Returns: 1d -0.3% | 5d -0.1% | 1m -1.5% | 3m -1.9%
52-week range: 78.38 - 81.32 (now 3.9% of the way up)
Volatility: ATR(14) 0.23 (0.3% of price) | annualised 20d 4.3%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.05</summary>

```text
Fund type: High Yield Bond
Yield: 5.9%
Credit quality: BB 57.9%, B 32.2%, Below B 8.3%, BBB 1.1%
Three-year record: +7.9% a year | beta to the market 0.67
Cost and size: expense ratio 0.49% | net assets 16.19B
What it is made of: Bonds 98.6%, Cash 1.2%, Preferred 0.2%
Largest holdings: BlackRock Cash Funds Treasury SL Agency 1.3%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.05</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US government bonds, 7-10 years (IEF) · Index fund — BEARISH, confidence 0.30

**Result:** REJECTED · no room for broad fund IEF under its 12% cap or the sleeve budget limit: equity 99830.14, price 90.84, existing exposure 11900.04, headroom 61.06

**In the model's own words:**

> IEF sits at the bottom of its 52-week range with 50d below 200d and yields grinding higher (10y 5.00%, +3bp on the week; 5y +7bp), against a Fed that just hiked to 3.75-4.00% and a dollar up 1.23. That is a coherent bearish rates backdrop rather than a one-day story. Offsetting it: RSI 31.6 is oversold, volume is thin at 0.37x, speculators are already net short 37% of open interest at the 77th percentile (crowded, and they added on the week), and the news notes yields fell Thursday as the market bought the Fed's inflation fight. The headline about AppLovin and the ETF-ratio listicle are irrelevant noise. Net: modest downtrend continuation, low conviction given crowding and stretched momentum.

**Main reasons it gave:**
- Close 90.82, only 1.3% off the 52-week low, 50d SMA below 200d
- 10-year at 5.00% (+3bp wk), 5-year +7bp; Fed hiked to 3.75-4.00%
- RSI 14 at 31.6 with volume 0.37x average — oversold and unconfirmed
- CFTC specs net short 37.1% of OI, +2.0% on week, 77th percentile crowding
- Dollar index +1.23 on week, VIX 15.4 and falling — no flight-to-quality bid

<details><summary><b>News</b> — score -0.10</summary>

- [The Bulls Still Have The Edge, But The Margin Is Narrowing](https://seekingalpha.com/article/4947839-bulls-still-have-edge-but-margin-narrowing)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  A review of several ETF-based market ratios continues to support the view that investors remain broadly constructive on the near-term outlook.
- [Treasury Yields Slide as Markets Buy Into Fed's Inflation Fight](https://finance.biggo.com/news/ce9e6630-2b65-456a-bc4a-49fee3d02f40)  
  <sub>BigGo Finance, 22 hours ago</sub>  
  Treasury yields fell across the curve on Thursday, a day after the Federal Reserve raised interest rates by a quarter point to a range of 3.75% to 4%…
- [Applovin Stock In Focus Amid Reportedly Ongoing SEC Probe; Convequity Says Wait For The Dip Before Investing](https://stocktwits.com/news-articles/markets/equity/applovin-stock-in-focus/cZRNLbcR4xr)  
  <sub>Stocktwits, 18 hours ago</sub>  
  The SEC stated to Bloomberg News that an “investigation involving AppLovin is still active and ongoing”.
- [Elizabeth Warren Calls Kevin Warsh Trump's 'Sock Puppet' - iShares 7-10 Year Treasury Bond ETF (NASDAQ:IE](https://www.benzinga.com/markets/economic-data/26/09/61859653/elizabeth-warren-kevin-warsh-sock-puppet-trump-rate-hike-peter-schiff)  
  <sub>Benzinga, 14 hours ago</sub>  
  Elizabeth Warren and Peter Schiff questioned the Fed's independence after Trump claimed he told Chair Kevin Warsh to vote on the rate hike.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 90.82 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 92.05 (-1.3%), 50d 92.75 (-2.1%), 200d 94.80 (-4.2%); 50d below 200d
Momentum: RSI(14) 31.6 | MACD -0.599 vs signal -0.489 (histogram -0.110)
Returns: 1d -0.5% | 5d -0.2% | 1m -2.7% | 3m -3.7%
52-week range: 90.73 - 97.99 (now 1.3% of the way up)
Volatility: ATR(14) 0.40 (0.4% of price) | annualised 20d 5.3%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Long Government
Yield: 4.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +2.9% a year | beta to the market 1.16
Cost and size: expense ratio 0.15% | net assets 41.82B
What it is made of: Bonds 99.6%, Cash 0.4%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 37.1% of open interest (5,225,295 contracts)
Change on the week: +2.0% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

_Not available today._

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> DBA is an agriculture-focused commodity fund showing mixed technicals and macro crosscurrents. Price is 2.5% below the 20-day SMA and momentum has rolled over (RSI 41.2, MACD histogram negative), suggesting near-term weakness. The 3-month return of +5.7% sits on top of a broader 4% gain versus the 200-day MA, indicating the fund has already captured a meaningful move. Macro conditions are mixed: Treasury yields rose 7bps at the short end this week and the dollar strengthened 1.23% on the week, both headwinds for commodity denominated in USD. The yield curve remains positively sloped at 102bps, which is neutral. Volume is running 37% of the 20-day average, indicating low conviction in either direction. VIX at 15.39 is mildly elevated but not alarming. The fund's underlying commodity exposure (agriculture, shown by the sector breakdown with no clear concentration in energy or metals) lacks a fresh catalyst; no major news or data surprise has occurred in the past 24 hours. The technical setup suggests a consolidation rather than a new leg up, and the macro backdrop—stronger dollar, rising short-term rates—creates headwinds. However, the fund is not yet in clear downtrend (above 200d SMA, in upper half of 52-week range at 66.5%), leaving room for stabilization. Conviction is modest because commodity timing calls lack edge and this situation is genuinely balanced rather than showing a decisive directional break.

**Main reasons it gave:**
- RSI 41 and negative MACD histogram signal momentum rollover
- Dollar index +1.23% on the week is headwind for USD-priced commodities
- Volume 37% of 20-day average shows low conviction in direction
- Price still 4% above 200d SMA prevents clear downtrend call
- Positively sloped yield curve at 102bps and no fresh catalyst limit upside case

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 28.14 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 28.86 (-2.5%), 50d 28.24 (-0.4%), 200d 27.04 (+4.0%); 50d above 200d
Momentum: RSI(14) 41.2 | MACD 0.124 vs signal 0.259 (histogram -0.135)
Returns: 1d -1.0% | 5d -2.7% | 1m -0.5% | 3m +5.7%
52-week range: 25.44 - 29.49 (now 66.5% of the way up)
Volatility: ATR(14) 0.30 (1.1% of price) | annualised 20d 13.1%
Volume: 0.37x the 20-day average
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
Three-year record: +13.3% a year | beta to the market 0.35
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> DBC is a broad commodities basket fund holding 50.6% cash and 44.8% other assets, with the largest real exposure in short-term Treasury ETFs and a small November Brent crude future position. Technicals show the fund near the top of its 52-week range (94.1%) with overbought momentum (RSI 64.4), elevated volatility at 19.1% annualized, and volume well below average at 0.48x. The trend is positive above all major moving averages (+2.8% vs 20d, +8.3% vs 50d, +19.1% vs 200d), but this appears mature: the fund has already rallied 19.4% over three months and sits at resistance. Macro backdrop is mixed: treasury yields rose modestly across the curve this week (+3-7 basis points), the dollar strengthened significantly (+1.23 on the week to 100.35), and the VIX remains elevated at 15.39, suggesting risk-off sentiment. A stronger dollar is typically headwinds for commodity prices. No news or data surprises have occurred to justify a directional move. Analyst coverage is sparse with no price targets provided. The fund's structure (heavy cash drag, low-cost exposure, 0.85% expense ratio) is neutral, but the technical maturity, elevated positioning at 52-week highs, and absence of a fresh catalyst do not support conviction in either direction. The modest positive bias reflects the intact uptrend but tempered by overbought conditions and structural headwinds from dollar strength.

**Main reasons it gave:**
- Price at 94.1% of 52-week range with RSI 64.4 signals overbought conditions
- Dollar index rose +1.23 on week, creating headwinds for commodity prices
- Volume 0.48x 20-day average suggests weak conviction despite positive trend
- Uptrend intact above 50d and 200d moving averages but no fresh catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 32.99 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 32.09 (+2.8%), 50d 30.47 (+8.3%), 200d 27.70 (+19.1%); 50d above 200d
Momentum: RSI(14) 64.4 | MACD 0.862 vs signal 0.852 (histogram 0.011)
Returns: 1d -0.2% | 5d -0.5% | 1m +7.2% | 3m +19.4%
52-week range: 22.07 - 33.68 (now 94.1% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 19.1%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> IWM is showing technical deterioration with the price 3.4-4.2% below its major moving averages, RSI deeply oversold at 32.6, and MACD negative with widening histogram. The fund has declined 6.3% over one month and 4.4% over three months, trading near the lower end of its 52-week range. However, multiple factors constrain a bearish call: macro backdrop is stable with normal yield curve slope, volatility elevated but not extreme at 15.39, and dollar strength this week may be a headwind but not a decisive catalyst. Positioning shows large speculators crowded net short at the 7th percentile—an extreme that often marks inflection points rather than continuation. Fund basics remain reasonable with a 3-year annualized return of 17.1% and valuations not stretched at P/E 17.30. The analyst view is too thin to weight heavily (1.7% coverage), but shows a buy bias and +23.8% price targets on those holdings. A Fed decision is imminent, and breadth data cited shows recent rebound after weakness, suggesting potential for stabilization rather than acceleration lower. The combination of oversold technicals, crowded short positioning, and absence of a clear macro catalyst argues for a neutral stance rather than a directional conviction either way.

**Main reasons it gave:**
- Price 3.4-4.2% below 20d and 50d moving averages; RSI 32.6 deeply oversold
- Large speculators net short at 7th percentile crowding, signaling potential reversal setup
- Yield curve normal and stable; no definitive macro catalyst prior to Fed announcement
- Three-year fund performance +17.1% annualized and analyst targets +23.8% on covered holdings temper downside conviction

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Russell 2000 ETF (IWM) Stock Price | Quotes & News](https://www.moomoo.com/stock/IWM-US?chain_id=Name1K9-3FXPhg.1laj5dg&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2FIWM-US%22%7D)  
  <sub>Moomoo, 7 hours ago</sub>  
  Track the latest iShares Russell 2000 ETF (IWM) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF trading and...
- [Zoomex Highlights ETF Perpetuals Ahead of This Week’s Federal Reserve Decision](https://markets.businessinsider.com/news/stocks/zoomex-highlights-etf-perpetuals-ahead-of-this-week-s-federal-reserve-decision-1036557174)  
  <sub>markets.businessinsider.com, 59 minutes ago</sub>  
  VICTORIA, Seychelles,, Sept. 18, 2026 (GLOBE NEWSWIRE) -- With the U.S. Federal Reserve scheduled to announce its latest interest-rate decision ...
- [Breadth Rebounds Sharply, but the Market Is Not Repaired Yet](https://www.chartmill.com/news/IWM/Chartmill-55012-Breadth-Rebounds-Sharply-but-the-Market-Is-Not-Repaired-Yet)  
  <sub>ChartMill, 5 hours ago</sub>  
  U.S. breadth rebounded sharply on Sept. 17, but weak moving-average and monthly participation keep the breadth trend at 3/7.
- [$30B Flows Into ETFs, IVV Leads With $6.5B Inflows - iShares Core S&P 500 ETF (ARCA:IVV)](https://www.benzinga.com/etfs/broad-u-s-equity-etfs/26/09/61869495/30b-flows-into-etfs-ivv-leads-with-6-5b-inflows)  
  <sub>Benzinga, 2 hours ago</sub>  
  U.S. ETFs attracted nearly $30B in daily inflows on Wednesday, led by IVV with $6.5B. VUG, VO and VTV also ranked among the top ETF creations.
- [Portfolio Fit: PJSM](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-pjsm/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  The PGIM Jennison Small-Mid Cap Core Equity ETF (NYSEARCA:PJSM) is one of the newest actively managed small- and mid-cap funds on the market,...
- [Triple Witching Day Analysis: SPY Pinned, QQQ Free, IWM Hedged, NVDA Chased, TSLA Capped](https://www.moomoo.com/community/feed/triple-witching-day-analysis-spy-pinned-qqq-free-iwm-hedged-117290914480134)  
  <sub>Moomoo, 9 hours ago</sub>  
  by Monta HONG, CFA | Options Strategist $SPDR S&P 500 ETF (SPY.US)$ was the one still pinned. It stayed wedged between its 760 put wall and 765 call w...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 282.59 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 292.41 (-3.4%), 50d 295.11 (-4.2%), 200d 274.82 (+2.8%); 50d above 200d
Momentum: RSI(14) 32.6 | MACD -3.524 vs signal -2.348 (histogram -1.176)
Returns: 1d -1.0% | 5d -2.2% | 1m -6.3% | 3m -4.4%
52-week range: 229.11 - 305.09 (now 70.4% of the way up)
Volatility: ATR(14) 3.53 (1.2% of price) | annualised 20d 12.0%
Volume: 0.83x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Small Blend
What it holds: P/E 17.30 | P/B 2.13 | P/S 1.31 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +17.1% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: JFrog Ltd Ordinary Shares 0.3%, Moog Inc Class A 0.3%, BlackRock Cash Funds Treasury SL Agency 0.3%, UMB Financial Corp 0.3%, Glaukos Corp 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.1%, Technology 13.8%, Industrials 13.2%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.8% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
  - GKOS: 2026-08-20 BTIG: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.35</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 25.5% of open interest (431,147 contracts)
Change on the week: +0.2% of open interest
Crowding: 7% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.35</summary>

_Not available today._

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> SHY is a short-duration government bond fund with a 3.6% yield and AA-rated holdings. Macro backdrop shows the 3-month yield at 3.98% (up 7bp this week) and the curve in normal upward slope at 102bp. The technical picture is decidedly weak: price is below all major moving averages (20d, 50d, 200d in downtrend), RSI at 29.7 signals oversold conditions, MACD histogram is negative, and the fund is down 1.0% over one month. However, conviction is modest because several cross-currents complicate the outlook. The fund's 3-month yield rising faster than longer yields (5-year and 10-year rose only 7bp and 3bp respectively) could support slightly higher rates ahead for short paper, which would modestly benefit a short-duration fund on yield rolldown. The CFTC positioning data (as of Sept 8, now stale) shows large speculators at 95th percentile crowding in a net short -- an extreme that is as often the end of a move as the middle. Fund flows and insider activity cannot be scored from this data. The technical oversold reading (RSI 29.7) could attract tactical buyers after a 1% monthly decline, offsetting some near-term downside risk. Headline sentiment remains constructively tilted, though the news score is mixed: one item notes a narrowing bull margin. Volume is below average, suggesting limited conviction behind either direction. No material catalyst has moved this week -- rates have drifted higher in a normal curve, and the Fed's recent action is already priced. This warrants a modest bullish lean on technicals and yield dynamics, but conviction is capped by the lack of a fresh catalyst and the crowded short positioning.

**Main reasons it gave:**
- RSI at 29.7 signals oversold conditions after 1% monthly decline
- Large speculators at 95th percentile crowding in net short position (as of Sept 8)
- 3-month yield up 7bp this week vs 3bp-7bp for longer tenors, supporting short-duration rolldown
- Price below all major moving averages with MACD histogram negative
- Below-average trading volume suggests weak conviction in either direction

<details><summary><b>News</b> — score +0.15</summary>

- [The Bulls Still Have The Edge, But The Margin Is Narrowing](https://seekingalpha.com/article/4947839-bulls-still-have-edge-but-margin-narrowing)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  A review of several ETF-based market ratios continues to support the view that investors remain broadly constructive on the near-term outlook.
- [Short-Term Bond ETFs to Gain as Fed Hikes Interest Rates](https://www.tradingview.com/news/zacks:4048914bf094b:0-short-term-bond-etfs-to-gain-as-fed-hikes-interest-rates/)  
  <sub>TradingView, 22 hours ago</sub>  
  In a historic shift for monetary policy, the Federal Reserve raised its benchmark federal funds rate by 25 basis points to a target range of 3.75-4.00% on...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 81.28 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 81.66 (-0.5%), 50d 81.82 (-0.7%), 200d 82.35 (-1.3%); 50d below 200d
Momentum: RSI(14) 29.7 | MACD -0.172 vs signal -0.131 (histogram -0.041)
Returns: 1d -0.1% | 5d -0.1% | 1m -1.0% | 3m -0.9%
52-week range: 81.24 - 83.18 (now 1.8% of the way up)
Volatility: ATR(14) 0.10 (0.1% of price) | annualised 20d 1.9%
Volume: 0.78x the 20-day average
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
Three-year record: +4.0% a year | beta to the market 0.22
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
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 29.7% of open interest (4,346,314 contracts)
Change on the week: -0.5% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### US inflation-linked bonds (TIP) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> TIP is a TIPS (Treasury Inflation-Protected Securities) fund trading below all major moving averages: down 1.1% from the 20-day SMA, 1.6% from the 50-day, and 3.8% from the 200-day. The 50-day trading below the 200-day signals a downtrend. Momentum is weak, with RSI at 29.1 (near oversold) and MACD histogram negative. Volume is below average, indicating low conviction behind the move. Technically, the fund sits at the low end of its 52-week range with no decisive reversal signal. Macro conditions are mixed: Treasury yields have risen moderately across the curve (3-month and 5-year both +7bp on the week), which is modestly bearish for TIPS since higher real rates reduce their relative appeal. The yield curve remains normal at +1.02 points. The dollar has strengthened (+1.23 on the week), which can be modestly supportive for US bonds. VIX at 15.39 remains mildly elevated. TIPS fundamentals remain solid: 5.0% yield, AA 99.9% credit quality, but the fund's beta of 0.68 to equities offers limited downside protection in a non-crisis environment. CFTC data shows large speculators are net short 37.1% of the 10Y note contract (up 2.0% on the week), placing them near historical crowding at the 77th percentile—suggesting the bearish positioning is neither extreme nor new. News is macro-focused (inflation, housing, sentiment) with no catalyst material enough to shift a broad duration trade. The technical weakness is notable but not dramatic, and positioning data is stale (from Sept 8). Without a clear catalyst—inflation surprise, Fed pivot, or decisive technical break—a NEUTRAL stance is appropriate. The mild technical deterioration and rising rates temper optimism, but oversold RSI and solid fundamentals prevent a bearish call.

**Main reasons it gave:**
- price down 3.8% vs 200d MA in established downtrend
- RSI 29.1 near oversold but volume below average shows weak conviction
- 3-month and 5-year yields up 7bp on week, modestly bearish for TIPS real rates
- large speculators net short at 77th percentile crowding, not at an extreme

<details><summary><b>News</b> — score +0.00</summary>

- [Nearly Half of Homebuyers Get Concessions From Sellers as Most Markets Tip in Buyers' Favor](https://finance.yahoo.com/real-estate/articles/nearly-half-homebuyers-concessions-sellers-120000954.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Redfin reports concessions are especially common in Sun Belt buyer's markets, including Atlanta and Nashville, where about 7 in 10 homebuyers are getting...
- [The Bulls Still Have The Edge, But The Margin Is Narrowing](https://seekingalpha.com/article/4947839-bulls-still-have-edge-but-margin-narrowing)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  A review of several ETF-based market ratios continues to support the view that investors remain broadly constructive on the near-term outlook.
- [Inflation nation: Are record income gains already gone?](https://seekingalpha.com/news/4644286-inflation-nation-are-record-income-gains-already-gone)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Census data: 2025 real median household income hit a record, but gains skewed to top earners; poverty fell and inflation threatens wages.
- [İş Yatırım Reports ETF Market-Making Activity in ISMDL](https://www.tipranks.com/news/company-announcements/is-yatirim-reports-etf-market-making-activity-in-ismdl)  
  <sub>TipRanks, 3 hours ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) has shared an announcement. İş Yatırım Menkul Değerler A.Ş., a Turkish investment services firm,...
- [Bloomberg Analyst Tips Bitcoin ETFs To Triple Gold - Here's The Trigger](https://coincodex.com/article/92219/bloomberg-analyst-tips-bitcoin-etfs-to-triple-gold-heres-the-trigger/)  
  <sub>CoinCodex, 4 hours ago</sub>  
  Bitcoin ETFs could surpass gold ETFs by a wide margin as lower volatility, institutional adoption, and stronger distribution fuel demand.
- [İş Yatırım Discloses ISX30 ETF Market-Making Transactions for 17 September 2026](https://www.tipranks.com/news/company-announcements/is-yatirim-discloses-isx30-etf-market-making-transactions-for-17-september-2026)  
  <sub>TipRanks, 3 hours ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) has issued an announcement. İş Yatırım Menkul Değerler A.Ş. reported its market-making activity in the ISX30...
- [Is Yatirim Reports No ETF Market-Making Trades on 17 September 2026](https://www.tipranks.com/news/company-announcements/is-yatirim-reports-no-etf-market-making-trades-on-17-september-2026)  
  <sub>TipRanks, 3 hours ago</sub>  
  Is Yatirim Menkul Degerler AS ( ($TR:ISMEN) ) has issued an announcement. Is Yatirim Menkul Degerler AS reported that on 17 September 2026 it did not...
- [Bitwise’s Solana Staking ETF Sees Modest Outflow as SOL Rally Pauses for Breath](https://www.tipranks.com/news/cryptocurrencies/bitwises-solana-staking-etf-sees-modest-outflow-as-sol-rally-pauses-for-breath)  
  <sub>TipRanks, 4 hours ago</sub>  
  Bitwise Solana Staking ETF's BSOL saw its first notable outflow in weeks, with $1.37 million exiting the fund on September 11, 2026.
- [Leveraged Bitcoin ETF Feels the Pinch as Traders Pull Cash Despite Underlying Rally](https://www.tipranks.com/news/cryptocurrencies/leveraged-bitcoin-etf-feels-the-pinch-as-traders-pull-cash-despite-underlying-rally)  
  <sub>TipRanks, 5 hours ago</sub>  
  Bitcoin-Leveraged ETF Sees Investor Chill as Outflows Nip at AUM ProShares Ultra Bitcoin ETF, ticker BITU, recorded net outflows of $1002967 on August 28,...
- [Hemlo Mining Added to VanEck Junior Gold Miners ETF](https://www.tipranks.com/news/company-announcements/hemlo-mining-added-to-vaneck-junior-gold-miners-etf)  
  <sub>TipRanks, 5 hours ago</sub>  
  Hemlo Mining ( ($TSE:HMMC) ) has shared an announcement. Hemlo Mining Corp., a Canadian gold producer centered on the long‑running Hemlo gold camp in...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 105.42 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 106.63 (-1.1%), 50d 107.13 (-1.6%), 200d 109.63 (-3.8%); 50d below 200d
Momentum: RSI(14) 29.1 | MACD -0.485 vs signal -0.361 (histogram -0.123)
Returns: 1d -0.3% | 5d -0.4% | 1m -1.9% | 3m -3.6%
52-week range: 105.39 - 112.20 (now 0.4% of the way up)
Volatility: ATR(14) 0.35 (0.3% of price) | annualised 20d 3.9%
Volume: 0.61x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Inflation-Protected Bond
Yield: 5.0%
Credit quality: AA 99.9% | US government debt 99.9%
Three-year record: +3.5% a year | beta to the market 0.68
Cost and size: expense ratio 0.18% | net assets 15.01B
What it is made of: Bonds 99.9%, Cash 0.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 37.1% of open interest (5,225,295 contracts)
Change on the week: +2.0% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Long Treasuries are in a clear downtrend (below 20/50/200d, 50d under 200d, 4% off 52-week lows, -6.4% in 3 months) with front-end yields still rising and the dollar firm, but the 30-year actually fell 2bp on the week and RSI at 42 is not decisive; volume is 0.59x average, so there is no break to trade. Spec positioning in ultra bonds is net short 36% of OI but only at the 33rd percentile, i.e. normal crowding. No fresh rate surprise beyond an already-digested quarter-point hike, so the honest answer is no side, with a mild bearish tilt from trend. Promotional 'why long bonds beat stocks' pieces and single-fund mandate/listicle news are noise and were discounted.

**Main reasons it gave:**
- Price 81.21 below 20d/50d/200d with 50d under 200d; 4.4% off 52-week low
- 10-year 5.00% (+3bp) and 5-year +7bp on the week while 30-year -2bp; curve normal at +1.02
- Volume 0.59x 20-day average, no confirmed breakdown; RSI 42.5, MACD histogram near flat
- Large specs net short 36% of ultra bond OI but only 33rd percentile crowding, +0.6% w/w
- Fed already hiked to 3.75-4% with yields subsequently falling -- no new policy surprise this cycle

<details><summary><b>News</b> — score +0.05</summary>

- [TLTW: Mandate Change Prompts A Downgrade (BATS:TLTW)](https://www.google.com/goto?url=CAESiAEB6zswFaMgTs4WCuPFDdUXZEFOJ186voX2DwQ7t_kcGXSKE5gPf0cFbj1HkmkZbBkXq-MFyigfJauRc-iZBlkCop9WM9yFegYr1_slLPZFMp3KtKAyme1b-aSjsV54Bjq7uNI4UJKu4bYgFne0cdNW3L_NeoEG5dkoci4mqD9B3HEksbvEFO5l)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  iShares 20+ Year Treasury Bond BuyWrite Strat ETF (TLTW) will change its mandate and name to 'iShares TLT Premium Income+ ETF' in October 2026.
- [Portfolio Fit: TSCZ](https://www.google.com/goto?url=CAESegHrOzAVokFNeacP_nAinZqTZd5i__cpPKE0W7FvLKj9WeJDKbXe-YyQZaQ3fcngLrhg5I0-i-IKapO4eXXtS7j2s45o_fTbMnHitXnnXAkDjZkaLArOeY4hBVde8Wzikt8C-xmHdWOZuLlJ_waUvzsQP1j-PMw8NjLV)  
  <sub>24/7 Wall St., 28 minutes ago</sub>  
  Investors hunting for fixed-income yield without stretching into corporate credit have a new option to consider: the T. Rowe Price Securitized Income ETF...
- [Rising 20-year yields and high equity risk prem...](https://pluang.com/en/news-feed/tlt-etf-analisis-y-peluang-investasi-pada-obligasi-pemerintah-20-tahun)  
  <sub>Pluang, 13 hours ago</sub>  
  The article discusses the current attractiveness of the TLT ETF, which tracks long-term government bonds, amid elevated 20-year yields around 5.3%.
- [TLT: My Father Taught Me Not To Speculate On Rates, I'm About To Do It With This ETF](https://www.google.com/goto?url=CAESmAEB6zswFeW6CIg8UMyP3x-NY67tD2ZSlNZcifHt4ht_iGN6dZimij9n6n8fnc3E1v6Xhj1el9tzpR3bvyyuaKr4wPyR_IS3pPxfks3BJOTCifGK1r8EMrpkhj6UHAlKjNwzduqeBrYrkYZUUzsVu4-304yrntCIPdnWXc_nQOIcg_QG1qDbWFXx9duZwPMuv-zJ14E9piLUNg)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  Considering TLT now? With 20-year yields near 5.3%, a rising equity risk premium, and strong convexity, see why long bonds may beat stocks.
- [Daily ETF Flows: QQQ Inflows Total Nearly $1B](https://www.google.com/goto?url=CAESlQEB6zswFfBnaPPQ2KqVXnqnMCdhj1czsgEMJBQmcUS3_ZAVxCDLbMW-Il-SYT777RlqtnulL_nNb34H21FAAYFgId485TL-J_uvrh5p5QBxMdpn2yIC53AgFPr_qL9w_q2rZiplIZe27EXAZ0jZ3lqZ0EN5apJHsFPmvhu-79RI4FUC1LjBc2ud5Ku6XRJYQ9FiT9Lh4A)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Here are the daily ETF fund flows for September 16, 2026.
- [IShares 20+ Year Treasury Bond ETF Options Spot-On: On September 17th, 973.19K Contracts Were Traded, With 13.35 Million Open Interest](https://www.google.com/goto?url=CAESlQEB6zswFWxEzpCIPNonQiQ8x7HUg1eBdNA9v0CL8MqlCuhoKDYDKdD96ersryM6tQVpRdmhgPFiM5AEV979UiGpOQMRS3pFYP6cnGS5FQyw7N0MAmPgZQVmHmE8rnVLui36y2fMrdSxMkD-0z4rA9T-4w-bTAZMk6Crku882OJKbLCYMmSLCmM99YaDhxbwgfrEmlLeyQ)  
  <sub>富途牛牛, 20 hours ago</sub>  
  OnSeptember 17th ET, $iShares 20+ Year Treasury Bond ETF(TLT.US)$ had active options trading, with a total trading volume of 973.19K options for the day,...
- [Dow, S&P 500 Futures Slip While Nasdaq Holds Firm As Trump Reinstates Hormuz Blockade: ORCL, SOUN, QTTB, FAC In Focus](https://www.google.com/goto?url=CAES0QEB6zswFdzNIRBgsKBrerZkv1R8bjdW3ujcXfdaZXch00uhI2o3aANHSs-gRQW436HMaXgn75RNrM64disSj3u_QXRrai4rJap_8RVBAgejaNNZmOSNv0xdDfVZNm3VC1yq-WkQr3l_1JxI6h0VeJCkIcNLYM1f05QzadA5eY4wl7sr-58gTVqzVrY87WKmX6dHNm8uDVsaTjM9wMDFtsru16ft4MFNbdrrjGtYjJTic-nHpO7nKeDFtdRRocj_a6S_4s12qm3DbDdroIIfT2d4aQ)  
  <sub>Stocktwits, 19 hours ago</sub>  
  The U.S.A. will be, from this point forward, known as 'THE GUARDIAN OF THE HORMUZ STRAIT,'” Trump said on social media.
- [How Defined-Maturity Bond ETFs Could Help You Outperform the S&P 500 Over the Next 5-10 Years](https://www.inkl.com/news/how-defined-maturity-bond-etfs-could-help-you-outperform-the-s-p-500-over-the-next-5-10-years)  
  <sub>inkl, 23 hours ago</sub>  
  Vanguard's launch of the BondBuilder Target Maturity ETF suite, charging an expense ratio of 0.08% or $8 on an initial $10,000 investment, just added fuel...
- [A 1-Point Rise in Bond Yields Could Swamp BND’s 4.7% Yield](https://247wallst.com/investing/etf/2026/09/17/a-1-point-rise-in-bond-yields-could-swamp-bnds-4-7-yield/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  BND's 4.7% yield offers less cushion than it appears, given that a 1-point yield rise erases 5.7% of NAV and wipes out more than a full year of income.
- [Treasury Yields Slide as Markets Buy Into Fed's Inflation Fight](https://www.google.com/goto?url=CAESewHrOzAVVAjlkUI-BOHUckq1oX_zSzfrb4pInvSHXQDt_-YGChCEenOEqIDXydOPrQb_OvaiYHxbRMCh36oQHRhxfpATnnofm3FficyyIe30lmqFoZQpe5ezxngIqGJdw4wT0MVekUL6DVSjxKvmW8RA6jWdb6CVnsfpjA)  
  <sub>BigGo Finance, 22 hours ago</sub>  
  Treasury yields fell across the curve on Thursday, a day after the Federal Reserve raised interest rates by a quarter point to a range of 3.75% to 4%…

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 81.21 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 81.95 (-0.9%), 50d 82.61 (-1.7%), 200d 85.87 (-5.4%); 50d below 200d
Momentum: RSI(14) 42.5 | MACD -0.477 vs signal -0.454 (histogram -0.023)
Returns: 1d -0.7% | 5d +0.4% | 1m -2.2% | 3m -6.4%
52-week range: 80.71 - 92.06 (now 4.4% of the way up)
Volatility: ATR(14) 0.70 (0.9% of price) | annualised 20d 9.1%
Volume: 0.59x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.05</summary>

```text
Fund type: Long Government
Yield: 4.7%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: -0.4% a year | beta to the market 2.39
Cost and size: expense ratio 0.15% | net assets 47.05B
What it is made of: Bonds 99.6%, Cash 0.4%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.05</summary>

_Not available today._

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 36.0% of open interest (2,399,505 contracts)
Change on the week: +0.6% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

_Not available today._

</details>

### US dollar (UUP) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> UUP tracks the USD Index, which has rallied sharply this week (+1.23%) to 100.35, pushing the dollar to the 91st percentile of its 52-week range. Technicals show the fund above all major moving averages with positive momentum (RSI 63.9, MACD positive), supporting the near-term uptrend. However, several factors argue for caution on extension: (1) large speculators are at the 93rd percentile of crowding in a net long position, which typically marks the maturity of a move rather than its beginning; (2) positioning deteriorated by -3.6% of open interest on the week, showing the crowd is reducing exposure into strength; (3) the yield curve has normalized (10y-3m spread at +102bps vs inverted) and Treasury yields rose only modestly (+3-7bps across the curve), limiting the fundamental tailwind for dollar strength; (4) volume is 0.54x average, suggesting thin participation in the move; (5) the fund is 100% cash with a 3.3% yield and negative 9.48 beta to equities, making it a volatility hedge more than a directional bet. The technicals are constructive but the positioning and the weakening intensity of the move argue against adding conviction. A NEUTRAL stance reflects the near-term strength tempered by signs of crowding and positioning deterioration.

**Main reasons it gave:**
- Large speculators at 93rd percentile crowding in net long, positioning down 3.6% on the week
- Dollar index at 91% of 52-week range with above-average moving averages but below-average volume
- Yield curve normalized to +102bps; Treasury yield moves modest despite dollar strength
- Fund composition 100% cash with -9.48 beta to equities, limiting directional leverage

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.40</summary>

```text
Last close 28.41 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 28.11 (+1.1%), 50d 28.21 (+0.7%), 200d 27.72 (+2.5%); 50d above 200d
Momentum: RSI(14) 63.9 | MACD 0.049 vs signal 0.000 (histogram 0.049)
Returns: 1d +0.1% | 5d +1.2% | 1m +1.9% | 3m +0.4%
52-week range: 26.47 - 28.60 (now 91.1% of the way up)
Volatility: ATR(14) 0.10 (0.4% of price) | annualised 20d 4.6%
Volume: 0.54x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

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
Rolled up from the 1 largest holdings, 48.8% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: AGPXX
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 10.7% of open interest (57,858 contracts)
Change on the week: -3.6% of open interest
Crowding: 93% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

_Not available today._

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> VGK (Vanguard FTSE Europe ETF) shows mixed signals that do not justify a directional call. The technical picture is weak: the fund has broken below its 20-day, 50-day and is tracking slightly above only its 200-day average; momentum is deteriorated with RSI at 34.1 and MACD histogram significantly negative; price has fallen 4.6% over one month despite remaining in the upper two-thirds of its 52-week range. Fund positioning is crowded at the 98th percentile, which historically marks either momentum exhaustion or vulnerability to a reversal rather than a signal to chase. The macro backdrop adds headwinds: the US dollar has strengthened sharply (+1.23 on the week to 100.35), which is a headwind for dollar-based investors in European equities; Treasury yields have risen across the short and intermediate curve, potentially increasing the opportunity cost of equity exposure. Offsetting these negatives, the fund's valuation metrics are modest (P/E 17.85, P/B 2.31), the yield at 2.8% is reasonable, three-year performance has been solid at +17.4%, and analyst sentiment on the five largest holdings (11.4% of the fund) is constructive with a weighted price target +18.1% above current levels. However, that analyst coverage is thin and applies to less than 12% of the fund. The VIX at 15.39 is slightly elevated but not alarming. No major policy or data surprise has occurred to justify a directional move. The technical deterioration, crowded positioning, and dollar strength combine to argue for patience rather than action at current levels.

**Main reasons it gave:**
- Price broke below 20d and 50d SMAs; RSI 34 and negative MACD histogram signal momentum deterioration
- Crowded long at 98th percentile of 52-week positioning distribution; historically marks vulnerability
- US dollar +1.23 on week to 100.35, headwind for European equity exposure in dollars
- Analyst price target +18.1% on largest 11.4% of holdings offers some offset, but coverage is thin
- Valuation modest at P/E 17.85 and 2.8% yield support longer-term case but do not justify entry into technical weakness

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Thales SA Stocks](https://www.tradingview.com/symbols/VIE-THAL/etfs/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore funds investing in THAL in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 88.01 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 90.87 (-3.1%), 50d 90.55 (-2.8%), 200d 87.35 (+0.8%); 50d above 200d
Momentum: RSI(14) 34.1 | MACD -0.675 vs signal -0.298 (histogram -0.377)
Returns: 1d -1.5% | 5d -2.2% | 1m -4.6% | 3m -0.3%
52-week range: 77.90 - 93.19 (now 66.2% of the way up)
Volatility: ATR(14) 0.88 (1.0% of price) | annualised 20d 11.1%
Volume: 1.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Europe Stock
What it holds: P/E 17.85 | P/B 2.31 | P/S 1.64 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +17.4% a year | beta to the market 0.90
Cost and size: expense ratio 0.06% | net assets 39.06B
What it is made of: Stocks 99.0%, Cash 0.7%, Other 0.3%
Largest holdings: ASML Holding NV 4.0%, HSBC Holdings PLC 2.2%, Roche Holding AG Ordinary Shares new 1.9%, Novartis AG Registered Shares 1.7%, Shell PLC 1.6%
Sector mix: Financial services 25.3%, Industrials 19.8%, Healthcare 12.1%, Technology 9.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.10 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.1% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 5.1% of open interest (477,461 contracts)
Change on the week: -0.6% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

_Not available today._

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.25

**In the model's own words:**

> VWO trades near 52-week highs with a constructive long-term trend (50d above 200d, +3.6% vs 200d SMA) but shows weakness on intermediate timeframes: down 1.7% over three months, below its 20-day SMA by 1.1%, with momentum divergence (RSI 46.8, MACD histogram negative). The macro backdrop is mixed: Treasury yields rose modestly across the curve this week with the dollar up 1.23%, which typically headwinds EM assets, though the yield curve remains normal and VIX at 15.39 is not extreme. CFTC positioning in EM index futures shows large speculators at only 55th percentile crowding—within normal range with minimal weekly change, suggesting no conviction shift among sophisticated players. Fund flows and structural positioning provide no clear directional signal. Analyst coverage of the top 22.2% of holdings shows unanimous buy ratings with +38% upside, but this thin coverage (limited to Taiwan semis and Chinese tech) does not represent the full emerging markets opportunity set and likely overstates consensus. Valuation at P/E 15.91 appears reasonable but uncompelling in context of rising US rates. Three-month performance of -1.7% and below-average volume (0.38x 20d) suggest momentum is stalled. The fund lacks a clear near-term catalyst: no data surprise, no decisive technical break, rate moves are incremental rather than structural, and positioning is neutral. Long-term fundamentals remain intact but near-term evidence does not justify a directional lean.

**Main reasons it gave:**
- Dollar strength +1.23 on week headwinds EM translation
- MACD histogram negative despite price near 52-week highs signals momentum divergence
- Large spec positioning at 55th percentile crowding—no directional consensus
- Analyst upside +38% limited to 22.2% of fund (Taiwan semis, Chinese tech), thin coverage
- Three-month return -1.7% with below-average volume suggests stalled momentum

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Hua Hong Grace Semiconductor Limited Stocks](https://www.tradingview.com/symbols/TRADEGATE-1HH/etfs/)  
  <sub>TradingView, 13 hours ago</sub>  
  Explore funds investing in 1HH in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 59.76 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 60.40 (-1.1%), 50d 59.68 (+0.1%), 200d 57.66 (+3.6%); 50d above 200d
Momentum: RSI(14) 46.8 | MACD -0.068 vs signal 0.113 (histogram -0.181)
Returns: 1d -0.2% | 5d -1.0% | 1m -0.5% | 3m -1.7%
52-week range: 52.42 - 61.44 (now 81.4% of the way up)
Volatility: ATR(14) 0.60 (1.0% of price) | annualised 20d 11.9%
Volume: 0.38x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Diversified Emerging Mkts
What it holds: P/E 15.91 | P/B 2.13 | P/S 1.86 | 3y earnings growth n/a
Yield: 2.3%
Three-year record: +16.9% a year | beta to the market 0.75
Cost and size: expense ratio 0.06% | net assets 168.36B
What it is made of: Stocks 95.3%, Cash 4.6%, Other 0.1%, Preferred 0.0%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 14.7%, Tencent Holdings Ltd 2.9%, Alibaba Group Holding Ltd Ordinary Shares 2.2%, MediaTek Inc 1.5%, Delta Electronics Inc 0.9%
Sector mix: Technology 31.8%, Financial services 20.2%, Consumer cyclical 9.9%, Basic materials 7.9%
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
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +38.0% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 4.2% of open interest (1,068,575 contracts)
Change on the week: +0.1% of open interest
Crowding: 55% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

## Sector and country funds

### US house builders (XHB) · Sector or country — BEARISH, confidence 0.40

**Result:** REJECTED · no room for focused fund XHB under its 7% cap or the sleeve budget limit: equity 99813.99, price 96.07, existing exposure 0.00, headroom 18.08

**In the model's own words:**

> Homebuilder/consumer-cyclical basket is in a clear downtrend (-11% in a month, 50d below 200d, price 4.5% off the 52-week low) against a genuinely hostile rate backdrop: a surprise Fed hike to 3.75-4.00%, 10-year at 5.00% and 30-year mortgage rates above 7%, which directly hits the housing demand this fund is levered to (beta 1.46). Dollar up on the week adds to tightening. Offsets are real but secondary: RSI 31.8 is oversold, volume is light (0.43x), and analyst targets on the top 20.9% of weight sit 23% above spot -- though that slice is thin and targets lag. The XRT listicle headline is noise. Modest bearish tilt rather than a high-conviction short given how stretched the move already is.

**Main reasons it gave:**
- Fed hiked 25bp to 3.75-4.00%, first hike since 2023
- 30-year mortgage rates above 7%, 10-year Treasury at 5.00%
- Price -11.2% in a month, 50d SMA below 200d, 4.5% off 52-week low
- RSI 31.8 oversold and volume only 0.43x average, limiting downside conviction
- Analyst roll-up covers just 20.9% of fund but shows +23.4% target upside

<details><summary><b>News</b> — score -0.50</summary>

- [Is State Street SPDR S&P Retail ETF (XRT) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/state-street-spdr-p-retail-102003647.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Making its debut on 06/19/2006, smart beta exchange traded fund State Street SPDR S&P Retail ETF (XRT) provides investors broad exposure to the Consumer...
- [Flow Focus | Warsh Hit the Tape. Triple Witching Comes Next. Where to Look?](https://www.moomoo.com/community/feed/flow-focus-warsh-hit-the-tape-triple-witching-comes-next-117291397349382)  
  <sub>Moomoo, 7 hours ago</sub>  
  Kevin Warsh made his move. On Wednesday the Fed raised rates a quarter point to 3.75-4.00% -- its first hike since 2023, a unanimous vote. The $U.S. 1...
- [U.S. Housing Market: From Bad To Worse](https://seekingalpha.com/article/4947894-us-housing-market-from-bad-to-worse?source=google_editors_picks)  
  <sub>Seeking Alpha, 47 minutes ago</sub>  
  The housing sector is facing mounting headwinds as 30-year mortgage rates surpass 7%, significantly impacting housing affordability. Click for more on this.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.50</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 96.07 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 101.28 (-5.2%), 50d 105.26 (-8.7%), 200d 106.67 (-9.9%); 50d below 200d
Momentum: RSI(14) 31.8 | MACD -2.707 vs signal -2.314 (histogram -0.393)
Returns: 1d -1.0% | 5d -2.4% | 1m -11.2% | 3m -13.5%
52-week range: 94.86 - 121.36 (now 4.5% of the way up)
Volatility: ATR(14) 2.22 (2.3% of price) | annualised 20d 19.0%
Volume: 0.43x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 19.52 | P/B 2.34 | P/S 1.36 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +7.9% a year | beta to the market 1.46
Cost and size: expense ratio 0.35% | net assets 1.33B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Installed Building Products Inc 4.4%, Owens-Corning Inc 4.3%, Allegion PLC 4.3%, Champion Homes Inc 4.1%, Williams-Sonoma Inc 3.9%
Sector mix: Consumer cyclical 60.7%, Industrials 37.9%, Real estate 1.5%
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
Rolled up from the 5 largest holdings, 20.9% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 73.5% | hold 26.5% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.4% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-15 Stifel: init, ? -> Buy
  - OC: 2026-09-11 Wells Fargo: main, Overweight -> Overweight
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-08-06 UBS: main, Buy -> Buy
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
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

### US electricity and water (XLU) · Sector or country — BEARISH, confidence 0.35

**Result:** REJECTED · no room for focused fund XLU under its 7% cap or the sleeve budget limit: equity 99813.32, price 41.12, existing exposure 0.00, headroom 22.94

**In the model's own words:**

> XLU closed at the very bottom of its 52-week range, below 20/50/200-day averages with a 50d/200d death cross and negative MACD; the rate backdrop is the driver, with the 10-year at 5.00% (+3bp) and 5-year +7bp on the week plus a firmer dollar, which is direct pressure on a bond-proxy, 2.8%-yield sector. Fundamentals are unremarkable (P/E 19 for a low-growth sector) and analyst roll-up is constructive but covers only 39% of the fund and lags price. RSI 31.5 and light volume argue against pressing, so conviction stays modest; single-name Cramer noise on NEE is ignored as irrelevant to the basket. No fund-flow or positioning data, so insider_score is null.

**Main reasons it gave:**
- Close 41.13 at the 52-week low, 0% of the way up the range
- 50d SMA below 200d; price -6.1% vs 50d, -7.7% vs 200d, MACD below signal
- 10-year yield at 5.00% (+3bp) and 5-year +7bp on the week — headwind for a 2.8%-yield bond proxy
- Dollar index +1.23 on the week, VIX subdued at 15.4 (risk-on rotation away from defensives)
- Analyst roll-up bullish (+22.4% targets, 70.6% buy) but only covers 39.4% of fund weight
- RSI 31.5 and 0.48x volume argue the downside is already partly discounted

<details><summary><b>News</b> — score -0.10</summary>

- [Leading And Lagging Sectors For September 18, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61867052/leading-and-lagging-sectors-september-18-2026)  
  <sub>Benzinga, 4 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLC) State Street Communication Services Select Sector SPDR ETF 112.6400 0.290 0.25 1.0K...
- [Webcast: Active ETFs are capturing investor attention - here’s why | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/14/active-etfs-are-capturing-investor-attention-heres-why?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 5 minutes ago</sub>  
  What's driving the rapid growth of active ETFs, and what could it mean for client portfolios? Join Fidelity Investments to explore the forces behind the...
- [Nasdaq 100 Rallies as Oil Slides, Yields Retreat: Stock Market Today](https://www.tradingview.com/news/benzinga:004d73752094b:0-nasdaq-100-rallies-as-oil-slides-yields-retreat-stock-market-today/)  
  <sub>TradingView, 23 hours ago</sub>  
  U.S. stocks rebounded sharply Thursday, erasing two sessions of losses as crude oil retreated from its geopolitical spike and Treasury yields eased back...
- [NextEra Energy stock reacts to Cramer sell call amid Dominion merger and earnings beat](https://www.ad-hoc-news.de/boerse/news/corporate-news/nextera-energy-stock-reacts-to-cramer-sell-call-amid-dominion-merger-and/70124887)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  NextEra Energy stock is up around 18 percent over the past year as of September 18, 2026, but a fresh Jim Cramer sell call puts the rally into question.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.10</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 41.13 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 42.54 (-3.3%), 50d 43.82 (-6.1%), 200d 44.55 (-7.7%); 50d below 200d
Momentum: RSI(14) 31.5 | MACD -0.657 vs signal -0.542 (histogram -0.115)
Returns: 1d -1.3% | 5d -3.0% | 1m -6.6% | 3m -8.1%
52-week range: 41.13 - 47.73 (now 0.0% of the way up)
Volatility: ATR(14) 0.62 (1.5% of price) | annualised 20d 15.5%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +11.7% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
Sector mix: Utilities 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 70.6% | hold 29.4% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +22.4% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - SO: 2026-08-21 Morgan Stanley: main, Underweight -> Underweight
  - DUK: 2026-09-18 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - CEG: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - AEP: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
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

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EPOL is a Poland-focused equity fund trading near its 52-week high with mild technical deterioration: RSI at midpoint (50.5), MACD histogram negative and below signal, and volume well below average during a small recent pullback. The 3-month return of +11.6% reflects a strong rally from March lows, but momentum indicators show no fresh strength. Macro backdrop is mixed: US rates have risen modestly this week and the dollar has strengthened (+1.23%), which can be headwinds for emerging market equities; the yield curve remains normal and VIX is slightly elevated but not alarming. Fund fundamentals are reasonable -- low P/E of 13.47, beta of 0.73 provides some defensive character, and 3.3% yield is solid -- but the analyst roll-up (47% of holdings) shows zero upside in consensus targets (-0.8% vs current prices), with all buy ratings suggesting limited further near-term appreciation. Fund flows and positioning data are absent, limiting visibility on conviction of money flows. The fund holds quality Polish names (banks, energy, materials) with no major catalyst or data surprise in the past week, and technicals show the rally is pausing rather than accelerating. No clear reason to abandon the position, but equally no fresh signal to add.

**Main reasons it gave:**
- RSI at midpoint with MACD below signal after 3-month +11.6% rally
- Analyst consensus 47% of holdings shows -0.8% upside vs current prices
- USD strength (+1.23 week, +1.23 YTD) headwind for emerging market fund
- Volume 22% of 20-day average during recent pullback shows weak participation
- Trading at 90% of 52-week high with lower momentum readings on each lower bar

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 44.35 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 44.62 (-0.6%), 50d 43.34 (+2.3%), 200d 39.01 (+13.7%); 50d above 200d
Momentum: RSI(14) 50.5 | MACD 0.381 vs signal 0.531 (histogram -0.150)
Returns: 1d -0.9% | 5d -2.6% | 1m -0.5% | 3m +11.6%
52-week range: 31.57 - 45.76 (now 90.1% of the way up)
Volatility: ATR(14) 0.63 (1.4% of price) | annualised 20d 17.5%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.47 | P/B 2.00 | P/S 1.36 | 3y earnings growth n/a
Yield: 3.3%
Three-year record: +42.2% a year | beta to the market 0.73
Cost and size: expense ratio 0.59% | net assets 848.26M
What it is made of: Stocks 99.3%, Cash 0.7%
Largest holdings: PKO Bank Polski SA 15.4%, Orlen SA 13.8%, Bank Polska Kasa Opieki SA 7.1%, Powszechny Zaklad Ubezpieczen SA 6.4%, KGHM Polska Miedz SA 4.6%
Sector mix: Financial services 46.1%, Energy 14.5%, Consumer cyclical 12.7%, Basic materials 6.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

```text
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.14 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.8% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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

_Not available today._

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWA (iShares Australia ETF) is trading below its 20-day, 50-day, and marginally above its 200-day moving averages, with RSI at 40 suggesting weak momentum and MACD histogram negative. The fund holds a 0.96 beta to broad market, so is not a momentum play; it is Australia-exposed and sized at $1.33B. Technicals show intraday weakness (-1.4% on the day, -4.2% on the month) on below-average volume (0.44x 20-day), which does not yet constitute a decisive break. Macro backdrop shows US yields rising modestly across the curve (3-month +7bps, 5-year +7bps, 10-year +3bps), the dollar strengthening sharply (+1.23 on the week to 100.35), and VIX at 15.39—elevated but not alarming. A stronger dollar pressures Australian equities and commodities, a headwind for this fund's large financials and basic materials exposure. The analyst roll-up covering 46.4% of holdings shows a weighted rating of 3.49 (between hold and sell), with a price target 6.5% *above* current prices—a modest positive that contradicts the near-term technical weakness. No material news catalyst appeared in the past 24 hours. The fund's three-year record of +12.4% annually is solid but not a near-term signal. Holdings are predominantly hold-rated (59.6% by weight) with significant sell weight (40.4%), signalling analyst ambivalence rather than conviction in either direction. While the macro picture (stronger dollar, rising rates) is slightly headwind-tilted for Australia, the technicals are weak but not yet broken, and the analyst view offers mild support. Conviction is muted because this is a macro timing call with no decisive catalyst, and the signals are mixed.

**Main reasons it gave:**
- Dollar strength +1.23 on week headwind for Australian equity
- Technicals weak: below 20d/50d SMA, RSI 40, negative MACD histogram
- Below-average volume on intraday decline signals lack of conviction
- Analyst roll-up 46.4% of fund weighted hold-to-sell with +6.5% price target offset by weak near-term momentum

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 28.72 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 29.67 (-3.2%), 50d 29.47 (-2.5%), 200d 28.53 (+0.7%); 50d above 200d
Momentum: RSI(14) 40.1 | MACD -0.219 vs signal -0.062 (histogram -0.157)
Returns: 1d -1.4% | 5d -1.9% | 1m -4.2% | 3m +0.5%
52-week range: 24.95 - 30.43 (now 68.7% of the way up)
Volatility: ATR(14) 0.39 (1.3% of price) | annualised 20d 17.7%
Volume: 0.44x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 21.06 | P/B 2.81 | P/S 3.39 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +12.4% a year | beta to the market 0.96
Cost and size: expense ratio 0.50% | net assets 1.33B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: BHP Group Ltd 16.3%, Commonwealth Bank of Australia 13.0%, National Australia Bank Ltd 5.9%, Westpac Banking Corp 5.7%, ANZ Group Holdings Ltd 5.5%
Sector mix: Financial services 41.1%, Basic materials 26.7%, Consumer cyclical 6.5%, Healthcare 5.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.05</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.49 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -6.5% above the current prices
Holdings read: BHP.AX, CBA.AX, NAB.AX, WBC.AX, ANZ.AX
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

_Not available today._

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWC trades below its 20- and 50-day moving averages in a technically weakened state, with RSI at 41.9 and negative MACD histogram signaling momentum loss. The fund's P/E of 19.49 and 3-year return of +21.6% annually suggest it is not cheap on a fundamental basis. Analyst coverage of its five largest holdings (28.3% of the fund) shows 74.3% buy ratings with a +9.3% price target, which is mildly constructive but reflects only a minority of the portfolio. The Canadian dollar has weakened against a strengthening US dollar (+1.23 on the week to 100.35), a headwind for CAD equity exports and dividend repatriation. Fund flows and broader macro data show no fresh catalyst: US Treasury yields edged higher across the curve, the VIX ticked down slightly to 15.39, and there is no material news flow. The fund's heavy weighting to financials (39.2%) and energy (17.9%) does not offset the near-term technical deterioration and lack of a clear directional driver. Volume is light at 0.27x the 20-day average, which limits confidence in any move. A modest bounce toward the 50-day SMA (60.64) is plausible, but the technicals and valuation offer no compelling case for outperformance in this cycle.

**Main reasons it gave:**
- RSI 41.9 and negative MACD histogram signal momentum loss
- Price 2.1% below 20-day SMA with volume at 0.27x average
- Canadian dollar weakness as USD index +1.23 on the week
- Analyst buy ratings of 74.3% on largest 5 holdings with +9.3% price target cover only 28.3% of fund
- P/E 19.49 and 3-year trailing return of 21.6% annually leave limited valuation margin

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 59.97 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 61.28 (-2.1%), 50d 60.64 (-1.1%), 200d 57.42 (+4.4%); 50d above 200d
Momentum: RSI(14) 41.9 | MACD -0.222 vs signal 0.017 (histogram -0.240)
Returns: 1d -0.7% | 5d -1.0% | 1m -3.0% | 3m +3.6%
52-week range: 49.72 - 62.64 (now 79.3% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 14.2%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 19.49 | P/B 2.83 | P/S 2.79 | 3y earnings growth n/a
Yield: 1.2%
Three-year record: +21.6% a year | beta to the market 0.79
Cost and size: expense ratio 0.50% | net assets 6.85B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Royal Bank of Canada 9.0%, The Toronto-Dominion Bank 6.3%, Shopify Inc Registered Shs -A- Subord Vtg 5.7%, Bank of Montreal 3.7%, Bank of Nova Scotia 3.6%
Sector mix: Financial services 39.2%, Energy 17.9%, Basic materials 16.1%, Industrials 8.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.3% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-11 Bernstein: init, ? -> Outperform
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
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

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWD is a Swedish-focused equity fund holding quality industrial and financial names with reasonable valuations (P/E 14.99, P/B 2.88) and solid three-year performance (+19.7% annually). However, near-term technicals show deterioration: the fund sits 3.3% below its 20-day SMA with RSI at 38.2 and negative MACD histogram, indicating oversold conditions but also momentum weakness. The 1-month return of -3.8% reflects recent selling pressure. The macro backdrop is mixed: US Treasury yields rose modestly across the curve this week (pushing up real rates), the dollar strengthened materially (+1.23%), and the VIX remains elevated at 15.39. A stronger dollar is a headwind for European equities. Analyst consensus on the four largest holdings (29.5% of fund) is constructive with 82% buy ratings and an 11.1% price target premium, but this covers less than one-third of the fund and does not shift the directional call. Fund flows and positioning data are absent, leaving insider_score null. The technical break below the 50-day and 20-day moving averages coupled with rising yields and dollar strength argues for caution, but oversold RSI and a normal yield curve slope prevent a bearish call. The case for a bounce exists, but there is no material catalyst to justify conviction above neutral.

**Main reasons it gave:**
- Price 3.3% below 20-day SMA with RSI 38.2 indicating oversold technicals but negative MACD momentum
- USD index +1.23% on week headwind for European equities
- Analyst buy ratings 82.1% on 29.5% of fund but covers less than one-third
- Treasury yields +3-7 basis points across curve raising real rate backdrop

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 50.91 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 52.66 (-3.3%), 50d 52.08 (-2.2%), 200d 51.27 (-0.7%); 50d above 200d
Momentum: RSI(14) 38.2 | MACD -0.361 vs signal -0.095 (histogram -0.266)
Returns: 1d -1.3% | 5d -1.9% | 1m -3.8% | 3m +1.1%
52-week range: 45.38 - 54.72 (now 59.2% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 15.9%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.99 | P/B 2.88 | P/S 2.90 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +19.7% a year | beta to the market 1.19
Cost and size: expense ratio 0.51% | net assets 755.74M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: Spotify Technology SA 10.2%, Investor AB Class B 9.5%, Volvo AB Class B 7.1%, Atlas Copco AB Class A 6.9%, Sandvik AB 5.3%
Sector mix: Industrials 46.0%, Financial services 24.9%, Communication services 13.9%, Technology 6.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.1% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-08-13 Argus Research: reit, Buy -> Buy
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

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWG is a German equity fund trading at a modest premium to its historical range and showing mixed signals. Technicals are weakening with price 3.3% below the 20-day moving average, RSI at 35 indicating oversold conditions, and negative MACD histogram, suggesting momentum has turned down despite above-average volume. The 1-month return of -4.5% reflects recent pressure. However, the analyst view of the largest 45.5% of holdings is constructively positioned with 78% buy ratings and a +17.5% price target above current levels, offsetting some technical weakness. Macro backdrop shows the dollar strengthening (+1.23 on the week), which is a headwind for a euro-denominated fund when converted to USD; US yields are rising modestly across the curve, consistent with a risk-off tilt. The fund's valuation at 18.4x P/E is reasonable but not cheap for a focused regional fund. The three-year track record of +18.1% annually suggests structural strength in the holdings, though current technicals suggest near-term consolidation or pullback before the analyst targets are reached. No material catalyst has emerged to break the recent downtrend, warranting a cautious neutral stance with a modest upside lean from analyst coverage.

**Main reasons it gave:**
- Price 3.3% below 20-day SMA with RSI 35 and negative MACD histogram, signaling near-term momentum weakness
- Analyst consensus 78% buy with +17.5% price target on largest 45.5% of fund, partially offsetting technicals
- Dollar strength (+1.23% on week) headwind for euro-denominated fund
- Recent -4.5% monthly decline despite solid three-year +18.1% annualized track record
- No macro catalyst or news to break recent consolidation pattern

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 42.06 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 43.49 (-3.3%), 50d 42.96 (-2.1%), 200d 42.37 (-0.7%); 50d above 200d
Momentum: RSI(14) 35.3 | MACD -0.270 vs signal -0.059 (histogram -0.212)
Returns: 1d -1.5% | 5d -1.9% | 1m -4.5% | 3m +1.3%
52-week range: 38.08 - 44.59 (now 61.2% of the way up)
Volatility: ATR(14) 0.45 (1.1% of price) | annualised 20d 12.3%
Volume: 1.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.40 | P/B 1.94 | P/S 1.28 | 3y earnings growth n/a
Yield: 1.9%
Three-year record: +18.1% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Siemens AG 12.1%, SAP SE 11.3%, Allianz SE 10.0%, Siemens Energy AG Ordinary Shares 6.4%, Deutsche Telekom AG 5.6%
Sector mix: Industrials 28.7%, Financial services 23.2%, Technology 15.9%, Consumer cyclical 7.4%
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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.83 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.5% above the current prices
Holdings read: SIE.DE, SAP.DE, ALV.DE, ENR.DE, DTE.DE
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

_Not available today._

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWI is an Italy-focused equity fund now trading 2.8% below both 20- and 50-day moving averages, with RSI at 36.6 indicating oversold conditions and MACD negative. The technical backdrop shows momentum loss over one month (-4.5%) but the fund remains above its 200-day MA (+4.0%), suggesting the downmove is a pullback rather than a trend break. The dollar has strengthened sharply this week (+1.23 against a global basket), which headwinds foreign equities, and US real yields across the curve have edged higher. Macro conditions are not decisively hawkish -- the curve remains upward-sloping and VIX is merely elevated, not spiking -- so the weakness appears tactical rather than regime-driven. Analyst consensus on the five largest holdings (51% of the fund) is unanimously bullish with a 12.5% price target, which is not corroborated by the current price action but suggests a floor for downside. Fund flows and positioning data are absent. The 3.0% yield and reasonable 15.25 P/E offer valuation support. Until a clearer technical break or macro catalyst emerges -- either a decisive reversal or confirmation of further decline -- the prudent stance is to wait for clarity.

**Main reasons it gave:**
- Price 2.8% below both 20d and 50d SMAs, RSI 36.6 indicating oversold but no reversal yet
- Dollar index +1.23 on the week headwinds foreign equities
- Analyst consensus on 51% of holdings unanimously buy with +12.5% price target
- Normal yield curve and VIX at 15.39 -- macro backdrop not decisively bearish

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 59.97 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 61.69 (-2.8%), 50d 61.72 (-2.8%), 200d 57.69 (+4.0%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -0.395 vs signal -0.203 (histogram -0.192)
Returns: 1d -2.0% | 5d -3.2% | 1m -4.5% | 3m -1.0%
52-week range: 50.31 - 63.35 (now 74.1% of the way up)
Volatility: ATR(14) 0.69 (1.1% of price) | annualised 20d 14.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.25 | P/B 1.85 | P/S 1.64 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +28.5% a year | beta to the market 0.88
Cost and size: expense ratio 0.50% | net assets 1.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: UniCredit SpA 16.8%, Intesa Sanpaolo 13.6%, Enel SpA 10.3%, Ferrari NV 5.2%, Eni SpA 5.0%
Sector mix: Financial services 52.6%, Utilities 16.3%, Industrials 9.7%, Consumer cyclical 9.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.5% above the current prices
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

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWJ has rallied to the 52-week high (90.6% of range) on solid technicals -- a 7.8% gain vs 200d SMA and positive momentum structurally. The BoJ's September rate hike to 1.25% is real tightening in a regime that had carried loose policy, which normally pressures equity valuations and JPY-denominated assets through higher discount rates. US Treasury yields have risen modestly (3-10y up 3-7bp this week) and the dollar has strengthened sharply (+1.23), headwinds for Japanese equities when valued in USD. The fund's valuation is moderate (P/E 19.1) and yield reasonable (3.7%), but the 3-year 18.9% CAGR leaves limited margin for error. Analyst coverage of the top 5 holdings (17% of fund) shows 100% buy ratings with +19.7% upside, but this is thin and a top-slice read only. Positioning in the Nikkei futures is light (27th percentile) with modest net long (2.7% of OI), showing no conviction clustering. The fund has lost 1.9% over 5d and is reversing (RSI 51.2, MACD histogram negative), volume is below average, and the tactical momentum has stalled despite the longer-trend strength. The BoJ tightening cycle is a structural headwind that offsets the run-up, and the fund's beta of 0.86 means it underperforms on global risk-off, which rising rates can trigger. No clear catalyst justifies a directional move beyond the already-executed rally.

**Main reasons it gave:**
- BoJ rate hike to 1.25% tightens financial conditions for JPY assets
- Dollar strength +1.23 on week headwind for USD-denominated Japan exposure
- Fund at 52-week high after 7.8% gain vs 200d SMA but 5d momentum reversing
- Analyst buy ratings on top 5 holdings (+19.7% upside) but covers only 17% of fund
- Nikkei futures positioning at 27th percentile shows no speculator crowding

<details><summary><b>News</b> — score +0.15</summary>

- [Small-Cap Japan ETF Hits a 52-Week High](https://finance.yahoo.com/markets/stocks/articles/small-cap-japan-etf-hits-124900516.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  iShares MSCI Japan Small-Cap ETF SCJ is probably on the radar for investors seeking momentum. The fund just hit a 52-week high and has surged 26.5% from its...
- [BoJ Hikes Rates, More Cautious Approach Likely Ahead: ETFs in Focus](https://www.tradingview.com/news/zacks:7fd88923e094b:0-boj-hikes-rates-more-cautious-approach-likely-ahead-etfs-in-focus/)  
  <sub>TradingView, 2 hours ago</sub>  
  The Bank of Japan (BoJ) raised its benchmark interest rate to 1.25% from 1% on Sept. 18, 2026, taking borrowing costs to their highest level in about three...
- [US Stock Market This Week: Are SPY, QQQ Beating Asian Equities?](https://stocktwits.com/news-articles/markets/equity/us-stock-market-this-week-are-spy-qqq-beating-asian-equities/cZtuFPnRB3Q)  
  <sub>Stocktwits, 9 hours ago</sub>  
  The Nasdaq index in the U.S. is set to post weekly gains, while the Dow and S&P 500, along with Asian markets including China, Japan, Taiwan,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 96.67 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 96.61 (+0.1%), 50d 94.95 (+1.8%), 200d 89.69 (+7.8%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD 0.622 vs signal 0.709 (histogram -0.087)
Returns: 1d -1.3% | 5d -1.9% | 1m +2.0% | 3m +0.4%
52-week range: 78.36 - 98.56 (now 90.6% of the way up)
Volatility: ATR(14) 1.38 (1.4% of price) | annualised 20d 15.0%
Volume: 0.52x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Japan Stock
What it holds: P/E 19.11 | P/B 2.01 | P/S 1.68 | 3y earnings growth n/a
Yield: 3.7%
Three-year record: +18.9% a year | beta to the market 0.86
Cost and size: expense ratio 0.49% | net assets 22.69B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Mitsubishi UFJ Financial Group Inc 4.6%, Toyota Motor Corp 3.5%, Sumitomo Mitsui Financial Group Inc 3.0%, Tokyo Electron Ltd 3.0%, Advantest Corp 2.9%
Sector mix: Industrials 22.9%, Technology 21.5%, Financial services 19.1%, Consumer cyclical 11.6%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.7% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 2.7% of open interest (42,440 contracts)
Change on the week: +0.5% of open interest
Crowding: 27% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWL is a Switzerland-focused equity fund with a defensive posture (healthcare and financials heavy) currently trading below all three intermediate moving averages after a -7% one-month drawdown. The technical picture shows bearish momentum with RSI at 32.6 (oversold) and MACD below signal, suggesting short-term weakness, while volume is depressed at 0.27x average, limiting the conviction of the move. The macro backdrop is mixed: dollar strength at +1.23 on the week and rising short-end yields create headwinds for a CHF-denominated fund from a currency perspective, but the curve remains normal and VIX is only moderately elevated. Analyst consensus on the five largest holdings (48.5% of the fund) is constructive with 74.5% buy ratings and an +11% mean price target, offering support; however, this upside expectation is partially offset by the recent weakness in the fund's price. The fund's three-year return of +11.7% annually and low beta (0.91) suggest it has been resilient, but current technicals and near-term bearish momentum indicators prevent a bullish call despite reasonable fundamental support. A bounce from oversold RSI is possible, but it lacks a clear catalyst and the dollar and rate moves this week are headwinds rather than tailwinds.

**Main reasons it gave:**
- RSI 32.6 and MACD negative histogram signal short-term oversold conditions
- Price -7% in one month, now below all three SMAs with depressed volume
- Dollar +1.23 on week, headwind for CHF-denominated holdings
- Analyst consensus 74.5% buy with +11% mean target on 48.5% of holdings
- Three-year annual return +11.7% with 0.91 beta shows resilience but no near-term catalyst evident

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 59.98 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 62.17 (-3.5%), 50d 62.80 (-4.5%), 200d 61.53 (-2.5%); 50d above 200d
Momentum: RSI(14) 32.6 | MACD -0.904 vs signal -0.649 (histogram -0.255)
Returns: 1d -0.6% | 5d -0.5% | 1m -7.0% | 3m -2.2%
52-week range: 53.86 - 65.08 (now 54.5% of the way up)
Volatility: ATR(14) 0.68 (1.1% of price) | annualised 20d 13.1%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +11.7% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.0% above the current prices
Holdings read: ROP.SW, NOVN.SW, NESN.SW, UBSG.SW, CFR.SW
Recent rating changes among them:
  - UBSG.SW: 2026-04-20 Barclays: up, Underweight -> Equal-Weight
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

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EWN is in a mild downtrend -- below both 20d and 50d SMAs, RSI 40, MACD negative and widening -- but still 4% above a rising 200d and 69% up its 52-week range, so this reads as a pullback within an uptrend rather than a break. Macro is a modest headwind: 10y at 5.00% (+3bp), short end +7bp, and a dollar index up 1.23 on the week pressures euro-denominated returns for a USD holder, though VIX at 15.4 shows no stress. Analyst roll-up on 44% of the fund is 100% buy with a +36% weighted target, but that is a bottom-up artefact of ASML/Nebius coverage, not a macro signal, and the fund's 21.8% ASML weight makes it a levered semi bet rather than a country trade. No news, no positioning or flow data, volume 0.05x average on the last bar makes the print low-information. Nothing here qualifies as a policy or data surprise, so NEUTRAL with a slight bearish tilt.

**Main reasons it gave:**
- Price 2.2% below 20d and 2.3% below 50d SMA, MACD histogram -0.249, RSI 40
- Still +4.2% above rising 200d with 50d above 200d -- uptrend intact
- Dollar index +1.23 on the week, a headwind for USD-denominated euro-asset returns
- 10y 5.00% (+3bp) with short end +7bp; curve normal, VIX 15.4, no macro surprise
- Analyst roll-up covers only 44% of fund and is dominated by ASML's 21.8% weight

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 66.57 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 68.05 (-2.2%), 50d 68.15 (-2.3%), 200d 63.87 (+4.2%); 50d above 200d
Momentum: RSI(14) 40.3 | MACD -0.580 vs signal -0.331 (histogram -0.249)
Returns: 1d -0.2% | 5d -1.9% | 1m -4.0% | 3m -6.0%
52-week range: 55.33 - 71.61 (now 69.0% of the way up)
Volatility: ATR(14) 0.87 (1.3% of price) | annualised 20d 13.7%
Volume: 0.05x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.97 | P/B 2.54 | P/S 1.84 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +22.6% a year | beta to the market 1.14
Cost and size: expense ratio 0.50% | net assets 626.66M
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ASML Holding NV 21.8%, ING Groep NV 9.0%, Prosus NV Ordinary Shares - Class N 5.1%, Nebius Group NV Shs Class-A- 4.3%, ASM International NV 4.0%
Sector mix: Technology 31.5%, Financial services 21.4%, Industrials 10.8%, Consumer defensive 10.7%
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
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.7% above the current prices
Holdings read: ASML.AS, INGA.AS, PRX.AS, NBIS, ASM.AS
Recent rating changes among them:
  - NBIS: 2026-09-09 Truist Securities: init, ? -> Buy
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

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWP is a focused Spain play holding 54.5% in the five largest positions, dominated by financials (45.4%) and utilities (20.0%). Technicals show deterioration: the fund is down 2.6% over five days and 3.0% over one month despite being up 5.7% from its 200-day average, suggesting recent weakness in an uptrend. RSI at 41 and a negative MACD histogram indicate momentum is waning. The fund trades at a reasonable valuation (P/E 16.28, yielding 2.7%) with analyst consensus modestly bullish at +2.8% target above current prices. However, macro headwinds are present: the US dollar strengthened +1.23 this week to 100.35, which is headwind for European equities; short-term rates rose 7bp and the curve remains normal. VIX elevated at 15.39 suggests some caution in risk appetite. The three-year annualized return of +33.7% reflects a strong historical run, but current momentum has stalled. No recent news or positioning data to support conviction. The analyst view covers only 54.5% of the fund and shows no recent catalyst changes. Low volume (0.21x average) reinforces that there is no immediate directional pressure.

**Main reasons it gave:**
- Price down 2.6% over five days with RSI(14) at 41 indicating momentum loss
- US dollar index +1.23 on the week headwind for European equities
- Analyst consensus +2.8% target but covering only 54.5% of fund
- Volume 0.21x 20-day average suggests weak conviction
- MACD negative histogram and price below all major moving averages

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 60.50 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 62.03 (-2.5%), 50d 61.41 (-1.5%), 200d 57.22 (+5.7%); 50d above 200d
Momentum: RSI(14) 41.0 | MACD -0.191 vs signal 0.034 (histogram -0.225)
Returns: 1d -1.8% | 5d -2.6% | 1m -3.0% | 3m +2.5%
52-week range: 48.25 - 63.23 (now 81.8% of the way up)
Volatility: ATR(14) 0.78 (1.3% of price) | annualised 20d 15.1%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 16.28 | P/B 2.22 | P/S 1.82 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +33.7% a year | beta to the market 0.87
Cost and size: expense ratio 0.50% | net assets 2.26B
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Banco Santander SA 19.2%, Banco Bilbao Vizcaya Argentaria SA 14.0%, Iberdrola SA 12.1%, CaixaBank SA 4.6%, Industria De Diseno Textil SA Share From Split 4.4%
Sector mix: Financial services 45.4%, Utilities 20.0%, Industrials 14.4%, Technology 5.9%
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

<details><summary><b>What analysts and big funds say</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.15</summary>

```text
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.8% above the current prices
Holdings read: SAN.MC, BBVA.MC, IBE.MC, CABK.MC, ITX.MC
Recent rating changes among them:
  - SAN.MC: 2023-11-08 JP Morgan: main, Neutral -> Neutral
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

### Taiwan (EWT) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EWT is near 52-week highs (97.7% of range) with a solid uptrend above 20/50/200d SMAs, but momentum is fading (MACD below signal, RSI 58, 3m return only +0.9%, volume 0.33x average). Macro is mildly unhelpful: 10y at 5.00% and rising, dollar up 1.23 on the week, which pressures EM/Taiwan equities. Analyst roll-up on 38% of the fund is uniformly buy with ~31% upside, but that is a bottom-up semiconductor call, not a country timing signal. Concentration is extreme (TSMC 22%, tech 74%) and beta 1.30 means this is a leveraged AI-cycle proxy at a full valuation (P/E 27, P/B 4.3) after +42%/yr for three years. No rate or data surprise this week, so no directional edge. Single-holding ETF-launch listicles in the news feed are noise and were disregarded.

**Main reasons it gave:**
- Price at 97.7% of 52-week range but 3-month return only +0.9% — stalling at highs
- MACD histogram negative (-0.199) with volume 0.33x 20-day average
- Dollar index +1.23 on the week and 10y yield at 5.00%, a headwind for EM equities
- Analyst roll-up on 38% of fund: 100% buy, +30.9% weighted target upside
- Extreme concentration: TSMC 22.1%, technology 73.9%, beta 1.30, P/E 27.3

<details><summary><b>News</b> — score +0.00</summary>

- [Portfolio Fit: CCML](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-ccml/?tpid=1663756&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Every AI server board and electric vehicle runs on a tiny ceramic component most investors have never heard of, and a brand-new ETF just made it possible to...
- [US Stock Market This Week: Are SPY, QQQ Beating Asian Equities?](https://stocktwits.com/news-articles/markets/equity/us-stock-market-this-week-are-spy-qqq-beating-asian-equities/cZtuFPnRB3Q)  
  <sub>Stocktwits, 9 hours ago</sub>  
  The Nasdaq index in the U.S. is set to post weekly gains, while the Dow and S&P 500, along with Asian markets including China, Japan, Taiwan,...
- [Portfolio Fit: AIFR](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-aifr/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Most semiconductor ETFs bury foundry exposure under layers of chip designers, equipment makers, and memory producers, which is exactly the problem a new...
- [Portfolio Fit: KCHP](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-kchp/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Investors trying to isolate the Korean piece of the AI memory cycle have historically had to buy it inside a broad country fund, where semiconductors are...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 110.99 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 108.62 (+2.2%), 50d 104.10 (+6.6%), 200d 86.29 (+28.6%); 50d above 200d
Momentum: RSI(14) 58.7 | MACD 1.517 vs signal 1.715 (histogram -0.199)
Returns: 1d +0.3% | 5d +0.1% | 1m +6.0% | 3m +0.9%
52-week range: 60.03 - 112.18 (now 97.7% of the way up)
Volatility: ATR(14) 2.16 (1.9% of price) | annualised 20d 24.0%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Greater China Region
What it holds: P/E 27.26 | P/B 4.29 | P/S 2.54 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +42.1% a year | beta to the market 1.30
Cost and size: expense ratio 0.59% | net assets 11.76B
What it is made of: Stocks 99.6%, Cash 0.4%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 22.1%, MediaTek Inc 6.0%, Delta Electronics Inc 4.0%, Hon Hai Precision Industry Co Ltd 3.3%, ASE Technology Holding Co Ltd 2.6%
Sector mix: Technology 73.9%, Financial services 14.0%, Basic materials 3.8%, Industrials 2.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 38.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.9% above the current prices
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

_Not available today._

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWU is a focused region fund on UK equities with a strong macro headwind and conflicting technical signals. The US dollar has rallied +1.23% this week to 100.35, creating a FX headwind for dollar-based investors in sterling assets; this is a material structural negative for a UK equity fund. Technicals show price 1.6% below its 20-day moving average on momentum deterioration (RSI 39, MACD histogram negative) with volume below average, suggesting weakness without conviction of reversal. The 52-week position at 73.7% of range offers no safety margin. However, the fund's largest holdings carry analyst support: the five constituents (36% of fund) are rated 50.1% buy / 49.9% hold with a weighted +11.7% price target, and AstraZeneca received an outperform initiation in August. The yield of 3.1% and a three-year track record of +18% annually (beta 0.68) suggest fundamentals are not broken. The macro backdrop is mixed: Treasury yields edged higher but the curve remains upward-sloping and normal; volatility at 15.39 is elevated but not extreme. The absence of news and weak volume suggest the market is pausing rather than decisively repricing. A weak pound and technical softness argue against a bullish call, but analyst support for the holdings and reasonable valuation (P/E 17.08, P/B 2.29) offer some foundation. The conviction is low because the dollar strength is a real headwind, technicals are deteriorating, and macro timing calls on regional funds are difficult; this is a position to watch for a rebound in sterling or a technical reversal on volume before leaning in.

**Main reasons it gave:**
- US dollar up 1.23% this week, creating FX headwind for UK equities
- RSI 39 and negative MACD histogram indicate momentum deterioration
- Top 5 holdings (36% of fund) have 50% buy ratings with +11.7% weighted price target
- Price 1.6% below 20-day MA with below-average volume suggests pause, not conviction
- Valuation reasonable (P/E 17.08) and 3.1% yield stable, but technical setup lacks support

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 47.19 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 48.27 (-2.2%), 50d 47.94 (-1.6%), 200d 46.49 (+1.5%); 50d above 200d
Momentum: RSI(14) 39.0 | MACD -0.154 vs signal -0.016 (histogram -0.138)
Returns: 1d -1.6% | 5d -1.6% | 1m -2.8% | 3m +3.8%
52-week range: 41.04 - 49.39 (now 73.7% of the way up)
Volatility: ATR(14) 0.46 (1.0% of price) | annualised 20d 11.5%
Volume: 0.56x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.08 | P/B 2.29 | P/S 1.52 | 3y earnings growth n/a
Yield: 3.1%
Three-year record: +18.0% a year | beta to the market 0.68
Cost and size: expense ratio 0.50% | net assets 3.79B
What it is made of: Stocks 97.9%, Other 1.1%, Cash 0.9%
Largest holdings: HSBC Holdings PLC 11.0%, Shell PLC 7.8%, AstraZeneca PLC 7.6%, Rolls-Royce Holdings PLC 5.3%, Unilever PLC 4.3%
Sector mix: Financial services 26.4%, Consumer defensive 14.3%, Industrials 13.9%, Healthcare 12.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 50.1% | hold 49.9% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.7% above the current prices
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

_Not available today._

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWW is Mexico-focused equity fund trading 3.1% below its 20-day moving average with RSI at 38.8 indicating oversold conditions, yet momentum remains negative (MACD histogram -0.333). The macro backdrop shows US dollar strength (+1.23 on week to 100.35), which typically pressures EM currencies and makes Mexican assets less attractive for foreign investors; Treasury yields have risen across the short end (+7bp at 3m and 5y), supporting the dollar carry. The fund's valuation is reasonable (P/E 12.68) with a 3.2% yield and analyst consensus on the largest 5 holdings is constructive (+17.7% price target), but this represents less than half the fund by weight and reflects sentiment that has already been reflected in consensus ratings. Volume is well below average (0.48x 20-day), suggesting weak commitment behind the recent decline. The one-month and three-month returns are slightly negative (-2.1% and -4.9% respectively), but these are modest and not accompanied by a clear technical breakdown or macro catalyst beyond the broad dollar strength. The analyst view is not actionable as a sufficient positive signal given the headwinds from currency and rate dynamics. Without fresh news, a clear technical reversal, or a material surprise in macro conditions, the appropriate response is to await clarity.

**Main reasons it gave:**
- US dollar strength (+1.23 week) headwind for EM
- Short-end Treasury yields +7bp supporting dollar carry
- RSI 38.8 oversold but volume 0.48x average suggests weak conviction
- Analyst targets +17.7% on largest 5 holdings (47.6% of fund) but below 50% coverage

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 73.57 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 75.96 (-3.1%), 50d 75.89 (-3.1%), 200d 75.64 (-2.7%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -0.633 vs signal -0.300 (histogram -0.333)
Returns: 1d -1.0% | 5d -2.4% | 1m -2.1% | 3m -4.9%
52-week range: 64.39 - 81.23 (now 54.5% of the way up)
Volatility: ATR(14) 1.30 (1.8% of price) | annualised 20d 17.5%
Volume: 0.48x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.68 | P/B 1.98 | P/S 1.49 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +10.6% a year | beta to the market 1.05
Cost and size: expense ratio 0.50% | net assets 1.82B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Grupo Mexico SAB de CV Class B 16.6%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.3%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Cemex SAB de CV 4.4%
Sector mix: Basic materials 27.3%, Consumer defensive 24.4%, Financial services 19.7%, Industrials 11.7%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.7% above the current prices
Holdings read: GMEXICOB.MX, GFNORTEO.MX, FEMSAUBD.MX, AMXB.MX, CEMEXCPO.MX
Recent rating changes among them:
  - GMEXICOB.MX: 2018-11-12 Citigroup: down, Buy -> Neutral
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

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> EWY presents a mixed picture with no clear macro catalyst. The Korean market surged 90% from its lows but has since corrected sharply with extreme volatility (44.5% annualized). Technicals show weakness: the price is 1.1% below its 20-day moving average, momentum (MACD) is negative with RSI near 50, and the fund is down 18.3% over three months despite being up 2.7% in one month. The 52-week range shows the fund at 71% of the way up, suggesting limited further upside room. Volume is well below average (0.36x), indicating low conviction in current direction. Macro headwinds are present: the dollar has strengthened +1.23% this week and US yields are steady to higher, which typically weighs on EM equities. However, the fund trades at attractive valuations (P/E 10.41, P/B 1.83) and holds quality semiconductor names (SK Hynix 23.7%, Samsung 22.2%) that benefit from AI. The analyst section is empty with no coverage rolled up, limiting directional conviction. The recent news highlights that Korea needs new buyers after the bubble faded, suggesting sentiment is cautious. Without a specific macro surprise, clear technical breakdown, or analyst support, and given the combination of negative momentum, recent weakness, and elevated volatility in a risk-off macro backdrop, NEUTRAL is the appropriate stance.

**Main reasons it gave:**
- MACD negative with RSI at neutral midpoint; price below 20-day MA
- Down 18.3% in three months; volume 0.36x average suggests weak conviction
- Dollar strengthened 1.23% this week; higher US yields headwind for EM
- Attractive valuations (P/E 10.41) but news frames market as needing new buyers after bubble
- 52-week rally already at 71% of range; limited upside room without catalyst

<details><summary><b>News</b> — score -0.15</summary>

- [Portfolio Fit: KCHP](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-kchp/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Investors trying to isolate the Korean piece of the AI memory cycle have historically had to buy it inside a broad country fund, where semiconductors are...
- [EWY: The Bubble Faded, But Korea Still Needs New Buyers (NYSEARCA:EWY)](https://seekingalpha.com/article/4947779-ewy-the-bubble-faded-but-korea-still-needs-new-buyers)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  The Korean stock market experienced extreme volatility, with a 90% rally from last year's bottom followed by sharp corrections. Learn more about the EWY ETF...
- [This Nation's Stock Market Is Outperforming All Others This Year. Should You Invest?](https://www.fool.com/investing/2026/09/18/this-nations-stock-market-is-outperforming-others/)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  The U.S. stock market is having a solid year by almost any measurement. The S&P 500 index has climbed almost 12% in 2026, following three stellar years,...
- [US Stock Market This Week: Are SPY, QQQ Beating Asian Equities?](https://stocktwits.com/news-articles/markets/equity/us-stock-market-this-week-are-spy-qqq-beating-asian-equities/cZtuFPnRB3Q)  
  <sub>Stocktwits, 9 hours ago</sub>  
  The Nasdaq index in the U.S. is set to post weekly gains, while the Dow and S&P 500, along with Asian markets including China, Japan, Taiwan,...
- [KOSPI rallies 90% from last year but faces vola...](https://pluang.com/en/news-feed/pasar-saham-korea-masih-butuh-pembeli-baru-setelah-gejolak)  
  <sub>Pluang, 6 hours ago</sub>  
  The Korean Stock Market (KOSPI) surged over 90% from its low last year but has since experienced sharp corrections and high volatility.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 179.12 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 181.03 (-1.1%), 50d 173.36 (+3.3%), 200d 151.58 (+18.2%); 50d above 200d
Momentum: RSI(14) 49.9 | MACD 1.326 vs signal 2.145 (histogram -0.819)
Returns: 1d -1.8% | 5d -5.1% | 1m +2.7% | 3m -18.3%
52-week range: 78.87 - 219.20 (now 71.4% of the way up)
Volatility: ATR(14) 6.62 (3.7% of price) | annualised 20d 44.5%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +44.1% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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
Rolled up from the 5 largest holdings, 53.5% of the fund by weight
Ratings by weight: buy n/a | hold n/a | sell n/a (mean n/a on a 1=strong buy to 5=strong sell scale)
Weighted price target: n/a above the current prices
Holdings read: 000660.KQ, 005930.KQ, 402340.KQ, 009150.KQ, 105560.KQ
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

_Not available today._

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> GDX has corrected 3.4% below its 20-day moving average and momentum is mixed: RSI at 51 sits at neutral while MACD histogram is negative, signaling weakening short-term momentum despite a +15.4% three-month rally. Macro headwinds are material: the dollar strengthened 1.23% this week to 100.35, a headwind for gold-denominated assets, while Treasury yields have drifted higher across the curve. The analyst view is constructive—all five largest holdings (39.9% of fund weight) carry buy ratings with a weighted +9.2% price target—but this covers less than 40% of the fund and represents rolled-up coverage of major producers, not a forward catalyst. News is dominated by junior miner inclusion announcements for GDXJ, the junior fund, not GDX itself; these are indexing events without directional signal. The fund's 50d SMA remains below its 200d, confirming an intact intermediate downtrend, though volume is weak at 0.45x average, suggesting the correction may be winding down rather than accelerating. A +5.0% gain above the 200d and position 56.7% of the way up the 52-week range leave room for further recovery, but no clear macro or technical trigger justifies conviction above neutral. The three-month +15.4% return has already captured much of recent momentum.

**Main reasons it gave:**
- Dollar strengthened 1.23% this week, headwind for gold
- RSI neutral and MACD histogram negative despite 15% three-month gain
- 50d SMA below 200d, intermediate downtrend intact
- Analyst consensus bullish on 40% of fund with +9.2% target, but coverage is thin
- News flow concerns GDXJ juniors, not GDX constituents

<details><summary><b>News</b> — score +0.00</summary>

- [Hemlo Mining Corp. Announces Inclusion in VanEck Junior Gold Miners ETF (GDXJ)](https://www.prnewswire.com/news-releases/hemlo-mining-corp-announces-inclusion-in-vaneck-junior-gold-miners-etf-gdxj-302882657.html)  
  <sub>PR Newswire, 6 hours ago</sub>  
  PRNewswire/ -- Hemlo Mining Corp. (TSX: HMMC) (OTCQX: HMMCF) ("Hemlo Mining" or the "Company") is pleased to announce that it has been added to the VanEck.
- [Sinda Ltd. Announces Inclusion in the VanEck Junior Gold Miners ETF (GDXJ)](https://www.marketscreener.com/news/sinda-ltd-announces-inclusion-in-the-vaneck-junior-gold-miners-etf-gdxj-ce785adada8bfe2d)  
  <sub>www.marketscreener.com, 5 hours ago</sub>  
  Sinda Ltd. (NYSE: SIND) (the “Company” or “Sinda”) today announced that its common stock will be added to the VanEck Junior Gold Miners ETF (“GDXJ”),...
- [The Case For Real Assets: One Of The Most Under-Owned Corners Of The Market](https://seekingalpha.com/article/4947834-case-for-real-assets-most-under-owned-corners-of-market?source=feed_sector_etf_portfolio_strategy)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Investors have put roughly $28 into bond funds for every $1 into commodity funds since 1997. Read more here.
- [GDX Correction Concludes, Anticipating Minimum 3-Wave Upside for AMEX:GDX by Elliottwave-Forecast](https://www.tradingview.com/chart/GDX/EIoI6JpE-GDX-Correction-Concludes-Anticipating-Minimum-3-Wave-Upside/)  
  <sub>TradingView, 15 hours ago</sub>  
  The short‑term Elliott Wave view in the Gold Miners ETF (GDX) shows that the rally from the July 17, 2026 low unfolded as a five‑wave impulse.
- [Sunshine Silver Mining joins VanEck Junior Gold Miners ETF, boosting visibility after recent IPO.](https://pluang.com/en/news-feed/sunshine-silver-mining-termasuk-dalam-vaneck-junior-gold-miners-etf)  
  <sub>Pluang, 6 hours ago</sub>  
  Sunshine Silver Mining & Refining Company announced its common stock will be added to the VanEck Junior Gold Miners ETF (GDXJ) as of September 18, 2026.
- [Hemlo Mining added to VanEck Junior Gold Miners ETF, boosting visibility and liquidity.](https://pluang.com/en/news-feed/hemlo-mining-termasuk-dalam-vaneck-junior-gold-miners-etf-gdxj)  
  <sub>Pluang, 6 hours ago</sub>  
  Hemlo Mining Corp. has been included in the VanEck Junior Gold Miners ETF (GDXJ) effective September 18, 2026. This inclusion marks a significant milestone...
- [Forrestania Resources Added to VanEck Junior Gold Miners ETF GDXJ](https://kalkine.com.au/news/announcements/forrestania-resources-added-to-vaneck-junior-gold-miners-etf-gdxj)  
  <sub>Kalkine, 15 hours ago</sub>  
  Forrestania Resources Limited (ASX:FRS) has disclosed that the company has been added to the VanEck Junior Gold Miners ETF (GDXJ), a globally recognised...
- [Forrestania joins GDXJ fund](https://mining.com.au/forrestania-joins-gdxj-fund/)  
  <sub>Mining.com.au, 13 hours ago</sub>  
  Forrestania Resources (ASX:FRS) has been added to the VanEck Junior Gold Miners ETF, which may increase awareness among global investors.
- [Forrestania Resources Joins VanEck Junior Gold Miners ETF (GDXJ) Portfolio](https://kalkinemedia.com/au/news/announcements/forrestania-resources-joins-vaneck-junior-gold-miners-etf-gdxj-portfolio)  
  <sub>Kalkine Media, 15 hours ago</sub>  
  Key Highlights. Forrestania Resources has been added to the VanEck Junior Gold Miners ETF (GDXJ). The GDXJ is recognized as one of the largest specialist...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 95.24 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 98.62 (-3.4%), 50d 87.97 (+8.3%), 200d 90.67 (+5.0%); 50d below 200d
Momentum: RSI(14) 51.1 | MACD 1.287 vs signal 2.496 (histogram -1.209)
Returns: 1d -0.7% | 5d -1.9% | 1m -2.1% | 3m +15.4%
52-week range: 68.28 - 115.84 (now 56.7% of the way up)
Volatility: ATR(14) 3.44 (3.6% of price) | annualised 20d 40.3%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Equity Precious Metals
What it holds: P/E 12.84 | P/B 2.68 | P/S 4.10 | 3y earnings growth n/a
Yield: 0.6%
Three-year record: +47.9% a year | beta to the market 0.83
Cost and size: expense ratio 0.51% | net assets 30.54B
What it is made of: Stocks 100.0%
Largest holdings: Newmont Corp 10.7%, Agnico Eagle Mines Ltd 10.7%, Barrick Mining Corp 7.4%, Wheaton Precious Metals Corp 5.8%, Anglogold Ashanti PLC 5.3%
Sector mix: Basic materials 100.0%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.2% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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

### India (INDA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> India equity fund showing weakness across multiple timeframes with technical deterioration offset partially by valuation support and analyst optimism on major holdings. The 50-day MA has crossed below the 200-day, price is 2.5% below the 50-day and 4.3% below the 200-day, RSI is oversold at 38.9, and MACD is negative with a widening histogram. Returns are negative across 1-month (-3.1%), 3-month (-3.2%), and year-to-date measures. Macro backdrop shows US Treasury yields rising (5-year +7bp, 10-year +3bp this week), dollar strengthening (+1.23 to 100.35), which typically pressures emerging markets. VIX at 15.39 is elevated but not crisis-level. Fund flows and positioning data are absent. On the positive side, the fund's P/E of 22.87 and P/B of 3.14 are not stretched for India's growth profile, the 5 largest holdings (24.7% of fund) are rated 100% buy by analysts with a +30.4% weighted price target, and the fund carries low expense ratio at 0.61%. However, analyst coverage is thin (only 24.7% of holdings) and the 3-year record of +1.9% annually with beta 0.56 suggests the fund has lagged broader markets. The weakness in price action combined with rising US rates and a stronger dollar creates headwinds; the analyst optimism on holdings and reasonable valuation provide limited floor. No decisive catalyst to warrant a directional call; current technicals and macro momentum argue against initiating longs, but valuation and analyst consensus prevent a bearish stance.

**Main reasons it gave:**
- 50d MA below 200d MA with price 4.3% below 200d SMA
- RSI 38.9 in oversold territory, MACD negative and widening
- US dollar +1.23 this week to 100.35, headwind for India equity
- Analyst consensus on top 5 holdings (24.7% of fund) at strong buy with +30.4% price target

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI India ETF Price and Live Chart in Rupiah | INDAON/IDR = 853.412](https://pintu.co.id/en/market/indaon)  
  <sub>Pintu, 13 hours ago</sub>  
  INDAON is a tokenized ETF issued by Ondo Global Markets (BVI) Limited, a real-world asset tokenization platform operating on blockchain networks including...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 48.01 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 49.05 (-2.1%), 50d 49.24 (-2.5%), 200d 50.16 (-4.3%); 50d below 200d
Momentum: RSI(14) 38.9 | MACD -0.455 vs signal -0.280 (histogram -0.175)
Returns: 1d +0.0% | 5d -1.2% | 1m -3.1% | 3m -3.2%
52-week range: 45.42 - 55.29 (now 26.2% of the way up)
Volatility: ATR(14) 0.45 (0.9% of price) | annualised 20d 14.2%
Volume: 0.77x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: India Equity
What it holds: P/E 22.87 | P/B 3.14 | P/S 2.72 | 3y earnings growth n/a
Yield: n/a
Three-year record: +1.9% a year | beta to the market 0.56
Cost and size: expense ratio 0.61% | net assets 6.75B
What it is made of: Stocks 100.1%, Cash -0.1%
Largest holdings: HDFC Bank Ltd 6.4%, Reliance Industries Ltd 6.0%, ICICI Bank Ltd 5.7%, Bharti Airtel Ltd 4.1%, Infosys Ltd 2.6%
Sector mix: Financial services 30.1%, Consumer cyclical 12.8%, Industrials 9.7%, Energy 8.6%
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.4% above the current prices
Holdings read: HDFCBANK.NS, RELIANCE.NS, ICICIBANK.NS, BHARTIARTL.NS, INFY.NS
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

_Not available today._

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> IYT is a concentrated transportation fund (top 5 holdings represent 53% of the fund) with mixed signals that do not compel a directional call. Technicals show weakness: the fund is down 7.5% in one month, trading 6.7% below its 50-day moving average, with RSI at 30.7 (oversold) and negative MACD histogram, while volume is subthreshold at 0.61x average. The fund's valuation multiples (P/E 20.28, P/B 4.25) remain elevated relative to historical norms for industrials. However, analyst coverage of the top holdings is broadly constructive: 90.8% buy-rated by weight with a +24.4% weighted price target, and recent rating changes include UNP upgraded to Buy on 2026-09-16. Macro backdrop shows rising short-term rates (3-month +7bp), a strengthening dollar (+1.23 on the week), and elevated VIX at 15.39—headwinds for equities and particularly for transportation (exposed to fuel costs and international demand). The fund's 1.28 beta to the market amplifies downside in a risk-off regime. The technicals suggest oversold conditions that could bounce, while analyst sentiment leans bullish, but the macro deterioration (rising rates, strong dollar) and technical breakdown do not yet signal a reversal. No decisive break either way; waiting for conviction.

**Main reasons it gave:**
- Technicals deeply oversold (RSI 30.7, -6.7% below 50d MA, -7.5% monthly)
- Analyst consensus +24.4% price target on 53% of fund (UNP Buy upgrade 2026-09-16)
- Dollar up 1.23 on week and short rates rising, headwind for transportation exposure
- Elevated valuation multiples (P/E 20.28, P/B 4.25) persist despite 1m decline
- Volume subthreshold at 0.61x 20d average, insufficient to confirm reversal

<details><summary><b>News</b> — score -0.15</summary>

- [IYT Looks 6.2% Overvalued on GF Value™ as of September 18, 2026](https://www.gurufocus.com/news/9087980/iyt-looks-62-overvalued-on-gf-value-as-of-september-18-2026)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 18, 2026, the iShares Transportation Average ETF (ticker: IYT) is trading near key technical pivot points derived from the DeMark calculation...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 80.07 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 83.73 (-4.4%), 50d 85.85 (-6.7%), 200d 81.07 (-1.2%); 50d above 200d
Momentum: RSI(14) 30.7 | MACD -1.550 vs signal -1.224 (histogram -0.327)
Returns: 1d -0.9% | 5d -2.5% | 1m -7.5% | 3m -4.6%
52-week range: 68.14 - 90.01 (now 54.5% of the way up)
Volatility: ATR(14) 1.30 (1.6% of price) | annualised 20d 16.4%
Volume: 0.61x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Industrials
What it holds: P/E 20.28 | P/B 4.25 | P/S 1.45 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +11.1% a year | beta to the market 1.28
Cost and size: expense ratio 0.37% | net assets 2.20B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Union Pacific Corp 17.8%, Uber Technologies Inc 15.4%, CSX Corp 9.4%, United Parcel Service Inc Class B 5.6%, Norfolk Southern Corp 4.9%
Sector mix: Industrials 83.8%, Technology 16.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.4% above the current prices
Holdings read: UNP, UBER, CSX, UPS, NSC
Recent rating changes among them:
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
  - UBER: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
  - CSX: 2026-07-24 Citigroup: main, Neutral -> Neutral
  - UPS: 2026-07-29 Stifel: main, Buy -> Buy
  - NSC: 2026-07-27 BMO Capital: main, Market Perform -> Market Perform
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

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> KRE holds a diversified basket of regional banks trading at low valuations (P/E 12.6, P/B 1.27) with a 2.2% yield. The technical picture is mixed: the fund is down 4.2% from its 50-day moving average and shows weak momentum (RSI 35.2, MACD negative), but remains above its 200-day average. Volume is light at 0.5x average. The macro backdrop shows yields rising modestly this week across the curve (3-month, 5-year up 7bps; 10-year up 3bps) with the yield curve normally sloped and the dollar strengthening. The analyst view is thin (7.1% coverage) but modestly constructive, with a 20.2% weighted price target above current prices on the top 5 holdings. Recent analyst actions are mixed: Morgan Stanley upgraded CFR and initiated PNFP at Overweight, but UBS initiated UMBF at Neutral. No news today, no macro surprise, and no decisive technical break. The valuation is attractive and the dividend is steady, but the price action is weak and momentum is deteriorating. Regional bank sentiment hinges on the interest rate path and economic growth; current conditions do not signal either a clear catalyst or a compelling reason to move. A small positive lean from valuations and analyst targets is offset by weak technicals and rising yields on a potentially margin-pressuring curve.

**Main reasons it gave:**
- RSI 35.2 with MACD below signal, price 4.2% below 50-day SMA
- P/E 12.6, P/B 1.27, and 2.2% yield suggest valuation floor
- Analyst price target 20.2% above current on top 5 holdings (7.1% coverage)
- Yields up 3-7bps this week; curve normally sloped but may pressure bank margins
- Low volume and no recent news; macro backdrop lacks a decisive catalyst

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 72.20 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 73.95 (-2.4%), 50d 75.36 (-4.2%), 200d 70.34 (+2.6%); 50d above 200d
Momentum: RSI(14) 35.2 | MACD -0.679 vs signal -0.520 (histogram -0.158)
Returns: 1d -0.7% | 5d -2.3% | 1m -3.7% | 3m +0.7%
52-week range: 58.14 - 77.93 (now 71.0% of the way up)
Volatility: ATR(14) 1.22 (1.7% of price) | annualised 20d 14.4%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 7.1% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.9% | hold 34.1% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.2% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-09-08 Morgan Stanley: up, Underweight -> Overweight
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-08-31 Benchmark: main, Buy -> Buy
  - PNFP: 2026-09-08 Morgan Stanley: init, ? -> Overweight
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
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

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> KSA is a focused Saudi Arabia equity fund with a low beta (0.18) to broader markets and modest three-year returns (+0.9% annually). The largest holdings (Al Rajhi Bank, Saudi Aramco, Saudi National Bank) trade at reasonable valuations (P/E 15.0) with analyst consensus bullish on the 44.4% covered by the top five (90% buy-rated, +15.3% price target). However, technicals are deteriorating: the price sits 2.8% below its 20-day MA, momentum is weak (RSI 35.3, MACD histogram deeply negative), and the fund is down 2.0-3.3% over the past month and three months. The 50-day MA is below the 200-day, signalling a downtrend. Volume is 34% of the 20-day average, indicating low conviction in either direction. Macro backdrop shows rising short-end yields (+7bp on the 3-month and 5-year) and a firmer dollar (+1.23 on the week), which can pressure emerging markets, though the yield curve remains normally sloped. The news—F-35 sales and Houthi tensions—touches geopolitics but does not constitute a material catalyst for the fund's near-term pricing. The fund's low beta and defensive characteristics suggest it will not lead in either direction. Analyst views on holdings are constructive but the technical deterioration, weak momentum, and low volume suggest the market has not yet priced in that upside, and near-term risk is biased down. A mild bearish lean is warranted on technicals, tempered by the fund's low volatility and reasonable valuations.

**Main reasons it gave:**
- Price 2.8% below 20-day MA with 50d below 200d; downtrend in place
- RSI 35.3 and MACD histogram -0.188 signal momentum deterioration
- Analyst consensus bullish (90% buy-rated) on largest holdings, +15.3% target, but technicals have not confirmed
- Volume at 34% of 20-day average suggests low conviction despite analyst upside
- Rising USD and short-end yields add headwind to emerging market regional fund

<details><summary><b>News</b> — score +0.00</summary>

- [Evening digest: US plans Saudi F-35 sales, oil prices fall](https://www.google.com/goto?url=CAESlwEB6zswFSmqNmkAGYQT9Tso6Zt9qwj0SWBe4JLfTlue5LRrm7nElr3bmTtCuzKbxIdMqAwcF6-RQBIN0XvIfYOWIerG4hYCJWZHiA_zTk0f9zYbK4rfY2tiA5EICFURgNwvJmETdCT47GNj9CQS0LQVm7Fb_VqpJPVB8oIYIcTFjfCntoGJ-OQ3j4GlsN7NyqGVjMh_IZrV)  
  <sub>Invezz, 20 hours ago</sub>  
  On Thursday, the US State Department notified Congress of a potential sale of up to 48 F-35 fighter jets to Saudi Arabia, while oil prices fell about 2% as...
- [Yemen War Debate Intensifies as Saudi Arabia Faces Houthi Attacks](https://www.google.com/goto?url=CAESmQEB6zswFeZi8Tgvs7KxX-tZo2HP9dD5rWVQyaMH8TnJTGxBccp7jQJE0jqopIZkSOV7_O6zp6qNyonpGGhdmSMl8eerP9HTL83hZd9F6F5VwjVE4oWYPUl2Lv2TXsHfAt0iRqYlPya-PamFmbvB_VXxuUVruE_Xj0zpdQ8PFC1bVyR9conVciUzRcZ17fJzB1xtXnIREQebx5Y)  
  <sub>Head Topics, 16 hours ago</sub>  
  A rewritten account of claims about Yemen, Saudi Arabia, Houthi actions, regional intervention and US diplomacy.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 37.34 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 38.40 (-2.8%), 50d 37.79 (-1.2%), 200d 38.14 (-2.1%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -0.168 vs signal 0.020 (histogram -0.188)
Returns: 1d -0.3% | 5d -2.3% | 1m -2.0% | 3m -3.3%
52-week range: 35.83 - 41.03 (now 29.0% of the way up)
Volatility: ATR(14) 0.29 (0.8% of price) | annualised 20d 11.1%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.06 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.3% above the current prices
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

_Not available today._

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> TUR is a focused Turkey equity fund showing technical weakness offset by attractive valuation and analyst support. Price has declined 5-9% over recent periods and trades 6% below its 20-day moving average, with momentum deteriorating (RSI 38.4, MACD negative). However, the fund's P/E of 13.81 and P/S of 0.66 remain attractive, and analysts covering its largest 5 holdings (40% of weight) are uniformly bullish with an 18.3% weighted price target. The yield of 2.1% is reasonable. Macro backdrop shows the dollar strengthening sharply (+1.23 on week) and Treasury yields rising, both headwinds for EM currencies and Turkish assets. The fund's low beta (0.44) and three-year return of only 0.9% annually suggest it has underperformed significantly. VIX at 15.39 is elevated but not extreme. The technical picture warrants caution, and currency strength is a headwind, but valuation support and analyst consensus prevent a bearish lean. This is a low-conviction hold awaiting either a technical bounce or macro reversal.

**Main reasons it gave:**
- Price -6% vs 20d MA with RSI 38.4 and negative MACD histogram
- P/E 13.81, P/S 0.66 near three-year lows attractive on valuation
- Analyst target +18.3% on 5 largest holdings (39.5% weight) all buy-rated
- US dollar +1.23 week headwind for Turkish assets
- 3-year record 0.9% annual return reflects persistent underperformance

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 37.25 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 39.65 (-6.1%), 50d 39.26 (-5.1%), 200d 39.25 (-5.1%); 50d above 200d
Momentum: RSI(14) 38.4 | MACD -0.455 vs signal -0.070 (histogram -0.385)
Returns: 1d -1.2% | 5d -7.9% | 1m -8.4% | 3m -9.1%
52-week range: 31.90 - 43.74 (now 45.2% of the way up)
Volatility: ATR(14) 0.81 (2.2% of price) | annualised 20d 34.7%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +0.9% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.68 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.3% above the current prices
Holdings read: ASELS.IS, TUPRS.IS, BIMAS.IS, AKBNK.IS, THYAO.IS
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

_Not available today._

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> VNQ shows mixed signals that do not support a directional call. Technicals are weak: the fund is down 5.4% over one month with RSI at 31.3 and MACD histogram negative, trading below all major moving averages. Macro backdrop is neutral-to-slightly-restrictive: Treasury yields have risen modestly across the curve this week (3M and 5Y +7bp), the dollar has strengthened +1.23 on the week, and the VIX remains elevated at 15.4, all headwinds for risk assets. However, fund basics show reasonable valuation relative to the portfolio's 3.6% yield and 0.98 beta, with three-year returns of +8.8% annualized. Analyst coverage of the five largest holdings (40% of the fund) is uniformly bullish, with a weighted price target 18.1% above current prices and all holdings rated buy, suggesting fundamental support at the holding level. The disconnect between weak technicals and bullish analyst consensus on the holdings, combined with rising rates and a stronger dollar pressuring real estate, argues for neutrality rather than either direction. The weakness appears technical and macro-driven rather than fundamental, but the macro headwinds are real enough to prevent a bullish lean without a reversal in yields or dollar strength. Recent coverage includes rating maintenance and one upgrade (AMT), not a catalyst.

**Main reasons it gave:**
- RSI 31.3 and MACD negative; trading 4.5% below 50d SMA
- Analyst consensus 100% buy with +18.1% price target on 40% of fund by weight
- Treasury yields +7bp at 3M and 5Y; dollar +1.23 on week; elevated VIX 15.4
- 3.6% yield and reasonable valuation at 3y +8.8% annualized return
- Low volume at 0.46x 20d average; 5d -1.6% and 1m -5.4% drawdowns

<details><summary><b>News</b> — score +0.00</summary>

- [These real estate stocks stand out for attractive valuations (VNQ:NYSEARCA)](https://seekingalpha.com/news/4644246-these-real-estate-stocks-stand-out-for-attractive-valuations)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  Discover 11 undervalued real estate stocks and REITs ranked by Valuation Grade, plus top real estate ETFs—get timely ideas for today's market.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.55</summary>

```text
Last close 93.26 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 96.02 (-2.9%), 50d 97.67 (-4.5%), 200d 94.30 (-1.1%); 50d above 200d
Momentum: RSI(14) 31.3 | MACD -1.212 vs signal -0.963 (histogram -0.249)
Returns: 1d -0.6% | 5d -1.6% | 1m -5.4% | 3m -2.4%
52-week range: 87.00 - 100.95 (now 44.9% of the way up)
Volatility: ATR(14) 1.13 (1.2% of price) | annualised 20d 9.1%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +8.8% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 70.82B
What it is made of: Stocks 99.1%, Cash 0.7%, Other 0.2%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 8.7%, Prologis Inc 6.9%, Equinix Inc 5.5%, American Tower Corp 4.3%
Sector mix: Real estate 99.4%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.1% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-10 BTIG: main, Buy -> Buy
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

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLB is trading modestly below its moving averages (50d SMA 51.77 vs 50.01 close) with momentum deteriorating sharply: RSI at 35.6 suggests oversold conditions, while MACD has turned negative with widening histogram. Recent price action shows -4.8% over one month and -1.4% today on below-average volume, typical of a pullback rather than a conviction move. News mentions cyclical rotation into automakers and dividend sustainability concerns, but these are thin narratives in a broad sector context. Macro backdrop is mixed: Treasury yields have ticked higher across the curve this week (3m, 5y both +7bp), the dollar has rallied 123bp, and VIX remains elevated at 15.4, conditions that typically constrain materials demand. Analyst coverage of the fund's top 37% of holdings is uniformly bullish—100% buy-rated with a +13.7% target—and recent rating initiations by Keybanc on Linde (Overweight) and RBC maintaining Newmont (Outperform) provide some support. Fund valuations are elevated (P/E 24.59, P/B 3.00) relative to long-term history, and the GuruFocus mention of overvaluation hints at a stretched entry point. The 52-week position (68th percentile) leaves room below, and the fund's 0.82 beta suggests it will underperform in a risk-off environment. Technicals and macro setup argue for patience; analyst targets provide upside optionality but are not a sufficient counter-signal to weakness. This is a pause rather than a clear inflection.

**Main reasons it gave:**
- RSI 35.6 and negative MACD histogram signal oversold momentum
- Treasury yields up 3-7bp across curve, dollar +123bp on week
- Analysts rate top 37% of holdings at 100% buy with +13.7% target
- P/E 24.59 and P/B 3.00 valuations elevated; GuruFocus signals overvaluation
- Below-average volume on 1.4% daily decline suggests thin conviction selling

<details><summary><b>News</b> — score +0.00</summary>

- [XLB Looks 4.5% Overvalued on GF Value™ as Dividend Sustainabilit](https://www.gurufocus.com/news/9087970/xlb-looks-45-overvalued-on-gf-value-as-dividend-sustainability-remains-key)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 18, 2026, the S&P Select Materials SPDR ETF (ticker: XLB) established critical pivot points signaling potential shifts in its trading range.
- [These materials stocks stand out for strong dividend growth (XLB:NYSEARCA)](https://seekingalpha.com/news/4644258-these-materials-stocks-stand-out-for-strong-dividend-growth?utm_source=tradingview&utm_medium=referral&feed_item_type=news)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Materials stocks remain an important area of the market as investors weigh commodity prices, industrial demand and the outlook for global economic growth.
- [Leading And Lagging Sectors For September 18, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61867052/leading-and-lagging-sectors-september-18-2026)  
  <sub>Benzinga, 4 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLC) State Street Communication Services Select Sector SPDR ETF 112.6400 0.290 0.25 1.0K...
- [Automaker Stocks Rally as Rotation Lifts Cyclicals: General Motors Climbs 4%, Stellantis Rises 4%, Ford Gains 3%, Tesla Adds 2%](https://247wallst.com/investing/2026/09/17/automaker-stocks-rally-as-rotation-lifts-cyclicals-general-motors-climbs-4-stellantis-rises-4-ford-gains-3-tesla-adds-2/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Four automakers with nothing in common are surging in lockstep Thursday morning, and the reason behind that unusual uniformity tells investors something...
- [XLY Looks 4.3% Undervalued on GF Value™](https://www.gurufocus.com/news/9087973/xly-looks-43-undervalued-on-gf-value)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 18, 2026, the latest pivot points for the State Street Consumer Discretionary Select Sector SPDR ETF (ticker: XLY) were identified using the...
- [These ten consumer discretionary stocks score highest on dividend growth (XLY:NYSEARCA)](https://seekingalpha.com/news/4644307-these-ten-consumer-discretionary-stocks-score-highest-on-dividend-growth)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Top 10 consumer discretionary dividend growth stocks with A+ grades (BKNG, HD, LOW, MCD & more).

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 50.01 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 52.04 (-3.9%), 50d 51.77 (-3.4%), 200d 50.40 (-0.8%); 50d above 200d
Momentum: RSI(14) 35.6 | MACD -0.520 vs signal -0.254 (histogram -0.266)
Returns: 1d -1.4% | 5d -1.8% | 1m -4.8% | 3m -3.5%
52-week range: 42.23 - 53.67 (now 68.1% of the way up)
Volatility: ATR(14) 0.79 (1.6% of price) | annualised 20d 15.2%
Volume: 0.39x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Natural Resources
What it holds: P/E 24.59 | P/B 3.00 | P/S 2.01 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +9.3% a year | beta to the market 0.82
Cost and size: expense ratio 0.08% | net assets 8.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Linde PLC 13.1%, Newmont Corp 7.8%, Freeport-McMoRan Inc 6.3%, Corteva Inc 4.9%, Air Products and Chemicals Inc 4.8%
Sector mix: Basic materials 84.5%, Consumer cyclical 15.5%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.7% above the current prices
Holdings read: LIN, NEM, FCX, CTVA, APD
Recent rating changes among them:
  - LIN: 2026-09-11 Keybanc: init, ? -> Overweight
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - FCX: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - CTVA: 2026-09-18 Argus Research: reit, Buy -> Buy
  - APD: 2026-09-11 Keybanc: init, ? -> Sector Weight
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

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLC holds communication services stocks with weighted analyst price targets 15.9% above current levels, and its top 5 holdings command unanimous buy ratings. However, the technical picture is deteriorated: the fund trades below both its 20-day and 50-day moving averages, momentum is negative with MACD histogram below its signal line, and the RSI sits at 47.2, suggesting recent selling pressure. The 1-day and 5-day returns are negative despite a broad market rebound Thursday. Netflix, a potential major holding or sector bellwether, was cut to Underweight by Wells Fargo, introducing sector-specific headwinds. Macro backdrop shows Treasury yields up modestly across most of the curve with the dollar strengthening (+1.23 on the week), which can pressure tech-heavy communication services. The fund trades below its 200-day moving average (-2.4%), signaling a longer-term downtrend. Volatility at 15.39 is elevated and volume is subdued. The analyst consensus on holdings is constructive and medium-term fundamentals remain sound, but near-term technical deterioration and Netflix weakness create a near-term headwind that offsets the positive fundamental backdrop. This deserves a hold signal with modest conviction, as the contradictions between analyst views and technical momentum are significant.

**Main reasons it gave:**
- Analysts see 15.9% upside on largest 5 holdings with 100% buy ratings
- Fund below 20d, 50d, and 200d moving averages; MACD histogram negative
- Netflix cut to Underweight by Wells Fargo, a sector headwind
- Rising treasury yields and stronger dollar pressure communication equities
- Subdued volume on recent weakness suggests limited conviction in selling

<details><summary><b>News</b> — score +0.00</summary>

- [Netflix Falls 4% as Wells Fargo Cuts Rating to Underweight With $57 Target; Disney Barely Budges](https://247wallst.com/investing/2026/09/18/netflix-falls-4-as-wells-fargo-cuts-rating-to-underweight-with-57-target-disney-barely-budges/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Wells Fargo just handed Netflix one of the street's most bearish ratings while a rival analyst pushed a price target nearly double that level,...
- [Leading And Lagging Sectors For September 18, 2026](https://www.google.com/goto?url=CAESngEB6zswFV7dPpP14v9zUI1kLd1L2Wlh7pwhL7YSy6JZCjXIXXaTElcFTT-zFlzhNYsdKeY3AH3vVCpHWhYNrDH3ZFPxPE8tpJt6YpAWuzkHpjCCbgDidmhr1BgPVoDkRN2-vHgurjT_riFnuJ5l8iH51x0eLVAhfSroGB1rVcQAik9jkL_nqVB098viMSGcT_ryjdggTfhchJlYMo0AtQ)  
  <sub>Benzinga, 3 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLC) State Street Communication Services Select Sector SPDR ETF 112.6400 0.290 0.25 1.0K...
- [Nasdaq 100 Rallies as Oil Slides, Yields Retreat: Stock Market Today](https://www.google.com/goto?url=CAEStQEB6zswFc8c6l2i9EBZWZ6FPIIWM3Qghj-taZ4zuXIOBYU2uZ9cNDdOZ5b5tPNDyoBcyULth0bjj5oZCjB9sNnbnb10hyIWiYb0YIWFW10c4Iz1h9wP6_1vjGQeJqj6WPrHRU0GDDeCN3t4iTlstEDZHpwV0s2qGZm0ixtmXHCaJSZPKWWQfwnvABRU4oZw6RYJqLp-jRLuPUC8lq5EBHQENV9I1uF6C23TaYVL-LqT54pEBQDm)  
  <sub>TradingView, 23 hours ago</sub>  
  U.S. stocks rebounded sharply Thursday, erasing two sessions of losses as crude oil retreated from its geopolitical spike and Treasury yields eased back...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 111.22 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 112.31 (-1.0%), 50d 111.20 (+0.0%), 200d 114.00 (-2.4%); 50d below 200d
Momentum: RSI(14) 47.2 | MACD 0.382 vs signal 0.464 (histogram -0.082)
Returns: 1d -1.0% | 5d -1.2% | 1m -0.1% | 3m +1.6%
52-week range: 105.38 - 120.08 (now 39.8% of the way up)
Volatility: ATR(14) 1.68 (1.5% of price) | annualised 20d 16.7%
Volume: 0.46x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.35</summary>

```text
Fund type: Communications
What it holds: P/E 15.38 | P/B 2.92 | P/S 2.06 | 3y earnings growth n/a
Yield: 1.3%
Three-year record: +20.1% a year | beta to the market 0.85
Cost and size: expense ratio 0.08% | net assets 22.43B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Meta Platforms Inc Class A 16.8%, Alphabet Inc Class A 10.3%, Alphabet Inc Class C 8.2%, AT&T Inc 5.3%, Verizon Communications Inc 5.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.9% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-07-23 Wolfe Research: up, Peer Perform -> Outperform
  - VZ: 2026-07-27 TD Cowen: main, Buy -> Buy
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

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLF trades below its 20- and 50-day moving averages after a 2.9% decline over the past month, with RSI at 36.6 and MACD deeply negative, signaling oversold technicals in the near term. However, the fund remains 4.0% above its 200-day SMA with an upward-sloping yield curve (1.02 points) and a normal macro backdrop. Analyst consensus on the largest holdings (41.5% of fund weight) is unanimously bullish with an 11.6% price target, and valuations at P/E 16.36 are reasonable for quality financial franchises. The fund's three-year performance of +19.0% annualized reflects structural strength. Against this, a Fed decision today creates near-term uncertainty; the dollar has surged 123 basis points this week, which typically pressures financial stocks; and volume is well below average, suggesting weak conviction. The technicals warrant caution despite fundamental support. A data surprise from the Fed announcement could shift this meaningfully, but without that catalyst the evidence points to a consolidation rather than a directional move.

**Main reasons it gave:**
- Oversold technicals with RSI 36.6 and MACD -0.264 histogram
- Analyst consensus 100% buy on top 41.5% of holdings with +11.6% price target
- Dollar up 123 bps this week, headwind for financials
- Fed decision today creates near-term uncertainty
- Volume 0.42x 20-day average, weak participation

<details><summary><b>News</b> — score +0.10</summary>

- [Zoomex Highlights ETF Perpetuals Ahead of This Week’s Federal Reserve Decision](https://markets.businessinsider.com/news/stocks/zoomex-highlights-etf-perpetuals-ahead-of-this-week-s-federal-reserve-decision-1036557174)  
  <sub>markets.businessinsider.com, 1 hour ago</sub>  
  VICTORIA, Seychelles,, Sept. 18, 2026 (GLOBE NEWSWIRE) -- With the U.S. Federal Reserve scheduled to announce its latest interest-rate decision ...
- [Betting Against Banks With FAZ? You’re Actually Shorting Insurers and Brokers](https://247wallst.com/investing/etf/2026/09/18/betting-against-banks-with-faz-youre-actually-shorting-insurers-and-brokers/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Traders reaching for FAZ to short banks after the latest Fed hike may be paying for exposure to insurers and payment networks instead, and the math gets...
- [Leading And Lagging Sectors For September 18, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61867052/leading-and-lagging-sectors-september-18-2026)  
  <sub>Benzinga, 3 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLC) State Street Communication Services Select Sector SPDR ETF 112.6400 0.290 0.25 1.0K...
- [3 Best ETFs for 14%+ Upside Potential, According to the AI Analyst](https://www.tipranks.com/news/3-best-etfs-for-14-upside-potential-according-to-the-ai-analyst)  
  <sub>TipRanks, 17 hours ago</sub>  
  TipRanks' ETF AI Analyst has an Outperform rating on the Vanguard Dividend Appreciation ETF ($VIG), Financial Select Sector SPDR Fund ($XLF),...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.10</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 55.82 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 57.37 (-2.7%), 50d 57.18 (-2.4%), 200d 53.69 (+4.0%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -0.299 vs signal -0.035 (histogram -0.264)
Returns: 1d -0.1% | 5d -2.5% | 1m -2.9% | 3m +4.2%
52-week range: 47.81 - 58.56 (now 74.5% of the way up)
Volatility: ATR(14) 0.70 (1.3% of price) | annualised 20d 13.3%
Volume: 0.42x the 20-day average
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
Three-year record: +19.0% a year | beta to the market 0.71
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.6% above the current prices
Holdings read: JPM, BRK-B, V, MA, BAC
Recent rating changes among them:
  - JPM: 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - V: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - MA: 2026-08-31 RBC Capital: main, Outperform -> Outperform
  - BAC: 2026-08-03 UBS: main, Buy -> Buy
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

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> XLI is in a clear short-term downtrend: -7.2% over a month, below the 20d and 50d SMAs and now 1.7% under the 200d, with RSI 31 and MACD negative. But that is oversold into support rather than a fresh break, and volume is only half average, so no decisive breakdown has occurred. Macro is mildly restrictive -- 10y at 5.00%, dollar +1.23 on the week -- with a Fed decision pending, which argues for waiting rather than pressing. Valuation is stretched (P/E 28.4, industrials now above tech on forward P/E), while analyst coverage of the top 25.8% of the fund is uniformly buy with +24.9% targets, an offsetting bullish but backward-looking read. No positioning data; flows not given, so insider dimension is null. Note the GuruFocus 'overvalued' items are low-quality promotional screens and were weighted lightly.

**Main reasons it gave:**
- RSI 31, price below 20d/50d and 1.7% under 200d SMA
- -7.2% 1-month return with volume only 0.52x average (no capitulation)
- Holdings P/E 28.4; industrials forward P/E now above technology
- 10y yield 5.00%, dollar +1.23 on week, Fed decision imminent
- Top-5 holdings 100% buy-rated, +24.9% weighted target over 25.8% of fund

<details><summary><b>News</b> — score -0.15</summary>

- [XLI Looks 15.7% Overvalued on GF Value™](https://www.gurufocus.com/news/9087987/xli-looks-157-overvalued-on-gf-value)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 18, 2026, Goldman Sachs Research highlighted a notable shift in sector valuations, with industrials now trading at a forward P/E of 19.4x,...
- [Industrials now trade at higher forward P/E than technology: Goldman Sachs (XLI:NYSEARCA)](https://seekingalpha.com/news/4644262-industrials-now-trade-at-higher-forward-pe-than-technology-goldman-sachs)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Goldman Sachs Research said industrials are now trading at a higher 12-month forward P/E valuation than technology, highlighting a shift in relative sector...
- [Leading And Lagging Sectors For September 18, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61867052/leading-and-lagging-sectors-september-18-2026)  
  <sub>Benzinga, 3 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLC) State Street Communication Services Select Sector SPDR ETF 112.6400 0.290 0.25 1.0K...
- [XLK hovers above the level that matters most (XLK:NYSEARCA)](https://seekingalpha.com/news/4644191-xlk-hovers-above-the-level-that-matters-most)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  XLK nears key $182 support where anchored VWAPs converge—an important test for the tech ETF's consolidation range.
- [Webcast: Active ETFs are capturing investor attention - here’s why | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/14/active-etfs-are-capturing-investor-attention-heres-why?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 3 minutes ago</sub>  
  What's driving the rapid growth of active ETFs, and what could it mean for client portfolios? Join Fidelity Investments to explore the forces behind the...
- [GE Aerospace Stabilizes After Pullback: Chart of the Day](https://www.barrons.com/articles/ge-aerospace-stock-stabilizes-after-pullback-chart-of-the-day-c527c0f5)  
  <sub>Barron's, 2 hours ago</sub>  
  Industrial stocks have emerged as the market's weakest link over the past month, with the State Street Industrial Select Sector SPDR ETF · XLI.
- [Zoomex Highlights ETF Perpetuals Ahead of This Week’s Federal Reserve Decision](https://markets.businessinsider.com/news/stocks/zoomex-highlights-etf-perpetuals-ahead-of-this-week-s-federal-reserve-decision-1036557174)  
  <sub>markets.businessinsider.com, 1 hour ago</sub>  
  VICTORIA, Seychelles,, Sept. 18, 2026 (GLOBE NEWSWIRE) -- With the U.S. Federal Reserve scheduled to announce its latest interest-rate decision ...
- [ETFs Investing in Nordson Corporation Stocks](https://www.tradingview.com/symbols/BIVA-NDSN/etfs/)  
  <sub>TradingView, 21 hours ago</sub>  
  Explore funds investing in NDSN in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.
- [XLK Looks 35.3% Overvalued on GF Value™ as of September 18, 2026](https://www.gurufocus.com/news/9087978/xlk-looks-353-overvalued-on-gf-value-as-of-september-18-2026)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 18, 2026, the Technology Select Sector SPDR ETF (ticker: XLK) established new pivot points using the DeMark analysis method, setting a pivot...
- [TTEQ: Technology Dashboard For September (NASDAQ:TTEQ)](https://seekingalpha.com/article/4947838-tteq-technology-dashboard-for-september)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Summary. Software and IT services appear undervalued relative to 11-year averages, while other subsectors remain overvalued. T Rowe Price Technology ETF...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.45</summary>

```text
Last close 168.76 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 173.94 (-3.0%), 50d 178.96 (-5.7%), 200d 171.63 (-1.7%); 50d above 200d
Momentum: RSI(14) 31.0 | MACD -3.212 vs signal -2.767 (histogram -0.445)
Returns: 1d -0.1% | 5d -2.1% | 1m -7.2% | 3m -6.7%
52-week range: 147.83 - 186.51 (now 54.1% of the way up)
Volatility: ATR(14) 2.45 (1.4% of price) | annualised 20d 12.9%
Volume: 0.52x the 20-day average
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
Three-year record: +18.8% a year | beta to the market 1.02
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.9% above the current prices
Holdings read: CAT, GE, RTX, GEV, UNP
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
  - RTX: 2026-08-03 Bernstein: main, Market Perform -> Market Perform
  - GEV: 2026-09-15 Bernstein: reit, Outperform -> Outperform
  - UNP: 2026-09-16 UBS: up, Neutral -> Buy
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

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.25

**In the model's own words:**

> XLY faces conflicting signals that do not support a directional call. Technicals are weak: the fund trades 3-5% below its major moving averages, RSI at 38 shows oversold conditions but momentum is deteriorating (MACD histogram negative), and the fund is at the low end of its 52-week range with volume below average. The downtrend across 1m, 3m and ytd returns is material, and the 200d slope is inverted against the 50d, a bearish setup. However, macro conditions remain benign: Treasury yields have moved modestly, the dollar strengthened but volatility remains elevated at 15.4, and energy has retreated. Analyst coverage of the top 55% of holdings is uniformly bullish (100% buy) with a +23.3% price target, but this is thin coverage and does not account for broader fund composition or cyclical sensitivity. Fund valuation at P/E 25.48 and P/B 5.89 is elevated for a consumer cyclical basket in a period of macro uncertainty. The rotation trade noted in news—automakers rallying then reversing—illustrates the choppiness in cyclical sentiment; a one-day reversal does not establish a directional bias. AMZN (24.4% weight) and TSLA (17.3% weight) dominate the fund, and analyst changes among top holdings are neutral-to-stable. Neither the technical break nor macro data suggests a clear entry point for a bullish call, and the oversold RSI with deteriorating momentum does not yet confirm a reversal. A bounce from oversold levels is possible but not yet visible in price action or volume. The case for a bearish call is similarly incomplete: the fund remains supported by positive analyst targets and has not broken technical support decisively.

**Main reasons it gave:**
- RSI at 38 with negative MACD histogram; price 3-5% below key moving averages
- Analyst consensus 100% buy on top 55% of fund, +23.3% weighted target
- Elevated P/E 25.48 and P/B 5.89 amid macro uncertainty and rotation chop
- One-day automaker rally reversed sharply; cyclical sentiment unstable

<details><summary><b>News</b> — score +0.00</summary>

- [These ten consumer discretionary stocks score highest on dividend growth (XLY:NYSEARCA)](https://www.google.com/goto?url=CAESpgEB6zswFYjWaXak5G0-ZdGsTJs41glbHztdqIs84NUIgIqorF8anKrpIG2Rfwp7o6HrErPFYNBUlraD2tzM1PdqAV0EEEqafiWN0z1DoNQ_y18wQDRVqM-rLtS6GMQqZS4w30VoK_56mWOhiwDts-dtAtPtNkLJ7n3Leyz8N4GnXD2dHfFqi8OrKCo8ODt-ttmj4x9q83JZZhaSu3zx7azvpTscYxw-)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Top 10 consumer discretionary dividend growth stocks with A+ grades (BKNG, HD, LOW, MCD & more).
- [Automaker Stocks Reverse as Rotation Trade Unwinds: General Motors and Stellantis Fall 4%, Ford Pulls Back](https://www.google.com/goto?url=CAESzAEB6zswFcVIw0MnYpr1EI5uXOkBZq3yyA-dzsPeYmaofpXkVfs5jRA1ToaORVw5uhKyAS2NjSmCRTnBYHsik5BzmiKwbHQJHji_oAYQfagc9D4kWxyhovurFRn3hpgVobp4MQ__a8fjHgfYl7Y0o6GEU_kBWQxO-75MtQcK-4szMyf21KXUW_QjuHnoFa48XoUoLIHxxu8pUWxEbgHyBib4959RxyVTupm9wdlIPfr_l5I4aSDk6qvrcQc8qoIjbiL9i18P-pO6L_qk1JU)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Thursday's rotation rally handed automakers a one-day reprieve from months of pressure, but Friday morning that same trade ran straight into reverse,...
- [XLY Looks 4.3% Undervalued on GF Value™](https://www.google.com/goto?url=CAESgwEB6zswFaIXl63CWnXegEIIZ8eMjdizebfjstMCebCkeEylBqdzYAvRUjg85vd7cejFT5E2euK4CDBBPzm-GPGagcLH-HgDDtOOjFhFKnFyLO3BcJKLrmYL-Skvg3FxAZl73sh7rE-MpKxNxAq3GS9D8Hy_SJWcQvuakzR2MkJREuwhCQ)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 18, 2026, the latest pivot points for the State Street Consumer Discretionary Select Sector SPDR ETF (ticker: XLY) were identified using the...
- [Automaker Stocks Rally as Rotation Lifts Cyclicals: General Motors Climbs 4%, Stellantis Rises 4%, Ford Gains 3%, Tesla Adds 2%](https://www.google.com/goto?url=CAES3AEB6zswFS5jipYu1Xsy_fY0Hb60s0aFwjmLf9lDbTlzktg2qJHD0wG50y4Qdj3XJb1ubN1dG21u5zLCejPg2SMDVq-3UYFTAObYFFQ_8DRpwPaOwPUo7NjGWSRgRWUMBtuCcIJP8och3f14xs7bZH2aKjh0_mCkz4MxPAQIBlhglorweWrzBWN3Y6mIMJgGLPKz7C6SRyrJccoGIfvGdVv_RmMnzUy0LsCpFUmHQioJHSotIizFKQOnQQKdKcin8gF1Qgd6Ff442Lbf-NM2TAFppAlJu6PWAntUk1rC)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Four automakers with nothing in common are surging in lockstep Thursday morning, and the reason behind that unusual uniformity tells investors something...
- [Nasdaq 100 Rallies as Oil Slides, Yields Retreat: Stock Market Today](https://www.google.com/goto?url=CAEStQEB6zswFf_POZUZuqdnIj0Fis2WPvIN6MIMNfW0gl0cdoson4VIpKwbSdrbe3GVnMh-M_b5Ug-sHQ3XWNknMhWD-ktCzvRRCzoJ-iFu8SlkTg7oZUTBPTtHycgGvUJeABHzM0YnsmfTjmVL5nL8jCu7whXPc2F_GdVEMaaxUNZEE-tQHvEqjsENP2cQw2-Jm56pnj6LY5dQQ1X0X77GaJkoQj1MMK9nfEcQD600mQsn8AEoH6AF)  
  <sub>TradingView, 23 hours ago</sub>  
  U.S. stocks rebounded sharply Thursday, erasing two sessions of losses as crude oil retreated from its geopolitical spike and Treasury yields eased back...
- [On Holding Climbs 5% as Kylian Mbappé Joins Its Football Push; Nike Slips](https://www.google.com/goto?url=CAESqwEB6zswFdvSsGVK4jGQZfvQdVWs6wZuO1PRNxXRxgyAn5dXk8k8-hd_odHDnrK0t4SG7iqJCsEYskZMAHBYazwHxK8Rc9N_G_vXxs_q1zb1BJK9tmomsoipyPlsGe_9l6DXJumiM677KRhg0Zd7NbRYc8UITETPlo1P4GQu5IsPvgM5bXJs38M_FNqH_vdyHXBilHns2fDGe92CrpAdfxbXSk9z9k5HKGUNwqI)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Kylian Mbappé is stepping into football boots for a Swiss brand that has never sold a cleat, and Nike stock is already feeling it.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 111.03 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 114.48 (-3.0%), 50d 115.37 (-3.8%), 200d 116.84 (-5.0%); 50d below 200d
Momentum: RSI(14) 38.0 | MACD -1.510 vs signal -1.070 (histogram -0.440)
Returns: 1d -0.3% | 5d -1.7% | 1m -6.4% | 3m -5.2%
52-week range: 105.66 - 124.52 (now 28.4% of the way up)
Volatility: ATR(14) 1.63 (1.5% of price) | annualised 20d 15.6%
Volume: 0.40x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 25.48 | P/B 5.89 | P/S 2.51 | 3y earnings growth n/a
Yield: 0.8%
Three-year record: +9.5% a year | beta to the market 1.16
Cost and size: expense ratio 0.08% | net assets 22.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 24.4%, Tesla Inc 17.3%, The Home Depot Inc 5.4%, McDonald's Corp 4.1%, Booking Holdings Inc 3.9%
Sector mix: Consumer cyclical 98.8%, Technology 1.2%
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
Rolled up from the 5 largest holdings, 55.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.77 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.3% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-03 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-09-16 Goldman Sachs: reit, Neutral -> Neutral
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-17 Citigroup: main, Buy -> Buy
  - BKNG: 2026-09-01 Rosenblatt: init, ? -> Buy
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

### Argentina (ARGT) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro catalyst specific to Argentina in the last day. Technicals are soft but not decisive: price below 20d and 50d SMAs, MACD rolled over, RSI 42, but sitting right on the 200d with 50d above 200d and thin volume. Macro backdrop is mildly adverse for an EM single-country fund: 10y at 5.00% and a dollar up 1.23 on the week, though VIX is calm at 15.4. Holdings analyst view is supportive (100% buy by weight, +30% weighted target) but covers only 51% of the fund and is heavily MercadoLibre-driven, so it does not justify a directional macro call. No positioning data; no flow data, so insider dimension left null.

**Main reasons it gave:**
- Price below 20d (-2.6%) and 50d (-1.5%) SMAs, MACD histogram -0.382, RSI 42
- Dollar index +1.23 on the week, a headwind for EM single-country equity
- 10-year at 5.00%, curve normal-sloping +1.02, VIX 15.4 with no rate surprise this week
- Analyst roll-up 100% buy with +29.6% weighted target but only 51% fund coverage, 25% in MELI alone
- Volume 0.37x 20-day average, so the pullback lacks conviction

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 92.61 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 95.04 (-2.6%), 50d 93.98 (-1.5%), 200d 92.74 (-0.1%); 50d above 200d
Momentum: RSI(14) 42.2 | MACD 0.107 vs signal 0.489 (histogram -0.382)
Returns: 1d -1.3% | 5d -2.9% | 1m +1.3% | 3m -4.6%
52-week range: 67.55 - 102.94 (now 70.8% of the way up)
Volatility: ATR(14) 1.89 (2.0% of price) | annualised 20d 17.9%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.15</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.48 | P/B 1.77 | P/S 1.36 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +28.7% a year | beta to the market 0.50
Cost and size: expense ratio 0.59% | net assets 815.33M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 25.4%, YPF SA ADR 9.5%, Vista Energy SAB de CV ADR 6.2%, Grupo Financiero Galicia SA ADR 5.6%, Banco Macro SA ADR 4.3%
Sector mix: Consumer cyclical 30.4%, Energy 19.4%, Financial services 14.4%, Basic materials 12.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.61 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +29.6% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, BMA
Recent rating changes among them:
  - MELI: 2026-09-03 BTIG: reit, Buy -> Buy
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
  - BMA: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> EIS sits in a mild uptrend (50d above 200d, price ~2.4% above both) but momentum is flattening (MACD histogram slightly negative, RSI 54) and volume is very thin at 0.19x average. No macro or Israel-specific catalyst in the last 24 hours. Macro backdrop is mildly restrictive: 10y at 5.00% with short and belly yields up on the week and a firmer dollar (+1.23), a modest headwind for a focused emerging/regional equity fund, though VIX at 15.4 is calm. Analyst roll-up is supportive (100% buy by weight, +15% target) but covers only 37.6% of the fund and is concentrated in Teva plus two banks. Nothing here clears the bar for a directional macro call.

**Main reasons it gave:**
- Price 2.4% above both 50d and 200d SMA with 50d above 200d, but MACD histogram -0.02 and RSI 54
- Volume only 0.19x 20-day average - no conviction in the move
- 10-year at 5.00% (+3bp), 5-year +7bp, dollar index +1.23 on the week
- Analyst roll-up 100% buy by weight, +15% weighted target, but only 37.6% coverage and top-heavy (Teva 10%, two banks 17%)
- No macro or region-specific news in past 24 hours

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 124.82 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 123.74 (+0.9%), 50d 121.95 (+2.4%), 200d 121.86 (+2.4%); 50d above 200d
Momentum: RSI(14) 54.3 | MACD 0.524 vs signal 0.544 (histogram -0.020)
Returns: 1d -0.4% | 5d +0.9% | 1m +1.5% | 3m +1.5%
52-week range: 94.16 - 137.69 (now 70.4% of the way up)
Volatility: ATR(14) 1.70 (1.4% of price) | annualised 20d 19.6%
Volume: 0.19x the 20-day average
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
Three-year record: +33.4% a year | beta to the market 1.07
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.37 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.0% above the current prices
Holdings read: TEVA, LUMI.TA, POLI.TA, TSEM.TA, ESLT.TA
Recent rating changes among them:
  - TEVA: 2026-09-09 Leerink Partners: init, ? -> Outperform
  - TSEM.TA: 2026-09-18 Barclays: init, ? -> Overweight
  - ESLT.TA: 2026-08-19 JP Morgan: main, Neutral -> Neutral
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

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise to trade. Brazil equities are 9% higher on the month but stalled this week (-2% over 5 days, MACD rolling over, 50d still below 200d) on thin volume. The macro backdrop is mildly unhelpful for EM: dollar index +1.23 on the week and the US 10-year at 5.00%, which is a headwind to a high-beta, commodity-heavy basket. Offsetting that, valuation is cheap (P/E 10.5, 4.1% yield) and analyst coverage on 41% of the fund is uniformly buy with a +23% weighted target, though one holding (NU) was downgraded. The only news item is an options-volume roundup, which is noise. Net: no edge either way.

**Main reasons it gave:**
- Dollar index +1.23 on the week and US 10-year at 5.00% -- headwind for EM/commodity beta
- 5d return -2.0% with MACD histogram negative after +9.3% month; 50d SMA still below 200d
- Volume only 0.41x 20-day average -- no decisive break
- Holdings P/E 10.5, 4.1% yield; analyst roll-up 100% buy, +23.5% target over 40.9% of fund
- Only news item is an options-volume roundup, not macro information

<details><summary><b>News</b> — score +0.00</summary>

- [IShares MSCI Brazil ETF Options Spot-On: On September 17th, 447.75K Contracts Were Traded, With 7.89 Million Open Interest](https://news.futunn.com/en/post/79435362/ishares-msci-brazil-etf-options-spot-on-on-september-17th)  
  <sub>富途牛牛, 20 hours ago</sub>  
  OnSeptember 17th ET, $iShares MSCI Brazil ETF(EWZ.US)$ had active options trading, with a total trading volume of 447.75K options for the day,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 37.43 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 37.07 (+1.0%), 50d 36.04 (+3.9%), 200d 36.18 (+3.5%); 50d below 200d
Momentum: RSI(14) 55.9 | MACD 0.641 vs signal 0.676 (histogram -0.035)
Returns: 1d -0.8% | 5d -2.0% | 1m +9.3% | 3m +11.0%
52-week range: 28.79 - 41.73 (now 66.8% of the way up)
Volatility: ATR(14) 0.80 (2.1% of price) | annualised 20d 23.4%
Volume: 0.41x the 20-day average
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
Three-year record: +11.4% a year | beta to the market 0.84
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.5% above the current prices
Holdings read: VALE3.SA, NU, ITUB4, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-09-16 Itau BBA: down, Outperform -> Market Perform
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

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro catalyst for South Africa this cycle. Technicals are mixed-to-soft: price below 20d and 200d SMA, 50d below 200d, MACD histogram negative, RSI 47, volume very thin. Fundamentals are cheap (P/E 9.3, 7.1% yield) and analyst roll-up over 45.6% of the fund is 100% buy with +23.5% targets, but that is heavily gold-miner driven and not a timing signal. Dollar up 1.2 on the week and a 10-year at 5.00% are mild headwinds for EM. No positioning or flow data, so insider score is null. Nothing specific enough to justify a side.

**Main reasons it gave:**
- Price below 20d (-2.8%) and 200d (-1.2%) SMAs with 50d under 200d
- MACD below signal, histogram -0.521, RSI 46.8
- Dollar index +1.23 on the week, 10y at 5.00% — EM headwind
- Holdings P/E 9.31 with 7.1% yield; 41% basic materials, 23.6% gold miners
- Analyst roll-up over 45.6% of fund: 100% buy, +23.5% weighted target

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.25</summary>

```text
Last close 68.42 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 70.41 (-2.8%), 50d 67.21 (+1.8%), 200d 69.25 (-1.2%); 50d below 200d
Momentum: RSI(14) 46.8 | MACD 0.152 vs signal 0.673 (histogram -0.521)
Returns: 1d -0.4% | 5d -2.4% | 1m -2.7% | 3m +2.5%
52-week range: 60.43 - 81.60 (now 37.7% of the way up)
Volatility: ATR(14) 1.32 (1.9% of price) | annualised 20d 24.4%
Volume: 0.20x the 20-day average
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
Three-year record: +27.4% a year | beta to the market 1.02
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.82 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.5% above the current prices
Holdings read: AU, GFI.JO, NPN.JO, FSR.JO, SBK.JO
Recent rating changes among them:
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Software ETF is in an uptrend (50d>200d, +16.8% 3m) but momentum has rolled over with MACD below signal, price below the 20d SMA and light volume. The macro backdrop is the real constraint: the 10-year at 5.00% and 5-year +7bp on the week with a firmer dollar is a poor setup for a 34x P/E, 1.21-beta basket, and realized vol of 42% annualised is high. Analyst roll-up is supportive but covers only 43% of the fund and is 100% buy, which is baseline for megacap software rather than new information; a Bernstein downgrade of 9.7%-weight PANW offsets. News is single-name noise (CRM, CRWD targets) and does not move a basket. No policy or data surprise this cycle, so no side.

**Main reasons it gave:**
- 10-year at 5.00%, 5-year +7bp on week, dollar +1.23 — headwind for high-multiple software
- MACD histogram -0.33 and price 0.7% below 20d SMA despite 50d>200d uptrend
- Holdings P/E 34.2, P/S 9.07 with beta 1.21 and 42% annualised 20d vol
- Analyst roll-up 100% buy, +10.9% target, but only 43.2% coverage; PANW downgraded by Bernstein
- News flow is single-name (CRM, CRWD, PLTR) rather than macro or sector-wide

<details><summary><b>News</b> — score +0.05</summary>

- [AI Agents Fuel Cybersecurity Demand: 3 Stocks to Watch - CrowdStrike Holdings (NASDAQ:CRWD), Okta (NASDAQ](https://www.benzinga.com/markets/tech/26/09/61870329/ai-agents-cybersecurity-stocks-crowdstrike-okta-sailpoint)  
  <sub>Benzinga, 2 hours ago</sub>  
  AI agents are lifting cybersecurity demand and valuations. BofA raised targets on CrowdStrike, Okta and SailPoint but kept Neutral ratings.
- [BlackBerry Climbs 6%, Mobileye Rises 5%: Is the Software-Defined Vehicle Trade Waking Up?](https://247wallst.com/investing/2026/09/17/blackberry-climbs-6-mobileye-rises-5-is-the-software-defined-vehicle-trade-waking-up/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  BlackBerry and Mobileye are surging together while their closest hardware peer sits frozen, and that split tells you something important about who is...
- [Why Is Salesforce Stock Falling Thursday?](https://www.tradingview.com/news/benzinga:2cd0d43da094b:0-why-is-salesforce-stock-falling-thursday/)  
  <sub>TradingView, 24 hours ago</sub>  
  Salesforce Inc. www.benzinga.com/quote/CRM(NYSE:CRM) stock fell more than 3% Thursday after the software company raised its fiscal 2027 revenue outlook to...
- [Barlow’s Research Roundup: BMO analyst picks biggest winners from an expected energy investment boom](https://www.theglobeandmail.com/investing/markets/inside-the-market/article-barlows-research-roundup-bmo-analyst-picks-biggest-winners-from-an/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Daily roundup of research and analysis from The Globe and Mail's market strategist Scott Barlow.
- [Data infrastructure software — the control layer of the AI stack](https://themalaysianreserve.com/2026/09/18/data-infrastructure-software-the-control-layer-of-the-ai-stack/)  
  <sub>The Malaysian Reserve, 16 hours ago</sub>  
  DATA infrastructure has decoupled from enterprise software in the first half (1H26). While seat-based Software as a Service (SaaS) de-rated violently in the...
- [Agentforce Triggers Renewal Surge, Sparking Salesforce AI Boom: Analyst](https://www.benzinga.com/analyst-stock-ratings/analyst-color/26/09/61863232/agentforce-triggers-renewal-surge-sparking-salesforce-ai-boom-analyst)  
  <sub>Benzinga, 6 hours ago</sub>  
  BNP Paribas maintains a $265 price forecast on Salesforce as expanding Agentforce AI monetization and share repurchases support a Q3 revenue reacceleration.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 104.04 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 104.76 (-0.7%), 50d 100.00 (+4.0%), 200d 93.67 (+11.1%); 50d above 200d
Momentum: RSI(14) 51.5 | MACD 1.044 vs signal 1.375 (histogram -0.330)
Returns: 1d -1.6% | 5d +2.5% | 1m +1.2% | 3m +16.8%
52-week range: 74.67 - 117.79 (now 68.1% of the way up)
Volatility: ATR(14) 2.75 (2.6% of price) | annualised 20d 42.1%
Volume: 0.32x the 20-day average
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
Three-year record: +14.3% a year | beta to the market 1.21
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.9% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-15 UBS: main, Buy -> Buy
  - PANW: 2026-09-17 Bernstein: down, Outperform -> Market Perform
  - MSFT: 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - CRWD: 2026-09-18 Stephens & Co.: main, Overweight -> Overweight
  - CRM: 2026-09-18 Citizens: reit, Market Outperform -> Market Outperform
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

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> ITA is in a sharp downtrend: -13.7% in a month, below 20/50/200d SMAs, RSI 24.8 deeply oversold with MACD still negative. That is a broken trend but also a stretched one, and volume is light (0.71x), so there is no decisive break to trade either way. Macro is mildly hostile to a 34x P/E industrials basket: 10y at 5.00% and a dollar up 1.23 on the week, though no rate or data surprise this cycle. Analyst roll-up over 57.5% of the fund is 100% buy with +27% targets, a genuine offset. Defense geopolitics (Iran drone downings, Poland base comment) is the usual tailwind narrative, but the TipRanks item is promotional listicle-grade and the ETF has fallen anyway. No macro catalyst, conflicting evidence: stay flat.

**Main reasons it gave:**
- RSI(14) 24.8, price -13.7% in one month and below 20/50/200d SMAs
- MACD -7.09 below signal, histogram still negative
- Analyst roll-up over 57.5% of weight: 100% buy, +27% weighted target
- 10-year at 5.00% and DXY +1.23 on week against a 34.7x P/E industrials basket
- Volume only 0.71x 20-day average -- no decisive break

<details><summary><b>News</b> — score +0.15</summary>

- [Two U.S. unmanned aircraft recently destroyed by Iran - report (ITA:BATS)](https://seekingalpha.com/news/4643966-two-us-unmanned-aircraft-destroyed-by-iran---report)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Iran shot down two U.S. MQ-1 drones, raising tension in the Strait of Hormuz and potential $8M+ losses.
- [Trump’s Poland Base Comment: Potential Tailwind for Aerospace & Defense ETFs](https://www.tipranks.com/news/catalyst/trumps-poland-base-comment-potential-tailwind-for-aerospace-defense-etfs)  
  <sub>TipRanks, 22 hours ago</sub>  
  President Trump has posted a new announcement on Truth Social, the social media platform. He wrote: “GREAT NEWS! Thanks to the bold leadership of my friend,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 212.40 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 224.50 (-5.4%), 50d 235.26 (-9.7%), 200d 230.14 (-7.7%); 50d above 200d
Momentum: RSI(14) 24.8 | MACD -7.087 vs signal -6.100 (histogram -0.987)
Returns: 1d -0.7% | 5d -3.0% | 1m -13.7% | 3m -11.1%
52-week range: 198.23 - 253.22 (now 25.8% of the way up)
Volatility: ATR(14) 3.98 (1.9% of price) | annualised 20d 14.0%
Volume: 0.71x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Industrials
What it holds: P/E 34.66 | P/B 6.62 | P/S 3.21 | 3y earnings growth n/a
Yield: 0.5%
Three-year record: +26.1% a year | beta to the market 0.99
Cost and size: expense ratio 0.37% | net assets 13.63B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: GE Aerospace 21.6%, RTX Corp 17.2%, Boeing Co 9.1%, General Dynamics Corp 4.8%, Lockheed Martin Corp 4.7%
Sector mix: Industrials 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 57.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.76 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.0% above the current prices
Holdings read: GE, RTX, BA, GD, LMT
Recent rating changes among them:
  - GE: 2026-07-23 Bernstein: main, Outperform -> Outperform
  - RTX: 2026-08-03 Bernstein: main, Market Perform -> Market Perform
  - BA: 2026-08-11 Argus Research: up, Hold -> Buy
  - GD: 2026-09-08 UBS: main, Neutral -> Neutral
  - LMT: 2026-09-08 UBS: up, Neutral -> Buy
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

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Technicals are mildly negative: price below 20/50/200-day SMAs, 50d under 200d, MACD below signal, RSI 41, near the lower end of the 52-week range on thin volume. Trade-truce headlines and a possible Trump-Xi summit are mildly supportive but are anticipation, not a realised policy change. Valuation is cheap (P/E 11.9) and the analyst roll-up is uniformly buy with very large upside, though it covers only a third of the fund and such targets are chronically optimistic. Macro is a modest headwind: dollar up 1.2 on the week and 10-year at 5.00%, which pressures EM equity. No positioning or flow data available. Nothing here clears the bar for a directional macro call.

**Main reasons it gave:**
- Price 7.4% below 200d SMA with 50d below 200d and MACD histogram -0.171
- Only 15.3% up the 52-week range, volume 0.36x average
- Dollar index +1.23 on the week, 10-year yield 5.00% — headwind for EM equity
- Holdings P/E 11.90, P/B 1.39 with 2.0% yield
- Analyst roll-up 100% buy, +57.5% target, but covers just 32.2% of fund

<details><summary><b>News</b> — score +0.15</summary>

- [Trump-Xi Meeting in the Cards: ETFs Currently in Focus](https://www.tradingview.com/news/zacks:0220861ca094b:0-trump-xi-meeting-in-the-cards-etfs-currently-in-focus/)  
  <sub>TradingView, 3 hours ago</sub>  
  The United States and China are moving closer to extending their trade truce, with negotiations focusing on selective tariff cuts ahead of the scheduled...
- [US Stock Market This Week: Are SPY, QQQ Beating Asian Equities?](https://stocktwits.com/news-articles/markets/equity/us-stock-market-this-week-are-spy-qqq-beating-asian-equities/cZtuFPnRB3Q)  
  <sub>Stocktwits, 9 hours ago</sub>  
  The Nasdaq index in the U.S. is set to post weekly gains, while the Dow and S&P 500, along with Asian markets including China, Japan, Taiwan,...
- [U.S. likely to delay new tariffs until after Trump-Xi summit - report](https://seekingalpha.com/news/4644182-us-likely-to-delay-new-tariffs-until-after-trump-xi-summit)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  US seen holding off on new excess capacity tariffs until after Chinese President Xi Jinping's visit. Read more.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 53.01 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 54.06 (-1.9%), 50d 54.45 (-2.7%), 200d 57.26 (-7.4%); 50d below 200d
Momentum: RSI(14) 41.2 | MACD -0.571 vs signal -0.400 (histogram -0.171)
Returns: 1d +0.6% | 5d +0.1% | 1m -4.3% | 3m +0.5%
52-week range: 50.48 - 66.99 (now 15.3% of the way up)
Volatility: ATR(14) 0.58 (1.1% of price) | annualised 20d 12.8%
Volume: 0.36x the 20-day average
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
Three-year record: +8.5% a year | beta to the market 0.44
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +57.5% above the current prices
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

_Not available today._

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> SMH sits in a chop: above the 20d and 200d but flat against the 50d, RSI 51, 3-month return -14.5% while still 70% up the 52-week range, and volume at only 0.34x average gives no confirmation either way. The macro backdrop is the real constraint -- the Fed just hiked, the 10-year is at 5.00% and the 5-year rose 7bp on the week with a firmer dollar, which is a headwind for a 2.06-beta basket trading at 37.8x earnings. Analyst roll-up over 49% of the fund is uniformly Buy with a +42% weighted target, but sell-side targets on mega-cap chips are a slow-moving, chronically optimistic input, not a catalyst. News is mostly ETF-launch listicles and promotional 'semis remain Buys' pieces, which I discount as noise. No policy or data surprise beyond an already-digested hike, no decisive technical break -- no edge this cycle.

**Main reasons it gave:**
- Price flat vs 50d SMA (-0.1%) with RSI 51 and volume 0.34x average -- no trend confirmation
- 3-month return -14.5% despite still trading 15.7% above the 200d SMA
- Fed hiked; 10-year 5.00%, 5-year +7bp on the week, dollar +1.23 -- headwind for a 37.8x P/E, 2.06-beta basket
- Analyst roll-up over 49.2% of fund: 100% buy, +41.8% weighted target, several fresh Overweight initiations
- News flow dominated by new-ETF promos and 'ETFs to buy' listicles rather than macro substance

<details><summary><b>News</b> — score +0.05</summary>

- [Portfolio Fit: CCML](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-ccml/?tpid=1663756&tv=link&tc=in_content)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  Every AI server board and electric vehicle runs on a tiny ceramic component most investors have never heard of, and a brand-new ETF just made it possible to...
- [Rates Could Reach 4.5% On AI Spending, And Semiconductors Get Paid First (NASDAQ:SMH)](https://seekingalpha.com/article/4947893-rates-could-reach-4-5-percent-on-ai-spending-and-semiconductors-get-paid-first)  
  <sub>Seeking Alpha, 43 minutes ago</sub>  
  iShares Semiconductor ETF and VanEck Semiconductor ETF semiconductor funds remain Buys as AI-driven capex fuels demand. Click for more on SMH and SOXX.
- [New ETF CCML offers direct investment in key As...](https://pluang.com/en/news-feed/peluncuran-etf-ccml-komponen-elektronik-pasar-pasif)  
  <sub>Pluang, 3 hours ago</sub>  
  Roundhill launched the CCML ETF on September 9, 2026, focusing exclusively on multilayer ceramic capacitors (MLCCs) and related electronic components...
- [FTXL: A 120% Semiconductor Winner With A Very Different Playbook (NASDAQ:FTXL)](https://seekingalpha.com/article/4947832-ftxl-a-120-percent-semiconductor-winner-with-a-very-different-playbook)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Summary. First Trust Nasdaq Semiconductor ETF (FTXL) delivered a 119.6% one-year return, outperforming SOXX and SMH with a distinct, less Nvidia-heavy...
- [Portfolio Fit: KCHP](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-kchp/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Investors trying to isolate the Korean piece of the AI memory cycle have historically had to buy it inside a broad country fund, where semiconductors are...
- [BofA Sees Global Chip Market Nearly Doubling: Semiconductor ETFs to Buy](https://www.tradingview.com/news/zacks:7dc70852b094b:0-bofa-sees-global-chip-market-nearly-doubling-semiconductor-etfs-to-buy/)  
  <sub>TradingView, 3 hours ago</sub>  
  With safety concerns and calls for a slowdown in AI development gaining momentum, questions surrounding the broader AI infrastructure trade have increased.
- [These 5 Green Stocks Have Crushed Clean Energy ETFs, S&P 500 And AI Funds In 2026](https://www.tradingview.com/news/stocktwits:7529918a5094b:0-these-5-green-stocks-have-crushed-clean-energy-etfs-s-p-500-and-ai-funds-in-2026/)  
  <sub>TradingView, 10 hours ago</sub>  
  In 2026, energy stocks saw a steady climb amid the ongoing war in the Middle East, while the artificial intelligence trade has also gained momentum...
- [Portfolio Fit: AIFR](https://247wallst.com/investing/etf/2026/09/18/portfolio-fit-aifr/)  
  <sub>24/7 Wall St., 4 hours ago</sub>  
  Most semiconductor ETFs bury foundry exposure under layers of chip designers, equipment makers, and memory producers, which is exactly the problem a new...
- [S&P 500, Nasdaq, Dow End Higher As Drop In Oil Prices Allays Inflationary Concerns — NVDA, MCD, CRWV, LMT, AMZN In Focus](https://www.tradingview.com/news/stocktwits:6a6aef51d094b:0-s-p-500-nasdaq-dow-end-higher-as-drop-in-oil-prices-allays-inflationary-concerns-nvda-mcd-crwv-lmt-amzn-in-focus/)  
  <sub>TradingView, 18 hours ago</sub>  
  U.S. stock indices closed higher Thursday as falling oil prices and Treasury yields eased some inflation concerns a day after the Federal Reserve hiked...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.05</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 564.01 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 557.37 (+1.2%), 50d 564.60 (-0.1%), 200d 487.27 (+15.7%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD -3.246 vs signal -3.691 (histogram 0.445)
Returns: 1d +0.6% | 5d -0.8% | 1m +0.6% | 3m -14.5%
52-week range: 315.71 - 668.91 (now 70.3% of the way up)
Volatility: ATR(14) 15.50 (2.7% of price) | annualised 20d 33.3%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

```text
Fund type: Technology
What it holds: P/E 37.78 | P/B 11.07 | P/S 13.20 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +55.6% a year | beta to the market 2.06
Cost and size: expense ratio 0.35% | net assets 67.79B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: NVIDIA Corp 22.6%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.7%, Broadcom Inc 6.1%, Micron Technology Inc 5.5%, Advanced Micro Devices Inc 5.4%
Sector mix: Technology 100.0%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +41.8% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-18 RBC Capital: reit, Outperform -> Outperform
  - AMD: 2026-09-10 Piper Sandler: init, ? -> Overweight
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

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro or policy surprise for biotech this cycle: news items are irrelevant roundups or single-name stories (retail ETF, QCOM, cruise lines) and none bear on the basket. Technicals are mixed-to-soft — price below the 20d SMA, MACD negative, RSI 44.9, -7.9% over the month, but still +13.9% above a rising 200d and 50d above 200d, i.e. an uptrend in pullback on light volume (0.5x). Macro is a mild headwind: 10y at 5.00% with the belly up 7bp and a dollar up 1.23 on the week is unhelpful for long-duration, cash-burning small-cap biotech, though the curve is normally sloped and VIX is calm at 15.4. Analyst roll-up covers only 9% of the fund and shows a weighted target below current prices with a Moderna downgrade — a fact about that slice, not the fund. Nothing here clears the bar for a directional macro timing call.

**Main reasons it gave:**
- Price below 20d SMA and MACD histogram -1.12 after -7.9% month, but 50d above rising 200d
- 10-year at 5.00% and 5-year +7bp with DXY +1.23 — duration headwind for unprofitable biotech
- Analyst roll-up covers only 9% of fund; weighted target 13.2% below current prices, MRNA cut to Sell
- Pullback occurring on 0.50x average volume — no decisive break
- No biotech-relevant macro or policy catalyst in the 24h news set

<details><summary><b>News</b> — score +0.00</summary>

- [Is State Street SPDR S&P Retail ETF (XRT) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/state-street-spdr-p-retail-102003647.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Making its debut on 06/19/2006, smart beta exchange traded fund State Street SPDR S&P Retail ETF (XRT) provides investors broad exposure to the Consumer...
- [5 Undervalued Oncology Stocks Wall Street Is Overlooking (NASDAQ:IBB)](https://www.google.com/goto?url=CAESmQEB6zswFRZ76omUXKkN26tKE0572t8lIE8bbVA05eiiv5c4BA9_St7uAuV6zR7xE4t209lV9efFVpnDvsWCd6JW-KQGbtjAjo7KvHidTJGUtVw3-nuGIizMHX43oSPUk2h2gUxOthf311Z5cJU9P42v6DfyGGqNwt6rulLiquY7UdnZvZ0hzvBzVarUJME5xoxj8hMNSpbES80)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Oncology spending may hit $441B by 2029 as growth slows from generics. Click here to see five underappreciated cancer stocks with catalysts and upside.
- [Why Did OPEN, NKE, CCL Stocks Crash To 52-Week Lows Today?](https://stocktwits.com/news-articles/markets/equity/why-did-open-nke-ccl-stocks-crash-to-52-week-lows-today/cZtY2PcRB2d)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Housing weakness, a prolonged athleticwear turnaround, and rising cruise fuel costs weighed on investor sentiment.
- [QCOM Stock Climbs To 2-Month High As AI Data Center Push Gains Momentum](https://www.google.com/goto?url=CAESwAEB6zswFcKxNMEczl_xQzKTCXckLPX_YRNlyTGUyH_c8KzdYMMv0Im_XaoFsrSTS3ur8K-5rMd9JlhGA9AbyL3fTB4huNc4qSPq3dzeV0jqDFTgsmlJInKGVUNLLDK_2RxlXUwTQa_tlQrPCRQH6Z0ztsphlxXMdrcNSlSqd-YokHyDPKxAWe6nwjKgbefY3Vg7kEDhYQK3fXHPMJRuYJjHbZdybNAOiBnKKuhgOK30_QV6oA5Ee22nfCXKC2wXkHA)  
  <sub>Stocktwits, 22 hours ago</sub>  
  Qualcomm's diversification beyond smartphones is gaining traction as investors assess its potential role in hyperscaler AI infrastructure.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 156.20 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 161.60 (-3.3%), 50d 157.56 (-0.9%), 200d 137.11 (+13.9%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD -0.782 vs signal 0.341 (histogram -1.123)
Returns: 1d -1.3% | 5d +0.0% | 1m -7.9% | 3m +11.0%
52-week range: 95.60 - 169.55 (now 81.9% of the way up)
Volatility: ATR(14) 4.06 (2.6% of price) | annualised 20d 24.9%
Volume: 0.50x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Health
What it holds: P/E n/a | P/B 0.20 | P/S 0.12 | 3y earnings growth n/a
Yield: 0.3%
Three-year record: +26.2% a year | beta to the market 1.12
Cost and size: expense ratio 0.35% | net assets 11.40B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Moderna Inc 2.8%, Twist Bioscience Corp 1.9%, Apogee Therapeutics Inc 1.5%, Kymera Therapeutics Inc Ordinary Shares 1.4%, Halozyme Therapeutics Inc 1.4%
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

<details><summary><b>What analysts and big funds say</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.30</summary>

```text
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.18 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -13.2% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - TWST: 2026-09-18 BWS Financial: main, Sell -> Sell
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-14 B of A Securities: main, Buy -> Buy
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

_Not available today._

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> XLE sits near 52-week highs after a +19.9% three-month run, with 50d above 200d, but momentum is cooling (MACD histogram negative, RSI 56, volume 0.42x average) and the last week was slightly down. Macro is a mild headwind: 10-year at 5.00% and a dollar up 1.23 on the week pressure cyclicals, though the curve is normally sloped and VIX is contained. Fundamentals are unremarkable-to-fair (P/E 17.7, 2.4% yield, cheap 0.08% fee), and the analyst roll-up over 52% of the fund is all-buy but with only +2.7% upside, i.e. price already near targets. News is listicle/roundup noise with no policy or data surprise. No specific catalyst justifies a directional bet.

**Main reasons it gave:**
- Price 93.7% of 52-week range after +19.9% 3-month run
- MACD histogram -0.218 and volume 0.42x average signal fading momentum
- 10-year yield at 5.00% and dollar +1.23 on the week
- Analyst roll-up 100% buy but weighted target only +2.7% above price
- News limited to dividend listicle and generic forecast piece

<details><summary><b>News</b> — score +0.00</summary>

- [Ten energy stocks with the strongest dividend growth grades (XLE:NYSEARCA)](https://seekingalpha.com/news/4644254-ten-energy-stocks-with-the-strongest-dividend-growth-grades)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Top 10 energy dividend-growth stocks for 2026, ranked by Seeking Alpha grades, plus key sector drivers and ETF ideas—see which names lead now.
- [Copper, XLE and CAC 40 Forecasts: Rising Yields Shape Today’s Watch List](https://www.fxempire.com/forecasts/article/premium-copper-xle-and-cac-40-forecasts-rising-yields-shape-todays-watch-list-1630011)  
  <sub>FXEmpire, 3 hours ago</sub>  
  Copper and XLE remain bullish as the CAC 40 tests support, while rising U.S. Treasury yields and the 10-year's approach toward 5% keep markets on edge.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 64.46 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 64.11 (+0.5%), 50d 61.18 (+5.4%), 200d 55.73 (+15.7%); 50d above 200d
Momentum: RSI(14) 56.5 | MACD 1.031 vs signal 1.249 (histogram -0.218)
Returns: 1d -0.0% | 5d -1.0% | 1m +1.4% | 3m +19.9%
52-week range: 42.61 - 65.93 (now 93.7% of the way up)
Volatility: ATR(14) 1.28 (2.0% of price) | annualised 20d 19.4%
Volume: 0.42x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.74 | P/B 2.58 | P/S 1.68 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +15.3% a year | beta to the market -0.07
Cost and size: expense ratio 0.08% | net assets 41.44B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 19.9%, Chevron Corp 14.9%, ConocoPhillips 6.2%, Marathon Petroleum Corp 5.4%, Phillips 66 5.3%
Sector mix: Energy 100.0%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.04 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.7% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - CVX: 2026-09-03 BMO Capital: main, Outperform -> Outperform
  - COP: 2026-09-14 UBS: main, Buy -> Buy
  - MPC: 2026-09-14 Raymond James: main, Outperform -> Outperform
  - PSX: 2026-09-17 BMO Capital: main, Outperform -> Outperform
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

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> XLK sits in a mild uptrend (above 20/50/200d, 50d>200d) but momentum is flat — MACD histogram effectively zero, RSI 55, volume at half average, and 3-month return negative, i.e. a consolidation range rather than a break. The macro backdrop is the main constraint: 10-year at 5.00% and 5-year +7bp on the week with a firmer dollar is not supportive of a 33x P/E, 1.5-beta sector, and the Fed decision lands this week, which argues for waiting rather than positioning. Analyst roll-up is bullish (100% buy, +28% weighted target) but covers only 45.7% of the fund and is a slow-moving input. News is noise: promotional exchange releases and a valuation listicle; the Seeking Alpha and GuruFocus items make directional claims and were discounted. No positioning or flow data, so insider dimension left null.

**Main reasons it gave:**
- MACD histogram 0.000 with RSI 55.3 and volume 0.53x average — stalled momentum
- 10y 5.00%, 5y +7bp on week, dollar +1.23 — rate headwind for a 1.5-beta sector
- Holdings P/E 33.0, P/B 11.4 with no 3y earnings growth figure
- Analyst roll-up 100% buy, +28.3% weighted target, but only 45.7% coverage
- Fed decision pending this week; VIX 15.4 and 3-month return -1.9%

<details><summary><b>News</b> — score +0.00</summary>

- [Zoomex Highlights ETF Perpetuals Ahead of This Week’s Federal Reserve Decision](https://www.google.com/goto?url=CAESwgEB6zswFSNhFK9ABTPi4Ni-Fq1TxFe6EiKrPstT53azep7SHzp9zaHJLpUof_nnT1PRc4-m0QasxZ8B4oEqlP3xfsezFw_GvV_Yl1ADBh2STB6Y0o74v4TNYGmNW7uPSDoSJQOvWSd06JygDneMcq_xM1-L2mDO-sb2DvzrrVMXMvNeKBclijkeu08fVcj5cfOqbCVeoZVb3ZQ8h1QzCLouaSTMAERCg-ysdbTn2SaWQHaWqmL5dR2_NgLkCAr-FgTH5Q)  
  <sub>markets.businessinsider.com, 1 hour ago</sub>  
  VICTORIA, Seychelles,, Sept. 18, 2026 (GLOBE NEWSWIRE) -- With the U.S. Federal Reserve scheduled to announce its latest interest-rate decision ...
- [TTEQ: Technology Dashboard For September (NASDAQ:TTEQ)](https://www.google.com/goto?url=CAESiAEB6zswFaexs6Yksk0sjuxLb_-P0sLpoRjeKCJcREbgm5qHfxMeS81jP1aya5P9sBGImZitHVAjCGW4nUCTLQOt10ptYNwD2z1I7_jlilOKA-odr0ar9emHVvEVmPNFcgbGhK5By19nj_KFRh6i31WmsYX9_JyEYlrgtzgZRh3VX98zml76rKZm)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Summary. Software and IT services appear undervalued relative to 11-year averages, while other subsectors remain overvalued. T Rowe Price Technology ETF...
- [Leading And Lagging Sectors For September 18, 2026](https://www.google.com/goto?url=CAESngEB6zswFaV2dmqaU92CRS8Pbo1UClURidyVQGIH8b3PxpNU-5_pqN4LpLOdhE4bCfD4ctpUuOkkpuEwnl8y7-qYUi31doa9W-3PDXuRTCUrfPfGe3EzJoIK6fAgSvZO-YN7zrpA9qwgYrMdAQMWWkxitQjJqBzvMocJsz1IHfQcvZxhcRDGF1D1Un3jh7H_mxySQYLDeg4JNw48O4TABQ)  
  <sub>Benzinga, 3 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLC) State Street Communication Services Select Sector SPDR ETF 112.6400 0.290 0.25 1.0K...
- [Zoomex Highlights Key ETF Market Trends Ahead of This Week’s Federal Reserve Decision](https://www.google.com/goto?url=CAESswEB6zswFVHRoDeEuEccJH1-CyiVus0MdPM4p4XaTe4X590geX70vJaCq8GAWUuJ3a-ZRQNSBYwf2Ba35wF0GV-qEFMsxxRH_9pLl2HTWXKGHRsF_EoyqFZSbU8CSTEW7R14d-mFX2ukmTU7oPBM4cQd6_SThyNDwAs-Srk-1u2F-cpw0CR043DJHjy5sIpkIRU9syRW8Q3g9Y5X0sORmu1eGLw9yLyZVU-daO_NCtXjajQ9LQ)  
  <sub>Brave New Coin, 16 hours ago</sub>  
  Zoomex brings the week's biggest ETF stories onto a single, rule-based derivatives venue, giving traders easy-to-use exposure to SPY, QQQ, IWM, XLF, XLK,...
- [XLK hovers above the level that matters most (XLK:NYSEARCA)](https://seekingalpha.com/news/4644191-xlk-hovers-above-the-level-that-matters-most)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  XLK nears key $182 support where anchored VWAPs converge—an important test for the tech ETF's consolidation range.
- [XLK Looks 35.3% Overvalued on GF Value™ as of September 18, 2026](https://www.google.com/goto?url=CAESmwEB6zswFZY3nsDHKoxzvtuS9Se8eRe1TCSdZIkpTav8hQeNwV8HHE7FzfKW36GWMSNFkfdv9zXeODHzj62n0o4umxeBRTEZ1RAAMpxb1nA5EJQ_-hork03Y5c_wz0n-8fWCvrbJa-RmNK5IuYfLPHbFXcM_6IYt43Rgm6G15WQDfULYk4TE_-FsmCC7_qPdSKkVuEO5M6QZ1uRmjw)  
  <sub>GuruFocus, 4 hours ago</sub>  
  On September 18, 2026, the Technology Select Sector SPDR ETF (ticker: XLK) established new pivot points using the DeMark analysis method, setting a pivot...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 187.85 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 185.29 (+1.4%), 50d 183.08 (+2.6%), 200d 162.43 (+15.6%); 50d above 200d
Momentum: RSI(14) 55.3 | MACD 0.736 vs signal 0.735 (histogram 0.000)
Returns: 1d -0.1% | 5d +0.1% | 1m +2.3% | 3m -1.9%
52-week range: 127.50 - 198.21 (now 85.3% of the way up)
Volatility: ATR(14) 3.39 (1.8% of price) | annualised 20d 21.0%
Volume: 0.53x the 20-day average
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
Three-year record: +30.5% a year | beta to the market 1.50
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.56 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +28.3% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - AAPL: 2026-09-18 Evercore ISI Group: main, Outperform -> Outperform
  - MSFT: 2026-09-15 Citizens: reit, Market Outperform -> Market Outperform
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-18 RBC Capital: reit, Outperform -> Outperform
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

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Staples are in a mild downtrend: price below 20d and 50d SMAs, RSI 41, MACD negative, -4% on the month, on light volume. Macro is a headwind for a bond-proxy defensive sector -- 10y at 5.00% and rising, dollar up 1.23, VIX low at 15 with cyclicals rotating (autos rallying), all of which favours risk-on over defensives. Offsetting that, valuation is not extreme relative to quality, analyst roll-up on 39.6% of the fund is 100% buy with +13.6% implied upside, and the fund sits just below its 200d with 50d still above 200d. No policy or data surprise specific to staples; this is a drift, not a break. NEUTRAL with a slight bearish tilt. Note the Seeking Alpha 'I'm taking a tactical position in staples' piece is a promotional opinion and carries no weight.

**Main reasons it gave:**
- Price -1.9% vs 20d and -2.1% vs 50d SMA, RSI 40.8, MACD histogram -0.169
- 10-year yield 5.00% (+0.03 wk), 5y +0.07 -- headwind for bond-proxy defensives
- Dollar index +1.23 on the week, VIX 15.4 and falling: risk-on backdrop favours cyclicals over staples
- Analyst roll-up on 39.6% of fund: 100% buy weight, +13.6% weighted target upside
- Volume 0.51x 20-day average -- no conviction behind the drift lower

<details><summary><b>News</b> — score -0.05</summary>

- [Ten consumer staples stocks with the strongest dividend growth grades (XLP:NYSEARCA)](https://seekingalpha.com/news/4644409-ten-consumer-staples-stocks-with-the-strongest-dividend-growth-grades)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Top 10 consumer staples stocks ranked by Dividend Growth Grade (A+ to A), plus key sector ETFs—find defensive, income-focused ideas; read now.
- [Is State Street SPDR S&P Retail ETF (XRT) a Strong ETF Right Now?](https://finance.yahoo.com/markets/stocks/articles/state-street-spdr-p-retail-102003647.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  Making its debut on 06/19/2006, smart beta exchange traded fund State Street SPDR S&P Retail ETF (XRT) provides investors broad exposure to the Consumer...
- [Webcast: Active ETFs are capturing investor attention - here’s why | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/14/active-etfs-are-capturing-investor-attention-heres-why?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 5 minutes ago</sub>  
  What's driving the rapid growth of active ETFs, and what could it mean for client portfolios? Join Fidelity Investments to explore the forces behind the...
- [Leading And Lagging Sectors For September 18, 2026](https://www.benzinga.com/etfs/sector-etfs/26/09/61867052/leading-and-lagging-sectors-september-18-2026)  
  <sub>Benzinga, 4 hours ago</sub>  
  Gainers Symbol Name Price Change ($) Change (%) Volume (NYSE:XLC) State Street Communication Services Select Sector SPDR ETF 112.6400 0.290 0.25 1.0K...
- [The Consumer Is Back, I'm Taking A Tactical Position In Staples](https://seekingalpha.com/article/4947728-consumer-back-i-taking-tactical-position-staples)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Summary. The Vibecession is ending on the data. Retail sales just posted their biggest gain since the U.S.-Iran war, and I'm taking a tactical position in...
- [Healthcare equipment sector undervalued; global...](https://pluang.com/en/news-feed/dashboard-sektor-kesehatan-ixj-september)  
  <sub>Pluang, 23 hours ago</sub>  
  The healthcare equipment subsector is currently undervalued compared to its historical averages, while other healthcare subsectors appear slightly...
- [Automaker Stocks Rally as Rotation Lifts Cyclicals: General Motors Climbs 4%, Stellantis Rises 4%, Ford Gains 3%, Tesla Adds 2%](https://247wallst.com/investing/2026/09/17/automaker-stocks-rally-as-rotation-lifts-cyclicals-general-motors-climbs-4-stellantis-rises-4-ford-gains-3-tesla-adds-2/)  
  <sub>24/7 Wall St., 24 hours ago</sub>  
  Four automakers with nothing in common are surging in lockstep Thursday morning, and the reason behind that unusual uniformity tells investors something...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.05</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 83.11 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 84.70 (-1.9%), 50d 84.92 (-2.1%), 200d 83.58 (-0.6%); 50d above 200d
Momentum: RSI(14) 40.8 | MACD -0.538 vs signal -0.369 (histogram -0.169)
Returns: 1d -0.5% | 5d -0.3% | 1m -4.0% | 3m -0.2%
52-week range: 75.60 - 90.01 (now 52.1% of the way up)
Volatility: ATR(14) 0.98 (1.2% of price) | annualised 20d 12.8%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.05</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 25.14 | P/B 4.58 | P/S 1.36 | 3y earnings growth n/a
Yield: 2.6%
Three-year record: +7.9% a year | beta to the market 0.49
Cost and size: expense ratio 0.08% | net assets 14.52B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 9.8%, Costco Wholesale Corp 8.9%, Coca-Cola Co 7.3%, Procter & Gamble Co 7.2%, Philip Morris International Inc 6.2%
Sector mix: Consumer defensive 98.2%, Consumer cyclical 1.8%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.6% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-10 DA Davidson: main, Buy -> Buy
  - COST: 2026-09-16 Oppenheimer: reit, Outperform -> Outperform
  - KO: 2026-07-30 Argus Research: main, Buy -> Buy
  - PG: 2026-08-07 Argus Research: down, Buy -> Hold
  - PM: 2026-07-30 Citigroup: main, Buy -> Buy
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

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro or policy surprise this cycle. Yields drifted slightly higher, dollar firmer, VIX flat and low — nothing decisive. XLV is still above its 50d and 200d with a golden cross and +12.5% over three months, but has given back 4.3% in a month, MACD is below signal and RSI is mid-range on light volume: a consolidation, not a break. Analyst roll-up over 44% of the fund is uniformly buy with ~11% upside, which is a mild positive but is standard sell-side posture. Holdings P/E ~30 is not cheap for the sector. News is a listicle and a valuation opinion piece — noise. No positioning or flow data available, so insider dimension is left null.

**Main reasons it gave:**
- Price above 50d (+0.8%) and 200d (+7.8%) with 50d above 200d, but below 20d and -4.3% on the month
- MACD -0.023 vs signal 0.528, RSI 48.8, volume 0.77x average — momentum stalling
- Analyst roll-up over 44.3% of fund: 100% buy, +11.4% weighted target upside
- Macro quiet: 10y +3bp, VIX 15.4 (-0.4), curve normal at +1.02 — no policy or data surprise
- Holdings P/E 30.5 and 1.5% yield leave little valuation cushion

<details><summary><b>News</b> — score +0.00</summary>

- [Healthcare equipment sector undervalued; global...](https://pluang.com/en/news-feed/dashboard-sektor-kesehatan-ixj-september)  
  <sub>Pluang, 23 hours ago</sub>  
  The healthcare equipment subsector is currently undervalued compared to its historical averages, while other healthcare subsectors appear slightly...
- [10 small-cap U.S. healthcare stocks with the weakest momentum grades](https://seekingalpha.com/news/4643697-10-small-cap-u-s-healthcare-stocks-with-the-weakest-momentum-grades)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Small-cap U.S. healthcare stocks have experienced severe downward pressure year to date, with several names carrying Seeking Alpha's lowest Momentum Grades...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 168.05 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 170.28 (-1.3%), 50d 166.75 (+0.8%), 200d 155.92 (+7.8%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD -0.023 vs signal 0.528 (histogram -0.551)
Returns: 1d -0.5% | 5d +1.6% | 1m -4.3% | 3m +12.5%
52-week range: 134.13 - 175.68 (now 81.6% of the way up)
Volatility: ATR(14) 2.29 (1.4% of price) | annualised 20d 14.4%
Volume: 0.77x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Health
What it holds: P/E 30.47 | P/B 4.77 | P/S 1.66 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +10.1% a year | beta to the market 0.52
Cost and size: expense ratio 0.08% | net assets 43.91B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Eli Lilly and Co 14.9%, Johnson & Johnson 10.4%, AbbVie Inc 7.4%, Merck & Co Inc 5.9%, UnitedHealth Group Inc 5.7%
Sector mix: Healthcare 100.0%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.4% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-18 Guggenheim: main, Buy -> Buy
  - JNJ: 2026-09-10 HSBC: main, Buy -> Buy
  - ABBV: 2026-09-10 HSBC: main, Buy -> Buy
  - MRK: 2026-09-10 HSBC: main, Buy -> Buy
  - UNH: 2026-07-21 JP Morgan: main, Overweight -> Overweight
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

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> CANE is a sugar futures fund trading near the 72nd percentile of its 52-week range with a positive trend structure (50d above 200d, up 11.6% from the 200d). Momentum is deteriorating—RSI sits at 46.8 with a negative MACD histogram—and volume is weak at 0.31x the 20-day average. The fund has rallied 18.1% over three months, but large speculators hold a crowded net long at the 100th percentile of the past year's positioning distribution, typically a crowding signal that often precedes mean reversion. The macro backdrop shows rising short-term Treasury yields (+7bp on 3-month and 5-year) with a steepening curve and a stronger dollar (+1.23 on the week), both headwinds for commodity prices. Most critically, this fund's cost of holding is severe: -11.8% annually from rolling contracts, meaning it has lagged the underlying commodity by 16.4% over three months. That structural drag is history, not a forecast, but it raises the hurdle for a bullish case. No fresh news or catalyst has emerged to sustain the recent rally. The technical deterioration, crowded positioning at an extreme, macro headwinds, and persistent roll costs balance the still-positive trend, yielding a modest lean to neutral rather than a clean sell.

**Main reasons it gave:**
- CFTC positioning at 100th percentile crowding—extreme long after 3-month rally
- Cost of holding -11.8% annually; fund underperformed commodity 16.4% in 3 months
- Momentum deteriorating: RSI 46.8, MACD histogram negative, volume 0.31x average
- Dollar +1.23 on week and short yields rising—macro headwinds for commodities
- Price at 72nd percentile of 52-week range after significant 3-month advance

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 11.04 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 11.38 (-3.0%), 50d 10.63 (+3.8%), 200d 9.90 (+11.6%); 50d above 200d
Momentum: RSI(14) 46.8 | MACD 0.160 vs signal 0.262 (histogram -0.102)
Returns: 1d -0.4% | 5d -4.2% | 1m -1.8% | 3m +18.1%
52-week range: 9.02 - 11.82 (now 72.1% of the way up)
Volatility: ATR(14) 0.22 (1.9% of price) | annualised 20d 24.1%
Volume: 0.31x the 20-day average
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
Cost of holding this fund instead of sugar itself: -11.8% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +18.1%, commodity +34.4%, gap -16.4% | 6 months: fund +7.2%, commodity +18.9%, gap -11.7% | 12 months: fund +5.7%, commodity +17.6%, gap -11.8%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 18.7% of open interest (1,276,579 contracts)
Change on the week: +0.4% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

_Not available today._

</details>

### Corn (CORN) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> Corn shows mixed signals across dimensions. Technically, the contract sits near 52-week highs (84.8th percentile) with momentum deteriorating -- RSI at 56 is neutral, MACD histogram negative, and volume tracking below average despite a 16% three-month rally. The trend remains positive (price above 50d and 200d SMAs) but the recent bar closed down 0.6% on thin participation. Positioning data (from Sept 8, now stale) shows speculators at the 100th percentile crowded long, a setup that historically marks exhaustion as often as continuation. The macro backdrop is mixed: the dollar strengthened +1.23 this week, which headwinds agricultural exports, while rates moved modestly higher across the curve. The news mention of Iran war and energy shocks is not directly relevant to corn demand or supply. The critical bearish fact is the cost of holding: this fund has structurally lost 13.1% annually due to contango roll losses, with a 9.8% gap over the past 3 months alone. That cost is not a direction signal but it is a material friction that tempers conviction on longs and favors shorts. No crop condition data is present (out of season), and no supply or demand shock has materialized. The recent 5% monthly gain has extended into a crowded positioning, leaving limited room for upside without a concrete supply disruption or demand catalyst, neither of which the data supports.

**Main reasons it gave:**
- Large speculators at 100th percentile crowding into long position as of week of Sept 8
- Fund structure carrying -13.1% annual roll cost versus the commodity itself
- Dollar index +1.23 on week headwinds agricultural export demand
- Recent momentum deteriorating despite three-month 16% gain: RSI neutral, MACD negative histogram, volume below average

<details><summary><b>News</b> — score +0.00</summary>

- [Charlie Bilello Warns of $100 Billion Iran War Fuel Shock as $4.43 Gas Prices Show the ‘Inflation Problem’ Isn’t Over](https://www.tradingview.com/news/benzinga:90c82aa05094b:0-charlie-bilello-warns-of-100-billion-iran-war-fuel-shock-as-4-43-gas-prices-show-the-inflation-problem-isn-t-over/)  
  <sub>TradingView, 7 hours ago</sub>  
  U.S. gas prices hit a record $4.43 per gallon for September, driven by the ongoing war in Iran. Market strategist Charlie Bilello warns that this energy...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.15</summary>

```text
Last close 19.71 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 19.89 (-0.9%), 50d 18.72 (+5.3%), 200d 18.05 (+9.2%); 50d above 200d
Momentum: RSI(14) 56.1 | MACD 0.352 vs signal 0.453 (histogram -0.101)
Returns: 1d -0.6% | 5d -1.1% | 1m +5.1% | 3m +16.3%
52-week range: 16.47 - 20.29 (now 84.8% of the way up)
Volatility: ATR(14) 0.30 (1.5% of price) | annualised 20d 14.9%
Volume: 0.58x the 20-day average
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
Cost of holding this fund instead of corn itself: -13.1% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.3%, commodity +26.1%, gap -9.8% | 6 months: fund +4.7%, commodity +12.1%, gap -7.4% | 12 months: fund +10.2%, commodity +23.4%, gap -13.1%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.45</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 23.0% of open interest (1,803,323 contracts)
Change on the week: +0.3% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.45</summary>

_Not available today._

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> CPER shows modest technical strength with price 8.1% above its 200-day SMA and trending above both 20d and 50d moving averages. Momentum remains mildly positive (RSI 54.2, MACD histogram negative but near signal line). However, several headwinds temper conviction: (1) Large speculators hold copper futures at the 90th percentile of positioning over 52 weeks, a crowded long that historically marks as often an end to moves as a continuation; (2) The cost of holding CPER versus physical copper is heavy at -5.3% annually due to contango roll losses; (3) Volume is well below average at 0.34x the 20-day norm, suggesting weak conviction behind the move; (4) Macro backdrop shows a strong dollar (up 1.23 this week to 100.35) which headwinds copper demand as a dollar-denominated commodity; (5) Treasury yields have moved up across the short and intermediate curve, which tightens financial conditions. The price is at the 92.6% level of its 52-week range, leaving limited room to extend higher. These offsetting factors—modest technical strength against crowded positioning, elevated carry costs, weak volume, and a strengthening dollar—do not support a directional conviction call.

**Main reasons it gave:**
- Crowded long at 90th percentile of positioning over past year
- Heavy cost of holding at -5.3% annually due to contango rolls
- Strong dollar up 1.23 on the week headwinds copper demand
- Volume 0.34x 20-day average signals weak conviction
- Price at 92.6% of 52-week range with limited upside room

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 40.10 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 39.71 (+1.0%), 50d 39.42 (+1.7%), 200d 37.08 (+8.1%); 50d above 200d
Momentum: RSI(14) 54.2 | MACD -0.060 vs signal -0.009 (histogram -0.051)
Returns: 1d +1.1% | 5d +2.4% | 1m +1.8% | 3m +3.2%
52-week range: 28.34 - 41.05 (now 92.6% of the way up)
Volatility: ATR(14) 0.73 (1.8% of price) | annualised 20d 28.4%
Volume: 0.34x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

```text
Cost of holding this fund instead of copper itself: -5.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +3.2%, commodity +5.0%, gap -1.8% | 6 months: fund +18.9%, commodity +23.2%, gap -4.2% | 12 months: fund +41.1%, commodity +46.4%, gap -5.3%
A commodity fund holds futures, not copper, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

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
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 27.6% of open interest (297,491 contracts)
Change on the week: +1.8% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

_Not available today._

</details>

### Gold (GLD) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> Gold is trading with conflicting signals. On the macro side, yields have ticked higher this week across the curve (particularly 3m, 5y at +7bp), which typically pressures gold as the opportunity cost of holding non-yielding assets increases; the dollar has also strengthened sharply (+1.23 on the week to 100.35), a headwind for commodities priced in USD. Technically, the picture is mixed: the fund is below its 20d and 200d moving averages, MACD is deeply negative with a large histogram, and it has fallen 3.5% from the 200d level, suggesting weakness. However, recent price action shows resilience—up 0.9% on the day and 3.8% over three months—and RSI at 51 is neutral rather than oversold. Volume is light at 0.45x average, limiting conviction in the move. Positioning shows large speculators at 85th percentile crowding (net long 32.8% of open interest) with minimal weekly change, neither a strong bullish nor bearish signal. The fund's cost of holding is negligible at 0.4% annually. The news flow is dominated by commentary comparing bitcoin ETF hedging dynamics to gold—a thematic piece about capital rotation between asset classes rather than a gold-specific fundamental catalyst. Yield rises, dollar strength, and technical weakness argue for caution, but the absence of a decisive break and the presence of some upside momentum prevent a bearish conviction. The macro backdrop does not yet support a confident directional move.

**Main reasons it gave:**
- Treasury yields up 3-7bp across the curve this week, raising opportunity cost of holding non-yielding gold
- Dollar index +1.23 on the week to 100.35, a headwind for USD-priced commodities
- Price below both 20d and 200d SMAs with MACD deeply negative and large histogram
- CFTC positioning at 85th percentile crowding with no directional change, neither bullish nor bearish signal
- News flow is thematic commentary on bitcoin vs gold rather than gold-specific fundamental catalyst

<details><summary><b>News</b> — score -0.20</summary>

- [JPMorgan says bitcoin could get more support than gold if ETF hedging eases](https://www.theblock.co/news/markets/2026-09-17-jpmorgan-bitcoin-gold-415421)  
  <sub>The Block, 23 hours ago</sub>  
  Bitcoin could get more support than gold if investors reduce their ETF hedges, according to JPMorgan analysts. Bitcoin and gold ETFs saw inflows after the...
- [Bitcoin Could Get More Support Than Gold as ETF Hedging Eases: JPMorgan](https://cryptorank.io/news/feed/8eb14-bitcoin-could-get-more-support-than-gold-as-etf-hedging-eases-jpmorgan)  
  <sub>CryptoRank, 11 hours ago</sub>  
  JPMorgan analysts led by Nikolaos Panigirtzoglou say Bitcoin could draw more price support than gold if hedging demand in the ETF market eases, noting short...
- [Bloomberg's ETF Analyst Says Bitcoin Funds Will Triple Gold Hours After Admitting They Burned Cash](https://247wallst.com/investing/etf/2026/09/17/bloombergs-etf-analyst-says-bitcoin-funds-will-triple-gold-hours-after-admitting-they-burned-cash/)  
  <sub>24/7 Wall St., 20 hours ago</sub>  
  Bloomberg's top ETF analyst made two posts ninety minutes apart that told very different stories about Bitcoin funds, and the price charts make one of those...
- [Bitcoin to Outperform Gold if ETF Hedging Eases, JPMorgan Says](https://www.tradingview.com/news/u_today:d05735a4b094b:0-bitcoin-to-outperform-gold-if-etf-hedging-eases-jpmorgan-says/)  
  <sub>TradingView, 20 hours ago</sub>  
  Bitcoin may have more room to gain ground against gold if investors start unwinding some of the defensive positions surrounding cryptocurrency...
- [JPMorgan says Bitcoin could get more support than gold as ETF hedges unwind](https://investinglive.com/cryptocurrency/jpmorgan-says-bitcoin-could-get-more-support-than-gold-as-etf-hedges-unwind/)  
  <sub>investingLive, 18 hours ago</sub>  
  JPMorgan says Bitcoin could gain more support than gold if investors unwind the short positions and options currently hedging their Bitcoin ETF holdings, a…
- [Gold futures turn higher as yields and oil prices decline (GLD:NYSEARCA)](https://seekingalpha.com/news/4644124-gold-futures-turn-higher-as-yields-and-oil-prices-decline)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Gold futures posted modest gains, helped by lower crude oil prices and a pullback in Treasury yields after the Federal Reserve delivered its first rate hike...
- [Bitcoin ETF Demand Insights From JPMorgan's Report](https://en.cryptonomist.ch/2026/09/18/bitcoin-etf-demand-jpmorgan/)  
  <sub>The Cryptonomist, 11 hours ago</sub>  
  Bitcoin ETF demand may outpace gold as hedging eases, says JPMorgan, highlighting market positioning and institutional trends in ETFs.
- [JPMorgan Says Bitcoin Could Beat Gold Once ETF Hedging Pressure Eases](https://startupfortune.com/jpmorgan-says-bitcoin-could-beat-gold-once-etf-hedging-pressure-eases/)  
  <sub>Startup Fortune, 22 hours ago</sub>  
  JPMorgan says bitcoin could outpace gold in the debasement trade once ETF hedging eases, citing higher put-to-call ratios and short interest on IBIT vs.
- [JPMorgan Says Unwinding Bitcoin ETF Hedges Could Give It an Edge Over Gold](https://finance.biggo.com/news/c1b9ef1d-ab91-46fa-b8c7-75b5f9773f19)  
  <sub>BigGo Finance, 17 hours ago</sub>  
  JPMorgan analysts led by Nikolaos Panigirtzoglou say Bitcoin could gain more support than gold if investors reduce hedging positions in spot Bitcoin ETFs.
- [JPMorgan Argues That Bitcoin Could Outperform Gold Under One Condition](https://www.bitget.com/amp/news/detail/12560605844060)  
  <sub>Bitget, 22 hours ago</sub>  
  JPMorgan analysts believe that if the high hedge positions in Bitcoin ETFs are resolved, Bitcoin could find stronger support than gold in the coming...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.35</summary>

```text
Last close 401.76 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 406.65 (-1.2%), 50d 392.99 (+2.2%), 200d 416.22 (-3.5%); 50d below 200d
Momentum: RSI(14) 51.1 | MACD -0.653 vs signal 1.135 (histogram -1.788)
Returns: 1d +0.9% | 5d +0.7% | 1m -2.9% | 3m +3.8%
52-week range: 335.62 - 495.90 (now 41.3% of the way up)
Volatility: ATR(14) 7.66 (1.9% of price) | annualised 20d 24.5%
Volume: 0.45x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.15</summary>

```text
Cost of holding this fund instead of gold itself: 0.4% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +3.8%, commodity +4.0%, gap -0.2% | 6 months: fund -5.8%, commodity -4.1%, gap -1.7% | 12 months: fund +19.2%, commodity +18.8%, gap +0.4%
A commodity fund holds futures, not gold, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.15</summary>

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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 32.8% of open interest (411,227 contracts)
Change on the week: -0.1% of open interest
Crowding: 85% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Silver (SLV) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> SLV has posted a modest 2% gain on the day and 3.5% over five days, riding a broader precious metals rally as oil declines and the Fed picture steadies. However, the macro and technical backdrop offer little conviction for a directional call. Treasury yields have ticked up across the curve this week, including the 3-month and 5-year, which historically headwind precious metals by raising the opportunity cost of non-yielding assets. The dollar has strengthened +1.23% on the week to 100.35, another headwind for dollar-denominated commodities. Technologically, SLV is still 8.6% below its 200-day moving average, with momentum already rolling over (RSI 54.7, MACD histogram negative at -0.231) despite the recent bounce. The 50-day SMA remains below the 200-day, confirming a downtrend on longer timeframes. CFTC positioning shows large speculators at 13.9% net long, up 1.9% on the week but only at the 73rd percentile, suggesting crowding within its normal range rather than an extreme. The fund's carry cost of -1.7% annually is a structural drag. The news flow is almost entirely about mining stock inclusions (Sunshine Silver in GDXJ) and relative strength in silver ETFs on a day of broad metal gains, not a material macro catalyst. A one-day bounce does not override the week's rates and dollar backdrop.

**Main reasons it gave:**
- Dollar strength +1.23% on the week headwinds precious metals
- Treasury yields up across 3m and 5y, raising opportunity cost
- Price still 8.6% below 200-day MA in downtrend structure
- MACD histogram negative at -0.231 despite one-day bounce
- Large speculator positioning at 73rd percentile, within normal range

<details><summary><b>News</b> — score +0.15</summary>

- [Sunshine Silver Mining & Refining Announces Inclusion in the VanEck Junior Gold Miners ETF](https://www.prnewswire.com/news-releases/sunshine-silver-mining--refining-announces-inclusion-in-the-vaneck-junior-gold-miners-etf-302883164.html)  
  <sub>PR Newswire, 6 hours ago</sub>  
  KELLOGG, Idaho, Sept. 18, 2026 /PRNewswire/ -- Sunshine Silver Mining & Refining Company (the "Company" or "Sunshine") (NYSE:SSMR), a mining company...
- [Sunshine Silver added to VanEck Junior Gold Miners ETF after June IPO](https://www.tradingview.com/news/tradingview:280189d8c2956:0-sunshine-silver-added-to-vaneck-junior-gold-miners-etf-after-june-ipo/)  
  <sub>TradingView, 6 hours ago</sub>  
  Sunshine Silver announced inclusion in the VanEck Junior Gold Miners ETF, marking broader market visibility after its June IPO.Key Highlights:Original SEC...
- [Schroders launches two active ETFs focused on equity of Europe and Japan](https://rankiapro.com/en/news/schroders-launches-two-active-etfs-focused-on-equity-of-europe-and-japan/)  
  <sub>RankiaPro, 7 hours ago</sub>  
  Schroders expands its active ETF platform with new Europe and Japan equity strategies, as AUM tops $3.7 billion in under a year.
- [Three months after its debut, Sunshine Silver is set to join a gold-and-silver mining fund.](https://www.stocktitan.net/news/SSMR/sunshine-silver-mining-refining-announces-inclusion-in-the-van-eck-epq4wqorhnwc.html)  
  <sub>Stock Titan, 6 hours ago</sub>  
  Sunshine Silver Mining & Refining (SSMR) will be added to the VanEck Junior Gold Miners ETF (GDXJ) effective at market close on September 18, 2026.
- [Australian ETF Movers for Friday | Global X Silver Miners ETF Was the Top Gainer](https://www.moomoo.com/news/post/76440508/australian-etf-movers-for-friday-global-x-silver-miners-etf)  
  <sub>Moomoo, 10 hours ago</sub>  
  TopGainers/Losers with the total trading value of A$572.16 million. Among them: $Global X Silver Miners ETF(SLVM.AU)$ was the top gainer, climbing 6.03% to...
- [Sunshine Silver Mining joins VanEck Junior Gold Miners ETF, boosting visibility after recent IPO.](https://pluang.com/en/news-feed/sunshine-silver-mining-termasuk-dalam-vaneck-junior-gold-miners-etf)  
  <sub>Pluang, 6 hours ago</sub>  
  Sunshine Silver Mining & Refining Company announced its common stock will be added to the VanEck Junior Gold Miners ETF (GDXJ) as of September 18, 2026.
- [Gold vs Silver: Which Is Better to Trade and Invest In? (2026)](https://www.dailyforex.com/forex-articles/gold-silver-trading-and-investing/249841)  
  <sub>DailyForex, 8 hours ago</sub>  
  Gold vs Silver: compare volatility, the Gold-Silver ratio, costs and risk to decide which metal offers better trading and investment opportunities in 2026.
- [GOF's Selloff Offers A Valuation Lesson With A Potential Silver Lining (NYSE:GOF)](https://seekingalpha.com/article/4947732-gofs-selloff-offers-a-valuation-lesson-with-a-potential-silver-lining)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Guggenheim Strategic Opportunities Fund now trades at a rare near double-digit discount, a level not seen since 2016. Learn why GOF CEF is a hold.
- [Shining bright! Gold, silver ETFs rise 2-3% as oil fall eclipses Fed hike](https://www.business-standard.com/markets/news/shining-bright-gold-silver-etfs-rise-2-3-as-oil-fall-outshines-fed-hike-126091800437_1.html)  
  <sub>Business Standard, 10 hours ago</sub>  
  Gold and silver exchange-traded funds (ETFs) gained up to 3 per cent in intraday deals on Friday, in line with the rise seen in the precious metals as...
- [UTI Silver ETF FoF Direct Growth Review 2026: NAV, Returns, Portfolio & Should You Invest?](https://univest.in/blogs/uti-silver-etf-fof-direct-growth-review-2026)  
  <sub>Univest, 9 hours ago</sub>  
  UTI Silver ETF FoF Direct Growth Plan NAV is ₹28.9382 as of 17 Sep 2026. 1Y return: 73.31%, 3Y return: 45.21%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.15</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 60.17 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 59.77 (+0.7%), 50d 56.82 (+5.9%), 200d 65.80 (-8.6%); 50d below 200d
Momentum: RSI(14) 54.7 | MACD 0.108 vs signal 0.339 (histogram -0.231)
Returns: 1d +2.0% | 5d +3.5% | 1m +0.3% | 3m +1.1%
52-week range: 37.99 - 105.60 (now 32.8% of the way up)
Volatility: ATR(14) 1.86 (3.1% of price) | annualised 20d 38.3%
Volume: 0.58x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.25</summary>

```text
Cost of holding this fund instead of silver itself: -1.7% a year -- a steady drag
Measured: 3 months: fund +1.1%, commodity +1.3%, gap -0.2% | 6 months: fund -8.4%, commodity -5.3%, gap -3.1% | 12 months: fund +59.2%, commodity +60.9%, gap -1.7%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.05</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.05</summary>

```text
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 13.9% of open interest (103,250 contracts)
Change on the week: +1.9% of open interest
Crowding: 73% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.05</summary>

_Not available today._

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> Soybean futures are at the 93rd percentile of their 52-week range after a strong 14% rally in three months, with technical momentum showing signs of fatigue: RSI at 60 is approaching overbought, MACD histogram has turned negative, and the latest daily bar closed down 1% on below-average volume. Large speculators hold a crowded long at the 98th percentile of positioning, a level historically more predictive of consolidation or pullback than continued strength. Macro conditions offer mixed support: the US dollar has strengthened notably this week (+1.23), which headwinds agricultural exports, while Treasury yields have risen and volatility remains elevated at 15.4, not conducive to risk-on commodity buying. The Trump-Xi trade truce narrative is supportive in principle but remains speculative—'in the cards' does not constitute a policy change or tariff cut. Fund carry costs are negligible, so the structural drag is not a factor. The technical position, extreme crowding, and currency headwind suggest the recent rally has priced in much optimism; a near-term consolidation or pullback is more likely than a breakout above the 52-week high. The case for a directional move either way is weak, and technical fatigue combined with crowding argues against adding long exposure here.

**Main reasons it gave:**
- Large speculators hold 98th percentile crowded long; extremes often precede reversals
- RSI 60 and negative MACD histogram signal momentum fatigue after 14% three-month rally
- US dollar strengthened 1.23% this week, headwind for commodity exports
- Price at 93% of 52-week range with below-average volume on down day
- Trump-Xi trade talks speculative; no concrete tariff cuts announced or priced

<details><summary><b>News</b> — score +0.20</summary>

- [Trump-Xi Meeting in the Cards: ETFs Currently in Focus](https://www.tradingview.com/news/zacks:0220861ca094b:0-trump-xi-meeting-in-the-cards-etfs-currently-in-focus/)  
  <sub>TradingView, 3 hours ago</sub>  
  The United States and China are moving closer to extending their trade truce, with negotiations focusing on selective tariff cuts ahead of the scheduled...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 27.68 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 27.38 (+1.1%), 50d 26.24 (+5.5%), 200d 24.39 (+13.5%); 50d above 200d
Momentum: RSI(14) 60.3 | MACD 0.531 vs signal 0.568 (histogram -0.037)
Returns: 1d -1.0% | 5d +0.7% | 1m +5.8% | 3m +14.1%
52-week range: 21.46 - 28.14 (now 93.1% of the way up)
Volatility: ATR(14) 0.35 (1.3% of price) | annualised 20d 17.7%
Volume: 0.67x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.3% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +14.1%, commodity +16.0%, gap -1.9% | 6 months: fund +14.3%, commodity +11.4%, gap +2.9% | 12 months: fund +24.4%, commodity +24.7%, gap -0.3%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 24.0% of open interest (1,070,401 contracts)
Change on the week: +1.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

_Not available today._

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.25

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Crude has run hard (+34% in 3 months, 92% of the 52-week range) and speculative positioning is at the 100th percentile of the past year and still rising -- a crowded long, which is as often the end of a move as the middle. Near-term news is softening: Saudi supply outlook improving, back-to-back down days, and the EIA forecast points to WTI near $73 by spring versus today's spot. Against that, trend and momentum remain intact (50d>200d, MACD positive, RSI 64) with no decisive break. USO also carries the structural note that it holds front-month futures; in backwardation that roll is currently a tailwind, but it is the reason USO lags peers over time. Macro is mildly unhelpful: dollar +1.23 on the week, 10y at 5.00%, VIX quiet. No rate or data surprise this cycle, so no directional call -- a mild downward tilt within NEUTRAL.

**Main reasons it gave:**
- CFTC spec net long at 100th percentile over 52 weeks, +0.9% of OI on the week -- extreme crowding
- EIA forecast of WTI falling to ~$73 by spring versus current elevated spot
- Saudi supply outlook improving; crude posts back-to-back losses
- Price 92.1% of 52-week range, +34.4% in 3 months, RSI 64 -- extended but trend intact
- Dollar index +1.23 on the week, 10y yield 5.00%, no macro surprise

<details><summary><b>News</b> — score -0.20</summary>

- [The Oil Fund Beating USO by Harvesting Roll Yield Faces Its Biggest Test Yet](https://finance.yahoo.com/markets/commodities/articles/oil-fund-beating-uso-harvesting-161036221.html)  
  <sub>Yahoo Finance, 49 minutes ago</sub>  
  DBO surged 108% year-to-date as WTI climbed from $57 to $107, but the EIA forecasts crude falling to $73 by spring. Unlike USO, DBO scans 13 months of...
- [Oil ETF DBO surges 108% YTD but faces risk as E...](https://pluang.com/en/news-feed/dana-minyak-yang-mengalahkan-uso-dengan-strategi-roll-yield-menghadapi-tes)  
  <sub>Pluang, 33 minutes ago</sub>  
  The Invesco DB Oil Fund (DBO) has gained 108% year-to-date by using a roll-yield strategy that benefits from crude oil's backwardation, outperforming the...
- [The U.S. Economy Is Diving Into A Stagflationary Oil Shock](https://seekingalpha.com/article/4947901-us-economy-diving-into-stagflationary-oil-shock)  
  <sub>Seeking Alpha, 40 minutes ago</sub>  
  Rising energy prices and Fed rate hikes threaten U.S. consumers and fuel stagflation risks. Click to read the full analysis here.
- [S&P 500, Nasdaq, Dow End Higher As Drop In Oil Prices Allays Inflationary Concerns — NVDA, MCD, CRWV, LMT, AMZN In Focus](https://www.tradingview.com/news/stocktwits:6a6aef51d094b:0-s-p-500-nasdaq-dow-end-higher-as-drop-in-oil-prices-allays-inflationary-concerns-nvda-mcd-crwv-lmt-amzn-in-focus/)  
  <sub>TradingView, 19 hours ago</sub>  
  U.S. stock indices closed higher Thursday as falling oil prices and Treasury yields eased some inflation concerns a day after the Federal Reserve hiked...
- [Dow Falls Over 500 Points, Nasdaq Sinks As Tech Stocks Tumble — Wells Fargo Warns 'Sugar Rush' Behind Recent Surge Likely Over](https://stocktwits.com/news-articles/markets/equity/dow-falls-nasdaq-sinks-as-tech-stocks-tumble-wells-fargo-warns/cZ0US2wR7Rg)  
  <sub>Stocktwits, 18 hours ago</sub>  
  U.S. equities declined in Tuesday morning's trade, erasing initial gains amid a broader decline in technology stocks after a surge on Monday.
- [Gasoline ETF (UGA) Touches New 52-Week High](https://finance.yahoo.com/markets/commodities/articles/gasoline-etf-uga-touches-52-182600630.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  United States Gasoline ETF UGA is probably on the radar for investors seeking momentum. The fund just hit a 52-week high and has surged 141.6% from its...
- [Crude oil posts back-to-back losses as Saudi supply outlook improves (USO:NYSEARCA)](https://seekingalpha.com/news/4644142-crude-oil-posts-back-to-back-losses-as-saudi-supply-outlook-improves)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Crude oil futures fell as concerns eased over Middle Eastern supply disruptions, with Saudi Arabia once again aiming to ship crude through the Strait of...
- [MSTR's Michael Saylor Says It's 'Time To Silence The Bears' Following Bitcoin's Rally To $72K](https://stocktwits.com/news-articles/markets/cryptocurrency/mstr-michael-saylor-says-it-s-time-to-silence-the-bears-after-bitcoin-rally/cZJfbvPRIAe)  
  <sub>Stocktwits, 18 hours ago</sub>  
  In a post on X, Michael Saylor shared an AI-generated video beating out bears amid Bitcoin's rally. BTIG also reiterated its 'Buy' rating on MSTR's stock...
- [Triple Witching, Falling Oil, and Fed Hopium Drive Up Stocks, But Downside Risks Remain](https://www.benzinga.com/Opinion/26/09/61851724/triple-witching-falling-oil-and-fed-hopium-drive-up-stocks-but-downside-risks-remain)  
  <sub>Benzinga, 24 hours ago</sub>  
  Triple Witching Please click here for an enlarged chart of SPDR S&P 500 ETF Trust (NYSE:SPY) which represents the benchmark stock market index S&P 500 (SPX)...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score +0.35</summary>

```text
Last close 154.33 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 143.68 (+7.4%), 50d 132.54 (+16.4%), 200d 111.29 (+38.7%); 50d above 200d
Momentum: RSI(14) 64.4 | MACD 7.837 vs signal 7.016 (histogram 0.821)
Returns: 1d -0.6% | 5d -0.4% | 1m +17.9% | 3m +34.4%
52-week range: 66.17 - 161.86 (now 92.1% of the way up)
Volatility: ATR(14) 4.85 (3.1% of price) | annualised 20d 42.5%
Volume: 0.52x the 20-day average
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 5.8% of open interest (1,939,911 contracts)
Change on the week: +0.9% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.35</summary>

_Not available today._

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.25

**In the model's own words:**

> WEAT shows mixed signals with no clear directional catalyst. Technicals are conflicted: the fund trades 3.1% below its 20-day moving average with RSI at 47.3 and MACD histogram negative, suggesting near-term weakness, but remains 12.6% above the 200-day MA with a normal upward-sloping curve. The 3-month return of +12.6% has stalled into recent weakness (1-day -1.5%, 5-day -1.6%), and volume is half of average, indicating low conviction. Positioning shows large speculators are crowded long at the 95th percentile with net buying actually reversing this week (-2.2% of open interest), a classic sign of exhaustion rather than momentum. Macro backdrop is neutral: Treasury yields rose modestly across the curve this week, the dollar strengthened meaningfully (+1.23), and VIX remains elevated at 15.4 but stable. Most critically, the fund's cost of holding is severe: -13.2% annualized drag from rolling futures contracts. This heavy structural cost requires a substantially larger wheat price move to justify a long position and acts as a persistent headwind. No fresh news, no supply or demand surprise, and no technical break justify directional conviction. The crowded long positioning combined with negative momentum and the structural cost disadvantage slightly favor caution, but not enough to reverse the intermediate uptrend.

**Main reasons it gave:**
- Large speculators crowded long at 95th percentile with net selling this week suggesting positioning exhaustion
- MACD histogram negative and RSI at 47.3 amid recent price weakness despite intermediate uptrend
- Fund cost of holding -13.2% annualized, requiring larger wheat move to justify long exposure
- Dollar strength (+1.23 on week) headwind for commodity-denominated assets
- Volume 0.30x average indicates low conviction in current price levels

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 25.84 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 26.67 (-3.1%), 50d 25.41 (+1.7%), 200d 22.95 (+12.6%); 50d above 200d
Momentum: RSI(14) 47.3 | MACD 0.265 vs signal 0.467 (histogram -0.203)
Returns: 1d -1.5% | 5d -1.6% | 1m +2.0% | 3m +12.6%
52-week range: 19.88 - 28.00 (now 73.4% of the way up)
Volatility: ATR(14) 0.62 (2.4% of price) | annualised 20d 30.7%
Volume: 0.30x the 20-day average
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
Cost of holding this fund instead of wheat itself: -13.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +12.6%, commodity +17.5%, gap -4.9% | 6 months: fund +10.7%, commodity +17.1%, gap -6.4% | 12 months: fund +21.6%, commodity +34.8%, gap -13.2%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-08, published the following Friday)
Large speculators: net long 1.0% of open interest (484,680 contracts)
Change on the week: -2.2% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

_Not available today._

</details>

### Natural gas (UNG) · Commodity — NEUTRAL, confidence 0.20

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro or policy surprise this week: yields moved a few basis points, VIX fell slightly, curve normally sloped. UNG's technicals are mixed -- price just above 20d and 50d but 50d below 200d and 9.8% under the 200d, sitting near the bottom decile of its 52-week range with RSI at a neutral 52. The one durable fact is the -14.2% annual roll cost, which is a standing tax on any long and a tailwind to shorts, but not a direction on its own. CFTC positioning shows specs modestly net short at the 35th percentile, i.e. unremarkable. The single news item concerns crude and DBO, not natural gas, and is irrelevant here; no gas storage data was provided. Nothing justifies a directional macro call.

**Main reasons it gave:**
- Roll/carry drag of -14.2% a year versus spot natural gas
- Price 9.8% below 200d SMA with 50d below 200d, but above 20d/50d -- mixed trend
- RSI 52, MACD barely positive: no momentum edge
- Specs net short 5.3% of OI, 35th percentile crowding, little weekly change
- Macro quiet: 10y +3bp, VIX 15.4 and falling, curve normal
- Only headline is crude/DBO-specific and not relevant to natural gas

<details><summary><b>News</b> — score +0.00</summary>

- [The Oil Fund Beating USO by Harvesting Roll Yield Faces Its Biggest Test Yet](https://247wallst.com/investing/etf/2026/09/18/the-oil-fund-beating-uso-by-harvesting-roll-yield-faces-its-biggest-test-yet/)  
  <sub>24/7 Wall St., 50 minutes ago</sub>  
  DBO's roll-yield strategy turned crude's backwardation into a triple-digit gain this year, but the EIA sees WTI dropping more than $30 by spring and no...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 3.98% (+0.07 on the week) | 5-year 4.86% (+0.07 on the week) | 10-year 5.00% (+0.03 on the week) | 30-year 5.33% (-0.02 on the week)
Yield curve, 10-year minus 3-month: +1.02 points -- upward sloping (normal)
US dollar index: 100.35 (+1.23 on the week)
Volatility (VIX): 15.39 (-0.4 on the week) -- elevated
```

</details>

<details><summary><b>Price and chart</b> — score -0.05</summary>

```text
Last close 10.41 (bar of 2026-09-18), from 502 daily bars
Trend: vs 20d SMA 10.37 (+0.4%), 50d 10.24 (+1.7%), 200d 11.54 (-9.8%); 50d below 200d
Momentum: RSI(14) 52.2 | MACD 0.025 vs signal 0.020 (histogram 0.004)
Returns: 1d +0.8% | 5d +2.4% | 1m +4.0% | 3m -11.3%
52-week range: 9.63 - 16.90 (now 10.7% of the way up)
Volatility: ATR(14) 0.28 (2.7% of price) | annualised 20d 24.2%
Volume: 1.13x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -14.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -11.3%, commodity -10.2%, gap -1.2% | 6 months: fund -17.1%, commodity -8.3%, gap -8.8% | 12 months: fund -20.5%, commodity -6.3%, gap -14.2%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-08, published the following Friday)
Large speculators: net short 5.3% of open interest (1,823,243 contracts)
Change on the week: -0.4% of open interest
Crowding: 35% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

_Not available today._

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

