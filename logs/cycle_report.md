# Daily report

**13 Oct 2026, 19:31 Israel time (16:31 UTC)** · 80 names checked · 0 traded · 14 with a problem

**Answers with no explanation:** 9 of 48 (the model wrote only a label, like “NEUTRAL”, where its reason should be). Their main reasons are still shown.

**Run:** started by the outside scheduler (via supabase-cron), on time (planned for 14:40 UTC).

| Group | Looked at | Took a side | No clear view | Problems |
| --- | --- | --- | --- | --- |
| Companies | 16 | 5 | 11 | 0 |
| Whole-market funds | 14 | 0 | 14 | 0 |
| Sector and country funds | 41 | 0 | 34 | 7 |
| Commodities | 9 | 0 | 2 | 7 |

## Open positions

Checked before any new trade. R is what the trade risked at entry; the ladder sells a third at +1R and another at +3R, the stop-loss follows the price up every day, and it only ever moves up.

| Position | What happened |
| --- | --- |
| United Kingdom (EWU) · Sector or country | **Stop raised.** At +0.67R, following the price. Stop-loss raised 45.71 → 45.88. |
| Alphabet (Google) (GOOGL) · Company | **Stop raised.** At +0.12R, following the price. Stop-loss raised 337.80 → 338.01. |
| Microsoft (MSFT) · Company | **Stop raised.** At +2.76R, following the price. Stop-loss raised 516.87 → 525.70. |
| Exxon Mobil (XOM) · Company | **Stop raised.** At +1.67R, following the price. Stop-loss raised 164.03 → 167.17. |
| Argentina (ARGT) · Sector or country | **Holding.** +0.14R, holding 80 shares. Stop-loss 86.01. |
| ASML (ASML) · Company | **Holding.** -0.79R, holding 2 shares. Stop-loss 1690.71. |
| Poland (EPOL) · Sector or country | **Holding.** +0.54R, holding 164 shares. Stop-loss 43.03. |
| Brazil (EWZ) · Sector or country | **Holding.** -0.11R, holding 165 shares. Stop-loss 41.48. |
| Gold mining companies (GDX) · Sector or country | **Holding.** -0.00R, holding 82 shares. Stop-loss 82.88. |
| Gold (GLD) · Commodity | **Holding.** +0.47R, holding 10 shares. Stop-loss 389.68. |
| US company bonds, riskier (HYG) · Index fund | **Holding.** -0.01R, holding 158 shares. Stop-loss 76.66. |
| US government bonds, 7-10 years (IEF) · Index fund | **Holding.** +2.11R, holding 40 shares. Stop-loss 89.85. |
| Eli Lilly (LLY) · Company | **Holding.** +0.45R, holding 4 shares. Stop-loss 1130.70. |
| Nvidia (NVDA) · Company | **Holding.** -0.37R, holding 22 shares. Stop-loss 218.74. |
| Novo Nordisk (NVO) · Company | **Holding.** +0.47R, holding 123 shares. Stop-loss 39.01. |
| Teva Pharmaceutical (TEVA) · Company | **Holding.** +0.82R, holding 128 shares. Stop-loss 38.87. |
| US inflation-linked bonds (TIP) · Index fund | **Holding.** +2.17R, holding 4 shares. Stop-loss 104.79. |
| US dollar (UUP) · Index fund | **Holding.** +3.14R, holding 142 shares. Stop-loss 28.86. |

## How to read this

Once a day the system looks at every name on the list. For each one it reads five kinds of evidence and gives each kind a score from -1.00 (bad) to +1.00 (good). Then it picks a side and says how sure it is, from 0.00 to 1.00.

The three sides: **BULLISH** = the model thinks the price will go up; **BEARISH** = the model thinks the price will go down; **NEUTRAL** = the model has no clear view.

Being sure is not enough on its own. A trade only happens when confidence reaches **0.30**. Below that the system writes down what it thought and does nothing. The size of a trade, the stop-loss and every limit are decided by plain code, not by the model.

Open positions are checked first, before any new trade. When a trade has earned back what it risked (+1R), a third of it is sold and the stop-loss moves up to the entry price, so it can no longer lose. At three times that (+3R) another third is sold and the stop moves up again. The last third stays open. Every day the stop-loss also follows the price up, so a position only ever closes when its stop is hit. The stop only ever moves up.

Under each name you will find the five scores. Click a grey line to open it and see the exact evidence behind that score. The words inside quotation marks are the model's own; nothing there has been rewritten.

## Companies

### Caterpillar (CAT) · Company — BULLISH, confidence 0.62

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- $1B investment in North Carolina to expand compact equipment manufacturing (positive catalyst)
- Four consecutive earnings beats (31%, 19%, 9%, 8%) indicating strong earnings momentum
- Strong fundamentals: 24% YoY revenue growth, 68% earnings growth, high ROE 57% (high debt/equity 232.8%)
- Technical indicators show bearish momentum (price below SMAs, RSI 38.5, MACD negative, low volume) tempering conviction

<details><summary><b>News</b> — score +0.50</summary>

- [Caterpillar (CAT) and Deere (DE) Slide as Treasury Yields Surge. Why Valuations Matter](https://finance.yahoo.com/markets/stocks/articles/caterpillar-cat-deere-slide-treasury-133517768.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  On October 7, Caterpillar Inc. (NYSE:CAT) slid as much as 7% to around $807-$813, with Deere & Company (NYSE:DE) down 4% to roughly $658 as the 30-year...
- [Caterpillar (CAT) Bets $1 Billion On North Carolina As Its Valuation Story Builds](https://simplywall.st/stocks/us/capital-goods/nyse-cat/caterpillar/news/caterpillar-cat-bets-1-billion-on-north-carolina-as-its-valu)  
  <sub>Simply Wall Street, 6 minutes ago</sub>  
  Caterpillar's North Carolina bet and what it means for investors Caterpillar (CAT) just committed about US$1b to expand compact equipment manufacturing in...
- [3 S&P 500 Stocks on Our Watchlist](https://stockstory.org/us/stocks/nasdaq/mu/news/buy-or-sell/3-sandp-500-stocks-on-our-watchlist)  
  <sub>StockStory, 6 hours ago</sub>  
  The S&P 500 (^GSPC) is full of established businesses, but only some continue to outperform the market. A few standout companies are thriving thanks to...
- [Caterpillar Inc. (CAT) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/CAT/latest-news/)  
  <sub>Yahoo Finance Singapore, 6 hours ago</sub>  
  Caterpillar (CAT) Surpasses Market Returns: Some Facts Worth Knowing ... Caterpillar's $1B Compact Equipment Investment:...
- [Caterpillar, Inc. Stock 12‑Month Price Target Cut to $984.88, Implies 23% Upside](https://www.tradingview.com/news/tradingview:0c964eb9d1f01:0-caterpillar-inc-stock-12-month-price-target-cut-to-984-88-implies-23-upside/)  
  <sub>TradingView, 16 hours ago</sub>  
  According to estimates from 25 analysts, Caterpillar, Inc. stock's average price target has fallen from $990.88 to $984.88, with forecasts ranging from $575...
- [Uncover the latest developments among dow jones stocks in today's session.](https://www.chartmill.com/news/GS/Chartmill-56103-Uncover-the-latest-developments-among-dow-jones-stocks-in-todays-session)  
  <sub>Chart Mill, 20 hours ago</sub>  
  Curious about the top performers within the dow jones index one hour before the close of the markets on Monday? Dive into the list of today's session's top...
- [Time to Buy the Dead-Cat Bounce in Income Stocks?](https://moneyandmarkets.com/time-to-buy-the-dead-cat-bounce-in-income-stocks/)  
  <sub>Money & Markets, 16 hours ago</sub>  
  A strong week for utilities may be a head fake, while tech's uptrend is giving investors another reason to rethink their favorite AI stocks.
- [Michael Burry Adds To NVDA, PLTR, ORCL Shorts — Why He’s Thinking About 2005 Again](https://stocktwits.com/news-articles/markets/equity/michael-burry-adds-to-nvda-pltr-orcl-shorts-why-he-is-thinking-about-2005-again/cZoNOyZRJXV)  
  <sub>Stocktwits, 13 hours ago</sub>  
  Michael Burry added to several of his biggest short positions, including Nvidia, Palantir and Oracle, while increasing his long-term bet on Molina...
- [Wall Street Zen upgrades Caterpillar stock to Buy](https://www.ad-hoc-news.de/boerse/news/corporate-news/wall-street-zen-upgrades-caterpillar-stock-to-buy/70313154)  
  <sub>ad-hoc-news.de, 4 hours ago</sub>  
  Adjusted profit per share was USD 8.17 in quarter two. Caterpillar stock trades EUR 712.00 on October 13, 2026, 1.71 percent below Xetra EUR 724.40.
- [DE, CNH, CAT, AGCO Stocks Slump - FTC, USDA Inquiry Puts Farm Equipment Market Practices In Focus](https://stocktwits.com/news-articles/markets/equity/de-cnh-cat-agco-stocks-slump-ftc-usda-inquiry-puts-farm-equipment-market-practices-in-focus/cZDv1OyRBZR)  
  <sub>Stocktwits, 17 hours ago</sub>  
  The FTC and USDA have opened an inquiry on possible barriers to buying, servicing and repairing agricultural equipment.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.60</summary>

```text
Last close 774.28 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 813.92 (-4.9%), 50d 820.57 (-5.6%), 200d 803.37 (-3.6%); 50d above 200d
Momentum: RSI(14) 38.5 | MACD -4.992 vs signal -1.144 (histogram -3.849)
Returns: 1d -3.1% | 5d -10.3% | 1m -1.2% | 3m -15.3%
52-week range: 504.76 - 1,064.90 (now 48.1% of the way up)
Volatility: ATR(14) 25.68 (3.3% of price) | annualised 20d 32.0%
Volume: 0.29x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.50</summary>

```text
Sector: Industrials / Farm & Heavy Construction Machinery | market cap 355.92B
Valuation: trailing P/E 33.33 | forward P/E 23.87 | P/B 18.35 | PEG 1.42
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

```text
Consensus: buy (mean 2.07 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 1 strong buy, 14 buy, 11 hold, 1 sell, 1 strong sell
Price target: mean 965.03 (+24.6% vs last close), range 575.00 - 1,155.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

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
  - 2026-05-13 JOHNSON DENISE C. (Officer): 6,196 shares, 5.64M
  - 2026-05-13 SCHAUPP WILLIAM E (Officer): 360 shares, 326.16K
(19 grant/option/gift transaction(s) excluded — compensation, not a view on the price)
```

</details>

<details><summary><b>Who is positioned how</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.00</summary>

_Not available today._

</details>

### MercadoLibre (MELI) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Mixed but net‑positive outlook: strong Q2 sales growth, bullish technicals, insider buying, and buy‑side analyst consensus outweigh modestly bearish fundamentals and a weak earnings record.

**Main reasons it gave:**
- Q2 2026 net sales up 43% driven by Brazil market (Pluang, 1 h ago)
- Insider purchases: Officer Marcelo bought 124 shares ($200 K) and Director Nicolás bought 600 shares ($994 K) (SEC filings)
- Technicals: price above 20‑, 50‑ and 200‑day SMAs; RSI 58.3; MACD positive
- Analyst consensus: buy (mean rating 1.62) with price target +19.9% vs last close
- Earnings record: 1 beat, 3 misses over last 4 quarters (weak earnings consistency)

<details><summary><b>News</b> — score +0.20</summary>

- [MercadoLibre, Inc. $MELI Stock: Perpetual Ltd Cuts Holdings](https://www.marketbeat.com/instant-alerts/filing-mercadolibre-inc-meli-stock-perpetual-ltd-cuts-holdings-2026-10-13/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Perpetual Ltd lowered its stake in shares of MercadoLibre, Inc. (NASDAQ:MELI - Free Report) by 11.7% during the 3rd quarter, according to the company in its...
- [MELI Dec 2028 2260.000 call (MELI281215C02260000) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MELI281215C02260000/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest MELI Dec 2028 2260.000 call (MELI281215C02260000) stock quote, history, news and other vital information to help you with your stock trading...
- [Reflecting On Online Marketplace Stocks’ Q2 Earnings: MercadoLibre (NASDAQ:MELI)](https://www.tradingview.com/news/stockstory:299fcd1cb094b:0-reflecting-on-online-marketplace-stocks-q2-earnings-mercadolibre-nasdaq-meli/)  
  <sub>TradingView, 11 hours ago</sub>  
  As the Q2 earnings season comes to a close, it's time to take stock of this quarter's best and worst performers in the online marketplace industry,...
- [Here's How Much $100 Invested In MercadoLibre 15 Years Ago Would Be Worth Today](https://www.benzinga.com/news/26/10/62312686/here-s-how-much-100-invested-mercadolibre-15-years-ago-would-be-worth-today)  
  <sub>Benzinga, 17 hours ago</sub>  
  MercadoLibre (NASDAQ:MELI) has outperformed the market over the past 15 years by 12.6% on an annualized basis producing an average annual return of 25.71%.
- [MercadoLibre posts 43% sales growth, driven by rising users and strong Brazil market in Q2 2026](https://pluang.com/en/news-feed/mercadolibre-meli-laporan-keuangan-q2-dan-prospek-latin-amerika)  
  <sub>Pluang, 1 hour ago</sub>  
  MercadoLibre reported a 43% increase in net sales for Q2 2026, fueled by strong user growth across its marketplace and Mercado Pago payment platform.
- [Trading the Move, Not the Narrative: (MELI) Edition](https://news.stocktradersdaily.com/news_release/150/Trading_the_Move,_Not_the_Narrative:_MELI_Edition_101326022602_1791872762.html)  
  <sub>Stock Traders Daily, 12 hours ago</sub>  
  Price-action only: Mercadolibre Inc. (MELI) movements set the tone for institutional models. Trading the Move, Not the Narrative: (MELI) Edition.
- [MELI Dec 2027 2820.000 call (MELI271217C02820000) Interactive Stock Chart - Yahoo Finance](https://ca.finance.yahoo.com/quote/MELI271217C02820000/chart/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Interactive Chart for MELI Dec 2027 2820.000 call (MELI271217C02820000), analyze all the data with a huge range of indicators.
- [Cantor Fitzgerald cuts target for MercadoLibre stock to USD 2,200](https://www.ad-hoc-news.de/boerse/news/corporate-news/cantor-fitzgerald-cuts-target-for-mercadolibre-stock-to-usd-2-200/70313072)  
  <sub>ad-hoc-news.de, 5 hours ago</sub>  
  MELI, US58733R1023. Cantor Fitzgerald cuts target for MercadoLibre stock to USD 2,200. Published on 10/13/2026 at 12:11 | Editorial responsibility: Rafael...
- [MercadoLibre's Commerce-Fintech Flywheel Gains Strength](https://es.tradingview.com/news/zacks:0bc3a5920094b:0-mercadolibre-s-commerce-fintech-flywheel-gains-strength/)  
  <sub>TradingView, 24 hours ago</sub>  
  MercadoLibre, Inc. MELI is seeing stronger customer engagement as the growing integration between its commerce marketplace and Mercado Pago financial...
- [MELI261016C01675000 Interactive Stock Chart | MELI Oct 2026 1675.000 call Stock](https://finance.yahoo.com/chart/MELI261016C01675000)  
  <sub>Yahoo Finance, 16 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.30</summary>

```text
Last close 1,895.42 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 1,803.93 (+5.1%), 50d 1,862.59 (+1.8%), 200d 1,834.25 (+3.3%); 50d above 200d
Momentum: RSI(14) 58.3 | MACD 5.167 vs signal -14.050 (histogram 19.217)
Returns: 1d +0.2% | 5d +2.0% | 1m -0.3% | 3m +2.8%
52-week range: 1,546.81 - 2,360.76 (now 42.8% of the way up)
Volatility: ATR(14) 54.76 (2.9% of price) | annualised 20d 41.1%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Consumer Cyclical / Internet Retail | market cap 96.09B
Valuation: trailing P/E 51.55 | forward P/E 33.46 | P/B 12.27 | PEG 1.00
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: buy (mean 1.62 on a 1=strong buy to 5=strong sell scale, 26 analysts)
Ratings: 4 strong buy, 16 buy, 6 hold, 0 sell, 0 strong sell
Price target: mean 2,271.93 (+19.9% vs last close), range 1,750.00 - 2,800.00
Recent rating changes:
  - 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-10-06 Susquehanna: main, Positive -> Positive
  - 2026-09-03 BTIG: reit, Buy -> Buy
  - 2026-08-11 JP Morgan: main, Neutral -> Neutral
  - 2026-08-06 Cantor Fitzgerald: main, Overweight -> Overweight
  - 2026-08-06 BTIG: reit, Buy -> Buy
Institutional ownership: 80.2%
Largest holders: Capital Research Global Investors (6.2%), BAILLIE GIFFORD & CO (6.0%), Capital International Investors (3.7%), Capital World Investors (3.5%), Morgan Stanley (2.9%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

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

### Procter & Gamble (PG) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Evercore upgraded PG to Outperform (fresh upgrade)
- RSI 64.9 and MACD positive, price above 20d/50d/200d SMAs (technical bullish signs)
- YoY earnings down 15.5% and PEG 3.79 (mixed fundamentals)
- Insider net buying of 91,724 shares (+4.5% holdings) but no distinct insider buyers (neutral)

<details><summary><b>News</b> — score +0.60</summary>

- [Procter & Gamble (PG) Stock May Be 22% Undervalued After $1.5B Investment](https://finance.yahoo.com/markets/stocks/articles/procter-gamble-pg-stock-may-072031174.html)  
  <sub>Yahoo Finance, 7 hours ago</sub>  
  Procter & Gamble has delivered steady gains for long term shareholders, and with the stock recently closing at US$153.20 the question now is whether that...
- [P&G Declares Quarterly Dividend](https://www.businesswire.com/news/home/20261013030117/en/PG-Declares-Quarterly-Dividend)  
  <sub>Business Wire, 47 minutes ago</sub>  
  The Procter & Gamble Company (NYSE:PG) announced at today's Annual Meeting of Shareholders that the P&G Board of Directors declared a quarterly dividend of...
- [Procter & Gamble (NYSE:PG) Stock Jumps 1.2% - Should You Buy?](https://www.marketbeat.com/instant-alerts/price-procter-gamble-nyse-pg-stock-jumps-12-should-you-buy-2026-10-12/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  Procter & Gamble (NYSE:PG) Stock Jumps 1.2% - What's Next?
- [Evercore Just Upgraded This Blue-Chip Dividend Stock to Outperform](https://www.barchart.com/story/news/6370130/evercore-just-upgraded-this-blue-chip-dividend-stock-to-outperform)  
  <sub>Barchart.com, 15 hours ago</sub>  
  Evercore just upgraded PG stock and raised its price target to $166, citing better U.S. execution even as higher costs are expected to cut fiscal 2027...
- [4 Dividend Kings Retirees Can Buy and Hold Forever: Safe Income for the Next 60 Years](https://247wallst.com/investing/2026/10/13/4-dividend-kings-retirees-can-buy-and-hold-forever-safe-income-for-the-next-60-years-2/)  
  <sub>24/7 Wall St., 3 hours ago</sub>  
  JNJ and PG earn "Very Safe" dividend ratings with payout ratios below 64%, backed by decades of consecutive annual increases. PepsiCo pays out 99.6% of free...
- [Uncover the latest developments among dow jones stocks in today's session.](https://www.chartmill.com/news/GS/Chartmill-56103-Uncover-the-latest-developments-among-dow-jones-stocks-in-todays-session)  
  <sub>Chart Mill, 20 hours ago</sub>  
  Curious about the top performers within the dow jones index one hour before the close of the markets on Monday? Dive into the list of today's session's top...
- [P&G declares quarterly dividend of $1.0885 per share By Investing.com](https://uk.investing.com/news/stock-market-news/pg-declares-quarterly-dividend-of-10885-per-share-93CH-4908081)  
  <sub>Investing.com UK, 42 minutes ago</sub>  
  CINCINNATI - The Procter & Gamble Company (NYSE:PG) declared a quarterly dividend of $1.0885 per share on its common stock, payable on or after November 16,...
- [Is Procter & Gamble (NYSE:PG) The Household Dividend Anchor For A Jittery Market?](https://kalkinemedia.com/us/stocks/dividend/is-procter-gamble-nysepg-the-household-dividend-anchor-for-a-jittery-market)  
  <sub>Kalkine Media, 1 hour ago</sub>  
  Procter & Gamble (NYSE:PG) kept lifting its dividend as consumer staples drew attention during a choppy stretch, placing the household-goods maker's long...
- [Procter & Gamble Company (The) (PG) Stock Forecasts](https://finance.yahoo.com/research/reports/MS_0P000004GV_AnalystReport_1791846905000)  
  <sub>Yahoo Finance, 13 hours ago</sub>  
  At Yahoo Finance, you get free stock quotes, up-to-date news, portfolio management resources, international market data, social interaction and mortgage...
- [Procter & Gamble stock sits 3.15 percent below its 52-week high](https://www.ad-hoc-news.de/boerse/news/corporate-news/procter-und-gamble-stock-sits-3-15-percent-below-its-52-week-high/70313387)  
  <sub>ad-hoc-news.de, 4 hours ago</sub>  
  Fiscal 2026 revenue reached USD 87.0 billion, up 3.00 percent. Procter & Gamble stock was EUR 137.63 on October 13, 2026 versus EUR 142.10.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 152.91 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 147.81 (+3.5%), 50d 146.25 (+4.6%), 200d 147.83 (+3.4%); 50d below 200d
Momentum: RSI(14) 64.9 | MACD 1.469 vs signal 0.748 (histogram 0.720)
Returns: 1d -0.2% | 5d +3.0% | 1m +4.6% | 3m +3.3%
52-week range: 138.04 - 167.20 (now 51.0% of the way up)
Volatility: ATR(14) 2.42 (1.6% of price) | annualised 20d 17.2%
Volume: 0.12x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.10</summary>

```text
Sector: Consumer Defensive / Household & Personal Products | market cap 355.44B
Valuation: trailing P/E 23.10 | forward P/E 20.67 | P/B 6.66 | PEG 3.79
Profitability: profit margin 18.4% | operating margin 22.1% | ROE 30.3%
Growth (YoY): revenue +1.5% | earnings -15.5%
Balance sheet: debt/equity 64.5% | free cash flow 13.28B
Risk: beta 0.38 | short interest 1.1% of float
Next earnings: 2026-10-22
```

</details>

<details><summary><b>What this fund holds</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score -0.10</summary>

```text
Earnings record, last 4 quarters: 4 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 in line | 2025-09-30 in line
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
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 23 analysts)
Ratings: 6 strong buy, 8 buy, 11 hold, 0 sell, 0 strong sell
Price target: mean 161.22 (+5.4% vs last close), range 143.00 - 186.00
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

### Toyota (TM) · Company — BULLISH, confidence 0.60

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:** no explanation. It wrote only “BUY”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Trailing P/E 8.27 indicates cheap valuation
- Four consecutive earnings beats (44% to 12% etc.)
- Analyst ratings: 2 strong buy, 2 buy with mean price target +24% upside
- Price above 20‑day SMA (+0.5%) but below 50‑day and 200‑day SMAs; volume 0.21× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score +0.10</summary>

```text
Last close 188.33 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 187.48 (+0.5%), 50d 190.51 (-1.1%), 200d 200.27 (-6.0%); 50d below 200d
Momentum: RSI(14) 50.8 | MACD -1.662 vs signal -1.742 (histogram 0.080)
Returns: 1d +2.0% | 5d +1.5% | 1m -4.7% | 3m +6.4%
52-week range: 166.50 - 248.29 (now 26.7% of the way up)
Volatility: ATR(14) 3.02 (1.6% of price) | annualised 20d 20.4%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Consumer Cyclical / Auto Manufacturers | market cap 223.02B
Valuation: trailing P/E 8.27 | forward P/E 11.93 | P/B 15.16 | PEG n/a
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

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

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### HDFC Bank (HDB) · Company — BULLISH, confidence 0.45

**Result:** REJECTED · no room under the sleeve budget limit

**In the model's own words:**

> Moderate bullish bias driven by recent institutional purchase, strong analyst consensus with sizable upside target, solid growth fundamentals, offset by weak technicals (low volume, price far below 200‑day SMA) and high valuation (P/B 9.35). No insider activity and mixed earnings record keep conviction moderate.

**Main reasons it gave:**
- Perpetual Ltd bought 1,961,566 shares, raising its stake by 126% (institutional purchase)
- Analyst consensus is buy (mean rating 1.75) with target price 30.52 (~33% upside)
- Technicals show low volume (0.08x 20‑day average) and price 14% below 200‑day SMA
- Fundamentals: revenue +16.6% YoY growth but high P/B ratio of 9.35

<details><summary><b>News</b> — score +0.20</summary>

- [HDFC Bank Limited (HDB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo! Finance Canada, 18 hours ago</sub>  
  HDFC Bank Limited (HDB) · 0.71% · -3.26% · -15.53% · -38.04% · -35.15% · -38.70% · 3,014.48%. Key Events. Baseline. Advanced Chart.
- [Perpetual Ltd Buys 1,961,566 Shares of HDFC Bank Limited $HDB](https://www.marketbeat.com/instant-alerts/filing-perpetual-ltd-buys-1961566-shares-of-hdfc-bank-limited-hdb-2026-10-13/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  Perpetual Ltd increased its stake in shares of HDFC Bank Limited (NYSE:HDB - Free Report) by 126.0% in the third quarter, according to the company in its...
- [HDFC Bank Limited (HDB) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/HDB/)  
  <sub>Yahoo Finance UK, 18 hours ago</sub>  
  HDFC Bank Limited (HDB) · 0.71% · -3.26% · -15.53% · -38.04% · -35.15% · -38.70% · 3,014.48%. Key events. Baseline. Advanced chart.
- [Motilal Oswal reiterates INR 925 target for HDFC Bank stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/motilal-oswal-reiterates-inr-925-target-for-hdfc-bank-stock/70315302)  
  <sub>ad-hoc-news.de, 2 hours ago</sub>  
  HDB, US40415F1012. Motilal Oswal reiterates INR 925 target for HDFC Bank stock. Published on 10/13/2026 at 14:51 | Editorial responsibility: Rafael Müller,...
- [Foreign investors net sold over 100 billion VND worth of FPT shares.](https://www.vietnam.vn/en/khoi-ngoai-ban-rong-hon-100-ty-dong-ma-fpt)  
  <sub>Vietnam.vn, 6 hours ago</sub>  
  (Dan Tri Newspaper) - This marks the 11th consecutive session of net selling by foreign investors. Since the beginning of this year, foreign investors have...
- [Abbott Laboratories (ABT) Stock Price, Quote & News, NYSE](https://techgraph.co/stock-market/quote/abt/)  
  <sub>TechGraph, 20 hours ago</sub>  
  Abbott Laboratories (ABT) stock price, quote and news on NYSE. Latest available chart and session move on TechGraph.
- [HDB Financial Services Share Price Rises; Valuation in Focus](https://univest.in/blogs/why-hdb-financial-services-l-share-price-rise-today-2026)  
  <sub>Univest, 8 hours ago</sub>  
  HDB Financial Services Share Price rose 3.14% to Rs 600.20. See price action, valuation, fundamentals and Finance NBFC peer context.
- [HDBank honors Kim Byoungho: what it means for HDBank stock](https://www.ad-hoc-news.de/boerse/news/corporate-news/hdbank-honors-kim-byoungho-what-it-means-for-hdbank-stock/70311641)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  HDBank, VN000000HDB1. HDBank honors Kim Byoungho: what it means for HDBank stock. Published on 10/13/2026 at 10:03 | Editorial responsibility: Rafael Müller...
- [Stock market on October 13th: FPT continues its decline, shareholders anxious about the sharp drop.](https://www.vietnam.vn/en/chung-khoan-13-10-fpt-miet-mai-giam-co-dong-thap-thom-truoc-da-lao-doc)  
  <sub>Vietnam.vn, 5 hours ago</sub>  
  Today's trading session saw FPT shares continue to fall to 56300 VND per share. Over the past month, the share price has lost 14.84%, and compared to the...
- [Exxon Mobil (XOM) Stock Price, Quote & News, NYSE](https://techgraph.co/stock-market/quote/xom/)  
  <sub>TechGraph, 23 hours ago</sub>  
  Exxon Mobil (XOM) stock price, quote and news on NYSE. Latest available chart and session move on TechGraph.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.15</summary>

```text
Last close 22.83 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 22.65 (+0.8%), 50d 22.94 (-0.5%), 200d 26.59 (-14.2%); 50d below 200d
Momentum: RSI(14) 51.6 | MACD -0.170 vs signal -0.204 (histogram 0.034)
Returns: 1d +1.1% | 5d +1.8% | 1m -0.3% | 3m -12.8%
52-week range: 21.84 - 37.18 (now 6.4% of the way up)
Volatility: ATR(14) 0.51 (2.2% of price) | annualised 20d 26.7%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.10</summary>

```text
Sector: Financial Services / Banks - Regional | market cap 117.31B
Valuation: trailing P/E 14.73 | forward P/E 16.41 | P/B 9.35 | PEG n/a
Profitability: profit margin 26.8% | operating margin 33.3% | ROE 13.8%
Growth (YoY): revenue +16.6% | earnings +18.1%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 0.41 | short interest 0.7% of float
Next earnings: 2026-10-17
```

</details>

<details><summary><b>What this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Does this company beat its own forecasts</b> — score +0.10</summary>

```text
Earnings record, last 4 quarters: 2 beats, 2 in line
  2026-06-30 in line | 2026-03-31 in line | 2025-12-31 beat by 61% | 2025-09-30 beat by 10%
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

```text
Consensus: buy (mean 1.75 on a 1=strong buy to 5=strong sell scale, 4 analysts)
Ratings: 1 strong buy, 2 buy, 1 hold, 0 sell, 0 strong sell
Price target: mean 30.52 (+33.7% vs last close), range 26.10 - 35.00
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

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

### Royal Bank of Canada (RY) · Company — NEUTRAL, confidence 0.40

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: negative short‑interest surge and weak technicals versus solid fundamentals, bullish analyst consensus, and a cluster of insider purchases. No clear, material catalyst for the next few days, so a neutral stance with moderate conviction.

**Main reasons it gave:**
- Short interest rose sharply in September (negative sentiment)
- Price below 20‑day and 50‑day SMAs, RSI 39.9, volume 0.11× 20‑day avg (weak technicals)
- Insiders bought 800k shares in late September (bullish insider activity)
- Analysts maintain buy consensus with +6.9% price target (bullish analyst view)
- Solid fundamentals: P/E 17, ROE 16.2%, earnings growth 12.8% YoY

<details><summary><b>News</b> — score -0.20</summary>

- [Royal Bank of Canada (RY.TO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY.TO/)  
  <sub>Yahoo! Finance Canada, 5 hours ago</sub>  
  Royal Bank of Canada (RY.TO) · -1.37% · -4.00% · 15.10% · 17.00% · 36.07% · 113.39% · 3,993.91%. Key Events. Baseline. Advanced Chart.
- [Royal Bank of Canada (RY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RY/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  3,252.35% · Previous Close 191.91 · Open 192.00 · Bid 185.00 x 20000 · Ask 207.00 x 10000 · Day's Range 192.26 - 193.57 · 52 Week Range 143.13 - 218.57 · Volume...
- [Royal Bank Of Canada (NYSE:RY) Stock Short Interest Climbs 140.9%](https://www.marketbeat.com/instant-alerts/options-royal-bank-of-canada-nyse-ry-stock-short-interest-climbs-1409-2026-10-13/)  
  <sub>MarketBeat, 5 hours ago</sub>  
  Royal Bank Of Canada (NYSE:RY - Get Free Report) (TSE:RY) was the target of a significant increase in short interest in the month of September.
- [Royal Bank of Canada (RY.TO) stock price, news, quote and history](https://au.finance.yahoo.com/quote/RY.TO/)  
  <sub>Yahoo Finance Australia, 12 hours ago</sub>  
  Royal Bank of Canada (RY.TO) · -1.37% · -4.00% · 15.10% · 17.00% · 36.07% · 113.39% · 3,993.91%. Key events. Baseline. Advanced chart.
- [Two in five Canadians needed the help of a charity or nonprofit last year: RBC poll](https://www.theglobeandmail.com/investing/markets/stocks/RY/pressreleases/6654530/two-in-five-canadians-needed-the-help-of-a-charity-or-nonprofit-last-year-rbc-poll/)  
  <sub>The Globe and Mail, 4 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-N) from The Globe and Mail including charting and trades.
- [Royal Bank of Canada stock pre-market at EUR 173.08](https://www.ad-hoc-news.de/boerse/news/vorboerse/royal-bank-of-canada-stock-pre-market-at-eur-173-08/70309399)  
  <sub>ad-hoc-news.de, 9 hours ago</sub>  
  Royal Bank of Canada stock is at EUR 173.08 pre-market on October 13, 2026, according to Lang & Schwarz. The quote was recorded at 7:40 a.m. CEST.
- [WEXF ETF Holdings List — HAN:WEXF](https://www.tradingview.com/symbols/HAN-WEXF/holdings/)  
  <sub>TradingView, 16 hours ago</sub>  
  Amundi ETF ICAV - Amundi MSCI World ex USA UCITS ETF USD. WEXF Hannover Stock Exchange. WEXF Hannover Stock Exchange. Market closed. No trades. No trades.
- [Can Royal Bank of Canada (TSX:RY) Sustain Its Strength?](https://kalkinemedia.com/ca/stocks/financial/can-royal-bank-of-canada-tsxry-sustain-its-strength)  
  <sub>Kalkine Media, 17 hours ago</sub>  
  Review Royal Bank of Canada's quarterly performance, digital banking, credit conditions, and diversified operations within the wider Canadian financial...
- [OSFI flags AI risks as Royal Bank of Canada stock trades at EUR 173.21](https://www.ad-hoc-news.de/boerse/news/corporate-news/osfi-flags-ai-risks-as-royal-bank-of-canada-stock-trades-at-eur-173-21/70312492)  
  <sub>ad-hoc-news.de, 6 hours ago</sub>  
  OSFI flagged frontier AI risks on October 8, 2026. Royal Bank of Canada stock was EUR 173.21 on October 13, 2026. Its market value was USD 267.9 billion on...
- [Why Lucid Group Stock Is Moving in Reverse Today](https://www.theglobeandmail.com/investing/markets/stocks/RY-T/pressreleases/6214019/why-lucid-group-stock-is-moving-in-reverse-today/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Detailed price information for Royal Bank of Canada (RY-T) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.50</summary>

```text
Last close 194.45 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 198.02 (-1.8%), 50d 204.37 (-4.9%), 200d 187.25 (+3.8%); 50d above 200d
Momentum: RSI(14) 39.9 | MACD -3.516 vs signal -3.228 (histogram -0.288)
Returns: 1d +0.9% | 5d -1.0% | 1m -5.2% | 3m -10.7%
52-week range: 144.58 - 217.87 (now 68.0% of the way up)
Volatility: ATR(14) 2.98 (1.5% of price) | annualised 20d 17.3%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 269.20B
Valuation: trailing P/E 17.00 | forward P/E 15.52 | P/B 2.87 | PEG 2.26
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

<details><summary><b>What analysts and big funds say</b> — score +0.50</summary>

```text
Consensus: buy (mean 2.13 on a 1=strong buy to 5=strong sell scale, 3 analysts)
Ratings: 4 strong buy, 5 buy, 5 hold, 0 sell, 1 strong sell
Price target: mean 207.92 (+6.9% vs last close), range 183.05 - 225.24
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

<details><summary><b>What analysts say about what this fund holds</b> — score +0.50</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.60</summary>

```text
Last 180 days: bought 0 shares in 0 transaction(s) | sold n/a shares in 0
Net: +0 shares | insiders hold 387,640 shares
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

### JPMorgan Chase (JPM) · Company — NEUTRAL, confidence 0.35

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> mixed signals: earnings miss and weak technicals pull down, but strong fundamentals and bullish analyst consensus offset; overall net small positive but not enough for a clear directional call

**Main reasons it gave:**
- Q3 earnings miss: EPS $5.75 vs $5.92 estimate
- Strong fundamentals: trailing P/E 14.38, ROE 17.8%
- Technical weakness: price below 20‑day and 50‑day SMA, RSI 42.9, low volume
- Analyst consensus buy with mean price target $372.14 (+10.9%)

<details><summary><b>News</b> — score -0.45</summary>

- [JPMorgan Chase & Co. (JPM) stock price, news, quote and history](https://uk.finance.yahoo.com/quote/JPM/)  
  <sub>Yahoo Finance UK, 3 hours ago</sub>  
  6,561.33% · Previous close 332.99 · Open 334.30 · Bid 336.50 x 8000 · Ask 334.90 x 16000 · Day's range 333.55 - 336.34 · 52-week range 279.10 - 366.50 · Volume...
- [JPMorgan posts rare profit miss as dealmaking, bond trading lose momentum](https://www.reuters.com/business/finance/jpmorgans-profit-rises-investment-banking-trading-strength-2026-10-13/)  
  <sub>Reuters, 3 hours ago</sub>  
  Oct 13 (Reuters) - JPMorgan Chase (JPM.N) , opens new tab fell short of quarterly profit estimates for the first time in nearly three years as market...
- [Stocks making the biggest moves premarket: JPMorgan Chase, Micron, UnitedHealth & more](https://www.cnbc.com/2026/10/13/stocks-making-the-biggest-moves-premarket-jpm-mu-unh.html)  
  <sub>CNBC, 3 hours ago</sub>  
  These are the stocks posting the largest moves before the bell.
- [JPM Stock: JPMorgan shares fluctuate after rare Q3 earnings miss and slowing dealmaking momentum](https://www.clarin.com/us-news/jpm-stock-jpmorgan-shares-fluctuate-after-rare-q3-earnings-miss-and-slowing-dealmaking-momentum_0_kBBM3aXQf8.html)  
  <sub>Clarin.com, 3 hours ago</sub>  
  A summer surge in Wall Street trading wasnt enough to prevent a rare quarterly earnings miss for JPMorgan Chase. While consumer lending held strong,...
- [JPMorgan profit misses analyst estimates as Jamie Dimon warns economic forces 'shift under the surface'](https://finance.yahoo.com/markets/article/jpmorgan-profit-misses-analyst-estimates-as-jamie-dimon-warns-economic-forces-shift-under-the-surface-112446859.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  JPMorgan Chase (JPM) reported another quarter of rising profits on Tuesday even as revenues from some of its biggest Wall Street businesses retreated after...
- [JPMorgan Chase & Co. $JPM Stock Holdings Boosted by NorthCrest Asset Manangement LLC](https://www.marketbeat.com/instant-alerts/filing-jpmorgan-chase-co-jpm-stock-holdings-boosted-by-northcrest-asset-manangement-llc-2026-10-13/)  
  <sub>MarketBeat, 3 hours ago</sub>  
  NorthCrest Asset Manangement LLC boosted its stake in JPMorgan Chase & Co. (NYSE:JPM - Free Report) by 2.5% in the 3rd quarter, according to the company in...
- [JPMorgan stock recovers after Q3 earnings disappoint as markets soften (JPM:NYSE)](https://seekingalpha.com/news/4652368-jpmorgan-stock-recovers-after-q3-earnings-disappoint-as-markets-soften)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  JPMorgan Chase (JPM) stock rose 1.1% in Tuesday premarket trading, recovering from an early dip, after the bank's Q3 earnings and revenue missed Wall Street...
- [Jamie Dimon Says U.S. Economy Remains Strong, But Warns Of Risks ‘Shifting Under The Surface’ — JPM Stock Gains Despite Q3 Earnings Miss](https://stocktwits.com/news-articles/markets/equity/jamie-dimon-us-economy-jpm-stock-gains-despite-q3-earnings-miss/cZxBLYzRBoq)  
  <sub>Stocktwits, 3 hours ago</sub>  
  JPMorgan reported an 8% increase in Q3 revenue to $50.2 billion, but below Wall Street's estimate of about $51.22 billion, according to Fiscal.ai.
- [JPMorgan Chase & Co. (NYSE:JPM) Q3 2026 Earnings Miss Estimates, Shares Slide Premarket](https://www.chartmill.com/news/JPM/Chartmill-56131-JPMorgan-Chase-Co-NYSEJPM-Q3-2026-Earnings-Miss-Estimates-Shares-Slide-Premarket)  
  <sub>ChartMill, 3 hours ago</sub>  
  JPMorgan Q3 2026 earnings miss estimates: revenue $50.17B vs $51.65B, EPS $5.75 vs $5.92; JPM shares fell 3.38% premarket on the miss.
- [JP Morgan Analysis - Is JPM Going to Trend Higher? - JPMorgan Chase (NYSE:JPM)](https://www.benzinga.com/trading-ideas/technicals/26/10/62323370/stock-of-the-day-is-jp-morgan-about-to-trend-higher)  
  <sub>Benzinga, 1 hour ago</sub>  
  JPMorgan Chase & Co. (NYSE:JPM is trading higher on Tuesday after releasing its third-quarter earnings report. The stock broke its recent downtrend last...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.45</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 335.56 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 337.73 (-0.6%), 50d 349.45 (-4.0%), 200d 322.21 (+4.1%); 50d above 200d
Momentum: RSI(14) 42.9 | MACD -4.787 vs signal -5.118 (histogram 0.332)
Returns: 1d +0.4% | 5d +1.3% | 1m -4.2% | 3m -3.3%
52-week range: 282.84 - 365.18 (now 64.0% of the way up)
Volatility: ATR(14) 6.19 (1.8% of price) | annualised 20d 16.9%
Volume: 0.65x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

```text
Sector: Financial Services / Banks - Diversified | market cap 891.98B
Valuation: trailing P/E 14.38 | forward P/E 13.36 | P/B 2.52 | PEG 1.57
Profitability: profit margin 34.9% | operating margin 50.4% | ROE 17.8%
Growth (YoY): revenue +30.4% | earnings +46.9%
Balance sheet: debt/equity n/a | free cash flow n/a
Risk: beta 1.01 | short interest 0.9% of float
Next earnings: 2026-10-13
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

<details><summary><b>What analysts and big funds say</b> — score +0.10</summary>

```text
Consensus: buy (mean 2.12 on a 1=strong buy to 5=strong sell scale, 22 analysts)
Ratings: 4 strong buy, 9 buy, 12 hold, 0 sell, 0 strong sell
Price target: mean 372.14 (+10.9% vs last close), range 305.00 - 420.00
Recent rating changes:
  - 2026-10-05 UBS: main, Buy -> Buy
  - 2026-09-28 HSBC: main, Hold -> Hold
  - 2026-08-14 Wells Fargo: main, Overweight -> Overweight
  - 2026-08-03 UBS: main, Buy -> Buy
  - 2026-07-20 Citigroup: main, Neutral -> Neutral
  - 2026-07-17 Evercore ISI Group: main, Outperform -> Outperform
Institutional ownership: 75.7%
Largest holders: Blackrock Inc. (7.8%), Vanguard Capital Management LLC (6.1%), State Street Corporation (4.7%), Bank of America Corporation (2.6%), Morgan Stanley (2.5%)
```

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.00</summary>

```text
Last 180 days: bought 136,610 shares in 7 transaction(s) | sold 230,236 shares in 19
Net: -93,626 shares (-0.9% of insider holdings) | insiders hold 10,393,508 shares
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

### Elbit Systems (ESLT) · Company — NEUTRAL, confidence 0.30

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: bearish technicals and a target cut offset by strong earnings record and modest analyst upside; overall net score is neutral.

**Main reasons it gave:**
- Jefferies cut target to $790 (negative news)
- Price 661.27 below 20‑day SMA 706.49, 50‑day SMA 735.94, 200‑day SMA 777.80 (technical weakness)
- RSI 32.7 and MACD histogram -4.695 indicating weak momentum (technical)
- Four consecutive earnings beats (earnings record)
- Trailing P/E 49.76 (high valuation) (fundamentals)

<details><summary><b>News</b> — score -0.20</summary>

- [QTEX Stock More Than Doubles Pre-Market: What’s Driving The Rally?](https://stocktwits.com/news-articles/markets/equity/why-is-qtex-stock-surging-today/cZgOTYeRepU)  
  <sub>Stocktwits, 19 hours ago</sub>  
  A little-known Nasdaq microcap suddenly became one of retail traders' hottest quantum bets on Tuesday. Shares of QTREX Quantum (QTEX) skyrocketed in...
- [Jefferies cuts target for Elbit Systems stock to USD 790](https://www.ad-hoc-news.de/boerse/news/corporate-news/jefferies-cuts-target-for-elbit-systems-stock-to-usd-790/70311255)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  ESLT, IL0010811243. Jefferies cuts target for Elbit Systems stock to USD 790. Published on 10/13/2026 at 09:36 | Editorial responsibility: Rafael Müller,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 661.27 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 706.49 (-6.4%), 50d 735.94 (-10.1%), 200d 777.80 (-15.0%); 50d below 200d
Momentum: RSI(14) 32.7 | MACD -20.930 vs signal -16.235 (histogram -4.695)
Returns: 1d +1.1% | 5d -4.3% | 1m -8.8% | 3m -9.6%
52-week range: 454.95 - 1,014.33 (now 36.9% of the way up)
Volatility: ATR(14) 16.80 (2.5% of price) | annualised 20d 27.1%
Volume: 1.02x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

```text
Sector: Industrials / Aerospace & Defense | market cap 30.99B
Valuation: trailing P/E 49.76 | forward P/E 36.01 | P/B 7.01 | PEG n/a
Profitability: profit margin 7.4% | operating margin 9.6% | ROE 15.2%
Growth (YoY): revenue +15.9% | earnings +34.2%
Balance sheet: debt/equity 19.3% | free cash flow -38.48M
Risk: beta -0.30 | short interest 0.8% of float
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

```text
Consensus: hold (mean 2.67 on a 1=strong buy to 5=strong sell scale, 6 analysts)
Ratings: 0 strong buy, 1 buy, 5 hold, 0 sell, 0 strong sell
Price target: mean 801.33 (+21.2% vs last close), range 518.00 - 960.00
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

### ASML (ASML) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ASML (ASML) Has EUV to Itself. Is 41 Times Earnings Too Much?](https://finance.yahoo.com/markets/stocks/articles/asml-asml-euv-itself-41-121354133.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The most important machine in the AI boom isn't a chip. It's the tool that prints them, and only one company makes the most advanced version.
- [Why is ASML stock sliding today?](https://www.investing.com/news/stock-market-news/why-is-asml-stock-sliding-today-93CH-4945877)  
  <sub>Investing.com, 5 hours ago</sub>  
  Investing.com -- ASML Holding NV stock slipped 1.2% during today's session, pulling back to €1,557.4 from a previous close of €1,575.8, as investors trimmed...
- [ASML Earnings: 6 Numbers Long-Term Investors Should Look For on Oct. 14](https://www.fool.com/investing/2026/10/13/asml-earnings-6-numbers-long-term-investors-should/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  ASML plays an irreplaceable role in manufacturing the world's most advanced artificial intelligence (AI) chips.
- [ASML options traders build deep downside defenses ahead of earnings (ASML:NASDAQ)](https://seekingalpha.com/news/4652487-asml-options-traders-build-deep-downside-defenses-ahead-of-earnings)  
  <sub>Seeking Alpha, 7 minutes ago</sub>  
  ASML options imply a ~5.5% post-earnings move as traders build key support/resistance levels and hedges.
- [SKHY Stock Slips As ASML Cost Shock Rattles Chip Traders](https://www.timothysykes.com/news/sk-hynix-inc-skhy-news-2026_10_13/)  
  <sub>Timothy Sykes, 3 hours ago</sub>  
  SK hynix Inc. stocks have been trading down by -5.36 percent amid reports of weakening AI memory demand outlook. Key Takeaways SK Hynix shares slid 2.3%...
- [SKHY Stock Drops As ASML Cost Shock Rattles Traders](https://stockstotrade.com/news/sk-hynix-inc-skhy-news-2026_10_13-2/)  
  <sub>StocksToTrade, 2 hours ago</sub>  
  SK hynix Inc. stocks have been trading down by -6.24 percent amid reports of weakening memory demand and cautious AI spending. Key Takeaways SK Hynix shares...
- [Micron, Seagate, Western Digital sink as chip sell-off deepens](https://www.cnbc.com/2026/10/13/sk-hynix-softbank-samsung-electronics-shares-tech-stocks-fall.html)  
  <sub>CNBC, 13 hours ago</sub>  
  Technology stocks tumbled Tuesday as a sell-off in U.S. semiconductor shares spilled into Asian and European markets.
- [Why October 14 Could Change Everything for ASML Stock](https://247wallst.com/investing/2026/10/12/why-october-14-could-change-everything-for-asml-stock/)  
  <sub>24/7 Wall St., 22 hours ago</sub>  
  ASML holds a near-monopoly on the machines powering the AI chip revolution, yet its stock keeps lagging the semiconductor rally. Its Q3 earnings report on...
- [SNDK, NVDA, SKHY, ASML Stocks Extend Slide Overnight As China’s Chip Challenge Rattles Investors](https://stocktwits.com/news-articles/markets/equity/sndk-nvda-skhy-asml-stocks-extend-slide-overnight-amid-china-ai-challenge-tech-rotation/cZZCeckR766)  
  <sub>Stocktwits, 19 hours ago</sub>  
  The company posted a net loss of $228.22 million, or a diluted loss of $0.95 per share. On an adjusted basis, Navitas reported a second-quarter EPS loss of...
- [Is ASML Holding NV's Stock a Buy Ahead of Its Q3 Earnings Report Wednesday?](https://www.fool.com/investing/2026/10/12/is-asml-holding-nvs-stock-a-buy-ahead-of-its-qx-earnings-report-tomorrow/)  
  <sub>The Motley Fool, 18 hours ago</sub>  
  ASML (ASML -1.69%) doesn't get as much attention as chip stocks like Nvidia do, but the European semiconductor capital equipment specialist is arguably just...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,715.07 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 1,759.49 (-2.5%), 50d 1,742.49 (-1.6%), 200d 1,568.51 (+9.3%); 50d above 200d
Momentum: RSI(14) 44.5 | MACD 14.367 vs signal 21.532 (histogram -7.165)
Returns: 1d -2.0% | 5d -6.5% | 1m +8.9% | 3m -5.5%
52-week range: 966.57 - 1,989.44 (now 73.2% of the way up)
Volatility: ATR(14) 50.59 (2.9% of price) | annualised 20d 29.1%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductor Equipment & Materials | market cap 658.76B
Valuation: trailing P/E 55.67 | forward P/E 29.32 | P/B 1,496.92 | PEG 1.58
Profitability: profit margin 30.1% | operating margin 37.1% | ROE 53.9%
Growth (YoY): revenue +21.3% | earnings +28.5%
Balance sheet: debt/equity 9.1% | free cash flow 8.44B
Risk: beta 1.30 | short interest 0.4% of float
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
Consensus: strong_buy (mean 1.43 on a 1=strong buy to 5=strong sell scale, 16 analysts)
Ratings: 6 strong buy, 31 buy, 4 hold, 1 sell, 0 strong sell
Price target: mean 2,109.57 (+23.0% vs last close), range 865.76 - 2,895.75
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
Net: +0 shares | insiders hold 1,707,111 shares
Distinct insiders: 0 buying, 0 selling
```

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

_Not available today._

</details>

### Alphabet (Google) (GOOGL) · Company — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [GOOG, GOOGL Stock Alert: Alphabet AI Issues and Subsequent 4% Stock Drop Trigger Securities Fraud Class Action for Investors](https://www.morningstar.com/news/pr-newswire/20261013ny70049/goog-googl-stock-alert-alphabet-ai-issues-and-subsequent-4-stock-drop-trigger-securities-fraud-class-action-for-investors)  
  <sub>Morningstar, 5 hours ago</sub>  
  GOOG, GOOGL Stock Alert: Alphabet AI Issues and Subsequent 4% Stock Drop Trigger Securities Fraud Class Action for Investors...
- [Why Google (GOOGL) Offers Asymmetric Upside Potential?](https://finance.yahoo.com/markets/stocks/articles/why-google-googl-offers-asymmetric-120806718.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Patient Capital Management, based in Baltimore, released its third-quarter 2026 investor letter for the “Patient Opportunity Equity Strategy”.
- [ALPHABET INC. (GOOG, GOOGL) SHAREHOLDER ALERT Bernstein](https://www.globenewswire.com/news-release/2026/10/13/3379813/0/en/alphabet-inc-goog-googl-shareholder-alert-bernstein-liebhard-llp-reminds-alphabet-inc-investors-of-upcoming-deadline.html)  
  <sub>GlobeNewswire, 1 hour ago</sub>  
  Alphabet Holdings Shareholders Between May 19, 2026 and July 16, 2026 - Contact Bernstein Liebhard For More Information Regarding Lawsuit...
- [GOOGL Stock Tops Retail Pick Over AMZN, META, MSFT For Next 12 Months – But META Leads Wall Street Upside](https://stocktwits.com/news-articles/markets/equity/googl-stock-tops-retail-sentiment-amzn-meta-msft-12-months/cZoq7QnRJhY)  
  <sub>Stocktwits, 20 hours ago</sub>  
  GOOGL stock captured 36% of the vote among more than 3,300 respondents, putting it well ahead of Microsoft (MSFT), which received 22%. Amazon (AMZN) and Meta...
- [Between Amazon and Alphabet One’s Gotten Much More Bang for Their 200 Billion Bucks](https://247wallst.com/investing/2026/10/13/between-amazon-and-alphabet-ones-gotten-much-more-bang-for-their-200-billion-bucks/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Google Cloud (GOOGL) grew 82% versus AWS's (AMZN) 37%, yet the faster grower trades at a cheaper 23x forward earnings than Amazon's 24x.
- [$10,000 Invested Equally in Alphabet and Nvidia Could Be Worth This Much by 2030](https://www.fool.com/investing/2026/10/12/10000-invested-equally-in-alphabet-and-nvidia-cou/)  
  <sub>The Motley Fool, 16 hours ago</sub>  
  Split $10000 between Alphabet and Nvidia today, and by 2030 that bet touches everything from search ads to robotaxis to quantum chips.
- [Alphabet’s Gemini Success: Fueling Growth And Investor Returns (NASDAQ:GOOGL)](https://seekingalpha.com/article/4953607-alphabet-gemini-success-fueling-growth-and-investor-returns)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  Alphabet Inc. stock is up 79% on Wiz and GCP AI security. Click for this GOOGL update and see if it is the right stock for you.
- [Wall Street analysts update Google (GOOGL) stock price target for 12 months](https://finbold.com/wall-street-analysts-update-google-googl-stock-price-target-for-12-months/)  
  <sub>Finbold, 22 hours ago</sub>  
  Despite Googl stock fallen more than 13% from its 52-week peak, analysts are largely expecting a rally to a new ATH in 12 months.
- [Big Tech Should Pay Iran Fees for Strait of Hormuz Cables: Iran Media Report - Alphabet (NASDAQ:GOOGL)](https://www.benzinga.com/markets/tech/26/10/62313882/google-meta-microsoft-and-amazon-should-pay-fees-for-hormuz-cables-report)  
  <sub>Benzinga, 9 hours ago</sub>  
  An Iranian news agency said Iran should make Google, Meta, Microsoft, and Amazon pay permit fees for subsea cables through the Strait of Hormuz.
- [Frances Arnold, Alphabet director, sells $28,257 in stock](https://www.investing.com/news/insider-trading-news/frances-arnold-alphabet-director-sells-28257-in-stock-93CH-4945272)  
  <sub>Investing.com, 14 hours ago</sub>  
  Frances Arnold, a director at Alphabet Inc. (NASDAQ:GOOGL), sold 83 shares of the company's Class C Capital Stock on September 30, 2026.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 354.26 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 346.55 (+2.2%), 50d 345.80 (+2.4%), 200d 340.42 (+4.1%); 50d above 200d
Momentum: RSI(14) 58.6 | MACD 2.076 vs signal 0.892 (histogram 1.184)
Returns: 1d +0.4% | 5d +1.9% | 1m +1.4% | 3m -4.5%
52-week range: 244.15 - 402.62 (now 69.5% of the way up)
Volatility: ATR(14) 8.13 (2.3% of price) | annualised 20d 20.5%
Volume: 0.33x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Communication Services / Internet Content & Information | market cap 4.33T
Valuation: trailing P/E 17.77 | forward P/E 23.24 | P/B 6.96 | PEG 1.25
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
Price target: mean 430.40 (+21.5% vs last close), range 340.00 - 515.00
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

- [Will Eli Lilly Do a Stock Split Before the End of 2026?](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-stock-split-end-062001028.html)  
  <sub>Yahoo Finance, 8 hours ago</sub>  
  When stocks start trading north of the $1,000 mark, investors often wonder if a stock split may be coming. A stock split reduces the price of a stock,...
- [BMO Capital Sticks to Its Buy Rating for Eli Lilly & Co (LLY)](https://www.theglobeandmail.com/investing/markets/stocks/LLY/pressreleases/6763726/bmo-capital-sticks-to-its-buy-rating-for-eli-lilly-co-lly/)  
  <sub>The Globe and Mail, 2 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [Missed Eli Lilly's Rally? Here Is What Holders Saw](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-lly/eli-lilly/news/missed-eli-lillys-rally-here-is-what-holders-saw)  
  <sub>Simply Wall Street, 11 hours ago</sub>  
  If Eli Lilly sat on your watchlist instead of in your portfolio, the gap between watching and owning may feel uncomfortable. For Eli Lilly shareholders,...
- [Eli Lilly Expects Up to $87 Billion in 2026 Revenue. Here's Why the Stock Still Looks Undervalued.](https://finance.yahoo.com/markets/stocks/articles/eli-lilly-expects-87-billion-093000216.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  Eli Lilly (NYSE: LLY) stock has soared 400% over the past five years, and though the momentum slowed in the early months of this year, it's now on the rise...
- [Eli Lilly & Co Shs Cert Deposito Arg Repr 0.14285714 Shs](https://www.tradingview.com/symbols/BCBA-LLY.CI/financials-income-statement/net-income-bef-disc-oper/)  
  <sub>TradingView, 7 hours ago</sub>  
  Net income before discontinued operations, quarterly and annual stats of Eli Lilly & Co Shs Cert Deposito Arg Repr 0.14285714 Shs.
- [Here Are Morgan Stanley's New Top Stock Picks For The Next 12-Months](https://stocktwits.com/news-articles/markets/equity/here-are-morgan-stanley-s-new-top-stock-picks-for-the-next-12-months/cZMRDYdRBIV)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Morgan Stanley unveils 2027 'vintage values' roster after 2026 roster outperforms S&P 500.
- [RBC Capital Sticks to Their Buy Rating for Eli Lilly & Co (LLY)](https://www.theglobeandmail.com/investing/markets/stocks/LLY-N/pressreleases/6712314/rbc-capital-sticks-to-their-buy-rating-for-eli-lilly-co-lly/)  
  <sub>The Globe and Mail, 3 hours ago</sub>  
  Detailed price information for Eli Lilly and Company (LLY-N) from The Globe and Mail including charting and trades.
- [Eli Lilly (LLY) Maintains Strong Growth Outlook Amid Price Press](https://www.gurufocus.com/news/9119366/eli-lilly-lly-maintains-strong-growth-outlook-amid-price-pressures)  
  <sub>GuruFocus, 23 hours ago</sub>  
  On October 12, 2026, RBC Capital Markets reaffirmed its "Outperform" rating for Eli Lilly and Co (LLY), setting a target price of $1500.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 1,176.59 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 1,165.56 (+0.9%), 50d 1,175.75 (+0.1%), 200d 1,077.55 (+9.2%); 50d above 200d
Momentum: RSI(14) 53.1 | MACD 2.516 vs signal -0.486 (histogram 3.002)
Returns: 1d -0.5% | 5d +1.7% | 1m +3.4% | 3m +1.7%
52-week range: 799.57 - 1,280.34 (now 78.4% of the way up)
Volatility: ATR(14) 32.20 (2.7% of price) | annualised 20d 20.2%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 1.05T
Valuation: trailing P/E 39.50 | forward P/E 24.69 | P/B 30.96 | PEG 1.14
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
Consensus: buy (mean 1.63 on a 1=strong buy to 5=strong sell scale, 29 analysts)
Ratings: 6 strong buy, 19 buy, 3 hold, 1 sell, 1 strong sell
Price target: mean 1,330.14 (+13.1% vs last close), range 930.00 - 1,600.00
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

- [Microsoft Reveals Next-Gen Maia 300 Custom AI Chip For Widespread Deployment](https://www.tikr.com/blog/microsoft-maia-300-custom-ai-chip-deployment)  
  <sub>TIKR.com, 2 hours ago</sub>  
  Now Live: Discover how much upside your favorite stocks could have using TIKR's new Valuation Model (It's free)>>>. What Happened? Microsoft (MSFT)...
- [Microsoft: Finally, Found Its AI Angle](https://seekingalpha.com/article/4953673-microsoft-finally-found-its-ai-angle)  
  <sub>Seeking Alpha, 7 hours ago</sub>  
  Microsoft has rebounded in AI sentiment, but fundamental capability gaps persist versus hyperscaler peers. Check out why MSFT stock is a hold.
- [MSFT Stock Jumps 3% After-Hours — Lower-Than-Expected Q4 Capex, Strong Azure Sales Boost Sentiment](https://stocktwits.com/news-articles/markets/equity/msft-stock-jumps-3-after-hours-lower-than-expected-q4-capex-strong-azure-sales-boost-sentiment/cZNT9ukRJTF)  
  <sub>Stocktwits, 11 hours ago</sub>  
  In a statement, Microsoft Chief Executive Officer Satya Nadella said the company now has over 30 million paid subscribers for Microsoft 365 Copilot, its Office...
- [Microsoft’s CEO Just Called for a Kill Switch on AI. Here Is What It Means for the Stock.](https://247wallst.com/investing/2026/10/13/microsofts-ceo-just-called-for-a-kill-switch-on-ai-here-is-what-it-means-for-the-stock/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Satya Nadella publicly asked for a way to stop his own AI products cold, and the reasoning behind that request has real consequences for whether Microsoft's...
- [Microsoft Stock Heads for a Record High With More AI Upside Ahead](https://www.barrons.com/articles/microsoft-stock-on-pace-record-high-d6d67bab)  
  <sub>Barron's, 38 minutes ago</sub>  
  Microsoft stock is on pace for a record closing high and Wall Street believes there's more upside.
- [J.P. Morgan Maintains Microsoft(MSFT.US) With Buy Rating, Maintains Target Price $625](https://www.moomoo.com/news/post/1001048927/jp-morgan-maintains-microsoft-msftus-with-buy-rating-maintains-target)  
  <sub>Moomoo, 48 minutes ago</sub>  
  J.P.Morgan analyst Samik Chatterjee maintains $Microsoft(MSFT.US)$ with a buy rating, and maintains the target price at $625.According to TipRanks data,...
- [Microsoft Stock Moves Higher Monday: What's Happening?](https://www.benzinga.com/trading-ideas/movers/26/10/62303851/microsoft-stock-moves-higher-monday-whats-happening)  
  <sub>Benzinga, 23 hours ago</sub>  
  Microsoft Corp (NASDAQ:MSFT) shares are climbing Monday. The company said it will scale up its Azure Maia system to multi-gigawatt deployments.
- [Dan Ives Says Semiconductor Sell-Off Is ‘Way Overdone’ As AI Spending Fears Rattle NVDA, MU, SKHY, SNDK](https://www.tradingview.com/news/stocktwits:d76483227094b:0-dan-ives-says-semiconductor-sell-off-is-way-overdone-as-ai-spending-fears-rattle-nvda-mu-skhy-sndk/)  
  <sub>TradingView, 4 hours ago</sub>  
  Semiconductor stocks extended their slide in morning trading on Tuesday as AI chip competition and AI spending concerns continued to weigh on the sector;...
- [MSFT Oct 2026 532.500 call (MSFT261009C00532500) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/MSFT261009C00532500/)  
  <sub>Yahoo! Finance Canada, 11 hours ago</sub>  
  Find the latest MSFT Oct 2026 532.500 call (MSFT261009C00532500) stock quote, history, news and other vital information to help you with your stock trading...
- [MSFT Stock Rises Premarket Ahead Of Q4 Results: CapEx, Azure Growth In Focus](https://stocktwits.com/news-articles/markets/equity/msft-stock-rises-premarket-ahead-of-q4-results-cap-ex-azure-growth-in-focus/cZNR8GoRJRW)  
  <sub>Stocktwits, 20 hours ago</sub>  
  Microsoft rose 1% in early premarket trading on Wednesday, ahead of its quarterly report after the markets close. Once one of the key stocks rising in the...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 548.52 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 514.46 (+6.6%), 50d 503.19 (+9.0%), 200d 434.58 (+26.2%); 50d above 200d
Momentum: RSI(14) 72.5 | MACD 12.755 vs signal 10.247 (histogram 2.508)
Returns: 1d +1.4% | 5d +3.6% | 1m +8.5% | 3m +38.6%
52-week range: 352.83 - 548.52 (now 100.0% of the way up)
Volatility: ATR(14) 11.43 (2.1% of price) | annualised 20d 21.1%
Volume: 0.36x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Software - Infrastructure | market cap 4.07T
Valuation: trailing P/E 30.90 | forward P/E 23.17 | P/B 9.21 | PEG 1.62
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
Price target: mean 589.60 (+7.5% vs last close), range 440.00 - 870.00
Recent rating changes:
  - 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
  - 2026-10-05 Scotiabank: main, Sector Outperform -> Sector Outperform
  - 2026-10-01 Wells Fargo: main, Overweight -> Overweight
  - 2026-09-30 Piper Sandler: main, Overweight -> Overweight
  - 2026-09-23 Stifel: up, Hold -> Buy
  - 2026-09-22 Oppenheimer: main, Outperform -> Outperform
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

- [Nvidia (NVDA) Was Among Claude AI’s Top Picks This Year. Can The Stock Keep Rising?](https://finance.yahoo.com/markets/stocks/articles/nvidia-nvda-among-claude-ai-133927424.html)  
  <sub>Yahoo Finance, 1 hour ago</sub>  
  While Nvidia Corporation (NASDAQ:NVDA) is one of the best-performing stock picks of Claude AI this year, ranking #2 on our list of the 8 best-performing...
- [Nvidia-backed AI Company Firmus Just Canceled its IPO. What That Means for NVDA Stock.](https://www.barchart.com/story/news/6666291/nvidia-backed-ai-company-firmus-just-canceled-its-ipo-what-that-means-for-nvda-stock)  
  <sub>Barchart.com, 4 hours ago</sub>  
  Firmus, backed by Nvidia, pulled its $5 billion IPO after investors balked at the price and debt. Here is what it means for Nvidia stock and the AI trade.
- [Broadcom vs. Nvidia: The AI Revolution Is Big Enough for Both. Here's the Better Buy.](https://www.fool.com/investing/2026/10/13/broadcom-vs-nvidia-the-ai-revolution-is-big-enough/)  
  <sub>The Motley Fool, 3 hours ago</sub>  
  Nvidia and Broadcom are two of the best-positioned stocks for the continued AI infrastructure boom.
- [NVDA Stock Climbs Over 1% — Nvidia Says Its AI ‘Roadmap Is Intact’ After Report Of Kyber Rack Delay](https://stocktwits.com/news-articles/markets/equity/nvda-stock-rises-after-nvidia-says-ai-roadmap-intact-despite-kyber-delay-report/cZm1ke5R7lr)  
  <sub>Stocktwits, 8 hours ago</sub>  
  NVDA Stock Climbs Over 1% — Nvidia Says Its AI 'Roadmap Is Intact' After Report Of Kyber Rack Delay. The chipmaker said its product roadmap remains on track...
- [Nvidia: The Buyback Is The Opportunity (NASDAQ:NVDA)](https://seekingalpha.com/article/4953767-nvidia-the-buyback-is-the-opportunity)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Nvidia Corporation maintains a Strong Buy as management backs FY28 guidance with a record $235B buyback program. Read more on NVDA stock here.
- [NVIDIA Corporation $NVDA Stock: Transamerica Financial Advisors LLC Increases Stake](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-transamerica-financial-advisors-llc-increases-stake-2026-10-13/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Transamerica Financial Advisors LLC boosted its position in shares of NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 8.1% in the second quarter,...
- [Nvidia (NVDA) vs. Broadcom (AVGO): Which AI Stock Is a Better Buy After the OpenAI Scare?](https://finance.yahoo.com/markets/stocks/articles/nvidia-nvda-vs-broadcom-avgo-204108303.html)  
  <sub>Yahoo Finance, 11 hours ago</sub>  
  On October 8, the Financial Times reported that OpenAI's annualized revenue was about $50 billion, roughly $20 billion below figures widely reported in...
- [NVIDIA Corporation $NVDA Stock: Jacobs Equity LLC Increases Holdings](https://www.marketbeat.com/instant-alerts/filing-nvidia-corporation-nvda-stock-jacobs-equity-llc-increases-holdings-2026-10-13/)  
  <sub>MarketBeat, 7 hours ago</sub>  
  Jacobs Equity LLC grew its position in NVIDIA Corporation (NASDAQ:NVDA - Free Report) by 59.7% during the 2nd quarter, according to its most recent Form 13F...
- [INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound](https://stocktwits.com/news-articles/markets/equity/intc-amd-mu-nvda-chip-stocks-tumble-again-stalling-a-nascent-rebound/cZZmX14R7wo)  
  <sub>Stocktwits, 8 hours ago</sub>  
  INTC, AMD, MU, NVDA: Chip Stocks Tumble Again, Stalling A Nascent Rebound. A rotation into Big Tech, coupled with fears that low-cost Chinese AI models could...
- [Nvidia Corp (NVDA): Jensen Huang’s Visionary Leadership Drives Long-Term AI Growth](https://finance.yahoo.com/markets/stocks/articles/nvidia-corp-nvda-jensen-huang-120916609.html)  
  <sub>Yahoo Finance, 3 hours ago</sub>  
  Patient Capital Management, based in Baltimore, released its third-quarter 2026 investor letter for the “Patient Opportunity Equity Strategy”.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 225.90 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 228.19 (-1.0%), 50d 222.97 (+1.3%), 200d 202.53 (+11.5%); 50d above 200d
Momentum: RSI(14) 48.8 | MACD 2.681 vs signal 3.507 (histogram -0.826)
Returns: 1d -0.2% | 5d -5.6% | 1m +7.1% | 3m +6.3%
52-week range: 165.17 - 239.24 (now 82.0% of the way up)
Volatility: ATR(14) 5.45 (2.4% of price) | annualised 20d 22.2%
Volume: 0.23x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Technology / Semiconductors | market cap 5.45T
Valuation: trailing P/E 28.56 | forward P/E 14.19 | P/B 23.82 | PEG 0.48
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
Price target: mean 328.72 (+45.5% vs last close), range 180.00 - 515.00
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

- [Novo Nordisk A/S (NVO) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/NVO/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Novo Nordisk A/S (NVO) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available 8 PM to 4 AM ET, Sunday through...
- [Buybacks total 37.8M B shares at Novo Nordisk (NVO), under a programme capped at DKK 15B.](https://www.stocktitan.net/sec-filings/NVO/6-k-novo-nordisk-a-s-current-report-foreign-issuer-54d2226138f6.html)  
  <sub>Stock Titan, 4 hours ago</sub>  
  Novo Nordisk A/S reported 23,090,000 B shares repurchased under the programme launched May 6, with a cumulative transaction value of DKK 6,758,876,433 as of...
- [Novo's 'Flashy' Ozempic, Wegovy Price Cuts Unlikely To Impact LLY Stock, Says BofA](https://stocktwits.com/news-articles/markets/equity/novo-flashy-ozempic-wegovy-price-cuts-unlikely-to-impact-lly-stock/cZRwBHzR4CD)  
  <sub>Stocktwits, 11 hours ago</sub>  
  Shares of Novo Nordisk and Eli Lilly slipped in afternoon trade after the former announced a reduction in the list prices of its weight loss drugs,...
- [Eli Lilly Expects Up to $87 Billion in 2026 Revenue. Here's Why the Stock Still Looks Undervalued.](https://www.theglobeandmail.com/investing/markets/stocks/NVO/pressreleases/6637579/eli-lilly-expects-up-to-87-billion-in-2026-revenue-heres-why-the-stock-still-looks-undervalued/)  
  <sub>The Globe and Mail, 5 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.
- [Novo Nordisk A/S (NOVO-B.CO) stock price, news, quote and history - Yahoo Finance](https://sg.finance.yahoo.com/quote/NOVO-B.CO/latest-news/)  
  <sub>Yahoo Finance Singapore, 9 hours ago</sub>  
  Find the latest Novo Nordisk A/S (NOVO-B.CO) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Novo Down 11% in a Month: How Should Investors Approach the Stock Now?](https://www.tradingview.com/news/zacks:f22847983094b:0-novo-down-11-in-a-month-how-should-investors-approach-the-stock-now/)  
  <sub>TradingView, 23 hours ago</sub>  
  Novo NVO shares have fallen 11.1% over the past month, with the Capital Markets Day in London on Sept. 21 emerging as the main source of investor...
- [BIOA, GLUE Stocks Clock Worst Day In Years— What’s The NVO Connection?](https://stocktwits.com/news-articles/markets/equity/bioa-glue-stocks-clock-worst-day-in-years-what-s-the-nvo-connection/cZN4NtDRJ5G)  
  <sub>Stocktwits, 15 hours ago</sub>  
  Citi noted BIOA's greater-than-60% drop and agreed the data is a negative for BioAge's heart-disease thesis, yet argued the size of the move “seems overdone”...
- [NVO Maintains Rating by BMO Capital -- Price Target Lowered to $40.00](https://www.gurufocus.com/news/9119687/nvo-maintains-rating-by-bmo-capital-price-target-lowered-to-4000)  
  <sub>GuruFocus, 20 hours ago</sub>  
  On October 20, 2023, BMO Capital maintained its rating on Novo Nordisk (NVO) as Market Perform. However, the price target has been significantly lowered...
- [4 Healthcare Stocks Worth Owning for the Next Decade](https://www.theglobeandmail.com/investing/markets/stocks/NVO/pressreleases/6196387/4-healthcare-stocks-worth-owning-for-the-next-decade/)  
  <sub>The Globe and Mail, 23 hours ago</sub>  
  Detailed price information for Novo Nordisk A/S ADR (NVO-N) from The Globe and Mail including charting and trades.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 38.42 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 38.99 (-1.5%), 50d 43.09 (-10.8%), 200d 45.26 (-15.1%); 50d below 200d
Momentum: RSI(14) 36.8 | MACD -1.517 vs signal -1.806 (histogram 0.289)
Returns: 1d -0.4% | 5d +2.4% | 1m -11.6% | 3m -24.0%
52-week range: 35.29 - 63.98 (now 10.9% of the way up)
Volatility: ATR(14) 0.92 (2.4% of price) | annualised 20d 35.9%
Volume: 0.14x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - General | market cap 169.55B
Valuation: trailing P/E 9.39 | forward P/E 11.59 | P/B 5.13 | PEG 4.32
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
Price target: mean 45.48 (+18.4% vs last close), range 39.73 - 61.76
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

- [TEVA Stock Alert: What to Know as Teva Therapeutics' Scores FDA Approval for Schizophrenia Treament](https://finance.yahoo.com/healthcare/articles/teva-stock-alert-know-teva-175358655.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Teva Pharmaceutical stock rallied Friday on FDA approval for Weltruza. But is it already too late to invest in TEVA shares? Let's find out!
- [Teva leaders will discuss medicines in development and the company's potential over five years.](https://www.stocktitan.net/news/TEVA/teva-to-host-r-d-day-on-wednesday-november-11-in-new-york-x91xbauxaoob.html)  
  <sub>Stock Titan, 17 hours ago</sub>  
  Teva Pharmaceutical Industries (TEVA) will host an R&D Day in New York City on November 11, 2026. Leadership will discuss its research and development...
- [Teva Pharmaceutical Industries (NYSE:TEVA) Stock Price Target Raised at JPMorgan Chase & Co.](https://www.marketbeat.com/instant-alerts/analyst-teva-pharmaceutical-industries-nyse-teva-stock-price-target-raised-at-jpmorgan-chase-co-2026-10-12/)  
  <sub>MarketBeat, 20 hours ago</sub>  
  JPMorgan Chase & Co. lifted their price objective on shares of Teva Pharmaceutical Industries from $40.00 to $50.00 and gave the stock an "overweight"...
- [Teva Pharmaceutical Industries Ltd. to Host R&D Day on November 11, 2026](https://www.quiverquant.com/news/Teva+Pharmaceutical+Industries+Ltd.+to+Host+R%26D+Day+on+November+11%2C+2026)  
  <sub>Quiver Quantitative, 17 hours ago</sub>  
  Teva Pharmaceutical Industries will host an R&D; Day on November 11, 2026, focusing on its pipeline.
- [ETFs Investing in Teva Pharmaceutical Industries Limited Stocks](https://www.tradingview.com/symbols/BMV-TEVA1/N/etfs/)  
  <sub>TradingView, 10 hours ago</sub>  
  Sorted by market value, the list below shows funds with Teva Pharmaceutical Industries Limited stocks. Equipped with price, change, and other helpful stats,...
- [JPMorgan raised target for Teva stock to USD 50.00](https://www.ad-hoc-news.de/boerse/news/corporate-news/jpmorgan-raised-target-for-teva-stock-to-usd-50-00/70311539)  
  <sub>ad-hoc-news.de, 7 hours ago</sub>  
  JPMorgan lifted its target from USD 40.00 to USD 50.00 on October 11, 2026. November 3, 2026 tests Teva stock.
- [FDA Approves Once-Monthly Olanzapine Injection for Adults with Schizophrenia](https://www.drugtopics.com/view/fda-approves-once-monthly-olanzapine-injection-for-adults-with-schizophrenia)  
  <sub>Drug Topics, 17 hours ago</sub>  
  Teva Pharmaceuticals' new olanzapine option is the first once-monthly subcutaneous injectable on the market for schizophrenia.
- [First Tracks climbs on ‘impressive’ celiac study data](https://www.biopharmadive.com/news/first-tracks-celiac-study-results-cd122/832726/)  
  <sub>BioPharma Dive, 17 hours ago</sub>  
  Initial study findings strengthened some analysts' belief that First Tracks' drug, one of a few in development aimed at the protein CD122,...
- [FDA Approves First Once-Monthly Subcutaneous Olanzapine LAI for Adults With Schizophrenia](https://www.pharmacytimes.com/view/fda-approves-first-once-monthly-subcutaneous-olanzapine-lai-for-adults-with-schizophrenia)  
  <sub>Pharmacy Times, 22 hours ago</sub>  
  The FDA approved olanzapine for extended-release injectable suspension (Weltruza; Teva Pharmaceuticals), the first once-monthly subcutaneous long-acting...
- [TEVA Maintained by JP Morgan -- Price Target Raised to $50.00](https://www.gurufocus.com/news/9119754/teva-maintained-by-jp-morgan-price-target-raised-to-5000)  
  <sub>GuruFocus, 19 hours ago</sub>  
  On October 1, 2023, JP Morgan maintained an Overweight rating for Teva Pharmaceutical Industries (TEVA). Analyst Chris Schott has raised the price target...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 41.28 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 39.63 (+4.2%), 50d 37.88 (+9.0%), 200d 34.01 (+21.4%); 50d above 200d
Momentum: RSI(14) 66.2 | MACD 0.845 vs signal 0.766 (histogram 0.079)
Returns: 1d +0.3% | 5d +5.5% | 1m +6.6% | 3m +30.8%
52-week range: 18.95 - 41.28 (now 100.0% of the way up)
Volatility: ATR(14) 1.19 (2.9% of price) | annualised 20d 29.2%
Volume: 0.20x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Healthcare / Drug Manufacturers - Specialty & Generic | market cap 48.15B
Valuation: trailing P/E 68.81 | forward P/E 13.35 | P/B 6.21 | PEG n/a
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
Price target: mean 47.17 (+14.2% vs last close), range 42.00 - 55.00
Recent rating changes:
  - 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - 2026-10-01 TD Cowen: init, ? -> Buy
  - 2026-09-23 Oppenheimer: init, ? -> Outperform
  - 2026-09-09 Leerink Partners: init, ? -> Outperform
  - 2026-09-04 UBS: main, Buy -> Buy
  - 2026-08-12 Barclays: main, Overweight -> Overweight
Institutional ownership: 24.5%
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

- [Fund Update: New $120.7M $XOM stock position opened by GATEWAY INVESTMENT ADVISERS LLC](https://www.quiverquant.com/news/Fund+Update%3A+New+%24120.7M+%24XOM+stock+position+opened+by+GATEWAY+INVESTMENT+ADVISERS+LLC)  
  <sub>Quiver Quantitative, 31 minutes ago</sub>  
  GATEWAY INVESTMENT ADVISERS LLC has opened a new $120.7M position in $XOM, per a new SEC 13F filing.
- [Why Are BATL, TPET, XOM, CVX, USO, UCO Stocks Rising Overnight?](https://stocktwits.com/news-articles/markets/equity/why-are-batl-tpet-xom-cvx-uso-uco-stocks-rising-overnight/cZZLqW1R7Mp)  
  <sub>Stocktwits, 9 hours ago</sub>  
  BATL, TPET, USO, UCO Stocks: Retail Sentiment. On Stocktwits, retail sentiment around BATL stock slipped from 'extremely bullish' to 'bullish' over 24 hours...
- [Will Elevated Crude Prices Enhance ExxonMobil's Cash Flows?](https://www.zacks.com/stock/news/3006177/will-elevated-crude-prices-enhance-exxonmobils-cash-flows)  
  <sub>Zacks Investment Research, 12 minutes ago</sub>  
  XOM stands to benefit from oil prices above $90 per barrel, with low-cost production in the Permian and Guyana supporting its earnings and cash flow...
- [A 1,500-share sale is planned by Xometry (XMTR) officer Sanjeev Singh Sahni.](https://www.stocktitan.net/sec-filings/XMTR/144-xometry-inc-sec-filing-8566efeba675.html)  
  <sub>Stock Titan, 2 hours ago</sub>  
  Xometry, Inc. (XMTR) is the issuer named in a Form 144 notice listing 1,500 shares of Class A common stock for sale by Officer Sanjeev Singh Sahni,...
- [ExxonMobil (NYSE:XOM) Shares Up 1.8% - What's Next?](https://www.marketbeat.com/instant-alerts/price-exxonmobil-nyse-xom-shares-up-18-whats-next-2026-10-12/)  
  <sub>MarketBeat, 17 hours ago</sub>  
  ExxonMobil (NYSE:XOM) Stock Jumps 1.8% - Should You Buy?
- [XOM Stock Gains 1.90% on Monday, Testing: Explained](https://journalarta.com/en/2026/10/13/xom-stock-gains-1-90-on-monday-testing-key-resistance/)  
  <sub>JournalArta, 6 hours ago</sub>  
  On October 12, 2026: price 172.15 USD, trend uptrend, RSI 69.3, support 158.30, resistance 172.15. technical analysis of xom stock. XOM Stock Gains — full…
- [Exxon, Oil Giants Top Buy Points After Deadly Saudi Airport Attacks](https://www.investors.com/news/oil-stocks-buy-points-chevron-exxon-oil-prices-rise-fang-trgp/)  
  <sub>Investor's Business Daily, 18 hours ago</sub>  
  Oil stocks popped near buy points with rising crude prices on Monday. Saudi airport attacks revived fears about supply risks due to global wars.
- [How Surging Guyana and Permian Output Will Impact ExxonMobil (XOM) Investors](https://finance.yahoo.com/energy/articles/surging-guyana-permian-output-impact-161112766.html)  
  <sub>Yahoo Finance, 23 hours ago</sub>  
  Recent reports highlight ExxonMobil Holdings' strong production growth from high-return assets in Guyana and the Permian Basin, with upstream volumes...
- [Two Utility Dividend Plays Are Quietly Beating XOM, CVX On Yield Amid Iran-Driven Oil Rally — Does Retail Know?](https://stocktwits.com/news-articles/markets/equity/two-utility-dividend-plays-are-quietly-beating-xom-cvx-on-yield-amid-iran-driven-oil-rally-does-retail-know/cZsMjYaRJHl)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Top energy stocks, top energy dividend stocks, top dividend stocks, Duke Energy, WEC Energy Group, Chevron, Exxon Mobil, ConocoPhillips, DUK stock,...
- [Exxon Mobil (XOM) Stock Price, Quote & News, NYSE](https://techgraph.co/stock-market/quote/xom/)  
  <sub>TechGraph, 23 hours ago</sub>  
  What is the 52-week range for XOM? The 52-week range for XOM is $110.39 to $176.41. Advertisement. Price quotes refresh periodically while this page...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 174.01 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 164.08 (+6.0%), 50d 162.28 (+7.2%), 200d 150.87 (+15.3%); 50d above 200d
Momentum: RSI(14) 71.5 | MACD 2.490 vs signal 1.466 (histogram 1.025)
Returns: 1d +1.1% | 5d +5.8% | 1m +5.4% | 3m +20.4%
52-week range: 110.64 - 174.01 (now 100.0% of the way up)
Volatility: ATR(14) 3.41 (2.0% of price) | annualised 20d 23.5%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

```text
Sector: Energy / Oil & Gas Integrated | market cap 715.49B
Valuation: trailing P/E 22.39 | forward P/E 15.18 | P/B 2.76 | PEG 1.38
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
Price target: mean 173.64 (-0.2% vs last close), range 142.00 - 200.00
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

### Europe (VGK) · Index fund — NEUTRAL, confidence 0.10

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst coverage thin (11.4% weight) with 65.7% buy rating and +15.7% price target
- CFTC speculators net long 0.1% and decreased 2.2% week over week
- Fund flows: share count down 4.2% (outflows) over the week
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.8; volume 0.13× 20‑day average

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 86.13 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 87.32 (-1.4%), 50d 89.90 (-4.2%), 200d 87.73 (-1.8%); 50d above 200d
Momentum: RSI(14) 38.8 | MACD -1.155 vs signal -1.120 (histogram -0.036)
Returns: 1d +0.4% | 5d -0.5% | 1m -3.5% | 3m -3.4%
52-week range: 77.90 - 93.19 (now 53.8% of the way up)
Volatility: ATR(14) 0.91 (1.1% of price) | annualised 20d 13.5%
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
Three-year record: +18.0% a year | beta to the market 0.90
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 11.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 65.7% | hold 34.3% | sell 0.0% (mean 2.11 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +15.7% above the current prices
Holdings read: ASML.AS, HSBA.L, ROP.SW, NOVN.SW, SHEL.L
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.15</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.15</summary>

```text
Contract: MSCI EAFE  - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 0.1% of open interest (493,234 contracts)
Change on the week: -2.2% of open interest
Crowding: 72% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.15</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -4.2% (-1.65B) over 7d
Shares outstanding: 432.95M | fund size: 37.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Farm goods basket (DBA) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance based on flat fund flows, mixed technicals, modest macro news impact, and stable fundamentals.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicating no net demand shift
- Technical indicators neutral: price above 20d, 50d, 200d SMAs but low volume and RSI 52.7
- USDA forecast larger corn production caused a brief price dip, but corn futures recouped, limiting impact
- Macro environment stable: yields modestly changed, dollar up 0.45% on week, VIX low at 15.21

<details><summary><b>News</b> — score +0.00</summary>

- [DBA: A Well-Rounded Commodity ETF, But With A K-1](https://seekingalpha.com/article/4953574-dba-a-well-rounded-commodity-etf-but-with-a-k-1)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Invesco DB Agriculture Fund ETF (DBA) offers diversified agricultural commodity exposure with an optimized roll yield. Since July 2020, DBA has delivered...
- [U.S. corn futures recoup slice of Friday's steep drop after USDA forecast larger crop](https://seekingalpha.com/news/4652289-us-corn-futures-recoup-slice-of-fridays-steep-drop-after-usda-forecast-larger-crop)  
  <sub>Seeking Alpha, 16 hours ago</sub>  
  US corn futures edged higher after the previous session's sharp decline in reaction to a surprise report from the USDA that forecast higher corn production...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 28.59 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 28.44 (+0.6%), 50d 28.45 (+0.5%), 200d 27.23 (+5.0%); 50d above 200d
Momentum: RSI(14) 52.7 | MACD -0.023 vs signal -0.027 (histogram 0.004)
Returns: 1d +0.5% | 5d -0.9% | 1m -1.3% | 3m +2.2%
52-week range: 25.44 - 29.49 (now 77.9% of the way up)
Volatility: ATR(14) 0.28 (1.0% of price) | annualised 20d 13.0%
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
Yield: 3.2%
Three-year record: +14.0% a year | beta to the market 0.35
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
Shares outstanding: 27.60M | fund size: 789.22M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Commodities basket (DBC) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Macro: inflation 3.4% and unemployment 4.2% in line with expectations
- Technical: price at 97.8% of 52‑week high, RSI 62.5, volume 0.09× 20‑day avg, no decisive break
- Fund flows: share count up 4.4% week‑over‑week indicating inflows
- Energy inventories: crude draw -3.2 MMbbl (bullish) vs natural gas build +85 Bcf (bearish)
- EIA outlook: WTI forecast down to $86 in six months (bearish for energy exposure)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 33.42 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 32.76 (+2.0%), 50d 31.70 (+5.4%), 200d 28.53 (+17.1%); 50d above 200d
Momentum: RSI(14) 62.5 | MACD 0.339 vs signal 0.343 (histogram -0.003)
Returns: 1d +0.3% | 5d +2.2% | 1m +0.8% | 3m +16.1%
52-week range: 22.10 - 33.68 (now 97.8% of the way up)
Volatility: ATR(14) 0.48 (1.4% of price) | annualised 20d 16.0%
Volume: 0.09x the 20-day average
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
Three-year record: +15.5% a year | beta to the market 1.05
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Natural gas: 3,500.0 billion cubic feet, +85.0 on the week (a build), 81% percentile over 52 weeks
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.40</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +4.4% (82.03M) over 7d
Shares outstanding: 57.95M | fund size: 1.94B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Developing country bonds (EMB) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish insider flow and technical trend offset by solid fundamentals and no macro surprise.

**Main reasons it gave:**
- Fund flows: -14.1% share count change (outflows) over 1 week
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 38.6 indicating modest bearish momentum
- Macro: no policy or data surprise; yields stable, upward‑sloping curve

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.30</summary>

```text
Last close 91.22 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 91.75 (-0.6%), 50d 93.47 (-2.4%), 200d 95.26 (-4.2%); 50d below 200d
Momentum: RSI(14) 38.6 | MACD -0.786 vs signal -0.869 (histogram 0.084)
Returns: 1d +0.2% | 5d +0.3% | 1m -2.1% | 3m -4.7%
52-week range: 90.14 - 97.74 (now 14.3% of the way up)
Volatility: ATR(14) 0.51 (0.6% of price) | annualised 20d 7.5%
Volume: 0.21x the 20-day average
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
Three-year record: +9.6% a year | beta to the market 1.10
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
Direction: money going out (1 week)
Share count change: 1 week: -14.1% (-2.12B) over 7d
Shares outstanding: 142.28M | fund size: 12.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US small companies (IWM) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: inflation 3.4% below Fed target, no rate hike
- Technical mix: price below 20d/50d/200d SMAs, RSI low (34.4) and MACD crossing bullish, low volume
- Analyst view bullish (+9.7% price target) but only covers 2% of fund (thin coverage)
- Positioning shows net short 24.8% and short increase (+2% OI), crowded short (8% percentile)

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Russell 2000 ETF (IWM) Stock Price | Quotes & News](https://www.moomoo.com/stock/IWM-US?chain_id=Name1K9-3FXPhg.1lcqpjg&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FGM-US%2Fcommunity%22%7D)  
  <sub>Moomoo, 15 hours ago</sub>  
  Track the latest iShares Russell 2000 ETF (IWM) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF trading and...
- [Should iShares U.S. Small-Cap Equity Factor ETF (SMLF) Be on Your Investing Radar?](https://finance.yahoo.com/markets/stocks/articles/ishares-u-small-cap-equity-092002134.html)  
  <sub>Yahoo Finance, 5 hours ago</sub>  
  The iShares U.S. Small-Cap Equity Factor ETF (SMLF) was launched on April 28, 2015, and is a passively managed exchange traded fund designed to offer broad...
- [AI Can Help Small-Caps Beat Megacap Tech Rivals. That Gives This ETF 20% Upside.](https://www.barrons.com/articles/ai-russell-2000-etf-small-caps-megacap-tech-ba90f46e)  
  <sub>Barron's, 20 hours ago</sub>  
  With lean teams, many small-caps can adopt AI tools quickly, automate workflows, and expand capacity without proportionally growing head count.
- [DFSV: A 'New' Yet Already Proven Value Fund (NYSEARCA:DFSV)](https://seekingalpha.com/article/4953632-dfsv-a-new-yet-already-proven-value-fund)  
  <sub>Seeking Alpha, 5 hours ago</sub>  
  DFA US Small Cap Value ETF earns a "Buy" rating for its diversified, value-and-profitability strategy, and outperformance. Learn more on DFSV here.
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [Nasdaq 100 Drops, SanDisk Tumbles 6% as AI Trade Falters: Stock Market Today](https://www.tradingview.com/news/benzinga:655132fc6094b:0-nasdaq-100-drops-sandisk-tumbles-6-as-ai-trade-falters-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were mixed at midday Monday as a selloff in AI-infrastructure names dragged the Nasdaq 100 and small caps lower, while the Dow edged higher and...
- [Most of the stock market has been in a bear mar...](https://pluang.com/en/news-feed/beta-negatif-dan-pasar-beruang-tersembunyi)  
  <sub>Pluang, 23 hours ago</sub>  
  Since May, most stocks in the market have been in a bear market, with 60% of S&P 500 stocks down over 20% and 87% down at least 10%, even as the S&P 500...
- [Small-Cap Stocks Are in Grave Danger Thanks to an Impending Debt Cliff. Use These 2 ETFs for Protection and Profit.](https://finance.yahoo.com/markets/stocks/articles/small-cap-stocks-grave-danger-163029015.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Small-cap stocks are telling a dangerous story. www.barchart.com. The story is one of persistent selling pressure. And with the iShares Russell 2000 ETF...
- [ValuEngine Weekly Commentary With Strategy Notes](https://seekingalpha.com/article/4953759-valuengine-weekly-commentary-strategy-notes)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  U.S. equity markets were mixed this week, with broader gains across value, defensive, and cyclical sectors offset by weakness in technology and the NASDAQ...
- [September CPI Preview: The Print That Could Break the Fed's Pause](https://www.moomoo.com/community/feed/september-cpi-preview-the-print-that-could-break-the-fed-117433024380934)  
  <sub>Moomoo, 5 hours ago</sub>  
  September CPI lands Wednesday, October 14 at 8:30 a.m. ET — the first inflation read after Kevin Warsh's Fed pulled the trigger on its first hike sinc...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 276.33 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 281.12 (-1.7%), 50d 290.72 (-4.9%), 200d 277.31 (-0.4%); 50d above 200d
Momentum: RSI(14) 34.4 | MACD -3.481 vs signal -3.545 (histogram 0.065)
Returns: 1d -0.6% | 5d -1.8% | 1m -4.0% | 3m -6.6%
52-week range: 229.11 - 305.09 (now 62.1% of the way up)
Volatility: ATR(14) 3.40 (1.2% of price) | annualised 20d 11.1%
Volume: 0.36x the 20-day average
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
Three-year record: +18.3% a year | beta to the market 1.27
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 2.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.7% above the current prices
Holdings read: XTSLA, TWST, MOG-A, FROG, TXG
Recent rating changes among them:
  - TWST: 2026-10-12 Canaccord Genuity: main, Buy -> Buy
  - MOG-A: 2026-10-09 TD Cowen: main, Buy -> Buy
  - FROG: 2026-09-04 DA Davidson: main, Buy -> Buy
  - TXG: 2026-10-12 Canaccord Genuity: main, Buy -> Buy
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: RUSSELL E-MINI - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 24.8% of open interest (425,152 contracts)
Change on the week: +2.0% of open interest
Crowding: 8% percentile over 52 weeks -- a crowded short by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 281.05M | fund size: 77.66B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, safer (LQD) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break on heavy volume, and while large outflows signal negative sentiment, they do not constitute a material macro catalyst. Technicals remain in a downtrend but lack a clear breakout, and yields have moved only modestly.

**Main reasons it gave:**
- US Treasury yields unchanged to slightly lower this week (10‑yr down 5 bps), no rate surprise
- Technical indicators show price below 20‑day, 50‑day, and 200‑day SMAs, but no decisive break on heavy volume
- Weekly outflow of -12.3% (≈$3.96 B) indicates negative sentiment but not a macro catalyst
- Yield curve remains upward sloping (+1.16), indicating normal market conditions

<details><summary><b>News</b> — score +0.00</summary>

- [Silent SPY, Simmering Credit, and a 3-Sigma NVDA Put/Call Shift | Options Market Statistics](https://www.moomoo.com/community/feed/silent-spy-simmering-credit-and-a-3-sigma-nvda-put-117433216204806)  
  <sub>Moomoo, 4 hours ago</sub>  
  By Luke Wu | Oct 13, 2026 Key Takeaways - Credit Simmering Again: 600K Call Strip Bets a Volatile Move in LQD This Week Noted yesterday both $Ishares ...
- [BlackRock Says the Market Has the Fed Wrong. It’s Buying Treasuries With Yields Above 5%](https://247wallst.com/investing/2026/10/13/blackrock-says-the-market-has-the-fed-wrong-its-buying-treasuries-with-yields-above-5/)  
  <sub>24/7 Wall St., 23 minutes ago</sub>  
  BlackRock just made its most aggressive shift in bond strategy since 2020, pulling money out of stocks to do it, but the real question is whether the Fed...
- [SPLB: IG Bond ETF With Less Bank Risk, But More Rate Risk (NYSEARCA:SPLB)](https://seekingalpha.com/article/4953578-splb-ig-bond-etf-with-less-bank-risk-but-more-rate-risk)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  SPLB ETF review: low-cost long-term corporate bond exposure with 5.91% yield, but high rate risk (11.9 duration).
- [CORP: Well-Rounded ETF In Corporate Bonds, But Not Low-Cost](https://seekingalpha.com/article/4948656-corp-well-rounded-etf-in-corporate-bonds-but-not-low-cost)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  The PIMCO Investment Grade Corporate Bond Index ETF offers broad exposure to USD-denominated investment-grade corporate bonds with a 5.43% SEC yield and...
- [IG: Your Guide To The Principal Investment Grade Corporate ETF](https://seekingalpha.com/article/4953281-ig-guide-to-the-principal-investment-grade-corporate-etf)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Review Principal's IG corporate bond ETF: active duration tweaks, BBB-heavy portfolio, yield vs 7-year Treasuries, returns, and best tax placement—read now.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 102.56 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 103.09 (-0.5%), 50d 104.75 (-2.1%), 200d 108.13 (-5.2%); 50d below 200d
Momentum: RSI(14) 36.9 | MACD -0.758 vs signal -0.851 (histogram 0.093)
Returns: 1d -0.0% | 5d +0.4% | 1m -1.7% | 3m -4.7%
52-week range: 101.83 - 112.92 (now 6.6% of the way up)
Volatility: ATR(14) 0.57 (0.6% of price) | annualised 20d 6.7%
Volume: 0.21x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.50</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.50</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -12.3% (-3.96B) over 7d
Shares outstanding: 276.27M | fund size: 28.33B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### S&P 500, equal weight (RSP) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, no decisive technical break, and mixed modest signals across analyst, insider, and fundamentals lead to a neutral stance.

**Main reasons it gave:**
- Analyst coverage thin (1.4% weight) with 78.5% buy rating but price target 16% below current price
- Large speculators net short 21.5% of open interest; short positions fell 1.8% of open interest this week
- Fund outflows of 6.3% of shares in the past week
- Technical indicators: price above 200‑day SMA, MACD histogram positive, but volume at 0.44× 20‑day average
- Macro: yields stable, VIX low (15.2), normal upward‑sloping yield curve

<details><summary><b>News</b> — score +0.00</summary>

- [Moomoo Singapore, a wealth-tech platform building an intelligent investing ecosystem, today shared that more than 7,000 subscriptions were received through its exclusive pre-listing offer for four Xtrackers UCITS ETFs that began trading on SGX today.](https://www.moomoo.com/sg/newsroom/moomoo-singapore-xtrackers-ucits-etf-investor-engagement)  
  <sub>Moomoo, 6 hours ago</sub>  
  Moomoo Singapore, a wealth-tech platform building an intelligent investing ecosystem, today shared that more than 7000 subscriptions were received through...
- [Keeping It Simple Has Paid Off In 2026 - And That Should Continue](https://seekingalpha.com/article/4953596-keeping-it-simple-has-paid-off-in-2026-and-that-should-continue)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  The S&P 500 has delivered double-digit returns through the first three quarters of 2026. Large-cap US stocks, as measured by the S&P 500, have outperformed...
- [The AI Rally, Mega-Cap Dominance & What Comes Next](https://www.zacks.com/stock/news/3005460/the-ai-rally-mega-cap-dominance-what-comes-next)  
  <sub>Zacks Investment Research, 19 hours ago</sub>  
  In this episode of ETF Spotlight, I speak with Christopher Dahlin, Invesco's Senior Factor & Core Equity Strategist, about the AI trade, equal-weighted...
- [Oil is Up Again But Inflation Bets Won't Follow. That's a Red Flag.](https://www.tastylive.com/news-insights/oil-is-up-again-but-inflation-bets-won-t-follow-that-s-a-red-flag)  
  <sub>tastylive, 9 hours ago</sub>  
  Crude oil is up again, but market inflation expectations have stopped tracking it. The last time that happened, a growth scare followed.
- [Invesco S&P 500 Top 50 ETF (XLG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLG/)  
  <sub>Yahoo! Finance Canada, 22 hours ago</sub>  
  Find the latest Invesco S&P 500 Top 50 ETF (XLG) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [S&P 500—What Happens In Q4 After A Negative September?](https://www.benzinga.com/Opinion/26/10/62301581/sp500-what-happens-in-q4-after-a-negative-september)  
  <sub>Benzinga, 24 hours ago</sub>  
  The final four months of the year are a particularly interesting period for stock markets, often associated with recognizable seasonal patterns.
- [Chip Weakness Hits Nasdaq Futures; Dow, Russell Solid](https://www.moomoo.com/community/feed/chip-weakness-hits-nasdaq-futures-dow-russell-solid-117433508167686?chain_id=Name1K9-3FXPhg.1lcs7a0&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A107%2C%22f%22%3A%22www.moomoo.com%2Fetfs%2F02840-HK%22%7D)  
  <sub>Moomoo, 3 hours ago</sub>  
  Tap the related stocks on the image above to add them to your Watchlist. Market Overview $E-mini S&P 500 Futures (DEC6) (ESmain.US)$ -0.10% to 7850.25...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 212.44 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 211.33 (+0.5%), 50d 216.17 (-1.7%), 200d 206.42 (+2.9%); 50d above 200d
Momentum: RSI(14) 48.7 | MACD -0.896 vs signal -1.452 (histogram 0.556)
Returns: 1d -0.4% | 5d +0.1% | 1m -1.2% | 3m -0.2%
52-week range: 182.18 - 222.77 (now 74.6% of the way up)
Volatility: ATR(14) 1.81 (0.9% of price) | annualised 20d 8.5%
Volume: 0.44x the 20-day average
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
Three-year record: +16.6% a year | beta to the market 0.84
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

<details><summary><b>What analysts and big funds say</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score -0.10</summary>

```text
Rolled up from the 5 largest holdings, 1.4% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 78.5% | hold 21.5% | sell 0.0% (mean 2.21 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -16.0% above the current prices
Holdings read: MRNA, P, ILMN, CRWD, RVTY
Recent rating changes among them:
  - MRNA: 2026-10-07 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - P: 2026-10-12 Guggenheim: main, Buy -> Buy
  - ILMN: 2026-10-07 Barclays: main, Underweight -> Underweight
  - CRWD: 2026-10-09 Needham: main, Buy -> Buy
  - RVTY: 2026-10-07 Barclays: main, Equal-Weight -> Equal-Weight
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: E-MINI S&P 500 - CHICAGO MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 21.5% of open interest (1,932,227 contracts)
Change on the week: -1.8% of open interest
Crowding: 27% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -6.3% (-6.40B) over 7d
Shares outstanding: 450.90M | fund size: 95.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 1-3 years (SHY) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, mixed positioning, modest inflows, and no decisive technical break.

**Main reasons it gave:**
- Positioning: large speculators net short 28% of open interest, down 2.3% week‑over‑week (crowded long 97th percentile) – mixed signal
- Fund flows: share count up 1.2% over the week, indicating modest inflows
- Macro: Treasury yields stable (10‑yr down 5 bps, 3‑mo up 3 bps) with no policy surprise
- Technical: price near 20‑day SMA, RSI 42, MACD just above signal – no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

- [BlackRock Says the Market Has the Fed Wrong. It’s Buying Treasuries With Yields Above 5%](https://247wallst.com/investing/2026/10/13/blackrock-says-the-market-has-the-fed-wrong-its-buying-treasuries-with-yields-above-5/)  
  <sub>24/7 Wall St., 21 minutes ago</sub>  
  BlackRock just made its most aggressive shift in bond strategy since 2020, pulling money out of stocks to do it, but the real question is whether the Fed...
- [ETF Inflows Top $41B as Investors Pile Into Brazil, Long Bonds](https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds)  
  <sub>ETF.com, 22 hours ago</sub>  
  Year-to-date inflows are just shy of $1.6 trillion, on pace for $2 trillion by the end of the year.
- [BlackRock upgrades Treasurys, downgrades equities (TLT:NASDAQ)](https://seekingalpha.com/news/4652452-blackrock-upgrades-treasurys-downgrades-equities)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  BlackRock Investment Institute this week upgraded U.S. Treasuries and cut U.S. equities to neutral, ending a six-year underweight stance on government debt...
- [Stocktwits Weekly Spread: What Shaped Treasury Yields And The Dollar This Week](https://stocktwits.com/news-articles/markets/equity/stocktwits-weekly-spread-what-shaped-treasury-yields-and-the-dollar-this-week/cZxTXunRBnZ)  
  <sub>Stocktwits, 19 hours ago</sub>  
  U.S. fixed-income and currency markets saw heightened volatility during the week ending Oct. 9, 2026, as a sustained surge in global crude oil prices...
- [BofA Survey: Bond yield chaos is still the largest market tail risk](https://seekingalpha.com/news/4652460-bofa-survey-bond-yield-chaos-is-still-the-largest-market-tail-risk)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  BofA fund manager survey: Disorderly bond yield spike tops Q4 tail risks, ahead of AI bubble and inflation. Learn more here.
- [Chip Selloff Knocks Vanguard's All-World ETF Off Its Record Perch](https://www.ad-hoc-news.de/boerse/news/unternehmensnachrichten/chip-selloff-knocks-vanguard-s-all-world-etf-off-its-record-perch/70314741)  
  <sub>ad-hoc-news.de, 2 hours ago</sub>  
  Vanguard FTSE All-World ETF fell 0.4% to EUR 173.00 as AI spending doubts hit chip stocks; Chinese DRAM news and Broadcom's warning weighed.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 81.18 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 81.18 (+0.0%), 50d 81.56 (-0.5%), 200d 82.20 (-1.2%); 50d below 200d
Momentum: RSI(14) 42.2 | MACD -0.108 vs signal -0.139 (histogram 0.031)
Returns: 1d +0.0% | 5d +0.1% | 1m -0.2% | 3m -1.0%
52-week range: 81.05 - 83.18 (now 6.3% of the way up)
Volatility: ATR(14) 0.10 (0.1% of price) | annualised 20d 1.6%
Volume: 0.10x the 20-day average
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

<details><summary><b>Buying and selling by company insiders</b> — score -0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score -0.10</summary>

```text
Contract: UST 2Y NOTE - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 28.0% of open interest (4,485,811 contracts)
Change on the week: -2.3% of open interest
Crowding: 97% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score -0.10</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +1.2% (323.11M) over 7d
Shares outstanding: 323.81M | fund size: 26.29B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 20+ years (TLT) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; modest bearish sentiment from speculator net short, but strong fundamentals and no clear macro surprise.

**Main reasons it gave:**
- Net short position of 30.2% of open interest with 85th percentile crowding, indicating modest bearish sentiment among large speculators
- Fund basics show high credit quality (AA) and 5.0% yield, supporting a neutral to slightly bullish view on fundamentals
- Yields fell slightly this week and inflation data was in line with expectations, providing no material macro surprise
- Technical indicators show price near 52‑week low with low volume and no decisive breakout

<details><summary><b>News</b> — score +0.00</summary>

- [BlackRock Says the Market Has the Fed Wrong. It’s Buying Treasuries With Yields Above 5%](https://247wallst.com/investing/2026/10/13/blackrock-says-the-market-has-the-fed-wrong-its-buying-treasuries-with-yields-above-5/)  
  <sub>24/7 Wall St., 23 minutes ago</sub>  
  BlackRock just made its most aggressive shift in bond strategy since 2020, pulling money out of stocks to do it, but the real question is whether the Fed...
- [TLT’s Yield Edge Is Thin Over SGOV (NASDAQ:TLT)](https://seekingalpha.com/article/4953642-tlts-yield-edge-is-thin-over-sgov)  
  <sub>Seeking Alpha, 9 hours ago</sub>  
  iShares 0-3 Month Treasury Bond ETF is a buy for cash needed within 12 months, and iShares 20+ Year Treasury Bond ETF is a hold. Read my analysis on TLT and...
- [Time for Inverse Bond ETFs as IMF Warns of Bond Market Risks?](https://www.tradingview.com/news/zacks:1a294b8a1094b:0-time-for-inverse-bond-etfs-as-imf-warns-of-bond-market-risks/)  
  <sub>TradingView, 3 hours ago</sub>  
  The International Monetary Fund (IMF) has warned that government bond yields could spike sharply and disorderly as rising inflation, mounting public debt...
- [SGOV ETF rated Buy for short-term cash needs; T...](https://pluang.com/en/news-feed/keunggulan-yield-tlt-terhadap-sgov-tipis)  
  <sub>Pluang, 9 hours ago</sub>  
  Benjamin C. Barry recommends buying the SGOV ETF for cash needed within 12 months due to its nearly 4% yield and low price volatility, making it suitable...
- [Too Many Investors Don’t Understand How Bonds Work](https://finance.yahoo.com/markets/options/articles/too-many-investors-don-t-164836884.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  If you are now under age 70, you probably were not paying that much attention to your portfolio the last time bonds mattered 15-20 years ago.
- [Fed's Waller Says Higher Treasury Yields Are 'Doing A Little Bit Of The Work' Of Tighter Monetary Policy](https://www.tradingview.com/news/stocktwits:3ca21d8a0094b:0-fed-s-waller-says-higher-treasury-yields-are-doing-a-little-bit-of-the-work-of-tighter-monetary-policy/)  
  <sub>TradingView, 4 hours ago</sub>  
  Federal Reserve Governor Christopher Waller said Tuesday that rising long-term U.S. Treasury yields are affecting interest-sensitive sectors such as housing...
- [S&P 500, Nasdaq Futures Pull Back After Trump Wants 'Couple Days To Think' About Iran Ceasefire Deal: ASTS, DELL, BB, SMCI In Focus](https://stocktwits.com/news-articles/markets/equity/sp500-nasdaq-futures-pull-back-after-trump-wants-couple-days-to-think-about-iran-ceasefire-deal/cZgS7tGRet0)  
  <sub>Stocktwits, 16 hours ago</sub>  
  According to a report from Axios, the U.S. and Iran have reached a tentative deal to extend the ceasefire between the two nations by 60 days and are on...
- [S&P 500, Nasdaq, Dow Futures Ease As Oil Rally Tempers AI Optimism Ahead of Big Tech Earnings: SMCI, OKLO, XE, SKHY, GOOG In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-dow-futures-ease-as-oil-rally-tempers-ai-optimism-ahead-of-big-tech-earnings-smci-oklo-xe-skhy-goog-in-focus/cZZmby1R7wd)  
  <sub>Stocktwits, 18 hours ago</sub>  
  U.S. futures declined amid rising oil prices as the conflict in the Middle East intensifies ahead of the peak earnings season.
- [Dow, S&P 500 Futures Edge Higher As Record Bank Earnings, Cooling Inflation Lift Risk Appetite: ASTS, ATAI, AAPL, PYPL in Focus](https://stocktwits.com/news-articles/markets/equity/dow-s-and-p-500-futures-edge-higher-as-record-bank-earnings-cooling-inflation-lift-risk-appetite-asts-atai-aapl-pypl-in-focus/cZZ3MwDR7rl)  
  <sub>Stocktwits, 22 hours ago</sub>  
  June's Producer Price Index (PPI) declined 0.3% from the previous month, marking its steepest drop in more than a year.
- [Nasdaq, S&P 500, Dow Futures Shake Off Iran Jitters As Investors Turn To AI Hyperscaler Earnings: INTC, TSLA, TTD, HIMS In Focus](https://stocktwits.com/news-articles/markets/equity/nasdaq-s-and-p-500-dow-futures-shake-off-iran-jitters-as-investors-turn-to-ai-hyperscaler-earnings-intc-tsla-ttd-hims-in-focus/cZZYW1bR7UM)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Markets were primarily focused on earnings from major companies, alongside rising oil prices due to the continued tensions between the U.S. and Iran.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 78.38 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 79.02 (-0.8%), 50d 80.92 (-3.1%), 200d 85.07 (-7.9%); 50d below 200d
Momentum: RSI(14) 39.9 | MACD -1.016 vs signal -1.098 (histogram 0.082)
Returns: 1d +0.4% | 5d +1.4% | 1m -3.2% | 3m -7.0%
52-week range: 77.11 - 92.06 (now 8.5% of the way up)
Volatility: ATR(14) 0.73 (0.9% of price) | annualised 20d 10.8%
Volume: 0.19x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Long Government
Yield: 5.0%
Credit quality: AA 100.0% | US government debt 99.6%
Three-year record: +0.7% a year | beta to the market 2.31
Cost and size: expense ratio 0.15% | net assets 46.23B
What it is made of: Bonds 99.6%, Cash 0.4%
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
Shares outstanding: 109.70M | fund size: 8.60B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Emerging markets (VWO) · Index fund — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “Neutral”, so the main reasons below are all it gave.

**Main reasons it gave:**
- No macro surprise: yields stable, no policy shift, VIX low
- Technicals: price near 52‑week high, RSI 47.7, MACD slightly negative, low volume, no decisive break
- Analyst view thin: only 22.2% coverage of fund, despite 100% buy rating and +40% price target
- Positioning: net long 4.3% of open interest, weekly increase +1.2%, crowding at 60th percentile
- Fundamentals: moderate valuation (P/E 15.9), 2% yield, stable performance, no major change

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.67 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 59.90 (-0.4%), 50d 60.18 (-0.8%), 200d 58.18 (+2.6%); 50d above 200d
Momentum: RSI(14) 47.7 | MACD -0.121 vs signal -0.097 (histogram -0.024)
Returns: 1d -0.1% | 5d -1.6% | 1m +0.1% | 3m +0.3%
52-week range: 52.42 - 61.44 (now 80.4% of the way up)
Volatility: ATR(14) 0.62 (1.0% of price) | annualised 20d 15.2%
Volume: 0.22x the 20-day average
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
Three-year record: +18.7% a year | beta to the market 0.75
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

<details><summary><b>What analysts and big funds say</b> — score +0.25</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.25</summary>

```text
Rolled up from the 5 largest holdings, 22.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.33 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.0% above the current prices
Holdings read: 2330.TW, 0700.HK, 9988.HK, 2454.TW, 2308.TW
Recent rating changes among them: none reported
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.10</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.10</summary>

```text
Contract: MSCI EM INDEX - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 4.3% of open interest (1,059,025 contracts)
Change on the week: +1.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.10</summary>

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 1.42B | fund size: 84.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US company bonds, riskier (HYG) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [HYG Handed a $300,000 Holder $18,255 of Taxable Income and $5,550 of Actual Gain](https://247wallst.com/investing/etf/2026/10/12/hyg-handed-a-300000-holder-18255-of-taxable-income-and-5550-of-actual-gain/)  
  <sub>24/7 Wall St., 14 hours ago</sub>  
  Holding a high-yield bond ETF in a taxable account can leave you owing the IRS far more than you actually earned, and most investors never notice until they...
- [High-yield bond ETF HYG can trigger tax bills f...](https://pluang.com/en/news-feed/etf-hyg-pajak-dan-keuntungan-aktual-pemegang-300000-dolar)  
  <sub>Pluang, 13 hours ago</sub>  
  A $300000 investment in the iShares iBoxx $ High Yield Corporate Bond ETF (HYG) generated $18255 in taxable interest income over 12 months, but the total...
- [SCYB: Rising Credit Spreads Provide An Opportunity As Yield Approaches 8% (NYSEARCA:SCYB)](https://seekingalpha.com/article/4953563-scyb-rising-credit-spreads-provide-an-opportunity-as-yield-approaches-8-percent)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Schwab High Yield Bond ETF: ~8% yield-to-maturity, 0.03% fee edge, and today's spread-driven opportunity. Learn more about the SCYB ETF here.
- [HYG and JNK shift to top ETF quartile, Craig Shapiro notes](https://tradersunion.com/news/market-voices/show/3774758-hyg-jnk-etf-movement/)  
  <sub>Traders Union, 22 hours ago</sub>  
  Craig Shapiro reports HYG and JNK rising from bottom to top quartile among ETFs, with metals higher and PFIX up intraday.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 77.07 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 77.65 (-0.7%), 50d 78.70 (-2.1%), 200d 79.77 (-3.4%); 50d below 200d
Momentum: RSI(14) 30.0 | MACD -0.481 vs signal -0.506 (histogram 0.025)
Returns: 1d -0.3% | 5d -0.3% | 1m -1.9% | 3m -3.4%
52-week range: 76.90 - 81.28 (now 4.0% of the way up)
Volatility: ATR(14) 0.30 (0.4% of price) | annualised 20d 4.3%
Volume: 0.29x the 20-day average
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
Three-year record: +8.0% a year | beta to the market 0.70
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
Direction: money coming in (1 week)
Share count change: 1 week: +3.5% (560.51M) over 7d
Shares outstanding: 217.82M | fund size: 16.79B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US government bonds, 7-10 years (IEF) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [BofA Survey: Bond yield chaos is still the largest market tail risk](https://seekingalpha.com/news/4652460-bofa-survey-bond-yield-chaos-is-still-the-largest-market-tail-risk)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  BofA fund manager survey: Disorderly bond yield spike tops Q4 tail risks, ahead of AI bubble and inflation. Learn more here.
- [Stocks Have Ignored 5% Treasury Yields — JPMorgan Strategist Says AI May Be Changing The Rules](https://stocktwits.com/news-articles/markets/equity/stocks-5-treasury-yields-ignored-jpmorgan-ai-changing-rules/cZxd5aRRBFd)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The 10-year Treasury yield briefly touched 5.36% earlier this week, its highest level since 2002, after rising 112 basis points since the end of 2025.
- [Fed's Waller Says Higher Treasury Yields Are 'Doing A Little Bit Of The Work' Of Tighter Monetary Policy](https://finance.yahoo.com/economy/policy/articles/feds-waller-says-higher-treasury-103559245.html)  
  <sub>Yahoo Finance, 4 hours ago</sub>  
  Government bond yields across the U.S. and other advanced economies have climbed to multidecade highs, with investors awaiting key U.S. inflation data.
- [BofA's Brian Moynihan Expects Fed To Hike Rates Three Times In 2026, Sees Inflation In 'Mid-2s' By End Of 2027](https://stocktwits.com/news-articles/markets/equity/bofa-brian-moynihan-expects-three-rate-hikes-in-2026-inflation-mid-2s-2027/cZo4ULBRJea)  
  <sub>Stocktwits, 17 hours ago</sub>  
  During an interview with CNBC, Moynihan said inflation had been easing before picking up again due to the effects of tariffs and the war on prices,...
- [Iran war has cost average U.S. household $2K, economist estimates (USO:NYSEARCA)](https://seekingalpha.com/news/4652203-iran-war-costing-average-us-household-2k-economist-estimates)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Iran war fallout is costing the average U.S. household nearly $2K, driven by higher energy prices, rising interest rates and military spending.
- [Treasury yields retreat amid IMF's 'severe impact' warning](https://invezz.com/au/news/2026/10/13/treasury-yields-retreat-amid-imfs-severe-impact-warning/)  
  <sub>Invezz, 3 hours ago</sub>  
  US Treasury yields fell on Tuesday as oil prices retreated from recent highs, offering some relief to the bond market after trading resumed following...
- [Why Robert E Hall, Michael Woodford won 2026 Nobel prize in economics?](https://invezz.com/sg/news/2026/10/12/why-robert-e-hall-michael-woodford-won-2026-nobel-prize-in-economics/)  
  <sub>Invezz, 24 hours ago</sub>  
  Robert E. Hall and Michael Woodford were awarded the 2026 Nobel Prize in Economics on Monday for their work that helps smooth out the economy's peaks and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.54 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 89.83 (-0.3%), 50d 91.49 (-2.1%), 200d 94.23 (-5.0%); 50d below 200d
Momentum: RSI(14) 37.7 | MACD -0.648 vs signal -0.745 (histogram 0.098)
Returns: 1d +0.1% | 5d +0.5% | 1m -1.5% | 3m -4.5%
52-week range: 88.92 - 97.99 (now 6.9% of the way up)
Volatility: ATR(14) 0.44 (0.5% of price) | annualised 20d 6.1%
Volume: 0.21x the 20-day average
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
Three-year record: +3.1% a year | beta to the market 1.16
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
Direction: money going out (1 week)
Share count change: 1 week: -1.0% (-421.19M) over 7d
Shares outstanding: 465.13M | fund size: 41.65B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US inflation-linked bonds (TIP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [Is the TIPS Bond ETF Warning Bitcoin Again? A Leading Indicator to Watch](https://www.bitget.com/amp/news/detail/12560605949337)  
  <sub>Bitget, 9 hours ago</sub>  
  Key Highlights Bitcoin trades at $83693 (-0.30% 24h) as the iShares TIPS Bond ETF turns sharply lower — a pattern Alphractal flags | Bitget crypto news!
- [The Five Largest Holdings in the RANK ETF After Its Latest Rebalance](https://www.tipranks.com/news/the-five-largest-holdings-in-the-rank-etf-after-its-latest-rebalance)  
  <sub>TipRanks, 4 hours ago</sub>  
  The Defiance KSM TipRanks Analyst ETF ($RANK) has completed its latest quarterly reconstitution and rebalance, which took effect after the close on...
- [SGX deepens global access with Xtrackers UCITS ETF listings](https://www.tipranks.com/news/company-announcements/sgx-deepens-global-access-with-xtrackers-ucits-etf-listings)  
  <sub>TipRanks, 10 hours ago</sub>  
  An update from Singapore Exchange ( ($SG:S68) ) is now available. Singapore Exchange's SGX Stock Exchange has strengthened its position as a gateway to...
- [3 Best ETFs to Bank on for an 11% Gain, According to AI Analyst](https://www.tipranks.com/news/3-best-etfs-to-bank-on-for-11-gain-according-to-ai-analyst)  
  <sub>TipRanks, 18 hours ago</sub>  
  Exchange-traded funds (ETFs) give investors a convenient way to follow the growth potential of major U.S. corporations. TipRanks' AI analyst flagged three...
- [Euro ETF Hit by $10 Million Exit as Traders Cool on Common Currency](https://www.tipranks.com/news/cryptocurrencies/euro-etf-hit-by-10-million-exit-as-traders-cool-on-common-currency)  
  <sub>TipRanks, 18 hours ago</sub>  
  Euro ETF sheds cash as traders rethink currency bets Invesco CurrencyShares Euro Trust's FXE recorded a sharp outflow of $10.34 million on October 06, 2026,...
- [Ethereum ETF Sees Fresh Inflows as Fidelity’s FETH Rides 40% Ether Rally](https://www.tipranks.com/news/cryptocurrencies/ethereum-etf-sees-fresh-inflows-as-fidelitys-feth-rides-40-ether-rally)  
  <sub>TipRanks, 15 hours ago</sub>  
  Ethereum ETF pulls in fresh capital as crypto rally resumes. The Fidelity Ethereum Fund ETF, FETH, logged net inflows of $5502988 on October 09, 2026,...
- [Why Is Invesco QQQ Trust ETF (QQQ) Down Today, Oct. 12?](https://www.tipranks.com/news/why-is-invesco-qqq-trust-etf-qqq-down-today-oct-12)  
  <sub>TipRanks, 19 hours ago</sub>  
  The Invesco QQQ Trust ETF ($QQQ), which tracks the performance of the Nasdaq-100 Index (NDX), was down 0.76% as of the time of writing on Monday.
- [Bitcoin’s Price Faces Hurdles on Path to $200,000 as BTC ETF Outflows Hit $681 Million](https://www.tipranks.com/news/bitcoins-price-faces-hurdles-on-path-to-200000-as-btc-etf-outflows-top-680-million)  
  <sub>TipRanks, 23 hours ago</sub>  
  Bitcoin's price (BTC-USD) traded near $82825 on Monday, October 12, as investor Simon Dixon debated whether the digital asset can reach $200000 before its...
- [3 Best Vanguard ETFs for Dividend Income and Growth Potential](https://www.tipranks.com/news/3-best-vanguard-etfs-for-dividend-income-and-growth-potential)  
  <sub>TipRanks, 23 hours ago</sub>  
  Dividend stocks can provide a steady stream of income while also offering the potential for long-term growth. Vanguard has several low-cost ETFs that make...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 104.56 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 104.61 (-0.1%), 50d 106.00 (-1.4%), 200d 109.13 (-4.2%); 50d below 200d
Momentum: RSI(14) 41.1 | MACD -0.504 vs signal -0.617 (histogram 0.114)
Returns: 1d +0.1% | 5d +0.4% | 1m -1.2% | 3m -3.3%
52-week range: 103.98 - 112.20 (now 7.0% of the way up)
Volatility: ATR(14) 0.36 (0.3% of price) | annualised 20d 4.8%
Volume: 0.17x the 20-day average
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
Three-year record: +3.8% a year | beta to the market 0.71
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
Direction: money going out (1 week)
Share count change: 1 week: -5.5% (-825.05M) over 7d
Shares outstanding: 136.41M | fund size: 14.26B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US dollar (UUP) · Index fund — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 29.05 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 28.76 (+1.0%), 50d 28.35 (+2.5%), 200d 27.81 (+4.5%); 50d above 200d
Momentum: RSI(14) 67.6 | MACD 0.216 vs signal 0.198 (histogram 0.018)
Returns: 1d -0.3% | 5d +0.5% | 1m +3.1% | 3m +2.8%
52-week range: 26.47 - 29.13 (now 97.0% of the way up)
Volatility: ATR(14) 0.12 (0.4% of price) | annualised 20d 5.0%
Volume: 0.24x the 20-day average
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
Three-year record: +3.9% a year | beta to the market -11.39
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
Direction: money coming in (1 week)
Share count change: 1 week: +43.8% (131.38M) over 7d
Shares outstanding: 14.85M | fund size: 431.43M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Sector and country funds

### Israel (EIS) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: bullish analyst view limited to 37.6% of fund, bearish technicals, flat fund flows, no macro surprise.

**Main reasons it gave:**
- Analyst view: 100% buy rating covering 37.6% of fund, price target +24.5% above current
- Technicals: price below 20d, 50d, 200d SMAs, RSI 40.8, MACD negative
- Fund flows flat over past week, share count unchanged
- Macro: yields down slightly, upward sloping curve, VIX low, no surprise data

<details><summary><b>News</b> — score +0.00</summary>

- [ETFs Investing in Teva Pharmaceutical Industries Limited Stocks](https://www.tradingview.com/symbols/BMV-TEVA1/N/etfs/)  
  <sub>TradingView, 10 hours ago</sub>  
  Explore funds investing in TEVA1/N in a single list with price, expense ratio, and more stats for an in-depth analysis of new opportunities.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 118.50 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 121.88 (-2.8%), 50d 122.61 (-3.4%), 200d 122.86 (-3.5%); 50d below 200d
Momentum: RSI(14) 40.8 | MACD -1.462 vs signal -0.914 (histogram -0.548)
Returns: 1d +1.3% | 5d -1.4% | 1m -3.7% | 3m -3.6%
52-week range: 97.88 - 137.69 (now 51.8% of the way up)
Volatility: ATR(14) 1.80 (1.5% of price) | annualised 20d 18.5%
Volume: 0.39x the 20-day average
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
Three-year record: +34.8% a year | beta to the market 1.09
Cost and size: expense ratio 0.59% | net assets 874.00M
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 37.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.17 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +24.5% above the current prices
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
Shares outstanding: 2.55M | fund size: 302.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Canada (EWC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals lack decisive break, modest positive flows, limited analyst coverage with modest buy bias.

**Main reasons it gave:**
- No macro surprise in recent data releases (inflation 3.4%, unemployment 4.2%, jobless claims 197k)
- Technical indicators show no decisive break (price above 20‑day SMA, MACD near signal, low volume)
- Fund flows modestly positive (+2% share count over 1 week)
- Analyst coverage limited to 29.3% of fund with modest buy bias (+4% price target)

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.59 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 59.30 (+0.5%), 50d 60.61 (-1.7%), 200d 57.90 (+2.9%); 50d above 200d
Momentum: RSI(14) 50.2 | MACD -0.437 vs signal -0.536 (histogram 0.099)
Returns: 1d +0.2% | 5d +0.7% | 1m -1.5% | 3m +0.2%
52-week range: 49.72 - 62.64 (now 76.4% of the way up)
Volatility: ATR(14) 0.64 (1.1% of price) | annualised 20d 14.1%
Volume: 0.35x the 20-day average
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
Three-year record: +23.5% a year | beta to the market 0.80
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 29.3% of the fund by weight
Ratings by weight: buy 74.1% | hold 25.9% | sell 0.0% (mean 2.19 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +4.0% above the current prices
Holdings read: RY, TD, SHOP, BMO.TO, BNS.TO
Recent rating changes among them:
  - RY: 2025-08-29 Argus Research: main, Buy -> Buy
  - TD: 2026-06-01 RBC Capital: main, Outperform -> Outperform
  - SHOP: 2026-10-12 Cantor Fitzgerald: main, Neutral -> Neutral
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
Share count change: 1 week: +2.0% (135.90M) over 7d
Shares outstanding: 118.85M | fund size: 7.08B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sweden (EWD) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall despite bullish analyst coverage, strong inflows, and solid fundamentals, because macro data show no surprise and technicals lack a decisive break.

**Main reasons it gave:**
- Share count rose +23.7% over the week, indicating strong inflows
- Analyst coverage of top holdings is 28.9% with 81.7% buy rating and +9.9% price target
- Technical indicators mixed: price just above 20‑day SMA but below 50‑day SMA, RSI 48.7, MACD slightly bullish, volume at 0.06× 20‑day average
- Macro data unchanged: yields stable, no rate surprise, inflation 3.4% and unemployment 4.2% in line with expectations

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 50.88 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 50.76 (+0.2%), 50d 52.08 (-2.3%), 200d 51.45 (-1.1%); 50d above 200d
Momentum: RSI(14) 48.7 | MACD -0.440 vs signal -0.520 (histogram 0.080)
Returns: 1d +0.8% | 5d +1.1% | 1m -1.2% | 3m +0.9%
52-week range: 45.38 - 54.72 (now 58.9% of the way up)
Volatility: ATR(14) 0.67 (1.3% of price) | annualised 20d 15.5%
Volume: 0.06x the 20-day average
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
Three-year record: +19.5% a year | beta to the market 1.25
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 4 largest holdings, 28.9% of the fund by weight
Ratings by weight: buy 81.7% | hold 18.3% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.9% above the current prices
Holdings read: SPOT, ATCO-A.ST, VOLV-B.ST, SAND.ST
Recent rating changes among them:
  - SPOT: 2026-10-12 Cantor Fitzgerald: main, Neutral -> Neutral
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
Share count change: 1 week: +23.7% (182.55M) over 7d
Shares outstanding: 18.73M | fund size: 953.18M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Germany (EWG) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, weak technicals, flat flows, modest fundamentals, bullish analyst view not decisive.

**Main reasons it gave:**
- Flat fund flows (0.0% change) indicate no net demand
- Price below 20‑day, 50‑day, and 200‑day SMAs with low volume (0.11× 20‑day avg) shows weak technicals
- Analyst consensus 78.7% buy and +16.6% price target suggests bullish outlook but not decisive
- Macro data unchanged: yields stable, VIX low, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 41.12 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 41.67 (-1.3%), 50d 42.93 (-4.2%), 200d 42.34 (-2.9%); 50d above 200d
Momentum: RSI(14) 39.7 | MACD -0.550 vs signal -0.528 (histogram -0.022)
Returns: 1d +0.4% | 5d -0.9% | 1m -3.7% | 3m -0.9%
52-week range: 38.08 - 44.59 (now 46.6% of the way up)
Volatility: ATR(14) 0.49 (1.2% of price) | annualised 20d 14.3%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.30</summary>

```text
Fund type: Focused Region
What it holds: P/E 17.64 | P/B 1.86 | P/S 1.23 | 3y earnings growth n/a
Yield: 2.0%
Three-year record: +18.9% a year | beta to the market 0.98
Cost and size: expense ratio 0.49% | net assets 1.47B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Siemens AG 12.1%, SAP SE 11.5%, Allianz SE 9.6%, Siemens Energy AG Ordinary Shares 6.7%, Deutsche Telekom AG 5.4%
Sector mix: Industrials 28.9%, Financial services 22.9%, Technology 16.4%, Healthcare 7.2%
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
Rolled up from the 5 largest holdings, 45.4% of the fund by weight
Ratings by weight: buy 78.7% | hold 21.3% | sell 0.0% (mean 1.91 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.6% above the current prices
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
Shares outstanding: 79.50M | fund size: 3.27B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Italy (EWI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no macro surprise, technicals weak, but analyst view bullish and fund inflows positive.

**Main reasons it gave:**
- US inflation 3.4% and Fed target unchanged – no macro surprise
- ETF price 56.57 below 20‑day SMA 58.70, 50‑day SMA 60.93, 200‑day SMA 58.09 – weak technicals
- Analyst consensus 100% buy with +18.4% price target – bullish outlook
- Fund inflows: share count +5.9% over past week – positive demand

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Europe Financials ETF (EUFN) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EUFN/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest iShares MSCI Europe Financials ETF (EUFN) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.40</summary>

```text
Last close 56.57 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 58.70 (-3.6%), 50d 60.93 (-7.2%), 200d 58.09 (-2.6%); 50d above 200d
Momentum: RSI(14) 32.6 | MACD -1.345 vs signal -1.134 (histogram -0.211)
Returns: 1d +0.7% | 5d -2.4% | 1m -7.1% | 3m -7.0%
52-week range: 50.47 - 63.35 (now 47.4% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 19.1%
Volume: 0.11x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.60</summary>

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
Rolled up from the 5 largest holdings, 53.0% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.03 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.4% above the current prices
Holdings read: UCG.MI, ISP.MI, ENEL.MI, ENI.MI, PRY.MI
Recent rating changes among them: none reported
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
Share count change: 1 week: +5.9% (66.14M) over 7d
Shares outstanding: 20.91M | fund size: 1.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Japan (EWJ) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro surprise, no decisive technical break, and mixed but modestly bullish signals from analysts, positioning and fundamentals lead to a neutral overall view.

**Main reasons it gave:**
- Analyst coverage thin (17% weight) but all‑buy rating and +16% price target
- CFTC speculators net short 8.2% of open interest, short position fell 6.9% OI (crowded short reduced)
- Fund share count rose 5.3% (1.17 B) over the week, indicating inflows
- Technicals: price above 200‑day SMA, but MACD histogram negative and no decisive break

<details><summary><b>News</b> — score +0.00</summary>

- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.
- [iShares MSCI EAFE ETF (EFA) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EFA/)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Find the latest iShares MSCI EAFE ETF (EFA) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Asia Markets & Central Banks (Korea Rate-Hike Bets, RBI Rupee Moves, SK Hynix Slide, India IPO Boom)](https://www.heygotrade.com/en/news/asia-markets-central-banks-korea-rate-hike-bets-rbi-rupee-moves-sk-hynix-slide-india-ipo-boom/)  
  <sub>Gotrade, 23 hours ago</sub>  
  Gotrade News - SK Hynix (SKHY) fell 2.97% in early Seoul trading on Monday, October 12, dragging the Kospi lower, as traders braced for more Bank of Korea.
- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 97.10 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 97.65 (-0.6%), 50d 96.90 (+0.2%), 200d 91.00 (+6.7%); 50d above 200d
Momentum: RSI(14) 48.6 | MACD 0.305 vs signal 0.457 (histogram -0.151)
Returns: 1d -0.2% | 5d -2.2% | 1m -0.5% | 3m +3.9%
52-week range: 79.29 - 99.32 (now 88.9% of the way up)
Volatility: ATR(14) 1.24 (1.3% of price) | annualised 20d 16.6%
Volume: 0.13x the 20-day average
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
Three-year record: +21.5% a year | beta to the market 0.83
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +16.0% above the current prices
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
Direction: money coming in (1 week)
Share count change: 1 week: +5.3% (1.17B) over 7d
Shares outstanding: 241.18M | fund size: 23.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Switzerland (EWL) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, flat fund flows, mixed technicals, and analyst coverage limited to <50% of the fund.

**Main reasons it gave:**
- Flat fund flows (0% change) indicating no net demand
- No macro surprise; yields stable and Fed target unchanged
- Technical mixed: price near 20‑day SMA, MACD histogram positive but low volume
- Analyst rating positive but covers only 48.2% of the fund

<details><summary><b>News</b> — score +0.00</summary>

- [Invesco S&P 500 Top 50 ETF (XLG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLG/)  
  <sub>Yahoo! Finance Canada, 9 hours ago</sub>  
  Find the latest Invesco S&P 500 Top 50 ETF (XLG) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 59.87 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 59.89 (-0.0%), 50d 61.80 (-3.1%), 200d 61.62 (-2.8%); 50d above 200d
Momentum: RSI(14) 44.8 | MACD -0.609 vs signal -0.725 (histogram 0.116)
Returns: 1d +0.6% | 5d +1.0% | 1m -1.0% | 3m -5.5%
52-week range: 55.06 - 65.08 (now 48.0% of the way up)
Volatility: ATR(14) 0.63 (1.1% of price) | annualised 20d 11.1%
Volume: 0.17x the 20-day average
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
Three-year record: +13.2% a year | beta to the market 0.91
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 48.2% of the fund by weight
Ratings by weight: buy 64.8% | hold 35.2% | sell 0.0% (mean 2.48 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.7% above the current prices
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
Shares outstanding: 28.62M | fund size: 1.71B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Netherlands (EWN) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bullish analyst view limited to <50% of holdings, flat fund flows, technicals not decisive, no macro surprise.

**Main reasons it gave:**
- Analyst consensus 100% buy with +34.4% price target covering 46.7% of fund
- Fund flows flat over past week (share count unchanged)
- Technical indicators: price below 20‑day SMA (-2.3%) and 50‑day SMA (-3.8%), RSI 39.7 (oversold), MACD negative
- Macro: no rate or data surprise; yield curve normal, VIX low

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 65.71 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 67.26 (-2.3%), 50d 68.28 (-3.8%), 200d 64.68 (+1.6%); 50d above 200d
Momentum: RSI(14) 39.7 | MACD -0.477 vs signal -0.309 (histogram -0.168)
Returns: 1d -0.5% | 5d -3.5% | 1m -1.2% | 3m -4.3%
52-week range: 55.33 - 71.61 (now 63.8% of the way up)
Volatility: ATR(14) 0.90 (1.4% of price) | annualised 20d 17.4%
Volume: 0.13x the 20-day average
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
Three-year record: +24.4% a year | beta to the market 1.09
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
Weighted price target: +34.4% above the current prices
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
Shares outstanding: 5.55M | fund size: 364.69M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Spain (EWP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, flat fund flows, modest bullish analyst view, but bearish technicals and low volume keep the overall stance neutral.

**Main reasons it gave:**
- Analyst coverage of top holdings (55.8% weight) shows 51.5% buy rating and +5.3% price target
- Fund flows flat (0% change) over the past week indicating no net demand
- Technical indicators bearish: price below 20‑day and 50‑day SMAs, RSI 38.6, MACD negative, volume at 0.05× 20‑day average
- Macro environment unchanged: yields stable, no policy surprise, VIX low at 15.2

<details><summary><b>News</b> — score +0.00</summary>

- [iShares MSCI Europe Financials ETF (EUFN) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/EUFN/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest iShares MSCI Europe Financials ETF (EUFN) stock quote, history, news and other vital information to help you with your stock trading and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 58.31 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 59.59 (-2.1%), 50d 61.22 (-4.7%), 200d 57.76 (+1.0%); 50d above 200d
Momentum: RSI(14) 38.6 | MACD -0.944 vs signal -0.828 (histogram -0.116)
Returns: 1d +0.5% | 5d -0.9% | 1m -4.4% | 3m -2.2%
52-week range: 48.73 - 63.23 (now 66.1% of the way up)
Volatility: ATR(14) 0.80 (1.4% of price) | annualised 20d 17.8%
Volume: 0.05x the 20-day average
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
Three-year record: +33.5% a year | beta to the market 0.88
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
Weighted price target: +5.3% above the current prices
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
Shares outstanding: 37.35M | fund size: 2.18B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Korea (EWY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, technicals bearish but not decisive, modest inflows and solid fundamentals.

**Main reasons it gave:**
- Share count rose 2.1% over the week, indicating modest inflows
- Price below 20‑day SMA and RSI 35.9, showing short‑term bearish momentum
- No macro surprise; yields stable and curve normal
- Fund fundamentals: low P/E 10.4, strong 3‑yr return +48%/yr, modest dividend yield 1.1%

<details><summary><b>News</b> — score +0.00</summary>

- [SK Hynix Stock Falls Below 200-Day Average: A Chinese Rival’s IPO Filing May Explain Why](https://www.tradingview.com/news/benzinga:4f6d993ba094b:0-sk-hynix-stock-falls-below-200-day-average-a-chinese-rival-s-ipo-filing-may-explain-why/)  
  <sub>TradingView, 3 hours ago</sub>  
  The layer of the AI trade that investors treated as the safest bottleneck is the one now being repriced fastest.SK hynix Inc. NASDAQ:SKHY fell 10.09% in...
- [Asia Markets & Central Banks (Korea Rate-Hike Bets, RBI Rupee Moves, SK Hynix Slide, India IPO Boom)](https://www.heygotrade.com/en/news/asia-markets-central-banks-korea-rate-hike-bets-rbi-rupee-moves-sk-hynix-slide-india-ipo-boom/)  
  <sub>Gotrade, 24 hours ago</sub>  
  Gotrade News - SK Hynix (SKHY) fell 2.97% in early Seoul trading on Monday, October 12, dragging the Kospi lower, as traders braced for more Bank of Korea.
- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.
- [U.S. ETF Express | Tradr 2X Short SNDK Daily ETF Was the Top Gainer, Rising 11.87%](https://www.moomoo.com/news/post/1000961998/us-etf-express-tradr-2x-short-sndk-daily-etf-was)  
  <sub>Moomoo, 18 hours ago</sub>  
  TopGainers/Losers2555 U.S. ETFs rose and 3483 fell today.The top gainer was $Tradr 2X Short SNDK Daily ETF(SNDQ.US)$, climbing 11.87% to close at $14.23.
- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 21 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 164.71 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 182.89 (-9.9%), 50d 179.68 (-8.3%), 200d 159.30 (+3.4%); 50d above 200d
Momentum: RSI(14) 35.9 | MACD -1.982 vs signal 0.575 (histogram -2.558)
Returns: 1d -3.2% | 5d -11.6% | 1m -6.5% | 3m -4.0%
52-week range: 82.69 - 219.20 (now 60.1% of the way up)
Volatility: ATR(14) 5.99 (3.6% of price) | annualised 20d 42.5%
Volume: 0.54x the 20-day average
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
Three-year record: +48.3% a year | beta to the market 2.48
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

<details><summary><b>Buying and selling by company insiders</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.30</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +2.1% (489.92M) over 7d
Shares outstanding: 147.94M | fund size: 24.37B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### South Africa (EZA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: technicals show a downtrend with weak momentum, fund flows are flat, and analyst coverage is bullish but limited to 43.4% of the fund.

**Main reasons it gave:**
- Price 64.27 below 20‑day SMA (65.20) and 200‑day SMA (68.98)
- RSI 43.4 and MACD -1.371 vs signal -1.360, indicating weak momentum
- Fund flows flat: share count unchanged (+0.0% over 7 days)
- Analyst view covers 43.4% of fund, rating 100% buy, price target +32.8% above current

<details><summary><b>News</b> — score +0.00</summary>

- [iShares Core MSCI Emerging Markets ETF (IEMG) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/IEMG/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest iShares Core MSCI Emerging Markets ETF (IEMG) stock quote, history, news and other vital information to help you with your stock trading and...
- [Invesco Solar ETF (TAN) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/TAN/)  
  <sub>Yahoo! Finance Canada, 7 hours ago</sub>  
  Find the latest Invesco Solar ETF (TAN) stock quote, history, news and other vital information to help you with your stock trading and investing.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 64.27 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 65.20 (-1.4%), 50d 67.89 (-5.3%), 200d 68.98 (-6.8%); 50d below 200d
Momentum: RSI(14) 43.4 | MACD -1.371 vs signal -1.360 (histogram -0.012)
Returns: 1d +0.8% | 5d +1.0% | 1m -6.2% | 3m +0.8%
52-week range: 60.43 - 81.60 (now 18.1% of the way up)
Volatility: ATR(14) 1.20 (1.9% of price) | annualised 20d 25.1%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.00</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.00</summary>

```text
Fund type: Focused Region
What it holds: P/E 10.44 | P/B 2.00 | P/S 1.73 | 3y earnings growth n/a
Yield: 7.9%
Three-year record: +26.7% a year | beta to the market 1.07
Cost and size: expense ratio 0.59% | net assets 473.79M
What it is made of: Stocks 99.7%, Cash 0.3%
Largest holdings: Anglogold Ashanti PLC 12.7%, Gold Fields Ltd 8.7%, Naspers Ltd Class N 8.4%, Firstrand Ltd 7.4%, Standard Bank Group Ltd 6.2%
Sector mix: Basic materials 39.1%, Financial services 34.4%, Consumer cyclical 12.8%, Communication services 6.4%
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
Rolled up from the 5 largest holdings, 43.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.99 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +32.8% above the current prices
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
Shares outstanding: 7.90M | fund size: 507.73M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Software (IGV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals bullish but low volume, flat fund flows, high valuation offsets strong analyst bullishness.

**Main reasons it gave:**
- Analyst consensus 100% buy with +10.7% price target (42.9% fund weight)
- Technicals bullish: price above 20‑day, 50‑day, 200‑day SMAs; RSI 61; MACD positive; volume 0.37× 20‑day avg
- Fund flows flat: share count unchanged (+0.0% over 7 days)
- Macro unchanged: yields stable, no policy surprise, VIX low at 15.2

<details><summary><b>News</b> — score +0.00</summary>

- [Jim Cramer Calls the Chip Trade Broken, but Semiconductors Are Still Up 62% in 2026](https://247wallst.com/investing/2026/10/13/jim-cramer-calls-the-chip-trade-broken-but-semiconductors-are-still-up-62-in-2026/)  
  <sub>24/7 Wall St., 2 hours ago</sub>  
  Jim Cramer declared chips a broken trade and software the new AI king, but the numbers behind his argument depend on when you start the clock.
- [SoundHound AI Slides 5% to Fresh Lows While C3.ai Climbs 4% on Northland Upgrade; UiPath Slips](https://www.aol.com/articles/soundhound-ai-slides-5-fresh-154631000.html)  
  <sub>AOL.com, 23 hours ago</sub>  
  SoundHound stock has crashed 48% this year while C3.ai jumped 4% after Northland upgraded it to Outperform with a $16 target. IGV software ETF slipped just...
- [Palo Alto CEO Calls AI-Led Software Selloff ‘Paranoid' — Sees Big Buying Window In Cybersecurity And Infra Stocks](https://stocktwits.com/news-articles/markets/equity/palo-alto-ceo-calls-ai-led-software-selloff-paranoid-sees-big-buying-window-in-cybersecurity-and-infra-stocks/cZBWu5pReT1)  
  <sub>Stocktwits, 19 hours ago</sub>  
  The market's “paranoid” and indiscriminate reaction to AI developments – driving a broad SaaS selloff – is likely to persist, Arora said.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 111.26 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 107.98 (+3.0%), 50d 105.53 (+5.4%), 200d 93.74 (+18.7%); 50d above 200d
Momentum: RSI(14) 61.1 | MACD 1.960 vs signal 1.686 (histogram 0.274)
Returns: 1d -0.0% | 5d +0.1% | 1m +4.3% | 3m +18.4%
52-week range: 74.67 - 117.08 (now 86.3% of the way up)
Volatility: ATR(14) 2.42 (2.2% of price) | annualised 20d 20.1%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Technology
What it holds: P/E 31.87 | P/B 7.50 | P/S 8.53 | 3y earnings growth n/a
Yield: 0.0%
Three-year record: +17.1% a year | beta to the market 1.22
Cost and size: expense ratio 0.38% | net assets 13.91B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: Palo Alto Networks Inc 9.7%, Palantir Technologies Inc Ordinary Shares - Class A 9.0%, CrowdStrike Holdings Inc Class A 8.9%, Microsoft Corp 8.5%, Oracle Corp 6.9%
Sector mix: Technology 93.2%, Communication services 4.2%, Financial services 2.2%, Consumer cyclical 0.3%
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
Rolled up from the 5 largest holdings, 42.9% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.65 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.7% above the current prices
Holdings read: PANW, PLTR, CRWD, MSFT, ORCL
Recent rating changes among them:
  - PANW: 2026-10-08 Amerx: init, ? -> Hold
  - PLTR: 2026-10-09 Barclays: init, ? -> Overweight
  - CRWD: 2026-10-09 Needham: main, Buy -> Buy
  - MSFT: 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
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
Shares outstanding: 12.50M | fund size: 1.39B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### India (INDA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: large outflows suggest bearish pressure, but no macro surprise, technicals show mixed signals, and analyst view is bullish but thin. The net of these factors yields a neutral stance.

**Main reasons it gave:**
- Fund flows: -13% share count change over 1 week (outflows of $894.3M)
- Technical trend: price below 50‑day and 200‑day SMA, indicating downtrend
- Analyst view: 100% buy rating on top holdings with +32.4% price target (thin coverage of 23.7% weight)
- Macro: no policy or rate surprise; yields stable, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [Asia Markets & Central Banks (Korea Rate-Hike Bets, RBI Rupee Moves, SK Hynix Slide, India IPO Boom)](https://www.heygotrade.com/en/news/asia-markets-central-banks-korea-rate-hike-bets-rbi-rupee-moves-sk-hynix-slide-india-ipo-boom/)  
  <sub>Gotrade, 24 hours ago</sub>  
  Gotrade News - SK Hynix (SKHY) fell 2.97% in early Seoul trading on Monday, October 12, dragging the Kospi lower, as traders braced for more Bank of Korea.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 47.28 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 47.10 (+0.4%), 50d 48.58 (-2.7%), 200d 49.60 (-4.7%); 50d below 200d
Momentum: RSI(14) 49.0 | MACD -0.629 vs signal -0.673 (histogram 0.044)
Returns: 1d +2.0% | 5d +1.2% | 1m -2.4% | 3m -3.0%
52-week range: 45.42 - 55.29 (now 18.8% of the way up)
Volatility: ATR(14) 0.51 (1.1% of price) | annualised 20d 14.9%
Volume: 0.59x the 20-day average
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
Three-year record: +1.7% a year | beta to the market 0.62
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
Weighted price target: +32.4% above the current prices
Holdings read: HDFCBANK.NS, ICICIBANK.NS, RELIANCE.NS, BHARTIARTL.NS, INFY.NS
Recent rating changes among them: none reported
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
Direction: money going out (1 week)
Share count change: 1 week: -13.0% (-894.30M) over 7d
Shares outstanding: 126.35M | fund size: 5.97B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Defence and aerospace (ITA) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: analysts are strongly bullish (100% buy, +31.8% price target) while recent fund flows show a sizable outflow (-10.5% shares, $1.4 B net redemption) and fundamentals are high‑valued (P/E 31.87, low yield 0.3%). Technicals show a downtrend but oversold momentum. No macro surprise or decisive technical break, so overall stance remains neutral.

**Main reasons it gave:**
- Analyst coverage: 100% buy, weighted price target +31.8% above current price
- Fund flows: -10.5% share count, $1.4B net outflows in past week
- Fund fundamentals: high P/E 31.87, low yield 0.3%
- Technicals: price below 20d/50d/200d SMAs, RSI 28.6 (oversold)

<details><summary><b>News</b> — score +0.00</summary>

- [Iran war has cost average U.S. household $2K, economist estimates (USO:NYSEARCA)](https://seekingalpha.com/news/4652203-iran-war-costing-average-us-household-2k-economist-estimates)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Iran war fallout is costing the average U.S. household nearly $2K, driven by higher energy prices, rising interest rates and military spending.
- [Regulator to allow crypto ETF trading](https://www.bangkokpost.com/business/general/3336114/regulator-to-allow-crypto-etf-trading)  
  <sub>Bangkok Post, 17 hours ago</sub>  
  The Securities and Exchange Commission (SEC) has introduced rules allowing cryptocurrency exchange-traded funds (crypto ETFs) to be established and traded...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 203.12 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 209.74 (-3.2%), 50d 225.83 (-10.1%), 200d 230.19 (-11.8%); 50d below 200d
Momentum: RSI(14) 28.6 | MACD -5.428 vs signal -5.801 (histogram 0.374)
Returns: 1d -1.4% | 5d -2.5% | 1m -6.3% | 3m -14.1%
52-week range: 198.23 - 253.22 (now 8.9% of the way up)
Volatility: ATR(14) 3.52 (1.7% of price) | annualised 20d 14.9%
Volume: 0.39x the 20-day average
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
Three-year record: +24.7% a year | beta to the market 0.98
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
Weighted price target: +31.8% above the current prices
Holdings read: GE, RTX, BA, HWM, LMT
Recent rating changes among them:
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - RTX: 2026-10-09 TD Cowen: main, Buy -> Buy
  - BA: 2026-10-12 Bernstein: main, Outperform -> Outperform
  - HWM: 2026-10-09 TD Cowen: main, Buy -> Buy
  - LMT: 2026-10-09 TD Cowen: main, Hold -> Hold
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
Direction: money going out (1 week)
Share count change: 1 week: -10.5% (-1.40B) over 7d
Shares outstanding: 58.71M | fund size: 11.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US regional banks (KRE) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No macro policy surprise or data release outside expectations; mixed signals from sector news, fund flows, analyst view, and technicals lead to a neutral stance.

**Main reasons it gave:**
- Institutional confidence in banks collapsed ahead of earnings (negative sector news)
- Fund outflows: -4.8% share count, -$186.35M in 1 week (bearish flow)
- Analyst view: 59.8% buy, price target +14.4% above current price (thin coverage 5.7% weight)
- Technical: price below 20‑day, 50‑day, 200‑day SMAs, RSI 36.8 (downtrend)

<details><summary><b>News</b> — score +0.00</summary>

- [Institutional Confidence in Banks Has Collapsed Ahead of Earnings](https://www.benzinga.com/markets/equities/26/10/62316482/institutional-confidence-in-banks-has-collapsed-ahead-of-earnings)  
  <sub>Benzinga, 5 hours ago</sub>  
  U.S. bank stocks lag the market as rising bond yields and tight deposit margins squeeze earnings. Discover key insights as big banks report.
- [Invesco KBW Bank ETF (KBWB) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/KBWB/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest Invesco KBW Bank ETF (KBWB) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [Nasdaq 100 Drops, SanDisk Tumbles 6% as AI Trade Falters: Stock Market Today](https://www.tradingview.com/news/benzinga:655132fc6094b:0-nasdaq-100-drops-sandisk-tumbles-6-as-ai-trade-falters-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were mixed at midday Monday as a selloff in AI-infrastructure names dragged the Nasdaq 100 and small caps lower, while the Dow edged higher and...
- [Small-Cap Stocks Are in Grave Danger Thanks to an Impending Debt Cliff. Use These 2 ETFs for Protection and Profit.](https://www.barchart.com/story/news/6210544/small-cap-stocks-are-in-grave-danger-thanks-to-an-impending-debt-cliff-use-these-2-etfs-for-protection-and-profit)  
  <sub>Barchart.com, 22 hours ago</sub>  
  Small-cap stocks are telling a dangerous story. www.barchart.com. The story is one of persistent selling pressure. And with the iShares Russell 2000 ETF...
- [Options Traders Are Back at 2021 Levels: Will Bitcoin Repeat That Year's Doubling?](https://beincrypto.com/options-traders-2021-levels-bitcoin-doubling/)  
  <sub>BeInCrypto, 6 hours ago</sub>  
  Options volume is back at 2021 levels, yet Bitcoin ETFs log outflows. See why BTC has not repeated its 2021 doubling.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 69.14 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 70.57 (-2.0%), 50d 73.41 (-5.8%), 200d 70.68 (-2.2%); 50d above 200d
Momentum: RSI(14) 36.8 | MACD -1.180 vs signal -1.179 (histogram -0.000)
Returns: 1d -0.6% | 5d -1.3% | 1m -6.7% | 3m -8.8%
52-week range: 58.14 - 77.93 (now 55.6% of the way up)
Volatility: ATR(14) 1.23 (1.8% of price) | annualised 20d 15.1%
Volume: 0.25x the 20-day average
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
Three-year record: +22.1% a year | beta to the market 1.04
Cost and size: expense ratio 0.35% | net assets 3.73B
What it is made of: Stocks 99.9%, Cash 0.1%
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
Ratings by weight: buy 59.8% | hold 40.2% | sell 0.0% (mean 2.24 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +14.4% above the current prices
Holdings read: UBSI, FIBK, ONB, HWC, EWBC
Recent rating changes among them:
  - UBSI: 2026-07-27 Keefe, Bruyette & Woods: main, Market Perform -> Market Perform
  - FIBK: 2026-10-05 Barclays: main, Underweight -> Underweight
  - ONB: 2026-10-09 RBC Capital: main, Sector Perform -> Sector Perform
  - HWC: 2026-10-05 Barclays: main, Overweight -> Overweight
  - EWBC: 2026-10-09 Truist Securities: main, Hold -> Hold
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
Share count change: 1 week: -4.8% (-186.35M) over 7d
Shares outstanding: 53.98M | fund size: 3.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### China (MCHI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: strong analyst bullishness on top holdings (+57% price target) is offset by significant outflows (-7.4% share count in one week) and weak technicals (price below 20‑, 50‑, 200‑day SMAs, RSI 45, low momentum). No macro surprise or policy shift observed.

**Main reasons it gave:**
- Fund flows: -7.4% share count (outflows) over 1 week
- Analyst view: 100% buy rating on top holdings, +57% price target
- Technicals: price below 20‑day, 50‑day, 200‑day SMAs; RSI 45; weak momentum
- Macro: no policy surprise, yields stable, VIX low

<details><summary><b>News</b> — score +0.00</summary>

- [Liquidity Mapping Around (MCHI) Price Events](https://news.stocktradersdaily.com/news_release/35/Liquidity_Mapping_Around_MCHI_Price_Events_101326015002_1791870602.html)  
  <sub>Stock Traders Daily, 13 hours ago</sub>  
  Price-action only: Ishares Msci China Etf (MCHI) movements set the tone for institutional models. Liquidity Mapping Around (MCHI) Price Events.
- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 8 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.
- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 20 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 52.16 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 52.47 (-0.6%), 50d 53.89 (-3.2%), 200d 56.52 (-7.7%); 50d below 200d
Momentum: RSI(14) 45.0 | MACD -0.499 vs signal -0.554 (histogram 0.055)
Returns: 1d +0.0% | 5d -0.1% | 1m -2.2% | 3m -3.7%
52-week range: 50.48 - 65.59 (now 11.1% of the way up)
Volatility: ATR(14) 0.65 (1.3% of price) | annualised 20d 18.3%
Volume: 0.43x the 20-day average
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
Three-year record: +9.6% a year | beta to the market 0.45
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
Weighted price target: +57.0% above the current prices
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
Share count change: 1 week: -7.4% (-473.93M) over 7d
Shares outstanding: 113.66M | fund size: 5.93B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Chip makers (SMH) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as macro shows no surprise, technical indicators are mixed, and while analyst coverage and fund inflows are bullish, fundamentals are high‑valuation and high‑beta in a rate‑sensitive environment.

**Main reasons it gave:**
- Fund flows: share count +15.5% (9.66B) in 1 week
- Analyst view: 100% buy rating, price target +40.7% above current price
- Technical: MACD 7.804 below signal 11.782 (negative momentum)
- Macro: Yield curve normal (+1.16) with no rate surprise
- VIX low at 15.21 (indicating low volatility)

<details><summary><b>News</b> — score +0.00</summary>

- [Semiconductor ETFs SMH, SOXX, SOXL Top Weekly Fund Flows For First Time, Analyst Says](https://stocktwits.com/news-articles/markets/equity/semiconductor-etfs-smh-soxx-soxl-top-weekly-fund-flows-for-first-time/cZoTfDrRJdK)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Semiconductor ETFs SMH, SOXX, SOXL Top Weekly Fund Flows For First Time, Analyst Says. According to senior ETF analyst Eric Balchunas at Bloomberg,...
- [Michael Burry's Big Short Gets Broader: Nvidia-Heavy Chip ETF, Nasdaq Now in Focus](https://www.tradingview.com/news/benzinga:1d48996d0094b:0-michael-burry-s-big-short-gets-broader-nvidia-heavy-chip-etf-nasdaq-now-in-focus/)  
  <sub>TradingView, 23 hours ago</sub>  
  In a Sunday Substack post, hedge fund manager Michael Burry said almost all of his short exposure now consists of put options on two instruments: the...
- [ROTH’s top October ETFs: Semiconductor and technology funds lead Quant rankings (XLK:NYSEARCA)](https://seekingalpha.com/news/4652173-roths-top-october-etfs-semiconductor-and-technology-funds-lead-quant-rankings)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  ROTH's October ETF picks: top tech, semiconductor & cloud funds plus energy/biotech and tactical utility/bond rebounds.
- [Michael Burry Pivots Bearish Bets to Nasdaq-100 and Chip ETF Puts, Sees Market Peak Within 9 Months](https://finance.biggo.com/news/849e4ffa-3c62-4694-8c4f-955fb797a352)  
  <sub>BigGo Finance, 20 hours ago</sub>  
  Michael Burry has concentrated nearly all of his short exposure into put options on the Nasdaq-100 Index and the VanEck Semiconductor ETF, according…
- [PLTR, MRCY Stocks Gain After Announcing Partnership To Automate US Defense Manufacturing](https://stocktwits.com/news-articles/markets/equity/pltr-mrcy-stocks-gain-palatir-mercury-systems-defence-partnership/cZoTX6TRJdo)  
  <sub>Stocktwits, 14 hours ago</sub>  
  Wall Street is expecting Palantir to report earnings per share of $0.35 on revenue of $1.8 billion in its Q2 report scheduled after the bell.
- [Semiconductor selloff: 10 chip stocks showing signs of oversold conditions (SMH:NASDAQ)](https://seekingalpha.com/news/4652398-semiconductor-selloff-deepens-10-chip-stocks-showing-signs-of-oversold-conditions)  
  <sub>Seeking Alpha, 3 hours ago</sub>  
  Semiconductor stocks are sliding on AI valuation fears, higher rates and China competition.
- [SA analyst: Rising yields could extend selloff in small caps](https://www.tradingview.com/news/seekingalpha:1e3855024094b:0-sa-analyst-rising-yields-could-extend-selloff-in-small-caps/)  
  <sub>TradingView, 19 hours ago</sub>  
  Wall Street ended mixed on Monday as investors prepared for a pivotal week of third-quarter bank earnings and fresh inflation data, with rising oil prices...
- [S&P 500, Dow, Nasdaq End Lower As Surging Oil Raises Odds For A September Rate Hike — ORCL, ADBE, M, NVDA, UBER In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-dow-nasdaq-end-lower-as-surging-oil-raises-odds-for-a-september-rate-hike/cZtapeARJ68)  
  <sub>Stocktwits, 15 hours ago</sub>  
  But futures were mixed, with S&P 500 futures marginally up, while Dow and Nasdaq futures slightly eased.
- [S&P 500, Nasdaq 100 End Lower On Chipmaker Weakness, While Salesforce Gains Aid Dow — META, MSFT, BMBL, CRM, SNAP In Focus](https://www.tradingview.com/news/stocktwits:d3c165c49094b:0-s-p-500-nasdaq-100-end-lower-on-chipmaker-weakness-while-salesforce-gains-aid-dow-meta-msft-bmbl-crm-snap-in-focus/)  
  <sub>TradingView, 16 hours ago</sub>  
  The S&P 500 and Nasdaq 100 ended lower on Monday, pulled down by weakness in chipmaker stocks as investors prepare for earnings season, which begins with...
- [S&P 500, Nasdaq 100, Dow End Week Higher With Traders Eyeing Earnings Season — MSFT, NFLX, SPCX, ASTS In Focus](https://stocktwits.com/news-articles/markets/equity/s-and-p-500-nasdaq-100-dow-end-week-higher-with-traders-eyeing-earnings-season/cZxGPMYRBnl)  
  <sub>Stocktwits, 24 hours ago</sub>  
  U.S. stock indices ended higher on Friday as technology stocks recovered from previous session losses and investors prepare for the start of earnings season...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 581.09 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 601.48 (-3.4%), 50d 579.96 (+0.2%), 200d 508.46 (+14.3%); 50d above 200d
Momentum: RSI(14) 43.8 | MACD 7.804 vs signal 11.782 (histogram -3.978)
Returns: 1d -1.7% | 5d -8.1% | 1m +7.3% | 3m -1.6%
52-week range: 325.10 - 668.91 (now 74.5% of the way up)
Volatility: ATR(14) 14.97 (2.6% of price) | annualised 20d 27.8%
Volume: 0.51x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Technology
What it holds: P/E 32.50 | P/B 11.65 | P/S 13.32 | 3y earnings growth n/a
Yield: 0.2%
Three-year record: +60.5% a year | beta to the market 2.00
Cost and size: expense ratio 0.35% | net assets 74.88B
What it is made of: Stocks 100.0%, Cash 0.0%
Largest holdings: NVIDIA Corp 19.3%, Taiwan Semiconductor Manufacturing Co Ltd ADR 9.3%, Advanced Micro Devices Inc 5.5%, Broadcom Inc 5.3%, Micron Technology Inc 4.9%
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
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.34 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +40.7% above the current prices
Holdings read: NVDA, TSM, AMD, AVGO, MU
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - TSM: 2026-10-06 Barclays: main, Overweight -> Overweight
  - AMD: 2026-10-06 Citigroup: main, Buy -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
  - MU: 2026-10-13 Rosenblatt: main, Buy -> Buy
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
Share count change: 1 week: +15.5% (9.66B) over 7d
Shares outstanding: 124.11M | fund size: 72.12B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Turkey (TUR) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, flat fund flows, mixed fundamentals, bearish technicals without decisive break.

**Main reasons it gave:**
- Fund flows flat: share count unchanged (+0.0% week over week)
- Price below 20‑day, 50‑day, and 200‑day SMAs (‑4.0%, ‑10.5%, ‑13.5%)
- RSI 33.6 indicating oversold conditions and MACD negative
- Analyst rating mean 1.69 (strong buy) covering 43.2% of fund weight

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 34.01 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 35.41 (-4.0%), 50d 38.01 (-10.5%), 200d 39.29 (-13.5%); 50d below 200d
Momentum: RSI(14) 33.6 | MACD -1.303 vs signal -1.266 (histogram -0.037)
Returns: 1d +0.6% | 5d -1.3% | 1m -14.5% | 3m -12.2%
52-week range: 31.90 - 43.74 (now 17.8% of the way up)
Volatility: ATR(14) 0.62 (1.8% of price) | annualised 20d 34.7%
Volume: 0.01x the 20-day average
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
Three-year record: -1.5% a year | beta to the market 0.61
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
Weighted price target: +24.2% above the current prices
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
Shares outstanding: 15.65M | fund size: 532.18M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Biotech (XBI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; bearish fund outflows and weak technicals offset bullish fundamentals and mixed analyst view.

**Main reasons it gave:**
- Fund flows: -8.8% share count change (outflows) over 1 week
- Technicals: price 3.9% below 20‑day SMA, RSI 39, MACD negative
- Macro: Fed expected 25 bp rate hike, 10‑yr yield down 5 bp, VIX 15.2
- Analyst view: 61% buy rating but weighted price target -9.1% below current price

<details><summary><b>News</b> — score +0.00</summary>

- [Biotech’s Rebound Reality: Surging M&A Deals Meet Deep Retail Skepticism](https://etfdb.com/leveraged-inverse-content-hub/biotech-s-rebound-surging-m-as-meet-retail-skepticism/)  
  <sub>ETF Database, 19 hours ago</sub>  
  Discover how soaring pharma M&A deals and a surging Direxion's LABU ETF contrast with record retail skepticism in the biotech sector.
- [Dow, S&P 500, Nasdaq Futures Edge Higher Ahead Of Fed Rate Hike Expectations: CRCL, WING, CAVA, FPS Stocks In Focus](https://stocktwits.com/news-articles/markets/equity/dow-s-and-p-500-nasdaq-futures-edge-higher-ahead-of-fed-rate-hike-expectations-crcl-wing-cava-fps-stocks-in-focus/cZtYTESRB22)  
  <sub>Stocktwits, 9 hours ago</sub>  
  According to CME FedWatch data, there is a 92.4% probability that the Fed will hike interest rates by 25 basis points from the current 3.50% to 3.75%.
- [Cathie Wood’s ARK Sells HOOD Stock Again – Even As Robinhood Hits 1M Gold Cards, Launches Platinum Card](https://stocktwits.com/news-articles/markets/equity/cathie-wood-ark-sells-hood-stock-robinhood-platinum-card/cZZnmxnR7xN)  
  <sub>Stocktwits, 14 hours ago</sub>  
  ARK sold HOOD again on Wednesday, buying SpaceX stock through all its ETFs. Robinhood launched the Platinum Card the same day, a premium offering with...
- [Why Did OPEN, NKE, CCL Stocks Crash To 52-Week Lows Today?](https://stocktwits.com/news-articles/markets/equity/why-did-open-nke-ccl-stocks-crash-to-52-week-lows-today/cZtY2PcRB2d)  
  <sub>Stocktwits, 18 hours ago</sub>  
  Housing weakness, a prolonged athleticwear turnaround, and rising cruise fuel costs weighed on investor sentiment.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 148.83 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 154.81 (-3.9%), 50d 158.37 (-6.0%), 200d 139.81 (+6.4%); 50d above 200d
Momentum: RSI(14) 39.0 | MACD -2.205 vs signal -1.668 (histogram -0.537)
Returns: 1d -1.7% | 5d -1.4% | 1m -5.6% | 3m -4.7%
52-week range: 105.12 - 169.55 (now 67.8% of the way up)
Volatility: ATR(14) 4.20 (2.8% of price) | annualised 20d 29.2%
Volume: 0.27x the 20-day average
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
Three-year record: +29.2% a year | beta to the market 1.09
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

<details><summary><b>What analysts and big funds say</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.20</summary>

```text
Rolled up from the 5 largest holdings, 9.2% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 61.1% | hold 38.9% | sell 0.0% (mean 2.09 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -9.1% above the current prices
Holdings read: TWST, MRNA, NTRA, IOVA, AMGN
Recent rating changes among them:
  - TWST: 2026-10-12 Canaccord Genuity: main, Buy -> Buy
  - MRNA: 2026-10-07 Morgan Stanley: main, Equal-Weight -> Equal-Weight
  - NTRA: 2026-10-07 Barclays: main, Overweight -> Overweight
  - IOVA: 2026-10-08 Baird: main, Neutral -> Neutral
  - AMGN: 2026-10-13 Guggenheim: main, Neutral -> Neutral
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
Direction: money going out (1 week)
Share count change: 1 week: -8.8% (-964.45M) over 7d
Shares outstanding: 67.38M | fund size: 10.03B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US house builders (XHB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall as no macro surprise, technicals lack decisive break, and fundamentals are moderate despite positive flows and bullish analyst view on a thin slice.

**Main reasons it gave:**
- Fund flows: +9.6% share count increase over 7 days indicating strong inflows
- Analyst coverage: 100% buy rating on top 5 holdings (17% of fund) with +18.3% price target
- Technicals: price below 20d, 50d, 200d SMAs; RSI 36.3 indicating oversold but low volume
- Macro: no surprise in inflation (3.4%) or Fed policy (target 4.0%)
- News: housing market risk from mortgage buydowns noted, but no immediate macro impact

<details><summary><b>News</b> — score +0.00</summary>

- [The Housing Market's Hidden Risk: Mortgage Buydowns As A Threat To The Industry (BATS:ITB)](https://seekingalpha.com/article/4953732-housing-markets-hidden-risk-mortgage-buydowns-threat-to-industry)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  Homebuilders face declining deliveries, lower average prices, shrinking margins, and rising net debt. Read why I remain long-term bullish on the housing...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 94.14 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 96.49 (-2.4%), 50d 101.58 (-7.3%), 200d 105.81 (-11.0%); 50d below 200d
Momentum: RSI(14) 36.3 | MACD -1.788 vs signal -1.804 (histogram 0.015)
Returns: 1d +0.1% | 5d -3.3% | 1m -4.2% | 3m -13.6%
52-week range: 94.05 - 121.36 (now 0.3% of the way up)
Volatility: ATR(14) 2.07 (2.2% of price) | annualised 20d 19.4%
Volume: 0.22x the 20-day average
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
Three-year record: +8.7% a year | beta to the market 1.48
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

<details><summary><b>What analysts and big funds say</b> — score +0.40</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.40</summary>

```text
Rolled up from the 5 largest holdings, 17.0% of the fund by weight  -- thin, so read this as a fact about that slice rather than the fund
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.67 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +18.3% above the current prices
Holdings read: SN, CVCO, SKY, JCI, W
Recent rating changes among them:
  - SN: 2026-08-07 TD Cowen: main, Buy -> Buy
  - CVCO: 2026-09-30 Oppenheimer: init, ? -> Outperform
  - SKY: 2026-09-30 Oppenheimer: init, ? -> Perform
  - JCI: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - W: 2026-10-08 Baird: main, Neutral -> Neutral
```

</details>

<details><summary><b>Buying and selling by company insiders</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>Money going into and out of this fund</b> — score +0.45</summary>

```text
Direction: money coming in (1 week)
Share count change: 1 week: +9.6% (124.19M) over 7d
Shares outstanding: 15.09M | fund size: 1.42B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US materials and chemicals (XLB) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall: analyst view modestly bullish but limited coverage, flat fund flows, technicals show price below key SMAs with no decisive break, macro environment unchanged.

**Main reasons it gave:**
- Analyst consensus 100% buy on top holdings with +13.8% price target (34.1% coverage)
- Fund flows flat over past week (0% net change in share count)
- Price below 20‑day, 50‑day and 200‑day SMAs; RSI 44, MACD line above signal
- Macro data unchanged: yields stable, VIX low, no surprise inflation or employment data

<details><summary><b>News</b> — score +0.00</summary>

- [Why I Monitor XLI And XLB As Leading Indicators For S&P 500 (NYSEARCA:XLI)](https://seekingalpha.com/article/4953753-why-i-monitor-xli-and-xlb-as-leading-indicators-for-s-and-p-500)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Industrial (XLI) and Materials (XLB) sectors have underperformed the broader market both in terms of price and dividend growth.
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 1.68% · -0.61% · -0.55% · -5.98% · -1.84% · 22.48% · 787.07%. Key...
- [Industrial and Materials sectors lag market wit...](https://pluang.com/en/news-feed/mengapa-saya-memantau-xli-dan-xlb-sebagai-indikator-terdepan-sp500)  
  <sub>Pluang, 2 hours ago</sub>  
  The Industrial (XLI) and Materials (XLB) sectors have underperformed the broader market, showing weak price and dividend growth. XLI's dividend fell 11.8%...
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 1.68% · -0.61% · -0.55% · -5.98% · -1.84% · 22.48% · 787.07%. Key...
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [Charlie Bilello Says Iran War Inflation Is 'Rewarding Big Oil,' Flags a 56% Spread Between XLE and XLY](https://www.benzinga.com/etfs/sector-etfs/26/10/62316125/charlie-bilello-says-iran-war-inflation-is-rewarding-big-oil-flags-a-56-spread-between-xle-and-xly)  
  <sub>Benzinga, 5 hours ago</sub>  
  Iran war-driven inflation boosts oil stocks, with XLE up 50%, while soaring fuel and commodity prices squeeze consumers.
- [ValuEngine Weekly Commentary With Strategy Notes](https://seekingalpha.com/article/4953759-valuengine-weekly-commentary-strategy-notes)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. equity markets were mixed this week, with broader gains across value, defensive, and cyclical sectors offset by weakness in technology and the NASDAQ...
- [9 Of 11 Sectors Rise Monday As Cyclicals Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62302120/9-of-11-sectors-rise-monday-as-cyclicals-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Nine of 11 sectors are higher in Monday's regular session, with cyclical sectors holding two of the top three positions. The leaders are separated rather...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 49.49 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 49.58 (-0.2%), 50d 51.28 (-3.5%), 200d 50.79 (-2.6%); 50d above 200d
Momentum: RSI(14) 44.0 | MACD -0.529 vs signal -0.634 (histogram 0.105)
Returns: 1d +0.1% | 5d -0.5% | 1m -2.0% | 3m -2.0%
52-week range: 42.23 - 53.67 (now 63.4% of the way up)
Volatility: ATR(14) 0.72 (1.5% of price) | annualised 20d 13.8%
Volume: 0.26x the 20-day average
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

<details><summary><b>What analysts and big funds say</b> — score +0.30</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.30</summary>

```text
Rolled up from the 5 largest holdings, 34.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.71 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +13.8% above the current prices
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
Shares outstanding: 71.92M | fund size: 3.56B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US media and communication (XLC) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, mixed technicals, modest fund flows, and bullish analyst view not enough to outweigh neutral backdrop.

**Main reasons it gave:**
- Analyst coverage 90.6% buy, weighted price target +11.2% above current price
- Fund flows flat, share count +0.4% week over week indicating limited demand
- Technicals mixed: price above 20‑day/50‑day SMA but below 200‑day SMA
- Macro backdrop stable: Treasury yields unchanged, no policy surprise

<details><summary><b>News</b> — score +0.00</summary>

- [Time to Buy the Dead-Cat Bounce in Income Stocks?](https://moneyandmarkets.com/time-to-buy-the-dead-cat-bounce-in-income-stocks/)  
  <sub>Money & Markets, 16 hours ago</sub>  
  Perhaps it was inevitable after the brutal beating the sector has endured, but the State Street Utilities Select Sector SPDR ETF (XLU) led all sectors...
- [Here's Why I'm Buying This Telecom Selloff Hand Over Fist (NYSE:VZ)](https://seekingalpha.com/article/4953558-heres-why-im-buying-this-telecom-selloff-hand-over-fist)  
  <sub>Seeking Alpha, 21 hours ago</sub>  
  Telecom stocks Verizon Communications Inc., AT&T Inc. & T-Mobile US, Inc. plunged on Starlink spectrum fears. Click for more on VZ, T, and TMUS prospects.
- [SECA ETF Holdings List — CBOE:SECA](https://www.tradingview.com/symbols/CBOE-SECA/holdings/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore Main Active Rotation ETF holdings with weight, market value, and other helpful data to make more informed decisions for SECA trading.
- [Nasdaq 100 Drops, SanDisk Tumbles 6% as AI Trade Falters: Stock Market Today](https://www.tradingview.com/news/benzinga:655132fc6094b:0-nasdaq-100-drops-sandisk-tumbles-6-as-ai-trade-falters-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were mixed at midday Monday as a selloff in AI-infrastructure names dragged the Nasdaq 100 and small caps lower, while the Dow edged higher and...
- [Form 4 State Street® Communication Services Select Sector SPDR® ETF For: 13 October](https://in.investing.com/news/stock-market-news/form-4-state-street-communication-services-select-sector-spdr-etf-for-13-october-93CH-5630142)  
  <sub>Investing.com India, 4 hours ago</sub>  
  Filed Pursuant to Rule 424(b)(2). Registration No. 333-277211. October 8, 2026. PRICING SUPPLEMENT. (To Prospectus dated February 21, 2024,.
- [A 6-Day Winning Streak Has Snap Stock Up 17%](https://www.trefis.com/stock/snap/articles/618456/a-6-day-winning-streak-has-snap-stock-up-17/2026-10-13)  
  <sub>Trefis, 8 hours ago</sub>  
  Snap stock is on a 6-day winning streak, up 17.0% since the run began. That added about $1.6 billion to the company's market value, which now stands at...
- [ValuEngine Weekly Commentary With Strategy Notes](https://seekingalpha.com/article/4953759-valuengine-weekly-commentary-strategy-notes)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. equity markets were mixed this week, with broader gains across value, defensive, and cyclical sectors offset by weakness in technology and the NASDAQ...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 112.76 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 111.95 (+0.7%), 50d 111.92 (+0.7%), 200d 113.61 (-0.7%); 50d below 200d
Momentum: RSI(14) 53.5 | MACD -0.130 vs signal -0.135 (histogram 0.005)
Returns: 1d +1.2% | 5d +1.0% | 1m -2.0% | 3m -0.5%
52-week range: 105.38 - 120.08 (now 50.2% of the way up)
Volatility: ATR(14) 1.60 (1.4% of price) | annualised 20d 20.0%
Volume: 0.29x the 20-day average
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
Three-year record: +19.1% a year | beta to the market 0.85
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
Weighted price target: +11.2% above the current prices
Holdings read: META, GOOGL, GOOG, WBD, DIS
Recent rating changes among them:
  - META: 2024-09-30 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOGL: 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - GOOG: 2026-10-08 TD Cowen: main, Buy -> Buy
  - WBD: 2026-09-29 Argus Research: down, Hold -> Sell
  - DIS: 2026-10-09 Needham: reit, Buy -> Buy
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
Share count change: 1 week: +0.4% (80.29M) over 7d
Shares outstanding: 204.10M | fund size: 23.01B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US banks and finance (XLF) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no macro surprise, technicals are mixed, analyst view bullish but unsupported by macro, fund flows flat.

**Main reasons it gave:**
- Yield curve unchanged (10y-3m spread +1.16) and yields stable
- Technical indicators neutral (RSI 49.3, price near 20‑day SMA, below 50‑day SMA)
- Analyst coverage 100% buy with +9.8% price target but no supporting macro catalyst
- Fund flows flat over past week (share count +0.0%)

<details><summary><b>News</b> — score +0.00</summary>

- [Goldman Sachs Rises on Equities-Led Earnings Beat; JPMorgan Chase Treads Water, Wells Fargo Declines 3%](https://247wallst.com/investing/2026/10/13/goldman-sachs-rises-on-equities-led-earnings-beat-jpmorgan-chase-treads-water-wells-fargo-declines-3/)  
  <sub>24/7 Wall St., 43 minutes ago</sub>  
  Goldman Sachs crushed Q3 estimates with EPS of $17.01 vs. $13.65 expected, as equities revenue surged 72% to $6.44 billion; GS stock jumped 3%, JPM rose 2%.
- [BofA survey shows biggest cut to bank overweight since 2023 (XLF:NYSEARCA)](https://seekingalpha.com/news/4652454-bofa-survey-shows-biggest-cut-to-bank-overweight-since-2023)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  BofA's fund manager survey shows banks saw the biggest allocation cut since 2023, while tech hit a 2020-high overweight.
- [Billionaire Investor Bought 2.56 Million Block Shares in Q2](https://www.benzinga.com/markets/large-cap/26/10/62310092/billionaire-investor-bought-2-56-million-block-shares-in-q2)  
  <sub>Benzinga, 19 hours ago</sub>  
  Dan Loeb's Third Point acquired approximately 2.56 million Block shares worth about $194 million as of June 30, according to the reported investment.
- [SA analyst: Rising yields could extend selloff in small caps](https://www.tradingview.com/news/seekingalpha:1e3855024094b:0-sa-analyst-rising-yields-could-extend-selloff-in-small-caps/)  
  <sub>TradingView, 19 hours ago</sub>  
  Wall Street ended mixed on Monday as investors prepared for a pivotal week of third-quarter bank earnings and fresh inflation data, with rising oil prices...
- [Chart of the Day: Will Earnings Change the Game for Morgan Stanley?](https://pro.thestreet.com/portfolio/chart-of-the-day-will-earnings-change-the-game-for-morgan-stanley)  
  <sub>RealMoney Pro, 24 hours ago</sub>  
  A huge week of earnings from the banks/financials awaits. Morgan Stanley (MS) will deliver results for its recently completed third quarter Wednesday,...
- [Calm before the bank earnings wave: XLF options chain signals quiet week (XLF:NYSEARCA)](https://seekingalpha.com/news/4652199-calm-before-the-bank-earnings-wave-xlf-options-chain-signals-quiet-week)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Options traders on Monday priced in a modest 2% price move for the Financial Select Sector SPDR Fund (XLF) ahead of major banks' third-quarter earnings...
- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Tuesday Amid Chip Weakness, Bank Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131042414.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.04% and the actively t.
- [Sector Update: Financial](https://finance.yahoo.com/markets/stocks/articles/sector-financial-172556967.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  Financial stocks were advancing in Monday afternoon trading, with the NYSE Financial Index and the State Street Financial Select Sector SPDR ETF (XLF) each...
- [Goldman Sachs Stock Traders Made $6.4B. Bond Desks Lagged - State Street SPDR S&P 500 ETF Trust (ARCA:SPY](https://www.benzinga.com/markets/large-cap/26/10/62322643/goldman-sachs-stock-traders-6-billion-bank-earnings-jpmorgan-wells-fargo)  
  <sub>Benzinga, 2 hours ago</sub>  
  Goldman Sachs stock jumps 4.5% after equities trading revenue soared 72% to $6.44 billion. JPMorgan and Wells Fargo show the same split with bond desks.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 55.05 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 54.58 (+0.9%), 50d 56.45 (-2.5%), 200d 53.69 (+2.5%); 50d above 200d
Momentum: RSI(14) 49.3 | MACD -0.534 vs signal -0.728 (histogram 0.194)
Returns: 1d +0.0% | 5d +1.9% | 1m -3.5% | 3m -2.7%
52-week range: 47.81 - 58.56 (now 67.3% of the way up)
Volatility: ATR(14) 0.69 (1.3% of price) | annualised 20d 12.7%
Volume: 0.43x the 20-day average
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
Three-year record: +20.1% a year | beta to the market 0.75
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

<details><summary><b>What analysts and big funds say</b> — score +0.45</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.45</summary>

```text
Rolled up from the 5 largest holdings, 42.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +9.8% above the current prices
Holdings read: BRK-B, JPM, V, MA, BAC
Recent rating changes among them:
  - BRK-B: 2026-08-10 UBS: main, Buy -> Buy
  - JPM: 2026-10-05 UBS: main, Buy -> Buy
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
Shares outstanding: 883.44M | fund size: 48.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US industry (XLI) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall; no material macro surprise, technicals show short‑term weakness, and fund flows are flat. Analyst coverage is bullish but limited to ~26% of the fund, and fundamentals are mixed.

**Main reasons it gave:**
- Fund flows flat: share count change +0.0% over 7 days
- Analyst coverage: 100% buy rating for top holdings with weighted price target +23.8% (covers 25.7% of fund)
- Technicals: price below 20‑day SMA (169.22), 50‑day SMA (175.19), 200‑day SMA (172.80); RSI 39.6 indicating short‑term weakness
- Macro: yields stable, upward‑sloping yield curve (+1.16), VIX low at 15.21

<details><summary><b>News</b> — score +0.00</summary>

- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Tuesday Amid Chip Weakness, Bank Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131042414.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.04% and the actively t.
- [Why I Monitor XLI And XLB As Leading Indicators For S&P 500 (NYSEARCA:XLI)](https://seekingalpha.com/article/4953753-why-i-monitor-xli-and-xlb-as-leading-indicators-for-s-and-p-500)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  Industrial (XLI) and Materials (XLB) sectors have underperformed the broader market both in terms of price and dividend growth.
- [Form 4 State Street® Communication Services Select Sector SPDR® ETF For: 13 October](https://in.investing.com/news/stock-market-news/form-4-state-street-communication-services-select-sector-spdr-etf-for-13-october-93CH-5630142)  
  <sub>Investing.com India, 4 hours ago</sub>  
  Filed Pursuant to Rule 424(b)(2). Registration No. 333-277211. October 8, 2026. PRICING SUPPLEMENT. (To Prospectus dated February 21, 2024,.
- [ValuEngine Weekly Commentary With Strategy Notes](https://seekingalpha.com/article/4953759-valuengine-weekly-commentary-strategy-notes)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. equity markets were mixed this week, with broader gains across value, defensive, and cyclical sectors offset by weakness in technology and the NASDAQ...
- [Invesco S&P 500 Equal Weight ETF (RSP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/RSP/)  
  <sub>Yahoo! Finance Canada, 6 hours ago</sub>  
  Find the latest Invesco S&P 500 Equal Weight ETF (RSP) stock quote, history, news and other vital information to help you with your stock trading and...
- [ROTH’s top October ETFs: Semiconductor and technology funds lead Quant rankings](https://www.tradingview.com/news/seekingalpha:fbc1c95c1094b:0-roth-s-top-october-etfs-semiconductor-and-technology-funds-lead-quant-rankings/)  
  <sub>TradingView, 23 hours ago</sub>  
  ROTH's October ETF picks favor technology exposure, with semiconductor, technology and cloud-computing funds leading the list, while energy and large-cap...
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  Find the latest State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock quote, history, news and other vital information to help you with...
- [Exchange-Traded Funds Fall as US Equities Turn Mixed After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-fall-us-171149294.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Broad Market Indicators Broad-market exchange-traded funds IWM and IVV fell. Actively traded Invesco QQQ Trust (QQQ) lost 0.7%. US equity indexes traded...
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock quote, history, news and other vital information to help you with...
- [9 Of 11 Sectors Rise Monday As Cyclicals Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62302120/9-of-11-sectors-rise-monday-as-cyclicals-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Nine of 11 sectors are higher in Monday's regular session, with cyclical sectors holding two of the top three positions. The leaders are separated rather...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 167.46 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 169.22 (-1.0%), 50d 175.19 (-4.4%), 200d 172.80 (-3.1%); 50d above 200d
Momentum: RSI(14) 39.6 | MACD -1.526 vs signal -1.793 (histogram 0.267)
Returns: 1d -1.0% | 5d -2.4% | 1m -1.5% | 3m -7.0%
52-week range: 147.83 - 186.51 (now 50.7% of the way up)
Volatility: ATR(14) 2.30 (1.4% of price) | annualised 20d 13.0%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Industrials
What it holds: P/E 27.43 | P/B 6.56 | P/S 2.92 | 3y earnings growth n/a
Yield: 1.1%
Three-year record: +19.9% a year | beta to the market 1.01
Cost and size: expense ratio 0.08% | net assets 29.83B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Caterpillar Inc 7.0%, GE Aerospace 6.1%, GE Vernova Inc 4.8%, RTX Corp 4.7%, Deere & Co 3.2%
Sector mix: Industrials 93.4%, Technology 6.1%, Basic materials 0.3%, Consumer cyclical 0.2%
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
Rolled up from the 5 largest holdings, 25.7% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.78 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +23.8% above the current prices
Holdings read: CAT, GE, GEV, RTX, DE
Recent rating changes among them:
  - CAT: 2024-10-14 JP Morgan: main, Overweight -> Overweight
  - GE: 2026-09-30 Wells Fargo: main, Overweight -> Overweight
  - GEV: 2026-10-13 Guggenheim: reit, Buy -> Buy
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
Shares outstanding: 136.63M | fund size: 22.88B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US technology (XLK) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Analyst view: 100% buy rating with weighted price target +20.1% for top holdings
- Fund flows: +5.4% share count increase over 1 week indicating inflows
- Fundamentals: high valuations (P/E 32, P/B 11.9) suggest modest bearish pressure
- Technicals: price above 20‑day SMA, 50‑day SMA above 200‑day SMA, RSI 52.5, MACD slightly below signal
- Macro: stable yields, low VIX, no surprise data releases

<details><summary><b>News</b> — score +0.00</summary>

- [ValuEngine Weekly Commentary With Strategy Notes](https://seekingalpha.com/article/4953759-valuengine-weekly-commentary-strategy-notes)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. equity markets were mixed this week, with broader gains across value, defensive, and cyclical sectors offset by weakness in technology and the NASDAQ...
- [Sector Update: Tech](https://finance.yahoo.com/markets/stocks/articles/sector-tech-165956604.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>
- [ROTH’s top October ETFs: Semiconductor and technology funds lead Quant rankings](https://www.tradingview.com/news/seekingalpha:fbc1c95c1094b:0-roth-s-top-october-etfs-semiconductor-and-technology-funds-lead-quant-rankings/)  
  <sub>TradingView, 23 hours ago</sub>  
  ROTH's October ETF picks favor technology exposure, with semiconductor, technology and cloud-computing funds leading the list, while energy and large-cap...
- [Yes, The Technology Sector Will Lead S&P Profit Growth (Again)](https://seekingalpha.com/article/4953588-yes-technology-sector-will-lead-sp-profit-growth-again)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  The MoneyShow Chart of the Day shows that profits at S&P 500 Index companies are expected to rise 24.4% in Q3. But earnings in the IT sector could soar as...
- [Time to Buy the Dead-Cat Bounce in Income Stocks?](https://moneyandmarkets.com/time-to-buy-the-dead-cat-bounce-in-income-stocks/)  
  <sub>Money & Markets, 16 hours ago</sub>  
  Perhaps it was inevitable after the brutal beating the sector has endured, but the State Street Utilities Select Sector SPDR ETF (XLU) led all sectors...
- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Tuesday Amid Chip Weakness, Bank Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131042414.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>
- [6% Treasury Yield: Wall Street’s Iceberg Warning For Stocks - iShares 20+ Year Treasury Bond ETF (NASDAQ](https://www.benzinga.com/markets/bonds/26/10/62323584/6-percent-treasury-yield-iceberg-warning-fund-managers-stocks-bonds)  
  <sub>Benzinga, 1 hour ago</sub>  
  Fund managers told BofA a 6% 10-year Treasury yield would make them swap stocks for bonds. One in five say yields are already there.
- [Ray Dalio Says This Is When the Artificial Intelligence (AI) Bubble Could Pop](https://www.theglobeandmail.com/investing/markets/stocks/NVDA-Q/pressreleases/6211407/ray-dalio-says-this-is-when-the-artificial-intelligence-ai-bubble-could-pop/)  
  <sub>The Globe and Mail, 22 hours ago</sub>  
  Detailed price information for Nvidia Corp (NVDA-Q) from The Globe and Mail including charting and trades.
- [Exchange-Traded Funds Fall as US Equities Turn Mixed After Midday](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-fall-us-171149294.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>
- [Sector Update: Tech Stocks Fall Monday Afternoon](https://finance.yahoo.com/technology/articles/sector-tech-stocks-fall-monday-173629949.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 195.19 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 195.69 (-0.3%), 50d 189.81 (+2.8%), 200d 166.87 (+17.0%); 50d above 200d
Momentum: RSI(14) 52.5 | MACD 2.783 vs signal 3.244 (histogram -0.461)
Returns: 1d -0.6% | 5d -3.4% | 1m +5.9% | 3m +7.5%
52-week range: 127.50 - 202.00 (now 90.9% of the way up)
Volatility: ATR(14) 2.99 (1.5% of price) | annualised 20d 17.2%
Volume: 0.37x the 20-day average
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
Three-year record: +33.8% a year | beta to the market 1.45
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 49.5% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.57 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +20.1% above the current prices
Holdings read: NVDA, AAPL, MSFT, AMD, AVGO
Recent rating changes among them:
  - NVDA: 2026-10-01 Cantor Fitzgerald: reit, Overweight -> Overweight
  - AAPL: 2026-10-12 JP Morgan: main, Overweight -> Overweight
  - MSFT: 2026-10-07 Evercore ISI Group: main, Outperform -> Outperform
  - AMD: 2026-10-06 Citigroup: main, Buy -> Buy
  - AVGO: 2026-09-10 Piper Sandler: init, ? -> Overweight
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
Share count change: 1 week: +5.4% (6.36B) over 7d
Shares outstanding: 640.32M | fund size: 124.98B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US everyday goods (XLP) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral stance as no material macro surprise, no decisive technical break, and flat fund flows. Analyst coverage is bullish but limited to < 50 % of the fund, and fundamentals are solid but not a catalyst.

**Main reasons it gave:**
- Macro data in line with expectations: Treasury yields stable, inflation 3.4% near target, no policy surprise
- Technicals show price above 20‑, 50‑ and 200‑day SMAs with modest momentum but low volume, no decisive break
- Fund flows flat over the past week, indicating no net demand shift
- Analyst coverage of top holdings (41.8 % weight) is 100 % buy with a +7.7 % price target, but limited to less than half the fund

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Staples Select Sector SPDR ETF (XLP) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLP/)  
  <sub>Yahoo! Finance Canada, 12 hours ago</sub>  
  State Street Consumer Staples Select Sector SPDR ETF (XLP) ... This price reflects trading activity during the overnight session on the Blue Ocean ATS, available...
- [Consumer Staples Select Sector SPDR Fund (XLP) Stock Price | Quotes & News](https://www.moomoo.com/stock/XLP-US?chain_id=Name1K9-3FXPhg.1lcsaqg&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FIFF-US%22%7D)  
  <sub>Moomoo, 1 hour ago</sub>  
  Track the latest Consumer Staples Select Sector SPDR Fund (XLP) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF...
- [Top and bottom 5 consumer staples stocks by Seeking Alpha Quant Score (XLP:NYSEARCA)](https://seekingalpha.com/news/4652029-top-and-bottom-5-consumer-staples-stocks-by-seeking-alpha-quant-score)  
  <sub>Seeking Alpha, 34 minutes ago</sub>  
  Consumer Staples stocks have underperformed the broader market during Q3, with the Consumer Staples Select Sector SPDR Fund (XLP) posting a 3.24% price...
- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Tuesday Amid Chip Weakness, Bank Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131042414.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.04% and the actively t.
- [Quant Spotlight: Top and bottom healthcare stocks ahead of Q3](https://seekingalpha.com/news/4651978-seeking-alpha-s-quant-spotlight-highest-and-lowest-rated-healthcare-stocks-ahead-of-q3)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  As the Q3 earnings season gets underway, healthcare investors are evaluating sector constituents through Seeking Alpha's quantitative framework.
- [Sector Update: Consumer Stocks Mixed Pre-Bell Monday](https://www.bitget.com/amp/news/detail/12560605946192)  
  <sub>Bitget, 23 hours ago</sub>  
  09:16 AM EDT, 10/12/2026 (MT Newswires) -- Consumer stocks were mixed premarket Monday, with the State Street Consumer Staples Select Sector SPDR ETF (XLP)...
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 1.68% · -0.61% · -0.55% · -5.98% · -1.84% · 22.48% · 787.07%. Key...
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 1.72% · 2.79% · 14.87% · 9.80% · 19.74% · 35.39% · 585.02%. Key Events. Baseline. Advanced Chart.
- [From Laggard to Leader: The Surprising Comeback of Healthcare](https://etfdb.com/equity-etf-content-hub/laggard-leader-surprising-comeback-healthcare/)  
  <sub>ETF Database, 5 minutes ago</sub>  
  Healthcare stocks have finally stepped back into the spotlight. After spending much of the past several years in the shadow of technology and AI, the sector...
- [Charlie Bilello Says Iran War Inflation Is 'Rewarding Big Oil,' Flags a 56% Spread Between XLE and XLY](https://www.benzinga.com/etfs/sector-etfs/26/10/62316125/charlie-bilello-says-iran-war-inflation-is-rewarding-big-oil-flags-a-56-spread-between-xle-and-xly)  
  <sub>Benzinga, 5 hours ago</sub>  
  Iran war-driven inflation boosts oil stocks, with XLE up 50%, while soaring fuel and commodity prices squeeze consumers.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 84.30 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 82.31 (+2.4%), 50d 84.00 (+0.4%), 200d 83.87 (+0.5%); 50d above 200d
Momentum: RSI(14) 59.1 | MACD -0.131 vs signal -0.574 (histogram 0.442)
Returns: 1d -0.1% | 5d +3.1% | 1m -0.1% | 3m +1.0%
52-week range: 75.60 - 90.01 (now 60.4% of the way up)
Volatility: ATR(14) 0.99 (1.2% of price) | annualised 20d 13.7%
Volume: 0.37x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score +0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score +0.20</summary>

```text
Fund type: Consumer Defensive
What it holds: P/E 23.91 | P/B 4.44 | P/S 1.29 | 3y earnings growth n/a
Yield: 2.7%
Three-year record: +10.7% a year | beta to the market 0.48
Cost and size: expense ratio 0.08% | net assets 13.45B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Walmart Inc 10.5%, Costco Wholesale Corp 9.2%, Procter & Gamble Co 7.7%, Coca-Cola Co 7.6%, Philip Morris International Inc 6.8%
Sector mix: Consumer defensive 98.5%, Consumer cyclical 1.5%
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
Rolled up from the 5 largest holdings, 41.8% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.80 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +7.7% above the current prices
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
Shares outstanding: 210.17M | fund size: 17.72B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US electricity and water (XLU) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Neutral overall – no material macro surprise, flat fund flows, and technicals show no decisive breakout despite a positive analyst view.

**Main reasons it gave:**
- Flat fund flows (share count unchanged) indicating no net demand
- Technicals: price below 50‑day and 200‑day SMA, low volume, no decisive breakout
- Macro data unchanged: yields stable, no surprise in inflation or Fed policy

<details><summary><b>News</b> — score +0.00</summary>

- [ROTH’s top October ETFs: Semiconductor and technology funds lead Quant rankings](https://www.tradingview.com/news/seekingalpha:fbc1c95c1094b:0-roth-s-top-october-etfs-semiconductor-and-technology-funds-lead-quant-rankings/)  
  <sub>TradingView, 23 hours ago</sub>  
  ROTH's October ETF picks favor technology exposure, with semiconductor, technology and cloud-computing funds leading the list, while energy and large-cap...
- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  Find the latest State Street Health Care Select Sector SPDR ETF (XLV) stock quote, history, news and other vital information to help you with your stock...
- [XX ETF Bets on S&P 500 Hitting 10,000 by 2030. What If It Happens Early?](https://www.ebc.com/forex/xx-etf-sp500-10000-by-2030-early-target)  
  <sub>EBC Financial Group, 11 hours ago</sub>  
  XX ETF targets an S&P 500 level of 10000 by 2030. Learn why reaching it early won't guarantee a profit and what determines the fund's payoff.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.10</summary>

```text
Last close 41.53 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 40.49 (+2.6%), 50d 42.12 (-1.4%), 200d 44.32 (-6.3%); 50d below 200d
Momentum: RSI(14) 54.3 | MACD -0.237 vs signal -0.558 (histogram 0.321)
Returns: 1d -0.3% | 5d +0.9% | 1m -0.7% | 3m -8.2%
52-week range: 39.25 - 47.73 (now 26.8% of the way up)
Volatility: ATR(14) 0.62 (1.5% of price) | annualised 20d 17.0%
Volume: 0.29x the 20-day average
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
Three-year record: +16.1% a year | beta to the market 0.40
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

<details><summary><b>What analysts and big funds say</b> — score +0.60</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.60</summary>

```text
Rolled up from the 5 largest holdings, 39.5% of the fund by weight
Ratings by weight: buy 80.6% | hold 19.4% | sell 0.0% (mean 2.01 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.7% above the current prices
Holdings read: NEE, SO, DUK, CEG, AEP
Recent rating changes among them:
  - NEE: 2026-10-06 Mizuho: main, Neutral -> Neutral
  - SO: 2026-10-13 Keybanc: main, Underweight -> Underweight
  - DUK: 2026-10-13 Keybanc: main, Overweight -> Overweight
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
Shares outstanding: 163.27M | fund size: 6.78B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US health care (XLV) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:** no explanation. It wrote only “NEUTRAL”, so the main reasons below are all it gave.

**Main reasons it gave:**
- Share count down 3.9% (‑$1.76B) in the past week indicating net outflows
- Analyst ratings: 100% buy on top holdings (44.3% weight) with a +12.2% price target
- Price above 20‑day, 50‑day, and 200‑day SMAs; MACD positive but volume only 0.36× 20‑day average
- Treasury yields stable; no policy surprise; VIX low at 15.2, indicating calm macro backdrop

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Health Care Select Sector SPDR ETF (XLV) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLV/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  State Street Health Care Select Sector SPDR ETF (XLV) · 1.72% · 2.79% · 14.87% · 9.80% · 19.74% · 35.39% · 585.02%. Key Events. Baseline. Advanced Chart.
- [Quant Spotlight: Top and bottom healthcare stocks ahead of Q3](https://seekingalpha.com/news/4651978-seeking-alpha-s-quant-spotlight-highest-and-lowest-rated-healthcare-stocks-ahead-of-q3)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  As the Q3 earnings season gets underway, healthcare investors are evaluating sector constituents through Seeking Alpha's quantitative framework.
- [Health Care Stocks Rose Even As Biotech Slipped](https://finimize.com/content/health-care-stocks-rose-even-as-biotech-slipped)  
  <sub>Finimize, 19 hours ago</sub>  
  Steris' $2.1 billion Xodus deal and a JPMorgan upgrade for Biogen helped lift XLV, while iShares Biotechnology ETF fell 1.2%.
- [UnitedHealth Rises 4% on Earnings Beat and Raised Full-Year Outlook; Humana Advances 2%](https://247wallst.com/investing/2026/10/13/unitedhealth-rises-4-on-earnings-beat-and-raised-full-year-outlook-humana-advances-2/)  
  <sub>24/7 Wall St., 1 hour ago</sub>  
  UnitedHealth Group (NYSE:UNH | UNH Price Prediction) shares are up 4% to $395.19 after the health insurer topped Q3 2026 profit estimates and raised its...
- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Tuesday Amid Chip Weakness, Bank Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131042414.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.04% and the actively t.
- [AbbVie, Eli Lilly among mega-cap healthcare stocks with A+ profitability grades (XLV:NYSEARCA)](https://seekingalpha.com/news/4652382-abbvie-eli-lilly-among-mega-cap-healthcare-stocks-with-a-profitability-grades)  
  <sub>Seeking Alpha, 4 hours ago</sub>  
  Q3 earnings season watchlist: 7 mega-cap healthcare stocks with A+ profitability—ABBV, AMGN, JNJ, LLY, MRK, TMO, UNH.
- [SECA ETF Holdings List — CBOE:SECA](https://www.tradingview.com/symbols/CBOE-SECA/holdings/)  
  <sub>TradingView, 23 hours ago</sub>  
  Explore Main Active Rotation ETF holdings with weight, market value, and other helpful data to make more informed decisions for SECA trading.
- [Sector Update: Healthcare](https://finance.yahoo.com/healthcare/articles/sector-healthcare-170734567.html)  
  <sub>Yahoo Finance, 22 hours ago</sub>  
  Healthcare stocks rose Monday afternoon, with the NYSE Healthcare Index and the State Street Health Care Select Sector SPDR ETF (XLV) each adding 0.3%.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.00</summary>

```text
Last close 170.20 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 169.02 (+0.7%), 50d 169.26 (+0.6%), 200d 157.21 (+8.3%); 50d above 200d
Momentum: RSI(14) 53.8 | MACD 0.316 vs signal 0.073 (histogram 0.243)
Returns: 1d -1.0% | 5d +1.9% | 1m +1.5% | 3m +7.5%
52-week range: 141.95 - 175.68 (now 83.8% of the way up)
Volatility: ATR(14) 2.60 (1.5% of price) | annualised 20d 12.3%
Volume: 0.36x the 20-day average
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
Three-year record: +11.2% a year | beta to the market 0.52
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

<details><summary><b>What analysts and big funds say</b> — score +0.64</summary>

_Not available today._

</details>

<details><summary><b>What analysts say about what this fund holds</b> — score +0.64</summary>

```text
Rolled up from the 5 largest holdings, 44.3% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.72 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +12.2% above the current prices
Holdings read: LLY, JNJ, ABBV, MRK, UNH
Recent rating changes among them:
  - LLY: 2026-10-12 RBC Capital: reit, Outperform -> Outperform
  - JNJ: 2026-10-07 Guggenheim: reit, Buy -> Buy
  - ABBV: 2026-10-13 RBC Capital: reit, Outperform -> Outperform
  - MRK: 2026-10-12 Citigroup: main, Neutral -> Neutral
  - UNH: 2026-10-09 TD Cowen: main, Hold -> Hold
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
Direction: money going out (1 week)
Share count change: 1 week: -3.9% (-1.76B) over 7d
Shares outstanding: 254.05M | fund size: 43.24B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US shopping and leisure (XLY) · Sector or country — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> Mixed signals: strong analyst buy rating and price target, but net outflows of -8.8% and technical downtrend with rising yields suggest bearish pressure. No clear macro surprise or decisive technical break, so overall neutral.

**Main reasons it gave:**
- Fund flows show net redemptions of -8.8% over the past week
- Analyst coverage of top holdings is 100% buy with a +19.8% price target
- Technical indicators show price below 50‑day and 200‑day SMA, indicating a downtrend
- Rising Treasury yields (10‑year at 5.22%) and a 6% yield warning suggest rotation to bonds
- War‑driven inflation and higher oil prices squeeze consumer discretionary spending

<details><summary><b>News</b> — score +0.00</summary>

- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo! Finance Canada, 19 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 1.68% · -0.61% · -0.55% · -5.98% · -1.84% · 22.48% · 787.07%. Key...
- [State Street Consumer Discretionary Select Sector SPDR ETF (XLY) stock price, news, quote and history](https://sg.finance.yahoo.com/quote/XLY/)  
  <sub>Yahoo Finance Singapore, 16 hours ago</sub>  
  State Street Consumer Discretionary Select Sector SPDR ETF (XLY) · 1.68% · -0.61% · -0.55% · -5.98% · -1.84% · 22.48% · 787.07%. Key...
- [Charlie Bilello Says Iran War Inflation Is 'Rewarding Big Oil,' Flags a 56% Spread Between XLE and XLY](https://www.benzinga.com/etfs/sector-etfs/26/10/62316125/charlie-bilello-says-iran-war-inflation-is-rewarding-big-oil-flags-a-56-spread-between-xle-and-xly)  
  <sub>Benzinga, 5 hours ago</sub>  
  Iran war-driven inflation boosts oil stocks, with XLE up 50%, while soaring fuel and commodity prices squeeze consumers.
- [Quant rating of consumer discretionary stocks ahead of Q3 earnings (F:NYSE)](https://seekingalpha.com/news/4652113-quant-rating-of-consumer-discretionary-stocks-ahead-if-q3-earnings)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  The State Street Consumer Discretionary Sel Sect SPDR ETF (XLY) declined nearly 8% in the third calendar quarter of 2025, lagging the broader S&P500 index,...
- [Sector Update: Consumer Stocks Mixed Pre-Bell Monday](https://www.bitget.com/amp/news/detail/12560605946192)  
  <sub>Bitget, 23 hours ago</sub>  
  09:16 AM EDT, 10/12/2026 (MT Newswires) -- Consumer stocks were mixed premarket Monday, with the State Street Consumer Staples Select Sector SPDR ETF (XLP)...
- [6% Treasury Yield: Wall Street’s Iceberg Warning For Stocks - iShares 20+ Year Treasury Bond ETF (NASDAQ](https://www.benzinga.com/markets/bonds/26/10/62323584/6-percent-treasury-yield-iceberg-warning-fund-managers-stocks-bonds)  
  <sub>Benzinga, 1 hour ago</sub>  
  Fund managers told BofA a 6% 10-year Treasury yield would make them swap stocks for bonds. One in five say yields are already there.
- [Sector Update: Consumer Stocks Mixed Monday Afternoon](https://ca.finance.yahoo.com/news/sector-consumer-stocks-mixed-monday-174008437.html)  
  <sub>Yahoo! Finance Canada, 21 hours ago</sub>  
  Consumer stocks were mixed Monday afternoon, with the State Street Consumer Staples Select Sector SPDR ETF (XLP) increasing 0.8% and the State Street...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score -0.20</summary>

```text
Last close 112.27 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 110.86 (+1.3%), 50d 114.22 (-1.7%), 200d 116.02 (-3.2%); 50d below 200d
Momentum: RSI(14) 51.7 | MACD -0.439 vs signal -0.929 (histogram 0.490)
Returns: 1d +0.0% | 5d +0.5% | 1m -0.5% | 3m -4.0%
52-week range: 105.66 - 124.52 (now 35.0% of the way up)
Volatility: ATR(14) 1.34 (1.2% of price) | annualised 20d 12.4%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score -0.20</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score -0.20</summary>

```text
Fund type: Consumer Cyclical
What it holds: P/E 24.00 | P/B 5.56 | P/S 2.32 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +12.9% a year | beta to the market 1.18
Cost and size: expense ratio 0.08% | net assets 21.27B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Amazon.com Inc 23.4%, Tesla Inc 17.7%, The Home Depot Inc 5.0%, McDonald's Corp 4.2%, TJX Companies Inc 4.1%
Sector mix: Consumer cyclical 98.7%, Technology 1.3%
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
Rolled up from the 5 largest holdings, 54.4% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.79 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.8% above the current prices
Holdings read: AMZN, TSLA, HD, MCD, TJX
Recent rating changes among them:
  - AMZN: 2026-10-12 Wells Fargo: main, Overweight -> Overweight
  - TSLA: 2026-10-12 Jefferies: main, Hold -> Hold
  - HD: 2026-09-09 Bernstein: main, Market Perform -> Market Perform
  - MCD: 2026-10-08 Bernstein: main, Market Perform -> Market Perform
  - TJX: 2026-08-26 Jefferies: down, Buy -> Hold
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
Direction: money going out (1 week)
Share count change: 1 week: -8.8% (-2.05B) over 7d
Shares outstanding: 188.50M | fund size: 21.16B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Argentina (ARGT) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 89.58 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 89.22 (+0.4%), 50d 92.04 (-2.7%), 200d 92.51 (-3.2%); 50d below 200d
Momentum: RSI(14) 48.1 | MACD -1.226 vs signal -1.533 (histogram 0.306)
Returns: 1d +0.4% | 5d -0.1% | 1m -6.1% | 3m -6.1%
52-week range: 70.49 - 102.94 (now 58.8% of the way up)
Volatility: ATR(14) 1.76 (2.0% of price) | annualised 20d 28.6%
Volume: 0.27x the 20-day average
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.73 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +30.1% above the current prices
Holdings read: MELI, YPF, VIST, GGAL, PAM
Recent rating changes among them:
  - MELI: 2026-10-12 Cantor Fitzgerald: main, Overweight -> Overweight
  - YPF: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - VIST: 2026-09-01 JP Morgan: main, Overweight -> Overweight
  - GGAL: 2026-06-25 JP Morgan: main, Overweight -> Overweight
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
Share count change: 1 week: -15.6% (-134.70M) over 7d
Shares outstanding: 8.13M | fund size: 728.53M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Poland (EPOL) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 44.33 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 44.27 (+0.2%), 50d 44.37 (-0.1%), 200d 39.84 (+11.3%); 50d above 200d
Momentum: RSI(14) 51.6 | MACD -0.129 vs signal -0.080 (histogram -0.049)
Returns: 1d +0.9% | 5d -0.4% | 1m -1.8% | 3m +8.0%
52-week range: 32.22 - 45.76 (now 89.5% of the way up)
Volatility: ATR(14) 0.65 (1.5% of price) | annualised 20d 22.4%
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
Three-year record: +42.9% a year | beta to the market 0.64
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
Weighted price target: +1.3% above the current prices
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
Share count change: 1 week: -3.7% (-32.14M) over 7d
Shares outstanding: 19.01M | fund size: 843.02M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Australia (EWA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [RBA September Minutes: Unanimous 25bps rate hike to 4.6%, hawkish stance maintained](https://seekingalpha.com/news/4652306-rba-september-minutes-unanimous-25bps-rate-hike-to-46-hawkish-stance-maintained)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  Minutes from the Reserve Bank of Australia's ((RBA)) September meeting revealed a unanimous decision to raise the cash rate by 25 basis points to 4.6%,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 28.77 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 28.53 (+0.8%), 50d 29.33 (-1.9%), 200d 28.72 (+0.2%); 50d above 200d
Momentum: RSI(14) 50.2 | MACD -0.202 vs signal -0.278 (histogram 0.075)
Returns: 1d +0.3% | 5d +0.8% | 1m -1.0% | 3m -0.1%
52-week range: 24.95 - 30.43 (now 69.7% of the way up)
Volatility: ATR(14) 0.33 (1.2% of price) | annualised 20d 17.4%
Volume: 0.08x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 20.31 | P/B 2.65 | P/S 3.31 | 3y earnings growth n/a
Yield: 3.0%
Three-year record: +13.9% a year | beta to the market 0.98
Cost and size: expense ratio 0.50% | net assets 1.21B
What it is made of: Stocks 99.2%, Cash 0.8%
Largest holdings: BHP Group Ltd 15.4%, Commonwealth Bank of Australia 12.6%, National Australia Bank Ltd 6.1%, Westpac Banking Corp 6.0%, ANZ Group Holdings Ltd 5.8%
Sector mix: Financial services 42.0%, Basic materials 25.4%, Consumer cyclical 6.5%, Healthcare 5.6%
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
Rolled up from the 5 largest holdings, 45.9% of the fund by weight
Ratings by weight: buy 0.0% | hold 59.5% | sell 40.5% (mean 3.41 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -7.5% above the current prices
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

```text
Direction: money going out (1 week)
Share count change: 1 week: -10.2% (-138.46M) over 7d
Shares outstanding: 42.31M | fund size: 1.22B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Taiwan (EWT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Stocktwits Passport Portfolio: QQQ Weekly Rally Leaves SPY, DIA And Asia In The Dust](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-qqq-weekly-rally-leaves-spy-dia-and-asia-in-the-dust/cZMazMoRBaW)  
  <sub>Stocktwits, 21 hours ago</sub>  
  The tech-heavy Nasdaq index surged past its American and Asian counterparts as AI stayed in focus this week.
- [Sun Life Financial INC Acquires 780,000 Shares of Ares Dynamic C](https://www.gurufocus.com/news/9120339/sun-life-financial-inc-acquires-780000-shares-of-ares-dynamic-credit-allocation-fund-inc-ardc-stock-trades-33-below-gf-value)  
  <sub>GuruFocus, 6 hours ago</sub>  
  A New Position in a Credit-Focused Closed-End Fund On 2026-09-14, Toronto-based Sun Life Financial INC (Trades, Portfolio) executed a Buy action on Ares...
- [Stocktwits Passport Portfolio: Wall Street Outpaces Asia As AI Trade Wobbles And Bond Yields Climb](https://stocktwits.com/news-articles/markets/equity/stocktwits-passport-portfolio-wall-street-outpaces-asia-as-ai-trade-wobbles-and-bond-yields-climb/cZD60nORBVY)  
  <sub>Stocktwits, 15 hours ago</sub>  
  The S&P 500 and Dow Jones Industrial Average are headed for marginal gains this week, even as South Korea, Japan, and Taiwan are poised to end lower.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 112.80 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 113.93 (-1.0%), 50d 109.56 (+3.0%), 200d 90.62 (+24.5%); 50d above 200d
Momentum: RSI(14) 50.4 | MACD 1.468 vs signal 1.925 (histogram -0.457)
Returns: 1d -1.3% | 5d -4.1% | 1m +5.2% | 3m +10.1%
52-week range: 60.03 - 118.00 (now 91.0% of the way up)
Volatility: ATR(14) 2.13 (1.9% of price) | annualised 20d 25.8%
Volume: 0.32x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Greater China Region
What it holds: P/E 28.15 | P/B 4.48 | P/S 2.64 | 3y earnings growth n/a
Yield: 0.9%
Three-year record: +45.2% a year | beta to the market 1.26
Cost and size: expense ratio 0.59% | net assets 12.34B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: Taiwan Semiconductor Manufacturing Co Ltd 21.9%, MediaTek Inc 7.2%, Delta Electronics Inc 3.9%, Hon Hai Precision Industry Co Ltd 3.2%, ASE Technology Holding Co Ltd 3.0%
Sector mix: Technology 74.2%, Financial services 14.3%, Basic materials 3.8%, Industrials 2.8%
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
Rolled up from the 5 largest holdings, 39.1% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.35 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +33.1% above the current prices
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
Share count change: 1 week: +6.4% (734.08M) over 7d
Shares outstanding: 107.68M | fund size: 12.15B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### United Kingdom (EWU) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 46.83 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 46.85 (-0.1%), 50d 47.77 (-2.0%), 200d 46.78 (+0.1%); 50d above 200d
Momentum: RSI(14) 47.3 | MACD -0.378 vs signal -0.420 (histogram 0.042)
Returns: 1d +0.3% | 5d +1.0% | 1m -2.3% | 3m +0.1%
52-week range: 41.34 - 49.39 (now 68.2% of the way up)
Volatility: ATR(14) 0.46 (1.0% of price) | annualised 20d 12.3%
Volume: 0.24x the 20-day average
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
Weighted price target: +15.0% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -3.7% (-143.61M) over 7d
Shares outstanding: 79.11M | fund size: 3.70B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Mexico (EWW) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 73.27 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 72.54 (+1.0%), 50d 74.75 (-2.0%), 200d 75.90 (-3.5%); 50d below 200d
Momentum: RSI(14) 50.4 | MACD -0.690 vs signal -0.933 (histogram 0.242)
Returns: 1d +0.0% | 5d +0.8% | 1m -2.1% | 3m -2.8%
52-week range: 64.84 - 81.23 (now 51.4% of the way up)
Volatility: ATR(14) 1.26 (1.7% of price) | annualised 20d 20.6%
Volume: 0.21x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Focused Region
What it holds: P/E 12.17 | P/B 1.90 | P/S 1.42 | 3y earnings growth n/a
Yield: 3.5%
Three-year record: +13.8% a year | beta to the market 1.07
Cost and size: expense ratio 0.50% | net assets 1.49B
What it is made of: Stocks 99.4%, Cash 0.6%
Largest holdings: Grupo Mexico SAB de CV Class B 16.4%, Grupo Financiero Banorte SAB de CV Class O 11.1%, Fomento Economico Mexicano SAB de CV Units Cons. Of 1 Shs-B- And 4 Shs-D- 8.8%, America Movil SAB de CV Ordinary Shares - Class B 7.2%, Wal - Mart de Mexico SAB de CV 4.4%
Sector mix: Basic materials 26.8%, Consumer defensive 24.8%, Financial services 19.5%, Industrials 12.1%
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
Rolled up from the 5 largest holdings, 47.8% of the fund by weight
Ratings by weight: buy 90.9% | hold 9.1% | sell 0.0% (mean 2.16 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +10.1% above the current prices
Holdings read: GMEXICOB.MX, GFNORTEO.MX, FEMSAUBD.MX, AMXB.MX, WALMEX.MX
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

```text
Direction: flat (1 week)
Share count change: 1 week: +0.0% (0.00) over 7d
Shares outstanding: 18.90M | fund size: 1.38B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Brazil (EWZ) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [ETF Inflows Top $41B as Investors Pile Into Brazil, Long Bonds](https://www.etf.com/sections/weekly-etf-flows/etf-inflows-top-41b-investors-pile-brazil-long-bonds)  
  <sub>ETF.com, 22 hours ago</sub>  
  Investors added $41.6 billion to US-listed ETFs during the week ending Friday, Oct. 9. That brought year-to-date inflows to just shy of $1.6 trillion,...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 43.03 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 39.32 (+9.4%), 50d 37.31 (+15.4%), 200d 36.79 (+17.0%); 50d above 200d
Momentum: RSI(14) 71.8 | MACD 1.719 vs signal 1.215 (histogram 0.504)
Returns: 1d -1.2% | 5d +0.1% | 1m +14.1% | 3m +19.9%
52-week range: 29.10 - 43.54 (now 96.5% of the way up)
Volatility: ATR(14) 1.03 (2.4% of price) | annualised 20d 49.3%
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
Three-year record: +20.3% a year | beta to the market 0.83
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
Weighted price target: +14.2% above the current prices
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
Shares outstanding: 200.55M | fund size: 8.63B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold mining companies (GDX) · Sector or country — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 15 hours ago</sub>  
  The fund normally invests at least 80% of its total assets in securities that comprise the fund's benchmark index. The index is a modified capitalization...
- [GDXJ Stock Price, Quote & News](https://www.syfe.com/stocks/us/gdxj)  
  <sub>Syfe, 20 hours ago</sub>  
  Get the latest VanEck Junior Gold Miners ETF (GDXJ) stock price, key stats and news. Track & Trade GDXJ with $0 commission on Syfe.
- [The Big Picture For Gold And Silver Could Not Be More Positive](https://seekingalpha.com/article/4953600-the-big-picture-for-gold-and-silver-could-not-be-more-positive)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  On gold's very long-term chart, stretching back to about 1981, its great 1970s bull market was followed by a severe Stage 4 bear market lasting until about...
- [Nasdaq 100 Drops, SanDisk Tumbles 6% as AI Trade Falters: Stock Market Today](https://www.tradingview.com/news/benzinga:655132fc6094b:0-nasdaq-100-drops-sandisk-tumbles-6-as-ai-trade-falters-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were mixed at midday Monday as a selloff in AI-infrastructure names dragged the Nasdaq 100 and small caps lower, while the Dow edged higher and...
- [VanEck UCITS ETFs Plc - Net Asset Value(s)](https://uk.finance.yahoo.com/news/vaneck-ucits-etfs-plc-net-060000210.html)  
  <sub>Yahoo Finance UK, 9 hours ago</sub>  
  Fund Name. NAV Date. Ticker Symbol. ISIN. Shares in Issue. Net Asset Value. NAV per Share. VanEck Emerging Markets High Yield Bond UCITS ETF. 2026-10-12.
- [BofA analysts see gold unable to hold above $4,000 over next three months (GLD:NYSEARCA)](https://seekingalpha.com/news/4652282-bofa-analysts-see-gold-unable-to-hold-above-4000-over-next-three-months)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Despite steady investment demand, Bank of America said it remains cautious on gold prices as physical demand remains weak, seeing prices unable to hold...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 87.32 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 90.37 (-3.4%), 50d 93.18 (-6.3%), 200d 91.08 (-4.1%); 50d above 200d
Momentum: RSI(14) 43.1 | MACD -1.758 vs signal -1.520 (histogram -0.238)
Returns: 1d -1.4% | 5d -1.0% | 1m -7.2% | 3m +18.0%
52-week range: 68.28 - 115.84 (now 40.0% of the way up)
Volatility: ATR(14) 2.79 (3.2% of price) | annualised 20d 37.5%
Volume: 0.21x the 20-day average
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
Three-year record: +49.7% a year | beta to the market 0.81
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
Weighted price target: +17.9% above the current prices
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
Share count change: 1 week: -15.4% (-4.68B) over 7d
Shares outstanding: 295.03M | fund size: 25.76B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Transport and delivery (IYT) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [The Cass Index signals a minor freight rebound even as economic headwinds remain (XTN:NYSEARCA)](https://seekingalpha.com/news/4652459-the-cass-index-signals-minor-freight-rebound-even-as-economic-headwinds-remain)  
  <sub>Seeking Alpha, 1 hour ago</sub>  
  The September 2026 Cass Transportation Index Report indicates signs of a developing freight market recovery, with shipment volumes rising for the second...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 79.46 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 79.68 (-0.3%), 50d 83.16 (-4.5%), 200d 81.42 (-2.4%); 50d above 200d
Momentum: RSI(14) 41.3 | MACD -0.905 vs signal -1.172 (histogram 0.267)
Returns: 1d -0.7% | 5d -0.3% | 1m -3.8% | 3m -9.2%
52-week range: 68.14 - 90.01 (now 51.8% of the way up)
Volatility: ATR(14) 1.07 (1.4% of price) | annualised 20d 13.9%
Volume: 0.16x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Industrials
What it holds: P/E 18.90 | P/B 3.94 | P/S 1.34 | 3y earnings growth n/a
Yield: 1.0%
Three-year record: +12.6% a year | beta to the market 1.32
Cost and size: expense ratio 0.37% | net assets 1.88B
What it is made of: Stocks 99.9%, Cash 0.1%
Largest holdings: Union Pacific Corp 17.4%, Uber Technologies Inc 15.1%, CSX Corp 9.3%, Delta Air Lines Inc 4.9%, United Airlines Holdings Inc 4.8%
Sector mix: Industrials 84.1%, Technology 15.9%
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
Rolled up from the 5 largest holdings, 51.6% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.64 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +27.1% above the current prices
Holdings read: UNP, UBER, CSX, DAL, UAL
Recent rating changes among them:
  - UNP: 2026-10-07 Citigroup: main, Buy -> Buy
  - UBER: 2026-10-12 Cantor Fitzgerald: reit, Overweight -> Overweight
  - CSX: 2026-10-07 Citigroup: main, Neutral -> Neutral
  - DAL: 2026-10-12 UBS: main, Buy -> Buy
  - UAL: 2026-10-07 Susquehanna: main, Positive -> Positive
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
Share count change: 1 week: -14.4% (-315.23M) over 7d
Shares outstanding: 23.51M | fund size: 1.87B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Saudi Arabia (KSA) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 3 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Behavioral Patterns of KSA and Institutional Flows](https://news.stocktradersdaily.com/news_release/14/Behavioral_Patterns_of_KSA_and_Institutional_Flows_101226095401_1791856441.html)  
  <sub>Stock Traders Daily, 17 hours ago</sub>  
  Key findings for Ishares Msci Saudi Arabia Etf (NYSE: KSA). Weak Near-Term Sentiment Could Catalyze Bearish Positioning; No clear price positioning signal...
- [Oil Prices Diverge As Traders Weigh Russian Diesel Relief Against Saudi Supply Risks: USO, UCO, In Focus](https://www.tradingview.com/news/stocktwits:148c484a2094b:0-oil-prices-diverge-as-traders-weigh-russian-diesel-relief-against-saudi-supply-risks-uso-uco-in-focus/)  
  <sub>TradingView, 6 hours ago</sub>  
  Oil prices mostly declined Tuesday as traders continued to assess the risks to energy supplies from Houthi attacks on Saudi Arabia and the potential impact...
- [China’s 4F² Threat to Micron—Houthis' Deadly Attack On Saudi Arabia Eclipses Trump’s Russian Diesel Deal](https://www.benzinga.com/Opinion/26/10/62308565/chinas-4f%C2%B2-threat-to-micron-houthis-deadly-attack-on-saudi-arabia-eclipses-trumps-russian-diesel-deal?utm_source=googlefinance)  
  <sub>Benzinga, 21 hours ago</sub>  
  Advance In Memory Chips Please click here for an enlarged chart of United States Oil ETF (NYSE:USO). Note the following: The chart shows oil ETF USO moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 35.79 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 36.68 (-2.4%), 50d 37.64 (-4.9%), 200d 38.11 (-6.1%); 50d below 200d
Momentum: RSI(14) 32.0 | MACD -0.504 vs signal -0.439 (histogram -0.064)
Returns: 1d +0.4% | 5d -3.0% | 1m -5.3% | 3m -3.2%
52-week range: 35.66 - 41.03 (now 2.4% of the way up)
Volatility: ATR(14) 0.32 (0.9% of price) | annualised 20d 11.8%
Volume: 0.33x the 20-day average
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
Three-year record: +1.8% a year | beta to the market 0.19
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
Ratings by weight: buy 90.3% | hold 9.7% | sell 0.0% (mean 2.08 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +19.4% above the current prices
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
Direction: money going out (1 week)
Share count change: 1 week: -7.5% (-47.21M) over 7d
Shares outstanding: 16.29M | fund size: 583.20M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US real estate (VNQ) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: The read operation timed out (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Franklin BSP Realty Trust PFD Series E Rates A Sell (Retired Investor) (NYSE:FBRT)](https://seekingalpha.com/mp/1026-ireit-hoya-capital/articles/6349040-franklin-bsp-realty-trust-pfd-series-e-rates-a-sell-retired-investor)  
  <sub>Seeking Alpha, 24 hours ago</sub>  
  With the FOMC recent rate increase, many preferred stocks have suffered double digits losses since the summer as illustrated by the decline in the Vanguard.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 90.79 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 91.03 (-0.3%), 50d 94.71 (-4.1%), 200d 94.41 (-3.8%); 50d above 200d
Momentum: RSI(14) 43.2 | MACD -1.333 vs signal -1.625 (histogram 0.291)
Returns: 1d -0.6% | 5d +1.0% | 1m -3.8% | 3m -7.2%
52-week range: 87.00 - 100.95 (now 27.2% of the way up)
Volatility: ATR(14) 1.22 (1.3% of price) | annualised 20d 14.3%
Volume: 0.21x the 20-day average
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
Three-year record: +10.7% a year | beta to the market 0.98
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
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 1.69 on a 1=strong buy to 5=strong sell scale)
Weighted price target: +17.5% above the current prices
Holdings read: VRTPX, WELL, PLD, EQIX, AMT
Recent rating changes among them:
  - WELL: 2024-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - PLD: 2026-09-01 Wells Fargo: main, Overweight -> Overweight
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
Direction: money going out (1 week)
Share count change: 1 week: -7.4% (-5.34B) over 7d
Shares outstanding: 732.60M | fund size: 66.51B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### US energy companies (XLE) · Sector or country — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 2 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Exchange-Traded Funds Lower, Equity Futures Mixed Pre-Bell Tuesday Amid Chip Weakness, Bank Earnings](https://finance.yahoo.com/markets/stocks/articles/exchange-traded-funds-lower-equity-131042414.html)  
  <sub>Yahoo Finance, 2 hours ago</sub>  
  The broad market exchange-traded fund SPDR S&P 500 ETF Trust (SPY) was down 0.04% and the actively t.
- [ValuEngine Weekly Commentary With Strategy Notes](https://seekingalpha.com/article/4953759-valuengine-weekly-commentary-strategy-notes)  
  <sub>Seeking Alpha, 2 hours ago</sub>  
  U.S. equity markets were mixed this week, with broader gains across value, defensive, and cyclical sectors offset by weakness in technology and the NASDAQ...
- [State Street's Energy ETF offers 18.5% yield wi...](https://pluang.com/en/news-feed/xlei-etf-dividen-tinggi-unik-18-persen)  
  <sub>Pluang, 9 hours ago</sub>  
  The State Street Energy Select Sector SPDR Premium Income ETF (XLEI) provides investors exposure to the energy sector with a high 18.5% trailing twelve...
- [Charlie Bilello Says Iran War Inflation Is 'Rewarding Big Oil,' Flags a 56% Spread Between XLE and XLY](https://www.benzinga.com/etfs/sector-etfs/26/10/62316125/charlie-bilello-says-iran-war-inflation-is-rewarding-big-oil-flags-a-56-spread-between-xle-and-xly)  
  <sub>Benzinga, 5 hours ago</sub>  
  Iran war-driven inflation boosts oil stocks, with XLE up 50%, while soaring fuel and commodity prices squeeze consumers.
- [Sector Update: Energy Stocks Edge Higher Premarket Tuesday](https://ca.finance.yahoo.com/news/sector-energy-stocks-edge-higher-132219561.html)  
  <sub>Yahoo! Finance Canada, 1 hour ago</sub>  
  Energy stocks were edging higher premarket Tuesday, with the State Street Energy Select Sector SPDR ETF (XLE) advancing by 0.7%.
- [XLEI: A Unique 18% Yield](https://seekingalpha.com/article/4953638-xlei-a-unique-18-percent-yield)  
  <sub>Seeking Alpha, 10 hours ago</sub>  
  The State Street Energy Select Sector SPDR Premium Income ETF offers a unique blend of energy sector exposure and a high 18.5% TTM yield. XLEI tracks XLE...
- [9 Of 11 Sectors Rise Monday As Cyclicals Lead](https://www.benzinga.com/etfs/sector-etfs/26/10/62302120/9-of-11-sectors-rise-monday-as-cyclicals-lead)  
  <sub>Benzinga, 24 hours ago</sub>  
  Nine of 11 sectors are higher in Monday's regular session, with cyclical sectors holding two of the top three positions. The leaders are separated rather...
- [Nasdaq 100 Drops, SanDisk Tumbles 6% as AI Trade Falters: Stock Market Today](https://www.tradingview.com/news/benzinga:655132fc6094b:0-nasdaq-100-drops-sandisk-tumbles-6-as-ai-trade-falters-stock-market-today/)  
  <sub>TradingView, 22 hours ago</sub>  
  U.S. stocks were mixed at midday Monday as a selloff in AI-infrastructure names dragged the Nasdaq 100 and small caps lower, while the Dow edged higher and...
- [Sector Update: Energy Stocks Gain Late Afternoon](https://finance.yahoo.com/energy/articles/sector-energy-stocks-gain-afternoon-195743000.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks were higher late Monday afternoon, with the NYSE Energy Sector Index and the State Street Energy Select Sector SPDR ETF (XLE) each adding 1.3%...
- [Sector Update: Energy](https://finance.yahoo.com/energy/articles/sector-energy-193724317.html)  
  <sub>Yahoo Finance, 19 hours ago</sub>  
  Energy stocks were higher late Monday afternoon, with the NYSE Energy Sector Index and the State Street Energy Select Sector SPDR ETF (XLE) each adding 1.3%...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 66.82 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 63.42 (+5.4%), 50d 62.96 (+6.1%), 200d 57.27 (+16.7%); 50d above 200d
Momentum: RSI(14) 68.5 | MACD 0.713 vs signal 0.331 (histogram 0.382)
Returns: 1d +1.2% | 5d +4.8% | 1m +3.5% | 3m +18.3%
52-week range: 42.64 - 66.82 (now 100.0% of the way up)
Volatility: ATR(14) 1.27 (1.9% of price) | annualised 20d 22.7%
Volume: 0.28x the 20-day average
```

</details>

<details><summary><b>Company numbers</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>What this fund holds</b> — score n/a</summary>

```text
Fund type: Equity Energy
What it holds: P/E 17.51 | P/B 2.47 | P/S 1.70 | 3y earnings growth n/a
Yield: 2.5%
Three-year record: +17.3% a year | beta to the market -0.03
Cost and size: expense ratio 0.08% | net assets 39.13B
What it is made of: Stocks 99.8%, Cash 0.2%
Largest holdings: ExxonMobil Holdings Corp 24.0%, Chevron Corp 18.1%, ConocoPhillips 6.7%, Valero Energy Corp 4.7%, Marathon Petroleum Corp 4.7%
Sector mix: Energy 100.0%
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
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
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

```text
Rolled up from the 5 largest holdings, 58.2% of the fund by weight
Ratings by weight: buy 100.0% | hold 0.0% | sell 0.0% (mean 2.12 on a 1=strong buy to 5=strong sell scale)
Weighted price target: -0.1% above the current prices
Holdings read: XOM, CVX, COP, VLO, MPC
Recent rating changes among them:
  - XOM: 2026-10-01 Wells Fargo: down, Overweight -> Equal-Weight
  - CVX: 2026-10-12 TD Cowen: main, Hold -> Hold
  - COP: 2026-10-07 Jefferies: main, Buy -> Buy
  - VLO: 2026-10-12 Evercore ISI Group: main, In-Line -> In-Line
  - MPC: 2026-10-12 Barclays: main, Overweight -> Overweight
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
Shares outstanding: 186.42M | fund size: 12.46B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

## Commodities

### Copper (CPER) · Commodity — NEUTRAL, confidence 0.00

**Result:** REJECTED · bias is NEUTRAL; no trade

**In the model's own words:**

> No material macro surprise, technicals bullish but low volume, heavy roll cost and outflows weigh against a bullish stance.

**Main reasons it gave:**
- Fund flows: -7% share count (outflows) over 1 week
- Positioning: net long 20.1% of OI, down 5.8% week
- Cost of holding: -5.4% annual roll cost
- Technicals: price 40.47 above 20d SMA (40.07) and 200d SMA (37.67) but volume 0.11x 20‑day average
- Macro: no surprise in inflation, unemployment, or rates; yields stable, USD up modestly

<details><summary><b>News</b> — score +0.00</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score +0.00</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score +0.20</summary>

```text
Last close 40.47 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 40.07 (+1.0%), 50d 39.94 (+1.3%), 200d 37.67 (+7.4%); 50d above 200d
Momentum: RSI(14) 55.0 | MACD 0.121 vs signal 0.077 (histogram 0.044)
Returns: 1d -0.4% | 5d +1.1% | 1m +5.8% | 3m +4.8%
52-week range: 30.53 - 41.43 (now 91.2% of the way up)
Volatility: ATR(14) 0.57 (1.4% of price) | annualised 20d 20.3%
Volume: 0.11x the 20-day average
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
Cost of holding this fund instead of copper itself: -5.4% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +4.8%, commodity +7.2%, gap -2.4% | 6 months: fund +8.6%, commodity +11.1%, gap -2.5% | 12 months: fund +33.7%, commodity +39.1%, gap -5.4%
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
Share count change: 1 week: -7.0% (-54.15M) over 7d
Shares outstanding: 17.74M | fund size: 718.19M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Sugar (CANE) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 12.39 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 11.61 (+6.7%), 50d 11.31 (+9.6%), 200d 10.07 (+23.0%); 50d above 200d
Momentum: RSI(14) 69.4 | MACD 0.298 vs signal 0.231 (histogram 0.068)
Returns: 1d +0.7% | 5d +1.1% | 1m +8.2% | 3m +26.3%
52-week range: 9.02 - 12.39 (now 100.0% of the way up)
Volatility: ATR(14) 0.21 (1.7% of price) | annualised 20d 24.2%
Volume: 0.31x the 20-day average
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
Cost of holding this fund instead of sugar itself: -10.7% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +26.3%, commodity +42.4%, gap -16.1% | 6 months: fund +31.0%, commodity +52.3%, gap -21.3% | 12 months: fund +20.6%, commodity +31.3%, gap -10.7%
A commodity fund holds futures, not sugar, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: SUGAR NO. 11 - ICE FUTURES U.S. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 21.8% of open interest (1,158,944 contracts)
Change on the week: +1.9% of open interest
Crowding: 100% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -10.3% (-6.32M) over 7d
Shares outstanding: 4.42M | fund size: 54.74M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

**Data that was missing** (counted as 0.00, never guessed):
- news unavailable: Bright Data returned an empty body with its 200; nothing to parse

### Corn (CORN) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [What to Watch Next After the USDA Gut-Punched Corn Prices Last Week](https://www.barchart.com/story/news/6252578/what-to-watch-next-after-the-usda-gut-punched-corn-prices-last-week)  
  <sub>Barchart.com, 20 hours ago</sub>  
  Corn prices were hit by a surprisingly bearish USDA report on Friday.
- [U.S. corn futures recoup slice of Friday's steep drop after USDA forecast larger crop](https://seekingalpha.com/news/4652289-us-corn-futures-recoup-slice-of-fridays-steep-drop-after-usda-forecast-larger-crop)  
  <sub>Seeking Alpha, 17 hours ago</sub>  
  US corn futures edged higher after the previous session's sharp decline in reaction to a surprise report from the USDA that forecast higher corn production...
- [CME Group (CME) Sets New Corn Futures Volume Record Amid Strong Agricultural Trading Growth](https://www.gurufocus.com/news/9120182/cme-group-cme-sets-new-corn-futures-volume-record-amid-strong-agricultural-trading-growth)  
  <sub>GuruFocus, 15 hours ago</sub>  
  On October 12, 2026, CME Group Inc (NASDAQ: CME) announced a new milestone for its Corn futures market, recording a daily volume high of 1206376 contracts...
- [Corn Gets a Dead Cat Bounce on Monday](https://www.barchart.com/story/news/6333801/corn-gets-a-dead-cat-bounce-on-monday)  
  <sub>Barchart.com, 17 hours ago</sub>  
  Corn futures posted steady to fractionally higher trade in deferred contracts on Monday, with front months posting 2 ½ to 3 ¼ cent gains for a dead cat...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 18.59 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 19.32 (-3.8%), 50d 19.19 (-3.1%), 200d 18.17 (+2.3%); 50d above 200d
Momentum: RSI(14) 37.7 | MACD -0.229 vs signal -0.099 (histogram -0.130)
Returns: 1d +0.7% | 5d -3.6% | 1m -7.1% | 3m +4.5%
52-week range: 16.47 - 20.29 (now 55.5% of the way up)
Volatility: ATR(14) 0.33 (1.8% of price) | annualised 20d 20.6%
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
Cost of holding this fund instead of corn itself: -10.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +4.5%, commodity +8.7%, gap -4.2% | 6 months: fund +4.7%, commodity +9.8%, gap -5.1% | 12 months: fund +7.5%, commodity +17.8%, gap -10.3%
A commodity fund holds futures, not corn, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

```text
Corn rated good or excellent: 54% of the US crop (week 40 of 2026)
Direction over 3 weeks: steady, -3 points
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
Contract: CORN - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 17.7% of open interest (1,859,993 contracts)
Change on the week: -2.8% of open interest
Crowding: 88% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -19.2% (-31.17M) over 7d
Shares outstanding: 7.06M | fund size: 131.25M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Gold (GLD) · Commodity — no answer, no confidence given

<details><summary><b>News</b> — score n/a</summary>

- [VanEck Gold Miners ETF (GDX) Stock Price, News, Quote & History](https://ca.finance.yahoo.com/quote/GDX/)  
  <sub>Yahoo! Finance Canada, 16 hours ago</sub>  
  Find the latest VanEck Gold Miners ETF (GDX) stock quote, history, news and other vital information to help you with your stock trading and investing.
- [September CPI Preview: The Print That Could Break the Fed's Pause](https://www.moomoo.com/community/feed/september-cpi-preview-the-print-that-could-break-the-fed-117433024380934)  
  <sub>Moomoo, 5 hours ago</sub>  
  September CPI lands Wednesday, October 14 at 8:30 a.m. ET — the first inflation read after Kevin Warsh's Fed pulled the trigger on its first hike sinc...
- [BofA analysts see gold unable to hold above $4,000 over next three months (GLD:NYSEARCA)](https://seekingalpha.com/news/4652282-bofa-analysts-see-gold-unable-to-hold-above-4000-over-next-three-months)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Despite steady investment demand, Bank of America said it remains cautious on gold prices as physical demand remains weak, seeing prices unable to hold...
- [South Korea's KOSPI, S&P 500, Gold Sink On US-Iran Tensions, But Bitcoin Holds $68K Floor](https://stocktwits.com/news-articles/markets/cryptocurrency/kospi-s-and-p-500-gold-sink-on-us-iran-tensions-but-bitcoin-holds/cZd9fmeRI5O)  
  <sub>Stocktwits, 8 hours ago</sub>  
  Bitcoin held above $68000 even as KOSPI dropped more than 10%, U.S. indices closed lower, and gold shed gains.
- [Gold futures long positions continue to decline, while ETF holdings hit record highs; what does this divergence signify?](https://www.moomoo.com/news/post/1001004282/gold-futures-long-positions-continue-to-decline-while-etf-holdings)  
  <sub>Moomoo, 8 hours ago</sub>  
  OnTuesday, October 13, spot gold prices are currently trading in a range of $4170 to $4190 per ounce, having posted a modest rebound last week but still...
- [Ameriprise sees Q3 S&P 500 EPS up 29.5%, leaving stocks little room for disappointment](https://www.bitget.com/amp/news/detail/12560605947774)  
  <sub>Bitget, 17 hours ago</sub>  
  Ameriprise flagged Q3 earnings season as a key test for year-end equities with the S&P 500 near records and yields above 5%.
- [Gold And Silver Recover - While Big Buyers Keep Accumulating](https://seekingalpha.com/article/4953543-gold-silver-recover-big-buyers-keep-accumulating)  
  <sub>Seeking Alpha, 22 hours ago</sub>  
  A softer inflation reading could ease expectations of further Fed tightening and help metals extend their recovery.
- [Bitcoin Could Rally to $94K, but First It Must Break Through This Key Price Zone](https://www.bitget.com/amp/news/detail/12560605948258)  
  <sub>Bitget, 18 hours ago</sub>  
  Crypto analyst Doctor Profit expects the world's largest crypto asset to resume its upward move soon, even though BTC failed to overcome $84000 on Mond...
- [The Big Picture For Gold And Silver Could Not Be More Positive](https://seekingalpha.com/article/4953600-the-big-picture-for-gold-and-silver-could-not-be-more-positive)  
  <sub>Seeking Alpha, 19 hours ago</sub>  
  On gold's very long-term chart, stretching back to about 1981, its great 1970s bull market was followed by a severe Stage 4 bear market lasting until about...
- [China’s 4F² Threat to Micron—Houthis' Deadly Attack On Saudi Arabia Eclipses Trump’s Russian Diesel Deal](https://www.benzinga.com/Opinion/26/10/62308565/chinas-4f%C2%B2-threat-to-micron-houthis-deadly-attack-on-saudi-arabia-eclipses-trumps-russian-diesel-deal?utm_source=googlefinance)  
  <sub>Benzinga, 21 hours ago</sub>  
  Advance In Memory Chips Please click here for an enlarged chart of United States Oil ETF (NYSE:USO). Note the following: The chart shows oil ETF USO moving...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 381.85 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 386.86 (-1.3%), 50d 397.44 (-3.9%), 200d 415.35 (-8.1%); 50d below 200d
Momentum: RSI(14) 43.7 | MACD -4.780 vs signal -4.812 (histogram 0.033)
Returns: 1d -0.1% | 5d -0.1% | 1m -2.8% | 3m +2.6%
52-week range: 362.32 - 495.90 (now 14.6% of the way up)
Volatility: ATR(14) 5.95 (1.6% of price) | annualised 20d 20.8%
Volume: 0.25x the 20-day average
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
Cost of holding this fund instead of gold itself: -1.4% a year -- a steady drag
Measured: 3 months: fund +2.6%, commodity +3.6%, gap -1.0% | 6 months: fund -14.2%, commodity -13.5%, gap -0.7% | 12 months: fund +3.4%, commodity +4.9%, gap -1.4%
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
Shares outstanding: 260.30M | fund size: 99.40B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Silver (SLV) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions unreachable: Server disconnected without sending a response. (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [Current price of silver as of Tuesday, Oct. 13, 2026](https://fortune.com/article/current-price-of-silver-10-13-2026/)  
  <sub>Fortune, 3 hours ago</sub>  
  If you're worried about increased inflation, adding precious metals like silver to your portfolio can be a smart choice.
- [September CPI Preview: The Print That Could Break the Fed's Pause](https://www.moomoo.com/community/feed/september-cpi-preview-the-print-that-could-break-the-fed-117433024380934)  
  <sub>Moomoo, 5 hours ago</sub>  
  September CPI lands Wednesday, October 14 at 8:30 a.m. ET — the first inflation read after Kevin Warsh's Fed pulled the trigger on its first hike sinc...
- [Silver Falls to $60. Is Now the Time to Load Up on the Precious Metal?](https://finance.yahoo.com/markets/commodities/articles/silver-falls-60-now-time-180602772.html)  
  <sub>Yahoo Finance, 21 hours ago</sub>  
  The iShares Silver Trust has made for a terrific long-term investment, generating returns of 160% in five years, but it's been struggling of late.
- [SILVERAXIS ETF Holdings List — BSE:SILVERAXIS](https://www.tradingview.com/symbols/BSE-SILVERAXIS/holdings/)  
  <sub>TradingView, 8 hours ago</sub>  
  Explore Axis Silver ETF holdings with weight, market value, and other helpful data to make more informed decisions for SILVERAXIS trading.
- [IT ETFs Surge Up to 3.92%; Gold, Silver ETFs Fall](https://hdfcsky.com/news/it-etfs-rise-3-5percent-as-gold-silver-defence-etfs-slip-liquid-funds-flat)  
  <sub>HDFC Sky, 8 hours ago</sub>  
  IT ETFs jumped up to 3.92% after TCS and HCLTech results, while 22 gold ETFs, all 19 silver ETFs and all three defence ETFs traded lower.
- [Gold (XAUUSD) & Silver Price Forecast: Can Gold Break $4,217 as Silver Eyes $61.72?](https://www.fxempire.com/forecasts/article/gold-xauusd-silver-price-forecast-can-gold-break-4217-as-silver-eyes-61-72-1637534)  
  <sub>FXEmpire, 8 hours ago</sub>  
  Gold holds above $4155 as Treasury yields ease ahead of U.S. CPI, while silver tests trendline resistance near $61.72 amid strong investment demand.
- [SIMILARITIES BETWEEN THE 1960–1980 PERIOD AND TODAY IN GOLD AND SILVER](https://www.barchart.com/story/news/6311852/similarities-between-the-1960-1980-period-and-today-in-gold-and-silver)  
  <sub>Barchart.com, 18 hours ago</sub>  
  The rise in commodities, particularly gold and silver, between 2024 and 2026 has led us to question whether a new commodity era has begun.
- [Silver faces a test of resilience](https://www.equiti.com/uae-en/news/global-macro-analysis/silver-faces-a-test-of-resilience/)  
  <sub>www.equiti.com, 3 hours ago</sub>  
  Silver enters Q4 caught between high US interest rates and a tightening physical market.
- [BofA analysts see gold unable to hold above $4,000 over next three months (GLD:NYSEARCA)](https://seekingalpha.com/news/4652282-bofa-analysts-see-gold-unable-to-hold-above-4000-over-next-three-months)  
  <sub>Seeking Alpha, 18 hours ago</sub>  
  Despite steady investment demand, Bank of America said it remains cautious on gold prices as physical demand remains weak, seeing prices unable to hold...
- [Gold, silver ETFs see sharp rise in inflows in September. Which metal should investors prefer now?](https://m.economictimes.com/mf/analysis/gold-silver-etfs-see-sharp-rise-in-inflows-in-september-which-metal-should-investors-prefer-now/articleshow/134908525.cms)  
  <sub>The Economic Times, 10 hours ago</sub>  
  In September, investor enthusiasm for gold and silver ETFs saw a notable increase, driven by ongoing market uncertainties and global tensions.

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 53.73 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 56.28 (-4.5%), 50d 58.01 (-7.4%), 200d 65.66 (-18.2%); 50d below 200d
Momentum: RSI(14) 39.9 | MACD -1.203 vs signal -1.001 (histogram -0.202)
Returns: 1d -1.1% | 5d -3.1% | 1m -5.5% | 3m +2.9%
52-week range: 42.40 - 105.60 (now 17.9% of the way up)
Volatility: ATR(14) 1.45 (2.7% of price) | annualised 20d 34.4%
Volume: 0.66x the 20-day average
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
Cost of holding this fund instead of silver itself: -9.3% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +2.9%, commodity +4.8%, gap -1.9% | 6 months: fund -25.4%, commodity -24.6%, gap -0.8% | 12 months: fund +18.3%, commodity +27.5%, gap -9.3%
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
Contract: SILVER - COMMODITY EXCHANGE INC. (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 7.2% of open interest (105,130 contracts)
Change on the week: +0.0% of open interest
Crowding: 15% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -12.4% (-4.19B) over 7d
Shares outstanding: 551.18M | fund size: 29.61B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Soybeans (SOYB) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 27.65 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 27.65 (-0.0%), 50d 26.94 (+2.6%), 200d 24.81 (+11.4%); 50d above 200d
Momentum: RSI(14) 54.6 | MACD 0.098 vs signal 0.159 (histogram -0.061)
Returns: 1d +0.7% | 5d -0.3% | 1m -0.1% | 3m +8.3%
52-week range: 21.56 - 28.14 (now 92.6% of the way up)
Volatility: ATR(14) 0.32 (1.2% of price) | annualised 20d 12.7%
Volume: 0.07x the 20-day average
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
Cost of holding this fund instead of soybeans itself: -0.3% a year -- close to nothing, as a physically backed fund should be
Measured: 3 months: fund +8.3%, commodity +7.7%, gap +0.7% | 6 months: fund +14.2%, commodity +11.8%, gap +2.4% | 12 months: fund +28.2%, commodity +28.6%, gap -0.3%
A commodity fund holds futures, not soybeans, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
```

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>How the crop is growing</b> — score n/a</summary>

```text
Soybeans rated good or excellent: 57% of the US crop (week 40 of 2026)
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

<details><summary><b>Buying and selling by company insiders</b> — score n/a</summary>

_Not available today._

</details>

<details><summary><b>Who is positioned how</b> — score n/a</summary>

```text
Contract: SOYBEANS - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 23.0% of open interest (1,121,298 contracts)
Change on the week: +0.4% of open interest
Crowding: 92% percentile over 52 weeks -- a crowded long by the standards of the past year
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -3.2% (-1.48M) over 7d
Shares outstanding: 1.65M | fund size: 45.56M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Natural gas (UNG) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [European natural gas hits highest in nearly four years on winter supply worries (UNG:NYSEARCA)](https://seekingalpha.com/news/4652494-european-natural-gas-hits-highest-in-nearly-four-years-on-winter-supply-worries)  
  <sub>Seeking Alpha, 10 minutes ago</sub>  
  European natural gas futures rose to their highest since December 2022, rising for a sixth straight day, as Middle East attacks threaten supplies and...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 11.14 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 10.71 (+4.1%), 50d 10.39 (+7.2%), 200d 11.31 (-1.5%); 50d below 200d
Momentum: RSI(14) 58.8 | MACD 0.143 vs signal 0.104 (histogram 0.039)
Returns: 1d +2.0% | 5d +3.7% | 1m +7.8% | 3m +5.6%
52-week range: 9.63 - 16.90 (now 20.8% of the way up)
Volatility: ATR(14) 0.35 (3.2% of price) | annualised 20d 45.0%
Volume: 0.25x the 20-day average
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
Cost of holding this fund instead of natural gas itself: -14.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund +5.6%, commodity +11.1%, gap -5.5% | 6 months: fund +5.5%, commodity +25.0%, gap -19.5% | 12 months: fund -9.7%, commodity +4.6%, gap -14.2%
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
Direction: money going out (1 week)
Share count change: 1 week: -25.5% (-157.44M) over 7d
Shares outstanding: 41.37M | fund size: 460.83M
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Oil (USO) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

- [United States Oil Fund, LP (USO) Options Chain - Yahoo Finance](https://ca.finance.yahoo.com/quote/USO/options/?date=1792540800&straddle=false&type=all)  
  <sub>Yahoo! Finance Canada, 10 hours ago</sub>  
  Contract Name, Last Trade Date (EDT), Strike, Last Price, Bid, Ask, Change, % Change, Volume, Open Interest, Implied Volatility...
- [United States Oil Fund LP (USO) Stock Price | Quotes & News](https://www.moomoo.com/stock/USO-US?chain_id=Name1K9-3FXPhg.1lcqbhg&global_content=%7B%22promote_id%22%3A13764%2C%22sub_promote_id%22%3A57%2C%22f%22%3A%22www.moomoo.com%2Fstock%2FMAR-US%22%7D)  
  <sub>Moomoo, 20 hours ago</sub>  
  Track the latest United States Oil Fund LP (USO) price, quotes, financial information, news, and analyst ratings on moomoo App for your ETF trading and...
- [Trump's Russia diesel deal will do little for U.S. prices, analysts say (USO:NYSEARCA)](https://seekingalpha.com/news/4652291-trumps-russia-diesel-deal-will-do-little-for-u-s-prices-analysts-say)  
  <sub>Seeking Alpha, 15 hours ago</sub>  
  President Trump's agreement with Russia to supply hundreds of thousands of tons of diesel is unlikely to significantly lower prices for American consumers,...
- [VLO Stock Heads For Best Year Since 1982 — Michael Burry Says It Has Become A ‘Huge Position’](https://stocktwits.com/news-articles/markets/equity/vlo-stock-best-year-1982-michael-burry-huge-position/cZtlx8lRBR0)  
  <sub>Stocktwits, 17 hours ago</sub>  
  Burry recovered his initial investment “and then some” for charity, while retaining a sizable stake that is “deep into house's money.”
- [China’s 4F² Threat to Micron—Houthis' Deadly Attack On Saudi Arabia Eclipses Trump’s Russian Diesel Deal](https://www.benzinga.com/Opinion/26/10/62308565/chinas-4f%C2%B2-threat-to-micron-houthis-deadly-attack-on-saudi-arabia-eclipses-trumps-russian-diesel-deal)  
  <sub>Benzinga, 21 hours ago</sub>  
  Advance In Memory Chips Please click here for an enlarged chart of United States Oil ETF (NYSE:USO). Note the following: The chart shows oil ETF USO moving...
- [Iran war has cost average U.S. household $2K, economist estimates (USO:NYSEARCA)](https://seekingalpha.com/news/4652203-iran-war-costing-average-us-household-2k-economist-estimates)  
  <sub>Seeking Alpha, 20 hours ago</sub>  
  Iran war fallout is costing the average U.S. household nearly $2K, driven by higher energy prices, rising interest rates and military spending.
- [Trump Reportedly Says Oil Prices Won’t Tumble Until After Midterms, While Iran Signals More Intense War — USO, UCO Rise](https://stocktwits.com/news-articles/markets/equity/trump-reportedly-says-oil-prices-wont-tumble-until-after-midterms-while-iran-signals-more-intense-war-uso-uco-rise/cZt7k6WRJC2)  
  <sub>Stocktwits, 20 hours ago</sub>  
  President Donald Trump reportedly said on Wednesday that energy prices elevated by the Iran war are unlikely to come down until after the midterm elections,...
- [Trump’s Russia Deal Is Unlikely To Save You From $6 Diesel](https://seekingalpha.com/article/4953531-trump-russia-deal-unlikely-to-save-you-from-6-diesel)  
  <sub>Seeking Alpha, 23 hours ago</sub>  
  U.S.-Russia diesel deal won't ease diesel prices; refining outages and Hormuz risks keep oil's risk premium high. Click for an updated market outlook.
- [Oil Prices Surge Nearly 10% — US Forces To Resume Maritime Blockade Against Iran On Tuesday](https://stocktwits.com/news-articles/markets/equity/oil-prices-surge-10-percent-us-forces-to-resume-maritime-blockade-against-iran-on-tuesday/cZmz6rZR7Yo)  
  <sub>Stocktwits, 22 hours ago</sub>  
  The U.S. Central Command said U.S. forces will enforce the blockade on vessels entering or leaving Iranian ports starting July 14 at 4 p.m. ET.
- [Oil Prices Diverge As Traders Weigh Russian Diesel Relief Against Saudi Supply Risks: USO, UCO, In Focus](https://finance.yahoo.com/energy/articles/oil-prices-diverge-traders-weigh-091648536.html)  
  <sub>Yahoo Finance, 6 hours ago</sub>  
  USO fell 1.5%, and UCO dropped 1.8%, while retail sentiment was 'neutral' on USO and 'bullish' on UCO. Brent futures declined nearly 1.5%, while WTI futures...

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 151.90 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 148.79 (+2.1%), 50d 140.20 (+8.3%), 200d 117.93 (+28.8%); 50d above 200d
Momentum: RSI(14) 57.4 | MACD 1.766 vs signal 2.110 (histogram -0.343)
Returns: 1d +0.6% | 5d +4.8% | 1m -3.0% | 3m +25.1%
52-week range: 66.17 - 161.86 (now 89.6% of the way up)
Volatility: ATR(14) 4.89 (3.2% of price) | annualised 20d 38.9%
Volume: 0.19x the 20-day average
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

_Not available today._

</details>

<details><summary><b>How much oil and gas is in storage</b> — score n/a</summary>

```text
US inventories, week ending 2026-10-02 (published the following Wednesday)
  Crude oil: 424.1 million barrels, -3.2 on the week (a draw), 40% percentile over 52 weeks
  Petrol: 204.7 million barrels, +0.4 on the week (a build), 4% percentile over 52 weeks -- low for the time of year
  Diesel: 105.1 million barrels, -0.0 on the week (a draw), 23% percentile over 52 weeks
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
Contract: WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE (positions as of 2026-10-06, published the following Friday)
Large speculators: net long 2.8% of open interest (1,889,422 contracts)
Change on the week: -1.4% of open interest
Crowding: 40% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -12.1% (-237.44M) over 7d
Shares outstanding: 11.37M | fund size: 1.73B
Creations and redemptions are settled money, not an opinion -- but they follow demand for the exposure, so read them as conviction rather than as a forecast of price.
```

</details>

### Wheat (WEAT) · Commodity — no answer, no confidence given

**This one did not finish:** https://api.deepinfra.com/v1/openai/chat/completions returned HTTP 429: {"error":{"message":"Model busy, retry later","type":"invalid_request_error","param":null,"code":"engine_overloaded"}} (gave up after 4 attempt(s))

<details><summary><b>News</b> — score n/a</summary>

_No news found for this one today._

</details>

<details><summary><b>Interest rates, the dollar and market nerves</b> — score n/a</summary>

```text
US Treasury yields: 3-month 4.06% (+0.03 on the week) | 5-year 5.01% (-0.01 on the week) | 10-year 5.22% (-0.05 on the week) | 30-year 5.57% (-0.07 on the week)
Yield curve, 10-year minus 3-month: +1.16 points -- upward sloping (normal)
US dollar index: 102.28 (+0.45 on the week)
Volatility (VIX): 15.21 (+0.2 on the week) -- elevated
Latest US data: inflation 3.4% (2026-08-01) | unemployment 4.2% (2026-09-01) | jobless claims 197k (2026-10-03)
Policy and expectations: Fed target 4.00% | market expects 2.3% inflation over 10 years
Rate path: 2-year Treasury 4.75% vs Fed target 3.75-4.00% -- the bond market prices about 4 quarter-point hikes over the next two years (a rough read: the 2-year also carries a term premium)
```

</details>

<details><summary><b>Price and chart</b> — score n/a</summary>

```text
Last close 24.58 (bar of 2026-10-13), from 501 daily bars
Trend: vs 20d SMA 25.27 (-2.7%), 50d 25.55 (-3.8%), 200d 23.35 (+5.3%); 50d above 200d
Momentum: RSI(14) 40.5 | MACD -0.361 vs signal -0.273 (histogram -0.087)
Returns: 1d +0.5% | 5d -3.6% | 1m -6.1% | 3m -1.4%
52-week range: 19.88 - 28.00 (now 57.9% of the way up)
Volatility: ATR(14) 0.49 (2.0% of price) | annualised 20d 19.6%
Volume: 0.17x the 20-day average
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
Cost of holding this fund instead of wheat itself: -14.2% a year -- heavy: rolling contracts costs this fund real money
Measured: 3 months: fund -1.4%, commodity -0.0%, gap -1.3% | 6 months: fund +8.7%, commodity +14.4%, gap -5.7% | 12 months: fund +21.7%, commodity +35.9%, gap -14.2%
A commodity fund holds futures, not wheat, and must sell each expiring contract to buy the next one. Where the next month costs more, that roll loses money every month. This gap is what the structure has actually cost, fees included -- it is history rather than a forecast, and it is not a direction: heavy carry is a reason to want a larger move to justify a long, and a tailwind for a short.
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
Contract: WHEAT-SRW - CHICAGO BOARD OF TRADE (positions as of 2026-10-06, published the following Friday)
Large speculators: net short 5.8% of open interest (497,181 contracts)
Change on the week: -1.2% of open interest
Crowding: 60% percentile over 52 weeks -- within its normal range
Read this as crowding, not as a forecast: an extreme is as often the end of a move as the middle of one.
```

</details>

<details><summary><b>Money going into and out of this fund</b> — score n/a</summary>

```text
Direction: money going out (1 week)
Share count change: 1 week: -20.5% (-73.86M) over 7d
Shares outstanding: 11.64M | fund size: 286.09M
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

