# Daily report

**25 Sep 2026, 19:21 Israel time (16:21 UTC)** · 80 names checked · 0 traded · 7 with a problem

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 1 | 15 | 0 |
| Whole-market funds | 14 | 0 | 13 | 1 |
| Sector and country funds | 41 | 0 | 38 | 3 |
| Commodities | 9 | 0 | 6 | 3 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| US government bonds, 7-10 years (IEF) · Index fund | **Sold part.** Sold 40 of 120 shares at +1.94R, 80 still held. Stop-loss raised 91.28 → 90.57. |
| Microsoft (MSFT) · Company | **Sold part.** Sold 3 of 10 shares at +1.17R, 7 still held. Stop-loss raised 477.77 → 492.61. |
| US government bonds, 20+ years (TLT) · Index fund | **Sold part.** Sold 45 of 135 shares at +1.62R, 90 still held. Stop-loss raised 82.41 → 80.48. |
| ASML (ASML) · Company | **Stop raised.** At +0.17R, following the price. Stop-loss raised 1619.35 → 1640.82. |
| Caterpillar (CAT) · Company | **Stop raised.** At +0.16R, following the price. Stop-loss raised 757.24 → 768.09. |
| Developing country bonds (EMB) · Index fund | **Stop raised.** At +1.93R, following the price. Stop-loss raised 93.39 → 92.80. |
| JPMorgan Chase (JPM) · Company | **Stop raised.** At +0.15R, following the price. Stop-loss raised 323.48 → 327.15. |
| US inflation-linked bonds (TIP) · Index fund | **Stop raised.** At +2.47R, following the price. Stop-loss raised 105.39 → 105.14. |
| Taiwan (EWT) · Sector or country | **Holding.** -0.06R, holding 33 shares. Stop-loss 110.28. |
| Gold (GLD) · Commodity | **Holding.** -0.20R, holding 10 shares. Stop-loss 403.77. |
| HDFC Bank (HDB) · Company | **Holding.** -0.33R, holding 90 shares. Stop-loss 22.23. |
| US regional banks (KRE) · Sector or country | **Holding.** -0.05R, holding 53 shares. Stop-loss 72.54. |
| Eli Lilly (LLY) · Company | **Holding.** +0.28R, holding 4 shares. Stop-loss 1130.70. |
| Nvidia (NVDA) · Company | **Holding.** +0.73R, holding 16 shares. Stop-loss 216.23. |
| Novo Nordisk (NVO) · Company | **Holding.** +0.39R, holding 123 shares. Stop-loss 41.12. |
| Procter & Gamble (PG) · Company | **Holding.** -0.34R, holding 14 shares. Stop-loss 143.18. |
| S&P 500, equal weight (RSP) · Index fund | **Holding.** +0.31R, holding 14 shares. Stop-loss 214.01. |
| Royal Bank of Canada (RY) · Company | **Holding.** -0.15R, holding 10 shares. Stop-loss 194.59. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** -0.12R, holding 128 shares. Stop-loss 37.12. |
| US dollar (UUP) · Index fund | **Holding.** +1.14R, holding 282 shares. Stop-loss 28.50. |
| US shopping and leisure (XLY) · Sector or country | **Holding.** -0.04R, holding 63 shares. Stop-loss 113.13. |
| Exxon Mobil (XOM) · Company | **Holding.** +0.01R, holding 13 shares. Stop-loss 156.50. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### MercadoLibre (MELI) · Company — NEUTRAL, confidence 0.80

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The recent profit miss and margin concerns (negative news) combined with bearish technical indicators (price below SMAs, low RSI, negative MACD, low volume) outweigh the bullish analyst consensus and modest insider buying. Fundamentals are mixed, with high valuation and leverage but strong revenue growth. Overall, the negative catalyst and technical weakness suggest a bearish short‑term outlook.

**Main reasons it gave:**
- Profit miss and margin concerns reported in recent news (Stocktwits, 12h ago)
- RSI 35 and MACD negative, price below 20‑day SMA (Technicals)
- Forward P/E 31.13 and debt/equity 168.6% indicate high valuation and leverage (Fundamentals)
- Earnings record: 1 beat, 3 misses over last 4 quarters (Earnings Record)

<details><summary><b>News</b> — score -0.60</summary>

- [MercadoLibre (MELI) Stock Looks Rich Relative To Its Earnings](https://finance.yahoo.com/markets/stocks/articles/mercadolibre-meli-stock-looks-rich-011401553.html)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  MercadoLibre has seen a sharp shift in sentiment over the past year, yet the longer term record still shows a solid gain. That gap between recent share...
- [MercadoLibre Stock Plunges On Margin Fears — Bulls Call It A ‘Laughable’ Selloff](https://stocktwits.com/news-articles/markets/equity/mercadolibre-stock-plunges-on-margin-fears-bulls-call-laughable-selloff/cZR6zYRRIb5)  
  <sub>Stocktwits, 12 hours ago</sub>  
  MELI stock was battered on Wednesday, even after better-than-expected revenue, as a profit miss weighed on investor sentiment.
- [MercadoLibre vs. Target: Which Stock Offers the Better Setup Now?](https://www.tradingview.com/news/zacks:5f84e6d02094b:0-mercadolibre-vs-target-which-stock-offers-the-better-setup-now/)  
  <sub>TradingView, 3 hours ago</sub>  
  As MercadoLibre, Inc. MELI and Target Corporation TGT continue to strengthen their respective business models and invest in long-term growth initiatives,...
- [MercadoLibre (Dinari Tokenized Stock) (MELI) Price Prediction for 2026 to 2031](https://www.bybit.com/en/price-prediction/mercadolibre-dinari-tokenized-stock/)  
  <sub>Bybit, 15 hours ago</sub>  
  Based on current prediction models, MELI is estimated to reach approximately $2,136 by 2030. Compared to its current price of $1,757, this suggests potential...
- [MELI stock falls 2.51 percent ahead of the open](https://www.ad-hoc-news.de/boerse/news/vorboerse/meli-stock-falls-2-51-percent-ahead-of-the-open/70181104)  
  <sub>AD HOC NEWS, 11 hours ago</sub>  
  At the close on September 24, 2026, MELI stock stood at USD 1754.13 after falling 2.51 percent. The Nasdaq Composite gained 0.01 percent,...
- [MELI261120C02220000 Interactive Stock Chart | MELI Nov 2026 2220.000 call Stock](https://finance.yahoo.com/chart/MELI261120C02220000)  
  <sub>Yahoo Finance, 14 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MercadoLibre (MELI) Sees a More Significant Dip Than Broader Market: Some Facts to Know](https://sg.finance.yahoo.com/news/mercadolibre-meli-sees-more-significant-205004165.html)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  The latest trading day saw MercadoLibre (MELI) settling at $1, representing a -2.51% change from its previous close.
- [MELI261023P01600000 Interactive Stock Chart | MELI Oct 2026 1600.000 put Stock](https://finance.yahoo.com/chart/MELI261023P01600000)  
  <sub>Yahoo Finance, 15 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI261030P01320000 Interactive Stock Chart | MELI Oct 2026 1320.000 put Stock](https://finance.yahoo.com/chart/MELI261030P01320000)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [MELI Nov 2026 1640.000 call (MELI261120C01640000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/MELI261120C01640000/)  
  <sub>Yahoo Finance UK, 21 hours ago</sub>  
  Find the latest MELI Nov 2026 1640.000 call (MELI261120C01640000) stock quote, history, news and other vital information to help you with your stock trading...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 1,740.37 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 1,878.52 (-7.4%), 50d 1,870.40 (-7.0%), 200d 1,845.05 (-5.7%); 50d above 200d
Momentum: RSI(14) 35.0 | MACD -32.756 vs signal -14.216 (histogram -18.540)
Returns: 1d -0.8% | 5d -2.6% | 1m -10.8% | 3m +3.9%
52-week range: 1,546.81 - 2,501.31 (now 20.3% of the way up)
Volatility: ATR(14) 58.14 (3.3% of price) | annualised 20d 27.5%
Volume: 0.27x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 88.23B
Valuation: trailing P/E 47.42 | forward P/E 31.13 | P/B 11.26 | PEG 1.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.70</summary>

```text
Consensus: buy (mean 1.56 on a 1=strong buy to 5=strong sell scale, 25 analysts)
Ratings: 4 strong buy, 16 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 2,272.28 (+30.6% vs last close), range 1,750.00 - 2,800.00
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

**In the model's own words:**

> BUY

**Main reasons it gave:**
- Gemini 4 AI launch expected earlier than year-end (Stocktwits, 3h)
- TPU business scaling across cloud, boosting growth (TradingKey, 2h)
- Strong fundamentals: 24% YoY revenue growth, 54.8% profit margin (Fundamentals)
- Analyst consensus strong buy, mean target +25% upside (Analyst view)

<details><summary><b>News</b> — score +0.30</summary>

- [Alphabet Inc. (GOOG.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GOOG.TO/)  
  <sub>Yahoo! Finance Canada, 1 hour ago</sub>  
  Alphabet Inc. (GOOG.TO) · -1.26% · -1.10% · 15.89% · 6.60% · 34.99% · 191.96% · 191.96%. Key Events. Baseline. Advanced Chart. Loading...
- [Alphabet (GOOGL) Stock May Trade At A Discount Despite Privacy Fine](https://simplywall.st/stocks/us/media/nasdaq-googl/alphabet/news/alphabet-googl-stock-may-trade-at-a-discount-despite-privacy)  
  <sub>Simply Wall Street, 6 hours ago</sub>  
  Alphabet has racked up hefty gains over the past few years, and with the stock now around US$342 per share investors are asking a simple question.
- [GOOGL Stock Inches Up Premarket: Retail Traders Are Buying The Dip After CapEx-Fueled Selloff](https://stocktwits.com/news-articles/markets/equity/googl-stock-inches-up-premarket-retail-traders-are-buying-the-dip-after-cap-ex-fueled-selloff/cZZYAMLR7yW)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The move came as a relief for the stock which has fallen sharply over the last two months.
- [The "Magnificent Seven" Stocks: Here's the 1 I'm Buying Hand Over Fist Right Now](https://www.fool.com/investing/2026/09/25/the-magnificent-seven-stocks-heres-the-1-im-buying/)  
  <sub>The Motley Fool, 1 hour ago</sub>  
  The "Magnificent Seven" stocks consist of Nvidia, Apple, Microsoft (MSFT +3.52%), Amazon (AMZN -0.34%), Alphabet (NASDAQ: GOOG) (GOOGL +0.50%),...
- [Alphabet's $30 Billion SpaceX Bill Isn't What It Looks Like (NASDAQ:GOOG)](https://seekingalpha.com/article/4949730-alphabets-30-billion-spacex-bill-isnt-what-it-looks-like)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Alphabet signed a deal to rent a large chunk of computing power from SpaceX's data centers, paying a discounted rate. Read why GOOG stock is a strong buy.
- [Alphabet Stock: How The Bears In Options Trading Can Take Advantage Of This Search Giant](https://investors.com/research/options/alphabet-googl-google-stock-bear-call-spread-options/)  
  <sub>Investor's Business Daily, 23 hours ago</sub>  
  Alphabet (GOOGL) stock fell nearly 4% Wednesday and crossed below the key 50-day moving average. That kind of bearish price action could indicate further...
- [Google Stock Forecast: TPU Growth Strengthens Alphabet’s Challenge to Nvidia](https://www.tradingkey.com/analysis/stocks/us-stocks/262184169-google-stock-forecast-tpu-growth-nvidia-challenge-tradingkey)  
  <sub>TradingKey, 2 hours ago</sub>  
  Alphabet's TPU business is scaling across Cloud and dedicated systems as GOOGL tests trendline support near $338.
- [Google's Answer To Meta’s Muse AI? DeepMind Chief Says Gemini 4 Launch Is Coming 'Much Earlier'](https://stocktwits.com/news-articles/markets/equity/googl-stock-steadies-after-worst-drop-in-a-month-as-deep-mind-chief-says-gemini-4-is-coming-much-earlier/cZM7YFyRBBo)  
  <sub>Stocktwits, 3 hours ago</sub>  
  Gemini 4 has entered early post-training and is expected to launch ahead of year-end. GOOGL shares had fallen nearly 5% over two sessions as Meta's Muse...
- [GOOGL, OpenAI, Anthropic Are Reportedly Building Their Own AI Safety Watchdog — But Without Government Oversight](https://es.tradingview.com/news/stocktwits:f02ea9d44094b:0-googl-openai-anthropic-are-reportedly-building-their-own-ai-safety-watchdog-but-without-government-oversight/)  
  <sub>TradingView, 19 hours ago</sub>  
  Alphabet Inc.'s (GOOGL) Google, OpenAI and Anthropic are reportedly pushing ahead with plans to create a new industry-led AI safety standards body without...
- [Alphabet Trades for 17 Times Earnings. The S&P 500 Trades for 25 Times Earnings. Is This the Best Stock to Buy in the Market?](https://www.theglobeandmail.com/investing/markets/stocks/GOOGL-Q/pressreleases/4797315/alphabet-trades-for-17-times-earnings-the-sp-500-trades-for-25-times-earnings-is-this-the-best-stock-to-buy-in-the-market/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Sometimes the market values fantastic stocks at low prices, just like it appears to be doing with Alphabet(NASDAQ: GOOG)(NASDAQ: GOOGL) right now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 343.63 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 342.16 (+0.4%), 50d 344.28 (-0.2%), 200d 338.21 (+1.6%); 50d above 200d
Momentum: RSI(14) 49.5 | MACD 0.060 vs signal -0.372 (histogram 0.432)
Returns: 1d +0.4% | 5d -1.7% | 1m +0.5% | 3m +1.8%
52-week range: 236.57 - 402.62 (now 64.5% of the way up)
Volatility: ATR(14) 8.79 (2.6% of price) | annualised 20d 27.3%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.70</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.20T
Valuation: trailing P/E 17.24 | forward P/E 23.06 | P/B 6.75 | PEG 1.25
Profitability: profit margin 54.8% | operating margin 34.0% | ROE 48.7%
Growth (YoY): revenue +24.2% | earnings +294.0%
Balance sheet: debt/equity 18.9% | free cash flow 22.67B
Risk: beta 1.23 | short interest 1.5% of float
Next earnings: 2026-10-28
```

</details>

<details><summary><b>What this fund holds</b> — score +0.70</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.70</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 missed
  2026-06-30 missed by 4% | 2026-03-31 missed by 3% | 2025-12-31 beat by 4% | 2025-09-30 beat by 29%
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: strong_buy (mean 1.38 on a 1=strong buy to 5=strong sell scale, 54 analysts)
Ratings: 13 strong buy, 43 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 429.46 (+25.0% vs last close), range 340.00 - 515.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

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

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material news catalyst; technicals show price below longer‑term averages with low volume; valuation is high (trailing P/E 55.3) despite strong growth; earnings record is strong (4 consecutive beats) but not a forward catalyst.

**Main reasons it gave:**
- No material news catalyst in the past 24 hours
- Price below 50‑day and 200‑day SMA with volume at 0.25× 20‑day average
- Trailing P/E of 55.3 indicates expensive valuation
- Four consecutive earnings beats (10‑21% beat) but no forward catalyst

<details><summary><b>News</b> — score +0.00</summary>

- [ESLT261016P00620000 interactive stock chart | ESLT Oct 2026 620.000 put stock](https://au.finance.yahoo.com/chart/ESLT261016P00620000)  
  <sub>Yahoo Finance Australia, 10 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [NICE Ltd. (NICE.TA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NICE.TA/)  
  <sub>Yahoo! Finance Canada, 17 hours ago</sub>  
  Find the latest NICE Ltd. (NICE.TA) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 734.05 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 725.24 (+1.2%), 50d 762.54 (-3.7%), 200d 769.03 (-4.5%); 50d below 200d
Momentum: RSI(14) 46.6 | MACD -3.118 vs signal -7.211 (histogram 4.093)
Returns: 1d -0.8% | 5d -1.3% | 1m +1.6% | 3m +2.6%
52-week range: 454.95 - 1,014.33 (now 49.9% of the way up)
Volatility: ATR(14) 16.08 (2.2% of price) | annualised 20d 14.5%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 34.40B
Valuation: trailing P/E 55.32 | forward P/E 39.98 | P/B 7.78 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.9% of float
Next earnings: 2026-11-24
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

```text
Consensus: none (mean n/a on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 816.33 (+11.2% vs last close), range 518.00 - 960.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

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

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### Toyota (TM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst consensus and strong earnings record are offset by bearish technicals and mixed fundamentals (low P/E but high debt and negative free cash flow). No news catalyst and no insider activity. Overall dimensions conflict, leading to a neutral directional view with low conviction.

**Main reasons it gave:**
- Technical indicators show bearish momentum (price below 20‑day/50‑day SMA, negative MACD, thin volume)
- Analyst consensus strong buy with mean price target +23.6% above last close
- Mixed fundamentals: low trailing P/E 8.65 but high debt/equity 115% and negative free cash flow
- Four consecutive earnings beats indicating strong earnings record

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 189.39 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 193.96 (-2.4%), 50d 190.07 (-0.4%), 200d 201.89 (-6.2%); 50d below 200d
Momentum: RSI(14) 45.6 | MACD -0.262 vs signal 0.834 (histogram -1.096)
Returns: 1d +1.4% | 5d -1.1% | 1m -1.3% | 3m +10.4%
52-week range: 166.50 - 248.29 (now 28.0% of the way up)
Volatility: ATR(14) 3.27 (1.7% of price) | annualised 20d 22.1%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 224.27B
Valuation: trailing P/E 8.65 | forward P/E 12.00 | P/B 15.02 | PEG n/a
Profitability: profit margin 8.6% | operating margin 7.9% | ROE 12.4%
Growth (YoY): revenue +10.4% | earnings +86.9%
Balance sheet: debt/equity 115.0% | free cash flow -3.60T
Risk: beta 0.34 | short interest 0.1% of float
Next earnings: 2026-11-05
```

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.20</summary>

```text
Earnings record, last 4 quarters: 4 beats
  2026-06-30 beat by 44% | 2026-03-31 beat by 12% | 2025-12-31 beat by 27% | 2025-09-30 beat by 24%
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
Consensus: strong_buy (mean 1.50 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 2 strong buy, 2 buy, 0 hold, 0 sell, 0 strong sell
Price target: mean 234.08 (+23.6% vs last close), range 230.00 - 239.31
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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML vs. Applied Materials: Which AI Chip-Equipment Stock Is the Better Buy?](https://finance.yahoo.com/technology/ai/articles/asml-vs-applied-materials-ai-040717818.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  ASML Holding N.V. (NASDAQ:ASML) and Applied Materials, Inc. (NASDAQ:AMAT) sell different tools, but both compete for the same investor dollar tied to...
- [ASML Stock Tumbles 6% As Investors Weigh China Risk — But Wall Street And Retail Investors Dismiss Selloff](https://stocktwits.com/news-articles/markets/equity/asml-stock-tumbles-6-as-investors-weigh-china-risk-but-wall-street-and-retail-investors-dismiss-selloff/cZZxMRFR76t)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Another user pinned the selloff on the stock pricing in high expectations. “Strong companies can still drop when valuations leave little room for disappointment...
- [Asml Stock Analysis: Momentum Cooling but Bulls Hold $1,722](https://en.cryptonomist.ch/2026/09/25/asml-stock-clings-to-bullish-structure-at-1722-as-momentum-fades/)  
  <sub>The Cryptonomist, 6 hours ago</sub>  
  Explore the latest Asml stock analysis with insights on momentum, key technical levels, and what influences price at $1722.50 in this update.
- [ASML (ASML) Q2 2026 Earnings Preview: $7.94 EPS Expected, 8% Options Swing; Triangle at $1,800](https://www.tradingkey.com/analysis/stocks/us-stocks/262030125-asml-q2-2026-earnings-preview-eps-triangle-breakout-1800-tradingkey)  
  <sub>TradingKey, 17 hours ago</sub>  
  ASML reports Q2 2026 earnings this morning. Consensus: EPS $7.94, revenue $10.27B. Options pricing an 8.36% swing either way. The stock has pulled back 11%...
- [TSMC Collaborates to Expand Large-Format Photomasks for High NA EUV](https://qz.com/tsmc-collaborates-to-expand-large-format-photomasks-for-high-na-euv)  
  <sub>qz.com, 13 hours ago</sub>  
  Taiwan Semiconductor and ASML are advancing 12-inch High-NA EUV photomasks to boost fab productivity, cut chipmaking costs and ease stitching constraints.
- [SNDK, NVDA, SKHY, ASML Stocks Extend Slide Overnight As China’s Chip Challenge Rattles Investors](https://stocktwits.com/news-articles/markets/equity/sndk-nvda-skhy-asml-stocks-extend-slide-overnight-amid-china-ai-challenge-tech-rotation/cZZCeckR766)  
  <sub>Stocktwits, 5 hours ago</sub>  
  The company posted a net loss of $228.22 million, or a diluted loss of $0.95 per share. On an adjusted basis, Navitas reported a second-quarter EPS loss of...
- [5 AI Semiconductor Stocks to Buy and Hold Through 2031](https://www.fool.com/investing/2026/09/24/5-ai-semiconductor-stocks-to-buy-and-hold-through/)  
  <sub>The Motley Fool, 19 hours ago</sub>  
  These five stocks look well-positioned to outperform over the next five years.
- [Is Taiwan Semiconductor (TSM) Stock a Better Bet than ASML Holding (ASML) as Advanced Chipmaking Accelerates?](https://finance.yahoo.com/technology/articles/taiwan-semiconductor-tsm-stock-better-210504814.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  On September 8, Taiwan Semiconductor Manufacturing Company Limited (NYSE:TSM) and ASML Holding N.V. (NASDAQ:ASML) announced a collaborative industry...
- [Is ASML Holding (NASDAQ:ASML) Facing a Real Market Test?](https://kalkinemedia.com/us/stocks/artificial-intelligence/is-asml-holding-nasdaqasml-facing-a-real-market-test)  
  <sub>Kalkine Media, 7 hours ago</sub>  
  Follow ASML Holding as investors assess advanced semiconductor lithography systems, the current catalyst, execution risks and the company evidence that may...
- [ASML Drops 1.8% as $400 Million High-NA Tools Reach More Fabs](https://www.tradingview.com/news/gurufocus:a91967fcf094b:0-asml-drops-1-8-as-400-million-high-na-tools-reach-more-fabs/)  
  <sub>TradingView, 20 hours ago</sub>  
  ASML Holding NASDAQ:ASML, the Dutch chipmaking equipment leader, won broader commitments for its roughly $400 million High-NA EUV machines. Its U.S. shares...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,742.00 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 1,686.38 (+3.3%), 50d 1,717.53 (+1.4%), 200d 1,524.92 (+14.2%); 50d above 200d
Momentum: RSI(14) 54.4 | MACD -1.816 vs signal -13.616 (histogram 11.800)
Returns: 1d +1.1% | 5d +3.7% | 1m -0.2% | 3m -2.9%
52-week range: 936.19 - 1,989.44 (now 76.5% of the way up)
Volatility: ATR(14) 52.33 (3.0% of price) | annualised 20d 41.2%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 669.10B
Valuation: trailing P/E 59.84 | forward P/E 29.42 | P/B 1,496.47 | PEG 1.58
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
Price target: mean 2,123.30 (+21.9% vs last close), range 881.94 - 2,824.13
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

- [Yields keep rising, Novo's tough week, why cat product sales are surging and more in Morning Squawk](https://www.cnbc.com/2026/09/25/5-things-to-know-before-the-stock-market-opens.html)  
  <sub>CNBC, 3 hours ago</sub>  
  Happy Friday. Your morning cup of joe may soon get harder to find, as Starbucks · closes more of its stores. Stock futures are slightly higher this morning...
- [Red Cat: A Guidance Cut Should Be Coming, And The Stock Already Knows](https://seekingalpha.com/article/4949643-red-cat-a-guidance-cut-should-be-coming-and-the-stock-already-knows)  
  <sub>Seeking Alpha, 12 hours ago</sub>  
  Red Cat Holdings (RCAT) analysis: cautious Hold amid 2026 revenue shortfall risk, improving margins, and cash burn concerns. Read here for more details.
- [What Would You Have Needed To Notice In Caterpillar Stock?](https://www.trefis.com/stock/cat/articles/616464/what-would-you-have-needed-to-notice-in-caterpillar-stock/2026-09-24)  
  <sub>Trefis, 22 hours ago</sub>  
  Caterpillar (CAT) stock returned 74% in the twelve months to September 23, 2026. A $10000 holding at the start was worth about $17350 at the end.
- [Red Cat Holdings, Inc. (RCAT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RCAT/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  -100.00% · Previous Close 6.59 · Open 6.49 · Bid 4.84 x 100 · Ask 12.00 x 100 · Day's Range 6.37 - 6.83 · 52 Week Range 5.77 - 18.78 · Volume 8,399,868 · Avg.
- [Dow Ends Sees Worst Day In Over A Year, Nasdaq Enters Correction Territory As Fed Decision Piques Inflation Concerns — SPCX, CAT, ADBE, SOFI, HIMS Stock In Focus](https://stocktwits.com/news-articles/markets/equity/dow-ends-sees-worst-day-in-over-a-year-nasdaq-enters-correction-territory/cZNT9JSRJTp)  
  <sub>Stocktwits, 14 hours ago</sub>  
  U.S. equity futures were little changed on Wednesday as investors digested Microsoft, Meta and Qualcomm earnings and the Federal Reserve's decision.
- [Is Caterpillar the Best Industrials Stock to Buy Right Now?](https://www.fool.com/investing/2026/09/24/is-caterpillar-the-best-industrials-stock-to-buy-r/)  
  <sub>The Motley Fool, 21 hours ago</sub>  
  The construction and heavy machinery company Caterpillar (CAT -0.83%) recently delivered one of its strongest quarters in history. A beneficiary of the...
- [Unusual Machines Jumps 6% as Drone Names Bounce Together; Ondas Climbs 4%, Red Cat Rises 3%](https://247wallst.com/investing/2026/09/24/unusual-machines-jumps-6-as-drone-names-bounce-together-ondas-climbs-4-red-cat-rises-3/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Drone stocks are surging together while the broader market sits flat, and the pattern of who is gaining the most reveals exactly where traders are placing...
- [Thursday's session: top gainers and losers in the dow jones index](https://www.chartmill.com/news/MSFT/Chartmill-55305-Thursdays-session-top-gainers-and-losers-in-the-dow-jones-index)  
  <sub>ChartMill, 23 hours ago</sub>  
  Stay updated with the movement of dow jones stocks in today's session. Discover which dow jones stocks are making waves on Thursday.
- [Caterpillar vs. Honeywell International: Which Industrials Stock Is a Better Buy in 2026?](https://www.theglobeandmail.com/investing/markets/stocks/CAT-N/pressreleases/4782565/caterpillar-vs-honeywell-international-which-industrials-stock-is-a-better-buy-in-2026/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Caterpillar Inc (CAT-N) from The Globe and Mail including charting and trades.
- [Caterpillar stock heads into the open after a 2.1 percent drop](https://www.ad-hoc-news.de/boerse/news/vorboerse/caterpillar-stock-heads-into-the-open-after-a-2-1-percent-drop/70181463)  
  <sub>AD HOC NEWS, 10 hours ago</sub>  
  At the close on September 24, 2026, Caterpillar stock fell 2.1 percent as the Dow dropped 0.3 percent to 51349.98; rising Treasury yields shaped the broader...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 810.32 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 802.74 (+0.9%), 50d 829.01 (-2.3%), 200d 789.51 (+2.6%); 50d above 200d
Momentum: RSI(14) 48.6 | MACD -6.914 vs signal -10.577 (histogram 3.663)
Returns: 1d +0.6% | 5d +0.2% | 1m -1.4% | 3m -18.8%
52-week range: 463.72 - 1,064.90 (now 57.7% of the way up)
Volatility: ATR(14) 22.77 (2.8% of price) | annualised 20d 25.7%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 372.48B
Valuation: trailing P/E 34.94 | forward P/E 25.03 | P/B 19.21 | PEG 1.42
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
Consensus: buy (mean 2.14 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 13 buy, 12 hold, 1 sell, 1 strong sell
Price target: mean 975.61 (+20.4% vs last close), range 575.00 - 1,225.00
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

- [HDFC Bank Limited (HDB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  3,048.97% · Previous Close 22.79 · Open 22.75 · Bid 23.10 x 800000 · Ask 23.25 x 550000 · Day's Range 22.75 - 22.99 · 52 Week Range 21.77 - 37.45 · Volume...
- [HDFC Bank Limited (HDB) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  HDFC Bank Limited (HDB) · -1.42% · -3.02% · -9.12% · -37.35% · -33.75% · -38.00% · 3,048.97%. Key events. Baseline. Advanced...
- [Kaplan Fox Shareholder Alert: Deadline to Lead in the Securities Fraud Lawsuit Against HDFC Bank Limited (NYSE: HDB) is October 13, 2026](https://www.theglobeandmail.com/investing/markets/stocks/HDB-N/pressreleases/4800138/kaplan-fox-shareholder-alert-deadline-to-lead-in-the-securities-fraud-lawsuit-against-hdfc-bank-limited-nyse-hdb-is-october-13-2026/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Hdfc Bank Ltd ADR (HDB-N) from The Globe and Mail including charting and trades.
- [INVESTOR ALERT: Pomerantz Law Firm Reminds Investors with Losses on their Investment in HDFC Bank Limited of Class Action Lawsuit and Upcoming Deadlines - HDB](https://www.prnewswire.com/news-releases/investor-alert-pomerantz-law-firm-reminds-investors-with-losses-on-their-investment-in-hdfc-bank-limited-of-class-action-lawsuit-and-upcoming-deadlines--hdb-302889619.html)  
  <sub>PR Newswire, 19 hours ago</sub>  
  PRNewswire/ -- Pomerantz LLP announces that a class action lawsuit has been filed against HDFC Bank Limited ("HDFC" or the "Company") (NYSE: HDB). Such...
- [HDB UPCOMING DEADLINE: Faruqi & Faruqi, LLP Reminds HDFC Bank Limited Investors of Securities Class Action Lawsuit Deadline on October 12, 2026](https://www.newsfilecorp.com/release/315700/HDB-UPCOMING-DEADLINE-Faruqi-Faruqi-LLP-Reminds-HDFC-Bank-Limited-Investors-of-Securities-Class-Action-Lawsuit-Deadline-on-October-12-2026?lang=fr)  
  <sub>TMX Newsfile, 18 hours ago</sub>  
  Faruqi & Faruqi, LLP Securities Litigation Partner James (Josh) Wilson Encourages Investors Who Suffered Losses In HDFC Bank Limited To...
- [Daily Brief Financials: National Stock Exchange, M-DAQ, RBL Bank, HDFC Bank (ADR), Spring Real Estate, Bajaj Finserv , Insurance Australia, Link REIT, Metlife Inc, Chubb and more](https://www.smartkarma.com/home/daily-briefs/daily-brief-financials-national-stock-exchange-m-daq-rbl-bank-hdfc-bank-adr-spring-real-estate-bajaj-finserv-insurance-australia-link-reit-metlife-inc-chubb-and-more/)  
  <sub>Smartkarma, 13 hours ago</sub>  
  National Stock Exchange (NSEIN IN) raised about US$2.4bn in its India IPO. NSE operates electronic platforms for trading equities, derivatives, currencies,...
- [Diamond Power Infrastructure (DIACABS-BE) Share Price Falls 3.54% Today](https://univest.in/blogs/why-diamond-power-infrastructure-share-price-price-fall-2026-09-25)  
  <sub>Univest, 8 hours ago</sub>  
  Diamond Power Infrastructure Share Price fell 3.54% to Rs 350.30. Check price action, technicals, valuation, ownership and sector context.
- [Motilal Oswal group gets SEBI custodian licence to start operations from Q4](https://m.economictimes.com/markets/stocks/news/motilal-oswal-group-gets-sebi-custodian-licence-to-start-operations-from-q4/articleshow/134478554.cms)  
  <sub>The Economic Times, 8 hours ago</sub>  
  Motilal Oswal Financial Services' wholly owned subsidiary MOCSPL has received SEBI approval to operate as a securities custodian, expanding the group's...
- [Naapbooks Ltd. Upper Circuit Today: Price, Data and Peers](https://univest.in/blogs/why-nbl-share-price-upper-circuit-today-2026)  
  <sub>Univest, 8 hours ago</sub>  
  Naapbooks Ltd. hit upper circuit on BSE on 25 September 2026 at Rs 151.2, a 5% move. Price action, valuation and peer context.
- [These large- and mid-cap stocks can give more than 20% return in 1 year, according to analysts](https://m.economictimes.com/markets/stocks/news/these-large-and-mid-cap-stocks-can-give-more-than-20-return-in-1-year-according-to-analysts/articleshow/134468554.cms)  
  <sub>The Economic Times, 21 hours ago</sub>  
  The next time you take some action in the stock market – whether it is buying or selling – ask yourself these questions: Why am I doing this?

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 22.93 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 22.87 (+0.3%), 50d 23.29 (-1.5%), 200d 27.39 (-16.3%); 50d below 200d
Momentum: RSI(14) 48.5 | MACD -0.107 vs signal -0.175 (histogram 0.068)
Returns: 1d +0.5% | 5d -1.0% | 1m -1.0% | 3m -10.9%
52-week range: 21.84 - 37.18 (now 7.1% of the way up)
Volatility: ATR(14) 0.54 (2.3% of price) | annualised 20d 36.2%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 117.86B
Valuation: trailing P/E 16.04 | forward P/E 16.48 | P/B 9.23 | PEG n/a
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
Price target: mean 30.77 (+34.2% vs last close), range 26.10 - 35.00
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

- [Why Did Banking Stocks GS, JPM, BAC Surge To 52-Week Highs Today?](https://stocktwits.com/news-articles/markets/equity/why-did-banking-stocks-gs-jpm-bac-surge-to-52-week-highs-today/cZZ2phOR7q6)  
  <sub>Stocktwits, 8 hours ago</sub>  
  GS stock led the climb among banking stocks, surging more than 9% after its record Q2 results triggered a buy-in. JPM stock rose 2.5% after its results surged...
- [JPMorgan Preferreds: The Temptation Of A 54% Redemption Upside (NYSE:JPM.PR.M)](https://seekingalpha.com/article/4949766-jp-morgan-preferreds-the-temptation-of-a-54-percent-redemption-upside)  
  <sub>Seeking Alpha, 48 minutes ago</sub>  
  Summary. JPMorgan Chase is unlikely to redeem its publicly traded preferreds despite their discounts to par and recent Series KK redemption. JPM's Series KK...
- [JPMorgan Chase & Co. $JPM Stock Position Lessened by Royal London Asset Management Ltd.](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-position-lessened-by-royal-london-asset-management-ltd-2026-09-25/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Royal London Asset Management Ltd. trimmed its position in shares of JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 1.4% in the second quarter,...
- [Here’s How Much You Would Have Made Owning JPMorgan Chase Stock In The Last 20 Years](https://www.benzinga.com/news/26/09/61987404/here-s-how-much-you-would-have-made-owning-jpmorgan-chase-stock-last-20-years)  
  <sub>Benzinga, 16 hours ago</sub>  
  JPMorgan Chase (NYSE:JPM) has outperformed the market over the past 20 years by 1.15% on an annualized basis producing an average annual return of 10.29%.
- [JPM261002P00340000 Interactive Stock Chart | JPM Oct 2026 340.000 put Stock](https://finance.yahoo.com/chart/JPM261002P00340000)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [J.P. Morgan backs a roughly $200 million forest plan in Paraguay, pairing timber with restoration.](https://www.stocktitan.net/news/JPM/office-of-the-president-of-the-republic-of-paraguay-and-j-p-morgan-ldbinplc7zm1.html)  
  <sub>Stock Titan, 20 hours ago</sub>  
  Grupo Robinson will contribute local knowledge, while the partners aim to process timber locally; capital deployment is expected to begin in early 2027.
- [Why Is PYPL Stock Surging Nearly 15% Overnight?](https://stocktwits.com/news-articles/markets/equity/why-is-pypl-stock-surging-nearly-15-overnight/cZZ2Ah2R7Ab)  
  <sub>Stocktwits, 2 hours ago</sub>  
  The payments giant has reportedly received a $53 billion buyout offer, a premium of more than 27% from the last close.
- [JPMorgan Chase & Co. $JPM Shares Sold by Manchester Financial Inc.](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-shares-sold-by-manchester-financial-inc-2026-09-25/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Manchester Financial Inc. lessened its holdings in shares of JPMorgan Chase & Co. (NYSE:JPM) by 73.2% in the second quarter, according to its most recent...
- [JP Morgan Chase & Co. (JPM) Stock Forecasts](https://ca.finance.yahoo.com/research/reports/MS_0P0000031C_AnalystReport_1790275518000)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [J.P. Morgan will serve as bank for MetaOptics' U.S. trading program. No new shares will be issued.](https://www.stocktitan.net/news/MOTLY/meta-optics-ltd-establishes-american-depositary-receipt-adr-ktqggbiv4j32.html)  
  <sub>Stock Titan, 15 hours ago</sub>  
  Ordinary shares stay on Singapore's SGX Catalist board; ADSs will trade on OTCQX, with no material impact expected for existing shareholders.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 339.52 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 351.08 (-3.3%), 50d 353.27 (-3.9%), 200d 321.24 (+5.7%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -3.659 vs signal -1.759 (histogram -1.900)
Returns: 1d +0.3% | 5d -2.9% | 1m -4.8% | 3m +3.2%
52-week range: 282.84 - 365.18 (now 68.8% of the way up)
Volatility: ATR(14) 6.53 (1.9% of price) | annualised 20d 17.9%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 902.52B
Valuation: trailing P/E 14.55 | forward P/E 13.59 | P/B 2.55 | PEG 1.57
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
Price target: mean 374.24 (+10.2% vs last close), range 305.00 - 436.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

```text
Last 180 days: bought 969,320 shares in 22 transaction(s) | sold 230,236 shares in 19
Net: +739,084 shares (+7.7% of insider holdings) | insiders hold 10,393,508 shares
Distinct insiders: 0 buying, 10 selling
Sales — weak evidence on their own; often scheduled 10b5-1 plans, tax on vesting, or diversification:
  - 2026-09-10 LEOPOLD ROBIN (Officer): 2,500 shares, 882.03K
  - 2026-08-11 LEOPOLD ROBIN (Officer): 2,500 shares, 903.52K
  - 2026-06-22 FRIEDMAN STACEY R. (General Counsel): 5,467 shares, 1.81M
  - 2026-05-20 FRIEDMAN STACEY R. (General Counsel): 5,468 shares, 1.64M
(11 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
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

- [Eli Lilly (LLY) Stock Is Up, What You Need To Know](https://finance.yahoo.com/healthcare/articles/eli-lilly-lly-stock-know-215258724.html)  
  <sub>Yahoo Finance, 17 hours ago</sub>  
  Shares of global pharmaceutical company Eli Lilly (NYSE:LLY) jumped 3.1% in the afternoon session after The U.S. Food and Drug Administration approved Eli...
- [Eli Lilly (LLY) Shares Just Moved, So What Is Driving Attention Now?](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/eli-lilly-lly-shares-just-moved-so-what-is-driving-attention)  
  <sub>Simply Wall Street, 4 hours ago</sub>  
  Eli Lilly (LLY) just secured U.S. FDA approval for Onswik, a once weekly basal insulin for adults with type 2 diabetes, an update that quickly drew investor...
- [Can Eli Lilly Stock Catch Up To Rivals It Outgrows?](https://www.trefis.com/stock/lly/articles/616445/can-eli-lilly-stock-catch-up-to-rivals-it-outgrows/2026-09-24)  
  <sub>Trefis, 20 hours ago</sub>  
  Eli Lilly (LLY) grew revenue 49.6% over the last twelve months, the fastest of the six companies in its peer group. It also runs the group's widest...
- [S&P 500, Nasdaq And Dow Close At Record Highs Amid Positive Reports Of US-Iran Ceasefire Negotiations — IBM, SNOW, CZR, AKTX, LLY In Focus Stocktwits](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-and-dow-close-at-record-highs-amid-positive-reports-of-us-iran-ceasefire-negotiations-ibm-snow-czr-aktx-lly-in-focus/cZgiu45Ret7)  
  <sub>Stocktwits, 6 hours ago</sub>  
  The S&P 500 rose 0.6%, and the Dow Jones gained 0.1%, while the Nasdaq 100 added 0.6%. Oil prices and Treasury yields eased as investors hoped for a...
- [91-year-old investor sees healthcare titan doubling in 3 years](https://www.thestreet.com/investing/stocks/lly-eli-lilly-stock-billionaire-investor-ken-langone-says-lly-could-hit-2000-share-price-3-to-4-years)  
  <sub>TheStreet, 7 hours ago</sub>  
  Billionaire Home Depot co-founder Ken Langone has held Lilly stock since 1977. Here's where he thinks it's going.
- [Viking Therapeutics Soared After Its Latest GLP-1 Data. Is It Too Late to Buy?](https://www.theglobeandmail.com/investing/markets/stocks/LLY-N/pressreleases/4795918/viking-therapeutics-soared-after-its-latest-glp-1-data-is-it-too-late-to-buy/)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [Nektar Therapeutics stock rises on $90M jury verdict vs Lilly](https://www.investing.com/news/stock-market-news/nektar-therapeutics-stock-rises-on-90m-jury-verdict-vs-lilly-4917615)  
  <sub>Investing.com, 2 hours ago</sub>  
  Investing.com -- Nektar Therapeutics (NASDAQ:NKTR) shares rose 3.6% in premarket trading Friday following a jury verdict awarding the company $90 million in...
- [Structure Therapeutics Inc. (GPCR) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GPCR/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Find the latest Structure Therapeutics Inc. (GPCR) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Explore the top gainers and losers within the S&P500 index in today's session.](https://www.chartmill.com/news/GDDY/Chartmill-55304-Explore-the-top-gainers-and-losers-within-the-SP500-index-in-todays-session)  
  <sub>ChartMill, 23 hours ago</sub>  
  Curious about the top performers within the S&P500 index in the middle of the day on Thursday? Dive into the list of today's session's top gainers and...
- [AbbVie vs. Eli Lilly: Which Star Pharma Stock Is a Better Buy in 2026?](https://www.fool.com/coverage/better-buy/2026/09/24/abbvie-vs-eli-lilly-which-star-pharma-stock-is-a-better-buy-in-2026/)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  Choosing between AbbVie (ABBV +0.01%) and Eli Lilly and Co (LLY +2.69%) requires weighing established income against explosive growth.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,164.66 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 1,149.87 (+1.3%), 50d 1,177.04 (-1.1%), 200d 1,070.00 (+8.8%); 50d above 200d
Momentum: RSI(14) 50.4 | MACD -4.469 vs signal -9.099 (histogram 4.630)
Returns: 1d -1.5% | 5d +1.0% | 1m -2.1% | 3m -3.6%
52-week range: 714.59 - 1,280.34 (now 79.6% of the way up)
Volatility: ATR(14) 32.46 (2.8% of price) | annualised 20d 19.1%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.04T
Valuation: trailing P/E 39.11 | forward P/E 24.50 | P/B 30.65 | PEG 1.14
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
Price target: mean 1,325.39 (+13.8% vs last close), range 930.00 - 1,600.00
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

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 516.18 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 500.04 (+3.2%), 50d 475.81 (+8.5%), 200d 432.06 (+19.5%); 50d above 200d
Momentum: RSI(14) 63.2 | MACD 6.782 vs signal 7.551 (histogram -0.769)
Returns: 1d +3.7% | 5d +4.5% | 1m +4.0% | 3m +38.4%
52-week range: 352.83 - 542.07 (now 86.3% of the way up)
Volatility: ATR(14) 11.64 (2.3% of price) | annualised 20d 25.2%
Volume: 0.74x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 3.83T
Valuation: trailing P/E 28.72 | forward P/E 21.80 | P/B 8.67 | PEG 1.62
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
Price target: mean 577.26 (+11.8% vs last close), range 440.00 - 870.00
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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data unreachable: The read operation timed out

### Nvidia (NVDA) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [NVIDIA’s Next AI Chip Ramp Could Open the Door to Another Major Stock Move](https://www.marketbeat.com/articles/nvidias-next-ai-chip-ramp-could-open-the-door-to-another-major-stock-move/)  
  <sub>MarketBeat, 1 hour ago</sub>  
  NVIDIA's NASDAQ: NVDA forecast to double its chip volume next year strengthens an already bullish growth outlook for the company and its stock.
- [A Ferrari Doesn’t Hold Value As Well As An NVIDIA Corporation (NVDA) GPU, According To Jim Cramer](https://finance.yahoo.com/markets/stocks/articles/ferrari-doesn-t-hold-value-100450518.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  NVIDIA Corporation (NASDAQ:NVDA) continues to be one of Cramer's top stocks due to the key role that the firm is playing in the AI rollout.
- [SNDK, NVDA, SKHY, ASML Stocks Extend Slide Overnight As China’s Chip Challenge Rattles Investors](https://stocktwits.com/news-articles/markets/equity/sndk-nvda-skhy-asml-stocks-extend-slide-overnight-amid-china-ai-challenge-tech-rotation/cZZCeckR766)  
  <sub>Stocktwits, 5 hours ago</sub>  
  The company posted a net loss of $228.22 million, or a diluted loss of $0.95 per share. On an adjusted basis, Navitas reported a second-quarter EPS loss of...
- [This Magnificent Seven Stock Could Deliver Outsized Returns Over the Next 5 Years](https://247wallst.com/investing/2026/09/25/this-magnificent-seven-stock-could-deliver-outsized-returns-over-the-next-5-years/)  
  <sub>24/7 Wall St., 39 minutes ago</sub>  
  NVDA trades at just 21x forward earnings despite 106% year-over-year revenue growth, 75% gross margins, and a 92% ROIC, and that mismatch is what drives the...
- [Nvidia Raised Its Dividend 2,400%, but a $10,000 Investment Still Pays Just $44 a Year](https://www.fool.com/investing/2026/09/25/nvidia-raised-its-dividend-2400-but-a-10000-invest/)  
  <sub>The Motley Fool, 6 hours ago</sub>  
  Nvidia (NVDA +0.28%) stock's run throughout the artificial intelligence (AI) revolution is the kind of story people talk about like folklore.
- [Nvidia Stock Rises as Elon Musk Reveals Huge New AI Chip Plans](https://www.tradingview.com/news/gurufocus:340da4c15094b:0-nvidia-stock-rises-as-elon-musk-reveals-huge-new-ai-chip-plans/)  
  <sub>TradingView, 2 hours ago</sub>  
  Nvidia NASDAQ:NVDA shares climbed about 1% in early Friday trading as SpaceX outlined plans to add hundreds of thousands of Nvidia processors to its...
- [Elon Musk Makes Massive Nvidia Move at SpaceX](https://finance.yahoo.com/technology/ai/articles/elon-musk-makes-massive-nvidia-130112892.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  This article first appeared on GuruFocus. Elon Musk is preparing another massive expansion of AI computing capacity, saying xAI's Colossus 2 cluster could...
- [Nvidia CEO Jensen Huang Says US Companies Should 'Absolutely' Use Chinese AI Models Despite Bessent’s Sanctions Warning](https://stocktwits.com/news-articles/markets/equity/nvda-jensen-huang-american-companies-absolutely-use-chinese-ai-models-bessent-sanctions-threat/cZZm0d1R7wU)  
  <sub>Stocktwits, 3 hours ago</sub>  
  Nvidia Corp. (NVDA) CEO Jensen Huang on Wednesday broke away from Trump administration officials' increasingly hardline stance against Chinese AI models,...
- [NVIDIA Corporation $NVDA Stock Sold by Montag A & Associates Inc.](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-sold-by-montag-a-associates-inc-2026-09-25/)  
  <sub>MarketBeat, 8 hours ago</sub>  
  Montag A & Associates Inc. reduced its holdings in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 2.1% in the 2nd quarter, according to the...
- [AMD vs. Nvidia: Which AI Stock Is the Better Buy?](https://finance.yahoo.com/markets/stocks/articles/amd-vs-nvidia-ai-stock-035909345.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  Advanced Micro Devices, Inc. (NASDAQ:AMD) crossed $1 trillion in market value on September 21 after closing roughly 187% higher for 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 224.41 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 221.72 (+1.2%), 50d 215.96 (+3.9%), 200d 199.47 (+12.5%); 50d above 200d
Momentum: RSI(14) 54.5 | MACD 2.228 vs signal 1.905 (histogram 0.323)
Returns: 1d -0.1% | 5d +1.0% | 1m +7.0% | 3m +16.6%
52-week range: 165.17 - 235.74 (now 83.9% of the way up)
Volatility: ATR(14) 5.87 (2.6% of price) | annualised 20d 32.3%
Volume: 0.25x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.42T
Valuation: trailing P/E 28.37 | forward P/E 14.31 | P/B 23.66 | PEG 0.48
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
Price target: mean 327.70 (+46.0% vs last close), range 180.00 - 515.00
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

- [Novo Nordisk A/S (NVO) is Attracting Investor Attention: Here is What You Should Know](https://finance.yahoo.com/markets/stocks/articles/novo-nordisk-nvo-attracting-investor-120004743.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Novo Nordisk (NVO) has been one of the most searched-for stocks on Zacks.com lately. So, you might want to look at some of the facts that could shape the...
- [4 stocks to watch on Friday: LION, NKE, TWLO, NVO (SPX:)](https://seekingalpha.com/news/4647107-4-stocks-to-watch-on-friday-lion-nke-twlo-nvo)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Stock index futures were higher on Friday while Treasury yields fell as investors focused on talks around reopening the Strait of Hormuz.
- [Novo Nordisk (NYSE: NVO) Heads For Worst Week In Six Months As NYSE Listing Talks And Singapore Drug Approval Fail To Reassure Investors](https://www.foreignpolicyjournal.com/2026/09/25/novo-nordisk-nyse-nvo-heads-for-worst-week-in-six-months-as-nyse-listing-talks-and-singapore-drug-approval-fail-to-reassure-investors/)  
  <sub>www.foreignpolicyjournal.com, 2 hours ago</sub>  
  Shares of Novo Nordisk (NYSE: NVO) are on course for their steepest weekly decline since late February, with the stock down 12% over the course of the week.
- [HIMS Stock Gained Nearly 6% On Wednesday — Barclays Sees Breakout Potential After Novo Partnership](https://stocktwits.com/news-articles/markets/equity/hims-stock-gains-nearly-6-percent-as-barclays-sees-breakout-potential-after-novo-partnership/cZKK7ffR7eJ)  
  <sub>Stocktwits, 16 hours ago</sub>  
  Shares of Hims & Hers Health (HIMS) gained nearly 6% in afternoon trading on Wednesday after Barclays turned more bullish on the telehealth company.
- [AbbVie vs. Novo Nordisk: Which Drug Giant Stock Is a Better Buy in 2026?](https://www.theglobeandmail.com/investing/markets/stocks/NVO-N/pressreleases/4788519/abbvie-vs-novo-nordisk-which-drug-giant-stock-is-a-better-buy-in-2026/)  
  <sub>The Globe and Mail, 18 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [Novo signs up to $1.3B deal for Nanexa drug-delivery technology (NVO:NYSE)](https://seekingalpha.com/news/4646973-novo-signs-up-to-13b-deal-for-nanexa-drug-delivery-technology)  
  <sub>Seeking Alpha, 8 hours ago</sub>  
  Novo Nordisk (NVO) signs up to €1.165B deal with Nanexa for PharmaShell drug-delivery tech for obesity & diabetes peptides.
- [Novo Nordisk (NVO) Sets Pipeline Sales Target Above $23 Billion By 2035](https://finance.yahoo.com/healthcare/articles/novo-nordisk-nvo-sets-pipeline-211642699.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Novo Nordisk (NYSE:NVO) outlined new long term growth ambitions and patent transition plans for semaglutide in a recent investor update.
- [LLY Stock Climbs As Oral GLP-1 Pill Beats Novo Nordisk, AstraZeneca’s Therapies In Diabetes Trials](https://stocktwits.com/news-articles/markets/equity/lly-stock-climbs-as-oral-glp-1-pill-crushes-rivals-in-diabetes-trials/cZ0vSJmR7bG)  
  <sub>Stocktwits, 21 hours ago</sub>  
  Lilly's Foundayo outperformed existing treatments on blood sugar control and weight loss in type 2 diabetes patients in three late-stage trials.
- [NVO Sep 2026 35.000 call (NVO260925C00035000) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/NVO260925C00035000/)  
  <sub>Yahoo Finance UK, 22 hours ago</sub>  
  Find the latest NVO Sep 2026 35.000 call (NVO260925C00035000) stock quote, history, news and other vital information to help you with your stock trading and...
- [South Korea's KOSPI, S&P 500, Gold Sink On US-Iran Tensions, But Bitcoin Holds $68K Floor](https://stocktwits.com/news-articles/markets/cryptocurrency/kospi-s-and-p-500-gold-sink-on-us-iran-tensions-but-bitcoin-holds/cZd9fmeRI5O)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Bitcoin held above $68000 even as KOSPI dropped more than 10%, U.S. indices closed lower, and gold shed gains.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.62 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 43.12 (-10.5%), 50d 45.80 (-15.7%), 200d 45.93 (-15.9%); 50d below 200d
Momentum: RSI(14) 30.0 | MACD -2.037 vs signal -1.516 (histogram -0.521)
Returns: 1d -0.0% | 5d -10.7% | 1m -18.2% | 3m -19.7%
52-week range: 35.29 - 63.98 (now 11.6% of the way up)
Volatility: ATR(14) 1.26 (3.3% of price) | annualised 20d 40.1%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 170.55B
Valuation: trailing P/E 9.58 | forward P/E 11.51 | P/B 5.00 | PEG 4.32
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
Price target: mean 46.41 (+20.2% vs last close), range 39.75 - 62.91
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

- [The Procter & Gamble Company (PG) latest stock news and headlines](https://uk.finance.yahoo.com/quote/PG/news/)  
  <sub>Yahoo Finance UK, 15 hours ago</sub>  
  The Procter & Gamble Company (PG) · 3 Stocks With Pricing Power When Inflation And Rates Stay High · 3 Unpopular Stocks Walking a Fine Line · 3 Dividend Kings...
- [P&G vs. Hershey: One Dividend Has a Major Advantage When Costs Surge](https://247wallst.com/investing/2026/09/25/pg-vs-hershey-one-dividend-has-a-major-advantage-when-costs-surge/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Both P&G and Hershey have paid dividends for decades, but one of them proved dangerously vulnerable when a single commodity turned against it,...
- [This Dividend Stock's Moat Is as Wide as It Gets. 3 Reasons to Buy and Hold It Forever.](https://www.fool.com/investing/2026/09/25/this-dividend-stocks-moat-is-as-wide-as-it-gets-3/)  
  <sub>The Motley Fool, 5 hours ago</sub>  
  Even among blue chip dividend stocks, Procter & Gamble (PG -1.16%) stands out for its competitive moat. It's the company behind popular consumer brands such...
- [Procter & Gamble (PG) Could Be 37% Overvalued On New Clinical Product Push](https://simplywall.st/stocks/us/household/nyse-pg/procter-gamble/news/procter-gamble-pg-could-be-37-overvalued-on-new-clinical-pro)  
  <sub>Simply Wall Street, 18 hours ago</sub>  
  Procter & Gamble (PG) just pushed two of its biggest personal care franchises further into clinical territory, rolling out Head & Shoulders HydraZinc...
- [Italy regulator closes P&G hair removal device probe after ad commitments By Reuters](https://www.investing.com/news/stock-market-news/italy-regulator-closes-pg-hair-removal-device-probe-after-ad-commitments-4916739)  
  <sub>Investing.com, 7 hours ago</sub>  
  ROME, Sept 25 (Reuters) - Italy's antitrust authority (AGCM) said on Friday it had closed its investigation into U.S. consumer goods maker Procter...
- [The public can access PG&E's results call online, and a replay will be available afterward.](https://www.stocktitan.net/news/PCG/pg-e-corporation-schedules-third-quarter-2026-earnings-release-and-o9en363sua5s.html)  
  <sub>Stock Titan, 17 hours ago</sub>  
  A toll-free replay will be available shortly after the call through Oct. 29, using code 92587; the webcast begins at 11 a.m. Eastern on Oct. 22.
- [These S&P500 stocks are the most active in today's session](https://www.chartmill.com/news/PCG/Chartmill-55313-These-SP500-stocks-are-the-most-active-in-todays-session)  
  <sub>ChartMill, 21 hours ago</sub>  
  Curious about the most active S&P500 stocks in today's session? Get insights into the stocks that are leading the way in terms of trading volume and market...
- [Procter & Gamble stock heads into the open after a 0.4 percent gain](https://www.ad-hoc-news.de/boerse/news/vorboerse/procter-and-gamble-stock-heads-into-the-open-after-a-0-4-percent-gain/70180886)  
  <sub>AD HOC NEWS, 11 hours ago</sub>  
  At the close on September 24, 2026, Procter & Gamble stock had gained 0.4 percent on the NYSE; the S&P 500 slipped less than 0.1 percent.
- [CDs Offer Certainty. Dividend Stocks Offer Something Retirees May Need More](https://247wallst.com/investing/2026/09/24/cds-offer-certainty-dividend-stocks-offer-something-retirees-may-need-more/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  When a retiree compares a federally insured CD to a dividend stock that has raised its payout for 70 straight years, the choice turns on a factor most...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 145.55 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 145.96 (-0.3%), 50d 145.96 (-0.3%), 200d 147.53 (-1.3%); 50d below 200d
Momentum: RSI(14) 48.4 | MACD 0.246 vs signal 0.197 (histogram 0.049)
Returns: 1d -0.1% | 5d -0.6% | 1m +0.4% | 3m -2.3%
52-week range: 138.04 - 167.20 (now 25.8% of the way up)
Volatility: ATR(14) 2.21 (1.5% of price) | annualised 20d 14.1%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 338.33B
Valuation: trailing P/E 22.02 | forward P/E 19.67 | P/B 6.34 | PEG 3.79
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
Price target: mean 160.61 (+10.3% vs last close), range 143.00 - 186.00
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

- [Are Finance Stocks Lagging Royal Bank Of Canada (RY) This Year?](https://finance.yahoo.com/markets/stocks/articles/finance-stocks-lagging-royal-bank-124002155.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  Investors interested in Finance stocks should always be looking to find the best-performing companies in the group. Has Royal Bank (RY) been one of those...
- [Royal Bank of Canada stock rises Thursday, outperforms market](https://www.marketwatch.com/data-news/royal-bank-of-canada-stock-rises-thursday-outperforms-market-a9b0c98f-5d4c4ed0ad9b?mod=mw_quote_news)  
  <sub>MarketWatch, 19 hours ago</sub>  
  Shares of Royal Bank of Canada RY inched 0.27% higher to C$282.11 Thursday, in what proved to be an otherwise all-around poor trading session for the...
- [Royal Bank of Canada stock rises before the bell after a C$1.5 billion offering](https://www.ad-hoc-news.de/boerse/news/vorboerse/royal-bank-of-canada-stock-rises-before-the-bell-after-a-c-1-5-billion/70181507)  
  <sub>AD HOC NEWS, 10 hours ago</sub>  
  At the close on September 24, 2026, Royal Bank of Canada stock was quoted at C$282.45 in Toronto, while a C$1.5 billion subordinated debenture offering...
- [I Think These 3 Canadian Stocks Are Absolutely Best in Class for Dividends](https://www.moomoo.com/news/post/1000195768/i-think-these-3-canadian-stocks-are-absolutely-best-in)  
  <sub>Moomoo, 18 hours ago</sub>  
  Canadahas plenty of dividend stocks. However, there are some elite passive-income stocks that stand above the rest. They have exceptional assets,...
- [Rakuten Bank (TSE:5838) Stock Could Be 43% Undervalued On Equity Returns](https://finance.yahoo.com/markets/stocks/articles/rakuten-bank-tse-5838-stock-031203751.html)  
  <sub>Yahoo Finance, 12 hours ago</sub>  
  Rakuten Bank has delivered a very strong 150.6% return over the past 3 years, yet the current share price leaves an open question about whether that...
- [Royal Bank of Canada Notes Admission of Gbp 475,000,000 Floating Rate Senior Notes Due September 2027](https://www.marketscreener.com/news/royal-bank-of-canada-notes-admission-of-gbp-475-000-000-floating-rate-senior-notes-due-september-202-ce785adfd98df32d)  
  <sub>marketscreener.com, 20 hours ago</sub>  
  Royal Bank of Canada had the following transferable securities admitted to trading on the London Stock Exchange's main market: Royal Bank of Canada GBP...
- [US Inflation Likely To Hit 3-Year High In May, RBC Says: ‘Bad News For Consumers, Good News For Labor Market’](https://stocktwits.com/news-articles/markets/equity/us-inflation-likely-to-hit-3-year-high-in-may-rbc-says/cZ0HyqlRe6x)  
  <sub>Stocktwits, 19 hours ago</sub>  
  Higher energy prices will push headline inflation higher, according to RBC economists. The research arm of the bank expects core CPI, which excludes...
- [I Looked Past the 2.5% Yield, and Here’s What Else RBC Stock Offers](https://www.fool.ca/2026/09/24/i-looked-past-the-2-5-yield-and-heres-what-else-rbc-stock-offers/)  
  <sub>The Motley Fool Canada, 19 hours ago</sub>  
  Royal Bank of Canada (TSX: RY) stock offers investors more than just a 2.5% dividend yield. For giants like Royal Bank of Canada, or RBC, growth is slow and...
- [Royal Bank of Canada Dividend 2.49%: Can Canada’s Banking Leader Sustain Long-Term Income Growth?](https://kalkine.ca/news/general-news/royal-bank-of-canada-dividend-249-can-canadas-banking-leader-sustain-long-term-income-growth)  
  <sub>kalkine.ca, 6 hours ago</sub>  
  You are reading a free article with opinions that may differ from the recommendation given by Kalkine in its paid research reports.
- [Royal Bank of Canada stock falls 2.03 percent after record profit](https://www.ad-hoc-news.de/boerse/news/corporate-news/royal-bank-of-canada-stock-falls-2-03-percent-after-record-profit/70183047)  
  <sub>AD HOC NEWS, 5 hours ago</sub>  
  Royal Bank of Canada stock traded at CAD 281.35 on September 24, 2026, after a 2.03 percent decline. Q3 net income rose 11 percent to CAD 6.024 billion.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 200.29 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 204.89 (-2.2%), 50d 208.01 (-3.7%), 200d 185.58 (+7.9%); 50d above 200d
Momentum: RSI(14) 38.9 | MACD -1.946 vs signal -1.400 (histogram -0.546)
Returns: 1d +0.4% | 5d -1.5% | 1m -3.3% | 3m -1.3%
52-week range: 143.64 - 217.87 (now 76.3% of the way up)
Volatility: ATR(14) 3.19 (1.6% of price) | annualised 20d 16.6%
Volume: 0.15x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 277.29B
Valuation: trailing P/E 17.71 | forward P/E 15.76 | P/B 2.92 | PEG 2.26
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
Price target: mean 208.92 (+4.3% vs last close), range 184.04 - 226.46
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

- [TEVA260925P00049000 Interactive Stock Chart | TEVA Sep 2026 49.000 put Stock](https://finance.yahoo.com/chart/TEVA260925P00049000)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Teva Pharmaceutical Industries Ltd. (NYSE:TEVA) Short Interest Update](https://www.marketbeat.com/instant-alerts/options-teva-pharmaceutical-industries-ltd-nyse-teva-short-interest-update-2026-09-24/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  Teva Pharmaceutical Industries Ltd. (NYSE:TEVA - Get Free Report) was the recipient of a large increase in short interest in the month of September.
- [Netlist Bags Federal Circuit Win After Court Rejects Micron’s Patent Challenge](https://stocktwits.com/news-articles/markets/equity/netlist-bags-federal-circuit-win-rejects-micron-patent-challenge/cZRNkluR4xw)  
  <sub>Stocktwits, 12 hours ago</sub>  
  The U.S. Court of Appeals for the Federal Circuit upheld the validity of the patents in an opinion on Friday, saying Micron failed to prove unpatentability...
- [TEVA Sep 2026 40.500 call (TEVA260925C00040500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TEVA260925C00040500/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest TEVA Sep 2026 40.500 call (TEVA260925C00040500) stock quote, history, news and other vital information to help you with your stock trading...
- [Huntington’s Disease Market is Projected to Grow at 14% CAGR by 2036 Owing to Advancements in Gene and RNA-Based Therapies | DelveInsight](https://www.barchart.com/press-releases/4788875/huntingtons-disease-market-is-projected-to-grow-at-14-cagr-by-2036-owing-to-advancements-in-gene-and-rna-based-therapies-delveinsight)  
  <sub>Barchart.com, 18 hours ago</sub>  
  The market dynamics for Huntington's Disease are witnessing significant growth driven by the advancements in gene and RNA-based therapies, rising disease...
- [Medincell stock declines 2% following a rally sequence](https://www.ideal-investisseur.fr/en/stock-news/medincell-stock-declines-2-following-a-rally-sequence/25844.html)  
  <sub>Idéal Investisseur, 1 hour ago</sub>  
  The Montpellier-based biopharmaceutical company is losing momentum this Friday, retreating three days after a notable rebound that had propelled it among...
- [TEVA Sep 2026 34.500 call (TEVA260925C00034500) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/TEVA260925C00034500/)  
  <sub>Yahoo Finance Singapore, 19 hours ago</sub>  
  Find the latest TEVA Sep 2026 34.500 call (TEVA260925C00034500) stock quote, history, news and other vital information to help you with your stock trading...
- [Alvotech (NASDAQ:ALVO) Shares Up 3.5% - Here's What Happened](https://www.marketbeat.com/instant-alerts/price-alvotech-nasdaq-alvo-shares-up-35-heres-what-happened-2026-09-24/)  
  <sub>MarketBeat, 23 hours ago</sub>  
  Alvotech (NASDAQ:ALVO) Stock Price Up 3.5% - Should You Buy?
- [TEVA Sep 2026 35.500 call (TEVA260925C00035500) interactive stock chart](https://au.finance.yahoo.com/quote/TEVA260925C00035500/chart/)  
  <sub>Yahoo Finance Australia, 18 hours ago</sub>  
  Interactive chart for TEVA Sep 2026 35.500 call (TEVA260925C00035500) – analyse all of the data with a huge range of indicators.
- [TEVA Sep 2026 37.500 put (TEVA260925P00037500) interactive stock chart – Yahoo Finance](https://sg.finance.yahoo.com/quote/TEVA260925P00037500/chart/)  
  <sub>Yahoo Finance Singapore, 18 hours ago</sub>  
  Interactive chart for TEVA Sep 2026 37.500 put (TEVA260925P00037500) – analyse all of the data with a huge range of indicators.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 39.10 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 37.94 (+3.1%), 50d 36.10 (+8.3%), 200d 33.44 (+16.9%); 50d above 200d
Momentum: RSI(14) 56.9 | MACD 0.954 vs signal 0.884 (histogram 0.070)
Returns: 1d -2.8% | 5d +0.3% | 1m +3.1% | 3m +17.7%
52-week range: 18.34 - 40.22 (now 94.9% of the way up)
Volatility: ATR(14) 1.24 (3.2% of price) | annualised 20d 35.0%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 45.60B
Valuation: trailing P/E 65.17 | forward P/E 12.85 | P/B 5.88 | PEG n/a
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
Price target: mean 44.00 (+12.5% vs last close), range 40.00 - 50.00
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

- [XOM|Exxon Mobil Corp|Price:162.140|Chg%:+0.910](https://www.tradingkey.com/markets/stocks/xom)  
  <sub>TradingKey, 11 hours ago</sub>  
  Valero shares declined due to profit-taking and valuation re-evaluations by investors. • The company reported an annual revenue of $115.97B and net profit of...
- [ExxonMobil Corporation (NYSE:XOM) Stock Has Average Target Price of $167.30 According to Brokerages](https://www.marketbeat.com/instant-alerts/consensus-exxonmobil-corporation-nyse-xom-stock-has-average-target-price-of-16730-according-to-brokerages-2026-09-25/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  ExxonMobil Corporation (NYSE:XOM - Get Free Report) has been given an average rating of "Hold" by the twenty-five research firms that are covering the...
- [MRNA, LNTH, BMY, CAPR, RARE Stocks In Focus — These FDA Decisions Could Shape August Trading](https://stocktwits.com/news-articles/markets/equity/mrna-lnth-bmy-capr-rare-stocks-in-focus-these-fda-decisions-could-shape-august-trading/cZoTYS7RJ30)  
  <sub>Stocktwits, 5 hours ago</sub>  
  Moderna is seeking approval for mRNA-1010, its experimental mRNA-based seasonal flu vaccine for adults 50 and older.Capricor is seeking full approval for...
- [Did ExxonMobil’s (XOM) 2076 Floating‑Rate Notes Just Quietly Redefine Its Long‑Term Funding Playbook?](https://finance.yahoo.com/energy/articles/did-exxonmobil-xom-2076-floating-161430852.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Earlier this week, ExxonMobil Holdings Corporation completed a US$185.883 million fixed‑income offering of senior unsecured floating rate notes due...
- [ExxonMobil Stock And Energy Names Worth Watching As Oil Volatility Builds](https://simplywall.st/stocks/us/energy/nyse-eqt/eqt/news/exxonmobil-stock-and-energy-names-worth-watching-as-oil-vola)  
  <sub>Simply Wall Street, 17 hours ago</sub>  
  Energy markets feel less like a spreadsheet and more like a pressure cooker right now, with the U.S.-Iran conflict, a looming Senate War Powers vote and...
- [Exclusive | Exxon Is Nearing Preliminary Deal to Invest in Venezuela’s Oil Fields](https://www.wsj.com/business/energy-oil/exxon-is-nearing-a-preliminary-deal-to-invest-in-venezuelas-oil-fields-8c02126b)  
  <sub>WSJ, 9 hours ago</sub>  
  U.S. oil company is negotiating a potential return to the Latin American country 19 years after its exit.
- [Why Xometry Stock Is Falling Today](https://www.quiverquant.com/news/Why+Xometry+Stock+Is+Falling+Today)  
  <sub>Quiver Quantitative, 18 hours ago</sub>  
  Xometry, Inc. (XMTR) is down 7.3% today. Here is some analysis on what might have caused this price movement. Analysis: The most likely explanation is a mix...
- [AI Supply Chains Are The Next Thing. Two Stocks Aim To Benefit.](https://www.investors.com/news/xmtr-stock-buy-point-avnet-xometry-ai-supply-chains/)  
  <sub>Investor's Business Daily, 19 hours ago</sub>  
  Both Xometry and Avnet are using artificial intelligence to ease bottlenecks in supply chains. XMRT stock tried to break out on Thursday.
- [ExxonMobil (NYSE:XOM) Stock Price Expected to Rise, The Goldman Sachs Group Analyst Says](https://www.marketbeat.com/instant-alerts/analyst-exxonmobil-nyse-xom-stock-price-expected-to-rise-the-goldman-sachs-group-analyst-says-2026-09-24/)  
  <sub>MarketBeat, 18 hours ago</sub>  
  The Goldman Sachs Group raised their price target on shares of ExxonMobil from $168.00 to $169.00 and gave the company a "neutral" rating in a report on...
- [Valero Energy Corp. stock outperforms competitors on strong trading day](https://www.marketwatch.com/data-news/valero-energy-corp-stock-outperforms-competitors-on-strong-trading-day-0276bc9b-42e0d45c4c2a?mod=goog_fin_scmw)  
  <sub>MarketWatch, 19 hours ago</sub>  
  advanced 1.87% to $382.86 Thursday, on what proved to be an all-around dismal trading session for the stock market, with the S&P 500 Index.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 161.51 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 162.53 (-0.6%), 50d 159.44 (+1.3%), 200d 148.00 (+9.1%); 50d above 200d
Momentum: RSI(14) 50.4 | MACD 0.609 vs signal 1.260 (histogram -0.651)
Returns: 1d -0.4% | 5d -1.2% | 1m +2.1% | 3m +18.3%
52-week range: 110.64 - 171.47 (now 83.6% of the way up)
Volatility: ATR(14) 3.71 (2.3% of price) | annualised 20d 27.0%
Volume: 0.17x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 664.11B
Valuation: trailing P/E 20.79 | forward P/E 14.58 | P/B 2.56 | PEG 1.38
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
Price target: mean 172.55 (+6.8% vs last close), range 142.00 - 200.00
Recent rating changes:
  - 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - 2026-08-19 Morgan Stanley: main, Overweight -> Overweight
  - 2026-08-17 Barclays: main, Overweight -> Overweight
  - 2026-08-07 TD Cowen: main, Buy -> Buy
  - 2026-08-04 Freedom Broker: up, Sell -> Hold
  - 2026-07-28 B of A Securities: down, Buy -> Neutral
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

> Neutral call due to lack of news, mixed technicals, flat fund flows, and neutral fundamentals.

**Main reasons it gave:**
- No news or macro surprise in the past 24h
- Technicals: price above 50‑day (28.32) and 200‑day (27.10) SMAs but below 20‑day SMA (28.88), RSI 45.7, MACD histogram -0.099
- Fund flows flat (share count unchanged) indicating neutral demand
- Fund fundamentals neutral: yield 3.1%, expense ratio 0.85%, 46% cash, three‑year return 13.8% per year

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.37 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 28.88 (-1.8%), 50d 28.32 (+0.2%), 200d 27.10 (+4.7%); 50d above 200d
Momentum: RSI(14) 45.7 | MACD 0.027 vs signal 0.126 (histogram -0.099)
Returns: 1d -0.6% | 5d +0.8% | 1m -0.8% | 3m +5.9%
52-week range: 25.44 - 29.49 (now 72.3% of the way up)
Volatility: ATR(14) 0.28 (1.0% of price) | annualised 20d 14.1%
Volume: 0.34x the 20-day average
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
Three-year record: +13.8% a year | beta to the market 0.35
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
Shares outstanding: 27.60M | fund size: 783.01M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Treasury yields rose modestly across the curve (+0.11 to +0.21) with no policy surprise
- Technicals show price below 20‑day, 50‑day, and 200‑day SMAs and RSI 25.1, but no decisive break on volume
- Fund flows flat: share count -0.1% over 7 days, indicating no strong demand shift
- Fund basics unchanged: yield 5.9%, credit quality BB/B stable

<details><summary><b>News</b> — score +0.00</summary>

- [iShares iBoxx $ High Yield Corporate Bond ETF (HYG) options chain](https://au.finance.yahoo.com/quote/HYG/options/?date=1793318400&straddle=false&type=all)  
  <sub>Yahoo Finance Australia, 19 hours ago</sub>  
  View the basic HYG option chain and compare options of iShares iBoxx $ High Yield Corporate Bond ETF on Yahoo Finance.
- [Exchange Traded Funds Top 10 Volume Leaders](https://www.moomoo.com/news/post/1000198314/exchange-traded-funds-top-10-volume-leaders)  
  <sub>Moomoo, 15 hours ago</sub>  
  NET% VOL STOCK (Symbol) LAST CHG CHG 100s Direxion Semicon Br 3x SOXS 33.63 -0.03 -0.09 83623490 iShares iBoxx $ HY Cp Bd HYG 77.89 -0.21 -0.27 74913084 G.
- [S&P 500 Divergence Deepens as Treasury Yields Surge](https://mottcapitalmanagement.com/sp-500-divergence-bond-volatility/)  
  <sub>Mott Capital Management, 17 hours ago</sub>  
  The S&P 500 and the equal-weight ETF have diverged significantly. Over the past year, the two-month moves in SPY and RSP have lined up less and less,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 77.74 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 78.76 (-1.3%), 50d 79.24 (-1.9%), 200d 79.97 (-2.8%); 50d below 200d
Momentum: RSI(14) 25.1 | MACD -0.377 vs signal -0.292 (histogram -0.085)
Returns: 1d -0.2% | 5d -1.0% | 1m -2.7% | 3m -2.6%
52-week range: 77.74 - 81.28 (now 0.0% of the way up)
Volatility: ATR(14) 0.26 (0.3% of price) | annualised 20d 4.7%
Volume: 0.40x the 20-day average
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
Share count change: 1 week: -0.1% (-12.12M) over 7d
Shares outstanding: 206.01M | fund size: 16.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Treasury yields rose modestly (+0.11 to +0.21) with no surprise, keeping the yield curve normal
- Technical indicators show a downtrend (price below 20‑day SMA, RSI 33.7) but no decisive break on heavy volume
- CFTC positioning shows net short 19.6% with a +6% increase, indicating modest bearish sentiment but not extreme
- Analyst coverage thin (1.7% of fund) despite strong buy rating, limiting impact on overall view
- Fund fundamentals are moderate (P/E 17.3, 3‑year return +18.4%/yr) with no major shift

<details><summary><b>News</b> — score +0.00</summary>

- [Bond liquidation wrecks small caps. Here's how bad some traders see it getting](https://www.cnbc.com/amp/2026/09/24/bond-liquidation-wrecks-small-caps-heres-how-bad-some-traders-see-it-getting.html)  
  <sub>CNBC, 21 hours ago</sub>  
  While the S&P 500 powers through rising bond yields and higher crude oil prices, one section of the U.S. stock market is falling behind.
- [Exchange-Traded Funds Mixed, US Equities Decline After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-mixed-us-171353361.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded fund IWM fell and IVV edged higher. Actively traded Invesco QQQ Trust (QQQ) added 0.1%.
- [Bond Market Flashes a Warning Not Seen Since 2007](https://247wallst.com/investing/2026/09/24/bond-market-flashes-a-warning-not-seen-since-2007/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Treasury yields just hit levels the bond market has not seen since before the financial crisis, and the pain is spreading fast into corners of the market...
- [S&P 500 Erases Losses as US, Iran Reportedly Discuss Hormuz Deal: Stock Market Today](https://www.tradingview.com/news/benzinga:8276f3b88094b:0-s-p-500-erases-losses-as-us-iran-reportedly-discuss-hormuz-deal-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 clawed back most of its morning decline at midday Thursday after sources told Reuters that U.S. and Iranian negotiators meeting in New York are...
- [Small Caps Crushed: IWM Sees $3.3B Outflow as Treasury Yields Surge - iShares Russell 2000 Index Fund (AR](https://www.benzinga.com/etfs/sector-etfs/26/09/61982431/small-caps-crushed-iwm-sees-3-3b-outflow-treasury-yields-surge)  
  <sub>Benzinga, 20 hours ago</sub>  
  IWM saw $3.3 billion in weekly outflows as the Russell 2000 fell 7.3% from mid-August, with rising Treasury yields adding pressure to small-cap stocks.
- [Small Caps Lose Ground as Rising Bond Yields Undermine Russell 2000 Rally](https://www.tekedia.com/small-caps-lose-ground-as-rising-bond-yields-undermine-russell-2000-rally/)  
  <sub>Tekedia, 8 hours ago</sub>  
  The US stock market's rally is increasingly splitting along size lines, with small-cap shares losing ground as rising Treasury yields and higher borrowing...
- [Form 4 iShares Russell 2000 ETF For: 24 September By Investing.com](https://in.investing.com/news/stock-market-news/form-4-ishares-russell-2000-etf-for-24-september-93CH-5605496)  
  <sub>Investing.com India, 22 hours ago</sub>  
  The Senior Autocallable Contingent Coupon Barrier Notes due September 27, 2032 Linked to the Worst-Performing of the iShares <sup>®</sup> Russell 2000 <sup>®</sup> ETF,...
- [Small-cap stocks lag as rising interest rates h...](https://pluang.com/en/news-feed/likuidasi-obligasi-bikin-saham-small-cap-tertekan-begini-parahnya)  
  <sub>Pluang, 21 hours ago</sub>  
  Small-cap stocks, represented by the Russell 2000 index, have fallen behind larger indexes like the S&P 500 and Nasdaq-100 in September due to rising...
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 281.37 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 288.58 (-2.5%), 50d 293.99 (-4.3%), 200d 275.68 (+2.1%); 50d above 200d
Momentum: RSI(14) 33.7 | MACD -3.763 vs signal -3.149 (histogram -0.614)
Returns: 1d -0.1% | 5d -1.0% | 1m -5.9% | 3m -6.2%
52-week range: 229.11 - 305.09 (now 68.8% of the way up)
Volatility: ATR(14) 3.45 (1.2% of price) | annualised 20d 12.7%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

```text
Fund type: Small Blend
What it holds: P/E 17.30 | P/B 2.13 | P/S 1.31 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +18.4% a year | beta to the market 1.24
Cost and size: expense ratio 0.19% | net assets 80.46B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: JFrog Ltd Ordinary Shares 0.3%, Moog Inc Class A 0.3%, BlackRock Cash Funds Treasury SL Agency 0.3%, UMB Financial Corp 0.3%, Glaukos Corp 0.3%
Sector mix: Healthcare 21.0%, Financial services 18.1%, Technology 13.8%, Industrials 13.2%
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

<details><summary><b>What analysts and big funds say</b> — score +0.01</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.01</summary>

```text
Rolled up from the 5 largest holdings, 1.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.2% above the current prices
Holdings read: FROG, MOG-A, XTSLA, UMBF, GKOS
Recent rating changes among them:
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - MOG-A: 2026-09-15 Guggenheim: init, ? -> Neutral
  - UMBF: 2026-09-14 UBS: init, ? -> Neutral
  - GKOS: 2026-09-22 Jefferies: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 19.6% of open interest (496,762 contracts)
Change on the week: +6.0% of open interest
Crowding: 30% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 79.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, modest outflows, fundamentals unchanged

**Main reasons it gave:**
- Treasury yields up 0.11‑0.21% across the curve, no rate surprise
- LQD net outflows of -0.7% (-$209.94M) over the week
- RSI 27.6 (oversold) but volume 0.47x 20‑day average, no decisive break
- Fund basics: yield 4.7%, credit quality A 46.6%/BBB 40.2%, 3‑yr return +4.6%/yr

<details><summary><b>News</b> — score +0.00</summary>

- [Bond Market Flashes a Warning Not Seen Since 2007](https://247wallst.com/investing/2026/09/24/bond-market-flashes-a-warning-not-seen-since-2007/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Treasury yields just hit levels the bond market has not seen since before the financial crisis, and the pain is spreading fast into corners of the market...
- [Daily ETF Flows: CORO Pulls In $4.2B](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-coro-pulls-210004066.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 16,352.50. 885,248.92. 1.85%.
- [BINC: Adding After The 2026 Rates Shock (NYSEARCA:BINC)](https://seekingalpha.com/article/4949749-binc-adding-after-the-2026-rates-shock)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  BlackRock's iShares Flexible Income Active ETF has demonstrated resilience in 2026, outperforming passive peers. Read more on BINC here.
- [This 8% Yield Bond ETF Bets Against Hurricanes, Earthquakes and Wildfires](https://247wallst.com/investing/etf/2026/09/24/this-8-yield-bond-etf-bets-against-hurricanes-earthquakes-and-wildfires/)  
  <sub>24/7 Wall St., 12 hours ago</sub>  
  Most bond investors bet on interest rates or corporate survival. A small corner of the fixed-income market takes a completely different wager, one where the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 102.83 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 104.83 (-1.9%), 50d 105.79 (-2.8%), 200d 108.62 (-5.3%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -0.665 vs signal -0.521 (histogram -0.144)
Returns: 1d -0.3% | 5d -1.8% | 1m -3.7% | 3m -6.1%
52-week range: 102.83 - 112.92 (now 0.0% of the way up)
Volatility: ATR(14) 0.58 (0.6% of price) | annualised 20d 7.2%
Volume: 0.47x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -0.7% (-209.94M) over 7d
Shares outstanding: 305.11M | fund size: 31.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No clear macro surprise, modest technical weakness, slight bearish insider positioning, stable fundamentals

**Main reasons it gave:**
- CFTC data shows net short 29.2% of 2‑year note with a +0.5% OI increase, indicating slight bearish pressure
- Crowding at the 95th percentile suggests extreme positioning, raising reversal risk
- Price below 20‑day, 50‑day, and 200‑day SMAs and RSI 31.9, showing weak technical momentum
- Yields rose modestly across the curve (+0.11 to +0.21) with no surprise, maintaining higher‑for‑longer environment
- Fund basics show AA‑rated credit quality and a 3.6% yield, indicating stable fundamentals

<details><summary><b>News</b> — score +0.00</summary>

- [4 No-Brainer ETFs I'm Buying if the Stock Market Crashes in 2026](https://www.theglobeandmail.com/investing/markets/markets-news/motley/4792374/4-no-brainer-etfs-i-m-buying-if-the-stock-market-crashes-in-2026/)  
  <sub>The Globe and Mail, 9 hours ago</sub>  
  Key Points. The State Street SPDR Portfolio S&P 500 Growth ETF encompasses about 140 of the fastest-growing companies in the S&P 500.
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  Find the latest iShares 20+ Year Treasury Bond ETF (TLT) stock quote, history, news and other vital information to help you with your stock trading and...
- [Vanguard's All-World ETF Extends Inflow Streak as Price Hovers Near Record](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-s-all-world-etf-extends-inflow-streak-as-price-hovers-near-record/70182206)  
  <sub>AD HOC NEWS, 8 hours ago</sub>  
  Vanguard's FTSE All-World UCITS ETF led European ETF inflows for a second week, drawing €429.8 million, as shares trade near their 52-week high.
- [Vanguard's All-World ETF Pulls In €429.8 Million in a Single Week as Tech Titans Tighten Their Gri](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-s-all-world-etf-pulls-in-429-8-million-in-a-single-week-as/70181562)  
  <sub>AD HOC NEWS, 10 hours ago</sub>  
  Vanguard's FTSE All-World ETF took €429.8 million in week 38, the most of any European ETF, as it trades 0.7% below its 52-week high.
- [Until yields bite growth, BofA sees a tech climax—and more bond pain](https://seekingalpha.com/news/4647093-until-yields-bite-growth-bofa-sees-a-tech-climax-and-more-bond-pain)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  BofA Global Research flags a 2020s regime shift: booming nominal GDP, falling long bonds.
- [Higher-for-longer is squeezing the weakest credits first, Apollo notes](https://seekingalpha.com/news/4647073-higher-for-longer-is-squeezing-the-weakest-credits-first-apollo-notes)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  The Federal Reserve's “higher for longer” stance is not landing evenly across corporate credit. Apollo's chief economist Torsten Slok argues the pressure is...
- [Vanguard's All-World ETF Climbs Back Toward Record High as Quarterly Payout Nears](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/vanguard-s-all-world-etf-climbs-back-toward-record-high-as-quarterly/70183787)  
  <sub>AD HOC NEWS, 3 hours ago</sub>  
  Vanguard FTSE All-World UCITS ETF trades near its 52-week high as investors await a USD 0.5434 per share quarterly distribution on September 30.
- [10-year Treasury yield holds near 5.17% as global bond selloff continues](https://invezz.com/au/news/2026/09/25/10-year-treasury-yield-holds-near-517percent-as-global-bond-selloff-continues/)  
  <sub>Invezz, 5 hours ago</sub>  
  The 10-year US Treasury yield was little changed at 5.17% on Friday, holding near its highest level since June 2007 as a global bond selloff extended into a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 81.16 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 81.45 (-0.4%), 50d 81.75 (-0.7%), 200d 82.31 (-1.4%); 50d below 200d
Momentum: RSI(14) 31.9 | MACD -0.190 vs signal -0.167 (histogram -0.023)
Returns: 1d +0.1% | 5d -0.1% | 1m -1.1% | 3m -1.3%
52-week range: 81.09 - 83.18 (now 3.1% of the way up)
Volatility: ATR(14) 0.11 (0.1% of price) | annualised 20d 2.1%
Volume: 0.27x the 20-day average
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
Three-year record: +3.9% a year | beta to the market 0.22
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.20</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 29.2% of open interest (4,433,736 contracts)
Change on the week: +0.5% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.20</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (11.24M) over 7d
Shares outstanding: 318.76M | fund size: 25.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, modest bullish analyst view (thin coverage), crowded long positioning with slight weekly decline, fundamentals stable.

**Main reasons it gave:**
- No macro surprise: Treasury yields rose modestly, curve unchanged, VIX low
- Technical indicators mixed: price below 20‑day and 50‑day SMAs, RSI 37.5, low volume
- Analyst view thin (11.4% coverage) but bullish: 65.7% buy, weighted price target +14.7%
- Positioning crowded long (95th percentile) with slight weekly decline (-0.4%)

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Standard Chartered PLC Stocks](https://www.tradingview.com/symbols/GETTEX-STD/etfs/)  
  <sub>TradingView, 3 hours ago</sub>  
  Explore funds investing in STD in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 88.04 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 89.84 (-2.0%), 50d 90.55 (-2.8%), 200d 87.52 (+0.6%); 50d above 200d
Momentum: RSI(14) 37.5 | MACD -0.795 vs signal -0.585 (histogram -0.210)
Returns: 1d -0.0% | 5d -0.2% | 1m -5.0% | 3m +1.0%
52-week range: 77.90 - 93.19 (now 66.3% of the way up)
Volatility: ATR(14) 0.91 (1.0% of price) | annualised 20d 12.1%
Volume: 0.14x the 20-day average
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
Three-year record: +18.1% a year | beta to the market 0.90
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.7% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.7% of open interest (626,488 contracts)
Change on the week: -0.4% of open interest
Crowding: 95% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.1% (-56.21M) over 7d
Shares outstanding: 437.67M | fund size: 38.53B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals lack decisive break, analyst coverage thin despite bullish rating, positioning modest and decreasing.

**Main reasons it gave:**
- Macro: US Treasury yields rose modestly (10‑yr +0.21% on the week) with no policy surprise
- Technical: price 60.04 just below 20‑day SMA (60.39), RSI 48.6, volume 0.30× 20‑day average
- Analyst view: thin coverage (22.2% of fund) but all buy, weighted price target +35.4% above current
- Positioning: large speculators net long 3.3% of open interest, down -0.9% week‑over‑week

<details><summary><b>News</b> — score +0.00</summary>

- [Vanguard International ETF Face-Off: VXUS vs. VWO](https://www.fool.com/coverage/etfs/2026/09/25/vanguard-international-etf-face-off-vxus-vs-vwo/)  
  <sub>The Motley Fool, 8 hours ago</sub>  
  The Vanguard Total International Stock ETF (VXUS -0.38%) and Vanguard FTSE Emerging Markets ETF (VWO -0.42%) both offer low-cost international...
- [Daily ETF Flows: CORO Pulls In $4.2B](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-coro-pulls-210004066.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 16,352.50. 885,248.92. 1.85%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.04 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 60.39 (-0.6%), 50d 59.81 (+0.4%), 200d 57.82 (+3.8%); 50d above 200d
Momentum: RSI(14) 48.6 | MACD 0.018 vs signal 0.073 (histogram -0.055)
Returns: 1d +0.3% | 5d +0.1% | 1m -1.0% | 3m +2.5%
52-week range: 52.42 - 61.44 (now 84.5% of the way up)
Volatility: ATR(14) 0.63 (1.0% of price) | annualised 20d 13.7%
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
Three-year record: +18.2% a year | beta to the market 0.75
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 3.3% of open interest (1,310,241 contracts)
Change on the week: -0.9% of open interest
Crowding: 37% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 85.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 32.91 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 32.59 (+1.0%), 50d 30.91 (+6.5%), 200d 27.94 (+17.8%); 50d above 200d
Momentum: RSI(14) 59.7 | MACD 0.622 vs signal 0.731 (histogram -0.109)
Returns: 1d -0.8% | 5d -0.1% | 1m +7.9% | 3m +23.9%
52-week range: 22.07 - 33.68 (now 93.4% of the way up)
Volatility: ATR(14) 0.47 (1.4% of price) | annualised 20d 18.7%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Commodities Broad Basket
What it holds: P/E n/a | P/B 0.00 | P/S 0.00 | 3y earnings growth n/a
Yield: 2.4%
Three-year record: +14.1% a year | beta to the market 1.05
Cost and size: expense ratio 0.85% | net assets 1.80B
What it is made of: Other 50.6%, Cash 44.8%, Bonds 2.7%, Stocks 1.9%
Largest holdings: Invesco Shrt-Trm Inv Gov&Agcy Instl 40.8%, Brent Crude Future Nov 26 8.9%, Invesco Short Term Treasury ETF 6.2%, Mini Ibovespa Future Dec 26 1.9%
```

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
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

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.0% (36.25M) over 7d
Shares outstanding: 55.34M | fund size: 1.82B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 91.86 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 93.63 (-1.9%), 50d 94.44 (-2.7%), 200d 95.59 (-3.9%); 50d below 200d
Momentum: RSI(14) 27.6 | MACD -0.601 vs signal -0.464 (histogram -0.137)
Returns: 1d -0.3% | 5d -1.6% | 1m -3.6% | 3m -4.8%
52-week range: 91.86 - 97.74 (now 0.0% of the way up)
Volatility: ATR(14) 0.46 (0.5% of price) | annualised 20d 6.5%
Volume: 0.50x the 20-day average
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
Share count change: 1 week: -0.5% (-73.42M) over 7d
Shares outstanding: 159.30M | fund size: 14.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Mortgage Rates Hit 2023 High, Ross Gerber Warns of Debt Spiral - iShares 7-10 Year Treasury Bond ETF (NAS](https://www.benzinga.com/markets/bonds/26/09/61989791/mortgage-rates-hit-a-2023-high-as-bond-market-meltdown-accelerates-ross-gerber-warns-of-a-debt-spiral)  
  <sub>Benzinga, 6 hours ago</sub>  
  The bond market 'meltdown' is pushing mortgage rates to their highest since 2023, as Ross Gerber warns of a debt spiral.
- [Dow falls 160 points as Treasury Yields and oil prices rise](https://invezz.com/pk/news/2026/09/24/dow-falls-160-points-as-treasury-yields-and-oil-prices-rise/)  
  <sub>Invezz, 18 hours ago</sub>  
  US stocks ended lower on Thursday, with the Dow Jones Industrial Average falling for a third straight session as Treasury yields reached multidecade highs...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.65 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 91.35 (-1.9%), 50d 92.43 (-3.0%), 200d 94.65 (-5.3%); 50d below 200d
Momentum: RSI(14) 25.6 | MACD -0.729 vs signal -0.595 (histogram -0.133)
Returns: 1d -0.0% | 5d -1.3% | 1m -3.9% | 3m -5.7%
52-week range: 89.65 - 97.99 (now 0.0% of the way up)
Volatility: ATR(14) 0.45 (0.5% of price) | annualised 20d 6.1%
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 34.7% of open interest (5,377,777 contracts)
Change on the week: +2.4% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.2% (-95.93M) over 7d
Shares outstanding: 458.94M | fund size: 41.14B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Invesco Taps BlackRock's Tim Clavin for ETF Capital Markets](https://etfdb.com/innovative-etfs-content-hub/invesco-taps-blackrock-tim-clavin/)  
  <sub>ETF Database, 22 hours ago</sub>  
  Tim Clavin leaves BlackRock to lead ETF capital markets at Invesco, whose five largest ETFs hold about $751 billion combined, led by QQQ.
- [S&P 500 Eyes Midterm Rally: ETFs to Watch in October 2026 - State Street SPDR S&P 500 ETF Trust (ARCA:SPY](https://www.benzinga.com/etfs/sector-etfs/26/09/61984746/sampp-500s-midterm-rally-setup-is-getting-interesting-these-etfs-could-hold-clues)  
  <sub>Benzinga, 19 hours ago</sub>  
  The S&P 500 enters a historically strong October-November stretch. Here's how ETFs could reveal the rally's real drivers.
- [Futures Signal Market Bounce; Three Stocks In Buy Areas](https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-market-rally-resilient-yields-oil-prices-rising-tesla-semi-event/)  
  <sub>Investor's Business Daily, 3 hours ago</sub>  
  Dow Jones futures rose, with the market showing resilience even as yields keep rising. Taiwan Semi is a buy. Tesla held a Semi event.
- [Daily ETF Flows: CORO Pulls In $4.2B](https://finance.yahoo.com/markets/options/articles/daily-etf-flows-coro-pulls-210004066.html)  
  <sub>Yahoo Finance, 18 hours ago</sub>  
  Top 10 Creations (All ETFs). Ticker. Name. Net Flows ($, mm). AUM ($, mm). AUM % Change. IVV · iShares Core S&P 500 ETF. 16,352.50. 885,248.92. 1.85%.
- [S&P 500 Divergence Deepens as Treasury Yields Surge](https://mottcapitalmanagement.com/sp-500-divergence-bond-volatility/)  
  <sub>Mott Capital Management, 17 hours ago</sub>  
  The S&P 500 and the equal-weight ETF have diverged significantly. Over the past year, the two-month moves in SPY and RSP have lined up less and less,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 210.58 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 214.96 (-2.0%), 50d 217.00 (-3.0%), 200d 205.34 (+2.6%); 50d above 200d
Momentum: RSI(14) 33.8 | MACD -2.010 vs signal -1.501 (histogram -0.508)
Returns: 1d +0.2% | 5d -0.8% | 1m -5.2% | 3m +0.1%
52-week range: 182.18 - 222.77 (now 70.0% of the way up)
Volatility: ATR(14) 1.76 (0.8% of price) | annualised 20d 8.9%
Volume: 0.42x the 20-day average
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
Ratings by weight: buy 67.9% | hold 32.1% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -3.5% above the current prices
Holdings read: MRNA, VEEV, ZBRA, CRL, DASH
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - VEEV: 2026-08-28 Citigroup: main, Neutral -> Neutral
  - ZBRA: 2026-09-15 Needham: main, Buy -> Buy
  - CRL: 2026-09-25 TD Cowen: main, Buy -> Buy
  - DASH: 2026-09-09 Scotiabank: init, ? -> Sector Outperform
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 12.0% of open interest (2,446,519 contracts)
Change on the week: +4.5% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.1% (1.04B) over 7d
Shares outstanding: 474.11M | fund size: 99.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [STIP: Simple TIPS ETF, For Risk-Averse Investors Concerned About Inflation (NYSEARCA:STIP)](https://seekingalpha.com/article/4949685-stip-simple-tips-etf-for-risk-averse-investors-concerned-about-inflation)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  STIP ETF offers short-term TIPS to hedge rising inflation with lower risk, as inflation stays above target and more Fed hikes loom. Read more on STIP here.
- [Short-term TIPS fund STIP is a smart choice ami...](https://pluang.com/en/news-feed/stip-etf-tips-sederhana-untuk-investor-anti-risiko-dengan-kekhawatiran-inflasi)  
  <sub>Pluang, 6 hours ago</sub>  
  The Vanguard Short-Term Inflation-Protected Securities ETF (STIP) focuses on short-term Treasury Inflation-Protected Securities (TIPS), which tend to...
- [BlackRock’s Model-Portfolio Shuffles Show AI Bets Are Evolving](https://www.bloomberg.com/news/newsletters/2026-09-24/how-is-blackrock-s-ai-trade-evolving-beyond-pioneers-of-the-tech?srnd=phx-india)  
  <sub>Bloomberg.com, 21 hours ago</sub>  
  Welcome to ETF IQ, a weekly newsletter dedicated to the $22.5 trillion global ETF industry. I'm Bloomberg News reporter Isabelle Lee, in for Katie Greifeld.
- [TASC 2026.10 A Low-Risk ETF-Trading Strategy — Indicator by PineCodersTASC](https://www.tradingview.com/script/2S4BqQzQ-TASC-2026-10-A-Low-Risk-ETF-Trading-Strategy/)  
  <sub>TradingView, 14 hours ago</sub>  
  OVERVIEW This script implements concepts from a short-term ETF investment strategy outlined by Markos Katsanos in the article "Selecting Strong ETFs While...
- [Best Performing ETFs: Top Returns at a Glance](https://www.tradingkey.com/markets/etf/best-performing?page=75)  
  <sub>TradingKey, 22 hours ago</sub>  
  View TradingKey's list of the best performing ETFs, including price changes, trading volume, multi-period returns, and performance charts.
- [Kansas City Fed's Schmid: Are we moving to a too-big-to-fail AI ecosystem? (TLT:NASDAQ)](https://seekingalpha.com/news/4647139-kansas-city-feds-schmid-are-we-moving-to-a-too-big-to-fail-ai-ecosystem)  
  <sub>Seeking Alpha, 21 minutes ago</sub>  
  "I think where we have started to really synthesize what's happening in the AI and the data center build out is, are we moving to a too-big-to-fail AI...
- [Top ETFs: Live Prices, Returns & Trends](https://www.tradingkey.com/markets/etf/top?page=97)  
  <sub>TradingKey, 20 hours ago</sub>  
  View the latest market data on top ETFs to watch, from price movements and trading volume to historical returns and performance trends.
- [3 Vanguard ETFs Flying Under the Radar with 20% Upside](https://www.tipranks.com/news/3-vanguard-etfs-flying-under-the-radar-with-20-upside)  
  <sub>TipRanks, 51 minutes ago</sub>  
  Vanguard ETFs are often known for their low costs and long-term stability, but not all of them get the attention they deserve. Some lesser-known Vanguard...
- [VTI vs. VXUS: Which Vanguard ETF Fits Your Portfolio Better?](https://www.tipranks.com/news/vti-vs-vxus-which-vanguard-etf-fits-your-portfolio-better)  
  <sub>TipRanks, 4 hours ago</sub>  
  Building a diversified portfolio often means looking beyond a single market. Vanguard Total Stock Market ETF ($VTI) and the Vanguard Total International...
- [Bitcoin ETF IBIT Pulls In $166 Million as Spot Prices Surge Past $84K](https://www.tipranks.com/news/cryptocurrencies/bitcoin-etf-ibit-pulls-in-166-million-as-spot-prices-surge-past-84k)  
  <sub>TipRanks, 5 hours ago</sub>  
  IShares Bitcoin Trust Registered's IBIT drew fresh attention on September 24, 2026, as the spot bitcoin ETF absorbed $166.3 million in net inflows.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.33 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 106.00 (-1.6%), 50d 106.81 (-2.3%), 200d 109.49 (-4.7%); 50d below 200d
Momentum: RSI(14) 25.3 | MACD -0.672 vs signal -0.513 (histogram -0.159)
Returns: 1d +0.0% | 5d -0.9% | 1m -3.0% | 3m -4.9%
52-week range: 104.30 - 112.20 (now 0.4% of the way up)
Volatility: ATR(14) 0.39 (0.4% of price) | annualised 20d 4.6%
Volume: 0.27x the 20-day average
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
Contract: UST 10Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 34.7% of open interest (5,377,777 contracts)
Change on the week: +2.4% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.2% (33.49M) over 7d
Shares outstanding: 142.21M | fund size: 14.84B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>  
  iShares 20+ Year Treasury Bond ETF (TLT) · -2.90% · -5.48% · -9.15% · -10.20% · -11.33% · -46.30% · -3.49%.
- [TLT ETF Tracking Long Duration Bonds Hits New Record Low - iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT](https://www.benzinga.com/trading-ideas/movers/26/09/61977138/quick-spark-the-tlt-etf-tracking-long-duration-bonds-hits-new-record-low)  
  <sub>Benzinga, 23 hours ago</sub>  
  The iShares 20+ iShares 20+ Year Treasury Bond ETF (NASDAQ:TLT) fell to a new record low of $79.71 on Thursday as long-duration U.S. Treasury bonds sold off...
- [Nasdaq, S&P 500 Futures Rise As Chip Rally Counters Iran Jitters Ahead Of Big Tech Earnings: Why IREN, ACHR, TSLA, BA Stocks Are Drawing Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-futures-rise-as-chip-rally-counters-iran-jitters-ahead-of-big-tech-earnings/cZZ1tCdR7HO)  
  <sub>Stocktwits, 3 hours ago</sub>  
  The VanEck Semiconductor ETF was up 0.41% at close, reversing three consecutive days of declines. However, tensions in the Middle East continued to rise...
- [Bond Market Flashes a Warning Not Seen Since 2007](https://247wallst.com/investing/2026/09/24/bond-market-flashes-a-warning-not-seen-since-2007/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Treasury yields just hit levels the bond market has not seen since before the financial crisis, and the pain is spreading fast into corners of the market...
- [Bond liquidation wrecks small caps. Here's how bad some traders see it getting](https://www.cnbc.com/amp/2026/09/24/bond-liquidation-wrecks-small-caps-heres-how-bad-some-traders-see-it-getting.html)  
  <sub>CNBC, 21 hours ago</sub>  
  While the S&P 500 powers through rising bond yields and higher crude oil prices, one section of the U.S. stock market is falling behind.
- [US Bond Yields Keep Climbing — But Retail Traders Still Can’t Get Enough Stocks](https://www.tradingview.com/news/stocktwits:c8405a6fb094b:0-us-bond-yields-keep-climbing-but-retail-traders-still-can-t-get-enough-stocks/)  
  <sub>TradingView, 8 hours ago</sub>  
  In the poll, 55% of users said they would invest in stocks right now, while only 17% said they would put their money in cash or bond markets.
- [S&P 500, Nasdaq, Dow Futures Climb As Historic SpaceX IPO Looms, Trump Hints Iran War May End: Why SNDK, ASTS, RDW, CRWV, RKLB Are Also Trending](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-climb-as-historic-spacex-ipo-looms-trump-hints-iran-war-may-end/cZK5isfR7Pd)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The biggest catalyst for markets on Friday is the SpaceX IPO, set to debut on the Nasdaq under the ticker SPCX.
- [Treasury Yields Hit 5%: The Hidden Duration In Your ETF Portfolio](https://www.tradingview.com/news/benzinga:06ee79955094b:0-treasury-yields-hit-5-the-hidden-duration-in-your-etf-portfolio/)  
  <sub>TradingView, 21 hours ago</sub>  
  The bond market is sending a warning that extends well beyond fixed income. The 10-year Treasury yield climbed to around 5.15% Thursday, its highest level...
- [A $55B Vanguard Bond Fund Manager Says ‘No Time To Be A Hero’ As Treasury Yields Spike Across The Curve](https://www.tradingview.com/news/stocktwits:6eee33b7b094b:0-a-55b-vanguard-bond-fund-manager-says-no-time-to-be-a-hero-as-treasury-yields-spike-across-the-curve/)  
  <sub>TradingView, 21 hours ago</sub>  
  Amid surging yields on long- and short-term U.S. government fixed-income assets, senior bond fund executives overseeing nearly $700 billion are taking a...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 78.97 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 81.35 (-2.9%), 50d 82.24 (-4.0%), 200d 85.67 (-7.8%); 50d below 200d
Momentum: RSI(14) 30.0 | MACD -0.677 vs signal -0.497 (histogram -0.180)
Returns: 1d -0.6% | 5d -2.8% | 1m -5.2% | 3m -9.6%
52-week range: 78.97 - 92.06 (now 0.0% of the way up)
Volatility: ATR(14) 0.75 (0.9% of price) | annualised 20d 10.4%
Volume: 0.63x the 20-day average
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
Three-year record: -0.0% a year | beta to the market 2.39
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
Contract: ULTRA UST BOND - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 32.9% of open interest (2,470,471 contracts)
Change on the week: +3.1% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 109.70M | fund size: 8.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.62 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 28.27 (+1.3%), 50d 28.23 (+1.4%), 200d 27.73 (+3.2%); 50d above 200d
Momentum: RSI(14) 68.1 | MACD 0.131 vs signal 0.072 (histogram 0.059)
Returns: 1d -0.2% | 5d +0.8% | 1m +2.1% | 3m +0.6%
52-week range: 26.47 - 28.69 (now 96.9% of the way up)
Volatility: ATR(14) 0.11 (0.4% of price) | annualised 20d 5.0%
Volume: 0.15x the 20-day average
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
Three-year record: +3.7% a year | beta to the market -9.48
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
Contract: USD INDEX - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 11.2% of open interest (43,744 contracts)
Change on the week: -21.9% of open interest
Crowding: 50% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.3% (-3.84M) over 7d
Shares outstanding: 10.48M | fund size: 299.97M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Slightly bullish tilt from strong analyst coverage and modest net inflows, but mixed technicals and no macro catalyst keep the overall view neutral.

**Main reasons it gave:**
- Analyst coverage: 100% buy on 45.5% of fund, weighted price target +14.7% above current price
- Fund flows: share count increased 1.3% over the past week, indicating net inflows
- Technicals: price above 20‑day (112.63) and 50‑day (111.33) SMA, RSI 51.2, volume 0.27× 20‑day average
- Fundamentals: P/E 15.38, 3‑year annualized return +21.1%, yield 1.3%

<details><summary><b>News</b> — score +0.00</summary>

- [These communication services stocks are trapped longest in bearish Quant ratings (XLC:NYSEARCA)](https://seekingalpha.com/news/4647118-these-communication-services-stocks-are-trapped-longest-in-bearish-quant-ratings)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Communication Services stock screen: only GOGO and TTD held Strong Sell Quant Ratings 60+ days amid ad demand and wireless trends.
- [Comcast Slips as KeyBanc Cuts to Underweight on Broadband Share Losses; AT&T and Verizon Hold Steady](https://247wallst.com/investing/2026/09/25/comcast-slips-as-keybanc-cuts-to-underweight-on-broadband-share-losses-att-and-verizon-hold-steady/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  KeyBanc's bearish turn on broadband is pulling Comcast Corporation (NASDAQ:CMCSA | CMCSA Price Prediction) lower, while the fiber carriers winning its...
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...
- [Meta’s AI Spending Shows ‘Clearest Signs’ Of Payoff Yet, TD Cowen Says — Muse Revenue Seen At $27B By 2031](https://www.tradingview.com/news/stocktwits:9a14778c5094b:0-meta-s-ai-spending-shows-clearest-signs-of-payoff-yet-td-cowen-says-muse-revenue-seen-at-27b-by-2031/)  
  <sub>TradingView, 4 hours ago</sub>  
  Meta Platforms Inc.'s (META) heavy artificial intelligence spending is showing its “clearest signs to date” of a potential payoff, according to TD Cowen,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 112.85 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 112.63 (+0.2%), 50d 111.33 (+1.4%), 200d 113.94 (-1.0%); 50d below 200d
Momentum: RSI(14) 51.2 | MACD 0.488 vs signal 0.492 (histogram -0.005)
Returns: 1d -1.0% | 5d +1.8% | 1m +0.2% | 3m +6.3%
52-week range: 105.38 - 120.08 (now 50.8% of the way up)
Volatility: ATR(14) 1.83 (1.6% of price) | annualised 20d 21.8%
Volume: 0.27x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.54 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.7% above the current prices
Holdings read: META, GOOGL, GOOG, T, VZ
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-09-18 Tigress Financial: main, Strong Buy -> Strong Buy
  - GOOG: 2026-07-23 JP Morgan: main, Overweight -> Overweight
  - T: 2026-09-21 BNP Paribas: up, Neutral -> Outperform
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
Share count change: 1 week: +1.3% (290.68M) over 7d
Shares outstanding: 197.59M | fund size: 22.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, mixed technicals, flat flows, strong analyst view limited to 37.6% of fund weight, moderate fundamentals.

**Main reasons it gave:**
- Yield curve remains upward sloping (+1.12 points) – no policy surprise
- MACD histogram negative (-0.209) and RSI neutral (46.7) – mixed technicals
- Fund flows flat (0% share count change) – no net demand
- Analyst coverage 100% buy with +18.4% price target, but only 37.6% of fund weight
- Price below 20‑day SMA (-1.2%) while above 50‑day (+0.2%) and 200‑day (+0.3%) SMAs

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 122.67 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 124.18 (-1.2%), 50d 122.43 (+0.2%), 200d 122.30 (+0.3%); 50d above 200d
Momentum: RSI(14) 46.7 | MACD 0.410 vs signal 0.619 (histogram -0.209)
Returns: 1d -0.1% | 5d -1.7% | 1m -0.8% | 3m +4.1%
52-week range: 94.28 - 137.69 (now 65.4% of the way up)
Volatility: ATR(14) 1.80 (1.5% of price) | annualised 20d 21.2%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.89 | P/B 2.43 | P/S 2.45 | 3y earnings growth n/a
Yield: 1.5%
Three-year record: +33.9% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 897.28M
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Teva Pharmaceutical Industries Ltd ADR 10.1%, Bank Leumi Le-Israel BM 9.0%, Bank Hapoalim BM 8.1%, Tower Semiconductor Ltd 5.5%, Elbit Systems Ltd 4.8%
Sector mix: Financial services 36.1%, Technology 18.1%, Healthcare 10.7%, Industrials 10.0%
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
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
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
Shares outstanding: 2.55M | fund size: 312.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral

**Main reasons it gave:**
- Fund flows: -1.3% share count (net outflow) over the past week
- Analyst view: 90.3% buy rating, price target +1.4% above current price
- Technicals: price near 52‑week high (92.2% of range) with low volume (0.19× 20‑day avg) and slight bearish MACD
- Macro: yields up modestly, no surprise data; VIX low at 15.42

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 44.66 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 44.79 (-0.3%), 50d 43.78 (+2.0%), 200d 39.30 (+13.7%); 50d above 200d
Momentum: RSI(14) 51.2 | MACD 0.302 vs signal 0.422 (histogram -0.120)
Returns: 1d -0.1% | 5d +0.6% | 1m -0.2% | 3m +16.7%
52-week range: 31.57 - 45.76 (now 92.2% of the way up)
Volatility: ATR(14) 0.65 (1.5% of price) | annualised 20d 19.4%
Volume: 0.19x the 20-day average
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
Three-year record: +42.9% a year | beta to the market 0.73
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 47.4% of the fund by weight
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.32 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -1.4% above the current prices
Holdings read: PKO.WA, PKN.WA, PEO.WA, PZU.WA, KGH.WA
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
Share count change: 1 week: -1.3% (-10.74M) over 7d
Shares outstanding: 18.66M | fund size: 833.14M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bearish analyst view offset by solid fundamentals and flat fund flows.

**Main reasons it gave:**
- Analyst coverage: 40.4% sell rating, weighted price target -5.6% vs current price
- Fund flows: flat week with -0.2% share count change (slight outflow)
- Technicals: price 3.2% below 20‑day SMA, RSI 37.7, MACD negative (moderate bearish momentum)
- Macro: Treasury yields rose modestly (10‑yr +0.21% week), no policy surprise, VIX low at 15.4

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 28.34 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 29.29 (-3.2%), 50d 29.47 (-3.8%), 200d 28.59 (-0.9%); 50d above 200d
Momentum: RSI(14) 37.7 | MACD -0.329 vs signal -0.207 (histogram -0.121)
Returns: 1d +0.1% | 5d -1.4% | 1m -6.0% | 3m +1.3%
52-week range: 24.95 - 30.43 (now 61.9% of the way up)
Volatility: ATR(14) 0.38 (1.3% of price) | annualised 20d 18.4%
Volume: 0.25x the 20-day average
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
Three-year record: +13.2% a year | beta to the market 0.96
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

<details><summary><b>What analysts and big funds say</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.35</summary>

```text
Rolled up from the 5 largest holdings, 46.4% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.6% | sell 40.4% (mean 3.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -5.6% above the current prices
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
Share count change: 1 week: -0.2% (-2.18M) over 8d
Shares outstanding: 45.82M | fund size: 1.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed fund‑specific signals lead to a neutral stance.

**Main reasons it gave:**
- Analyst coverage of top holdings (28.3% weight) shows 74.3% buy rating and +6.5% price target
- Fund flows flat with -0.5% share count change over the week
- Fund basics: moderate valuation (P/E 19.49) and strong 3‑year record (+23% annual)
- Macro: US Treasury yields rose modestly across the curve, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Kevin O'Leary Explains Why His Big AI Bet is Uranium, Not Big Tech: 'The Trade is Now the Energy Trade'](https://www.benzinga.com/markets/market-summary/26/09/61941964/kevin-oleary-explains-why-his-big-ai-bet-is-uranium-not-big-tech-the-trade-is-now-the-energy-trade)  
  <sub>Benzinga, 8 hours ago</sub>  
  Editor's Note: This story has been corrected to reflect the performance of the ETFs accurately. Venture capitalist and investor Kevin O'Leary says he is...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.42 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 60.69 (-2.1%), 50d 60.73 (-2.1%), 200d 57.60 (+3.2%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -0.369 vs signal -0.186 (histogram -0.183)
Returns: 1d -0.0% | 5d -1.3% | 1m -4.5% | 3m +2.8%
52-week range: 49.72 - 62.64 (now 75.1% of the way up)
Volatility: ATR(14) 0.65 (1.1% of price) | annualised 20d 14.4%
Volume: 0.25x the 20-day average
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
Three-year record: +23.0% a year | beta to the market 0.79
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 28.3% of the fund by weight
Ratings by weight: buy 74.3% | hold 25.7% | sell 0.0% (mean 2.20 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.5% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-09-23 Wedbush: reit, Outperform -> Outperform
  - BMO.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
  - BNS.TO: 2026-05-28 RBC Capital: main, Sector Perform -> Sector Perform
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
Share count change: 1 week: -0.5% (-31.63M) over 8d
Shares outstanding: 112.70M | fund size: 6.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; analyst view is bullish, but recent outflows and slightly bearish technicals offset that. No macro surprise or decisive technical break.

**Main reasons it gave:**
- Analyst ratings: 82.1% buy, weighted price target +10.5% above current
- Fund flows: 1.4% share count decline over the past week (net outflows)
- Technical indicators: price below 20‑day SMA, RSI 42.9, MACD below signal
- Macro: US Treasury yields rose across the curve, indicating tightening

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 51.20 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 52.07 (-1.7%), 50d 52.22 (-2.0%), 200d 51.36 (-0.3%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -0.361 vs signal -0.254 (histogram -0.107)
Returns: 1d +0.3% | 5d +0.3% | 1m -5.1% | 3m +4.4%
52-week range: 45.38 - 54.72 (now 62.3% of the way up)
Volatility: ATR(14) 0.69 (1.4% of price) | annualised 20d 15.8%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 14.99 | P/B 2.88 | P/S 2.90 | 3y earnings growth n/a
Yield: 3.4%
Three-year record: +20.3% a year | beta to the market 1.19
Cost and size: expense ratio 0.51% | net assets 755.74M
What it is made of: Stocks 98.9%, Cash 1.1%
Largest holdings: Spotify Technology SA 10.2%, Investor AB Class B 9.5%, Volvo AB Class B 7.1%, Atlas Copco AB Class A 6.9%, Sandvik AB 5.3%
Sector mix: Industrials 46.0%, Financial services 24.9%, Communication services 13.9%, Technology 6.2%
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
Rolled up from the 4 largest holdings, 29.5% of the fund by weight
Ratings by weight: buy 82.1% | hold 17.9% | sell 0.0% (mean 1.97 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.5% above the current prices
Holdings read: SPOT, VOLV-B.ST, ATCO-A.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-08-13 Argus Research: reit, Buy -> Buy
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
Share count change: 1 week: -1.4% (-10.50M) over 8d
Shares outstanding: 14.52M | fund size: 743.21M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, bullish analyst view not enough to outweigh neutral macro and technicals.

**Main reasons it gave:**
- Analyst coverage of top holdings is bullish: 78% buy rating and +16.3% price target
- Fund flows flat over the past week, indicating no net demand
- Technical indicators show price below 20‑day and 50‑day SMAs, RSI 39.1, low volume, suggesting short‑term weakness
- Macro backdrop unchanged: yields rose modestly, dollar index up, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 42.06 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 42.96 (-2.1%), 50d 43.05 (-2.3%), 200d 42.39 (-0.8%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -0.375 vs signal -0.242 (histogram -0.133)
Returns: 1d +0.5% | 5d -0.2% | 1m -5.1% | 3m +3.5%
52-week range: 38.08 - 44.59 (now 61.2% of the way up)
Volatility: ATR(14) 0.47 (1.1% of price) | annualised 20d 13.4%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 18.40 | P/B 1.94 | P/S 1.28 | 3y earnings growth n/a
Yield: 1.9%
Three-year record: +18.5% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.82B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Siemens AG 12.1%, SAP SE 11.3%, Allianz SE 10.0%, Siemens Energy AG Ordinary Shares 6.4%, Deutsche Telekom AG 5.6%
Sector mix: Industrials 28.7%, Financial services 23.2%, Technology 15.9%, Consumer cyclical 7.4%
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
Rolled up from the 5 largest holdings, 45.5% of the fund by weight
Ratings by weight: buy 78.0% | hold 22.0% | sell 0.0% (mean 1.87 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.3% above the current prices
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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, technicals mixed, flows flat, fundamentals moderate, analyst view bullish but limited coverage.

**Main reasons it gave:**
- Analyst view: 100% buy rating and +11% price target for top holdings (50.9% of fund weight)
- Fund flows flat: share count +0.3% over 7 days
- Technicals: price below 20‑day (61.10) and 50‑day (61.70) SMAs, RSI 40.3, MACD negative
- Macro: yields up modestly (10‑yr +0.21% week), no surprise data releases
- Fundamentals: moderate valuation (P/E 15.25) and strong 3‑yr record (+28.9%/yr)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.03 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 61.10 (-1.8%), 50d 61.70 (-2.7%), 200d 57.87 (+3.7%); 50d above 200d
Momentum: RSI(14) 40.3 | MACD -0.495 vs signal -0.360 (histogram -0.135)
Returns: 1d +0.2% | 5d -0.0% | 1m -4.6% | 3m +2.4%
52-week range: 50.31 - 63.35 (now 74.5% of the way up)
Volatility: ATR(14) 0.71 (1.2% of price) | annualised 20d 16.4%
Volume: 0.20x the 20-day average
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
Three-year record: +28.9% a year | beta to the market 0.88
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 50.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.0% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, RACE.MI, ENI.MI
Recent rating changes among them:
  - RACE.MI: 2026-07-31 UBS: main, Buy -> Buy
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
Share count change: 1 week: +0.3% (3.34M) over 7d
Shares outstanding: 18.69M | fund size: 1.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Analyst view: 100% buy rating on 17% of fund weight, price target +16.5% (thin coverage)
- CFTC net long 4.3% (+1.5% change) vs fund outflows -1.7% share count (neutral net sentiment)
- Technicals: price above 20d/50d/200d SMAs, RSI 52.6, MACD below signal, low volume (no decisive break)
- Macro: Treasury yields rose modestly, no policy surprise, VIX 15.42 (low volatility)

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 4 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.
- [Nikkei rises through the bond shock: is Kospi walking into a selloff after Chuseok?](https://invezz.com/au/news/2026/09/25/nikkei-rises-through-the-bond-shock-is-kospi-walking-into-a-selloff-after-chuseok/)  
  <sub>Invezz, 10 hours ago</sub>  
  Asian stocks were mixed on Friday, with Japan's Nikkei 225 pushing higher while South Korea's Kospi remained closed for Chuseok, leaving two of the region's...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 97.33 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 97.13 (+0.2%), 50d 95.36 (+2.1%), 200d 90.05 (+8.1%); 50d above 200d
Momentum: RSI(14) 52.6 | MACD 0.451 vs signal 0.614 (histogram -0.162)
Returns: 1d +1.6% | 5d +0.3% | 1m +2.0% | 3m +4.9%
52-week range: 78.36 - 98.78 (now 92.9% of the way up)
Volatility: ATR(14) 1.45 (1.5% of price) | annualised 20d 17.6%
Volume: 0.30x the 20-day average
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
Three-year record: +19.7% a year | beta to the market 0.86
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.5% above the current prices
Holdings read: 8306.T, 7203.T, 8316.T, 8035.T, 6857.T
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

```text
Contract: NIKKEI STOCK AVERAGE YEN DENOM - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 4.3% of open interest (22,625 contracts)
Change on the week: +1.5% of open interest
Crowding: 38% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.7% (-383.62M) over 7d
Shares outstanding: 229.75M | fund size: 22.36B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; technical weakness, high valuations, flat flows, and no macro surprise offset bullish analyst sentiment.

**Main reasons it gave:**
- Technicals: price below 20‑day, 50‑day and 200‑day SMAs, RSI 39.1, low volume
- Fundamentals: high valuation metrics (P/E 24.65, P/B 4.25) suggest overvaluation
- Analyst view: 74.5% buy rating and +9.6% price target indicate bullish sentiment
- Fund flows: flat share count (0.0% change) indicating neutral demand
- Macro: no rate or policy surprise; yields up modestly, curve normal

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.33 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 61.27 (-1.5%), 50d 62.58 (-3.6%), 200d 61.59 (-2.0%); 50d above 200d
Momentum: RSI(14) 39.1 | MACD -0.729 vs signal -0.723 (histogram -0.006)
Returns: 1d -0.2% | 5d +0.5% | 1m -6.0% | 3m -3.3%
52-week range: 53.86 - 65.08 (now 57.7% of the way up)
Volatility: ATR(14) 0.67 (1.1% of price) | annualised 20d 13.8%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 24.65 | P/B 4.25 | P/S 2.78 | 3y earnings growth n/a
Yield: 1.7%
Three-year record: +13.0% a year | beta to the market 0.91
Cost and size: expense ratio 0.50% | net assets 2.42B
What it is made of: Stocks 99.0%, Cash 1.0%
Largest holdings: Roche Holding AG Ordinary Shares new 13.6%, Novartis AG Registered Shares 12.4%, Nestle SA 11.1%, UBS Group AG Registered Shares 6.8%, Compagnie Financiere Richemont SA Class A 4.6%
Sector mix: Healthcare 37.5%, Financial services 20.6%, Consumer defensive 13.3%, Industrials 11.8%
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 48.5% of the fund by weight
Ratings by weight: buy 74.5% | hold 25.5% | sell 0.0% (mean 2.40 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.6% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Analyst coverage 44.1% of fund weight, all buy, price target +30% above current
- Price near 20‑day SMA, RSI 48.9, low volume (0.09× 20‑day avg)
- Fund flows flat, share count unchanged over 1 week
- US Treasury yields up across curve, dollar index +0.78% on week, no macro surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 67.73 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 67.71 (+0.0%), 50d 68.16 (-0.6%), 200d 64.09 (+5.7%); 50d above 200d
Momentum: RSI(14) 48.9 | MACD -0.293 vs signal -0.336 (histogram 0.043)
Returns: 1d +0.3% | 5d +1.1% | 1m -1.9% | 3m +0.7%
52-week range: 55.33 - 71.61 (now 76.2% of the way up)
Volatility: ATR(14) 0.91 (1.3% of price) | annualised 20d 16.4%
Volume: 0.09x the 20-day average
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
Three-year record: +24.2% a year | beta to the market 1.14
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 44.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.62 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.0% above the current prices
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
Shares outstanding: 5.55M | fund size: 375.90M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall call; no material macro surprise, modest analyst bias, flat fund flows, and technicals lack decisive breakout.

**Main reasons it gave:**
- Flat fund flows: share count unchanged (+0.0% over 1 week)
- Analyst coverage: 52% buy, 48% hold, weighted price target +2% above current price
- Technical: price 1.2% below 20‑day SMA, volume 0.10× 20‑day average, no decisive breakout
- Macro: Treasury yields up (10‑yr +0.21% week), VIX low at 15.42, no data surprise
- Fundamentals: moderate valuation (P/E 16.28), yield 2.7%, strong 3‑yr record (+33.7% per year)

<details><summary><b>News</b> — score +0.00</summary>

- [美股ETF追踪 | 隔夜全球油气价格大涨 天然气ETF涨超6%](https://emwap.eastmoney.com/a/202609253884024126.html)  
  <sub>东方财富, 9 hours ago</sub>  
  如何低门槛投资美股？ 周四美股三大指数窄幅震荡，道琼斯指数微跌0.31%，纳斯达克综合指数微涨0.01%，标普500指数微跌0.02%。大型科技股表现分化，Meta大涨4.50%领涨，...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 60.81 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 61.55 (-1.2%), 50d 61.58 (-1.2%), 200d 57.44 (+5.9%); 50d above 200d
Momentum: RSI(14) 45.1 | MACD -0.278 vs signal -0.148 (histogram -0.131)
Returns: 1d +0.1% | 5d +0.4% | 1m -3.3% | 3m +3.6%
52-week range: 48.25 - 63.23 (now 83.9% of the way up)
Volatility: ATR(14) 0.78 (1.3% of price) | annualised 20d 16.7%
Volume: 0.10x the 20-day average
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
Three-year record: +33.7% a year | beta to the market 0.87
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 54.5% of the fund by weight
Ratings by weight: buy 52.0% | hold 48.0% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +2.0% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break; positive analyst view, fund flows, and fundamentals are offset by weak short‑term technical momentum and lack of macro catalyst.

**Main reasons it gave:**
- Analyst coverage of top holdings shows 69.5% buy rating and +11.9% price target
- Fund flows positive: share count up 1.2% in the past week
- Fundamentals: P/E 17.08, yield 3.1%, three‑year return +18.2% per year
- Technicals: price below 20‑day and 50‑day SMAs, RSI 39.6, MACD negative, low volume
- No macro surprise: yields rising, no policy change, VIX low

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 47.08 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 47.87 (-1.6%), 50d 48.01 (-1.9%), 200d 46.59 (+1.1%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD -0.260 vs signal -0.149 (histogram -0.111)
Returns: 1d -0.2% | 5d -0.4% | 1m -3.6% | 3m +2.9%
52-week range: 41.04 - 49.39 (now 72.4% of the way up)
Volatility: ATR(14) 0.45 (1.0% of price) | annualised 20d 11.1%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.25</summary>

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
Rolled up from the 5 largest holdings, 36.0% of the fund by weight
Ratings by weight: buy 69.5% | hold 30.5% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +11.9% above the current prices
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
Share count change: 1 week: +1.2% (44.29M) over 7d
Shares outstanding: 79.87M | fund size: 3.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Mexico (EWW) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and flat fund flows. Analyst view is bullish but limited to ~48% of assets; fundamentals are attractive. Overall the mix yields a neutral stance.

**Main reasons it gave:**
- Technical indicators show price below 20‑day, 50‑day and 200‑day SMAs and RSI 39.2, indicating weak momentum
- US Treasury yields rose across the curve and the dollar index increased, pressuring emerging‑market equities
- Analyst coverage of top holdings is 100% buy with a weighted price target +16.8% above current price
- Fund flows are flat, indicating no net demand shift

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 72.91 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 74.94 (-2.7%), 50d 75.73 (-3.7%), 200d 75.76 (-3.8%); 50d below 200d
Momentum: RSI(14) 39.2 | MACD -0.847 vs signal -0.613 (histogram -0.234)
Returns: 1d +0.6% | 5d -0.6% | 1m -6.0% | 3m -3.3%
52-week range: 64.39 - 81.23 (now 50.6% of the way up)
Volatility: ATR(14) 1.23 (1.7% of price) | annualised 20d 16.4%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.68 | P/B 1.98 | P/S 1.49 | 3y earnings growth n/a
Yield: 3.2%
Three-year record: +10.8% a year | beta to the market 1.05
Cost and size: expense ratio 0.50% | net assets 1.82B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: Grupo Mexico SAB de CV Class B 16.6%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.3%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Cemex SAB de CV 4.4%
Sector mix: Basic materials 27.3%, Consumer defensive 24.4%, Financial services 19.7%, Industrials 11.7%
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
Rolled up from the 5 largest holdings, 47.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.8% above the current prices
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
Shares outstanding: 18.90M | fund size: 1.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest outflows offset by strong fundamentals and uptrend, no macro surprise.

**Main reasons it gave:**
- Fund flows: -6.6% share count decline over 1 week indicating net outflows
- Fund fundamentals: low P/E 10.41 and strong 3-year record +48.6% annualized
- Technicals: price above 20d, 50d, 200d SMAs (+1.4%, +6.3%, +20.8%) but low volume (0.32x 20‑day avg)
- Macro: no major surprise; yields up modestly, VIX low (15.42), dollar up (+0.78%)

<details><summary><b>News</b> — score +0.00</summary>

- [The Zacks Analyst Blog Highlights CHAT, BWET, BNO, AIS, EWY and FTXL](https://www.zacks.com/stock/news/2995570/the-zacks-analyst-blog-highlights-chat-bwet-bno-ais-ewy-and-ftxl?cid=CS-YAHOO-FT-press_releases-2995570)  
  <sub>Zacks Investment Research, 6 hours ago</sub>  
  CHAT and other ETFs surged in 2026 as AI demand, geopolitical shocks and energy disruptions drove sharp gains.
- [Beyond 60/40: ETFs for a Balanced Retirement Portfolio](https://www.tradingview.com/news/zacks:6f3e9dc09094b:0-beyond-60-40-etfs-for-a-balanced-retirement-portfolio/)  
  <sub>TradingView, 4 hours ago</sub>  
  As retirement draws an end to one's earnings period, a smart allocation of assets is needed to enjoy a regular stream of income.
- [FLKR: In My View, The July Margin Calls Have Created An Opportunity (NYSEARCA:FLKR)](https://seekingalpha.com/article/4949703-flkr-in-my-view-the-july-margin-calls-have-created-an-opportunity)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Summary. It's strange, but the Franklin FTSE South Korea ETF seems to trade at a steep discount despite robust earnings growth expectations.
- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 4 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.
- [Nikkei rises through the bond shock: is Kospi walking into a selloff after Chuseok?](https://invezz.com/au/news/2026/09/25/nikkei-rises-through-the-bond-shock-is-kospi-walking-into-a-selloff-after-chuseok/)  
  <sub>Invezz, 10 hours ago</sub>  
  Asian stocks were mixed on Friday, with Japan's Nikkei 225 pushing higher while South Korea's Kospi remained closed for Chuseok, leaving two of the region's...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 185.90 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 183.26 (+1.4%), 50d 174.85 (+6.3%), 200d 153.94 (+20.8%); 50d above 200d
Momentum: RSI(14) 53.6 | MACD 2.323 vs signal 2.338 (histogram -0.015)
Returns: 1d +1.8% | 5d +2.5% | 1m +3.8% | 3m -5.8%
52-week range: 78.87 - 219.20 (now 76.3% of the way up)
Volatility: ATR(14) 6.39 (3.4% of price) | annualised 20d 46.6%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.41 | P/B 1.83 | P/S 1.70 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +48.6% a year | beta to the market 2.50
Cost and size: expense ratio 0.59% | net assets 27.72B
What it is made of: Stocks 99.5%, Cash 0.5%
Largest holdings: SK hynix Inc 23.7%, Samsung Electronics Co Ltd 22.2%, SK Square 2.9%, Samsung Electro-Mechanics Co Ltd 2.7%, KB Financial Group Inc 2.0%
Sector mix: Technology 54.6%, Industrials 17.0%, Financial services 11.1%, Consumer cyclical 5.1%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.40</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -6.6% (-1.91B) over 8d
Shares outstanding: 144.98M | fund size: 26.95B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals mixed, analyst view bullish but limited, and fund flows flat.

**Main reasons it gave:**
- US Treasury yields rose modestly (3‑month +0.11%, 10‑year +0.21% on the week) with no policy surprise
- Technical momentum neutral: RSI 47.8, MACD below signal (histogram -0.189), price below 20‑day SMA
- Analyst view bullish but limited to 40.9% of fund (100% buy, weighted price target +26.5%)
- Fund flows flat: share count unchanged (+0.0% over 7 days)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 36.79 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 37.57 (-2.1%), 50d 36.22 (+1.6%), 200d 36.28 (+1.4%); 50d below 200d
Momentum: RSI(14) 47.8 | MACD 0.376 vs signal 0.565 (histogram -0.189)
Returns: 1d -0.3% | 5d -1.9% | 1m +3.0% | 3m +6.1%
52-week range: 28.79 - 41.73 (now 61.9% of the way up)
Volatility: ATR(14) 0.78 (2.1% of price) | annualised 20d 23.8%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.40</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.48 | P/B 1.79 | P/S 1.28 | 3y earnings growth n/a
Yield: 4.1%
Three-year record: +12.6% a year | beta to the market 0.84
Cost and size: expense ratio 0.59% | net assets 8.17B
What it is made of: Stocks 96.5%, Cash 2.7%, Preferred 0.8%
Largest holdings: Vale SA 10.1%, Nu Holdings Ltd Ordinary Shares Class A 9.5%, Itau Unibanco Holding SA Participating Preferred 7.7%, Petroleo Brasileiro SA Petrobras Participating Preferred 7.0%, Petroleo Brasileiro SA Petrobras 6.6%
Sector mix: Financial services 34.1%, Energy 17.4%, Basic materials 14.5%, Utilities 12.4%
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
Rolled up from the 5 largest holdings, 40.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.5% above the current prices
Holdings read: VALE3.SA, NU, ITUB4, PETR4, PETR3.SA
Recent rating changes among them:
  - NU: 2026-09-16 Itau BBA: down, Outperform -> Market Perform
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
Shares outstanding: 200.55M | fund size: 7.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage and strong fundamentals offset by bearish fund outflows, negative technical momentum, and macro pressure from rising yields and a stronger dollar.

**Main reasons it gave:**
- Fund flows: -3.1% share count decline over 1 week (outflows)
- Analyst coverage: 100% buy rating on top holdings, price target +12.9% above current
- Technicals: MACD negative, RSI 46.3, price below 20‑day SMA
- Macro: US Treasury yields up and dollar stronger, pressuring gold miners
- Fundamentals: strong 3‑year performance (+49.7%/yr) and moderate valuations (P/E 12.84)

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  VanEck Gold Miners ETF (GDX) · -3.72% · -10.81% · 10.60% · 6.35% · 27.70% · 211.15% · 152.88%. Key Events. Baseline. Advanced Chart. Loading chart...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 92.49 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 96.27 (-3.9%), 50d 90.00 (+2.8%), 200d 91.00 (+1.6%); 50d below 200d
Momentum: RSI(14) 46.3 | MACD 0.270 vs signal 1.275 (histogram -1.005)
Returns: 1d +0.2% | 5d -3.1% | 1m -9.7% | 3m +20.1%
52-week range: 68.28 - 115.84 (now 50.9% of the way up)
Volatility: ATR(14) 3.29 (3.6% of price) | annualised 20d 41.4%
Volume: 0.21x the 20-day average
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
Three-year record: +49.7% a year | beta to the market 0.83
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

<details><summary><b>What analysts and big funds say</b> — score +0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.35</summary>

```text
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.9% above the current prices
Holdings read: NEM, AEM.TO, ABX.TO, WPM.TO, AU
Recent rating changes among them:
  - NEM: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AEM.TO: 2026-09-16 RBC Capital: main, Sector Perform -> Sector Perform
  - ABX.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - WPM.TO: 2026-09-16 RBC Capital: main, Outperform -> Outperform
  - AU: 2026-09-16 RBC Capital: main, Outperform -> Outperform
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
Direction: money going out (1 week)
Share count change: 1 week: -3.1% (-920.18M) over 7d
Shares outstanding: 313.33M | fund size: 28.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive breakout, fund flows flat, analyst view bullish but limited coverage, fundamentals high valuation temper outlook.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.11 to +0.21) with no surprise
- IGV price above 20‑day, 50‑day, and 200‑day SMAs but volume is low (0.26x 20‑day average) and no decisive breakout
- Fund flows flat over the past week (share count +0.0%) indicating neutral demand
- Analyst coverage of top holdings (43.2% weight) is 100% buy with a modest +5.5% price target

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Expanded Tech-Software Sector ETF (IGV) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/IGV/)  
  <sub>Yahoo Finance Singapore, 8 hours ago</sub>  
  iShares Expanded Tech-Software Sector ETF (IGV) · 1.30% · 4.59% · 32.58% · 0.15% · -7.00% · 26.84% · 955.67%. Key events. Baseline. Advanced chart.
- [3 Software ETFs to Buy as the SaaSpocalypse Bottoms Out](https://www.tradingview.com/news/zacks:7aefc720e094b:0-3-software-etfs-to-buy-as-the-saaspocalypse-bottoms-out/)  
  <sub>TradingView, 3 hours ago</sub>  
  The "SaaSpocalypse" is officially over. What began in early 2026 as a brutal sell-off, driven by existential fears that artificial intelligence (AI) coding...
- [Software's Recovery Is Still Loading](https://seekingalpha.com/article/4949642-software-recovery-is-still-loading)  
  <sub>Seeking Alpha, 13 hours ago</sub>  
  It's been just over a year since the iShares Software ETF peaked on September 22, 2025, and getting back to that level has been a work in progress.
- [iShares Software ETF rallies 43% but still 9.4% below last year's peak](https://pluang.com/en/news-feed/pemulihan-perangkat-lunak-masih-berjalan)  
  <sub>Pluang, 13 hours ago</sub>  
  The iShares Software ETF (IGV) has gained 43% since its peak on September 22, 2025, recovering above its 50- and 200-day moving averages.
- [Behavioral Patterns of IGV and Institutional Flows](https://news.stocktradersdaily.com/news_release/21/Behavioral_Patterns_of_IGV_and_Institutional_Flows_092426100002_1790301602.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Price-action only: Ishares Expanded Tech-software Sector Etf (IGV) movements set the tone for institutional models. Behavioral Patterns of IGV and...
- [UiPath Slides 3%, Extending a 24% Monthly Decline; ServiceNow and Pegasystems Slip](https://247wallst.com/investing/2026/09/24/uipath-slides-3-extending-a-24-monthly-decline-servicenow-and-pegasystems-slip/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  UiPath is sinking again while the broader software sector barely budges, and the automation corner of the market may be telling investors something the...
- [Buy SPY Or QQQ, Hold Software, And Sell Semiconductor (SP500)](https://seekingalpha.com/article/4949491-buy-spy-or-qqq-hold-software-and-sell-semiconductors)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  SOXX's AI-driven valuation premium looks excessive vs IGV and SPY/QQQ.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 106.93 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 105.56 (+1.3%), 50d 101.40 (+5.5%), 200d 93.66 (+14.2%); 50d above 200d
Momentum: RSI(14) 56.0 | MACD 1.387 vs signal 1.360 (histogram 0.028)
Returns: 1d -0.2% | 5d +2.5% | 1m +4.4% | 3m +21.2%
52-week range: 74.67 - 117.08 (now 76.1% of the way up)
Volatility: ATR(14) 2.52 (2.4% of price) | annualised 20d 32.4%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Technology
What it holds: P/E 34.20 | P/B 8.09 | P/S 9.07 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +16.7% a year | beta to the market 1.21
Cost and size: expense ratio 0.38% | net assets 15.74B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: Palantir Technologies Inc Ordinary Shares - Class A 10.3%, Palo Alto Networks Inc 9.7%, Microsoft Corp 9.2%, CrowdStrike Holdings Inc Class A 7.4%, Salesforce Inc 6.6%
Sector mix: Technology 94.4%, Communication services 3.8%, Financial services 1.5%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 43.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.66 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +5.5% above the current prices
Holdings read: PLTR, PANW, MSFT, CRWD, CRM
Recent rating changes among them:
  - PLTR: 2026-09-23 Rosenblatt: main, Buy -> Buy
  - PANW: 2026-09-21 Morgan Stanley: main, Overweight -> Overweight
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
Shares outstanding: 12.50M | fund size: 1.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, modest inflows, strong analyst rating but not enough to outweigh mixed fundamentals and technicals.

**Main reasons it gave:**
- Analyst coverage of top holdings (57.5% weight) shows 100% buy rating and a +26.3% price target
- Fund flows indicate a 1.2% share count increase over the week, showing modest inflows
- Technical indicators: RSI 28.5 (oversold) and MACD histogram positive, yet price remains below 20‑day, 50‑day, and 200‑day SMAs
- Macro data: Treasury yields rose modestly, dollar index up 0.78%, VIX low at 15.42, and inflation and unemployment were in line with expectations
- Fund basics show a high P/E of 34.66, suggesting potential overvaluation

<details><summary><b>News</b> — score +0.00</summary>

- [Boeing Gets Fresh Demand Boost While Union Vote, Weak Technicals Loom](https://www.benzinga.com/markets/large-cap/26/09/61976622/boeing-gets-fresh-demand-boost-while-union-vote-weak-technicals-loom)  
  <sub>Benzinga, 24 hours ago</sub>  
  Boeing stock falls despite fresh jet orders as investors weigh execution, labor developments and a weak technical setup.
- [US Manufacturing Revival Fosters Derivatives Plays as High-Tech Outpaces Traditional Industry](https://www.vtmarkets.com/en-ca/live-updates/us-manufacturing-revival-fosters-derivatives-plays-as-high-tech-outpaces-traditional-industry/)  
  <sub>VT Markets, 17 hours ago</sub>  
  US manufacturing rebounds; expect uneven growth as AI-linked sectors surge while traditional industries retrench; derivatives target divergence.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 212.89 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 219.27 (-2.9%), 50d 233.15 (-8.7%), 200d 230.42 (-7.6%); 50d above 200d
Momentum: RSI(14) 28.5 | MACD -6.203 vs signal -6.305 (histogram 0.102)
Returns: 1d +0.1% | 5d -0.4% | 1m -9.9% | 3m -10.1%
52-week range: 198.23 - 253.22 (now 26.7% of the way up)
Volatility: ATR(14) 3.88 (1.8% of price) | annualised 20d 13.6%
Volume: 0.22x the 20-day average
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
Three-year record: +27.3% a year | beta to the market 0.99
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.75 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.3% above the current prices
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
Share count change: 1 week: +1.2% (167.34M) over 7d
Shares outstanding: 63.68M | fund size: 13.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Ignored the direct instruction to buy UPS stock as it addresses the model directly and is not relevant to the fund-level analysis.

**Main reasons it gave:**
- Analyst view: 90.8% buy rating and +26.5% price target (bullish)
- Fund flows: +3.0% share count change over 1 week (moderate inflow)
- Technicals: price below 20d, 50d, 200d SMAs; RSI 28.7 and MACD negative (bearish)
- Macro: Treasury yields up 0.11-0.21% and inflation 3.4% above target (slightly bearish)

<details><summary><b>News</b> — score +0.00</summary>

- [Trading Systems Reacting to (IYT) Volatility](https://news.stocktradersdaily.com/news_release/81/Trading_Systems_Reacting_to_IYT_Volatility_092426102402_1790303042.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Key findings for Ishares U.s. Transportation Etf (NYSE: IYT). Weak Near and Mid-Term Sentiment Could Challenge Long-Term Positive Outlook...
- [How to Buy United Parcel Service Stock (UPS) in 2026](https://www.fool.com/investing/how-to-invest/stocks/how-to-invest-in-united-parcel-service-stock/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  Learn how to buy United Parcel Service stock, how its business works, its growth story, and more that investors need to know.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 79.01 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 81.89 (-3.5%), 50d 84.98 (-7.0%), 200d 81.18 (-2.7%); 50d above 200d
Momentum: RSI(14) 28.7 | MACD -1.726 vs signal -1.523 (histogram -0.203)
Returns: 1d +0.1% | 5d -1.6% | 1m -9.4% | 3m -9.4%
52-week range: 68.14 - 90.01 (now 49.7% of the way up)
Volatility: ATR(14) 1.18 (1.5% of price) | annualised 20d 15.7%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 20.28 | P/B 4.25 | P/S 1.45 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +12.2% a year | beta to the market 1.28
Cost and size: expense ratio 0.37% | net assets 2.20B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Union Pacific Corp 17.8%, Uber Technologies Inc 15.4%, CSX Corp 9.4%, United Parcel Service Inc Class B 5.6%, Norfolk Southern Corp 4.9%
Sector mix: Industrials 83.8%, Technology 16.2%
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
Rolled up from the 5 largest holdings, 53.1% of the fund by weight
Ratings by weight: buy 90.8% | hold 9.2% | sell 0.0% (mean 1.84 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.5% above the current prices
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
Share count change: 1 week: +3.0% (64.31M) over 7d
Shares outstanding: 27.50M | fund size: 2.17B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no material macro surprise, policy shift, or decisive technical breakout is present. Analyst view and recent inflows are modestly bullish, while fundamentals and technicals are slightly bearish, offsetting each other.

**Main reasons it gave:**
- Analyst view: 90% buy, price target +17% (covers 44.4% of fund)
- Fund flows: share count +1.5% over 7 days indicating net inflows
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 35 (oversold) but no decisive breakout
- Fundamentals: moderate valuation (P/E 15) and low three‑year return (+1.6%/yr) with high expense ratio (0.75%)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 37.03 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 37.92 (-2.3%), 50d 37.80 (-2.0%), 200d 38.14 (-2.9%); 50d below 200d
Momentum: RSI(14) 35.2 | MACD -0.307 vs signal -0.173 (histogram -0.134)
Returns: 1d +0.4% | 5d -1.1% | 1m -6.2% | 3m -2.0%
52-week range: 35.83 - 41.03 (now 23.2% of the way up)
Volatility: ATR(14) 0.29 (0.8% of price) | annualised 20d 8.1%
Volume: 0.22x the 20-day average
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
Three-year record: +1.6% a year | beta to the market 0.18
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 44.4% of the fund by weight
Ratings by weight: buy 90.0% | hold 10.0% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.0% above the current prices
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
Share count change: 1 week: +1.5% (9.59M) over 7d
Shares outstanding: 17.11M | fund size: 633.67M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: bullish analyst coverage of top holdings (+53.9% price target) covering 32% of the fund, modestly positive fundamentals (low P/E, decent 3‑yr return), but recent outflows of 1.7% of shares and bearish technicals (price below 20‑, 50‑, 200‑day SMAs, RSI 40, low volume). Macro conditions are neutral with no policy surprise. These offsetting factors lead to a neutral overall stance.

**Main reasons it gave:**
- Fund flows show 1.7% share outflow over the week (bearish sentiment)
- Analyst coverage of top holdings is 100% buy with +53.9% price target (bullish for 32% of fund)
- Technicals indicate the ETF is below 20‑, 50‑, 200‑day SMAs, RSI 40, low volume (bearish momentum)
- Macro environment: yields rising, dollar up, VIX low, no major policy surprise (neutral macro)

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://finance.yahoo.com/markets/stocks/articles/stocktwits-passport-portfolio-qqq-weekly-060930878.html)  
  <sub>Yahoo Finance, 9 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.
- [Four Reasons Why FLCH Is Back To Being A 'BUY Rating' For Me (NYSEARCA:FLCH)](https://seekingalpha.com/article/4949565-four-reasons-why-flch-is-back-to-being-a-buy-rating-for-me?source=google_editors_picks)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The Franklin FTSE China ETF is upgraded to BUY, driven by attractive valuations and a favorable risk/reward profile. Click for more on FLCH.
- [Trump-Xi summit: No breakthrough beyond trade truce extension](https://seekingalpha.com/news/4646978-trump-xi-summit-key-takeaways)  
  <sub>Seeking Alpha, 6 hours ago</sub>  
  China's President Xi Jinping will wrap up his state visit to the U.S. on Friday, but the trip did not yield major breakthroughs beyond the two-month...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 52.58 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 53.62 (-1.9%), 50d 54.45 (-3.4%), 200d 57.04 (-7.8%); 50d below 200d
Momentum: RSI(14) 40.1 | MACD -0.444 vs signal -0.411 (histogram -0.033)
Returns: 1d -0.5% | 5d -0.9% | 1m -4.6% | 3m +4.2%
52-week range: 50.48 - 66.99 (now 12.7% of the way up)
Volatility: ATR(14) 0.62 (1.2% of price) | annualised 20d 15.7%
Volume: 0.31x the 20-day average
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
Three-year record: +9.2% a year | beta to the market 0.44
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 32.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +53.9% above the current prices
Holdings read: 0700.HK, 9988.HK, 00939, 01398, 1810.HK
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
Share count change: 1 week: -1.7% (-103.75M) over 7d
Shares outstanding: 116.37M | fund size: 6.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The analyst view is strongly bullish (100% buy rating, +36.2% price target) while fund flows show a sharp outflow of -11% share count (≈$8.35 B) over the past week, creating a bearish pressure. Technicals are moderately bullish (price above 20‑, 50‑, 200‑day SMAs, RSI 62.4) but volume is low, and macro conditions show no surprise data or policy shift. The bullish analyst signal is offset by bearish flow and neutral fundamentals, leading to a neutral overall stance.

**Main reasons it gave:**
- Analyst view: 100% buy rating and weighted price target +36.2% above current price
- Fund flows: share count down -11% (≈$8.35B outflows) over the past week
- Technicals: price above 20‑day, 50‑day, 200‑day SMAs, RSI 62.4, but volume only 0.32× 20‑day average
- Macro: modest rise in Treasury yields, VIX low at 15.42, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [VanEck Semiconductor ETF (Derivatives) Price (SMH/USD) Today | Live Price, Market Cap & Chart](https://www.binance.com/en/price/vaneck-semiconductor-etf-derivatives)  
  <sub>Binance, 17 hours ago</sub>  
  The current price of VanEck Semiconductor ETF (Derivatives) (SMH) is $600.32. Top cryptocurrency prices are updated in real-time on Binance's price directory.
- [Why Semiconductor Investors Are Rotating From SMH's Nvidia Concentration to PSI's Equal-Weight Approach](https://247wallst.com/investing/etf/2026/09/24/why-semiconductor-investors-are-rotating-from-smhs-nvidia-concentration-to-psis-equal-weight-approach/)  
  <sub>24/7 Wall St., 18 hours ago</sub>  
  SMH has long been the go-to semiconductor ETF, but a quieter rival with a radically different weighting structure beat it by a stunning margin over the past...
- [EXCLUSIVE: Why AI Semiconductor Stocks Are a 'Dangerous Playground' For Investors](https://www.benzinga.com/markets/tech/26/09/61981929/ai-semiconductor-stocks-dangerous-playground)  
  <sub>Benzinga, 21 hours ago</sub>  
  MarketVector's Josh Kaplan calls AI semiconductor stocks a “dangerous playground” as investors rotate across an increasingly crowded trade.
- [Semiconductor ETF PSI outperforms SMH by 20% du...](https://pluang.com/en/news-feed/mengapa-investor-semi-konversi-dari-smh-nvidia-ke-psi-pendekatan-berat-seimbang)  
  <sub>Pluang, 18 hours ago</sub>  
  The Invesco Semiconductors ETF (PSI) has outperformed the VanEck Semiconductor ETF (SMH) by over 20 percentage points in the past year.
- [Chip Equipment Makers Are Leading a New Leg of the AI Rally](https://startupfortune.com/chip-equipment-makers-are-leading-a-new-leg-of-the-ai-rally/)  
  <sub>Startup Fortune, 11 hours ago</sub>  
  Tokyo Electron, Advantest and Lasertec surged as investors rotated from Nvidia-heavy SMH into equal-weight chip ETF PSI amid record 2026 equipment.
- [S&P 500, Dow, Nasdaq Futures Ease As Treasury Yields Continue To Spike — ORCL, META, AKAM, GOOGL, MGM In Focus](https://www.tradingview.com/news/stocktwits:91f0cfca1094b:0-s-p-500-dow-nasdaq-futures-ease-as-treasury-yields-continue-to-spike-orcl-meta-akam-googl-mgm-in-focus/)  
  <sub>TradingView, 15 hours ago</sub>  
  The Dow Jones index ended lower on Thursday as Treasury yields continued their upward march amid hawkish remarks from Federal Reserve officials.
- [S&P 500 Eyes Midterm Rally: ETFs to Watch in October 2026 - State Street SPDR S&P 500 ETF Trust (ARCA:SPY](https://www.benzinga.com/etfs/sector-etfs/26/09/61984746/sampp-500s-midterm-rally-setup-is-getting-interesting-these-etfs-could-hold-clues?utm_source=googlefinance)  
  <sub>Benzinga, 19 hours ago</sub>  
  The S&P 500 enters a historically strong October-November stretch. Here's how ETFs could reveal the rally's real drivers.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 605.57 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 568.78 (+6.5%), 50d 565.87 (+7.0%), 200d 493.28 (+22.8%); 50d above 200d
Momentum: RSI(14) 62.4 | MACD 9.120 vs signal 3.121 (histogram 5.999)
Returns: 1d +0.8% | 5d +5.7% | 1m +9.0% | 3m -1.0%
52-week range: 321.06 - 668.91 (now 81.8% of the way up)
Volatility: ATR(14) 16.09 (2.7% of price) | annualised 20d 34.4%
Volume: 0.32x the 20-day average
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
Three-year record: +62.5% a year | beta to the market 2.06
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 49.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +36.2% above the current prices
Holdings read: NVDA, TSM, AVGO, MU, AMD
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - TSM: 2026-09-02 Stifel: init, ? -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-24 Rosenblatt: main, Buy -> Buy
  - AMD: 2026-09-25 B of A Securities: main, Buy -> Buy
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
Direction: money going out (1 week)
Share count change: 1 week: -11.0% (-8.35B) over 7d
Shares outstanding: 111.56M | fund size: 67.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, technicals show no decisive breakout, analyst view bullish but limited coverage.

**Main reasons it gave:**
- US Treasury yields rose modestly across the curve (+0.11 to +0.21) with no policy surprise
- Fund flows flat over the week (share count +0.0%) indicating no net demand
- Price below 20‑day, 50‑day, 200‑day SMAs; RSI 35.3, MACD negative, no decisive breakout
- Analyst coverage limited to 39.5% of fund, rating 100% buy with +18.5% price target

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Turkey ETF (TUR) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TUR/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  iShares MSCI Turkey ETF (TUR) · -2.94% · -9.59% · -4.66% · 6.30% · 3.65% · 74.65% · -26.08%. Key Events. Baseline. Advanced Chart.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 36.37 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 38.79 (-6.2%), 50d 39.09 (-7.0%), 200d 39.33 (-7.5%); 50d below 200d
Momentum: RSI(14) 35.3 | MACD -0.773 vs signal -0.466 (histogram -0.307)
Returns: 1d -0.6% | 5d -2.4% | 1m -10.4% | 3m -7.2%
52-week range: 31.90 - 43.74 (now 37.8% of the way up)
Volatility: ATR(14) 0.74 (2.0% of price) | annualised 20d 35.3%
Volume: 0.52x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Focused Region
What it holds: P/E 13.81 | P/B 1.21 | P/S 0.66 | 3y earnings growth n/a
Yield: 2.1%
Three-year record: +2.1% a year | beta to the market 0.44
Cost and size: expense ratio 0.59% | net assets 225.08M
What it is made of: Stocks 100.4%, Cash -0.4%
Largest holdings: Aselsan Elektronik Sanayi Ve Ticaret AS 11.2%, Tupras-Turkiye Petrol Rafineleri AS 9.7%, Bim Birlesik Magazalar AS 8.7%, Akbank TAS 5.6%, Turk Hava Yollari AO 4.4%
Sector mix: Industrials 31.2%, Financial services 14.7%, Consumer defensive 11.9%, Basic materials 11.1%
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
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.5% above the current prices
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
Shares outstanding: 15.65M | fund size: 569.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> The fund shows mixed signals: bullish analyst consensus (+19.3% price target) and modest net inflows (+0.7% share count) are offset by rising Treasury yields (10‑yr at 5.21% vs fund yield 3.6%) and a bearish technical picture (price below 20‑, 50‑, and 200‑day SMAs, RSI 25.6). No clear macro surprise or decisive technical break is present, so the overall stance remains neutral.

**Main reasons it gave:**
- 10-year Treasury yield rose 21 bps to 5.21%, higher than the fund's 3.6% yield – pressure on REIT valuations
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 25.6 indicating bearish momentum
- Share count increased 0.7% over the week, indicating modest net inflows
- Analyst consensus 100% buy with a weighted price target +19.3% above current price – bullish sentiment

<details><summary><b>News</b> — score +0.20</summary>

- [JPMorgan Turns Contrarian on Interest Rates, Upgrades 3 REITs](https://www.benzinga.com/real-estate/reit/26/09/61992066/jpmorgan-turns-contrarian-on-interest-rates-upgrades-3-reits)  
  <sub>Benzinga, 4 hours ago</sub>  
  Why is JPMorgan bullish on REITs despite high Treasury yields? Explore their contrarian upgrades on WELL, MAC, and EGP.
- [A $1 Million VOO Holder Owes Tax on $10,450 in Dividends He Never Saw Because He Reinvested Them](https://247wallst.com/investing/etf/2026/09/24/a-1-million-voo-holder-owes-tax-on-10450-in-dividends-he-never-saw-because-he-reinvested-them/)  
  <sub>24/7 Wall St., 17 hours ago</sub>  
  Your broker reinvests every VOO dividend automatically, so you never see the cash, but the IRS sees it just fine. The tax bill hiding inside a taxable...
- [3 Vanguard ETFs Flying Under the Radar with 20% Upside](https://www.tipranks.com/news/3-vanguard-etfs-flying-under-the-radar-with-20-upside)  
  <sub>TipRanks, 60 minutes ago</sub>  
  Vanguard ETFs are often known for their low costs and long-term stability, but not all of them get the attention they deserve. Some lesser-known Vanguard...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 90.56 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 94.37 (-4.0%), 50d 97.06 (-6.7%), 200d 94.35 (-4.0%); 50d above 200d
Momentum: RSI(14) 25.6 | MACD -1.592 vs signal -1.264 (histogram -0.328)
Returns: 1d -0.7% | 5d -2.5% | 1m -8.2% | 3m -8.2%
52-week range: 87.00 - 100.95 (now 25.5% of the way up)
Volatility: ATR(14) 1.13 (1.2% of price) | annualised 20d 11.9%
Volume: 0.61x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

```text
Fund type: Real Estate
What it holds: P/E 30.19 | P/B 2.59 | P/S 4.94 | 3y earnings growth n/a
Yield: 3.6%
Three-year record: +10.3% a year | beta to the market 0.98
Cost and size: expense ratio 0.13% | net assets 70.82B
What it is made of: Stocks 99.1%, Cash 0.7%, Other 0.2%
Largest holdings: Vanguard Real Estate II Index 14.5%, Welltower Inc 8.7%, Prologis Inc 6.9%, Equinix Inc 5.5%, American Tower Corp 4.3%
Sector mix: Real estate 99.4%, Communication services 0.4%, Energy 0.1%, Industrials 0.0%
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
Rolled up from the 5 largest holdings, 39.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.3% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
  - EQIX: 2026-09-21 Rothschild & Co: init, ? -> Buy
  - AMT: 2026-08-20 Barclays: up, Equal-Weight -> Overweight
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
Share count change: 1 week: +0.7% (479.46M) over 7d
Shares outstanding: 756.41M | fund size: 68.50B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, technicals show no decisive break, analyst view is mixed, and modest outflows do not dominate the picture.

**Main reasons it gave:**
- Weekly fund outflows of -2.6% (≈$295M) indicate modest bearish pressure
- Analyst ratings: 43% buy, 57% hold, no sell, weighted price target -19.2% suggests mixed sentiment
- Technicals: price below 20‑day (159.17) and 50‑day (157.73) SMAs, RSI 44.1, MACD negative, volume 0.28× 20‑day average
- Macro: yields up modestly, VIX low at 15.42, no data surprise

<details><summary><b>News</b> — score +0.00</summary>

- [SBIO ETF rated Sell due to overvaluation and hi...](https://pluang.com/en/news-feed/sbio-pipeline-menjanjikan-potensi-pengembalian-tidak-memadai)  
  <sub>Pluang, 9 hours ago</sub>  
  The SBIO ETF is rated Sell because its market price of $62.22 significantly exceeds its fair net asset value (NAV) of $37.86, indicating overvaluation.
- [Biotech: The Party's Over, The Top Is In (NYSEARCA:XBI)](https://seekingalpha.com/article/4949579-biotech-the-partys-over-the-top-is-in)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Summary. The State Street SPDR S&P Biotech ETF has likely peaked after a 60% rally over the past year. Key tailwinds—practice-changing drug approvals,...
- [Biotech ETF XBI likely peaked after 60% rally a...](https://pluang.com/en/news-feed/bioteknologi-puncak-pasar-sudah-lewati)  
  <sub>Pluang, 18 hours ago</sub>  
  The State Street SPDR S&P Biotech ETF (XBI) has likely reached its peak following a strong 60% rally over the past year. This surge was driven by factors...
- [Arcturus Gets Citi Upgrade After Positive Liver Disease Study Data – But BTIG Says Therapy’s Benefit Is Hard To Measure](https://finance.yahoo.com/healthcare/articles/arcturus-gets-citi-upgrade-positive-175912535.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Arcturus is developing ARCT-810 for patients with OTCD, a rare genetic disorder in which the liver cannot properly remove toxic ammonia from the blood.
- [SBIO: Promising Pipelines, Insufficient Return Potential](https://seekingalpha.com/article/4949662-sbio-promising-pipelines-insufficient-return-potential)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  SBIO should be treated as a speculative satellite holding; broader ETFs like XBI or IBB offer more balanced risk and maturity profiles.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 155.00 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 159.17 (-2.6%), 50d 157.73 (-1.7%), 200d 137.99 (+12.3%); 50d above 200d
Momentum: RSI(14) 44.1 | MACD -0.943 vs signal -0.371 (histogram -0.572)
Returns: 1d -0.7% | 5d -1.1% | 1m -8.0% | 3m -0.2%
52-week range: 95.86 - 169.55 (now 80.3% of the way up)
Volatility: ATR(14) 4.23 (2.7% of price) | annualised 20d 27.1%
Volume: 0.28x the 20-day average
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
Three-year record: +28.9% a year | beta to the market 1.12
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

<details><summary><b>What analysts and big funds say</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.00</summary>

```text
Rolled up from the 5 largest holdings, 9.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 43.2% | hold 56.8% | sell 0.0% (mean 2.28 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -19.2% above the current prices
Holdings read: MRNA, TWST, APGE, KYMR, HALO
Recent rating changes among them:
  - MRNA: 2026-09-03 Rothschild & Co: down, Neutral -> Sell
  - TWST: 2026-09-18 BWS Financial: main, Sell -> Sell
  - APGE: 2026-08-13 Truist Securities: main, Hold -> Hold
  - KYMR: 2026-09-22 Stifel: main, Buy -> Buy
  - HALO: 2026-09-02 HC Wainwright & Co.: reit, Buy -> Buy
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
Share count change: 1 week: -2.6% (-294.73M) over 7d
Shares outstanding: 70.47M | fund size: 10.92B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bullish analyst coverage (+21.7% price target) versus bearish fund outflows and high mortgage rates; fundamentals are neutral.

**Main reasons it gave:**
- Mortgage rates exceed 7% for first time since Jan 2025
- Fund flows show -1.2% share count decline over 1 week
- Analyst coverage of top holdings: 78.9% buy, price target +21.7% above current price
- Price below 20‑day, 50‑day, and 200‑day SMAs
- RSI at 38.9 indicating oversold conditions

<details><summary><b>News</b> — score +0.00</summary>

- [Mortgage rates exceed 7% mark after over one-and-a-half years (XLRE:NYSEARCA)](https://seekingalpha.com/news/4646784-mortgage-rates-exceed-7-mark-after-over-one-and-a-half-years)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Mortgage rates surpassed the 7% threshold for the first time since January 2025, according to the Weekly Mortgage Applications Survey.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 97.07 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 99.18 (-2.1%), 50d 104.15 (-6.8%), 200d 106.42 (-8.8%); 50d below 200d
Momentum: RSI(14) 38.9 | MACD -2.229 vs signal -2.332 (histogram 0.103)
Returns: 1d +0.3% | 5d +0.7% | 1m -8.4% | 3m -16.1%
52-week range: 94.86 - 121.36 (now 8.3% of the way up)
Volatility: ATR(14) 2.08 (2.1% of price) | annualised 20d 22.4%
Volume: 0.20x the 20-day average
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
Three-year record: +9.3% a year | beta to the market 1.46
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
Ratings by weight: buy 78.9% | hold 21.1% | sell 0.0% (mean 2.15 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +21.7% above the current prices
Holdings read: IBP, OC, ALLE, SKY, WSM
Recent rating changes among them:
  - IBP: 2026-09-25 Evercore ISI Group: main, In-Line -> In-Line
  - OC: 2026-09-11 Wells Fargo: main, Overweight -> Overweight
  - ALLE: 2026-08-10 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - SKY: 2026-08-06 UBS: main, Buy -> Buy
  - WSM: 2026-09-09 Evercore ISI Group: main, In-Line -> In-Line
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
Share count change: 1 week: -1.2% (-15.49M) over 7d
Shares outstanding: 13.40M | fund size: 1.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – bullish analyst view is offset by weak technicals, flat fund flows and no macro catalyst.

**Main reasons it gave:**
- XLB trading below 20‑day SMA (51.16) and 50‑day SMA (51.70), RSI 36.6, MACD -0.649 (bearish technicals)
- Analyst coverage of top holdings (37% of fund) is 100% buy with weighted price target +13.7% (bullish analyst view)
- Fund flows flat: share count unchanged (+0.0%) over the past week (neutral insider sentiment)
- Macro environment stable: Treasury yields rose modestly, no surprise in inflation or unemployment, VIX low at 15.42 (no macro catalyst)

<details><summary><b>News</b> — score +0.00</summary>

- [9 Of 11 Sectors Fall In Friday Trading As Cyclicals Lead](https://www.benzinga.com/trading-ideas/movers/26/09/61998944/9-of-11-sectors-fall-in-friday-trading-as-cyclicals-lead)  
  <sub>Benzinga, 18 minutes ago</sub>  
  Friday's regular session has two sectors higher and nine lower, with growth and cyclical sectors split across the top three positions.
- [S&P 500’s Midterm Rally Setup Is Getting Interesting: These ETFs Could Hold the Clues](https://www.tradingview.com/news/benzinga:8356427a1094b:0-s-p-500-s-midterm-rally-setup-is-getting-interesting-these-etfs-could-hold-the-clues/)  
  <sub>TradingView, 19 hours ago</sub>  
  The U.S. stock market is entering a historically stronger stretch of the midterm-election cycle, but the next leg of the rally may have less to do with...
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 49.66 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 51.16 (-2.9%), 50d 51.70 (-3.9%), 200d 50.54 (-1.8%); 50d above 200d
Momentum: RSI(14) 36.6 | MACD -0.649 vs signal -0.495 (histogram -0.154)
Returns: 1d -0.0% | 5d -0.7% | 1m -7.5% | 3m -3.8%
52-week range: 42.23 - 53.67 (now 64.9% of the way up)
Volatility: ATR(14) 0.73 (1.5% of price) | annualised 20d 14.4%
Volume: 0.35x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Natural Resources
What it holds: P/E 24.59 | P/B 3.00 | P/S 2.01 | 3y earnings growth n/a
Yield: 1.6%
Three-year record: +10.8% a year | beta to the market 0.82
Cost and size: expense ratio 0.08% | net assets 8.75B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Linde PLC 13.1%, Newmont Corp 7.8%, Freeport-McMoRan Inc 6.3%, Corteva Inc 4.9%, Air Products and Chemicals Inc 4.8%
Sector mix: Basic materials 84.5%, Consumer cyclical 15.5%
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
Rolled up from the 5 largest holdings, 37.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.70 on a 1=strong buy to 5=strong sell scale)
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
Shares outstanding: 71.92M | fund size: 3.57B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, mixed fundamentals, flat flows, and technicals show no decisive break.

**Main reasons it gave:**
- Fund flows flat: share count unchanged (+0.0% week)
- Energy inventories: crude oil +3.0M barrels (build) and natural gas +53 BCF (build) – bearish
- EIA price outlook: WTI forecast down 10% over six months – bearish
- Analyst view: 100% buy rating, +6.6% price target, covering 51.7% of fund – bullish
- Technical indicators: MACD below signal, RSI 44.9, volume 0.37x 20‑day average – no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Midstream ETFs Gather $1.1B in Flows Amid Energy Volatility](https://etfdb.com/energy-infrastructure-content-hub/midstream-etfs-gather-11b-flows/)  
  <sub>ETF Database, 19 hours ago</sub>  
  Discover why midstream ETFs like AMLP and ENFR are gathering strong net flows and delivering attractive income yield in 2026.
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...
- [SLB Lands Multi-Year Saudi Aramco Deals For 450-Plus Wells](https://www.benzinga.com/markets/large-cap/26/09/61980898/slb-lands-multi-year-saudi-aramco-deals-for-450-plus-wells)  
  <sub>Benzinga, 21 hours ago</sub>  
  SLB secured multi-year Saudi Aramco contracts to provide end-to-end well construction services supporting oil and gas development across Saudi Arabia.
- [Exchange-Traded Funds, Equity Futures up Pre-Bell Friday as Treasury Yields Rise, Oil Prices Fall](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-equity-futures-132448177.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was up 0.3%, and the actively tra.
- [Sector Update: Energy Stocks Rise Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-rise-afternoon-195809963.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks rose late Thursday afternoon with the NYSE Energy Sector Index gaining 0.4% and the State Street Energy Select Sector SPDR ETF (XLE) adding...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 62.12 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 64.00 (-2.9%), 50d 61.76 (+0.6%), 200d 56.14 (+10.7%); 50d above 200d
Momentum: RSI(14) 44.9 | MACD 0.157 vs signal 0.654 (histogram -0.497)
Returns: 1d -0.8% | 5d -3.4% | 1m -0.5% | 3m +15.4%
52-week range: 42.61 - 65.93 (now 83.7% of the way up)
Volatility: ATR(14) 1.26 (2.0% of price) | annualised 20d 21.7%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.35</summary>

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

<details><summary><b>Does this company beat its own forecasts</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What holding this fund costs you</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.35</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Crude oil: 426.4 million barrels, +3.0 on the week (a build), 58% percentile over 52 weeks
  Petrol: 206.0 million barrels, -1.7 on the week (a draw), 8% percentile over 52 weeks -- low for the time of year
  Diesel: 107.4 million barrels, -0.4 on the week (a draw), 33% percentile over 52 weeks
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
A build is more supply than demand and a draw is the reverse, so a build reads bearish and a draw bullish -- as a rule of thumb, not a law. Weigh the change and how unusual the level is above the level itself, and remember the market has already seen this number.
```

</details>

<details><summary><b>How the crop is growing</b> — score -0.35</summary>

_Not available today._

</details>

<details><summary><b>What analysts and big funds say</b> — score +0.55</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.55</summary>

```text
Rolled up from the 5 largest holdings, 51.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.05 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +6.6% above the current prices
Holdings read: XOM, CVX, COP, MPC, PSX
Recent rating changes among them:
  - XOM: 2026-09-03 Piper Sandler: main, Neutral -> Neutral
  - CVX: 2026-09-25 HSBC: main, Buy -> Buy
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
Shares outstanding: 186.42M | fund size: 11.58B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no clear macro surprise or decisive technical break. Analyst coverage is bullish, but fund flows are flat and technicals show mixed short‑term momentum.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +13.1% above current price
- Fund flows: flat share count change (+0.0%) over the past week
- Technical indicators: price below 20‑day SMA (56.58) and 50‑day SMA (57.04), RSI 28.2, MACD -0.713
- Macro data: Treasury yields rose (3‑month +0.11, 5‑year +0.18, 10‑year +0.21) and market pricing ~4 Fed hikes
- News: Quant screen flags 13 financial stocks as Sell/Strong Sell for 60+ days

<details><summary><b>News</b> — score +0.00</summary>

- [These financials stocks are trapped longest in bearish Quant ratings (XLF:NYSEARCA)](https://seekingalpha.com/news/4647029-these-financials-stocks-are-trapped-longest-in-bearish-quant-ratings)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Quant screen flags 13 financial-sector stocks rated Sell/Strong Sell for 60+ days amid shifting rates and credit.
- [S&P 500, Nasdaq, Dow Futures Edge Higher Ahead Of Fed Rate Decision: INTC, SNAP, SOFI, RUM In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-dow-futures-edge-higher-ahead-of-fed-rate-decision/cZK0WgFR74u)  
  <sub>Stocktwits, 9 hours ago</sub>  
  The Dow surged to a fresh intraday record on Tuesday before finishing at an all-time closing high, marking its second straight record close.
- [Sector Update: Financial Stocks Softer Late Afternoon](https://www.bitget.com/amp/news/detail/12560605870394)  
  <sub>Bitget, 14 hours ago</sub>  
  03:54 PM EDT, 09/24/2026 (MT Newswires) -- Financial stocks were lower in late Thursday afternoon trading, with the NYSE Financial Index and the State Stree...
- [Klarna Falls 3% as Selling Persists Weeks After Its Guidance Cut; Affirm Advances 2%](https://247wallst.com/investing/2026/09/24/klarna-falls-3-as-selling-persists-weeks-after-its-guidance-cut-affirm-advances-2/)  
  <sub>24/7 Wall St., 23 hours ago</sub>  
  Klarna keeps sliding weeks after a guidance cut rattled investors, while Affirm moves in the opposite direction as traders rally around its AI underwriting...
- [Form 4 iShares Russell 2000 ETF For: 24 September By Investing.com](https://uk.investing.com/news/stock-market-news/form-4-ishares-russell-2000-etf-for-24-september-93CH-4882013)  
  <sub>Investing.com UK, 22 hours ago</sub>  
  The Senior Autocallable Contingent Coupon Barrier Notes due September 27, 2032 Linked to the Worst-Performing of the iShares <sup>®</sup> Russell 2000 <sup>®</sup> ETF,...
- [Webcast: Mining’s new math: Power, compute, and sustainability | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/28/minings-new-math-power-compute-and-sustainability?partnerref=APWebinarLandingPage)  
  <sub>Advisor Perspectives, 33 minutes ago</sub>  
  Join industry experts from CoinShares for an educational webcast exploring the future landscape of bitcoin mining enterprises.
- [Sector Update: Financial](https://finance.yahoo.com/markets/stocks/articles/sector-financial-192823046.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Financial stocks were softer in late Thursday afternoon trading, with the NYSE Financial Index and the State Street Financial Select Sector SPDR ETF (XLF)...
- [Sector Update: Financial Stocks Decrease in Afternoon Trading](https://finance.yahoo.com/markets/stocks/articles/sector-financial-stocks-decrease-afternoon-181109505.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Financial stocks were softer in Thursday afternoon trading, with the NYSE Financial Index and the State Street Financial Select Sector SPDR ETF (XLF) each...
- [Webcast: Navigating a Changing Rate Environment | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/06/navigating-a-changing-rate-environment?partnerref=APWebinarLandingPage)  
  <sub>Advisor Perspectives, 20 hours ago</sub>  
  Rising rate environments can create all sorts of challenges for traditional bond portfolios, but they also open the door for certain opportunities.
- [These 3 ETFs Could Deliver 11%+ Returns, Says the AI Analyst](https://www.tipranks.com/news/these-3-etfs-could-deliver-11-returns-says-the-ai-analyst)  
  <sub>TipRanks, 21 hours ago</sub>  
  TipRanks' ETF AI Analyst expects the Financial Select Sector SPDR Fund ($XLF), Schwab U.S. Broad Market ETF ($SCHB), and Calvert U.S. Large-Cap Core...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 54.51 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 56.58 (-3.7%), 50d 57.04 (-4.4%), 200d 53.73 (+1.5%); 50d above 200d
Momentum: RSI(14) 28.2 | MACD -0.713 vs signal -0.408 (histogram -0.305)
Returns: 1d -0.0% | 5d -2.4% | 1m -6.4% | 3m +1.8%
52-week range: 47.81 - 58.56 (now 62.3% of the way up)
Volatility: ATR(14) 0.71 (1.3% of price) | annualised 20d 13.1%
Volume: 0.22x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Financial
What it holds: P/E 16.36 | P/B 2.42 | P/S 3.50 | 3y earnings growth n/a
Yield: 1.4%
Three-year record: +19.3% a year | beta to the market 0.71
Cost and size: expense ratio 0.08% | net assets 54.59B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: JPMorgan Chase & Co 11.7%, Berkshire Hathaway Inc Class B 11.3%, Visa Inc Class A 7.7%, Mastercard Inc Class A 5.8%, Bank of America Corp 5.0%
Sector mix: Financial services 98.1%, Technology 1.6%, Industrials 0.3%
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
Rolled up from the 5 largest holdings, 41.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.1% above the current prices
Holdings read: JPM, BRK-B, V, MA, BAC
Recent rating changes among them:
  - JPM: 2026-08-14 Wells Fargo: main, Overweight -> Overweight
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
Shares outstanding: 883.44M | fund size: 48.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, mixed technicals, bullish analyst view limited to ~26% of fund, and flat fund flows.

**Main reasons it gave:**
- No macro surprise; yields rose modestly across the curve (+0.11 to +0.21) without shock
- Technical indicators mixed: price below 20‑day, 50‑day, and 200‑day SMAs, RSI 36.3, MACD bullish cross, low volume (0.26× avg)
- Analyst view bullish (100% buy, +23.8% price target) but covers only 25.8% of fund weight
- Fund flows flat (share count +0.0% over 1 week), indicating no net demand

<details><summary><b>News</b> — score +0.00</summary>

- [9 Of 11 Sectors Fall In Friday Trading As Cyclicals Lead](https://www.benzinga.com/trading-ideas/movers/26/09/61998944/9-of-11-sectors-fall-in-friday-trading-as-cyclicals-lead)  
  <sub>Benzinga, 17 minutes ago</sub>  
  Friday's regular session has two sectors higher and nine lower, with growth and cyclical sectors split across the top three positions.
- [XLU ETF Hits a 52-Week Low as 5% Treasuries Reset Utility Valuations](https://www.ebc.com/forex/xlu-etf-hits-52-week-low-treasuries-reset-utility-valuations)  
  <sub>EBC Financial Group, 8 hours ago</sub>  
  XLU ETF's fresh 52-week low reflects a reset in utility valuations and financing costs, not weakening electricity demand. The fund closed at $39.36 on...
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...
- [Webcast: Mining’s new math: Power, compute, and sustainability | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/28/minings-new-math-power-compute-and-sustainability?partnerref=APWebinarLandingPage)  
  <sub>Advisor Perspectives, 37 minutes ago</sub>  
  Join industry experts from CoinShares for an educational webcast exploring the future landscape of bitcoin mining enterprises.
- [Exchange-Traded Funds Mixed, US Equities Decline After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-mixed-us-171353361.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded fund IWM fell and IVV edged higher. Actively traded Invesco QQQ Trust (QQQ) added 0.1%.
- [S&P 500 Erases Losses as US, Iran Reportedly Discuss Hormuz Deal: Stock Market Today](https://www.tradingview.com/news/benzinga:8276f3b88094b:0-s-p-500-erases-losses-as-us-iran-reportedly-discuss-hormuz-deal-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 clawed back most of its morning decline at midday Thursday after sources told Reuters that U.S. and Iranian negotiators meeting in New York are...
- [Webcast: Navigating a Changing Rate Environment | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/06/navigating-a-changing-rate-environment?partnerref=APWebinarLandingPage)  
  <sub>Advisor Perspectives, 20 hours ago</sub>  
  Rising rate environments can create all sorts of challenges for traditional bond portfolios, but they also open the door for certain opportunities.
- [GE Aerospace Stock Faces Pressure As Jefferies Cuts Price Target](https://www.benzinga.com/markets/large-cap/26/09/61979916/ge-aerospace-stock-faces-pressure-as-jefferies-cuts-price-target)  
  <sub>Benzinga, 22 hours ago</sub>  
  GE Aerospace stock rebounds after Jefferies trims its target; strong services backlog and engine demand support the longer-term outlook.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 169.55 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 171.59 (-1.2%), 50d 177.89 (-4.7%), 200d 172.02 (-1.4%); 50d above 200d
Momentum: RSI(14) 36.3 | MACD -2.615 vs signal -2.758 (histogram 0.143)
Returns: 1d +0.4% | 5d -0.1% | 1m -6.0% | 3m -6.4%
52-week range: 147.83 - 186.51 (now 56.2% of the way up)
Volatility: ATR(14) 2.25 (1.3% of price) | annualised 20d 12.3%
Volume: 0.26x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

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
Rolled up from the 5 largest holdings, 25.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
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
Shares outstanding: 136.63M | fund size: 23.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: analysts bullish (+25% price target) but fund flows negative (‑6.1% share count), technicals bullish yet volume low; macro stable with no surprise data.

**Main reasons it gave:**
- Analyst view bullish: weighted price target +25.2% above current price
- Fund flows negative: share count down 6.1% over 1 week
- Technical momentum bullish: RSI 65.1, MACD positive, price near 52‑week high
- Macro stable: yields up modestly, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 196.11 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 188.41 (+4.1%), 50d 184.47 (+6.3%), 200d 163.68 (+19.8%); 50d above 200d
Momentum: RSI(14) 65.1 | MACD 2.871 vs signal 1.891 (histogram 0.980)
Returns: 1d +0.7% | 5d +3.4% | 1m +7.3% | 3m +8.3%
52-week range: 127.50 - 198.21 (now 97.0% of the way up)
Volatility: ATR(14) 3.29 (1.7% of price) | annualised 20d 19.4%
Volume: 0.32x the 20-day average
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
Three-year record: +34.3% a year | beta to the market 1.50
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 45.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.55 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +25.2% above the current prices
Holdings read: NVDA, AAPL, MSFT, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - AAPL: 2026-09-23 B of A Securities: reit, Buy -> Buy
  - MSFT: 2026-09-23 Stifel: up, Hold -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-09-24 Rosenblatt: main, Buy -> Buy
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
Direction: money going out (1 week)
Share count change: 1 week: -6.1% (-7.92B) over 7d
Shares outstanding: 618.75M | fund size: 121.34B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise or decisive technical break occurred; analyst view is bullish but offset by weak technicals and flat fund flows.

**Main reasons it gave:**
- Analyst view: 100% buy rating with +13.2% price target for top holdings
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 36; MACD negative; volume 0.33× 20‑day average
- Fund flows: flat, share count unchanged over the past week
- Macro: yields up modestly, no surprise in inflation, unemployment, or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

- [Only two consumer staples stocks have long-running Strong Sell Quant ratings (XLP:NYSEARCA)](https://seekingalpha.com/news/4647014-only-two-consumer-staples-stocks-have-long-running-strong-sell-quant-ratings)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  Only two consumer staples stocks have stayed Strong Sell 60+ days—BellRing (BRBR) and Vital Farms (VITL).
- [Sector Update: Consumer Stocks Decline Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-decline-afternoon-195131056.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were lower late Thursday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) declining 0.6% and the State Street...
- [XLV vs IBB: How Healthcare Diversification Compares to Biotech Concentration](https://www.fool.com/coverage/etfs/2026/09/24/xlv-vs-ibb-how-healthcare-diversification-compares-to-biotech-concentration/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  XLV offers exposure to the broader healthcare sector, while IBB targets biotech innovators. Here's how the two stack up on risk, returns,...
- [Exchange-Traded Funds Mixed, US Equities Decline After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-mixed-us-171353361.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded fund IWM fell and IVV edged higher. Actively traded Invesco QQQ Trust (QQQ) added 0.1%.
- [9 Of 11 Sectors Fall In Friday Trading As Cyclicals Lead](https://www.benzinga.com/trading-ideas/movers/26/09/61998944/9-of-11-sectors-fall-in-friday-trading-as-cyclicals-lead)  
  <sub>Benzinga, 17 minutes ago</sub>  
  Friday's regular session has two sectors higher and nine lower, with growth and cyclical sectors split across the top three positions.
- [S&P 500’s Midterm Rally Setup Is Getting Interesting: These ETFs Could Hold the Clues](https://www.tradingview.com/news/benzinga:8356427a1094b:0-s-p-500-s-midterm-rally-setup-is-getting-interesting-these-etfs-could-hold-the-clues/)  
  <sub>TradingView, 19 hours ago</sub>  
  The U.S. stock market is entering a historically stronger stretch of the midterm-election cycle, but the next leg of the rally may have less to do with...
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 81.62 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 83.64 (-2.4%), 50d 84.70 (-3.6%), 200d 83.67 (-2.4%); 50d above 200d
Momentum: RSI(14) 36.0 | MACD -0.846 vs signal -0.637 (histogram -0.209)
Returns: 1d -0.1% | 5d -1.4% | 1m -5.4% | 3m -3.6%
52-week range: 75.60 - 90.01 (now 41.8% of the way up)
Volatility: ATR(14) 0.96 (1.2% of price) | annualised 20d 10.7%
Volume: 0.33x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 39.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.81 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.2% above the current prices
Holdings read: WMT, COST, KO, PG, PM
Recent rating changes among them:
  - WMT: 2026-09-10 DA Davidson: main, Buy -> Buy
  - COST: 2026-09-25 JP Morgan: main, Overweight -> Overweight
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
Shares outstanding: 210.17M | fund size: 17.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: macro environment (rising yields) and technicals are bearish, but analyst coverage is bullish and fundamentals are solid; fund flows are flat, providing no directional pressure.

**Main reasons it gave:**
- Treasury yields rose across the curve (+0.11 to +0.21% on the week)
- XLU price at 52‑week low, below 20‑, 50‑ and 200‑day SMAs
- Analyst coverage 80.9% buy, weighted price target +26% above current price
- Fund flows flat over the past week (share count +0.0%)
- Fund fundamentals: P/E 19.02, yield 2.8%, beta 0.43

<details><summary><b>News</b> — score +0.00</summary>

- [XLU ETF Hits a 52-Week Low as 5% Treasuries Reset Utility Valuations](https://www.ebc.com/forex/xlu-etf-hits-52-week-low-treasuries-reset-utility-valuations)  
  <sub>EBC Financial Group, 8 hours ago</sub>  
  XLU ETF's fresh 52-week low reflects a reset in utility valuations and financing costs, not weakening electricity demand. The fund closed at $39.36 on...
- [Bond Market Flashes a Warning Not Seen Since 2007](https://247wallst.com/investing/2026/09/24/bond-market-flashes-a-warning-not-seen-since-2007/)  
  <sub>24/7 Wall St., 21 hours ago</sub>  
  Treasury yields just hit levels the bond market has not seen since before the financial crisis, and the pain is spreading fast into corners of the market...
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 39.22 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 41.72 (-6.0%), 50d 43.26 (-9.3%), 200d 44.46 (-11.8%); 50d below 200d
Momentum: RSI(14) 21.1 | MACD -1.038 vs signal -0.789 (histogram -0.249)
Returns: 1d -0.4% | 5d -4.6% | 1m -9.9% | 3m -15.1%
52-week range: 39.22 - 47.73 (now 0.0% of the way up)
Volatility: ATR(14) 0.59 (1.5% of price) | annualised 20d 13.9%
Volume: 0.30x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Utilities
What it holds: P/E 19.02 | P/B 2.14 | P/S 2.65 | 3y earnings growth n/a
Yield: 2.8%
Three-year record: +11.1% a year | beta to the market 0.43
Cost and size: expense ratio 0.08% | net assets 21.84B
What it is made of: Stocks 100.0%, Cash 0.1%
Largest holdings: NextEra Energy Inc 13.0%, Southern Co 7.5%, Duke Energy Corp 7.1%, Constellation Energy Corp 6.7%, American Electric Power Co Inc 5.1%
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
Rolled up from the 5 largest holdings, 39.4% of the fund by weight
Ratings by weight: buy 80.9% | hold 19.1% | sell 0.0% (mean 2.02 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +26.2% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-09-18 Morgan Stanley: main, Overweight -> Overweight
  - SO: 2026-09-18 Morgan Stanley: main, Underweight -> Underweight
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
Shares outstanding: 163.27M | fund size: 6.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong analyst buy rating and price target (+10.3%) are offset by recent net outflows (-1.3% share count, $563 M) and modest technical momentum (price above SMAs but MACD below signal, low volume). Macro conditions show rising yields but no surprise data, keeping the broader backdrop unchanged.

**Main reasons it gave:**
- Analyst view: 100% buy rating, weighted price target +10.3% above current price
- Fund flows: -1.3% share count over 1 week (net outflows of $563 M)
- Technical trend: price above 20‑day, 50‑day, 200‑day SMAs but MACD below signal, low volume
- Macro: yields up across curve, no surprise data; VIX low at 15.42

<details><summary><b>News</b> — score +0.00</summary>

- [XLV vs IBB: How Healthcare Diversification Compares to Biotech Concentration](https://www.fool.com/coverage/etfs/2026/09/24/xlv-vs-ibb-how-healthcare-diversification-compares-to-biotech-concentration/)  
  <sub>The Motley Fool, 23 hours ago</sub>  
  XLV offers exposure to the broader healthcare sector, while IBB targets biotech innovators. Here's how the two stack up on risk, returns,...
- [Sector Update: Healthcare Stocks Advance Late Afternoon](https://finance.yahoo.com/healthcare/articles/sector-healthcare-stocks-advance-afternoon-200124301.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Healthcare stocks were higher late Thursday afternoon, with the NYSE Healthcare Index increasing 0.9% and the State Street Health Care Select Sector SPDR...
- [S&P 500 Erases Losses as US, Iran Reportedly Discuss Hormuz Deal: Stock Market Today](https://www.tradingview.com/news/benzinga:8276f3b88094b:0-s-p-500-erases-losses-as-us-iran-reportedly-discuss-hormuz-deal-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  The S&P 500 clawed back most of its morning decline at midday Thursday after sources told Reuters that U.S. and Iranian negotiators meeting in New York are...
- [8 Of 11 Sectors Fall In Thursday Trading As Leaders Split](https://www.benzinga.com/etfs/sector-etfs/26/09/61981197/8-of-11-sectors-fall-in-thursday-trading-as-leaders-split)  
  <sub>Benzinga, 21 hours ago</sub>  
  Three sectors are higher and eight are lower in Thursday's regular session, with growth, cyclical and defensive sectors each represented among the top three...
- [Xtr.IE-Xtr.MSCI Fntc In ETF B (FXFNT.DE) Performance History](https://ca.finance.yahoo.com/quote/FXFNT.DE/performance/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Current and Historical Performance Performance for Xtr.IE-Xtr.MSCI Fntc In ETF B on Yahoo Finance.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 169.87 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 169.18 (+0.4%), 50d 167.69 (+1.3%), 200d 156.32 (+8.7%); 50d above 200d
Momentum: RSI(14) 54.0 | MACD 0.264 vs signal 0.295 (histogram -0.032)
Returns: 1d -0.0% | 5d +0.9% | 1m -2.1% | 3m +5.9%
52-week range: 134.13 - 175.68 (now 86.0% of the way up)
Volatility: ATR(14) 2.37 (1.4% of price) | annualised 20d 13.0%
Volume: 0.30x the 20-day average
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
Three-year record: +10.9% a year | beta to the market 0.52
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.3% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-09-22 TD Cowen: reit, Buy -> Buy
  - JNJ: 2026-09-10 HSBC: main, Buy -> Buy
  - ABBV: 2026-09-10 HSBC: main, Buy -> Buy
  - MRK: 2026-09-10 HSBC: main, Buy -> Buy
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
Share count change: 1 week: -1.3% (-563.15M) over 7d
Shares outstanding: 258.49M | fund size: 43.91B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 88.80 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 94.18 (-5.7%), 50d 93.63 (-5.2%), 200d 92.69 (-4.2%); 50d above 200d
Momentum: RSI(14) 31.3 | MACD -0.963 vs signal -0.219 (histogram -0.744)
Returns: 1d -0.9% | 5d -3.9% | 1m -6.0% | 3m -2.7%
52-week range: 67.55 - 102.94 (now 60.0% of the way up)
Volatility: ATR(14) 1.84 (2.1% of price) | annualised 20d 17.7%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 15.48 | P/B 1.77 | P/S 1.36 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +30.1% a year | beta to the market 0.50
Cost and size: expense ratio 0.59% | net assets 815.33M
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: MercadoLibre Inc 25.4%, YPF SA ADR 9.5%, Vista Energy SAB de CV ADR 6.2%, Grupo Financiero Galicia SA ADR 5.6%, Banco Macro SA ADR 4.3%
Sector mix: Consumer cyclical 30.4%, Energy 19.4%, Financial services 14.4%, Basic materials 12.0%
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
Rolled up from the 5 largest holdings, 51.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +35.6% above the current prices
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

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.8% (21.04M) over 7d
Shares outstanding: 8.79M | fund size: 780.52M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://www.tradingview.com/news/stocktwits:cd352f483094b:0-stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/)  
  <sub>TradingView, 9 hours ago</sub>  
  A historic summit between U.S. President Donald Trump and Chinese President Xi Jinping also influenced markets, keeping Chinese stocks in the spotlight...
- [Beyond 60/40: ETFs for a Balanced Retirement Portfolio](https://www.tradingview.com/news/zacks:6f3e9dc09094b:0-beyond-60-40-etfs-for-a-balanced-retirement-portfolio/)  
  <sub>TradingView, 4 hours ago</sub>  
  As retirement draws an end to one's earnings period, a smart allocation of assets is needed to enjoy a regular stream of income.
- [iShares 20+ Year Treasury Bond ETF (TLT) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TLT/)  
  <sub>Yahoo! Finance Canada, 23 hours ago</sub>
- [Global X Cybersecurity ETF (BUG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/BUG/)  
  <sub>Yahoo! Finance Canada, 24 hours ago</sub>

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 114.57 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 110.80 (+3.4%), 50d 105.28 (+8.8%), 200d 87.52 (+30.9%); 50d above 200d
Momentum: RSI(14) 61.7 | MACD 2.206 vs signal 2.004 (histogram 0.202)
Returns: 1d +1.3% | 5d +2.6% | 1m +7.7% | 3m +11.4%
52-week range: 60.03 - 115.64 (now 98.1% of the way up)
Volatility: ATR(14) 2.25 (2.0% of price) | annualised 20d 27.0%
Volume: 0.24x the 20-day average
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
Three-year record: +45.3% a year | beta to the market 1.30
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
Direction: money going out (1 week)
Share count change: 1 week: -6.5% (-813.61M) over 8d
Shares outstanding: 101.73M | fund size: 11.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [iShares MSCI Turkey ETF (TUR) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TUR/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  Find the latest iShares MSCI Turkey ETF (TUR) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 66.18 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 69.23 (-4.4%), 50d 67.60 (-2.1%), 200d 69.26 (-4.4%); 50d below 200d
Momentum: RSI(14) 40.0 | MACD -0.525 vs signal 0.043 (histogram -0.567)
Returns: 1d +0.4% | 5d -3.4% | 1m -7.7% | 3m +5.0%
52-week range: 60.43 - 81.60 (now 27.2% of the way up)
Volatility: ATR(14) 1.31 (2.0% of price) | annualised 20d 24.6%
Volume: 0.31x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 9.31 | P/B 2.24 | P/S 1.92 | 3y earnings growth n/a
Yield: 7.1%
Three-year record: +26.5% a year | beta to the market 1.02
Cost and size: expense ratio 0.59% | net assets 578.49M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 13.7%, Gold Fields Ltd 9.9%, Naspers Ltd Class N 8.8%, Firstrand Ltd 7.1%, Standard Bank Group Ltd 6.1%
Sector mix: Basic materials 41.0%, Financial services 33.2%, Consumer cyclical 12.8%, Communication services 6.2%
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
Rolled up from the 5 largest holdings, 45.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.5% above the current prices
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 7.90M | fund size: 522.86M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Liquidity Mapping Around (INDA) Price Events](https://news.stocktradersdaily.com/news_release/24/Liquidity_Mapping_Around_INDA_Price_Events_092426100601_1790301961.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Price-action only: Ishares Msci India Etf (INDA) movements set the tone for institutional models. Liquidity Mapping Around (INDA) Price Events.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 47.78 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 48.64 (-1.8%), 50d 49.16 (-2.8%), 200d 50.02 (-4.5%); 50d below 200d
Momentum: RSI(14) 39.6 | MACD -0.442 vs signal -0.376 (histogram -0.066)
Returns: 1d +0.5% | 5d -0.5% | 1m -4.0% | 3m -3.6%
52-week range: 45.42 - 55.29 (now 23.9% of the way up)
Volatility: ATR(14) 0.44 (0.9% of price) | annualised 20d 13.1%
Volume: 0.24x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: India Equity
What it holds: P/E 22.87 | P/B 3.14 | P/S 2.72 | 3y earnings growth n/a
Yield: n/a
Three-year record: +2.9% a year | beta to the market 0.56
Cost and size: expense ratio 0.61% | net assets 6.75B
What it is made of: Stocks 100.1%, Cash -0.1%
Largest holdings: HDFC Bank Ltd 6.4%, Reliance Industries Ltd 6.0%, ICICI Bank Ltd 5.7%, Bharti Airtel Ltd 4.1%, Infosys Ltd 2.6%
Sector mix: Financial services 30.1%, Consumer cyclical 12.8%, Industrials 9.7%, Energy 8.6%
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
Rolled up from the 5 largest holdings, 24.7% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.36 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.4% above the current prices
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

```text
Direction: money coming in (1 week)
Share count change: 1 week: +0.8% (53.73M) over 7d
Shares outstanding: 140.00M | fund size: 6.69B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 71.43 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 73.13 (-2.3%), 50d 74.92 (-4.7%), 200d 70.51 (+1.3%); 50d above 200d
Momentum: RSI(14) 36.7 | MACD -1.051 vs signal -0.818 (histogram -0.233)
Returns: 1d +0.7% | 5d -1.8% | 1m -4.2% | 3m -5.0%
52-week range: 58.14 - 77.93 (now 67.1% of the way up)
Volatility: ATR(14) 1.18 (1.6% of price) | annualised 20d 15.9%
Volume: 0.37x the 20-day average
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
Three-year record: +22.8% a year | beta to the market 1.04
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
Weighted price target: +20.1% above the current prices
Holdings read: CFR, SSB, BPOP, PNFP, UMBF
Recent rating changes among them:
  - CFR: 2026-09-08 Morgan Stanley: up, Underweight -> Overweight
  - SSB: 2026-07-28 Citigroup: main, Buy -> Buy
  - BPOP: 2026-09-22 Citigroup: main, Buy -> Buy
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

```text
Direction: money coming in (1 week)
Share count change: 1 week: +4.1% (159.01M) over 7d
Shares outstanding: 56.34M | fund size: 4.02B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Starbucks to Close Select North America Coffeehouses, Cuts Store Outlook](https://www.benzinga.com/markets/large-cap/26/09/61997944/starbucks-to-close-select-north-america-coffeehouses-cuts-store-outlook)  
  <sub>Benzinga, 46 minutes ago</sub>  
  Starbucks Corp (NASDAQ:SBUX) shares are up slightly Friday morning. The company is in focus after announcing plans to close underperforming coffeehouses in...
- [S&P 500 Eyes Midterm Rally: ETFs to Watch in October 2026 - State Street SPDR S&P 500 ETF Trust (ARCA:SPY](https://www.benzinga.com/etfs/sector-etfs/26/09/61984746/sampp-500s-midterm-rally-setup-is-getting-interesting-these-etfs-could-hold-clues)  
  <sub>Benzinga, 19 hours ago</sub>  
  The S&P 500 enters a historically strong October-November stretch. Here's how ETFs could reveal the rally's real drivers.
- [Sector Update: Consumer](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-170523628.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Consumer stocks fell Thursday afternoon with the State Street Consumer Staples Select Sector SPDR ETF (XLP) declining 0.4% and the State Street Consumer...
- [Nike Pulls Back on Bank of America Downgrade and $30 Price Objective; Dick's Ticks Up, On Holding Holds Flat](https://247wallst.com/investing/2026/09/25/nike-pulls-back-on-bank-of-america-downgrade-and-30-price-objective-dicks-ticks-up-on-holding-holds-flat/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Nike (NYSE:NKE | NKE Price Prediction) is slipping after Bank of America concluded that the sneaker giant's turnaround will arrive a full fiscal year later...
- [Sector Update: Consumer Stocks Decline Late Afternoon](https://finance.yahoo.com/markets/stocks/articles/sector-consumer-stocks-decline-afternoon-195131056.html)  
  <sub>Yahoo Finance, 20 hours ago</sub>  
  Consumer stocks were lower late Thursday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) declining 0.6% and the State Street...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 110.10 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 112.90 (-2.5%), 50d 114.81 (-4.1%), 200d 116.65 (-5.6%); 50d below 200d
Momentum: RSI(14) 36.9 | MACD -1.487 vs signal -1.313 (histogram -0.174)
Returns: 1d -0.2% | 5d -0.8% | 1m -6.0% | 3m -3.7%
52-week range: 105.66 - 124.52 (now 23.5% of the way up)
Volatility: ATR(14) 1.58 (1.4% of price) | annualised 20d 15.8%
Volume: 0.32x the 20-day average
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
Three-year record: +12.1% a year | beta to the market 1.16
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.13 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.6% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, BKNG
Recent rating changes among them:
  - AMZN: 2026-09-03 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-09-25 StoneX: reit, Buy -> Buy
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-09-24 BMO Capital: main, Outperform -> Outperform
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
Share count change: 1 week: +0.4% (97.89M) over 7d
Shares outstanding: 202.54M | fund size: 22.30B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Sugar (CANE) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- No macro data surprise (inflation 3.4% in line with expectations)
- Technical indicators mixed: price below 20-day SMA, RSI neutral, MACD negative, low volume
- Positioning shows crowded long (98th percentile) with slight weekly decrease
- Heavy cost of holding (-10.3% annual) drags long performance
- Fund inflows (+2.2% share count increase) indicate demand

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 11.24 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 11.38 (-1.2%), 50d 10.78 (+4.3%), 200d 9.94 (+13.2%); 50d above 200d
Momentum: RSI(14) 52.0 | MACD 0.092 vs signal 0.158 (histogram -0.066)
Returns: 1d -0.2% | 5d +1.8% | 1m +0.1% | 3m +16.9%
52-week range: 9.02 - 11.82 (now 79.5% of the way up)
Volatility: ATR(14) 0.19 (1.7% of price) | annualised 20d 23.1%
Volume: 0.31x the 20-day average
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
Cost of holding this fund instead of sugar itself: -10.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.9%, commodity +33.1%, gap -16.2% | 6 months: fund +5.8%, commodity +17.3%, gap -11.5% | 12 months: fund +8.6%, commodity +19.0%, gap -10.3%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 18.5% of open interest (1,219,523 contracts)
Change on the week: -0.2% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.2% (1.25M) over 7d
Shares outstanding: 5.18M | fund size: 58.24M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Positioning net long fell 5.1% week‑over‑week
- Fund flows: share count down 6.4% over 7 days
- Cost of holding heavy at -5.5% annual, tailwind for short
- Technicals: volume at 0.17× 20‑day average, no decisive break

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 40.58 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 39.87 (+1.8%), 50d 39.68 (+2.3%), 200d 37.28 (+8.8%); 50d above 200d
Momentum: RSI(14) 55.1 | MACD 0.271 vs signal 0.144 (histogram 0.127)
Returns: 1d -0.2% | 5d +0.9% | 1m +1.3% | 3m +8.7%
52-week range: 29.37 - 41.43 (now 92.9% of the way up)
Volatility: ATR(14) 0.70 (1.7% of price) | annualised 20d 28.6%
Volume: 0.17x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.5% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +8.7%, commodity +9.9%, gap -1.2% | 6 months: fund +21.7%, commodity +24.0%, gap -2.2% | 12 months: fund +36.6%, commodity +42.1%, gap -5.5%
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.25</summary>

```text
Contract: COPPER- #1 - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (289,463 contracts)
Change on the week: -5.1% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.25</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -6.4% (-50.69M) over 7d
Shares outstanding: 18.31M | fund size: 742.85M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, mixed but slightly bearish behavioral and cost signals.

**Main reasons it gave:**
- Positioning net long fell 2.2% week over week
- Fund flows outflows of -1.5% share count
- Cost of holding drag -1.7% per year
- Technicals near 52‑week high with low volume

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 27.78 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 27.78 (+0.0%), 50d 26.51 (+4.8%), 200d 24.51 (+13.4%); 50d above 200d
Momentum: RSI(14) 58.3 | MACD 0.431 vs signal 0.507 (histogram -0.077)
Returns: 1d -0.5% | 5d +0.4% | 1m +3.9% | 3m +13.4%
52-week range: 21.46 - 28.14 (now 94.7% of the way up)
Volatility: ATR(14) 0.34 (1.2% of price) | annualised 20d 16.7%
Volume: 0.28x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -1.7% a year -- a steady drag
Measured: 3 months: fund +13.4%, commodity +16.4%, gap -3.0% | 6 months: fund +14.1%, commodity +11.7%, gap +2.3% | 12 months: fund +28.3%, commodity +30.0%, gap -1.7%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.10</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 21.9% of open interest (1,104,880 contracts)
Change on the week: -2.2% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -1.5% (-720.99K) over 7d
Shares outstanding: 1.65M | fund size: 45.88M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- CFTC data shows a crowded long position (98th percentile) with a slight net long decrease of -0.3% of open interest
- EIA weekly crude inventories rose by 3.0 million barrels (build), indicating bearish supply pressure
- EIA price outlook forecasts WTI to decline to $84.5 in 3 months and $79 in 6 months, a bearish outlook
- Fund flows show a 7.2% increase in share count over the week, indicating inflows
- Geopolitical news: Houthi attacks spiked Brent prices but Hormuz talks reduced risk, creating mixed impact

<details><summary><b>News</b> — score +0.00</summary>

- [Brent crude jumps above $106 after Houthi attack against Saudi sites (USO:NYSEARCA)](https://seekingalpha.com/news/4646946-brent-crude-jumps-above-106-after-houthi-attack-against-saudi-sites)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Crude oil futures rose in a volatile session as a spate of Houthi attacks on Saudi targets raised fresh concerns of escalation in the Middle East.
- [Peter Schiff Warns Record Diesel Prices Could Leave US Vulnerable To Next Energy Shock, Says Trump's Dies](https://www.benzinga.com/markets/commodities/26/09/61989833/peter-schiff-warns-record-diesel-prices-could-leave-us-vulnerable-to-next-energy-shock-says-trumps-diesel-export-ban-could-backfire)  
  <sub>Benzinga, 6 hours ago</sub>  
  Peter Schiff warns soaring diesel prices and SPR depletion could leave the U.S. vulnerable during energy crisis.
- [Trump Reportedly Says Oil Prices Won’t Tumble Until After Midterms, While Iran Signals More Intense War — USO, UCO Rise](https://stocktwits.com/news-articles/markets/equity/trump-reportedly-says-oil-prices-wont-tumble-until-after-midterms-while-iran-signals-more-intense-war-uso-uco-rise/cZt7k6WRJC2)  
  <sub>Stocktwits, 15 hours ago</sub>  
  President Donald Trump reportedly said on Wednesday that energy prices elevated by the Iran war are unlikely to come down until after the midterm elections,...
- [‘Big Short’ Michael Burry Warns Of Dollar ‘Train Wreck’ — Bets On Fine Wine Against AI, Quantum And US Debt Risks](https://stocktwits.com/news-articles/markets/equity/michael-burry-dollar-train-wreck-bets-on-fine-wine-against-ai-quantum-us-debt-risks/cZtXchvRJ6x)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Michael Burry is buying discounted European fine wine as a hedge against dollar weakness, inflation and potential financial-system disruption.
- [Opinion: The options market is sending a contrarian signal about oil prices](https://www.marketwatch.com/story/the-options-market-is-sending-a-contrarian-signal-about-oil-prices-a8812210)  
  <sub>MarketWatch, 2 hours ago</sub>  
  Investor sentiment on an exchange-traded fund tracking oil prices is getting very bullish again — enough to flash a contrarian sell signal.
- [Energy Stocks Slipped As Oil And Gas Prices Fell](https://finimize.com/content/energy-stocks-slipped-as-oil-and-gas-prices-fell-3)  
  <sub>Finimize, 1 hour ago</sub>  
  WTI crude dipped to $92.71 a barrel while Atlas Energy Solutions jumped on data-center deals with a frontier AI lab.
- [Hormuz reopening talks are back in play as Washington and Tehran discuss a phased deal](https://seekingalpha.com/news/4646788-hormuz-reopening-talks-are-back-in-play-as-washington-and-tehran-discuss-a-phased-deal)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  US stocks rise as US-Iran Hormuz talks cut geopolitical risk and send oil lower.
- [Dow falls 160 points as Treasury Yields and oil prices rise](https://invezz.com/ie/news/2026/09/24/dow-falls-160-points-as-treasury-yields-and-oil-prices-rise/)  
  <sub>Invezz, 19 hours ago</sub>  
  US stocks ended lower on Thursday, with the Dow Jones Industrial Average falling for a third straight session as Treasury yields reached multidecade highs...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 151.32 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 148.41 (+2.0%), 50d 135.69 (+11.5%), 200d 113.24 (+33.6%); 50d above 200d
Momentum: RSI(14) 57.4 | MACD 5.049 vs signal 6.041 (histogram -0.993)
Returns: 1d -1.2% | 5d -1.6% | 1m +18.8% | 3m +43.5%
52-week range: 66.17 - 161.86 (now 89.0% of the way up)
Volatility: ATR(14) 5.10 (3.4% of price) | annualised 20d 44.0%
Volume: 0.32x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.30</summary>

```text
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 5.4% of open interest (1,955,764 contracts)
Change on the week: -0.3% of open interest
Crowding: 98% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +7.2% (133.33M) over 8d
Shares outstanding: 13.04M | fund size: 1.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> NEUTRAL

**Main reasons it gave:**
- Large speculators increased net short by 1.8% of open interest (bearish)
- Fund inflows: share count up 0.5% (1.83M) over 7 days (bullish)
- Cost of holding fund vs wheat: -13.4% annual (heavy roll cost, bearish for long)
- US wheat crop condition improved to 51% good/excellent (+2 pts YoY) (bearish)

<details><summary><b>News</b> — score +0.00</summary>

- [Wheat Falling Lower on Friday with Black Sea Pressure](https://www.barchart.com/story/news/4799108/wheat-falling-lower-on-friday-with-black-sea-pressure)  
  <sub>Barchart.com, 3 hours ago</sub>  
  Wheat is under pressure to start Friday, with the three exchanges down 12 to 20 cents. The wheat complex saw some pressure on Thursday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 25.32 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 26.57 (-4.7%), 50d 25.56 (-1.0%), 200d 23.07 (+9.7%); 50d above 200d
Momentum: RSI(14) 42.4 | MACD -0.003 vs signal 0.219 (histogram -0.222)
Returns: 1d -1.0% | 5d -2.1% | 1m -6.2% | 3m +14.2%
52-week range: 19.88 - 28.00 (now 67.0% of the way up)
Volatility: ATR(14) 0.57 (2.2% of price) | annualised 20d 24.8%
Volume: 0.67x the 20-day average
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
Cost of holding this fund instead of wheat itself: -13.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +14.2%, commodity +20.9%, gap -6.7% | 6 months: fund +9.5%, commodity +15.5%, gap -6.0% | 12 months: fund +21.1%, commodity +34.6%, gap -13.4%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score -0.25</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score -0.25</summary>

```text
Wheat rated good or excellent: 51% of the US crop (week 34 of 2026)
Direction over 1 weeks: not enough readings to say
Same week last year: 49% (+2 points)
A better crop means more supply, which reads bearish for the price, and a worse one bullish. The trend matters more than the level, and the market has already seen this: it is published on a schedule everyone trades.
```

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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 0.8% of open interest (485,138 contracts)
Change on the week: -1.8% of open interest
Crowding: 90% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +0.5% (1.83M) over 7d
Shares outstanding: 13.94M | fund size: 353.09M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Corn (CORN) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Corn Eases Lower as Export Business Disappoints](https://www.barchart.com/story/news/4789374/corn-eases-lower-as-export-business-disappoints)  
  <sub>Barchart.com, 17 hours ago</sub>  
  Corn futures rounded out the Thursday trade, with fractional to 2 ½ cent losses across the most contracts at the close. The CmdtyView national average Cash...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 19.61 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 19.97 (-1.8%), 50d 18.95 (+3.5%), 200d 18.10 (+8.4%); 50d above 200d
Momentum: RSI(14) 50.5 | MACD 0.218 vs signal 0.335 (histogram -0.117)
Returns: 1d -0.3% | 5d -0.4% | 1m -2.1% | 3m +16.3%
52-week range: 16.47 - 20.29 (now 82.3% of the way up)
Volatility: ATR(14) 0.30 (1.6% of price) | annualised 20d 15.3%
Volume: 0.70x the 20-day average
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
Cost of holding this fund instead of corn itself: -13.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +16.3%, commodity +27.3%, gap -11.0% | 6 months: fund +4.8%, commodity +12.5%, gap -7.7% | 12 months: fund +10.7%, commodity +23.9%, gap -13.2%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 22.5% of open interest (1,843,824 contracts)
Change on the week: -0.5% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: -0.1% (-226.69K) over 7d
Shares outstanding: 8.25M | fund size: 161.81M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Beyond 60/40: ETFs for a Balanced Retirement Portfolio](https://www.tradingview.com/news/zacks:6f3e9dc09094b:0-beyond-60-40-etfs-for-a-balanced-retirement-portfolio/)  
  <sub>TradingView, 4 hours ago</sub>  
  As retirement draws an end to one's earnings period, a smart allocation of assets is needed to enjoy a regular stream of income.
- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [These Precious Metals ETFs Beat The S&P 500 Over The Past Year — Can The Rally Survive The Iran Whiplash?](https://stocktwits.com/news-articles/markets/equity/these-precious-metals-etfs-beat-the-sp500-over-the-past-year/cZmAMRFR7FW)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Over the past year, top precious metals ETFs have delivered far superior returns than the benchmark S&P 500 index. The iShares Silver Trust (SLV) surged...
- [Gold likely continues to struggle as bond yields surge, Forex.com analyst says (GLD:NYSEARCA)](https://seekingalpha.com/news/4646928-gold-likely-continues-to-struggle-as-bond-yields-surge-forex-com-analyst-says)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures have fallen for four straight sessions, and Forex.com analyst Fawad Razaqzada sees room for further declines as elevated oil prices drive...
- [‘Big Short’ Michael Burry Warns Of Dollar ‘Train Wreck’ — Bets On Fine Wine Against AI, Quantum And US Debt Risks](https://stocktwits.com/news-articles/markets/equity/michael-burry-dollar-train-wreck-bets-on-fine-wine-against-ai-quantum-us-debt-risks/cZtXchvRJ6x)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Michael Burry is buying discounted European fine wine as a hedge against dollar weakness, inflation and potential financial-system disruption.
- [Gold's Short-Run Outlook Has Gotten Weaker](https://seekingalpha.com/article/4949482-golds-short-run-outlook-has-gotten-weaker?source=google_editors_picks)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  Summary. Gold's recent volatility and underperformance versus equities and bonds prompt a shift from a bullish to a neutral stance.
- [South Korea's KOSPI, S&P 500, Gold Sink On US-Iran Tensions, But Bitcoin Holds $68K Floor](https://stocktwits.com/news-articles/markets/cryptocurrency/kospi-s-and-p-500-gold-sink-on-us-iran-tensions-but-bitcoin-holds/cZd9fmeRI5O)  
  <sub>Stocktwits, 7 hours ago</sub>  
  Bitcoin held above $68000 even as KOSPI dropped more than 10%, U.S. indices closed lower, and gold shed gains.
- [Webcast: Mining’s new math: Power, compute, and sustainability | ETF Trends](https://www.advisorperspectives.com/webinars/2026/10/28/minings-new-math-power-compute-and-sustainability?partnerref=APSidebar)  
  <sub>Advisor Perspectives, 46 minutes ago</sub>  
  Join industry experts from CoinShares for an educational webcast exploring the future landscape of bitcoin mining enterprises.
- [Here are 3 alternatives for investors looking to dodge the bond-market beatdown](https://www.marketwatch.com/story/here-are-3-alternatives-for-investors-looking-to-dodge-the-bond-market-beatdown-ec8fda43)  
  <sub>MarketWatch, 21 hours ago</sub>  
  U.S. stocks have kept chugging higher this year, but bonds haven't been able to shake off a five-year slump. That has sent some investors interested in a...
- [Day 489: Rate Hike + Trump 2.0 Day 612](https://www.moomoo.com/community/feed/day-489-rate-hike-trump-2-0-day-612-117332152352774)  
  <sub>Moomoo, 1 hour ago</sub>  
  Market Recap | Friday, September 25, 2026 Microsoft steals Meta's spotlight, yields keep climbing regardless After Meta's roughly 4.5% Thursday ra...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 392.65 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 399.30 (-1.7%), 50d 395.42 (-0.7%), 200d 416.43 (-5.7%); 50d below 200d
Momentum: RSI(14) 44.5 | MACD -1.884 vs signal -0.543 (histogram -1.341)
Returns: 1d +0.2% | 5d -2.1% | 1m -6.8% | 3m +5.1%
52-week range: 344.75 - 495.90 (now 31.7% of the way up)
Volatility: ATR(14) 6.88 (1.8% of price) | annualised 20d 23.0%
Volume: 0.22x the 20-day average
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
Cost of holding this fund instead of gold itself: -0.0% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +5.1%, commodity +5.2%, gap -0.2% | 6 months: fund -2.0%, commodity -1.5%, gap -0.5% | 12 months: fund +14.4%, commodity +14.4%, gap -0.0%
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
Contract: GOLD - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 32.5% of open interest (409,899 contracts)
Change on the week: -0.3% of open interest
Crowding: 77% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 260.30M | fund size: 102.21B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Pan American Silver Corp. (PAAS) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/PAAS/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest Pan American Silver Corp. (PAAS) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [These Precious Metals ETFs Beat The S&P 500 Over The Past Year — Can The Rally Survive The Iran Whiplash?](https://stocktwits.com/news-articles/markets/equity/these-precious-metals-etfs-beat-the-sp500-over-the-past-year/cZmAMRFR7FW)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Over the past year, top precious metals ETFs have delivered far superior returns than the benchmark S&P 500 index. The iShares Silver Trust (SLV) surged...
- [Who safeguards the gold and silver behind your ETF? SEBI approves tighter vault rules](https://www.moneycontrol.com/news/business/personal-finance/who-safeguards-the-gold-and-silver-behind-your-etf-sebi-approves-tighter-vault-rules-14038069.html)  
  <sub>Moneycontrol.com, 9 hours ago</sub>  
  SEBI will bring vaults holding gold and silver for ETFs under common rules for security, segregation, insurance and reconciliation.
- [Gold likely continues to struggle as bond yields surge, Forex.com analyst says (GLD:NYSEARCA)](https://seekingalpha.com/news/4646928-gold-likely-continues-to-struggle-as-bond-yields-surge-forex-com-analyst-says)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Gold futures have fallen for four straight sessions, and Forex.com analyst Fawad Razaqzada sees room for further declines as elevated oil prices drive...
- [SEBI tightens rules to safeguard gold and silver held for ETFs | Vault bullion must match recorded quantity | Inshorts](https://inshorts.com/en/amp_news/sebi-tightens-rules-to-safeguard-gold-and-silver-held-for-etfs-1790332122011)  
  <sub>Inshorts, 5 hours ago</sub>  
  SEBI has approved tighter rules for vaults storing gold and silver for ETFs and other regulated bullion products. The framework will cover vault managers'...
- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- ['Silver prices can again cross ₹3 lakh/kg mark': Expert sees 19% return in gold pegging prices at ₹1.80 lak...](https://www.bhaskarenglish.in/business/news/gold-silver-price-hike-india-bullion-market-2026-outlook-139142449.html)  
  <sub>Bhaskar English, 9 hours ago</sub>  
  Gold and silver prices rose today, 25 September. According to the India Bullion and Jewellers Association (IBJA), the price of 10 grams of 24-carat gold...
- [Gold, silver ETFs get a new vaulting framework: SEBI raises vault managers' net worth requirement](https://www.businesstoday.in/personal-finance/story/gold-silver-etfs-get-a-new-vaulting-framework-sebi-raises-vault-managers-net-worth-requirement-557685-2026-09-24)  
  <sub>Business Today, 24 hours ago</sub>  
  SEBI has approved a new vaulting framework covering bullion underlying gold and silver ETFs and other specified bullion-related instruments,...
- [Gold Rate Today in Delhi 25th September 2026 : 22 & 24 Carat, Todays Gold Price in Delhi](https://www.businesstoday.in/commodity/gold-rate-in-delhi-today)  
  <sub>Business Today, 3 hours ago</sub>  
  Gold rate in Delhi on Friday, Sep 25, 2026 : Today, the price of 24-carat Gold in Delhi is ₹1,52,820 per 10 grams. A day earlier, on Sep 24, 2026, the rate...
- [India's gold imports fall sharply: Kotak sees 'good, bad and ugly' outcomes](https://www.business-standard.com/finance/personal-finance/india-s-gold-imports-fall-sharply-kotak-sees-good-bad-and-ugly-outcomes-126092500254_1.html)  
  <sub>Business Standard, 11 hours ago</sub>  
  old imports plunge after duty hike: Kotak sees three possible explanations. Lower household demand could help India's external balances, but a shift to...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 58.01 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 58.88 (-1.5%), 50d 57.46 (+1.0%), 200d 65.96 (-12.0%); 50d below 200d
Momentum: RSI(14) 47.7 | MACD -0.015 vs signal 0.180 (histogram -0.194)
Returns: 1d +0.7% | 5d -3.2% | 1m -5.8% | 3m +8.9%
52-week range: 41.03 - 105.60 (now 26.3% of the way up)
Volatility: ATR(14) 1.75 (3.0% of price) | annualised 20d 40.0%
Volume: 0.42x the 20-day average
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
Cost of holding this fund instead of silver itself: -1.7% a year -- a steady drag
Measured: 3 months: fund +8.9%, commodity +9.0%, gap -0.1% | 6 months: fund -4.5%, commodity -4.6%, gap +0.1% | 12 months: fund +45.7%, commodity +47.4%, gap -1.7%
A commodity fund holds futures, not silver, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-09-15, published the following Friday)
Large speculators: net long 12.7% of open interest (103,745 contracts)
Change on the week: -1.3% of open interest
Crowding: 65% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -4.3% (-1.52B) over 8d
Shares outstanding: 585.04M | fund size: 33.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Hormuz reopening talks are back in play as Washington and Tehran discuss a phased deal](https://seekingalpha.com/news/4646788-hormuz-reopening-talks-are-back-in-play-as-washington-and-tehran-discuss-a-phased-deal)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  US stocks rise as US-Iran Hormuz talks cut geopolitical risk and send oil lower.
- [Brent crude jumps above $106 after Houthi attack against Saudi sites (USO:NYSEARCA)](https://seekingalpha.com/news/4646946-brent-crude-jumps-above-106-after-houthi-attack-against-saudi-sites)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  Crude oil futures rose in a volatile session as a spate of Houthi attacks on Saudi targets raised fresh concerns of escalation in the Middle East.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.09% (+0.11 on the week) | 5-year 5.04% (+0.18 on the week) | 10-year 5.21% (+0.21 on the week) | 30-year 5.52% (+0.18 on the week)
Yield curve, 10-year minus 3-month: +1.12 points -- upward sloping (normal)
US dollar index: 101.00 (+0.78 on the week)
Volatility (VIX): 15.42 (+0.6 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.1% (2026-08-01) | jobless claims 197k (2026-09-19)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.85% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 11.00 (bar of 2026-09-25), from 502 daily bars
Trend: vs 20d SMA 10.53 (+4.4%), 50d 10.28 (+7.0%), 200d 11.43 (-3.7%); 50d below 200d
Momentum: RSI(14) 58.4 | MACD 0.180 vs signal 0.087 (histogram 0.093)
Returns: 1d -4.8% | 5d +5.7% | 1m +5.7% | 3m -7.3%
52-week range: 9.63 - 16.90 (now 18.8% of the way up)
Volatility: ATR(14) 0.36 (3.3% of price) | annualised 20d 42.3%
Volume: 0.86x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -23.0% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -7.3%, commodity -1.0%, gap -6.4% | 6 months: fund -7.1%, commodity +6.7%, gap -13.8% | 12 months: fund -11.0%, commodity +12.0%, gap -23.0%
A commodity fund holds futures, not natural gas, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-09-18 (published the following Wednesday)
  Natural gas: 3,351.0 billion cubic feet, +53.0 on the week (a build), 73% percentile over 52 weeks
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
Contract: NAT GAS NYME - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-09-15, published the following Friday)
Large speculators: net short 5.5% of open interest (1,820,003 contracts)
Change on the week: -0.2% of open interest
Crowding: 33% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -2.8% (-17.13M) over 8d
Shares outstanding: 54.07M | fund size: 594.83M
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

